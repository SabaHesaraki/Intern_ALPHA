x = 0
y = 0
direction = "north"

while True:
    command = input("robot> ").split()

    match command:
        case ["quit"]:
            break

        case ["status"]:
            print(f"at ({x}, {y}) facing {direction}")

        case ["move", steps] if steps.isdigit():
            steps = int(steps)

            match direction:
                case "north":
                    y += steps
                case "east":
                    x += steps
                case "south":
                    y -= steps
                case "west":
                    x -= steps

            print(f"at ({x}, {y}) facing {direction}")

        case ["turn", "right"]:
            if direction == "north":
                direction = "east"
            elif direction == "east":
                direction = "south"
            elif direction == "south":
                direction = "west"
            else:
                direction = "north"

            print(f"at ({x}, {y}) facing {direction}")

        case ["turn", "left"]:
            if direction == "north":
                direction = "west"
            elif direction == "west":
                direction = "south"
            elif direction == "south":
                direction = "east"
            else:
                direction = "north"

            print(f"at ({x}, {y}) facing {direction}")

        case ["teleport", new_x, new_y] if new_x.lstrip("-").isdigit() and new_y.lstrip("-").isdigit():
            x = int(new_x)
            y = int(new_y)
            print(f"at ({x}, {y}) facing {direction}")

        case _:
            print("unknown command")

