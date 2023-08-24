import pytest
import pysimplified as pysf

class TestPythonSimplifiedLibrary:
	def test_library_exists(self):
		assert pysf is not None
		
	def test_quadratic_exists(self):
		assert pysf.quadratic is not None
		
	def test_quadratic_output_tuple(self):
		a,b,c = 1,5,6
		output = pysf.quadratic(a,b,c)
		assert type(output) == tuple
		
	def test_quadratic_output_tuple_of_floats(self):
		a,b,c = 1,5,6
		output = pysf.quadratic(a,b,c)
		assert type(output[0]) == float
		assert type(output[1]) == float
	
	def test_quadratic_output_tuple_of_two_floats(self):
		a,b,c = 1,5,6
		output = pysf.quadratic(a,b,c)
		assert len(output) == 2

	def test_quadratic_ideal(self):
		a,b,c = 1,5,6
		output = pysf.quadratic(a,b,c)
		assert output == (-2., -3.)
		
	def test_quadratic_boundary1(self):
		'''
		test max boundary inputs
		'''
		a = 10000000000000000000
		b = 99999999999999999999
		c = -7383205930254632388
		
		output = pysf.quadratic(a,b,c)
		
		assert type(output) == tuple
		assert type(output[0]) == float
		assert type(output[1]) == float
		print("\n")
		print("extremley large:", output)
		
	def test_quadratic_boundary2(self):
		'''
		test min boundary inputs
		'''
		a = 0.000000000000000001
		b = 0.000000000000000099
		c = -0.00000000000000002
		
		output = pysf.quadratic(a,b,c)
		
		assert type(output) == tuple
		assert type(output[0]) == float
		assert type(output[1]) == float
		print("extremley small:", output)
	
	def test_quadratic_bad_math(self):
		a,b,c = 0,5,6
		with pytest.raises(ValueError):
			pysf.quadratic(a,b,c)
