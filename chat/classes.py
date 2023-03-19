import json

class Player:
    def __init__(self, nickname):
        self.nickname = nickname

class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return { 'nickname': obj.nickname }
        return super().default(obj)