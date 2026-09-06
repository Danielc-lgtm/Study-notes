---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Fibre Bundle"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, principal-bundles]
---

# Notation

For a principal $G$-bundle $\pi : P \to M$, the right action of $g \in G$ is $u \mapsto u \cdot g = R_g(u)$. A local section is $s_U : U \to P$ with $\pi \circ s_U = \mathrm{id}_U$; the corresponding local trivialization is $\Phi_U^{-1}(p, g) = s_U(p) \cdot g$. The fibre over $p$ is $\pi^{-1}(p)$, a $G$-orbit, diffeomorphic to $G$ once a basepoint is chosen. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the registry.

---

# Statement

> **Theorem (Frankel 17.8 + equivalence of formulations).** Let $\pi : P \to M$ be a principal $G$-bundle in the fibre-bundle sense — i.e., a fibre bundle whose typical fibre is $G$ and whose transition functions act on $F = G$ by left translation. Then:
>
> 1. The structure group $G$ acts on $P$ from the right by a smooth action $P \times G \to P$, $(u, g) \mapsto u \cdot g$.
> 2. The right action is **free**: $u \cdot g = u$ implies $g = e$.
> 3. The right action **preserves fibres**: $\pi(u \cdot g) = \pi(u)$.
> 4. The right action is **transitive on each fibre**: if $\pi(u) = \pi(v)$, then $v = u \cdot g$ for a unique $g \in G$.
> 5. **Local sections of $\pi$ correspond bijectively to local trivializations**, via $\Phi_U^{-1}(p, g) = s_U(p) \cdot g$.
>
> Conversely, given a smooth manifold $P$ with a smooth, free, proper right $G$-action whose orbit space $P/G$ inherits a smooth manifold structure such that $\pi : P \to P/G$ is a submersion, then $\pi : P \to M := P/G$ is a principal $G$-bundle in the fibre-bundle sense.

> **Corollary.** A principal $G$-bundle admits a global section if and only if it is trivial (isomorphic to $M \times G$).

---

# Motivation

This theorem says the **right $G$-action on a principal bundle is intrinsic and globally defined**, not requiring any choice of trivialization. This is the conceptual payoff of working with principal bundles: the structure group acts on the *total space* of the principal bundle in a canonical, gauge-independent way, even though the corresponding action on the fibre of an associated vector bundle is gauge-dependent. The theorem also gives the converse — a free smooth right $G$-action with smooth orbit space is automatically a principal bundle — which is the constructive route to building principal bundles. Whenever you have such an action, you have a principal bundle for free.

The deeper significance is the **equivalence of two definitions**: the "fibre bundle with structure group acting by left translation" (good for transition-function calculations) and the "manifold with free right $G$-action" (good for global structural questions). Different problems want different formulations, and the theorem says we can switch between them costlessly.

---

# Sources and Targets

**Sources (input broadening).**

*Source 1: A fibre bundle $\pi : P \to M$ with typical fibre $G$ and structure group $G$ acting by left translation.* This is the definition of a principal bundle as a fibre bundle. The theorem applies to any such bundle automatically. The B → A bridge is trivial here — the theorem starts directly from this hypothesis.

*Source 2: A smooth manifold $P$ with a free smooth right $G$-action whose orbit space is Hausdorff and smooth.* By the converse direction of the theorem, this is also a principal bundle. The B → A bridge requires *properness* of the action: freeness alone is not enough for Hausdorff orbit space (the irrational-winding-on-the-torus example). The Hausdorff and smoothness of $P/G$ are guaranteed by **properness** of the action (preimages of compact sets compact under $(u, g) \mapsto (u, u\cdot g)$), and in nice cases (compact $G$ acting on a manifold) properness is automatic. So the practical source is "free action of a compact Lie group on a smooth manifold" or "free proper action of any Lie group."

*Source 3: A transitive smooth action of a Lie group $G$ on a manifold $M$, with stabilizer $H \leq G$.* By Frankel's Fundamental Principle 17.10 and Theorem 17.11, $M \cong G/H$ and $G \to G/H = M$ is a principal $H$-bundle. The B → A bridge: a transitive action means every point of $M$ is in a single $G$-orbit, and the stabilizer is the "internal symmetry" left over; the closed subgroup theorem and 17.11 give the bundle structure. This is the homogeneous-bundle source.

