from nonebot import on_command, CommandSession
import requests

def get_daily_content():
	url = 'http://open.iciba.com/dsapi/'
	daily_content = requests.get(url)
	daily_content_english = daily_content.json()['content']
	daily_content_chinese = daily_content.json()['note']
	return [daily_content_english, daily_content_chinese]

@on_command('daily', aliases = ('每日一句', ))
async def daily(session: CommandSession):
	daily_send = await get_daily()
	await session.send("金山词霸每日一句")
	await session.send(daily_send[0] + '\n' +  daily_send[1])
	
async def get_daily():
	daily_sentence = get_daily_content()
	return daily_sentence