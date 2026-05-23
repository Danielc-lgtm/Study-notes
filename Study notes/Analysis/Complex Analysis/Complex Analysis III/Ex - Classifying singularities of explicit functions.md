---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Removable Singularity, Pole, Essential Singularity"
  - "Thm - Riemann's Removable Singularity Theorem"
  - "Thm - Pole Characterization"
  - "Def - Residue"
tags: [analysis, complex-analysis]
---

# Problem Statement

Classify the singularity at $z = 0$ for each of the following functions, and compute its residue (when meaningful):

(a) $f_1(z) = 1/\sin z$
(b) $f_2(z) = \sin(1/z)$
(c) $f_3(z) = (\sin z)/z$

**Recall:**

![[Def - Removable Singularity, Pole, Essential Singularity#The Definition]]

Boundedness ⟹ removable ([[Thm - Riemann's Removable Singularity Theorem|Riemann]]); $|f| \to \infty$ ⟺ pole ([[Thm - Pole Characterization]]); neither ⟹ essential.

---

# Convergent Strategy

**Problem class:** Classify each isolated singularity by inspecting behaviour or Laurent expansion. The strategy: identify which of "bounded", "$|f| \to \infty$", "neither" holds, and conclude.

**Assumption pattern:** Three concrete functions, each with a (potential) singularity at $0$. The trichotomy is exhaustive, so each is exactly one of removable, pole, essential.

**Theorem routing:** Use Taylor/Laurent expansion to identify negative-power coefficients. Use the qualitative characterizations (bounded/unbounded/oscillatory) as sanity checks.

**Key decision point:** For each function, decide which characterization is easiest. Sometimes the Laurent expansion is obvious; sometimes the limiting behaviour of $|f|$ is.

---

# Legal Operations Used

1. **Taylor-expand** $\sin z = z - z^3/3! + z^5/5! - \ldots$ near $0$.
2. **Read off the Laurent expansion** of each function from this Taylor expansion.
3. **Identify negative-power coefficients**:
   - None ⟹ removable.
   - Finitely many ⟹ pole.
   - Infinitely many ⟹ essential.
4. **Compute residue** as the coefficient of $1/z$.

---

# Hints

> [!note]- Hint 1
> For (a) $1/\sin z$: $\sin z = z(1 - z^2/6 + \ldots)$, so $1/\sin z = (1/z)(1 + z^2/6 + \ldots)^{-1}$ — a simple pole at $0$.

> [!note]- Hint 2
> For (b) $\sin(1/z)$: substitute $w = 1/z$ into $\sin w = w - w^3/6 + \ldots$ to get $\sin(1/z) = 1/z - 1/(6z^3) + \ldots$ — infinitely many negative-power terms.

> [!note]- Hint 3
> For (c) $(\sin z)/z$: $\sin z/z = (z - z^3/6 + \ldots)/z = 1 - z^2/6 + \ldots$ — no negative-power terms.

---

# Solution

**(a) $f_1(z) = 1/\sin z$ — simple pole at $0$, residue $1$**

> [!note]- Derivation
> $\sin z = z - z^3/3! + z^5/5! - \ldots = z(1 - z^2/6 + z^4/120 - \ldots)$. So $\sin z$ has a simple zero at $0$ (the leading term is $z$, with derivative $\cos 0 = 1$ at $0$).
>
> Therefore $1/\sin z$ has a simple pole at $0$ (a simple zero in the denominator gives a simple pole). The residue is computed via the quotient formula: $\operatorname{Res}_0(1/\sin z) = 1/(\cos 0) = 1$.
>
> Alternative Laurent computation: $1/\sin z = (1/z)\cdot 1/(1 - z^2/6 + \ldots) = (1/z)(1 + z^2/6 + \ldots) = 1/z + z/6 + 7z^3/360 + \ldots$. The coefficient of $1/z$ is $1$ — the residue. ✓

**(b) $f_2(z) = \sin(1/z)$ — essential singularity at $0$**

> [!note]- Derivation
> Substituting $w = 1/z$ in the Taylor expansion $\sin w = w - w^3/3! + w^5/5! - w^7/7! + \ldots$:
> $$\sin(1/z) = \frac{1}{z} - \frac{1}{3! z^3} + \frac{1}{5! z^5} - \frac{1}{7! z^7} + \ldots.$$
> Infinitely many negative-power terms (every odd negative power has a nonzero coefficient), so by definition this is an *essential singularity*.
>
> The residue is the coefficient of $1/z$, which is $1$.
>
> Verification of "essential" via behaviour: $\sin(1/z)$ takes every value in $\mathbb{C}$ infinitely often in every punctured neighborhood of $0$, by Casorati–Weierstrass. Concretely: $\sin(1/z) = 0$ at $z = 1/(n\pi)$ for all $n \neq 0$ (which accumulate at $z = 0$), and $\sin(1/z) = 1$ at $z = 1/(\pi/2 + 2\pi n)$, etc. So $|f|$ neither tends to a finite limit nor to infinity.

**(c) $f_3(z) = (\sin z)/z$ — removable singularity at $0$**

> [!note]- Derivation
> Taylor-expand $\sin z = z - z^3/6 + z^5/120 - \ldots$, so
> $$\frac{\sin z}{z} = 1 - \frac{z^2}{6} + \frac{z^4}{120} - \ldots,$$
> a power series with no negative-power terms. So the singularity at $0$ is removable; $f_3$ extends to a holomorphic function on $\mathbb{C}$ with $f_3(0) = 1$.
>
> Residue is the coefficient of $1/z$, which is $0$ (no $1/z$ term).
>
> Verification of "removable" via boundedness: $|\sin z/z| \leq 1$ for $z$ real near $0$ (and is bounded for complex $z$ near $0$ as well, by the Taylor expansion). By [[Thm - Riemann's Removable Singularity Theorem|Riemann]], the singularity is removable.

> [!note]- Complete formal solution
> **(a)** $\sin z = z(1 - z^2/6 + \ldots)$ has a simple zero at $0$, so $1/\sin z$ has a *simple pole* at $0$. The residue, by the quotient formula with $g = 1, h = \sin z$, $h'(0) = \cos 0 = 1$: $\operatorname{Res}_0(1/\sin z) = 1$.
>
> **(b)** Laurent expansion $\sin(1/z) = 1/z - 1/(6z^3) + 1/(120 z^5) - \ldots$ has *infinitely many* negative-power terms, so $0$ is an *essential singularity*. Residue: $\operatorname{Res}_0\sin(1/z) =$ coefficient of $1/z$ = $1$.
>
> **(c)** Laurent expansion $(\sin z)/z = 1 - z^2/6 + z^4/120 - \ldots$ has *no* negative-power terms, so $0$ is *removable*. The function extends to $f_3(0) = 1$. Residue $= 0$. $\blacksquare$

---

# Key Takeaways

**The trichotomy is exhaustive: every isolated singularity is exactly one of removable, pole, essential.** To classify, count the nonzero negative-power coefficients in the Laurent expansion: $0 \to$ removable, finitely many $\to$ pole, infinitely many $\to$ essential.

**Trigger-reaction pattern — "$1/f$ where $f$ has a simple zero" → simple pole, residue $1/f'$.** This is the workhorse pattern. $1/\sin z$ at $0$, $1/\tan z$ at $0$, $1/(z - 1)$ at $1$, $1/p(z)$ where $p$ is a polynomial with simple roots — all fit this pattern.

**Substitution into known Taylor expansions is the cleanest way to get Laurent expansions of composite functions.** For $\sin(1/z)$, the substitution $w = 1/z$ into $\sin w = w - w^3/6 + \ldots$ instantly gives the Laurent expansion. Same trick for $e^{1/z}, \cos(1/z)$, etc. The key is that composing a Taylor series with $1/z$ produces a Laurent series with infinitely many negative powers — *all* such substitutions produce essential singularities, except in degenerate cases.

**The qualitative test: bounded ⟹ removable, $|f| \to \infty$ ⟹ pole, neither ⟹ essential.** This is the operational checklist. Even without computing the full Laurent expansion, knowing the limiting behaviour of $|f|$ classifies the singularity.

**An essential singularity's residue is well-defined.** The residue is just the $c_{-1}$ coefficient, defined regardless of whether the singularity is a pole or essential. For $\sin(1/z)$ the residue is $1$; for $e^{1/z}$ the residue is also $1$. The residue theorem applies whether the enclosed singularities are poles or essential.
