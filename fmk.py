from willie.module import commands
from willie.tools import Identifier
import random

@commands('fmk')
def fmk(bot, trigger, found_match=None):

	nicks = trigger[5:].strip().split()

	if len(nicks) == 0:
		nicks = bot.privileges[Identifier(trigger.sender)].keys()
	else:
		if len(nicks) != 3:
			bot.say('you must pick 3 persons')
			return

	random.shuffle(nicks)
	
	s = 'fuck ' + nicks[0] + ', marry ' + nicks[1] + ', kill ' + nicks[2]

	bot.say(s)

