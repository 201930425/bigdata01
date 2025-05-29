#open api : wttr.in (weather info)
import kiosk as kk
import requests

if __name__ == "__main__":
    # url = f"https://wttr.in/suwon?format=%C+%t&lang=ko"
    url = f"https://naver.com/kim" #404 page not found
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text.strip())
    else:
        print(f"상태 코드 : {response.status_code}")
    kk.run()
    kk.print_receipt()
    kk.print_ticket_number()