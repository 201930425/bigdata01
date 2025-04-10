drinks = ["아이스 아메리카노","카페 라떼", "수박 주스", "딸기주스"]
prices = [1500,2500, 4000, 4200]

total_price = 0
# amounts = list()
# for _ in range(len(drinks)):
#     amounts.append(0)
amounts = [0 for _ in range(len(drinks))] #list compregension(리스트축약)

total_price = 0

def order_process(idx):
    """
    주문 처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 수량 업데이트
    :return:
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

menu_texts = ""
for j in range(len(drinks)):
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원 "
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

print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")
print(f"총 주문 금액 : {total_price}원")