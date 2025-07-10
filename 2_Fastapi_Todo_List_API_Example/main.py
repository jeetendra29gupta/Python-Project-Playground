import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ==========================================
# 🔧 Step 1: Database Setup
# ==========================================

# SQLite DB connection string
DATABASE_URL = "sqlite:///./todo.db"

# SQLAlchemy engine and session maker
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()


# ==========================================
# 🗃️ Step 2: SQLAlchemy Model
# ==========================================

class TodoDB(Base):
    """
    SQLAlchemy ORM model for a Todo item.
    Represents a row in the 'todos' table.
    """
    __tablename__ = "todos"

    tid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task = Column(String, nullable=False)
    status = Column(Boolean, default=False)


# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)


# ==========================================
# 🧾 Step 3: Pydantic Response Model
# ==========================================

class Todo(BaseModel):
    """
    Pydantic model used to serialize responses for TodoDB objects.
    """
    tid: int
    task: str
    status: bool

    class Config:
        from_attributes = True  # Enable ORM compatibility


class TodoCreate(BaseModel):
    """
    Pydantic model for creating a new Todo item.
    Used to validate input data for creating todos.
    """
    task: str


class TodoUpdate(BaseModel):
    """
    Pydantic model for updating an existing Todo item.
    Used to validate input data for updating todos.
    """
    task: str


class TodoModify(BaseModel):
    """
    Pydantic model for modifying an existing Todo item.
    Used to validate input data for modifying todos.
    """
    is_done: bool


# ==========================================
# 🚀 Step 4: FastAPI App Initialization
# ==========================================

app = FastAPI(title="Todo API (Simple Input)")


# ==========================================
# 🔗 Step 5: Dependency for DB Session
# ==========================================

def get_db():
    """
    FastAPI dependency that provides a database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# ⚙️ Step 6: Helper Function
# ==========================================

def get_todo_or_404(tid: int, db: Session) -> TodoDB:
    """
    Helper to fetch a Todo by ID or raise 404 if not found.

    Args:
        tid (int): Todo ID
        db (Session): SQLAlchemy session

    Returns:
        TodoDB: The found Todo object
    """
    todo = db.query(TodoDB).filter(TodoDB.tid == tid).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# ==========================================
# 📡 Step 7: API Routes
# ==========================================

@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint to verify API is running.
    """
    return {"message": "Welcome to the simple Todo API"}


@app.post("/todos", tags=["Todos"])
def create_todo(task: TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new todo item.

    Args:
        task (str): Task description
        db (Session): Database session

    Returns:
        TodoDB: Created todo object
    """
    new_todo = TodoDB(task=task.task)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.get("/todos", tags=["Todos"])
def get_all_todos(db: Session = Depends(get_db)):
    """
    Retrieve all todo items.

    Args:
        db (Session): Database session

    Returns:
        List[TodoDB]: All todos
    """
    return db.query(TodoDB).all()


@app.get("/todos/{tid}", tags=["Todos"])
def get_todo(tid: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific todo by ID.

    Args:
        tid (int): Todo ID
        db (Session): Database session

    Returns:
        TodoDB: Retrieved todo object
    """
    return get_todo_or_404(tid, db)


@app.put("/todos/{tid}", tags=["Todos"])
def update_todo(tid: int, task: TodoUpdate, db: Session = Depends(get_db)):
    """
    Update task text of an existing todo. Resets status to False.

    Args:
        tid (int): Todo ID
        task (str): New task text
        db (Session): Database session

    Returns:
        TodoDB: Updated todo object
    """
    todo = get_todo_or_404(tid, db)
    print(task.task)
    todo.task = task.task
    todo.status = False
    db.commit()
    db.refresh(todo)
    return todo


@app.patch("/todos/{tid}", tags=["Todos"])
def patch_status(tid: int, is_done: TodoModify, db: Session = Depends(get_db)):
    """
    Update only the status of a todo (done or pending).

    Args:
        tid (int): Todo ID
        is_done (bool): True if done, False if pending
        db (Session): Database session

    Returns:
        TodoDB: Updated todo object
    """
    todo = get_todo_or_404(tid, db)
    todo.status = is_done.is_done
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{tid}", tags=["Todos"])
def delete_todo(tid: int, db: Session = Depends(get_db)):
    """
    Delete a specific todo by ID.

    Args:
        tid (int): Todo ID
        db (Session): Database session

    Returns:
        dict: Success message
    """
    todo = get_todo_or_404(tid, db)
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}


@app.delete("/reset/todos", tags=["Todos"])
def reset_todos(db: Session = Depends(get_db)):
    """
    Delete all todos in the database.

    Args:
        db (Session): Database session

    Returns:
        dict: Success message
    """
    db.query(TodoDB).delete()
    db.commit()
    return {"message": "All todos have been deleted"}


# ==========================================
# 🚦 Step 8: Run with Uvicorn (Dev Mode)
# ==========================================

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8181, reload=True)
