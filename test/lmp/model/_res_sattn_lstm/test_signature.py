r"""Test :py:class:`lmp.model._res_sattn_lstm` signature."""

import inspect
from inspect import Parameter, Signature
from typing import Dict, Optional

from lmp.model._res_sattn_lstm import ResSAttnLSTMBlock, ResSAttnLSTMModel
from lmp.model._res_sattn_rnn import ResSAttnRNNBlock, ResSAttnRNNModel
from lmp.model._sattn_rnn import SAttnRNNBlock
from lmp.tknzr._base import BaseTknzr


def test_class():
    r"""Ensure class signature."""
    assert inspect.isclass(ResSAttnLSTMBlock)
    assert not inspect.isabstract(ResSAttnLSTMBlock)
    assert issubclass(ResSAttnLSTMBlock, ResSAttnRNNBlock)
    assert issubclass(ResSAttnLSTMBlock, SAttnRNNBlock)
    assert inspect.isclass(ResSAttnLSTMModel)
    assert not inspect.isabstract(ResSAttnLSTMModel)
    assert issubclass(ResSAttnLSTMModel, ResSAttnRNNModel)


def test_class_attribute():
    r"""Ensure class attributes' signature."""
    assert isinstance(ResSAttnLSTMModel.model_name, str)
    assert ResSAttnLSTMModel.model_name == 'res-sattn-LSTM'
    assert ResSAttnLSTMModel.file_name == 'model-{}.pt'


def test_instance_method():
    r"""Ensure instance methods' signature."""
    assert hasattr(ResSAttnLSTMBlock, '__init__')
    assert inspect.signature(ResSAttnLSTMBlock.__init__) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='d_hid',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='n_hid_lyr',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='p_hid',
                kind=Parameter.KEYWORD_ONLY,
                annotation=float,
                default=Parameter.empty,
            ),
            Parameter(
                name='kwargs',
                kind=Parameter.VAR_KEYWORD,
                annotation=Optional[Dict],
            ),
        ],
        return_annotation=Signature.empty,
    )

    assert hasattr(ResSAttnLSTMModel, '__init__')
    assert inspect.signature(ResSAttnLSTMModel.__init__) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='d_emb',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='d_hid',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='n_hid_lyr',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='n_post_hid_lyr',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='n_pre_hid_lyr',
                kind=Parameter.KEYWORD_ONLY,
                annotation=int,
                default=Parameter.empty,
            ),
            Parameter(
                name='p_emb',
                kind=Parameter.KEYWORD_ONLY,
                annotation=float,
                default=Parameter.empty,
            ),
            Parameter(
                name='p_hid',
                kind=Parameter.KEYWORD_ONLY,
                annotation=float,
                default=Parameter.empty,
            ),
            Parameter(
                name='tknzr',
                kind=Parameter.KEYWORD_ONLY,
                annotation=BaseTknzr,
                default=Parameter.empty,
            ),
            Parameter(
                name='kwargs',
                kind=Parameter.VAR_KEYWORD,
                annotation=Optional[Dict],
            ),
        ],
        return_annotation=Signature.empty,
    )


def test_inherent_method():
    r'''Ensure inherent methods' signature are same as base class.'''
    assert (
        inspect.signature(ResSAttnRNNModel.forward)
        ==
        inspect.signature(ResSAttnLSTMModel.forward)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.load)
        ==
        inspect.signature(ResSAttnLSTMModel.load)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.loss_fn)
        ==
        inspect.signature(ResSAttnLSTMModel.loss_fn)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.pred)
        ==
        inspect.signature(ResSAttnLSTMModel.pred)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.ppl)
        ==
        inspect.signature(ResSAttnLSTMModel.ppl)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.save)
        ==
        inspect.signature(ResSAttnLSTMModel.save)
    )

    assert (
        inspect.signature(ResSAttnRNNModel.train_parser)
        ==
        inspect.signature(ResSAttnLSTMModel.train_parser)
    )
