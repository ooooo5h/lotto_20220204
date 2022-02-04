def solution(id_list, report, k):
    
    print(f'아이디 목록 : {id_list}')
    
#     동일한 신고 데이터는 미리 중복을 제거하자
#     list / dict외에도 set(집합) 자료형 => 같은 원소를 여러개를 집어넣어도 하나로만 취급됨(중복제거)

    report = list(set(report))
    
    print(f'신고 데이터 목록 : {report}')
    
#     id_list를 이용해서, 사용자 목록을 담을 공간을 만들자
    user_info_list = []
    
#     사용자 정보를 만드는 for문
    for uid in id_list:
        user_info = {
            'id' : uid,
            'report_users' : [],  # 내가 신고한 사람들
            'reported_users' : [], # 나를 신고한 사람들
            'email_users' : [], # 내가 신고한 사람 중, 정지까지 이뤄진 사람들
        }
        user_info_list.append(user_info)
        
#    신고 데이터를 활용해서 사용자 정보를 가공하는 for문을 만들자
    for report_data in report:
        data = report_data.split()
        report_user_id = data[0]  # 신고한 사람
        troll_user_id = data[1]  # 신고받은 사람
        
#         사용자 목록을 돌아보자. id를 가지고 비교해서 신고한 데이터와 신고당한 데이터를 채우자
        for user in user_info_list:
#         신고한 사람의 아이디와 같다면 내 신고 목록에 트롤 아이디를 추가하자
#          나중에 신고횟수가 누적되면, 정지안내를 받을 근거로 등록
            if user['id'] == report_user_id:
                user['report_users'].append(troll_user_id)
            elif user['id'] == troll_user_id:
                # 내가 신고를 받은 입장이라면, 나의 나를 신고한 사람에, 제보자를 등록하자
                user['reported_users'].append(report_user_id)
        
#         내가 신고를 k회 이상 받았다면, 정지 처분 => 나를 신고한 사람들에게 안내를 주기
    for user in user_info_list:
        if len(user['reported_users']) >= k:
            # 나를 신고한 사람을 찾아서 email_users에 등록해줘야함
            for report_user in user_info_list:
                # k회 이상 신고 받은 내 아이디가 상대방의 신고 목록에 들어있는가?
                if user['id'] in report_user['report_users']:
                    report_user['email_users'].append(user['id'])
            
    answer = []  
        
#    완성된 사용자 정보를 출력하는 for문     
    for user in user_info_list:      
        print(f"사용자 목록 : {user}")
        answer.append(len(user['email_users']))
    
    
    
    return answer