class Bet:

    answer_dict = {
        0: 'Победа во встрече',
        1: 'Победа на карте',
        2: 'Cчет',
        3: 'ФБ',
        4: 'Первые 10 убийств',
        5: 'Первый аегис',
        6: 'Количество карт',
        7: '>38 мин',
        8: '<36 мин',
        9: 'Rampage!',
    }

    def __init__(self):
        self.action = ''
        self.coefficient = 0
        self.amount = 0
        self.team = '_'


    @staticmethod
    def ask():
        return input('Хотите закончить: "end"\n'
                     'Хотите поставить: "bet"\n'
                     'Хотите результировать: ""\n')

    def do_bet(self):

        self.action = int(input('На какое событие ставка:\n'
                                '0. Победа во встрече\n'
                                '1. Победа на карте\n'
                                '2. Точный счет\n'
                                '3. Первая кровь\n'
                                '4. Первые 10 убийств\n'
                                '5. Первый аегис\n'
                                '6. Количество карт\n'
                                '7. Карта > 38 мин\n'
                                '8. Карта < 36 мин\n'
                                '9. Rampage!\n'))

        if self.action < 6:
            self.team = input('название команды\n')
        else:
            self.team = '_'

        self.coefficient = float(input('Какой коэффициент\n'))
        self.amount = int(input('Сколько поставите\n'))

        file = open('history/log.txt', 'a', encoding='utf8')
        file.write(f"{self.answer_dict[self.action]}|{self.team}|{self.coefficient}|{self.amount}|-\n")
        file.close()

    def record(self):
        file = open('history/log.txt', 'r+', encoding='utf8')
        data = file.read()
        for line in data.split('\n'):
            # print(line)
            activity, team, kf, amount, is_finish = line.split('|')
            if is_finish == '+':
                pass
            else:
                print(activity, team)
        file.close()