*Source 4: A short exact sequence of Lie groups $1 \to H \to G \to G/H \to 1$ with $H$ closed and normal.* In this case $G \to G/H$ is a principal $H$-bundle and *also* a Lie group homomorphism, giving the covering bundle picture. The B → A bridge: closedness of $H$ (which makes the quotient smooth) + the right $H$-multiplication (which is the principal action). This is the "Lie group as principal bundle" source, with examples like $\mathrm{Spin}(n) \to \mathrm{SO}(n)$.

**Targets (output amplification).**

*Target 1: Conclude triviality from a global section.* The theorem gives the corollary: $P$ is trivial iff it admits a global section. So the existence-of-a-section question (an analytic / topological question) reduces to triviality of the bundle (a structural question). Combined with **obstruction theory**, the failure to admit a section is measured by characteristic classes ($c_1$ for $U(1)$-bundles, $w_2$ for $\mathrm{SO}(n) \to \mathrm{Spin}(n)$ reduction, Euler class for $TM$).

*Target 2: Build associated bundles automatically.* The right $G$-action on $P$ combined with any left $G$-action on a manifold $F$ gives the associated bundle $P \times_G F$. The functorial $F \mapsto P \times_G F$ produces *all* bundles with structure group $G$ from a single $P$. This is the bridge from principal bundles to vector bundles, tensor bundles, gauge fields, etc.

*Target 3: Compute holonomy and characteristic classes as gauge-invariant quantities.* Since the right $G$-action is intrinsic, any equivariant object on $P$ (a connection 1-form, a curvature 2-form, an invariant polynomial of the curvature) is automatically gauge-independent on the base. This is the basis of Chern-Weil theory.

*Target 4: Set up gauge transformations correctly.* A gauge transformation of $P$ is a $G$-equivariant automorphism $\phi : P \to P$ covering the identity on $M$. The intrinsic right $G$-action is what makes this definition meaningful — equivariance with respect to a trivialization-dependent action would not be well-defined.

---

# Why Is It True

The theorem is true because of a single algebraic-group identity: **left and right translation in a group commute**. For any $g, h \in G$, $L_g \circ R_h = R_h \circ L_g$, i.e., $g(uh) = (gu)h$. This is just associativity of group multiplication restated.

In the principal-bundle setting, the transition functions $c_{UV}(p)$ act on the fibre $G$ by *left* translation: in trivialization $\Phi_U$ the fibre point $u$ has coordinate $g_U \in G$, in $\Phi_V$ it has coordinate $g_V = c_{VU}(p)g_U$. Now define the right action on $u$ by $u \cdot h = \Phi_U^{-1}(p, g_U h)$. The question is whether this is well-defined across trivializations. In $\Phi_V$, the right-multiplied point has $V$-coordinate $c_{VU}(p)(g_U h) = (c_{VU}(p)g_U)h = g_V h$ — which is exactly $u \cdot h$ in $V$-coordinates. **So the right action is well-defined precisely because left and right multiplication commute.**

The whole machinery of principal bundles — the intrinsic right action, the equivalence of the two definitions, the bijection between sections and trivializations, the gauge transformations — is downstream of this single algebraic fact.

**Mechanism summary: the right action is well-defined globally because left-translation transition functions commute with right multiplication in $G$ — i.e., the entire theory rests on the associativity of group multiplication.**

The corollary about global sections is also automatic from this picture: a global section $s : M \to P$ defines a global trivialization $\Phi(p, g) = s(p) \cdot g$ (using freeness and transitivity of the right action to make this a bijection on fibres), and vice versa.

---

# What Makes This Hard

The hardest step is recognizing that the **right action is well-defined globally** — i.e., independent of the local trivialization used to define it. The argument is the one-line commutation $L_c R_h = R_h L_c$, but the *meaning* of that argument requires holding both sides of the picture (transition functions on the left, structural action on the right) in mind simultaneously. The common error is to confuse left and right actions, or to assume the right action depends on a choice of trivialization (because it is computed *in* a trivialization in the first place).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Given a fibre bundle $P \to M$ with fibre $G$ and left-translation transition functions, define the right action locally (in each trivialization) and check it agrees on overlaps using $L_c R_h = R_h L_c$. For the converse, build trivializations from local slices of the action.

