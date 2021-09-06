def find_total_score_combinations(final_score, individual_plays):

    return find_score_combinations_rec(final_score, individual_plays, 0)
    # return final_score_combinations_dp(final_score, individual_plays)


def find_score_combinations_rec(final_score, individual_plays, index):
    if index >= len(individual_plays):
        return 0

    if individual_plays[index] == final_score:
        return 1
    with_play_included, with_play_excluded = 0, 0

    if individual_plays[index] <= final_score:
        with_play_included = find_score_combinations_rec(final_score - individual_plays[index], individual_plays,
                                                           index)

    with_play_excluded = find_score_combinations_rec(final_score, individual_plays, index+1)

    return with_play_excluded + with_play_included


def final_score_combinations_dp(final_score, individual_plays):
    dp = [[0 for _ in range(final_score+1)] for _ in range(len(individual_plays))]
    for i in range(final_score+1):
        dp[0][i] = 1 if individual_plays[0] == i else 0
    for i in range(len(individual_plays)):
        dp[i][0] = 1

    for i in range(1, len(individual_plays)):
        for j in range(1, final_score + 1):
            with_cur_play = dp[i-1][j-individual_plays[i]]+1
            without_cur_play = dp[i-1][j]
            dp[i][j] = with_cur_play + without_cur_play
    return dp[-1][-1]


if __name__ == '__main__':
    print(final_score_combinations_dp(12, [2, 3,7]))
    print(find_total_score_combinations(12, [2, 3,7]))
