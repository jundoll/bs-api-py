
# load modules
from requests_api import request

from ..entity import SearchResponse

# const
SERVER = 'https://beatsaver.com/api'


# definition
async def search_maps(
    # Options are a little weird, I may add another enum field in future to make this clearer.
    # true = both, false = only ai, null = no ai
    automapper: bool = False,
    # chroma
    chrome: bool = False,
    # cinema
    cinema: bool = False,
    # curated
    curated: bool = False,
    # Instant
    from_: str = '',
    # fullSpread
    fullSpread: bool = False,
    # Float
    maxBpm: float = 0,
    # maxDuration
    maxDuration: int = 0,
    # Float
    maxNps: float = 0,
    # Float
    maxRating: float = 0,
    # me
    me: bool = False,
    # Float
    minBpm: float = 0,
    # minDuration
    minDuration: int = 0,
    # Float
    minNps: float = 0,
    # Float
    minRating: float = 0,
    # noodle
    noodle: bool = False,
    # page
    page: int = 0,
    # q
    q: str = '',
    # ranked
    ranked: bool = False,
    # sortOrder
    sortOrder: str = '',
    # Comma seperated tags
    tags: str = '',
    # Instant
    to: str = ''
):
    """
    GET /search/text/{page}
    """

    # prepare query
    query_list = []
    if automapper:
        query_list.append(f'automapper={automapper}')
    if chrome:
        query_list.append(f'chrome=true')
    if cinema:
        query_list.append(f'cinema=true')
    if curated:
        query_list.append(f'curated=true')
    if from_:
        query_list.append(f'from={from_}')
    if fullSpread:
        query_list.append(f'fullSpread=true')
    if maxBpm > 0:
        query_list.append(f'maxBpm={maxBpm}')
    if maxDuration > 0:
        query_list.append(f'maxDuration={maxDuration}')
    if maxNps > 0:
        query_list.append(f'maxNps={maxNps}')
    if maxRating > 0:
        query_list.append(f'maxRating={maxRating}')
    if me:
        query_list.append(f'me=true')
    if minBpm > 0:
        query_list.append(f'minBpm={minBpm}')
    if minDuration > 0:
        query_list.append(f'minDuration={minDuration}')
    if minNps > 0:
        query_list.append(f'minNps={minNps}')
    if minRating > 0:
        query_list.append(f'minRating={minRating}')
    if noodle:
        query_list.append(f'noodle=true')
    if q:
        query_list.append(f'q={q}')
    if ranked:
        query_list.append(f'ranked=true')
    if (sortOrder == 'Latest') or (sortOrder == 'Relevance') or (sortOrder == 'Rating'):
        query_list.append(f'sortOrder={sortOrder}')
    if tags:
        query_list.append(f'tags={tags}')
    if to:
        query_list.append(f'to={to}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/search/text/{page}{query}'
    response_dict = await request.get(request_url)
    return SearchResponse.gen(response_dict)
