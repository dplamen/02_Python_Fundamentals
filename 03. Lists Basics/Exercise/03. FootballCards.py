cards = input().split()
team_A = [str(x) for x in range(1,12)]
team_B = [str(x) for x in range(1, 12)]
terminated = False
for card in cards:
    team, number = card.split('-')
    if team == 'A' and number in team_A:
        team_A.remove(number)
    elif team == 'B' and number in team_B:
        team_B.remove(number)
    if len(team_A) < 7 or len(team_B) < 7:
        terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated:
    print('Game was terminated')
