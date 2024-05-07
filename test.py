#!/usr/bin/python3
from fabric.api import run, env, local, task, sudo
import os
from datetime import datetime


"""using fabric generate a .tgz archive of the web_static folder"""


@task
def do_test():
    """fab function"""
    env.hosts = ['100.25.143.79', '100.25.222.39']
    for env.host_string in env.hosts:
    	print(run('ls -l'))


do_test()
   
	
