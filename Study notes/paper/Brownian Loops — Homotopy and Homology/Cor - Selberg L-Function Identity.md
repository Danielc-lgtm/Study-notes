---
type: corollary
subject: probability-geometry
prereqs:
  - "Def - Selberg L-Function"
  - "Def - Mass in a Homology Class"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, zeta-functions, homology]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 6.4"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface.
- $\chi : H_1(X, \mathbb{Z}) \to S^1$ a unitary character; $\widehat{H_1(X, \mathbb{Z})}$ the character torus.
- $\mathcal P_X$ the set of oriented primitive closed geodesics; $\ell_\gamma > 0$ the length of $\gamma \in \mathcal P_X$; $[\gamma] \in H_1(X, \mathbb{Z})$ its homology class.
- $\kappa \ge -\tfrac14$ the killing parameter; $s = \tfrac12 + \sqrt{\tfrac14 + \kappa}$ the spectral parameter (assumed $\operatorname{Re}s > \delta$).
- $\mu^\kappa_X(C_X(\gamma^m))$ the killed loop-measure mass of the free homotopy class winding $m$ times around $\gamma$ (§3.1.2): $\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$.
- $L_X(s, \chi) = \prod_\gamma \prod_{k \ge 0}(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma})$ the Selberg $L$-function (Def 6.3).

> [!recall]- Unitary character satisfies $\chi([\gamma])^m = \chi(m[\gamma])$
> **Formally:** because $\chi : H_1(X, \mathbb{Z}) \to S^1$ is a group homomorphism, $\chi(\beta_1 + \beta_2) = \chi(\beta_1)\chi(\beta_2)$; applied $m$ times to $\beta = [\gamma]$ gives $\chi(m[\gamma]) = \chi([\gamma])^m$. Both sides are complex numbers of modulus $1$; $|\chi([\gamma])^m| = |\chi([\gamma])|^m = 1$.
> **In words:** the character value on "the class of $\gamma$ iterated $m$ times" is the $m$-th power of the character value on the class of $\gamma$. This is what makes the log-expansion of the $L$-function reorganisable into a sum indexed by pairs $(\gamma, m)$, weighted by a phase $\chi([\gamma])^m$ that depends only on the *homology* of the iterate.
> **Concretely:** on the torus $T^2$, $\chi_{(u,v)}((a, b)) = e^{2\pi i(au + bv)}$; iterating a horizontal loop $2$ times gives homology class $(2, 0)$, so $\chi_{(u,v)}((2, 0)) = e^{4\pi i u} = (e^{2\pi i u})^2 = \chi_{(u,v)}((1, 0))^2$ — the identity in play. See [[Def - First Homology, Characters, and Finite Fourier Analysis]].

> [!recall]- Killed loop-measure mass of $C_X(\gamma^m)$
> **Formally:** $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$, positive, with $s = \tfrac12 + \sqrt{\tfrac14 + \kappa}$. Summing over all pairs $(\gamma, m)$ gives $\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m)) = -\log Z_X(s)$, the Selberg zeta identity ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]).
> **In words:** the number attached to each free-homotopy loop class, exponentially penalising length; its total over all classes is a value of the Selberg zeta. The identity below writes the same partition function structure with a character insertion.
> **Concretely:** at $s = 2$, $\ell_\gamma = 1$, $m = 1$: $\mu^\kappa(C_X(\gamma)) = \frac11\cdot\frac{e^{-1}}{e - 1} \approx \frac{0.368}{1.718} \approx 0.214$. Full derivation: [[Thm - Mass of a Subordinate Brownian Loop Class]].

---

# Statement

> **Corollary 6.4 (Selberg $L$-function identity; Belyaev–Huseynli 6.4).** Let $\chi : H_1(X, \mathbb{Z}) \to S^1$ be a unitary character and $s = \tfrac12 + \sqrt{\tfrac14 + \kappa}$ with $\operatorname{Re}s > \delta$. Then
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \frac{1}{m}\cdot\chi([\gamma])^m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}.$$
> The middle expression is the log-expansion of the Selberg $L$-function, term-by-term equal to the sum of *character-weighted* free-homotopy-class masses; the right-hand equality substitutes the closed-form mass from §3.1.2.

---

# In One Line

The log of the Selberg $L$-function equals the sum of killed loop masses over free homotopy classes, each weighted by the character value $\chi([\gamma])^m$ of its net homology — the untwisted identity ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Cor 4.3]]) with a character insertion.

---

# Why It's True

