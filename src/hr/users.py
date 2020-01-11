import pwd
import subprocess
import sys

def add(user_info):
    print(f"Adding user '{user_info['name']}'")
    try:
        subprocess.call([
            'useradd',
            '-p',
            user_info['password'],
            '-G',
            user_info['groups'],
            user_info['name'],
        ])
    except:
        print(f"Failed to add user '{user_info['name']}'")
        sys.exit(1)

def remove(user_info):
    print(f"Removing user '{user_info['name']}'")
    try:
        subprocess.call([
            'userdel',
            '-r',
            user_info['name'],
        ])
    except:
        print(f"Failed to remove user '{user_info['name']}'")
        sys.exit(1)

def update(user_info):
    print(f"Updating user '{user_info['name']}'")
    try:
        subprocess.call([
            'usermod',
            '-p',
            user_info['password'],
            '-G',
            user_info['groups'],
            user_info['name'],
        ])
    except:
        print(f"Failed to update user '{user_info['name']}'")
        sys.exit(1)

def sync(user_info, existing_users):
    pass
