import subprocess


def checking():
    """
    Allows you to check if the requirements are up to
    date and update them if necessary
    """
    try:
        subprocess.run(["poetry", "install"])
    except Exception as e:
        print("Error:", e)
