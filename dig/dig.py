import dns.resolver

def dig():
	answers = dns.resolver.resolve('yandex.ru', 'AAAA')
	for rdata in answers:
		print(type(rdata))
		print(repr(rdata))
		# print('1. ' + str(rdata))
		#print('Host', rdata.exchange, 'has preference', rdata.preference)

def txt():
	answers = dns.resolver.resolve('enigma.code.energy', 'TXT')
	for rdata in answers:
		print(type(rdata))
		print(repr(rdata))
		# print('1. ' + str(rdata))
		#print('Host', rdata.exchange, 'has preference', rdata.preference)

txt()