**Subgoal decomposition:**

1. **Subgoal 1: Define the right action locally.** In a trivialization $\Phi_U : \pi^{-1}(U) \to U \times G$, define $u \cdot h := \Phi_U^{-1}(\pi(u), \mathrm{pr}_2(\Phi_U(u)) \cdot h)$.
   - *Hint:* Just right-multiply the second coordinate.
   - *Why needed:* This is the candidate global right action, defined patch by patch.

2. **Subgoal 2: Verify it agrees on overlaps.** On $U \cap V$, $g_V = c_{VU}(p)g_U$, and $g_V h = c_{VU}(p) g_U h$ by associativity. Hence $u \cdot h$ has $V$-coordinate $g_V h$, same as if defined in $V$-trivialization directly.
   - *Hint:* Use the cocycle / transition formula plus group associativity.
   - *Why needed:* Confirms the local right actions glue into a global one.

3. **Subgoal 3: Verify freeness.** If $u \cdot h = u$, then $g_U h = g_U$ in any trivialization, giving $h = e$ by group cancellation.
   - *Hint:* Right cancellation in $G$.

4. **Subgoal 4: Verify transitivity on fibres.** For $u, v$ in the same fibre, $g_U^v = g_U^u h$ for $h = (g_U^u)^{-1}g_U^v$, so $v = u \cdot h$.
   - *Hint:* Set $h = g_U^{-1}g_U'$ for the desired group element.

5. **Subgoal 5: Local sections ↔ trivializations.** A local section $s_U : U \to P$ gives $\Phi_U^{-1}(p, g) = s_U(p) \cdot g$ (bijection by freeness + transitivity on fibres). Conversely, a trivialization gives a section $s_U(p) = \Phi_U^{-1}(p, e)$.

6. **Subgoal 6: Converse direction.** Given a free proper right $G$-action with smooth orbit space, build trivializations by choosing local sections of $P \to P/G$ (which exist by the slice theorem for proper Lie group actions).

7. **Subgoal 7: Corollary.** Global section $\Leftrightarrow$ global trivialization $\Leftrightarrow$ bundle is trivial.

---

# Lemma Decomposition

> [!note]- Lemma 1: Left and right multiplication in $G$ commute
> **Statement:** For all $g, h, k \in G$, $g(hk) = (gh)k$. Equivalently, $L_g \circ R_k = R_k \circ L_g$ as maps $G \to G$.
>
> **Hint:** This is associativity of multiplication in $G$.
>
> **Why needed:** This is the *only* group-theoretic fact used in the entire proof; everything else follows.
>
> > [!note]- Full proof
> > $L_g(R_k(h)) = L_g(hk) = g(hk) = (gh)k = R_k(gh) = R_k(L_g(h))$. The middle equality is the associativity axiom of the group $G$.

> [!note]- Lemma 2: The right action is well-defined on overlaps
> **Statement:** If $u \in \pi^{-1}(U \cap V)$ has trivialization coordinates $g_U$ in $\Phi_U$ and $g_V = c_{VU}(p)g_U$ in $\Phi_V$, then the right multiplication $u \cdot h$ has trivialization coordinates $g_U h$ in $\Phi_U$ and $g_V h$ in $\Phi_V$, with $g_V h = c_{VU}(p)(g_U h)$.
>
> **Hint:** Apply Lemma 1: $c_{VU}(p)(g_U h) = (c_{VU}(p)g_U)h = g_V h$.
>
> **Why needed:** Confirms the local right action defined in each trivialization is consistent across overlaps, hence defines a global smooth action on $P$.
>
> > [!note]- Full proof
> > By definition $g_V = c_{VU}(p)g_U$, where $c_{VU}(p) \in G$ acts on the fibre $G$ by *left* translation. The candidate $V$-coordinate of $u \cdot h$ is $c_{VU}(p)(g_U h)$, and by associativity (Lemma 1) this equals $(c_{VU}(p)g_U)h = g_V h$. So the right multiplication agrees in both trivializations, and the action is globally well-defined. Smoothness follows from smoothness in each chart and smoothness of the transition functions.

