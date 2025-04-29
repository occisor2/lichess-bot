import chess

pawn_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]


knight_table = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]


bishop_table = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]


rook_table = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]


queen_table = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]


king_table = [
    20, 30, -5, 0, -5, -5, 30, 20,
    20, 20, -5, -5, -5, -5, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]


def evaluate(board: chess.Board) -> float:
    white_pawns = sum(pawn_table[pos] for pos in
                      board.pieces(chess.PAWN, chess.WHITE))
    white_kights = sum(knight_table[pos] for pos in
                       board.pieces(chess.KNIGHT, chess.WHITE))
    white_bishops = sum(bishop_table[pos] for pos in
                        board.pieces(chess.BISHOP, chess.WHITE))
    white_rooks = sum(rook_table[pos] for pos in
                      board.pieces(chess.ROOK, chess.WHITE))
    white_queen = sum(queen_table[pos] for pos in
                      board.pieces(chess.QUEEN, chess.WHITE))
    white_king = sum(king_table[pos] for pos in
                     board.pieces(chess.KING, chess.WHITE))
    white = white_pawns + white_kights + white_bishops + \
        white_rooks + white_queen + white_king

    black_pawns = sum(pawn_table[pos] for pos in
                      board.pieces(chess.PAWN, chess.BLACK).mirror())
    black_kights = sum(knight_table[pos] for pos in
                       board.pieces(chess.KNIGHT, chess.BLACK).mirror())
    black_bishops = sum(bishop_table[pos] for pos in
                        board.pieces(chess.BISHOP, chess.BLACK).mirror())
    black_rooks = sum(rook_table[pos] for pos in
                      board.pieces(chess.ROOK, chess.BLACK).mirror())
    black_queen = sum(queen_table[pos] for pos in
                      board.pieces(chess.QUEEN, chess.BLACK).mirror())
    black_king = sum(king_table[pos] for pos in
                     board.pieces(chess.KING, chess.BLACK).mirror())
    black = black_pawns + black_kights + black_bishops + \
        black_rooks + black_queen + black_king

    return white - black
