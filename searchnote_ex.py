from jmcomic import *

client = JmOption.default().new_jm_client()

# 分页查询，search_site就是禁漫网页上的【站内搜索】
page: JmSearchPage = client.search_site(search_query='+MANA +无修正', page=1)
# page默认的迭代方式是page.iter_id_title()，每次迭代返回 albun_id, title
for album_id, title in page:
    print(f'[{album_id}]: {title}')

# 直接搜索禁漫车号
page = client.search_site(search_query='427413')
album: JmAlbumDetail = page.single_album
print(album.tags)