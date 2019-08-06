from nonebot import on_command, CommandSession

@on_command('help', aliases = ('帮助', '说明', '说明书'))
async def help(session: CommandSession):
	plugins = nonebot.plugin.get_loaded_plugins()
	await session.send(plugins)