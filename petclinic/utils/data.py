import os.path

import yaml

from petclinic.utils.log import log


class Data:
    @classmethod
    def load_yaml(cls, path):
        root_path = os.path.realpath(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )
        log.debug(root_path)
        yaml_path = os.path.join(root_path, path)
        # log.debug(yaml_path)

        with open(yaml_path) as f:
            env = yaml.safe_load(f)
            # log.debug(env)
            return env


if __name__ == '__main__':
    env1 = Data.load_yaml('data/env.yaml')
    host = env1[env1['default']]
