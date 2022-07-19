from setuptools import setup

setup(
    name='BSAPI',
    version="0.4.5",
    license='MIT',
    packages=[
        'BSAPI.beatsaver', 'BSAPI.beatsaver.api', 'BSAPI.beatsaver.entity',
        'BSAPI.accsaber', 'BSAPI.accsaber.api', 'BSAPI.accsaber.entity',
        'BSAPI.scoresaber', 'BSAPI.scoresaber.api', 'BSAPI.scoresaber.entity'
    ],
    package_dir={
        'BSAPI.beatsaver': 'beatsaver',
        'BSAPI.beatsaver.api': 'beatsaver/api',
        'BSAPI.beatsaver.entity': 'beatsaver/entity',
        'BSAPI.accsaber': 'accsaber',
        'BSAPI.accsaber.api': 'accsaber/api',
        'BSAPI.accsaber.entity': 'accsaber/entity',
        'BSAPI.scoresaber': 'scoresaber',
        'BSAPI.scoresaber.api': 'scoresaber/api',
        'BSAPI.scoresaber.entity': 'scoresaber/entity'
    },
    install_requires=[
        'requests-api-py@ git+https://github.com/jundoll/requests-api-py.git'
    ]
)
