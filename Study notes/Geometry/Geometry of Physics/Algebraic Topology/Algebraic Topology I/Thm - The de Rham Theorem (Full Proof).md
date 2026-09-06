---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Def - Singular Cohomology"
  - "Def - de Rham Cohomology"
  - "Thm - Mayer-Vietoris for Singular Homology"
  - "Thm - The Mayer-Vietoris Sequence"
  - "Thm - The Poincaré Lemma on a Star-Shaped Region"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, algebraic-topology, de-rham, comparison-theorem]
---

# Notation

$M$ is a smooth manifold (Hausdorff, second countable).

- $\Omega^k(M)$ — smooth $k$-forms on $M$; $d : \Omega^k \to \Omega^{k+1}$ exterior derivative; $H^k_{dR}(M) = \ker d / \mathrm{im}\, d$ the [[Def - de Rham Cohomology|de Rham cohomology]].
- $C_p^\infty(M; \mathbb{R})$ — the **smooth singular chain group**: formal real-linear combinations of smooth singular $p$-simplices $\sigma : \Delta^p \to M$. $H_p^\infty(M; \mathbb{R})$ — smooth singular homology.
- $C_p(M; \mathbb{R})$, $H_p(M; \mathbb{R})$ — full singular homology with real coefficients (using all continuous simplices).
- $H^p(M; \mathbb{R}) = \mathrm{Hom}_\mathbb{R}(H_p(M; \mathbb{R}), \mathbb{R})$ — [[Def - Singular Cohomology|singular cohomology]] over $\mathbb{R}$.
- For a smooth $p$-simplex $\sigma$ and a smooth $p$-form $\omega$: $\int_\sigma \omega = \int_{\Delta^p} \sigma^* \omega$, the **integration pairing**.
- $\mathcal{I} : H^p_{dR}(M) \to H^p(M; \mathbb{R})$ — the **de Rham homomorphism**, $\mathcal{I}[\omega][c] = \int_c \omega$.

A **good cover** of $M$ is an open cover $\{U_\alpha\}$ such that every non-empty finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ is diffeomorphic to $\mathbb{R}^n$ (in particular, contractible). Every smooth manifold admits a good cover by geodesically convex balls in any Riemannian metric.

---

# Statement

> **Theorem (de Rham).** For every smooth manifold $M$ and every nonnegative integer $p$, the **de Rham homomorphism**
> $$
> \mathcal{I} : H^p_{dR}(M) \to H^p(M; \mathbb{R}), \qquad \mathcal{I}[\omega][c] = \int_c \omega
> $$
> is a $\mathbb{R}$-linear isomorphism. Two paradigmatically different cohomology theories — one from smooth forms and integration, one from continuous singular simplices and combinatorial coboundary — produce the same answer.

> **Corollary (Topological invariance).** $H^p_{dR}(M)$ is a topological invariant: $H^p_{dR}(M) \cong H^p_{dR}(N)$ whenever $M$ and $N$ are homeomorphic. More strongly, it depends only on the homotopy type.

> **Corollary (Cup product = wedge product).** The de Rham isomorphism is a ring isomorphism with respect to the wedge product on $H^*_{dR}$ and the cup product on $H^*(M; \mathbb{R})$: $\mathcal{I}([\omega] \wedge [\eta]) = \mathcal{I}[\omega] \smile \mathcal{I}[\eta]$. (Stated here; proof omitted — uses the explicit formula for cup product on singular cochains.)

> **Corollary (Betti numbers and the de Rham polynomial).** The dimensions $b_p(M) = \dim H^p_{dR}(M)$ are the Betti numbers of $M$. The de Rham Poincaré polynomial $\sum b_p t^p$ is a topological invariant.

The proof reduces by Mayer–Vietoris on a good cover to the case of Euclidean balls (where both sides are trivially $\mathbb{R}$ in degree zero and zero elsewhere), and uses the five lemma to propagate the isomorphism to the global manifold.

---

# Motivation

de Rham cohomology, defined from smooth differential forms, looks like a creature of smooth geometry. After all, you cannot define $H^k_{dR}$ for an arbitrary topological space — there are no forms there. So it is a smooth-manifold invariant, and the question is what additional structure (beyond the smooth structure) it captures.

Singular cohomology, by contrast, is defined for any topological space. It is built combinatorially from continuous simplices and the simplicial coboundary, and it satisfies the **Eilenberg–Steenrod axioms** (homotopy invariance, long exact sequence, excision, additivity, dimension). It is the "universal" ordinary cohomology theory on topological spaces.

The de Rham theorem says these two cohomologies *agree* on smooth manifolds. The map between them is concrete: integration of forms over cycles, $\int_c \omega$. This map is well-defined on cohomology classes — by Stokes's theorem, $\int_c \omega$ depends only on the de Rham class $[\omega]$ (changes by exact $d\eta$ contribute zero by Stokes applied to the closed cycle) and the homology class $[c]$ (changes by boundaries $\partial b$ contribute $\int_{\partial b} \omega = \int_b d\omega = 0$ for closed $\omega$).

The deep content is that this map is an *isomorphism* — every singular cohomology class is detected by some closed form, and only forms in the same de Rham class give the same functional. This identifies the two theories completely.

Why is this remarkable? Because the two definitions use *completely different technologies*. de Rham uses smooth forms, the exterior derivative, integration. Singular cohomology uses continuous maps, formal sums, the simplicial coboundary. There is no a priori reason they should agree — the agreement is the theorem.

The consequences are far-reaching. **Every singular-cohomology computation** — via CW structures, Mayer–Vietoris, spectral sequences — *applies to de Rham cohomology*. Conversely, **every smooth-form computation** — via Hodge theory, Chern–Weil theory, integration of curvature forms — *gives a topological invariant*. The two viewpoints become a single subject.

The proof strategy is a beautiful instance of "comparison theorems via good covers." Both sides satisfy Mayer–Vietoris (with parallel constructions on each side); both sides reduce to $\mathbb{R}$ in degree zero and zero in positive degrees on contractible domains. So if we cover $M$ by contractibles and iterate Mayer–Vietoris, the isomorphism propagates from local pieces (where it is trivial) to the global manifold (where it is the theorem). The "five lemma" of homological algebra is what makes this propagation work: in a commutative diagram of long exact sequences, if four vertical maps are isomorphisms, the fifth is too.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$M$ is a smooth manifold; $\omega$ is a closed smooth form; $c$ is a smooth singular cycle.*

The first disguised source is **knowledge of singular cohomology by other means.** Property $B$: $H^k(M; \mathbb{R})$ has been computed by topological methods (CW structure, Mayer–Vietoris for singular cohomology, cellular cohomology). The bridge: by de Rham, $H^p_{dR}(M) \cong H^p(M; \mathbb{R})$. So a singular-cohomology answer immediately gives a de Rham answer, without further smooth-form computation. *Example application:* $H^*(\mathbb{CP}^n)$ is computed combinatorially as a polynomial ring $\mathbb{Z}[x]/(x^{n+1})$; de Rham then gives $H^*_{dR}(\mathbb{CP}^n)$ for free.

The second disguised source is **a smooth invariant of $M$ that can be computed via forms.** Property $B$: a curvature integral, characteristic number, or similar smooth-form invariant produces a real number. The bridge: by de Rham, this real number is a singular cohomology pairing, hence a topological invariant. *Example application:* the **Euler characteristic** $\chi(M)$, by Chern–Gauss–Bonnet expressed as $\chi(M) = \int_M e(TM)$ for a curvature representative of the Euler class; the topological invariance of $\chi$ is then guaranteed.

The third disguised source is **smooth approximation of continuous data.** Property $B$: a continuous singular cycle, not initially smooth. The bridge: by Whitney approximation, every continuous map (and every continuous homotopy of maps) is homotopic to a smooth one (resp. smooth homotopy). So every continuous cycle is homologous to a smooth one, and the de Rham pairing is well-defined on all of singular homology, not just the smooth part.

The fourth disguised source is **a fibre bundle or covering space situation.** Property $B$: a smooth map $\pi : E \to B$ with topologically tractable fibre. The bridge: the de Rham theorem applies to all relevant spaces, and the spectral sequence of the fibration (Serre, Leray, etc.) on the singular side translates to a spectral sequence on the de Rham side. *Example application:* computing $H^*(BG)$ for a Lie group $G$ via the universal bundle and the de Rham theorem.

**Targets (Output Amplification)**

The conclusion $C$: *$H^p_{dR}(M) \cong H^p(M; \mathbb{R})$ via the integration pairing.*

Combine $C$ with **the Eilenberg–Steenrod axioms.** Singular cohomology satisfies all five. By de Rham, $H^p_{dR}$ satisfies all five on smooth manifolds. The further result $E$: de Rham cohomology is *characterised* as the unique cohomology theory on smooth manifolds satisfying the axioms — a uniqueness theorem.

Combine $C$ with **the universal coefficient theorem.** $H^p(M; \mathbb{R}) = \mathrm{Hom}(H_p(M; \mathbb{Z}), \mathbb{R})$ (no $\mathrm{Ext}$ contribution, since $\mathbb{R}$ is divisible). The further result $E$: the dimensions of $H^p_{dR}(M)$ are the ranks of integer homology — the **Betti numbers** — and they recover the topological invariant of $M$ via smooth-form computations.

Combine $C$ with **Poincaré duality.** For a compact oriented $n$-manifold, $H^k(M; \mathbb{R}) \cong H^{n-k}(M; \mathbb{R})$ via cap product. The further result $E$: by de Rham, $H^k_{dR}(M) \cong H^{n-k}_{dR}(M)$ realised by the **Hodge star** $\star : \Omega^k \to \Omega^{n-k}$ (when $M$ is Riemannian) — a smooth-form version of a topological duality. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

Combine $C$ with **Chern–Weil theory.** Characteristic classes of vector bundles (Chern, Pontryagin, Euler) can be represented by curvature integrals on the de Rham side. By de Rham, these represent integer cohomology classes (up to torsion). The further result $E$: characteristic numbers — integer-valued topological invariants — are computable by smooth curvature integrals.

---

# Why Is It True

**The single sentence: both the de Rham complex $(\Omega^\bullet, d)$ and the singular cochain complex $(C^\bullet(-; \mathbb{R}), \delta)$ are *resolutions* of the constant sheaf $\mathbb{R}$ on $M$, and any two such resolutions compute the same cohomology by the universal property of derived functors; concretely realised via Mayer–Vietoris induction on a good cover, with both sides trivialised on contractible pieces.**

The intuition for why the two theories agree comes from the local case. On a contractible open set $U \subseteq M$:
- $H^k_{dR}(U) = 0$ for $k \geq 1$ ([[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]]) and $H^0_{dR}(U) = \mathbb{R}$ (constant functions).
- $H^k(U; \mathbb{R}) = 0$ for $k \geq 1$ (contractible spaces have trivial cohomology) and $H^0(U; \mathbb{R}) = \mathbb{R}$.

So the two theories agree on contractible pieces — both equal $\mathbb{R}$ in degree zero and zero in positive degrees. The de Rham homomorphism $\mathcal{I}$ on a contractible $U$ is the map "evaluate at any point" composed with the obvious identification $H^0_{dR}(U) = \mathbb{R}$ = $H^0(U; \mathbb{R})$, which is clearly an isomorphism.

The general manifold is then a "gluing" of contractible pieces. By a Riemannian metric, every smooth manifold admits a **good cover** — an open cover $\{U_\alpha\}$ such that every finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ is contractible (in fact diffeomorphic to $\mathbb{R}^n$). On a good cover, both de Rham cohomology and singular cohomology satisfy Mayer–Vietoris, and the gluing combinatorics are the same: the singular Mayer–Vietoris uses inclusions of cover elements, the de Rham Mayer–Vietoris uses pullback under inclusions. The de Rham homomorphism $\mathcal{I}$ commutes with these structure maps (naturality), so it commutes with the Mayer–Vietoris connecting maps.

By the **five lemma**: in a commutative diagram of long exact sequences with four out of five vertical maps being isomorphisms, the fifth is too. The cover $\{U_1, U_2\}$ gives a Mayer–Vietoris sequence. If $\mathcal{I}$ is an isomorphism on $U_1$, $U_2$, and $U_1 \cap U_2$, then by five lemma $\mathcal{I}$ is an isomorphism on $U_1 \cup U_2$. Iterating: if $\mathcal{I}$ is an isomorphism on each contractible piece and on their intersections (which are also contractible by the good-cover property), then by induction it is an isomorphism on the union of any finite sub-collection, hence on $M$ if the cover is finite.

For non-compact $M$ with a possibly infinite good cover, one uses a partition-of-unity argument (Lee §18) or a colimit / direct-limit argument to extend the finite-cover statement to the global manifold.

A technical wrinkle: the de Rham homomorphism is defined on *smooth* singular chains, while singular cohomology uses all continuous singular chains. The bridge is the **Whitney approximation theorem**: every continuous singular cycle is homologous to a smooth one. So smooth singular cohomology agrees with continuous singular cohomology — and the de Rham homomorphism becomes well-defined on the latter via the former.

---

# What Makes This Hard

The conceptual obstacle is recognising that the smooth-structure-dependent de Rham theory and the purely topological singular theory really do produce the same answer — the deep claim is that **the smooth structure leaves no fingerprint on the cohomology**, beyond what is already determined by the underlying homotopy type.

The proof's hardest technical step is **bridging continuous and smooth singular homology** via Whitney approximation (Lee, Theorem 18.7). One has to construct a smoothing operator on the singular chain complex that respects the boundary structure and is chain-homotopic to the identity. The construction is explicit (use the local convex structure of charts to smooth each simplex), but the verification that everything commutes is technically involved.

The most common error is to overlook that the de Rham homomorphism is **natural** — its commutativity with restriction maps, with pullback, and with Mayer–Vietoris connecting maps is what makes the inductive proof work. Without naturality, the five lemma cannot be applied, and the inductive argument fails. Proving naturality is essentially the proof of well-definedness done carefully.

A subtle conceptual issue: the de Rham theorem is sometimes confused with "every closed form is the pullback of a unique singular cochain." That is *not* quite right — the de Rham *class* corresponds to a singular cohomology *class*, with both having many representatives. The integration pairing $\int_c \omega$ is the well-defined invariant.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define the de Rham homomorphism via integration. Verify well-definedness using Stokes's theorem. Verify it is an isomorphism on convex open subsets of $\mathbb{R}^n$ (using Poincaré lemma on the de Rham side and contractibility on the singular side). Verify naturality with respect to Mayer–Vietoris sequences on both sides. Apply Mayer–Vietoris and the five lemma to propagate the isomorphism to any manifold admitting a finite good cover. Use a partition-of-unity / direct-limit argument for non-compact manifolds.

**Subgoal decomposition:**

1. **Define the de Rham homomorphism.** For $[\omega] \in H^p_{dR}(M)$ and $[c] \in H_p(M; \mathbb{R})$ (represented by a smooth cycle), define $\mathcal{I}[\omega][c] = \int_c \omega$. By Whitney approximation, every continuous cycle is homologous to a smooth one, so the right side is well-defined on the homology class.
   - *Hint:* Integral of a smooth form over a smooth chain.
   - *Why needed:* This is the candidate isomorphism.

2. **Well-definedness via Stokes.** Show $\int_c \omega$ depends only on $[\omega] \in H^p_{dR}$ and $[c] \in H_p$. (i) If $\omega' = \omega + d\eta$, then $\int_c (\omega' - \omega) = \int_c d\eta = \int_{\partial c} \eta = 0$ since $\partial c = 0$. (ii) If $c' = c + \partial b$, then $\int_{c' - c} \omega = \int_{\partial b} \omega = \int_b d\omega = 0$ since $d\omega = 0$.
   - *Hint:* Apply Stokes's theorem twice.
   - *Why needed:* This makes $\mathcal{I}$ a well-defined map on classes.

3. **$\mathcal{I}$ is an isomorphism on a convex open subset of $\mathbb{R}^n$.** For $U \subseteq \mathbb{R}^n$ convex (or star-shaped), both sides are $\mathbb{R}$ in degree zero (constant functions on $U$ ↔ "evaluate at a point" functional) and zero in positive degrees (Poincaré lemma; contractibility). The de Rham homomorphism in degree zero sends $1 \in H^0_{dR}(U) = \mathbb{R}$ to the constant-$1$ functional in $H^0(U; \mathbb{R}) = \mathbb{R}$ — non-zero, hence an isomorphism on the $1$-dimensional space.
   - *Hint:* Both sides are $\mathbb{R}$ in degree $0$ and zero elsewhere by Poincaré lemma / contractibility.
   - *Why needed:* Base case for the induction.

4. **Naturality with respect to pullback and Mayer–Vietoris.** $\mathcal{I}$ commutes with pullback by smooth maps: for $f : M \to N$ smooth, $\mathcal{I} \circ f^*_{dR} = f^*_{\text{sing}} \circ \mathcal{I}$. $\mathcal{I}$ commutes with the connecting maps $\delta_{dR}$ and $\delta_{\text{sing}}$ of the respective Mayer–Vietoris sequences for an open cover $\{U, V\}$ of any smooth manifold.
   - *Hint:* Naturality with respect to smooth maps follows from "integrate the pullback" = "pullback the integral." Naturality with Mayer–Vietoris is a chain-level check using the explicit formulas for the connecting maps.
   - *Why needed:* Required to apply the five lemma in the inductive step.

5. **Five lemma argument.** Given an open cover $M = U \cup V$ with $\mathcal{I}$ an isomorphism on $U$, $V$, and $U \cap V$, the commutative diagram of Mayer–Vietoris sequences (singular and de Rham) has four out of five vertical maps being isomorphisms; by the **five lemma**, the fifth — which is $\mathcal{I}$ on $M$ — is also an isomorphism.
   - *Hint:* Standard five-lemma argument from homological algebra. The diagram:
   $$
   \begin{array}{c}
   \cdots \to H^{p-1}_{dR}(U \cap V) \to H^p_{dR}(M) \to H^p_{dR}(U) \oplus H^p_{dR}(V) \to H^p_{dR}(U \cap V) \to H^{p+1}_{dR}(M) \to \cdots \\
   \downarrow \mathcal{I} \quad\quad\quad \downarrow \mathcal{I} \quad\quad\quad \downarrow \mathcal{I} \oplus \mathcal{I} \quad\quad\quad \downarrow \mathcal{I} \quad\quad\quad \downarrow \mathcal{I} \\
   \cdots \to H^{p-1}(U \cap V; \mathbb{R}) \to H^p(M; \mathbb{R}) \to H^p(U; \mathbb{R}) \oplus H^p(V; \mathbb{R}) \to H^p(U \cap V; \mathbb{R}) \to H^{p+1}(M; \mathbb{R}) \to \cdots
   \end{array}
   $$
   - *Why needed:* This is the inductive step.

6. **Finite good cover induction.** Every smooth manifold admits a good cover by geodesically convex balls in some Riemannian metric (Lee Theorem 1.34). For compact $M$, the cover is finite. Iterate the five lemma along the good cover: each finite-piece cover gives an isomorphism on the union, by induction. Eventually $\mathcal{I}$ is an isomorphism on all of $M$.
   - *Hint:* Use that finite intersections in a good cover are themselves contractible (hence the isomorphism holds on intersections by step 3).
   - *Why needed:* Completes the proof for compact $M$.

7. **Non-compact case via partition of unity / colimit.** For non-compact $M$, use that $M$ is the increasing union of compact pieces, and the de Rham and singular cohomologies are colimits of the finite-piece cohomologies. The isomorphism on each finite piece propagates to the colimit.
   - *Hint:* Partition of unity arguments; see Lee §18.
   - *Why needed:* Completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Well-definedness of the de Rham Homomorphism
> **Statement:** For $\omega \in \Omega^p(M)$ closed and $c$ a smooth $p$-cycle, the integral $\int_c \omega$ depends only on the cohomology class $[\omega] \in H^p_{dR}(M)$ and the homology class $[c] \in H_p^\infty(M; \mathbb{R})$.
>
> **Hint:** Two applications of Stokes's theorem: one for $\omega' = \omega + d\eta$ (use $\partial c = 0$), one for $c' = c + \partial b$ (use $d\omega = 0$).
>
> **Why needed:** Without well-definedness, the de Rham homomorphism is not a well-defined map of cohomology groups.
>
> > [!note]- Full proof
> > *Independence of representative for $[\omega]$:* if $\omega' = \omega + d\eta$, then by Stokes,
> > $$
> > \int_c \omega' - \int_c \omega = \int_c d\eta = \int_{\partial c} \eta = 0,
> > $$
> > since $\partial c = 0$ (assuming $c$ is a cycle).
> >
> > *Independence of representative for $[c]$:* if $c' = c + \partial b$, then by Stokes,
> > $$
> > \int_{c'} \omega - \int_c \omega = \int_{\partial b} \omega = \int_b d\omega = 0,
> > $$
> > since $d\omega = 0$ (assuming $\omega$ is closed).

> [!note]- Lemma 2: $\mathcal{I}$ is an Isomorphism on Convex Open Subsets of $\mathbb{R}^n$
> **Statement:** For $U \subseteq \mathbb{R}^n$ convex open, the de Rham homomorphism $\mathcal{I} : H^p_{dR}(U) \to H^p(U; \mathbb{R})$ is an isomorphism for every $p$. Specifically: both sides are $\mathbb{R}$ in degree $0$ and zero in positive degrees.
>
> **Hint:** Use the Poincaré lemma on the de Rham side and contractibility (homotopy invariance) on the singular side.
>
> **Why needed:** This is the base case of the inductive comparison.
>
> > [!note]- Full proof
> > *de Rham side:* By the Poincaré lemma ([[Thm - The Poincaré Lemma on a Star-Shaped Region]]), $H^k_{dR}(U) = 0$ for $k \geq 1$. In degree $0$, $H^0_{dR}(U) = \{f : U \to \mathbb{R} : df = 0\} = \{\text{locally constant functions}\}$ which equals $\mathbb{R}$ since $U$ is connected.
> >
> > *Singular side:* $U$ is contractible (convex), so by homotopy invariance, $H^p(U; \mathbb{R}) = H^p(\text{point}; \mathbb{R})$, which is $\mathbb{R}$ in degree zero and zero elsewhere.
> >
> > *The map $\mathcal{I}$ in degree $0$:* a closed $0$-form is a function $f$ on $U$ with $df = 0$, i.e. a constant function $f \equiv \lambda \in \mathbb{R}$. A $0$-cycle in $U$ is a formal sum of points (with vanishing boundary in degree $-1$, automatic). The pairing $\int_p f = f(p) = \lambda$ for any point $p$. So $\mathcal{I}(\lambda) \in H^0(U; \mathbb{R}) = \mathbb{R}$ is the functional "evaluate at any point" times $\lambda$. This is the generator of $H^0(U; \mathbb{R}) = \mathbb{R}$ when $\lambda = 1$. So $\mathcal{I}$ in degree $0$ is the identity $\mathbb{R} \to \mathbb{R}$, an isomorphism.
> >
> > In degrees $\geq 1$ both sides are zero, so $\mathcal{I}$ is trivially an isomorphism.

> [!note]- Lemma 3: Naturality with respect to Mayer–Vietoris
> **Statement:** For an open cover $\{U, V\}$ of a smooth manifold $M$, the de Rham homomorphism $\mathcal{I}$ commutes with the Mayer–Vietoris connecting maps on both sides — the diagram of long exact sequences
> $$
> \begin{array}{c}
> \cdots \to H^p_{dR}(M) \to H^p_{dR}(U) \oplus H^p_{dR}(V) \to H^p_{dR}(U \cap V) \xrightarrow{\delta_{dR}} H^{p+1}_{dR}(M) \to \cdots \\
> \downarrow \mathcal{I} \quad \quad \downarrow \mathcal{I} \oplus \mathcal{I} \quad \quad \downarrow \mathcal{I} \quad \quad \downarrow \mathcal{I} \\
> \cdots \to H^p(M; \mathbb{R}) \to H^p(U; \mathbb{R}) \oplus H^p(V; \mathbb{R}) \to H^p(U \cap V; \mathbb{R}) \xrightarrow{\delta_{\text{sing}}} H^{p+1}(M; \mathbb{R}) \to \cdots
> \end{array}
> $$
> commutes — every square is commutative.
>
> **Hint:** The horizontal maps in the de Rham sequence are induced by pullback under inclusions (and partition-of-unity arguments for $\delta_{dR}$); the horizontal maps in the singular sequence are induced by inclusion (and a chain-level "subdivision-and-split" argument for $\delta_{\text{sing}}$). Both connecting maps respect integration, which is the chain-level intertwining.
>
> **Why needed:** Required for the five lemma argument that propagates the de Rham isomorphism from cover pieces to the union.
>
> > [!note]- Sketch
> > The commutativity of the "obvious" squares (those involving pullback or inclusion induced maps) is the easy direction: integration of forms over chains commutes with pullback and restriction.
> > 
> > The non-trivial square is the one involving the connecting maps $\delta_{dR}$ and $\delta_{\text{sing}}$. The de Rham $\delta_{dR}$ is constructed via a partition of unity $\{\rho_U, \rho_V\}$: a class $[\eta] \in H^p_{dR}(U \cap V)$ extends to $\rho_U \eta$ on $U$ and $\rho_V \eta$ on $V$, and $d(\rho_U \eta) - d(\rho_V \eta) \in \Omega^{p+1}(M)$ is the representative of $\delta_{dR}[\eta]$. The singular $\delta_{\text{sing}}$ on a class $[c] \in H^p(M; \mathbb{R})$ involves subdividing a cocycle and splitting it across $U$, $V$. The commutativity reduces to Stokes's theorem on the partition-of-unity decomposition, plus the chain-level identity for the singular subdivision.
> >
> > Full details are in Lee, Theorem 18.14, or Bott–Tu, Theorem 8.9. The verification is technical but mechanical.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For every smooth manifold $M$ and every $p \geq 0$, the de Rham homomorphism $\mathcal{I} : H^p_{dR}(M) \to H^p(M; \mathbb{R})$ is an isomorphism.
>
> *Proof.*
>
> **Step 1 — well-definedness.** By Lemma 1, $\mathcal{I}[\omega][c] = \int_c \omega$ is well-defined modulo the cohomology and homology classes. It is $\mathbb{R}$-linear in each argument by linearity of the integral.
>
> **Step 2 — base case (convex open subsets of $\mathbb{R}^n$).** By Lemma 2, $\mathcal{I}$ is an isomorphism on any convex open subset of $\mathbb{R}^n$.
>
> **Step 3 — induction on a finite good cover.** Let $\{U_1, \dots, U_n\}$ be a finite good cover of $M$ (cover by geodesically convex balls in some Riemannian metric; such a cover exists for any compact manifold). We prove the theorem for $M_k = U_1 \cup \cdots \cup U_k$ by induction on $k$.
>
> *Base case $k = 1$:* $M_1 = U_1$ is contractible (diffeomorphic to a ball), so by Step 2, $\mathcal{I}$ is an isomorphism.
>
> *Inductive step:* Assume $\mathcal{I}$ is an isomorphism on $M_{k-1}$. Consider the open cover $M_k = M_{k-1} \cup U_k$, with intersection $M_{k-1} \cap U_k$. By the good-cover property, $M_{k-1} \cap U_k = (U_1 \cap U_k) \cup \cdots \cup (U_{k-1} \cap U_k)$ is the union of contractibles. The hypothesis on $M_{k-1}$ (inductively isomorphism), and on $U_k$ (Step 2), gives $\mathcal{I}$ as an isomorphism on both. Need to verify on $M_{k-1} \cap U_k$ as well: this is a "smaller" union of contractibles, so by another induction (on $k$ separately), $\mathcal{I}$ is an isomorphism on $M_{k-1} \cap U_k$ as well.
>
> Apply the **Five Lemma** to the commutative diagram (Lemma 3) of Mayer–Vietoris sequences with the cover $\{M_{k-1}, U_k\}$ of $M_k$. Four out of five vertical maps are isomorphisms (by induction: on $M_{k-1}$, $U_k$, and $M_{k-1} \cap U_k$); hence $\mathcal{I}$ on $M_k$ is also an isomorphism.
>
> After $n$ steps, $M_n = M$ and $\mathcal{I}$ is an isomorphism on $M$ — assuming $M$ is compact.
>
> **Step 4 — non-compact case.** For non-compact $M$, $M$ is the increasing union of compact submanifolds $K_1 \subseteq K_2 \subseteq \cdots$ (using the second-countable assumption). On each $K_n$ — taking a good cover and applying Step 3 — $\mathcal{I}$ is an isomorphism. The cohomologies $H^p_{dR}(M)$ and $H^p(M; \mathbb{R})$ are computed as inverse limits of the cohomologies of $K_n$'s, and naturality (Lemma 3) ensures the isomorphism propagates to the limit. Details in Lee §18.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Betti numbers from de Rham computations.** Compute $H^p_{dR}(M)$ for a manifold by direct form computation or de Rham Mayer–Vietoris; conclude the Betti numbers $b_p(M) = \dim H^p_{dR}(M)$ — topological invariants. *Example:* $b_k(T^n) = \binom{n}{k}$ from the de Rham computation using wedges of angular forms; by de Rham, these are also the singular Betti numbers.

**Euler characteristic via Chern–Gauss–Bonnet.** For a compact oriented even-dimensional Riemannian manifold $M$, the Chern–Gauss–Bonnet theorem expresses $\chi(M) = \int_M e(TM)$, where $e(TM)$ is the Euler form (a specific polynomial in the curvature). The de Rham theorem ensures that this curvature integral is a topological invariant — it does not depend on the metric chosen.

**Periods of closed forms.** For a closed $p$-form $\omega$ and a basis of $H_p(M; \mathbb{Z})$, the **periods** $\pi_i = \int_{z_i} \omega$ determine $[\omega] \in H^p_{dR}(M; \mathbb{R})$ completely. Conversely, given any prescribed real numbers $\pi_1, \dots, \pi_b$, there exists a closed $p$-form with those periods. This is the de Rham theorem in periods form (Frankel 13.4a, formula 13.35) and is the practical way to construct closed forms with prescribed cohomology.

**Topological obstructions to smooth structures.** Two non-homeomorphic smooth manifolds can be distinguished by their de Rham cohomology (which is a topological invariant by de Rham). Conversely, two homeomorphic smooth manifolds with the same de Rham cohomology — even with isomorphic homotopy types — might have different smooth structures (e.g. Milnor's exotic $7$-spheres). The de Rham theorem says smooth structure doesn't add cohomological information beyond what topology already encodes, but it leaves room for *other* invariants (Donaldson, Seiberg–Witten) to distinguish smooth structures.

**Maxwell's equations in cohomological form.** In Minkowski space, the electromagnetic field is a closed $2$-form $F$ on spacetime, satisfying $dF = 0$ (homogeneous Maxwell). By the de Rham theorem on a contractible region of spacetime, $F = dA$ for a $1$-form $A$ — the four-potential. The gauge freedom $A \mapsto A + d\chi$ is the cohomological non-uniqueness of the primitive. On non-contractible regions (e.g. spacetime with monopoles removed), the de Rham cohomology of the region encodes the magnetic monopole charges as integer periods of $F$ — see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Bridges

- **[[Thm - The de Rham Theorem (Statement)|de Rham theorem statement]] in `Differential Geometry X`** — the statement-only version we filled in earlier. This page is its proof. The two are the same theorem; together they form the bridge between de Rham cohomology and singular cohomology.

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]]** — the local input. Both de Rham and singular cohomology agree on contractible pieces (each is $\mathbb{R}$ in degree zero, zero in higher degrees). The de Rham theorem assembles these local agreements via Mayer–Vietoris.

- **[[Thm - Homotopy Invariance of de Rham Cohomology|Homotopy invariance of de Rham cohomology]]** — the de Rham version of the singular-cohomology homotopy invariance. Both forms-side and singular-side cohomologies are homotopy invariants, and the de Rham theorem makes this match precise.

- **[[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris (singular)]]** and **[[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris (de Rham)]]** — the inductive engines. Both have Mayer–Vietoris sequences, and they agree (via the de Rham homomorphism). The proof of de Rham reduces to showing the two Mayer–Vietoris sequences agree by naturality.

- **The Eilenberg–Steenrod axioms** — singular cohomology satisfies them; by de Rham, $H^*_{dR}$ also satisfies them on smooth manifolds. The Eilenberg–Steenrod uniqueness theorem (cohomology theories agreeing on a point agree on CW complexes) gives an abstract reason why the two theories must agree.

- **Hodge theory** — on a compact oriented Riemannian manifold, the de Rham cohomology has *canonical* representatives — harmonic forms. By de Rham, harmonic forms are representatives of singular cohomology classes, mediated by the integration pairing. The Hodge decomposition is a refinement of de Rham (see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]]).

- **Group theory: cohomology as quotients of abelian groups** — both $H^k_{dR}(M)$ and $H^k(M; \mathbb{R})$ are $\mathbb{R}$-vector spaces (in particular [[Def - Abelian Group|abelian groups]]). The de Rham homomorphism is a group homomorphism, and the isomorphism is one of abelian groups (in fact of $\mathbb{R}$-vector spaces).

---

# Unlocked by This

> [!tip] **Topological Invariance of $H^k_{dR}$** *(from this same topic)*
> Homeomorphic smooth manifolds have isomorphic de Rham cohomology. This is immediate from de Rham + topological invariance of singular cohomology, but it is striking because the smooth structure was used to define the de Rham complex. The conclusion: smooth structure makes no contribution to cohomology — the answer is purely topological.

> [!tip] **Singular Cohomology of Smooth Manifolds via Forms** *(from this same topic)*
> Every singular cohomology computation on a smooth manifold has an equivalent de Rham computation. This means many topological invariants — Betti numbers, Euler characteristic, signature, characteristic classes — can be computed by smooth-form techniques (integration, Hodge theory, Chern–Weil theory). The "smoothness" can be exploited to make explicit calculations tractable.

> [!tip] **Hodge Decomposition and Harmonic Forms** *(from Riemannian Geometry)*
> On a compact oriented Riemannian manifold, Hodge theory picks out a *canonical* representative of each de Rham cohomology class — the unique harmonic form satisfying $\Delta\omega = 0$. By de Rham, this gives canonical representatives in singular cohomology too. The Hodge decomposition $\Omega^k = \ker \Delta \oplus d\Omega^{k-1} \oplus d^*\Omega^{k+1}$ is the analytic refinement of the de Rham theorem. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

> [!tip] **Chern–Weil Theory and Characteristic Classes** *(from Differential Topology)*
> Characteristic classes of vector bundles — Chern, Pontryagin, Euler classes — are de Rham cohomology classes built from curvature of a connection (Chern–Weil construction). By de Rham, they are also singular cohomology classes — topological invariants of the bundle, computable by smooth-form techniques. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]].

> [!tip] **Gauge Theory and Instanton Numbers** *(from Mathematical Physics)*
> In gauge theory, the **instanton number** of a connection is the de Rham cohomology class of $\mathrm{tr}(F \wedge F)$ for the curvature $F$ — an integer (topological), but computed as an integral of forms. By de Rham, this matches the second Chern class of the underlying principal bundle, connecting physics to topology. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

> [!tip] **Sheaf Cohomology and the Abstract de Rham Theorem** *(from Sheaf Theory)*
> The de Rham theorem is one instance of a much more general phenomenon: every **soft resolution** of the constant sheaf $\mathbb{R}$ on a manifold computes the same cohomology, which equals the sheaf cohomology $H^*(M; \mathbb{R})$. The de Rham complex is one such resolution; the Čech complex is another; the simplicial cochain complex is a third. The abstract de Rham theorem says all of these compute the same cohomology — the de Rham theorem on smooth manifolds is one (very concrete) instance.

> [!tip] **Comparison Theorems in Arithmetic Geometry** *(from Algebraic Geometry)*
> For a smooth proper variety $X$ over $\mathbb{Q}$, there are four "classical" cohomology theories: **Betti** (singular cohomology of complex points), **de Rham** (algebraic differential forms), **étale** ($\ell$-adic for primes $\ell$), and **crystalline** ($p$-adic). The comparison theorems between these — Artin's comparison, $p$-adic Hodge theory — are the modern generalisations of the de Rham theorem of this chapter, and they form the central machinery of arithmetic geometry.
