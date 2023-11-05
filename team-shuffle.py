import random

# Set the number of teams and people per team
num_teams = 6
people_per_team = 3

# Define the list of team members
team_members = ['John', 'Jane'] 
# removed for privacy

# Shuffle the list of team members
random.shuffle(team_members)

# Divide the shuffled list into sublists of people_per_team size
teams = [team_members[i:i+people_per_team] for i in range(0, len(team_members), people_per_team)]

#If the last team has fewer members, move them to a different team
if len(teams[-1]) < people_per_team:
    teams[-2] += teams[-1]
    teams.pop()

# If there are more teams than required, merge the last few teams
# while len(teams) > num_teams:
#     teams[-2] += teams[-1]
#     teams.pop()

# Print the teams
print(f"{num_teams} teams with {people_per_team} people per team:")
for i, team in enumerate(teams):
    print(f"Team {i+1}: {', '.join(team)}")
