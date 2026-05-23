---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - Smooth Homotopy of Maps"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
tags: [geometry, differential-geometry, cohomology, homotopy]
---

# Notation

$M, N$ are smooth manifolds (possibly with boundary). $F, G : M \to N$ are smooth maps. A **smooth homotopy** from $F$ to $G$ is a smooth $H : M \times \mathbb{R} \to N$ with $H(\cdot, 0) = F$ and $H(\cdot, 1) = G$ (defined on a neighborhood of $M \times [0, 1]$ in $M \times \mathbb{R}$). The pullback $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ is the linear map induced by pullback of forms — see [[Def - de Rham Cohomology]]. Two maps are **smoothly homotopic** if such an $H$ exists; the relation is an equivalence — see [[Def - Smooth Homotopy of Maps]].

---

# Statement

> **Theorem (Homotopy Invariance).** If $F, G : M \to N$ are smoothly homotopic smooth maps between smooth manifolds, then the induced cohomology maps $F^* = G^* : H^k_{dR}(N) \to H^k_{dR}(M)$ are equal for every $k \geq 0$.

> **Corollary.** If $M$ and $N$ are smoothly homotopy equivalent — that is, there are smooth $F : M \to N$ and $G : N \to M$ with $F \circ G \simeq \mathrm{id}_N$ and $G \circ F \simeq \mathrm{id}_M$ — then $H^k_{dR}(M) \cong H^k_{dR}(N)$ for every $k$, with isomorphism induced by $F$ (or equivalently by $G$).

> **Corollary (Topological invariance).** Homeomorphic smooth manifolds have isomorphic de Rham cohomology. (Every homeomorphism is, after Whitney approximation, a smooth homotopy equivalence; the corollary then applies.)

> **Corollary (Cohomology of contractible manifolds).** Any contractible smooth manifold $M$ has $H^k_{dR}(M) = 0$ for every $k \geq 1$ and $H^0_{dR}(M) = \mathbb{R}$. (The inclusion of a point is a homotopy equivalence, so $H^*_{dR}(M) \cong H^*_{dR}(\text{point})$.)

---

# Motivation

The de Rham cohomology $H^k_{dR}(M)$ is defined entirely from smooth structure — forms, derivatives, integrals. One might reasonably expect that it depends sensitively on the smooth structure, and that different smooth structures on the same topological manifold would give different answers. The homotopy invariance theorem says this is *not* what happens. de Rham cohomology depends only on the *homotopy type* of $M$ — a much coarser invariant than the smooth structure, indeed coarser than the topology itself. Spaces that can be continuously deformed into one another (in either direction) have identical de Rham cohomology.

This is remarkable for two reasons. First, it shows that an a priori smooth-structure-dependent invariant turns out to be topological — even *homotopical*. This is the bridge that connects de Rham theory to the broader world of algebraic topology, where invariants are defined for all topological spaces and are typically computed from singular simplices. The [[Thm - The de Rham Theorem (Statement)|de Rham theorem]] makes this bridge precise by identifying $H^k_{dR}(M)$ with the singular cohomology $H^k(M; \mathbb{R})$, but homotopy invariance is the first hint that such an identification is even possible.

Second, homotopy invariance is the *computational* engine of de Rham theory. Most manifolds whose cohomology we care about are too complicated to handle directly, but they are *homotopy equivalent* to simpler spaces whose cohomology is easy. The Möbius strip is homotopy equivalent to $S^1$ (via the core circle deformation retract); the punctured plane $\mathbb{R}^2 \setminus \{0\}$ is homotopy equivalent to $S^1$ (via radial projection); a tubular neighborhood of any submanifold is homotopy equivalent to the submanifold itself. In each case, before computing cohomology directly, we deform-retract to a simpler space.

The result reduces a smooth-geometric question to a purely topological one: *what is the homotopy type of $M$?* If this is known (and for most manifolds of interest it is), the cohomology is determined.

The technique of proof is itself instructive. The homotopy operator construction $h : \Omega^k(N) \to \Omega^{k-1}(M)$ satisfying $dh + hd = G^* - F^*$ is a *chain homotopy* — the algebraic-topology analogue of a continuous deformation. The pattern "construct a chain homotopy by integrating along a homotopy" is the prototype for every homotopy-invariance theorem in cohomology theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$F$ and $G$ are smoothly homotopic.* The skill is recognizing this in disguise.

