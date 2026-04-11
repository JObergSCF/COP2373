import random

#Deck class using 0–51 values
class Deck:
    def __init__(self, size):
        #Create list of cards and shuffle right away
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        #If out of cards, reshuffle and start over
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...")

        #Move to next card and return it
        self.current_card += 1
        return self.card_list[self.current_card - 1]


#Convert number to readable card
def card_name(card_num):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
             '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank = ranks[card_num % 13]      # get rank
    suit = suits[card_num // 13]     # get suit
    return rank + " of " + suit


def main():
    deck = Deck(52)
    hand = []

    #Deal starting hand (5 cards)
    for i in range(5):
        hand.append(deck.deal())

    print("Your hand:")
    for i in range(5):
        print(str(i + 1) + ".", card_name(hand[i]))

    #Ask user what to replace
    choice = input("Enter card numbers to replace separated by commas: ")

    if choice.strip() != "":
        replace_list = choice.split(",")

        #Replace selected cards
        for num in replace_list:
            num = num.strip()
            if num.isdigit():
                pos = int(num)
                if 1 <= pos <= 5:
                    hand[pos - 1] = deck.deal()

    print("\nYour new hand:")
    for i in range(5):
        print(str(i + 1) + ".", card_name(hand[i]))


if __name__ == "__main__":
    main()