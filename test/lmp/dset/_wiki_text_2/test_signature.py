r"""Test :py:class:`lmp.dset.WikiText2Dset` signature."""

import inspect
from typing import get_type_hints

from lmp.dset import BaseDset, WikiText2Dset


def test_class():
    r"""Ensure class signature."""
    assert inspect.isclass(WikiText2Dset)
    assert not inspect.isabstract(WikiText2Dset)
    assert issubclass(WikiText2Dset, BaseDset)


def test_class_attribute():
    r"""Ensure class attributes' signature."""
    assert get_type_hints(WikiText2Dset) == get_type_hints(BaseDset)
    assert WikiText2Dset.df_ver == 'train'
    assert WikiText2Dset.dset_name == 'wikitext-2'
    assert WikiText2Dset.file_name == 'wiki.{}.tokens.zip'
    assert WikiText2Dset.lang == 'en'
    assert WikiText2Dset.vers == ['test', 'train', 'valid']
    assert WikiText2Dset.url == ''.join([
        'https://github.com/ProFatXuanAll',
        '/demo-dataset/raw/main/wikitext-2',
    ])


def test_inherent_method():
    r'''Ensure inherent methods' signature are the same as base class.'''
    assert WikiText2Dset.__getitem__ == BaseDset.__getitem__
    assert (
        inspect.signature(WikiText2Dset.__init__)
        ==
        inspect.signature(BaseDset.__init__)
    )
    assert WikiText2Dset.__iter__ == BaseDset.__iter__
    assert WikiText2Dset.__len__ == BaseDset.__len__
    assert WikiText2Dset.download == BaseDset.download
