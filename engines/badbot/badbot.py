from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
import chess
import random


class BadBot(MinimalEngine):
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:
        move = random.choice(list(board.legal_moves))
        return chess.engine.PlayResult(move, None)
