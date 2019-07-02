from crawlers import Fixture


def getFixturesFor_U12_d6():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517367-26183607&a=SFIX"
    team = "Mt Gravatt U12 Div 6 Sth"
    # r=requests.get("https://morvanzhou.github.io/static/scraping/basic-structure.html")
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def getFixturesFor_MensCity_league4():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517329-25901610&a=SFIX"
    team = "Mt Gravatt Hawks MC4G"
    # r=requests.get("https://morvanzhou.github.io/static/scraping/basic-structure.html")
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def main():
    getFixturesFor_U12_d6()


if __name__ == "__main__":
    main()
