from fastapi import FastAPI, HTTPException
from mangum import Mangum

from dynamodb import get_dynamodb_table

app = FastAPI()


@app.get("/index")
async def index():
    return {"message": "Hello World"}


@app.get("/items")
async def read_items():
    try:
        table = get_dynamodb_table()
        response = table.scan()
        items = response.get("Items", [])
        return {"items": items}

    except Exception as e:
        print(f"❌ Error within Lambda (GET /items): {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/items")
async def create_item(item: dict):
    try:
        table = get_dynamodb_table()
        table.put_item(Item=item)
        return {"message": "Item added", "item": item}

    except Exception as e:
        print(f"❌ Error within Lambda (POST /items): {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create item: {e}")


handler = Mangum(app)
