---
type: theorem
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Symplectic Vector Space"
  - "Def - Closed and Exact Forms"
  - "Def - Flow of a Vector Field"
  - "Def - Lie Derivative of a Differential Form"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Notation

$(M, \omega)$ is a symplectic manifold of dimension $2n$. **Darboux coordinates** are local coordinates $(q^1, \dots, q^n, p_1, \dots, p_n)$ in which $\omega = \sum_i dp_i \wedge dq^i$, the standard symplectic form on $\mathbb{R}^{2n}$. Moser's trick uses a one-parameter family of forms $\omega_t$ ($t \in [0,1]$) and a time-dependent vector field $X_t$ whose flow conjugates $\omega_0$ to $\omega_1$.

---

# Statement

> **Theorem (Darboux).** Let $(M, \omega)$ be a symplectic manifold of dimension $2n$. Around every point $p \in M$ there exists an open neighbourhood $U \ni p$ and local coordinates $(q^1, \dots, q^n, p_1, \dots, p_n) : U \to \mathbb{R}^{2n}$ — called **Darboux (or canonical) coordinates** — in which
> $$\omega\big|_U = \sum_{i=1}^n dp_i \wedge dq^i.$$
> Equivalently, every $2n$-dimensional symplectic manifold is locally symplectomorphic to $(\mathbb{R}^{2n}, \omega_0)$ with the standard symplectic form $\omega_0 = \sum dp_i \wedge dq^i$.

**Corollary (no local invariants).** Two symplectic manifolds of equal dimension are locally indistinguishable: any two points in any two such manifolds have neighbourhoods that are symplectomorphic via a chart-to-chart map. In particular, **symplectic geometry has no local invariants** — no symplectic analogue of curvature.

---

# Motivation

Darboux's theorem is the structural watershed of symplectic geometry. It says that **everything interesting in symplectic geometry is global**: there are no local quantities (no analogue of curvature) by which two symplectic manifolds can be distinguished. This is a dramatic contrast with Riemannian geometry, where the local data (Riemann curvature tensor) completely determines the local structure and two Riemannian manifolds are locally isomorphic only when their curvatures agree pointwise.

The reason for this dichotomy is the closedness axiom $d\omega = 0$. In Riemannian geometry, the metric $g$ is a tensor field with no integrability condition imposed, and its curvature is a genuine local invariant. In symplectic geometry, the form $\omega$ satisfies $d\omega = 0$ — an integrability condition that is exactly what allows the local trivialization to standard form. Without closedness (in **almost-symplectic** geometry), there are local invariants and no Darboux theorem.

The historical role of Darboux's theorem is foundational: it justifies the universal use of canonical coordinates $(q^i, p_i)$ in classical mechanics. Hamilton's equations $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$ are not just a coordinate formula for a specific phase space — they are the **universal local form** of Hamiltonian dynamics on *any* symplectic manifold. The proof of Darboux's theorem is what allows us to write Hamilton's equations in this canonical form everywhere.

The modern proof of Darboux's theorem is **Moser's trick** (Jürgen Moser, 1965), a deformation argument that has become one of the most-used techniques in symplectic geometry. The idea: deform the given symplectic form $\omega$ to the standard form $\omega_0$ along a path $\omega_t = (1-t)\omega_0 + t\omega$ of symplectic forms (or some similar interpolation), find a time-dependent vector field $X_t$ whose flow $\phi_t$ pulls $\omega_t$ back to $\omega_0$, and use $\phi_1$ as the desired symplectomorphism. The technique generalizes to many uniqueness theorems in symplectic geometry: the **Moser stability theorem** (symplectic forms in the same cohomology class are isotopic), the **Weinstein neighbourhood theorem** for Lagrangian submanifolds, and others.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis of Darboux's theorem is mild: any symplectic manifold $(M, \omega)$. The interesting question is what kinds of conditions and structures imply you're working with a symplectic manifold — sometimes non-obviously.

**Source: a closed nondegenerate 2-form.** This is the direct hypothesis: $d\omega = 0$ and $\omega$ nondegenerate. Verifying these two algebraic-and-differential conditions makes Darboux applicable. The bridge is direct: just check the two axioms. *Example use:* given a 2-form on a cotangent bundle that is exact ($\omega = -d\theta$ for some $\theta$), closedness is automatic; check nondegeneracy in coordinates and apply Darboux.

**Source: a cotangent bundle $T^*Q$.** Every cotangent bundle is canonically symplectic ([[Def - The Canonical Symplectic Form on a Cotangent Bundle]]) with $\omega = -d\theta$. So Darboux's theorem applies, and in fact the canonical coordinates $(q^i, p_i)$ on $T^*Q$ inherited from coordinates $(q^i)$ on $Q$ are *already* Darboux coordinates — no further work needed. *Example use:* working on the phase space of any mechanical system, you automatically have Darboux coordinates.

**Source: an oriented Riemannian surface.** Every oriented Riemannian $2$-manifold has a symplectic form: its area form. Darboux says these are all locally $(\mathbb{R}^2, dx \wedge dy)$. The bridge: closedness is automatic in dimension $2$ (no $3$-forms exist), and nondegeneracy is the assumption of non-vanishing. *Example use:* the area form on $S^2$ is locally just $dx \wedge dy$ (in stereographic coordinates), making symplectic computations elementary.

**Source: a Kähler manifold.** A Kähler manifold has compatible symplectic, complex, and Riemannian structures, with the imaginary part of the Hermitian metric being the symplectic form. Darboux applies — and in fact every Kähler manifold is *locally* $(\mathbb{C}^n, h_0)$ with the standard Hermitian metric, by a stronger theorem combining Darboux with the existence of holomorphic local coordinates. *Example use:* working on $\mathbb{CP}^n$ with the Fubini–Study metric, Darboux coordinates exist around every point and look like the standard $(\mathbb{C}^n, \omega_0)$.

**Source: an almost-complex manifold with vanishing Nijenhuis tensor.** By the Newlander–Nirenberg theorem, such a manifold is complex. If furthermore it carries a compatible nondegenerate closed 2-form, it is Kähler, hence Darboux applies. *Example use:* recognizing complex structures often reveals symplectic structure.

**Targets (Output Amplification).**

Darboux's theorem produces local coordinates in which $\omega$ has standard form, with several powerful consequences when combined with other tools.

**Target + computational simplicity = trivial local formulas for $X_H$, $\{f,g\}$, $\omega^n$.** Once you have Darboux coordinates, the entire calculus simplifies dramatically: $X_H = (\partial H/\partial p_i)\partial_{q^i} - (\partial H/\partial q^i)\partial_{p_i}$, $\{f,g\} = \partial_{q^i}f \partial_{p_i}g - \partial_{p_i}f \partial_{q^i}g$, $\omega^n/n! = dq^1 \wedge \cdots \wedge dq^n \wedge dp_1 \wedge \cdots \wedge dp_n$. All abstract symplectic computations become coordinate computations. *Combination use:* a local question about a symplectic manifold reduces to a calculation on $\mathbb{R}^{2n}$, which can be done by undergraduate calculus.

**Target + Hamiltonian = local form of Hamilton's equations.** Once Darboux coordinates exist locally, Hamilton's equations $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$ are the local form of Hamiltonian dynamics on every symplectic manifold. This is the universal status of Hamilton's equations. *Combination use:* studying a local dynamical question on any symplectic manifold reduces to studying the corresponding ODE on $\mathbb{R}^{2n}$.

**Target + invariance under symplectomorphisms = symplectomorphisms permute Darboux coordinates.** Two Darboux coordinate systems on the same neighbourhood are related by a symplectomorphism. So the entire local theory of symplectomorphisms can be developed in standard coordinates, and questions about "the symplectic structure up to local equivalence" reduce to questions about the symplectic group $\mathrm{Sp}(2n, \mathbb{R})$. *Combination use:* classifying local symplectic phenomena (e.g., germs of Lagrangian submanifolds at a point) reduces to representation theory of $\mathrm{Sp}(2n, \mathbb{R})$.

**Target + Moser's trick = uniqueness of symplectic structures in same cohomology class.** Generalizing Darboux, **Moser's stability theorem** says that two symplectic forms $\omega_0, \omega_1$ on a closed manifold $M$, with $[\omega_0] = [\omega_1] \in H^2_{dR}(M)$ and connected by a path of symplectic forms, are *globally* symplectomorphic. The proof uses the same Moser trick — extend Darboux from local to global. *Combination use:* classify symplectic structures by cohomology class plus isotopy class, reducing the classification to (topological) cohomology theory.

---

# Why Is It True

**The mechanism in one sentence:** *the closedness $d\omega = 0$ provides exactly the integrability condition needed to "flatten" the symplectic form to standard form by an integrating diffeomorphism.*

Here is the intuition. Suppose we want to bring a closed nondegenerate 2-form $\omega$ to the standard form $\omega_0 = \sum dp_i \wedge dq^i$ on $\mathbb{R}^{2n}$ via some diffeomorphism $\phi$. We need $\phi^*\omega = \omega_0$, or equivalently (after working with $\phi^{-1}$) $\phi^*\omega_0 = \omega$. The construction proceeds by interpolation: deform $\omega_0$ to $\omega$ along a smooth path $\omega_t$ of symplectic forms, then find a time-dependent vector field $X_t$ whose flow $\phi_t$ realizes the deformation, so that $\phi_t^*\omega_t = \omega_0$ for all $t \in [0, 1]$. At $t = 1$ we have $\phi_1^*\omega = \omega_0$, the desired symplectomorphism.

Differentiating $\phi_t^*\omega_t = \omega_0$ with respect to $t$ and using the formula $d/dt(\phi_t^*\omega_t) = \phi_t^*(\mathcal{L}_{X_t}\omega_t + \partial\omega_t/\partial t)$, we get the condition $\mathcal{L}_{X_t}\omega_t + \partial\omega_t/\partial t = 0$. By Cartan's magic formula and closedness of $\omega_t$ (which we ensure by choosing the path of symplectic forms), $\mathcal{L}_{X_t}\omega_t = d\iota_{X_t}\omega_t$. So we need

$$d\iota_{X_t}\omega_t = -\frac{\partial\omega_t}{\partial t}.$$

The right-hand side is the derivative of the path $\omega_t$, which is itself a closed 2-form (the path lies in the space of closed forms). For the equation to be solvable for $X_t$, we need $-\partial\omega_t/\partial t$ to be **exact**, say $-\partial\omega_t/\partial t = d\sigma_t$ for some 1-form $\sigma_t$. Then we just set $\iota_{X_t}\omega_t = \sigma_t$, which is solvable for $X_t$ because $\omega_t$ is nondegenerate.

This is the **Moser trick**. The key technical point: locally (in a Darboux chart) we can ensure the exactness $-\partial\omega_t/\partial t = d\sigma_t$ by the **Poincaré lemma** — every closed form on a contractible region is exact. Globally, we would need cohomological vanishing, which is the content of Moser's stability theorem.

**Why does this work specifically for symplectic forms?** Because:
1. Nondegeneracy lets us solve $\iota_{X_t}\omega_t = \sigma_t$ for $X_t$, given $\sigma_t$ (the symplectic-form-to-vector-field isomorphism).
2. Closedness lets us reduce $\mathcal{L}_{X_t}\omega_t$ to $d\iota_{X_t}\omega_t$ via Cartan, eliminating the $\iota_{X_t}d\omega_t$ term.
3. The Poincaré lemma provides the local primitive $\sigma_t$ of the exact form $-\partial\omega_t/\partial t$.

Without closedness, step (2) fails and an extra $\iota_{X_t}d\omega_t$ term remains, which cannot be cancelled. Without nondegeneracy, step (1) fails and $X_t$ cannot be uniquely defined. Both axioms are essential.

**For symplectic vector spaces (the linear case), the analog of Darboux is much easier**: it is the **linear Darboux theorem** (existence of a symplectic basis), proved by a Gram–Schmidt-like induction. Pick a nonzero $v_1$, find $u_1$ with $\omega(v_1, u_1) = 1$ (possible by nondegeneracy), restrict to the orthogonal complement $\mathrm{span}(v_1, u_1)^\omega$ (which is $(2n-2)$-dimensional and still symplectic), and iterate. The resulting basis $(v_1, \dots, v_n, u_1, \dots, u_n)$ is a symplectic basis. **Darboux's theorem is the manifold version of the linear Darboux theorem, with the integrability via Moser providing the smoothness.**

---

# What Makes This Hard

The conceptual leap is realizing that the entire proof reduces to **solving an ODE for a time-dependent vector field whose flow conjugates two forms** — the Moser trick. Most people, encountering Darboux for the first time, try to prove it by an explicit coordinate construction (à la Gram–Schmidt) and run into the difficulty that the coordinates have to be *smooth* and *consistent across the patch*. The non-obvious step is to recognize that the consistency of coordinates is exactly the integrability of a vector field, and that this integrability is provided by closedness + Poincaré lemma. The most common error is to forget that the Poincaré lemma is local (requires contractibility) — Moser's trick proves Darboux *locally* for this reason, and the global generalization (Moser stability) requires additional cohomological hypotheses.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use the **Moser trick**: deform the given $\omega$ to the standard form $\omega_0$ along a path $\omega_t$ in the space of closed nondegenerate 2-forms, find a time-dependent vector field $X_t$ whose flow $\phi_t$ realizes the deformation (so $\phi_t^*\omega_t = \omega_0$ for all $t$), and conclude $\phi_1^*\omega = \omega_0$ — the diffeomorphism we want.

**Subgoal decomposition:**

1. **Reduction to a linear question at a point.** Use the linear Darboux theorem (existence of a symplectic basis of $T_pM$) to choose coordinates $(q^i, p_i)$ around $p$ such that $\omega|_p = \sum_i dp_i \wedge dq^i|_p$ — i.e., the symplectic form equals the standard one *at the single point $p$*.
   - *Hint:* this is pure linear algebra (Gram–Schmidt on the tangent space).
   - *Why needed:* gives a starting point where $\omega$ and $\omega_0$ agree.

2. **Setup the Moser path.** Define $\omega_t := \omega_0 + t(\omega - \omega_0)$ for $t \in [0, 1]$, where $\omega_0$ is the standard form in the coordinates from step 1. Then $\omega_0 = \omega_0$, $\omega_1 = \omega$, and at $p$ we have $\omega_t|_p = \omega_0|_p$ for all $t$ (since $\omega|_p = \omega_0|_p$). In a small enough neighbourhood of $p$, $\omega_t$ is still nondegenerate by continuity.
   - *Hint:* affine interpolation between two closed forms gives a path of closed forms.
   - *Why needed:* gives a path of symplectic forms from $\omega_0$ to $\omega$.

3. **Find the primitive 1-form $\sigma_t$.** The derivative $\partial\omega_t/\partial t = \omega - \omega_0$ is a closed form (difference of two closed forms). On a contractible neighbourhood of $p$, by the **Poincaré lemma**, $\omega - \omega_0 = d\beta$ for some 1-form $\beta$. Define $\sigma_t := -\beta$ (so $d\sigma_t = -(\omega - \omega_0) = -\partial\omega_t/\partial t$).
   - *Hint:* Poincaré lemma — on a star-shaped region every closed form is exact.
   - *Why needed:* provides the right-hand side of the Moser equation.

4. **Solve for $X_t$ via nondegeneracy.** Define $X_t$ pointwise by $\iota_{X_t}\omega_t = \sigma_t$. This has a unique smooth solution $X_t$ because $\omega_t$ is nondegenerate.
   - *Hint:* $\omega_t$ nondegenerate, $\sigma_t$ given, solve for $X_t$.
   - *Why needed:* defines the vector field whose flow we will use.

5. **Integrate to get a flow $\phi_t$.** Solve the ODE $d\phi_t/dt = X_t \circ \phi_t$ with $\phi_0 = \mathrm{id}$, on a small enough neighbourhood of $p$ and small enough time interval (we'll need $t = 1$). Since at $p$ we have $X_t|_p = 0$ (because $\sigma_t|_p = 0$ from $\omega|_p = \omega_0|_p$), the flow $\phi_t$ fixes $p$ and is defined for $t \in [0, 1]$ in a neighbourhood.
   - *Hint:* standard ODE existence theory.
   - *Why needed:* gives the diffeomorphism realizing the deformation.

6. **Verify $\phi_t^*\omega_t = \omega_0$.** Compute $\frac{d}{dt}(\phi_t^*\omega_t) = \phi_t^*(\mathcal{L}_{X_t}\omega_t + \partial\omega_t/\partial t) = \phi_t^*(d\iota_{X_t}\omega_t + \partial\omega_t/\partial t) = \phi_t^*(d\sigma_t + \partial\omega_t/\partial t) = \phi_t^*(-(omega - \omega_0) + (\omega - \omega_0)) = 0$, using Cartan's magic formula and $d\omega_t = 0$. So $\phi_t^*\omega_t$ is constant in $t$, hence equals $\phi_0^*\omega_0 = \omega_0$.
   - *Hint:* Cartan's magic formula, closedness of $\omega_t$, and the definitions of $X_t$ and $\sigma_t$.
   - *Why needed:* shows the flow gives the desired symplectomorphism.

7. **Conclude.** At $t = 1$: $\phi_1^*\omega = \phi_1^*\omega_1 = \omega_0$. So $\phi_1$ is a local diffeomorphism (in a neighbourhood of $p$, fixing $p$) with $\phi_1^*\omega = \omega_0$ — i.e., $\phi_1$ is a local symplectomorphism. Pulling back coordinates via $\phi_1$ gives Darboux coordinates for $\omega$.
   - *Hint:* the construction is complete.
   - *Why needed:* delivers the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Linear Darboux theorem
> **Statement:** Every $2n$-dimensional symplectic vector space $(V, \omega)$ admits a basis $(e_1, \dots, e_n, f_1, \dots, f_n)$ with $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$ and $\omega(e_i, f_j) = \delta_{ij}$.
>
> **Hint:** Gram–Schmidt-like induction on $\dim V$.
>
> **Why needed:** Provides the starting point where $\omega$ equals the standard form $\omega_0$ at the chosen point $p$.
>
> > [!note]- Full proof
> > By induction on $n$. For $n = 0$, $V = 0$ and there is nothing to prove. For $n \geq 1$: pick any nonzero $v \in V$. By nondegeneracy, there exists $u \in V$ with $\omega(v, u) = 1$ (rescale if needed). Note $v \neq u$ (else $\omega(v, v) = 1 \neq 0$ contradicts antisymmetry $\omega(v,v) = 0$). Set $e_1 = v$, $f_1 = u$.
> >
> > Let $W = \{w \in V : \omega(w, e_1) = \omega(w, f_1) = 0\}$. We claim $V = \mathrm{span}(e_1, f_1) \oplus W$ and $W$ is symplectic of dimension $2n - 2$.
> >
> > For the decomposition: given $x \in V$, set $a = \omega(x, f_1)$, $b = -\omega(x, e_1)$, $w = x - ae_1 - bf_1$. Compute $\omega(w, e_1) = \omega(x, e_1) - b\omega(f_1, e_1) = \omega(x, e_1) - b(-1) = \omega(x, e_1) + b = 0$. Similarly $\omega(w, f_1) = 0$. So $w \in W$. Uniqueness follows from the formula for $(a, b)$.
> >
> > For $W$ symplectic: $\omega|_W$ is the restriction of an antisymmetric form, hence antisymmetric. For nondegeneracy: if $w \in W$ and $\omega(w, w') = 0$ for all $w' \in W$, then together with $\omega(w, e_1) = \omega(w, f_1) = 0$ we get $\omega(w, V) = 0$, hence $w = 0$ by nondegeneracy of $\omega$ on $V$.
> >
> > By induction, $W$ has a symplectic basis $(e_2, \dots, e_n, f_2, \dots, f_n)$. Combining gives the symplectic basis $(e_1, \dots, e_n, f_1, \dots, f_n)$ of $V$.

> [!note]- Lemma 2: Poincaré lemma on a contractible region
> **Statement:** Let $U \subseteq \mathbb{R}^{2n}$ be a star-shaped open region. Then every closed $k$-form on $U$ is exact: $d\beta = 0 \implies \beta = d\eta$ for some $(k-1)$-form $\eta$ on $U$.
>
> **Hint:** Explicit construction via a contracting homotopy.
>
> **Why needed:** Provides the primitive 1-form $\beta$ with $d\beta = \omega - \omega_0$ in step 3 of the rederivation scaffold.
>
> > [!note]- Full proof
> > Standard; see [[Thm - The Poincaré Lemma]]. The construction: if $U$ is star-shaped at $p$, define the homotopy $h_t(x) = p + t(x - p)$, a retraction to $\{p\}$, and use the explicit homotopy operator $\eta := \int_0^1 \iota_{X_t}(h_t^*\beta) dt$ where $X_t = (x - p)/t$ (radial vector field). Then $d\eta + \eta d = \mathrm{id}$ on positive-degree forms (homotopy invariance of de Rham cohomology), so $d\beta = 0$ implies $\beta = d\eta + \eta(d\beta) = d\eta$.

> [!note]- Lemma 3: The Moser equation has a unique smooth solution $X_t$
> **Statement:** Given a smooth path $\omega_t$ of closed nondegenerate 2-forms and a smooth path $\sigma_t$ of 1-forms with $d\sigma_t = -\partial\omega_t/\partial t$, the equation $\iota_{X_t}\omega_t = \sigma_t$ has a unique smooth solution $X_t$ as a time-dependent vector field.
>
> **Hint:** Nondegeneracy of $\omega_t$ provides the bundle isomorphism $TM \to T^*M$.
>
> **Why needed:** Defines the vector field whose flow conjugates $\omega_0$ to $\omega_t$.
>
> > [!note]- Full proof
> > The map $X \mapsto \iota_X\omega_t$ is a bundle isomorphism $TM \to T^*M$ at each point (because $\omega_t$ is nondegenerate). Smooth dependence on $t$ is inherited from the smoothness of $\omega_t$ and $\sigma_t$. So $X_t := (\omega_t^\flat)^{-1}(\sigma_t)$ is a smooth time-dependent vector field, satisfying $\iota_{X_t}\omega_t = \sigma_t$ by construction. Uniqueness is automatic from the isomorphism.

> [!note]- Lemma 4: The flow $\phi_t$ exists for $t \in [0, 1]$ near $p$
> **Statement:** The flow of the time-dependent vector field $X_t$ exists for $t \in [0, 1]$ in some neighbourhood of $p$, with $\phi_t(p) = p$ (the flow fixes $p$).
>
> **Hint:** Standard ODE existence theorem; use that $X_t|_p = 0$.
>
> **Why needed:** Provides the symplectomorphism $\phi_1$ realizing the Darboux change of coordinates.
>
> > [!note]- Full proof
> > At the point $p$, we have $\omega_t|_p = \omega|_p = \omega_0|_p$ (since at $p$ the original form already equals the standard form), so $\partial\omega_t/\partial t|_p = 0$. By choice of $\beta$ in the Poincaré lemma — which has $\beta|_p = 0$ — we have $\sigma_t|_p = 0$. From $\iota_{X_t}\omega_t = \sigma_t$ and nondegeneracy, $X_t|_p = 0$.
> >
> > So $p$ is a stationary point of $X_t$ for all $t$, and the flow $\phi_t$ fixes $p$. The standard ODE existence theorem (for time-dependent vector fields with continuous time-dependence) then gives existence of $\phi_t$ for $t$ in a neighbourhood of $0$, in a neighbourhood of $p$. Since $X_t$ vanishes at $p$, the flow does not "blow up" near $p$, and we can extend it to $t \in [0, 1]$.

---

# Formal Proof

> [!note]- Complete formal proof (Moser's trick)
> Let $(M, \omega)$ be a symplectic manifold of dimension $2n$, and let $p \in M$ be the point around which we seek Darboux coordinates.
>
> **Step 0 — Well-posedness.** We construct local coordinates in a contractible (in fact convex) neighbourhood of $p$. Working in a chart around $p$ identifying a neighbourhood with an open subset of $\mathbb{R}^{2n}$, we may assume $M = \mathbb{R}^{2n}$ near $p$, with $p$ corresponding to the origin. The neighbourhood will be shrunk as needed.
>
> **Step 1 — Linear normalization.** Apply Lemma 1 to the tangent space $T_pM$: choose a symplectic basis $(e_1, \dots, e_n, f_1, \dots, f_n)$. Choose linear coordinates $(q^i, p_i)$ on $\mathbb{R}^{2n}$ adapted to this basis, so that $\partial_{q^i}|_p = e_i$, $\partial_{p_j}|_p = f_j$. Then $\omega|_p = \sum_i dp_i \wedge dq^i|_p = \omega_0|_p$, the standard form at $p$.
>
> **Step 2 — Moser path.** Define the path of $2$-forms
> $$\omega_t := (1 - t)\omega_0 + t\omega, \qquad t \in [0, 1].$$
> Each $\omega_t$ is closed (linear combination of closed forms), and at $p$ it equals $\omega_0|_p = \omega|_p$. By continuity of $\omega_t$ in $t$ and of nondegeneracy in $t$ (a closed condition on the determinant), $\omega_t$ is nondegenerate in some neighbourhood of $p$ for all $t \in [0, 1]$. Shrink the neighbourhood so this holds throughout.
>
> **Step 3 — Primitive 1-form via Poincaré.** The form $\omega - \omega_0$ is closed (both forms are closed) and vanishes at $p$. On a star-shaped neighbourhood of $p$ in $\mathbb{R}^{2n}$, by Lemma 2 (Poincaré lemma), $\omega - \omega_0 = d\beta$ for some smooth 1-form $\beta$. We may furthermore arrange $\beta|_p = 0$ by adding to $\beta$ a constant 1-form: replacing $\beta$ by $\beta - \beta|_p$ keeps the equation $d\beta = \omega - \omega_0$ valid and ensures $\beta|_p = 0$. (Alternatively, the explicit Poincaré primitive $\beta = \int_0^1 \iota_{X_s}(h_s^*(\omega - \omega_0))ds$ with the radial homotopy $h_s(x) = sx$ vanishes at $p = 0$.)
>
> Set $\sigma_t := -\beta$ for all $t$ (a constant 1-form in $t$, but using "$\sigma_t$" notation for clarity in the Moser equation). Then $\partial\omega_t/\partial t = \omega - \omega_0 = -d\sigma_t$, the Moser condition.
>
> **Step 4 — Vector field via nondegeneracy.** By Lemma 3, define $X_t$ as the unique smooth time-dependent vector field with $\iota_{X_t}\omega_t = \sigma_t$. By the choice $\sigma_t|_p = -\beta|_p = 0$ and the nondegeneracy of $\omega_t|_p$, we have $X_t|_p = 0$ for all $t$.
>
> **Step 5 — Flow.** By Lemma 4, the time-dependent flow $\phi_t$ of $X_t$ exists for $t \in [0, 1]$ in a (possibly smaller) neighbourhood of $p$, with $\phi_0 = \mathrm{id}$ and $\phi_t(p) = p$.
>
> **Step 6 — Verification $\phi_t^*\omega_t = \omega_0$.** Compute
> $$\frac{d}{dt}(\phi_t^*\omega_t) = \phi_t^*\left(\mathcal{L}_{X_t}\omega_t + \frac{\partial\omega_t}{\partial t}\right).$$
> By Cartan's magic formula $\mathcal{L}_{X_t}\omega_t = d\iota_{X_t}\omega_t + \iota_{X_t}d\omega_t = d\sigma_t + 0 = d\sigma_t$, using $d\omega_t = 0$ and $\iota_{X_t}\omega_t = \sigma_t$. So
> $$\frac{d}{dt}(\phi_t^*\omega_t) = \phi_t^*(d\sigma_t + (\omega - \omega_0)) = \phi_t^*(d\sigma_t - d\sigma_t) = 0,$$
> using $-d\sigma_t = \omega - \omega_0 = \partial\omega_t/\partial t$. So $\phi_t^*\omega_t$ is constant in $t$, equal to its $t = 0$ value $\phi_0^*\omega_0 = \omega_0$.
>
> **Step 7 — Conclusion.** At $t = 1$: $\phi_1^*\omega_1 = \omega_0$, i.e., $\phi_1^*\omega = \omega_0$. So $\phi_1$ is a local diffeomorphism (in a neighbourhood of $p$, fixing $p$) with $\phi_1^*\omega = \omega_0$. The Darboux coordinates for $\omega$ in this neighbourhood are then $\phi_1^{-1}$ pulled back of the linear coordinates $(q^i, p_i)$. Equivalently: defining $\tilde q^i := q^i \circ \phi_1^{-1}$ and $\tilde p_i := p_i \circ \phi_1^{-1}$, we have $\omega = \sum_i d\tilde p_i \wedge d\tilde q^i$ in these coordinates.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian / Lorentzian geometry: integrability of structures.** Compare Darboux's theorem with the **integrability theorem for almost-complex structures** (Newlander–Nirenberg) and the **flatness criterion for Riemannian metrics** (vanishing of the Riemann tensor). All three are integrability theorems: when a certain "structure" satisfies an algebraic-differential closedness condition, it is locally trivial — locally identical to the standard model. Riemannian metrics need the much stronger condition of vanishing curvature (because Riemannian geometry has nontrivial local invariants); symplectic structures need only $d\omega = 0$. Almost-complex structures need the vanishing of the Nijenhuis tensor (a $T^*M$-valued tensor).

**Algebraic topology: Reidemeister torsion and lens spaces.** While Darboux says symplectic manifolds have no local invariants, the *global* invariants are deeply interesting. The cohomology class $[\omega] \in H^2_{dR}(M)$ is the simplest; **symplectic capacities** (Hofer, Hofer–Zehnder, Gromov width) are real-valued invariants beyond cohomology; **Floer homology** is a graded-module invariant. Darboux's theorem is what makes the local theory "free" and lets all the interesting questions concentrate at the global level.

**Lie theory: Cartan–Killing forms and adjoint orbits.** The **Kirillov–Kostant–Souriau Poisson structure** on the dual $\mathfrak{g}^*$ of a Lie algebra has **coadjoint orbits** as its symplectic leaves. By Darboux, each coadjoint orbit is locally $(\mathbb{R}^{2k}, \omega_0)$ — but globally the orbits have rich structure: $S^2$ for $\mathfrak{su}(2)^*$ (the integer spheres of integer-spin representations), flag manifolds for higher groups. The **orbit method** in representation theory uses geometric quantization of these orbits to produce irreducible representations of Lie groups.

**Numerical analysis: symplectic integrators.** Computer simulations of Hamiltonian systems use **symplectic integrators** — discretization schemes that preserve the symplectic structure (or a discrete analogue thereof) at each timestep. The reason these schemes have superior long-time stability is essentially Darboux's theorem: locally, every symplectic manifold is $\mathbb{R}^{2n}$, and the discretization respects this local structure. Non-symplectic integrators (e.g., standard Runge–Kutta) accumulate spurious dissipation over long times, violating energy conservation; symplectic integrators preserve a slightly perturbed Hamiltonian exactly, giving correct qualitative behavior on exponential timescales.

---

# Bridges

- **[[Thm - Hamiltonian Flows are Symplectomorphisms]]**: this is a *global* fact about Hamiltonian flows preserving $\omega$, derived from Cartan's magic formula. Darboux's theorem is a complementary *local* fact: regardless of what the global Hamiltonian flow looks like, in any Darboux chart the dynamics is just Hamilton's equations on $\mathbb{R}^{2n}$. Together they say "Hamiltonian dynamics looks the same in every local chart and preserves the local structure globally".

- **[[Thm - Liouville's Theorem on Phase Space Volume]]**: Liouville's theorem in Darboux coordinates becomes the trivial statement "the Lebesgue measure on $\mathbb{R}^{2n}$ is preserved by Hamilton's equations", which can be verified by direct calculation. Without Darboux, the volume form $\omega^n/n!$ requires care to interpret on a general symplectic manifold; with Darboux, it's just $dq^1 \cdots dq^n dp_1 \cdots dp_n$.

- **The Newlander–Nirenberg theorem** (from complex differential geometry): integrability of an almost-complex structure ($N_J = 0$) makes it locally a complex structure (locally biholomorphic to $\mathbb{C}^n$). This is a structural analogue of Darboux: a closedness condition (vanishing Nijenhuis tensor) makes a local structure (almost-complex) integrate to a flat model (complex coordinates). The proof techniques are very different (Newlander–Nirenberg uses elliptic PDE), but the conceptual statements are parallel.

- **The Moser stability theorem** (the global version of Darboux): two symplectic forms $\omega_0, \omega_1$ on a closed manifold $M$ with $[\omega_0] = [\omega_1] \in H^2_{dR}(M)$ and connected by a path of symplectic forms are globally symplectomorphic. The proof is essentially the same Moser trick, with the Poincaré lemma replaced by the cohomological condition $[\omega_1 - \omega_0] = 0 \in H^2_{dR}(M)$ (which lets you find the global primitive). Darboux is the *local* case where $M$ is contractible (a chart) and the cohomological hypothesis is automatic.

- **The Weinstein neighbourhood theorem** for Lagrangian submanifolds: every Lagrangian $L \subset (M, \omega)$ has a tubular neighbourhood symplectomorphic to a neighbourhood of the zero section in $(T^*L, \omega_{T^*L})$. This is a Lagrangian-relative version of Darboux: it normalizes the symplectic structure near a Lagrangian, just as Darboux normalizes it near a point. The proof again uses Moser's trick.

---

# Unlocked by This

> [!tip] No Local Symplectic Invariants — All Interesting Symplectic Geometry is Global *(Foundational)*
> Darboux's theorem is the structural statement that **symplectic geometry has no local invariants**. There is no symplectic analogue of curvature, no symplectic curvature tensor. All distinctions between symplectic manifolds are global. This is the founding insight of **symplectic topology** as a subject distinct from differential geometry: the central questions are about cohomology classes, intersections of Lagrangians, fixed points of symplectomorphisms, capacities — all global. Even within "symplectic geometry proper", the questions are about global existence of symplectomorphisms, global moment maps, global generating functions. The local theory is "trivial" (just $\mathbb{R}^{2n}$ everywhere), so all the depth concentrates globally.

> [!tip] Moser's Trick as a Universal Method *(from Symplectic Topology)*
> The technique used to prove Darboux — Moser's trick — generalizes to a host of uniqueness theorems in symplectic geometry, beyond Darboux itself:
> - **Moser stability:** symplectic forms in the same cohomology class connected by a path are globally symplectomorphic.
> - **Weinstein neighbourhood theorem:** Lagrangian submanifolds have standard tubular neighbourhoods.
> - **Weinstein isotropic embedding theorem:** isotropic submanifolds can be extended to Lagrangians.
> - **Symplectic neighborhoods of points / submanifolds:** various refinements of Darboux relative to submanifolds.
>
> The pattern is universal: "deform a structure to a standard one along a path, integrate the time-dependent vector field whose flow realizes the deformation, conclude that the time-1 map is the desired diffeomorphism". This is the workhorse argument of the subject.

> [!tip] Symplectic Integrators in Numerical Analysis *(from Computational Physics)*
> The local triviality from Darboux's theorem motivates **symplectic integration schemes** for numerically solving Hamilton's equations. A symplectic integrator is a discretization that preserves a discrete analogue of the symplectic form at each timestep. The simplest example is the **leap-frog scheme** for separable Hamiltonians $H = T(p) + V(q)$: $p_{n+1/2} = p_n - (h/2)\nabla V(q_n)$, $q_{n+1} = q_n + h \nabla T(p_{n+1/2})$, $p_{n+1} = p_{n+1/2} - (h/2)\nabla V(q_{n+1})$. This scheme preserves the symplectic structure exactly and has superior long-time stability: in the solar system simulation over billions of years, symplectic integrators give qualitatively correct planetary orbits while non-symplectic methods exhibit spurious energy drift. The **backward error analysis** explains why: a symplectic integrator solves *exactly* a Hamiltonian system whose Hamiltonian is a small perturbation of the original — and the perturbed Hamiltonian inherits all the qualitative dynamical properties of the original.
