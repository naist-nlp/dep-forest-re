#!/bin/sh
#
# A unit test for training.
#
# The final model parameters are saved at `test_data/saved`.

exec python3 network.py --config_file  test_data/test.cfg --model Parser
