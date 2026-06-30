---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Poincaré Group"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

A [[Def - The Poincaré Group|Poincaré transformation]] $f$ acts on Minkowski spacetime by $\overrightarrow{O\,f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}$, where $\Lambda$ is its Lorentz part and $\boldsymbol{v} = \overrightarrow{O\,f(O)}$ its translation vector; we write $f = (\boldsymbol{v}, \Lambda)$. Working with $c = 1$ and a fixed origin $O$:

1. Let $f_1 = (\boldsymbol{v}_1, \Lambda_1)$ and $f_2 = (\boldsymbol{v}_2, \Lambda_2)$. Compute the composition $f_1\circ f_2$ by applying the action formula twice, and show
$$f_1\circ f_2 = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2).$$
2. Identify precisely where the factor $\Lambda_1$ enters, and explain why it multiplies $\boldsymbol{v}_2$ rather than $\boldsymbol{v}_1$.
3. Verify the identity element is $(\boldsymbol{0}, \mathrm{Id})$ and derive the inverse $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$.
4. Confirm associativity of the group law directly from the formula.

**Recall:**

![[Def - The Poincaré Group#The Definition]]

A [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda$ is a linear map of the displacement space preserving the metric. The composition of two affine maps is affine; the key fact used is that the linear part of an affine map acts on *everything* to its right, including any translation produced earlier.

---

# Convergent Strategy

**Problem class.** A *derive-the-group-law* problem: compute the composition of two transformations from their action and read off the group multiplication. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for group-structure problems says to write every transformation as a pair $(\boldsymbol{v}, \Lambda)$ and substitute into the action formula.

**Assumption pattern.** The single tool is the action formula $\overrightarrow{O\,f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}$, applied twice. The signpost is "compose two Poincaré transformations" — always apply the inner one first, then the outer one, and track how the outer Lorentz part acts on the inner translation.

**Theorem routing.** No external theorem: the derivation is direct substitution. Apply $f_2$ to get $\overrightarrow{O\,f_2(M)} = \Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2$; apply $f_1$ to $f_2(M)$, with its Lorentz part $\Lambda_1$ acting on the whole displacement $\overrightarrow{O\,f_2(M)}$; collect to find translation part $\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2$ and Lorentz part $\Lambda_1\Lambda_2$. This *is* [[Def - The Poincaré Group|the group law]].

**Key decision point.** The crux — and the only place to go wrong — is realising that when $f_1$ acts on $f_2(M)$, its Lorentz part $\Lambda_1$ acts on the *entire* displacement $\overrightarrow{O\,f_2(M)}$, which already contains the translation $\boldsymbol{v}_2$ that $f_2$ produced. So $\boldsymbol{v}_2$ gets rotated by $\Lambda_1$. The natural-but-wrong expectation is that the translations simply add ($\boldsymbol{v}_1 + \boldsymbol{v}_2$); the factor $\Lambda_1$ is the whole reason the group is a semidirect, not a direct, product.

---

# Legal Operations Used

1. **Decompose a Poincaré transformation as $(\boldsymbol{v}, \Lambda)$** (operation 4 from the topic page). Both $f_1$ and $f_2$ are written in pair form, with $\boldsymbol{v}$ the image of the origin and $\Lambda$ the linear part.

2. **Compose using the action formula** (operation 5 from the topic page, here *derived* rather than used): applying $\overrightarrow{O\,f(M)} = \Lambda\overrightarrow{OM} + \boldsymbol{v}$ twice produces the semidirect law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$.

---

# Hints

> [!note]- Hint 1
> Apply $f_2$ first: $\overrightarrow{O\,f_2(M)} = \Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2$. Now apply $f_1$ to the point $f_2(M)$, treating $f_2(M)$ as the new input event $N$: $\overrightarrow{O\,f_1(N)} = \Lambda_1\overrightarrow{ON} + \boldsymbol{v}_1$.

> [!note]- Hint 2
> Substitute $\overrightarrow{ON} = \overrightarrow{O\,f_2(M)} = \Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2$ into the previous line. The Lorentz part $\Lambda_1$ is linear, so it distributes over the sum: $\Lambda_1(\Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2) = \Lambda_1\Lambda_2\overrightarrow{OM} + \Lambda_1\boldsymbol{v}_2$.

> [!note]- Hint 3
> Collect: $\overrightarrow{O\,(f_1\circ f_2)(M)} = \Lambda_1\Lambda_2\overrightarrow{OM} + (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2)$. Reading off the Lorentz part $\Lambda_1\Lambda_2$ and translation part $\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2$ gives the group law.

---

# Solution

The derivation is two applications of the action formula. Step 1 applies $f_2$ then $f_1$, with $\Lambda_1$ distributing over the displacement produced by $f_2$, yielding the law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$. Step 2 isolates the role of $\Lambda_1$. Steps 3–4 extract the identity, inverse, and associativity.

**Step 1: Compose by applying the action twice.**

> [!note]- Derivation
> Apply $f_2 = (\boldsymbol{v}_2, \Lambda_2)$ to a generic event $M$:
> $$\overrightarrow{O\,f_2(M)} = \Lambda_2\,\overrightarrow{OM} + \boldsymbol{v}_2.$$
> Now apply $f_1 = (\boldsymbol{v}_1, \Lambda_1)$ to the event $f_2(M)$. The action formula, with input event $f_2(M)$, reads
> $$\overrightarrow{O\,f_1(f_2(M))} = \Lambda_1\,\overrightarrow{O\,f_2(M)} + \boldsymbol{v}_1.$$
> Substitute the first line into the second, and use that $\Lambda_1$ is *linear* so it distributes over the sum:
> $$\overrightarrow{O\,(f_1\circ f_2)(M)} = \Lambda_1\big(\Lambda_2\,\overrightarrow{OM} + \boldsymbol{v}_2\big) + \boldsymbol{v}_1 = \underbrace{\Lambda_1\Lambda_2}_{\text{Lorentz part}}\,\overrightarrow{OM} + \underbrace{\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2}_{\text{translation part}}.$$
> This has the form of a Poincaré action $\overrightarrow{O\,g(M)} = \Lambda_g\overrightarrow{OM} + \boldsymbol{v}_g$ with $\Lambda_g = \Lambda_1\Lambda_2$ and $\boldsymbol{v}_g = \boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2$. Hence
> $$f_1\circ f_2 = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2).$$
> (This is Gourgoulhon's eq. 8.23.)

**Step 2: Where $\Lambda_1$ enters, and why on $\boldsymbol{v}_2$.**

> [!note]- Derivation
> The factor $\Lambda_1$ multiplies $\boldsymbol{v}_2$ because, when $f_1$ acts on the event $f_2(M)$, its Lorentz part $\Lambda_1$ acts on the *entire* displacement $\overrightarrow{O\,f_2(M)}$ — and that displacement already contains the translation $\boldsymbol{v}_2$ that $f_2$ produced. So $f_1$ rotates/boosts everything that came before it, including $f_2$'s shift. By contrast $\boldsymbol{v}_1$ is $f_1$'s *own* translation, applied last, after $\Lambda_1$ has acted, so it is added bare.
>
> Physically: a boost changes what "translate by $\boldsymbol{v}_2$" means, because it changes the axes against which $\boldsymbol{v}_2$ is measured. Applying $f_2$ (which translates by $\boldsymbol{v}_2$) and *then* $f_1$ (which boosts by $\Lambda_1$) is not the same as applying the translation in $f_1$'s frame — the earlier translation is seen, by the later boost, re-expressed in rotated coordinates. The asymmetry "$\Lambda_1$ on $\boldsymbol{v}_2$, not $\Lambda_2$ on $\boldsymbol{v}_1$" records the order of composition: the *outer* (later) transformation's linear part acts on the *inner* (earlier) translation.

**Step 3: Identity and inverse.**

> [!note]- Derivation
> *Identity.* The pair $(\boldsymbol{0}, \mathrm{Id})$ satisfies $(\boldsymbol{0}, \mathrm{Id})(\boldsymbol{v}, \Lambda) = (\boldsymbol{0} + \mathrm{Id}\,\boldsymbol{v}, \mathrm{Id}\,\Lambda) = (\boldsymbol{v}, \Lambda)$ and $(\boldsymbol{v}, \Lambda)(\boldsymbol{0}, \mathrm{Id}) = (\boldsymbol{v} + \Lambda\boldsymbol{0}, \Lambda\,\mathrm{Id}) = (\boldsymbol{v}, \Lambda)$. So $(\boldsymbol{0}, \mathrm{Id})$ is the identity.
>
> *Inverse.* Seek $(\boldsymbol{w}, \Sigma)$ with $(\boldsymbol{v}, \Lambda)(\boldsymbol{w}, \Sigma) = (\boldsymbol{0}, \mathrm{Id})$. The group law gives $(\boldsymbol{v} + \Lambda\boldsymbol{w}, \Lambda\Sigma) = (\boldsymbol{0}, \mathrm{Id})$, so $\Lambda\Sigma = \mathrm{Id} \Rightarrow \Sigma = \Lambda^{-1}$, and $\boldsymbol{v} + \Lambda\boldsymbol{w} = \boldsymbol{0} \Rightarrow \boldsymbol{w} = -\Lambda^{-1}\boldsymbol{v}$. Hence
> $$(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v},\; \Lambda^{-1}).$$
> Note the inverse translation is $-\Lambda^{-1}\boldsymbol{v}$, *not* $-\boldsymbol{v}$ — the semidirect twist appears again. One checks the left inverse agrees: $(-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})(\boldsymbol{v}, \Lambda) = (-\Lambda^{-1}\boldsymbol{v} + \Lambda^{-1}\boldsymbol{v}, \Lambda^{-1}\Lambda) = (\boldsymbol{0}, \mathrm{Id})$.

**Step 4: Associativity.**

> [!note]- Derivation
> Compute $\big[(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2)\big](\boldsymbol{v}_3, \Lambda_3)$ two ways. Grouping left:
> $$(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2,\; \Lambda_1\Lambda_2)(\boldsymbol{v}_3, \Lambda_3) = \big(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2 + \Lambda_1\Lambda_2\boldsymbol{v}_3,\; \Lambda_1\Lambda_2\Lambda_3\big).$$
> Grouping right:
> $$(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2 + \Lambda_2\boldsymbol{v}_3,\; \Lambda_2\Lambda_3) = \big(\boldsymbol{v}_1 + \Lambda_1(\boldsymbol{v}_2 + \Lambda_2\boldsymbol{v}_3),\; \Lambda_1\Lambda_2\Lambda_3\big) = \big(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2 + \Lambda_1\Lambda_2\boldsymbol{v}_3,\; \Lambda_1\Lambda_2\Lambda_3\big).$$
> The two agree (using linearity of $\Lambda_1$ in the right grouping and associativity of Lorentz matrix multiplication), so the group law is associative. Together with the identity and inverses, this confirms the Poincaré transformations form a group.

> [!note]- Complete formal solution
> Applying $f_2 = (\boldsymbol{v}_2, \Lambda_2)$ then $f_1 = (\boldsymbol{v}_1, \Lambda_1)$ to an event $M$: $\overrightarrow{O\,f_2(M)} = \Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2$, then $\overrightarrow{O\,(f_1\circ f_2)(M)} = \Lambda_1(\Lambda_2\overrightarrow{OM} + \boldsymbol{v}_2) + \boldsymbol{v}_1 = \Lambda_1\Lambda_2\overrightarrow{OM} + (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2)$, so $f_1\circ f_2 = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$. The factor $\Lambda_1$ multiplies $\boldsymbol{v}_2$ because the outer transformation's linear part acts on the entire displacement produced by the inner one, including its translation. The identity is $(\boldsymbol{0}, \mathrm{Id})$; from $(\boldsymbol{v} + \Lambda\boldsymbol{w}, \Lambda\Sigma) = (\boldsymbol{0}, \mathrm{Id})$ the inverse is $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$. Associativity holds since both groupings give $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2 + \Lambda_1\Lambda_2\boldsymbol{v}_3, \Lambda_1\Lambda_2\Lambda_3)$. Hence the Poincaré transformations form a group with the semidirect law. $\blacksquare$

---

# Key Takeaways

**The semidirect law comes from "the outer linear part acts on the inner translation" — track what acts on what.** The entire derivation hinges on one observation: when you compose $f_1\circ f_2$, the Lorentz part $\Lambda_1$ of the *outer* (later-applied) transformation acts on the whole displacement built by the *inner* (earlier) one, which already includes $f_2$'s translation $\boldsymbol{v}_2$. That is why $\boldsymbol{v}_2$ gets rotated to $\Lambda_1\boldsymbol{v}_2$ while $\boldsymbol{v}_1$ is added bare. The transferable diagnostic, whenever you compose affine or "group element acting on a translation" structures, is to ask which linear parts have already acted by the time each translation is applied — the answer dictates which translations get rotated. This pattern recurs in every semidirect product (the Euclidean group, gauge transformations, frame bundles) and in the composition of any "rotation-then-shift" operations.

**The inverse translation is $-\Lambda^{-1}\boldsymbol{v}$, not $-\boldsymbol{v}$ — the twist propagates everywhere.** A reader who internalises only "to invert, negate the translation" will get the inverse wrong. The semidirect structure forces $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$: you must un-rotate the translation by $\Lambda^{-1}$ before negating it, because the inverse Lorentz transformation re-expresses the shift in the original axes. The same twist appears in conjugation (which sends a translation $\boldsymbol{v}$ to $\Lambda\boldsymbol{v}$, the calculation behind normality) and in the composition law itself. The lesson: in a semidirect product, *every* formula that involves both factors carries a stray Lorentz matrix, and forgetting it is the characteristic error. Whenever you write a Poincaré inverse, product, or conjugate, expect a $\Lambda$ on the translation.

**Verifying the group axioms is the same one substitution, reused.** Associativity, the identity, and the inverse all fall out of substituting into the single formula $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ — there is no separate machinery for each. This is the general shape of "prove a presented set with a given law is a group": one computes the product, then checks identity, inverse, and associativity by direct substitution, and the work is mechanical once the law is in hand. The reusable habit is to treat the composition law as the master object and derive every structural property from it, rather than re-deriving from the action each time. For the Poincaré group this master law is the gateway to everything in §12.2 — normality of the translations, the failure of the direct-product structure, and (by differentiation) the Lie bracket all start here.
