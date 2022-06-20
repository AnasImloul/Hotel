import threading

lock = threading.Lock()

state = 0

users = []



def new_user(index):
    global state

    for i in range(1_000):

        while state != index:
            continue

        users[index][1] += 1

        lock.acquire()
        print(f"user{index + 1} : {users[index][1]}")
        lock.release()

        state = (state + 1) % len(users)


def add_user():
    users.append([new_user, 0])


for i in range(9):
    add_user()

for i in range(len(users)):
    threading.Thread(target=users[i][0], args=(i,)).start()
