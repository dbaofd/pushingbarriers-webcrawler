import requests
from bs4 import BeautifulSoup
from crawlers import Fixture
import datetime
import re


def formatDate(s):
    newFormDate = re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)  # remove st,nd,rd,th from date
    newFormDate = re.sub("'", "20", newFormDate)  # replace ' with 20
    newFormDate = datetime.datetime.strptime(newFormDate, '%d %b %Y').date()
    return newFormDate


def getAddress(venueTd):
    a = venueTd.find_all('a')
    address = ''
    if (a != []):
        for j in a:
            r = requests.get('http://www.qcsa.org.au/Draw/' + j['href'])
            soup = BeautifulSoup(r.content, features="html.parser")
            allTables = soup.find_all('table')
            allTds = allTables[1].find_all('td')
            allInfo = allTds[2].find_all(text=True)
            # this td contains all the venue info, but info is separated by <br> tag
            # findall by text=True will get a list of text that are separated by <br>
            address = allInfo[1] + ", " + allInfo[3]
    return address


def getFixturesForBlackStoneUnitedDragons(data, team):
    url = "http://www.qcsa.org.au/Draw/WebsiteComponents/ShowResultsDisplayData.asp"
    myFixtures = []
    exceptionFlag = False
    try:
        r = requests.post(url, data=data)
    except Exception as e:
        exceptionFlag = True
        print(e)

    if (exceptionFlag == False):
        if (str(r.status_code) == '200'):
            soup = BeautifulSoup(r.content, features="html.parser")
            alltable = soup.find_all('table')
            for indexi, i in enumerate(alltable):
                if indexi == 2:
                    trofTable = i.find_all('tr')
                    for indexj, j in enumerate(trofTable):
                        if (indexj > 0):
                            tdofTr = j.find_all('td')
                            fixtureDate = formatDate(tdofTr[1].get_text())
                            today = datetime.date.today()  # get today's date
                            if (fixtureDate >= today):  # we only focus on matches after today
                                if (tdofTr[6].get('class') != None):
                                    # if class != none means this tag is our team, other this tag is opsition
                                    fixtureOpposition = tdofTr[8].get_text()  # here we need to find opposition
                                else:
                                    fixtureOpposition = tdofTr[6].get_text()
                                detailedVenue = getAddress(tdofTr[10])
                                myFixtures.append(Fixture.Fixture(tdofTr[0].get_text().strip(),
                                                                  datetime.datetime.strftime(fixtureDate, "%Y/%m/%d"),
                                                                  tdofTr[2].get_text(), tdofTr[10].get_text(),
                                                                  detailedVenue, fixtureOpposition, team))
        else:
            myFixtures.append(
                Fixture.Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                                'fail to grap info for this team', '', team))
    else:
        myFixtures.append(
            Fixture.Fixture('', '', '', 'website is unreachable', 'fail to grap info for this team', '', team))
    Fixture.printFixtures(myFixtures)
    # Fixture.writeOutputFile(r)
    return myFixtures


def getFixturesFor_U12_d4():
    data = {"ClubCode": "WELSH", "AgeGrp": "U12", "Division": "4", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U12 Div4"
    myFixtures = getFixturesForBlackStoneUnitedDragons(data, team)
    return myFixtures


def getFixturesFor_U14_d2():
    data = {"ClubCode": "WELSH", "AgeGrp": "U14", "Division": "2", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U14 Div2"
    myFixtures = getFixturesForBlackStoneUnitedDragons(data, team)
    return myFixtures


def getFixturesFor_U16_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1516B", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1516B Div1"
    myFixtures = getFixturesForBlackStoneUnitedDragons(data, team)
    return myFixtures


def getFixturesFor_U16girls_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1516G", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1516G Div1"
    myFixtures = getFixturesForBlackStoneUnitedDragons(data, team)
    return myFixtures


def getFixturesFor_U18_d1():
    data = {"ClubCode": "WELSH", "AgeGrp": "U1718M", "Division": "1", "Team": "", "GameDate": "", "RoundNo": "",
            "GroundCode": "", "showLiveResults": "ON"}
    team = "BlackStone U1718M Div1"
    myFixtures = getFixturesForBlackStoneUnitedDragons(data, team)
    return myFixtures


def main():
    getFixturesFor_U14_d2()


if __name__ == "__main__":
    main()
