# 주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들거에요
# input()을 통해서 3가지 중 한가지를 입력 받아서 작동시킬 수 있어요

i = 0

stock = { # key값을 이용해서 value  딕셔너리를 써야하는 상황은 어떤 스토리 기반으로 데이터가 구성되었을 떄
    "팥붕어빵": 10,
    "슈크림붕어빵": 7,
    "초코붕어빵": 4,
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "초코붕어빵": 0,
}

price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵": 1500,
}

# 붕어빵 주문
def order_bread():
    while True:
        bread_type = input("붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가기를 원하시면 뒤로가기를 입력해주세요")
        if bread_type == "뒤로가기":
            print("뒤로가기")
            break
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: "))
            if stock[bread_type] > bread_count: # 창고에 있는 빵의 개수가 니가 주문한 개수보다 많은지 확인해 볼게(조건)
                stock[bread_type] -= bread_count
                sales[bread_type] =+ bread_count
                print(f'{bread_type} {bread_count}개가 판매 되었습니다.')
            else:
                print(f'재고가 부족합니다. 현재{stock[bread_type]}개만 주문 가능합니다.') # 미안해 지금 주문 가능한 빵의 개수는 00개야
        else:
            print("잘못된 시도입니다 다시 시도하십시오")

# 붕어빵 admin 기능
def admin_mode():
    while True:
        bread_type = input("붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가기를 원하시면 뒤로가기를 입력해주세요")
        if bread_type == "뒤로가기":
            print("뒤로가기")
            break
        if bread_type in stock:
            bread_count = int(input("입고할 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f'{bread_type} {bread_count}개가 입고 되었습니다, 현재 {stock[bread_type]}개 남았습니다.')
        else:
            print("잘못된 시도입니다 다시 시도하십시오")

# 붕어빵 총 매출
def calculate_sales():
    # total_sales = sum(sales[key] * price[key] for key in sales)
    total = 0
    for key in sales:
        total += (sales[key] * price[key])
    print(f'금일 총 매출은 {total}원 입니다.')

# 붕어빵 메인화면
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):") # 주문
    if mode == "종료":
        calculate_sales()
        print("시스템이 종료되었습니다.")
        break
    elif mode == "주문":
        order_bread()
        pass
    elif mode == "관리자":
        admin_mode()
        pass