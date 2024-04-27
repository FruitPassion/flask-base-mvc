import base64
import hashlib

import bcrypt
from configparser_crypt import ConfigParserCrypt


def encrypt_password(password, salt=13):
    """
    Encrypts a password using bcrypt and a salt
    :param password: The password to encrypt
    :param salt: The salt to use, default is 13
    :return: The encrypted password
    """
    return bcrypt.hashpw(get_b64(password), bcrypt.gensalt(salt))


def compare_passwords(new_passw, old_passwd):
    """
    Compares a new password with an old one
    :param new_passw: The new password
    :param old_passwd: The old password
    :return: True if the passwords match, False otherwise
    """
    if isinstance(old_passwd, str):
        old_passwd = bytes(old_passwd, "utf-8")
    return bcrypt.checkpw(get_b64(str(new_passw)), old_passwd)


def get_b64(password):
    """
    Returns the base64 encoding of a password
    :param password: The password to encode
    :return: The base64 encoding of the password
    """
    return base64.b64encode(hashlib.sha256(password.encode("utf_8")).digest())


def generate_key():
    """
    Generates a key and saves it in a file
    """
    conf_file = ConfigParserCrypt()
    conf_file.generate_key()
    aes_key = conf_file.aes_key
    out_file = open("key.encrypt", "wb")
    out_file.write(aes_key)
    out_file.close()


def encrypt_file(db_password):
    """
    Encrypts a file with a password
    :param db_password: The password to encrypt
    """
    conf_file = ConfigParserCrypt()
    in_file = open("key.encrypt", "rb")
    key = in_file.read()
    in_file.close()
    conf_file.aes_key = key

    conf_file.add_section("DBS")
    conf_file["DBS"]["db_password"] = db_password

    with open("dbs.encrypted", "wb") as file_handle:
        conf_file.write_encrypted(file_handle)
