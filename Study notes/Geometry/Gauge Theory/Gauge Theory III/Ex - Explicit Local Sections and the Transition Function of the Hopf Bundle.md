---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - The Hopf Bundle"
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - The Hopf Map"
  - "Def - Principal G-Bundle"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $S^3 = \{(w_1, w_2) \in \mathbb{C}^2 : |w_1|^2 + |w_2|^2 = 1\}$ be the unit three-sphere, on which the circle group $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ acts on the right by simultaneous scalar multiplication, $(w_1, w_2) \cdot \lambda = (w_1 \lambda, w_2 \lambda)$. The **Hopf bundle** is the principal $U(1)$-bundle whose projection is the **Hopf map**
$$\operatorname{Hopf} : S^3 \longrightarrow S^2 \subset \mathbb{C} \times \mathbb{R}, \qquad \operatorname{Hopf}(w_1, w_2) = \frac{\big(4 w_1 \overline{w_2},\; 4|w_2|^2 - |w_1|^2\big)}{4|w_2|^2 + |w_1|^2},$$
where the target is the two-sphere $S^2 = \{(z, t) \in \mathbb{C} \times \mathbb{R} : |z|^2 + t^2 = 1\}$ and $\overline{w_2}$ is the complex conjugate. Cover $S^2$ by the two open sets
$$U_1 = S^2 \setminus \{(0, -1)\} \quad (\text{all of } S^2 \text{ except the south pole}), \qquad U_2 = S^2 \setminus \{(0, 1)\} \quad (\text{except the north pole}),$$
with overlap $U_{12} = U_1 \cap U_2 = S^2 \setminus \{(0, 1), (0, -1)\} = \{(z, t) \in S^2 : z \neq 0\}$. Consider the two candidate maps
$$s_1(z, t) = \left(\frac{4|z|^2}{(1+t)^2} + 1\right)^{-1/2} \left(\frac{2z}{1+t},\; 1\right) \quad \text{on } U_1, \qquad s_2(z, t) = \left(1 + \frac{|z|^2/4}{(1-t)^2}\right)^{-1/2} \left(1,\; \frac{\overline{z}/2}{1-t}\right) \quad \text{on } U_2.$$

**Prove the following.**

1. **(Sections.)** Each of $s_1$ and $s_2$ takes values in $S^3$ (its norm is one) and is a section of the Hopf bundle over its domain, meaning $\operatorname{Hopf} \circ s_1 = \operatorname{id}_{U_1}$ and $\operatorname{Hopf} \circ s_2 = \operatorname{id}_{U_2}$.
2. **(Transition function.)** Compute the transition function $g_{12} : U_{12} \to U(1)$ determined by $s_2 = s_1 \cdot g_{12}$, and show that
$$g_{12}(z, t) = \frac{\overline{z}}{|z|} = \frac{|z|}{z}.$$
3. **(Cocycle check.)** Verify that $g_{12}$ and its partner $g_{21}(z, t) = z/|z|$ satisfy the cocycle relation $g_{12} \, g_{21} = 1$ on $U_{12}$.

Throughout, the only geometric input needed beyond algebra is the sphere constraint $|z|^2 + t^2 = 1$, which we use in the equivalent form $(1 - t)(1 + t) = 1 - t^2 = |z|^2$.

> [!warning] Source correction (Bär, Example 2.2.17)
> Bär's printed second section reads $s_2(z, t) = \big(1 + \tfrac{|z|^2/4}{(1-t)^2}\big)^{-1/2}\big(1, \tfrac{z/2}{1-t}\big)$ — with $z$, not $\overline{z}$, in the last slot. With that unconjugated slot the map lands in the *wrong fibre*: one computes $\operatorname{Hopf}(s_2^{\text{printed}}(z, t)) = (\overline{z}, t)$, not $(z, t)$, so it is not a section over $U_2$. The conjugate $\overline{z}$ is forced by the requirement that $\operatorname{Hopf}$ carry $s_2$ back to the point $(z, t)$; we prove this below and use the corrected form $s_2(z,t) = d\,(1, \tfrac{\overline{z}/2}{1-t})$ throughout. Correspondingly the transition function for the convention $s_2 = s_1 g_{12}$ is $g_{12} = |z|/z = \overline{z}/|z|$; the value $z/|z|$ that Bär records is the *inverse cocycle* $g_{21} = g_{12}^{-1}$. The bundle is unaffected: $\{g_{12}\}$ and $\{g_{21}\}$ define the same Hopf bundle up to isomorphism, differing only by the relabelling that swaps the two charts. See Step 3 for the full accounting.

**Recall:**

The objects in play are the Hopf bundle as a principal $U(1)$-bundle, the Hopf map itself, and the notion of a local section and its transition function.

![[Def - The Hopf Bundle#The Definition]]

The [[Def - The Hopf Bundle|Hopf bundle]] is the principal $U(1)$-bundle $\operatorname{Hopf} : S^3 \to S^2$; its fibres are exactly the $U(1)$-orbits $\{(w_1 \lambda, w_2 \lambda) : |\lambda| = 1\}$, the great circles of $S^3$. That the fibres are the orbits is what makes $\operatorname{Hopf}$ a principal-bundle projection, and it is why the Hopf map must be invariant under the right action: replacing $(w_1, w_2)$ by $(w_1 \lambda, w_2 \lambda)$ multiplies $w_1 \overline{w_2}$ by $\lambda \overline{\lambda} = |\lambda|^2 = 1$ and leaves $|w_1|^2, |w_2|^2$ unchanged, so $\operatorname{Hopf}$ is constant on orbits — this is precisely why the conjugate appears on $w_2$.

![[Def - The Hopf Map#The Definition]]

![[Def - Transition Functions and the Cocycle Condition#The Definition]]

A [[Def - Transition Functions and the Cocycle Condition|transition function]] is defined as follows. Given local sections $s_\alpha : U_\alpha \to P|_{U_\alpha}$ of a principal $G$-bundle over an open cover $\{U_\alpha\}$, on each overlap $U_{\alpha\beta}$ the freeness of the right $G$-action produces a *unique* smooth map $g_{\alpha\beta} : U_{\alpha\beta} \to G$ with
$$s_\beta(x) = s_\alpha(x) \cdot g_{\alpha\beta}(x) \qquad \text{for all } x \in U_{\alpha\beta}.$$
Uniqueness is exactly the statement that the action is free: if $s_\alpha g = s_\alpha g'$ then $g = g'$. These maps satisfy the cocycle conditions $g_{\alpha\alpha} = e$, $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$, and $g_{\alpha\beta} g_{\beta\gamma} g_{\gamma\alpha} = e$. Here $G = U(1)$ is abelian and written multiplicatively as unit complex numbers, so the group operation is complex multiplication, the identity is $1$, and $g^{-1} = \overline{g}$ for $g \in U(1)$.

A [[Def - Principal G-Bundle|local section]] over $U \subseteq S^2$ is a smooth map $s : U \to S^3$ with $\operatorname{Hopf} \circ s = \operatorname{id}_U$: it picks, smoothly in $x \in U$, one point $s(x)$ out of the fibre $\operatorname{Hopf}^{-1}(x)$. That the Hopf bundle admits the two local sections $s_1, s_2$ but *no* global section is the reason it is a non-trivial bundle; see [[Ex - The Hopf Map is a Submersion|the submersion property of the Hopf map]] for why the fibres are smooth circles in the first place.

---

# Convergent Strategy

**Problem class.** This is a *verify-and-compute* problem of the standard "local trivialisation" kind: given explicit formulas for local sections of a principal bundle, first confirm they *are* sections, then extract the group-valued transition function that glues the two trivialisations. It is the concrete engine behind the cocycle description of bundles — the transition function $g_{12}$ we compute here is the single datum from which the entire Hopf bundle is reconstructed as $\bigsqcup_\alpha U_\alpha \times U(1) / \sim$, and its non-triviality (it winds once around the equator) is what forces the bundle to be non-trivial. The whole calculation is algebra driven by one geometric constraint, $|z|^2 + t^2 = 1$.

**Assumption pattern.** Every step uses the sphere constraint in exactly one form: $(1 - t)(1 + t) = 1 - t^2 = |z|^2$. This is the recognisable trigger — whenever a denominator $(1 + t)^2 + |z|^2$ or $(1 \pm t)$ appears, it is there to be collapsed by $|z|^2 = 1 - t^2$. The normalising prefactors of $s_1$ and $s_2$ are *engineered* to be the reciprocals of the Euclidean norms of the bracketed vectors, so "norm one" is automatic algebra that needs no constraint; the constraint enters only in checking that $\operatorname{Hopf}$ returns the base point. The second recognisable pattern is that the $U(1)$-action multiplies *both* complex coordinates by the *same* unit scalar $\lambda$ — the single most common slip in this computation is to apply different phases to the two slots, and guarding against it is the heart of part 2.

**Theorem routing.** The route is: (i) compute $|s_i|^2$ directly from the definition of the normalising constant, getting $1$ with no constraint; (ii) substitute $s_1, s_2$ into $\operatorname{Hopf}$ and simplify each of the two output coordinates using $(1 - t)(1 + t) = |z|^2$, obtaining $(z, t)$ — this uses the invariance-forcing conjugate $\overline{w_2}$ in the Hopf map, and is exactly where the conjugate in $s_2$ becomes necessary; (iii) solve $s_1 \cdot g_{12} = s_2$ for the *single* scalar $g_{12}$ by reading it off the second coordinate, where $s_1$ has the real entry $1$, so $g_{12}$ is simply the second coordinate of $s_2$ divided by the normalising ratio; (iv) confirm the first coordinate is consistent, which is where the constraint reappears; (v) check $|g_{12}| = 1$ and the cocycle relation. The uniqueness clause of [[Def - Transition Functions and the Cocycle Condition|the transition-function definition]] guarantees there is only one such $g_{12}$, so any consistent value we find is *the* answer.

**Key decision point.** The one genuinely non-obvious move is recognising that a *single* unit scalar $\lambda = g_{12}(z,t)$ must convert $s_1$ into $s_2$, and that this scalar is over-determined: it must simultaneously satisfy $(s_1)_1 \lambda = (s_2)_1$ and $(s_1)_2 \lambda = (s_2)_2$. Reading it off the *second* coordinate is easiest because $(s_1)_2 = (\text{prefactor}) \cdot 1$ is essentially real; the first coordinate then furnishes an independent consistency check that the constraint $|z|^2 = (1-t)(1+t)$ makes work out. It is precisely this over-determination that exposes Bär's misprint: with his unconjugated $s_2$ the two coordinates demand *different* phases ($z/|z|$ from one, $|z|/z$ from the other), an impossibility for a group action, which is the fingerprint of the conjugation error.

---

# Legal Operations Used

This solution deploys the following operations, keyed to the transition-function machinery on [[Def - Transition Functions and the Cocycle Condition|the topic page's Legal Operations]] (numbers to be reconciled by the topic page).

1. **Verify a candidate map is a section by post-composing with the projection.** To show $s : U \to S^3$ is a section, one checks the two things a section must satisfy: it lands in the total space ($|s|^2 = 1$, so $s(x) \in S^3$), and $\operatorname{Hopf} \circ s = \operatorname{id}_U$. Both are verified by direct substitution.

2. **Collapse a sphere denominator with the defining constraint.** Every occurrence of $(1 + t)^2 + |z|^2$ or $1 + 2t + t^2 + |z|^2$ is rewritten using $|z|^2 = 1 - t^2$, turning it into $2(1 + t)$ (and likewise $(1-t)^2 + |z|^2 = 2(1 - t)$). This is the single algebraic lever of the whole page.

3. **Extract the transition function from the second coordinate.** In the defining relation $s_2 = s_1 \cdot g_{12}$, read $g_{12}$ off the coordinate in which $s_1$ has the simplest (real, positive-multiple-of-one) entry, then verify the other coordinate is consistent. This uses operation "read off a free-action element" from the topic page: the value is unique because the $U(1)$-action is free.

4. **Confirm consistency across both coordinates as an over-determination check.** Because a single $\lambda \in U(1)$ must act on both slots, computing $\lambda$ from each slot and demanding equality is both a consistency check and the mechanism that detects a conjugation error.

5. **Use $g^{-1} = \overline{g}$ in $U(1)$ and the cocycle relation $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$.** In the abelian group $U(1)$ the inverse is complex conjugation, so the second cocycle identity reads $g_{21} = \overline{g_{12}}$; this delivers $g_{21} = z/|z|$ from $g_{12} = \overline{z}/|z|$ and gives the cocycle check for free.

---

# Hints

> [!note]- Hint 1
> "Norm one" is easier than it looks: the prefactor of each $s_i$ is defined as $(\text{sum of squared moduli of the bracketed entries})^{-1/2}$. So $|s_i|^2$ is that prefactor squared times that same sum — it collapses to $1$ by construction, with no need for the sphere constraint. Save the constraint $|z|^2 + t^2 = 1$ for the harder half: checking $\operatorname{Hopf}(s_i) = (z, t)$.

> [!note]- Hint 2
> To check $\operatorname{Hopf}(s_1(z,t)) = (z,t)$, write $s_1 = c\,(2z/(1+t),\, 1)$ with $c = (4|z|^2/(1+t)^2 + 1)^{-1/2}$, so $w_1 = 2cz/(1+t)$ and $w_2 = c$. Substitute into $\operatorname{Hopf}$. The factors of $c^2$ cancel between numerator and denominator. In the denominator you will meet $(1 + t)^2 + |z|^2$; expand it as $1 + 2t + t^2 + |z|^2$ and use $t^2 + |z|^2 = 1$ to get $2(1 + t)$.

> [!note]- Hint 3
> For $s_2$, the second complex coordinate is $\overline{z}/2 \big/ (1 - t)$ — with a *conjugate*. Check what $\operatorname{Hopf}$ does to $s_2$ and watch how the conjugate in the Hopf map's first slot, $4 w_1 \overline{w_2}$, combines with the conjugate in $w_2$ to produce $z$ (not $\overline{z}$). If you drop the conjugate in $s_2$, you will land on $\overline{z}$ instead — that is the misprint.

> [!note]- Hint 4
> For the transition function, you want the *single* unit scalar $\lambda$ with $s_1 \lambda = s_2$. Read it from the second coordinate: $(s_1)_2 = c$ is real and positive, so $\lambda = (s_2)_2 / c$ up to the ratio of prefactors; its phase is the phase of $(s_2)_2 = d\,\overline{z}/2/(1-t)$, namely the phase of $\overline{z}$, i.e. $\overline{z}/|z|$. Since $|\lambda| = 1$ automatically (both sections have norm one), conclude $\lambda = \overline{z}/|z| = |z|/z$. Then verify the first coordinate is consistent using $|z|^2 = (1-t)(1+t)$.

---

# Solution

The plan is to treat each claim by direct substitution, letting one algebraic identity do all the work. First we confirm the two prefactors are exactly the reciprocal norms, so both maps land on $S^3$ automatically. Then we push $s_1$ and $s_2$ through the Hopf map, and in each case the constraint $(1 - t)(1 + t) = |z|^2$ collapses the denominator $(1 \pm t)^2 + |z|^2$ to $2(1 \pm t)$, returning the base point $(z, t)$. Finally we solve $s_2 = s_1 g_{12}$ for the unique unit scalar $g_{12}$; reading it off the near-real second coordinate gives $g_{12} = \overline{z}/|z|$, the first coordinate confirms it, and the cocycle identity $g_{21} = \overline{g_{12}}$ closes the problem.

Throughout write $c(z, t) = \big(\tfrac{4|z|^2}{(1+t)^2} + 1\big)^{-1/2}$ and $d(z, t) = \big(1 + \tfrac{|z|^2/4}{(1-t)^2}\big)^{-1/2}$ for the two prefactors, both real and positive on their domains.

**Step 1: Both sections have norm one, so they map into $S^3$.**

For each $i$, the prefactor is the reciprocal of the Euclidean norm of the bracketed vector, so $|s_i|^2 = 1$; no constraint is needed.

> [!note]- Derivation
> **The prefactor cancels the norm.** For $s_1$, the bracketed vector is $v_1 = \big(\tfrac{2z}{1+t}, 1\big) \in \mathbb{C}^2$, whose squared Euclidean norm is
> $$|v_1|^2 = \left|\frac{2z}{1+t}\right|^2 + |1|^2 = \frac{4|z|^2}{(1+t)^2} + 1 \qquad (\text{definition of the Hermitian norm on } \mathbb{C}^2).$$
> By the definition of $c$, this is exactly $c^{-2}$. Therefore
> $$|s_1|^2 = |c\, v_1|^2 = c^2 |v_1|^2 = c^2 \cdot c^{-2} = 1 \qquad (\text{since } c > 0 \text{ is real, } |c v_1|^2 = c^2 |v_1|^2).$$
> Hence $s_1(z, t) \in S^3$ for every $(z, t) \in U_1$.
>
> **The same for $s_2$.** The bracketed vector is $v_2 = \big(1, \tfrac{\overline{z}/2}{1-t}\big)$, with
> $$|v_2|^2 = 1 + \left|\frac{\overline{z}/2}{1-t}\right|^2 = 1 + \frac{|z|^2/4}{(1-t)^2} \qquad (\text{since } |\overline{z}| = |z|),$$
> which is exactly $d^{-2}$. Thus $|s_2|^2 = d^2 |v_2|^2 = 1$, and $s_2(z, t) \in S^3$ for every $(z, t) \in U_2$. Smoothness of both maps is clear from the formulas: on $U_1$ we have $1 + t > 0$ so no denominator vanishes, and the prefactor is a smooth positive function; on $U_2$ we have $1 - t > 0$ likewise.

**Step 2: Each section is carried by the Hopf map to its base point.**

Substituting $s_1$ and (the corrected) $s_2$ into $\operatorname{Hopf}$ returns $(z, t)$, using $(1 - t)(1 + t) = |z|^2$.

> [!note]- Derivation
> **Compute $\operatorname{Hopf}(s_1)$.** Write $s_1 = (w_1, w_2)$ with $w_1 = \tfrac{2cz}{1+t}$ and $w_2 = c$ (real). Then $\overline{w_2} = c$ and
> $$4 w_1 \overline{w_2} = 4 \cdot \frac{2cz}{1+t} \cdot c = \frac{8 c^2 z}{1+t} \qquad (\text{multiplying}),$$
> $$4 |w_2|^2 = 4 c^2, \qquad |w_1|^2 = \frac{4 c^2 |z|^2}{(1+t)^2} \qquad (\text{squaring moduli}).$$
> The common Hopf denominator is
> $$4|w_2|^2 + |w_1|^2 = 4 c^2 + \frac{4 c^2 |z|^2}{(1+t)^2} = \frac{4 c^2 \big[(1+t)^2 + |z|^2\big]}{(1+t)^2} \qquad (\text{common denominator } (1+t)^2).$$
> **First output coordinate.** Dividing,
> $$\frac{4 w_1 \overline{w_2}}{4|w_2|^2 + |w_1|^2} = \frac{8 c^2 z/(1+t)}{4 c^2\big[(1+t)^2 + |z|^2\big]/(1+t)^2} = \frac{2 z (1+t)}{(1+t)^2 + |z|^2} \qquad (c^2 \text{ cancels; one factor } (1+t) \text{ cancels}).$$
> Now collapse the denominator with the constraint: $(1+t)^2 + |z|^2 = 1 + 2t + t^2 + |z|^2 = 2 + 2t = 2(1 + t)$, using $t^2 + |z|^2 = 1$. Hence
> $$\frac{2 z (1+t)}{2(1+t)} = z \qquad (\text{cancel } 2(1+t)).$$
> **Second output coordinate.**
> $$\frac{4|w_2|^2 - |w_1|^2}{4|w_2|^2 + |w_1|^2} = \frac{4 c^2 - 4 c^2 |z|^2/(1+t)^2}{4 c^2\big[(1+t)^2 + |z|^2\big]/(1+t)^2} = \frac{(1+t)^2 - |z|^2}{(1+t)^2 + |z|^2} \qquad (c^2 \text{ and } (1+t)^{-2} \text{ cancel}).$$
> The numerator collapses too: $(1+t)^2 - |z|^2 = 1 + 2t + t^2 - |z|^2 = 1 + 2t + t^2 - (1 - t^2) = 2t + 2t^2 = 2t(1 + t)$, again by $|z|^2 = 1 - t^2$. With the denominator $2(1+t)$ from above,
> $$\frac{2t(1+t)}{2(1+t)} = t \qquad (\text{cancel } 2(1+t)).$$
> Therefore $\operatorname{Hopf}(s_1(z, t)) = (z, t)$, so $s_1$ is a section over $U_1$.
>
> **Compute $\operatorname{Hopf}(s_2)$ (the conjugate is essential).** Write $s_2 = (w_1, w_2)$ with $w_1 = d$ (real) and $w_2 = d \cdot \tfrac{\overline{z}/2}{1-t}$, so $\overline{w_2} = d \cdot \tfrac{z/2}{1-t}$. Then
> $$4 w_1 \overline{w_2} = 4 d \cdot d \frac{z/2}{1-t} = \frac{2 d^2 z}{1-t} \qquad (\text{here the conjugate on } w_2 \text{ turns } \overline{z} \text{ back into } z),$$
> $$4|w_2|^2 = 4 d^2 \frac{|z|^2/4}{(1-t)^2} = \frac{d^2 |z|^2}{(1-t)^2}, \qquad |w_1|^2 = d^2 \qquad (\text{squaring moduli}).$$
> The denominator is $4|w_2|^2 + |w_1|^2 = d^2\big[\tfrac{|z|^2}{(1-t)^2} + 1\big] = \tfrac{d^2\,[\,|z|^2 + (1-t)^2\,]}{(1-t)^2}$, and $|z|^2 + (1-t)^2 = (1 - t^2) + 1 - 2t + t^2 = 2 - 2t = 2(1 - t)$ by the constraint, so the denominator equals $\tfrac{2 d^2}{1 - t}$. **First output coordinate:**
> $$\frac{4 w_1 \overline{w_2}}{4|w_2|^2 + |w_1|^2} = \frac{2 d^2 z/(1-t)}{2 d^2/(1-t)} = z \qquad (d^2 \text{ and } (1-t)^{-1} \text{ cancel}).$$
> **Second output coordinate:**
> $$\frac{4|w_2|^2 - |w_1|^2}{4|w_2|^2 + |w_1|^2} = \frac{d^2 |z|^2/(1-t)^2 - d^2}{2 d^2/(1-t)} = \frac{|z|^2 - (1-t)^2}{2(1-t)} \qquad (d^2 \text{ cancels; multiply num. and den. by } (1-t)^2 \big/ (1-t)^2 ),$$
> and $|z|^2 - (1-t)^2 = (1 - t^2) - 1 + 2t - t^2 = 2t - 2t^2 = 2t(1 - t)$, so this is $\tfrac{2t(1-t)}{2(1-t)} = t$. Therefore $\operatorname{Hopf}(s_2(z,t)) = (z, t)$, and $s_2$ is a section over $U_2$.

> [!warning] Why the conjugate is not optional
> Repeat the second computation with Bär's *printed* $s_2^{\text{printed}} = d\,(1, \tfrac{z/2}{1-t})$, i.e. $w_2 = d \tfrac{z/2}{1-t}$, so $\overline{w_2} = d \tfrac{\overline{z}/2}{1-t}$. Then $4 w_1 \overline{w_2} = \tfrac{2 d^2 \overline{z}}{1-t}$, and the *same* denominator $\tfrac{2d^2}{1-t}$ gives first coordinate $\overline{z}$, not $z$. Concretely at $(z, t) = (i, 0)$: $s_2^{\text{printed}}(i, 0) = \tfrac{2}{\sqrt 5}(1, i/2) = \tfrac{1}{\sqrt 5}(2, i)$, and $\operatorname{Hopf}\big(\tfrac{1}{\sqrt5}(2, i)\big)$ has first coordinate $\tfrac{4 \cdot \tfrac{2}{\sqrt5}\cdot\overline{(i/\sqrt5)}}{\cdots} = \tfrac{4\cdot\frac{2}{\sqrt5}\cdot\frac{-i}{\sqrt5}}{8/5} = -i = \overline{i}$. So the printed section sits over $(\,\overline{z}, t) = (-i, 0)$, the wrong point. The corrected $s_2(i,0) = \tfrac{1}{\sqrt5}(2, -i)$ lies over $(i, 0)$, as required. This is why we use $\overline{z}$.

**Step 3: The transition function is $g_{12}(z, t) = \overline{z}/|z| = |z|/z$.**

Solving $s_2 = s_1 \cdot g_{12}$ for the unique unit scalar $g_{12}$ gives $g_{12} = \overline{z}/|z|$; the value $z/|z|$ is its inverse $g_{21}$.

> [!note]- Derivation
> **Set up the defining relation.** By [[Def - Transition Functions and the Cocycle Condition|the definition]], on $U_{12} = \{z \neq 0\}$ there is a unique $g_{12}(z,t) \in U(1)$ with
> $$s_2(z, t) = s_1(z, t) \cdot g_{12}(z, t), \qquad \text{i.e.} \qquad d\left(1, \frac{\overline{z}/2}{1-t}\right) = c\left(\frac{2z}{1+t}, 1\right) g_{12} \qquad (\text{action multiplies both slots by the same } g_{12}).$$
> Uniqueness holds because the $U(1)$-action is free: if $s_1 g = s_1 g'$ then $g = g'$.
>
> **Read $g_{12}$ off the second coordinate.** Equating the second components,
> $$d \cdot \frac{\overline{z}/2}{1-t} = c \cdot 1 \cdot g_{12} \quad\Longrightarrow\quad g_{12} = \frac{d}{c} \cdot \frac{\overline{z}/2}{1-t} \qquad (\text{divide by } c > 0).$$
> Since $d, c, (1 - t)$ are real and positive, the phase (argument) of $g_{12}$ equals the phase of $\overline{z}$, namely $\overline{z}/|z|$. Because both $s_1$ and $s_2$ have norm one and $g_{12} \in U(1)$ is forced to have modulus one (the action preserves norm), we conclude
> $$g_{12}(z, t) = \frac{\overline{z}}{|z|}.$$
> Using $|z|^2 = z \overline{z}$, this is the same as $\overline{z}/|z| = \overline{z}\, z / (|z|\, z) = |z|^2/(|z| z) = |z|/z$, so equivalently $g_{12} = |z|/z$.
>
> **Confirm consistency on the first coordinate.** Equating first components requires $d = c \cdot \tfrac{2z}{1+t} \cdot g_{12}$. Substituting $g_{12} = \overline{z}/|z|$,
> $$c \cdot \frac{2z}{1+t} \cdot \frac{\overline{z}}{|z|} = c \cdot \frac{2 |z|^2}{(1+t)|z|} = c \cdot \frac{2|z|}{1+t} \qquad (z \overline{z} = |z|^2).$$
> It remains to check $c \cdot \tfrac{2|z|}{1+t} = d$. Squaring and comparing, this is
> $$\frac{4|z|^2}{(1+t)^2}\Big/\Big(\frac{4|z|^2}{(1+t)^2} + 1\Big) \;\overset{?}{=}\; 1\Big/\Big(1 + \frac{|z|^2/4}{(1-t)^2}\Big),$$
> i.e. $\dfrac{4|z|^2}{4|z|^2 + (1+t)^2} = \dfrac{(1-t)^2}{(1-t)^2 + |z|^2/4}$. Clear denominators using $|z|^2 = (1-t)(1+t)$: on the left, $4|z|^2 + (1+t)^2 = 4(1-t)(1+t) + (1+t)^2 = (1+t)(5 - 3t)$, so the left side is $\tfrac{4(1-t)(1+t)}{(1+t)(5-3t)} = \tfrac{4(1-t)}{5-3t}$; on the right, $(1-t)^2 + |z|^2/4 = (1-t)^2 + (1-t)(1+t)/4 = (1-t)\tfrac{5-3t}{4}$, so the right side is $\tfrac{(1-t)^2}{(1-t)(5-3t)/4} = \tfrac{4(1-t)}{5-3t}$. The two sides agree, so $c \tfrac{2|z|}{1+t} = d$ (both positive), and the first coordinate is consistent. Hence $g_{12} = \overline{z}/|z|$ is the transition function.

> [!warning] Bär's displayed computation and the two-phase slip
> Bär computes $s_1 \cdot \tfrac{z}{|z|}$ and reports it equals $s_2$, concluding $g_{12} = z/|z|$. His displayed intermediate vector is $c\big(\tfrac{2|z|}{1+t}, \tfrac{z}{|z|}\big)$. But look at the two slots: the first slot $\tfrac{2z}{1+t} \mapsto \tfrac{2|z|}{1+t}$ requires *multiplying by $\overline{z}/|z|$* (since $\tfrac{2z}{1+t}\cdot\tfrac{\overline{z}}{|z|} = \tfrac{2|z|}{1+t}$), while the second slot $1 \mapsto \tfrac{z}{|z|}$ requires *multiplying by $z/|z|$*. A right $U(1)$-action multiplies both slots by the *same* scalar, so these two phases must coincide — and they do not (unless $z$ is real positive). The consistent common factor is $\lambda = \overline{z}/|z| = |z|/z$, which is what produces the corrected $s_2 = d(1, \tfrac{\overline{z}/2}{1-t})$ and the transition $g_{12} = |z|/z$. The value $z/|z|$ that Bär also records, and that the coordinator's content map adopts, is the inverse cocycle $g_{21} = g_{12}^{-1}$; see the next step.

**Step 4: Cocycle check, $g_{12} \, g_{21} = 1$.**

The partner transition function is $g_{21} = z/|z|$, and $g_{12} g_{21} = 1$ on $U_{12}$, as the cocycle conditions require.

> [!note]- Derivation
> By the second cocycle identity, $g_{21} = g_{12}^{-1}$. In the abelian group $U(1)$, the inverse of a unit complex number is its conjugate, so
> $$g_{21} = \overline{g_{12}} = \overline{\left(\frac{\overline{z}}{|z|}\right)} = \frac{z}{|z|} \qquad (\text{conjugation is the inverse in } U(1);\ \overline{\overline{z}} = z,\ |z| \text{ real}).$$
> Then directly
> $$g_{12}(z, t)\, g_{21}(z, t) = \frac{\overline{z}}{|z|} \cdot \frac{z}{|z|} = \frac{z \overline{z}}{|z|^2} = \frac{|z|^2}{|z|^2} = 1 \qquad (z\overline{z} = |z|^2),$$
> valid for every $(z, t) \in U_{12}$, where $z \neq 0$. This is the two-chart instance of the cocycle relation $g_{\alpha\beta} g_{\beta\alpha} = e$; the third condition $g_{\alpha\beta} g_{\beta\gamma} g_{\gamma\alpha} = e$ is vacuous here as there is no third chart on the two-set cover.

> [!note]- Complete formal solution
> **Claim.** With $s_1(z,t) = c\,(\tfrac{2z}{1+t}, 1)$ on $U_1 = S^2 \setminus\{(0,-1)\}$ and $s_2(z,t) = d\,(1, \tfrac{\overline{z}/2}{1-t})$ on $U_2 = S^2 \setminus\{(0,1)\}$, where $c = (\tfrac{4|z|^2}{(1+t)^2}+1)^{-1/2}$ and $d = (1 + \tfrac{|z|^2/4}{(1-t)^2})^{-1/2}$: both are smooth local sections of the Hopf bundle, and the transition function $s_2 = s_1 g_{12}$ is $g_{12}(z,t) = \overline{z}/|z| = |z|/z$, with $g_{21} = z/|z|$ and $g_{12} g_{21} = 1$.
>
> *Proof.* We use throughout the sphere constraint $|z|^2 + t^2 = 1$, equivalently $(1-t)(1+t) = |z|^2$.
>
> **Norm one.** The bracketed vectors are $v_1 = (\tfrac{2z}{1+t}, 1)$ and $v_2 = (1, \tfrac{\overline{z}/2}{1-t})$, with $|v_1|^2 = \tfrac{4|z|^2}{(1+t)^2}+1 = c^{-2}$ and $|v_2|^2 = 1 + \tfrac{|z|^2/4}{(1-t)^2} = d^{-2}$ (using $|\overline{z}| = |z|$). Hence $|s_1|^2 = c^2 c^{-2} = 1$ and $|s_2|^2 = d^2 d^{-2} = 1$, so $s_1(U_1), s_2(U_2) \subset S^3$. Both maps are smooth because $1 + t > 0$ on $U_1$ and $1 - t > 0$ on $U_2$, so no denominator vanishes.
>
> **Sections.** Writing $s_1 = (w_1, w_2) = (\tfrac{2cz}{1+t}, c)$: $4 w_1 \overline{w_2} = \tfrac{8 c^2 z}{1+t}$, $4|w_2|^2 = 4c^2$, $|w_1|^2 = \tfrac{4c^2|z|^2}{(1+t)^2}$, and $4|w_2|^2 + |w_1|^2 = \tfrac{4c^2[(1+t)^2 + |z|^2]}{(1+t)^2}$. Since $(1+t)^2 + |z|^2 = 1 + 2t + t^2 + |z|^2 = 2(1+t)$, the first Hopf coordinate is $\tfrac{8c^2 z/(1+t)}{4c^2 \cdot 2(1+t)/(1+t)^2} = \tfrac{2z(1+t)}{2(1+t)} = z$, and the second is $\tfrac{4|w_2|^2 - |w_1|^2}{4|w_2|^2 + |w_1|^2} = \tfrac{(1+t)^2 - |z|^2}{(1+t)^2 + |z|^2} = \tfrac{2t(1+t)}{2(1+t)} = t$, using $(1+t)^2 - |z|^2 = 2t(1+t)$. Thus $\operatorname{Hopf}(s_1) = (z,t)$. Writing $s_2 = (d, d\tfrac{\overline{z}/2}{1-t})$, the conjugate in $4 w_1 \overline{w_2} = \tfrac{2d^2 z}{1-t}$ restores $z$; with $4|w_2|^2 + |w_1|^2 = \tfrac{d^2[|z|^2 + (1-t)^2]}{(1-t)^2} = \tfrac{2d^2}{1-t}$ (as $|z|^2 + (1-t)^2 = 2(1-t)$), the first coordinate is $z$ and the second is $\tfrac{|z|^2 - (1-t)^2}{2(1-t)} = \tfrac{2t(1-t)}{2(1-t)} = t$. Thus $\operatorname{Hopf}(s_2) = (z,t)$, and both are sections.
>
> **Transition function.** The freeness of the $U(1)$-action gives a unique $g_{12} \in U(1)$ with $s_2 = s_1 g_{12}$ on $U_{12} = \{z \neq 0\}$. The second components give $d\tfrac{\overline{z}/2}{1-t} = c\, g_{12}$, so $g_{12} = \tfrac{d}{c}\tfrac{\overline{z}/2}{1-t}$, whose phase is that of $\overline{z}$; as $|g_{12}| = 1$, we get $g_{12} = \overline{z}/|z| = |z|/z$. The first components are consistent: $c\tfrac{2z}{1+t}\cdot\tfrac{\overline{z}}{|z|} = c\tfrac{2|z|}{1+t}$, which equals $d$ because $\big(c\tfrac{2|z|}{1+t}\big)^2 = \tfrac{4|z|^2}{4|z|^2+(1+t)^2} = \tfrac{4(1-t)}{5-3t} = \tfrac{(1-t)^2}{(1-t)^2 + |z|^2/4} = d^2$ (both positive), using $|z|^2 = (1-t)(1+t)$ to simplify $4|z|^2 + (1+t)^2 = (1+t)(5-3t)$ and $(1-t)^2 + |z|^2/4 = (1-t)(5-3t)/4$.
>
> **Cocycle.** In $U(1)$, $g_{21} = g_{12}^{-1} = \overline{g_{12}} = z/|z|$, and $g_{12} g_{21} = \tfrac{\overline{z}}{|z|}\tfrac{z}{|z|} = \tfrac{|z|^2}{|z|^2} = 1$ on $U_{12}$. $\blacksquare$

> [!warning] Illegal but tempting: applying different phases to the two coordinates
> The seductive shortcut is to "simplify each coordinate of $s_1 \cdot \lambda$ separately", conjugating in one slot but not the other to make both match $s_2$. This is exactly the slip that yields the spurious $g_{12} = z/|z|$. A right $U(1)$-action is scalar multiplication by *one* $\lambda$ in *both* slots; the moment the two slots demand different phases, either the target section or the group element has been miswritten. The extra condition that would legitimise "different phases" is a *non-abelian* structure group where the two frame vectors transform by genuinely different group elements — but for the abelian $U(1)$ acting diagonally on $\mathbb{C}^2$, one scalar governs both, and the two-coordinate consistency check is mandatory.

---

# Key Takeaways

**Verifying a section is two checks, and normalising prefactors make the first one free.** A candidate map $s : U \to S^3$ is a section of the Hopf bundle precisely when it satisfies two conditions: it lands in the total space, $|s|^2 = 1$, and it is a right inverse of the projection, $\operatorname{Hopf} \circ s = \operatorname{id}_U$. The recurring design pattern — visible in both $s_1$ and $s_2$ — is that the author *defines the scalar prefactor to be the reciprocal norm of the bracketed vector*, so the first check collapses to $c^2 \cdot c^{-2} = 1$ with no geometry at all. Whenever you meet a section written as (prefactor) $\times$ (vector), test first whether the prefactor is the reciprocal norm; if so, norm-one is automatic and you can spend your effort on the second, substantive check. The transferable diagnostic: the difficulty of "is this a section?" almost always lives entirely in the projection identity, not in membership of the total space.

**A single geometric constraint, wielded in one canonical form, drives an entire trigonometric-looking computation.** Every non-trivial simplification on this page — collapsing $(1+t)^2 + |z|^2$ to $2(1+t)$, collapsing $(1-t)^2 + |z|^2$ to $2(1-t)$, turning $(1+t)^2 - |z|^2$ into $2t(1+t)$, matching the two prefactors — is a single application of $|z|^2 = 1 - t^2 = (1-t)(1+t)$. The lesson for spaced practice is to *identify the one constraint and pre-commit to its most useful algebraic form* before starting. On the sphere the useful form is the factored $(1-t)(1+t) = |z|^2$, because the denominators that appear are quadratics in $(1 \pm t)$ that this identity linearises. The same discipline recurs wherever a computation lives on a level set (a sphere, a group manifold, a constraint surface): find the constraint, write it in the form that matches the denominators you will face, and let it be the only nontrivial move. The trigger condition is "denominators built from the constraint's variables"; the reaction is "substitute the constraint to linearise them."

**The over-determination of a transition function is both how you compute it and how you catch an error.** A transition function $g_{\alpha\beta}$ is defined by a *single* group equation $s_\beta = s_\alpha g_{\alpha\beta}$, but when the sections live in a vector space this equation has one scalar unknown and several coordinate equations — it is over-determined, and consistency is guaranteed only because $s_\alpha, s_\beta$ genuinely lie in the same fibre. Exploit this twice over. To *compute* $g_{\alpha\beta}$, read it off the coordinate where $s_\alpha$ is simplest (here the second, where $s_1$ has the real entry $1$), which turns a group-inversion problem into a division. To *check* your work, verify the remaining coordinates; a mismatch is not a dead end but a signal, usually of a conjugation or an inverse-versus-element confusion. On this page the mismatch between the two coordinates is exactly what reveals Bär's misprint: the printed second section demands the phase $z/|z|$ from one slot and $|z|/z$ from the other, an impossibility for the diagonal action of the abelian group $U(1)$, which is resolved only by restoring the conjugate to $s_2$ and reading the transition as $|z|/z = \overline{z}/|z|$.

**Conjugation, invariance, and the direction of a cocycle are the same bookkeeping seen three ways.** The Hopf map must carry a conjugate on $w_2$ so that it is invariant under the diagonal $U(1)$-action $(w_1, w_2) \mapsto (w_1\lambda, w_2\lambda)$; that same conjugation propagates into the section $s_2$ (which needs $\overline{z}$, not $z$, to land in the right fibre) and into the transition function ($\overline{z}/|z|$ rather than $z/|z|$). Because $U(1)$ is abelian with $g^{-1} = \overline{g}$, swapping the roles of the two charts — computing $g_{21}$ instead of $g_{12}$ — is literally complex conjugation, so the "two answers" $z/|z|$ and $\overline{z}/|z|$ are inverse cocycles defining the *same* bundle. The transferable principle: whenever a group-valued datum appears with an ambiguous sign or conjugate, pin it down by tracking which convention (which chart is $\alpha$, which is $\beta$; is $g^{-1}$ conjugation?) you fixed, and remember that the bundle itself is invariant under the coboundary and inversion symmetries, so an inverse-labelled cocycle is not a wrong answer but a differently-labelled correct one. This transition function's single winding around the equator — $z/|z| = e^{i\theta}$ as $z = |z| e^{i\theta}$ traverses the equator once — is the seed of the Hopf bundle's non-triviality and, in [[Def - The Hopf Bundle|the classifying computation]], of its first Chern number $\pm 1$; companion exercise [[Ex - The Cocycle of the Frame Bundle of the Sphere in Stereographic Charts]] runs the same machinery for the tangent bundle of $S^2$ and finds winding $\pm 2$.
