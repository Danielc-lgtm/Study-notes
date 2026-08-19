---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Selberg L-Function"
  - "Def - Mass in a Homology Class"
  - "Cor - Selberg L-Function Identity"
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
tags: [paper, brownian-loops, homology, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 6.5"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface (closed of genus $g$, or of genus $g$ with $b \ge 1$ ends).
- $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$, $r = 2g$ (closed) or $r = 2g + b - 1$ (with $b$ ends).
- $\widehat{H_1(X, \mathbb{Z})} \cong (S^1)^r$ the *character torus* (Pontryagin dual), a compact abelian group; $d\chi$ its normalised Haar measure (total mass $1$).
- $\beta \in H_1(X, \mathbb{Z})$ a homology class; $\chi \in \widehat{H_1(X, \mathbb{Z})}$ a unitary character; $\chi(\beta) \in S^1$ the phase; $\overline{\chi(\beta)}$ its complex conjugate.
- $\kappa \ge -\frac14$ the killing parameter; $s = \frac12 + \sqrt{\frac14 + \kappa}$; $\operatorname{Re}s > \delta$.
- $L_X(s, \chi) = \prod_\gamma \prod_{k \ge 0}(1 - \chi([\gamma])e^{-(s+k)\ell_\gamma})$ the Selberg $L$-function.
- $\mu^\kappa_X(\beta) = \sum_{m[\gamma] = \beta}\mu^\kappa_X(C_X(\gamma^m))$ the killed loop mass in homology class $\beta$ (Def 6.1).

> [!recall]- Character orthogonality on the torus $\widehat{H_1(X, \mathbb{Z})}$
> **Formally:** the character torus $\widehat{H_1(X, \mathbb{Z})} \cong (S^1)^r$ is a compact abelian group; its *normalised Haar measure* $d\chi$ is the unique translation-invariant probability measure on it (concretely, $d\chi = d\theta_1\cdots d\theta_r$ on $(\mathbb{R}/\mathbb{Z})^r$). *Character orthogonality* is the identity: for every $\beta, \beta' \in H_1(X, \mathbb{Z})$,
> $$\int_{\widehat{H_1(X, \mathbb{Z})}}\chi(\beta')\,\overline{\chi(\beta)}\,d\chi = \begin{cases}1, & \beta' = \beta,\\ 0, & \beta' \ne \beta.\end{cases}$$
> **In words:** distinct characters are orthogonal when integrated against each other over the whole torus with the natural probability measure; this is the Fourier-inversion identity for the abelian group $H_1(X, \mathbb{Z})$. Multiplying a Fourier expansion by the character-value at a specific class $\beta$ and integrating extracts the coefficient at $\beta$ — exactly like the "read off the $n$-th Fourier coefficient" recipe for periodic functions on the circle, generalised to a lattice.
> **Concretely:** on the circle $S^1 = \mathbb{R}/\mathbb{Z}$ with $H_1 = \mathbb{Z}$, the characters are $\chi_u(n) = e^{2\pi i n u}$; orthogonality reads $\int_0^1 e^{2\pi i(n' - n)u}\,du = \delta_{n', n}$ — the elementary computation. On the torus $T^2$ with $H_1 = \mathbb{Z}^2$: $\int_0^1\!\int_0^1 e^{2\pi i((a' - a)u + (b' - b)v)}\,du\,dv = \delta_{a', a}\delta_{b', b}$, product of two circle identities. Full detail: [[Def - First Homology, Characters, and Finite Fourier Analysis]].

> [!recall]- Corollary 6.4 (Selberg $L$-function log-expansion)
> **Formally:** for a unitary $\chi$ and $\operatorname{Re}s > \delta$,
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)),$$
> the double sum absolutely convergent (by the Selberg zeta convergence estimates for $\operatorname{Re}s > \delta$, since $|\chi([\gamma])^m| = 1$).
> **In words:** the log of the twisted zeta is a character-weighted sum of the killed loop masses over free-homotopy classes. Each $(\gamma, m)$ contributes its mass multiplied by a character phase depending only on the homology of the iterate $\gamma^m$.
> **Concretely:** on the toy $\Gamma = \langle \tau_0 \rangle$ with $\ell = 1$, $s = 2$, and $\chi_u([\tau_0^n]) = e^{2\pi i n u}$: $-\log L_X(2, \chi_u) = \sum_{m \ge 1}\frac{e^{2\pi i m u}}{m}\cdot\frac{e^{-m}}{e^m - 1}$; at $u = 0$ this collapses to $-\log Z_X(2)$; at $u = 1/2$ every second term has a minus sign. Full derivation: [[Cor - Selberg L-Function Identity]].

> [!recall]- Mass in a homology class $\mu^\kappa_X(\beta)$
> **Formally:** $\mu^\kappa_X(\beta) = \sum_{m[\gamma] = \beta}\mu^\kappa_X(C_X(\gamma^m))$, a positive finite number (Def 6.1); infinitely many pairs $(\gamma, m)$ typically project to the same $\beta$, but the sum converges by the Selberg-zeta convergence.
> **In words:** the killed loop mass, grouped not by free-homotopy class but by *net winding* around each cycle. Free-homotopy classes with the same net winding but different orders of traversal share a homology class and their masses add.
> **Concretely:** on the flat torus $T^2$ where $\Gamma = \mathbb{Z}^2$ is abelian, each homology class contains a *single* free-homotopy class, so $\mu^\kappa_X((a, b)) = \mu^\kappa_X(C_X(\gamma_{(a,b)}))$ directly. On a genus-$2$ closed surface with $H_1 = \mathbb{Z}^4$, $\mu^\kappa_X((1, 0, 0, 0))$ sums over the infinitely many free-homotopy classes whose net winding is one loop around the first meridian. See [[Def - Mass in a Homology Class]].

---

# Statement

> **Theorem 6.5 (Fourier expansion and inversion by homology class; Belyaev–Huseynli 6.5).** Let $X$ be a geometrically finite hyperbolic surface with $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^r$, and let $\kappa \ge -\frac14$ with $s = \frac12 + \sqrt{\frac14 + \kappa}$ satisfying $\operatorname{Re}s > \delta$.
>
> **(Fourier expansion.)** For every unitary character $\chi \in \widehat{H_1(X, \mathbb{Z})}$, the logarithm of the Selberg $L$-function admits the absolutely convergent expansion
> $$-\log L_X(s, \chi) = \sum_{\beta \in H_1(X, \mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta).\qquad (\star)$$
>
> **(Inversion.)** For each $\beta \in H_1(X, \mathbb{Z})$,
> $$\mu^\kappa_X(\beta) = \int_{\widehat{H_1(X, \mathbb{Z})}}\!\!\big(-\log L_X(s, \chi)\big)\,\overline{\chi(\beta)}\,d\chi,\qquad (\star\star)$$
> with $d\chi$ the normalised Haar measure on $\widehat{H_1(X, \mathbb{Z})} \cong (S^1)^r$.

---

# In One Line

The Selberg $L$-function's log is the Fourier transform (on the character torus) of the sequence of killed loop masses graded by homology; character orthogonality inverts it, extracting the mass in any single homology class $\beta$ as one integral over the torus.

---

# Why It's True

**Mechanism.** *Corollary 6.4 writes $-\log L_X(s, \chi)$ as a double sum over $(\gamma, m)$ with weight $\chi([\gamma])^m$; use the character-homomorphism identity $\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta)$ to regroup the sum by homology class $\beta$; recognise the inner sum over $\{(\gamma, m) : m[\gamma] = \beta\}$ as $\mu^\kappa_X(\beta)$; the resulting expansion is $(\star)$. Integrating both sides against $\overline{\chi(\beta)}$ over the character torus and swapping sum and integral (allowed by absolute convergence), character orthogonality kills every term except the one with $\beta' = \beta$, giving $(\star\star)$.*

This is Fourier analysis on the abelian group $H_1(X, \mathbb{Z})$: the sequence of "mass in class $\beta$" values is a function $\mu^\kappa_X : H_1 \to \mathbb{R}_{\ge 0}$; its Fourier transform on the character torus is the function $\chi \mapsto -\log L_X(s, \chi)$; and Fourier inversion recovers the original function. The mechanism is the same as expanding a periodic function on the circle as a Fourier series and recovering the coefficients by integrating against $e^{-2\pi i n \theta}$.

---

# Proof

> [!note]- Gap-free proof
> **Step 1 — regroup Corollary 6.4 by homology class.** Start from the log-expansion of the Selberg $L$-function:
> $$-\log L_X(s, \chi) = \sum_{\gamma \in \mathcal P_X}\sum_{m = 1}^\infty \chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m)). \tag{Cor 6.4}$$
> Because $\chi$ is a group homomorphism, $\chi([\gamma])^m = \chi(m[\gamma])$; and every pair $(\gamma, m)$ has some homology class $\beta := m[\gamma] \in H_1(X, \mathbb{Z})$. Regrouping the double sum by this homology class (the collection of pairs $(\gamma, m)$ with $m[\gamma] = \beta$ is a subset of the index set, and their union over $\beta$ partitions the whole index set),
> $$-\log L_X(s, \chi) = \sum_{\beta \in H_1(X, \mathbb{Z})}\Big(\sum_{\substack{\gamma \in \mathcal P_X,\ m \ge 1\\ m[\gamma] = \beta}}\mu^\kappa_X(C_X(\gamma^m))\Big)\chi(\beta) = \sum_{\beta \in H_1(X, \mathbb{Z})}\mu^\kappa_X(\beta)\,\chi(\beta),$$
> the last equality by Definition 6.1. The regrouping is legitimate because the double sum is absolutely convergent for $\operatorname{Re}s > \delta$ (Fubini). This gives $(\star)$.
>
> **Step 2 — Fourier-invert by character orthogonality.** Multiply both sides of $(\star)$ by $\overline{\chi(\beta)}$ and integrate over the character torus $\widehat{H_1(X, \mathbb{Z})}$ against normalised Haar measure $d\chi$:
> $$\int_{\widehat{H_1}}\!\big(-\log L_X(s, \chi)\big)\,\overline{\chi(\beta)}\,d\chi = \int_{\widehat{H_1}}\!\Big(\sum_{\beta' \in H_1(X, \mathbb{Z})}\mu^\kappa_X(\beta')\,\chi(\beta')\Big)\overline{\chi(\beta)}\,d\chi.$$
> The integrand on the right is absolutely dominated by $\sum_{\beta'}\mu^\kappa_X(\beta')\cdot 1 = -\log L_X(s, \chi \equiv 1) = -\log Z_X(s) < \infty$ pointwise in $\chi$ (using $|\chi(\beta')| = |\chi(\beta)| = 1$ and $\mu^\kappa_X(\beta') \ge 0$), which is a finite constant. Since the Haar measure has total mass $1$, dominated convergence lets us swap sum and integral:
> $$= \sum_{\beta' \in H_1(X, \mathbb{Z})}\mu^\kappa_X(\beta')\int_{\widehat{H_1}}\chi(\beta')\overline{\chi(\beta)}\,d\chi.$$
>
> **Step 3 — apply character orthogonality.** By the [[Def - First Homology, Characters, and Finite Fourier Analysis|orthogonality relation]] $\int_{\widehat{H_1}}\chi(\beta')\overline{\chi(\beta)}\,d\chi = \mathbf 1_{\beta' = \beta}$, only the term $\beta' = \beta$ survives:
> $$\int_{\widehat{H_1}}\!\big(-\log L_X(s, \chi)\big)\,\overline{\chi(\beta)}\,d\chi = \mu^\kappa_X(\beta)\cdot 1 = \mu^\kappa_X(\beta),$$
> which is $(\star\star)$. $\blacksquare$

**Absolute convergence remark.** Absolute convergence of the Fourier series $\sum_{\beta}\chi(\beta)\mu^\kappa_X(\beta)$ (uniformly in $\chi$) is exactly the statement that $\sum_\beta \mu^\kappa_X(\beta) < \infty$; and this sum equals the untwisted total $-\log Z_X(s)$ by the trivial-character limit of $(\star)$ — a fact independently established as [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]. So the convergence hypothesis is met precisely when the untwisted zeta identity is finite, i.e. $\operatorname{Re}s > \delta$.

**Sanity check: $\beta = 0$.** The trivial class $\beta = 0 \in H_1(X, \mathbb{Z})$ has $\chi(0) = 1$ for every character. Then $(\star\star)$ reads $\mu^\kappa_X(0) = \int_{\widehat{H_1}}(-\log L_X(s, \chi))\,d\chi$: the *average* of $-\log L_X(s, \chi)$ over the character torus equals the mass in the trivial homology class. That trivial class consists of the *homologically trivial* loops (non-contractible loops that nevertheless have zero net winding — commutators and their products); on a closed genus-$g$ surface with $g \ge 2$ this class is non-empty and its mass is the character-torus average of $-\log L_X$.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]]. The Jacobian reformulation for the closed case is [[Remark - Jacobian Form of the Fourier Inversion|Remark 6.6]]. [[Prop - Total Homology of the Loop Soup|Proposition 6.7]] applies the same Fourier-inversion mechanism to the characteristic function $\mathbb E[\chi(\beta(\lambda))]$ of the loop soup's total homology, giving the distribution of $\beta(\lambda)$ as a character-torus integral of $L_X(s, \chi)^{-\lambda}$.
