class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        win_per = self.team_wins / (self.team_wins + self.team_losses)
        return win_per

    # TODO: Define print_standing()
    def print_standing(self):
        if self.get_win_percentage() >= .50:
            print(f'Congratulations, Team {self.team_name} has a winning average!')
        else:
            print(f'Team {self.team_name} has a losing average.')

if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.team_name = user_name
    team.team_wins = user_wins
    team.team_losses = user_losses

    team.get_win_percentage()
    team.print_standing()
