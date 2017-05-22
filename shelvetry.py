import shelve

def setGame(chat_id, mode, task):
    from quiz import count, generate
    from prime import guessing, isprime, inventing
    from polynom import mult
    from radius import voluming
    with shelve.open("data") as storage:
        if (mode == 0):
             storage[str(chat_id)] = eval(task)
        if(mode == 1):
            storage[str(chat_id)] = isprime(task)
        if(mode == 2):
            storage[str(chat_id)] = mult(task)
        if(mode == 3):
            storage[str(chat_id)] = voluming(task)


def getanswer(chat_id):
    with shelve.open("data") as storage:
        try:
            ans = storage[str(chat_id)]
            return ans
        except KeyError:
            return None

def endgame(chat_id):
    with shelve.open("data") as storage:
        try:
            del storage[str(chat_id)]
        except KeyError:
            return