import json
from bilibili_api import user, sync

# 实例化
u = user.User(5947893)


async def main():
    print(sync(u.get_relation_info())["follower"])

# 入口
sync(main())