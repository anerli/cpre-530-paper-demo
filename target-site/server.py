from fastapi import FastAPI, Cookie, Response, Body, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import secrets

from starlette.requests import Request

'''
Mock banking site.

This logic is not at all secure, but the point is to
have as simple server which demonstrates the FastAPI
exploit.
'''

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
        # "http://localhost:3000",
        # "localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    #response.set_cookie(key="username", value=username)
    #sessions[username] = token
    sessions[token] = username
    # Example funds
    funds[username] = 1000
    #return {"detail": "Success"}
    print('Sessions:', sessions)

    return {"funds": funds[username]}

# def check_token(username, token):
#     return username in sessions and sessions[username] == token



@api.post("/transfer")
async def transfer_funds(to_user: str = Body(...), amount: int = Body(...), sessioncookie: str = Cookie(None)):
    '''
    All parameters passed in JSON body to demonstrate the exploit.
    '''
    #from_user 
    # https://fastapi.tiangolo.com/tutorial/cookie-params/
    # if not check_token(from_user, sessioncookie):
    #     raise HTTPException("Invalid Session Cookie!")
    assert sessioncookie in sessions
    from_user = sessions[sessioncookie]

    # Ensure a positive amount is being transferred
    assert amount > 0
    # Check that sending user has enough
    assert funds[from_user] >= amount
    # Check that users exist
    assert from_user in funds and to_user in funds

    funds[from_user] -= amount
    funds[to_user] += amount

    print('Updated funds:', funds)

@api.post("/test")
async def test(request: Request):
    print(request)
    

