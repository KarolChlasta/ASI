from typing import Any

from pydantic import BaseModel


class Parameters:
    def __init__(self):
        self.learning_rate: float = 0.001
        self.num_epochs: float = 10
        self.batch_size: float = 64
        self.dropout_rate: float = 0.5


class WebParameters(BaseModel):
    learning_rate: float = None
    num_epochs: float = None
    batch_size: float = None
    dropout_rate: float = None
