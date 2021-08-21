r"""Test the downloaded file

Test target:
- :py:meth:`lmp.tknzr._ch_poem.ChPoemDset.download`.
"""
import os

from lmp.dset._ch_poem import ChPoemDset
from lmp import path


def test_dset_file_exist(dset_ver, download_dset, cleandir):
    r"""Dataset must be downloaded to right places"""

    file_path = os.path.join(path.DATA_PATH, download_dset.file_name.format(dset_ver))

    assert os.path.exists(path.DATA_PATH)
    assert os.path.exists(file_path)

