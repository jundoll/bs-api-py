# bs-api-py

## How to
### Install
```console
$ pip install git+https://github.com/jundoll/bs-api-py.git
```

### Use (sample)
#### beatsaver
```python
coming soon
```

<!-- 
import BSAPI.beatsaver as beatsaver
import asyncio
-->

#### scoresaber
```python
import BSAPI.scoresaber as scoresaber
import asyncio

# get a result of request 'https://scoresaber.com/api/players'
player_list = asyncio.run(scoresaber.get_players())
```

#### accsaber
```python
import BSAPI.accsaber as accsaber
import asyncio

# get a result of request 'https://api.accsaber.com/players'
player_list = asyncio.run(accsaber.get_players())
```

## Reference
### BeatSaver API docs
https://api.beatsaver.com/docs/

### ScoreSaber API docs
https://docs.scoresaber.com/

<!--
### AccSaber github account
https://github.com/accsaber
-->