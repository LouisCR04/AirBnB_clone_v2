#!/usr/bin/python3
"""Python script that uses Fabric to pack, upload and deploy a package"""

from os.path import exists, isdir
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['54.90.41.29', '54.88.199.223']


def do_pack():
    """Creates a tar gzipped archive of the directory web_static."""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except e:
        return None


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


def deploy():
    """Calls the archive & deploy functions"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
