---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Hairy Ball Theorem"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Vector Bundle"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $S^2 = \{x \in \mathbb{R}^3 : |x| = 1\}$ and let $TS^2 \to S^2$ be its tangent bundle, a smooth real vector bundle of rank $2$ with fibre $T_xS^2 = \{v \in \mathbb{R}^3 : \langle v, x\rangle = 0\}$. Let
$$\operatorname{Fr}(TS^2) \;=\; \bigsqcup_{x \in S^2} \operatorname{Fr}(T_xS^2) \;\xrightarrow{\ \pi\ }\; S^2$$
be its **frame bundle**, the principal $GL_2(\mathbb{R})$-bundle whose fibre $\operatorname{Fr}(T_xS^2)$ is the set of linear isomorphisms $\mathbb{R}^2 \to T_xS^2$ (equivalently, ordered bases of $T_xS^2$). Prove that $\operatorname{Fr}(TS^2)$ admits **no global smooth section**: there is no smooth map $\sigma \colon S^2 \to \operatorname{Fr}(TS^2)$ with $\pi \circ \sigma = \operatorname{id}_{S^2}$.

This is the last clause of Exercise 25 (p. 12) of Haydys, *Introduction to Gauge Theory* ("in particular, show that the frame bundle of $TS^2$ does not admit any global sections"). The standing conventions of the series are those of the topic page **[[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]]**: manifolds are smooth, Hausdorff, second countable; Lie groups act on principal bundles on the right, $\operatorname{Fr}(E)$ carrying the right $GL_k(\mathbb{R})$-action $p \cdot h = p \circ h$; $\Gamma(E)$ is the space of smooth sections.

**Recall.** The ingredients are the frame bundle of a rank-$2$ vector bundle, the notion of a global frame, the equivalence of frames with sections of the frame bundle, and the hairy ball obstruction.

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

For a rank-$k$ real **[[Def - Vector Bundle|vector bundle]]** $E \to M$, the **[[Def - Frame Bundle of a Vector Bundle|frame bundle]]** $\operatorname{Fr}(E) = \bigsqcup_{m} \operatorname{Fr}(E_m)$ has fibre $\operatorname{Fr}(E_m)$ equal to the set of linear isomorphisms $p \colon \mathbb{R}^k \to E_m$, with the right $GL_k(\mathbb{R})$-action $p \cdot h = p \circ h$ (composition on $\mathbb{R}^k$). Its smooth structure is given by the charts
$$\Psi_U \colon U \times GL_k(\mathbb{R}) \to \pi^{-1}(U), \qquad \Psi_U(m, h) = e(m) \cdot h,$$
built from any local frame $e = (e_1, \dots, e_k)$ of $E$ over $U$, where $e(m) \colon \mathbb{R}^k \to E_m$ is the isomorphism sending the standard basis vector $\mathbf{e}_j$ to $e_j(m)$; two such charts differ by the smooth transition $(m, h) \mapsto (m, g(m) h)$ with $g$ the frame change. A **global frame** of $E$ is an ordered $k$-tuple $(e_1, \dots, e_k)$ of global sections that is a basis of every fibre; identifying $p \in \operatorname{Fr}(E_m)$ with the ordered basis $(p(\mathbf{e}_1), \dots, p(\mathbf{e}_k))$ of $E_m$, a section of $\operatorname{Fr}(E)$ is exactly a global frame of $E$.

![[Thm - Hairy Ball Theorem#Statement]]

We invoke the **[[Thm - Hairy Ball Theorem|hairy ball theorem]]** in the case $n = 1$: *the sphere $S^2$ admits no nowhere-vanishing smooth tangent vector field.* Equivalently, every $s \in \Gamma(TS^2)$ has a zero.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

The relevant clause of **[[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]** is that a vector bundle $E$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global section, and that global sections of $\operatorname{Fr}(E)$ correspond bijectively to global frames of $E$.

---

# Convergent Strategy

**Problem class.** This is again a *no-global-section* problem, one step removed from **[[Ex - The Tangent Bundle of S^2 is Nontrivial]]**: instead of a section of $TS^2$ we are forbidding a section of the associated *frame* bundle. The class is "*decode the section of an associated principal bundle into elementary data on the base, then obstruct that data*". A section of $\operatorname{Fr}(TS^2)$ is not an abstract object: unravelled, it is a smoothly varying ordered basis of the tangent plane, and its first vector is an ordinary vector field.

**Assumption pattern.** The base is the even sphere $S^2$ and the bundle is the frame bundle of the *tangent* bundle — the precise combination that lets a component of a frame be read as a tangent field and handed to the hairy ball theorem. The trigger is "a section of $\operatorname{Fr}(TM)$ over an even sphere": whenever a problem asks for a global frame of the tangent bundle of $S^{2n}$, the first frame vector is the obstruction. Over a parallelisable manifold — a Lie group, $S^1$, $S^3$ — the same request is *satisfiable*, so the parity of the sphere is again doing the work.

**Theorem routing.** There are two routes, and we give the self-contained one as the main proof and the structural one as a cross-check. The **direct route**: a section $\sigma$ of $\operatorname{Fr}(TS^2)$ is a smooth field of ordered bases $x \mapsto (e_1(x), e_2(x))$; its first component $e_1$ is a smooth vector field, and being part of a basis it is nowhere zero, contradicting **[[Thm - Hairy Ball Theorem|the hairy ball theorem]]**. The **structural route**: by **[[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]**, a global section of $\operatorname{Fr}(TS^2)$ exists if and only if $TS^2$ is trivial; but $TS^2$ is nontrivial by the companion exercise, so no section exists.

**Key decision point.** The one substantive move is *extracting the first vector of the frame and checking its smoothness and nonvanishing*. The nonvanishing is immediate — a basis has no zero vector — but the smoothness must be argued from the smooth structure of $\operatorname{Fr}(TS^2)$, since "$e_1$" is defined by evaluating the abstract section on a fixed standard basis vector. This is where the chart $\Psi_U(m,h) = e(m)h$ is used: it exhibits $e_1$ locally as a smooth linear combination of a reference frame, so that the vector field $e_1$ is genuinely smooth and the hairy ball theorem applies.

---

# Legal Operations Used

The numbering refers to the Legal Operations of the topic page **[[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]]**.

1. **Read a section of a frame bundle as a global frame of the vector bundle.** A smooth section $\sigma \colon M \to \operatorname{Fr}(E)$ assigns to each $m$ a linear isomorphism $\sigma(m) \colon \mathbb{R}^k \to E_m$; setting $e_j(m) := \sigma(m)(\mathbf{e}_j)$ gives an ordered $k$-tuple that is a basis of every fibre, i.e. a global frame.

2. **Extract a single component and verify its smoothness in a local chart.** The map $e_1(m) = \sigma(m)(\mathbf{e}_1)$ is smooth because, in the chart $\Psi_U(m,h) = \tilde e(m) h$ built from a reference frame $\tilde e$, one has $\sigma(m) = \tilde e(m) \cdot h(m)$ with $h \colon U \to GL_k(\mathbb{R})$ smooth, so $e_1$ is a smooth combination $\sum_j \tilde e_j\, h_{j1}$ of the smooth reference sections.

3. **Use that a basis vector is nonzero to transfer nonvanishing.** As $(e_1(x), e_2(x))$ is a basis of $T_xS^2$, its first vector $e_1(x)$ is nonzero for every $x$; the frame yields a nowhere-vanishing tangent field.

4. **Transport a global obstruction to force a contradiction.** Confront the nowhere-vanishing field $e_1$ with the hairy ball theorem, which forbids it on $S^2$.

5. **Reroute through triviality (cross-check).** Apply the sections–triviality theorem to convert "no section of $\operatorname{Fr}(TS^2)$" into "$TS^2$ not trivial", linking the result to **[[Ex - The Tangent Bundle of S^2 is Nontrivial]]**.

---

# Hints

> [!note]- Hint 1
> Do not treat a section of $\operatorname{Fr}(TS^2)$ as an opaque object. Unpack the definition of the frame bundle: what geometric datum on $S^2$ does a section assign to each point? Once you see it as a *frame*, ask what its individual vectors are.

> [!note]- Hint 2
> A section $\sigma$ gives, at each $x$, an ordered basis $(e_1(x), e_2(x))$ of the tangent plane $T_xS^2$. Consider just the first vector, $e_1$. It is a vector field on $S^2$. What do you know about the vectors of a basis — can any of them be the zero vector?

> [!note]- Hint 3
> A basis contains no zero vector, so $e_1$ is *nowhere vanishing*. If you have also convinced yourself $e_1$ is *smooth* (use the chart $\Psi_U(m,h) = \tilde e(m)h$ to write $e_1$ as a smooth combination of a reference frame), you have a smooth nowhere-vanishing tangent field on $S^2$ — which the hairy ball theorem forbids. Alternatively, quote that $\operatorname{Fr}(E)$ has a global section iff $E$ is trivial, and cite the companion exercise.

---

# Solution

A section of $\operatorname{Fr}(TS^2)$ is, once unpacked, a smoothly varying ordered basis of the tangent plane. Its first vector is a smooth vector field, and because it belongs to a basis it never vanishes — a nowhere-vanishing tangent field on $S^2$, which the hairy ball theorem prohibits. The only point requiring care is the smoothness of that first vector, which we read off the frame bundle's defining charts.

**Step 0: Fix the objects and the goal.** We must show $\operatorname{Fr}(TS^2)$ has no global smooth section. Suppose, for contradiction, that a smooth section $\sigma \colon S^2 \to \operatorname{Fr}(TS^2)$ with $\pi \circ \sigma = \operatorname{id}_{S^2}$ exists.

> [!note]- Derivation
> By the definition of the **[[Def - Frame Bundle of a Vector Bundle|frame bundle]]**, for each $x \in S^2$ the value $\sigma(x)$ lies in the fibre $\operatorname{Fr}(T_xS^2)$ (because $\pi(\sigma(x)) = x$), and an element of $\operatorname{Fr}(T_xS^2)$ is a linear isomorphism
> $$\sigma(x) \colon \mathbb{R}^2 \to T_xS^2.$$
> Thus $\sigma$ assigns to every point a linear isomorphism from $\mathbb{R}^2$ to the tangent plane at that point, and does so smoothly. This is the entire datum we shall exploit.

**Step 1: Decode the section as a global frame.**

Define $e_1(x) := \sigma(x)(\mathbf{e}_1)$ and $e_2(x) := \sigma(x)(\mathbf{e}_2)$, where $\mathbf{e}_1 = (1,0)$ and $\mathbf{e}_2 = (0,1)$ are the standard basis of $\mathbb{R}^2$. Then $(e_1(x), e_2(x))$ is an ordered basis of $T_xS^2$ for every $x$; that is, $(e_1, e_2)$ is a global frame of $TS^2$.

> [!note]- Derivation
> For fixed $x$, the map $\sigma(x) \colon \mathbb{R}^2 \to T_xS^2$ is a linear isomorphism (Step 0). A linear isomorphism carries a basis to a basis: since $(\mathbf{e}_1, \mathbf{e}_2)$ is a basis of $\mathbb{R}^2$, its image
> $$\big(\sigma(x)(\mathbf{e}_1),\, \sigma(x)(\mathbf{e}_2)\big) = \big(e_1(x),\, e_2(x)\big)$$
> is a basis of the image space $T_xS^2$ (an isomorphism preserves linear independence and spanning). Hence at every point the pair $(e_1(x), e_2(x))$ is an ordered basis of the tangent plane.

**Step 2: The first frame vector is a smooth vector field.**

The assignment $e_1 \colon S^2 \to TS^2$, $x \mapsto \sigma(x)(\mathbf{e}_1)$, is a smooth section of $TS^2$, that is, a smooth vector field.

> [!note]- Derivation
> That $e_1$ is a section is immediate: $e_1(x) = \sigma(x)(\mathbf{e}_1) \in T_xS^2$, so $\pi_{TS^2}(e_1(x)) = x$.
>
> For smoothness, work in a chart of $\operatorname{Fr}(TS^2)$. Fix $x_0 \in S^2$ and a coordinate neighbourhood $U \ni x_0$ on which $TS^2$ has a smooth local frame $\tilde e = (\tilde e_1, \tilde e_2)$ (such $U$ exists by the definition of a vector bundle: a local trivialisation over $U$ supplies a smooth frame). By the definition of the frame bundle, the chart
> $$\Psi_U \colon U \times GL_2(\mathbb{R}) \to \pi^{-1}(U), \qquad \Psi_U(m, h) = \tilde e(m) \cdot h = \tilde e(m) \circ h,$$
> is a diffeomorphism, where $\tilde e(m) \colon \mathbb{R}^2 \to T_mS^2$ is the isomorphism with $\tilde e(m)(\mathbf{e}_j) = \tilde e_j(m)$. Since $\sigma$ maps $U$ into $\pi^{-1}(U)$ and is smooth, the composite
> $$\Psi_U^{-1} \circ \sigma \colon U \to U \times GL_2(\mathbb{R}), \qquad m \mapsto (m, h(m))$$
> is smooth, so its second component $h \colon U \to GL_2(\mathbb{R})$ is a smooth matrix-valued map. Applying $\Psi_U$ back, $\sigma(m) = \tilde e(m) \circ h(m)$ as isomorphisms $\mathbb{R}^2 \to T_mS^2$; evaluating at $\mathbf{e}_1$,
> $$e_1(m) = \sigma(m)(\mathbf{e}_1) = \tilde e(m)\big(h(m)\,\mathbf{e}_1\big) = \tilde e(m)\!\left(\sum_{j=1}^{2} h_{j1}(m)\,\mathbf{e}_j\right) = \sum_{j=1}^{2} h_{j1}(m)\, \tilde e_j(m) \qquad \text{(linearity of } \tilde e(m)\text{)},$$
> where $h_{j1}$ are the entries of the first column of $h$. Each $h_{j1} \colon U \to \mathbb{R}$ is smooth (a component of the smooth map $h$) and each $\tilde e_j$ is a smooth section, so $e_1 = h_{11}\tilde e_1 + h_{21}\tilde e_2$ is a smooth section of $TS^2$ over $U$. As $x_0$ was arbitrary and smoothness is local, $e_1$ is smooth on all of $S^2$.

**Step 3: The vector field is nowhere vanishing.**

For every $x \in S^2$, $e_1(x) \neq 0$.

> [!note]- Derivation
> By Step 1, $(e_1(x), e_2(x))$ is a basis of $T_xS^2$. A basis is by definition linearly independent, and a linearly independent tuple cannot contain the zero vector (the zero vector satisfies the nontrivial dependence $1 \cdot 0 = 0$). Hence $e_1(x) \neq 0$. Equivalently, $e_1(x) = \sigma(x)(\mathbf{e}_1) \neq 0$ because $\sigma(x)$ is injective and $\mathbf{e}_1 \neq 0$. As $x$ was arbitrary, $e_1$ vanishes nowhere.

**Step 4: Collide with the hairy ball theorem.**

The field $e_1$ contradicts the hairy ball theorem; therefore no section $\sigma$ exists.

> [!note]- Derivation
> By Steps 2 and 3, $e_1 \in \Gamma(TS^2)$ is a smooth nowhere-vanishing tangent vector field on $S^2$. The **[[Thm - Hairy Ball Theorem|hairy ball theorem]]** ($n = 1$) states that $S^2$ admits no nowhere-vanishing smooth tangent vector field: every element of $\Gamma(TS^2)$ has a zero. The contradiction is exactly that $e_1$ is nowhere zero (Step 3) yet must have a zero (hairy ball theorem). The sole assumption was the existence of the section $\sigma$ (Step 0); it is therefore untenable. Hence $\operatorname{Fr}(TS^2)$ has no global smooth section.

> [!note]- Complete formal solution
> **Claim.** The frame bundle $\operatorname{Fr}(TS^2) \to S^2$ admits no global smooth section.
>
> Suppose, for contradiction, that $\sigma \colon S^2 \to \operatorname{Fr}(TS^2)$ is a smooth section, $\pi \circ \sigma = \operatorname{id}$. For each $x$, $\sigma(x) \in \operatorname{Fr}(T_xS^2)$ is a linear isomorphism $\mathbb{R}^2 \to T_xS^2$. Put $e_1(x) = \sigma(x)(\mathbf{e}_1)$.
>
> Since $\sigma(x)$ is a linear isomorphism, it carries the basis $(\mathbf{e}_1, \mathbf{e}_2)$ of $\mathbb{R}^2$ to a basis $(e_1(x), e_2(x))$ of $T_xS^2$; in particular $e_1(x) \neq 0$ for every $x$.
>
> The section $e_1$ is smooth: on a neighbourhood $U$ with a smooth reference frame $\tilde e = (\tilde e_1, \tilde e_2)$, the chart $\Psi_U(m,h) = \tilde e(m) \circ h$ is a diffeomorphism, so writing $\sigma(m) = \tilde e(m) \circ h(m)$ the map $h \colon U \to GL_2(\mathbb{R})$ is smooth, whence $e_1 = h_{11}\tilde e_1 + h_{21}\tilde e_2$ is a smooth vector field on $U$; smoothness being local, $e_1 \in \Gamma(TS^2)$.
>
> Thus $e_1$ is a smooth nowhere-vanishing tangent vector field on $S^2$, contradicting the hairy ball theorem, which forces every tangent field on $S^2$ to vanish somewhere. The assumed section cannot exist; $\operatorname{Fr}(TS^2)$ has no global section. $\blacksquare$

> [!note]- Cross-check via the sections–triviality theorem
> The same conclusion follows structurally. By **[[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]**, a vector bundle $E$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global section. Taking $E = TS^2$: a global section of $\operatorname{Fr}(TS^2)$ would force $TS^2$ to be trivial. But $TS^2$ is nontrivial by **[[Ex - The Tangent Bundle of S^2 is Nontrivial]]**. Therefore $\operatorname{Fr}(TS^2)$ has no global section. This route packages the frame-to-field argument inside the triviality theorem; the direct proof above is the same reasoning made explicit, with the smoothness of the first frame vector written out.

> [!warning] Illegal but tempting shortcut: reading nonvanishing without smoothness
> It is tempting to declare the proof finished the instant one observes that a frame has no zero vector, skipping Step 2. But the hairy ball theorem forbids *smooth* nowhere-vanishing tangent fields; a merely set-theoretic assignment $x \mapsto e_1(x)$ with no regularity is not what the theorem constrains, and a non-smooth nonvanishing field on $S^2$ is easy to write down (rotate a fixed frame discontinuously). The step that earns the contradiction is verifying, via the chart $\Psi_U(m,h) = \tilde e(m)h$, that $e_1$ is genuinely smooth. The extra condition that legitimises the shortcut is precisely the smoothness of the section $\sigma$, which propagates to $e_1$ only through the smooth structure of the frame bundle.

---

# Key Takeaways

**A section of the frame bundle is a global frame, and its individual vectors are the elementary handle by which the frame bundle is obstructed.** The reusable principle is that the frame bundle $\operatorname{Fr}(E)$ is not a mysterious auxiliary space: a global section of it *is* a global frame of $E$, and a global frame is a list of nowhere-vanishing, pointwise-independent vector fields. So any obstruction to global frames — most sharply, the impossibility of even one nowhere-vanishing section — is automatically an obstruction to sections of the frame bundle. The trigger to apply this is any question about global sections, triviality, or reductions of $\operatorname{Fr}(E)$: translate immediately into the language of frames and fields on the base, where the topological input lives. The transferable diagnostic is that the frame bundle inherits its (non)triviality entirely from $E$, and a single frame vector is usually enough to see it.

**Nonvanishing is cheap; smoothness is the clause that makes the topology bite.** The subtle point, worth carrying to every proof of this shape, is that the hairy ball theorem — and every characteristic-class or degree obstruction — constrains *smooth* objects. The nonvanishing of a frame vector is a triviality of linear algebra, true pointwise with no regularity at all, and by itself proves nothing, since discontinuous nonvanishing fields exist on every sphere. The content is that a smooth section of the frame bundle yields a *smooth* nowhere-vanishing field, and establishing this requires unwinding the smooth structure of $\operatorname{Fr}(E)$ through its charts $\Psi_U(m,h) = e(m)h$: the abstract section, composed with the chart, produces a smooth matrix-valued function $h$, whose columns assemble the frame vectors as smooth combinations of a reference frame. Whenever a proof passes from a section of a principal or frame bundle to data on the base, this chart computation is the step that must be written, not assumed.

**This is the frame-bundle face of the tangent bundle's nontriviality, and the two exercises are one theorem seen twice.** For calibration, hold this result beside **[[Ex - The Tangent Bundle of S^2 is Nontrivial]]**. There, triviality of $TS^2$ was refuted by producing a nowhere-vanishing field from a trivialisation; here, a section of $\operatorname{Fr}(TS^2)$ is refuted by producing the same kind of field from a frame. The **[[Thm - Sections of a Principal Bundle and Triviality|sections–triviality theorem]]** makes the identification exact: "$TS^2$ trivial", "$TS^2$ has a global frame", and "$\operatorname{Fr}(TS^2)$ has a global section" are three names for one condition, all defeated by the single fact that an even sphere admits no nowhere-vanishing tangent field. The general lesson is that principal bundles and their associated vector bundles carry the same triviality information, so one is free to obstruct whichever is more convenient; over $S^{2n}$ the tangent field is the most elementary obstruction, and the parity of the dimension is, once more, the whole of the matter.
