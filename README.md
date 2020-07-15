# snapshotanalyzer
Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo and uses boto3 to manage AWS 3C2 instance snapshots

## Configuring

shotty uses the configuration file created by the AWS CLI e.g.


## Running

`pipenv run python3 shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* depends on command
*project* is optional
