# cython: language_level = 3, boundscheck = False 


cdef extern from "../../src/objects.h": 
	ctypedef struct CALLBACK_2ARG: 
		double (*callback)(double, double, void *) 
		void *user_func 

