from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    User Management Utility
    """)
    parser.add_argument('filename', help="Path to JSON to use for User Management Task")
    parser.add_argument('--export', action='store_true', help="Export current settings to inventory file")
    return parser
