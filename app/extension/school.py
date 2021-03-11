import datetime
import typing
from collections import defaultdict, namedtuple
from typing import Dict, List, Optional, Type

import aiocache
import neispy
from aiocache.base import SENTINEL

from app.config import NEIS_API_KEY, REDIS_PORT
from app.error import NEIS_API_KEY_NOT_FOUND
from app.extension.redis import REDIS_CLIENT


class NEISClient:
    def __init__(self):
        self.rc = REDIS_CLIENT(host="redis", port=REDIS_PORT)
        if not NEIS_API_KEY:
            raise NEIS_API_KEY_NOT_FOUND
        self.neis = neispy.Client(KEY=NEIS_API_KEY)

    async def get_neis_code(self):
        sc_info = await self.neis.schoolInfo(SCHUL_NM="경희고등학교")
        AE: str = sc_info[0]["ATPT_OFCDC_SC_CODE"]
        SE: str = sc_info[0]["SD_SCHUL_CODE"]
        code: typing.List[str, str] = [AE, SE]
        return code

    async def cafeteria(self) -> typing.List[typing.Dict[str, str]]:
        # ca = await self.rc.cache.get(key="cafeteria")
        # if ca is not None:
        #     return ca
        # else:
        CODE = await self.get_neis_code()
        KST = datetime.timezone(datetime.timedelta(hours=9))
        now = datetime.datetime.now(tz=KST)
        YMD = now.strftime("%Y%m%d")
        _meal = await self.neis.mealServiceDietInfo(CODE[0], CODE[1], MLSV_YMD=YMD)
        da = []
        _da = da.append
        for meal in _meal:
            _da({meal.MMEAL_SC_NM: meal.DDISH_NM.replace("<br/>", "\n")})
        # await self.rc.cache.set(key="cafeteria", value=da, ttl=1800)
        return da

