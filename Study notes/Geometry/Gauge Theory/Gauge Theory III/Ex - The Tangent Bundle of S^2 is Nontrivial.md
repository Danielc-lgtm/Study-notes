---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Hairy Ball Theorem"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Vector Bundle"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $S^2 = \{x \in \mathbb{R}^3 : |x| = 1\}$ be the round two-sphere and $TS^2 \to S^2$ its tangent bundle, a smooth real vector bundle of rank $2$ whose fibre over $x$ is the tangent plane $T_xS^2 = \{v \in \mathbb{R}^3 : \langle v, x\rangle = 0\}$. Prove that $TS^2$ is **not trivial**: there is no isomorphism of vector bundles
$$\Phi \colon S^2 \times \mathbb{R}^2 \;\xrightarrow{\ \cong\ }\; TS^2$$
covering the identity of $S^2$.

This is Exercise 3 (p. 5) of Haydys, *Introduction to Gauge Theory*, whose hint is to apply the hairy ball theorem (the same source's item I2.1.1). The standing conventions of this series are those of the topic page **[[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]]**: manifolds are smooth, Hausdorff, and second countable; $\Gamma(E)$ denotes the space of smooth sections of a bundle $E$; a vector bundle is **trivial** when it is isomorphic, over the identity of the base, to a product bundle $M \times \mathbb{R}^k$.

**Recall.** The two ingredients are the tangent bundle as a rank-$2$ vector bundle, the notion of a trivialisation, and the topological obstruction supplied by the hairy ball theorem.

![[Def - Vector Bundle#The Definition]]

A rank-$k$ real **[[Def - Vector Bundle|vector bundle]]** $\pi \colon E \to M$ is a smooth surjection whose fibres $E_m = \pi^{-1}(m)$ carry $k$-dimensional real vector-space structures, locally modelled by trivialisations: over each point there is an open $U \subseteq M$ and a diffeomorphism $\psi_U \colon \pi^{-1}(U) \to U \times \mathbb{R}^k$ that covers the identity of $U$ (that is, $\operatorname{pr}_1 \circ \psi_U = \pi$) and restricts on each fibre $E_m$ to a linear isomorphism $E_m \to \{m\} \times \mathbb{R}^k$. A **section** of $E$ over $U \subseteq M$ is a smooth map $s \colon U \to E$ with $\pi \circ s = \operatorname{id}_U$; a section of $TM$ is precisely a smooth **vector field** on $M$. A **homomorphism** of vector bundles $E \to F$ over $M$ is a smooth fibre-preserving map that is linear on each fibre, and an **isomorphism** is a homomorphism that is a linear isomorphism on every fibre; a vector bundle is **trivial** when it admits an isomorphism to the product bundle $M \times \mathbb{R}^k$ over the identity.

![[Thm - Hairy Ball Theorem#Statement]]

The result we invoke is the **[[Thm - Hairy Ball Theorem|hairy ball theorem]]**, in the smallest even-dimensional case: *the sphere $S^2$ admits no nowhere-vanishing smooth tangent vector field.* Equivalently, every smooth section $s \in \Gamma(TS^2)$ has a zero: there is a point $x_0 \in S^2$ with $s(x_0) = 0 \in T_{x_0}S^2$.

For the frame-bundle reformulation used in the companion exercise we shall also lean on the following equivalence.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

The relevant clause of **[[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]** states that a vector bundle $E \to M$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global smooth section; and a global section of $\operatorname{Fr}(E)$ is the same datum as a global smooth frame of $E$, that is, an ordered $k$-tuple of sections that is a basis of every fibre.

---

# Convergent Strategy

**Problem class.** This is a *nontriviality* problem: we must show that a given bundle is **not** isomorphic to a product. The direct attack — inspecting every conceivable isomorphism and finding a defect in each — is hopeless, so the problem belongs to the class solved by *transporting a global obstruction*. We identify one property that every trivial bundle enjoys, and exhibit a topological theorem asserting that $TS^2$ fails to have it. The property here is the existence of a nowhere-vanishing global section, and the obstruction is the hairy ball theorem.

**Assumption pattern.** The only hypothesis is that the base is $S^2$, an even-dimensional sphere; everything else is the standard structure of the tangent bundle. The recognisable trigger is the pairing "*rank equals base dimension, base is $S^{2n}$*", which is exactly the regime in which a rank-$2$ bundle over $S^2$ can be probed by a single section and the hairy ball theorem can speak. Were the base an odd sphere, or the rank strictly larger than the dimension, this exact route would give no contradiction, and indeed $TS^1$ and $TS^3$ *are* trivial.

**Theorem routing.** The route is short and forced. Assume a trivialisation $\Phi \colon S^2 \times \mathbb{R}^2 \to TS^2$ exists. Feed it a *constant* nonzero input, say the first standard basis vector $\mathbf{e}_1 \in \mathbb{R}^2$, to manufacture a global section $s(x) := \Phi(x, \mathbf{e}_1)$ of $TS^2$. Because $\Phi$ is fibrewise a linear *isomorphism*, it sends the nonzero vector $\mathbf{e}_1$ to a nonzero vector in every fibre, so $s$ is *nowhere vanishing*. This directly contradicts **[[Thm - Hairy Ball Theorem|the hairy ball theorem]]**, which forbids any nowhere-vanishing tangent field on $S^2$.

**Key decision point.** The single non-obvious move is *choosing to evaluate the trivialisation on a constant section*. Nothing in the statement mentions sections at all; the trivialisation is an isomorphism of total spaces. The insight is that a trivialisation is exactly the device that turns constant functions on the base into global sections of the bundle, and that fibrewise injectivity is precisely what guarantees a *constant nonzero* input yields a *nowhere-zero* output. The decision to keep the input constant (rather than an arbitrary section of $S^2 \times \mathbb{R}^2$) is what makes nonvanishing automatic and puts us in immediate collision with the obstruction.

---

# Legal Operations Used

The solution uses the following legal operations of the chapter, applied to the concrete bundle $TS^2$; the numbering refers to the Legal Operations of the topic page **[[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]]** and will be reconciled there.

1. **Evaluate a trivialisation on a constant section to produce a global section.** Given an isomorphism $\Phi \colon S^2 \times \mathbb{R}^2 \to TS^2$ and a fixed vector $v \in \mathbb{R}^2$, the assignment $x \mapsto \Phi(x, v)$ is a smooth global section of $TS^2$, because $x \mapsto (x, v)$ is a smooth global section of the product bundle and $\Phi$ is smooth and fibre-preserving.

2. **Use fibrewise injectivity to transfer nonvanishing.** A vector-bundle isomorphism is a linear isomorphism on each fibre; a linear isomorphism sends nonzero vectors to nonzero vectors. Hence a constant nonzero input produces a section that is nonzero at every point.

3. **Transport a global obstruction to force a contradiction.** Confront the manufactured nowhere-vanishing section with the hairy ball theorem, which asserts no such section of $TS^2$ exists; the contradiction refutes the assumed trivialisation.

4. **Reformulate triviality through the frame bundle (bridge to the companion exercise).** By operation on the sections–triviality theorem, triviality of $E$ is equivalent to the existence of a global section of $\operatorname{Fr}(E)$; this reroutes the same contradiction through $\operatorname{Fr}(TS^2)$ and is the content of **[[Ex - The Frame Bundle of TS^2 Admits No Global Section]]**.

---

# Hints

> [!note]- Hint 1
> You are asked to prove a *negative*: that no isomorphism $S^2 \times \mathbb{R}^2 \cong TS^2$ exists. Argue by contradiction — assume one exists — and look for a global object it would hand you that $S^2$ is known to forbid. What can a trivialisation of a *tangent* bundle produce that the hairy ball theorem talks about?

> [!note]- Hint 2
> A trivialisation $\Phi \colon S^2 \times \mathbb{R}^2 \to TS^2$ turns *functions into sections*. Feed it the simplest possible input: the constant map $x \mapsto (x, \mathbf{e}_1)$, where $\mathbf{e}_1 = (1,0)$. The output $s(x) = \Phi(x, \mathbf{e}_1)$ is a smooth vector field on $S^2$. Why is it nowhere zero?

> [!note]- Hint 3
> On each fibre, $\Phi$ restricts to a *linear isomorphism* $\Phi_x \colon \mathbb{R}^2 \to T_xS^2$. Injectivity means $\Phi_x(\mathbf{e}_1) \neq 0$ whenever $\mathbf{e}_1 \neq 0$ — which it is. So $s(x) = \Phi_x(\mathbf{e}_1) \neq 0$ for *every* $x$. You now hold a nowhere-vanishing tangent field on $S^2$. Quote the theorem that says this cannot exist.

---

# Solution

The argument is a contradiction in three steps: assume a trivialisation, use it to build a global vector field out of a constant input, observe that fibrewise injectivity makes that field nowhere zero, and collide with the hairy ball theorem. The whole force of the proof sits in the phrase "fibrewise isomorphism": it is what upgrades a *nonzero constant* into a *nowhere-vanishing section*.

**Step 0: Fix the objects and the goal.** We must show $TS^2$ is not trivial. We argue by contradiction: suppose there is a vector-bundle isomorphism $\Phi \colon S^2 \times \mathbb{R}^2 \to TS^2$ over the identity, and derive a contradiction with the hairy ball theorem.

> [!note]- Derivation
> By the definition of a **[[Def - Vector Bundle|vector-bundle isomorphism]]**, $\Phi$ is a smooth map that is fibre-preserving — $\pi_{TS^2} \circ \Phi = \operatorname{pr}_1$, where $\operatorname{pr}_1 \colon S^2 \times \mathbb{R}^2 \to S^2$ is the projection of the product bundle and $\pi_{TS^2} \colon TS^2 \to S^2$ is the tangent projection — and, on each fibre $\{x\} \times \mathbb{R}^2$, restricts to a linear isomorphism onto $T_xS^2$. Write this fibre restriction as
> $$\Phi_x \colon \mathbb{R}^2 \to T_xS^2, \qquad \Phi_x(v) := \Phi(x, v),$$
> so that each $\Phi_x$ is a bijective linear map (a linear isomorphism of the two-dimensional real vector spaces $\mathbb{R}^2$ and $T_xS^2$). This is the only structure of $\Phi$ we shall use.

**Step 1: Build a global vector field from a constant input.**

Define $s \colon S^2 \to TS^2$ by $s(x) := \Phi(x, \mathbf{e}_1)$, where $\mathbf{e}_1 = (1,0) \in \mathbb{R}^2$. Then $s$ is a smooth section of $TS^2$, that is, a smooth vector field on $S^2$.

> [!note]- Derivation
> The constant assignment $\iota \colon S^2 \to S^2 \times \mathbb{R}^2$, $\iota(x) = (x, \mathbf{e}_1)$, is smooth (it is $\operatorname{id}_{S^2}$ paired with a constant map) and is a section of the product bundle, since $\operatorname{pr}_1(\iota(x)) = x$. Composing with the smooth map $\Phi$,
> $$s = \Phi \circ \iota \colon S^2 \to TS^2$$
> is smooth (composition of smooth maps). It is a section because
> $$\pi_{TS^2}\big(s(x)\big) = \pi_{TS^2}\big(\Phi(x, \mathbf{e}_1)\big) = \operatorname{pr}_1(x, \mathbf{e}_1) = x \qquad \text{(since } \Phi \text{ is fibre-preserving, } \pi_{TS^2}\circ\Phi = \operatorname{pr}_1\text{)},$$
> so $\pi_{TS^2} \circ s = \operatorname{id}_{S^2}$. A smooth section of the tangent bundle is by definition a smooth vector field on $S^2$: for each $x$, $s(x) \in T_xS^2$.

**Step 2: The field is nowhere vanishing.**

For every $x \in S^2$, $s(x) \neq 0$ in $T_xS^2$.

> [!note]- Derivation
> Fix $x \in S^2$. By Step 0, the fibre map $\Phi_x \colon \mathbb{R}^2 \to T_xS^2$ is a linear isomorphism, hence injective. An injective linear map has trivial kernel, so it sends every nonzero vector to a nonzero vector:
> $$\mathbf{e}_1 \neq 0 \implies \Phi_x(\mathbf{e}_1) \neq 0 \qquad \text{(injectivity of } \Phi_x\text{, i.e. } \ker \Phi_x = \{0\}\text{)}.$$
> But $s(x) = \Phi(x, \mathbf{e}_1) = \Phi_x(\mathbf{e}_1)$, so $s(x) \neq 0$. As $x \in S^2$ was arbitrary, $s$ vanishes nowhere.

**Step 3: Collide with the hairy ball theorem.**

The existence of $s$ contradicts the hairy ball theorem; therefore no trivialisation $\Phi$ exists, and $TS^2$ is nontrivial.

> [!note]- Derivation
> By Steps 1 and 2, $s \in \Gamma(TS^2)$ is a smooth nowhere-vanishing tangent vector field on $S^2$. The **[[Thm - Hairy Ball Theorem|hairy ball theorem]]**, in the case $n = 1$, states that $S^2 = S^{2}$ admits *no* nowhere-vanishing smooth tangent vector field: every $s \in \Gamma(TS^2)$ has a zero. The two statements are contradictory — the named contradiction is "the field $s$ is simultaneously nowhere zero (Step 2) and forced to have a zero (hairy ball theorem)". The only assumption we made was the existence of the trivialisation $\Phi$ (Step 0); it must be false. Hence $TS^2$ is not isomorphic to $S^2 \times \mathbb{R}^2$, i.e. $TS^2$ is nontrivial.

> [!note]- Complete formal solution
> **Claim.** The tangent bundle $TS^2 \to S^2$ is not trivial.
>
> Suppose, for contradiction, that there is a vector-bundle isomorphism $\Phi \colon S^2 \times \mathbb{R}^2 \to TS^2$ over the identity of $S^2$. By definition of a vector-bundle isomorphism, $\Phi$ is smooth, fibre-preserving ($\pi_{TS^2} \circ \Phi = \operatorname{pr}_1$), and restricts on each fibre to a linear isomorphism $\Phi_x \colon \mathbb{R}^2 \to T_xS^2$, $\Phi_x(v) = \Phi(x,v)$.
>
> Define $s \colon S^2 \to TS^2$ by $s(x) = \Phi(x, \mathbf{e}_1)$ with $\mathbf{e}_1 = (1,0)$. As the composite of the smooth section $x \mapsto (x, \mathbf{e}_1)$ of the product bundle with the smooth map $\Phi$, the map $s$ is smooth; and $\pi_{TS^2}(s(x)) = \operatorname{pr}_1(x, \mathbf{e}_1) = x$, so $s$ is a section of $TS^2$, that is, a smooth vector field on $S^2$.
>
> For each $x$, the map $\Phi_x$ is a linear isomorphism, hence injective, so $\Phi_x(\mathbf{e}_1) \neq 0$ because $\mathbf{e}_1 \neq 0$. Thus $s(x) = \Phi_x(\mathbf{e}_1) \neq 0$ for every $x \in S^2$: the field $s$ vanishes nowhere.
>
> This contradicts the hairy ball theorem, which asserts that every smooth tangent vector field on $S^2$ has a zero. Therefore the assumed isomorphism $\Phi$ cannot exist, and $TS^2$ is nontrivial. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "rank $2$ over $S^2$, so nontrivial"
> One is tempted to declare $TS^2$ nontrivial merely because it is a rank-$2$ bundle over $S^2$, as though every bundle over a sphere were nontrivial. This is false: the *trivial* rank-$2$ bundle $S^2 \times \mathbb{R}^2$ is a rank-$2$ bundle over $S^2$, and it is trivial by construction; and $TS^1$, $TS^3$, $TS^7$ are all trivial. Rank and base alone decide nothing. The genuine input is the *even* dimension of the sphere entering through the hairy ball theorem — the extra condition that turns "rank-$2$ bundle over $S^2$" into "nontrivial" is precisely the topological obstruction, not a counting of ranks.

> [!note]- Independent cross-check via the Euler number
> The conclusion is consistent with the characteristic-class computation carried out later in the series: the Euler class of $TS^2$ integrates to the Euler characteristic, $\int_{S^2} e(TS^2) = \chi(S^2) = 2 \neq 0$, whereas a trivial bundle has vanishing Euler class. A nonzero Euler number is an independent certificate of nontriviality. The present proof needs none of this machinery; it extracts the same fact from the single, elementary obstruction that a tangent field on $S^2$ must vanish somewhere.

---

# Key Takeaways

**To prove a bundle nontrivial, produce a global object that a trivial bundle would carry and that a theorem forbids on this base.** The reusable principle is that triviality is a *positive* statement — "an isomorphism to a product exists" — and the cheapest way to refute a positive statement is to extract from it a concrete consequence that is independently known to be impossible. A trivial rank-$k$ bundle carries $k$ pointwise-independent global sections, in particular a single nowhere-vanishing one; so a nonvanishing global section is a necessary condition for triviality. Whenever the base is a space on which nonvanishing sections of the bundle in question are obstructed — the sphere $S^{2n}$ for its tangent bundle, an orientation-reversing loop for a real line bundle, a nonzero degree for a complex line bundle over a surface — the obstruction *is* the nontriviality proof. The trigger to reach for this pattern is any request to show a specific, geometrically natural bundle fails to be a product: do not search among isomorphisms, search for the forbidden section.

**A trivialisation is a machine that converts constant data on the base into global sections, and fibrewise injectivity is what preserves nonvanishing.** The transferable diagnostic is to remember what a trivialisation actually *does*: an isomorphism $\Phi \colon M \times \mathbb{R}^k \to E$ lets one push forward the manifestly available sections of the product bundle — above all the constant sections $x \mapsto (x, v)$ — to sections of $E$. Because $\Phi$ is a linear isomorphism on every fibre, and linear isomorphisms have trivial kernel, a constant nonzero $v$ yields a section $s(x) = \Phi_x(v)$ that is nonzero at every point, and $k$ linearly independent choices $v = \mathbf{e}_1, \dots, \mathbf{e}_k$ yield a global frame. This is the exact mechanism that makes "trivial $\Rightarrow$ global frame $\Rightarrow$ nowhere-vanishing section" run, and it is worth internalising because the converse direction — building a trivialisation *from* a global frame — is the content of the sections–triviality theorem used throughout the chapter.

**The even dimension of the sphere is the whole story, and its absence is why odd spheres behave oppositely.** The lesson for calibration is to locate precisely which hypothesis carries the weight. Here it is not the rank of the bundle, not the smoothness of $\Phi$, not any feature of $S^2$ as a manifold beyond the parity of its dimension: it is that $S^2$ is an *even*-dimensional sphere, the exact class on which the hairy ball theorem asserts every tangent field vanishes. The parallel with the companion result **[[Ex - The Frame Bundle of TS^2 Admits No Global Section]]** is instructive: that exercise reroutes the identical obstruction through the frame bundle, using the sections–triviality theorem to translate "$\operatorname{Fr}(TS^2)$ has no global section" into "$TS^2$ is not trivial", so that the two exercises are two faces of one fact. When a spaced-practice reconstruction of this proof stalls, the recovery key is to ask "what does an even sphere forbid?" — the answer, a nowhere-vanishing tangent field, is the entire obstruction.
