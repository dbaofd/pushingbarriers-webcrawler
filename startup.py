from crawlers import *
from mysqlhelper import MysqlHelper
import datetime
import time



def main():
    blackStoneGameInfo = BlackStoneUnitedDragons.getFixturesFor_U12_d4() + BlackStoneUnitedDragons.getFixturesFor_U14_d2() + \
                         BlackStoneUnitedDragons.getFixturesFor_U16_d1() + BlackStoneUnitedDragons.getFixturesFor_U16girls_d1() + \
                         BlackStoneUnitedDragons.getFixturesFor_U18_d1()
    annerleyGameInfo = AnnerleyFC.getFixturesFor_U11_Liberia() + AnnerleyFC.getFixturesFor_U12_d6() + \
                       AnnerleyFC.getFixturesFor_U13_BYPL() + AnnerleyFC.getFixturesFor_U14_d5()
    westernPrideInfo = WesternPrideFC.getFixturesFor_U16_NPL()
    mtGravattInfo = MtGravattHawksFC.getFixturesFor_U12_d6() + MtGravattHawksFC.getFixturesFor_MensCity_league4()
    westBrisbaneFalconsInfo = WestBrisbaneFalconsBC.getFixturesFor_2019GYL_d2()
    westDistrictInfo = WestDistrictsNA.getFixturesFor_Riverlife_9_d3() + WestDistrictsNA.getFixturesFor_Riverlife_15_d6() + \
                       WestDistrictsNA.getFixturesFor_Riverlife_19_d4()
    allInfo = blackStoneGameInfo + annerleyGameInfo + westernPrideInfo + mtGravattInfo + westBrisbaneFalconsInfo + westDistrictInfo
    db = MysqlHelper.connectdb()
    MysqlHelper.truncatedb(db)
    MysqlHelper.insertdb(db, allInfo)
    MysqlHelper.setUpdateTime(db)
    MysqlHelper.closedb(db)
    # MyLog.Logger('updated-game-schedule.log',level='updated-game-schedule').logger.info("updated-game-schedule");



if __name__ == "__main__":
    main()
