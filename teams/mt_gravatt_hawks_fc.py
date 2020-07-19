from crawlers import sportstg_com_crawler


def get_fixtures_for_u12_d6():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517367-26183607&a=SFIX"
    team = "Mt Gravatt U12 Div 6 Sth"
    team_id = 10
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_mens_city_league4():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-9386-136864-517329-25901610&a=SFIX"
    team = "Mt Gravatt Hawks MC4G"
    team_id = 11
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def main():
    get_fixtures_for_u12_d6()


if __name__ == "__main__":
    main()
