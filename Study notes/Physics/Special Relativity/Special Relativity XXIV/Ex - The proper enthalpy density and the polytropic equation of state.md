---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Equation of State and Speed of Sound"
  - "Def - Perfect Fluid"
tags: [physics, special-relativity]
---

# Problem Statement

1. From the first law $d\rho = T\,ds + \sum_a\mu_a\,dn_a$ and the first law of thermodynamics for a comoving volume, derive the Euler relation $\rho + p = Ts + \sum_a\mu_a n_a$ and hence the Gibbs–Duhem relation $dp = s\,dT + \sum_a n_a\,d\mu_a$. Identify $\rho + p$ as the proper enthalpy density.
2. For a barotropic fluid ($\rho = \rho(n)$, so $T = 0$), show that $\rho + p = \mu n$, i.e. the chemical potential equals the enthalpy per baryon $h = (\rho+p)/n$, and that $\mu = d\rho/dn$.
3. For the polytrope $\rho(n) = m_{\mathrm b}n + \frac{\kappa}{\gamma-1}n^\gamma$ (adiabatic index $\gamma$), compute $\mu = d\rho/dn$ and deduce the pressure $p(n) = \kappa\,n^\gamma$.

**Recall:**

The equation of state is $\rho = \rho(s, \{n_a\})$ with $T = (\partial\rho/\partial s)$, $\mu_a = (\partial\rho/\partial n_a)$, and first law $d\rho = T\,ds + \sum_a\mu_a\,dn_a$ (see [[Def - Equation of State and Speed of Sound]]). A barotropic fluid has $\rho = \rho(n)$ and $T = 0$. The enthalpy per baryon is $h = (\rho+p)/n$. The proper enthalpy density is $\rho + p$, the combination appearing in the [[Def - Perfect Fluid|perfect-fluid tensor]] and the inertia.

---

# Convergent Strategy

**Problem class.** A *thermodynamic-derivation* problem, referencing the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]]: thermodynamic quantities are derivatives of the equation of state, and the enthalpy combination $\rho + p$ is what appears in the dynamics.

**Assumption pattern.** The first law $d\rho = T\,ds + \sum\mu_a\,dn_a$ plus the standard thermodynamic first law $dU = T\,dS - p\,dV + \sum\mu_a\,dN_a$ for a comoving volume are the inputs. The signpost is "equation of state", "enthalpy", or "polytrope".

**Theorem routing.** Part 1 compares the two first laws (applied to $U = \rho V$, $S = sV$, $N_a = n_a V$) to extract the Euler relation, then differentiates it for Gibbs–Duhem. Part 2 specialises to $T = 0$. Part 3 substitutes the polytropic $\rho(n)$.

**Key decision point.** The crux of part 1 is taking the differential of $U = \rho V$ with $S = sV$, $N_a = n_a V$, comparing with the thermodynamic first law, and reading off the coefficient of $dV$ — which gives $p = -\rho + Ts + \sum\mu_a n_a$, the Euler relation. The natural error is to forget the $dV$ term or to mishandle the homogeneity (extensivity) of $U$, $S$, $N_a$ in $V$.

---

# Legal Operations Used

1. **Compute thermodynamic derivatives from the equation of state** (operation 10 from the topic page): $T$, $\mu_a$, and the enthalpy are all derivatives of $\rho(s, \{n_a\})$.

2. **Use the first law of thermodynamics** (the energy-equation interpretation from [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]): comparing the relativistic and thermodynamic first laws yields the Euler relation.

---

# Hints

> [!note]- Hint 1
> Take a comoving volume $V$ with $U = \rho V$, $S = sV$, $N_a = n_a V$. Differentiate $U = \rho V$ using $d\rho = T\,ds + \sum\mu_a\,dn_a$: $dU = V\,d\rho + \rho\,dV = V(T\,ds + \sum\mu_a\,dn_a) + \rho\,dV$. Rewrite $V\,ds = d(sV) - s\,dV = dS - s\,dV$, similarly for $n_a$. Collect the $dV$ terms.

> [!note]- Hint 2
> You get $dU = T\,dS + \sum\mu_a\,dN_a + (\rho - Ts - \sum\mu_a n_a)\,dV$. Compare with the thermodynamic first law $dU = T\,dS - p\,dV + \sum\mu_a\,dN_a$. The $dV$ coefficients give $-p = \rho - Ts - \sum\mu_a n_a$, i.e. $\rho + p = Ts + \sum\mu_a n_a$.

> [!note]- Hint 3
> Differentiate the Euler relation and subtract the first law $d\rho = T\,ds + \sum\mu_a\,dn_a$ to get Gibbs–Duhem $dp = s\,dT + \sum n_a\,d\mu_a$. For barotropic $T = 0$: $\rho + p = \mu n$, and $\mu = d\rho/dn$. For the polytrope, $d\rho/dn = m_{\mathrm b} + \frac{\kappa\gamma}{\gamma-1}n^{\gamma-1} = \mu$, then $p = \mu n - \rho$.

---

# Solution

The proper enthalpy density $\rho + p$ emerges from comparing the relativistic and thermodynamic first laws; for a barotropic fluid it equals $\mu n$, and for a polytrope the chemical potential is the derivative of the energy density, yielding $p = \kappa n^\gamma$.

**Step 1: The Euler and Gibbs–Duhem relations.**

> [!note]- Derivation
> Take a comoving volume $V$ with total energy $U = \rho V$, entropy $S = sV$, particle numbers $N_a = n_a V$. Differentiate $U = \rho V$, using the relativistic first law $d\rho = T\,ds + \sum_a\mu_a\,dn_a$:
> $$dU = V\,d\rho + \rho\,dV = V\Big(T\,ds + \sum_a\mu_a\,dn_a\Big) + \rho\,dV.$$
> Now $V\,ds = d(sV) - s\,dV = dS - s\,dV$, and $V\,dn_a = dN_a - n_a\,dV$. Substitute:
> $$dU = T(dS - s\,dV) + \sum_a\mu_a(dN_a - n_a\,dV) + \rho\,dV = T\,dS + \sum_a\mu_a\,dN_a + \Big(\rho - Ts - \sum_a\mu_a n_a\Big)dV.$$
> Compare with the standard first law $dU = T\,dS - p\,dV + \sum_a\mu_a\,dN_a$. The $dV$ coefficients must match:
> $$-p = \rho - Ts - \sum_a\mu_a n_a \quad\Longrightarrow\quad \boxed{\rho + p = Ts + \sum_a\mu_a n_a,}$$
> the **Euler relation**. The combination $\rho + p$ is the **proper enthalpy density**. Differentiating the Euler relation, $d\rho + dp = T\,ds + s\,dT + \sum(\mu_a\,dn_a + n_a\,d\mu_a)$, and subtracting the first law $d\rho = T\,ds + \sum\mu_a\,dn_a$ leaves
> $$dp = s\,dT + \sum_a n_a\,d\mu_a,$$
> the **Gibbs–Duhem relation**.

**Step 2: Barotropic fluid.**

> [!note]- Derivation
> A barotropic fluid has $\rho = \rho(n)$ alone, so $T = (\partial\rho/\partial s) = 0$. The Euler relation (single species, $\mu_a\to\mu$, $n_a\to n$) becomes
> $$\rho + p = \mu n \quad\Longrightarrow\quad \mu = \frac{\rho+p}{n} = h,$$
> the chemical potential equals the **enthalpy per baryon** $h$. And from the first law with $T = 0$, $d\rho = \mu\,dn$, so
> $$\mu = \frac{d\rho}{dn}.$$

**Step 3: The polytrope.**

> [!note]- Derivation
> For $\rho(n) = m_{\mathrm b}n + \frac{\kappa}{\gamma-1}n^\gamma$, the chemical potential is
> $$\mu = \frac{d\rho}{dn} = m_{\mathrm b} + \frac{\kappa}{\gamma-1}\cdot\gamma\,n^{\gamma-1} = m_{\mathrm b} + \frac{\kappa\gamma}{\gamma-1}n^{\gamma-1}.$$
> The pressure follows from the Euler relation $p = \mu n - \rho$:
> $$p = \Big(m_{\mathrm b} + \frac{\kappa\gamma}{\gamma-1}n^{\gamma-1}\Big)n - \Big(m_{\mathrm b}n + \frac{\kappa}{\gamma-1}n^\gamma\Big) = \frac{\kappa\gamma}{\gamma-1}n^\gamma - \frac{\kappa}{\gamma-1}n^\gamma = \frac{\kappa(\gamma-1)}{\gamma-1}n^\gamma,$$
> i.e.
> $$\boxed{p(n) = \kappa\,n^\gamma.}$$
> This is the **polytropic equation of state**: pressure proportional to a power of the baryon density, with $\gamma$ the adiabatic index. For a non-relativistic degenerate electron gas $\gamma = 5/3$; for an ultra-relativistic one $\gamma = 4/3$. The rest-mass term $m_{\mathrm b}n$ in $\rho$ does not contribute to $p$ — pressure comes entirely from the internal (degeneracy) energy.

> [!note]- Complete formal solution
> Differentiating $U = \rho V$ with $S = sV$, $N_a = n_a V$ and using $d\rho = T\,ds + \sum\mu_a\,dn_a$ gives $dU = T\,dS + \sum\mu_a\,dN_a + (\rho - Ts - \sum\mu_a n_a)dV$; matching the thermodynamic first law's $dV$ term yields the Euler relation $\rho + p = Ts + \sum\mu_a n_a$, so $\rho + p$ is the proper enthalpy density, and differencing gives Gibbs–Duhem $dp = s\,dT + \sum n_a\,d\mu_a$. For a barotropic fluid $T = 0$, so $\rho + p = \mu n$ ($\mu = h$) and $\mu = d\rho/dn$. For the polytrope $\rho = m_{\mathrm b}n + \frac{\kappa}{\gamma-1}n^\gamma$, $\mu = m_{\mathrm b} + \frac{\kappa\gamma}{\gamma-1}n^{\gamma-1}$ and $p = \mu n - \rho = \kappa n^\gamma$. $\blacksquare$

---

# Key Takeaways

**The combination $\rho + p$ is the proper enthalpy density, and it appears because of extensivity.** The central lesson is that $\rho + p$ — the combination that governs the inertia of a fluid element and the speed of sound — is the proper enthalpy density, and it emerges from comparing the relativistic first law $d\rho = T\,ds + \sum\mu_a\,dn_a$ with the standard thermodynamic first law $dU = T\,dS - p\,dV + \sum\mu_a\,dN_a$. The Euler relation $\rho + p = Ts + \sum\mu_a n_a$ is a consequence of the extensivity (homogeneity in volume) of energy, entropy, and particle number, and it is *why* pressure enters the enthalpy. The transferable insight: whenever you see $\rho + p$ in a relativistic fluid equation, recognise it as the enthalpy density $Ts + \sum\mu_a n_a$, and recall that its appearance traces to the fact that accelerating or compressing a fluid element does work against pressure. This single combination ties the thermodynamics of the equation of state to the dynamics of the fluid.

**For barotropic matter the chemical potential is the enthalpy per baryon.** The clean specialisation $T = 0 \Rightarrow \mu = h = (\rho+p)/n$ is worth holding onto: in cold matter, the chemical potential (the energy to add one baryon) is exactly the enthalpy per baryon (the energy plus pressure-work per baryon), because there is no entropy contribution. This is the regime of white-dwarf and neutron-star interiors, where the equation of state is barotropic and $\mu = d\rho/dn$ is the single thermodynamic function that determines everything. The diagnostic: for cold dense matter, do not carry temperature and entropy — the chemical potential *is* the enthalpy per baryon, and the pressure follows from $p = \mu n - \rho$. This is the simplification that makes degenerate-matter equations of state tractable.

**The polytrope's pressure comes entirely from the internal energy, not the rest mass.** The computation $p = \kappa n^\gamma$ for $\rho = m_{\mathrm b}n + \frac{\kappa}{\gamma-1}n^\gamma$ reveals that the rest-mass term $m_{\mathrm b}n$ contributes nothing to the pressure — all the pressure comes from the internal (degeneracy or thermal) energy density $\frac{\kappa}{\gamma-1}n^\gamma$. This is physically sensible: rest mass is inert, and pressure is a response to *internal* energy. The reusable principle is that the polytropic relation $p \propto n^\gamma$ with adiabatic index $\gamma$ encapsulates a wide range of matter — $\gamma = 5/3$ for non-relativistic degenerate fermions, $\gamma = 4/3$ for ultra-relativistic ones, $\gamma = 1 + 1/N$ for various polytropic stellar models — and that the index $\gamma$ controls both the stiffness (and hence the sound speed $c_s^2 = dp/d\rho$) and the stability of self-gravitating configurations. The trigger to recall: cold dense matter is well-modelled by a polytrope, and the single parameter $\gamma$ determines its stellar-structure behaviour, including the famous $\gamma = 4/3$ instability threshold for radiation-dominated and ultra-relativistic stars.
