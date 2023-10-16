from utils.bet import Bet


def main():
    while True:
        session = Bet
        answer = session.ask()

        if answer == 'end':
            break
        elif answer == 'bet':
            Bet.do_bet(session)
        else:
            Bet.record(session)


if __name__ == "__main__":
    main()
