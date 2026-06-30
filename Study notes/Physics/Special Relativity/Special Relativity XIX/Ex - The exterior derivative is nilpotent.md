---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Exterior Derivative"
  - "Thm - Properties of the Exterior Derivative"
tags: [physics, special-relativity]
---

# Problem Statement

Prove that the exterior derivative is nilpotent, $\mathbf{d}\circ\mathbf{d} = 0$.

1. Prove it for a $0$-form (scalar field) $f$ by computing $(\mathbf{d}\mathbf{d}f)_{\alpha\beta}$ directly.
2. Prove it for a $1$-form $A$ by computing $(\mathbf{d}\mathbf{d}A)_{\alpha\beta\gamma}$ and showing each term cancels.
3. Explain in one paragraph why the general statement $\mathbf{d}^2 = 0$ reduces, for every degree, to the equality of mixed partial derivatives, and why this is *independent of the connection*.
4. Deduce that every exact form is closed, and state what the converse (the Poincaré lemma) requires.

**Recall:**

![[Def - The Exterior Derivative#The Definition]]

In a coordinate basis $(\mathbf{d}f)_\alpha = \partial_\alpha f$, $(\mathbf{d}A)_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$, and $(\mathbf{d}A)_{\alpha\beta\gamma} = \partial_\alpha A_{\beta\gamma} + \partial_\beta A_{\gamma\alpha} + \partial_\gamma A_{\alpha\beta}$. A form is **closed** if $\mathbf{d}A = 0$ and **exact** if $A = \mathbf{d}B$ (see [[Thm - Properties of the Exterior Derivative]]).

---

# Convergent Strategy

**Problem class.** A *prove-a-structural-identity* problem, establishing the single most important property of the exterior derivative. The route is a direct component computation, invoking the equality of mixed partials.

**Assumption pattern.** Smoothness of the forms (so mixed partials commute) is the only hypothesis. Antisymmetry of the output indices is what makes the symmetric second-derivative pairs cancel.

**Theorem routing.** Parts 1–2 use the partial-derivative form of $\mathbf{d}$ from [[Def - The Exterior Derivative]]. Part 3 is the conceptual generalisation. Part 4 cites the Poincaré lemma from [[Thm - Properties of the Exterior Derivative]].

**Key decision point.** The crux is recognising that the second partial derivatives $\partial_\alpha\partial_\beta(\cdots)$ are symmetric in $\alpha\beta$ while the exterior derivative antisymmetrises them, so the antisymmetric-symmetric contraction is zero. This is the whole mechanism, identical at every degree.

---

# Legal Operations Used

1. **Antisymmetrise to get the exterior derivative, then drop the Christoffels** (operation 6 from the topic page). Apply $\mathbf{d}$ twice using partial derivatives.
2. **Use $\mathbf{d}^2 = 0$** (operation 7 from the topic page) — here we are proving exactly this operation.

---

# Hints

> [!note]- Hint 1
> $(\mathbf{d}f)_\beta = \partial_\beta f$. Apply $\mathbf{d}$ again: $(\mathbf{d}\mathbf{d}f)_{\alpha\beta} = \partial_\alpha(\mathbf{d}f)_\beta - \partial_\beta(\mathbf{d}f)_\alpha = \partial_\alpha\partial_\beta f - \partial_\beta\partial_\alpha f$.

> [!note]- Hint 2
> $(\mathbf{d}A)_{\beta\gamma} = \partial_\beta A_\gamma - \partial_\gamma A_\beta$. Then $(\mathbf{d}\mathbf{d}A)_{\alpha\beta\gamma} = \partial_\alpha(\mathbf{d}A)_{\beta\gamma} + \partial_\beta(\mathbf{d}A)_{\gamma\alpha} + \partial_\gamma(\mathbf{d}A)_{\alpha\beta}$. Substitute and expand into six second-derivative terms.

> [!note]- Hint 3
> The six terms pair up: $\partial_\alpha\partial_\beta A_\gamma$ cancels $\partial_\beta\partial_\alpha A_\gamma$, and so on, because $\partial_\alpha\partial_\beta = \partial_\beta\partial_\alpha$.

> [!note]- Hint 4
> Mixed partials commute for smooth functions (Schwarz). The exterior derivative is connection-free, so $\mathbf{d}^2$ cannot depend on the Christoffels — the only thing it can depend on is the symmetry of second partials, which forces it to vanish.

---

# Solution

The plan: Step 1 proves $\mathbf{d}^2 f = 0$ for scalars in one line (equal mixed partials). Step 2 does the $1$-form case, six terms cancelling in pairs. Step 3 generalises and notes the connection-independence; Step 4 draws the exact-implies-closed conclusion.

**Step 1: Nilpotency on scalars.**

> [!note]- Derivation
> For a scalar field $f$, $(\mathbf{d}f)_\beta = \partial_\beta f$. Applying the exterior derivative again (a $1$-form goes to a $2$-form):
> $$(\mathbf{d}\mathbf{d}f)_{\alpha\beta} = \partial_\alpha(\mathbf{d}f)_\beta - \partial_\beta(\mathbf{d}f)_\alpha = \partial_\alpha\partial_\beta f - \partial_\beta\partial_\alpha f.$$
> For a smooth $f$, mixed second partial derivatives are equal (Schwarz's / Clairaut's theorem), so $\partial_\alpha\partial_\beta f = \partial_\beta\partial_\alpha f$ and
> $$(\mathbf{d}\mathbf{d}f)_{\alpha\beta} = 0.$$
> Nilpotency on scalars is exactly the symmetry of second partial derivatives.

**Step 2: Nilpotency on $1$-forms.**

> [!note]- Derivation
> For a $1$-form $A$, $(\mathbf{d}A)_{\beta\gamma} = \partial_\beta A_\gamma - \partial_\gamma A_\beta$. The exterior derivative of this $2$-form is the $3$-form
> $$(\mathbf{d}\mathbf{d}A)_{\alpha\beta\gamma} = \partial_\alpha(\mathbf{d}A)_{\beta\gamma} + \partial_\beta(\mathbf{d}A)_{\gamma\alpha} + \partial_\gamma(\mathbf{d}A)_{\alpha\beta}.$$
> Substitute each $\mathbf{d}A$ and expand:
> $$= \partial_\alpha(\partial_\beta A_\gamma - \partial_\gamma A_\beta) + \partial_\beta(\partial_\gamma A_\alpha - \partial_\alpha A_\gamma) + \partial_\gamma(\partial_\alpha A_\beta - \partial_\beta A_\alpha)$$
> $$= \underbrace{\partial_\alpha\partial_\beta A_\gamma - \partial_\beta\partial_\alpha A_\gamma}_{0} + \underbrace{\partial_\beta\partial_\gamma A_\alpha - \partial_\gamma\partial_\beta A_\alpha}_{0} + \underbrace{\partial_\gamma\partial_\alpha A_\beta - \partial_\alpha\partial_\gamma A_\beta}_{0} = 0,$$
> where the six second-derivative terms cancel in three pairs by the equality of mixed partials. So $(\mathbf{d}\mathbf{d}A)_{\alpha\beta\gamma} = 0$.

**Step 3: The general statement and connection-independence.**

> [!note]- Derivation
> For a $p$-form, applying $\mathbf{d}$ twice produces, in each output slot, an alternating sum of second partial derivatives $\partial_\mu\partial_\nu A_{\cdots}$ of the components. In each such term the two derivative indices $\mu,\nu$ are antisymmetrised by the construction of $\mathbf{d}$ (they occupy distinct antisymmetrised output slots), while $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ is symmetric in those indices. A tensor symmetric in a pair of indices, contracted with one antisymmetric in the same pair, is zero — so every term cancels, and $\mathbf{d}\mathbf{d}A = 0$ for all degrees.
>
> This is *independent of the connection*: the exterior derivative is metric-free (the Christoffels cancelled when $\mathbf{d}$ was defined), so $\mathbf{d}^2$ cannot contain any Christoffel symbol. The only structure left for it to depend on is the symmetry of second partial derivatives, and that symmetry forces it to vanish. One could not prove $\mathbf{d}^2 = 0$ for the *covariant* derivative — $\nabla_\alpha\nabla_\beta - \nabla_\beta\nabla_\alpha$ is *not* zero; it is the Riemann curvature. Nilpotency is special to the exterior derivative precisely because antisymmetrisation removes the connection, leaving only the (always symmetric) second partials.

**Step 4: Exact implies closed; the converse needs topology.**

> [!note]- Derivation
> If a form is exact, $A = \mathbf{d}B$, then $\mathbf{d}A = \mathbf{d}\mathbf{d}B = 0$, so $A$ is closed:
> $$\text{exact} \Longrightarrow \text{closed}.$$
> The converse — that every closed form is exact — is *not* automatic; it is the **Poincaré lemma**, and it holds only on a contractible (star-shaped) domain. On flat spacetime, which is convex, every closed form is indeed exact; on a region with a hole, a closed form may fail to be exact, and the failure detects the hole (this is de Rham cohomology). So nilpotency gives the easy half (exact $\Rightarrow$ closed) for free everywhere, while the hard half (closed $\Rightarrow$ exact) requires the domain to have trivial topology.

> [!note]- Complete formal solution
> For a scalar, $(\mathbf{d}\mathbf{d}f)_{\alpha\beta} = \partial_\alpha\partial_\beta f - \partial_\beta\partial_\alpha f = 0$ by equality of mixed partials. For a $1$-form, $(\mathbf{d}\mathbf{d}A)_{\alpha\beta\gamma} = \partial_\alpha(\partial_\beta A_\gamma-\partial_\gamma A_\beta) + \partial_\beta(\partial_\gamma A_\alpha-\partial_\alpha A_\gamma) + \partial_\gamma(\partial_\alpha A_\beta-\partial_\beta A_\alpha) = 0$, the six terms cancelling in pairs. In general, $\mathbf{d}\mathbf{d}A$ antisymmetrises symmetric second partials $\partial_\mu\partial_\nu A_{\cdots}$, giving zero; this is connection-independent because $\mathbf{d}$ is metric-free, so only the symmetry of second partials can matter. Hence $\mathbf{d}^2 = 0$, every exact form is closed, and the converse (closed $\Rightarrow$ exact) is the Poincaré lemma, valid on star-shaped domains. $\blacksquare$

---

# Key Takeaways

**$\mathbf{d}^2 = 0$ is the equality of mixed partial derivatives, dressed in form language.** The most important structural fact of the exterior calculus has the most elementary cause: $\partial_\alpha\partial_\beta = \partial_\beta\partial_\alpha$ for smooth functions. Every time you apply $\mathbf{d}$ twice, you produce second partial derivatives that are symmetric in the differentiation indices, and the antisymmetrisation built into $\mathbf{d}$ annihilates them. This is why nilpotency holds at every degree by the same one-line mechanism, and why it requires only smoothness. The transferable recognition is that any "second-derivative-of-an-antisymmetric-object" vanishes for this reason — it is the source of the homogeneous Maxwell equations, of the closedness of every field strength built as $\mathbf{d}A$, and of the two classical curl identities, all of which are $\mathbf{d}^2 = 0$ in disguise.

**Nilpotency is the signature of the exterior derivative, and its failure for the covariant derivative is the curvature.** It is illuminating to contrast $\mathbf{d}^2 = 0$ with the covariant derivative: $\nabla_\alpha\nabla_\beta - \nabla_\beta\nabla_\alpha$ acting on a vector is *not* zero — it is the Riemann curvature tensor $R^\rho{}_{\sigma\alpha\beta}v^\sigma$. The difference is exactly the connection: the covariant second derivative carries Christoffel-squared and Christoffel-derivative terms that do not cancel, and their irreducible part is the curvature. The exterior derivative, being metric-free, has no such terms, so its square vanishes identically. This contrast is worth holding onto, because it explains why the metric-free, topological content of physics (carried by $\mathbf{d}$, with $\mathbf{d}^2 = 0$) is clean and universal, while the metric-dependent, geometric content (carried by $\boldsymbol{\nabla}$, whose commutator $[\nabla,\nabla]$ is the curvature) is where gravity lives.

**Exact implies closed for free; closed implies exact is a question about the shape of space.** The half of the closed-exact relationship that follows from nilpotency — exact $\Rightarrow$ closed — costs nothing and holds on any domain. The other half — closed $\Rightarrow$ exact — is the Poincaré lemma and is *false* in general, holding only when the domain is contractible. This asymmetry is the doorway to de Rham cohomology: the quotient of closed forms by exact forms measures exactly how the converse fails, and that measure is a topological invariant counting the holes in the space. The practical upshot for physics is that the existence of a potential (a scalar potential for a curl-free field, a vector potential for a divergence-free field) is guaranteed on simply connected regions but can fail around obstructions — the Aharonov–Bohm flux, the magnetic monopole — and recognising when you are on a contractible domain is what licenses the introduction of a potential.
