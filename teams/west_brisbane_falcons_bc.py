from crawlers import sportstg_com_crawler

def get_fixtures_for_2019gyl_d2():
    url = "http://websites.sportstg.com/team_info.cgi?c=1-4826-75261-524375-26469179&a=SFIX"
    team = "West Brisbane Falcons Black 2019 G.Y.L D2"
    team_id=12

    my_fixtures = sportstg_com_crawler.get_fixtures(url, team, team_id, 1)
    return my_fixtures

def main():
    get_fixtures_for_2019gyl_d2()


if __name__ == "__main__":
    main()
