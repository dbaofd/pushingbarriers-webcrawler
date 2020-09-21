from crawlers import sportstg_com_crawler


def get_fixtures_for_u14_npl():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9385-138099-555047-26649741&a=SFIX"
    team = "Western Pride FC U14 NPL(MALE)"
    team_id = 16
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures


def get_fixtures_for_u18_npl():
    url = "https://websites.sportstg.com/team_info.cgi?c=0-9385-138099-555036-26649681&a=SFIX"
    team = "Western Pride FC U18 NPL(FEMALE)"
    team_id = 18
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def get_fixtures_for_u12_d1_sth():
    url = "https://websites.sportstg.com/team_info.cgi?c=1-9386-196515-561766-26692744&a=SFIX"
    team = "Western Pride U12 Div1 Sth"
    team_id = 31
    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 0)
    return my_fixtures

def main():
    get_fixtures_for_u18_npl()


if __name__ == "__main__":
    main()
