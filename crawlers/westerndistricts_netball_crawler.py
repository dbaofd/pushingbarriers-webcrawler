import requests
from bs4 import BeautifulSoup
from crawlers import Fixture
import datetime

def format_date_time(date_str):
    new_form_date_time = datetime.datetime.strptime(date_str, '%d %b %y %I:%M%p').date()
    return new_form_date_time


def get_date_and_time_string(date_str):
    new_form_date_time = datetime.datetime.strptime(date_str, '%d %b %y %I:%M%p')
    new_form_date_time = datetime.datetime.strftime(new_form_date_time, '%Y/%m/%d %H:%M')
    return new_form_date_time[0:10], new_form_date_time[11:]


def get_address(venue_td):
    address = ''
    a = venue_td.find('a')
    # a['onclick']: javascript:sh_ven(8674,39344,1);
    venue_page_parameters = a['onclick'].strip().replace('javascript:sh_ven(', '').replace(');', '').split(',')
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/venue.aspx?venueID=" + \
          venue_page_parameters[0] + "&entityID=" + venue_page_parameters[1] + "&popup=" + venue_page_parameters[2]
    if (venue_page_parameters[0] != '0'):
        # when the first parameter equals to 0 means this game has been cancelled, no venue
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='html.parser')
        all_tables = soup.find_all('table')
        all_tds = all_tables[1].find_all('td')
        all_info = all_tds[1].find_all(text=True)
        address = all_info[1] + ',' + all_info[2].split(',')[0]
    return address


def do_first_request():  # this website uses viewstate, in order to imitate request data from server,
    # here the first thing we need to do is to get the viewstate, viewgenerator, eventVlidation
    # from the website by visiting the website
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/draw.aspx"
    exception_falg = False
    try:
        r = requests.get(url)
    except Exception as e:
        exception_falg = True
        print(e)
    if (exception_falg == False):
        soup = BeautifulSoup(r.content, features="html.parser")
        view_state_input = soup.find('input', {"id": "__VIEWSTATE"})
        view_generator_input = soup.find('input', {"id": "__VIEWSTATEGENERATOR"})
        event_validation_input = soup.find('input', {"id": "__EVENTVALIDATION"})
        view_state = view_state_input['value']
        view_generator = view_generator_input['value']
        event_validation = event_validation_input['value']
    else:
        view_state = ''
        view_generator = ''
        event_validation = ''
    return view_state, view_generator, event_validation


def get_fixtures(season_code, team_code, team_full_name, team_short_name, team_id):
    view_state, view_generator, event_validation = do_first_request()
    url = "http://www.westerndistricts.qld.netball.com.au/common/pages/public/rv/draw.aspx"
    querystring = {"entityid": "39344"}
    data = {
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_ScriptManager1_TSM": ";;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:en-AU:b7585254-495e-4311-9545-1f910247aca5:ea597d4b:b25378d2",
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_StyleManager1_TSSM": "",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATE": view_state,
        "__VIEWSTATEGENERATOR": view_generator,
        "__EVENTVALIDATION": event_validation,
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_widget723dc8fb415444ca9a67b2578861a904_ctl01_Menu2_ClientState": "",
        "ctl00_MainPlaceHolder2_RVPageTemplateControl_rvsb_compOpModeSelector_RadTabStrip1_ClientState": {
            "selectedIndexes": ["0"], "logEntries": [], "scrollState": {}},
        "ctl00$MainPlaceHolder2$RVPageTemplateControl$rvsb$rvsbc_0$lc": season_code,
        "ctl00$MainPlaceHolder2$RVPageTemplateControl$rvsb$rvsbc_3$lc": team_code,
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
    my_fixtures = []
    exception_flag = False
    try:
        r = requests.request("POST", url, data=data, headers=headers, params=querystring)
    except Exception as e:
        exception_flag = True
        print(e)
    if (exception_flag == False):
        if (str(r.status_code) == '200'):
            soup = BeautifulSoup(r.content, features="html.parser")
            all_table = soup.find_all(
                'table')  # there are three tables in this page, the first table contains the info we need.
            allTr = all_table[0].find_all('tr')
            for indexi, i in enumerate(allTr):
                td_of_tr = i.find_all('td')
                if (indexi > 0):  # There is no td in first tr, it only contains th
                    if (i.get('class') == ['tblSubHeader']):
                        rnd = td_of_tr[0].get_text().replace('\n', '').replace('Round ', '')
                    elif (td_of_tr[1].get_text() == team_short_name or td_of_tr[3].get_text() == team_short_name):
                        fixture_date = format_date_time(td_of_tr[0].get_text())
                        today = datetime.date.today()  # get today's date
                        if (fixture_date >= today):  # we only focus on matches after today
                            fixture_date, fixture_time = get_date_and_time_string(
                                td_of_tr[0].get_text())  # seprate date and time
                            if (td_of_tr[1].get_text() == team_short_name):
                                fixture_opposition = td_of_tr[3].get_text()
                            else:
                                fixture_opposition = td_of_tr[1].get_text()
                            address = get_address(td_of_tr[4])
                            my_fixtures.append(
                                Fixture.Fixture(rnd, fixture_date, fixture_time, td_of_tr[4].get_text().replace('\n', ''),
                                                address, fixture_opposition, team_full_name, team_id))
        else:
            my_fixtures.append(
                Fixture.Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                                'fail to grap info for this team', '', team_full_name))
    else:
        my_fixtures.append(
            Fixture.Fixture('', '', '', 'website is unreachable', 'fail to grap info for this team', '', team_full_name))

    Fixture.print_fixtures(my_fixtures)
    # Fixture.writeOutputFile(r)

    return my_fixtures