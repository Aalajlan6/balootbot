# Setting cards
class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.team = None  # boolean. True for same team, false for opposing team

class gameStates:
    def __init__(self):
        self.players = [player("Player 1"), player("Player 2"), player("Player 3"), player("Player 4")]
        self.deck = []
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.ranks = ["7", "8", "9", "10", "J", "Q", "K", "A"]
        self.current_player_index = 0
        self.ruleset = "sun" #or "hokm"
        self.hokm = None #(diamonds, clubs, hearts, spades), only if Hokm is invoked
        self.opposing_team_score = 0
        self.same_team_score = 0
        self.current_player = self.players[self.current_player_index]
        self.phase = "buying" #or "playing"
        self.buy_card = None #Single card offered for sale during buying phase
        self.dealer_index = 0 # Dealer index, changes every round clockwise, first buyer is to the right (+1 on index)

class rulset:
    def __init__(self, game_state):
        self.game_state = game_state
        self.rank_strength = ["7", "8", "9", "J", "Q", "K", "10", "A"] #Weakest to strongest
# Rulset for Hokm
class sunRules (rulset):
    def __init__(self, game_state):
        super().__init__(game_state)
class hokmRules(rulset):
    def __init__(self, game_state):
        super().__init__(game_state)
        self.hokm_rank_strength = ["7", "8", "Q", "K", "10", "A", "9", "J"] #Weakest to strongest
        self.chosen_suit = game_state.hokm


        