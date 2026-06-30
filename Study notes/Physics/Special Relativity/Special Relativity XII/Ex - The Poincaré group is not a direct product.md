---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Poincaré Group"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Def - The Poincaré Group|Poincaré group]] decomposes, as a set, into a translation part and a Lorentz part, $f = (\boldsymbol{v}, \Lambda)$, which tempts one to call it the direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$. Show this is false: it is a *semidirect* product. Working with $c = 1$:

1. Recall that the **direct product** $(G_1, *_1) \times (G_2, *_2)$ composes componentwise: $(a_1, a_2)(b_1, b_2) = (a_1 *_1 b_1,\, a_2 *_2 b_2)$. State what the Poincaré composition would be if it were the direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$, namely $(\boldsymbol{v}_1 + \boldsymbol{v}_2,\, \Lambda_1\Lambda_2)$.
2. Recall the actual Poincaré law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\, \Lambda_1\Lambda_2)$ and show it agrees with the direct-product law if and only if $\Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_2$ for all relevant $\boldsymbol{v}_2$.
3. Exhibit a concrete counterexample: take $\Lambda_1$ a boost and $\boldsymbol{v}_2$ a spacelike translation it does not fix, and compute $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$, so the two laws disagree.
4. Explain in physical terms why the semidirect twist is *forced*: translating-then-boosting must differ from boosting-then-translating, because a boost changes the axes against which a translation is measured. Show this by composing a boost and a translation in both orders and exhibiting that they do not commute.

**Recall:**

![[Def - The Poincaré Group#The Definition]]

The **direct product** of groups composes each factor independently and makes both factors normal subgroups that commute. The **semidirect product** $N \rtimes H$ has $H$ acting on $N$, so the factors do *not* commute; the actual Poincaré law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ has the Lorentz part $\Lambda_1$ acting on the translation $\boldsymbol{v}_2$. A [[Def - The Lorentz Group|Lorentz boost]] $\Lambda$ does not fix a generic four-vector.

---

# Convergent Strategy

**Problem class.** A *distinguish-two-structures* problem: prove a group is a semidirect, not a direct, product by exhibiting where the composition laws differ. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for group-structure problems says to compare $\Lambda_1\boldsymbol{v}_2$ with $\boldsymbol{v}_2$.

**Assumption pattern.** The two candidate laws differ by exactly the factor $\Lambda_1$ on $\boldsymbol{v}_2$. They agree iff $\Lambda_1$ fixes every translation, i.e. iff the Lorentz action is trivial — which it is not. The signpost is "is it a direct or semidirect product?": compute whether the off-diagonal action $\Lambda_1\boldsymbol{v}_2$ is trivial.

**Theorem routing.** The route is a single counterexample: choose $\Lambda_1$ a boost and $\boldsymbol{v}_2$ a four-vector it moves, and exhibit $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$. Then the actual law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \cdots)$ differs from the direct-product law $(\boldsymbol{v}_1 + \boldsymbol{v}_2, \cdots)$, settling it. The physical half shows a boost and a translation fail to commute, which is the group-theoretic content of the twist.

**Key decision point.** The crux is realising that the *only* difference between the two laws is whether the Lorentz part acts on the translation, and that a single $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$ kills the direct-product hypothesis. The deeper point — why the twist is forced — is that a boost re-expresses a translation in rotated coordinates, so the order of boost and translation matters; the non-commutativity of boost and translation *is* the semidirect structure. Choosing a boost (not a rotation) and a translation it actually moves is what makes the counterexample bite.

---

# Legal Operations Used

1. **Compose using the semidirect law** (operation 5 from the topic page). The actual law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ is compared against the hypothetical direct-product law.

2. The exercise is the explicit counterexample behind illegal operation 2 of the topic page ("treating the Poincaré group as $\mathbb{R}^4 \times \mathrm{O}(1,3)$"): it exhibits the boost $\Lambda_1$ and translation $\boldsymbol{v}_2$ with $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$ that forbids the direct-product structure.

---

# Hints

> [!note]- Hint 1
> The direct product would compose translations by plain addition: $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, \Lambda_1\Lambda_2)$. The actual law has $\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2$. They differ by the factor $\Lambda_1$ on $\boldsymbol{v}_2$.

> [!note]- Hint 2
> The two laws coincide iff $\Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_2$ for all $\boldsymbol{v}_2$ — i.e. iff every Lorentz transformation fixes every four-vector, i.e. iff the Lorentz action is trivial. It is not (a boost moves four-vectors), so they differ.

> [!note]- Hint 3
> Take a boost along $x$ with rapidity $\zeta$: $\Lambda_1(t, x, y, z) = (t\cosh\zeta + x\sinh\zeta,\, t\sinh\zeta + x\cosh\zeta,\, y,\, z)$. Apply it to $\boldsymbol{v}_2 = (0, 1, 0, 0)$ (a unit spatial translation): you get $(\sinh\zeta, \cosh\zeta, 0, 0) \neq (0, 1, 0, 0)$ for $\zeta \neq 0$. So $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$.

> [!note]- Hint 4
> Compose a pure boost $(\boldsymbol{0}, \Lambda)$ and a pure translation $(\boldsymbol{a}, \mathrm{Id})$ in both orders: $(\boldsymbol{0}, \Lambda)(\boldsymbol{a}, \mathrm{Id}) = (\Lambda\boldsymbol{a}, \Lambda)$ but $(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda) = (\boldsymbol{a}, \Lambda)$. They differ ($\Lambda\boldsymbol{a} \neq \boldsymbol{a}$), so boost and translation do not commute — the hallmark of a semidirect, not direct, product.

---

# Solution

The two structures differ by exactly one factor. Step 1 writes the direct-product law. Step 2 shows it agrees with the actual law iff the Lorentz action is trivial. Step 3 exhibits a boost and a translation with $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$. Step 4 shows boost and translation do not commute, the physical reason the twist is forced.

**Step 1: What the direct-product law would be.**

> [!note]- Derivation
> The **direct product** $(G_1, *_1) \times (G_2, *_2)$ is the Cartesian product $G_1 \times G_2$ with the componentwise law $(a_1, a_2)(b_1, b_2) = (a_1 *_1 b_1,\, a_2 *_2 b_2)$ — each factor minds its own business, neither aware of the other. Were the Poincaré group the direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$, with $G_1 = (\mathbb{R}^4, +)$ and $G_2 = (\mathrm{O}(1,3), \cdot)$, its law would be
> $$(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) \overset{?}{=} (\boldsymbol{v}_1 + \boldsymbol{v}_2,\; \Lambda_1\Lambda_2) \qquad\text{(direct product, addition in the translation slot)}.$$
> The translations would simply add, the Lorentz parts simply multiply, and the two would never interact.

**Step 2: Agreement iff the Lorentz action is trivial.**

> [!note]- Derivation
> The actual Poincaré law (from [[Def - The Poincaré Group]] / [[Ex - The semidirect product group law of the Poincaré group]]) is
> $$(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2).$$
> Comparing with the hypothetical direct-product law, the Lorentz slots agree ($\Lambda_1\Lambda_2$ both times), and the translation slots agree iff
> $$\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_1 + \boldsymbol{v}_2 \iff \Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_2.$$
> For the laws to coincide *as group laws*, this must hold for *all* $\Lambda_1 \in \mathrm{O}(1,3)$ and all $\boldsymbol{v}_2 \in \mathbb{R}^4$ — i.e. *every* Lorentz transformation must fix *every* four-vector. That is the statement that the Lorentz action on $\mathbb{R}^4$ is trivial. It is manifestly false: the defining action of $\mathrm{O}(1,3)$ on four-vectors is the standard one, and a non-identity Lorentz transformation moves four-vectors. So the actual law is *not* the direct-product law.

**Step 3: A concrete counterexample.**

> [!note]- Derivation
> Take $\Lambda_1$ a boost along the $x$-axis with rapidity $\zeta \neq 0$:
> $$\Lambda_1(t, x, y, z) = (t\cosh\zeta + x\sinh\zeta,\; t\sinh\zeta + x\cosh\zeta,\; y,\; z),$$
> and take $\boldsymbol{v}_2 = (0, 1, 0, 0)$, a unit translation in the $x$-direction. Then
> $$\Lambda_1\boldsymbol{v}_2 = (0\cdot\cosh\zeta + 1\cdot\sinh\zeta,\; 0\cdot\sinh\zeta + 1\cdot\cosh\zeta,\; 0,\; 0) = (\sinh\zeta,\; \cosh\zeta,\; 0,\; 0).$$
> Since $\cosh\zeta > 1$ and $\sinh\zeta \neq 0$ for $\zeta \neq 0$,
> $$\Lambda_1\boldsymbol{v}_2 = (\sinh\zeta, \cosh\zeta, 0, 0) \neq (0, 1, 0, 0) = \boldsymbol{v}_2.$$
> So for these choices the actual translation slot $\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_1 + (\sinh\zeta, \cosh\zeta, 0, 0)$ differs from the direct-product slot $\boldsymbol{v}_1 + \boldsymbol{v}_2 = \boldsymbol{v}_1 + (0, 1, 0, 0)$. The two composition laws give different answers, so the Poincaré group is *not* the direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$. It is the **semidirect** product $\mathbb{R}^4 \rtimes \mathrm{O}(1,3)$.

**Step 4: Boost and translation do not commute — why the twist is forced.**

> [!note]- Derivation
> Compose a pure boost $g = (\boldsymbol{0}, \Lambda)$ and a pure translation $h = (\boldsymbol{a}, \mathrm{Id})$ in both orders. *Boost then translation* ($g$ applied after $h$, i.e. $g\circ h$):
> $$(\boldsymbol{0}, \Lambda)(\boldsymbol{a}, \mathrm{Id}) = (\boldsymbol{0} + \Lambda\boldsymbol{a},\; \Lambda\cdot\mathrm{Id}) = (\Lambda\boldsymbol{a},\; \Lambda).$$
> *Translation then boost* ($h\circ g$):
> $$(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda) = (\boldsymbol{a} + \mathrm{Id}\cdot\boldsymbol{0},\; \mathrm{Id}\cdot\Lambda) = (\boldsymbol{a},\; \Lambda).$$
> The Lorentz parts agree, but the translation parts are $\Lambda\boldsymbol{a}$ versus $\boldsymbol{a}$ — *different* whenever $\Lambda\boldsymbol{a} \neq \boldsymbol{a}$, which is the case for a boost and a generic $\boldsymbol{a}$. So boost and translation **do not commute**: $gh \neq hg$. In a direct product the two factors *would* commute (componentwise composition makes them independent), so the failure to commute is precisely the proof that the structure is semidirect, not direct.
>
> Physically: a boost changes the coordinate axes against which a displacement is measured. "Translate by $\boldsymbol{a}$, then boost" carries the displacement $\boldsymbol{a}$ along unchanged and then boosts the whole configuration; "boost, then translate by $\boldsymbol{a}$" applies the displacement *after* the axes have been boosted, so the same numerical $\boldsymbol{a}$ now points in boosted directions. The translation $\boldsymbol{a}$ means something different before and after the boost, and the discrepancy is exactly $\Lambda\boldsymbol{a} - \boldsymbol{a}$. The semidirect twist $\Lambda_1\boldsymbol{v}_2$ in the group law is the bookkeeping that records this: the later transformation's Lorentz part re-expresses the earlier translation. The twist is not a convention; it is forced by the geometric fact that boosts and translations interfere.

> [!note]- Complete formal solution
> The direct product $\mathbb{R}^4 \times \mathrm{O}(1,3)$ would compose by $(\boldsymbol{v}_1 + \boldsymbol{v}_2, \Lambda_1\Lambda_2)$, whereas the actual Poincaré law is $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$. These agree iff $\Lambda_1\boldsymbol{v}_2 = \boldsymbol{v}_2$ for all $\Lambda_1, \boldsymbol{v}_2$, i.e. iff the Lorentz action is trivial — which is false. Concretely, a boost of rapidity $\zeta \neq 0$ sends $\boldsymbol{v}_2 = (0,1,0,0)$ to $(\sinh\zeta, \cosh\zeta, 0, 0) \neq \boldsymbol{v}_2$, so the two laws differ and the Poincaré group is the semidirect product $\mathbb{R}^4 \rtimes \mathrm{O}(1,3)$, not the direct product. The twist is forced because boost and translation do not commute: $(\boldsymbol{0}, \Lambda)(\boldsymbol{a}, \mathrm{Id}) = (\Lambda\boldsymbol{a}, \Lambda)$ while $(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda) = (\boldsymbol{a}, \Lambda)$, differing by $\Lambda\boldsymbol{a} - \boldsymbol{a}$ — a boost changes the axes against which a translation is measured, so the order matters. $\blacksquare$

---

# Key Takeaways

**Direct versus semidirect is decided by one question: does the off-diagonal action act trivially?** The entire distinction reduces to whether $\Lambda_1\boldsymbol{v}_2$ equals $\boldsymbol{v}_2$. If the Lorentz part acts trivially on translations, the product is direct; if it acts non-trivially — as it must, since boosts move four-vectors — the product is semidirect. A single counterexample $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$ settles it. The transferable diagnostic for any candidate direct product $N \times H$: check whether $H$ really acts trivially on $N$; if there is any non-trivial action, the honest structure is the semidirect product $N \rtimes H$. This is the standard test, and it applies to the Euclidean group (rotations move translations — semidirect), the affine group, and gauge groups (the gauge action on fields is non-trivial — semidirect).

**Non-commuting factors are the fingerprint of a semidirect product.** Step 4's computation — that a boost and a translation fail to commute, $gh \neq hg$ — is the group-theoretic heart of the matter. In a *direct* product the two factors commute (componentwise composition makes them independent), so any failure of two factors to commute proves the product is not direct. The boost–translation non-commutativity $\Lambda\boldsymbol{a} \neq \boldsymbol{a}$ is exactly the semidirect twist. The reusable insight: to decide whether a group built from two subgroups is direct or semidirect, check whether elements of one subgroup commute with elements of the other; non-commutativity forces the semidirect structure and identifies which factor acts on which. This is often faster than computing the full composition law.

**The twist is geometry, not convention — a boost re-expresses a translation in rotated axes.** The deepest takeaway is *why* the semidirect twist is forced rather than chosen. A translation $\boldsymbol{a}$ is a displacement measured against some axes; a boost rotates those axes; so the same numerical $\boldsymbol{a}$ means a different physical displacement before and after the boost. Translating-then-boosting and boosting-then-translating therefore genuinely differ, by exactly $\Lambda\boldsymbol{a} - \boldsymbol{a}$, and the group law's factor $\Lambda_1\boldsymbol{v}_2$ is the record of this. This is not special to relativity: in *any* setting where a "rotation-like" operation acts on a "translation-like" one — rigid motions of space, gauge transformations acting on fields, frame changes acting on coordinates — the two interfere and the composite structure is semidirect. Recognising the semidirect twist as the geometric statement "the linear part re-expresses the translation" lets you predict the composition law of such groups without re-deriving it, and explains why the Poincaré group's representation theory (Wigner's induced representations) must build states from the momentum eigenvalues of the *normal* translation factor.
