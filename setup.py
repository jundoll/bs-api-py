from setuptools import setup

setup(
    name='BSAPI',
    version="0.1.0",
    license='MIT',
    packages=[
        'BSAPI.lib',
        'BSAPI.scoresaber', 'BSAPI.scoresaber.entity'
    ],
    package_dir={
        'BSAPI.lib': 'lib',
        'BSAPI.scoresaber': 'scoresaber/api',
        'BSAPI.scoresaber.entity': 'scoresaber/entity'
    }
)
