from qutils import ROOT_DIR, __version__


def test_version():
    assert __version__ == '0.1.0'


def test_root_dir():
    print(ROOT_DIR)
