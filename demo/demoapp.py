#!/usr/bin/env python3
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
"""
Trivial ctypesgen demo library consumer
from http://code.google.com/p/ctypesgen

 NOTE demolib.py needs to be generated via:

    ../ctypesgen.py -o pydemolib.py -l demolib demolib.h
    ../ctypesgen.py -o pydemolib.py -l demolib.so demolib.h


"""

import sys

import pydemolib  # generated from demolib.h by ctypesgen

import ctypes
import numpy
import tensorflow as tf

def do_demo():
    a = 1
    b = 2
    result = pydemolib.trivial_add(a, b)
    print("a", a)
    print("b", b)
    print("result", result)

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # print("numpy array")
    # print(x_train[0])

    c_double_p   = ctypes.POINTER(ctypes.c_double)
    c_double_p_p = ctypes.POINTER(c_double_p)
    # data = x_train[0]
    data = numpy.array([[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]])
    m = data.shape[0]
    n = data.shape[1]
    data = data.astype(numpy.float64)
    data_p = data.ctypes.data_as(c_double_p)
    data_p_p = data.ctypes.data_as(c_double_p_p)
    print("m, n", m, n)
    print(data)

    # print(type(data_p))
    # print(type(ctypes.POINTER(ctypes.POINTER(ctypes.c_double))))

    # m = ctypes.c_int(x_train[0].shape[0])
    # n = ctypes.c_int(x_train[0].shape[1])
    result2 = pydemolib.trivial_array_add(data_p, m, n)
    print("result2", result2)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    do_demo()

    return 0


if __name__ == "__main__":
    sys.exit(main())
