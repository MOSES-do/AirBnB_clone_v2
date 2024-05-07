#!/usr/bin/python3
from fabric.api import run, env, local, task, sudo, put
import os
import sys
from datetime import datetime


"""using fabric generate a .tgz archive of the web_static folder"""


@task
def do_deploy(archive_path):
    """fab function"""
    if not os.path.exists(archive_path):
        return False
    env.hosts = ['100.25.143.79', '100.25.222.39']
    for env.host_string in env.hosts:
        try:
            """upload archive to /tmp/ directory on the server"""
            put(archive_path, '/tmp/')

            """remove the '.' extension part of the archive name"""
            release_folder = archive_path.split('.')[0]
            sudo(f"mkdir -p /data/web_static/releases/{release_folder}")
            """Extract archive to the folder /data/web_static/releases"""
            sudo(
                f"tar -xzf /tmp/web_static_20240507065512.tgz "
                f"-C /data/web_static/releases/{release_folder} "
                f"--no-same-owner "
                )
            """Delete archive_path from /tmp/"""
            sudo(f"rm /tmp/web_static_20240507065512.tgz")

            """Delete symbolic link at /data/web_static/current"""
            sudo(f"rm -f /data/web_static/current")

            """create new symbolic link /data/web_static/current"""
            sudo(
                f"ln -sf /data/web_static/releases/{release_folder} "
                f"/data/web_static/current "
                )
            print('New version deployed!')
        except Exception as e:
            print(f"Error: {e}")
            return False
    return True


do_deploy(sys.argv[3])
