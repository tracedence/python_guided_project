import unittest
from inspect import getfullargspec
from ..build import complex_number
from greyatomlib.python_guided_project.q01_create_class.build import complex_numbers
import pandas as pd
import numpy as np
import math


a = complex_numbers(4,4)
b = complex_numbers(4,-3)

c = complex_number(4,4)
d = complex_number(4,-3)

class Testing(unittest.TestCase):

        # check the defaults of the function

    def test_initiate_function(self):
        self.assertEqual(a.real, c.real)
        self.assertEqual(b.imag,d.imag)
        
    def test_add(self):
        x = a+b
        y = c+d
        self.assertEqual(x.real,y.real)
        self.assertEqual(x.imag,y.imag)

    def test_sub(self):
        x = a-b
        y = c-d
        self.assertEqual(x.real,y.real)
        self.assertEqual(x.imag,y.imag)

    def test_mul(self):
        x = a*b
        y = c*d
        self.assertEqual(x.real,y.real)
        self.assertEqual(x.imag,y.imag)
   
    def test_div(self):
        self.assertEqual(a.__truediv__(b),c.__truediv__(d))

    def test_absolute_value(self):
        self.assertEqual(a.abs(),c.abs())

    def test_argument(self):
        self.assertEqual(a.argument(),c.argument())

    def test_conjugate(self):
        self.assertEqual(a.real,c.real)
        self.assertEqual(b.imag,d.imag)

