import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ---- Database Setup ----
DATABASE_URL = "sqlite:///./todo.db"  # SQLite DB file path

# Create SQLAlchemy engine and session maker
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for declarative models
Base = declarative_base()


# ---- SQLAlchemy Model ----
class TodoDB(Base):
    """
    SQLAlchemy ORM model for a Todo item.
    Fields:
        - tid: primary key integer ID
        - task: string description of the todo task
        - status: boolean indicating completion (False = pending, True = done)
    """
    __tablename__ = "todos"

    tid = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    status = Column(Boolean, default=False)


# Create database tables
Base.metadata.create_all(bind=engine)


# ---- Pydantic Output Model ----
class Todo(BaseModel):
    """
    Pydantic model for serializing TodoDB instances in API responses.
    """
    tid: int
    task: str
    status: bool

    class Config:
        # Enable ORM mode to allow serialization from SQLAlchemy objects
        from_attributes = True


# ---- FastAPI App ----
app = FastAPI(title="Todo API (Simple Input)")


# ---- Dependency ----
def get_db():
    """
    FastAPI dependency that provides a SQLAlchemy session.
    Ensures session is closed after request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---- Helper Function ----
def get_todo_or_404(tid: int, db: Session) -> TodoDB:
    """
    Retrieve a TodoDB item by id from the database.
    Raises HTTP 404 if not found.

    Args:
        tid (int): Todo ID
        db (Session): SQLAlchemy database session

    Returns:
        TodoDB: ORM Todo object
    """
    todo = db.query(TodoDB).filter(TodoDB.tid == tid).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# ---- Routes ----
@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint welcoming users to the API.
    """
    return {"message": "Welcome to the simple Todo API"}


@app.post("/todos", tags=["Todos"])
def create_todo(task: str, db: Session = Depends(get_db)):
    """
    Create a new todo item with the given task description.

    Args:
        task (str): Task description (from query parameter)
        db (Session): Database session (injected)

    Returns:
        TodoDB: The created todo item
    """
    new_todo = TodoDB(task=task, status=False)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.get("/todos", tags=["Todos"])
def get_all_todos(db: Session = Depends(get_db)):
    """
    Retrieve all todo items from the database.

    Args:
        db (Session): Database session (injected)

    Returns:
        List[TodoDB]: List of all todos
    """
    return db.query(TodoDB).all()


@app.get("/todos/{tid}", tags=["Todos"])
def get_todo(tid: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific todo item by id.

    Args:
        tid (int): Todo ID from path
        db (Session): Database session (injected)

    Returns:
        TodoDB: The requested todo item
    """
    return get_todo_or_404(tid, db)


@app.put("/todos/{tid}", tags=["Todos"])
def update_todo(tid: int, task: str, db: Session = Depends(get_db)):
    """
    Update the task description of an existing todo item.
    Resets the status to False (pending).

    Args:
        tid (int): Todo ID
        task (str): New task description (from query parameter)
        db (Session): Database session

    Returns:
        TodoDB: Updated todo item
    """
    todo = get_todo_or_404(tid, db)
    todo.task = task
    todo.status = False
    db.commit()
    db.refresh(todo)
    return todo


@app.patch("/todos/{tid}", tags=["Todos"])
def patch_status(tid: int, is_done: bool, db: Session = Depends(get_db)):
    """
    Update the status (done/pending) of a todo item.

    Args:
        tid (int): Todo ID
        is_done (bool): New status, True for done, False for pending (from query parameter)
        db (Session): Database session

    Returns:
        TodoDB: Updated todo item
    """
    todo = get_todo_or_404(tid, db)
    todo.status = is_done
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{tid}", tags=["Todos"])
def delete_todo(tid: int, db: Session = Depends(get_db)):
    """
    Delete a todo item by ID.

    Args:
        tid (int): Todo ID
        db (Session): Database session

    Returns:
        dict: Confirmation message
    """
    todo = get_todo_or_404(tid, db)
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}


@app.delete("/reset/todos", tags=["Todos"])
def reset_todos(db: Session = Depends(get_db)):
    """
    Delete all todo items from the database, effectively resetting the todos table.

    Args:
        db (Session): SQLAlchemy database session (injected by FastAPI)

    Returns:
        dict: Confirmation message indicating all todos have been deleted
    """
    # Delete all rows in the todos table
    db.query(TodoDB).delete()
    # Commit the transaction to apply changes
    db.commit()
    # Return a success message
    return {"message": "All todos have been deleted"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8181, reload=True)
