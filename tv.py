class Tv(object):

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
		volume = int(self.volume)
		volume +=1
		if volume >= 10:
			volume = 10
		self.volume = str(volume)
		print('\ngłosnosc\n'+' |' * volume)

	def vol_minus(self):
		volume = int(self.volume)
		volume -=1
		if volume <= 0:
			volume = 0
		self.volume = str(volume)
		print('\ngłosnosc\n'+' |' * volume)

	def channel_change(self):
		channel = int(self.channel)
		chanChange = int(input('\nPodôj numrã karnôlu: '))
		if chanChange in range(1,101):
			channel = chanChange
			print('karnôl '+str(channel))
		else:
			print('Ni ma taczégò karnôlu.')
		self.channel = str(channel)

	def check(self):
		print('\nkarnôl '+self.channel+'\ngłosnosc '+self.volume)

def main():
	tv = Tv()
	print("""
		0 - skùńczë
		1 - zmieni karnôl
		2 - sprôwdzë karnôl i głosnosc
		- - zmiészi głosnosc
		+ - zwikszi głosnosc""")
	choice = None
	while choice != '0':
		choice = input('\nWëbiérzë rozkôz: ')
		if choice == '-':
			tv.vol_minus()
		elif choice == '+':
			tv.vol_plus()
		elif choice == '1':
			tv.channel_change()
		elif choice == '2':
			tv.check()
		elif choice == '0':
			print('\nDo ùzdrzeniô!')
		else:
			print('\nlëchi wëbiér')
main()