The first disguised source is **two maps that agree up to a continuous deformation, with smoothness available.** Property $B$: there is a continuous homotopy between $F$ and $G$ (not necessarily smooth). By the Whitney approximation theorem, every continuous homotopy can be perturbed to a smooth one in the same homotopy class. So a continuous homotopy is just as good as a smooth one for cohomology purposes. The non-obvious step is recognizing that the smooth/continuous distinction is irrelevant at the level of cohomology, given Whitney approximation. *Example application:* showing that a continuous map between manifolds induces the same cohomology map as any smooth approximation.

The second disguised source is **the inclusion of a deformation retract.** Property $B$: $A \subseteq M$ is a deformation retract — there is a retraction $r : M \to A$ ($r|_A = \mathrm{id}_A$) and a homotopy $H : M \times I \to M$ from $\mathrm{id}_M$ to the inclusion $i \circ r$, with $H(a, t) = a$ for $a \in A$. The bridge: $i$ and $r$ are smooth homotopy inverses, so $H^*(M) \cong H^*(A)$. *Example:* the standard inclusion $S^{n-1} \hookrightarrow \mathbb{R}^n \setminus \{0\}$ is a deformation retract (radial homotopy), so $H^*(\mathbb{R}^n \setminus \{0\}) \cong H^*(S^{n-1})$.

The third disguised source is **a fiber bundle with contractible base or fiber.** Property $B$: $E \to B$ is a smooth fiber bundle with contractible base $B$. The bridge: the bundle is trivial (a section exists, the bundle is the pullback of a bundle over the point), so $E \simeq F$ where $F$ is the fiber. *Example:* a tubular neighborhood of $\partial M$ in $M$ is a bundle over $\partial M$ with contractible fiber $[0, 1)$, so it is homotopy equivalent to $\partial M$.

**Targets (Output Amplification)**

The conclusion $C$: *$F^* = G^*$ on cohomology.*

Combine $C$ with **a smooth deformation retract.** $C$ applied to $(i, r)$ gives $H^*_{dR}(M) \cong H^*_{dR}(A)$. The further result $E$: cohomology of $M$ can be computed from cohomology of a simpler subspace $A$. This is the workhorse of every concrete cohomology computation. The non-obvious payoff: a smooth-manifold cohomology becomes a cohomology of a (typically lower-dimensional) subspace, often a circle, sphere, or wedge of spheres.

Combine $C$ with **the Whitney approximation theorem.** Whitney says every continuous map between smooth manifolds is homotopic to a smooth one. So the homotopy invariance theorem extends to continuous maps: a continuous $F : M \to N$ has a well-defined pullback on cohomology, computed by smoothing $F$ to any smooth $\tilde F \simeq F$ and using $\tilde F^*$. The further result $E$: de Rham cohomology becomes a functor on the *topological* category of smooth manifolds with continuous maps.

Combine $C$ with **the existence of a smooth homotopy equivalence $M \simeq M'$.** $C$ gives $H^*_{dR}(M) \cong H^*_{dR}(M')$. The further result $E$: if $M'$ is "simpler" than $M$ — a CW complex, a wedge of spheres, a manifold of lower dimension — the cohomology of $M$ is determined by that of $M'$. This routes hard cohomology questions through homotopy theory.

---

# Why Is It True

**The single sentence: a smooth homotopy $H$ from $F$ to $G$ induces a homotopy operator $h$ between the pullback maps $F^*$ and $G^*$ at the form level, with $dh + hd = G^* - F^*$, and the right side vanishes on cohomology classes.**

The picture is the same as in the [[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]], but with an arbitrary homotopy $H$ replacing the radial contraction. Given $H : M \times I \to N$ with $H_0 = F$, $H_1 = G$, the pullback $H^*\omega$ of a form on $N$ is a form on $M \times I$. To produce a form on $M$ — to "integrate out" the $t$-direction — we contract with the vector field $\partial_t$ on $M \times I$, getting a form of one lower degree, and then integrate over $t \in [0, 1]$. This defines a linear map $h : \Omega^k(N) \to \Omega^{k-1}(M)$:

$$h\omega := \int_0^1 i_t^*\iota_{\partial_t}H^*\omega \, dt.$$

Cartan's magic formula $\mathcal{L}_{\partial_t} = d\iota_{\partial_t} + \iota_{\partial_t}d$, applied to $H^*\omega$ on $M \times I$, gives (after integrating and using Fundamental Theorem of Calculus on the $\mathcal{L}_{\partial_t}$ side)

