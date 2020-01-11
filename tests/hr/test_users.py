import pytest
import subprocess


from hr import users

## encrypted version of password for bobby
password = '$6$sNTVN2chgsPs0hEK$jog2VZqccDTP94RuZSbtknMoCGcWhvH5QYhnVkSgCPhKKmWciQQSQHLukSOIsE7AUxqVBn4M8nuiYcUJdyoHi.' 

user_dict = {
    'name': 'bobby',
    'groups': ['wheel', 'dev'],
    'password': password
}

def test_users_add(mocker):
    """
    Given a user dictionary. `users.add(....)` should
    utilize `useradd` to create a user with the password
    and groups.
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        user_dict['password'],
        '-G',
        user_dict['groups'],
        user_dict['name'],
    ])

def test_users_remove(mocker):
    """
    Given a user dictionary, `users.remove(....)` should
    utilize `userdel` to delete the user.
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        user_dict['name'],
    ])

def test_users_update(mocker):
    """
    Given a user dictionary, `users.update(....)` should
    utilize `usermod` to set the groups and the password
    for the user.
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        user_dict['password'],
        '-G',
        user_dict['groups'],
        user_dict['name'],
    ])

def test_users_sync(mocker):
    """
    Given a list of user dictionaries, `users.sync(....)` should
    create missing users, remove extra non-system users, and update
    existing users. A list of existing usernames can be passed in or
    default users will be used.
    """
    existing_user_names = ['cloud_user', 'bob']
    user_info = [
        user_dict,
        {
            'name': 'jose',
            'groups': ['wheel'],
            'password': password
        }
    ]
    mocker.patch('subprocess.call')
    users.sync(user_info, existing_user_names)

    subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            user_dict['password'],
            '-G',
            user_dict['gropus'],
            user_dict['name'],
        ]),
        mocker.call([
            'useradd',
            '-p',
            user_dict['password'],
            '-G',
            user_dict['groups'],
            user_dict['name'],
        ]),
        mocker.call([
            'userdel',
            '-r',
            user_dict['name'],
        ])
    ])
