from setuptools import setup, find_packages

setup(
    name='bs_scoresaber_api',
    version="1.0.0",
    license='MIT',
    packages=['scoresaber_api'],#, 'scoresaber_api.entity'],
    package_dir={'scoresaber_api': 'scoresaber/api'}#,'scoresaber_api.entity': 'scoresaber/entity'}
)

