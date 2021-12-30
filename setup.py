from setuptools import setup

setup(
    name='BSAPI',
    version="0.1.0",
    license='MIT',
    packages=['BSAPI', 'BSAPI.scoresaber'],
    package_dir={'BSAPI': '', 'BSAPI.scoresaber': 'scoresaber/api'}
)
