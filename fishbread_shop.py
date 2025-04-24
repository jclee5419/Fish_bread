# 붕어빵 메인화면
from fishbread_model import BreadShop

shop = BreadShop()

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):") # 주문
    if mode == "종료":
        shop.calculate_sales()
        print("시스템이 종료되었습니다.")
        break
    elif mode == "주문":
        shop.order_bread()
        pass
    elif mode == "관리자":
        shop.admin_mode()
        pass
# 로직이 숨겨지고 / 로직들만 별도로 관리해서 유지보수 하기 쉬움