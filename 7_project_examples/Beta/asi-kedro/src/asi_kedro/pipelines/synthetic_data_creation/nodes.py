"""
This is a boilerplate pipeline 'synthetic_data_creation'
generated using Kedro 0.18.14
"""
import pandas as pd
from typing import Tuple
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

def create_synth_data(og_data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(og_data)
    
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(og_data)

    synth_data = synthesizer.sample(num_rows=3000)
    concat_data = pd.concat([og_data, synth_data])
    return synth_data, concat_data