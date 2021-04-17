from crawlers import qcsa_org_crawler


def get_fixtures_for_u1718_d1():
    data = {"ClubCode": "WESTW", "AgeGrp": "U1718M", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "Westminster Warriors U1718 Div1"
    team_id = 43
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures