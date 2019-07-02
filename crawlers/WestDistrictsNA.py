import requests
from bs4 import BeautifulSoup
from crawlers import Fixture
import datetime


def formatDateTime(d):
    newFormDateTime = datetime.datetime.strptime(d, '%d %b %y %I:%M%p').date()
    return newFormDateTime


def getDateAndTimeString(d):
    newFormDateTime = datetime.datetime.strptime(d, '%d %b %y %I:%M%p')
    newFormDateTime = datetime.datetime.strftime(newFormDateTime, '%Y/%m/%d %H:%M')
    return newFormDateTime[0:10], newFormDateTime[11:]


def getAddress(venueTd):
    address = ''
    a = venueTd.find('a')
    # a['onclick']: javascript:sh_ven(8674,39344,1);
    venuePageParameters = a['onclick'].strip().replace('javascript:sh_ven(', '').replace(');', '').split(',')
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/venue.aspx?venueID=" + \
          venuePageParameters[0] + "&entityID=" + venuePageParameters[1] + "&popup=" + venuePageParameters[2]
    if (venuePageParameters[0] != '0'):
        # when the first parameter equals to 0 means this game has been cancelled, no venue
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='html.parser')
        allTables = soup.find_all('table')
        allTds = allTables[1].find_all('td')
        allInfo = allTds[1].find_all(text=True)
        address = allInfo[1] + ',' + allInfo[2].split(',')[0]
        # Fixture.writeOutputFile(r)
    return address


def doFirstRequest():  # this website uses viewstate, in order to imitate request data from server,
    # here the first thing we need to do is to get the viewstate, viewgenerator, eventVlidation
    # from the website by visiting the website
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/draw.aspx"
    exceptionFalg = False
    try:
        r = requests.get(url)
    except Exception as e:
        exceptionFalg = True
        print(e)
    if (exceptionFalg == False):
        soup = BeautifulSoup(r.content, features="html.parser")
        viewStateInput = soup.find('input', {"id": "__VIEWSTATE"})
        viewGeneratorInput = soup.find('input', {"id": "__VIEWSTATEGENERATOR"})
        eventValidationInput = soup.find('input', {"id": "__EVENTVALIDATION"})
        viewState = viewStateInput['value']
        viewGenerator = viewGeneratorInput['value']
        eventValidation = eventValidationInput['value']
    else:
        viewState = ''
        viewGenerator = ''
        eventValidation = ''
    return viewState, viewGenerator, eventValidation


def getFixturesForWestDistrictNA(seasonCode, teamCode, teamFullName, teamShortName):
    viewState, viewGenerator, eventValidation = doFirstRequest()
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/draw.aspx"
    querystring = {"entityid": "39344"}
    data = {
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_ScriptManager1_TSM": ";;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:en-AU:b7585254-495e-4311-9545-1f910247aca5:ea597d4b:b25378d2",
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_StyleManager1_TSSM": "",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATE": viewState,
        "__VIEWSTATEGENERATOR": viewGenerator,
        "__EVENTVALIDATION": eventValidation,
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_widget723dc8fb415444ca9a67b2578861a904_ctl01_Menu2_ClientState": "",
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_rvsb_compOpModeSelector_RadTabStrip1_ClientState": {
            "selectedIndexes": ["0"], "logEntries": [], "scrollState": {}},
        "ctl00$MainPlaceHolder2$RVPageTemplateControl$rvsb$rvsbc_0$lc": seasonCode,
        "ctl00$MainPlaceHolder2$RVPageTemplateControl$rvsb$rvsbc_3$lc": teamCode,
        "ctl00$MainPlaceHolder2$RVPageTemplateControl$rvsb$ctl08": "Go"}
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Origin': "http://www.westerndistricts.qld.netball.com.au",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Referer': "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/draw.aspx?entityid=39344",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        'Cookie': "_ga=GA1.3.208407951.1561528108; _gid=GA1.3.183615835.1561528108; RVCONFIG_N=OPMODE=1; __gads=ID=97cab470773a22b9:T=1561528584:S=ALNI_MYgYj_M9X86OKLdDSmDdMkN2cteGA; RVCONFIG=SelBar_rvsbc_0=108&SelBar_rvsbc_3=39849_1,_ga=GA1.3.208407951.1561528108; _gid=GA1.3.183615835.1561528108; RVCONFIG_N=OPMODE=1; __gads=ID=97cab470773a22b9:T=1561528584:S=ALNI_MYgYj_M9X86OKLdDSmDdMkN2cteGA; RVCONFIG=SelBar_rvsbc_0=108&SelBar_rvsbc_3=39849_1; RVCONFIG_N=OPMODE=1",
        'Postman-Token': "146fbf78-d751-4bc8-bd94-487f550036ec,1aff7b9b-2df1-4cbb-8ade-d442d1d4c331",
        'Host': "www.westerndistricts.qld.netball.com.au",
        'content-length': "8440",
        'cache-control': "no-cache"
    }
    myFixtures = []
    exceptionFlag = False
    try:
        r = requests.request("POST", url, data=data, headers=headers, params=querystring)
    except Exception as e:
        exceptionFlag = True
        print(e)
    if (exceptionFlag == False):
        if (str(r.status_code) == '200'):
            soup = BeautifulSoup(r.content, features="html.parser")
            allTable = soup.find_all(
                'table')  # there are three tables in this page, the first table contains the info we need.
            allTr = allTable[0].find_all('tr')
            for indexi, i in enumerate(allTr):
                tdofTr = i.find_all('td')
                if (indexi > 0):  # There is no td in first tr, it only contains th
                    if (i.get('class') == ['tblSubHeader']):
                        rnd = tdofTr[0].get_text().replace('\n', '').replace('Round ', '')
                    elif (tdofTr[1].get_text() == teamShortName or tdofTr[3].get_text() == teamShortName):
                        fixtureDate = formatDateTime(tdofTr[0].get_text())
                        today = datetime.date.today()  # get today's date
                        if (fixtureDate >= today):  # we only focus on matches after today
                            fixtureDate, fixtureTime = getDateAndTimeString(
                                tdofTr[0].get_text())  # seprate date and time
                            if (tdofTr[1].get_text() == teamShortName):
                                fixtureOpposition = tdofTr[3].get_text()
                            else:
                                fixtureOpposition = tdofTr[1].get_text()
                            address = getAddress(tdofTr[4])
                            myFixtures.append(
                                Fixture.Fixture(rnd, fixtureDate, fixtureTime, tdofTr[4].get_text().replace('\n', ''),
                                                address, fixtureOpposition, teamFullName))
        else:
            myFixtures.append(
                Fixture.Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                                'fail to grap info for this team', '', teamFullName))
    else:
        myFixtures.append(
            Fixture.Fixture('', '', '', 'website is unreachable', 'fail to grap info for this team', '', teamFullName))

    Fixture.printFixtures(myFixtures)
    # Fixture.writeOutputFile(r)

    return myFixtures


def getFixturesFor_Riverlife_9_d3():
    seasonCode = '108'
    teamCode = '39849_1'
    teamFullName = 'Riverlife 09 2019 DS 16-18 yrs Div 3'
    teamShortName = 'Riverlife 09'
    myFixtures = getFixturesForWestDistrictNA(seasonCode, teamCode, teamFullName, teamShortName)
    return myFixtures


def getFixturesFor_Riverlife_15_d6():
    seasonCode = '108'
    teamCode = '39842_1'
    teamFullName = 'Riverlife 15 2019 DS 14/15 yrs Div 6'
    teamShortName = 'Riverlife 15'
    myFixtures = getFixturesForWestDistrictNA(seasonCode, teamCode, teamFullName, teamShortName)
    return myFixtures


def getFixturesFor_Riverlife_19_d4():
    seasonCode = '108'
    teamCode = '39829_1'
    teamFullName = 'Riverlife 19 2019 DS 13 yrs Div 4'
    teamShortName = 'Riverlife 19'
    myFixtures = getFixturesForWestDistrictNA(seasonCode, teamCode, teamFullName, teamShortName)
    return myFixtures


def main():
    getFixturesFor_Riverlife_19_d4()


if __name__ == "__main__":
    main()
