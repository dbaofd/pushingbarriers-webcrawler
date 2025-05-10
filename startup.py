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
from teams import western_spirit_fc
from teams import westminster_warriors_fc
from teams import blackstone_united_dragons_fc
from teams import ipswich_knights
from teams import oxley_united_fc
from teams import virginia_united
from teams import wynnum_wolves
from teams import north_brisbane_fc
from mysql_helper import mysql_helper
import datetime
import time


def main():
    mt_gravatt_fixtures = mt_gravatt_hawks_fc.get_fixtures_for_u16_mjl() + mt_gravatt_hawks_fc.get_fixtures_for_u18_d3() + \
                          mt_gravatt_hawks_fc.get_fixtures_for_u15_d2_south()
    #brisbane_strikers_fixtures = brisbane_strikers.get_fixtures_for_u16_npl()
    centenary_stormers_fixtures = centenary_stormers_fc.get_fixtures_for_u14_d1_south() + \
                                  centenary_stormers_fc.get_fixtures_for_u15_mjl() + \
                                  centenary_stormers_fc.get_fixtures_for_u18_d1() + \
                                  centenary_stormers_fc.get_fixtures_for_fqpl3_u23() + \
                                  centenary_stormers_fc.get_fixtures_for_u20_metro_men() + \
                                  centenary_stormers_fc.get_fixtures_for_u12_tempest() + \
                                  centenary_stormers_fc.get_fixtures_for_u13_d4_south() + \
                                  centenary_stormers_fc.get_fixtures_for_u13_d2_girls()
    olympic_fc_fixtures = olympic_fc.get_fixtures_for_u15_mjl() + olympic_fc.get_fixtures_for_u14_mjl()
    newmarket_fc_fixtures = newmarket_fc.get_fixtures_for_u14_d1_north()
    virginia_united_fixtures = virginia_united.get_fixtures_for_u15_fqpl()
    wynnum_wolves_fixtures = wynnum_wolves.get_fixtures_for_u14_d1_south()
    north_brisbane_fc_fixtures = north_brisbane_fc.get_fixtures_for_u15_d1_girls()
    annerley_fixtures = annerley_fc.get_fixtures_for_u14_d2()
    # western_pride_fixtures = western_pride_fc.get_fixtures_for_u13_npl()
    # rochedale_rovers_fixtures = rochedale_rovers.get_fixtures_for_u14_bypl()
    # grange_thistle_fixtures = grange_thistle.get_fixtures_for_u14_girls_d1()
    # western_spirit_fixture = western_spirit_fc.get_fixtures_for_u18_d1_silver()
    # westminster_warriors_fixture = westminster_warriors_fc.get_fixtures_for_u1718_d1()
    # blackstone_united_dragons_fc_fixture = blackstone_united_dragons_fc.get_fixtures_for_sm_d3() + \
    #                                        blackstone_united_dragons_fc.get_fixtures_for_u1516b_d2() + \
    #                                        blackstone_united_dragons_fc.get_fixtures_for_u14_d2()
    # ipswich_knights_fixtures = ipswich_knights.get_fixtures_for_u18_d2()
    # oxley_united_fixtures=oxley_united_fc.get_fixtures_for_canale_cup()
    all_info = mt_gravatt_fixtures + \
               centenary_stormers_fixtures + olympic_fc_fixtures + \
               newmarket_fc_fixtures + virginia_united_fixtures + \
               wynnum_wolves_fixtures + north_brisbane_fc_fixtures + annerley_fixtures
    db = mysql_helper.connect_db()
    mysql_helper.truncate_db(db)
    mysql_helper.insert_db(db, all_info)
    mysql_helper.set_update_time(db)
    mysql_helper.close_db(db)

    # MyLog.Logger('updated-game-schedule.log',level='updated-game-schedule').logger.info("updated-game-schedule");


if __name__ == "__main__":
    main()
