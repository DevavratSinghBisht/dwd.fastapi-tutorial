from fastapi import FastAPI

app = FastAPI()

# Query Params
@app.get("/query")
async def read_item(param: int):
    '''
    When you declare other function parameters that are not part of the path parameters,
    they are automatically interpreted as "query" parameters.
    '''
    return {"param" : param}



# Default Query Params
@app.get("/default")
async def read_item(param1: int = 0, param2: int = 10):
    return {"param1" : param1, "param2": param2}


#Optonal query param
@app.get("/optional")
async def read_item(mandatory: str, optional: str | None = None):
    if optional:
        return {"mandatory": mandatory, "optional": optional}
    return {"mandatory": mandatory}



# Multiple path and query parameters
@app.get("/multiple_params/{path_param1}/{path_param2}")
async def read_item(
    path_param1: int, path_param2: str, query_param: str | None = None, short: bool = False
):
    item = {"path_param1": path_param1, "path_param2": path_param2}
    if query_param:
        item.update({"param1": query_param})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
