from dataclasses import dataclass
from typing import Literal, TypeAlias


Measurement: TypeAlias = Literal['loss', 'evaluate']
Metric: TypeAlias = Literal['r2', 'mse', 'f1', 'accuracy', 'roc_auc', 'loss']


@dataclass
class PlotParams:
    measurement: Measurement
    dataset_number: int
    model_name = 'AugmentedReLUNetwork'
    metric: Metric
    p: float
    frac: float