import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the total score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    """Compares the scores and determines the winner."""
    if user_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards = []
    dealer_cards = []
    game_over = False

    # Initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        # Check for Blackjack or game over conditions
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want to draw another card
            user_should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer's turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# Run the game
play_game()
