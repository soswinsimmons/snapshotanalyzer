from setuptools import setup

setup(
    name='snapshotanalyzer',
    version='0.1',
    author='Sean Simmons',
    description='a tool to manage AWS EC2 instances',
    license='GPLv3',
    packages=['shotty'],
    url='https://github.com/soswinsimmons/snapshotanalyzer',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)
