import RPi.GPIO as g
import time
import os

a = os.environ['relay_a']
b = os.environ['relay_b']
c = os.environ['relay_c']
d = os.environ['relay_d']


g.setmode(g.BCM)
g.setup(a,g.OUT)
g.setup(b,g.OUT)
g.setup(c,g.OUT)
g.setup(d,g.OUT)

g.output(a,g.HIGH)
g.output(b,g.HIGH)
g.output(c,g.HIGH)
g.output(d,g.HIGH)

def turn_off():
	g.output(a,g.HIGH)
	g.output(b,g.HIGH)
	g.output(c,g.HIGH)
	g.output(d,g.HIGH)


def turn_on():
	g.output(a,g.LOW)
	g.output(b,g.LOW)
	g.output(c,g.LOW)
	g.output(d,g.LOW)

