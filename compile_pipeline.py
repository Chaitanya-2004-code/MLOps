from kfp.compiler import Compiler

from pipeline import movie_ai_pipeline


Compiler().compile(
    pipeline_func=movie_ai_pipeline,
    package_path="movie_ai_pipeline.yaml"
)

print("Pipeline compiled successfully.")