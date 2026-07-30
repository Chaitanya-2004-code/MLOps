from kfp import dsl

from components.collect import collect
from components.clean import clean
from components.feature import feature
from components.train import train
from components.evaluate import evaluate
from components.deploy import deploy


@dsl.pipeline(
    name="movie-ai-pipeline",
    description="End-to-End Movie Recommendation MLOps Pipeline"
)
def movie_ai_pipeline():

    # Step 1
    collect_task = collect()

    # Step 2
    clean_task = clean(
        input_dataset=collect_task.outputs["output_dataset"]
    )

    # Step 3
    feature_task = feature(
        input_dataset=clean_task.outputs["output_dataset"]
    )

    # Step 4
    train_task = train(
        input_dataset=feature_task.outputs["output_dataset"]
    )

    # Step 5
    evaluate_task = evaluate(
        input_dataset=feature_task.outputs["output_dataset"],
        input_model=train_task.outputs["output_model"]
    )

    # Step 6
    deploy(
        input_model=train_task.outputs["output_model"]
    ).after(evaluate_task)