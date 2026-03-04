#where game is ran, calls bot when its its turn.

from rules import *
import random


def main():
    #Set bot position randomly (between four slots)
    bot_position = random.randint(0, 3)
    print(f"Bot is in position {bot_position}")
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
    print("Players:")
    for p in game_state.players:
        print(p.name)
    # Initialize deck
    for suit in game_state.suits:
        for rank in game_state.ranks:
            game_state.deck.append(card(suit, rank))
    # Shuffle deck
    random.shuffle(game_state.deck)
    # Randomly pick dealer
    game_state.dealer_index = random.randint(0, 3)
    print(f"Dealer is {game_state.players[game_state.dealer_index].name}")
    #Declare order of play for this current round (start at dealer, then go clockwise)
    order_of_play = []
    for i in range(4):
        order_of_play.append(game_state.players[(game_state.dealer_index + i) % 4])
    print("Order of play:")
    for p in order_of_play:
        print(p.name)

if __name__ == "__main__":
    main()