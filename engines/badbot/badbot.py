from lib.engine_wrapper import MinimalEngine
import lib.lichess_types as lichess_types
from typing import override
import chess
import random
import math


class BadBot(MinimalEngine):
    @override
    def search(self, board: chess.Board, time_limit: chess.engine.Limit,
               ponder: bool, draw_offered: bool,
               root_moves: lichess_types.MOVE) -> chess.engine.PlayResult:

                   depth = 2
                   score_best = float('-inf')
                   move_best = None

                   for move in board.legal_moves:
                       board.push(move)
                       score = self.minimax(board, depth -1, float('-inf'), float('inf'), False)
                       board.pop()

                       if score > score_best:
                           score_best = score
                           move_best = move

                   if move_best is None:
                       move_best = move = random.choice(list(board.legal_moves))
                   
                   return chess.engine.PlayResult(move_best, None)

    def evaluate(self, board: chess.Board) -> float:

        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
        }

        score = 0
        
        if board.is_checkmate():
            if board.turn:
                return float('-inf')
            else:
                return float('inf')


        #adds a miteral value to the amount of pieces on the board, ie if the opponent has less pieces of a higher value, 
        #return a higher score.
        for piece_type, value in piece_values.item():
            score += len(board.pieces(piece_type, chess.WHITE)) * value
            score -= len(board.pieces(piece_type, chess.BLACK)) * value
            
        if board.turn == chess.WHITE:
            return score
        else:
            return -score

    def minimax(self, board: chess.Board, depth: int, alpha: float, beta: float,
                maxing_player: bool) -> float:
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
