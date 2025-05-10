from crawlers import sportstg_com_crawler

def get_fixtures_for_u15_d1_girls():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-162699-602185-26934804&a=SFIX"
    team = "North Brisbane U15 Div1 Girls"
    team_id = 65
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures