class Player:
    team = "Falcons"
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def add_score(self, points):
        self.score = self.score + points
    def show_score(self):
        print(self.name, self.score, self.team)

player1 = Player("Alex", 20)
player2 = Player("Brian", 30)
player1.add_score(10)          # player1.score = 30
player2.add_score(5)           # player2.score = 35
player1.score = player1.score + 5   # player1.score = 35
Player.team = "Eagles"         # class variable changes
player3 = Player("Carol", 15)
player3.add_score(player1.score)    # add 35 → player3.score = 50

player1.show_score()
player2.show_score()
player3.show_score()