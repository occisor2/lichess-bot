from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
from typing import override
import chess
import math
import random


class BadBot(MinimalEngine):
    """simple and bad chess bot"""
    @override
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:
        depth = 3
        move = self.minimax(board, depth)

        return chess.engine.PlayResult(move, None)

    def evaluate(self, board: chess.Board) -> float:
        """Evaluate the board using a material score"""
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
        }
        score = 0

        if board.is_checkmate():
            return math.inf

        white_material = 0
        black_material = 0
        for piece_type, value in piece_values.items():
            white_material += len(board.pieces(piece_type, chess.WHITE)) * value
            black_material += len(board.pieces(piece_type, chess.BLACK)) * value

        score = (white_material - black_material)

        return score

    def minimax(self, board: chess.Board, depth: int) -> chess.Move:
        """Alpha-Beta Pruning minimax implementation using a negamax
        variant"""
        def minimax(board: chess.Board, depth: int, alpha: float,
                    beta: float, maxing_player: bool) -> float:
            if depth == 0 or board.is_game_over():
                turn = 1 if maxing_player else -1
                return self.evaluate(board) * turn

            moves = board.legal_moves
            value = -math.inf

            for move in moves:
                board.push(move)  # update the board to this move
                value = max(value, -minimax(board, depth - 1, -beta,
                                            -alpha, not maxing_player))
                board.pop()  # restore board to previous move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return value

        print('MOVES')
        moves = []
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, -math.inf, math.inf, False)
            board.pop()
            print(f'move: "{move}", score: {score}')
            moves.append((move, score))

        # Choose randomly among best or worst moves if they are tied
        best_score = max(moves, key=lambda m: m[1])[1] \
            if depth % 2 == 0 else min(moves, key=lambda m: m[1])[1]
        best_moves = [m[0] for m in moves if m[1] == best_score]
        best = random.choice(best_moves)

        print(f'BEST: {best}, {best_score}')

        return best
