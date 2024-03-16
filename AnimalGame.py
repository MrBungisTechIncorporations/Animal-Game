import random

def get_valid_input(prompt, validator, error_message):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print(error_message)

def is_valid_card_number(value):
    return value.isdigit() and len(value) == 16

def is_valid_expiration_date(value):
    if len(value) != 5:
        return False
    mm, yy = value.split('/')
    return mm.isdigit() and yy.isdigit() and len(mm) == 2 and len(yy) == 2 and value[2] == '/'

def is_valid_cvc(value):
    return value.isdigit() and len(value) == 3

def main():
    intro = '😱 ANIMAL GAME!😱'
    print(intro)

    force_card_payment = random.choice([True, False])

    if force_card_payment:
        print("Sorry, we can't accept cash at this moment.")
        payment_method = "card"
    else:
        payment_method = get_valid_input("Do you want to pay with cash or card? ", lambda x: x.lower() in ["cash", "card"], "Please enter 'cash' or 'card'.")

    if payment_method.lower() == "card":
        card_number = get_valid_input("Enter your credit card number: ", is_valid_card_number, "Please enter a valid 16-digit credit card number.")
        expiration_date = get_valid_input("Enter your card's expiration date (MM/YY): ", is_valid_expiration_date, "Please enter a valid expiration date in MM/YY format.")
        cvc = get_valid_input("Enter your card's CVC: ", is_valid_cvc, "Please enter a valid 3-digit CVC.")

    play = input("Test your luck! If you get the alien, you'll win a lot of money! When you're ready, type: \"Play\" ")
    while play.lower() != "play":
        play = input()

    if random.choice([True, False]):
        print("Sorry! insufficient funds!")
    else:
        emojis = [
            "🐵", "🐒", "🦍", "🦧", "🐶", "🐕", "🦮", "🐕‍🦺", "🐩", "🐺",
            "🦊", "🦝", "🐱", "🐈", "🐈‍⬛", "🦁", "🐯", "🐅", "🐆", "🐴",
            "🐎", "🦄", "🦓", "🦌", "🦬", "🐮", "🐂", "🐃",
            "🐄", "🐷", "🐖", "🐗", "🐽", "🐏", "🐑", "🐐", "🐪", "🐫",
            "🦙", "🦒", "🐘", "🦣", "🦏", "🦛", "🐭", "🐁", "🐀", "🐹",
            "🐰", "🐇", "🐿️", "🦫", "🦔", "🦇", "🐻", "🐻‍️", "🐨",
            "🐼", "🦥", "🦦", "🦨", "🦘", "🦡", "👽"
        ]

        random_emoji = random.choice(emojis)

        if random_emoji == "👽":
            print("💵" * 1000000)
            print("Winner! Winner! You hit the jackpot!!")
        else:
            print(f"AWWWW! Too bad! You got: {random_emoji}")

            global count_no_alien
            count_no_alien += 1

            if count_no_alien % 10 == 0:
                print("Remember! Every Gambler quits before they earn 10000000 dollars! Never give up and keep gambling! 💪")

if __name__ == "__main__":
    count_no_alien = 0
    main()