> [!note]- Lemma 3: A local section determines a local trivialization
> **Statement:** Given a smooth local section $s_U : U \to P$, the map $\Phi : U \times G \to \pi^{-1}(U)$, $\Phi(p, g) := s_U(p) \cdot g$, is a $G$-equivariant diffeomorphism (with $G$ acting on the right of both sides), i.e., a local trivialization of $P$.
>
> **Hint:** Use freeness + transitivity on fibres to show $\Phi$ is a bijection; smoothness comes from smoothness of $s_U$ and the right action.
>
> **Why needed:** Establishes the bijection "local sections $\leftrightarrow$ local trivializations" claimed in the theorem.
>
> > [!note]- Full proof
> > $\Phi$ is smooth (smooth $s_U$, smooth right action). It is $G$-equivariant: $\Phi(p, gh) = s_U(p)(gh) = (s_U(p)g)h = \Phi(p, g)\cdot h$. It is fibrewise bijective: each fibre $\pi^{-1}(p)$ is a single $G$-orbit (transitivity on fibres) of $s_U(p)$ (freeness gives uniqueness of the group element taking $s_U(p)$ to any other fibre point). The inverse is smooth because the local trivialization on $P$ is smooth and the right action is smooth. So $\Phi$ is a diffeomorphism.

> [!note]- Lemma 4: A global section exists iff the bundle is trivial
> **Statement:** $P$ is isomorphic to $M \times G$ as a principal $G$-bundle iff there exists a smooth global section $s : M \to P$.
>
> **Hint:** Apply Lemma 3 globally.
>
> **Why needed:** This is the corollary.
>
> > [!note]- Full proof
> > ($\Leftarrow$) Given $s : M \to P$, Lemma 3 with $U = M$ gives a global trivialization $\Phi : M \times G \to P$, exhibiting $P \cong M \times G$. ($\Rightarrow$) Given a trivialization $\Phi : M \times G \to P$, the section $s(p) := \Phi(p, e)$ is a global section.

> [!note]- Lemma 5: A free proper right $G$-action admits local sections
> **Statement:** If $G$ acts freely and properly on $P$ from the right with smooth orbit space $M = P/G$, then $\pi : P \to M$ admits local sections — i.e., for each $p \in M$ there is an open neighborhood $U$ of $p$ and a smooth $s : U \to P$ with $\pi \circ s = \mathrm{id}_U$.
>
> **Hint:** Use the slice theorem for proper Lie group actions (or the local triviality of submersions plus a partition of unity).
>
> **Why needed:** Confirms that the converse direction of the theorem — manifold with free proper action $\Rightarrow$ principal bundle — has the needed local trivializations.
>
> > [!note]- Full proof
> > The quotient $\pi : P \to P/G$ is a submersion (since the action has smooth quotient), and every smooth submersion admits local sections in a neighborhood of any point: pick a slice $S \subset P$ through $u_0 \in \pi^{-1}(p)$ transverse to the fibre, and $\pi|_S$ is a local diffeomorphism by the implicit function theorem. Define $s$ on a neighborhood $U$ of $p$ as $\pi|_S^{-1}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Forward direction** (fibre-bundle $\Rightarrow$ free right action):
>
> Let $P \to M$ be a principal $G$-bundle with structure-group cocycle $\{c_{UV}\}$ acting on $F = G$ by left translation. Define the right action $u \cdot h$ in each trivialization $\Phi_U$ by Lemma 2's prescription; the lemma establishes consistency across overlaps and smoothness. Freeness, fibre-preservation, and fibrewise transitivity are immediate from group cancellation and the structure of $G \cong$ fibre.
>
> **Lemma 3** establishes the bijection between local sections and local trivializations.
>
> **Converse direction** (free right action $\Rightarrow$ fibre-bundle):
>
> Let $P$ carry a free, proper, smooth right $G$-action with smooth orbit space $M = P/G$ and submersive $\pi$. By Lemma 5, $\pi$ admits a local section $s : U \to P$ over each $p \in M$. By Lemma 3 (applied in reverse), each such section gives a local trivialization $\Phi : U \times G \to \pi^{-1}(U)$. On overlaps, two trivializations differ by left translation: $\Phi_V^{-1} \circ \Phi_U(p, g) = (p, c_{VU}(p)g)$ for some smooth $c_{VU} : U \cap V \to G$. The cocycle condition follows from the consistency of the local trivializations. So $P$ is a fibre bundle with fibre $G$ and structure-group $G$ acting by left translation — a principal $G$-bundle.
>
> **Corollary (global section $\Leftrightarrow$ trivial)**: Lemma 4.

