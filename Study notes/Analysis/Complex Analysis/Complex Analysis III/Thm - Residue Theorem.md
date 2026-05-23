---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Residue"
  - "Def - Winding Number"
  - "Def - Simply Connected Domain in Complex Analysis"
  - "Thm - Cauchy's Theorem for Simply Connected Domains"
  - "Thm - Laurent Series Theorem"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open, $f$ meromorphic on $U$ with poles $w_1, w_2, \ldots$ (a discrete set), $\gamma$ a closed piecewise $C^1$ curve in $U$ avoiding the poles. $I(\gamma; w)$ is the winding number, $\operatorname{Res}_w f$ is the residue. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Residue Theorem).** Let $U \subseteq \mathbb{C}$ be open and simply connected, and let $f$ be meromorphic on $U$ with poles $w_1, w_2, \ldots$ (a discrete set in $U$). Let $\gamma$ be a closed piecewise $C^1$ curve in $U$ avoiding the poles, and assume only finitely many poles $w_i$ satisfy $I(\gamma; w_i) \neq 0$. Then
> $$\int_\gamma f(z)\,dz = 2\pi i \sum_{i} I(\gamma; w_i)\,\operatorname{Res}_{w_i} f,$$
> the sum being over all poles $w_i$ with nonzero winding number (equivalently, over all isolated singularities of $f$ in $U$, the others contributing zero).

---

# Motivation

The residue theorem is the master theorem of contour integration. Cauchy's theorem says closed integrals of *holomorphic* functions vanish; the residue theorem extends this to *meromorphic* functions, giving an explicit formula for the closed integral in terms of the function's local data (residues at poles) and the contour's topology (winding numbers around poles).

This is the bridge between local complex analysis (residues, Laurent expansion at a point) and global complex analysis (contour integrals, topology). It is the workhorse of Chapter 3 and the rest of complex analysis: every contour integral computation in §3.4, every counting argument via the argument principle in §3.5, every transform inversion via Bromwich integration — all reduce to applying the residue theorem.

The intuitive picture: a meromorphic function's contour integral picks up a contribution from each pole the contour winds around. The pole's contribution is $2\pi i \cdot (\text{winding number}) \cdot (\text{residue})$. So global integration = sum of local residues weighted by topology. This is the *unifying frame* of the residue theorem: every contour integral is a sum over the function's singularities, with the topological weights being integer-valued and the residues being complex numbers.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ meromorphic, $\gamma$ closed curve avoiding poles, $\gamma$ null-homotopic (or $U$ simply connected)". Sources broaden the recognition:

**$f$ a rational function and $\gamma$ any standard closed contour.** Property $B$: $f = P/Q$ with $P, Q$ polynomials and $Q$ has only isolated zeros. Bridge: rational functions are meromorphic on $\mathbb{C}$ (poles only at zeros of $Q$). Closed curves in $\mathbb{C}$ that avoid these poles are valid. Triggers most computational applications.

**$f = g e^{ih}$ or other oscillatory product, $\gamma =$ real axis closed by a semicircle.** Property $B$: $f$ is a rational function times an exponential factor. Bridge: still meromorphic with isolated poles; the semicircle closure transforms a real-axis integral into a contour integral, applying the residue theorem to evaluate. The exponential factor controls the semicircle's contribution (Jordan's lemma).

**$f$ has an essential singularity inside the contour.** Property $B$: $f$ is "meromorphic" except for some essential singularities, but the contour avoids them. Bridge: the residue theorem applies to all isolated singularities, including essential ones — the residue is just $c_{-1}$ of the Laurent expansion, defined whether the singularity is a pole or essential. The "meromorphic" hypothesis can be relaxed to "holomorphic except for isolated singularities".

**$\gamma$ is a sum of closed curves (cycle).** Property $B$: $\gamma = \gamma_1 + \gamma_2 + \ldots + \gamma_n$, a formal sum of closed curves. Bridge: by linearity of integration and winding number, the residue theorem extends to cycles. Useful when a "contour" is best described as a difference of two contours.

**Targets (Output Amplification)**

The conclusion is "$\int_\gamma f\,dz = 2\pi i \sum_w I(\gamma; w) \operatorname{Res}_w f$".

Combine with **specific choices of $\gamma$ and $f$.** Property $D$: $\gamma$ a circle $|z - a| = r$, $f$ a rational function with poles inside the disc. Amplified result $E$: $\int_{|z-a|=r} f\,dz = 2\pi i \sum_{|w - a| < r} \operatorname{Res}_w f$ — a clean direct formula for circle integrals.

Combine with **the argument principle setup.** Property $D$: $f$ is itself $g'/g$ for a meromorphic $g$. The residues of $g'/g$ are integers (orders of zeros and poles of $g$). Amplified result $E$: the argument principle $\frac{1}{2\pi i}\oint g'/g\,dz = N - P$.

Combine with **the Laurent expansion structure.** Property $D$: the function $f$ has a complicated Laurent expansion. Amplified result $E$: the residue theorem says only the $c_{-1}$ coefficients matter for the integral. All other Laurent coefficients are "invisible" to contour integration. This radical compression is the source of residue calculus's power.

Combine with **summation of series.** Property $D$: choosing $f(z) = \pi \cot(\pi z) g(z)$ for specific $g$, where $\pi\cot(\pi z)$ has poles at integers with residue $1$. Amplified result $E$: the integral $\oint \pi \cot(\pi z) g(z)\,dz$ around a large contour picks up $\sum_n g(n)$, evaluating infinite sums as residue computations.

---

# Why Is It True

The proof has a clean and memorable structure. Subtract from $f$ its principal part at each pole inside the contour: define $h(z) = f(z) - \sum_i P_i(z)$, where $P_i$ is the principal part of $f$ at $w_i$ (a finite sum of negative-power terms, $\sum_{n \geq 1} c_{-n}^{(i)}/(z - w_i)^n$). Then $h$ has *removable* singularities at each $w_i$ (since subtracting the principal part removes all the negative-power terms), and is holomorphic on $U$. By Cauchy's theorem on simply connected $U$ (or null-homotopy of $\gamma$ in $U$), $\int_\gamma h\,dz = 0$.

So $\int_\gamma f\,dz = \sum_i \int_\gamma P_i(z)\,dz$. Each $P_i$ is a finite sum of terms $c_{-n}^{(i)}/(z - w_i)^n$. The integrals: $\int_\gamma 1/(z - w_i)^n\,dz = 2\pi i \cdot I(\gamma; w_i)$ if $n = 1$, and $0$ if $n \geq 2$ (the latter has a primitive $-(n-1)^{-1}(z - w_i)^{-(n-1)}$, single-valued on $\mathbb{C}\setminus\{w_i\}$, so the closed integral vanishes).

Therefore $\int_\gamma P_i\,dz = c_{-1}^{(i)} \cdot 2\pi i \cdot I(\gamma; w_i) = 2\pi i \cdot I(\gamma; w_i) \cdot \operatorname{Res}_{w_i} f$. Summing over $i$, $\int_\gamma f\,dz = 2\pi i \sum_i I(\gamma; w_i) \operatorname{Res}_{w_i} f$.

The conceptual point: the *principal parts* (negative-power Laurent terms) carry all the residue information; the holomorphic remainder $h$ integrates to zero by Cauchy. Among the principal-part terms, only the $1/(z - w_i)$ term survives integration; all higher negative-power terms have single-valued antiderivatives. So *only the residue ($c_{-1}$) survives*, and the topological weight is the winding number around the pole.

This is the *true name* of the residue theorem: it is **Cauchy's theorem plus the integral computation $\oint 1/(z - w)\,dz = 2\pi i \cdot I(\gamma; w)$**. The "$1/(z - w)$" is the unique Laurent term that has no single-valued primitive; everything else is exact.

---

# What Makes This Hard

The non-obvious step is **subtracting principal parts to reduce to Cauchy's theorem**. The trick is to recognize that $f - \sum P_i$ is holomorphic on $U$ (the principal parts cancel out all negative powers in Laurent expansions), so its closed integral vanishes by Cauchy. Then computing $\int_\gamma P_i\,dz$ reduces to the single integral $\oint 1/(z - w_i)\,dz$ via the disappearance of higher negative-power terms. A common mistake is to apply Cauchy's theorem directly to $f$ — but $f$ has poles, so the theorem doesn't apply; the principal-part subtraction is what makes Cauchy applicable. A second slip is to forget that for higher-order poles, only $c_{-1}$ contributes to the residue — students sometimes try to include all Laurent coefficients.

---

# Rederivation Scaffold

**High-level strategy:**
Subtract from $f$ its principal parts at all poles inside the contour. The result is holomorphic, so its closed integral vanishes by Cauchy. The remaining integrals are over principal parts, each reducing to $2\pi i \cdot I(\gamma; w_i) \cdot c_{-1}^{(i)} = 2\pi i \cdot I(\gamma; w_i) \cdot \operatorname{Res}_{w_i} f$.

**Subgoal decomposition:**

1. **Identify the poles inside.** Let $w_1, \ldots, w_n$ be the poles of $f$ with $I(\gamma; w_i) \neq 0$.

2. **Compute the principal part at each pole.** $P_i(z) = \sum_{k \geq 1} c_{-k}^{(i)}/(z - w_i)^k$, a finite sum (pole of finite order) or convergent series (essential).

3. **Show $f - \sum_i P_i$ is holomorphic on $U$.** At each $w_i$, the principal part of $f - \sum_j P_j$ is zero (the $w_i$-part of $f$ cancels with $-P_i$), so $w_i$ is removable.

4. **Apply Cauchy's theorem to $f - \sum P_i$.** $\int_\gamma (f - \sum P_i)\,dz = 0$, so $\int_\gamma f\,dz = \sum_i \int_\gamma P_i\,dz$.

5. **Compute $\int_\gamma P_i\,dz$.** Only the $1/(z - w_i)$ term contributes: $\int_\gamma 1/(z - w_i)\,dz = 2\pi i \cdot I(\gamma; w_i)$; higher negative-power terms integrate to zero. So $\int_\gamma P_i\,dz = 2\pi i \cdot I(\gamma; w_i) \cdot c_{-1}^{(i)}$.

6. **Sum:** $\int_\gamma f\,dz = 2\pi i \sum_i I(\gamma; w_i) \operatorname{Res}_{w_i} f$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Principal parts and removable singularities
> **Statement:** If $f$ has Laurent expansion $\sum c_n (z - a)^n$ at $a$, with principal part $P(z) = \sum_{n \geq 1} c_{-n}(z - a)^{-n}$, then $f - P$ has a removable singularity at $a$.
>
> > [!note]- Full proof
> > The Laurent expansion of $f - P$ at $a$ is $\sum_{n \geq 0} c_n (z - a)^n$ — only nonnegative-power terms. So $f - P$ extends holomorphically to $a$ with value $c_0$.

> [!note]- Lemma 2: $\oint (z - w)^{-n}\,dz = 0$ for $n \geq 2$, and $2\pi i \cdot I(\gamma; w)$ for $n = 1$
> **Statement:** For $\gamma$ a closed piecewise $C^1$ curve in $\mathbb{C} \setminus \{w\}$, $\oint_\gamma (z - w)^{-n}\,dz = 0$ for $n \geq 2$, and $\oint_\gamma (z - w)^{-1}\,dz = 2\pi i \cdot I(\gamma; w)$.
>
> > [!note]- Full proof
> > For $n \geq 2$: the function $(z - w)^{-n}$ has primitive $-(n-1)^{-1}(z - w)^{-(n-1)}$, holomorphic on $\mathbb{C} \setminus \{w\}$, so the closed integral is zero.
> > For $n = 1$: this is the integral formula for the winding number — see [[Thm - Existence and Properties of the Winding Number]].

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f$ be meromorphic on $U$ with poles $w_1, \ldots, w_n$ (assumed finite; in general use a compactness argument to reduce to finitely many poles with $I(\gamma; w_i) \neq 0$). Let $\gamma$ be a closed piecewise $C^1$ curve in $U$ avoiding the poles, with $\gamma$ null-homotopic in $U$ (or $U$ simply connected, so this is automatic).
>
> Let $P_i(z) = \sum_{k = 1}^{N_i} c_{-k}^{(i)}/(z - w_i)^k$ be the principal part of $f$ at $w_i$ (where $N_i$ is the order of the pole — or the truncation if $w_i$ is an essential singularity, but the argument below extends).
>
> Define $h(z) := f(z) - \sum_{i=1}^n P_i(z)$. At each $w_j$, the Laurent expansion of $h$ has no negative-power terms (the $P_j$ subtracts out the principal part of $f$, while the other $P_i$ for $i \neq j$ are holomorphic at $w_j$, contributing Taylor terms). So by Lemma 1 (or directly), $h$ has a removable singularity at each $w_j$.
>
> Therefore $h$ extends to a holomorphic function on $U$ (more precisely on $U' = U \setminus \{\text{essential singularities of } f\}$, but assume only poles for clarity). By [[Thm - Cauchy's Theorem for Simply Connected Domains|Cauchy's theorem]] (or because $\gamma$ is null-homotopic in $U$), $\int_\gamma h\,dz = 0$.
>
> So $\int_\gamma f\,dz = \sum_{i=1}^n \int_\gamma P_i\,dz$. By Lemma 2,
> $$\int_\gamma P_i\,dz = \sum_{k = 1}^{N_i} c_{-k}^{(i)} \int_\gamma (z - w_i)^{-k}\,dz = c_{-1}^{(i)} \cdot 2\pi i \cdot I(\gamma; w_i),$$
> since terms with $k \geq 2$ contribute zero. Recognizing $c_{-1}^{(i)} = \operatorname{Res}_{w_i} f$,
> $$\int_\gamma f\,dz = 2\pi i \sum_{i=1}^n I(\gamma; w_i) \operatorname{Res}_{w_i} f. \quad\blacksquare$$
>
> **Generalization to essential singularities.** When $f$ has essential singularities, the principal part is an infinite series. The argument extends provided the principal-part series converges uniformly on $\gamma$ (which holds for the Laurent expansion of an essential singularity, since the Laurent series converges on the punctured disc). Integrating termwise picks out only $c_{-1}$ from each principal part, and the formula remains the same: $\int_\gamma f\,dz = 2\pi i \sum I(\gamma; w_i) \operatorname{Res}_{w_i} f$.

---

# Cross-Field Exercise Suggestions

**Real integral evaluation.** Show $\int_{-\infty}^\infty dx/(1 + x^2) = \pi$ by closing the real axis with an upper semicircle. The function $1/(1 + z^2)$ has poles at $\pm i$; only $z = i$ is enclosed; $\operatorname{Res}_i 1/(1 + z^2) = 1/(2i)$. Semicircle contribution vanishes as radius $\to \infty$. Result: $2\pi i \cdot 1/(2i) = \pi$.

**Argument principle.** For $g$ meromorphic, $g'/g$ is meromorphic with simple poles at zeros and poles of $g$, with residues equal to the orders. The integral $\frac{1}{2\pi i}\oint g'/g\,dz =$ "sum of residues" = (zeros of $g$) − (poles of $g$) counted with multiplicity. This is the argument principle, derivable from the residue theorem.

**Summing series via $\pi \cot(\pi z)$.** The function $\pi\cot(\pi z)$ has simple poles at integers with residue $1$. For a function $g$ holomorphic on $\mathbb{C}$ and decaying at $\infty$, $\oint_{\Gamma_N} \pi\cot(\pi z) g(z)\,dz = 0$ (large square contour, integral vanishes by decay), so by the residue theorem the sum of residues vanishes, giving $\sum_n g(n) = -\sum_{\text{poles of } g} \operatorname{Res}_{w}[\pi\cot(\pi z) g(z)]$. Evaluates $\sum 1/n^2 = \pi^2/6$ and similar.

**Inverse Laplace transforms.** $f(t) = (2\pi i)^{-1}\int_{c-i\infty}^{c+i\infty} F(s) e^{st}\,ds$. For $t > 0$, close the contour to the left half-plane (so $e^{st}$ decays); residues at poles of $F$ in the left half-plane give $f(t) = \sum \operatorname{Res}_{s_k}[F(s) e^{st}]$.

---

# Bridges

- **[[Def - Residue]]** — the local data being summed.

- **[[Def - Winding Number]]** — the topological weight.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — the engine: the holomorphic remainder $h$ has closed integral zero.

- **[[Thm - Argument Principle]]** — a direct corollary, with $f = g'/g$.

- **[[Thm - Rouché's Theorem]]** — applied via the argument principle.

---

# Unlocked by This

> [!tip] All of Real Integral Evaluation via Contours *(from §3.4)*
> Every result in §3.4 is the residue theorem plus a clever contour choice: rational integrals via semicircles, oscillatory integrals via Jordan's lemma, trigonometric integrals via unit-circle parameterization, keyhole contour integrals, etc.

> [!tip] The Argument Principle and Rouché *(from §3.5)*
> The residue theorem applied to $g'/g$ gives the [[Thm - Argument Principle|argument principle]], from which [[Thm - Rouché's Theorem|Rouché's theorem]], the [[Thm - Open Mapping Theorem|open mapping theorem]], and the [[Thm - Local Mapping Degree|local mapping degree]] all follow.
