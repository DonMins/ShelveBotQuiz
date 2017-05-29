import shelve

def setans(chat_id, mode, task):
    from quiz import count, generate
    from prime import isprime, inventing
    from polynom import mult
    from radius import voluming

    with shelve.open("data") as storage:
        list = storage[str(chat_id)]
        list[0] = task
        if (mode == 0):

            storage[str(chat_id)] = list
        if(mode == 1):

            storage[str(chat_id)] = list
        if(mode == 2):

            storage[str(chat_id)] = list
        if(mode == 3):
            storage[str(chat_id)] = list
        storage.close()

def setgame(id):
    with shelve.open("data") as storage:
        storage[str(id)] = [0, 0, 0]
        storage.close()


def getanswer(chat_id):
    with shelve.open("data") as storage:
        try:
            list = storage[str(chat_id)]
            ans = list[0]
            storage.close()
            return ans
        except KeyError:
            storage.close()
            return None

def endgame(chat_id):
    with shelve.open("data") as storage:
        try:
            del storage[str(chat_id)]
            storage.close()
        except KeyError:
            storage.close()
            return

def incscore(id):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[1] += 1
        storage[str(id)] = list
        storage.close()

def decscore(id):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[1] -= 2
        storage[str(id)]  = list
        storage.close()

def setdif(id, dif):
    with shelve.open("data") as storage:
        list = storage[str(id)]
        list[-1] = dif
        storage[str(id)] = list
        storage.close()

def getdif(id):
    with shelve.open("data") as storage:
        return storage[str(id)][-1]

def getscore(id):
    with shelve.open("data") as storage:
        return storage[str(id)][1]

