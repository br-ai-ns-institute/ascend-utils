"""Quick intro for TF on Ascend platform."""

import os
import tensorflow as tf
from npu_bridge.estimator.npu.keras_to_npu import model_to_npu_estimator
from npu_bridge.estimator.npu.npu_config import NPURunConfig

# ======================== COMMON TF CODE (not Ascend specific) =======================

# Prepare data (same as in TF quickstart)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create model (same as in TF quickstart)
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

# ======================== ASCEND SPECIFIC =============================================

# The following section is specific for Ascend platform and deals with the
# conversion of a standard Keras model to a NPUEstimator, which can be
# trained on Ascend devices.

# First set the environment variables for Ascend device to 0. This is necessary
# for the correct functioning of the ascend device. It can also be done from a
# starting bash script, or from a JSON table file. This is the simplest example
# that uses only python, and a single Ascend device.
os.environ["ASCEND_DEVICE_ID"] = "0"
os.environ["JOB_ID"] = "10385"

session_config = tf.ConfigProto()
# The configuration has to use the NPURunConfig class in order to work correctly with
# the Ascend devices. The model directory has to be created manually.
run_config = NPURunConfig(session_config=session_config, model_dir="./model")

# Convert the model built by using Keras to an NPUEstimator object.
# This is the main step in converting from Keras to NPUEstimator.
estimator = model_to_npu_estimator(keras_model=model, config=run_config)


def input_fn(features, labels, batch_size):
    """returns tf.data.Dataset created from tensor slices.

    This function is necessary for the correct functioning of the NPUEstimator
    model, and is used to define its inputs for training and evaluation.
    """
    # convert input to a Dataset
    dataset = tf.data.Dataset.from_tensor_slices((features, labels))
    # shuffle, repeat and batch
    return dataset.shuffle(1000).repeat().batch(batch_size, drop_remainder=True)


# ======================== TRAIN AND EVALUATE ==========================================

print("=================== STARTING TRAINING =========================================")
batch_size = 128
estimator.train(input_fn=lambda: input_fn(x_train, y_train, batch_size), steps=1000)

print("=================== STARTING EVALUATION =======================================")
evaluations = estimator.evaluate(
    input_fn=lambda: input_fn(x_test, y_test, batch_size), steps=1000
)
print("=================== TESTING ACCURACY ==========================================")
print(f"Testing Accuracy: {evaluations['acc']}")
