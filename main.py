from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Game(BaseModel):
    LA: int
    Boston: int
    BestPlayer: str


scores = {
}


@app.get("/get-score/{game}/{my_team}")
def get_item(game: int, my_team=Path(None, description="Name of your city")):
    return getattr(scores[game], my_team)


@app.get("/get-highest-score")
def get_item(player: str):
    NumberOfTimesBestPlayer = 0
    for game in scores:
        if getattr(scores[game], "BestPlayer") == player:
            NumberOfTimesBestPlayer += 1

    return NumberOfTimesBestPlayer


@app.post("/create-game/{game_id}")
def create_game(game_id: int, game: Game):
    if game_id in scores:
        return {"Game already exists"}

    scores[game_id] = game
    return scores[game_id]
