from pyrogram import Filters
from asyncio import sleep

from nana import app, Command, AdminSettings
from nana.helpers.PyroHelpers import msg
from nana.helpers.string import replace_text
from nana.helpers.aiohttp_helper import AioHttp

__MODULE__ = "Urban"
__HELP__ = """
Search for urban dictionary

──「 **Urban Dictionary** 」──
-> `ud (text or reply to a word)`
Search urban for dictionary
"""


@app.on_message(Filters.user(AdminSettings) & Filters.command("ud", Command))
async def urban_dictionary(_client, message):
    if len(message.text.split()) == 1:
        await msg(message, text="Usage: `ud example`")
        return
    try:
        text = message.text.split(None, 1)[1]
        response = await AioHttp().get_json(f"http://api.urbandictionary.com/v0/define?term={text}")
        word = response['list'][0]['word']
        definition = response['list'][0]['definition']
        example = response['list'][0]['example']
        teks = f"**Text: {replace_text(word)}**\n**Meaning:**\n`{replace_text(definition)}`\n\n**Example:**\n`{replace_text(example)}`"
        await msg(message, text=teks)
        return
    except Exception as e:
            await msg(message, text="`The Unban Dictionary API could not be reached`")
            print(e)
            await sleep(3)
            await message.delete()
