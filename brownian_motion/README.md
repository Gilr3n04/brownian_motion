# Discrete Impulsive Model for Random Heating and Brownian Motion

Analisi numerica e presentazione tecnica basate sul modello a impulsi discreti di **John D. Ramshaw (2010)** (*Am. J. Phys.* 78, 1), focalizzate su:
- dinamica impulsiva senza attrito, correlazioni pre/post-impulso e lavoro medio positivo ($\langle W_n \rangle > 0$);
- *random walk* 1D nello spazio delle velocità e crescita irreversibile dell'energia cinetica media;
- introduzione dello smorzamento ($\alpha$) e convergenza a uno stato stazionario con plateau finito.

## Struttura del repository

```text
.
├── src/
│   ├── frictionless.py   # Evoluzione impulsiva senza attrito, varianza e random walk 1D
│   ├── asimmetry.py      # Correlazioni prima/dopo l'impulso e calcolo del lavoro medio W_n
│   └── langevin.py       # Dinamica impulsiva con smorzamento (alpha) e rilassamento al plateau
├── figures/              # Figure generate tramite save_fig da motion_analysis.ipynb
├── motion_analysis.ipynb # Notebook principale per simulazioni e generazione delle figure
├── .gitignore
└── README.md