# TensorFlow quickstart on Ascend (using NPUEstimator conversion)

The file `ascend_quickstart.py` aims to make a parallel between the standard TF quickstart
and the Ascned platform, with the least amound of customization necessary. It does so by
utilizing the guidlines on [this page](https://support.huawei.com/enterprise/en/doc/EDOC1100155039/8cc4626a/keras-to-npuestimator-conversion). This is to some degree common with what most people
are presented with on the Huawei `taining_handson` seminar (in the example with the same name.

The main idea is to create a standard Keras model and then converting to a `NPUEstimator` model,
that can run on ascend devices natively. The code should be self explanatory, with a lot of
comments sprinkled throughout.

## running the example
It's best to run the example by using the `Makefile` utility and a Docker container. Clone the
repository and navigate to the `ascend-utils` folder. Then run:

`make python file=tutorials/ascend_quickstart.py`

It should start outputting something similar to the following

```
WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From ascend_quickstart.py:40: The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.

2021-10-11 17:04:50.171265: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2021-10-11 17:04:50.205450: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2200000000 Hz
2021-10-11 17:04:50.208755: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5631a9802c80 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-10-11 17:04:50.208807: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:Warning:job config file does not exist
============== STARTING TRAINING ======================================
WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/tensorflow_core/python/training/training_util.py:236: Variable.initialized_value (from tensorflow.python.ops.variables) is deprecated and will be removed in a future version.
Instructions for updating:
Use Variable.read_value. Variables in 2.X are initialized automatically both in eager and graph (inside tf.defun) contexts.
WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/tensorflow_core/python/ops/init_ops.py:97: calling GlorotUniform.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
WARNING:tensorflow:From /usr/local/lib/python3.7/site-packages/tensorflow_core/python/ops/init_ops.py:97: calling Zeros.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
```

After a while, it should output the training accuracy around 0.97. This means that the training was successful. The model is stored in the local directory that you provided (instructions in the code). The output should end with something like this:

```
2021-10-11 17:06:59.502913: W tf_adapter/util/infershape_util.cc:313] The InferenceContext of node _SOURCE is null.
2021-10-11 17:06:59.502957: W tf_adapter/util/infershape_util.cc:313] The InferenceContext of node _SINK is null.
2021-10-11 17:06:59.503368: W tf_adapter/util/infershape_util.cc:313] The InferenceContext of node group_deps is null.
2021-10-11 17:07:22.533637: W tf_adapter/util/infershape_util.cc:313] The InferenceContext of node _SOURCE is null.
2021-10-11 17:07:22.533711: W tf_adapter/util/infershape_util.cc:313] The InferenceContext of node _SINK is null.
============== TESTING ACCURACY =======================================
Testing Accuracy: 0.9759296774864197
```
