# -*- coding:utf-8 -*-

"""
    WeChat KUAKUA_Robot v0.1
"""


import itchat, re
from itchat.content import *
import random
import json

"""
    Constants
"""

REPLY = {'夸我': [
        u'你真是太优秀！',
        u'啥也不说了，你真棒！',
        u'每天看到你心情好呢！',
        u'你真是一位可爱的小天使啊！',
        u'一看你就是美丽与善良的化身 夸！',
        u'你上辈子一定拯救了银河系吧，优秀！',
        u'德才兼备说的就是你这样的社会主义接班人！',
        u'你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！',
        u'有人说你不好看，我二话不说给他买了只导盲犬！',
        u'看着你，工作日的下午茶都要甜上几分',
        u'说星星好看的人一定没有见过你的眼睛',
        u'有颜就是任性啊...(ಥ _ ಥ)',
        u'好喜欢你啊',
        u'求求你不要在用脸蛋来杀人了, 我已经厌倦了在你面前反复去世',
        u'你一定是上帝派来拯救我的天使',
        u'快停止散发魅力吧，你这个浑身充满荷尔蒙的家伙！',
        u'上辈子可能是碳酸饮料，一见到你我就开心得冒泡',
        u'天神下凡',
        u'请节制你那让人欲罢不能的帅气！',
        u'你简直就是人类美学的奇迹',
        u'你真好看',
        u'月色与血色之间，你就是那第三种绝色',
        u'绕地球9999圈赶来朝拜你的容颜！',
        u'你的名字，是我见过最短的情诗',
        u'过分帅气可是违法的哦'],
    'default': [
        u'太棒了！',
        u'真不错！',
        u'好开心！',
        u'嗯哪！',
        u'没什么好说的了，我送你一道彩虹屁吧！']}


@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    # 这里一定要修改成你想加群的群的名称  
    if msg['User']['NickName'] == u'<你的群名称>':
        print('Message from: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)
        print('MSG: %s' % msg['Text'])
        match = re.search(u'夸我', msg['Text']) or re.search(u'求夸', msg['Text']) or re.search(u'夸一下', msg['Text'])

        print('isAt is:%s' % msg['isAt'])
        if match or msg['isAt']:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('夸我 is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['夸我']) - 1)
            itchat.send('@%s\n%s' % (username, REPLY['夸我'][randomIdx]), msg['FromUserName'])
        elif msg['isAt']:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('@%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+' * 5)


itchat.auto_login(enableCmdQR=-2, hotReload=True)
itchat.run()
