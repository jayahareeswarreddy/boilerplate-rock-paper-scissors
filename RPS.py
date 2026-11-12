
import random

def player(prev_play, opponent_history=[], my_history=[]):

    counter = {"R": "P", "P": "S", "S": "R"}
    moves = ["R", "P", "S"]

    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
    else:
        opponent_history.append(prev_play)

    def predict_quincy(i, history):
        choices = ["R", "R", "P", "P", "S"]
        return choices[(i + 1) % 5]

    def predict_kris(i, history):
        if i == 0:
            return "R"
        return counter[history[i - 1]]

    def predict_mrugesh(i, history):
        previous = [""] + history[:i]
        last_ten = previous[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        if most_frequent == "":
            most_frequent = "S"
        return counter[most_frequent]

    def predict_abbey(i, history):
        previous = ["R"] + history[:i]
        play_order = {}

        for j in range(1, len(previous)):
            pair = previous[j - 1] + previous[j]
            play_order[pair] = play_order.get(pair, 0) + 1

        last_move = previous[-1]
        potential = [
            last_move + "R",
            last_move + "P",
            last_move + "S"
        ]

        prediction = max(
            potential,
            key=lambda x: play_order.get(x, 0)
        )[-1]

        return counter[prediction]

    predictors = [
        predict_quincy,
        predict_kris,
        predict_mrugesh,
        predict_abbey
    ]

    if not opponent_history:
        next_move = random.choice(moves)
    else:
        scores = []

        for predictor in predictors:
            score = 0

            for i, actual in enumerate(opponent_history):
                expected = predictor(i, my_history)

                if expected == actual:
                    score += 1

            scores.append(score)

        best = scores.index(max(scores))
        predicted = predictors[best](len(my_history), my_history)
        next_move = counter[predicted]

    my_history.append(next_move)
    return next_move
