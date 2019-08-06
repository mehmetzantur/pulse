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
	
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	#GPIO.setup(11, GPIO.IN)
	print('Pulse listening is started...')

	time_stamp = 0000000000.00
	time_now = time.time()
	
	while 1:
		if stopFlag == False:

			if GPIO.input(11) == True:
				if signal == False:

					counter = counter + 1
					print('pulse ' + str(counter))
					signal = True
					
					while 1:
						
						if GPIO.input(11) == False:
							signal = False
							#time.sleep(0.05)
							break

			else:
				#print('out dış')
				
				while 1:
					if GPIO.input(11) == True:
						break
						
# def my_callback(channel):
	# global time_stamp       # put in to debounce  
	# time_now = time.time()  
	# if (time_now - time_stamp) >= 0.3:  
		# print "Rising edge detected on port 24 - even though, in the main thread,"  
		# print "we are still waiting for a falling edge - how cool?\n"  
	# time_stamp = time_now     
    
if __name__ == '__main__':
	main()




