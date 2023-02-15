
class MoneyMachine:
    CURRENCY = '#'

    MONEY_VALUE = {
        'Biyar': 5,
        'Faiba': 10,
        'Muri': 20,
        'Wazobia': 50
    }

    def __init__(self, profit, cur_profit=0):
        self.cur_profit = cur_profit
        self.profit = profit

    def process_money(self):
        print('Please insert Monies.')
        for money in self.MONEY_VALUE:
            while True:
                try:
                    self.cur_profit += int(input(f'How many {money}: ')) * self.MONEY_VALUE[money]
                    break
                except ValueError:
                    print(f'Please enter a quantity of {money}')
        return self.cur_profit

    @property
    def report(self):
        return (f'Profit: #{self.profit}')

    def make_transaction(self, format_item, no_pages):
        price = format_item.price * no_pages
        print(f'Your price is {price}')
        
        self.process_money()

        if self.cur_profit >= price:
            self.profit += price
            change = self.cur_profit - price
            self.cur_profit = 0
            print(f'\nHere is your {self.CURRENCY}{change} in change')
            return True
        print("Sorry that's not enough money. Money refunded")
        self.cur_profit = 0
        return False
