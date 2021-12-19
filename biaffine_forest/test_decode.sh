#!/bin/sh
#
# A unit test for decoding.
#
# The decoded outputs will be put on `test_data/saved`.

# --test for 1-best output
# --nbest for Eisner's algorithm
# --cubesparse for edge-wise method

exec python3 network.py --save_dir test_data/saved --model Parser --test
