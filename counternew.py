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
	
	status = 0
	counterx = 1
	
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.IN)
	
	print('Pulse listening is started...')

	
	while 1:
		
		
		if GPIO.input(11) == 1 and counterx == 1:
			counterx = 0
			counter = counter + 1
			print('pulse ' + str(counter))
			
			while 1:
				
				if GPIO.input(11) == 1 and counterx == 1:
					counterx = 0
					pass
				
				if GPIO.input(11) == 0 and counterx == 0:
					counterx = 1
					break		
			time.sleep(0.1)

		# if GPIO.input(11) == 1:
			# if status == 0:
						
				# GPIO.output(13, 1)
				
				# if GPIO.input(15) == 1:
					# GPIO.output(13, 0)
					# counter = counter + 1
					# print('pulse ' + str(counter))
					# status = 1
					
					# while 1:
						# if GPIO.input(11) == 1:
							# GPIO.output(13, 0)
							# pass
						# else:
							# status = 0
							# break
				
			# else:
				# status = 0
					
					
					
	
	
# if GPIO.input(11) and counterx == 1:

	# counter = counter + 1
	# print('pulse ' + str(counter))
	
	# while 1:
		
		# if GPIO.input(11) == True and counterx == 1:
			# counterx = 2
			# pass
		
		# if GPIO.input(11) == False and counterx == 2:
			# counterx = 1
			# break				
					
					
if __name__ == '__main__':
	main()




