from kfp import dsl
from kfp.dsl import Input, Output, Dataset, Model, Metrics
import pandas as pd
import joblib

from sklearn.metrics import accuracy_score


@dsl.component(
    base_image="python:3.11",
    packages_to_install=[
        "pandas==2.2.2",
        "scikit-learn==1.5.1",
        "joblib==1.4.2"
    ]
)
def evaluate(
    input_dataset: Input[Dataset],
    input_model: Input[Model],
    metrics: Output[Metrics]
):
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score

    df = pd.read_csv(input_dataset.path)

    X = df[["age", "watch_time", "engagement"]]
    y = df["liked_movie"]

    model = joblib.load(input_model.path)

    predictions = model.predict(X)

    accuracy = accuracy_score(y, predictions)

    metrics.log_metric("accuracy", float(accuracy))

    print("Accuracy:", accuracy)