---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - Immersion, Submersion, and Embedding"
  - "Thm - Local Submersion Theorem"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds, $m = \dim M$, $n = \dim N$. An **open map** is a map that sends open sets to open sets. A **quotient map** is a continuous surjection $f : X \to Y$ such that $V \subseteq Y$ is open iff $f^{-1}(V) \subseteq X$ is open. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Submersions are Open Maps).** Every smooth submersion $F : M \to N$ is an open map: for every open subset $U \subseteq M$, the image $F(U)$ is open in $N$.

> **Corollary (Surjective submersions are quotient maps).** Every surjective smooth submersion $F : M \to N$ is a topological quotient map.

> **Corollary (Submersions detect openness of preimages).** A subset $V \subseteq N$ is open in $N$ if and only if $F^{-1}(V) \subseteq M$ is open in $M$ — assuming $F$ is a *surjective* submersion. (One direction is continuity; the surjective-submersion case gives the other.)

---

# Motivation

This theorem is the topological consequence of the [[Thm - Local Submersion Theorem|local submersion theorem]]'s coordinate normal form. It says that submersions are not just *locally* nice (locally projections), but *globally* open as maps — they preserve openness in both directions. This makes submersions the smooth-category analogue of topological quotient maps: in topology, a quotient map is the prototypical "open + surjective" map characterising the quotient topology; in differential geometry, a surjective submersion is the prototype of the smooth quotient construction.

The result is short but consequential. It tells us that the image of a submersion is automatically a topologically nice subset of the target — open if the domain is open. So when we apply the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] to a submersion, the conclusion "$F^{-1}(c)$ is a properly embedded submanifold" implies *not just* the manifold structure on the preimage, but a useful topological property of the map itself: surjective submersions exhibit their codomains as quotients of their domains. This is the foundation of the **smooth quotient theorem** (Lie [[Def - Group|group]] actions producing homogeneous spaces) and of **fibre bundle theory** (locally trivial submersions).

The result also fails dramatically for *immersions* — providing a useful contrast. An immersion's image, with the [[Def - Subspace|subspace]] topology, need not be open (the inclusion of the sphere into Euclidean space is the canonical example: $S^n \hookrightarrow \mathbb{R}^{n+1}$ is a smooth embedding but its image is closed and lower-dimensional, hence not open). Immersions preserve the *injection* direction of openness (an embedding is a homeomorphism onto its image), while submersions preserve the *surjection* direction.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$F$ is a smooth submersion". Recognising this in disguise:

The first disguised source is **a smooth fibre bundle projection**. Property $B$: $\pi : E \to B$ is a fibre bundle. The bridge: fibre bundle projections are submersions (in local trivialisations, they are coordinate projections). The non-obviousness: even when the global structure of the bundle is complicated, the projection is automatically open by Submersion-is-Open. *Example:* the projection $TM \to M$ from the tangent bundle is open, so vector field "support" (closure of the set where the field is nonzero) projects to an open set in $M$.

The second disguised source is **a free, proper Lie group action's quotient projection**. Property $B$: $G$ acts freely and properly on $M$ smoothly, and $\pi : M \to M/G$ is the quotient. The bridge: $\pi$ is a smooth submersion by the smooth quotient theorem. *Example:* the projection $\mathrm{O}(n+1) \to S^n$ exhibiting the sphere as a homogeneous space is open — hence open subsets of $\mathrm{O}(n+1)$ (e.g., balls in the orthogonal group) project to open subsets of $S^n$.

The third disguised source is **a local diffeomorphism**. Property $B$: $F$ is a local diffeomorphism. The bridge: local diffeomorphisms are submersions (and immersions, and have $\dim M = \dim N$). *Example:* covering maps are local diffeomorphisms, hence open. The exponential map $\mathbb{R} \to S^1$ is open — open intervals in $\mathbb{R}$ project to open arcs in $S^1$.

**Targets (Output Amplification)**

The conclusion is "$F(U)$ is open in $N$ for every open $U \subseteq M$".

Combine with **a surjectivity hypothesis.** Property $D$: $F$ is surjective. The amplified result $E$: $F$ is a topological quotient map. The quotient topology is the strongest one making $F$ continuous; since open sets project to open sets and continuity goes the other way, the quotient topology coincides with $N$'s topology. So $N$ is the topological quotient of $M$ by the fibre relation. This is the foundation of the smooth quotient construction.

Combine with **the characteristic property.** Property $D$: a map $G : N \to P$ is being tested for smoothness. The amplified result $E$: when $F$ is a surjective submersion, $G$ is smooth iff $G \circ F$ is smooth. The "if" direction uses openness: $G \circ F$ smooth gives smoothness on each local-section image, and openness lets us glue these into smoothness on a neighbourhood of any point of $N$. This is the *characteristic property of surjective smooth submersions*.

Combine with **a compactness hypothesis.** Property $D$: $M$ is compact. The amplified result $E$: $F(M) = N$ is open *and* closed (continuous image of compact is compact, hence closed in Hausdorff). So $F(M)$ is a clopen subset of $N$; if $N$ is connected, $F$ is surjective. *Example:* a compact connected manifold cannot map to a non-compact connected manifold by a submersion. This is the obstruction behind various surjectivity theorems.

---

# Why Is It True

The theorem is a one-line consequence of the [[Thm - Local Submersion Theorem|local submersion theorem]]: the local theorem says that, in coordinates, a submersion *is* a coordinate projection, and coordinate projections are patently open. Globally, openness is a local property, so the local conclusion globalises.

**The bolded one-liner mechanism summary: in submersion-normal-form coordinates, $F$ is the projection $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^n)$ — and coordinate projections are open by elementary topology.**

Here is the argument. Let $U \subseteq M$ be open, and let $q \in F(U)$. We want to show $q$ has a neighbourhood in $N$ contained in $F(U)$.

Pick $p \in U$ with $F(p) = q$. By the local submersion theorem, there are smooth charts $(U_p, \varphi)$ around $p$ in $M$ and $(V_q, \psi)$ around $q$ in $N$ with $F(U_p) \subseteq V_q$, in which $F$ has the coordinate representation $\hat F(x^1, \dots, x^m) = (x^1, \dots, x^n)$ — the standard projection.

