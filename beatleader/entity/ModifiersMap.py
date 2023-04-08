
# load modules
from dataclasses import dataclass


# definition class
@dataclass(frozen=True)
class ModifiersMap:
    da: float
    fs: float
    sf: float
    ss: float
    gn: float
    na: float
    nb: float
    nf: float
    no: float
    pm: float
    sc: float
    sa: float
    op: float


# definition function
def gen(response):
    instance = ModifiersMap(
        da=response.get('da'),
        fs=response.get('fs'),
        sf=response.get('sf'),
        ss=response.get('ss'),
        gn=response.get('gn'),
        na=response.get('na'),
        nb=response.get('nb'),
        nf=response.get('nf'),
        no=response.get('no'),
        pm=response.get('pm'),
        sc=response.get('sc'),
        sa=response.get('sa'),
        op=response.get('op')
    )
    return instance


def gen_list(response):
    if response is not None:
        if len(response) == 0:
            return []
        else:
            return [gen(v) for v in response]
