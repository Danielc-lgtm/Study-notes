---
type: theorem
subject: hodge-theory
prereqs:
  - "Def - Harmonic Form"
  - "Def - Hodge Laplacian"
  - "Thm - Harmonic Forms Represent de Rham Cohomology"
  - "Def - Riemannian Manifold"
tags: [geometry, hodge-theory, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a closed (compact, without boundary) Riemannian $n$-manifold. The Ricci tensor is $\operatorname{Ric}$, a symmetric $(0, 2)$-tensor; we write $\operatorname{Ric}(X, X)$ for its evaluation on $X \in TM$. The condition **positive Ricci curvature** means $\operatorname{Ric}(X, X) > 0$ for all $X \neq 0$ at every point; **nonnegative Ricci** means $\operatorname{Ric}(X, X) \geq 0$. The Hodge Laplacian on $1$-forms is $\Delta = d\delta + \delta d$; the rough Laplacian is $\nabla^*\nabla$ (formal $L^2$-adjoint of the connection); the Weitzenböck formula on $1$-forms is $\Delta\omega = \nabla^*\nabla\omega + \operatorname{Ric}(\omega^\sharp, \cdot)$, with $\omega^\sharp$ the vector field dual to $\omega$ via the metric. The first Betti number is $b_1(M) = \dim H^1_{dR}(M; \mathbb{R})$.

---

# Statement

> **Bochner's Theorem.** Let $(M, g)$ be a closed Riemannian $n$-manifold. If the Ricci curvature is positive ($\operatorname{Ric}(X, X) > 0$ for every $X \neq 0$ at every point of $M$), then every harmonic $1$-form vanishes identically. Consequently
> $$H^1_{dR}(M; \mathbb{R}) = 0, \qquad b_1(M) = 0.$$

> **Corollary (nonnegative Ricci).** If $\operatorname{Ric} \geq 0$ on $M$, every harmonic $1$-form is parallel ($\nabla h = 0$). Consequently $b_1(M) \leq n$, with equality iff $M$ is a flat torus quotient ($M = T^n /\Gamma$ for a finite group $\Gamma$).

---

# Motivation

Bochner's theorem is the prototypical result connecting *curvature* (a metric-geometric quantity) to *topology* (a smooth invariant via Betti numbers). It established the **Bochner technique** as a powerful method: introduce a harmonic form, compute the Laplacian of its squared length using the Weitzenböck formula, integrate over the closed manifold, and use curvature positivity to force the form to vanish.

The theorem matters for three reasons.

**First, it is a "vanishing theorem" — curvature kills cohomology.** Without curvature input, the first Betti number $b_1(M)$ of a closed manifold is unconstrained. Positive Ricci forces $b_1 = 0$, a strong topological restriction. The same template generalizes: nonnegative scalar curvature obstructs harmonic spinors (Lichnerowicz), positive bisectional curvature obstructs holomorphic forms on Kähler manifolds (Kodaira vanishing). Every "curvature-positivity kills cohomology" theorem in geometry follows this pattern.

**Second, it is the simplest demonstration of the Bochner technique.** The proof is a clean three-step argument: (i) take a harmonic form, (ii) apply the Weitzenböck formula to compute $\Delta|h|^2$, (iii) integrate over the closed manifold and use curvature positivity. The technique generalizes — replace $\mathrm{Ric}$ with $\mathrm{scal}$, replace harmonic $1$-forms with harmonic spinors, replace the manifold with a vector bundle — and produces an enormous variety of vanishing theorems.

**Third, it constrains the topology of positively curved manifolds.** Combined with Myers's theorem (positive Ricci implies compact and finite fundamental group), Bochner's theorem says: positively-Ricci-curved manifolds are topologically simple. The sphere theorems (Berger, Brendle–Schoen) refine this further: pinched positive sectional curvature determines the topology essentially uniquely.

The result is **not** a topological theorem in disguise — it genuinely requires the Riemannian metric. The sphere $S^n$ ($n \geq 2$) has positive Ricci with $b_1 = 0$, consistent with Bochner. The torus $T^n$ has $b_1 = n$ and is Ricci-flat, also consistent (positive Ricci is needed, not just nonnegative). The hyperbolic space form $\mathbb{H}^n/\Gamma$ has negative Ricci and can have arbitrarily large $b_1$, consistent with positive Ricci being essential. The theorem is sharp at all these examples.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is: closed Riemannian manifold with positive Ricci curvature. Several non-obvious sources lead to satisfying this hypothesis.

The most common source is **a manifold with a positive-Ricci metric**. Property $B$: a closed manifold $M$ admitting some Riemannian metric $g$ with $\operatorname{Ric}_g > 0$. The bridge is the implication "exists positive-Ricci metric $\Rightarrow$ $b_1(M) = 0$" — a topological condition on $M$. Examples: $S^n$ for $n \geq 2$ admits the round metric with $\operatorname{Ric} = (n-1)g > 0$. $\mathbb{CP}^n$ admits the Fubini–Study metric with positive Ricci. **Compact Lie groups with bi-invariant metrics** have nonnegative Ricci (with positivity in some cases); compact symmetric spaces of positive type have positive Ricci. The topological corollary: none of these can have nonzero $b_1$ — verifiable independently.

A second source is **a manifold with a positive-sectional-curvature metric**. Property $B$: a closed manifold $M$ with $\operatorname{sec}_g > 0$ (sectional curvature, a stronger condition than Ricci). The bridge: $\operatorname{sec} > 0 \Rightarrow \operatorname{Ric} > 0$ (Ricci is a contraction of the Riemann tensor that recovers averaged sectional curvature), so Bochner applies and $b_1 = 0$. The combination of Bochner with **Myers's theorem** ($\operatorname{Ric} \geq (n-1)k$ for $k > 0$ implies diameter $\leq \pi/\sqrt{k}$ and $\pi_1$ finite) gives strong topological restrictions on positively curved manifolds.

A third source is **a Lie group with bi-invariant metric**. Property $B$: a compact Lie group $G$ with a bi-invariant metric. The bridge: for such metrics, $\operatorname{Ric}_g(X, X) = \frac{1}{4}\|\mathrm{ad}_X\|^2 \geq 0$, with equality iff $\mathrm{ad}_X = 0$, i.e., $X$ is in the centre $Z(\mathfrak{g})$. For a semisimple Lie group, $Z(\mathfrak{g}) = 0$, so $\operatorname{Ric}_g > 0$ and Bochner applies: $b_1(G) = 0$. The exceptional Lie groups, simple Lie groups, etc., all have $b_1 = 0$. For $G$ with nontrivial centre (like $U(n) = \mathrm{SU}(n) \times U(1)/\mathbb{Z}_n$), $\operatorname{Ric} \geq 0$ with kernel along the $U(1)$ factor, giving $b_1 = 1$ — at the boundary of Bochner's vanishing.

A fourth source is **a closed manifold quotient of a positive-Ricci universal cover**. Property $B$: $M = \tilde M/\Gamma$ with $\tilde M$ a closed positive-Ricci Riemannian manifold and $\Gamma$ a freely acting finite group. The bridge: $\tilde M$ has $b_1(\tilde M) = 0$ by Bochner, and standard topology shows $H^1(M; \mathbb{R}) \subseteq H^1(\tilde M; \mathbb{R}) = 0$, so $b_1(M) = 0$.

**Targets (Output Amplification)**

The conclusion is $b_1(M) = 0$ for positive-Ricci closed Riemannian manifolds. Combined with other facts, this produces several powerful results.

The most powerful combination is **Bochner plus Myers gives simply-connected-like restriction**. Bochner: $b_1 = 0$. Myers: $\pi_1$ finite. Combining, positive-Ricci closed Riemannian manifolds have *finite* abelianized fundamental group ($\pi_1^{ab} = H_1(M; \mathbb{Z})$ finite). For simply-connected $M$, this is automatic; for non-simply-connected $M$, $\pi_1$ is finite but can be nonabelian (e.g., $\mathbb{RP}^n = S^n/\mathbb{Z}_2$ has $\pi_1 = \mathbb{Z}_2$, finite, with $b_1 = 0$ confirming Bochner).

A second combination is **Bochner plus Hodge isomorphism gives "no harmonic $1$-form = no $H^1$"**. The chain: Bochner kills harmonic $1$-forms, the Hodge isomorphism identifies $\mathcal{H}^1$ with $H^1_{dR}$, so $H^1_{dR} = 0$. The result $b_1 = 0$ is a topological statement derived from harmonic-form analysis via Hodge theory.

A third combination is **Bochner generalized to other curvature conditions**. The Bochner technique works on higher forms via generalized Weitzenböck formulas, with curvature terms involving the full Riemann tensor (Lichnerowicz formula). For closed Kähler manifolds with positive holomorphic bisectional curvature, the Bochner technique on $(p, q)$-forms gives **Kodaira vanishing**: $H^{p,q}(X, L) = 0$ for $p + q > \dim X$ when $L$ is ample. Each case is a Bochner-style argument with different curvature input.

A fourth combination is **Bochner plus the equality case gives rigidity**. The corollary "nonnegative Ricci forces harmonic $1$-forms to be parallel, with $b_1 \leq n$" plus the equality $b_1 = n$ forces the manifold to be a flat torus quotient. This is a **rigidity theorem**: among closed manifolds with $\operatorname{Ric} \geq 0$ and $b_1 = n$, only flat tori (up to finite cover) appear. The same combination applied to higher Bochner formulas gives rigidity statements like "compact Ricci-flat Kähler with $b_1 = n$ is a flat torus" and more.

---

# Why Is It True

The intuition is a **conservation calculation** on harmonic forms: a harmonic form's pointwise length cannot be both "smoothed out" by the Laplacian and "averaged to zero" by Stokes, unless the form is zero everywhere. Curvature is what forces the smoothing to be one-signed.

In detail: take a harmonic $1$-form $h$. The Weitzenböck formula reads $\Delta h = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$ (which the proof derives from the Ricci identity on covariant derivatives of forms). Since $\Delta h = 0$ (harmonic), this gives $\nabla^*\nabla h = -\operatorname{Ric}(h^\sharp, \cdot)$.

Pair both sides with $h$ in $L^2$: $\langle\nabla^*\nabla h, h\rangle = -\langle\operatorname{Ric}(h^\sharp, \cdot), h\rangle = -\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$. The left side, by adjointness, is $\|\nabla h\|^2_{L^2} \geq 0$. So
$$\|\nabla h\|^2_{L^2} = -\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g.$$
Now use positive Ricci: $\operatorname{Ric}(h^\sharp, h^\sharp) > 0$ wherever $h \neq 0$. The right side is $\leq 0$ (and $< 0$ if $h \not\equiv 0$). The left side is $\geq 0$. So both must be $0$: $\|\nabla h\|^2 = 0$ (hence $\nabla h = 0$, $h$ is parallel) and $\int\operatorname{Ric}(h^\sharp, h^\sharp) = 0$ (hence $h^\sharp = 0$ pointwise where $\operatorname{Ric} > 0$, which is everywhere).

So $h \equiv 0$. Combined with the Hodge isomorphism, $\mathcal{H}^1 = 0$ gives $H^1_{dR} = 0$.

**The one-line mechanism summary:** **the integral $\int_M\langle\Delta|h|^2/2\rangle\operatorname{vol}_g = -\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g - \|\nabla h\|^2$ vanishes on a closed manifold, and positivity of $\operatorname{Ric}$ forces both $\operatorname{Ric}$-term and the $\nabla h$-term to vanish, so $h$ is parallel and is zero where $\operatorname{Ric}$ is positive.**

The deeper insight: **harmonic forms are "balanced" — their $L^2$ norm is critical**. The Weitzenböck formula decomposes the variation of $|h|^2$ into a manifestly nonnegative "rough" term (the gradient squared) and a curvature term. When the curvature is one-signed (positive Ricci), the only way to balance is for both terms to vanish. The harmonic form is then constant or zero.

A variation gives the nonnegative case: with $\operatorname{Ric} \geq 0$, both $\|\nabla h\|^2 = 0$ (so $h$ parallel) and $\int\operatorname{Ric}(h^\sharp, h^\sharp) = 0$ (so $h^\sharp$ in the kernel of $\operatorname{Ric}$ everywhere). The conclusion is "harmonic = parallel + Ricci-flat direction", giving the rigidity statement for $b_1 = n$.

---

# What Makes This Hard

The proof is compressed. The Weitzenböck formula is the conceptual bottleneck — its derivation involves the Ricci identity on covariant derivatives of forms, which uses the formula for the commutator $[\nabla_i, \nabla_j]$ on a form (giving a Riemann tensor contraction that reduces to Ricci on $1$-forms). Most expositions cite the formula and verify it; deriving it from scratch is a several-line calculation.

The most common error: **forgetting the integration step**. The Bochner technique requires *integrating* the Weitzenböck calculation over the closed manifold to kill the rough Laplacian's integral via Stokes' theorem. Without the integration, "$\Delta|h|^2 = $ something" is just a pointwise identity with no topological consequence. The integration is what converts the local PDE identity into a global vanishing.

A second error: **conflating "harmonic form" on a closed manifold with "harmonic function" on $\mathbb{R}^n$**. The Bochner argument is for *forms* on a *closed* manifold; harmonic functions on $\mathbb{R}^n$ (like $e^x\cos y$) need not vanish under positive curvature. The closed-manifold hypothesis is essential to apply Stokes / integration by parts.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Take a harmonic $1$-form $h$. The Weitzenböck formula gives $\Delta h = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$, so $0 = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$. Pair with $h$ in $L^2$: $0 = \|\nabla h\|^2 + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$. Positive Ricci forces both terms to vanish, hence $h \equiv 0$. By the Hodge isomorphism, $b_1(M) = 0$.

**Subgoal decomposition:**

1. **Weitzenböck formula on $1$-forms.** $\Delta\omega = \nabla^*\nabla\omega + \operatorname{Ric}(\omega^\sharp, \cdot)$ for any $\omega \in \Omega^1(M)$.
   - *Hint:* Compute $\delta d\omega$ and $d\delta\omega$ in terms of covariant derivatives, using the Ricci identity $[\nabla_i, \nabla_j]\omega_k = -R_{ijk}{}^l\omega_l$. Trace gives Ricci.
   - *Why needed:* Splits $\Delta$ into a non-negative "rough" part and a curvature part, the key algebraic identity for Bochner.

2. **Pair with $h$ and use adjoint identity.** $\langle\nabla^*\nabla h, h\rangle_{L^2} = \|\nabla h\|^2_{L^2}$.
   - *Hint:* $\nabla^*$ is the formal $L^2$-adjoint of $\nabla$, so $\langle\nabla^*\nabla h, h\rangle = \langle\nabla h, \nabla h\rangle = \|\nabla h\|^2$.
   - *Why needed:* Converts the rough Laplacian into a manifestly nonnegative integral.

3. **Integrate the Weitzenböck identity for a harmonic form.** $0 = \langle\Delta h, h\rangle = \|\nabla h\|^2 + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$.
   - *Hint:* $\Delta h = 0$ gives the equation; use step 2 for the first term.
   - *Why needed:* Two nonnegative terms summing to zero; both must be zero.

4. **Both terms vanish.** $\|\nabla h\|^2 = 0 \Rightarrow \nabla h = 0$ ($h$ is parallel). $\int_M\operatorname{Ric}(h^\sharp, h^\sharp) = 0 \Rightarrow \operatorname{Ric}(h^\sharp, h^\sharp) = 0$ pointwise (by continuity of the integrand).
   - *Hint:* Two nonnegative integrals summing to zero are each zero; the integrands are nonnegative continuous functions, so each is zero pointwise.
   - *Why needed:* Extracts the pointwise consequence from the integrated identity.

5. **Use positive Ricci to force $h = 0$.** $\operatorname{Ric}(h^\sharp, h^\sharp) = 0$ pointwise + $\operatorname{Ric}$ positive-definite at every point $\Rightarrow h^\sharp = 0$ at every point $\Rightarrow h = 0$.
   - *Hint:* Positive-definite bilinear form $B$ with $B(v, v) = 0 \Rightarrow v = 0$.
   - *Why needed:* The curvature condition is what gives the final pointwise vanishing.

6. **Apply Hodge isomorphism.** $\mathcal{H}^1(M) = \{0\}$ + Hodge isomorphism $\Rightarrow H^1_{dR}(M) = 0$.
   - *Hint:* $\dim H^1_{dR} = \dim\mathcal{H}^1 = 0$.
   - *Why needed:* Concludes the topological statement $b_1 = 0$.

7. **(Corollary, nonnegative case)** With $\operatorname{Ric} \geq 0$: from step 4, $\nabla h = 0$ ($h$ parallel) and $\operatorname{Ric}(h^\sharp, h^\sharp) = 0$ pointwise. The space of parallel $1$-forms has [[Def - Dimension|dimension]] $\leq n$ (since $\nabla$-parallel sections of $\Omega^1$ are determined by their value at a single point). Hence $b_1 \leq n$. Equality iff $M$ has flat connection on $T^*M$, iff $M$ is a flat torus quotient.

---

# Lemma Decomposition

> [!note]- Lemma 1: Weitzenböck formula on $1$-forms
> **Statement:** For any $\omega \in \Omega^1(M)$ on a Riemannian manifold,
> $$\Delta\omega = \nabla^*\nabla\omega + \operatorname{Ric}(\omega^\sharp, \cdot),$$
> where $\Delta = d\delta + \delta d$ is the [[Def - Hodge Laplacian|Hodge Laplacian]], $\nabla^*\nabla$ is the rough Laplacian (formal adjoint of $\nabla$ followed by $\nabla$), and $\operatorname{Ric}(\omega^\sharp, \cdot)$ is the $1$-form $X \mapsto \operatorname{Ric}(\omega^\sharp, X)$.
>
> **Hint:** Express $d\delta\omega$ and $\delta d\omega$ in covariant derivatives. Use the Ricci identity $[\nabla_i, \nabla_j]\omega_k = -R_{ijk}{}^l\omega_l$ to convert one of the resulting commutators into a Riemann tensor contraction; tracing gives Ricci.
>
> **Why needed:** Splits $\Delta$ into a non-negative term ($\nabla^*\nabla$, the "rough" Laplacian) and a curvature term ($\operatorname{Ric}$). The non-negativity of $\nabla^*\nabla$ is what makes the Bochner argument work.
>
> > [!note]- Full proof (sketch)
> > In local coordinates, $\omega = \omega_k dx^k$. Then $(\delta d\omega)_k = -\nabla^j\nabla_j\omega_k + \nabla^j\nabla_k\omega_j$ (after some computation), and $(d\delta\omega)_k = -\nabla_k\nabla^j\omega_j$. Combining:
> > $$(\Delta\omega)_k = -\nabla^j\nabla_j\omega_k + \nabla^j\nabla_k\omega_j - \nabla_k\nabla^j\omega_j = -\nabla^j\nabla_j\omega_k + [\nabla^j, \nabla_k]\omega_j.$$
> > The commutator $[\nabla^j, \nabla_k]\omega_j = -R_{jk}{}^j{}_l\omega^l = -R_{kl}\omega^l$ by tracing the Ricci identity (and the Ricci tensor is $R_{kl} = R^j{}_{jkl}$ — the trace of the Riemann tensor on first and third indices). So
> > $$(\Delta\omega)_k = -\nabla^j\nabla_j\omega_k + R_{kl}\omega^l = (\nabla^*\nabla\omega)_k + (\operatorname{Ric}\omega)_k.$$
> > Hence $\Delta\omega = \nabla^*\nabla\omega + \operatorname{Ric}(\omega^\sharp, \cdot)$.

> [!note]- Lemma 2: The rough Laplacian's $L^2$-pairing is the gradient squared
> **Statement:** For $\omega \in \Omega^1(M)$ on a closed Riemannian manifold, $\langle\nabla^*\nabla\omega, \omega\rangle_{L^2} = \|\nabla\omega\|^2_{L^2} = \int_M|\nabla\omega|^2\operatorname{vol}_g \geq 0$.
>
> **Hint:** Adjointness of $\nabla^*$ and $\nabla$: $\langle\nabla^*\eta, \omega\rangle = \langle\eta, \nabla\omega\rangle$. Apply with $\eta = \nabla\omega$.
>
> **Why needed:** Converts the rough Laplacian's contribution to a manifestly nonnegative integral.
>
> > [!note]- Full proof
> > $\nabla^*$ is the formal $L^2$-adjoint of the connection $\nabla : \Omega^1(M) \to \Omega^1(M) \otimes \Omega^1(M) = $ sections of $T^*M\otimes T^*M$. The pairing $\langle\nabla^*\eta, \omega\rangle_{L^2} = \langle\eta, \nabla\omega\rangle_{L^2}$ for $\omega \in \Omega^1(M)$ and $\eta$ a $(0,2)$-tensor.
> >
> > Applied with $\eta = \nabla\omega$: $\langle\nabla^*\nabla\omega, \omega\rangle = \langle\nabla\omega, \nabla\omega\rangle = \|\nabla\omega\|^2 = \int_M|\nabla\omega|^2\operatorname{vol}_g \geq 0$.

> [!note]- Lemma 3: Bochner integral identity for harmonic $1$-forms
> **Statement:** If $h \in \mathcal{H}^1(M)$ on a closed Riemannian manifold, then
> $$0 = \|\nabla h\|^2_{L^2} + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g.$$
>
> **Hint:** Pair the Weitzenböck identity $\Delta h = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$ with $h$ in $L^2$, then use $\Delta h = 0$ and Lemma 2.
>
> **Why needed:** The key identity that combines Weitzenböck with harmonicity to give a quadratic inequality.
>
> > [!note]- Full proof
> > $\Delta h = 0$ (since $h$ is harmonic). By Lemma 1, $0 = \Delta h = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$.
> >
> > Pair with $h$ in $L^2$: $0 = \langle\nabla^*\nabla h, h\rangle + \langle\operatorname{Ric}(h^\sharp, \cdot), h\rangle$.
> >
> > By Lemma 2, $\langle\nabla^*\nabla h, h\rangle = \|\nabla h\|^2 \geq 0$.
> >
> > The second term: $\langle\operatorname{Ric}(h^\sharp, \cdot), h\rangle = \int_M g(\operatorname{Ric}(h^\sharp, \cdot), h)\operatorname{vol}_g = \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$, using $g(h, \cdot) \cdot h^\sharp = g(h^\sharp, h^\sharp)\cdot\mathrm{id}$... actually directly: $g(\operatorname{Ric}(h^\sharp, \cdot), h) = \operatorname{Ric}(h^\sharp, h^\sharp)$ since $h(X) = g(h^\sharp, X)$ for all $X$, so $g$-pairing the form $\operatorname{Ric}(h^\sharp, \cdot)$ with $h$ gives $\operatorname{Ric}(h^\sharp, h^\sharp)$.
> >
> > Combining: $0 = \|\nabla h\|^2 + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$.

> [!note]- Lemma 4: Positive Ricci kills harmonic $1$-forms
> **Statement:** If $\operatorname{Ric} > 0$ everywhere on a closed Riemannian manifold, then every harmonic $1$-form vanishes identically.
>
> **Hint:** Both terms in the Bochner identity (Lemma 3) are nonnegative; they sum to zero, so each is zero. Positive-definiteness of $\operatorname{Ric}$ then forces $h^\sharp = 0$.
>
> **Why needed:** The direct topological conclusion: harmonic $1$-forms vanish.
>
> > [!note]- Full proof
> > By Lemma 3, $0 = \|\nabla h\|^2 + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$. Both terms are nonnegative (the first by Lemma 2, the second by $\operatorname{Ric} \geq 0$). Sum zero $\Rightarrow$ each zero.
> >
> > $\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g = 0$ with $\operatorname{Ric}(h^\sharp, h^\sharp) \geq 0$ continuous $\Rightarrow \operatorname{Ric}(h^\sharp, h^\sharp) = 0$ pointwise (by continuity, a nonnegative continuous function integrating to zero is zero everywhere).
> >
> > $\operatorname{Ric}$ is positive-definite at every point (hypothesis $\operatorname{Ric} > 0$), so $\operatorname{Ric}(v, v) = 0 \Rightarrow v = 0$. Applied with $v = h^\sharp(p)$: $h^\sharp(p) = 0$ for every $p$, hence $h^\sharp \equiv 0$, hence $h \equiv 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (Bochner).** Let $(M, g)$ be a closed Riemannian $n$-manifold with $\operatorname{Ric}_g(X, X) > 0$ for all $X \neq 0$. Then $b_1(M) = 0$.
>
> *Proof.*
>
> **Step 0 — Well-posedness.** Since $M$ is closed Riemannian, the Hodge Laplacian $\Delta$ on $1$-forms is a self-adjoint elliptic operator with finite-dimensional kernel $\mathcal{H}^1(M)$. By the Hodge isomorphism ([[Thm - Harmonic Forms Represent de Rham Cohomology]]), $\dim\mathcal{H}^1(M) = b_1(M)$. We aim to show $\mathcal{H}^1(M) = \{0\}$.
>
> **Step 1 — Take a harmonic $1$-form.** Let $h \in \mathcal{H}^1(M)$, so $\Delta h = 0$.
>
> **Step 2 — Apply Weitzenböck.** By Lemma 1, $\Delta h = \nabla^*\nabla h + \operatorname{Ric}(h^\sharp, \cdot)$. Combined with $\Delta h = 0$:
> $$\nabla^*\nabla h = -\operatorname{Ric}(h^\sharp, \cdot).$$
>
> **Step 3 — Pair with $h$ in $L^2$.** $\langle\nabla^*\nabla h, h\rangle_{L^2} = -\langle\operatorname{Ric}(h^\sharp, \cdot), h\rangle_{L^2}$. By Lemma 2, $\langle\nabla^*\nabla h, h\rangle = \|\nabla h\|^2_{L^2}$. The right side is $-\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g$ (as in Lemma 3). Hence
> $$\|\nabla h\|^2_{L^2} + \int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g = 0.$$
>
> **Step 4 — Both terms vanish.** Both $\|\nabla h\|^2 \geq 0$ and $\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g \geq 0$ (the second by $\operatorname{Ric}(h^\sharp, h^\sharp) \geq 0$). Their sum is zero, so each is zero.
>
> **Step 5 — Use positive Ricci.** $\int_M\operatorname{Ric}(h^\sharp, h^\sharp)\operatorname{vol}_g = 0$ with the integrand a nonnegative continuous function implies the integrand is zero pointwise. Hence $\operatorname{Ric}(h^\sharp(p), h^\sharp(p)) = 0$ for all $p \in M$. Since $\operatorname{Ric}$ is positive-definite at every $p$ (by hypothesis), $h^\sharp(p) = 0$ for all $p$. Hence $h \equiv 0$.
>
> **Step 6 — Conclude.** $\mathcal{H}^1(M) = \{0\}$. By the Hodge isomorphism, $b_1(M) = \dim\mathcal{H}^1(M) = 0$. $\qquad\blacksquare$
>
> *Corollary (nonnegative Ricci).* If $\operatorname{Ric} \geq 0$ instead of $> 0$, Step 5 fails to force $h = 0$, but $\nabla h = 0$ (from $\|\nabla h\|^2 = 0$) — so $h$ is parallel. Parallel sections of $T^*M$ are determined by their value at a single point, so $\dim$ (parallel $1$-forms) $\leq \dim T^*_pM = n$. Hence $b_1(M) \leq n$. Equality holds iff the manifold has a flat metric (parallel transport is identity), iff $M$ is a flat torus quotient $T^n/\Gamma$ for a finite group $\Gamma$.

---

# Cross-Field Exercise Suggestions

**Riemannian geometry — checking Bochner on standard examples.** Verify $b_1(S^n) = 0$ via Bochner: the round metric has $\operatorname{Ric} = (n-1)g > 0$, so Bochner gives $b_1 = 0$; verify directly from the cohomology of $S^n$ (which is $\mathbb{R}$ in degrees $0$ and $n$, zero elsewhere). Verify the same for $\mathbb{CP}^n$ with the Fubini–Study metric. Verify that the flat $T^n$ saturates the nonnegative-Ricci corollary: $\operatorname{Ric} = 0$ and $b_1 = n$.

**Lie theory — semisimple Lie [[Def - Group|groups]] have $b_1 = 0$.** A compact semisimple Lie group $G$ has trivial centre, so the bi-invariant metric gives $\operatorname{Ric}(X, X) = \frac{1}{4}\|\mathrm{ad}_X\|^2 > 0$ for $X \neq 0$. Bochner: $b_1(G) = 0$. Verify for specific groups: $\mathrm{SU}(2) = S^3$ has $b_1 = 0$; $\mathrm{SU}(n)$ for $n \geq 2$ has $b_1 = 0$; $\mathrm{SO}(n)$ for $n \geq 3$ has $b_1 = 0$. For $U(n) = (\mathrm{SU}(n)\times U(1))/\mathbb{Z}_n$, the centre is nontrivial ($U(1)$), so Ricci is nonnegative with a kernel, and $b_1(U(n)) = 1$ — at the Bochner boundary.

**Complex geometry — Bochner for Kähler manifolds and Kodaira vanishing.** On a compact Kähler manifold with positive bisectional curvature, the Bochner technique on $(p, q)$-forms with bundle coefficients gives **Kodaira vanishing**: $H^q(X, K_X^{-1}\otimes L) = 0$ for $q > 0$, when $L$ is positive (ample). The proof structure parallels Bochner: harmonic $L$-valued forms, Weitzenböck involving the curvature of $L$ and the metric, integration, positivity forcing vanishing.

**Mathematical physics — gauge theories on positive-Ricci backgrounds.** In Yang–Mills theory on a closed Riemannian $4$-manifold with positive Ricci curvature, the moduli space of [[Def - Instanton|instantons]] (self-dual connections) has dimension bounded by Hodge-theoretic data on the base; positive Ricci constrains $b^+_2$ and $b^-_2$ via Bochner-style arguments. For positive scalar curvature, the **Lichnerowicz–Singer theorem** says: a closed spin manifold with positive scalar curvature has no harmonic spinors. This is the spin-geometric Bochner.

---

# Bridges

- **Weitzenböck formula** — the foundational identity for the Bochner technique. On $1$-forms, $\Delta = \nabla^*\nabla + \operatorname{Ric}$; on $k$-forms, $\Delta = \nabla^*\nabla + R_k$ for an explicit curvature operator $R_k$ involving the Riemann tensor (Lichnerowicz formula). The Bochner technique applies whenever $R_k \geq 0$, forcing harmonic forms in degree $k$ to be parallel and (in the strict case) to vanish.

- **[[Thm - Harmonic Forms Represent de Rham Cohomology|Hodge isomorphism]]** — the bridge from vanishing of harmonic forms to vanishing of cohomology. Without the Hodge isomorphism, Bochner only gives an analytic statement; with it, Bochner becomes a topological constraint.

- **Myers's theorem** — on a closed Riemannian manifold with $\operatorname{Ric} \geq (n-1)k > 0$, the diameter is $\leq \pi/\sqrt{k}$, and the fundamental group is finite. Combined with Bochner, this gives **strong topological restrictions on positive-Ricci closed manifolds**: $\pi_1$ finite and $b_1 = 0$, so $H_1(M; \mathbb{Z})$ is finite.

- **Kodaira vanishing theorem** — the Bochner technique applied to Hermitian holomorphic line bundles on compact Kähler manifolds. For an ample line bundle $L$, $H^q(X, L \otimes \Omega^p) = 0$ for $p + q > \dim X$. The proof: take a $\bar\partial$-harmonic $L$-valued $(p, q)$-form, apply the bundle Weitzenböck (Bochner–Kodaira–Nakano formula), use the positivity of $L$'s Chern curvature to force vanishing. Kodaira vanishing is the algebraic-geometric Bochner.

- **Lichnerowicz formula and harmonic spinors** — on a spin manifold, the Dirac operator $D$ satisfies $D^2 = \nabla^*\nabla + \frac{1}{4}\mathrm{scal}$ (Lichnerowicz). For positive scalar curvature, $D^2$ is positive, forcing harmonic spinors to vanish. This is the spin analog of Bochner, and is the input to the **Lichnerowicz–Singer theorem** on closed spin manifolds with positive scalar curvature having $\hat A(M) = 0$ — a topological invariant computable from Pontryagin classes.

---

# Unlocked by This

> [!tip] Bochner Technique and Vanishing Theorems *(from Geometric Analysis)*
> The Bochner technique generalizes far beyond the original Bochner theorem. Every "curvature-positivity kills cohomology" theorem in geometry follows this pattern: harmonic representative + Weitzenböck-style identity + curvature positivity + integration on closed manifold $\Rightarrow$ vanishing. The litany includes: **Kodaira vanishing** (positive line bundles kill $H^q(X, L\otimes\Omega^p)$ for $p+q>\dim X$); **Akizuki–Nakano vanishing** (refined Kodaira); **Bochner–Kodaira–Nakano formula** (Hermitian holomorphic line bundles); **Lichnerowicz–Singer** (positive scalar curvature kills harmonic spinors); **Yano's theorem** (positive Ricci kills harmonic vector fields); many more. Each is a specific instance of the same template.

> [!tip] Curvature-Topology Inequalities in the Style of Synge *(from Riemannian Geometry)*
> Bochner's theorem fits into a larger family of curvature-topology inequalities. **Synge's theorem**: a closed orientable even-dimensional manifold with positive sectional curvature is simply connected. **Bonnet–Myers**: positive lower Ricci bound implies compact and finite $\pi_1$. **Cartan–Hadamard**: nonpositive sectional curvature on a simply connected manifold implies it is diffeomorphic to $\mathbb{R}^n$. Each theorem extracts topological information from curvature, by different techniques. Bochner is the curvature-Betti version; Synge and Bonnet–Myers are curvature-$\pi_1$ versions; Cartan–Hadamard is curvature-diffeomorphism.

> [!tip] Witten's Supersymmetric Bochner Technique *(from Mathematical Physics)*
> Witten reinterpreted the Bochner technique in terms of **supersymmetric quantum mechanics on a manifold**. The Hodge Laplacian is the supersymmetric Hamiltonian; harmonic forms are the supersymmetric vacua (zero-energy ground states); the supersymmetry algebra implies the index $\sum_k(-1)^k\dim\mathcal{H}^k = \chi(M)$ is invariant under deformations of the theory. The Bochner technique becomes a *deformation* argument: deform the Hamiltonian by a Morse function $f$, getting a one-parameter family of Hamiltonians; the spectrum becomes localized at the critical points of $f$ in the large-deformation limit, giving the **Morse inequalities** $b_k \leq c_k(f)$ via a curvature-positivity-style argument on the deformed Hamiltonian.

> [!tip] Ricci Flow and Topology *(from Geometric Analysis)*
> The Bochner technique provides static topological obstructions from curvature. **Ricci flow** is a dynamic version: evolve a metric by $\partial_t g = -2\operatorname{Ric}$, hoping that the flow converges to a metric of definite curvature, which then gives topological constraints by Bochner. Hamilton's program, completed by Perelman, used Ricci flow to prove the **Poincaré conjecture** (every simply connected closed $3$-manifold is $S^3$) and the **geometrization conjecture** (every closed $3$-manifold decomposes into pieces with one of eight geometries). The Bochner-style monotonicity formulas (entropy, reduced volume) are central tools — Perelman's $W$-entropy is a beautiful application of the Bochner technique in the flow setting.
