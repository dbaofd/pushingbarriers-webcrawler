from crawlers import Fixture


def getFixturesFor_2019GYL_d2():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-4826-75261-524375-26469179&a=SFIX"
    team = "West Brisbane Falcons Black 2019 G.Y.L D2"
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def main():
    getFixturesFor_2019GYL_d2()


if __name__ == "__main__":
    main()
