r"""Test :py:class:`lmp.tknzr.BaseTknzr` signature."""

import argparse
import inspect
from inspect import Parameter, Signature
from typing import ClassVar, Dict, List, Optional, Sequence, get_type_hints

from lmp.tknzr import BaseTknzr


def test_class():
    r"""Ensure abstract class signature.

    Subclass only need to implement method tknzr and dtknzr.
    """
    assert inspect.isclass(BaseTknzr)
    assert inspect.isabstract(BaseTknzr)


def test_class_attribute():
    r"""Ensure class attributes' signature."""
    assert get_type_hints(BaseTknzr) == {
        'bos_tk': ClassVar[str],
        'bos_tkid': ClassVar[int],
        'eos_tk': ClassVar[str],
        'eos_tkid': ClassVar[int],
        'file_name': ClassVar[str],
        'pad_tk': ClassVar[str],
        'pad_tkid': ClassVar[int],
        'tknzr_name': ClassVar[str],
        'unk_tk': ClassVar[str],
        'unk_tkid': ClassVar[int],
    }
    assert BaseTknzr.bos_tk == '[bos]'
    assert BaseTknzr.bos_tkid == 0
    assert BaseTknzr.eos_tk == '[eos]'
    assert BaseTknzr.eos_tkid == 1
    assert BaseTknzr.file_name == 'tknzr.json'
    assert BaseTknzr.pad_tk == '[pad]'
    assert BaseTknzr.pad_tkid == 2
    assert BaseTknzr.tknzr_name == 'base'
    assert BaseTknzr.unk_tk == '[unk]'
    assert BaseTknzr.unk_tkid == 3


def test_class_method():
    r"""Ensure class methods' signature."""
    assert hasattr(BaseTknzr, 'load')
    assert inspect.ismethod(BaseTknzr.load)
    assert BaseTknzr.load.__self__ == BaseTknzr
    assert inspect.signature(BaseTknzr.load) == Signature(
        parameters=[
            Parameter(
                name='exp_name',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=str,
            ),
        ]
    )


def test_instance_method():
    r"""Ensure instance methods' signature."""
    assert hasattr(BaseTknzr, '__init__')
    assert inspect.isfunction(BaseTknzr.__init__)
    assert inspect.signature(BaseTknzr.__init__) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='is_uncased',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=bool,
            ),
            Parameter(
                name='max_vocab',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=int,
            ),
            Parameter(
                name='min_count',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=int,
            ),
            Parameter(
                name='tk2id',
                kind=Parameter.KEYWORD_ONLY,
                default=None,
                annotation=Optional[Dict[str, int]],
            ),
            Parameter(
                name='kwargs',
                kind=Parameter.VAR_KEYWORD,
                annotation=Optional[Dict],
            ),
        ],
        return_annotation=Signature.empty,
    )
    assert hasattr(BaseTknzr, 'batch_enc')
    assert inspect.isfunction(BaseTknzr.batch_enc)
    assert inspect.signature(BaseTknzr.batch_enc) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_txt',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=Sequence[str],
            ),
            Parameter(
                name='max_seq_len',
                kind=Parameter.KEYWORD_ONLY,
                default=-1,
                annotation=int,
            ),
        ],
        return_annotation=List[List[int]],
    )
    assert hasattr(BaseTknzr, 'batch_dec')
    assert inspect.isfunction(BaseTknzr.batch_dec)
    assert inspect.signature(BaseTknzr.batch_dec) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_tkids',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=Sequence[Sequence[int]],
            ),
            Parameter(
                name='rm_sp_tks',
                kind=Parameter.KEYWORD_ONLY,
                default=False,
                annotation=bool,
            ),
        ],
        return_annotation=List[str],
    )

    assert hasattr(BaseTknzr, 'build_vocab')
    assert inspect.isfunction(BaseTknzr.build_vocab)
    assert inspect.signature(BaseTknzr.build_vocab) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_txt',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=Sequence[str],
            ),
        ],
        return_annotation=None,
    )

    assert hasattr(BaseTknzr, 'dec')
    assert inspect.isfunction(BaseTknzr.dec)
    assert inspect.signature(BaseTknzr.dec) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='tkids',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=Sequence[int],
            ),
            Parameter(
                name='rm_sp_tks',
                kind=Parameter.KEYWORD_ONLY,
                default=False,
                annotation=Optional[bool],
            ),
        ],
        return_annotation=str,
    )

    assert hasattr(BaseTknzr, 'dtknz')
    assert inspect.isfunction(BaseTknzr.dtknz)
    assert inspect.signature(BaseTknzr.dtknz) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='tks',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=Sequence[str],
            ),
        ],
        return_annotation=str,
    )

    assert hasattr(BaseTknzr, 'enc')
    assert inspect.isfunction(BaseTknzr.enc)
    assert inspect.signature(BaseTknzr.enc) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='txt',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=str,
            ),
            Parameter(
                name='max_seq_len',
                kind=Parameter.KEYWORD_ONLY,
                default=-1,
                annotation=Optional[int],
            ),
        ],
        return_annotation=List[int],
    )

    assert hasattr(BaseTknzr, 'norm')
    assert inspect.isfunction(BaseTknzr.norm)
    assert inspect.signature(BaseTknzr.norm) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='txt',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=str,
            ),
        ],
        return_annotation=str,
    )

    assert hasattr(BaseTknzr, 'save')
    assert inspect.isfunction(BaseTknzr.save)
    assert inspect.signature(BaseTknzr.save) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='exp_name',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=str,
            ),
        ],
        return_annotation=None,
    )

    assert hasattr(BaseTknzr, 'tknz')
    assert inspect.isfunction(BaseTknzr.tknz)
    assert inspect.signature(BaseTknzr.tknz) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='txt',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=str,
            ),
        ],
        return_annotation=List[str],
    )


def test_abstract_method():
    r"""Ensure abstract method's signature."""
    assert 'dtknz' in BaseTknzr.__abstractmethods__
    assert 'tknz' in BaseTknzr.__abstractmethods__


def test_static_method():
    r"""Ensure static methods' signature."""
    assert hasattr(BaseTknzr, 'train_parser')
    assert inspect.isfunction(BaseTknzr.train_parser)
    assert inspect.signature(BaseTknzr.train_parser) == Signature(
        parameters=[
            Parameter(
                name='parser',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
                annotation=argparse.ArgumentParser,
            ),
        ],
        return_annotation=None,
    )
