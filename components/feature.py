from kfp import dsl
from kfp.dsl import Input, Output, Dataset
import pandas as pd


@dsl.component(
    base_image="python:3.11",
    packages_to_install=["pandas==2.2.2"]
)
def feature(
    input_dataset: Input[Dataset],
    output_dataset: Output[Dataset]
):
    import pandas as pd

    df = pd.read_csv(input_dataset.path)

    df["engagement"] = df["watch_time"] * df["liked_movie"]

    df.to_csv(output_dataset.path, index=False)

    print("Feature engineered dataset saved:", output_dataset.path)