from .lib import docker
import os
import click
from configparser import ConfigParser


@click.group()
def cli():
    click.echo('> ' * 6 + 'start pesi')


@click.command()
@click.option('--path', '-p', default=os.getcwd(), help='path of project,default where you type pesi')
@click.option('--conn', default=None, help='specify other docker remote api,default none,'
                                           'use setup.cfg.docker_remote_api')
@click.option('--pull', type=bool, default=True, help='allow pull image,default true')
@click.option('--rm', type=bool, default=True, help='')
@click.option('--nocache', type=bool, default=False, help='not use cache,default true')
def build(path, conn, pull, rm, nocache):
    """
    1.read setup.cfg\n
    2.connect docker rmote api\n
    3.build docker image on remote docker server\n
    """
    _init(path=path)
    _build(path=path, conn=conn, pull=pull, rm=rm, nocache=nocache)


def _build(path, conn, pull, rm, nocache):
    click.echo('> ' * 6 + 'build docker image')
    click.echo('> ' * 6 + 'project path: ' + path)
    config = ConfigParser()
    cfg_path = os.path.join(path, 'setup.cfg')
    config.read(cfg_path)

    docker_path = os.path.join(path, 'deploy')
    docker_file_path = os.path.join(docker_path, 'Dockerfile')

    if not os.path.exists(docker_file_path):
        click.echo('> ' * 6 + 'Dockerfile not found')
        raise EOFError

    project_name = config.get('metadata', 'name')
    project_version = config.get('metadata', 'version')

    docker_remote_api = conn if conn else config.get('docker', 'docker_remote_api')

    try:
        client = docker.DockerClient(docker_remote_api)
    except Exception as e:
        print(type(docker_remote_api), docker_remote_api)
        click.echo('> ' * 6 + 'docker client connection error')
        click.echo(e)
        return

    tag = '{}:{}'.format(project_name, project_version)
    try:
        res = client.images.build(path=docker_path, pull=pull, rm=rm, nocache=nocache, tag=tag)
    except Exception as e:
        print(type(tag), tag)
        click.echo('> ' * 6 + 'docker build image error')
        click.echo(e)

        return

    click.echo(res)
    click.echo('> ' * 6 + 'build docker image done')


# @click.command()
# @click.option('--path', '-p', default=os.getcwd(), help='path of project dir')
# @click.option('--bdist_wheel', is_flag=True, help='create wheel file')
# @click.option('--down_reqs', is_flag=True, help='download requirements package from requirements.txt')
def _init(path, bdist_wheel=None, down_reqs=None):
    """
    1. init project requirements, cp project to deploy dir
    2. (option) create wheel file
    2. (option) pip download libraries required from setup.py or requirements.txt
    3. cp requirements and wheel file to deploy
    :return:
    """
    click.echo('> ' * 6 + 'init project')
    click.echo('> ' * 6 + 'project path: ' + path)

    deploy_path = os.path.join(path, 'deploy')

    if not os.path.exists(deploy_path):
        click.echo('> ' * 6 + 'deploy dir not found')
        raise EOFError

    if bdist_wheel:
        click.echo('> ' * 6 + 'creating wheel')
        os.system('rm -rf build/ dist/ *egg-info/ deploy/dist/ ')
        os.system('python setup.py bdist_wheel')
        os.system('mv dist/ deploy/')

    config = ConfigParser()
    cfg_path = os.path.join(path, 'setup.cfg')
    config.read(cfg_path)
    project_name = config.get('metadata', 'name')

    os.system('rm -rf {}'.format(os.path.join(path, 'deploy/app')))
    os.system('cp -r {} {}'.format(os.path.join(path, project_name), os.path.join(path, 'deploy/app')))

    if down_reqs:
        click.echo('> ' * 6 + 'getting dependencies')
        os.system('cd deploy && rm -rf requirements/ && mkdir requirements && cd requirements '
                  '&& pip download -r ../requirements.txt')

    click.echo('> ' * 6 + 'init project done')


cli.add_command(build)

if __name__ == '__main__':
    cli()
