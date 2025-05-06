from random import random, randrange, randint

random_v = random()
print(random_v)  # 0.0 ~ 1.0 미만인 임의의 수
print(random() * 10)  # 0.0 ~ 10.0 미만인 임의의 수
print((random() * 10) + 1)  # 1 ~ 10 이하인 임의의 수

# 로또 (function => random, randrange, randint)
# 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
