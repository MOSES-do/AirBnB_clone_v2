#!/usr/bin/env python3
import tarfile

# Open the .tgz file
with tarfile.open('versions/web_static_20240507065512.tgz', 'r') as tar:
    # List the contents of the tarball
    for member in tar.getmembers():
        print(member.name)

