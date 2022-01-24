# Tutorial-HUAWEI-Ascend-910-NPU

PREREQUISITES:

  * [Completed SSH remote tutorial](https://github.com/kalusev/ssh-remote-tutorial)

First step is to clone the **ascend-utils** repositorium from GitHub. You should open a New Terminal and then run the command

>**git clone** https://github.com/br-ai-ns-institute/ascend-utils 

in the Terminal window.

![picture m](https://user-images.githubusercontent.com/97163298/149993334-3cac0feb-8930-4dd4-a884-91a60c0bc938.png)

![picture m1](https://user-images.githubusercontent.com/97163298/149993415-63595f6b-c801-4930-9c16-3fde71575ecb.png)

Then we go to the open folder button and we select **ascend-utils** folder and **click ok** (if necessary enter your password).

![picture m2](https://user-images.githubusercontent.com/97163298/149994944-4c035abd-530a-4607-85e8-7dd8a46fc73c.png)

Then we select the Terminal button, located at the top of the page, and select New Terminal, which will open a Terminal in a new window and we can see that we are now on ubuntu, specifically on **username@ubuntu-brains:~/ascend-utils$** 

![picture 6](https://user-images.githubusercontent.com/97163298/149995256-65857c35-749b-4097-85ec-ded395e6976f.png)

In Terminal we input command 
>**npu-smi info** 

and we will see the status of our Ascend devices. We look at the **HBM-Usage(MB)** section of the table and if it is showing 0 in the row of the device, this is an indicator that device is not being used at the moment, if we have any other value than 0, the device is currently used. This shows us which device is available.

![picture 7](https://user-images.githubusercontent.com/97163298/149996582-9260e645-7040-4efe-897f-338b0d3dbe45.png)

You can also use the command

>**npu-smi info watch -i 4 -c 0 -d 5 -s ptaicmb**

Which gives us a information about the monitoring data of all chips or a single chip.  
[More about this subject](https://support.huawei.com/enterprise/en/doc/EDOC1100116422/9d06c1ee/introduction-to-the-npu-smi-command-for-versions-100-1010)
and other commands regarding the Huawei npu-smi commands you can find on this link.

![picture smi](https://user-images.githubusercontent.com/97163298/149998617-6642ffdd-3e38-4d6a-a1ce-cc3c265a99ba.png)

We need to use dockers in order to get all the necessary packages for our training run. Through command

>**docker image ls** 

we can list all of the docker image files.

![picture 8](https://user-images.githubusercontent.com/97163298/149999576-debf377d-406f-4e90-a8fd-bcb84334cce4.png)

In order to use appropriate docker image we need to run container with that docker image. Command 

>**docker ps** 

print out containers that are running.

![picture m3](https://user-images.githubusercontent.com/97163298/150000008-8a49a4ad-4ecf-4eec-b2ea-fd7fde29c974.png)

If our container is not running already, you need to run the docker command

>**docker run --name demo_seminar -d -it -e ASCEND_VISIBLE_DEVICES=1,4 --mount type=blind,source=/home df8e2e867f54 /bin/bash** 

and you need to add right docker IMAGE ID, that you can see when you run previous command **docker image ls**. In this case IMAGE ID df8e2e867f54.

![picture m4](https://user-images.githubusercontent.com/97163298/150001456-50e274ab-33e5-4534-a777-cff9f9d4f883.png)

After this we run the command 

>**make python file=tutorials/tf_qs.py**

and our training is executed on our CPU. We run it on our CPU and not on NPU, so we did not gain any benefit.

![picture 9](https://user-images.githubusercontent.com/97163298/150001753-98a38ddf-ba3f-4656-917e-5aa695bf4344.png)

So, we need to copy **helpers.py** file from GitHub sentinel repository **https://github.com/br-ai-ns-institute/sentinel** to our local device in the cloned **ascend-utils** folder, that is in the tutorials folder under **ascend-utils**. We go on the folder tutorials, showed on the left side of the VS code and then click on the first button (new file) and create a new python file **helpers.py**.

![picture 10](https://user-images.githubusercontent.com/97163298/150004038-1efc9300-5eb5-4b11-88d5-8e3dab2c4d35.png)

Then copy the code from the original **helpers.py** file and save the file with ctrl+s command.
Then we need to modify our original **helpers.py** so it run on NPU device. Modified code you can find here,

```

import os
import tensorflow as tf
from npu_bridge.npu_init import *
from tensorflow.core.protobuf.rewriter_config_pb2 import RewriterConfig
from tensorflow.python.keras import backend as K



class NpuHelperForTF:
    """Initialize NPU session for TF on Ascend platform."""

    def __init__(self, device_id, rank_id, rank_size, job_id, rank_table_file):
        # Init Ascend
        os.environ["ASCEND_DEVICE_ID"] = device_id
        os.environ["JOB_ID"] = job_id
        os.environ["RANK_ID"] = rank_id
        os.environ["RANK_SIZE"] = rank_size
        os.environ["RANK_TABLE_FILE"] = rank_table_file

        sess_config = tf.ConfigProto()
        custom_op = sess_config.graph_options.rewrite_options.custom_optimizers.add()
        custom_op.name = "NpuOptimizer"
        custom_op.parameter_map["use_off_line"].b = True
        custom_op.parameter_map["precision_mode"].s = tf.compat.as_bytes("force_fp16")
        custom_op.parameter_map["graph_run_mode"].i = 0

        custom_op.parameter_map["dynamic_input"].b = True
        custom_op.parameter_map["dynamic_graph_execute_mode"].s = tf.compat.as_bytes("lazy_recompile")

        sess_config.graph_options.rewrite_options.remapping = RewriterConfig.OFF
        sess_config.graph_options.rewrite_options.memory_optimization = RewriterConfig.OFF

        self._sess = tf.Session(config=sess_config)
        K.set_session(self._sess)


    def sess(self):
        return self._sess
        
```

and you copied it into the **helpers.py** file and save the file with **ctrl+s** command. This step is shown here for you to see the modification in the code that is necessary in order to run our Model on NPU.

Also, you need to modify the **tf_qs.py** file that you cloned. Modified code you can find here, and you copied it into the **tf_qs.py** file:

```

"""TF quickstart example running on NPU devices."""

import tensorflow as tf
from helpers import NpuHelperForTF

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ]
)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

npu_config = {
    "device_id": "0",
    "rank_id": "0",
    "rank_size": "0",
    "job_id": "10385",
    "rank_table_file": "",
}
print("________________________ INIT NPU SESSION ________________________")
sess = NpuHelperForTF(**npu_config).sess()

print("________________________ COMPILE MODEL ___________________________")
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

print("________________________ TRAINING ________________________________")
model.fit(x_train, y_train, epochs=5)

print("________________________ EVALUATE ________________________________")
model.evaluate(x_test, y_test, verbose=2)

print("________________________ CLOSE NPU SESSION _______________________")
sess.close()
```
and save the file with **ctrl+s** command.

Now, you can run the command again

>**make python file=tutorials/tf_qs.py**

and now our Model will run on NPU and print out our results, with CLOSE NPU SESSION as a marker that the procces is finished. 

![picture 11](https://user-images.githubusercontent.com/97163298/150006541-0c49b339-a1b7-4f68-a273-cd4e2fa34c3f.png)





![picture 12](https://user-images.githubusercontent.com/97163298/150006655-2e43d974-9b1f-4060-bb90-23cd7efa594a.png)

