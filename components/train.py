from kfp import dsl
from kfp.dsl import Input, Output, Dataset, Model

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


@dsl.component(
    base_image="python:3.11",
    packages_to_install=[
        "pandas==2.2.2",
        "scikit-learn==1.5.1",
        "joblib==1.4.2"
    ]
)
def train(
    input_dataset: Input[Dataset],
    output_model: Output[Model]
):
    import pandas as pd
    import joblib
    from sklearn.ensemble import RandomForestClassifier

    df = pd.read_csv(input_dataset.path)

    X = df[["age", "watch_time", "engagement"]]
    y = df["liked_movie"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, output_model.path)

    print("Model saved:", output_model.path)