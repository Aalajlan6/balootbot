#where game is ran, calls bot when its its turn.

from rules import *
import random
from bot import *

def main():
    game_state = gameStates()
    # Initialize players, one bot one teammate two opponents, bot position is random then the rest are filled in clockwise order, so if bot is 0 then 2 is teammate, 1 and 3 are opponents, if bot is 1 then 2 is teammate, 3 and 0 are opponents, etc.
    bot_position = random.randint(0, 3)
    teammate_position = (bot_position + 2) % 4
    opponent1_position = (bot_position + 1) % 4
    opponent2_position = (bot_position + 3) % 4
    for i in range(4):
        if i == bot_position:
            game_state.players[i].name = "Bot"
            game_state.players[i].team = True
        elif i == teammate_position:
            game_state.players[i].name = "Teammate"
            game_state.players[i].team = True
        elif i == opponent1_position:
            game_state.players[i].name = "Opponent 1"
            game_state.players[i].team = False
        elif i == opponent2_position:
            game_state.players[i].name = "Opponent 2"
            game_state.players[i].team = False
    #print("Players:")
    # Initialize deck
    for suit in SUITS:
        for rank in RANKS:
            game_state.deck.append(card(suit, rank))
    # Shuffle deck
    random.shuffle(game_state.deck)
    # Randomly pick dealer
    game_state.dealer_index = random.randint(0, 3)
    #print(f"Dealer is {game_state.players[game_state.dealer_index].name}")
    #Declare order of play for this current round (start at dealer, then go clockwise)
    order_of_play = []
    for i in range(4):
        order_of_play.append(game_state.players[(game_state.dealer_index + i) % 4])
    # print("Order of play:")
    # for p in order_of_play:
    #     print(p.name)


    # Deal first cards, 5 each, then show buy card.
    for i in range(5):
        for p in order_of_play:
            p.hand.append(game_state.deck.pop())
    game_state.buy_card = game_state.deck.pop()
    print(f"Buy card is {game_state.buy_card.rank} of {game_state.buy_card.suit}")
    # Check each player's check TESTING
    # for p in order_of_play:
    #     print(f"{p.name} has the following hand:")
    #     for c in p.hand:
    #         print(f"{c.rank} of {c.suit}")
    #     # Here we would call the bot's check function if p is the bot, and the other players would have their own logic for checking. For now we will just print out their hands and the buy card.
    




    # Buy phase
    #Start at player to the right of dealer, go clockwise
    #options for buy is buy sun, buy hokm, pass
    #Special options for dealer and left of dealer: 
    #ashkal, rulset is sun but buyer's teammate get card
    #for now, manual inputs for all players (including bot, but we're calling bot check to simulate a bot)
    
if __name__ == "__main__":
    main()