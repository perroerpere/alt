import random

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0

    for card in hand:
        hand_value += get_card_value(card)
    if hand_value >= 22:
        for card in hand:
            if get_card_value(card) == 11:
                hand_value -= 10

    return hand_value


def deal_cards():
    while len(player_cards) < 2:
        card = random.choice(deck)
        deck.remove(card)
        player_cards.append(card)
        card1 = random.choice(deck)
        deck.remove(card1)
        dealer_cards.append(card1)


def print_result(wager, player_cards, player, dealer):
    global chips
    if player == 21 and len(player_cards) == 2:
        print(f"You gt blackjack and win 2 times your bet")
        new_chips = chips + (wager*2)
        print(f"You win {(wager*2)}. new balance:{new_chips}")
        chips = new_chips
    elif dealer >= 22:
        print(f"dealer has over 21 and bust. player wins.")
        new_chips = chips + wager
        print(f"You win {wager}. new balance:{new_chips}")
        chips = new_chips
    elif player >= 22:
        print("player bust. player lose.")
        new_chips = chips - wager
        print(f"You lose {wager}. new balance:{new_chips}")
        chips = new_chips
    elif player > dealer:
        print(f"player has higher value. player wins.")
        new_chips = chips + wager
        print(f"You win {wager}. new balance:{new_chips}")
        chips = new_chips
    elif dealer > player:
        print(f"dealer has higher value. player lose.")
        new_chips = chips - wager
        print(f"You lose {wager}. new balance:{new_chips}")
        chips = new_chips
    elif dealer == player:
        print(f"dealer and player has the same value. player push.")



def hit_card(player_cards):
    card = random.choice(deck)
    deck.remove(card)
    player_cards.append(card)


def check_bal(chips):
    if chips <= 0:
        print(f"\nyou have run out of chips:(")
        exit()


def game_start(chips):
    print("lets start a game")
    print(f"you have {chips} chips.\n")
    wager = 0
    while wager == 0:
        try:
            wager += int(input(f"how many chips do you want to wager?"))
            print()
            if wager > chips:
                print("please enter a number within your chip range.")
                wager -= wager

        except ValueError:
            print("please enter a valid number")
    return wager


with open("chpis.txt") as file:
    content = file.read()

chips = 50
if int(content) > int(chips):
    chips = int(content)

spill = True

while spill == True:
    check_bal(chips)

    wager = game_start(chips)

    player_cards = []
    dealer_cards = []

    deck = get_new_shuffled_deck()
    deal_cards()

    print(f"player cards are {player_cards} with a total value of {calculate_hand_value(player_cards)}")
    print(f"Dealers cards are {dealer_cards[0]} and an unknown card")


    if calculate_hand_value(player_cards) == 21:
        print("du fikk blackjack")

    elif calculate_hand_value(player_cards) != 21:
        hit_or_stand = input("\nHit or Stand? (h/s): ")

        if hit_or_stand == "h":
            hit_cards = True

            while hit_cards == True:
                hit_card(player_cards)
                print(f"\nplayer got the card {player_cards[-1]}")
                print(f"\nPlayer hand is {player_cards} with a value of {calculate_hand_value(player_cards)}")
                player_cards_value = calculate_hand_value(player_cards)

                if player_cards_value >= 22:
                    print(f"\nyou bust")
                    hit_cards = False

                elif player_cards_value == 21:
                    print("\nYou got 21!")
                    hit_cards = False

                else:
                    hit_or_stand = input(f"hit or stand?: ")
                    if hit_or_stand == "s":
                        hit_cards = False
        else:
            print()

        if calculate_hand_value(player_cards) >= 22:
            print(f"\nDealer hand is {dealer_cards} with a value of {calculate_hand_value(dealer_cards)}")

        elif calculate_hand_value(dealer_cards) <= 17:
            print(f"\nDealer hand is {dealer_cards} with a value of {calculate_hand_value(dealer_cards)}")
            print("\ndealer must hit til 17 or above")
            while calculate_hand_value(dealer_cards) <= 16:
                hit_card(dealer_cards)
                print(f"\ndealer got the card {dealer_cards[-1]}")
                print(f"\nDealer hand is {dealer_cards} with a value of {calculate_hand_value(dealer_cards)}")

        elif calculate_hand_value(dealer_cards) >= 17:
            print(f"\nDealers hand in {dealer_cards} with a total value of {calculate_hand_value(dealer_cards)}")

    print(f"\nPlayer hand is {player_cards} with a value of {calculate_hand_value(player_cards)}")

    print_result(wager, player_cards, calculate_hand_value(player_cards), calculate_hand_value(dealer_cards))
    valg = input(f"\n\ndo you want to play again? y/n: ")

    if valg == "n":
        print(f"you ended the game with {chips} amount of chips")
        spill = False

        with open("chpis.txt", "w") as file:
            file.write(str(chips))
            file.close()