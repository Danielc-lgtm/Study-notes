# PAGE SPEC

- **Filename:** `Thm - Solutions of the Lorentz Force Equation Have Constant Speed and Exist Uniquely.md`
- **Type:** theorem
- **Chapter:** Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory  (folder `Gauge Theory VII/`)
- **Section:** §7.2 Electrodynamics as a U(1) Gauge Theory

## Spec (from the manifest)

type: theorem (two parts); source items: B-T3.2.1, B-T3.2.2, B-I3.2.7; prereqs: [Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass, Def - Metric-Compatible Connection, Thm - Existence and Uniqueness of Integral Curves]; statement: (i) Every solution $c$ of $\frac{\nabla}{d\tau}c' + F(c',\cdot)^\sharp = 0$ satisfies $\frac{d}{d\tau}\langle c',c'\rangle = 0$; hence a solution that is timelike at one instant is timelike throughout and is parametrised proportionally to eigentime. (ii) For every $p\in M$ and $X\in T_pM$ there is a unique maximal solution $c$ with $c(\tau_0) = p$, $c'(\tau_0) = X$; proof: (i) Bär: $\frac{d}{d\tau}\langle c',c'\rangle = 2\langle\frac{\nabla}{d\tau}c',c'\rangle = -2F(c',c') = 0$ (metric compatibility of Levi-Civita, then skew-symmetry of $F$) — full; (ii) Bär says "since (3.12) is a linear ODE" (source typo: Bär Rem. 3.2.2 calls (3.12) linear; it is a second-order ODE with smooth coefficients, not linear in general) — the writer rewrites (3.12) as a first-order ODE for $(c,c')$ on $TM$, i.e. as the integral-curve equation of the smooth vector field $Z(v) := S(v) - (F(v,\cdot)^\sharp)^{\text{vert}}$ on $TM$ ($S$ the geodesic spray, vertical lift of $-F(v,\cdot)^\sharp$), in coordinates $\ddot c^k + \Gamma^k_{ij}\dot c^i\dot c^j + g^{kl}F_{il}\dot c^i = 0$, and invokes `Thm - Existence and Uniqueness of Integral Curves` (DG V) and `Thm - Fundamental Theorem on Flows`; spec: pattern identical to `Thm - Existence and Uniqueness of Geodesics` (RG II) — cite it as the $F = 0$ case; mechanism: a skew force does no work.
