#!/usr/bin/python3
from fabric.api import env, sudo, put, task
import os
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.user = 'ubuntu'
env.hosts = ['100.25.143.79', '100.25.222.39']


"""using fabric to distribute files to web servers"""


@task
def deploy():
    """using fabric to distribute files"""
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    dev_deploy = do_deploy(archive_path)
    return dev_deploy