---

# Cross-Field Exercise Suggestions

1. **Algebraic geometry / line bundles.** The tautological line bundle $\mathcal{O}(-1)$ over $\mathbb{CP}^n$ is the associated bundle of the principal $\mathbb{C}^*$-bundle $\mathbb{C}^{n+1} \setminus \{0\} \to \mathbb{CP}^n$. Verify that the free $\mathbb{C}^*$-action by scalar multiplication gives a principal bundle and identify the global sections of $\mathcal{O}(d)$ for various $d$. The non-existence of nonzero global sections of $\mathcal{O}(-1)$ corresponds to the theorem above: the principal bundle is nontrivial, so no global section exists.

2. **Numerical analysis / fibre bundles for moduli spaces.** In computer vision, the space of all "calibrated camera poses" is a principal $\mathrm{SE}(3)$-bundle over the base of 3D reconstructions, with the gauge freedom corresponding to overall coordinate choice. The theorem above guarantees this is a principal bundle in the geometric sense and underlies the parametrization of pose-estimation algorithms in machine learning.

3. **Quantum information / fibre bundles of pure states.** The space of pure quantum states on $\mathcal{H} = \mathbb{C}^{n+1}$ is $\mathbb{CP}^n = S^{2n+1}/U(1)$, with $S^{2n+1} \to \mathbb{CP}^n$ a principal $U(1)$-bundle. Apply the theorem: the right $U(1)$-action by phase multiplication is free on $S^{2n+1}$, and the quotient is smooth (the Hopf bundle in the case $n = 1$). The non-existence of a global continuous "phase choice" is the global-section obstruction, and is the geometric meaning of the **Berry phase**.

---

# Bridges

- **[[Def - Fibre Bundle]]** — A fibre bundle is the general object, with fibre any manifold $F$ and structure group $G \leq \mathrm{Diff}(F)$. A principal bundle is the special case $F = G$ with left-translation transition functions, and this theorem makes precise that this special case has the extra structure of a globally defined right $G$-action on the total space.

- **[[Def - Associated Bundle]]** — Given a principal $G$-bundle $P$ and a left $G$-action on $F$, the associated bundle $P \times_G F$ is a fibre bundle with fibre $F$ and the same structure group. The intrinsic right $G$-action on $P$ from this theorem is what makes the diagonal-quotient construction $(u, y) \sim (u \cdot g, g^{-1}y)$ well-defined; without the right action being intrinsic, the associated bundle would depend on choices.

- **[[Def - Homogeneous Bundle]]** — The homogeneous bundle $H \to G \to G/H$ for closed $H \leq G$ is the canonical example of the converse direction of this theorem: a Lie group with right multiplication by its closed subgroup is automatically a principal bundle. This makes coset spaces a primary source of principal bundles in geometry.

- **[[Thm - Associated-Bundle Construction Yields a Bundle]]** — The associated-bundle construction depends on this theorem to define the action: the diagonal action of $G$ on $P \times F$ uses the intrinsic right action on $P$, and the resulting quotient is a bundle in the fibre-bundle sense.

---

# Unlocked by This

> [!tip] Gauge Transformation Group $\mathcal{G}(P)$ *(from Gauge Theory)*
> A **gauge transformation** of $P$ is a $G$-equivariant diffeomorphism $\phi : P \to P$ covering the identity on $M$. The equivariance with respect to the intrinsic right $G$-action is the entire content; without this theorem, "equivariant" would not be a well-defined condition. The gauge group $\mathcal{G}(P) = \Gamma(\mathrm{Ad}\,P)$ is the infinite-dimensional Lie group of all such automorphisms and is the home of all gauge-symmetric physics.

> [!tip] Principal Bundle Connections *(from Gauge Theory III)*
> A connection on a principal $G$-bundle is a $\mathfrak{g}$-valued 1-form on $P$ satisfying equivariance with respect to the right $G$-action (in addition to the vertical condition). This theorem is what makes "equivariance with respect to right action" a global condition, hence makes the principal-bundle definition of a connection unambiguous. See [[Gauge Theory III — Connections in Principal and Associated Bundles]].
