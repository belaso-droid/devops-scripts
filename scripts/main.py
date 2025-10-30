import argparse
import os
import sys
from devops_scripts.utils import load_config, get_project_root

def main():
    parser = argparse.ArgumentParser(description='DevOps Scripts')
    parser.add_argument('--config', help='Path to configuration file', default=os.path.join(get_project_root(), 'config.yaml'))
    args = parser.parse_args()

    config = load_config(args.config)

    if not config:
        print('Error: Invalid configuration file')
        sys.exit(1)

    # Example usage: Run a command based on the configuration
    if 'commands' in config:
        for command in config['commands']:
            print(f'Running command: {command["name"]}')
            if 'args' in command:
                print(f'Arguments: {command["args"]}')  # Example usage of command arguments

if __name__ == '__main__':
    main()