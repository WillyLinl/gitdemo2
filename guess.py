import random

a = set()
while True:
    x = random.randint(1, 49)

    a.add(x)
    if len(a) == 6:
        while True:
            x = random.randint(1, 49)
            if x not in a:
                print(
                    f"大樂透號碼:{a}  特別號為:{x}",
                )
                break
        break
