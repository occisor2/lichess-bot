from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
from typing import override
import chess
import math
import random
import time
from . import piece_tables


class BadBot(MinimalEngine):
    """simple and bad chess bot"""
    @override
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:
        depth = 3

        self.nodes_searched = 0
        self.cut_nodes = 0

        start = time.perf_counter_ns()
        move = self.minimax(board, depth)
        stop = time.perf_counter_ns()

        t = round((stop - start)/1000000)
        print(f'Search Time: {t}ms')
        print(f'Nodes searched: {self.nodes_searched}')
        print(f'Nodes cut: {self.cut_nodes}')

        return chess.engine.PlayResult(move, None)

    def evaluate(self, board: chess.Board) -> float:
        """
        Evaluate the board.
        """
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 6,
            chess.QUEEN: 9,
        }
        color = 1 if board.turn == chess.WHITE else -1
        score = 0

        if board.is_checkmate():
            return math.inf

        white_material = 0
        black_material = 0
        material = 0
        for piece_type, value in piece_values.items():
            white_material += len(board.pieces(piece_type, chess.WHITE)) * value
            black_material += len(board.pieces(piece_type, chess.BLACK)) * value

        material = (white_material - black_material) * color
        position = piece_tables.evaluate(board) * color

        score = material + position

        return score

    def minimax(self, board: chess.Board, depth: int) -> chess.Move:
        """Alpha-Beta Pruning minimax implementation using a negamax
        variant"""
        def minimax(board: chess.Board, depth: int, alpha: float,
                    beta: float, turn) -> float:
            if depth == 0 or board.is_game_over():
                return self.evaluate(board) * turn

            moves = board.legal_moves
            value = -math.inf

            for move in moves:
                board.push(move)  # update the board to this move
                value = max(value, -minimax(board, depth - 1, -beta,
                                            -alpha, -turn))
                board.pop()  # restore board to previous move
                alpha = max(alpha, value)
                self.nodes_searched += 1
                if alpha >= beta:
                    self.cut_nodes += 1
                    break

            return value

        moves = []
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, -math.inf, math.inf, 1)
            board.pop()
            moves.append((move, score))

        # Choose randomly among best or worst moves if they are tied
        best_score = max(moves, key=lambda m: m[1])[1] \
            if depth % 2 == 0 else min(moves, key=lambda m: m[1])[1]
        best_moves = [m[0] for m in moves if m[1] == best_score]
        best = random.choice(best_moves)

        return best
