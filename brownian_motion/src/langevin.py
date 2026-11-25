import matplotlib.pyplot as plt
import numpy as np

num_particles = 10000
num_steps = 600
v0 = 0.0
sigma_dv = 1.0  # Deviazione standard di \Delta v
mean_dv_sq = sigma_dv**2  # <\Delta v^2>
alphas = [0.005, 0.01, 0.02, 0.05]

def simulate_damped_heating(num_particles, num_steps, alpha, sigma_dv, v0=0.0):
  v = np.full(num_particles, v0, dtype=float)
  v_sq_mean = np.zeros(num_steps)

  for n in range(num_steps):
    delta_v = np.random.normal(loc=0.0, scale=sigma_dv, size=num_particles)
    v = (1.0 - alpha) * v + delta_v
    v_sq_mean[n] = np.mean(v**2)

  return v, v_sq_mean

n_steps_array = np.arange(num_steps)
colors = ["teal", "royalblue", "darkorange", "purple"]

plt.figure(figsize=(10, 6))

final_velocities = {}

for alpha, color in zip(alphas, colors):
  v_final, v_sq_mean = simulate_damped_heating(num_particles=num_particles,num_steps=num_steps,alpha=alpha,sigma_dv=sigma_dv,v0=v0,)
  final_velocities[alpha] = v_final

  # Curva simulata
  plt.plot(n_steps_array,v_sq_mean,color=color,linewidth=2,label=rf"Simulazione $\alpha = {alpha}$",)


  v_sq_asymp_approx = mean_dv_sq / (2.0 * alpha)
  plt.axhline(v_sq_asymp_approx,color=color,linestyle="--",linewidth=1.5,alpha=0.8,label=rf"Teoria $\alpha = {alpha}$: $\langle v^2 \rangle \approx {v_sq_asymp_approx:.1f}$",)

plt.xlabel("Numero di passi ($n$)", fontsize=12)
plt.ylabel(r"Energia cinetica media proporzionale ($\langle v^2 \rangle$)", fontsize=12)
plt.title("Modello Impulsivo con Attrito: Raggiungimento dello Stato Stazionario",fontsize=14,)
plt.legend(fontsize=9, ncol=2)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


alpha_test = alphas[-1]
v_eq = final_velocities[alpha_test]
var_eq_theory = mean_dv_sq / (2.0 * alpha_test)

plt.figure(figsize=(8, 5))
plt.hist(v_eq,bins=50,density=True,color="lightgreen",edgecolor="black",alpha=0.7,label=rf"Velocità a fine simulazione ($\alpha = {alpha_test}$)",)

v_axis = np.linspace(min(v_eq), max(v_eq), 200)
gauss_eq = (1/ np.sqrt(2 * np.pi * var_eq_theory)* np.exp(-(v_axis**2) / (2 * var_eq_theory)))

plt.plot(v_axis,gauss_eq,color="crimson",linewidth=2.5,label=rf"Maxwell-Boltzmann 1D ($\sigma^2 = {var_eq_theory:.1f}$)",)

plt.xlabel("Velocità $v$", fontsize=12)
plt.ylabel("Densità di probabilità", fontsize=12)
plt.title(rf"Distribuzione stazionaria delle velocità ($\alpha = {alpha_test}$)",fontsize=14,)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()