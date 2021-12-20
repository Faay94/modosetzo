# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from datetime import datetime

from pytz import timezone as tz
from pyUltroid.dB.asst_fns import *
from pyUltroid.dB.sudos import is_fullsudo
from pyUltroid.functions.helper import inline_mention
from pyUltroid.misc import owner_and_sudos
from telethon import Button, events
from telethon.utils import get_display_name

from strings.strings import get_string

from . import *

Owner_info_msg = (
    udB.get("BOT_INFO_START")
    or f"""
**Owner** - {OWNER_NAME}
**OwnerID** - `{OWNER_ID}`

**Message Forwards** - {udB.get("PMBOT")}

**Ultroid [v{ultroid_version}](https://github.com/TeamUltroid/Ultroid), powered by @TeamUltroid**
"""
)

_settings = [
    [
        Button.inline("API Kᴇʏs", data="apiset"),
        Button.inline("Bot PM", data="chatbot"),
    ],
    [
        Button.inline("Live User", data="alvcstm"),
        Button.inline("Anti Chats", data="ppmset"),
    ],
    [
        Button.inline("FTS", data="otvars"),
        Button.inline("VC Bᴏᴛ", data="vcb"),
    ],
    [Button.inline("« Volver", data="mainmenu")],
]

_start = [
    [
        Button.inline("Idioma 🌐", data="lang"),
        Button.inline("Configuraciones ⚙️", data="setter"),
    ],
    [
        Button.inline("Estadísticas ✨", data="stat"),
        Button.inline("GBL 📻", data="bcast"),
    ],
    [Button.inline("Zona 🌎", data="tz")],
]


@callback("ownerinfo")
async def own(event):
    await event.edit(
        Owner_info_msg,
        buttons=[Button.inline("Close", data="closeit")],
        link_preview=False,
    )


@callback("closeit")
async def closet(lol):
    await lol.delete()


@asst_cmd(pattern="start ?(.*)", forwards=False, func=lambda x: not x.is_group)
async def ultroid(event):
    if not is_added(event.sender_id) and str(event.sender_id) not in owner_and_sudos():
        add_user(event.sender_id)
        kak_uiw = udB.get("OFF_START_LOG")
        if not kak_uiw or kak_uiw != "True":
            msg = f"{inline_mention(event.sender)} `[{event.sender_id}]` started your [Assistant bot](@{asst.me.username})."
            buttons = [[Button.inline("Info", "itkkstyo")]]
            if event.sender.username:
                buttons[0].append(Button.url("User", "t.me/" + event.sender.username))
            await event.client.send_message(
                int(udB["LOG_CHANNEL"]), msg, buttons=buttons
            )
    if (event.sender_id != OWNER_ID) and not is_fullsudo(event.sender_id):
        ok = ""
        u = await event.client.get_entity(event.chat_id)
        if not udB.get("STARTMSG"):
            if udB.get("PMBOT") == "True":
                ok = "Iniciaste el userbot, puedes enviar un mensaje o simplemente irte alv ."
            await event.reply(
                f"Hola [{get_display_name(u)}](tg://user?id={u.id}), UserBot xd [{ultroid_bot.me.first_name}](tg://user?id={ultroid_bot.uid})!\n\n{ok}",
                file=udB.get("STARTMEDIA"),
                buttons=[Button.inline("Info.", data="ownerinfo")]
                if Owner_info_msg != "False"
                else None,
            )
        else:
            me = f"[{ultroid_bot.me.first_name}](tg://user?id={ultroid_bot.uid})"
            mention = f"[{get_display_name(u)}](tg://user?id={u.id})"
            await event.reply(
                udB.get("STARTMSG").format(me=me, mention=mention),
                file=udB.get("STARTMEDIA"),
                buttons=[Button.inline("Info.", data="ownerinfo")],
            )
    else:
        name = get_display_name(event.sender_id)
        if event.pattern_match.group(1) == "set":
            await event.reply(
                "Selecciona una opción-",
                buttons=_settings,
            )
        else:
            await event.reply(
                get_string("ast_3").format(name),
                buttons=_start,
            )


@callback("itkkstyo", owner=True)
async def ekekdhdb(e):
    text = f"Cuándo el nuevo visitante visitará su Assistant Bot. Recibirá este mensaje de registro. !\n\nPara deshabilitar : {HNDLR}setredis OFF_START_LOG True"
    await e.answer(text, alert=True)


@callback("mainmenu", owner=True, func=lambda x: not x.is_group)
async def ultroid(event):
    await event.edit(
        get_string("ast_3").format(OWNER_NAME),
        buttons=_start,
    )


@callback("stat", owner=True)
async def botstat(event):
    ok = len(get_all_users())
    msg = """Ultroid Assistant - Stats
Total Users - {}""".format(
        ok,
    )
    await event.answer(msg, cache_time=0, alert=True)


@callback("bcast", owner=True)
async def bdcast(event):
    ok = get_all_users()
    await event.edit(f"• Broadcast to {len(ok)} users.")
    async with event.client.conversation(OWNER_ID) as conv:
        await conv.send_message(
            "Introduzca el mensaje de difusión.\nUsar /cancel para detener la difusión.",
        )
        response = await conv.get_response()
        if response.message == "/cancel":
            return await conv.send_message("Cancelled!!")
        success = 0
        fail = 0
        await conv.send_message(f"Iniciar una transmisión {len(ok)} users...")
        start = datetime.now()
        for i in ok:
            try:
                await asst.send_message(int(i), response.message)
                success += 1
            except BaseException:
                fail += 1
        end = datetime.now()
        time_taken = (end - start).seconds
        await conv.send_message(
            f"""
**Broadcast completed in {time_taken} seconds.**
Total Users in Bot - {len(ok)}
**Sent to** : `{success} users.`
**Failed for** : `{fail} user(s).`""",
        )


@callback("setter", owner=True)
async def setting(event):
    await event.edit(
        "Elija entre las siguientes opciones -",
        buttons=_settings,
    )


@callback("tz", owner=True)
async def timezone_(event):
    await event.delete()
    pru = event.sender_id
    var = "TIMEZONE"
    name = "Timezone"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            "Envíe su zona horaria desde esta lista [Ver desde aquí](http://www.timezoneconverter.com/cgi-bin/findzone.tzc)"
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("mainmenu"),
            )
        try:
            tz(themssg)
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} changed to {themssg}\n",
                buttons=get_back_button("mainmenu"),
            )
        except BaseException:
            await conv.send_message(
                "Wrong TimeZone, Try again",
                buttons=get_back_button("mainmenu"),
            )
