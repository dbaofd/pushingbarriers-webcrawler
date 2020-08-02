from crawlers import sportstg_com_crawler


def get_fixtures_for_u16_d3():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9386-136821-553728-26683997&a=SFIX"
    team = "Centenary Stormers U16 Div3"
    team_id = 28
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures
