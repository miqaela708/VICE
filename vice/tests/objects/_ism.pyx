# cython: language_level = 3, boundscheck = False 

from __future__ import absolute_import 
__all__ = [
	"test_ism_constructor", 
	"test_ism_destructor" 
] 
from . cimport _ism 

_RETURN_VALUE_MESSAGE_ = { 
	1: 		"Success", 
	0: 		"Failure" 
}


def test_ism_constructor(): 
	""" 
	Tests the ISM constructor function at vice/src/objects/ism.h 
	""" 
	print("ISM constructor: %s" % (
		_RETURN_VALUE_MESSAGE_[_ism.test_ism_initialize()] 
	)) 


def test_ism_destructor(): 
	""" 
	Tests the ISM destructor function at vice/src/objects/ism.h 
	""" 
	print("ISM destructor: %s" % (
		_RETURN_VALUE_MESSAGE_[_ism.test_ism_free()] 
	)) 

