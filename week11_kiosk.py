import kiosk as kk

if __name__ == "__main__":
    kk.run()
    kk.print_receipt()
    print(f"번호표 : {kk.get_ticket_number()}")