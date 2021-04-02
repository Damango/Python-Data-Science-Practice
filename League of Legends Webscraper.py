import csv
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://na.op.gg/summoner/userName=Busters'

uClient = uReq(my_url)


page_html = uClient.read()

page_soup = soup(page_html, "html.parser")


games = page_soup.findAll("div", {"class": 'GameItemWrap'})


writer = open('./CSV Files/games.csv', 'w', )
headers = 'Game_Length, Game_Outcome \n'
writer.write(headers)

gamesLength = len(games)

i = 0

while i < gamesLength:
    gameLength = games[i].find("div", {'class', 'GameLength'}).get_text()
    gameOutCome = games[i].find('div', {'class', 'GameResult'}).text.strip()
    print(gameLength)
    print(gameOutCome)
    print('')

    writer.write(' ' + gameLength + ' ' + gameOutCome)

    i += 1


oneGame = games[0].find("div", {'class', 'GameLength'})

# print(oneGame.get_text())
writer.close()


uClient.close()
