import os
from absl import logging
from typing import Text
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner
from tfx.orchestration import metadata, pipeline

PIPELINE_NAME = 'pipeline-anemia'

DATA_ROOT = 'data'
TRANSFORM_MODULE_FILE = 'transform.py'
TRAINER_MODULE_FILE = 'trainer.py'

OUTPUT_BASE = 'outputs'
serving_model_dir = os.path.join(OUTPUT_BASE, 'serving_model')
pipeline_root = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
metadata_path = os.path.join(pipeline_root, 'metadata.sqlite')


def initialize_local_pipeline(components, pipeline_root: Text) -> pipeline.Pipeline:

    logging.info(f'Pipeline root set to: {pipeline_root}')
    beam_args = [
        '--direct_running_mode=multi_processing'
        # 0 auto-detect based on the number of CPUs available
        # duraing execution time
        '----direct_num_workers=0'
    ]

    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            metadata_path
        ),
        eam_pipeline_args=beam_args
    )


if __name__ == '__main__':
    logging.set_verbosity(logging.INFO)

    from modules.components import initialize_components
    components = initialize_components(
        DATA_ROOT,
        training_module=TRAINER_MODULE_FILE,
        transform_module=TRANSFORM_MODULE_FILE,
        training_steps=64,
        eval_steps=64,
        serving_model_dir=serving_model_dir,
    )

    section = initiialize_local_pipeline(components, pipeline_root)
    BeamDagRunner().run(pipeline = section)