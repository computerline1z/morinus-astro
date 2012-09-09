import chart
import math
import util


class Points:
	def __init__(self, valid, points):
		self.valid = valid
		self.pts = points


class ZodParsBase:
	"""Computes zodiacal parallels (abstract)"""

	def __init__(self, obl):
		self.obl = obl
	

	def getEclPoints(self, lon, decl, onEcl):
		'''Calculates points of the Ecliptic from declination'''
		lPARALLEL = chart.Chart.PARALLEL
		CONTRAPARALLEL = chart.Chart.CONTRAPARALLEL

		origdecl = decl

		if decl < 0.0:
			decl *= -1

		if decl > self.obl:
			return Points(False, ((-1.0, lPARALLEL), (-1.0, lPARALLEL), (-1.0, lPARALLEL), (-1.0, lPARALLEL)))

		if onEcl:
			if decl == self.obl:
				lon += 180.0
				lon = util.normalize(lon)
				return Points(True, ((lon, CONTRAPARALLEL), (-1.0, lPARALLEL)))
			else:
				lon1 = lon+180.0
				lon1 = util.normalize(lon1)
				lon2 = 360.0-lon1
				lon3 = util.normalize(lon2+180.0)
				return Points(True, ((lon1, CONTRAPARALLEL), (lon2, lPARALLEL), (lon3, CONTRAPARALLEL)))
		else:
			if decl == self.obl:
				lon1 = math.degrees(math.asin(math.sin(math.radians(origdecl))/math.sin(math.radians(self.obl))))
				lon1 = util.normalize(lon1)
				lon2 = util.normalize(lon1+180.0)
				return Points(True, ((lon1, lPARALLEL), (lon2, CONTRAPARALLEL)))
			else:
				lon1 = math.degrees(math.asin(math.sin(math.radians(origdecl))/math.sin(math.radians(self.obl))))
				lon1 = util.normalize(lon1)
				lon2 = util.normalize(lon1+180.0)
				lon3 = 360.0-lon2
				lon4 = util.normalize(lon3+180.0)
				return Points(True, ((lon1, lPARALLEL), (lon2, CONTRAPARALLEL), (lon3, lPARALLEL), (lon4, CONTRAPARALLEL)))

		# return Points(False, ((-1.0, lPARALLEL), (-1.0, lPARALLEL), (-1.0, lPARALLEL), (-1.0, lPARALLEL)))



