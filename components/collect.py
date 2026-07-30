from kfp import dsl
from kfp.dsl import Output, Dataset
import pandas as pd


@dsl.component(
    base_image="python:3.11",
    packages_to_install=["pandas==2.2.2"]
)
def collect(output_dataset: Output[Dataset]):
    """
    Collect sample movie user data and save it
    as a Kubeflow Dataset artifact.
    """
    import pandas as pd

    df = pd.DataFrame(
        {
            "age": [20, 22, 35, 40, 29],
            "watch_time": [120, 45, 300, 180, 210],
            "liked_movie": [1, 0, 1, 1, 0]
        }
    )

    df.to_csv(output_dataset.path, index=False)

    print("Dataset saved to:", output_dataset.path)