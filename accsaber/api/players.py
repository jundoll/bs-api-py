
# load modules
import asyncio
import os

import requests
from bs4 import BeautifulSoup

from ..entity import Player

# const
SERVER = 'https://accsaber.com'
if 'USER_AGENT' in os.environ.keys():
    USER_AGENT = os.environ['USER_AGENT'].encode()
else:
    USER_AGENT = ''


# definition
async def get_players(
):
    """
    GET /leaderboards/overall
    """

    # request
    request_url = f'{SERVER}/leaderboards/overall'
    response = requests.get(request_url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.content, "html.parser")
    await asyncio.sleep(1)
    return Player.genList(soup, request_url)


async def get_player(
    # scoresaber ID
    playerId: float
):
    """
    GET /profile/{playerId}/overall/scores
    """

    # request
    request_url = f'{SERVER}/profile/{playerId}/overall/scores'
    response = requests.get(request_url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.content, "html.parser")
    await asyncio.sleep(1)
    return Player.gen(soup)
