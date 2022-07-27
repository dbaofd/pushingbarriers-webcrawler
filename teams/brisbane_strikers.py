from crawlers import sportstg_com_crawler

def get_fixtures_for_u15_npl():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9385-138103-582629-26822699&a=SFIX"
    team = "Brisbane Strikers U15 NPL"
    team_id = 35
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u16_npl():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-205987-598512-26939367&a=SFIX"
    team = "Brisbane Strikers U16 NPL"
    team_id = 54
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u18_npl():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-205987-598514-26939363&a=SFIX"
    team = "Brisbane Strikers U18 NPL"
    team_id = 62
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures