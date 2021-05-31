def calc_thi(T, hum):
	RH = hum/100
	thi = (0.8*T)+(RH*(T-14.4))+46.4
	return thi
