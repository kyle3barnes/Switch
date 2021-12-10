from src.PlayingCard import PlayingCard


class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Switch:
    playingCard = PlayingCard()

    def get_hands(self, deck):
        hands = self.playingCard.deal_cards(deck, 7, 2)
        return hands[0], hands[1]

    def user_turn(self, deck, user_hand, previous_card, previous_card_number):
        self.show_previous_card(previous_card, user_hand)
        played_card = input("Please enter the card you would like to play: ")
        played_card = self.check_valid(deck, previous_card, played_card, user_hand, previous_card_number)

        index = 0
        for i in range(len(user_hand)):
            if played_card == user_hand[i]:
                index = i

        user_hand.pop(index)

        return played_card, user_hand

    def comp_turn(self, deck, comp_hand, previous_card, previous_card_number):
        played_card = self.get_comp_card(comp_hand, previous_card)
        played_card = self.check_valid(deck, previous_card, played_card, comp_hand, previous_card_number)

        index = 0
        for i in range(len(comp_hand)):
            if played_card == comp_hand[i]:
                index = i

        comp_hand.pop(index)

        return played_card, comp_hand

    def get_comp_card(self, comp_hand, previous_card):
        counter = 0
        for i in range(len(comp_hand)):
            if comp_hand[i][1] == previous_card[1]:
                played_card = comp_hand[i]
                counter = i
            elif comp_hand[i][0] == previous_card[0]:
                played_card = comp_hand[i]
                counter = i
            else:
                played_card = None
        comp_hand.pop(counter)
        return played_card

    def check_valid(self, deck, previous_card, played_card, hand, previous_card_number):

        if played_card is None or played_card == "":
            hand.append(deck.pop())
            return hand  # fix this to not return hand to played card

        if played_card[0] == previous_card[0] or played_card[1] == previous_card[1]:
            previous_card_number += 1
            return played_card

        v = False
        while not v:
            print("You have entered an invalid choice, please try again...")
            self.show_previous_card(previous_card, hand)
            played_card = input("Please enter the card you would like to play: ")

            if played_card[0] == previous_card[0] or played_card[1] == previous_card[1] or played_card[1] == "A":
                v = True

        return played_card

    def show_previous_card(self, previous_card, user_hand):
        print()
        print(Colour.PURPLE + previous_card + Colour.END + "\nThis is the previous card played.")
        print("Here is your hand\n\n", user_hand)

    def two_card_played(self, deck, user_hand, comp_hand, user):
        if not user:
            print("Opponent placed a two! Pick up two cards.\n", user_hand)
            user_hand.append(deck.pop())
            user_hand.append(deck.pop())
        else:
            print("You placed a two! Opponent must pick up two cards.\n", user_hand)
            comp_hand.append(deck.pop())
            comp_hand.append(deck.pop())

        return user_hand, comp_hand

    def eight_card_played(self, hand, user):
        if not user:
            print("Opponent placed an eight! Miss a turn.\n")
        else:
            print("You placed an eight! Opponent will miss a turn.\n")

    def black_jack_card_played(self, deck, user_hand, comp_hand, previous_card_number, user):
        if not user:
            print("Opponent placed a black jack! pick up the amount of cards dealt already.\n", user_hand)
            for i in range(previous_card_number):
                user_hand.append(deck.pop())
        else:
            print("You placed a black jack! Opponent must pick up the amount of cards dealt already.\n", user_hand)
            for i in range(previous_card_number):
                comp_hand.append(deck.pop())

        return user_hand, comp_hand

    def determine_special_cards(self, deck, card, user, user_hand, comp_hand, previous_card_number):
        if card[1] == 2:
            user_hand, comp_hand = self.two_card_played(self, deck, user_hand, comp_hand, user)
        elif card[1] == 8:
            self.eight_card_played(self, user_hand, comp_hand, user)
        elif card[1] == "J" and card[0] in ["H", "D"]:
            user_hand, comp_hand = self.black_jack_card_played(self, deck, user_hand, comp_hand, previous_card_number, user)

        return user_hand, comp_hand

    def game(self, deck, user_hand, comp_hand):
        print(comp_hand)
        previous_card = deck.pop()
        previous_card_number = 0

        while len(user_hand) > 0 and len(comp_hand) > 0:
            # user
            user = True
            user_played_card, user_hand = self.user_turn(deck, user_hand, previous_card, previous_card_number)
            previous_card = user_played_card
            self.determine_special_cards(self, deck, user_played_card, user, user_hand, previous_card_number)
            # comp
            user = False
            comp_played_card, comp_hand = self.comp_turn(deck, comp_hand, previous_card, previous_card_number)
            previous_card = comp_played_card
            self.determine_special_cards(self, deck, comp_played_card, user, comp_hand, previous_card_number)

    def play_game(self):

        deck = self.playingCard.generate_deck()
        deck = self.playingCard.shuffle_cards(deck)
        user_hand, comp_hand = self.get_hands(deck)
        self.game(deck, user_hand, comp_hand)


switch = Switch()
playingCard = PlayingCard()

switch.play_game()
