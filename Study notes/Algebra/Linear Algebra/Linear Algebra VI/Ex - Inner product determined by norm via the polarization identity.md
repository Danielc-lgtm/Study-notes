---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
  - "Thm - Parallelogram Law"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be an inner product space over $\mathbf{F}$.

**(Real case.)** Show that if $\mathbf{F} = \mathbb{R}$, then
$$
\langle u, v\rangle = \frac{\|u + v\|^2 - \|u - v\|^2}{4} \qquad \text{for every } u, v \in V.
$$

**(Complex case.)** Show that if $\mathbf{F} = \mathbb{C}$, then
$$
\langle u, v\rangle = \frac{\|u + v\|^2 - \|u - v\|^2 + i\|u + iv\|^2 - i\|u - iv\|^2}{4} \qquad \text{for every } u, v \in V.
$$

These formulas — the **polarization identities** — show that **the inner product is determined by the norm alone**.

**Recall:**

The norm $\|v\| = \sqrt{\langle v, v\rangle}$ is induced from the inner product (see [[Def - Norm Induced by an Inner Product]]). The squared-norm expansion is:
$$
\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2,
$$
$$
\|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.
$$

![[Thm - Parallelogram Law#Statement]]

The complex inner product is conjugate-linear in the second slot: $\langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle$.

---

# Convergent Strategy

**Problem class.** This is a *recover a structure from a coarser one* problem: given the inner-product-induced norm, recover the inner product. The strategy is to expand the norms in terms of the inner product and combine them so that the inner product survives while the auxiliary terms cancel.

**Assumption pattern.** The hypothesis is that the norm comes from an inner product (so the squared-norm expansion is available). Over $\mathbb{R}$, $\langle u, v\rangle$ is real, so $\operatorname{Re}\langle u, v\rangle = \langle u, v\rangle$, and the two-term expansion suffices. Over $\mathbb{C}$, $\langle u, v\rangle$ has both a real part and an imaginary part, and recovering both requires four terms (involving $u \pm v$ and $u \pm iv$).

**Theorem routing.** Direct algebraic manipulation of the squared-norm expansion. No named theorem is invoked beyond the inner-product axioms and the definition of the norm.

**Key decision point.** In the complex case, the choice to use $u \pm iv$ for the imaginary part. The expansion $\|u + iv\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, iv\rangle + \|v\|^2 = \|u\|^2 + 2\operatorname{Re}(-i \langle u, v\rangle) + \|v\|^2 = \|u\|^2 + 2\operatorname{Im}\langle u, v\rangle + \|v\|^2$ — *the imaginary part of $\langle u, v\rangle$ appears as the cross-term*. This is the key insight that motivates the four-term complex formula.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VI — §6 Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Expand $\|\alpha u + \beta v\|^2$ using sesquilinearity** (operation 1). The fundamental identity $\|u \pm v\|^2 = \|u\|^2 \pm 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$ is the algebraic engine of both polarization identities. Over $\mathbb{C}$, additional applications give $\|u \pm iv\|^2 = \|u\|^2 \mp 2\operatorname{Im}\langle u, v\rangle + \|v\|^2$.

2. **Use the polarization identity** (operation 10) — this is the technique being proved, so the exercise is more about *deriving* the operation than applying it.

---

# Hints

> [!note]- Hint 1
> The squared-norm expansion $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$ is the algebraic engine. Compute $\|u + v\|^2 - \|u - v\|^2$ and see what cancels.

> [!note]- Hint 2
> In the real case, $\operatorname{Re}\langle u, v\rangle = \langle u, v\rangle$, and the cross-term doubles when you subtract $\|u - v\|^2$ from $\|u + v\|^2$. So $\|u + v\|^2 - \|u - v\|^2 = 4\langle u, v\rangle$.

> [!note]- Hint 3
> In the complex case, $\|u + v\|^2 - \|u - v\|^2 = 4\operatorname{Re}\langle u, v\rangle$ — but you need $\langle u, v\rangle$, not just its real part. To recover the imaginary part, use $\|u + iv\|^2$.

> [!note]- Hint 4
> $\|u + iv\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, iv\rangle + \|v\|^2$. Compute $\operatorname{Re}\langle u, iv\rangle = \operatorname{Re}(\bar i \langle u, v\rangle) = \operatorname{Re}(-i\langle u, v\rangle) = \operatorname{Im}\langle u, v\rangle$. So $\|u + iv\|^2 - \|u - iv\|^2 = 4\operatorname{Im}\langle u, v\rangle$.

> [!note]- Hint 5
> Combine: $\langle u, v\rangle = \operatorname{Re}\langle u, v\rangle + i\operatorname{Im}\langle u, v\rangle = \frac{\|u + v\|^2 - \|u - v\|^2}{4} + i\frac{\|u + iv\|^2 - \|u - iv\|^2}{4}$.

---

# Solution

The strategy is to expand the squared norms in terms of inner products and observe what survives the subtraction.

**Plan:** Step 1 derives the real-case identity via $\|u + v\|^2 - \|u - v\|^2$. Step 2 derives the imaginary part of $\langle u, v\rangle$ via $\|u + iv\|^2 - \|u - iv\|^2$. Step 3 combines the two to give the full complex polarization identity. The complex case strictly generalizes the real one (when $\langle u, v\rangle$ is real, the imaginary-part terms vanish).

**Step 1: Real case — $\langle u, v\rangle = \frac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$.**

Subtract the two norm-squared expansions; the diagonal terms cancel and the cross-term doubles.

> [!note]- Derivation
> Expand $\|u + v\|^2$ using sesquilinearity (over $\mathbb{R}$, this is just bilinearity):
> $$\|u + v\|^2 = \langle u + v, u + v\rangle = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2 = \|u\|^2 + 2\langle u, v\rangle + \|v\|^2,$$
> where the last step uses $\langle v, u\rangle = \langle u, v\rangle$ over $\mathbb{R}$ (real inner product is symmetric).
>
> Similarly,
> $$\|u - v\|^2 = \|u\|^2 - 2\langle u, v\rangle + \|v\|^2.$$
>
> Subtracting:
> $$\|u + v\|^2 - \|u - v\|^2 = 4\langle u, v\rangle.$$
>
> Dividing by $4$: $\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$.

**Step 2: Imaginary part of $\langle u, v\rangle$ via $\|u \pm iv\|^2$ (complex case).**

Compute the squared norms $\|u + iv\|^2$ and $\|u - iv\|^2$; their difference gives $4\operatorname{Im}\langle u, v\rangle$.

> [!note]- Derivation
> Expand $\|u + iv\|^2$ using sesquilinearity:
> $$\|u + iv\|^2 = \langle u + iv, u + iv\rangle = \|u\|^2 + \langle u, iv\rangle + \langle iv, u\rangle + \|iv\|^2.$$
>
> Use $\langle u, iv\rangle = \overline{i}\,\langle u, v\rangle = -i\langle u, v\rangle$ (conjugate-linearity in the second slot), and $\langle iv, u\rangle = i\langle v, u\rangle = i\overline{\langle u, v\rangle}$ (linearity in the first slot, conjugate-symmetry). Also $\|iv\|^2 = |i|^2 \|v\|^2 = \|v\|^2$.
>
> So
> $$\|u + iv\|^2 = \|u\|^2 - i\langle u, v\rangle + i\overline{\langle u, v\rangle} + \|v\|^2.$$
>
> Write $\langle u, v\rangle = a + bi$ with $a = \operatorname{Re}\langle u, v\rangle$ and $b = \operatorname{Im}\langle u, v\rangle$. Then $\overline{\langle u, v\rangle} = a - bi$.
>
> Compute $-i\langle u, v\rangle + i\overline{\langle u, v\rangle} = -i(a + bi) + i(a - bi) = -ai - bi^2 + ai - bi^2 = b - b \cdot (-1) - b \cdot (-1)$ — let me redo this.
>
> $-i(a + bi) = -ai - bi^2 = -ai + b$.
>
> $i(a - bi) = ai - bi^2 = ai + b$.
>
> Adding: $-ai + b + ai + b = 2b = 2\operatorname{Im}\langle u, v\rangle$.
>
> So
> $$\|u + iv\|^2 = \|u\|^2 + 2\operatorname{Im}\langle u, v\rangle + \|v\|^2.$$
>
> By the same calculation with $-i$ in place of $i$,
> $$\|u - iv\|^2 = \|u\|^2 - 2\operatorname{Im}\langle u, v\rangle + \|v\|^2.$$
>
> Subtracting: $\|u + iv\|^2 - \|u - iv\|^2 = 4\operatorname{Im}\langle u, v\rangle$.

**Step 3: Combine — full complex polarization identity.**

Use Step 1 (which gives the real part of $\langle u, v\rangle$) and Step 2 (which gives the imaginary part) to assemble $\langle u, v\rangle$.

> [!note]- Derivation
> From Step 1 (modified for the complex case, where the cross-terms give the real part):
> $$\|u + v\|^2 - \|u - v\|^2 = 4 \operatorname{Re}\langle u, v\rangle.$$
> Dividing by $4$: $\operatorname{Re}\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$.
>
> From Step 2: $\operatorname{Im}\langle u, v\rangle = \tfrac{1}{4}(\|u + iv\|^2 - \|u - iv\|^2)$.
>
> Combining,
> $$\langle u, v\rangle = \operatorname{Re}\langle u, v\rangle + i\operatorname{Im}\langle u, v\rangle = \frac{\|u + v\|^2 - \|u - v\|^2 + i\|u + iv\|^2 - i\|u - iv\|^2}{4}.$$

> [!note]- Complete formal solution
> **(Real case.)** Expand:
> $$\|u + v\|^2 = \|u\|^2 + 2\langle u, v\rangle + \|v\|^2,$$
> $$\|u - v\|^2 = \|u\|^2 - 2\langle u, v\rangle + \|v\|^2.$$
> Subtracting and dividing by $4$:
> $$\langle u, v\rangle = \frac{\|u + v\|^2 - \|u - v\|^2}{4}.$$
>
> **(Complex case.)** Expand:
> $$\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2,$$
> $$\|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.$$
> Subtracting: $\|u + v\|^2 - \|u - v\|^2 = 4\operatorname{Re}\langle u, v\rangle$.
>
> For the imaginary part, expand $\|u + iv\|^2$. Using $\langle u, iv\rangle = \bar i \langle u, v\rangle = -i\langle u, v\rangle$ and $\langle iv, u\rangle = i\langle v, u\rangle = i\overline{\langle u, v\rangle}$:
> $$\|u + iv\|^2 = \|u\|^2 + \langle u, iv\rangle + \langle iv, u\rangle + \|iv\|^2 = \|u\|^2 - i\langle u, v\rangle + i\overline{\langle u, v\rangle} + \|v\|^2 = \|u\|^2 + 2\operatorname{Im}\langle u, v\rangle + \|v\|^2,$$
> where the last equality uses $-i\langle u, v\rangle + i\overline{\langle u, v\rangle} = -i(a + bi) + i(a - bi) = 2b$ for $\langle u, v\rangle = a + bi$, identifying $b = \operatorname{Im}\langle u, v\rangle$.
>
> Similarly $\|u - iv\|^2 = \|u\|^2 - 2\operatorname{Im}\langle u, v\rangle + \|v\|^2$.
>
> Subtracting: $\|u + iv\|^2 - \|u - iv\|^2 = 4\operatorname{Im}\langle u, v\rangle$.
>
> Combining: $\langle u, v\rangle = \operatorname{Re}\langle u, v\rangle + i\operatorname{Im}\langle u, v\rangle = \frac{1}{4}(\|u + v\|^2 - \|u - v\|^2) + \frac{i}{4}(\|u + iv\|^2 - \|u - iv\|^2)$, which is the complex polarization identity. $\blacksquare$

---

# Key Takeaways

**The inner product and the norm are equivalent data.** The polarization identity is the precise statement that the norm $\|v\| = \sqrt{\langle v, v\rangle}$ contains *all* the information of the inner product — and indeed of every inner product on $V$, since the same identity recovers any inner product from its induced norm. Knowing the norm is the same as knowing the inner product. This is one direction of an equivalence; the other is that $\langle\cdot,\cdot\rangle$ determines $\|\cdot\|$ by definition. Together they say: in an inner product space, the norm and the inner product are two views of the same structure. The transferable lesson: norm-level information feeds back into inner-product-level computations via polarization, so a problem that gives you norms is a problem that secretly gives you inner products.

**The complex case has four terms because $\langle u, v\rangle$ has two real degrees of freedom.** Over $\mathbb{R}$, $\langle u, v\rangle$ is a single real number, and one combination of two norms ($\|u + v\|^2, \|u - v\|^2$) suffices to extract it. Over $\mathbb{C}$, $\langle u, v\rangle$ has both a real and an imaginary part, doubling the information; correspondingly, four norms ($\|u + v\|^2, \|u - v\|^2, \|u + iv\|^2, \|u - iv\|^2$) are needed to extract both parts. The number of terms in the polarization identity matches the [[Def - Dimension|dimension]] of $\mathbf{F}$ over $\mathbb{R}$ (one for $\mathbb{R}$, two for $\mathbb{C}$). This dimensional accounting explains why the complex polarization identity looks more complicated than the real one — there is genuinely twice as much information to recover.

**The Jordan-von Neumann characterisation of inner-product norms.** This exercise, combined with the parallelogram law and an axiom-by-axiom verification, gives the full Jordan-von Neumann theorem: a norm on a vector space comes from an inner product if and only if it satisfies the parallelogram law. The proof in the "if" direction defines a candidate inner product via the polarization identity and verifies that it is sesquilinear, conjugate-symmetric, positive — and the parallelogram law is precisely what is needed for the additivity check. This is the structural reason "Hilbert space" is a property of the *norm* alone: it captures all the Hilbert-geometric content. The transferable lesson is the test for whether a particular Banach space is a Hilbert space — check the parallelogram law on a pair of vectors; if it fails, you have a Banach space that is not a Hilbert space (and hence has no inner-product structure compatible with the norm).

**The trigger-reaction pattern: norm information ⟶ polarization ⟶ inner-product information.** Whenever a problem gives you control over $\|u + v\|, \|u - v\|, \|u + iv\|, \|u - iv\|$ (or any of the relevant combinations), the polarization identity lets you extract $\langle u, v\rangle$. This is the recipe for "I know norms but need inner products". The reverse direction is even simpler: $\|v\|^2 = \langle v, v\rangle$ — to compute norm-squared, use the inner product. Together these establish that norm and inner product are interconvertible, with polarization being the conversion in one direction. The pattern appears in functional-analytic proofs of inner-product-structure preservation: if a map preserves the norm, the polarization identity forces it to preserve the inner product too.
