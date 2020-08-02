import requests
from bs4 import BeautifulSoup
from crawlers import Fixture
import datetime
import re

"""
Summary of the file.
The crawler is for qcsa website.
"""
def format_date(date_str):
    """
    Resolve the extracted date, transform it into to standard date form.
    :param date_str: string.
    :return: new_form_date: date.
    """
    new_form_date = re.sub(r'(\d)(st|nd|rd|th)', r'\1', date_str)  # remove st,nd,rd,th from date
    new_form_date = re.sub("'", "20", new_form_date)  # replace ' with 20
    new_form_date = datetime.datetime.strptime(new_form_date, '%d %b %Y').date()
    return new_form_date


def get_address(venue_td):
    """
    Get the address of a game.
    :param venue_td: html <td>.
    :return: address: string.
    """
    a = venue_td.find_all('a')
    address = ''
    if (a != []):
        for j in a:
            r = requests.get('http://www.qcsa.org.au/Draw/' + j['href'])
            soup = BeautifulSoup(r.content, features="html.parser")
            all_tables = soup.find_all('table')
            all_tds = all_tables[0].find_all('td')
            all_info = all_tds[2].find_all(text=True)

            # this td contains all the venue info, but info is separated by <br> tag
            # findall by text=True will get a list of text that are separated by <br>
            address = all_info[1] + ", " + all_info[3]
    return address


def get_fixtures(data, team, team_id):
    """
    Get the fixtures for a team.
    :param data: json, data used to query fixtures for a team.
    :param team:
    :param team_id:
    :return: my_fixtures: fixtures of a team.
    """
    url = "http://www.qcsa.org.au/Draw/WebsiteComponents/ShowResultsDisplayData.asp"
    my_fixtures = []
    exception_flag = False
    try:
        r = requests.post(url, data=data)
    except Exception as e:
        exception_flag = True
        print(e)

    if (exception_flag == False):
        if (str(r.status_code) == '200'):
            soup = BeautifulSoup(r.content, features="html.parser")
            all_table = soup.find_all('table')
            for indexi, i in enumerate(all_table):
                if indexi == 2:
                    tr_of_table = i.find_all('tr')

                    for indexj, j in enumerate(tr_of_table):
                        if (indexj > 0):  # indexj=0 is the table title
                            td_of_tr = j.find_all('td')
                            fixture_date = format_date(td_of_tr[1].get_text())
                            today = datetime.date.today()  # get today's date
                            if (fixture_date >= today):  # we only focus on matches after today
                                if (td_of_tr[6].get('class') != None):  # td with class label is my team
                                    # if class != none means this tag is our team, other this tag is opsition
                                    fixture_opposition = td_of_tr[8].get_text()  # here we need to find opposition
                                else:
                                    fixture_opposition = td_of_tr[6].get_text()
                                detailed_venue = get_address(td_of_tr[10])
                                my_fixtures.append(Fixture.Fixture(td_of_tr[0].get_text().strip(),
                                                                   datetime.datetime.strftime(fixture_date, "%Y/%m/%d"),
                                                                   td_of_tr[2].get_text(), td_of_tr[10].get_text(),
                                                                   detailed_venue, fixture_opposition, team, team_id))
        else:
            my_fixtures.append(
                Fixture.Fixture('', '', '', 'website server internal error(' + str(r.status_code) + ')',
                                'fail to grab info for this team', '', team, team_id))
    else:
        my_fixtures.append(
            Fixture.Fixture('', '', '', 'website is unreachable', 'fail to grab info for this team', '', team, team_id))
    Fixture.print_fixtures(my_fixtures)
    return my_fixtures
