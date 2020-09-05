from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("app started")


@app.on_event("shutdown")
def shutdown_event():
    print("app stoped")


@app.get("/")
def read_root():
    return {"Hello": "World"}