from crawlers import sportstg_com_crawler


def get_fixtures_for_u18_d2_silver():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9386-136813-567393-26676494&a=SFIX"
    team = "Oxley United Mens U18 Div 2 Silver"
    team_id = 13
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures
