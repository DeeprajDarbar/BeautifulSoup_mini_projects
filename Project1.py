import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.skysports.com/premier-league-table/2019"
page = requests.get(url)
# print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
league = soup.find('table', class_='standing-table__table')
# print(league)
league_table = league.find_all('tbody')

league_2019 = []
for league_teams in league_table:
    rows = league_teams.find_all('tr')
    for row in rows:
        team_names = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        team_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()
        #print(team_names,team_points)
        league_dict = {'Name':team_names,'Points':team_points}
        league_2019.append(league_dict)

df = pd.DataFrame(league_2019)
df.head()
