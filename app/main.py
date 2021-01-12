from fastapi import FastAPI

api = FastAPI()

@api.get("/")
async def live_test():
    return "Hi"