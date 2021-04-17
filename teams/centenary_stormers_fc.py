from crawlers import sportstg_com_crawler


def get_fixtures_for_u16_d3():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9386-136821-553728-26683997&a=SFIX"
    team = "Centenary Stormers U16 Div3"
    team_id = 28
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u13_bypl():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136821-576239-26804019&a=SFIX"
    team = "Centenary Stormers U13 BYPL"
    team_id = 37
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u14_bypl():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136821-576252-26804021&a=SFIX"
    team = "Centenary Stormers U14 BYPL"
    team_id = 38
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u16_d4():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136821-576938-26821011&a=SFIX"
    team = "Centenary Stormers U16 Div4"
    team_id = 39
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u18_d2():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136821-576980-26831706&a=SFIX"
    team = "Centenary Stormers Mens U18 Div2"
    team_id = 40
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u12_mixed_d7():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-136821-586189-26846086&a=SFIX"
    team = "Centenary Stormers U12 Mixed Div7"
    team_id = 36
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures