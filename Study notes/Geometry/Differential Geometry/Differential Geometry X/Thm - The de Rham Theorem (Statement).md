---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - Differential k-Form on a Manifold"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, differential-geometry, cohomology, de-rham]
---

# Notation

$M$ is a smooth manifold. $H^k_{dR}(M)$ is the de Rham cohomology — see [[Def - de Rham Cohomology]]. $H_k(M; \mathbb{R})$ is the **singular homology** of $M$ with real coefficients (vector space of formal real-coefficient combinations of continuous singular $k$-cycles modulo boundaries). $H^k(M; \mathbb{R}) = \mathrm{Hom}_\mathbb{R}(H_k(M; \mathbb{R}), \mathbb{R})$ is the **singular cohomology** with real coefficients — the linear dual of singular homology. A **smooth singular $k$-cycle** is a formal real-linear combination of smooth maps $\Delta^k \to M$ (smooth simplices) whose boundary is zero; by **Theorem 18.7** (Lee), smooth singular homology agrees with the usual singular homology.

---

# Statement

> **Theorem (de Rham).** For every smooth manifold $M$ and every nonnegative integer $k$, the **de Rham homomorphism**
> $$\mathcal{I} : H^k_{dR}(M) \to H^k(M; \mathbb{R}), \qquad \mathcal{I}[\omega][c] := \int_c \omega,$$
> defined for closed forms $\omega$ and smooth singular cycles $c$, is a well-defined $\mathbb{R}$-linear **isomorphism**.

In words: *integration of closed forms over smooth cycles gives a natural isomorphism between de Rham cohomology and singular cohomology with real coefficients.* Two paradigmatically different definitions of cohomology — one from smooth structure and calculus, the other from topology and combinatorics — produce the same answer.

> **Corollary (de Rham cohomology is a topological invariant).** Homeomorphic smooth manifolds have isomorphic de Rham cohomology. More: [[Def - Homotopy|homotopy]] equivalent smooth manifolds have isomorphic de Rham cohomology. The de Rham cohomology, although defined smoothly, depends only on the [[Def - Homotopy|homotopy]] type.

> **Corollary (Betti numbers from forms).** The [[Def - Dimension|dimensions]] $b_k(M) := \dim_\mathbb{R} H^k_{dR}(M)$ are the **Betti numbers** of $M$ — the topological invariants whose alternating sum is the **Euler characteristic** $\chi(M) = \sum_k (-1)^k b_k$.

We state but do not prove this theorem; the proof — a Mayer–Vietoris induction on good covers, reducing to the case of Euclidean balls where the Poincaré lemma trivializes both sides — is given in Lee Chapter 18. The point of this page is the statement and its consequences for our overall picture of cohomology.

---

# Motivation

de Rham cohomology, defined from smooth forms, looks like it ought to depend sensitively on the smooth structure. After all, you cannot define $H^k_{dR}$ for an arbitrary topological space — there are no forms there. So it is a smooth-manifold invariant, and the surprising claim is that the answer is a *topological* invariant — even a *homotopical* one.

Singular cohomology, by contrast, is defined for any topological space. It is built from continuous simplices — maps from standard simplices $\Delta^k$ into the space — and the boundary operator from algebraic topology. Two homotopy-equivalent topological spaces have isomorphic singular cohomology, by a standard homological-algebra argument.

The de Rham theorem says these two cohomologies *agree* on smooth manifolds. The map between them is concrete: a closed form $\omega$ defines a functional on cycles by $c \mapsto \int_c \omega$. The integral is well-defined when $\omega$ is closed and $c$ has no boundary (closed cycle), because in that case Stokes's theorem gives $\int_c \omega = \int_{c'} \omega$ whenever $c$ and $c'$ are homologous (differ by a boundary). Likewise, if $\omega$ and $\omega'$ differ by an exact form $d\eta$, then $\int_c \omega - \int_c \omega' = \int_c d\eta = \int_{\partial c} \eta = 0$ (since $c$ has no boundary). So $\int_c \omega$ depends only on the cohomology class $[\omega]$ and the homology class $[c]$.

The deep content is that this map is an *isomorphism* — every singular cohomology class is detected by integration of some closed form, and only forms in the same de Rham class give the same functional. This identifies the two theories.

Why is this remarkable? Because the two definitions use *completely different* technologies. de Rham uses smooth forms, the exterior derivative, and integration. Singular cohomology uses continuous maps, formal sums, and the simplicial boundary operator. There is no a priori reason they should agree — the agreement is a deep theorem about how smooth structure interacts with topology.

The consequences are far-reaching. *Every singular-cohomology computation* — from CW complex structures, from the Eilenberg–Steenrod axioms, from spectral sequences — *applies to de Rham cohomology*. Conversely, *every smooth-manifold-cohomology computation* — via Stokes, via Hodge theory, via integration of characteristic forms — *gives a topological invariant*. The two viewpoints become a single subject.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$M$ is a smooth manifold; $\omega$ is a closed form, $c$ a smooth singular cycle.*

The first disguised source is **knowledge of singular cohomology by other means.** Property $B$: $H^k(M; \mathbb{R})$ has been computed by topological methods (e.g., CW structure, Mayer–Vietoris for singular cohomology). The bridge: by de Rham, $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, so the singular-cohomology answer is also the de Rham answer — no further computation needed. *Example application:* $H^*(S^n)$ is computed combinatorially as the cellular cohomology of the CW structure; de Rham then gives $H^k_{dR}(S^n)$ for free.

The second disguised source is **a topological invariant of $M$ that can be computed via forms.** Property $B$: a smooth invariant — an integral, a characteristic class, a curvature integral — gives a real number. The bridge: by de Rham, this real number is a singular-cohomology pairing, hence a topological invariant. *Example:* the **Euler characteristic** $\chi(M)$, computable as the alternating sum of dimensions of de Rham cohomology, is a topological invariant (and also computable by combinatorial cell counts via cellular cohomology).

The third disguised source is **smooth approximation of continuous data.** Property $B$: a continuous singular cycle, which is not smooth. The bridge: by Whitney approximation, every continuous map is homotopic to a smooth one, so every continuous cycle is homologous to a smooth one. Integration is well-defined on the smooth approximation, and the de Rham pairing is well-defined on all singular homology. *Example:* the topological theory of integration of forms — building $\int_c \omega$ for *any* continuous $k$-cycle $c$ by first smoothing and then integrating.

**Targets (Output Amplification)**

The conclusion $C$: *$H^k_{dR}(M) \cong H^k(M; \mathbb{R})$ via the integration pairing.*

Combine $C$ with **the Eilenberg–Steenrod axioms.** Singular cohomology satisfies the Eilenberg–Steenrod axioms (homotopy invariance, excision, dimension, long exact sequence of pairs). By de Rham, $H^k_{dR}$ satisfies all the same axioms — on smooth manifolds. The further result $E$: de Rham cohomology is *characterized* as the cohomology theory satisfying these axioms on smooth manifolds — a uniqueness theorem.

Combine $C$ with **the universal coefficient theorem.** Singular cohomology with real coefficients is computable from integer-coefficient singular homology via the universal coefficient theorem: $H^k(M; \mathbb{R}) \cong \mathrm{Hom}(H_k(M; \mathbb{Z}), \mathbb{R})$ (when $H_*(M; \mathbb{Z})$ is finitely generated, which it is for compact $M$). The further result $E$: the dimensions of $H^k_{dR}(M)$ are the ranks of integer homology — the *Betti numbers* — and they recover the topological invariant of $M$ via smooth-form computations.

Combine $C$ with **Poincaré duality.** For a compact oriented $n$-manifold, $H^k(M; \mathbb{R}) \cong H^{n-k}(M; \mathbb{R})$ via the cap product with the fundamental class. The further result $E$: by de Rham, $H^k_{dR}(M) \cong H^{n-k}_{dR}(M)$, with the isomorphism mediated by Poincaré duality. This is a smooth-form version of a topological duality, computable both ways.

---

# Why Is It True

**The single sentence (proof philosophy): the de Rham complex and the singular cochain complex are both *resolutions* of the constant sheaf $\mathbb{R}$ on $M$, and both compute the same cohomology by the universality of derived functors — concretely realized via Mayer–Vietoris induction on a good cover, with both sides trivialized on contractible pieces.**

The intuition for why the two theories agree comes from the local case. On a contractible open set $U \subseteq M$:
- $H^k_{dR}(U) = 0$ for $k \geq 1$ (Poincaré lemma) and $H^0_{dR}(U) = \mathbb{R}$.
- $H^k(U; \mathbb{R}) = 0$ for $k \geq 1$ (contractible spaces have trivial cohomology) and $H^0(U; \mathbb{R}) = \mathbb{R}$.

So the two theories agree on contractible pieces. The general manifold is then a "gluing" of contractible pieces, and both theories assemble from local data via Mayer–Vietoris, with the same gluing combinatorics. The de Rham homomorphism $\mathcal{I}$ is *natural* under restrictions and pullbacks, so it commutes with the gluing — and since it is an isomorphism on the contractible pieces, it is an isomorphism on the whole manifold by induction.

Lee's proof (Theorem 18.14) implements this strategy precisely. Step 1: $\mathcal{I}$ is an isomorphism for a single convex open subset of $\mathbb{R}^n$ (by Poincaré lemma on both sides, recovering $\mathbb{R}$ in degree 0 and 0 otherwise). Step 2: $\mathcal{I}$ commutes with the Mayer–Vietoris sequences for de Rham and singular cohomology, so if $\mathcal{I}$ is an isomorphism on $U$, $V$, $U \cap V$, it is an isomorphism on $U \cup V$ by the five lemma. Step 3: every smooth manifold has a good cover (a cover by convex open sets in some Riemannian metric, with all finite intersections also convex). Iterating Mayer–Vietoris on this cover propagates the isomorphism from contractible pieces to the entire manifold.

The technical wrinkles: defining the de Rham homomorphism requires integrating forms over *smooth* singular cycles, while singular homology uses *continuous* cycles. Lee bridges this with the **Whitney approximation theorem**: smooth singular homology equals singular homology, via a smoothing operator (Theorem 18.7).

The proof is a beautiful instance of "global cohomology theories are determined by their local behavior plus excision/Mayer–Vietoris" — the same principle that gives the uniqueness of cohomology theories satisfying the Eilenberg–Steenrod axioms.

---

# What Makes This Hard

The conceptual obstacle is recognizing that the smooth-structure-dependent de Rham theory and the purely topological singular theory really do produce the same answer — the deep claim is that *the smooth structure leaves no fingerprint on the cohomology*. The proof's hardest step is **bridging continuous and smooth singular homology** via Whitney approximation (`Theorem 18.7` in Lee), which requires a careful smoothing construction that respects boundary structures. The most common error is to overlook that the de Rham homomorphism is *natural* — its commutativity with restriction maps and Mayer–Vietoris is what makes the inductive proof work, and proving naturality is essentially the proof of well-definedness done carefully.

---

# Rederivation Scaffold

(We do not prove the de Rham theorem here — it is a substantial result occupying a chapter of Lee. The scaffold below summarizes the strategy; the full proof is in `Differential Geometry X` as a stated result.)

**This section is self-sufficient at the strategy level: reading what follows should let you reconstruct the overall structure of the proof.**

**High-level strategy:** Define the de Rham homomorphism by integration of forms over smooth simplices, using Stokes's theorem to check well-definedness on cohomology classes. Verify the isomorphism on contractible open sets via Poincaré lemma on both sides. Verify naturality (commutativity with restriction maps and Mayer–Vietoris sequences). Apply Mayer–Vietoris and the five lemma to propagate the isomorphism to any manifold with a finite good cover. Use a partition-of-unity argument to extend to non-finite covers.

**Subgoal decomposition:**

1. **Define the de Rham homomorphism.** For $[\omega] \in H^k_{dR}(M)$ and $[c] \in H_k(M; \mathbb{R})$ (with $c$ represented by a smooth cycle), define $\mathcal{I}[\omega][c] = \int_c \omega$.
   - *Hint:* The integral makes sense because $\omega$ is smooth and $c$ is a smooth cycle (formal sum of smooth simplices).
   - *Why needed:* This is the candidate isomorphism.

2. **Well-definedness via Stokes.** Show $\int_c \omega$ depends only on $[\omega]$ and $[c]$: if $\omega' = \omega + d\eta$, then $\int_c (\omega' - \omega) = \int_c d\eta = \int_{\partial c} \eta = 0$ (since $\partial c = 0$). If $c' = c + \partial b$, then $\int_{c'-c} \omega = \int_{\partial b} \omega = \int_b d\omega = 0$ (since $d\omega = 0$).
   - *Hint:* This is the standard pairing of Stokes's theorem: closed forms see only homology classes.
   - *Why needed:* It shows $\mathcal{I}$ is well-defined.

3. **$\mathcal{I}$ is an isomorphism on convex open sets.** For convex $U \subseteq \mathbb{R}^n$, both sides are $\mathbb{R}$ in degree 0 (and 0 in positive degrees); the de Rham homomorphism in degree 0 sends the constant function 1 to the functional "evaluate at any point" — non-zero, hence an isomorphism on the 1-dimensional space.
   - *Hint:* Use the Poincaré lemma for de Rham and the contractibility of $U$ for singular.
   - *Why needed:* The base case for the induction.

4. **Naturality and commutativity with Mayer–Vietoris.** $\mathcal{I}$ commutes with pullback by smooth maps, with the connecting [[Def - Homomorphism|homomorphisms]] of de Rham and singular Mayer–Vietoris sequences. Verify both naturalities.
   - *Hint:* Naturality with respect to maps follows from pullback of forms equals pullback of cycles; commutativity with Mayer–Vietoris is a chain-level verification using the explicit form of $\delta$.
   - *Why needed:* These are needed to apply the five lemma.

5. **Five lemma argument.** Given Mayer–Vietoris cover $U \cup V = M$ with $\mathcal{I}$ an isomorphism on $U$, $V$, $U \cap V$ — by the commutative diagram of Mayer–Vietoris sequences, the five lemma forces $\mathcal{I}$ to be an isomorphism on $M$.
   - *Hint:* The five lemma is a standard fact of homological algebra: in a commutative diagram of long exact sequences, if four out of five vertical maps are [[Def - Isomorphism|isomorphisms]], the fifth is too.
   - *Why needed:* This is the inductive step.

6. **Finite good cover induction.** Every smooth manifold admits a good cover (by convex open sets, all finite intersections convex). For compact $M$, the cover is finite; iterate the five lemma to propagate from convex to $M$. For non-compact $M$, use a partition-of-unity argument and a colimit construction (Step 4 in Lee's proof).
   - *Hint:* Existence of a good cover comes from any Riemannian metric on $M$ — [[Def - Geodesic|geodesic]] balls work, by `Theorem 1.34` in Lee.
   - *Why needed:* This completes the proof.

---

# Lemma Decomposition

We omit detailed lemma decomposition — the full proof is in Lee Chapter 18 and is substantially longer than space allows. The most important supporting lemma:

> [!note]- Lemma: Smooth singular homology equals singular homology
> **Statement:** For any smooth manifold $M$ and any $k$, the natural inclusion of smooth singular chains into all singular chains induces an isomorphism $H_k^{\infty}(M) \cong H_k(M)$ on homology.
>
> **Hint:** Construct a smoothing operator $s : C_*(M) \to C_*^\infty(M)$ such that $s \circ i = \mathrm{id}$ and $i \circ s$ is chain-homotopic to the identity. Use Whitney approximation theorem to smooth each individual simplex relative to the boundary.
>
> **Why needed:** It identifies the homology used in the de Rham pairing with the standard singular homology, allowing us to view $\mathcal{I}$ as a map into singular cohomology.
>
> > [!note]- Sketch
> > This is Theorem 18.7 in Lee. Define the smoothing operator on each singular simplex $\sigma : \Delta^k \to M$ by constructing a homotopy $H_\sigma$ from $\sigma$ to a smooth simplex $\tilde\sigma$ using Whitney approximation, then assemble across all simplices in a way compatible with face maps. Show the smoothing operator is a chain map; construct a chain homotopy between $i \circ s$ and the identity. The argument is technical but constructive.

---

# Formal Proof

The full proof of the de Rham theorem is omitted here; see Lee Chapter 18. We state the theorem and use it.

---

# Cross-Field Exercise Suggestions

**Betti numbers from de Rham computations.** Compute $H^k_{dR}(M)$ for some manifold by direct form computation or Mayer–Vietoris; conclude the Betti numbers $b_k(M) = \dim H^k_{dR}(M)$ — topological invariants. For example, $b_k(T^n) = \binom{n}{k}$ from the de Rham computation; by de Rham, these are also the Betti numbers of the topological torus.

**Euler characteristic from forms.** For a compact oriented $n$-manifold, $\chi(M) = \sum_k (-1)^k b_k = \sum_k (-1)^k \dim H^k_{dR}(M)$. By the **Gauss–Bonnet theorem** (Chern's generalization), $\chi(M)$ equals an integral of a curvature form: $\chi(M) = \int_M e(TM)$, where $e(TM)$ is the Euler class. The de Rham theorem ensures that this integral — a smooth computation — is a topological invariant.

**Detecting non-trivial cohomology classes via integration.** To prove a closed form $\omega$ defines a non-trivial cohomology class, find a singular cycle $c$ with $\int_c \omega \neq 0$. By de Rham, $\mathcal{I}[\omega]$ is non-zero, so $[\omega] \neq 0$ in $H^k_{dR}$. *Example:* the angular form $d\theta$ on $\mathbb{R}^2 \setminus \{0\}$ has $\int_{S^1} d\theta = 2\pi$, so $[d\theta] \neq 0$ in $H^1_{dR}(\mathbb{R}^2 \setminus \{0\})$.

**Topological obstructions to smooth structures.** Two non-homeomorphic smooth manifolds can be distinguished by their de Rham cohomology (which is a topological invariant by de Rham). This says smooth structure doesn't add cohomological information beyond what topology already encodes — a deep fact about how smooth structure and topology relate.

---

# Bridges

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]]** — the local input. Both de Rham and singular cohomology agree on contractible pieces (each is trivial in positive degrees, $\mathbb{R}$ in degree 0). The de Rham theorem then says they agree on assembling pieces, by Mayer–Vietoris.

- **[[Thm - Homotopy Invariance of de Rham Cohomology|Homotopy invariance]]** — the de Rham version of the singular-cohomology homotopy invariance. Both forms-side and singular-side cohomologies are homotopy invariants; the de Rham theorem makes this match precise.

- **[[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris]]** — the inductive engine. Both de Rham and singular cohomology have Mayer–Vietoris sequences, and they agree (via the de Rham homomorphism). The proof of de Rham reduces to showing the two Mayer–Vietoris sequences agree, which is a naturality check.

- **The Eilenberg–Steenrod axioms** — singular cohomology satisfies them; by de Rham, $H^*_{dR}$ also satisfies them on smooth manifolds. The Eilenberg–Steenrod uniqueness theorem (cohomology theories agreeing on a point agree on CW complexes) gives an abstract reason why the two theories must agree.

- **Hodge theory** — on a compact oriented Riemannian manifold, the de Rham cohomology has *canonical* representatives — harmonic forms. By de Rham, harmonic forms are also representatives of singular cohomology classes, mediated by the integration pairing. The Hodge decomposition is a refinement of de Rham, picking out the orthogonal complement of the exact and co-exact pieces.

- **Group theory: cohomology as quotient of abelian groups** — both $H^k_{dR}(M)$ and $H^k(M; \mathbb{R})$ are $\mathbb{R}$-vector spaces (in particular abelian groups). The de Rham homomorphism is a group homomorphism, and the isomorphism is an isomorphism of abelian groups (and of $\mathbb{R}$-vector spaces). The de Rham theorem is, at the algebra level, an isomorphism of [[Def - Quotient Group|quotient groups]].

---

# Unlocked by This

> [!tip] **Topological invariance of $H^k_{dR}$** *(from this same topic)*
> Homeomorphic smooth manifolds have isomorphic de Rham cohomology. This is immediate from de Rham + topological invariance of singular cohomology, but it is striking because the smooth structure was used to define the de Rham complex. The conclusion: smooth structure makes no contribution to cohomology — the answer is purely topological.

> [!tip] **Singular cohomology of smooth manifolds via forms** *(from this same topic)*
> Every singular cohomology computation on a smooth manifold has an equivalent de Rham computation (by de Rham). This means many topological invariants — Betti numbers, Euler characteristic, signature, characteristic classes — can be computed by smooth-form techniques (integration, Hodge theory, Chern–Weil theory).

> [!tip] **Hodge decomposition and harmonic forms** *(from Riemannian Geometry)*
> On a compact oriented Riemannian manifold, Hodge theory picks out a *canonical* representative of each de Rham cohomology class — the unique harmonic form satisfying $\Delta\omega = 0$. By de Rham, this gives canonical representatives in singular cohomology too. The Hodge decomposition $\Omega^k = \ker \Delta \oplus d\Omega^{k-1} \oplus d^*\Omega^{k+1}$ is the analytic refinement of the de Rham theorem.

> [!tip] **Chern–Weil theory and characteristic classes** *(from Differential Topology)*
> Characteristic classes of vector bundles — Chern, Pontryagin, Euler classes — are de Rham cohomology classes built from curvature of a connection (Chern–Weil construction). By de Rham, they are also singular cohomology classes — topological invariants of the bundle, computable by smooth-form techniques.

> [!tip] **Gauge theory and instanton numbers** *(from Mathematical Physics)*
> In gauge theory, the **instanton number** of a connection is the de Rham cohomology class of $\mathrm{tr}(F \wedge F)$ for the curvature $F$ — an integer (topological), but computed as an integral of forms. By de Rham, this matches the second Chern class of the underlying principal bundle, connecting physics to topology.

> [!tip] **Sheaf cohomology and the abstract de Rham theorem** *(from Sheaf Theory)*
> The de Rham theorem is one instance of a much more general phenomenon: every soft resolution of the constant sheaf $\mathbb{R}$ on a manifold computes the same cohomology, which equals the sheaf cohomology $H^*(M; \mathbb{R})$. The de Rham complex is one such resolution; the Čech complex is another; the simplicial cochain complex is a third. The abstract de Rham theorem says all of these compute the same cohomology — the de Rham theorem on smooth manifolds is one (very concrete) instance.
