# name=Arturia DBI

# MIDI MESSAGES
# Byte data: [ STATUS | DATA 1 | DATA 2 ]

import utils

"""
Stop Button
On:
	176
	240
	252
Off:
	176
	
Standard notes
On:
	144
Off:
	128
"""

EventNameT = ['Note Off', 'Note On ', 'Key Aftertouch', 'Control Change','Program Change',  'Channel Aftertouch', 'Pitch Bend', 'System Message' ]

def OnInit():
	print("Rick Howell - Basic DBI Script")

def OnMidiIn(event):
	if event.status != 144 and event.status != 128:
		event.handled = True

def OnMidiMsg(event):
	# TODO : Step Repeat does not get recorded
	event.handled = False
	print("{:X} {:X} {:2X} {}".format(event.status, event.data1, event.data2, EventNameT[(event.status - 0x80) // 16] + ': ' + utils.GetNoteName(event.data1)))

