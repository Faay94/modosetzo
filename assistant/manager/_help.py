# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import *

START = """
🪅 **Menú Ayuda** 🪅

✘  /start : Comprueba que estoy vivo o no.
✘  /help : Recibe este mensaje.
"""

ADMINTOOLS = """✘ **AdminTools** ✘

• /pin : Ancla el mensaje respondido
• /pinned : Obtener mensaje anclado en el chat.
• /unpin : Desanclar el mensaje respondido
• /unpin all : Desanclar todos los mensajes anclados.

• /ban (username/id/reply) : Prohibir al usuario
• /unban (username/id/reply) : Anular la prohibición del usuario.

• /mute (username/id/reply) : Silenciar al usuario.
• /unmute (username/id/reply) : Activar el silencio del usuario.

• /tban (username/id/reply) (time) : Prohibición temporal 
• /tmute (username/id/reply) (time) : Temporal silencia un usuario.

• /purge (purge messages)

• /setgpic (reply photo) : mantener la foto de chat del grupo.
• /delgpic : eliminar la foto de chat actual."""

UTILITIES = """
✘ ** Utilities ** ✘

• /info (reply/username/id) : Obtén la info .
• /id : obtén chat/user id.
• /tr : traduce ..

• /paste (reply file/text) : pega texto en  Spaceb.in
• /meaning (text) : xd .
• /google (query) : busca en Google ..

• /suggest (query/reply) : crea una Yes / No encuesta .
"""

LOCKS = """
✘ ** Locks ** ✘

• /lock (query) : bloquean contenido .
• /unlock (query) : desbloquea contenido .

• All Queries
- `msgs` : for mensajes.
- `inlines` : for xd.
- `media` : for all medias.
- `games` : for games.
- `sticker` : for stickers.
- `polls` : for polls.
- `gif` : for gifs.
- `pin` : for pins.
- `changeinfo` : for change info right.
"""

MISC = """
✘  **Misc**  ✘

• /joke : Get Random Jokes.
• /decide : Decide Something..
"""

STRINGS = {"Admintools": ADMINTOOLS, "locks": LOCKS, "Utils": UTILITIES, "Misc": MISC}

MNGE = udB.get("MNGR_EMOJI") or "•"


def get_buttons():
    BTTS = []
    keys = STRINGS.copy()
    while keys:
        BT = []
        for i in list(keys)[:2]:
            text = MNGE + " " + i + " " + MNGE
            BT.append(Button.inline(text, "hlp_" + i))
            del keys[i]
        BTTS.append(BT)
    url = "https://t.me/" + asst.me.username + "?startgroup=true"
    BTTS.append([Button.url("Agregame", url)])
    return BTTS


@asst_cmd(pattern="help")
async def helpish(event):
    if not event.is_private:
        url = f"https://t.me/{asst.me.username}?start=start"
        return await event.reply(
            "Contactame en pv", buttons=Button.url("Click", url)
        )
    if str(event.sender_id) in owner_and_sudos() and (
        udB.get("DUAL_MODE") and (udB.get("DUAL_HNDLR") == "/")
    ):
        return
    BTTS = get_buttons()
    await event.reply(START, buttons=BTTS)


@callback("mngbtn", owner=True)
async def ehwhshd(e):
    buttons = get_buttons()
    buttons.append([Button.inline("<< Volver", "Abierto")])
    await e.edit(buttons=buttons)


@callback("mnghome")
async def home_aja(e):
    await e.edit(START, buttons=get_buttons())


@callback(re.compile("hlp_(.*)"))
async def do_something(event):
    match = event.pattern_match.group(1).decode("utf-8")
    await event.edit(STRINGS[match], buttons=Button.inline("<< Back", "mnghome"))
