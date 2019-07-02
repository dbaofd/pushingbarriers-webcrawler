import datetime
from bs4 import BeautifulSoup
import requests


class Fixture():
    def __init__(self, rnd, date, time, venue, address, opposition, team):
        self.rnd = rnd
        self.date = date
        self.time = time
        self.venue = venue
        self.address = address
        self.opposition = opposition
        self.team = team

    def get_rnd(self):
        return self.rnd

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_venue(self):
        return self.venue

    def get_address(self):
        return self.address

    def get_opposition(self):
        return self.opposition

    def get_team(self):
        return self.team


def formatDate(s):
    newFormDate = datetime.datetime.strptime(s, '%d/%m/%y').date()
    return newFormDate


def printFixtures(myFixtures):
    for index in range(0, len(myFixtures)):
        print(myFixtures[index].get_rnd() + "\n" + myFixtures[index].get_date() + "\n" + myFixtures[
            index].get_time() + "\n" + myFixtures[index].get_venue() + "\n" + myFixtures[index].get_address()
              + '\n' + myFixtures[index].get_opposition() + "\n" + myFixtures[index].get_team())
        print("**************************")


def writeOutputFile(r):
    filename = "output.html"
    f = open(filename, "w")
    f.write(r.content.decode("utf-8"))
    f.close


def getAddressForFC(venueTd):
    a = venueTd.find_all('a')  # the venue td contains <a> tag with href, the href links to a detail
    address = ''  # localtion of venue
    if (a != []):  # the length of a is 1 aways
        # sometimes when a game is cancelled, there is no venue provided, so there will be no <a> tag
        for j in a:
            r = requests.get('http://websites.sportstg.com/' + j['href'])
            soup = BeautifulSoup(r.content, features="html.parser")
            address = soup.find_all('div', {'class': "venue-desc"})
            if (address[0].get_text() != ' '):
                # sometimes the herf links to a location page without detailed venue information
                # which makes the program can't find div with venue-desc class
                address = address[0].get_text()
            else:  # if situation mentioned above happens, use venue to set the detailedlvenue
                address = venueTd.get_text()
    return address


def getAddressForBC(venueTd):
    # the reason we need this function is football venues and basketball venues have different web page structures
    # so we need this to grap detailed venue for basketball club
    a = venueTd.find_all('a')
    address = ''
    if (a != []):
        for j in a:
            r = requests.get('http://websites.sportstg.com/' + j['href'])
            soup = BeautifulSoup(r.content, features="html.parser")
            allTables = soup.find_all('table')
            allTds = allTables[0].find_all('td')  # detailed venue information is in the first table
            allInfo = allTds[1].find_all(text=True)
            address = allInfo[0] + ", " + allInfo[1]  # detailed venue information is in the second td
    return address


def getFixtures(url, team):
    myFixtures = []
    exceptionFlag = False
    try:
        r = requests.get(url)
    except Exception as e:
        exceptionFlag = True
        print(e)
    if (exceptionFlag == False):  # website is reachable
        if (str(r.status_code) == '200'):  # status code is 200 which is good
            soup = BeautifulSoup(r.content, features="html.parser")
            alltr = soup.find_all('tr')  # all the info we need is in <tr></tr>
            for indexi, i in enumerate(alltr):
                tdofTr = i.find_all('td')  # for every fixture, attributes are in different <td></td>
                if (len(tdofTr) >= 8):  # why set td number greater than 8? Because  a fixture usually has 9 td tags
                    # while a fixture is cancelled, it has 8 td tags, you can check the web saurce code
                    fixtureDate = formatDate(tdofTr[1].get_text()[0:8])
                    today = datetime.date.today()  # get today's date
                    if (fixtureDate >= today):  # compare fixtureDate with today, we only focus on fixture after today
                        if (team != "West Brisbane Falcons Black 2019 G.Y.L D2"):  # the only basketball team we got
                            address = getAddressForFC(tdofTr[3])
                        else:
                            address = getAddressForBC(tdofTr[3])
                        myFixtures.append(
                            Fixture(tdofTr[0].get_text().strip(), datetime.datetime.strftime(fixtureDate, "%Y/%m/%d"),
                                    tdofTr[2].get_text(), tdofTr[3].get_text(), address, tdofTr[6].get_text(), team))
        else:
            myFixtures.append(
                Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                        'fail to grap info for this team', '', team))
    else:
        myFixtures.append(
            Fixture('', '', '', 'website is unreachable', 'fail to grap info for this team', '', team))
    printFixtures(myFixtures)
    # writeOutputFile(r)

    return myFixtures
