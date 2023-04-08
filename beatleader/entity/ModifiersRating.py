
# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class ModifiersRating:
    id: int
    fsPredictedAcc: float
    fsPassRating: float
    fsAccRating: float
    fsTechRatinggn: float
    fsStars: float
    ssPredictedAcc: float
    ssPassRating: float
    ssAccRating: float
    ssTechRating: float
    ssStars: float
    sfPredictedAcc: float
    sfPassRating: float
    sfAccRating: float
    sfTechRating: float
    sfStars: float


# definition function
def gen(response):
    instance = ModifiersRating(
        id=response.get('id'),
        fsPredictedAcc=response.get('fsPredictedAcc'),
        fsPassRating=response.get('fsPassRating'),
        fsAccRating=response.get('fsAccRating'),
        fsTechRatinggn=response.get('fsTechRatinggn'),
        fsStars=response.get('fsStars'),
        ssPredictedAcc=response.get('ssPredictedAcc'),
        ssPassRating=response.get('ssPassRating'),
        ssAccRating=response.get('ssAccRating'),
        ssTechRating=response.get('ssTechRating'),
        ssStars=response.get('ssStars'),
        sfPredictedAcc=response.get('sfPredictedAcc'),
        sfPassRating=response.get('sfPassRating'),
        sfAccRating=response.get('sfAccRating'),
        sfTechRating=response.get('sfTechRating'),
        sfStars=response.get('sfStars')
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
