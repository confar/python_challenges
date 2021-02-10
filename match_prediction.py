def get_winner(score):
    if score[1] == score[0]:
        return [False, False]
    return score[0] > score[1], score[1] > score[0]


def prediction(pred, real):
    pred = tuple(pred.split(':'))
    real = tuple(real.split(':'))
    if pred == real:
        return 2
    if get_winner(pred) == get_winner(real):
        return 1
    else:
        return 0


assert prediction('1:2', "1:2") == 2
assert prediction('1:1', "1:1") == 2
assert prediction('2:1', "5:1") == 1
assert prediction('2:30', "5:1") == 0
