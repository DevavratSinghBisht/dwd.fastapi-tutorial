from fastapi import FastAPI

from enum import Enum

app = FastAPI()

# Path Param
@app.get("/path-param/{pathParam}")
async def getPathParam(pathParam):
    return {'pathParam': pathParam, "type": str(type(pathParam))}

#Path param with data type
@app.get("/path-param-int/{pathParam}")
async def getPathParamInt(pathParam: int):
    return {'pathParam': pathParam, "type": str(type(pathParam))}

@app.get("/path-param-float/{pathParam}")
async def getPathParamFloat(pathParam: float):
    return {'pathParam': pathParam, "type": str(type(pathParam))}



# Precedence matters
@app.get("/param/param")
async def getParam():
    return{"param": "This is not a dynamic param"}

@app.get("/param/{param}")
async def getParamDynamic(param):
    return {"param": param}

#Using Enums
class Vehicle(str, Enum):
    car = "car"
    truck = "truck"
    bike = "bike"

@app.get("/vehicle/{vehicle}")
async def get_vehicle(vehicle : Vehicle):
    return {'vehicle': vehicle}

@app.get("/vehicle-str/{vehicle}")
async def get_vehicle(vehicle : str):
    return {'vehicle': vehicle}

#Path param containing paths
@app.get("/files/check/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}