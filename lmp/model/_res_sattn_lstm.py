r"""Residual connected LSTM language model with self attention mechanism."""

from typing import ClassVar, Dict, Optional

import torch.nn as nn

from lmp.model._res_sattn_rnn import ResSAttnRNNBlock, ResSAttnRNNModel
from lmp.model._sattn_rnn import SAttnRNNBlock
from lmp.tknzr._base import BaseTknzr


class ResSAttnLSTMBlock(ResSAttnRNNBlock, SAttnRNNBlock):
    r"""Residual connected LSTM block with self attention mechanism.

    Same architecture as :py:class:`lmp.model.ResSAttnRNNBlock` but replace RNN
    with LSTM instead.

    Parameters
    ==========
    d_hid: int
        Hidden dimension for LSTM and self attention linear transformation
        weights (including query, key, value and output).
        Must be bigger than or equal to ``1``.
    kwargs: Dict, optional
        Useless parameter.
        Intently left for subclass parameters extension.
    n_hid_lyr: int
        Number of residual connected self attention LSTM layers.
        Must be bigger than or equal to ``1``.
    p_hid: float
        Dropout probability for every hidden representations.
        Must satisfy ``0.0 <= p_hid <= 1.0``.
    """

    def __init__(
            self,
            *,
            d_hid: int,
            n_hid_lyr: int,
            p_hid: float,
            **kwargs: Optional[Dict],
    ):
        super().__init__(
            d_hid=d_hid,
            n_hid_lyr=n_hid_lyr,
            p_hid=p_hid,
            **kwargs,
        )

        # Override RNN layer with LSTM.
        # Input tensor : Output of `ResSAttnLSTMModel.pre_hid`.
        # Input shape  : `(B, S, H)`.
        # Input dtype  : `torch.float32`.
        # Output tensor: Batch of recurrent token hidden states.
        # Output shape : `(B, S, H)`.
        # Output dtype : `torch.float32`.
        self.recur = nn.ModuleList([
            nn.LSTM(input_size=d_hid, hidden_size=d_hid, batch_first=True)
            for _ in range(n_hid_lyr)
        ])


class ResSAttnLSTMModel(ResSAttnRNNModel):
    r"""Residual connected LSTM language model with self attention mechanism.

    Same architecture as :py:class:`lmp.model.ResSAttnRNNModel` but replace
    residual connected self attention RNN with residual connected self
    attention LSTM instead.

    Parameters
    ==========
    d_emb: int
        Token embedding dimension.
        Must be bigger than or equal to ``1``.
    d_hid: int
        Hidden dimension for Feed-Forward layers and residual connected self
        attention LSTM layers.
        Must be bigger than or equal to ``1``.
    kwargs: Dict, optional
        Useless parameter.
        Intently left for subclass parameters extension.
    n_hid_lyr: int
        Number of residual connected self attention LSTM layers.
        Must be bigger than or equal to ``1``.
    n_post_hid_lyr: int
        Number of Feed-Forward layers after residual connected self attention
        LSTM layers.
        All layers are paired with ReLU activatons except for the last one.
        Must be bigger than or equal to ``1``.
    n_pre_hid_lyr: int
        Number of Feed-Forward layers before residual connected self attention
        LSTM layers.
        All layers are paired with ReLU activatons.
        Must be bigger than or equal to ``1``.
    p_emb: float
        Dropout probability for token embeddings.
        Must satisfy ``0.0 <= p_emb <= 1.0``.
    p_hid: float
        Dropout probability for every hidden representations.
        Must satisfy ``0.0 <= p_hid <= 1.0``.
    tknzr: lmp.tknzr.BaseTknzr
        Tokenizer instance with attributes ``pad_tkid`` and ``vocab_size``.

    Attributes
    ==========
    hid: lmp.model.SAttnLSTMBlock
        Self attention LSTM with residual connection which encode temporal
        features.
        Each time step's hidden state depends on current input and previous
        hidden state.
        Drop temporal features with probability ``p_hid``.
    model_name: ClassVar[str]
        Model name is ``res-sattn-LSTM``.
        Used for command line argument parsing.
    """
    model_name: ClassVar[str] = 'res-sattn-LSTM'

    def __init__(
            self,
            *,
            d_emb: int,
            d_hid: int,
            n_hid_lyr: int,
            n_post_hid_lyr: int,
            n_pre_hid_lyr: int,
            p_emb: float,
            p_hid: float,
            tknzr: BaseTknzr,
            **kwargs: Optional[Dict],
    ):
        super().__init__(
            d_emb=d_emb,
            d_hid=d_hid,
            n_hid_lyr=n_hid_lyr,
            n_post_hid_lyr=n_post_hid_lyr,
            n_pre_hid_lyr=n_pre_hid_lyr,
            p_emb=p_emb,
            p_hid=p_hid,
            tknzr=tknzr,
            **kwargs,
        )

        # Override residual connected self attention RNN layer with residual
        # connected self attention LSTM.
        # Input tensor : Output of `self.pre_hid`.
        # Input shape  : `(B, S, H)`.
        # Input dtype  : `torch.float32`.
        # Output tensor: Batch of recurrent token hidden states.
        # Output shape : `(B, S, H)`.
        # Output dtype : `torch.float32`.
        self.hid = ResSAttnLSTMBlock(
            d_hid=d_hid,
            n_hid_lyr=n_hid_lyr,
            p_hid=p_hid,
            **kwargs,
        )
