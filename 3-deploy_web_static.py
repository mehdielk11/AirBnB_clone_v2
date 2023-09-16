#!/usr/bin/python3
"""
    Script generates a .tgz archive from web_static folder and
    distributes archive to web servers
"""
from fabric.operations import local, run, put, env


env.hosts = ['34.224.71.206', '54.174.221.228']
env.user = 'ubuntu'


def do_pack():
    """
        Function creates a .tgz archive from all files in web_static folder

        Each archive will be stored in versions folder

        Archive name:
            web_static_<year><month><day><hour><minute><second>.tgz

        Returns:
            archive path if successful
            None if fail
    """
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """
        Function distributes an archive to web servers

        Returns:
            True if operations succeed
            False if archive_path doesn't exist or fail
    """
    import os

    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    filename = archive_path[11:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename
    if not run('mkdir -p {}'.format(foldername)).succeeded:
        return False
    if not run('tar -xzf {} -C {}'.format(filename, foldername)).succeeded:
        return False
    if not run('rm {}'.format(filename)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(foldername,
                                              foldername)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(foldername)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        foldername)).succeeded


def deploy():
    """
        Function packs and deploys an archive
    """
    an = do_pack()
    if an is False:
        return False
    return do_deploy(an)


if __name__ == "__main__":
    deploy()
