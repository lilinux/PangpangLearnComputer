#!/usr/bin/env python
#coding: utf8

letters = 'ABC123456789'

tips = (
    '宝包请按%s',
    '宝包你按了%s吗',
    '宝包再按一下%s',
)

good_msg = (
    '太棒了, 宝包答对了',
    '宝包真厉害',
)

bad_msg = (
    '只差一点了, 别灰心',
    '没有答对, 再试一次吧',
)

from random import choice
from os import environ
from utils import getch, say

l = choice(letters)

while True:
    say(choice(tips), l)
    if environ.get('TISHI'):
        print(l)
        lb = getch().upper()
        print(lb)
    else:
        lb = getch().upper()
    if lb == l:
        say(choice(good_msg))
        break
    else:
        say(choice(bad_msg))
