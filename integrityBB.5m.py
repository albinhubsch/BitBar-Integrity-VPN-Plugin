#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <bitbar.title>Integrity VPN check</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Albin Hubsch - albin.hubsch@gmail.com</bitbar.author>
# <bitbar.author.github>albinhubsch</bitbar.author.github>
# <bitbar.desc>Short description of what your plugin does.</bitbar.desc>
# <bitbar.image> ...image </bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/albinhubsch/BitBar-Integrity-VPN-Plugin</bitbar.abouturl>

# Imports
import urllib2

# Vars
url = "https://integrity.st/"
match = {'good': 'Hey, you are connecting via Integrity right now!',
			'bad': "You are not connecting via Integrity right now!"}

icon = {'good': "👻",
			'bad': "🚫"}

message = {'short': '',
			'long': ''}

# Send request to Integrity.st
try:
	request = urllib2.urlopen(url, timeout=4).read()
except Exception, e:
	print 'Error: '+e.message
	exit()

# Check result
if match['bad'] in request:
	message['short'] = icon['bad']
	message['long'] = match['bad']
elif match['good'] in request:
	message['short'] = icon['good']
	message['long'] = match['good']
else:
	message['short'] = ' Error'
	message['long'] = 'Something went wrong fetching Integrity status'

# Print results
print message['short']
print '---'
print message['long'] + '| href=https://integrity.st/'