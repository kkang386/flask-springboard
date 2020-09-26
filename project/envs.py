import sys, inspect

class Envs():
    envs = {}

    def __init__(self, conf_module):
        for name, obj in inspect.getmembers(sys.modules[conf_module]):
            if inspect.isclass(obj) and obj.ENV_NAME:
                self.envs[obj.ENV_NAME] = conf_module + "." + name

    def get_env(self, env_name):
        if env_name in self.envs.keys():
            return self.envs[env_name]
        else:
            raise Exception("Invalid environment name: '" + env_name + "'")

"""
a = Envs()
print (a.get_env('config')) # loads config classes in the config.py
"""
