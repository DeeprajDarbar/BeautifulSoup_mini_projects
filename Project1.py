import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.skysports.com/premier-league-table/2019"
page = requests.get(url)
# print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
league = soup.find('table', class_='standing-table__table')
# print(league)
league_table = league.find_all('tbody')

league_2019, ln, lgd, lg = [],[],[],[]
for league_teams in league_table:
    rows = league_teams.find_all('tr')
    for row in rows:
        team_names = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        team_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()
        team_diff = row.find_all('td', class_='standing-table__cell')[8].text.strip()
        team_g = row.find_all('td', class_='standing-table__cell')[6].text.strip()
        #print(team_names,team_points)
        league_dict = {'Name':team_names,'Points':team_points}
        league_dict1 = {'Name':team_names, 'Goaldiff': team_diff}
        ln.append(team_names)
        lgd.append(int(team_diff))
        lg.append(int(team_g))
        league_2019.append(league_dict)
df = pd.DataFrame({'Name':ln,'Goaldiff':lgd})
print(df.head())
df.plot(x='Name', y='Goaldiff', rot=0)
dt = pd.DataFrame({'Name':ln,'Goal':lg})
print(dt.head())
dt.plot.bar(x='Name', y='Goal', rot=0)
plt.show()
