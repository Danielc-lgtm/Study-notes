---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Electromagnetic Field Invariants"
  - "Thm - Reduction to Parallel Electric and Magnetic Fields"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

For each of the following electromagnetic fields (given relative to some inertial observer $\mathcal{O}$, in SI units with $c$ explicit), compute the invariants $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$, classify the field, and state whether there is a frame in which it is purely electric, purely magnetic, or static — and if so, give the velocity of the boost.

1. A plane electromagnetic wave: $\mathbf{E} = E_0\cos\phi\,e_2$, $\mathbf{B} = \frac{E_0}{c}\cos\phi\,e_3$, with $\phi = k(x - ct)$ (so $\mathbf{E}\perp\mathbf{B}$, both $\perp$ the propagation direction $e_1$, and $E = cB$).
2. Crossed fields with $\mathbf{E} = E\,e_2$, $\mathbf{B} = B\,e_3$, $cB > E$ (a velocity-selector configuration).
3. The field of a [[Def - Field of a Charge in Uniform Translation|uniformly moving charge]], for which $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$ with $|\mathbf{U}| < c$.
4. A field with $\mathbf{E} = E\,e_1$, $\mathbf{B} = B\,e_1$ (parallel fields, both nonzero).

Show that the sign of $I_1$ and the vanishing of $I_2$ are frame-independent, and use them to decide the reducibility in each case.

**Recall:**

![[Thm - The Electromagnetic Field Invariants#Statement]]

The [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] says a non-null field ($(I_1,I_2)\ne(0,0)$) can be boosted to make $\mathbf{E}\parallel\mathbf{B}$; if also $I_2 = 0$ and $I_1\ne0$, it reduces to purely magnetic (at $U = E/B$ if $I_1 > 0$) or purely electric (at $U = c^2B/E$ if $I_1 < 0$). A **null** field ($I_1 = I_2 = 0$) cannot be reduced.

---

# Convergent Strategy

**Problem class.** A *classify-an-invariant* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.2]]: compute the two Lorentz scalars and read off the field's frame-independent class. The routine is purely arithmetic once the fields are given — evaluate $I_1$ and $I_2$, then apply the classification and reduction rules.

**Assumption pattern.** Each field is given in one frame; the assumption that $I_1$ and $I_2$ are *invariant* is what lets a single-frame computation settle the field's character in *all* frames. The signposts are the relations among the fields: $E = cB$ with $\mathbf{E}\perp\mathbf{B}$ flags a null field; $\mathbf{E}\perp\mathbf{B}$ with unequal magnitudes flags a reducible crossed field; $\mathbf{E}\parallel\mathbf{B}$ flags $I_2\ne0$, irreducible to a single field.

**Theorem routing.** Each part routes through the [[Thm - The Electromagnetic Field Invariants|invariants theorem]] (to compute and classify) and then the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] (to decide reducibility and find the boost). The plane wave (part 1) is the key case where reduction *fails*.

**Key decision point.** The non-obvious recognition is that $I_1 = I_2 = 0$ is a genuinely distinct class — the null field — that *cannot* be simplified by any boost, unlike every other field. The temptation is to assume every field can be made purely electric or magnetic; the plane wave is the counterexample, and seeing why ($E = cB$ in every frame) is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 4 (compute the invariants in a convenient frame)** from the topic page: evaluate $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ for each field. This is the core computation in all four parts.

2. **Operation 5 (reduce to a pure or parallel field)** from the topic page: use the values of $I_1$, $I_2$ to decide the canonical form and, when $I_2 = 0$, the reducing velocity $U = E/B$ or $U = c^2B/E$. This is the classification step.

---

# Hints

> [!note]- Hint 1
> For each field just plug into $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$. The sign of $I_1$ tells you mostly-electric ($<0$) or mostly-magnetic ($>0$); $I_2 = 0$ tells you $\mathbf{E}\perp\mathbf{B}$.

> [!note]- Hint 2
> For the plane wave, note $E = cB$ so $c^2B^2 = E^2$ and $I_1 = 0$; and $\mathbf{E}\perp\mathbf{B}$ so $I_2 = 0$. Both vanish — this is a *null* field, and the reduction theorem says it *cannot* be made purely electric, purely magnetic, or static.

> [!note]- Hint 3
> For the moving-charge field, use $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$: then $\mathbf{E}\cdot\mathbf{B} = 0$ (so $I_2 = 0$), and $|\mathbf{B}| = \frac{U}{c^2}|\mathbf{E}|\sin\angle \le \frac{U}{c^2}|\mathbf{E}| < \frac{1}{c}|\mathbf{E}|$, so $cB < E$ and $I_1 < 0$ (mostly electric). It can be made purely electric — at the charge's own velocity.

> [!note]- Hint 4
> For parallel fields, $\mathbf{E}\cdot\mathbf{B} = EB \ne 0$, so $I_2 = cEB \ne 0$: the field is *already* parallel and cannot be reduced to a single field (a boost can never kill one of two parallel nonzero fields, because $I_2\ne0$ is invariant).

---

# Solution

The plan is to evaluate $I_1$ and $I_2$ for each field and read off the class and reducibility. Part 1 (plane wave) is the null field, irreducible. Part 2 (crossed, $cB>E$) is mostly magnetic, reducible to purely magnetic. Part 3 (moving charge) is mostly electric, reducible to purely electric. Part 4 (parallel) has $I_2\ne0$, already parallel and irreducible to a single field. The decisive insight is that the invariants alone determine all of this.

**Step 1: The plane wave is null.**

> [!note]- Derivation
> $\mathbf{E} = E_0\cos\phi\,e_2$, $\mathbf{B} = \frac{E_0}{c}\cos\phi\,e_3$. Then
> $$I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2 = c^2\frac{E_0^2}{c^2}\cos^2\phi - E_0^2\cos^2\phi = 0,$$
> $$I_2 = c\,\mathbf{E}\cdot\mathbf{B} = c\,(E_0\cos\phi)(\tfrac{E_0}{c}\cos\phi)(e_2\cdot e_3) = 0.$$
> Both invariants vanish: the plane wave is a **null** field. By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] it is the exceptional case that *cannot* be reduced — there is no frame in which it is purely electric, purely magnetic, or static. In every frame $E = cB$ and $\mathbf{E}\perp\mathbf{B}$: the wave looks like a wave to all observers (its amplitude and frequency Doppler-shift, but it stays a null field). This is the radiative class, exactly the field of an accelerated charge far away.

**Step 2: Crossed fields with $cB > E$ are mostly magnetic.**

> [!note]- Derivation
> $\mathbf{E} = E\,e_2$, $\mathbf{B} = B\,e_3$, $\mathbf{E}\perp\mathbf{B}$. Then
> $$I_1 = c^2B^2 - E^2 > 0 \quad(\text{since } cB > E), \qquad I_2 = c\,\mathbf{E}\cdot\mathbf{B} = 0.$$
> The field is **mostly magnetic** ($I_1 > 0$) with $\mathbf{E}\perp\mathbf{B}$ ($I_2 = 0$). By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction corollary]], it can be made **purely magnetic** by a boost perpendicular to both fields, at velocity
> $$U = \frac{E}{B} < c \quad(\text{since } E < cB),$$
> directed along $\mathbf{E}\times\mathbf{B} = e_2\times e_3\cdot EB = EB\,e_1$, i.e. along $e_1$. In that frame $\mathbf{E}' = 0$ and $\mathbf{B}' = \Gamma^{-1}\mathbf{B}$ — this is exactly the Wien-filter pass velocity, and the $\mathbf{E}\times\mathbf{B}/B^2$ drift velocity.

**Step 3: The moving-charge field is mostly electric.**

> [!note]- Derivation
> With $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$,
> $$I_2 = c\,\mathbf{E}\cdot\mathbf{B} = \frac{c}{c^2}\,\mathbf{E}\cdot(\mathbf{U}\times\mathbf{E}) = 0,$$
> since $\mathbf{U}\times\mathbf{E}$ is perpendicular to $\mathbf{E}$. For $I_1$, $|\mathbf{B}| = \frac{1}{c^2}|\mathbf{U}||\mathbf{E}|\sin\alpha$ (with $\alpha$ the angle between $\mathbf{U}$ and $\mathbf{E}$), so $c^2|\mathbf{B}|^2 = \frac{U^2\sin^2\alpha}{c^2}|\mathbf{E}|^2 \le \frac{U^2}{c^2}|\mathbf{E}|^2 < |\mathbf{E}|^2$, giving
> $$I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2 < 0.$$
> The field is **mostly electric** ($I_1 < 0$) with $\mathbf{E}\perp\mathbf{B}$. By the reduction corollary it can be made **purely electric** at velocity $U = c^2B/E$ — and this is exactly the charge's own velocity, recovering the charge's rest frame where $\mathbf{B}' = 0$ and $\mathbf{E}'$ is the Coulomb field. The invariants confirm what we built in: the moving-charge field is the boosted Coulomb field, mostly electric in every frame.

**Step 4: Parallel fields have $I_2 \ne 0$.**

> [!note]- Derivation
> $\mathbf{E} = E\,e_1$, $\mathbf{B} = B\,e_1$, parallel. Then
> $$I_1 = c^2B^2 - E^2 \quad(\text{sign depends on whether } cB \gtrless E), \qquad I_2 = c\,\mathbf{E}\cdot\mathbf{B} = cEB \ne 0.$$
> Since $I_2 \ne 0$, the fields are *already* parallel (consistent with the reduction theorem, which says a non-null field can be made parallel — here it already is), and they **cannot** be reduced to a single field: killing $\mathbf{E}$ or $\mathbf{B}$ would make $I_2 = c\,\mathbf{E}'\cdot\mathbf{B}' = 0$, contradicting the invariance of $I_2 = cEB\ne0$. The most one can do is boost *along* $e_1$ (the common direction), which leaves both fields unchanged. A field with $I_2\ne0$ always has both $\mathbf{E}$ and $\mathbf{B}$ nonzero in every frame.

> [!note]- Complete formal solution
> Compute $(I_1, I_2)$ for each field. **(1) Plane wave:** $E = cB$ and $\mathbf{E}\perp\mathbf{B}$ give $I_1 = 0$, $I_2 = 0$ — a null field, irreducible (no frame makes it pure or static). **(2) Crossed, $cB>E$:** $I_1 = c^2B^2 - E^2 > 0$, $I_2 = 0$ — mostly magnetic, reducible to purely magnetic at $U = E/B$. **(3) Moving charge,** $\mathbf{B} = \frac{1}{c^2}\mathbf{U}\times\mathbf{E}$: $I_2 = 0$ (orthogonal) and $c^2B^2 = \frac{U^2\sin^2\alpha}{c^2}E^2 < E^2$ so $I_1 < 0$ — mostly electric, reducible to purely electric at $U = c^2B/E$ (the charge's velocity). **(4) Parallel:** $I_2 = cEB\ne0$ — already parallel, irreducible to a single field since $I_2\ne0$ is invariant. In all cases the signs of $I_1$ and the vanishing of $I_2$ are frame-independent (full contractions of $F$), so the classification holds in every frame. $\blacksquare$

---

# Key Takeaways

**Two numbers classify a field for all observers.** The whole exercise is a drill in the single most labour-saving fact of §21.2: the field's character — mostly electric, mostly magnetic, or null — and the orthogonality of $\mathbf{E}$ and $\mathbf{B}$ are read off two scalars, $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$, computed in *any one* frame. Because these are full contractions of the [[Def - The Electromagnetic Field Tensor|field tensor]], their values (and especially the sign of $I_1$ and the vanishing of $I_2$) are frame-independent. The trigger is any question of the form "what kind of field is this?" or "can this field be transformed to be purely electric?" — compute the invariants, and the answer follows from the classification without solving for the transformation. This converts qualitative questions about a field into a two-line arithmetic check.

**The null field is the irreducible exception, and it is the radiation field.** The deepest content is part 1: a field with $I_1 = I_2 = 0$ — equal amplitudes ($E = cB$) and perpendicular ($\mathbf{E}\perp\mathbf{B}$) — *cannot* be reduced to a single field or to rest by any boost, because the required boost would need $U = c$. The plane electromagnetic wave is the archetype, and this is exactly the radiative ("null") part of the field of an accelerated charge. The lesson is that not every field can be simplified: the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] has one exceptional orbit, the null fields, and they are physically the most important ones — light itself. Recognising $E = cB$ with $\mathbf{E}\perp\mathbf{B}$ as the signature of a null field, in any frame, is a reusable diagnostic.

**$I_2 \ne 0$ forbids reduction to a single field.** The contrast between parts 2/3 (where $I_2 = 0$ and one field can be eliminated) and part 4 (where $I_2 \ne 0$ and both fields persist in every frame) is the operational meaning of the second invariant. Since $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ is invariant, a field with $\mathbf{E}\cdot\mathbf{B} \ne 0$ has both fields nonzero for *every* observer — you can align them (the reduction theorem) but never kill one. The diagnostic: if $I_2 \ne 0$, stop looking for a purely-electric or purely-magnetic frame, it does not exist; the best canonical form is parallel nonzero $\mathbf{E}$ and $\mathbf{B}$. This is why a general field with $I_2\ne0$ produces the "helix with increasing pitch" motion of [[Thm - Motion of a Charge in a Uniform Field]] — there is irreducibly both an accelerating and a bending field.
