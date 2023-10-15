from datetime import datetime

import vestaboard
from loguru import logger

from . import ENV

logger.add(sink="main.log", level="INFO")

if __name__ == "__main__":
    installation = vestaboard.Installable(
        ENV["KEY"], ENV["SECRET"], saveCredentials=False
    )
    board = vestaboard.Board(installation)
    now = datetime.now()
    board.post(f"TEST {now}")