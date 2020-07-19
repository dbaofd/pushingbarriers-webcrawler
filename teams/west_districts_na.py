from crawlers import  westerndistricts_netball_crawler

def get_fixtures_for_riverlife_9_d3():
    season_code = '113'
    team_code = '39849_1'
    team_full_name = 'Riverlife 09 2019 DS 16-18 yrs Div 3'
    team_short_name = 'Riverlife 09'
    team_id=13
    my_fixtures = westerndistricts_netball_crawler.get_fixtures(season_code, team_code, team_full_name, team_short_name,team_id)
    return my_fixtures


def get_fixtures_for_riverlife_15_d6():
    season_code = '113'
    team_code = '39842_1'
    team_full_name = 'Riverlife 15 2019 DS 14-15 yrs Div 6'
    team_short_name = 'Riverlife 15'
    team_id=14
    my_fixtures = westerndistricts_netball_crawler.get_fixtures(season_code, team_code, team_full_name, team_short_name,team_id)
    return my_fixtures


def get_fixtures_for_riverlife_19_d4():
    season_code = '113'
    team_code = '39829_1'
    team_full_name = 'Riverlife 19 2019 DS 13 yrs Div 4'
    team_short_name = 'Riverlife 19'
    team_id=15
    my_fixtures = westerndistricts_netball_crawler.get_fixtures(season_code, team_code, team_full_name, team_short_name,team_id)
    return my_fixtures


def main():
    get_fixtures_for_riverlife_19_d4()


if __name__ == "__main__":
    main()