**Mechanism.** *Expand the log of each Euler factor using $-\log(1 - z) = \sum_m z^m/m$ (valid since $|z| = |\chi([\gamma])|e^{-(\operatorname{Re}s + k)\ell_\gamma} < 1$ for $\operatorname{Re}s > 0$); sum the geometric series over $k$ to collapse the double product to a single sum over $m$; recognise the resulting summand as the closed-form killed loop mass, multiplied by $\chi([\gamma])^m$.*

This is the untwisted computation from the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta log-expansion]], with the modification that each factor now carries a character phase $\chi([\gamma])$. Because $|\chi([\gamma])| = 1$ the convergence estimates carry over unchanged, and because $\chi([\gamma])$ is $k$-independent it factors out of the $k$-sum, leaving the geometric-series identity from §4.1 untouched.

---

# Proof

> [!note]- Gap-free proof
> **Step 0 — take the log of the Euler product.** By definition, $L_X(s, \chi) = \prod_\gamma\prod_{k \ge 0}(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma})$; absolute convergence for $\operatorname{Re}s > \delta$ (established in Def 6.3, using $|\chi([\gamma])| = 1$) lets us take the logarithm term-by-term:
> $$-\log L_X(s, \chi) = -\sum_{\gamma \in \mathcal P_X}\sum_{k = 0}^\infty \log\!\big(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma}\big).$$
>
> **Step 1 — Taylor-expand each $-\log(1 - z)$.** For $z \in \mathbb{C}$ with $|z| < 1$, $-\log(1 - z) = \sum_{m = 1}^\infty \frac{z^m}{m}$. Here $z = \chi([\gamma])e^{-(s+k)\ell_\gamma}$, so $|z| = |\chi([\gamma])|\cdot e^{-(\operatorname{Re}s + k)\ell_\gamma} = e^{-(\operatorname{Re}s + k)\ell_\gamma} < 1$ whenever $\operatorname{Re}s + k > 0$ — automatically true for $\operatorname{Re}s > \delta > 0$ and $k \ge 0$. Hence
> $$-\log\!\big(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma}\big) = \sum_{m = 1}^\infty \frac{1}{m}\big(\chi([\gamma])e^{-(s+k)\ell_\gamma}\big)^{\!m} = \sum_{m = 1}^\infty \frac{\chi([\gamma])^m}{m}\,e^{-(s+k)m\ell_\gamma}.$$
>
> **Step 2 — swap the $k$-sum inside.** All terms are absolutely summable (bounded in modulus by the untwisted expansion, which converges by [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|the Selberg zeta convergence]] for $\operatorname{Re}s > \delta$), so
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \frac{\chi([\gamma])^m}{m}\underbrace{\sum_{k = 0}^\infty e^{-(s+k)m\ell_\gamma}}_{(*)}.$$
>
> **Step 3 — evaluate the inner geometric series $(*)$.** With $r := e^{-m\ell_\gamma} \in (0, 1)$,
> $$\sum_{k = 0}^\infty e^{-(s+k)m\ell_\gamma} = e^{-sm\ell_\gamma}\sum_{k = 0}^\infty r^k = \frac{e^{-sm\ell_\gamma}}{1 - e^{-m\ell_\gamma}} = \frac{e^{-sm\ell_\gamma}}{1 - e^{-m\ell_\gamma}}\cdot\frac{e^{m\ell_\gamma}}{e^{m\ell_\gamma}} = \frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1},$$
> where the last equality multiplied numerator and denominator by $e^{m\ell_\gamma}$.
>
> **Step 4 — substitute back and recognise the mass.** Combining:
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \frac{\chi([\gamma])^m}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1} = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \chi([\gamma])^m\underbrace{\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}}_{= \mu^\kappa_X(C_X(\gamma^m))\ \text{by §3.1.2}}.$$
> This is the identity. $\blacksquare$

**Sanity check: $\chi \equiv 1$.** With the trivial character $\chi([\gamma]) = 1$ for every $\gamma$, the identity collapses to $-\log Z_X(s) = \sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))$ — the [[Thm - Selberg Zeta Identity for the Total Loop Mass|untwisted Selberg zeta identity]] of Corollary 4.3. This is the correct limiting case: no character weight means every class contributes with weight $1$, and the sum is the total mass.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]]. The identity is the *pre*-Fourier form of the homology decomposition: [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]] regroups the double sum over $(\gamma, m)$ by their common homology class $\beta = m[\gamma]$ (using $\chi([\gamma])^m = \chi(\beta)$) and then Fourier-inverts on the character torus to extract each $\mu^\kappa_X(\beta)$. [[Prop - Total Homology of the Loop Soup|Proposition 6.7]] uses it as the $\chi \not\equiv 1$ input to the Poisson exponential formula.
