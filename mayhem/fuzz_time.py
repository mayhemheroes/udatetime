#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports():
    from udatetime.rfc3339 import from_rfc3339_string, to_rfc3339_string

@atheris.instrument_func
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        dt = from_rfc3339_string(fdp.ConsumeRemainingString())
        to_rfc3339_string(dt)
    except ValueError as e:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
