"""find sum of START and END with dedicated printing and time checking

결과: 이상하네 if를 안 쓴 for문이 더 길게 나올때가 더 많다
"""
import time

START = 1
END = 10_000

sum = 0

print("=== using pure loop ==")
start_time = time.time()

for i in range(START, END):
    print(f"{i} + ", end="'")
    sum += i

print(f"{END} = ", end="")
sum += END

print(sum)
end_time = time.time()
time2 = end_time - start_time

sum = 0

print("=== using unnecessary if ===")
start_time = time.time()
for i in range(START, END + 1):
    if i < END:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")
    sum += i

print(sum)
end_time = time.time()
time1 = end_time - start_time


###

print(f"time1 : {time1}")
print(f"time2 : {time2}")
