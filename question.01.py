import random

input_numbers = []

for i in range(6):
    while True:
        input_num = int(input(f'{i+1}번째 숫자 입력 : '))
        
        range_ok = input_num in range(1, 46)
        duplicated_ok = input_num not in input_numbers
        
        if range_ok and duplicated_ok:
            input_numbers.append(input_num)
            break
        
        elif not range_ok:
            print('1부터 45까지의 숫자를 입력하세요.')
            
        else:
            print('중복된 숫자는 입력할 수 없습니다.')
        
input_numbers.sort()
print(f'내 숫자 : {input_numbers}')

win_nums = []

for i in range(6):
    
    while True:
        random_num = random.randint(1,45)
        
        duplicated_ok = random_num not in win_nums
        
        if duplicated_ok:
            win_nums.append(random_num)
            break
        
win_nums.sort()       

while True:
    bonus_num = random.randint(1, 45)
    duplicated_ok = bonus_num not in win_nums
    
    if duplicated_ok:
        break

 
print(f'당첨번호')

# win_nums = [1,2,3,4,5,6]  # 임시번호로 테스트
print(win_nums)

print('보너스번호 확인')
print(bonus_num)

correct_num_count = 0
for my_num in input_numbers:
    if my_num in win_nums:
        correct_num_count += 1
        
if correct_num_count == 6:
    print('1등')
elif correct_num_count == 5:
    print('3등')
elif correct_num_count == 4:
    print('4등')
elif correct_num_count == 3:
    print('5등')
else :
    print('꽝')
     