$$dh\omega + hd\omega = i_1^*H^*\omega - i_0^*H^*\omega = (H \circ i_1)^*\omega - (H \circ i_0)^*\omega = G^*\omega - F^*\omega,$$

where in the last step we used $H \circ i_1 = G$ and $H \circ i_0 = F$.

On cohomology classes, $[\omega]$ being a class means $d\omega = 0$, so $hd\omega = 0$, and the chain homotopy identity reduces to $G^*\omega - F^*\omega = dh\omega$. Passing to cohomology, $dh\omega$ is exact, so $[G^*\omega - F^*\omega] = 0$ in $H^*(M)$, i.e. $G^*[\omega] = F^*[\omega]$.

The key conceptual point: the chain homotopy $h$ is the algebraic shadow of the geometric homotopy $H$. The identity $dh + hd = G^* - F^*$ encodes the fact that "two homotopic maps differ by a boundary on cohomology," and the right side becoming zero on closed forms (modulo exacts) is the precise mechanism by which homotopic maps are forced to induce equal cohomology maps.

This is the same construction as in the Poincaré lemma — there, the homotopy was from the identity to a constant map, the constant pullback was zero (on positive-degree forms), and the identity reduced to $\omega = d(h\omega)$ for closed $\omega$. Here, neither endpoint pullback is zero, but their *difference* is the boundary $dh\omega$.

---

# What Makes This Hard

The conceptual obstacle is believing the result at all: it says that cohomology — defined from rigid smooth-structure data — depends only on the much-floppier homotopy type, indifferent to the actual geometry of the homotopy. In the proof, the non-obvious step is **recognizing that the chain homotopy operator's existence is the precise algebraic mechanism that makes homotopy invariance work**. People often try to prove homotopy invariance by direct computation (showing $F^*\omega - G^*\omega$ is exact for each closed $\omega$ separately) — this is essentially trying to find $h\omega$ ad hoc for each $\omega$, when the elegant route is to define $h$ once and let the identity $dh + hd = G^* - F^*$ handle every closed form simultaneously. The common error is to overlook the contribution of the $\iota_{\partial_t}$ term and try to do everything with just $H^*$ and integrals.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Construct a chain homotopy operator $h : \Omega^k(N) \to \Omega^{k-1}(M)$ from the smooth homotopy $H$. Verify the chain homotopy identity $dh + hd = G^* - F^*$. Conclude that on closed forms, $G^* - F^*$ is exact, hence vanishes in cohomology.

**Subgoal decomposition:**

1. **Define the homotopy operator.** Given $H : M \times I \to N$ with $H_0 = F$, $H_1 = G$, define $h\omega = \int_0^1 i_t^*\iota_{\partial_t}H^*\omega \, dt$ for $\omega \in \Omega^k(N)$, where $i_t : M \to M \times I$, $i_t(x) = (x, t)$ and $\partial_t$ is the canonical vector field on $M \times I$.
   - *Hint:* This is the integral of a form-valued function of $t$, well-defined because the integrand is a smooth section of $\Lambda^{k-1}T^*M$.
   - *Why needed:* It is the candidate chain homotopy operator.

2. **Use Cartan's magic formula and Fundamental Theorem of Calculus.** Compute, for $\omega \in \Omega^k(N)$,
   $$\int_0^1 \mathcal{L}_{\partial_t}(H^*\omega) \, dt = i_1^*H^*\omega - i_0^*H^*\omega = G^*\omega - F^*\omega,$$
   using Fundamental Theorem of Calculus on the $t$-derivative and $H \circ i_t = H_t$.
   - *Hint:* $\mathcal{L}_{\partial_t}$ is the $t$-derivative along $\partial_t$; integrating gives the endpoint difference.
   - *Why needed:* This is the algebraic identity that turns the homotopy into a chain map relation.

3. **Apply Cartan's magic formula.** $\mathcal{L}_{\partial_t} = d\iota_{\partial_t} + \iota_{\partial_t}d$. Apply this to $H^*\omega$:
   $$\mathcal{L}_{\partial_t}H^*\omega = d\iota_{\partial_t}H^*\omega + \iota_{\partial_t}H^*d\omega,$$
   using pullback-commutes-with-$d$.
   - *Hint:* Cartan's magic formula is [[Thm - Cartan's Magic Formula]] from `Differential Geometry VIII`.
   - *Why needed:* It splits the $\mathcal{L}_{\partial_t}$ term into two pieces — the first becomes $dh\omega$ after integrating, the second becomes $hd\omega$.

