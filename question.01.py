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


    