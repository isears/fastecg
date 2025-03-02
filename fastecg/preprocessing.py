import torch


class EcgPreprocessor(torch.nn.Module):

    def __init__(self, freq: int):
        super().__init__()

        self.freq = freq

    def forward(self, sig: torch.Tensor) -> torch.Tensor:
        # TODO:
        return sig
