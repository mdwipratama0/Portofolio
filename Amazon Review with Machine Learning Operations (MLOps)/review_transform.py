import string
import tensorflow as tf
import tensorflow_transform as tft

LABEL_KEY = "label"
FEATURE_KEY = "content"


def transformed(key):
    return f"{key}_xf"


def preprocessing_fn(inputs):
    outputs = dict()

    outputs[transformed(FEATURE_KEY)] = tf.strings.lower(
        inputs[FEATURE_KEY]
    )
    outputs[transformed(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
