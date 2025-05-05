import cmath
from math import sqrt, ceil, floor, isclose
from random import random, randrange, randint

abs_x = abs(-5)
assert abs_x == 5

pow_x = pow(5, 2)
assert pow_x == 25

max_x = max(15, 3)
assert max_x == 15

min_x = min(15, 3)
assert min_x == 3

sqrt_x = sqrt(4)
assert sqrt_x == 2
assert isclose(sqrt_x, 2.0, rel_tol=1e-09, abs_tol=1e-09)

# 허수 -> cmath
result = cmath.sqrt(-4)
assert result == 2j

# 라운딩
rounding_x = round(3.141592, 3)
assert isclose(rounding_x, 3.142, rel_tol=1e-09, abs_tol=1e-09)

# 내림
floor_x = floor(3.141592)
assert floor_x == 3

ceil_x = ceil(3.141592)
assert ceil_x == 4

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성

# 로또 (function => random, randrange, randint)
# 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
