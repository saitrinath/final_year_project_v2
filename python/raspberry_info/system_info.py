import psutil as p

def get_server_stats():
	cpu_usage = p.cpu_percent()
	cpu_temp = p.sensors_temperatures()['cpu_thermal'][0][1]
	cpu_freq = p.cpu_freq()[0]
	memory = p.virtual_memory()[2]

	return cpu_usage, cpu_temp, cpu_freq, memory