4. **Combine the steps and conclude.** Integrating gives $dh\omega + hd\omega = G^*\omega - F^*\omega$ at the form level. For closed $\omega$, $hd\omega = 0$, so $G^*\omega - F^*\omega = dh\omega$ is exact, hence $[G^*\omega] = [F^*\omega]$ in $H^*(M)$.
   - *Hint:* "Exact = boundary in the de Rham complex = trivial in cohomology."
   - *Why needed:* This is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence of a homotopy operator for the inclusions $i_0, i_1$
> **Statement:** For any smooth manifold $M$, there exists a homotopy operator $h : \Omega^k(M \times I) \to \Omega^{k-1}(M)$ between the pullback maps $i_0^*, i_1^* : \Omega^*(M \times I) \to \Omega^*(M)$, satisfying $dh + hd = i_1^* - i_0^*$.
>
> **Hint:** Define $h\omega = \int_0^1 i_t^*\iota_{\partial_t}\omega \, dt$ where $i_t : M \to M \times I$ is $i_t(x) = (x, t)$.
>
> **Why needed:** This is the "universal" homotopy operator — the homotopy invariance for general $(F, G)$ follows by pulling back along $H : M \times I \to N$.
>
> > [!note]- Full proof
> > For $\omega \in \Omega^k(M \times I)$, define $h\omega = \int_0^1 i_t^*\iota_{\partial_t}\omega \, dt$. The integrand is a smooth $(k-1)$-form on $M$ depending smoothly on $t$, so the integral is a smooth $(k-1)$-form on $M$.
> >
> > Differentiation under the integral and Cartan's magic formula give
> > $$d h\omega = \int_0^1 d(i_t^*\iota_{\partial_t}\omega)\,dt = \int_0^1 i_t^* d\iota_{\partial_t}\omega \,dt,$$
> > using $i_t^* \circ d = d \circ i_t^*$.
> >
> > Also $h d\omega = \int_0^1 i_t^*\iota_{\partial_t} d\omega \, dt$.
> >
> > Adding and applying Cartan's magic formula $d\iota_{\partial_t} + \iota_{\partial_t} d = \mathcal{L}_{\partial_t}$:
> > $$dh\omega + hd\omega = \int_0^1 i_t^*\mathcal{L}_{\partial_t}\omega \, dt = \int_0^1 \frac{d}{dt}(i_t^*\omega) \, dt = i_1^*\omega - i_0^*\omega,$$
> > by Fundamental Theorem of Calculus and the identity $i_t^*\mathcal{L}_{\partial_t} = \frac{d}{dt} i_t^*$ (which follows from the definition of Lie derivative — see Lee Proposition 12.36).

> [!note]- Lemma 2: Composing with a homotopy gives a chain homotopy for $(F, G)$
> **Statement:** Let $H : M \times I \to N$ be a smooth homotopy from $F$ to $G$, and let $h_0 : \Omega^k(M \times I) \to \Omega^{k-1}(M)$ be the universal homotopy operator from Lemma 1. Then $h := h_0 \circ H^* : \Omega^k(N) \to \Omega^{k-1}(M)$ satisfies $dh + hd = G^* - F^*$.
>
> **Hint:** Use Lemma 1 with $\omega$ replaced by $H^*\omega$, and note $i_t \circ H = H_t$, so $H_t^* = (H \circ i_t)^* = i_t^*H^*$.
>
> **Why needed:** This is the chain homotopy operator we want, built by transporting the universal one along $H^*$.
>
> > [!note]- Full proof
> > For $\omega \in \Omega^k(N)$, $H^*\omega \in \Omega^k(M \times I)$. Apply Lemma 1:
> > $$dh_0(H^*\omega) + h_0 d(H^*\omega) = i_1^*H^*\omega - i_0^*H^*\omega.$$
> > Since pullback commutes with $d$, $d(H^*\omega) = H^*d\omega$, so the left side is $dh_0H^*\omega + h_0 H^* d\omega = dh\omega + h(d\omega)$. Since $H \circ i_1 = G$ and $H \circ i_0 = F$, the right side is $G^*\omega - F^*\omega$. So $dh + hd = G^* - F^*$.

