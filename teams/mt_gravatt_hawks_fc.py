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
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-576936-26817149&a=SFIX"
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
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9386-136864-567394-26675993&a=SFIX"
    team = "Mt Gravatt Hawks Mens City 7 Gold"
    team_id = 29
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u16_d2():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-576943-26817056&a=SFIX"
    team = "Mt Gravatt Hawks U16 Div2"
    team_id = 32
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u18_d3():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-136864-602156-26934013&a=SFIX"
    team = "Mt Gravatt Hawks U18 Div3"
    team_id = 33
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_mens_city3_silver():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136864-576868-26831659&a=SFIX"
    team = "Mt Gravatt Hawks Mens City 3 Silver"
    team_id = 52
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u16_mjl():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-136864-602159-26934167&a=SFIX"
    team = "Mt Gravatt Hawks U16 MJL"
    team_id = 53
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u15_d2_south():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-136864-602172-26934035&a=SFIX"
    team = "Mt Gravatt Hawks U15 Div2 South"
    team_id = 66
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def main():
    get_fixtures_for_u12_d6()


if __name__ == "__main__":
    main()