Shrink $U_p$ to $U_p \cap U$, still open, still containing $p$. In coordinates, $\varphi(U_p \cap U)$ is open in $\mathbb{R}^m$. The projection $\hat F : \mathbb{R}^m \to \mathbb{R}^n$ is an open map (the standard projection is open by elementary topology — its image $(x^1, \dots, x^n)$ depends continuously on $(x^1, \dots, x^m)$, and for any open set $W \subseteq \mathbb{R}^m$, the projection $\hat F(W) = \{(x^1, \dots, x^n) : (x^1, \dots, x^n, y^1, \dots, y^{m-n}) \in W$ for some $y\}$ is open as a union of "horizontal slices" of open sets — actually it's open because the projection is the canonical map of a product onto a factor).

So $\hat F(\varphi(U_p \cap U))$ is open in $\mathbb{R}^n$, hence $\psi^{-1}(\hat F(\varphi(U_p \cap U))) \subseteq V_q$ is open in $N$. By construction, this set is contained in $F(U_p \cap U) \subseteq F(U)$, and it contains $q$ (since $\psi^{-1}(\hat F(\varphi(p))) = F(p) = q$). So $q$ has a neighbourhood in $N$ contained in $F(U)$.

Since $q$ was arbitrary in $F(U)$, $F(U)$ is open in $N$.

The argument is short because the local submersion theorem has done the work: it has already put $F$ into the standard projection form, and projections are manifestly open.

Why is openness of coordinate projection itself "elementary"? Because for any open box $B = \prod_i (a_i, b_i)$ in $\mathbb{R}^m$, the projection $\hat F(B) = \prod_{i \leq n}(a_i, b_i)$ is again an open box in $\mathbb{R}^n$. General open sets are unions of open boxes, so projections of general opens are unions of open boxes, hence open. This is the basic fact about product topologies (the projections are open).

The corollary "surjective submersions are quotient maps" follows from the definition of quotient map. A quotient map is a continuous surjection $f$ such that $V$ is open iff $f^{-1}(V)$ is open. The forward direction is continuity. For the reverse: if $f^{-1}(V)$ is open in $M$, then $V = f(f^{-1}(V))$ (using surjectivity) is the image of an open set under $f$, hence open by Submersion-is-Open. So $V$ open in $N$ iff $f^{-1}(V)$ open in $M$, i.e., $f$ is a quotient map.

---

# What Makes This Hard

The argument is short, and the main "trap" is in applying it incorrectly to non-submersions: students sometimes try to claim that immersions are open (false: an embedding's image need not be open), or that any smooth surjection is a quotient map (false: a smooth surjection need not be a submersion, and need not be open — example: $\mathbb{R}^2 \to \mathbb{R}$ given by $(x, y) \mapsto xy$, where the image of any small neighbourhood of the origin contains $0$ but is not a neighbourhood of $0$ in $\mathbb{R}$). The conceptual content is that *only* submersions are guaranteed to be open; surjective non-submersions can fail. The conclusion is sharp: the local-submersion-theorem coordinate form is exactly the structure that makes openness automatic, and it requires the differential to be surjective at every point.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
A point $q \in F(U)$ has a preimage $p \in U$. Apply the local submersion theorem at $p$: in suitable charts, $F$ is the standard projection. Open sets in $M$ restrict to open sets in the chart, and projections of open sets in Euclidean space are open. Translate back to $N$ via the chart.

**Subgoal decomposition:**

1. **Pick a preimage point.** Given $U \subseteq M$ open and $q \in F(U)$, pick $p \in U \cap F^{-1}(q)$.
   - *Hint:* $q$ in the image means at least one preimage exists.

2. **Apply the local submersion theorem.** Get charts $(U_p, \varphi)$ at $p$ and $(V_q, \psi)$ at $q$ in which $F$ is the standard projection $\hat F(x^1, \dots, x^m) = (x^1, \dots, x^n)$.
   - *Hint:* This is the [[Thm - Local Submersion Theorem|local submersion theorem]]'s output.

3. **Restrict to the open intersection.** Replace $U_p$ by $U_p \cap U$, still open, still containing $p$. In coordinates, $\varphi(U_p \cap U)$ is an open subset of $\mathbb{R}^m$ containing $0$ (the origin, since the chart was centred at $p$).
   - *Hint:* Intersection of open sets is open; chart maps are [[Def - Homeomorphism|homeomorphisms]].

4. **Project to $\mathbb{R}^n$.** The image $\hat F(\varphi(U_p \cap U))$ is open in $\mathbb{R}^n$ because the standard projection of an open set in $\mathbb{R}^m$ onto its first $n$ coordinates is open. Specifically: for any open box $B = \prod_i (a_i, b_i) \subseteq \mathbb{R}^m$, the projection $\hat F(B) = \prod_{i \leq n}(a_i, b_i)$ is an open box in $\mathbb{R}^n$.
   - *Hint:* Projections in product topologies are open.

5. **Translate back to $N$.** The set $\psi^{-1}(\hat F(\varphi(U_p \cap U)))$ is open in $N$ (preimage of open under the homeomorphism $\psi$), contained in $V_q$, contained in $F(U_p \cap U) \subseteq F(U)$, and contains $q$.
   - *Hint:* Chart inverse homeomorphism preserves openness.

6. **Conclude.** $q$ has an open neighbourhood in $F(U)$. Since $q$ was arbitrary, $F(U)$ is open.
   - *Hint:* "Every point has a neighbourhood in $F(U)$" is the definition of $F(U)$ being open.

---

# Lemma Decomposition

> [!note]- Lemma 1: The standard projection is an open map
> **Statement:** The standard projection $\pi : \mathbb{R}^m \to \mathbb{R}^n$, $\pi(x^1, \dots, x^m) = (x^1, \dots, x^n)$, is an open map: for every open $W \subseteq \mathbb{R}^m$, $\pi(W)$ is open in $\mathbb{R}^n$.
>
> **Hint:** Every open set is a union of open boxes. The projection of an open box is an open box.
>
> **Why needed:** It is the elementary topological fact behind the manifold result. Without this, the whole proof has no content.
>
> > [!note]- Full proof
> > Let $W \subseteq \mathbb{R}^m$ be open. For each $x \in W$, by definition there is an open box $B_x = \prod_{i=1}^m (a^x_i, b^x_i)$ with $x \in B_x \subseteq W$. The projection $\pi(B_x) = \prod_{i=1}^n (a^x_i, b^x_i)$ is an open box in $\mathbb{R}^n$, containing $\pi(x)$.
> >
> > So $\pi(W) = \pi\left(\bigcup_{x \in W} B_x\right) = \bigcup_{x \in W} \pi(B_x)$ is a union of open boxes in $\mathbb{R}^n$, hence open.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be a smooth submersion and $U \subseteq M$ open. We show $F(U)$ is open in $N$.
>
> **Step 1.** Let $q \in F(U)$. Pick $p \in U$ with $F(p) = q$.
>
> **Step 2.** By the [[Thm - Local Submersion Theorem|local submersion theorem]] applied at $p$, there exist smooth charts $(U_p, \varphi)$ on $M$ centred at $p$ and $(V_q, \psi)$ on $N$ centred at $q$, with $F(U_p) \subseteq V_q$, such that the coordinate representation $\psi \circ F \circ \varphi^{-1}$ is the standard projection $\hat F : \mathbb{R}^m \to \mathbb{R}^n$, $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^n)$.
>
> **Step 3.** Replace $U_p$ by $U_p \cap U$; still open, still containing $p$. Set $W = \varphi(U_p \cap U) \subseteq \mathbb{R}^m$, which is open (as the image of an open set under the chart homeomorphism).
>
> **Step 4.** By Lemma 1, $\hat F(W) \subseteq \mathbb{R}^n$ is open. So $\psi^{-1}(\hat F(W))$ is open in $N$ (preimage of open under the chart homeomorphism $\psi^{-1}$).
>
> **Step 5.** Verify $\psi^{-1}(\hat F(W)) \subseteq F(U_p \cap U) \subseteq F(U)$. Indeed, for any $y \in \psi^{-1}(\hat F(W))$, we have $\psi(y) = \hat F(x)$ for some $x \in W = \varphi(U_p \cap U)$, so $x = \varphi(p')$ for some $p' \in U_p \cap U$. Then $\psi(y) = \hat F(\varphi(p')) = \psi(F(p'))$, so $y = F(p') \in F(U_p \cap U) \subseteq F(U)$.
>
> **Step 6.** Also $q = F(p) \in \psi^{-1}(\hat F(W))$ since $p \in U_p \cap U$ and $\hat F(\varphi(p)) = \hat F(0) = 0 = \psi(q)$, so $\psi(q) \in \hat F(W)$.
>
> **Step 7.** $q$ has the open neighbourhood $\psi^{-1}(\hat F(W))$ contained in $F(U)$. Since $q \in F(U)$ was arbitrary, $F(U)$ is open. $\qquad\blacksquare$
>
> **Corollary (Quotient map property).** Suppose $F$ is also surjective. To show $F$ is a quotient map, we need: $V \subseteq N$ is open iff $F^{-1}(V) \subseteq M$ is open.
>
> The forward direction is continuity: if $V$ is open, $F^{-1}(V)$ is open.
>
> For the reverse: if $F^{-1}(V)$ is open in $M$, then $F(F^{-1}(V))$ is open in $N$ by the theorem just proved. But for surjective $F$, $F(F^{-1}(V)) = V$. So $V$ is open. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fibre bundles in physics.** Gauge theory's principal bundles $P \to M$ have the projection an open submersion. The openness is what makes "local gauge transformations" well-defined — a gauge transformation on an open subset of $M$ pulls back to a gauge transformation on its open preimage in $P$, and the two descend through the open projection.

**The smooth quotient theorem.** A free, proper smooth action of a Lie group $G$ on $M$ has the quotient map $\pi : M \to M/G$ a surjective submersion, hence a quotient map. The openness of $\pi$ is what gives the orbit space its quotient topology, and the manifold structure on $M/G$ depends on this in subtle ways (the smooth structure must be consistent with the open-projection topology).

**The Hopf [[Def - Fibration|fibration]]'s open structure.** The Hopf map $h : S^3 \to S^2$ is a surjective submersion, hence open. Hence open neighbourhoods on $S^2$ pull back to open neighbourhoods on $S^3$, and any "patch" of $S^2$ admits a local product structure $h^{-1}(U) \cong U \times S^1$. See [[Ex - The Hopf Map is a Submersion]].

---

# Bridges

- **[[Thm - Local Submersion Theorem|Local Submersion Theorem]]** — the engine. The openness theorem is a one-line corollary of the local submersion theorem's normal form plus the elementary fact that coordinate projections are open.

- **[[Def - Immersion, Submersion, and Embedding|Submersion]]** — the structural input. The theorem is a feature of submersions specifically, not arbitrary smooth maps. Immersions, in particular, are *not* open (the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$ is closed and not open).

- **Topological quotient maps** — the analogue. In topology, a surjective open continuous map is a quotient map. In smooth geometry, a surjective smooth submersion is the smooth-category quotient map. The Submersion-is-Open theorem is what makes this analogy work.

- **Characteristic property of submersions** — the downstream consequence. A surjective smooth submersion $\pi : M \to N$ satisfies: $G : N \to P$ is smooth iff $G \circ \pi$ is smooth. The openness theorem is one of the two ingredients (the other is the local section theorem); together they give the characteristic property.

---

# Unlocked by This

> [!tip] Surjective Smooth Submersions as Quotient Maps *(from this topic)*
> A surjective smooth submersion is a topological quotient map. This is the cleanest characterisation: open + continuous + surjective = quotient map. It is the foundation of the smooth quotient theorem.

> [!tip] Smooth Fibre Bundle Structure *(from Algebraic Topology)*
> A surjective submersion with locally trivial fibres is a **fibre bundle**, and the projection is open. The openness is one of the technical inputs to the long exact sequence of homotopy groups for a fibration.

> [!tip] Homogeneous Spaces as Quotient Manifolds *(from Lie Theory)*
> When a Lie group $G$ acts freely and properly on $M$, the quotient $M/G$ is a smooth manifold and $\pi : M \to M/G$ is an open surjective submersion. The openness makes the quotient topology on $M/G$ coincide with the manifold topology.

> [!tip] Closed Maps via Compactness *(from Topology)*
> A continuous map from a compact space to a Hausdorff space is automatically closed. Combined with openness (for submersions), this gives "clopen" image — a finite union of components. This is one route to surjectivity theorems for compact-domain submersions.
