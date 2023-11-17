from bilibili_api import bangumi, sync
from bilibili_api.bangumi import IndexFilter as IF
async def main():
    filters = bangumi.IndexFilterMeta.Anime(area=IF.Area.JAPAN,
        year=IF.make_time_filter(start=2019, end=2022, include_end=True),
        season=IF.Season.SPRING,
        style=IF.Style.Anime.NOVEL)
    index = await bangumi.get_index_info(filters=filters, order=IF.Order.SCORE, sort=IF.Sort.DESC, pn=2, ps=20)
    print(index)

sync(main())