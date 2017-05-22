import shelve

def setans(chat_id, mode, task):
    from quiz import count, generate
    from prime import isprime, inventing
    from polynom import mult
    from radius import voluming

    with shelve.open("data") as storage:
        list = storage[str(chat_id)]
        if (mode == 0):
            list[0] = eval(task)
            storage[str(chat_id)] = list
        if(mode == 1):
            list[0] = isprime(task)
            storage[str(chat_id)] = list
        if(mode == 2):
            list[0] = mult(task)
            storage[str(chat_id)] = list
        if(mode == 3):
            list[0] = voluming(task)
            storage[str(chat_id)] = list

def setgame(id):
    with shelve.open("data") as storage:
        storage[str(id)] = [0, 0, 0]


def getanswer(chat_id):
    with shelve.open("data") as storage:
        try:
            list = storage[str(chat_id)]
            ans = list[0]
            return ans
        except KeyError:
            return None

def endgame(chat_id):
    with shelve.open("data") as storage:
        try:
            del storage[str(chat_id)]
        except KeyError:
            return

def incscore(id):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[1] += 1
        storage[str(id)] = list

def decscore(id):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[1] -= 2
        storage[str(id)]  = list

def setdif(id, dif):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[-1] = dif
        storage[str(id)] = list

def getdif(id):
    with shelve.open("data") as storage:
        return storage[str(id)][-1]

def getscore(id):
    with shelve.open("data") as storage:
        return storage[str(id)][1]

