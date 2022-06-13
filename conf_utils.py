import configparser
from pathlib import Path

import appdirs

APP_NAME = 'FR2pdf'

CONFIG_DIR = appdirs.user_config_dir(APP_NAME)
CONFIG_FILE_NAME = 'config'
CONFIG_FILE_PATH = CONFIG_DIR + '/' + CONFIG_FILE_NAME

STANDARD_DOWNLOAD_PATH = str(Path.home()) + '/FR2pdf_Downloads'

FR_SECTION = 'FR'
FR_LOGIN_USERNAME = 'username'
FR_LOGIN_PASSWORD = 'password'
FR_DOWNLOAD_DIR = 'download_dir'
FR_EDITION = 'edition'

# create config directory if not already existing
if not Path(CONFIG_FILE_PATH).exists():
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)

# load existing config
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)

# add section if not existing
if not config.has_section(FR_SECTION):
    config.add_section(FR_SECTION)


def save_config():
    with open(CONFIG_FILE_PATH, 'w+') as config_file:
        config.write(config_file)


def setup_FR_login():
    config.set(FR_SECTION, FR_LOGIN_USERNAME, '')
    config.set(FR_SECTION, FR_LOGIN_PASSWORD, '')
    save_config()


def setup_download_dir():
    config.set(FR_SECTION, FR_DOWNLOAD_DIR, STANDARD_DOWNLOAD_PATH)
    save_config()


def setup_FR_section():
    config.set(FR_SECTION, FR_EDITION, 'Stadtausgabe')
    save_config()


def get_username():
    if not config.has_option(FR_SECTION, FR_LOGIN_USERNAME):
        setup_FR_login()
    return config.get(FR_SECTION, FR_LOGIN_USERNAME)


def get_password():
    if not config.has_option(FR_SECTION, FR_LOGIN_PASSWORD):
        setup_FR_login()
    return config.get(FR_SECTION, FR_LOGIN_PASSWORD)


def get_download_path():
    if not config.has_option(FR_SECTION, FR_DOWNLOAD_DIR):
        setup_download_dir()
    download_path = config.get(FR_SECTION, FR_DOWNLOAD_DIR)
    Path(download_path).mkdir(parents=True, exist_ok=True)
    return download_path


def get_edition():
    if not config.has_option(FR_SECTION, FR_EDITION):
        setup_FR_section()
    return config.get(FR_SECTION, FR_EDITION)
