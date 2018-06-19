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
2. FlyCapture 2.12.3.2 SDK - Linux Ubuntu 16.04 (64-bit)

Follow the README file provided with those two packages to properly install essential dependencies.

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

