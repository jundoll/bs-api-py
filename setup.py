from setuptools import setup

setup(
    name='BSAPI',
    version="0.2.1",
    license='MIT',
    packages=[
        'BSAPI.accsaber', 'BSAPI.accsaber.api', 'BSAPI.accsaber.entity',
        'BSAPI.scoresaber', 'BSAPI.scoresaber.api', 'BSAPI.scoresaber.entity'
    ],
    package_dir={
        'BSAPI.accsaber': 'accsaber',
        'BSAPI.accsaber.api': 'accsaber/api',
        'BSAPI.accsaber.entity': 'accsaber/entity',
        'BSAPI.scoresaber': 'scoresaber',
        'BSAPI.scoresaber.api': 'scoresaber/api',
        'BSAPI.scoresaber.entity': 'scoresaber/entity'
    }
)
