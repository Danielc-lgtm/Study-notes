---
type: definition
subject: geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
tags: [paper, zeta-functions, homology]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 6.3"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\mathcal P_X$ its set of oriented primitive closed geodesics; $\ell_\gamma > 0$ the length of $\gamma \in \mathcal P_X$; $[\gamma] \in H_1(X, \mathbb{Z})$ its homology class.
- $s \in \mathbb{C}$ the spectral/zeta variable; $\delta$ the critical exponent of $\Gamma$; the definition below converges absolutely for $\operatorname{Re}s > \delta$.
- $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$ the first homology group; $\chi : H_1(X, \mathbb{Z}) \to S^1$ a *unitary character* (group homomorphism into the unit circle $S^1 = \{z \in \mathbb{C} : |z| = 1\}$); $\widehat{H_1(X, \mathbb{Z})} \cong (S^1)^r$ the character torus.
- $Z_X(s) = \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$ the (untwisted) Selberg zeta function.

> [!recall]- Selberg zeta function $Z_X(s)$
> **Formally:** for $\operatorname{Re}s > \delta$, $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$; the double product converges absolutely and extends meromorphically to all of $\mathbb{C}$. Its logarithm expands term-wise as $-\log Z_X(s) = \sum_{\gamma, m \ge 1}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$.
> **In words:** an analytic function built as an infinite product with one factor per closed geodesic $\gamma$ and per integer $k \ge 0$. The whole product converges for $s$ sufficiently large; the shape is that of a "geodesic determinant". Zeros of $Z_X$ encode Laplace-eigenvalues by the Selberg trace formula. In this note, replacing $1$ by $\chi([\gamma])\cdot 1$ in each factor twists the product by a character.
> **Concretely:** for a toy $\Gamma = \langle \tau_0 \rangle$ with $\tau_0 : z \mapsto e z$ (one primitive geodesic of length $\ell = 1$), $Z_X(s) = \prod_{k \ge 0}(1 - e^{-(s+k)})$; at $s = 2$, $Z_X(2) = (1-e^{-2})(1-e^{-3})(1-e^{-4})\cdots \approx 0.774$. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Unitary character $\chi$ of $H_1(X, \mathbb{Z})$
> **Formally:** a *unitary character* is a group homomorphism $\chi : H_1(X, \mathbb{Z}) \to S^1$. Since $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$, a character is fixed by its values $\chi(e_j) = e^{2\pi i \theta_j} \in S^1$ on a $\mathbb{Z}$-basis $e_1, \ldots, e_r$, so the set of unitary characters (the *character torus* $\widehat{H_1(X, \mathbb{Z})}$) is itself the compact torus $(S^1)^r = (\mathbb{R}/\mathbb{Z})^r$. Homomorphism: $\chi(\beta_1 + \beta_2) = \chi(\beta_1)\chi(\beta_2)$; in particular $\chi([\gamma^m]) = \chi(m[\gamma]) = \chi([\gamma])^m$.
> **In words:** a way of assigning to each net-winding vector $\beta \in \mathbb{Z}^r$ a complex phase $\chi(\beta) \in S^1$ that respects addition of windings. The character-torus is exactly the set of such phase assignments; you can integrate over it (using normalised Haar measure) to average a function of $\chi$, and character orthogonality then Fourier-inverts. In the definition below, each closed geodesic $\gamma$ contributes not just the length $\ell_\gamma$ but also the phase $\chi([\gamma])$ of its net winding — a homology-dependent weight.
> **Concretely:** on the torus $T^2$ with $H_1 = \mathbb{Z}^2$, the characters are $\chi_{(u, v)}(a, b) = e^{2\pi i(au + bv)}$, parametrised by $(u, v) \in [0, 1)^2$; the character torus is $[0, 1)^2$ with Haar measure $du\,dv$. On a genus-$2$ closed surface, $H_1 = \mathbb{Z}^4$ and the character torus is $[0, 1)^4$. Full detail: [[Def - First Homology, Characters, and Finite Fourier Analysis]].

---

# Statement

> **Definition 6.3 (Selberg $L$-function; Belyaev–Huseynli 6.3).** For a unitary character $\chi : H_1(X, \mathbb{Z}) \to S^1$ and $\operatorname{Re}s > \delta$,
> $$L_X(s, \chi) := \prod_{\gamma \in \mathcal P_X}\prod_{k = 0}^{\infty}\big(1 - \chi([\gamma])\,e^{-(s + k)\ell_\gamma}\big).$$
> This is the Selberg zeta function twisted by the one-dimensional unitary representation $\chi$: the double product converges absolutely for $\operatorname{Re}s > \delta$ (because $|\chi([\gamma])| = 1$ makes the twisted terms have the same absolute size as the untwisted ones), and $L_X(s, \chi)$ extends meromorphically to all of $\mathbb{C}$. When $\chi \equiv 1$ is the trivial character, $\chi([\gamma]) = 1$ for every $\gamma$, so $L_X(s, \chi) = Z_X(s)$.

---

# In One Line

The Selberg zeta with each geodesic factor multiplied by a character-value phase $\chi([\gamma])$ — the geodesic analogue of a Dirichlet $L$-function, engineered so that its logarithm's Fourier coefficients on the character torus are exactly the homology-class masses $\mu^\kappa_X(\beta)$.

