# Integration Test Plugin

A plugin which enable testing of target executables on Python3 unittest framework.

Intended user

* The person who wants to test executable with automated method. And the executable outputs stream.


## Introduction

**Integration Test Plugin** is a Python package which adds testing functionality for executable to Python unittest.
It supports automation because it is designed to be used with Python unittest together.
And it works on various platforms.

![Concept](doc/development/20_design/image/concept.png)

User can define their own test case on python3 code using this package.

The Integration Test Plugin verifies behavior of process under test through stream such as stdout, stderr, log file.
These verifies have timeout.
When tested process crashes, the crash is detected as timeout.


## Features

* **Verification**
    * Tests can check expected patterns are in stream output.
    * Tests can check exit of process and exit code.
    * Tests can check presence of file, directory.
* **Crash detection**
    * Tests can detect and make the result NG if the process under test crashes.
* **Automation support**
    * All test cases can be discovered and run by command-line operation.


## Motivation

With stream, we can test behavior of whole executable easily.
[launch_testing](https://github.com/ros2/launch) is known as one of testing tool using stream.
It has useful assertions such as `assertWaitFor` verifies that expected string is in stream.
But, it is not available on out of ROS because it depends on ROS environment.

Therefore, this project aims to create a generic integration test tool that does not depend on specific platform.


## Prerequisites

#### Supported Platform

* Linux
* Windows
* MacOS

#### Required Software

* **Python 3** 3.6.8 or above


## How to Use

#### Install

```sh
pip install integration_test_plugin
```

#### Example

There are 2 examples.

###### Run

```sh
python -m unittest example.test_air_conditioner_simulation
python -m unittest example.test_mailer
```

###### Code

* [test_air_conditioner_simulation](example/test_air_conditioner_simulation.py)
* [test_mailer](example/test_mailer.py)

#### Verifier

Following verifiers are available on this project.
Details are on implementation comment.

|Verifier|Package|
|:---|:---|
|ProcessVerifier.assertExit()|integration_test_plugin.process_verifier|
|StreamVerifier.assertPattern()|integration_test_plugin.stream_verifier|
|assertFileExist()<br>assertFileNotExist()<br>assertDirectoryExist()<br>assertDirectoryNotExist()|integration_test_plugin.path_verifier|


## License

Copyright 2024 [Hidekazu TAKAHASHI](https://github.com/Bacondish2023).
This project is free and open-source software licensed
under the **MIT License**.
