# 1) 아아 : 2000 2) 라때 : 2500
while True:
    menu = input("1) 아이스 아메리카노 2) 카페라떼 3) 주문종료 : ")
    if menu == "1":
        print("아이스 아메리카노를 주문하셨습니다. 가격은 2000원 입니다")
    elif menu == "2":
        print("카페 라떼를 주문하셨습니다. 가격은 2500원 입니다")
    elif menu == "3":
        print("주문을 종료합니다")
        break