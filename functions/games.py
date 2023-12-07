import requests


def get_games():
    genres = {}
    url = "https://www.freetogame.com/api/games?"
    games_list = requests.get(url).json()
    for i in range(0, 100):
        if games_list[i]["genre"] not in genres:
            genres[games_list[i]["genre"]] = []
        genres[games_list[i]["genre"]].append(games_list[i])

    for genre in list(genres.keys()):
        if len(genres[genre]) < 4:
            del genres[genre]
    return genres


def get_game(onegame):
    url = "https://www.freetogame.com/api/games?"
    games_list = requests.get(url).json()
    for game in games_list:
        if onegame == game["title"]:
            return game
    return {"error": "this game doesn't exist"}
