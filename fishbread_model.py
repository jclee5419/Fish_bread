class BreadShop:
    def __init__(self):
        self.stock = {"팥붕어빵": 10, "슈크림붕어빵": 7, "초코붕어빵": 4}
        self.sales = {"팥붕어빵": 0, "슈크림붕어빵": 0, "초코붕어빵": 0}
        self.price = {"팥붕어빵" : 1000, "슈크림붕어빵" : 1200, "초코붕어빵": 1500}

# 붕어빵 주문
    def order_bread(self):
        while True:
            bread_type = input("붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가기를 원하시면 뒤로가기를 입력해주세요")
            if bread_type == "뒤로가기":
                print("뒤로가기")
                break
            if bread_type in self.stock:
                bread_count = int(input("주문할 개수를 입력하세요: "))
                if self.stock[bread_type] > bread_count: # 창고에 있는 빵의 개수가 니가 주문한 개수보다 많은지 확인해 볼게(조건)
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] =+ bread_count
                    print(f'{bread_type} {bread_count}개가 판매 되었습니다.')
                else:
                    print(f'재고가 부족합니다. 현재{self.stock[bread_type]}개만 주문 가능합니다.') # 미안해 지금 주문 가능한 빵의 개수는 00개야
            else:
                print("잘못된 시도입니다 다시 시도하십시오")

    # 붕어빵 admin 기능
    def admin_mode(self):
        while True:
            bread_type = input("붕어빵을 선택해주세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가기를 원하시면 뒤로가기를 입력해주세요")
            if bread_type == "뒤로가기":
                print("뒤로가기")
                break
            if bread_type in self.stock:
                bread_count = int(input("입고할 개수를 입력하세요: "))
                self.stock[bread_type] += bread_count
                print(f'{bread_type} {bread_count}개가 입고 되었습니다, 현재 {self.stock[bread_type]}개 남았습니다.')
            else:
                print("잘못된 시도입니다 다시 시도하십시오")

    # 붕어빵 총 매출
    def calculate_sales(self):
        # total_sales = sum(sales[key] * price[key] for key in sales)
        total = 0
        for key in self.sales:
            total += (self.sales[key] * self.price[key])
        print(f'금일 총 매출은 {total}원 입니다.')