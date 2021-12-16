from fastapi import FastAPI, Cookie, Response, Body
from fastapi.staticfiles import StaticFiles
import secrets

'''
Mock banking site.
'''

app = FastAPI()


sessions = {}
funds = {}

# TODO: Break

api = FastAPI(root_path="/api")

app.mount("/api", api)
app.mount("/", StaticFiles(directory='public', html=True), name="static")


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/login/{username}")
async def login(username: str, response: Response):
    '''
    Mock login endpoint.
    To eliminate the need for a password, since that is not the point of this
    demonstration, just a username is passed to the endpoint which essentially
    creates a temporary mock user.
    A session cookie is returned from this endpoint.
    '''
    # https://fastapi.tiangolo.com/advanced/response-cookies/
    token = secrets.token_hex(16)
    response.set_cookie(key="sessioncookie", value=token)
    sessions[username] = token
    # Example funds
    funds[username] = 1000
    #return {"detail": "Success"}
    print('Sessions:', sessions)

    return {"funds": funds[username]}

def check_token(username, token):
    return username in sessions and sessions[username] == token

@api.post("/transfer")
async def transfer_funds(sessioncookie: str = Cookie(None)):
    # https://fastapi.tiangolo.com/tutorial/cookie-params/
    pass

