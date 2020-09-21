from teams import blackstone_united_dragons_fc
from teams import oxley_united_fc
from teams import mt_gravatt_hawks_fc
from teams import annerley_fc
from teams import south_united_fc
from teams import centenary_stormers_fc
from teams import ipswich_city_sc
from teams import western_pride_fc
from mysql_helper import mysql_helper
import datetime
import time


def main():
    blackstone_fixtures = blackstone_united_dragons_fc.get_fixtures_for_u18_d1() + blackstone_united_dragons_fc.get_fixtures_for_u1516b_d2() + \
                          blackstone_united_dragons_fc.get_fixtures_for_u14_d1() + blackstone_united_dragons_fc.get_fixtures_for_u12_d2() + \
                          blackstone_united_dragons_fc.get_fixtures_for_sm_d4()
    oxley_united_fixtures = oxley_united_fc.get_fixtures_for_u18_d2_silver()
    mt_gravatt_fixtures = mt_gravatt_hawks_fc.get_fixtures_for_u15_d2() + mt_gravatt_hawks_fc.get_fixtures_for_u14_d3_sth() + \
                          mt_gravatt_hawks_fc.get_fixtures_for_mens_city7_gold()
    annerley_fixtures = annerley_fc.get_fixtures_for_u13_d5_sth()
    south_united_fixtures = south_united_fc.get_fixtures_for_u14_d1()
    centenary_stormers_fixtures = centenary_stormers_fc.get_fixtures_for_u16_d3()
    ipswich_city_fixtures = ipswich_city_sc.get_fixtures_for_u18_women()
    western_pride_fixtures = western_pride_fc.get_fixtures_for_u12_d1_sth()
    all_info = blackstone_fixtures + oxley_united_fixtures + mt_gravatt_fixtures + \
               annerley_fixtures + south_united_fixtures + centenary_stormers_fixtures + \
               ipswich_city_fixtures + western_pride_fixtures
    db = mysql_helper.connect_db()
    mysql_helper.truncate_db(db)
    mysql_helper.insert_db(db, all_info)
    mysql_helper.set_update_time(db)
    mysql_helper.close_db(db)

    # MyLog.Logger('updated-game-schedule.log',level='updated-game-schedule').logger.info("updated-game-schedule");


if __name__ == "__main__":
    main()
