from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
from typing import override
import chess
import math


class BadBot(MinimalEngine):
    @override
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:
        depth = 4
        move = self.get_move(board, depth)

        return chess.engine.PlayResult(move, None)

    def get_move(self, board, depth):
        top_move = None
        # Opposite of our minimax
        if board.turn == chess.WHITE:
            top_eval = -math.inf
        else:
            top_eval = math.inf

            for move in board.legal_moves:
                board.push(move)
                # WHEN WE ARE BLACK, WE WANT TRUE AND TO GRAB THE SMALLEST VALUE
                eval = self.minimax(board, depth - 1, -math.inf, math.inf, board.turn)

                board.pop()

                if board.turn == chess.WHITE:
                    if eval > top_eval:
                        top_move = move
                        top_eval = eval
                    else:
                        if eval < top_eval:
                            top_move = move
                            top_eval = eval

                            print("CHOSEN MOVE: ", top_move, "WITH EVAL: ", top_eval)
                            return top_move

    def evaluate(self, board: chess.Board) -> float:
        pass

    def minimax(self, board: chess.Board, depth: int, alpha: float,
                beta: float, maxing_player: bool) -> float:
        if depth == 0 or board.is_game_over():
            pass

        if maxing_player:
            max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = self.minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
            return max_eval
        else:
            min_eval = math.inf
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
