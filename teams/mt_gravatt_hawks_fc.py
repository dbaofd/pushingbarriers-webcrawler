from crawlers import sportstg_com_crawler


def get_fixtures_for_u12_d6():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517367-26183607&a=SFIX"
    team = "Mt Gravatt U12 Div 6 Sth"
    team_id = 10
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_mens_city_league4():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517329-25901610&a=SFIX"
    team = "Mt Gravatt Hawks MC4G"
    team_id = 11
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u15_d2():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-553723-26676362&a=SFIX"
    team = "Mt Gravatt Hawks U15 Div2"
    team_id = 25
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u14_d3_sth():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-553750-24836632&a=SFIX"
    team = "Mt Gravatt U14 Div3 Sth"
    team_id = 26
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_mens_city7_gold():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-553750-24836632&a=SFIX"
    team = "Mt Gravatt Hawks Mens City 7 Gold"
    team_id = 29
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def main():
    get_fixtures_for_u12_d6()


if __name__ == "__main__":
    main()
