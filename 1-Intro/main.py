'''
Here we will create an hellow world API using few lines of code.

The generic command to start the app can be thought of as:
`uvicorn <filename>:<FastAPIObjectName>`.

In our case filename is `main.py` and the name of the FastAPI object is `app`.
So the application can be started using the following command: `uvicorn main:app`

`--reload` flag can be used so that any changes that we make during development
can be reflected without a need to manually restart the application. 
The final command becomes `uvicorn main:app --reload`.

The app will get hosted at `http://127.0.0.1:8000/` by default 
and the Swagger UI can be seen at `http://127.0.0.1:8000/docs`.
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello-world")
async def root():
    '''
    Provides a dummy response to a get request.

    params:
        None

    returns:
        response (dict <str:str>) : dummy response
    '''
    response = {"message": "Hello World"}
    return response