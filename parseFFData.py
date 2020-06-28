import xml.etree.ElementTree as ET
import json

tree = ET.parse('matchups2019.xml')
root = tree.getroot()
teams = root[0]
# I've removed the namespace on the elements for ease
# if parsing real data, need to handle that
allTeamInfo = {}

for team in teams:
    teamKey = team.find('team_key').text
    teamName = team.find('name').text
    teamPointsElems = team.findall("./matchups/matchup/teams/team[1]/team_points")
    weekToPoints = {}
    for teamPointElem in teamPointsElems:
        week = int(teamPointElem.find('week').text)
        points = float(teamPointElem.find('total').text)
        weekToPoints[week] = points 
    rank = int(team.find("./team_standings/rank").text)
    grade = team.find("./draft_grade").text

    teamInfo = {}
    teamInfo['rank'] = rank
    teamInfo['scores'] = weekToPoints
    teamInfo['grade'] = grade
    allTeamInfo[teamName] = teamInfo

with open('weekScores2019.json', 'w') as fp:
    json.dump(allTeamInfo, fp)
