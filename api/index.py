from .get_available import get_docks_available

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def main():
    string_builder = []
    open_docks = get_docks_available()
    for i, (station_name, num_docks) in enumerate(open_docks.items()):
        if i < len(open_docks)-1:
            string_builder.append(f"{station_name} has {num_docks} open docks\n")
        else:
            string_builder.append(f"{station_name} has {num_docks} open docks")

    return PlainTextResponse(''.join(string_builder))
