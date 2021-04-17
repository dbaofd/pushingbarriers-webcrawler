from crawlers import sportstg_com_crawler


def get_fixtures_for_u18_d2():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-196468-576980-26831615&a=SFIX"
    team = "Ipswich Knights Mens U18 Div2"
    team_id = 50
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures
