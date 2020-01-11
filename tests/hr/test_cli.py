import pytest

from hr import cli

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_missing_args(parser):
    with pytest.raises(SystemExit):
        """
        The parser will exit if no arguments given
        """
        parser.parse_args([])


def test_parser_if_file_path_given(parser):
    """
    Parse will not exit if file path given
    """
    args = parser.parse_args(["/some/path"])
    assert args.filename == "/some/path"
    

def test_parser_if_export_option_given(parser):
    """
    Parser will give export value of true if given
    """
    args = parser.parse_args(["/some/path", "--export"])
    assert args.export == True

def test_parser_if_export_option_defaults_to_false(parser):
    """
    If no export option given parser will set `export` to False
    """
    args = parser.parse_args(["/some/path",])
    assert args.export == False
