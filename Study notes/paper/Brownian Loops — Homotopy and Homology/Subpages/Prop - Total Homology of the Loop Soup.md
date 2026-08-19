---
type: proposition
subject: probability-geometry
prereqs:
  - "Def - Poisson Point Process and the Loop Soup"
  - "Thm - Fourier Inversion by Homology Class"
  - "Cor - Selberg L-Function Identity"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, homology, point-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 6.7"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface with $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$.
- $\kappa > 0$ the killing rate, $s = \frac12 + \sqrt{\frac14 + \kappa}$ the spectral parameter, $\operatorname{Re}s > \delta$.
- $\mu^\kappa_X$ the killed Brownian loop measure on the loop space $C_X$; total mass $-\log Z_X(s) < \infty$.
- $\lambda > 0$ the intensity of the loop soup; $\mathcal L_\lambda$ the Poisson point process on $C_X$ with intensity measure $\lambda\,\mu^\kappa_X$ (a random countable collection of loops on $X$).
- $\mathcal L^*_\lambda \subset \mathcal L_\lambda$ the *non-contractible, non-cusp-peripheral* loops of the soup: those whose free-homotopy class is neither the trivial class nor a class winding only around a cusp; equivalently, those with a non-trivial homology-class-carrying representative.
- $[\eta] \in H_1(X, \mathbb{Z})$ the homology class of a loop $\eta \in C_X$ (well-defined for $\eta \in \mathcal L^*_\lambda$).
- $\beta(\lambda) := \sum_{\eta \in \mathcal L^*_\lambda}[\eta] \in H_1(X, \mathbb{Z})$ the *total homology* of the loop soup — a random element of $H_1(X, \mathbb{Z})$; the sum is over the finitely-many-with-probability-one non-trivial loops in $\mathcal L_\lambda$, so it makes sense as a finite integer-vector sum.
- $L_X(s, \chi)$ the Selberg $L$-function; $Z_X(s)$ the Selberg zeta; $\widehat{H_1(X, \mathbb{Z})}$ the character torus with Haar measure $d\chi$.

> [!recall]- Loop soup $\mathcal L_\lambda$ and its counts
> **Formally:** for the σ-finite intensity $\lambda\,\mu^\kappa_X$ on the loop space $(C_X, \mathcal C_X)$, the *loop soup* $\mathcal L_\lambda$ is the Poisson point process with that intensity — a random countable subset $\mathcal L_\lambda \subset C_X$ (equivalently a random integer-valued measure $\sum_{\eta}\delta_\eta$) satisfying (i) for every measurable $A \subset C_X$ with $\mu^\kappa_X(A) < \infty$, the count $N_A := \#(\mathcal L_\lambda \cap A)$ is Poisson with mean $\lambda\,\mu^\kappa_X(A)$; (ii) disjoint measurable sets give independent counts.
> **In words:** a random scatter of loops on $X$; the number of loops falling into any given measurable class is Poisson with mean the class's mass times $\lambda$; loops in disjoint classes are counted independently. Feeding the killed loop measure in as intensity is what turns each numerical mass into a distributional statement.
> **Concretely:** on a surface with total killed-loop mass $-\log Z_X(s) = 0.68$ and intensity $\lambda = 1$, the total number of non-trivial soup loops $\#\mathcal L^*_\lambda$ is Poisson with mean $-\lambda\log Z_X(s) = 0.68$: about $51\%$ chance of $0$ loops, $35\%$ chance of $1$, $12\%$ chance of $2$, $3\%$ chance of $\ge 3$. Each loop, given it exists, has homology class distributed according to $\mu^\kappa_X(\beta)/(-\log Z_X(s))$. Full detail: [[Def - Poisson Point Process and the Loop Soup]].

> [!recall]- Poisson exponential (Campbell) formula
> **Formally:** for a Poisson point process $\Pi$ on $(S, \mathcal S)$ with σ-finite intensity $\Lambda$, and a measurable $F : S \to \mathbb{C}$ satisfying $\int_S(|e^{F} - 1|)\,d\Lambda < \infty$,
> $$\mathbb{E}\Big[\prod_{x \in \Pi}e^{F(x)}\Big] = \exp\!\Big(\int_S(e^{F(x)} - 1)\,\Lambda(dx)\Big).$$
> Convergence of the RHS integral is exactly what ensures the LHS product is a.s. finite and integrable.
> **In words:** the expectation of an $F$-multiplicative functional of a Poisson process is $\exp$ of an *additive* functional $e^F - 1$ integrated against the intensity — the fundamental "multiplicative-to-additive" identity for Poisson processes. Proof sketch: condition on $\#\Pi \cap A = n$ for each finite-mass region $A$; the $n$ points are i.i.d. from $\Lambda/\Lambda(A)$; expectations of products of i.i.d. become $n$-th powers of a single expectation, and the Poisson mixture over $n$ turns the moment-generating polynomial into $\exp$.
> **Concretely:** for a Poisson process on $\mathbb{R}$ of rate $\lambda$ (intensity $\Lambda = \lambda\,dx$), taking $F(x) = \log(1 + f(x))$ for $f \ge 0$ integrable gives $\mathbb{E}\prod(1 + f(x_i)) = \exp(\lambda \int f\,dx)$ — the classical Campbell identity. Reference: Kingman, *Poisson Processes*, §3.

---

# Statement

