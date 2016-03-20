import io, os
import json, time
import click
import subprocess
from app.github import github
from app.server import server

config_path = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.json'
repository = json.loads(io.open(config_path, 'r').read())
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
BITGO_PATH = repository['bitgo_path']

@click.command()
@click.option('--issue', '-i', default=False)
@click.option('--description', '-d', default=False)
@click.option('--init', is_flag=True, default=False)
def cli(issue, description, init):
    try:
        BITGO_PATH
    except:
        return print('Please ensure that BitGo Express is installed and that its path is set in config/config.js')

    try:
        ACCESS_TOKEN
    except:
        return print('Please set your BitGo access token before continuing')
    try:
        GITHUB_TOKEN
    except:
        return print('Please set your GitHub access token before continuing')
    
    if (init):
        os.system(BITGO_PATH + '/bin/bitgo-express --debug --port 3080 --env prod --bind localhost &')
        server.run()
        return time.sleep(10)
    return github.create_issue(issue, description)


