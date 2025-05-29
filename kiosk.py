# import datetime
from datetime import datetime
import sqlite3
import requests

drinks = ["아이스 아메리카노","카페 라떼", "수박 주스", "딸기주스"]
prices = [1500,2500, 4000, 4200]
total_price = 0
amounts = [0] * len(drinks)

#할인 적용 정책
DISCOUNT_THRESHOLD = 10000 #할인이 적용되는 임계값 (임계값 이상이면 할인 적용)
DISCOUNT_RATE =0.05  # 할인율

def run() -> None:
    """
    키오스크 실행(구동) 함수
    :return: None
    """
    while True:
        try:
            menu = int(input(display_menu()))
            if len(drinks) >= menu >= 1:
                order_process(menu - 1)
            elif menu == len(drinks)+1:
                print("주문을 종료합니다")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요")

def apply_discount(price: int) -> float:
    """
    총 금액이 특정 금액(임계값)을 넘어서면 할인율 적용 함수
    :param price: 할인 전 총 금액
    :return: 할인이 적용된 금액 또는 할인이 적용되지 않는 금액
    """
    if price >=DISCOUNT_THRESHOLD:
        return price * (1 - DISCOUNT_RATE)
    return price

def print_ticket_number() -> int:
    """
    주문 번호표 출력함수
    :return:
    """
    conn = sqlite3.connect('cafe.db')  # db instance open
    cur = conn.cursor()
    cur.execute('''
        create table if not exists ticket (
        id integer primary key autoincrement,
        number integer not null,
        created_at text not null default(datetime('now', 'localtime'))
        )
    ''')
    conn.commit()

    cur.execute('select id from ticket order by number desc limit 1')
    result = cur.fetchone()

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if result is None:
        number = 1
        cur.execute('insert into ticket (number, created_at) values (?, ?)', (number,now))
    else:
        number = result[0] +1
        cur.execute('insert into ticket (number, created_at) values (?, ?)', (number,now))
    conn.commit()

    print(f"번호표 : {number} ({now})")
    conn.close()  # free db instance

def order_process(idx :int) -> None:
    """
    주문 처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 수량 업데이트
    :return:
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다\n")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

def display_menu() -> str:
    """
    날씨 부가 정보 및 음료 선택 메뉴 디스플레이 기능
    :return:
    """
    try:
        url = f"https://wttr.in/suwon?format=2"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text.strip())
        else:
            print(f"상태 코드 : {response.status_code}")
    except Exception as err:
        print(f"오류 : {err}")
    print("=" * 30)
    menu_texts = "".join([f"{j + 1}) {drinks[j]} {prices[j]}원\n" for j in range(len(drinks))])
    menu_texts = menu_texts + f"{len(drinks) + 1}) 주문종료 : "
    return menu_texts

def print_receipt() -> None:
    """
    영수증 출력기능
    :return: 없음
    """
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")

    discounted_price = apply_discount(total_price)
    discount = total_price - discounted_price

    print(f"할인 전 총 주문 금액 : {total_price}원")
    if discount >0:
        print(f"할인 금액 : {discount}원 ({DISCOUNT_RATE*100}% 할인)")
        print(f"할인 적용 후 지불하실 총 금액은 {discounted_price}원 입니다.")
    else:
        print(f"할인이 적용되지 않았습니다.\n지불하실 총 금액인 {total_price}원 입니다.")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def test() -> None:
    """
    앞으로 키오스크에 추가할 기능
    :return:
    """
    pass