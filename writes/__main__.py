import random
import sys
from datetime import datetime

import vestaboard
from loguru import logger

from . import ENV
from .words import ADJECTIVES, BODY_PARTS, PROCEDURES

logger.add(sink="main.log", level="INFO")

def _get_proc_body_adj():
    return (
        random.choice(ADJECTIVES),
        random.choice(BODY_PARTS),
        random.choice(PROCEDURES),
    )

if __name__ == "__main__":
    name = sys.argv[1]
    installation = vestaboard.Installable(
        ENV["KEY"], ENV["SECRET"], saveCredentials=False
    )
    board = vestaboard.Board(installation)
    now = datetime.now()
    date = now.strftime("%m.%d.%Y")
    time = now.strftime("%I:%M%p")
    procedure = _get_proc_body_adj()
    board.post(f"EMERGENCY PROCEDURES\n{date} {time}\n\nPATIENT: {name}\n{procedure[0]} {procedure[1]}\n{procedure[2]}")