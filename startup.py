from teams import blackstone_united_dragons_fc
from teams import oxley_united_fc
from teams import mt_gravatt_hawks_fc
from teams import annerley_fc
from teams import south_united_fc
from teams import centenary_stormers_fc
from teams import ipswich_city_sc
from teams import western_pride_fc
from teams import brisbane_strikers
from teams import olympic_fc
from teams import newmarket_fc
from teams import rochedale_rovers
from teams import grange_thistle
from mysql_helper import mysql_helper
import datetime
import time


def main():
    mt_gravatt_fixtures = mt_gravatt_hawks_fc.get_fixtures_for_u15_d2() + mt_gravatt_hawks_fc.get_fixtures_for_u16_d2()
    annerley_fixtures = annerley_fc.get_fixtures_for_u14_d4()
    brisbane_strikers_fixtures = brisbane_strikers.get_fixtures_for_u15_npl()
    centenary_stormers_fixtures = centenary_stormers_fc.get_fixtures_for_u13_bypl() + centenary_stormers_fc.get_fixtures_for_u14_bypl() + \
                                  centenary_stormers_fc.get_fixtures_for_u16_d4()
    western_pride_fixtures = western_pride_fc.get_fixtures_for_u13_npl()
    olympic_fc_fixtures = olympic_fc.get_fixtures_for_u14_d1()
    newmarket_fc_fixtures = newmarket_fc.get_fixtures_for_u13_d3()
    rochedale_rovers_fixtures = rochedale_rovers.get_fixtures_for_u14_bypl()
    grange_thistle_fixtures = grange_thistle.get_fixtures_for_u14_girls_d1()
    all_info = mt_gravatt_fixtures + annerley_fixtures + brisbane_strikers_fixtures + \
               centenary_stormers_fixtures + western_pride_fixtures + olympic_fc_fixtures + \
               newmarket_fc_fixtures + rochedale_rovers_fixtures + grange_thistle_fixtures
    db = mysql_helper.connect_db()
    mysql_helper.truncate_db(db)
    mysql_helper.insert_db(db, all_info)
    mysql_helper.set_update_time(db)
    mysql_helper.close_db(db)

    # MyLog.Logger('updated-game-schedule.log',level='updated-game-schedule').logger.info("updated-game-schedule");


if __name__ == "__main__":
    main()
