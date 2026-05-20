---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Rouché's Theorem"
  - "Thm - Argument Principle"
tags: [analysis, complex-analysis]
---

# Problem Statement

Show that $p(z) = z^5 + 3z + 1$ has exactly one zero in $|z| < 1$.

**Recall:**

![[Thm - Rouché's Theorem#Notation]]

Rouché: if $|f - g| < |f|$ on $\gamma$, then $f, g$ have the same zero count in the region bounded by $\gamma$.

---

# Convergent Strategy

**Problem class:** Counting zeros of a polynomial in a specific region, via dominant-term comparison.

**Assumption pattern:** $p(z) = z^5 + 3z + 1$. The term $3z$ is the dominant term *on $|z| = 1$*: $|3z| = 3$, while $|z^5 + 1| \leq 2$ on $|z| = 1$. So $|p - 3z| = |z^5 + 1| < |3z|$, and we can compare $p$ with $3z$.

**Theorem routing:** Apply Rouché with $f = 3z$ (whose zero count in $|z| < 1$ is known: $1$, the single zero at $0$) and $g = p$.

**Key decision point:** Choose the dominant term *on the boundary*. On $|z| = 1$, the dominant term of $p$ is $3z$, not $z^5$ (since $|z^5| = 1 < 3$ on the unit circle). On $|z| = R$ for $R$ large, $z^5$ would be dominant.

---

# Legal Operations Used

1. **Identify the dominant term on the boundary $|z| = 1$**: $3z$, with $|3z| = 3$ on the boundary.
2. **Bound the remainder $|p(z) - 3z| = |z^5 + 1|$** on $|z| = 1$ by the triangle inequality: $\leq 1 + 1 = 2$.
3. **Compare with the dominant term**: $|p - 3z| \leq 2 < 3 = |3z|$.
4. **Apply Rouché**: $p$ and $3z$ have the same zero count in $|z| < 1$, namely $1$.

---

# Hints

> [!note]- Hint 1
> Compare $p$ with one of its terms on $|z| = 1$. Try $f = 3z$ (the "middle" term) — it has size $3$ on $|z| = 1$, while the other terms have size $\leq 2$.

> [!note]- Hint 2
> Bound $|p(z) - 3z| = |z^5 + 1|$ on $|z| = 1$: by triangle inequality, $|z^5 + 1| \leq |z^5| + |1| = 1 + 1 = 2$. And $|3z| = 3$. So $|p - 3z| \leq 2 < 3 = |3z|$.

> [!note]- Hint 3
> By Rouché, $p$ and $3z$ have the same zero count in $|z| < 1$. The function $3z$ has exactly one zero (at $z = 0$, simple). Hence $p$ has exactly one zero in $|z| < 1$.

---

# Solution

The proof breaks into three short steps. Step 1 sets up the Rouché comparison by choosing the dominant term $f(z) = 3z$ on the unit circle; Step 2 verifies the strict inequality $|p - 3z| = |z^5 + 1| \leq 2 < 3 = |3z|$ on $|z| = 1$; Step 3 applies Rouché to conclude $p$ has the same zero count as $3z$ in $|z| < 1$, namely $1$. The non-obvious move is in Step 1 — choosing $3z$ (the *linear*, not highest-degree, term) as the dominant comparison is what works on $|z| = 1$, because on a small circle low-degree terms tend to dominate, the opposite of the $R \to \infty$ regime.

**Step 1: Set up the comparison**

We compare $p(z) = z^5 + 3z + 1$ with $f(z) = 3z$ on the circle $|z| = 1$. The difference is $p(z) - 3z = z^5 + 1$.

**Step 2: Verify Rouché's hypothesis**

> [!note]- Derivation
> On $|z| = 1$:
> $$|p(z) - 3z| = |z^5 + 1| \leq |z^5| + |1| = 1 + 1 = 2,$$
> and
> $$|3z| = 3.$$
> So $|p(z) - 3z| \leq 2 < 3 = |3z|$ on $|z| = 1$. (The inequality is *strict* — we need this for Rouché.)

**Step 3: Apply Rouché**

> [!note]- Derivation
> By [[Thm - Rouché's Theorem|Rouché's theorem]], $p$ and $3z$ have the same number of zeros in $|z| < 1$, counted with multiplicity.
>
> $f(z) = 3z$ has exactly one zero in $|z| < 1$: at $z = 0$, simple. So $p$ has exactly one zero in $|z| < 1$.

> [!note]- Complete formal solution
> Let $f(z) = 3z$ and $g(z) = p(z) = z^5 + 3z + 1$, both holomorphic on $\overline{\mathbb{D}}$.
>
> On $|z| = 1$:
> $$|f(z) - g(z)| = |{-z^5 - 1}| = |z^5 + 1| \leq |z|^5 + 1 = 2 < 3 = |3z| = |f(z)|.$$
>
> By [[Thm - Rouché's Theorem|Rouché's theorem]], $f$ and $g$ have the same number of zeros in $|z| < 1$. Since $f = 3z$ has exactly one zero (at $z = 0$), $p$ has exactly one zero in $|z| < 1$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "count zeros of polynomial in a region" → "compare with a dominant term on the boundary".** Rouché's theorem is the standard tool. The art is choosing the right comparison: pick the term of the polynomial that is *largest on the boundary*, and compare against it.

**The "dominant term" depends on the region.** On $|z| = 1$, the constant or linear terms can dominate (smaller-degree terms are larger on small circles). On $|z| = R$ for $R$ large, the highest-degree term dominates. For a polynomial $p$ of degree $n$, on a large circle of radius $R$ much larger than the coefficients, $p$ behaves like $z^n$, and Rouché gives the fundamental theorem of algebra.

**Strict inequality is crucial.** Rouché requires $|f - g| < |f|$ *strictly*. Equality at a single point invalidates the homotopy argument. Always check the inequality is strict on the entire boundary.

**Combine with Rouché on different regions.** To locate all zeros of a polynomial, apply Rouché on several circles: one for counting in $|z| < 1$, another for $|z| < 2$, etc. Subtract to count zeros in annular regions.
