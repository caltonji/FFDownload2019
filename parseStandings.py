import xml.etree.ElementTree as ET
import json

tree = ET.parse('standingsByYear.xml')
root = tree.getroot()

# I've removed the namespace on the elements for ease
# if parsing real data, need to handle that
# leaguesData = {}
teamsData = {}
for league in root.findall("./leagues/league"):
    season = league.find("./season").text
    print(season)
    for team in league.findall("./standings/teams/team"):
        teamName = team.find("name").text
        managerName = team.find("./managers/manager/nickname").text
        managerEmailElem = team.find("./managers/manager/email")
        managerEmail = managerEmailElem.text if managerEmailElem != None else "NA"
        managerId = team.find("./managers/manager/guid").text
        rank = int(team.find("./team_standings/rank").text)
        totalPoints = float(team.find("./team_points/total").text)
        if managerId not in teamsData:
            teamsData[managerId] = {}
        teamsData[managerId][season] = {
            "team": teamName,
            "nickname": managerName,
            "email": managerEmail,
            "rank": rank,
            "points": totalPoints
        }

with open('teamsByYear.json', 'w') as fp:
    json.dump(teamsData, fp)