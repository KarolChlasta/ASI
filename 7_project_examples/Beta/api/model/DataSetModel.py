from typing import Optional
from pydantic import BaseModel


class KedroDataSet(BaseModel):
    ph: Optional[float]
    Hardness: Optional[float]
    Solids: Optional[float]
    Chloramines: Optional[float]
    Sulfate: Optional[float]
    Conductivity: Optional[float]
    Organic_carbon: Optional[float]
    Trihalomethanes: Optional[float]
    Turbidity: Optional[float]
    Potability: Optional[int]