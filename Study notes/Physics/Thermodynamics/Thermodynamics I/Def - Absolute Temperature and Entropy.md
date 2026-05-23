---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
  - "Def - Caratheodory's Principle (Inaccessibility)"
  - "Thm - The Heat 1-Form is Integrable"
tags: [physics, thermodynamics]
---

# Notation

$M^{n+1}$ is the [[Def - Thermodynamic State Space|thermodynamic state space]]; $\delta Q$ is the [[Def - Heat 1-Form and Work 1-Form|heat 1-form]]; $T : M \to \mathbb{R}_{>0}$ is the absolute temperature; $S : M \to \mathbb{R}$ is the entropy; both are globally defined smooth functions. The fundamental relation is $\delta Q = T\, dS$. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

This is a compound page: it defines two interlocking notions — the **absolute temperature** $T$ and the **entropy** $S$ — because they are extracted together as the integrating factor and integral of the heat 1-form, and neither is fully usable without the other.

---

# Axiom Motivation

Once Caratheodory's principle has produced the integrability of $\ker \delta Q$ via [[Thm - Caratheodory's Theorem on the Second Law]], the [[Thm - The Frobenius Theorem|Frobenius theorem]] (in its single-Pfaffian form) guarantees that *locally* there exist smooth functions $\lambda \neq 0$ and $f$ with $\delta Q = \lambda\, df$. The function $\lambda$ is an integrating factor; $f$ is its integral. The question is: what physical interpretations should $\lambda$ and $f$ be given, and can they be promoted from local to global functions?

The first design choice is to call $f$ the **entropy** $S$. This is justified by the second-law-as-irreversibility property: along any irreversible process (stirring, free expansion), $S$ never decreases. This monotonicity is not automatic from the local Frobenius theorem; it requires an additional physical input — the assumption that "stirring" can be undone only at the cost of net heat exchange, which Frankel uses to show that adiabatic surfaces are *totally ordered* by stirring (you can stir from a low-entropy leaf to a high-entropy leaf, never vice versa). The function $S$ is then chosen to be monotone in the stirring direction, fixing its sign and labelling the leaves consistently. Without this, $S$ would be defined only modulo orientation of the foliation; with it, $S$ has a natural direction of increase.

The second design choice is to call $\lambda$ the **absolute temperature** $T$. The motivation here is subtler. The function $\lambda$ is not unique: $\delta Q = \lambda\, df = (\lambda h(f))\, d(g(f))$ for any smooth $g$ with $g'(f) = 1/h(f)$. So $(\lambda, f)$ is determined only up to a transformation $(\lambda, f) \mapsto (\lambda/g'(f), g(f))$ — there are infinitely many integrating-factor-integral pairs for a given $\delta Q$. To pin down $T$ and $S$ uniquely, you need a *universality* assumption: combining two systems $A$ and $B$ in thermal contact gives a composite system whose integrating factor on the joint state space is the *same function of empirical temperature* as each subsystem's integrating factor. This common function defines the absolute temperature $T$ uniquely up to a multiplicative constant (the choice of unit, e.g. the kelvin defined by the triple point of water).

Why does universality fix $T$? Because two systems in thermal equilibrium have the same temperature — that is the meaning of "thermal equilibrium" (the zeroth law of thermodynamics). If $T_A$ and $T_B$ are the integrating factors of $A$ and $B$ separately, then in the combined system the heat form is $\delta Q_{AB} = \delta Q_A + \delta Q_B = T_A\, dS_A + T_B\, dS_B$. For this to have an integrating factor on the combined state space — which it must, since the combined system also obeys Caratheodory — and for that integrating factor to be a state function of the combined system, the ratio $T_A/T_B$ must depend only on the common temperature (the "empirical temperature" $\theta$ shared at equilibrium). A short argument then shows $T_A = T_B$ as functions of $\theta$, up to a universal constant. This is Caratheodory's argument for the universality of $T$; details are in Buchdahl's book and in Wightman's introduction to Israel's monograph.

The third design choice is the sign of $T$: we require $T > 0$. This is *not* automatic from Frobenius — $\lambda$ could be negative on some part of $M$ — but is fixed by the convention that **heating raises the entropy** (positive heat absorbed at positive temperature increases $S$). With $\delta Q = T\, dS$, an isochoric heating process ($\delta W = 0$) gives $\delta Q = dU > 0$ (heating raises $U$), and we want this to give $dS > 0$ as well, forcing $T > 0$. Negative absolute temperatures *do* occur in physics — for systems with bounded energy spectra, like spin systems — and the formalism extends to them via $1/T = (\partial S/\partial U)_V$, but for ordinary gases and fluids $T > 0$ throughout. We adopt the convention $T > 0$ for this topic.

The fourth design choice — and the most physically important — is the **second law in the irreversible-process form**: $dS \geq \delta Q / T_{\text{surr}}$, with equality for reversible quasistatic processes. This Clausius inequality is the *strong* form of the second law; it implies entropy can only increase in an isolated system ($\delta Q = 0 \Rightarrow dS \geq 0$). The proof requires the additional input that irreversible processes (stirring etc.) connect states only in the direction of increasing $S$, which is Frankel's stirring-direction assumption made precise.

