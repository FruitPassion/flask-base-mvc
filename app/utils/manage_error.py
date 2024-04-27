import logging
import sys


def logging_erreur(e, message="Exception occurred : "):
    """
    Log an error message and the exception that caused it
    :param e: The exception that caused the error
    :param message: The message to log
    """
    f = open("logs/error.log", "r")
    ligne_depart = len(f.readlines()) + 1
    logging.exception(message + str(e))
    ligne_fin = ligne_depart + (len(f.readlines()) - 1)
    f.close()
    f = open("logs/error.log", "r")
    mess = ""
    for i, line in enumerate(f):
        if "^^^^^" in line.strip():
            continue
        if ligne_depart <= i <= ligne_fin:
            mess = mess + line.strip() + "<br>"
    f.close()
    return mess


def more_error(e, message="Exception occurred : "):
    """
    Log an error message and the exception that caused it
    :param e: The exception that caused the error
    :param message: The message to log
    """
    logging.error(message)

    e_type, _, e_traceback = sys.exc_info()

    e_message = str(e)
    e_line_number = e_traceback.tb_lineno

    logging.error(e_type)
    logging.error(e_message)
    logging.error(
        e_traceback.tb_frame.f_code.co_filename + " line : " + str(e_line_number)
    )


class ProjectError(Exception):
    pass


class ConfigurationError(ProjectError):
    pass


class LogOpeningError(ProjectError):
    pass
