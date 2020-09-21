from crawlers import qcsa_org_crawler


def get_fixtures_for_u12_d4():
    data = {"ClubCode": "WELSH", "AgeGrp": "U12", "Division": "4", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U12 Div4"
    team_id = 5
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u14_d2():
    data = {"ClubCode": "WELSH", "AgeGrp": "U14", "Division": "2", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U14 Div2"
    team_id = 6
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u16_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1516B", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1516B Div1"
    team_id = 7
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u16girls_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1516G", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1516G Div1"
    team_id = 8
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u18_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1718M", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1718M Div1"
    team_id = 1
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u1516b_d2():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1516B", "Division": "2", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1516B Div2"  # cannot name the team with U15/16B
    # because this name will be involved in a query. '/' will cause 404, since '/' is keyword in query
    team_id = 3
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u14_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U14", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U14 Div1"
    team_id = 3
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_u12_d2():
    data = {"ClubCode": "WELSH", "AgeGrp": "U12", "Division": "2", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U12 Div2"
    team_id = 4
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def get_fixtures_for_sm_d4():
    data = {"ClubCode": "WELSH", "AgeGrp": "SM", "Division": "4", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone SM Div4"
    team_id = 22
    my_fixtures = qcsa_org_crawler.get_fixtures(data, team, team_id)
    return my_fixtures


def main():
    get_fixtures_for_sm_d4()


if __name__ == "__main__":
    main()
