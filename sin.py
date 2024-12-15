import os

import matplotlib.pyplot as plt
import numpy as np


def f(t):
    result = np.zeros_like(t)
    result[(t >= 0) & (t < np.pi / 2)] = -np.sin(t[(t >= 0) & (t < np.pi / 2)])
    result[(t >= np.pi / 2) & (t < np.pi)] = 0
    result[(t >= np.pi) & (t < np.pi * 3 / 2)] = 0
    result[(t >= np.pi * 3 / 2) & (t < np.pi * 2)] = -np.sin(t[(t >= np.pi * 3 / 2) & (t < np.pi * 2)])
    return result


def cyclic_function(t):
    period = 2 * np.pi
    return f((t % period + period) % period)


gt = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
y = cyclic_function(gt)

for k in range(-8, 9):
    mask = ~(np.isclose(gt, k * np.pi / 2))
    gt = gt[mask]
    y = y[mask]

plt.figure(figsize=(10, 4))
plt.plot(gt, y, label='По синусам')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

r = 8
for k in range(-r, r + 1):
    plt.axvline(k * np.pi / 2, color='red', linewidth=1.0, linestyle=(0, (5, 10)), alpha=0.5)
    plt.text(k * np.pi / 2, 1.05, f'{k}π/2', horizontalalignment='center', fontsize=8)

exclusion_points = [k * np.pi - np.pi / 2 for k in range(-3, 5)]
exclusion_width = 0.05
for point in exclusion_points:
    plt.axvspan(point - exclusion_width, point + exclusion_width, color='white', zorder=3)

plt.xlabel("t")
plt.ylabel("f(t)")
plt.ylim(-1, 1)
plt.grid(alpha=0.3)
plt.legend()

os.makedirs("img", exist_ok=True)
plt.savefig("img/sin.png", dpi=500, bbox_inches="tight")

plt.show()
