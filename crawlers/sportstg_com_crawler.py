import datetime
from bs4 import BeautifulSoup
import requests
from crawlers import Fixture

def format_date(str_date):
    new_form_date = datetime.datetime.strptime(str_date, '%d/%m/%y').date()
    return new_form_date

def write_output_file(r):
    file_name = "output.html"
    f = open(file_name, "w")
    f.write(r.content.decode("utf-8"))
    f.close


def get_address_for_fc(venue_td):
    a = venue_td.find_all('a')  # the venue td contains <a> tag with href, the href links to a detail
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
                address = venue_td.get_text()
    return address


def get_address_for_bc(venue_td):
    # the reason we need this function is football venues and basketball venues have different web page structures
    # so we need this to grap detailed venue for basketball club
    a = venue_td.find_all('a')
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


def get_fixtures(url, team, team_id, team_type):
    #team_type 1:basket, 0:football
    my_fixtures = []
    exception_flag = False
    try:
        r = requests.get(url)
    except Exception as e:
        exception_flag = True
        print(e)
    if (exception_flag == False):  # website is reachable
        if (str(r.status_code) == '200'):  # status code is 200 which is good
            soup = BeautifulSoup(r.content, features="html.parser")
            alltr = soup.find_all('tr')  # all the info we need is in <tr></tr>
            today = datetime.date.today()  # get today's date
            for indexi, i in enumerate(alltr):
                tdofTr = i.find_all('td')  # for every fixture, attributes are in different <td></td>
                if (len(tdofTr) >= 8):  # why set td number greater than 8? Because  a fixture usually has 9 td tags
                    # while a fixture is cancelled, it has 8 td tags, you can check the web saurce code
                    fixture_date = format_date(tdofTr[1].get_text()[0:8])
                    if (fixture_date >= today):  # compare fixtureDate with today, we only focus on fixture after today
                        if (team_type != 1):  # the only basketball team we got
                            print(tdofTr[3])
                            address = get_address_for_fc(tdofTr[3])
                        else:
                            address = get_address_for_bc(tdofTr[3])
                        my_fixtures.append(
                            Fixture.Fixture(tdofTr[0].get_text().strip(), datetime.datetime.strftime(fixture_date, "%Y/%m/%d"),
                                    tdofTr[2].get_text(), tdofTr[3].get_text(), address, tdofTr[6].get_text(), team, team_id))
        else:
            my_fixtures.append(
                Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                        'fail to grap info for this team', '', team, team_id))
    else:
        my_fixtures.append(
            Fixture('', '', '', 'website is unreachable', 'fail to grap info for this team', '', team, team_id))
    Fixture.print_fixtures(my_fixtures)
    write_output_file(r)

    return my_fixtures