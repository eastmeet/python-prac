from decimal import Decimal

print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

# 몫(quotient)
print("quotient 10 // 5 = " + str(10 // 5))
assert 10 // 5 == 2, "몫 계산이 잘못되었습니다"

# 나머지(reminder)
print("reminder 10 % 5 = " + str(10 % 5))
assert 10 % 5 == 0, "나머지 계산이 잘못되었습니다"

# decimal prac
price = Decimal('100000.90899897898789789724721934789729847890')
tax_rate = Decimal('0.154')
sum_result = price * tax_rate
print(sum_result)

# exception handling
try:
  print(price / 0)
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")



