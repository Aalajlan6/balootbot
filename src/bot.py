#For now just manual inputs until we implement ml



def bot_buy_phase(game_state):
    #Start at player to the right of dealer, go clockwise
    #options for buy is buy sun, buy hokm, pass
    #Special options for dealer and left of dealer: 
    #ashkal, rulset is sun but buyer's teammate get card
    #for now, manual inputs for all players (including bot, but we're calling bot check to simulate a bot)

    #take terminal input
    print("Bot's turn to buy:")
    print("Options:")
    print("1. Buy Sun")
    print("2. Buy Hokm")
    print("3. Pass")
    print("4. Ashkal (if available)")
    can_ashkal = game_state.players[game_state.dealer_index].team == game_state.current_player.team or game_state.players[(game_state.dealer_index + 1) % 4].team == game_state.current_player.team
    choice = input("Enter your choice: ")
    if choice == "1":
        game_state.buy_phase = "sun"
        print("Bot chose to buy Sun.")
    elif choice == "2":
        game_state.buy_phase = "hokm"
        print("Bot chose to buy Hokm.")
    elif choice == "3":
        game_state.buy_phase = "pass"
        print("Bot chose to pass.")
    elif choice == "4" and can_ashkal:
        game_state.buy_phase = "ashkal"
        print("Bot chose to buy Ashkal.")
    else:
        print("Invalid choice. Please try again.")
        bot_buy_phase(game_state)
