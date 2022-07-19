
# load modules
import os

from requests_api import request

from ..entity import Player

# const
SERVER = 'https://api.accsaber.com'
if 'USER_AGENT' in os.environ.keys():
    USER_AGENT = os.environ['USER_AGENT'].encode()
else:
    USER_AGENT = ''


# definition
async def get_players(
):
    """
    GET /players
    """

    # request
    request_url = f'{SERVER}/players'
    response = await request.get(request_url, user_agent=USER_AGENT)
    return Player.genList(response)


async def get_player(
    # scoresaber ID
    playerId: float
):
    """
    GET /players/{playerId}/scores
    """

    # request
    request_url = f'{SERVER}/profile/{playerId}/overall/scores'
    response = await request.get(request_url, user_agent=USER_AGENT)
    return Player.gen(response)
