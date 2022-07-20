from setuptools import setup

setup(
    name='BSAPI',
    version="0.5.0",
    license='MIT',
    packages=[
        'BSAPI.accsaber', 'BSAPI.accsaber.api', 'BSAPI.accsaber.entity',
        'BSAPI.beatleader', 'BSAPI.beatleader.api', 'BSAPI.beatleader.entity',
        'BSAPI.beatsaver', 'BSAPI.beatsaver.api', 'BSAPI.beatsaver.entity',
        'BSAPI.scoresaber', 'BSAPI.scoresaber.api', 'BSAPI.scoresaber.entity'
    ],
    package_dir={
        'BSAPI.accsaber': 'accsaber',
        'BSAPI.accsaber.api': 'accsaber/api',
        'BSAPI.accsaber.entity': 'accsaber/entity',
        'BSAPI.beatleader': 'beatleader',
        'BSAPI.beatleader.api': 'beatleader/api',
        'BSAPI.beatleader.entity': 'beatleader/entity',
        'BSAPI.beatsaver': 'beatsaver',
        'BSAPI.beatsaver.api': 'beatsaver/api',
        'BSAPI.beatsaver.entity': 'beatsaver/entity',
        'BSAPI.scoresaber': 'scoresaber',
        'BSAPI.scoresaber.api': 'scoresaber/api',
        'BSAPI.scoresaber.entity': 'scoresaber/entity'
    },
    install_requires=[
        'requests-api-py@ git+https://github.com/jundoll/requests-api-py.git'
    ]
)
