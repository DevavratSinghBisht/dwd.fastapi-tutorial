'''
The app can be started using the following command:
`uvicorn intro:app`

This happpens because the name of the file is `intro.py`
and the name of the FastAPI object is `app`

The generic command can be thought of as:
`uvicorn <filename>:<FastAPIObjectName>`
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