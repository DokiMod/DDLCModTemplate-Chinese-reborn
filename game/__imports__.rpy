
# __imports__.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

python early:
    # For Achievements/Gallery
    import math 

    # For Credits
    import datetime

    # For Glitchtext
    import random

    # For Splash
    import re
    import os

    # For BSOD
    import subprocess
    import platform

    # For Gallery
    import threading
    import renpy.display.image as imgcore

init -19 python:
    persistent.enable_discord = True
    # For Discord RPC
    if persistent.enable_discord:
        from discord_rpc import DiscordRPC
        from pypresence import DiscordNotFound
        try:
            RPC = DiscordRPC("979471077187125248")
        except DiscordNotFound: pass
