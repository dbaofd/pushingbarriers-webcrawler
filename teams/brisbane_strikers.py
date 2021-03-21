from crawlers import sportstg_com_crawler

def get_fixtures_for_u15_npl():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9385-138103-582629-26822699&a=SFIX"
    team = "Brisbane Strikers U15 NPL"
    team_id = 35
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures