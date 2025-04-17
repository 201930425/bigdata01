drinks = ["아이스 아메리카노","카페 라떼", "수박 주스", "딸기주스"]
prices = [1500,2500, 4000, 4200]
total_price = 0
amounts = [0] * len(drinks)#amounts = [0 for _ in range(len(drinks))]

def order_process(idx):
    """
    주문 처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 수량 업데이트
    :return:
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

def display_menu(ids):
    """
    음료 선택 메뉴 디스플레이 기능
    :param ids: 고객이 선택한 메뉴 -1(인텍스)
    :return: 없음
    """
menu_texts = "".join([f"{j+1}) {drinks[j]} {prices[j]}원 "for j in range(len(drinks))])
menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료 :  "

while True:
    menu =int(input(menu_texts))
    if len(drinks)>= menu >= 1:
        order_process(menu-1)
    elif menu == len(drinks)+1:
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")

print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")
print(f"총 주문 금액 : {total_price}원")