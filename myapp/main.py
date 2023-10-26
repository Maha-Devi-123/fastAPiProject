from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import api

app = FastAPI()
app.include_router(api.router)

