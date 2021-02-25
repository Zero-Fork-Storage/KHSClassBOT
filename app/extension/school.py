import typing
import neispy
import datetime
from app.config import NEIS_API_KEY
from app.error import NEIS_API_KEY_NOT_FOUND


class NEISClient:
    def __init__(self):
        if not NEIS_API_KEY:
            raise NEIS_API_KEY_NOT_FOUND
        self.neis = neispy.Client(KEY=NEIS_API_KEY)

    async def get_neis_code(self):
        sc_info = await self.neis.schoolInfo(SCHUL_NM="경희고등학교")
        print(sc_info)
        AE: str = sc_info[0]["ATPT_OFCDC_SC_CODE"]
        SE: str = sc_info[0]["SD_SCHUL_CODE"]

        code: typing.List[str, str] = [AE, SE]
        return code

    async def cafeteria(self) -> typing.List[typing.Dict[str, str]]:
        CODE = await self.get_neis_code()
        now = datetime.datetime.now()
        YMD = now.strftime("%Y%m%d")
        _meal = await self.neis.mealServiceDietInfo(CODE[0], CODE[1], MLSV_YMD=YMD)
        da = []
        _da = da.append
        for meal in _meal:
            _da({meal.MMEAL_SC_NM: meal.DDISH_NM.replace("<br/>", "\n")})
        return da
