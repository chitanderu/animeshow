from bilibili_api import bangumi, sync
from bilibili_api.bangumi import IndexFilter as IF
async def main():
    filters = bangumi.IndexFilterMeta.Anime(area=IF.Area.JAPAN,
        year=IF.make_time_filter(start=2022, end=2023, include_end=True),
        season=IF.Season.SPRING,
        style=IF.Style.Anime.NOVEL)
    index = await bangumi.get_index_info(filters=filters, order=IF.Order.SCORE, sort=IF.Sort.DESC, pn=2, ps=20)
    #print(index)

    list_items = index['list'] #获得该年份的所有番剧list

    for item in list_items:
     print(item)


sync(main())