> [!note]- Lemma 3: The chain homotopy identity implies cohomology equality
> **Statement:** Let $f, g : C^* \to D^*$ be cochain maps between cochain complexes, and suppose $h : C^k \to D^{k-1}$ satisfies $dh + hd = g - f$. Then on cohomology, $f_* = g_* : H^*(C) \to H^*(D)$.
>
> **Hint:** Apply $f - g = -(dh + hd)$ to a closed cochain $c$ and observe $hd c = 0$.
>
> **Why needed:** This is the algebraic mechanism by which chain homotopies become cohomology equalities — a purely formal step in homological algebra.
>
> > [!note]- Full proof
> > Let $c \in C^k$ be closed, $dc = 0$. Then $(g - f)(c) = (dh + hd)(c) = dh(c) + hd(c) = dh(c) + 0 = dh(c)$, which is exact. So $[g(c)] - [f(c)] = [dh(c)] = 0$ in $H^k(D)$, i.e. $f_*[c] = g_*[c]$. Since this holds for every closed $c$, $f_* = g_*$ on $H^*(C)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F, G : M \to N$ be smooth maps and $H : M \times I \to N$ a smooth homotopy with $H_0 = F$, $H_1 = G$. We show $F^* = G^*$ on $H^*_{dR}$.
>
> **Step 1 — Universal homotopy operator.** Define $h_0 : \Omega^k(M \times I) \to \Omega^{k-1}(M)$ by
> $$h_0\eta = \int_0^1 i_t^*\iota_{\partial_t}\eta \, dt.$$
> By Lemma 1, $d h_0\eta + h_0 d\eta = i_1^*\eta - i_0^*\eta$ for every $\eta \in \Omega^k(M \times I)$.
>
> **Step 2 — Transport via $H^*$.** Define $h := h_0 \circ H^* : \Omega^k(N) \to \Omega^{k-1}(M)$. By Lemma 2, $dh + hd = G^* - F^*$ at the form level.
>
> **Step 3 — Pass to cohomology.** For a closed form $\omega \in \Omega^k(N)$ ($d\omega = 0$): $hd\omega = 0$, so $G^*\omega - F^*\omega = dh\omega$, which is exact. Hence $[G^*\omega] = [F^*\omega]$ in $H^k_{dR}(M)$, i.e. $G^*[\omega] = F^*[\omega]$. Since $\omega$ was an arbitrary closed form, $G^* = F^*$ on $H^k_{dR}$. $\blacksquare$
>
> **Corollary (homotopy equivalent manifolds have isomorphic cohomology).** If $F : M \to N$ and $G : N \to M$ satisfy $G \circ F \simeq \mathrm{id}_M$ and $F \circ G \simeq \mathrm{id}_N$, then by Step 3 applied twice, $F^* \circ G^* = (G \circ F)^* = \mathrm{id}_{H^*(M)}$ and $G^* \circ F^* = (F \circ G)^* = \mathrm{id}_{H^*(N)}$. So $F^*$ and $G^*$ are inverse isomorphisms.

---

# Cross-Field Exercise Suggestions

**Cohomology via deformation retract.** Many cohomology computations reduce to homotopy invariance via *deformation retracts*. The standard examples: $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$ via radial projection; the Möbius strip $\simeq S^1$ via core circle inclusion; a tubular neighborhood of any submanifold $N \subseteq M$ is homotopy equivalent to $N$. Each of these reduces a hard computation to one about a simpler space.

**Mayer–Vietoris on contractible covers.** When a manifold has a cover by contractible open sets, the cohomology of each piece is trivial (Poincaré lemma + homotopy invariance), and all cohomological information is contained in the gluing data of the cover. This is the strategy used to compute $H^*(S^n)$, $H^*(T^n)$, and via spectral sequences $H^*(\mathbb{CP}^n)$, $H^*(\mathrm{Gr})$, etc.

**Topological invariance.** The Whitney approximation theorem says every continuous map between smooth manifolds is homotopic to a smooth one. Combining with homotopy invariance, *homeomorphic smooth manifolds have isomorphic de Rham cohomology*. This is striking because the de Rham construction uses derivatives — yet the answer is independent of the smooth structure.

