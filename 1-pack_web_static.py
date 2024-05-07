#!/usr/bin/python3
from fabric.api import run, env, local, task
import os
from datetime import datetime
"""using fabric generate a .tgz archive of the web_static folder"""


@task
def do_pack():
    """fab function"""
    #hosts = ['ubuntu@100.25.143.79', 'ubuntu@100.25.222.39']
    #for env.host_string in hosts:
    #    print(env.host_string)
    #    run("whoami")
    #    run('ls -l')
    try:
        source_dir = 'web_static'
        destination_dir = 'versions'
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Archive file name
        arch_filename = f'web_static_{timestamp}.tgz'

        os.makedirs(destination_dir, exist_ok=True)

        local(f"tar -cvzf {destination_dir}/{arch_filename} -C {source_dir} .")

        print(f"Packing {source_dir} to {destination_dir}/{arch_filename}")

        return os.path.join(destination_dir, arch_filename)
    except Exception as e:
        print(f"Error: {e}")

        return None

do_pack()
    
