r"""
This file preprocesses the data files in this directory containing the
initial-final remnant mass information. It produces output files in the
corresponding vice/yields/ccsne/LC18/FeH_/v_/ directories, each containing
two columns: the initial stellar mass in Msun on the left and the final remnant
mass in Msun on the right.

ARGV
----
1) the name of the raw input file

Example
-------
$ python remnants.processor.py mcut-SetR.txt
"""

import sys
import os


class initial_final_mass_table:

	def __init__(self, FeH = 0, vrot = 0):
		self.FeH = FeH
		self.vrot = vrot
		self._raw = self.read_file(sys.argv[1])


	def save_table(self):
		r"""
		Saves the table to the appropriate directory under the name
		remnants.dat.
		"""
		table = self.get_table()
		with open("../FeH%d/v%d/remnants.dat" % (self.FeH, self.vrot),
			'w') as out:
			out.write("""\
# This file has been procedurally generated by
# vice/yields/ccsne/LC18/raw/remnants.processor.py given the initial-final
# remnant mass table in vice/yields/ccsne/LC18/raw/%s.
#
# initial mass [Msun]         final mass [Msun]
""" % (sys.argv[1]))
			for i in range(len(table)):
				out.write("%.3e\t%.3e\n" % (table[i][0], table[i][1]))
			out.close()


	def get_table(self):
		r"""
		Get the table for the [Fe/H] and rotational velocity encoded in the
		attributes 'FeH' and 'vrot'. Initial masses in Msun will always be the
		same regardless of these parameters.
		"""
		initial_masses = [13., 15., 20., 25., 30., 40., 60., 80., 120.]
		# The column of remnant masses to take for a given rotational velocity
		column = {
			0: 1,
			150: 6,
			300: 11
		}[self.vrot]
		# the rows of remnant masses to take for a given metallicity
		rows = {
			0: list(range(9)),
			-1: list(range(9, 18)),
			-2: list(range(18, 27)),
			-3: list(range(27, 36))
		}
		remnant_masses = [self._raw[row][column] for row in rows[self.FeH]]
		for i in range(len(remnant_masses)):
			if remnant_masses[i] < 0: remnant_masses[i] = 0
		return [list(_) for _ in zip(initial_masses, remnant_masses)]


	@property
	def FeH(self):
		r"""
		The metallicity [Fe/H] of the stars.
		"""
		return self._FeH


	@FeH.setter
	def FeH(self, value):
		if isinstance(value, int):
			if value in [0, -1, -2, -3]:
				self._FeH = value
			else:
				raise LookupError("""\
Only [Fe/H] = -3, -2, -1, and 0 are available.""")
		else:
			raise TypeError("Attribute 'FeH' must be an integer. Got: %s" % (
				type(value)))


	@property
	def vrot(self):
		r"""
		The rotational velocity in km/s of the stars.
		"""
		return self._vrot


	@vrot.setter
	def vrot(self, value):
		if isinstance(value, int):
			if value in [0, 150, 300]:
				self._vrot = value
			else:
				raise LookupError("Only vrot = 0, 150, and 300 are available.")
		else:
			raise TypeError("Attribute 'vrot' must be an integer. Got: %s" % (
				type(value)))


	@staticmethod
	def read_file(name):
		r"""
		Read the raw data file.

		Parameters
		----------
		name : ``str``
			The name of the data file. Should be in the same directory as this
			script.

		Returns
		-------
		data : ``dict``
			The contents of the file. Keys to the dictionary will be the column
			headers at the top of the file, each mapped to a list of floats taken
			from the corresponding column of the file.
		"""
		with open(name, 'r') as f:
			keys = f.readline().split()
			contents = []
			while True:
				line = f.readline()
				if line == "": break
				contents.append([float(_) for _ in line.split()])
			f.close()
		return contents


if __name__ == "__main__":
	table = initial_final_mass_table()
	for FeH in [-3, -2, -1, 0]:
		for vrot in [0, 150, 300]:
			table.FeH = FeH
			table.vrot = vrot
			table.save_table()

