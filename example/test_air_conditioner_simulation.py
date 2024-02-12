#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

import os
import subprocess
import time
import tempfile

import integration_test_plugin.stream_verifier as stream_verifier
import integration_test_plugin.process_verifier as process_verifier
import integration_test_plugin.path_verifier as path_verifier


class TestAirConditionerSimulationStdout(unittest.TestCase):
    '''
    A test fixture which tests mock_air_conditioner_simulation.py with stdout.
    '''

    def setUp(self):
        self.__data_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data'

        # Luanch the process under test
        # It is necessary that pass PIPE to the stdout parameter for using stream output.
        # Setting STDOUT to stderr makes together stdout and stderr.
        self.__process = subprocess.Popen(
            args=('python', '-B', self.__data_dir + os.sep + 'mock_air_conditioner_simulation.py'),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)


    def tearDown(self):
        self.__process.kill()


    def test_typical(self):
        # Create a process verifier instance.
        p_verifier = process_verifier.ProcessVerifier(self.__process)

        # Create a stream verifier instance.
        # This is necessary for checking stream.
        s_verifier = stream_verifier.StreamVerifier(self.__process.stdout)

        # This test expects following patterns are appeared in stream in this order.
        s_verifier.assertPattern('Air conditioner start')
        s_verifier.assertPattern('Initialize done')
        s_verifier.assertPattern('Wait for user interaction')
        s_verifier.assertPattern('Enter heating mode')
        s_verifier.assertPattern('Wait for user interaction')
        s_verifier.assertPattern('Stop required by user')
        s_verifier.assertPattern('Shutdown')

        # This test expects that the process exits in 10 seconds from outputting 'Shutdown' and exit code is 0.
        # This assertion is designed to be used once per the process because the process exits.
        p_verifier.assertExit(exit_code = 0, timeout = 10)


class TestAirConditionerSimulationLogfile(unittest.TestCase):
    '''
    A test fixture which tests mock_air_conditioner_simulation.py with logfile.
    '''


    def setUp(self):
        self.__data_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data'
        self.__process = None


    def tearDown(self):
        pass # nothing to do


    def test_typical(self):

        # This test case uses temporary directory.
        # This is optional and user can use normal directory.
        with tempfile.TemporaryDirectory() as tmpdir:
            path_logfile = tmpdir + os.sep + 'logging.txt'

            try:
                self.__process = subprocess.Popen(
                    args=('python', '-B', self.__data_dir + os.sep + 'mock_air_conditioner_simulation.py', '-l', path_logfile),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    universal_newlines=True)

                p_verifier = process_verifier.ProcessVerifier(self.__process)

                # wait for file creation
                path_verifier.assertFileExist(path_logfile, timeout = 10)

                with open(path_logfile, 'r') as fp:
                    s_verifier = stream_verifier.StreamVerifier(fp)

                    s_verifier.assertPattern('Air conditioner start')
                    s_verifier.assertPattern('Initialize done')
                    s_verifier.assertPattern('Wait for user interaction')
                    s_verifier.assertPattern('Enter heating mode')
                    s_verifier.assertPattern('Wait for user interaction')
                    s_verifier.assertPattern('Stop required by user')
                    s_verifier.assertPattern('Shutdown')

                    p_verifier.assertExit(exit_code = 0, timeout = 10)

            finally:
                # Clean up code.
                # This is optional and required for closing resources before the temporary directory is removed.
                del p_verifier # ProcessVerifier terminates the process
                del s_verifier # StreamVerifier closes fp


if __name__ == '__main__':
    # executed
    unittest.main()
