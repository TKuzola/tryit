'''
Created on Mar 12, 2018

@author: Tony Kuzola
'''
import configparser
import json
import xml.dom.minidom
import yaml
from bs4 import BeautifulSoup


def sample_configs():
    '''
    Main routine to demonstrate different configuration file use

    Reads configuration files and prints out some parameters
    '''
    # INI file example
    config = configparser.ConfigParser()
    config.read('config.ini')

    secret_key = config['DEFAULT']['SECRET_KEY']  # 'secret-key-of-myapp'
    ci_hook_url = config['CI']['HOOK_URL']  # 'web-hooking-url-from-ci-service'

    print(secret_key)
    print(ci_hook_url)
    print(config)

    # JSON example
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

        secret_key = config['DEFAULT']['SECRET_KEY']  # 'secret-key-of-myapp'
        ci_hook_url = config['CI']['HOOK_URL']  # 'web-hooking-url-from-ci-service'

        print(secret_key)
        print(ci_hook_url)
        print(config)

    # YAML example
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    for section in cfg:
        print(section)
    print(cfg['mysql'])
    print(cfg['other'])

    # XML example with BeautifulSoup
    with open("config.xml") as xml_file:
        content = xml_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    print(soup.mysql.host.contents[0])
    for tag in soup.other.preprocessing_queue:
        print(tag)

    # Native XML example
    dom1 = xml.dom.minidom.parse('backupSpec.xml')

    directories = dom1.getElementsByTagName('directory')
    for directory in directories:
        source_dir_path = ''
        target_dir_path = ''

        source_dirs = directory.getElementsByTagName("source")
        for source_dir in source_dirs:
            source_dir_path = source_dir.firstChild.data
            print(source_dir_path)
        target_dirs = directory.getElementsByTagName("target")
        for target_dir in target_dirs:
            target_dir_path = target_dir.firstChild.data
            print(target_dir_path)


if __name__ == '__main__':
    sample_configs()
