from fastapi import FastAPI, Request
from rec_handler import getMusic

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("app started")


@app.on_event("shutdown")
async def shutdown_event():
    print("app stoped")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/song/{song_name}/artist/{artist}/number/{number_of_song}")
async def read_user_item(
    song_name: str, artist: str, number_of_song: int, request: Request
):
    client_host = request.client.host

    musics, called = getMusic(song=song_name, artist=artist, k=number_of_song)

    if musics:
        result = {
            "host": client_host,
            "status": 200,
            "based_On": "music: {0}, artist: {1}".format(called[0], called[1]),
            "reccommended": musics,
        }
    else:
        result = {
            "host": client_host,
            "Status": 404,
            "based_On": "music: {0}, artist: {1}".format(called[0], called[1]),
            "reccommended": "Not Found!",
        }

    return result
