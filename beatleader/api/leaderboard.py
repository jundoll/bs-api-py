
# load modules
import os

from requests_api import request

from ..entity import LeaderboardInfoResponseResponseWithMetadata

# const
SERVER = 'https://api.beatleader.xyz'
if 'USER_AGENT' in os.environ.keys():
    USER_AGENT = os.environ['USER_AGENT'].encode()
else:
    USER_AGENT = ''


# definition
async def get_leaderboards(
    # Default value : 1
    page: int = 1,
    # Default value : 10
    count: int = 10,
    #
    sortBy: str = '',
    #
    order: str = '',
    #
    search: str = '',
    #
    type: str = '',
    #
    mode: str = '',
    #
    mapType: int = 0,
    # Available values : 0, 1, 2
    allTypes: int = 0,
    # Available values : 0, 2, 4, 8, 16, 32
    mapRequirements: int = 0,
    # Available values : 0, 1, 2
    allRequirements: int = 0,
    #
    mytype: str = '',
    #
    stars_from: float = 0,
    #
    stars_to: float = 0,
    #
    accrating_from: float = 0,
    #
    accrating_to: float = 0,
    #
    passrating_from: float = 0,
    #
    passrating_to: float = 0,
    #
    techrating_from: float = 0,
    #
    techrating_to: float = 0,
    #
    date_from: int = 0,
    #
    date_to: int = 0
):
    """
    GET /leaderboards
    """

    # prepare query
    query_list = []
    if page > 0:
        query_list.append(f'page={page}')
    if count > 0:
        query_list.append(f'count={count}')
    if sortBy:
        query_list.append(f'sortBy={sortBy}')
    if order:
        query_list.append(f'order={order}')
    if search:
        query_list.append(f'search={search}')
    if type:
        query_list.append(f'type={type}')
    if mode:
        query_list.append(f'mode={mode}')
    if mapType > 0:
        query_list.append(f'mapType={mapType}')
    if allTypes in [0, 1, 2]:
        query_list.append(f'allTypes={allTypes}')
    if mapRequirements in [0, 2, 4, 8, 16, 32]:
        query_list.append(f'mapRequirements={mapRequirements}')
    if allRequirements in [0, 1, 2]:
        query_list.append(f'paallRequirementsge={allRequirements}')
    if mytype:
        query_list.append(f'mytype={mytype}')
    if (stars_from > 0) and (stars_from <= 18):
        query_list.append(f'stars_from={stars_from}')
    if (stars_from <= stars_to) and (stars_to > 0) and (techrating_to <= 18):
        query_list.append(f'stars_to={stars_to}')
    if (accrating_from > 0) and (accrating_from <= 18):
        query_list.append(f'accrating_from={accrating_from}')
    if (accrating_from <= accrating_to) and (accrating_to > 0) and (techrating_to <= 18):
        query_list.append(f'accrating_to={accrating_to}')
    if (passrating_from > 0) and (passrating_from <= 18):
        query_list.append(f'passrating_from={passrating_from}')
    if (passrating_from <= passrating_to) and (passrating_to > 0) and (techrating_to <= 18):
        query_list.append(f'passrating_to={passrating_to}')
    if (techrating_from > 0) and (techrating_from <= 18):
        query_list.append(f'techrating_from={techrating_from}')
    if (techrating_from <= techrating_to) and (techrating_to > 0) and (techrating_to <= 18):
        query_list.append(f'techrating_to={techrating_to}')
    if (date_from > 0):
        query_list.append(f'date_from={date_from}')
    if (date_to > 0):
        query_list.append(f'date_to={date_to}')
    if len(query_list) > 0:
        query = f'?{"&".join(query_list)}'
    else:
        query = ''

    # request
    request_url = f'{SERVER}/leaderboards{query}'
    response = await request.get(request_url, user_agent=USER_AGENT)
    return LeaderboardInfoResponseResponseWithMetadata.gen(response)
