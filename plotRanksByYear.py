import matplotlib.pyplot as plt
import json

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

teamData = {}
with open('teamsByYear.json') as json_file: 
    teamData = json.load(json_file)

# iterate teams in order of rank
for teamId in teamData:
    seasonsData = teamData[teamId]
    seasons = list(seasonsData.keys())
    ranks = [data['rank'] for data in seasonsData.values()]
    teams = [data['team'] for data in seasonsData.values()]
    nickname = list(seasonsData.values())[0]['nickname']

    plt.plot(seasons, ranks, label=nickname, lw=0.5, marker=".", ms=12)
    for i in range(len(teams)):
        label = teams[i] + "\n (" + nickname + ")"
        plt.annotate(
            label, # this is the text
            (seasons[i],ranks[i]), # this is the point to label
            fontsize=6,
            textcoords="offset points", # how to position the text
            xytext=(0,10), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center

# set up labels and axes
plt.xlabel('season')
plt.ylabel('rank')
# plt.legend()

plt.gca().invert_yaxis()
# plt.grid(True)

# locs, labels = plt.yticks()
ticks = list(range(14))
labels = [str(tick) for tick in ticks]
labels[0] = ""
labels[-1] = ""
plt.yticks(ticks, labels)
# show
plt.show()