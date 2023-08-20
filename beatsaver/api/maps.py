
# load modules
import os

from requests_api import request

from ..entity import MapDetail

# const
SERVER = 'https://beatsaver.com/api'
if 'USER_AGENT' in os.environ.keys():
    USER_AGENT = os.environ['USER_AGENT'].encode()
else:
    USER_AGENT = ''


# definition
async def get_map_info_by_hash(
    # Get map(s) for a map hash
    # Up to 50 hashes seperated by commas
    hash: str = '',
):
    """
    GET /maps/hash/{hash}
    """

    # request
    request_url = f'{SERVER}/maps/hash/{hash}'
    response_dict = await request.get(request_url, user_agent=USER_AGENT)
    return MapDetail.gen(response_dict)
