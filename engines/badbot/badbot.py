from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
from typing import override
import chess
import random


class BadBot(MinimalEngine):
    @override
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:
        move = random.choice(list(board.legal_moves))
        return chess.engine.PlayResult(move, None)

    def evaluate(board: chess.Board) -> float:
        pass

    def minimax(board: chess.Board, depth: int, alpha: float, beta: float,
                maxing_player) -> float:
        pass
