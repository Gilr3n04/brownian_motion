import numpy as np
import matplotlib.pyplot as plt

num_particles = 10000
num_steps = 500
v0 = 0.0
sigma_dv = 1.0

v = np.full(num_particles, v0)
v_sq_mean = np.zeros(num_steps)
num_trajectories_to_save = 3
trajectories_v2 = np.zeros((num_trajectories_to_save, num_steps))

for n in range(num_steps):
  delta_v = np.random.normal(loc=0.0, scale=sigma_dv, size=num_particles)
  v = v + delta_v
  v_sq_mean[n] = np.mean(v**2)
  trajectories_v2[:, n] = v[:num_trajectories_to_save] ** 2

mean_delta_v_squared = sigma_dv**2
n_steps_array = np.arange(num_steps)

v_sq_theory = v0**2 + n_steps_array * mean_delta_v_squared

plt.figure(figsize=(10, 6))

for i in range(num_trajectories_to_save):
  plt.plot(n_steps_array, trajectories_v2[i], color="gray", alpha=0.5, linestyle="--",)

plt.plot([], [], color="gray", linestyle="--", label="Singole particelle ($v^2$)")

plt.plot(n_steps_array, v_sq_mean, color="royalblue", linewidth=2.5, label=r"Media d'insieme simulata $\langle v_n^2 \rangle$")

plt.plot(n_steps_array, v_sq_theory, color="crimson", linestyle=":", linewidth=2, label=r"Teoria: $\langle v_0^2 \rangle + n \langle \Delta v^2 \rangle$")

plt.xlabel("Numero di passi ($n$)", fontsize=12)
plt.ylabel(r"Energia cinetica media proporzionale ($\langle v^2 \rangle$)", fontsize=12)
plt.title("Riscaldamento Casuale (Random Heating) senza Attrito — Impulsi Gaussiani", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.hist(v,
    bins=50,
    density=True,
    color="skyblue",
    edgecolor="black",
    alpha=0.7,
    label="Distribuzione finale di $v$",)

variance_theory = num_steps * (sigma_dv**2)
v_axis = np.linspace(min(v), max(v), 200)

gaussian_theory = (1/ np.sqrt(2 * np.pi * variance_theory)* np.exp(-(v_axis**2) / (2 * variance_theory)))

# Usiamo rf"" (raw f-string) per evitare i warning con \sigma
plt.plot(v_axis,gaussian_theory,color="crimson",linewidth=2.5,label=rf"Gaussiana teorica ($\sigma^2$ = {variance_theory})",)

plt.xlabel("Velocità $v$", fontsize=12)
plt.ylabel("Densità di probabilità", fontsize=12)
plt.title(f"Distribuzione delle velocità a $n = {num_steps}$ passi (Random Walk)",fontsize=14,)
plt.legend(fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()