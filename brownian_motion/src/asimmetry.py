import matplotlib.pyplot as plt
import numpy as np

num_particles = 10000
num_steps = 500
v0 = 0.0
sigma_dv = 1.0
mean_dv_sq = sigma_dv**2

v = np.full(num_particles, v0, dtype=float)

c_pre = np.zeros(num_steps, dtype=float)  # <v_{n-1} * \Delta v_n> = 0
c_post = np.zeros(num_steps, dtype=float)  # <v_n * \Delta v_n> = <\Delta v^2>
w_mean_step = np.zeros(num_steps, dtype=float)  # <W_n> = 1/2 <v_n^2 - v_{n-1}^2>

for n in range(num_steps):
  v_prev = v.copy()
  delta_v = np.random.normal(loc=0.0, scale=sigma_dv, size=num_particles)
  v = v_prev + delta_v

  # Correlazioni prima e dopo l'impulso
  c_pre[n] = np.mean(v_prev * delta_v)
  c_post[n] = np.mean(v * delta_v)

  # Lavoro impulsivo medio al passo n (in unita' di massa m=1): 1/2 * (v_n^2 - v_{n-1}^2)
  w_n = 0.5 * (v**2 - v_prev**2)
  w_mean_step[n] = np.mean(w_n)

n_steps_array = np.arange(num_steps)
w_cum_sim = np.cumsum(w_mean_step)
w_cum_theory = (n_steps_array + 1) * (0.5 * mean_dv_sq)

print(
    f"Media <v_{{n-1}} dv_n>: {np.mean(c_pre):.4f} (teoria: 0.0) | Media <v_n"
    f" dv_n>: {np.mean(c_post):.4f} (teoria: {mean_dv_sq:.4f})"
)
print(
    f"Lavoro medio per passo <W_n>: {np.mean(w_mean_step):.4f} (teoria:"
    f" {0.5 * mean_dv_sq:.4f})"
)

# Grafico 5A: Asimmetria temporale delle correlazioni
plt.figure(figsize=(10, 5.5))
plt.plot(
    n_steps_array,
    c_pre,
    color="royalblue",
    linewidth=1.5,
    alpha=0.8,
    label=r"Pre-impulso: $\langle v_{n-1}\Delta v_n \rangle$",
)
plt.plot(
    n_steps_array,
    c_post,
    color="darkorange",
    linewidth=1.5,
    alpha=0.85,
    label=r"Post-impulso: $\langle v_n\Delta v_n \rangle$",
)
plt.axhline(
    0.0, color="crimson", linestyle="--", linewidth=1.5, label=r"Teoria pre: $0$"
)
plt.axhline(
    mean_dv_sq,
    color="black",
    linestyle="--",
    linewidth=1.8,
    label=rf"Teoria post: $\langle \Delta v^2 \rangle = {mean_dv_sq:.1f}$",
)

plt.xlabel("Passo temporale ($n$)", fontsize=12)
plt.ylabel("Correlazione media", fontsize=12)
plt.title(
    "Asimmetria Temporale: $\\langle v_{n-1}\\Delta v_n \\rangle$ vs"
    " $\\langle v_n\\Delta v_n \\rangle$",
    fontsize=13,
)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# Grafico 5B: Lavoro medio per passo e lavoro cumulato (Esperimento 2A)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(
    n_steps_array,
    w_mean_step,
    color="royalblue",
    linewidth=1.4,
    alpha=0.8,
    label=r"Simulazione $\langle W_n \rangle$",
)
ax1.axhline(
    0.5 * mean_dv_sq,
    color="crimson",
    linestyle="--",
    linewidth=2,
    label=rf"Teoria: $\frac{{1}}{{2}}\langle \Delta v^2 \rangle = {0.5 * mean_dv_sq:.2f}$",
)
ax1.set_xlabel("Passo temporale ($n$)", fontsize=11)
ax1.set_ylabel(r"Lavoro medio per passo $\langle W_n \rangle$", fontsize=11)
ax1.set_title("Lavoro medio per impulso", fontsize=12)
ax1.legend(fontsize=9.5)
ax1.grid(True, linestyle="--", alpha=0.6)

ax2.plot(
    n_steps_array,
    w_cum_sim,
    color="royalblue",
    linewidth=2.2,
    label=r"Lavoro cumulato simulato $\sum W_k$",
)
ax2.plot(
    n_steps_array,
    w_cum_theory,
    color="crimson",
    linestyle=":",
    linewidth=2,
    label=r"Teoria: $\frac{1}{2}\langle v_n^2 - v_0^2 \rangle$",
)
ax2.set_xlabel("Passo temporale ($n$)", fontsize=11)
ax2.set_ylabel(r"Lavoro cumulato $\sum_{k=1}^{n+1} \langle W_k \rangle$", fontsize=11)
ax2.set_title("Esperimento 2A — Lavoro cumulato", fontsize=12)
ax2.legend(fontsize=9.5)
ax2.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()