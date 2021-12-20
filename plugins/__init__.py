# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio
import os
import time
from random import choice

from pyUltroid import *
from pyUltroid.dB import ULTROID_IMAGES
from pyUltroid.functions.helper import *
from pyUltroid.functions.info import *
from pyUltroid.functions.misc import *
from pyUltroid.functions.tools import *
from pyUltroid.misc._assistant import asst_cmd, callback, in_pattern
from pyUltroid.misc._decorators import ultroid_cmd
from pyUltroid.misc._wrappers import eod, eor
from pyUltroid.version import __version__, ultroid_version
from telethon import Button, events
from telethon.tl import functions, types

from strings import get_string

Redis = udB.get
client = bot = ultroid_bot

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id
LOG_CHANNEL = int(udB.get("LOG_CHANNEL"))
INLINE_PIC = udB.get("INLINE_PIC") or choice(ULTROID_IMAGES)
if INLINE_PIC == "False":
    INLINE_PIC = None
Telegraph = telegraph_client()

List = []
Dict = {}
N = 0

STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # UltroidSupport
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
]

KANGING_STR = [
    "Llamando al presidente para robar tu sticker...",
    "Setzo hehe...",
    "Setzo pal sticker hehe...",
    "Robando Sticker...",
    "Hey,  buen sticker, lo robaré..",
    "Espera lo robo...",
    "Al parecer este sticker va pa mi pack...",
    "Aquí te verás mejor",
    "Secuestrando sticker...",
    "Robando sticker pa... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
