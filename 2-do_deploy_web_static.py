#!/usr/bin/python3
"""Distributes an Archive to web servers"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['54.90.41.29', '54.88.199.223']


def do_deploy(archive_path):
    """Deploys the archive to the ?tmp/ folder, & uncompresses it"""
    if exists(archive_path) is False:
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except e:
        return False
