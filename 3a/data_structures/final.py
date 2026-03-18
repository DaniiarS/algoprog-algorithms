class Participant:
    def __init__(self, uni_name, team_number = -1):
        self.uni_name = uni_name
        self.team_number = team_number

p, n, k = map(int, input().split())

teams = []

for i in range(p):
    uni_name = input()
    team = Participant(uni_name)

    teams.append(team)

team_numbers = list(map(int, input().split()))

for i in range(p):
    teams[i].team_number = team_numbers[i]

for i in range(p):
    print(teams[i].uni_name, teams[i].team_number)
