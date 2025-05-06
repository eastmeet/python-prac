'''
Quiz) 월 4회 스터디를 한다. 3번은 온라인 1번은 오프라인
condition 1. 랜덤으로 날짜를 뽑아야한다.
condition 2. 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
condition 1. 매월 1~3일은 스터디 준비를 하므로 제외

출력문 ex) 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
'''
from random import sample

VALID_DAYS = range(4, 28)
study_days = sample(VALID_DAYS, 4)
offline_days = study_days[3]
print(f"오프라인 스터디 모임 날짜는 매월 {offline_days}일로 선정되었습니다.")
