import sys
import string
from willie.module import commands

def string_to_num(txt):
    characters = '0123456789' + string.ascii_letters
    txt = txt.lower().strip()
    txt = ' '.join(txt.split())
    word_sums = 0
    for word in txt.split():
        word_sum = 0
        for letter in word:
            n = characters.index(letter)
            word_sum += n
        word_sums += word_sum
    return word_sums

def deconstruct(num):
    sum = 0
    for n in str(num):
        sum += int(n)
    if len(str(sum)) > 1:
        return deconstruct(sum)
    else:
        return sum

@commands('numb')
def stringnum(bot, trigger, found_match=None):
    try:
        txt = trigger[6:]
        num1 = string_to_num(txt)
        num2 = deconstruct(num1)
        bot.say(txt + ' = ' + str(num1) + ' -> ' + str(num2))
    except:
        bot.say('format must be alphanumeric')