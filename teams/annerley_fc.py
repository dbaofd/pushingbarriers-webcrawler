from crawlers import sportstg_com_crawler


def get_fixtures_for_u14_d5():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136810-553233-19927606&a=SFIX"
    team = "ANNERLEY U13 DIV 1 STH"
    team_id = 1
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_u13_bypl():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-516233-21637625&a=SFIX"
    team = "Annerley U13 BYPL"
    team_id = 2
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_u12_d6():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-517367-26423699&a=SFIX"
    team = "Annerley U12 Div 6 Sth"
    team_id = 3
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_u11_liberia():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136810-517461-26422349&a=SFIX"
    team = "Annerley U11 Liberia (Cross River)"
    team_id = 4
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_u13_d5_sth():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136810-553222-26676398&a=SFIX"
    team = "Annerley U13 Div5 Sth"
    team_id = 23
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u14_d4():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136810-576921-26817055&a=SFIX"
    team = "Annerley U14 Div4 Sth"
    team_id = 34
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def main():
    get_fixtures_for_u14_d5()


if __name__ == "__main__":
    main()