---

# Motivation and Unpacking

**The number-theoretic analogy.** For the Riemann zeta / Dirichlet $L$-functions, one starts with a product over primes $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ and twists it by a Dirichlet character $\chi : (\mathbb{Z}/n)^\times \to S^1$ to get $L(s, \chi) = \prod_p (1 - \chi(p)p^{-s})^{-1}$; the twisted logarithm's Fourier coefficients over the character group then detect *primes in a fixed arithmetic progression modulo $n$*. Here the story runs identically with the substitutions "primes $\to$ closed geodesics", "$\mathbb{Z}/n$ modular arithmetic $\to$ integer homology $H_1(X, \mathbb{Z})$": twisting the Selberg zeta by a unitary character of $H_1$ produces a generating function whose Fourier coefficients over the character torus detect *primitive geodesic iterates in a fixed homology class*.

**Structural sanity check: $\chi \equiv 1$ gives back Selberg.** If $\chi$ is the trivial character (mapping every $\beta$ to $1 \in S^1$), each factor $1 - \chi([\gamma])e^{-(s+k)\ell_\gamma} = 1 - e^{-(s+k)\ell_\gamma}$ is exactly a Selberg-zeta factor, so $L_X(s, \chi) = Z_X(s)$. This is a healthy sanity check: the untwisted case is recovered, and integrating a general $L_X(s, \chi)$ over the character torus against the trivial character should reproduce (up to a total-mass normalisation) the untwisted Selberg identity.

**Convergence and meromorphic continuation.** Absolute convergence of the double product for $\operatorname{Re}s > \delta$ is immediate: $|1 - \chi([\gamma])e^{-(s+k)\ell_\gamma}| = |1 - z|$ with $|z| = e^{-(\operatorname{Re}s + k)\ell_\gamma} < 1$, so $-\log(1 - z) = \sum_{m \ge 1}z^m/m$ converges and $|-\log(1 - z)| \le -\log(1 - |z|)$, so the log of the product is bounded by the untwisted $-\log Z_X(s)$ in absolute value. Meromorphic continuation is a standard consequence of the Selberg-zeta continuation (applied character by character); the paper cites this rather than reproving it, and the notes take it as given.

**Concretely.** On the toy surface $\Gamma = \langle \tau_0 \rangle$ with $\ell = 1$ and $H_1 = \mathbb{Z}$ generated by $[\tau_0]$, a character $\chi_u([\tau_0^n]) = e^{2\pi i n u}$ ($u \in [0, 1)$) gives $L_X(s, \chi_u) = \prod_{k \ge 0}(1 - e^{2\pi i u}e^{-(s+k)})$: at $s = 2$, $u = 1/2$ (so $\chi([\tau_0]) = -1$), $L_X(2, \chi_{1/2}) = \prod_{k \ge 0}(1 + e^{-(2+k)}) = (1 + e^{-2})(1 + e^{-3})\cdots \approx 1.155\cdot 1.050\cdot 1.018\cdots \approx 1.245$; the untwisted $Z_X(2) \approx 0.774$. The twist visibly changes the value; averaging $L_X(2, \chi_u)$-related quantities in $u \in [0, 1)$ against $e^{-2\pi i n u}$ then extracts the mass in homology class $n$.

**Why the twist is by a *character*, not by a more general representation.** The Ruelle zeta ($R_X(s) = Z_X(s)/Z_X(s+1)$) has a *matrix-valued* twist by a finite-dimensional representation $\rho : \Gamma \to \mathrm{GL}(V_\rho)$, giving $R_X(s, \rho) = \prod_{\gamma}\det(I - \rho(\tau)e^{-s\ell_\gamma})$ (see [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]]). For the *Selberg* zeta, the same matrix twist exists but is heavier machinery. The paper needs only the one-dimensional case — characters $\chi : \Gamma \to S^1$ that factor through the abelianisation $H_1$ — because these are exactly the objects that Fourier-invert over the *abelian* group $H_1$ to detect a fixed homology class. Higher-dimensional representations $\rho$ would detect finer information (irreducible representations of the whole non-abelian $\Gamma$, via a Peter–Weyl expansion) but are not needed for the homology-class question.

**Standard names.** *Selberg $L$-function*, *twisted Selberg zeta*; the *twist* is by a *one-dimensional unitary character* of $H_1(X, \mathbb{Z})$, equivalently a unitary representation $\chi : \Gamma \to S^1$ that factors through the abelianisation. Reference: Bunke–Olbrich, *Selberg zeta and theta functions* (1995); Fried, *The zeta functions of Ruelle and Selberg I* (1986).

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]] as Definition 6.3. Its log-expansion is [[Cor - Selberg L-Function Identity|Corollary 6.4]], which regroups the log-expansion by homology class $\beta$ (using $\chi([\gamma])^m = \chi(\beta)$ when $m[\gamma] = \beta$). Fourier inversion on the character torus then gives [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]], and the Poisson exponential formula composed with the identity gives the total-homology distribution of the loop soup in [[Prop - Total Homology of the Loop Soup|Proposition 6.7]].
