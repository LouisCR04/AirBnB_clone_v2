#!/usr/bin/env bash
# Generates a tgz archive from contents of web_static dir

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a tgz archive from contents of web_static directory"""

    d_time = datetime.utcnow()

    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(d_time.year,
                                                         d_time.month
                                                         d_time.day
                                                         d_time.hour
                                                         d_time.minute
                                                         d_time.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
