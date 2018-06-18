# flir-util

This is a repository that contains all the scripts for FLIR Blackfly cameras.

## Usage

### Environment Set Up
All codes are implemented in **Python3** and use APIs for **Ubuntu Linux 16.04**.

First of all, you should install **Python3** and **pip**.

To install **Python3**, run following commands in your terminal:
```sh
$ sudo apt-get install python3
$ sudo apt-get update
```

To install **pip**, run following commands in your terminal:
```sh
$ sudo apt-get install python3-pip
```
To be able to run the script, you probably will also need following API and SDKs:
1. PyCapture 2.11.425 for Python2 and Python3 - Ubuntu Linux (64-bit) 
2. FlyCapture 2.12.3.2 SDK - Linux Ubuntu 16.04 (64-bit) [**Optional**]
3. Spinnaker 1.13.0.31 SDK - Linux Ubuntu 16.04 (64-bit) [**Optional**]

Without PyCapture, you will **NOT** be able to run the script since it is the API that this script uses. However, you won't need FlyCapture and Spinnaker to run the script but in order to configure your cameras properly, you will need at least **ONE** of them.

To run the script, run following commands in your terminal:
```sh
$ cd [DirectoryOfTheFile]
$ python3 [NameOfTheScript].py
```
For instance:

```sh
$ cd Desktop
$ python3 RawData.py
```
Then, images will be generated in the format of PNG.

**More details could be found in comments for each file.**

