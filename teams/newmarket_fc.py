from crawlers import sportstg_com_crawler


def get_fixtures_for_u13_d3():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136877-576866-26817058&a=SFIX"
    team = "Newmarket FC U13 Div3 Nth"
    team_id = 45
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u14_d1_north():
    url = "https://websites.mygameday.app/team_info.cgi?c=0-9386-136877-602167-26934128&a=SFIX"
    team = "Newmarket FC U14 Div1 North"
    team_id = 61
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures