# coding: utf-8

import random
from willie.module import commands

@commands('decide')
def decide(bot, trigger, found_match=None):

	args = ' '.join(trigger.strip().split())

	if args == '.decide':
		return

	if ',' not in args:
		arg_list = args[8:].split()
	else:
		arg_list = args[8:].split(',')

	if arg_list.count(arg_list[0]) == len(arg_list):
		bot.say('it seems you already know')
	else:
		bot.say(random.choice(arg_list).strip())
