from setuptools import setup, find_packages

setup(
    name='BSAPI',
    version="1.0.0",
    license='MIT',
    packages=['BSAPI.scoresaber'],
    package_dir={'BSAPI.scoresaber': 'scoresaber/api'}
)