> **Proposition 6.7 (distribution of the loop soup's total homology; Belyaev–Huseynli 6.7).** Let $s = \frac12 + \sqrt{\frac14 + \kappa}$ with $\operatorname{Re}s > \delta$; let $\mathcal L_\lambda$ be the killed Brownian loop soup of intensity $\lambda > 0$; and let
> $$\beta(\lambda) := \sum_{\eta \in \mathcal L^*_\lambda}[\eta] \in H_1(X, \mathbb{Z})$$
> be the total homology of the non-contractible, non-cusp-peripheral loops in the soup. The sum is finite almost surely, because $\#\mathcal L^*_\lambda$ is Poisson of finite mean $\lambda\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m)) = -\lambda\log Z_X(s)$.
>
> Then, for every unitary character $\chi \in \widehat{H_1(X, \mathbb{Z})}$,
> $$\mathbb{E}\big[\chi(\beta(\lambda))\big] = \Big(\frac{Z_X(s)}{L_X(s, \chi)}\Big)^{\!\lambda},\qquad (\ast)$$
> and consequently, for each $\beta \in H_1(X, \mathbb{Z})$,
> $$\mathbb{P}\big(\beta(\lambda) = \beta\big) = Z_X(s)^\lambda\int_{\widehat{H_1(X, \mathbb{Z})}}L_X(s, \chi)^{-\lambda}\,\overline{\chi(\beta)}\,d\chi. \qquad (\ast\ast)$$
> The complex power is defined by $L_X(s, \chi)^{-\lambda} := \exp(-\lambda\log L_X(s, \chi))$ with $\log L_X(s, \chi)$ given by Corollary 6.4.

---

# In One Line

The characteristic function of the loop soup's net homology is $(Z_X(s)/L_X(s, \chi))^\lambda$; Fourier-inverting on the character torus gives the probability of each total-homology value $\beta$ as an integral of $L_X(s, \chi)^{-\lambda}$ against $\overline{\chi(\beta)}$.

---

# Why It's True

**Mechanism.** *For $\chi$ a unitary character, $\prod_{\eta \in \mathcal L^*_\lambda}\chi([\eta]) = \chi(\sum_\eta [\eta]) = \chi(\beta(\lambda))$ (character = homomorphism); the Poisson exponential formula turns the expectation of this product into $\exp$ of $\lambda\int(\chi([\eta]) - 1)\,d\mu^\kappa_X$; two applications of the Selberg-family identities (Corollary 6.4 for the $\chi([\eta])$ term, Corollary 4.3 for the $-1$ term) evaluate the integral as $-\log L_X(s, \chi) + \log Z_X(s)$; exponentiating gives $(\ast)$. Multiplying $(\ast)$ by $\overline{\chi(\beta)}$ and integrating over the character torus, character orthogonality isolates $\beta$ and gives $(\ast\ast)$.*

The Poisson exponential formula is what turns the sum-over-loops in the exponent of $\chi(\beta(\lambda))$ into an *integral* against the intensity — that is, into an object the Selberg-family identities can evaluate. Fourier inversion then recovers the discrete distribution from its characteristic function.

---

# Proof

> [!note]- Gap-free proof
> **Step 0 — the Poisson exponential (Campbell) formula.**
>
> > [!cite]- External input — Poisson exponential formula
> > **Statement (typed):** for a Poisson point process $\Pi$ on a measurable space $(S, \mathcal S)$ with σ-finite intensity $\Lambda$, and any measurable $F : S \to \mathbb{C}$ with $\int_S|e^{F(x)} - 1|\,\Lambda(dx) < \infty$,
> > $$\mathbb{E}\Big[\prod_{x \in \Pi}e^{F(x)}\Big] = \exp\Big(\int_S(e^{F(x)} - 1)\,\Lambda(dx)\Big).$$
> > **Why it's true (intuition):** conditional on the counts in a finite partition, the points are i.i.d. from $\Lambda/\Lambda(\cdot)$; the product's expectation factorises; summing over Poisson-distributed counts gives $\exp$ of the additive functional. **Source:** Kingman, *Poisson Processes* (1993), §3.3.
>
> **Step 1 — apply Campbell with $e^F = \chi$.** Take $F(\eta) := \log\chi([\eta])$ (a $\mathbb{C}$-valued function of the loop; on $\mathcal L^*_\lambda$ we choose a measurable branch of $\log$ into $[0, 2\pi i)$, which is fine since $|\chi([\eta])| = 1$). Then $e^{F(\eta)} = \chi([\eta])$, and
> $$\prod_{\eta \in \mathcal L^*_\lambda}e^{F(\eta)} = \prod_{\eta}\chi([\eta]) = \chi\Big(\sum_{\eta}[\eta]\Big) = \chi(\beta(\lambda)),$$
> using the character homomorphism $\chi(\beta_1 + \beta_2) = \chi(\beta_1)\chi(\beta_2)$ iterated over the finite (a.s.) sum. So
> $$\mathbb{E}[\chi(\beta(\lambda))] = \mathbb{E}\Big[\prod_{\eta \in \mathcal L^*_\lambda}e^{F(\eta)}\Big] = \exp\Big(\lambda\int_{C_X^*}(\chi([\eta]) - 1)\,\mu^\kappa_X(d\eta)\Big),$$
> where the intensity of $\mathcal L^*_\lambda$ is $\lambda\mu^\kappa_X$ restricted to non-contractible non-cusp-peripheral loops, and $C_X^*$ denotes that subset of loop space. The integrability hypothesis $\int|\chi([\eta]) - 1|\,d\mu^\kappa_X \le 2\int d\mu^\kappa_X = 2(-\log Z_X(s)) < \infty$ is satisfied.
>
> **Step 2 — evaluate the intensity integral by the Selberg identities.** The measure $\mu^\kappa_X$ restricted to $C_X^*$ decomposes over free homotopy classes (§3.1.2):
> $$\int_{C_X^*}(\chi([\eta]) - 1)\,\mu^\kappa_X(d\eta) = \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}(\chi([\gamma])^m - 1)\,\mu^\kappa_X(C_X(\gamma^m)),$$
> where $\chi([\eta]) = \chi([\gamma])^m$ for $\eta \in C_X(\gamma^m)$ (using $[\gamma^m] = m[\gamma]$ and $\chi(m[\gamma]) = \chi([\gamma])^m$). Split into two sums:
> $$\sum_{\gamma, m}\chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)) \;-\; \sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m)).$$
> The first is $-\log L_X(s, \chi)$ by [[Cor - Selberg L-Function Identity|Corollary 6.4]]. The second is $-\log Z_X(s)$ by [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] (or Cor 6.4 with $\chi \equiv 1$). Together:
> $$\lambda\int_{C_X^*}(\chi([\eta]) - 1)\,\mu^\kappa_X(d\eta) = \lambda\big(-\log L_X(s, \chi) + \log Z_X(s)\big) = \lambda\log\frac{Z_X(s)}{L_X(s, \chi)}.$$
> Exponentiating,
> $$\mathbb{E}[\chi(\beta(\lambda))] = \exp\Big(\lambda\log\frac{Z_X(s)}{L_X(s, \chi)}\Big) = \Big(\frac{Z_X(s)}{L_X(s, \chi)}\Big)^{\!\lambda},$$
> which is $(\ast)$.
>
> **Step 3 — Fourier-invert on the character torus.** Multiply $(\ast)$ by $\overline{\chi(\beta)}$ and integrate over $\widehat{H_1(X, \mathbb{Z})}$ against normalised Haar measure $d\chi$:
> $$\int_{\widehat{H_1}}\mathbb{E}[\chi(\beta(\lambda))]\,\overline{\chi(\beta)}\,d\chi = \int_{\widehat{H_1}}\Big(\frac{Z_X(s)}{L_X(s, \chi)}\Big)^{\!\lambda}\overline{\chi(\beta)}\,d\chi = Z_X(s)^\lambda\int_{\widehat{H_1}}L_X(s, \chi)^{-\lambda}\overline{\chi(\beta)}\,d\chi. \tag{i}$$
> On the other side, since $\beta(\lambda)$ takes values in the countable set $H_1(X, \mathbb{Z})$,
> $$\mathbb{E}[\chi(\beta(\lambda))] = \sum_{\beta' \in H_1(X, \mathbb{Z})}\mathbb{P}(\beta(\lambda) = \beta')\,\chi(\beta'),$$
> and integrating against $\overline{\chi(\beta)}$, swapping sum and integral (justified by $|\chi(\beta')| = 1$ and $\sum_{\beta'}\mathbb{P}(\cdot) = 1$, so the integrand is dominated by $1$),
> $$\int_{\widehat{H_1}}\mathbb{E}[\chi(\beta(\lambda))]\,\overline{\chi(\beta)}\,d\chi = \sum_{\beta'}\mathbb{P}(\beta(\lambda) = \beta')\int_{\widehat{H_1}}\chi(\beta')\overline{\chi(\beta)}\,d\chi = \mathbb{P}(\beta(\lambda) = \beta), \tag{ii}$$
> by [[Def - First Homology, Characters, and Finite Fourier Analysis|character orthogonality]] (only $\beta' = \beta$ survives). Equating (i) and (ii),
> $$\mathbb{P}(\beta(\lambda) = \beta) = Z_X(s)^\lambda\int_{\widehat{H_1}}L_X(s, \chi)^{-\lambda}\overline{\chi(\beta)}\,d\chi,$$
> which is $(\ast\ast)$. $\blacksquare$

**Sanity check: $\lambda \to 0^+$.** For small intensity the soup is empty with high probability, so $\beta(\lambda) = 0$ w.h.p. Indeed $(\ast)$ gives $\mathbb{E}[\chi(\beta(\lambda))] = (Z_X(s)/L_X(s, \chi))^\lambda \to 1$ as $\lambda \to 0^+$ (for any fixed $\chi$), so the characteristic function tends to $1$: $\beta(\lambda) \to 0$ in distribution. And $\mathbb{P}(\beta(\lambda) = 0) = Z_X(s)^\lambda\int L_X(s, \chi)^{-\lambda}d\chi \to 1$ as $\lambda \to 0^+$ (the integrand $\to 1$, and $Z_X(s)^\lambda \to 1$). Consistent.

**Sanity check: $\chi \equiv 1$.** With the trivial character, $L_X(s, \chi) = Z_X(s)$, so $(Z_X(s)/L_X(s, \chi))^\lambda = 1 = \mathbb{E}[1] = \mathbb{E}[\chi(\beta(\lambda))]$ — trivially. This is the correct normalisation: the "$0$-th Fourier coefficient" of the characteristic function equals $1$.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]] as Proposition 6.7. It is the paper's final § 6 statement — completing the promise of §6.2 to give not just the *mean* mass in each homology class ($\mu^\kappa_X(\beta)$ via Theorem 6.5) but the full *distribution* of the loop soup's total homology (via the Poisson exponential). Downstream, §7 lifts the whole homotopy/homology framework to hyperbolic $3$-manifolds; the analogous proposition there would follow from the same Campbell + Selberg-identity mechanism.
