
from dfmapper import DataFrameMapper, DataFrameColumn

class UserDfm(DataFrameMapper):

    user_id = DataFrameColumn(int)
    username = DataFrameColumn(str)
    articles = DataFrameColumn(list)

user_dfm = UserDfm()


class ArticleDfm(DataFrameMapper):

    pass

article_dfm = ArticleDfm()

article_dfm = ArticleDfm({
    'aritcle_id': [11, 12, 13],
    'title': ['A', 'B', 'C']
})
