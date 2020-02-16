
from __future__ import absolute_import 
try: 
	__VICE_SETUP__ 
except NameError: 
	__VICE_SETUP__ = False 

if not __VICE_SETUP__: 

	__all__ = [ 
		"test", 
		"agb", 
		"ccsne", 
		"channel", 
		"dataset", 
		"element", 
		"fromfile", 
		"imf", 
		"integral", 
		"ism", 
		"mdf", 
		"migration", 
		"multizone", 
		"singlezone", 
		"sneia", 
		"ssp", 
		"tracer" 
	] 
	# from ._agb import * 
	# from ._ccsne import * 
	# from ._channel import * 
	# from ._dataset import * 
	# from ._element import * 
	# from ._fromfile import * 
	# from ._imf import * 
	# from ._integral import * 
	# from ._ism import * 
	# from ._mdf import * 
	# from ._migration import * 
	# from ._multizone import * 
	# from ._singlezone import * 
	# from ._sneia import * 
	# from ._ssp import * 
	# from ._tracer import * 

	from .._test_utils import moduletest 
	from . import _agb as agb 
	from . import _ccsne as ccsne 
	from . import _channel as channel 
	from . import _dataset as dataset 
	from . import _element as element 
	from . import _fromfile as fromfile 
	from . import _imf as imf 
	from . import _integral as integral 
	from . import _ism as ism 
	from . import _mdf as mdf 
	from . import _migration as migration 
	from . import _multizone as multizone 
	from . import _singlezone as singlezone 
	from . import _sneia as sneia 
	from . import _ssp as ssp 
	from . import _tracer as tracer 

	# __all__.extend(agb.__all__) 
	# __all__.extend(ccsne.__all__) 
	# __all__.extend(channel.__all__) 
	# __all__.extend(dataset.__all__) 
	# __all__.extend(element.__all__) 
	# __all__.extend(fromfile.__all__) 
	# __all__.extend(imf.__all__) 
	# __all__.extend(integral.__all__) 
	# __all__.extend(ism.__all__) 
	# __all__.extend(mdf.__all__) 
	# __all__.extend(migration.__all__) 
	# __all__.extend(multizone.__all__) 
	# __all__.extend(singlezone.__all__) 
	# __all__.extend(sneia.__all__) 
	# __all__.extend(ssp.__all__) 
	# __all__.extend(tracer.__all__) 

	def test(run = True): 
		""" 
		Runs all test functions in this module 
		""" 
		test = moduletest("VICE object memory management") 
		test.new(agb.test_agb_grid_constructor()) 
		test.new(agb.test_agb_grid_destructor()) 
		test.new(ccsne.test_ccsne_yield_specs_constructor()) 
		test.new(ccsne.test_ccsne_yield_specs_destructor()) 
		test.new(channel.test_channel_constructor()) 
		test.new(channel.test_channel_destructor()) 
		test.new(dataset.test_dataset_constructor()) 
		test.new(dataset.test_dataset_destructor()) 
		test.new(element.test_element_constructor()) 
		test.new(element.test_element_destructor()) 
		test.new(fromfile.test_fromfile_constructor()) 
		test.new(fromfile.test_fromfile_destructor()) 
		test.new(imf.test_imf_constructor()) 
		test.new(imf.test_imf_destructor()) 
		test.new(integral.test_integral_constructor()) 
		test.new(integral.test_integral_destructor()) 
		test.new(ism.test_ism_constructor()) 
		test.new(ism.test_ism_destructor()) 
		test.new(mdf.test_mdf_constructor()) 
		test.new(mdf.test_mdf_destructor()) 
		test.new(migration.test_migration_constructor()) 
		test.new(migration.test_migration_destructor()) 
		test.new(multizone.test_multizone_constructor()) 
		test.new(multizone.test_multizone_destructor()) 
		test.new(singlezone.test_singlezone_constructor()) 
		test.new(singlezone.test_singlezone_destructor()) 
		test.new(sneia.test_sneia_yield_specs_constructor()) 
		test.new(sneia.test_sneia_yield_specs_destructor()) 
		test.new(ssp.test_ssp_constructor()) 
		test.new(ssp.test_ssp_destructor()) 
		test.new(tracer.test_tracer_constructor()) 
		test.new(tracer.test_tracer_destructor()) 
		if run: 
			test.run() 
		else: 
			return test 

else: 
	pass 
