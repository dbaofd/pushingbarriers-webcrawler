from crawlers import sportstg_com_crawler


def get_fixtures_for_u14_d1():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-196524-576951-26799802&a=SFIX"
    team = "Olympic FC U14 Div1"
    team_id = 11
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures