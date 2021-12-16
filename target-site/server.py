from fastapi import FastAPI, Cookie, Response, Body
import secrets

'''
Mock banking site.
'''

app = FastAPI()

sessions = {}

# TODO: Break


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/login/{username}")
async def login(username: str, response: Response):
    # https://fastapi.tiangolo.com/advanced/response-cookies/
    token = secrets.token_bytes(16)
    response.set_cookie(key="sessioncookie", value=token)
    sessions[username] = token
    #return {"detail": "Success"}

def check_token(username, token):
    return username in sessions and sessions[username] == token

@app.post("/transfer")
async def transfer_funds():
    # https://fastapi.tiangolo.com/tutorial/cookie-params/
    pass