id_number = "911012-1234567"

print("성별 : " + id_number[7])
print("연 : " + id_number[0:2]) # 0 부터 2 직전까지 [0, 2)
print("월 : " + id_number[2:4])
print("요일 : " + id_number[4:6])
print("생년월일 : " + id_number[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + id_number[7:])
print("뒤 7자리 (뒤에부터) : " + id_number[-7:])
# 맨 뒤에서 7번째부터 끝까지