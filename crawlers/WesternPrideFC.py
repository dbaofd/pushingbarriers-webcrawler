from crawlers import Fixture


def getFixturesFor_U16_NPL():
    url = "http://websites.sportstg.com/team_info.cgi?c=0-9385-138099-514969-26388820&a=SFIX"
    team = "Western Pride FC U16 NPL"
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def main():
    getFixturesFor_U16_NPL()


if __name__ == "__main__":
    main()
