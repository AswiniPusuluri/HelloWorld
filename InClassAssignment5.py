from collections import deque


class Player(object):
    def __init__(self, name, age, skills, style=None):
        self.name = name
        self.age = age
        self.skills = skills
        self.style = style

    def get_player(self):
        print(self.name, self.age, self.skills, self.style)


class Team(object):
    def __init__(self, name, year, total_matches, matches_win):
        self.name = name
        self.year = year
        self.total_matches = total_matches
        self.matches_win = matches_win
        self._players = deque()

    def add_player(self, obj):
        if obj:
            self._players.append(obj)
        else:
            print("Please provide player object")

    def remove_player(self, obj):
        if obj:
            self._players.remove(obj)
        else:
            print("Please provide player object")

    def get_players(self):
        for player in self._players:
            player.get_player()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    p1 = Player("Mahendra", 46, "Wicket Kipper", "Right-Hand Batsman")
    p2 = Player("Sachin", 35, "Batsman", "Right-Hand Batsman")
    p3 = Player("Saurabh", 44, "Batsman", "Left-Hand Batsman")
    p4 = Player("Zahir", 38, "Bauwller", "Medium Pace Bauwller")
    p5 = Player("Yuvraj", 43, "All rounder")

    t1 = Team("India", 2020, 10, 4)
    t1.add_player(p1)
    t1.add_player(p2)
    t1.add_player(p3)
    t1.add_player(p4)
    t1.add_player(p5)
    print('***************team1****************')
    t1.get_players()

    t2 = Team("Australia", 2020, 7, 7)
    t2.add_player(p1)
    t2.add_player(p2)
    t2.add_player(p3)
    t2.add_player(p4)
    t2.add_player(p5)
    print('***************team2****************')
    t2.get_players()

    t3 = Team("SriLanka", 2020, 8, 6)
    t3.add_player(p1)
    t3.add_player(p2)
    t3.add_player(p3)
    t3.add_player(p4)
    t3.add_player(p5)
    print('***************team3****************')
    t3.get_players()
    # plot
    Teams = [t1.name, t2.name, t3.name]
    Win_matches = [t1.matches_win, t2.matches_win, t3.matches_win]

    plt.bar(Teams, Win_matches)
    plt.title('Team Vs Win_matches')
    plt.xlabel('Teams')
    plt.ylabel('Win_matches')
    plt.show()


