from crawlers import sportstg_com_crawler


def get_fixtures_for_u14_bypl():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136848-576252-26796646&a=SFIX"
    team = "Rochedale Rovers U14 BYPL"
    team_id = 46
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures