---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Hurwitz's Theorem"
  - "Def - Locally Uniform Convergence"
  - "Thm - Locally Uniform Limit of Holomorphic is Holomorphic"
tags: [analysis, complex-analysis]
---

# Problem Statement

Show that $(1 + z/n)^n \to e^z$ locally uniformly on $\mathbb{C}$, and use [[Thm - Hurwitz's Theorem|Hurwitz's theorem]] to conclude that $e^z$ is nowhere zero on $\mathbb{C}$.

**Recall:**

![[Thm - Hurwitz's Theorem#Notation]]

Hurwitz: if $f_n$ holomorphic and nonvanishing on $U$, $f_n \to f$ locally uniformly, then either $f \equiv 0$ or $f$ is nonvanishing.

---

# Convergent Strategy

**Problem class:** Use Hurwitz's theorem to deduce a property of the limit function from properties of an approximating sequence. The classical application: prove $e^z$ has no zeros.

**Assumption pattern:** $(1 + z/n)^n$ for $n \in \mathbb{N}$, with the limit being the entire function $e^z$.

**Theorem routing:** Two parts:
- (i) Show $(1 + z/n)^n \to e^z$ locally uniformly.
- (ii) Identify zeros of $(1 + z/n)^n$ and conclude $(1 + z/n)^n$ is nonvanishing on any compact set for $n$ large enough.
- (iii) Apply Hurwitz: $e^z$ is either identically zero or nonvanishing; clearly not identically zero ($e^0 = 1$), so nonvanishing.

**Key decision point:** The zeros of $(1 + z/n)^n$ are at $z = -n$ (with multiplicity $n$, but at a single point). For any compact set $K$, $-n \notin K$ for $n$ sufficiently large.

---

# Legal Operations Used

1. **Establish locally uniform convergence** of $(1 + z/n)^n \to e^z$ on $\mathbb{C}$. This is a standard result; uses uniform convergence of the Taylor expansion of $\log(1 + w)$ for $|w|$ small.

2. **Identify zeros of $(1 + z/n)^n$.** The polynomial $(1 + z/n)^n$ has zeros only at $z = -n$ (the single root of $1 + z/n = 0$).

3. **For any compact $K \subset \mathbb{C}$, choose $n_0$ such that $-n \notin K$ for all $n \geq n_0$.** Then $(1 + z/n)^n$ is nonvanishing on $K$ for $n \geq n_0$.

4. **Apply Hurwitz on each disc $D(0, R)$.** Conclude $e^z$ is either identically zero or nonvanishing on $D(0, R)$.

5. **Exclude the identically-zero case.** $e^0 = 1 \neq 0$, so $e^z \not\equiv 0$. Hence $e^z$ is nonvanishing.

---

# Hints

> [!note]- Hint 1
> Locally uniform convergence: on $|z| \leq R$, $n\log(1 + z/n) = z - z^2/(2n) + O(1/n^2)$ for $n$ large, uniformly in $z$. Exponentiating: $(1 + z/n)^n = e^{n\log(1 + z/n)} \to e^z$ uniformly on $|z| \leq R$.

> [!note]- Hint 2
> Each $(1 + z/n)^n$ has only one zero, at $z = -n$. For any fixed $R$, $|-n| > R$ when $n > R$, so the zero is outside the disc.

> [!note]- Hint 3
> By Hurwitz, on each disc $D(0, R)$: $e^z$ is either identically zero on $D(0, R)$ or nonvanishing on $D(0, R)$. Since $e^0 = 1 \neq 0$, the second alternative holds. So $e^z$ is nonvanishing on every disc, hence on $\mathbb{C}$.

---

# Solution

**Step 1: Locally uniform convergence $(1 + z/n)^n \to e^z$**

> [!note]- Derivation
> Fix $R > 0$ and consider $|z| \leq R$. For $n > R$, $|z/n| < 1$, so $\log(1 + z/n)$ is defined (principal branch) and:
> $$\log(1 + z/n) = \frac{z}{n} - \frac{z^2}{2n^2} + \frac{z^3}{3n^3} - \ldots$$
> Multiplying by $n$: $n\log(1 + z/n) = z - z^2/(2n) + z^3/(3n^2) - \ldots = z + O(R^2/n)$ uniformly for $|z| \leq R$.
>
> Exponentiating: $(1 + z/n)^n = e^{n\log(1 + z/n)} = e^{z + O(R^2/n)} = e^z \cdot e^{O(R^2/n)} = e^z \cdot (1 + O(R^2/n))$.
>
> So $|(1 + z/n)^n - e^z| = |e^z|\cdot |e^{O(R^2/n)} - 1| \leq e^R \cdot O(R^2/n) \to 0$ uniformly in $z \in \overline{D(0, R)}$ as $n \to \infty$.
>
> So the convergence is uniform on every closed disc $\overline{D(0, R)}$, equivalently locally uniform on $\mathbb{C}$.

**Step 2: Zeros of $(1 + z/n)^n$**

> [!note]- Derivation
> The polynomial $(1 + z/n)^n = 0$ iff $1 + z/n = 0$ iff $z = -n$. So $(1 + z/n)^n$ has a single zero at $z = -n$ (of multiplicity $n$).
>
> For any $R > 0$ and any $n > R$: $|-n| = n > R$, so the zero is outside the disc $\overline{D(0, R)}$. Hence $(1 + z/n)^n$ is nowhere zero on $D(0, R)$ for $n > R$.

**Step 3: Apply Hurwitz**

> [!note]- Derivation
> Fix any $R > 0$. The sequence $f_n(z) = (1 + z/n)^n$ for $n > R$ is holomorphic and nonvanishing on $D(0, R)$, with $f_n \to e^z$ locally uniformly on $D(0, R)$.
>
> By [[Thm - Hurwitz's Theorem|Hurwitz's theorem]] applied to $f_n$ on the connected open set $D(0, R)$: either $e^z \equiv 0$ on $D(0, R)$, or $e^z$ is nonvanishing on $D(0, R)$.
>
> Since $e^0 = 1 \neq 0$, the first alternative fails. So $e^z$ is nonvanishing on $D(0, R)$.
>
> As $R$ was arbitrary, $e^z$ is nonvanishing on all of $\mathbb{C}$.

> [!note]- Complete formal solution
> **Convergence.** For $|z| \leq R$ and $n > R$, $|z/n| < 1$, so the principal branch of $\log(1 + z/n)$ is defined, with Taylor expansion $n\log(1 + z/n) = z + O(R^2/n)$ uniformly. Exponentiating, $(1 + z/n)^n = e^z \cdot (1 + O(R^2/n)) \to e^z$ uniformly on $\overline{D(0, R)}$.
>
> **Zeros.** $(1 + z/n)^n$ has its only zero at $z = -n$, which lies outside $D(0, R)$ for $n > R$.
>
> **Hurwitz.** On $D(0, R)$, the sequence $f_n = (1 + z/n)^n$ (for $n > R$) is holomorphic and nonvanishing, with $f_n \to e^z$ locally uniformly. By [[Thm - Hurwitz's Theorem|Hurwitz]], $e^z$ is either identically zero or nonvanishing on $D(0, R)$. The first is ruled out by $e^0 = 1$.
>
> So $e^z$ is nonvanishing on every disc $D(0, R)$, hence on $\mathbb{C}$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "limit of nonvanishing functions" → "Hurwitz".** This is the standard tool for transferring "no zeros" properties from approximating sequences to limits. Apply whenever a holomorphic function is obtained as a limit and you want to know if it vanishes.

**The classical proof of $e^z$ nonvanishing is via Hurwitz applied to its polynomial approximations.** Alternative: $e^z \cdot e^{-z} = 1$, so $e^z$ never vanishes (because the product is $1 \neq 0$). Both are valid; the Hurwitz route generalizes to other functions defined by limits or series.

**The crucial step is checking the zeros of $f_n$ leave the compact set.** Hurwitz applies "on each connected open set", and the nonvanishing of $f_n$ must hold *on that set*. For $(1 + z/n)^n$, the zeros are far from the origin for large $n$, so any compact set is eventually disjoint from the zeros — exactly what Hurwitz needs.

**Generalization — Weierstrass products and infinite products of nonvanishing functions.** The Weierstrass factorization theorem expresses entire functions with prescribed zeros as infinite products. Hurwitz controls the zeros in the limit. The general principle: zeros of holomorphic functions are robust under locally uniform convergence (either preserved at $f_n$'s zeros, or the limit is identically zero).
