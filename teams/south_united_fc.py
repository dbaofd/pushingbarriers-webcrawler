from crawlers import sportstg_com_crawler

def get_fixtures_for_u14_d1():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-196476-553731-25891178&a=SFIX"
    team = "Souths United U14 Div 1 (Under Div2)"
    team_id = 27
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures