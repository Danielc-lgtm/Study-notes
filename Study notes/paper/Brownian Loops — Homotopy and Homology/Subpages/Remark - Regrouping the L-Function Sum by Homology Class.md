---
type: remark
subject: probability-geometry
prereqs:
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
  - "Def - Mass in a Homology Class"
  - "Cor - Selberg L-Function Identity"
tags: [paper, brownian-loops, homology, harmonic-analysis]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §6.2 — the identity $\\chi([\\gamma])^m = \\chi(\\beta)$ that regroups Cor 6.4's double sum by homology"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\Gamma \subset \mathrm{PSL}(2, \mathbb{R})$ discrete torsion-free.
- $\mathcal P_X$ the set of oriented primitive closed geodesics; $\ell_\gamma > 0$ its length; $[\gamma] \in H_1(X, \mathbb{Z})$ its homology class (image under the Hurewicz map $\Gamma \twoheadrightarrow H_1$).
- $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$ the first homology group; $\beta \in H_1(X, \mathbb{Z})$ a class; $r = 2g$ (closed) or $2g + b - 1$ (with $b$ ends).
- $\chi : H_1(X, \mathbb{Z}) \to S^1$ a unitary character; $\chi(\beta) \in S^1$ its value at $\beta$; $|\chi(\beta)| = 1$.
- $\mu^\kappa_X(C_X(\gamma^m))$ the killed loop-measure mass of the free homotopy class $C_X(\gamma^m)$ (§3.1.2).
- $\mu^\kappa_X(\beta) := \sum_{(\gamma, m):\,m[\gamma] = \beta}\mu^\kappa_X(C_X(\gamma^m))$ the killed loop mass grouped by homology class (Def 6.1).
- $L_X(s, \chi) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma})$ the Selberg $L$-function (Def 6.3), absolutely convergent for $\operatorname{Re}s > \delta$.
- $s = \frac12 + \sqrt{\frac14 + \kappa}$ the spectral parameter, $\operatorname{Re}s > \delta$.

> [!recall]- Hurewicz map $\gamma \mapsto [\gamma]$; iteration gives $[\gamma^m] = m[\gamma]$
> **Formally:** the *Hurewicz map* is the quotient homomorphism $h : \pi_1(X) \cong \Gamma \twoheadrightarrow \Gamma^{\mathrm{ab}} = H_1(X, \mathbb{Z})$, sending $\gamma \mapsto [\gamma]$. Because $h$ is a homomorphism, $[\gamma_1 \gamma_2] = [\gamma_1] + [\gamma_2]$ in the additively-written abelianisation; iterating, $[\gamma^m] = m[\gamma]$ for every integer $m$.
> **In words:** the Hurewicz map is "forget the order in which handles are traversed, keep only the net winding around each independent cycle." Composing loops multiplies in $\pi_1$ (non-abelian) but adds in $H_1$ (abelian); iterating a single loop $m$ times therefore multiplies its net winding by $m$.
> **Concretely:** on the torus $T^2$ with $\pi_1 = \mathbb{Z}^2$ already abelian, $h$ is the identity: $[(1, 0)^m] = m(1, 0) = (m, 0)$. On a genus-$2$ surface with generators $a_1, b_1, a_2, b_2$ and relation $[a_1, b_1][a_2, b_2] = 1$, the Hurewicz map sends $a_i, b_i$ to the standard basis of $H_1 = \mathbb{Z}^4$; the commutator relation dies in the abelianisation (it maps to $0$). Full detail: [[Def - First Homology, Characters, and Finite Fourier Analysis]].

> [!recall]- Unitary character $\chi : H_1(X, \mathbb{Z}) \to S^1$
> **Formally:** a *unitary character* is a group homomorphism $\chi : H_1(X, \mathbb{Z}) \to S^1 = \{z \in \mathbb{C} : |z| = 1\}$; equivalently, a function $\chi : H_1 \to \mathbb{C}$ with $\chi(\beta_1 + \beta_2) = \chi(\beta_1)\chi(\beta_2)$ and $|\chi(\beta)| = 1$ for all $\beta_1, \beta_2, \beta \in H_1$. The set of unitary characters forms the *character torus* (Pontryagin dual) $\widehat{H_1(X, \mathbb{Z})} \cong (S^1)^r$: after choosing a $\mathbb{Z}$-basis $e_1, \ldots, e_r$ and phases $\theta_1, \ldots, \theta_r \in \mathbb{R}/\mathbb{Z}$, $\chi(e_j) = e^{2\pi i\theta_j}$ determines $\chi$ uniquely.
> **In words:** a rule for assigning a complex phase (unit-modulus complex number) to each homology class, in a way that respects addition of net windings (adding two homology classes multiplies their phases). Because $\chi$ is a homomorphism, it sends *integer multiples* to *integer powers*: $\chi(m\beta) = \chi(\beta)^m$. This power-of-a-scalar structure is what makes it possible to collapse the double sum over $(\gamma, m)$ into a sum over $\beta$ — the character weight at $(\gamma, m)$ is $\chi([\gamma])^m$, which by the homomorphism property equals $\chi(m[\gamma]) = \chi(\beta)$, a function of $\beta = m[\gamma]$ alone.
> **Concretely:** on the torus $T^2$ with $H_1 = \mathbb{Z}^2$, $\chi_{(u,v)}(a, b) = e^{2\pi i(au + bv)}$ for $(u, v) \in [0, 1)^2 = \widehat{H_1(T^2, \mathbb{Z})}$. The identity in play: $\chi_{(u,v)}((1, 0))^m = e^{2\pi i m u} = e^{2\pi i (m\cdot u)} = \chi_{(u,v)}(m, 0) = \chi_{(u,v)}(m\cdot(1, 0))$. Full detail: [[Def - First Homology, Characters, and Finite Fourier Analysis]].

> [!recall]- Corollary 6.4 log-expansion of $-\log L_X(s, \chi)$
> **Formally:** for $\chi$ a unitary character and $\operatorname{Re}s > \delta$,
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)),$$
> the double sum absolutely convergent by the Selberg-zeta convergence estimates for $\operatorname{Re}s > \delta$ (which use $|\chi([\gamma])^m| = 1$).
> **In words:** the log of the character-twisted Selberg zeta expands as a sum of killed loop masses over free homotopy classes, each weighted by the character phase $\chi([\gamma])^m$. Each $(\gamma, m)$ contributes its mass multiplied by the character value on the *specific pair* $(\gamma, m)$; but by the homomorphism identity below, this phase depends only on $\beta = m[\gamma]$, not on the individual $(\gamma, m)$.
> **Concretely:** on the toy $\Gamma = \langle\tau_0\rangle$ with $\ell = 1$, $s = 2$, $\chi_u([\tau_0^n]) = e^{2\pi i n u}$: $-\log L_X(2, \chi_u) = \sum_{m \ge 1}\frac{e^{2\pi i m u}\cdot e^{-m}}{m(e^m - 1)}$. Full derivation: [[Cor - Selberg L-Function Identity]].

---

# Claim / Identity

> **Claim (regrouping the Selberg $L$-function sum by homology).** Let $\chi \in \widehat{H_1(X, \mathbb{Z})}$ be a unitary character and $s$ with $\operatorname{Re}s > \delta$. Then, for every pair $(\gamma, m)$ with $\gamma \in \mathcal P_X$ and $m \ge 1$,
> $$\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta)\quad\text{whenever}\quad \beta := m[\gamma].\qquad (\bigstar)$$
> Consequently the double sum over free homotopy classes in [[Cor - Selberg L-Function Identity|Corollary 6.4]] regroups by homology class:
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)) = \sum_{\beta \in H_1(X, \mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta).\qquad (\bigstar\bigstar)$$

---

# In One Line

Because a unitary character is a group homomorphism, the character weight $\chi([\gamma])^m$ attached to the $(\gamma, m)$ term of Corollary 6.4 is really a function $\chi(\beta)$ of the homology class $\beta = m[\gamma]$ alone — so the double sum over free homotopy classes collapses to a single Fourier series over homology classes.

---

# Why It's True

**Mechanism.** *Iterating a loop $m$ times sends its homology class $[\gamma]$ to $m[\gamma]$ (the Hurewicz map is a homomorphism); a unitary character on the abelian group $H_1(X, \mathbb{Z})$ sends multiples to powers ($\chi(m\beta) = \chi(\beta)^m$). Composing these two homomorphism identities gives $\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta)$ whenever $\beta = m[\gamma]$. So the character phase in Cor 6.4 is a function of $\beta$ alone; every summand with the same $\beta$ carries the same phase; and the double sum regroups by $\beta$, with the inner sum recognised as $\mu^\kappa_X(\beta)$ by Definition 6.1.*

The identity is the smallest observation in §6.2, but everything else in §6.2 depends on it. It is the *reason* one grades by homology rather than homotopy in this construction: only the homology grading is compatible with character weighting, and only character weighting Fourier-inverts.

---

# Derivation

> [!note]- Gap-free derivation
>
> **Step 1 — Hurewicz iterates.** The Hurewicz map $h : \Gamma \twoheadrightarrow H_1(X, \mathbb{Z})$ is a group homomorphism from the multiplicatively-written $\Gamma$ to the additively-written abelianisation. So for every $\gamma \in \Gamma$ and every integer $m \ge 1$,
> $$[\gamma^m] = h(\gamma^m) = h(\gamma) + h(\gamma) + \cdots + h(\gamma)\ (\text{$m$ times}) = m\,h(\gamma) = m[\gamma].$$
>
> **Step 2 — character multiplicativity.** A unitary character $\chi : H_1(X, \mathbb{Z}) \to S^1$ is a group homomorphism from the additive group $H_1$ to the multiplicative group $S^1$: $\chi(\beta_1 + \beta_2) = \chi(\beta_1)\chi(\beta_2)$. Iterated, $\chi(m\beta) = \chi(\beta)^m$ for every integer $m$ (in particular $\chi(0) = \chi(\beta)^0 = 1$).
>
> **Step 3 — compose the two identities to get $(\bigstar)$.** For any $(\gamma, m)$, define $\beta := m[\gamma]$ (Step 1). Then
> $$\chi([\gamma])^m \underset{\text{Step 2}}{=} \chi(m[\gamma]) \underset{\text{def. of }\beta}{=} \chi(\beta).$$
> This is $(\bigstar)$. The identity depends on nothing about $\gamma$ except its homology class $[\gamma]$, and depends on $m$ only through the product $m[\gamma] = \beta$.
>
> **Step 4 — regroup the Corollary 6.4 sum by $\beta$ (proof of $(\bigstar\bigstar)$).** Start from Corollary 6.4:
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)).$$
> The index set $I := \{(\gamma, m) : \gamma \in \mathcal P_X,\ m \ge 1\}$ partitions as $I = \bigsqcup_{\beta \in H_1(X, \mathbb{Z})}I_\beta$, where $I_\beta := \{(\gamma, m) \in I : m[\gamma] = \beta\}$; the sets $I_\beta$ are pairwise disjoint (each $(\gamma, m)$ has a unique image $m[\gamma]$) and their union is all of $I$. The double sum is absolutely convergent for $\operatorname{Re}s > \delta$ (because $|\chi([\gamma])^m| = 1$, so absolute values reduce to the untwisted Selberg zeta convergence), which lets us rearrange it (Fubini) by summing over $\beta$ first:
> $$-\log L_X(s, \chi) = \sum_{\beta \in H_1(X, \mathbb{Z})}\sum_{(\gamma, m) \in I_\beta}\chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)).$$
> Inside $I_\beta$ we have $\chi([\gamma])^m = \chi(\beta)$ by $(\bigstar)$, a constant in $(\gamma, m)$; pull it out:
> $$= \sum_{\beta \in H_1(X, \mathbb{Z})}\chi(\beta)\underbrace{\sum_{(\gamma, m) \in I_\beta}\mu^\kappa_X(C_X(\gamma^m))}_{= \mu^\kappa_X(\beta)\ \text{by Def 6.1}} = \sum_{\beta \in H_1(X, \mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta).$$
> The identification of the inner sum with $\mu^\kappa_X(\beta)$ is the definition of the *mass in a homology class* (Definition 6.1). This is $(\bigstar\bigstar)$. $\blacksquare$
>
> **Sanity check: $\chi \equiv 1$.** With the trivial character, $\chi(\beta) = 1$ for every $\beta$, and $(\bigstar\bigstar)$ collapses to $-\log Z_X(s) = \sum_\beta \mu^\kappa_X(\beta) = \sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))$ — the untwisted Selberg zeta identity ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Cor 4.3]]), recovered by summing homology-graded masses over all $\beta$. **Sanity check: torus.** On $T^2$ with $\Gamma = \mathbb{Z}^2$ abelian, the Hurewicz map is the identity, so each homology class $\beta = (a, b)$ contains exactly one *free-homotopy* class $C_{T^2}(\gamma_{(a,b)})$; the inner sum in Step 4 has a single term and $\mu^\kappa_{T^2}(\beta) = \mu^\kappa_{T^2}(C_{T^2}(\gamma_{(a,b)}))$ directly. Homology and homotopy coincide in the abelian case.

---

# Where the paper uses this

Stated inline in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]], immediately after Definition 6.1 (as the motivation for grading by homology and for introducing the Selberg $L$-function of Def 6.3). Explicitly recalled in [[Remark - Provenance of the Homology Class Definition|Remark 6.2]] as "the mechanism that makes the regrouping tractable." Applied as Step 1 of the proof of [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]] (Fourier expansion by homology class) and again inside the intensity-integral evaluation in the proof of [[Prop - Total Homology of the Loop Soup|Proposition 6.7]].
