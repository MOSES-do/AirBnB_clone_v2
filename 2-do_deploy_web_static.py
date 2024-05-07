#!/usr/bin/python3
from fabric.api import env, sudo, put
import os
from datetime import datetime
env.user = 'ubuntu'
env.hosts = ['100.25.143.79', '100.25.222.39']

"""using fabric to distribute files to web servers"""


def do_deploy(archive_path):
    """using fabric to distribute files"""
    if not os.path.exists(archive_path):
        return False
    """for env.host_string in env.hosts:"""
    try:
        """upload archive to /tmp/ directory on the server"""
        put(archive_path, '/tmp/')

        """remove the '.' extension part of the archive name"""
        release_folder = archive_path.split('.')[0]
        """remove the 'versions/' from archive_path"""
        web_tgz = archive_path.split('/')[-1]

        sudo(f"mkdir -p /data/web_static/releases/{release_folder}")
        """Extract archive to the folder /data/web_static/releases"""
        sudo(
            f"tar -xzf /tmp/{web_tgz} "
            f"-C /data/web_static/releases/{release_folder} "
            f"--no-same-owner "
            )
        """Delete archive_path from /tmp/"""
        sudo(f"rm /tmp/{web_tgz}")

        """Delete symbolic link at /data/web_static/current"""
        sudo(f"rm -f /data/web_static/current")

        """create new symbolic link /data/web_static/current"""
        sudo(
            f"ln -sf /data/web_static/releases/{release_folder} "
            f"/data/web_static/current "
            )
	# Recursively assign ownership of data to user running script.
        sudo(f"chown -R ubuntu:ubuntu /data/")
        print('New version deployed!')
        return True
    except:
        return False
