from teams import blackstone_united_dragons_fc
from mysql_helper import mysql_helper
import datetime
import time


def main():
    blackstone_fixtures = blackstone_united_dragons_fc.get_fixtures_for_u18_d1() + blackstone_united_dragons_fc.get_fixtures_for_u1516b_d2() + \
                         blackstone_united_dragons_fc.get_fixtures_for_u14_d1() + blackstone_united_dragons_fc.get_fixtures_for_u12_d2() + \
                         blackstone_united_dragons_fc.get_fixtures_for_sm_d4()
    # annerleyGameInfo = AnnerleyFC.getFixturesFor_U11_Liberia() + AnnerleyFC.getFixturesFor_U12_d6() + \
    #                    AnnerleyFC.getFixturesFor_U13_BYPL() + AnnerleyFC.getFixturesFor_U14_d5()
    # westernPrideInfo = WesternPrideFC.getFixturesFor_U18_NPL()
    # mtGravattInfo = MtGravattHawksFC.getFixturesFor_U12_d6() + MtGravattHawksFC.getFixturesFor_MensCity_league4()
    # westBrisbaneFalconsInfo = WestBrisbaneFalconsBC.getFixturesFor_2019GYL_d2()
    #westDistrictInfo = WestDistrictsNA.getFixturesFor_Riverlife_9_d3() + WestDistrictsNA.getFixturesFor_Riverlife_15_d6() + \
                       #WestDistrictsNA.getFixturesFor_Riverlife_19_d4()
    allInfo = blackstone_fixtures
    db = mysql_helper.connect_db()
    mysql_helper.truncate_db(db)
    mysql_helper.insert_db(db, allInfo)
    mysql_helper.set_update_time(db)
    mysql_helper.close_db(db)

    # MyLog.Logger('updated-game-schedule.log',level='updated-game-schedule').logger.info("updated-game-schedule");



if __name__ == "__main__":
    main()
