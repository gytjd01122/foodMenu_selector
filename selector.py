import random

### 코드 설명
# 코드 제목 : 음식메뉴 선택기
# 만든 목적 : 코드라이언 코딩학습, 음식메뉴 선정시 빠르고 편리하게 골라주기 위해서 만듬.
# 만든 이 : saebyeol
# 만든 날짜 : 2020-11-22
# 최종수정일 : 2020-11-22

"""
    ### 코드 내용에 대한 설명
    # 만든 기능 : 음식 메뉴 추가,삭제, 고르기
    # 디버그 모드 :  0 = OFF, 1 = ON
"""

DEBUG_MODE = 0

lunch = set(["된장찌개", "김치찌개", "불고기"])

while True:
    
    print("기본 음식메뉴는" + str(lunch) + "입니다.")

    print("메뉴를 선택하세요. : " )
    selected_menuNumber =  input("추가 1, 삭제 2, 고르기 3 : ")
    
    if DEBUG_MODE == 1: # 디버깅용
        print(type(selected_menuNumber))

    if selected_menuNumber == "1": #음식메뉴 추가하기 
        # 음식메뉴 추가시 할 명령
        to_addMenu =  input("추가할 음식 입력 : ")
        lunch.add(to_addMenu)

        print(lunch)

    elif selected_menuNumber == "2":  #음식메뉴 삭제하기 
        # 음식메뉴 삭제시 할 명령
        print("삭제할 음식을 입력하세요")
        print("현재 등록된 음식은" + str(lunch) + " 입니다.")

        to_deleteMenu = input("삭제할 음식 : ")
        lunch.remove(to_deleteMenu)
        
        print(lunch)

    elif selected_menuNumber == "3": #음식메뉴 고르기 
        # 음식메뉴 랜덤선택시 할 명령
        selected_menu =  random.sample(lunch,1)
        print("선택된 음식메뉴는 " + str(selected_menu) + " 입니다.")