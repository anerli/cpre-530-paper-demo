from fastapi import FastAPI, Cookie, Response, Body
from fastapi.staticfiles import StaticFiles
import secrets

'''
Mock banking site.
'''

app = FastAPI()


sessions = {}

# TODO: Break

api = FastAPI(root_path="/api")

app.mount("/api", api)
app.mount("/", StaticFiles(directory='public', html=True), name="static")


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/login/{username}")
async def login(username: str, response: Response):
    # https://fastapi.tiangolo.com/advanced/response-cookies/
    token = secrets.token_hex(16)
    response.set_cookie(key="sessioncookie", value=token)
    sessions[username] = token
    #return {"detail": "Success"}
    print('Sessions:', sessions)

def check_token(username, token):
    return username in sessions and sessions[username] == token

@api.post("/transfer")
async def transfer_funds():
    # https://fastapi.tiangolo.com/tutorial/cookie-params/
    pass