---

# The Definition

Assume Caratheodory's principle ([[Def - Caratheodory's Principle (Inaccessibility)]]) holds, so by [[Thm - The Heat 1-Form is Integrable]] the heat 1-form satisfies $\delta Q \wedge d(\delta Q) = 0$ globally on $M$. Suppose further that every adiabatic leaf meets a fixed transversal curve (the "basic transversal" of Frankel's construction — physically, "heating at constant volume from a reference state"), so that the local integrating factor and entropy extend to global functions.

The **absolute temperature** of the system is the unique smooth function $T : M \to \mathbb{R}_{>0}$ such that:

1. $T$ is an integrating factor for $\delta Q$: there exists a smooth function $S : M \to \mathbb{R}$ with $\delta Q = T\, dS$.
2. $T$ depends only on the empirical temperature (universality across systems in thermal equilibrium): for any two systems $A, B$ in thermal contact, the integrating factors $T_A, T_B$ on their state spaces are the same function of the common empirical temperature, up to a universal multiplicative constant (the choice of unit).
3. $T > 0$ everywhere (heating raises entropy).

The **entropy** of the system is the smooth function $S : M \to \mathbb{R}$, determined up to an additive constant, satisfying $dS = \delta Q / T$. By construction, $S$ is constant on each adiabatic leaf (the level sets of $S$ are precisely the adiabatic surfaces), and $S$ takes the same value at two states iff they are quasistatically adiabatically connected.

The **second law of thermodynamics in differential form** is the inequality

$$dS \geq \frac{\delta Q}{T_{\text{surr}}}$$

for any infinitesimal process, with equality iff the process is quasistatic and reversible. Integrated along an arbitrary (possibly irreversible) process from $x$ to $y$:

$$S(y) - S(x) \geq \int_x^y \frac{\delta Q_{\text{actual}}}{T_{\text{surr}}}.$$

Specialised to an **adiabatic** process ($\delta Q_{\text{actual}} = 0$): $S(y) \geq S(x)$, with equality iff reversible. This is the entropy-increase principle.

---

# Relate to Other Fields / Compression

The absolute temperature is the **universal integrating factor for $\delta Q$ across all thermodynamic systems in mutual thermal equilibrium**. The entropy is its **integral**, a state function whose level sets are the adiabatic surfaces.

**True name:** The absolute temperature is **the proportionality between heat absorbed and entropy increase: $T = \delta Q / dS$**. The entropy is **the function whose level sets are the adiabats**, equivalently **the function that increases monotonically under stirring**. These two functions package the entire second law: $T$ is what you measure with a thermometer, $S$ is what you measure with a Carnot cycle.

In statistical mechanics, the same two quantities arise differently: $S$ is **Boltzmann entropy** $S = k_B \log W$ counting microstates compatible with a macrostate, and $T$ is the Lagrange multiplier in the maximum-entropy derivation of the Gibbs distribution, $1/T = (\partial S/\partial U)_V$. The numerical agreement between these statistical-mechanical $T, S$ and Caratheodory's geometrical $T, S$ is one of the most important facts in physics — it ties microscopic dynamics to macroscopic thermodynamics. The connection is established via the equivalence of ensembles in the thermodynamic limit.

In information theory, **Shannon entropy** $H(p) = -\sum_i p_i \log p_i$ on a probability distribution coincides numerically with $S/k_B$ when $p$ is the equilibrium Gibbs distribution. So $S/k_B$ measures the "information content" needed to specify the microstate given the macrostate — but in equilibrium *only*. Out of equilibrium, the distinction between thermodynamic entropy and Shannon entropy matters, and the **Jarzynski equality** and **fluctuation theorems** are the rigorous tools for handling that distinction.

---

# Examples / Corollaries

**Is an instance: ideal gas $T$ and $S$.** For a simple ideal gas with $pV = nRT_{\text{empirical}}$ and $U = (f/2)nR T_{\text{empirical}}$, the heat form is $\delta Q = (f/2)nR\, dT_{\text{empirical}} + (nRT_{\text{empirical}}/V)\, dV$. The integrating factor is $\lambda = 1/T_{\text{empirical}}$, giving $\delta Q/\lambda = T_{\text{empirical}}^{-1} \delta Q$ exact. So $T = T_{\text{empirical}}$ (the ideal-gas empirical temperature coincides with the absolute temperature, up to a unit), and $S = (f/2)nR \log T + nR \log V + \text{const}$. See [[Ex - Compute the Entropy of an Ideal Gas]].

**Is an instance: entropy increase in free expansion of an ideal gas.** A free expansion of an ideal gas from $V_1$ to $V_2 > V_1$ with $T$ unchanged has $\Delta S = nR \log(V_2/V_1) > 0$. The actual process is irreversible (and adiabatic with $Q_{\text{actual}} = 0$), so the second law gives $\Delta S \geq 0$, which is satisfied with strict inequality.

**Is NOT an instance: $T$ and $S$ unique without universality.** Without the universality requirement, the pair $(\lambda, f)$ extracting an integrating factor and integral from $\delta Q$ is not unique: replacing $(T, S)$ by $(T/g'(S), g(S))$ for any monotone smooth $g$ gives another valid pair $(\tilde T, \tilde S)$ with $\tilde T\, d\tilde S = \delta Q$. The universality requirement (same integrating factor as a function of empirical temperature, for any system in thermal equilibrium) is what pins down $T$ uniquely up to a unit constant.

**Is NOT an instance: negative temperatures in textbooks for ordinary gases.** Ordinary gases have $T > 0$ always, because $\partial S/\partial U > 0$ (more energy means more microstates). Spin systems with bounded energy spectra can have $\partial S/\partial U < 0$ at high enough energy — population inversion — and the formal $1/T < 0$ then. These "negative temperatures" are *hotter* than any positive temperature (heat flows from negative-$T$ to positive-$T$ when they are placed in contact). The Caratheodory framework extends to them with care, but for this topic we restrict to $T > 0$.

**Calibration check.** If you understand the definition, you should be able to (1) explain why the integrating factor for $\delta Q$ is determined only up to a transformation $(\lambda, f) \mapsto (\lambda/g'(f), g(f))$, and how universality across systems fixes this freedom to a multiplicative constant, (2) write down $S$ for an ideal gas in $(T, V)$ coordinates and verify $dS$ is exact, and (3) state the Clausius inequality and explain why, in a closed cycle, $\oint dS = 0$ but $\oint \delta Q / T \leq 0$, with equality iff the cycle is reversible.

---

# Unlocked by This

> [!tip] Thermodynamic Potentials and Legendre Transforms *(from this topic)*
> With $T$ and $S$ as state functions, the differential of the internal energy becomes $dU = T\, dS - p\, dV$, expressing $U$ in its **natural variables** $(S, V)$. Legendre-transforming the conjugate pairs $(S, T)$ and $(V, p)$ produces the [[Def - Thermodynamic Potential (U, H, F, G)|other thermodynamic potentials]] $H = U + pV$, $F = U - TS$, $G = U + pV - TS$, each natural in different variables and useful for different experimental setups. The Maxwell relations are then $d^2 = 0$ applied to each potential.

> [!tip] Statistical-Mechanical Identification: $S = k_B \log W$, $1/T = \partial S/\partial U$ *(from Statistical Mechanics)*
> **Statistical mechanics** identifies the thermodynamic entropy with $S = k_B \log W$, where $W = W(U, V, N)$ is the number of microstates of the system compatible with macroscopic energy $U$, volume $V$, and particle number $N$. The thermodynamic temperature satisfies $1/T = (\partial S/\partial U)_{V, N}$. This identification — first by Boltzmann, then made rigorous by Gibbs — bridges classical thermodynamics to microscopic mechanics, and is the foundation of the **Gibbs measure** and the **maximum entropy principle**. It also explains the *direction* of entropy increase: irreversible processes are those that move the system toward macrostates with overwhelmingly larger numbers of compatible microstates, and the second law becomes a statistical statement about overwhelming probability rather than absolute prohibition.

> [!tip] Information-Theoretic Entropy: Shannon, von Neumann, Kolmogorov *(from Information Theory)*
> **Shannon entropy** $H(p) = -\sum_i p_i \log p_i$ on a discrete probability distribution coincides numerically with $S/k_B$ when $p$ is the equilibrium Gibbs distribution at temperature $T$. **Von Neumann entropy** $S = -\mathrm{Tr}(\rho \log \rho)$ is the quantum-mechanical generalisation, applicable to density matrices, and underlies quantum information theory and the entropy of entanglement. **Kolmogorov complexity** $K(x)$ is the length of the shortest program producing a given microstate description $x$; algorithmic entropy is closely related to Shannon entropy for typical (random) strings but differs systematically for structured strings. The active research direction **Maxwell's demon and algorithmic thermodynamics** unifies these notions — replacing macroscopic thermodynamic entropy with an algorithmic-information-theoretic version in which the "second law" applies to observers performing computations on microstate descriptions.

> [!tip] Bekenstein-Hawking Entropy of Black Holes *(from General Relativity)*
> Black holes have an entropy $S_{\text{BH}} = A/(4 \ell_P^2)$ where $A$ is the horizon area and $\ell_P$ the Planck length, and a Hawking temperature $T_H = \hbar c^3/(8\pi GM k_B)$ inversely proportional to mass. The four **laws of black hole mechanics** parallel the laws of thermodynamics with horizon area playing the role of entropy and surface gravity the role of temperature — making this one of the deepest and most surprising appearances of the Caratheodory $T$-$S$ structure in nature. The microscopic origin of $S_{\text{BH}}$ (the underlying "microstates" of a black hole) is the principal mystery driving research on **quantum gravity** and the **holographic principle**.
