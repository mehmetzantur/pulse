# -*- coding: utf-8 -*-

import sys

import RPi.GPIO as GPIO
import time

time_stamp = time.time() 

def main():
	
	stopFlag = False
	counter = 0
	signal = False
	sigtick = False
	isFirst = True
	
	counterx = 1
	
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	#GPIO.setup(11, GPIO.IN)
	print('Pulse listening is started...')

	
	while 1:

		if GPIO.input(11) and counterx == 1:

			counter = counter + 1
			print('pulse ' + str(counter))
			
			while 1:
				
				if GPIO.input(11) == True and counterx == 1:
					counterx = 2
					pass
				
				if GPIO.input(11) == False and counterx == 2:
					counterx = 1
					break
					
					
					
					
					
					
if __name__ == '__main__':
	main()




