# ascend-utils
Utilities for working with Huawei Atlas 800 (3010) server, with Ascend PCIe cards

This repo represents the collection of useful tools for working with the Huawei server
Atlas 800 (3010). It is meant to be populated by the researchers of the br.ai.ns
institute, but also by other users of the same server (installed locally in Novi Sad).

## Table of contents
### Intro
### Setting up and using the Docker container
### [Using the Makefile](using_the_makefile.md)
### [Tutorials](tutorials/README.md)

### Usage

#### Setting docker container
You should use the `Makefile` variable [`CONTAINER`](https://github.com/br-ai-ns-institute/ascend-utils/blob/main/Makefile#L17) to set it to the desired docker container.
Use the standard docker commands to see which containers are available. You can download
your own image from [Ascendhub](https://ascendhub.huawei.com/#/index), and create your own container, for usage with this scropt.

#### Running commands
You should copy this file to the root of a directory you're using to store your code.
Then, from the same root directory, you can use the commands such as:

```
make npu
```
which will output the result of a `npu-smi info` [command](https://support.huawei.com/enterprise/en/doc/EDOC1100133280/52956c41/npu-smi-commands), like so:
```
+------------------------------------------------------------------------------------+
| npu-smi 21.0.2                   Version: 21.0.2                                   |
+----------------------+---------------+---------------------------------------------+
| NPU   Name           | Health        | Power(W)   Temp(C)                          |
| Chip                 | Bus-Id        | AICore(%)  Memory-Usage(MB)  HBM-Usage(MB)  |
+======================+===============+=============================================+
| 1     910A           | OK            | 64.3       56                               |
| 0                    | 0000:3B:00.0  | 0          1809 / 15079      0    / 32768   |
+======================+===============+=============================================+
| 4     910A           | OK            | 65.6       58                               |
| 0                    | 0000:86:00.0  | 0          1809 / 15079      0    / 32768   |
+======================+===============+=============================================+
```

or

```
make run file=/home/slobodan/training_handson/process1.sh
```
which will run the training handson example in the running docker container.
