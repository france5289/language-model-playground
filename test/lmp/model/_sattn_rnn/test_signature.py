r"""Test :py:class:`lmp.model._sattn_rnn` signature."""

import inspect
from inspect import Parameter, Signature
from typing import Dict, Optional

import torch
import torch.nn as nn

from lmp.model import RNNModel, SAttnRNNBlock, SAttnRNNModel
from lmp.tknzr import BaseTknzr


def test_class():
    r"""Ensure class signature."""
    assert inspect.isclass(SAttnRNNBlock)
    assert not inspect.isabstract(SAttnRNNBlock)
    assert issubclass(SAttnRNNBlock, nn.Module)
    assert inspect.isclass(SAttnRNNModel)
    assert not inspect.isabstract(SAttnRNNModel)
    assert issubclass(SAttnRNNModel, RNNModel)


def test_class_attribute():
    r"""Ensure class attributes' signature."""
    assert isinstance(SAttnRNNModel.model_name, str)
    assert SAttnRNNModel.model_name == 'sattn-RNN'
    assert SAttnRNNModel.file_name == 'model-{}.pt'


def test_instance_method():
    r"""Ensure instance methods' signature."""
    assert hasattr(SAttnRNNBlock, '__init__')
    assert inspect.signature(SAttnRNNBlock.__init__) == Signature(
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
    )

    assert hasattr(SAttnRNNBlock, 'forward')
    assert inspect.signature(SAttnRNNBlock.forward) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_tk_mask',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                annotation=torch.Tensor,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_tk_reps',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                annotation=torch.Tensor,
                default=Parameter.empty,
            ),
        ],
        return_annotation=torch.Tensor,

    )

    assert hasattr(SAttnRNNModel, '__init__')
    assert inspect.signature(SAttnRNNModel.__init__) == Signature(
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
    )

    assert hasattr(SAttnRNNModel, 'create_mask')
    assert inspect.signature(SAttnRNNModel.create_mask) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_prev_tkids',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                annotation=torch.Tensor,
                default=Parameter.empty,
            ),
        ],
        return_annotation=torch.Tensor,
    )

    assert hasattr(SAttnRNNModel, 'forward')
    assert inspect.signature(SAttnRNNModel.forward) == Signature(
        parameters=[
            Parameter(
                name='self',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                default=Parameter.empty,
            ),
            Parameter(
                name='batch_prev_tkids',
                kind=Parameter.POSITIONAL_OR_KEYWORD,
                annotation=torch.Tensor,
                default=Parameter.empty,
            ),
        ],
        return_annotation=torch.Tensor,
    )


def test_inherent_method():
    r'''Ensure inherent methods' signature are same as base class.'''
    assert (
        inspect.signature(RNNModel.forward)
        ==
        inspect.signature(SAttnRNNModel.forward)
    )

    assert (
        inspect.signature(RNNModel.load)
        ==
        inspect.signature(SAttnRNNModel.load)
    )

    assert (
        inspect.signature(RNNModel.loss_fn)
        ==
        inspect.signature(SAttnRNNModel.loss_fn)
    )

    assert (
        inspect.signature(RNNModel.pred)
        ==
        inspect.signature(SAttnRNNModel.pred)
    )

    assert (
        inspect.signature(RNNModel.ppl)
        ==
        inspect.signature(SAttnRNNModel.ppl)
    )

    assert (
        inspect.signature(RNNModel.save)
        ==
        inspect.signature(SAttnRNNModel.save)
    )

    assert (
        inspect.signature(RNNModel.train_parser)
        ==
        inspect.signature(SAttnRNNModel.train_parser)
    )
