import argparse
import os
import sys
import string
import random

from django.core.management import execute_from_command_line
import django

def createSuperUser(username, email = "", firstName = "", lastName = ""):
    from django.contrib.auth.models import User
    invalidInputs = ["", None]

    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 16))    
    print("LAVA Superuser password is : " + str(password))

    if username.strip() in invalidInputs or password.strip() in invalidInputs:
        return None

    user = User(
        username = username,
        email = email,
        first_name = firstName,
        last_name = lastName,
    )
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

    return user

def main():
    # Is the script called from an installed packages or from a source install?
    installed = not sys.argv[0].endswith("manage.py")

    # Create the command line parser
    parser = argparse.ArgumentParser()
    manage = parser
    if installed:
        subparser = parser.add_subparsers(dest="subcommand", help="Manage LAVA")
        subparser.required = True
        manage = subparser.add_parser("manage")

    #manage.add_argument(
    #    "command", nargs="...", help="Invoke this Django management command"
    #)

    # Parse the command line
    #options = parser.parse_args()

    # Choose the right Django settings
    if installed:
        settings = "lava_server.settings.prod"
    else:
        # Add the root dir to the python path
        find_sources()
        settings = "lava_server.settings.dev"
    os.environ["DJANGO_SETTINGS_MODULE"] = settings
    django.setup()
    createSuperUser("root","test@test.com","","")
    print("Root user created")
main()
