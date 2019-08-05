from os import path

import nonebot

import config

if __name == '__main__':
	nonebot.init(config)
	nonebot.load_builtin_plugins()
	nonebot.run()