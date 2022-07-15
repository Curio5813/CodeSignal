a = [50, 60, 60, 45, 70]

def alternatingSums(a):
    """
    Several people are standing in a row and need to be divided into two teams. The first
    person goes into team 1, the second goes into team 2, the third goes into team 1 again,
    the fourth into team 2, and so on.
    """
    team1, team2, teams = 0, 0, []
    for k in range(0, len(a)):
        if k % 2 == 0:
            team1 += a[k]
        if k % 2 == 1:
            team2 += a[k]
    teams.append(team1)
    teams.append(team2)
    return teams


print(alternatingSums(a))
