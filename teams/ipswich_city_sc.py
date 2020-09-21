from crawlers import sportstg_com_crawler


def get_fixtures_for_u18_women():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9386-136859-558964-26676449&a=SFIX"
    team = "Ipswich City U18 Women"
    team_id = 30
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures
