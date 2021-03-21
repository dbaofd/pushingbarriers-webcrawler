from crawlers import sportstg_com_crawler

def get_fixtures_for_u14_girls_d1():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136865-576940-26817147&a=SFIX"
    team = "Grange Thistle U14 Girls Div1"
    team_id = 47
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures