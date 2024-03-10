from fastapi import FastAPI

app = FastAPI()

fake_db = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]

# Query Params
@app.get("/items/")
async def read_item(skip: int, limit: int):
    '''
    When you declare other function parameters that are not part of the path parameters,
    they are automatically interpreted as "query" parameters.
    '''
    return fake_db[skip : skip + limit]



# Default Query Params
@app.get("/items-default/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_db[skip : skip + limit]


#Optonal query param
@app.get("/items/{item_id}")
async def read_item(mandatory: str, optional: str | None = None):
    if optional:
        return {"mandatory": mandatory, "optional": optional}
    return {"mandatory": mandatory}



# Multiple path and query parameters
@app.get("/users/{key}/items/{value}")
async def read_item(
    key: int, value: str, query: str | None = None, short: bool = False
):
    item = {"value": value, "key": key}
    if query:
        item.update({"query": query})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item