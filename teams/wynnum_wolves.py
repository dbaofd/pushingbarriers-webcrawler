from crawlers import sportstg_com_crawler

def get_fixtures_for_u14_d1_south():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-196496-602180-26934817&a=SFIX"
    team = "Wynnum Wolves U14 Div1 South"
    team_id = 64
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures