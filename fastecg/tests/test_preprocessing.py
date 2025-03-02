import pytest
import torch
from typing import Literal
from importlib.resources import files
from fastecg.preprocessing import EcgPreprocessor
import numpy as np
import neurokit2 as nk


@pytest.fixture(params=[100, 500])
def sample_raw_ecg(request) -> tuple[torch.Tensor, int]:
    freq = request.param

    test_batch = torch.stack(
        [
            torch.load(files(f"fastecg.tests.data.{freq}hz") / f"sig{idx}.pt")
            for idx in range(0, 10)
        ]
    )

    return test_batch, freq


def test_preprocessing(sample_raw_ecg):
    sig_in, freq = sample_raw_ecg
    preprocessor = EcgPreprocessor(freq=freq)

    sig_out = preprocessor(sig_in)

    nk_cleaned = torch.stack(
        [
            np.apply_along_axis(nk.ecg_clean, 1, sig_in[idx], sampling_rate=freq)
            for idx in range(0, sig_in.shape[0])
        ]
    )

    assert sig_out.shape == nk_cleaned.shape
