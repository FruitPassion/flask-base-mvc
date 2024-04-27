import sys

from utils.manage_error import ConfigurationError


def check_config(config):
    """
    Check the requested configuration
    :param config: Name of the requested configuration
    :return: True if the configuration is valid
    """
    if config not in ["dev", "prod", "test"]:
        raise ConfigurationError(
            "The configuration requested is not valid (must be dev, prod, test)"
        )
    return True


def read_config(file_name):
    """
    Read the content of a file
    :param file_name: Name of the file to read
    :return: Content of the file
    :exception FileNotFoundError: If the file is not found
    """
    try:
        with open(file_name, "r") as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        print(f"File {file_name} not found")
        sys.exit(1)
