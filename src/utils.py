def getop(name: str, ops: list):
    for op in ops:
        if op["name"] == name:
            return op["value"]
    return None
