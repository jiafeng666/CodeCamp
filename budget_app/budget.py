class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.saving = 0
        self.cost = 0

    def __str__(self):
        len_cate = len(self.name)
        len_lstar = (30-len_cate) // 2
        text = len_lstar * '*' + self.name + (30-len_lstar-len_cate) * '*'
        for led in self.ledger:
            amo = led['amount']
            desc = led['description']

            if isinstance(amo, int):
                amo = str(amo) + '.00'
            len_val = len(str(amo))
            txt = desc + (30-len(desc)-len_val) * ' ' + str(amo)
            if len(txt) > 30:
                left_len = 30 - len_val - 1
                txt = desc[:left_len] + ' ' + str(amo)
            text += '\n' + txt

        text += '\n' + 'Total: ' + str(self.saving)
        return text

    def deposit(self, *param):
        try:
            amo, desc = param
        except:
            amo = param[0]
            desc = ''

        bill = {
            'amount': amo,
            'description': desc
        }
        self.ledger.append(bill)
        self.saving += amo

    def withdraw(self, *param):
        try:
            amo, desc = param
        except:
            amo = param[0]
            desc = ''

        check = self.check_funds(amo)
        if not check:
            return False
        bill = {
            'amount': float('-' + str(amo)) if '.' in str(amo) else int('-' + str(amo)),
            'description': desc
        }
        self.ledger.append(bill)
        self.saving -= amo
        self.cost += amo
        return True

    def get_balance(self):
        return self.saving

    def transfer(self, amo, bud):
        check = self.check_funds(amo)
        if not check:
            return False
        self.withdraw(amo, f'Transfer to {bud.name}')
        bud.deposit(amo, f'Transfer from {self.name}')
        return True

    def check_funds(self, amo):
        return False if amo > self.saving else True


def create_spend_chart(category):
    text = 'Percentage spent by category'

    total_cost = 0
    cate_list = []
    for cate in category:
        cate_dict = {
            'name': cate.name,
            'cost': cate.cost
        }
        cate_list.append(cate_dict)
        total_cost += cate.cost

    for cat in cate_list:
        cat['rate'] = int(cat['cost'] / total_cost * 10) * 10

    txt = ''
    for i in range(100, -10, -10):
        o_line = ''
        for cat in cate_list:
            o_line += ' '
            if cat['rate'] >= i:
                o_line += 'o '
            else:
                o_line += '  '
        txt = (3-len(str(i))) * ' ' + f'{i}|' + o_line + ' '
        text += '\n' + txt

    horizon_line = 4 * ' ' + (len(txt)-4) * '-'
    text += '\n' + horizon_line

    long_name = max(list(map(lambda ca: len(ca['name']), cate_list)))
    lines = ''
    for i in range(long_name):
        lines += 3 * ' '
        line = ''
        for cate in cate_list:
            try:
                line += '  ' + cate['name'][i]
            except:
                line += '   '
        lines += line + '  \n'
    text += '\n' + lines
    return text.rstrip('\n')


if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())

    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)

    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print()
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))