**Fiber bundles and the Leray–Hirsch theorem.** For a fiber bundle $E \to B$ with fiber $F$, the cohomology of $E$ is determined (under suitable hypotheses) by that of $B$ and $F$ via the Leray–Hirsch theorem. The proof uses homotopy invariance to identify local trivializations $\pi^{-1}(U_\alpha) \simeq U_\alpha \times F$ with their cohomology in product form $H^*(U_\alpha) \otimes H^*(F)$.

---

# Bridges

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]]** — the homotopy invariance theorem with the second map taken constant. The Poincaré lemma is the special case "homotopy from identity to constant"; the constant pullback annihilates positive-degree forms, and the identity $\omega = d(h\omega) + h(d\omega)$ reduces to $\omega = d(h\omega)$ for closed $\omega$. The same homotopy operator construction works for both.

- **Smooth homotopy and the Whitney approximation theorem** — the link between continuous and smooth maps. Whitney says every continuous map is smoothly homotopic to a smooth one, so the *smooth* homotopy classes agree with the *continuous* homotopy classes on smooth manifolds. This lets homotopy invariance of de Rham cohomology be upgraded to *topological* invariance.

- **Singular cohomology of homotopy equivalent spaces** — by the [[Thm - The de Rham Theorem (Statement)|de Rham theorem]], $H^*_{dR}(M) \cong H^*_{\mathrm{sing}}(M; \mathbb{R})$. The homotopy invariance of singular cohomology is a standard fact of algebraic topology; the present theorem is the smooth-manifold version, equivalent to the singular version via the de Rham isomorphism. The two are different *proofs* of the same fact, each using its own complex's geometry.

- **The fundamental group and $H^1$** — for a connected $M$, there is an injective linear map $H^1_{dR}(M) \to \mathrm{Hom}(\pi_1(M, q), \mathbb{R})$ sending $[\omega]$ to $[\gamma] \mapsto \int_\gamma \omega$. By homotopy invariance the right side depends only on the homotopy class of $\gamma$. The map is an isomorphism when $\pi_1$ is abelian (which it is after passing to $\pi_1/[\pi_1, \pi_1] = H_1(M; \mathbb{Z})$ — see Lee Theorem 17.17 for the precise statement).

- **Chain homotopy in homological algebra** — the proof technique here (constructing $h$ with $dh + hd = g - f$) is the general algebraic notion of a *chain homotopy* in any chain complex. Two chain maps are chain homotopic iff they induce equal maps on cohomology. The de Rham case is one instance of this general algebraic phenomenon; the same machinery powers homotopy invariance in singular cohomology, group cohomology, Lie algebra cohomology, and sheaf cohomology.

---

# Unlocked by This

> [!tip] **Cohomology of $S^n$ via Mayer–Vietoris** *(from this same topic)*
> Homotopy invariance applied to the open hemisphere cover of $S^n$: each hemisphere is contractible (homotopy equivalent to a point), so $H^*$ of each is trivial in positive degrees, and the intersection — a thickened equator — is homotopy equivalent to $S^{n-1}$. Iterating Mayer–Vietoris from $n = 1$ upward computes $H^*(S^n) = \mathbb{R}$ in degrees $0$ and $n$, zero elsewhere.

> [!tip] **Topological invariance of de Rham cohomology** *(from this same topic)*
> Homeomorphic smooth manifolds have isomorphic de Rham cohomology, despite the construction using smooth structure. This forces all of de Rham theory to be a topological invariant, paving the way for the [[Thm - The de Rham Theorem (Statement)|de Rham theorem]] identifying it with singular cohomology.

> [!tip] **Homotopy groups and stable cohomology** *(from Algebraic Topology)*
> Cohomology being a homotopy invariant motivates the study of the **homotopy category** — spaces modulo homotopy equivalence, smooth maps modulo smooth homotopy. The objects of this category are no longer manifolds in the strict sense but homotopy types, and every cohomology theory factors through it. The **stable homotopy category** then takes a further step into stable phenomena.

> [!tip] **Eilenberg–Steenrod axioms** *(from Algebraic Topology)*
> A **cohomology theory** is, by definition, a contravariant functor on topological spaces satisfying homotopy invariance, excision, dimension, and Mayer–Vietoris (or long exact sequence of pairs). De Rham cohomology satisfies all these axioms (on the category of smooth manifolds), making it a cohomology theory in the Eilenberg–Steenrod sense, and the uniqueness theorem (cohomology theories agreeing on a point agree everywhere on CW complexes) is what underlies the [[Thm - The de Rham Theorem (Statement)|de Rham theorem]].
