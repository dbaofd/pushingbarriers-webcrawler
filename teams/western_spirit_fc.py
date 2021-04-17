from crawlers import sportstg_com_crawler


def get_fixtures_for_u18_d1_silver():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136869-576945-26831567&a=SFIX"
    team = "Western Spirit U18 Div1 Silver"
    team_id = 48
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures