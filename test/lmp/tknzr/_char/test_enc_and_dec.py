r"""Test token encoding and decoding.

Test target:
- :py:meth:`lmp.tknzr.CharTknzr.dec`.
- :py:meth:`lmp.tknzr.CharTknzr.enc`.
"""

from typing import List

import pytest

from lmp.tknzr import CharTknzr


@pytest.mark.parametrize(
    'parameters,test_input,expected',
    [
        # Test subject:
        # Empty input.
        #
        # Expectation:
        # Return only `[bos]` and `[eos]`.
        (
            {
                'is_uncased': True,
                'max_seq_len': -1,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                },
            },
            '',
            [CharTknzr.bos_tkid, CharTknzr.eos_tkid],
        ),
        # Test subject:
        # Encoding format.
        #
        # Expectation:
        # Add `[bos]` token at the front and `[eos]` at the end of token
        # sequence.
        # Output token ids instead of tokens.
        (
            {
                'is_uncased': True,
                'max_seq_len': -1,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                    'b': 5,
                    'c': 6,
                },
            },
            'abc',
            [CharTknzr.bos_tkid, 4, 5, 6, CharTknzr.eos_tkid],
        ),
        # Test subject:
        # Case sensitive.
        #
        # Expectation:
        # Treat cases differently when `is_uncased == False`
        (
            {
                'is_uncased': False,
                'max_seq_len': -1,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                    'A': 5,
                },
            },
            'aAa',
            [CharTknzr.bos_tkid, 4, 5, 4, CharTknzr.eos_tkid],
        ),
        # Test subject:
        # Truncate sequence when sequence length is larger than `max_seq_len`.
        #
        # Expectation:
        # Output sequence length equals to `max_seq_len`.
        (
            {
                'is_uncased': True,
                'max_seq_len': 4,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            'aaa',
            [CharTknzr.bos_tkid, 4, 4, 4],
        ),
        # Test subject:
        # Pad sequence when sequence length is less than `max_seq_len`.
        #
        # Expectation:
        # Output sequence length equals to `max_seq_len`.
        (
            {
                'is_uncased': True,
                'max_seq_len': 6,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            'aaa',
            [
                CharTknzr.bos_tkid,
                4, 4, 4,
                CharTknzr.eos_tkid,
                CharTknzr.pad_tkid,
            ],
        ),
        # Test subject:
        # Encounter unknown tokens.
        #
        # Expectation:
        # Replace unknown tokens with unknown token id.
        (
            {
                'is_uncased': True,
                'max_seq_len': -1,
                'max_vocab': -1,
                'min_count': 1,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            'abab',
            [
                CharTknzr.bos_tkid,
                4,
                CharTknzr.unk_tkid,
                4,
                CharTknzr.unk_tkid,
                CharTknzr.eos_tkid,
            ],
        ),
    ],
)
def test_enc(parameters, test_input: str, expected: List[int]):
    r"""Encode text to token ids."""

    tknzr = CharTknzr(
        is_uncased=parameters['is_uncased'],
        max_vocab=parameters['max_vocab'],
        min_count=parameters['min_count'],
        tk2id=parameters['tk2id'],
    )

    out = tknzr.enc(test_input, max_seq_len=parameters['max_seq_len'])

    assert out == expected

    if parameters['max_seq_len'] != -1:
        assert len(out) == parameters['max_seq_len']


@pytest.mark.parametrize(
    'parameters,test_input,expected',
    [
        # Test subject:
        # Empty input.
        #
        # Expectation:
        # Return empty string.
        (
            {
                'is_uncased': True,
                'max_vocab': -1,
                'min_count': 1,
                'rm_sp_tks': True,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                },
            },
            [],
            '',
        ),
        # Test subject:
        # Decoding format.
        #
        # Expectation:
        # Output text with special tokens.
        (
            {
                'is_uncased': True,
                'max_vocab': -1,
                'min_count': 1,
                'rm_sp_tks': False,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            [
                CharTknzr.bos_tkid,
                4,
                CharTknzr.unk_tkid,
                CharTknzr.eos_tkid,
                CharTknzr.pad_tkid,
            ],
            '{}a{}{}{}'.format(
                CharTknzr.bos_tk,
                CharTknzr.unk_tk,
                CharTknzr.eos_tk,
                CharTknzr.pad_tk,
            ),
        ),
        # Test subject:
        # Remove special tokens but not unknown tokens.
        #
        # Expectation:
        # Unknown tokens must be reserved.
        (
            {
                'is_uncased': True,
                'max_vocab': -1,
                'min_count': 1,
                'rm_sp_tks': True,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            [
                CharTknzr.bos_tkid,
                4,
                CharTknzr.unk_tkid,
                CharTknzr.eos_tkid,
                CharTknzr.pad_tkid,
            ],
            f'a{CharTknzr.unk_tk}',
        ),
        # Test subject:
        # Encounter unknown token ids.
        #
        # Expectation:
        # Replace unknown token ids with unknown tokens.
        (
            {
                'is_uncased': True,
                'max_vocab': -1,
                'min_count': 1,
                'rm_sp_tks': True,
                'tk2id': {
                    CharTknzr.bos_tk: CharTknzr.bos_tkid,
                    CharTknzr.eos_tk: CharTknzr.eos_tkid,
                    CharTknzr.pad_tk: CharTknzr.pad_tkid,
                    CharTknzr.unk_tk: CharTknzr.unk_tkid,
                    'a': 4,
                },
            },
            [
                CharTknzr.bos_tkid,
                4,
                5,
                CharTknzr.eos_tkid,
            ],
            f'a{CharTknzr.unk_tk}',
        ),
    ],
)
def test_dec(parameters, test_input: List[int], expected: str):
    r"""Decode token ids to text."""

    tknzr = CharTknzr(
        is_uncased=parameters['is_uncased'],
        max_vocab=parameters['max_vocab'],
        min_count=parameters['min_count'],
        tk2id=parameters['tk2id'],
    )

    assert (
        tknzr.dec(test_input, rm_sp_tks=parameters['rm_sp_tks'])
        ==
        expected
    )
