import matplotlib.pyplot as plt
import numpy as np


def koch_curve(p1, p2, level):
    if level == 0:
        return [p1, p2]
    else:
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = (p2 - p1) / 3
        p3 = p1 + delta
        p5 = p2 - delta
        angle = np.pi / 3
        rotation = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )
        p4 = p3 + rotation @ (delta)
        return (
            koch_curve(p1, p3, level - 1)
            + koch_curve(p3, p4, level - 1)[1:]
            + koch_curve(p4, p5, level - 1)[1:]
            + koch_curve(p5, p2, level - 1)[1:]
        )


def draw_snowflake(level):
    points = []
    size = 1.0
    angles = [0, -120, 120]
    for i in range(3):
        angle_rad = np.radians(angles[i])
        start = (np.cos(angle_rad) * size, np.sin(angle_rad) * size)
        end = (
            np.cos(np.radians(angles[(i + 1) % 3])) * size,
            np.sin(np.radians(angles[(i + 1) % 3])) * size,
        )
        segment = koch_curve(start, end, level)
        points.extend(segment[:-1])
    points.append(points[0])
    x, y = zip(*points)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color="black")
    plt.axis("equal")
    plt.axis("off")
    plt.savefig("koch_snowflake.png", bbox_inches="tight")
    print("Зображення збережено як koch_snowflake.png")


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії (0–5): "))
    draw_snowflake(level)
