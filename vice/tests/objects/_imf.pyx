# cython: language_level = 3, boundscheck = False 

from __future__ import absolute_import 
__all__ = [
	"test_imf_constructor", 
	"test_imf_destructor" 
] 
from . cimport _imf 

_RETURN_VALUE_MESSAGE_ = { 
	1: 		"Success", 
	0: 		"Failure" 
}


def test_imf_constructor(): 
	""" 
	Tests the IMF constructor function at vice/src/objects/imf.h 
	""" 
	print("IMF constructor: %s" % (
		_RETURN_VALUE_MESSAGE_[_imf.test_imf_initialize()] 
	)) 


def test_imf_destructor(): 
	""" 
	Tests the IMF destructor function at vice/src/objects/imf.h 
	""" 
	print("IMF destructor: %s" % (
		_RETURN_VALUE_MESSAGE_[_imf.test_imf_free()]
	)) 

