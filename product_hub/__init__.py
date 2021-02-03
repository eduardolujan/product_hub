import os
import sys
import pathlib

import environ


def get_project_path():
    """
    Get project path
    @return: current path
    @rtype: str
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path


def get_env():
    current_path = get_project_path()
    project_path = pathlib.Path(current_path).parent
    env_path = os.path.join(project_path, '.env')
    env = environ.Env()
    if os.path.exists(env_path):
        env.read_env(env_path)
    return env

