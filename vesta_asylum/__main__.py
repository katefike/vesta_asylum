import vestaboard
import sys
from loguru import logger
import random

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
    procedure = _get_proc_body_adj()
    board.post(f"{name}'s\n{procedure[0]}\n{procedure[1]}\n{procedure[2]}")