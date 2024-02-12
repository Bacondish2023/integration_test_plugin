#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@brief A mock of an application software.

Outputs logging to specified stream, stdout or file.
And the time in this software is the same as real time.
In other words, real-time-factor is 1.

This software behaves following scenario
- starts
- connects to mail server
- fetches mail server
- waits for user interaction
- (user pushes exit button)
- disconnects mail server
- exits
'''

import os
import sys
import getopt
import time

from contextlib import contextmanager


def main():
    path_logfile = None

    # ---> check argument
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hl:', ['help', 'logfile='])
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(1)

    for o, a in opts:
        if (o == '-h') or (o == '--help'):
            printUsage()
            sys.exit(0)
        if (o == '-l') or (o == '--logfile'):
            path_logfile = a
    # <--- check argument

    # Contains touple of time(seconds) and logging.
    scenario = (
        (0.0, 'Mailer starts'),
        (1.0, 'Connect to server'),
        (1.2, 'Fetche server'),
        (3.0, 'Wait for user interaction'),
        (5.0, 'Exit required by user'),
        (5.1, 'Disconnect mail server'),
        (6.0, 'Exit'),
    )

    playScenario(scenario, path_logfile)

    sys.exit(0)


def playScenario(scenario, path_logfile):
    time_start = time.time();

    with open_stream(path_logfile) as stream:
        for event in scenario:
            schedule_event = time_start + event[0]
            event_logging = event[1]

            while True:
                time_current = time.time();

                if time_current >= schedule_event:
                    # cause
                    stream.log(event_logging)
                    break
                else:
                    time.sleep(0.05)


def printUsage():
    print('Usage:')
    print('    {0} [options] project_root codegen_dir top_build_configuration'.format(os.path.basename(__file__)))
    print('    {0} -h'.format(os.path.basename(__file__)))
    print('')
    print('Options:')
    print('    -l, --logfile path   Outputs logging to specified file')
    print('')
    print('Print help:')
    print('  -h, --help: show help message')


class LoggingStream:
    def __init__(self, path_logfile = None):
        self._fd = None

        if path_logfile is None:
            pass # nothing to do. Logging goes to stdout.
        else:
            self._fd = open(path_logfile, 'w',  encoding='utf-8')

    def __del__(self):
        if self._fd is None:
            pass
        else:
            self._fd.close()

    def log(self, message):
        if self._fd is None:
            print(message, flush = True)
        else:
            self._fd.write(message + '\n')
            self._fd.flush()


@contextmanager
def open_stream(path_logfile):
   logging_stream = LoggingStream(path_logfile)
   try:
       yield logging_stream
   finally:
       del logging_stream


if __name__ == '__main__':
    # executed
    main()
else:
    # imported
    pass
