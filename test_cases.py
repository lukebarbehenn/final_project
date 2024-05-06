import pytest
 
from fp_code import getweather 

def test_getweather():

    assert getweather(38.91982068626991, -77.03656476393802)

