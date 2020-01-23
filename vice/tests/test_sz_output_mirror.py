
from __future__ import print_function, division
import math 
import vice 
import warnings 
import sys 
import gc 
sys.stdout.flush() 

try: 
	ModuleNotFoundError 
except NameError: 
	ModuleNotFoundError = ImportError
try: 
	import numpy as np 
	_OUTTIMES_ = np.linspace(0, 10, 201) 
except (ImportError, ModuleNotFoundError): 
	_OUTTIMES_ = 201 * [0.] 
	for i in range(201): 
		_OUTTIMES_[i] = 0.05 * i 

def test_parameters(**kwargs): 
	"""
	kwargs: keyword arguments to pass to vice.singlezone 
	""" 
	tracker = {
		"singlezone":		True, 
		"mirror":			True, 
		"output":			True, 
		"history":			True, 
		"mdf": 				True 
	}
	try: 
		vice.singlezone(**kwargs).run(_OUTTIMES_, overwrite = True) 
	except: 
		tracker["singlezone"] = False 
	try: 
		assert(isinstance(vice.history("onezonemodel"), vice.dataframe)) 
	except: 
		tracker["history"] = False 
	try: 
		assert(isinstance(vice.mdf("onezonemodel"), vice.dataframe)) 
	except: 
		tracker["mdf"] = False 
	try: 
		out = vice.output("onezonemodel") 
		assert(isinstance(out, vice.output)) 
		assert(isinstance(out.history, vice.dataframe)) 
		assert(isinstance(out.mdf, vice.dataframe)) 
		assert(isinstance(out.ccsne_yields, vice.dataframe)) 
		assert(isinstance(out.sneia_yields, vice.dataframe)) 
		assert(isinstance(out.elements, tuple)) 
	except: 
		tracker["output"] = False 
	try: 
		assert(isinstance(vice.mirror(out), vice.singlezone)) 
	except: 
		tracker["mirror"] = False 
	return tracker 



def main(): 
	"""
	Runs the tests on the singlezone object, the output object, and the 
	mirror function. 
	"""
	warnings.filterwarnings("ignore") 
	print("=================================================================")
	print("TESTING: vice.singlezone") 
	print("         vice.output") 
	print("         vice.mirror") 
	out = open("test_sz_output_mirror.out", 'w') 
	_MODES_ = ["ifr", "sfr", "gas"] 
	_IMF_ = ["kroupa", "salpeter", lambda m: m**-2] 
	_ETA_ = [2.5, lambda t: 2.5 * math.exp( -t / 4.0 )] 
	_ZIN_ = [0, 1.0e-8, lambda t: 1.0e-8 * (t / 10.0), {
		"o":		lambda t: 0.0057 * (t / 10.0),  
		"fe": 		0.0013
	}]
	_RECYCLING_ = ["continuous", 0.4] 
	_RIA_ = ["plaw", "exp", lambda t: t**-1.5] 
	_TAU_STAR_ = [2.0, lambda t: 2.0 + t / 10.0] 
	_SCHMIDT_ = [False, True] 
	_AGB_MODEL_ = ["cristallo11", "karakas10"] 

	a = 0 # track number of integrations 
	b = 1 # total number of integrations 
	for i in [_MODES_, _IMF_, _ETA_, _ZIN_, _RECYCLING_, _RIA_, _TAU_STAR_, 
		_SCHMIDT_, _AGB_MODEL_]: 
		b *= len(i) 

	keys = ["success", "failure"] 
	singlezone_tracker = dict(zip(keys, [0, 0])) 
	mirror_tracker = dict(zip(keys, [0, 0])) 
	output_tracker = dict(zip(keys, [0, 0])) 
	history_tracker = dict(zip(keys, [0, 0])) 
	mdf_tracker = dict(zip(keys, [0, 0])) 
	params = {} 
	for i in _MODES_: 
		for j in _IMF_: 
			for k in _ETA_: 
				for l in _ZIN_: 
					for m in _RECYCLING_: 
						for n in _RIA_: 
							for o in _TAU_STAR_: 
								for p in _SCHMIDT_: 
									for q in _AGB_MODEL_: 
										params["elements"] = ["fe", "o", "c"] 
										params["mode"] = i 
										params["IMF"] = j 
										params["eta"] = k 
										params["Zin"] = l 
										params["recycling"] = m 
										params["RIa"] = n 
										params["tau_star"] = o 
										params["schmidt"] = p 
										params["agb_model"] = q 
										params["dt"] = 0.05
										results = test_parameters(**params) 
										if results["singlezone"]: 
											singlezone_tracker["success"] += 1
										else:
											singlezone_tracker["failure"] += 1 
										if results["mirror"]: 
											mirror_tracker["success"] += 1
										else:
											mirror_tracker["failure"] += 1 
										if results["output"]: 
											output_tracker["success"] += 1
										else:
											output_tracker["failure"] += 1 
										if results["history"]: 
											history_tracker["success"] += 1
										else:
											history_tracker["failure"] += 1 
										if results["mdf"]: 
											mdf_tracker["success"] += 1
										else:
											mdf_tracker["failure"] += 1 

										a += 1
										sys.stdout.write("Progress: %.1f%%\r" % (
											a / b * 100)) 
										sys.stdout.flush() 
										gc.collect() 
										
	#######
	message = """\
vice.singlezone :: %d successes :: %d failures 
vice.history :: %d successes :: %d failures 
vice.mdf :: %d successes :: %d failures 
vice.output :: %d successes :: %d failures 
vice.mirror :: %d successes :: %d failures \
""" % (
		singlezone_tracker["success"], singlezone_tracker["failure"], 
		history_tracker["success"], history_tracker["failure"], 
		mdf_tracker["success"], mdf_tracker["failure"], 
		output_tracker["success"], output_tracker["failure"], 
		mirror_tracker["success"], mirror_tracker["failure"]
		)
	print(message) 
	out.write(message) 
	out.close() 

if __name__ == "__main__": 
	main() 





