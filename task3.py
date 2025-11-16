order = 0


def print_towers(towers):
    print("\nСтан башт:")
    for name in ["A", "B", "C"]:
        print(f"{name}: {towers[name]}")


def move_disk(n, source, target, auxiliary, towers):
    global order
    order += 1
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Крок #{order} | Перемістити диск {disk} з {source} на {target}")
        print_towers(towers)
    else:
        move_disk(n - 1, source, auxiliary, target, towers)
        move_disk(1, source, target, auxiliary, towers)
        move_disk(n - 1, auxiliary, target, source, towers)


def hanoi_with_state(n):
    towers = {"A": list(reversed(range(1, n + 1))), "B": [], "C": []}
    print("Початковий стан:")
    print_towers(towers)
    move_disk(n, "A", "C", "B", towers)


def calculate_hanoi_moves(n):
    return 2**n - 1


if __name__ == "__main__":
    try:
        disks = int(input("Введіть кількість дисків: "))
        steps = calculate_hanoi_moves(disks)
        print(f"Рішення для {disks} дисків потребуватиме: {steps} кроків.")
        if disks < 1:
            print("Кількість дисків має бути більше 0.")
        else:
            hanoi_with_state(disks)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
