import random

print(1)
print("haha")
print("修改")
print("大樂透")
print("你好")
# 號碼不能重複
# 要排序

a = set()
while True:
    x = random.randint(1, 49)

    a.add(x)
    if len(a) == 6:
        while True:
            x = random.randint(1, 49)
            if x not in a:
                print(
                    f"大樂透號碼:{sorted(list(a))}  特別號為:{x}",
                )
                break
        break
