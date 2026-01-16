import math


def euclidien_dist(x: tuple, y: tuple) -> float:
    ind = 0
    s = 0
    while ind < 3:
        s += (y[ind] - x[ind]) ** 2
        ind += 1
    return math.sqrt(s)


def parse_string_cords(str_pos: str):
    splitted = str_pos.split(',')
    ind = 0
    try:
        while ind < 3:
            splitted[ind] = int(splitted[ind])
            ind += 1
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(
            "Error details - Type: ValueError, "
            f"Args: {e.args}"
            )
        return
    else:
        return tuple(splitted)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    pos = (10, 20, 5)
    print("\nPosition created:", pos)
    ref = (0, 0, 0)
    distance_to_ref = euclidien_dist(ref, pos)
    print(f"Distance between {ref} and {pos}: {distance_to_ref}")

    str_pos = "10, 20, 30"
    print(f'\nParsing coordinates: "{str_pos}"')
    pos = parse_string_cords(str_pos=str_pos)
    if pos is not None:
        print("Parsed position:", pos)
        print(f"Distance between {ref} and {pos}:", euclidien_dist(pos, ref))

    str_pos = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{str_pos}"')
    err_pos = parse_string_cords(str_pos=str_pos)

    print("\nUnpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
