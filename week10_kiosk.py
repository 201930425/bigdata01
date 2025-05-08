import kiosk as kk

if __name__ == "__main__":
    while True:
        try:
            menu = int(input(kk.display_menu()))
            if len(kk.drinks) >= menu >= 1:
                kk.order_process(menu - 1)
            elif menu == len(kk.drinks)+1:
                print("주문을 종료합니다")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요")

    kk.print_receipt()