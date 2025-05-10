from crawlers import sportstg_com_crawler

def get_fixtures_for_u15_fqpl():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-136818-598504-26915627&a=SFIX"
    team = "Virginia United U15 FQPL"
    team_id = 63
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures