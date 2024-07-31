from bilibili_api import article, sync


async def main():
    # 创建专栏类
    ar = article.Article(7309319)
    # 如果专栏为公开笔记，则转换为笔记类
    # NOTE: 笔记类的函数与专栏类的函数基本一致
    if ar.is_note():
        ar = ar.turn_to_note()
    # 加载内容
    await ar.fetch_content()
    # 写入 markdown
    with open('article.md', 'w', encoding='utf8') as f:
        f.write(ar.markdown())


sync(main())