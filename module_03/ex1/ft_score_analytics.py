import sys


def print_stats(argv: list[str]):
    print("=== Player Score Analytics ===")
    ind = 1
    argv_len = len(argv)
    if argv_len < 2:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return
    numbers = []
    while ind < argv_len:
        try:
            x = int(argv[ind])
            numbers.append(x)
        except ValueError as e:
            print("An error occured:", e)
        ind += 1
    print("Scores processed:", numbers)
    total_players = len(numbers)
    print("Total players:", total_players)
    total_score = sum(numbers)
    print("Total score:", total_score)
    print("Average score:", total_score / total_players)
    max_score = max(numbers)
    print("High score:", max_score)
    min_score = min(numbers)
    print("Low score:", min_score)
    print("Score range:", max_score - min_score)


if __name__ == "__main__":
    print_stats(sys.argv)
