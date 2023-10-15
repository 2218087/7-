class 붕어빵:      # "붕어빵 클래스"로 객체 생성하기
    def __init__(self, contents, price):
      self.contents = contents
      self.price = price
      self.total_sales = 0    #초기 총판매금을 0으로 설정

    def sell(self):      #sell 함수 정의
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total_sales += self.price     #판매 금액을 총 판매금에 더함

    def eat(self):        #eat 함수 정의
        print(f"{self.contents} 붕어빵을 먹습니다.")

    def display_total_sales(self):
        print(f"총 판매금:{self.total_sales}원")

슈크림붕어빵 = 붕어빵("슈크림", 1500)    # 매개 변수에 따라 붕어빵의 속성정보가 다른 객체 생성
팥붕어빵 = 붕어빵("팥", 1000)
김치붕어빵 = 붕어빵("김치", 1500)
피자붕어빵 = 붕어빵("피자", 1800)

슈크림붕어빵.sell()
슈크림붕어빵.eat()
슈크림붕어빵.sell()
슈크림붕어빵.eat()

팥붕어빵.sell()
팥붕어빵.eat()

김치붕어빵.sell()
김치붕어빵.eat()
김치붕어빵.sell()
김치붕어빵.eat()
김치붕어빵.sell()
김치붕어빵.eat()

피자붕어빵.sell()
피자붕어빵.eat()
피자붕어빵.sell()
피자붕어빵.eat()
피자붕어빵.sell()
피자붕어빵.eat()
피자붕어빵.sell()
피자붕어빵.eat()

슈크림붕어빵.display_total_sales()
팥붕어빵.display_total_sales()
김치붕어빵.display_total_sales()
피자붕어빵.display_total_sales()
