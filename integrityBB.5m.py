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

import urllib2

url = "https://integrity.st/"
bad_match = "You are not connecting via Integrity right now!"
good_match = ""

bad_icon = '⛔'
good_icon = '😎'
msg_short = ''
msg_long = ''

request = urllib2.urlopen(url).read()

if bad_match in request:
	msg_short = bad_icon
	msg_long = 'You are not connecting via Integrity right now!'
elif good_match in request:
	msg_short = good_icon
	msg_long = 'Awesome! You\'re surfing like them!'
else:
	msg_short = ' Error'
	msg_long = 'Something went wrong fetching Integrity status'

print 'VPN:' + msg_short
print '---'
print msg_long + '| href=https://integrity.st/'