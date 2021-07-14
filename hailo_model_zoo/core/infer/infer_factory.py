"""Contains a factory for network infer."""
from hailo_model_zoo.core.infer.tf_infer import tf_infer
from hailo_model_zoo.core.infer.np_infer import np_infer
from hailo_model_zoo.core.infer.face_infer import facenet_infer
from hailo_model_zoo.core.infer.tf_infer_second_stage import tf_infer_second_stage

NAME_TO_INFER = {
    'tf_infer': tf_infer,
    'np_infer': np_infer,
    'facenet_infer': facenet_infer,
    'tf_infer_second_stage': tf_infer_second_stage,
}


def get_infer(infer_type):
    """ Returns infer_fn(endnodes, **kwargs)
        Args:
            name: The name of the task.
        Returns:
            infer_fn: A function that postprocesses a batch.

        Raises:
            ValueError: If infer `name` is not recognized.
    """

    if infer_type not in NAME_TO_INFER:
        raise ValueError('infer key [%s] was not recognized' % infer_type)

    return NAME_TO_INFER[infer_type]
