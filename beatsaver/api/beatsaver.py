
# load modules
import json
from urllib import error

from attrdict import AttrDict

from . import api, scoresaber


# definition
class BeatSaver:

    songHash = None
    diff = None

    def get_songMetaInfoFromLeaderboardID(self, leaderboardID):
        ss = scoresaber.ScoreSaber()
        songHash, diff = ss.leaderboardID2songHashAndDiff(leaderboardID)
        self.songHash = songHash
        self.diff = str.lower(diff).replace('+', 'Plus')
        return (self.songHash, self.diff)

    async def fetch_songInfo(self, songHash):
        url = f'https://beatsaver.com/api/maps/by-hash/{songHash}'
        try:
            response = await api.fetch_page(url)
        except error.HTTPError as e:
            if e.code == 404:
                return None
            else:
                raise e
        responseJson = AttrDict(json.load(response))
        return responseJson
