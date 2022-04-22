from random import randint


def coins(reps, streak = 3):
    res = 0

    for i in range(reps):
        timer = 0
        counter = 0
        last_result = -1

        while counter < streak:
            timer += 1
            x = randint(0, 1)
            if x == last_result: counter += 1
            else:
                counter = 1
                last_result = x
        
        res += timer

    return res / reps


print(coins(50))
print(coins(50, 1))
print(coins(100, 10))