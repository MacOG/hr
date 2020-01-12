import os
import sys

from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    User Management Utility
    """)
    parser.add_argument('filename', help="Path to JSON to use for User Management Task")
    parser.add_argument('--export', action='store_true', help="Export current settings to inventory file")
    return parser

def main():
    from hr import inventory, users

    args = create_parser().parse_args()
    if os.getuid() == 0:
        if args.export:
            inventory.dump(args.filename)
        else:
            users_info = inventory.load(args.filename)
            users.sync(users_info)
    else:
        if args.export == True:
            print(f"Must be run as root! Try using:\n `sudo hr --export {args.filename}")
            return sys.exit(1)
        else:
            print(f"Must be run as root! Try using:\n `sudo hr {args.filename}")
