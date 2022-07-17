
# load modules
import requests
from bs4 import BeautifulSoup

from ...common import USER_AGENT
from ..entity import Player

# const
SERVER = 'https://accsaber.com'


# definition
def get_players(
):
    """
    GET /leaderboards/overall
    """

    # request
    request_url = f'{SERVER}/leaderboards/overall'
    response = requests.get(request_url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.content, "html.parser")
    return Player.genList(soup, request_url)


def get_player(
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
    return Player.gen(soup)
