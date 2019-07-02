from crawlers import Fixture


def getFixturesFor_U14_d5():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-517357-25667157&a=SFIX"
    team = "Annerley FC U14 Div 5 Sth"
    myFixtures = Fixture.getFixtures(url, team)
    print("helloworld")
    return myFixtures


def getFixturesFor_U13_BYPL():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-516233-21637625&a=SFIX"
    team = "Annerley U13 BYPL"
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def getFixturesFor_U12_d6():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-517367-26423699&a=SFIX"
    team = "Annerley U12 Div 6 Sth"
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def getFixturesFor_U11_Liberia():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-517461-26422349&a=SFIX"
    team = "Annerley U11 Liberia (Cross River)"
    myFixtures = Fixture.getFixtures(url, team)
    return myFixtures


def main():
    getFixturesFor_U14_d5()
    # getFixturesFor_U13_BYPL()
    # getFixturesFor_U12_d6()
    # getFixturesFor_U11_Liberia()


if __name__ == "__main__":
    main()
