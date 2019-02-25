# Biésów Smãtk

class Tv(object):
	'''instantiation of TV class
	object would have volume and channel attributes'''
	def __init__(self, volume = '1', channel = '1'):
		print('Jes włącził telezdrzélnik, co mô 100 karnôlów.')
		print('\nkarnôl '+channel+'\ngłosnosc '+volume)
		self.volume = volume
		self.channel = channel

	
	#def volume_change(self):
	#	volChange = ''
	#	volume = int(self.volume)
	#	while volChange not in ('+','-'):
	#		volChange = input('Wpiszë "+", żebë wzyc głosni abò "-", żebë wzyc cëszi.')
	#		if volChange == '+':
	#			volume += 1
	#			if volume >= 10:
	#				volume = 10
	#		elif volChange == '-':
	#			volume -= 1
	#			if volume <= 0:
	#				volume = 0
	#		else:
	#			print('Wpiszë "+" abò "-": ')
	#	self.volume = str(volume)

	def vol_plus(self):
		'''volume up'''
		volume = int(self.volume)
		volume +=1
		if volume >= 10:
			volume = 10
		self.volume = str(volume)
		print('\ngłosnosc\n'+' |' * volume)

	def vol_minus(self):
		'''volume down'''
		volume = int(self.volume)
		volume -=1
		if volume <= 0:
			volume = 0
		self.volume = str(volume)
		print('\ngłosnosc\n'+' |' * volume)

	def channel_change(self):
		'''changing channel in range from 1 to 100 inclusive or changing not'''
		channel = int(self.channel)
		try:
			chanChange = int(input('\nPodôj numrã karnôlu: '))
		except(ValueError):
			print('\nNi ma taczégò karnôlu.')
			chanChange = channel
		if chanChange in range(1,101):
			channel = chanChange
			print('\nkarnôl '+str(channel))
		else:
			print('\nNi ma taczégò karnôlu.')
		self.channel = str(channel)

	def check(self):
		'''checking channel and volume'''
		print('\nkarnôl '+self.channel+'\ngłosnosc '+self.volume)

def main():
	'''main block of program'''
	tv = Tv()
	print("""
		0 - skùńczë
		1 - zmieni karnôl
		2 - sprôwdzë karnôl i głosnosc
		- - zmiészi głosnosc
		+ - zwikszi głosnosc""")
	choice = None #loop of remote control
	while choice != '0': #exit condition is zero
		choice = input('\nWëbiérzë rozkôz: ')
		if choice == '-': #volume down
			tv.vol_minus()
		elif choice == '+': #volume up
			tv.vol_plus()
		elif choice == '1': #channel change
			tv.channel_change()
		elif choice == '2': #check channel and volume
			tv.check()
		elif choice == '0': #exit
			print('\nDo ùzdrzeniô!')
		else:
			print('\nlëchi wëbiér') #other choice statement

main() #calling main function