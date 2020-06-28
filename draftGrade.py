import matplotlib.pyplot as plt
import json

allScores = {}
with open('weekScores2019.json') as json_file: 
    allScores = json.load(json_file)

# # iterate teams in order of rank
# for teamName in sorted(allScores, key=lambda i: allScores[i]['rank']):
#     teamScores = allScores[teamName]['scores']
#     weeks = [int(week) for week in teamScores.keys()]
#     points = list(teamScores.values())

#     rank = allScores[teamName]['rank']

#     label = str(rank) + " " + teamName + " " + str(int(sum(points)))
#     lineWidth = 2 if rank == 5 else 0
#     plt.plot(weeks, points, label=label, lw=lineWidth, marker=".", ms=24)

# # set up labels and axes
# plt.xlabel('Week')
# plt.ylabel('Points')
# plt.legend()
# axes = plt.gca()
# axes.set_ylim([0,250])

# # show
# plt.show()

# iterate teams in order of rank
# for teamName in sorted(allScores, key=lambda i: allScores[i]['rank']):
#     teamScores = allScores[teamName]['scores']
#     weeks = [int(week) for week in teamScores.keys()]
#     points = list(teamScores.values())

#     rank = allScores[teamName]['rank']

#     label = str(rank) + " " + teamName + " " + str(int(sum(points)))
#     lineWidth = 2 if rank == 1 else 0
#     plt.plot(weeks, points, label=label, lw=lineWidth, marker=".", ms=24)

# # set up labels and axes
# plt.xlabel('Week')
# plt.ylabel('Points')
# plt.legend()
# axes = plt.gca()
# axes.set_ylim([0,250])
orderedTeamNames = sorted(allScores, key=lambda i: allScores[i]['grade'])
grades = [allScores[team]['grade'] for team in orderedTeamNames]
ranks = [allScores[team]['rank'] for team in orderedTeamNames]

plt.table(
    cellText=grades,
    rowLabels=orderedTeamNames,
    colLabels=['grade'],
    loc='bottom')

# show
plt.show()