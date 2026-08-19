---
type: corollary
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.6"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface with critical exponent $\delta$.
- $\mathcal P_X$ — the primitive oriented closed geodesics of $X$; each $\gamma$ of length $\ell_\gamma > 0$.
- $\tau \in \Gamma$ — the primitive hyperbolic element representing $\gamma$; $\tau^m$ represents the winding-$m$ class.
- $\rho : \Gamma \to \mathrm{GL}(V_\rho)$ — a finite-dimensional complex representation of $\Gamma$: a group homomorphism from $\Gamma$ to the invertible linear maps of a finite-dimensional complex vector space $V_\rho$, with $\dim V_\rho < \infty$. Not necessarily unitary.
- $c_\rho \in [0, \infty)$ — the convergence exponent of the twisted Ruelle product: the infimum of $s > 0$ such that $\prod_{\gamma}\det(I - \rho(\tau) e^{-s\ell_\gamma})$ converges absolutely. When $\rho$ is unitary, $c_\rho = \delta$.
- $\operatorname{tr}\rho(\tau^m) \in \mathbb C$ — the trace of the matrix $\rho(\tau^m) = \rho(\tau)^m \in \mathrm{GL}(V_\rho)$ (using that $\rho$ is a homomorphism).
- $s \in \mathbb C$ — the spectral variable, with $\operatorname{Re} s > \max(c_\rho, \frac12)$.
- $\kappa_-(s) := s(s - 1)$, $\kappa_+(s) := s(s + 1)$ — two killing rates keyed to $s$, chosen so that $\frac12 + \sqrt{\frac14 + \kappa_-(s)} = s$ and $\frac12 + \sqrt{\frac14 + \kappa_+(s)} = s + 1$.
- $\mu^{\kappa}_X$ — the killing-$\kappa$ Brownian loop measure on $X$.
- $R_X(s, \rho) := \prod_{\gamma \in \mathcal P_X}\det(I - \rho(\tau) e^{-s\ell_\gamma})$ — the twisted Ruelle zeta function; well-defined since $\det(I - \rho(q \tau q^{-1}) e^{-s\ell_\gamma}) = \det(\rho(q)(I - \rho(\tau)e^{-s\ell_\gamma})\rho(q^{-1})) = \det(I - \rho(\tau) e^{-s\ell_\gamma})$.

> [!recall]- Group representation $\rho : \Gamma \to \mathrm{GL}(V_\rho)$
> **Formally:** a **finite-dimensional complex representation** of a group $\Gamma$ is a group homomorphism $\rho : \Gamma \to \mathrm{GL}(V_\rho)$ where $V_\rho$ is a finite-dimensional complex vector space and $\mathrm{GL}(V_\rho)$ is the group of invertible linear maps $V_\rho \to V_\rho$. So $\rho(\mathrm{id}) = I$ (identity matrix) and $\rho(gh) = \rho(g)\rho(h)$ for all $g, h \in \Gamma$. $\rho$ is **unitary** if $V_\rho$ carries a Hermitian inner product and every $\rho(g)$ is unitary ($\rho(g)^*\rho(g) = I$).
> **In words:** a rule that assigns a matrix to every group element in a way that respects composition — multiplying two group elements is the same as multiplying their assigned matrices. It lets you "see" the group's structure through matrix algebra. Unitary means the matrices preserve length.
> **Concretely:** the **trivial representation** sends every $g \in \Gamma$ to the $1 \times 1$ identity matrix; here $V_\rho = \mathbb C$, $\dim = 1$, and $\rho(\tau) = 1$ for all $\tau$. Any **character** $\chi : \Gamma \to S^1 \subset \mathbb C^*$ is a $1$-dimensional unitary representation (a homomorphism to the unit circle). On the torus $\Gamma = \mathbb Z^2$, the characters are $\chi_{(u, v)}(a, b) = e^{2\pi i(au + bv)}$ for $(u, v) \in [0, 1)^2$. Higher-dimensional example: the standard representation of $\Gamma \subset \mathrm{PSL}(2, \mathbb R)$ into itself is $2$-dimensional.

> [!recall]- Twisted Ruelle zeta $R_X(s, \rho)$
> **Formally:** $R_X(s, \rho) := \prod_{\gamma \in \mathcal P_X}\det(I - \rho(\tau) e^{-s\ell_\gamma})$, a product of $\dim V_\rho \times \dim V_\rho$ determinants — one factor per closed geodesic — convergent for $\operatorname{Re} s > c_\rho$. The trivial representation recovers the ordinary Ruelle zeta $R_X(s) = \prod_\gamma (1 - e^{-s\ell_\gamma})$; a character $\chi$ gives $R_X(s, \chi) = \prod_\gamma (1 - \chi(\tau) e^{-s\ell_\gamma})$.
> **In words:** a variant of the Ruelle zeta function where each geodesic factor $1 - e^{-s\ell_\gamma}$ is replaced by a matrix determinant $\det(I - \rho(\tau)e^{-s\ell_\gamma})$; the matrix $\rho(\tau)$ records how the representation sees the geodesic. Taking $\det$ collapses the matrix back to a complex number, so the whole product is a complex number. This is a device to *sort loops by a group-theoretic label*.
> **Concretely:** on $T^2$ with $\Gamma = \mathbb Z^2$, the character $\chi_{(u,v)}(a, b) = e^{2\pi i(au + bv)}$ gives $R_X(s, \chi_{(u,v)}) = \prod_\gamma(1 - \chi_{(u,v)}(a_\gamma, b_\gamma) e^{-s\ell_\gamma})$: each geodesic labelled by its winding numbers $(a_\gamma, b_\gamma)$ contributes a phase $e^{2\pi i(a_\gamma u + b_\gamma v)}$. Integrating $(u, v) \in [0, 1)^2$ against the character $e^{-2\pi i(a_0 u + b_0 v)}$ picks out only the geodesics with $(a_\gamma, b_\gamma) = (a_0, b_0)$ — the homology-class projection §6 uses. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Determinant expansion $-\log\det(I - M) = \sum_{m \ge 1}\operatorname{tr}(M^m)/m$
> **Formally:** for a square complex matrix $M$ with spectral radius $\|M\| < 1$ (all eigenvalues strictly inside the unit disk), $\det(I - M) = \exp(\operatorname{tr}\log(I - M)) = \exp(-\sum_{m \ge 1}\operatorname{tr}(M^m)/m)$; equivalently $-\log\det(I - M) = \sum_{m \ge 1}\operatorname{tr}(M^m)/m$.
> **In words:** the log-determinant of $I - M$ is a linear function (trace) of $\log(I - M)$; expanding $\log(1 - x) = -\sum_{m \ge 1} x^m/m$ and taking the trace (linear!) gives the formula. It converts a product formula (over geodesics with matrix factors) into a sum over "$m$ times each geodesic" with a trace weighting.
> **Concretely:** for $M = \lambda I$ (scalar), $\det(I - \lambda I) = (1 - \lambda)^{\dim V}$ and $-\log\det(I - M) = -\dim V \log(1 - \lambda) = \dim V \sum_{m \ge 1}\lambda^m/m$; the formula says the same thing, since $\operatorname{tr}(\lambda^m I) = \dim V \cdot \lambda^m$. For $M = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.3\end{pmatrix}$, $-\log\det(I - M) = -\log(0.5) - \log(0.7) = \log 2 + \log(10/7) \approx 0.693 + 0.357 = 1.050$; the series gives $\sum_m (0.5^m + 0.3^m)/m = (0.5 + 0.25/2 + \ldots) + (0.3 + 0.09/2 + \ldots) \approx 0.693 + 0.357 = 1.050$. **Short derivation:** for $M$ diagonalisable with eigenvalues $\lambda_j$, $\det(I - M) = \prod_j(1 - \lambda_j)$, so $\log\det(I - M) = \sum_j \log(1 - \lambda_j) = -\sum_j \sum_m \lambda_j^m/m = -\sum_m (\sum_j \lambda_j^m)/m = -\sum_m \operatorname{tr}(M^m)/m$; extend to non-diagonalisable $M$ by continuity.

> [!recall]- Killed class-mass shape $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-\sigma)L}}{e^L - 1}$
> **Formally:** for killing rate $\kappa \ge -\frac14$ and spectral parameter $\sigma(\kappa) := \frac12 + \sqrt{\frac14 + \kappa}$, the killed class-mass computed in §3.1.2 is $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-\sigma(\kappa))L}}{e^L - 1}$ with $L = m\ell_\gamma$.
> **In words:** for the killed Brownian loop measure, each free homotopy class's mass has an explicit closed form: the $1/m$ from the winding, and a ratio of two exponentials in $L$ controlled by $\sigma$. This is what makes the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] applicable and, here, will produce the difference identity below.
> **Concretely:** at $\kappa = 0$ ($\sigma = 1$), $\mu^0_X(C_X(\gamma^m)) = \frac{1}{m(e^L - 1)}$ — the pure Brownian formula. At $\kappa = 2$ ($\sigma = 2$), $\mu^2_X(C_X(\gamma^m)) = \frac{e^{-L}}{m(e^L - 1)}$. Full detail: [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] and its §3.1.2 case.

---

# Statement

> **Corollary (twisted Ruelle zeta identity; Belyaev–Huseynli 4.6).** Let $\rho : \Gamma \to \mathrm{GL}(V_\rho)$ be a finite-dimensional complex representation with convergence exponent $c_\rho$, and set $\kappa_\pm(s) := s(s \pm 1)$ for $s \in \mathbb C$. Then for every $s$ with $\operatorname{Re} s > \max(c_\rho, \frac12)$,
> $$-\log R_X(s, \rho) \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\operatorname{tr}\rho(\tau^m)\,\Big[\mu^{\kappa_-(s)}_X\big(C_X(\gamma^m)\big) - \mu^{\kappa_+(s)}_X\big(C_X(\gamma^m)\big)\Big] \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-s m \ell_\gamma}}{m}.$$

---

# In One Line

$-\log$ of the twisted Ruelle zeta at $s$ is a **trace-weighted difference** of killed loop masses (killing rates $\kappa_-(s)$ and $\kappa_+(s)$), and the difference **telescopes** each class down to the clean $e^{-sm\ell_\gamma}/m$ term needed for the group-theoretic decomposition of §6 (characters, homology).

---

# Why It's True

**Mechanism (one sentence).** *The determinant expansion $-\log\det(I - M) = \sum_{m \ge 1}\operatorname{tr}(M^m)/m$ turns the twisted Ruelle product into a trace-weighted geodesic sum; independently, the difference of two killed class-masses at spectral parameters $s$ and $s + 1$ collapses algebraically to exactly the same trace-free sum $e^{-sm\ell_\gamma}/m$; matching the two gives the identity.*

The corollary has two conceptual jobs. First, it **exhibits** $-\log R_X(s, \rho)$ as a probabilistic quantity — a difference of loop masses weighted by a group character. Second, and more usefully for §6, it **isolates each geodesic's contribution as $e^{-sm\ell_\gamma}/m$**, without the Bessel-type $1/(e^L - 1)$ denominators of the raw class-masses. That clean shape is what lets §6 insert a character $\chi$ and integrate over the character group to project onto a single homology class.

The construction of $\kappa_\pm(s) := s(s \pm 1)$ is chosen precisely so that the two spectral parameters $\sigma(\kappa_\pm)$ are $s$ and $s + 1$; the difference of the two class-masses then telescopes.

---

# Proof

> [!note]- Gap-free proof of Corollary 4.6
> **Step 1 — apply the determinant expansion to the twisted Ruelle product.** For $\operatorname{Re} s > c_\rho$, the matrix $M_\gamma := \rho(\tau) e^{-s\ell_\gamma}$ satisfies $\|M_\gamma\| < 1$ (this is the meaning of $c_\rho$), so the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent#The Definition|determinant expansion]] applies to each factor:
> $$-\log\det(I - M_\gamma) \;=\; \sum_{m \ge 1}\frac{\operatorname{tr}(M_\gamma^m)}{m} \;=\; \sum_{m \ge 1}\frac{\operatorname{tr}\big(\rho(\tau) e^{-s\ell_\gamma}\big)^m}{m} \;=\; \sum_{m \ge 1}\frac{\operatorname{tr}\rho(\tau)^m\,e^{-sm\ell_\gamma}}{m}.$$
> The last equality uses that $\rho(\tau) e^{-s\ell_\gamma}$ is a scalar $e^{-s\ell_\gamma}$ times the matrix $\rho(\tau)$, so $(\rho(\tau) e^{-s\ell_\gamma})^m = \rho(\tau)^m e^{-sm\ell_\gamma}$. Since $\rho$ is a homomorphism, $\rho(\tau)^m = \rho(\tau^m)$. Summing over $\gamma$ and taking $-\log$ of the product,
> $$-\log R_X(s, \rho) \;=\; \sum_{\gamma \in \mathcal P_X}\sum_{m \ge 1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m} \qquad (*).$$
> The rearrangement of the (triple) sum is legitimate because the absolute value of each term is at most $\|\rho(\tau^m)\|\,e^{-\operatorname{Re}(s)\,m\ell_\gamma}/m$, and this is summable for $\operatorname{Re} s > c_\rho$ by definition of $c_\rho$. This proves the equality of the middle expression and the rightmost expression once we have Step 2's algebra.
>
> **Step 2 — compute the difference of two killed class-masses.** By the killed class-mass formula ([[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] with §3.1.2), for $\kappa \ge -\frac14$ and $\sigma(\kappa) := \frac12 + \sqrt{\frac14 + \kappa}$,
> $$\mu^\kappa_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{(1-\sigma(\kappa))L}}{e^L - 1}, \qquad L = m\ell_\gamma.$$
> Verify the branch identities: with $\kappa_-(s) = s(s - 1) = s^2 - s$, we have $\frac14 + \kappa_-(s) = \frac14 + s^2 - s = (s - \frac12)^2$, so $\sqrt{\frac14 + \kappa_-(s)} = s - \frac12$ (for $\operatorname{Re} s > \frac12$, the principal square root is $s - \frac12$), hence $\sigma(\kappa_-(s)) = \frac12 + (s - \frac12) = s$. Similarly $\frac14 + \kappa_+(s) = \frac14 + s^2 + s = (s + \frac12)^2$, so $\sqrt{\cdots} = s + \frac12$ and $\sigma(\kappa_+(s)) = s + 1$. So
> $$\mu^{\kappa_-(s)}_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{(1-s)L}}{e^L - 1}, \qquad \mu^{\kappa_+(s)}_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{(1-(s+1))L}}{e^L - 1} \;=\; \frac{1}{m}\cdot\frac{e^{-sL}}{e^L - 1}.$$
> Their difference is
> $$\mu^{\kappa_-(s)}_X\big(C_X(\gamma^m)\big) - \mu^{\kappa_+(s)}_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{(1-s)L} - e^{-sL}}{e^L - 1}.$$
> Factor the numerator: $e^{(1-s)L} - e^{-sL} = e^{-sL}(e^L - 1)$. So
> $$\mu^{\kappa_-(s)}_X\big(C_X(\gamma^m)\big) - \mu^{\kappa_+(s)}_X\big(C_X(\gamma^m)\big) \;=\; \frac{1}{m}\cdot\frac{e^{-sL}(e^L - 1)}{e^L - 1} \;=\; \frac{e^{-sL}}{m} \;=\; \frac{e^{-sm\ell_\gamma}}{m}.$$
> The denominator $e^L - 1$ cancels — this is the *telescoping* that makes the difference clean.
>
> **Step 3 — assemble the middle equality.** Multiplying the Step-2 difference by $\operatorname{tr}\rho(\tau^m)$ and summing over $\gamma \in \mathcal P_X$ and $m \ge 1$,
> $$\sum_{\gamma}\sum_{m \ge 1}\operatorname{tr}\rho(\tau^m)\,\big[\mu^{\kappa_-(s)}_X - \mu^{\kappa_+(s)}_X\big]\big(C_X(\gamma^m)\big) \;=\; \sum_{\gamma}\sum_{m \ge 1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m},$$
> which is exactly the right side of $(*)$. Combining with $(*)$,
> $$-\log R_X(s, \rho) \;=\; \sum_{\gamma}\sum_{m \ge 1}\operatorname{tr}\rho(\tau^m)\,\big[\mu^{\kappa_-(s)}_X - \mu^{\kappa_+(s)}_X\big]\big(C_X(\gamma^m)\big).$$
> The condition $\operatorname{Re} s > \max(c_\rho, \frac12)$ ensures both the Step-1 convergence ($c_\rho$) and the Step-2 branch choice ($\frac12$; and, via the reindexing $\sigma = s + 1 > \frac32$, also that the $\kappa_+(s)$-class-mass is well-defined). $\blacksquare$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.2]]. The identity is the paper's engine for the homology decomposition of **§6**: specialising $\rho$ to a unitary character $\chi : \Gamma \to S^1$ and integrating over the character group projects the trace-weighted sum onto individual first-homology classes, giving the probability measure on $H_1(X; \mathbb Z)$ that the paper's title advertises. The telescoping Step 2 — the algebraic cancellation of $e^L - 1$ — is what makes each class contribute the clean scalar $e^{-sm\ell_\gamma}/m$ that Fourier analysis in §6 can handle.
