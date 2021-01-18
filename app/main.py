from fastapi import FastAPI

from app.config import STAGE
from app.resource import get_git_branch_name

VERSION = "0.1"

api = FastAPI()


@api.get("/")
async def live_test():
    branch = await get_git_branch_name()
    server_status = {
        "name": "bottern",
        "version": VERSION,
        "branch": branch,
        "stage": STAGE,
    }
    return server_status
