from nonebot import on_command, CommandSession

@on_command('weather', aliases = ('天气'))
async def weather(session: CommandSession):
	city = session.get('city', prompt = '你把你城市给👴交了')
	weather_report = await get_weather_of_city(city)
	await session.send(weather_report)
	
@weather.args_parser
async def _(session: CommandSession):
	stripped_arg = session.current_arg_text.strip()
	
	if session.is_first_run:
		if stripped_arg:
			session.state['city'] = stripped_arg
		return
		
	if not stripped_arg:
		session.pause('你把你城市名给👴交了')
	
	session.state[session.current_key] = stripped_arg

async def get_weather_of_city(city: str) -> str:
	return "👴8知道"
		
