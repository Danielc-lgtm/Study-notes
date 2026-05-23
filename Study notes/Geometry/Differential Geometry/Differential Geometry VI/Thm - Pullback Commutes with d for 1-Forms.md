---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Pullback of a Covector Field"
  - "Def - The Differential of a Function as a 1-Form"
  - "Def - Covector Field and Differential 1-Form"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, pullback, naturality]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds, $g \in C^\infty(N)$, and $F^*g = g \circ F \in C^\infty(M)$ is the pullback of $g$. The differential $d$ takes 0-forms (functions) to 1-forms ([[Def - The Differential of a Function as a 1-Form]]). The pullback of 1-forms is $F^* : \Omega^1(N) \to \Omega^1(M)$ ([[Def - Pullback of a Covector Field]]).

---

# Statement

> **Theorem (Naturality of $d$ on functions).** Let $F : M \to N$ be a smooth map between smooth manifolds, and let $g \in C^\infty(N)$. Then
> $$F^*(dg) = d(F^*g) = d(g \circ F)$$
> as 1-forms on $M$.
>
> **Corollary.** Pullback commutes with the differential operator on functions in either order: pulling back the differential of $g$ is the same as taking the differential of the pulled-back function.

This is the degree-$0$ case of the more general statement that pullback commutes with the exterior derivative on all $k$-forms — see [[Thm - Pullback Commutes with d for Forms on Manifolds]] for the higher-degree generalization.

---

# Motivation

This theorem is the **structural keystone** of the differential-forms theory. It says that the differential operator $d$ is **natural** with respect to smooth maps: it does not depend on the coordinate system, the choice of trivialization, or the source manifold — it commutes with every pullback.

Why is this the keystone? Because it is what makes the de Rham complex a *functor* on the category of smooth manifolds. The diagram

$$\begin{array}{ccc}
C^\infty(N) & \xrightarrow{d_N} & \Omega^1(N) \\
\downarrow F^* & & \downarrow F^* \\
C^\infty(M) & \xrightarrow{d_M} & \Omega^1(M)
\end{array}$$

commutes by this theorem — pulling back functions via $F^*$ on the left, then differentiating on the bottom, gives the same result as differentiating on the top, then pulling back the 1-form on the right. This naturality, extended to higher $k$, makes the de Rham complex a chain complex of contravariant functors, and de Rham cohomology a contravariant functor from smooth manifolds to graded vector spaces. The de Rham theorem then identifies $H^k_{dR}$ with the topological singular cohomology — a topological invariant.

So this theorem, modest-looking, is what builds the bridge from differential geometry to algebraic topology. Without it, the differential operator would be a chart-dependent computation; with it, $d$ is a natural transformation, and the whole machinery of de Rham cohomology becomes available.

A second reason the theorem matters is **computational**: it tells you that to compute $F^*(dg)$, you can just compute the differential of $g \circ F$ in any chart on $M$ — a one-line computation — rather than computing $dg$ on $N$ first and then pulling it back via the more involved formula. This shortcut is the practical content of naturality.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a smooth map $F : M \to N$ and a smooth function $g \in C^\infty(N)$". This data is extremely common.

The most common source is **computing pullbacks of differentials in coordinates**. Given a coordinate chart on $N$ with coordinates $y^j$ and a function $g(y^1, \dots, y^n)$, $dg = (\partial g/\partial y^j) dy^j$. Pulling back: $F^*(dg) = (\partial g/\partial y^j)(F(x)) \cdot F^*(dy^j) = (\partial g/\partial y^j)(F(x)) \cdot d(y^j \circ F) = (\partial g/\partial y^j)(F(x)) \cdot dF^j$. The theorem gives this the alternative form $d(g \circ F) = (\partial (g \circ F)/\partial x^i) dx^i$, which via the chain rule equals the first expression. Reconciling these two computations is exactly the theorem.

A second source is **verifying invariance properties**. The theorem ensures that constructions defined via the differential operator transform correctly under pullback: closed forms ($dg = $ something fixed) pull back to closed forms, exact forms pull back to exact forms, and the cohomology classes are well-defined on the pulled-back space. Whenever an "invariant" claim about forms needs verification, this theorem is the engine.

A third source is **the chain rule on manifolds**. Pulling back the differential of $g$ via $F$ amounts to differentiating the composition $g \circ F$, which is the manifold-native form of the chain rule. The theorem is, in a sense, the chain rule for 1-forms.

A fourth source is **the gauge-theoretic transformation of differentials**. In gauge theory, a "gauge transformation" $F : M \to G$ acts on associated bundles by composing with $F$. The differential of a section under gauge transformation involves $F^*(d\sigma)$ kinds of expressions, and the theorem ensures these compute the gauge-transformed differentials correctly.

**Targets (Output Amplification)**

The conclusion $F^*(dg) = d(F^*g)$ is the naturality of $d$ on functions. Combined with one further fact, it produces structural consequences.

The first combination is **theorem plus the higher-degree generalization gives full naturality of $d$**. For $k$-forms $\omega \in \Omega^k(N)$, $F^*(d\omega) = d(F^*\omega)$ in $\Omega^{k+1}(M)$. This higher-degree version is proved by induction on $k$, using the degree-$0$ theorem as the base case together with the multiplicative structure (the Leibniz rule for $d$ and the multiplicativity of $F^*$ with $\wedge$). The full naturality makes the de Rham complex a chain complex.

A second combination is **theorem plus closedness gives "pullback of closed is closed"**. If $d\omega = 0$ on $N$, then $d(F^*\omega) = F^*(d\omega) = F^*(0) = 0$ on $M$. So pullback preserves closedness, and consequently descends to a map on de Rham cohomology.

A third combination is **theorem plus exactness gives "pullback of exact is exact"**. If $\omega = dg$ on $N$, then $F^*\omega = F^*(dg) = d(F^*g)$ on $M$ — exact, with potential function $F^*g = g \circ F$. So pullback preserves exactness, and the resulting cohomology map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ is well-defined.

A fourth combination is **theorem plus the de Rham theorem makes the pullback a topological functor**. $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ exists by the previous combination; the de Rham theorem identifies these with singular cohomology, and on that side the pullback is the usual topological pullback. So the differential-geometric and topological pullbacks agree, making de Rham theory a functorial bridge.

---

# Why Is It True

The intuition is direct: **both sides are 1-forms on $M$ that, when paired with any tangent vector $v$ at $p$, give the directional derivative of $g \circ F$ at $p$ in the direction $v$**. The two routes — pulling back the differential vs differentiating the pullback — both compute the same thing because both encode "how does $g$ change along the curve $F \circ \gamma$ where $\gamma$ tangent vector is $v$".

**The one-line mechanism summary: pairing both sides with a tangent vector $v$ at $p$, $F^*(dg)_p(v) = dg_{F(p)}(dF_p(v)) = (dF_p(v))(g) = v(g \circ F) = d(g \circ F)_p(v)$, where the third equality uses the chain rule for derivations.**

The proof is essentially this one line. Pair both 1-forms with an arbitrary tangent vector $v \in T_pM$:

$F^*(dg)_p(v)$ by the pullback definition is $dg_{F(p)}(dF_p(v))$. By the differential-as-functional definition, $dg_{F(p)}(dF_p(v)) = dF_p(v)(g)$ — the directional derivative of $g$ along the vector $dF_p(v) \in T_{F(p)}N$.

$d(g \circ F)_p(v) = v(g \circ F)$ by the same differential-as-functional definition, applied to the composed function $g \circ F$ on $M$.

The two are equal by the chain rule for derivations: $v(g \circ F) = dF_p(v)(g)$. This is the standard "chain rule for tangent vectors" — pushing forward $v$ to $T_{F(p)}N$ and then acting on $g$ is the same as having $v$ act directly on the composite $g \circ F$.

Since the two 1-forms agree pointwise on every tangent vector, they are equal as 1-forms.

So the theorem is a one-line application of the chain rule for derivations, dressed in covector-field clothing.

---

# What Makes This Hard

The substantive step is recognizing that the **chain rule for tangent vectors** $v(g \circ F) = dF_p(v)(g)$ is exactly what the theorem expresses at the level of 1-forms. Beginners sometimes prove the theorem coordinate-wise (writing $dg = (\partial g/\partial y^j) dy^j$ and pulling back), which works but obscures the structural content. The chain-rule-for-derivations argument is the cleanest proof and reveals why the theorem is true at the level of definitions.

A common error is to **confuse the directions of $F^*$**: pullback goes from $N$ to $M$, while $F$ goes from $M$ to $N$. Getting the directions right in the chain $dg$ (on $N$) $\to F^*(dg)$ (on $M$) requires care, particularly when stating the theorem in coordinates.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show the two 1-forms agree pointwise on every tangent vector. The pointwise pairing on either side, when unpacked using the definitions of pullback, differential, and tangent vectors, reduces to the chain rule for derivations: $v(g \circ F) = (dF_p(v))(g)$.

**Subgoal decomposition:**

1. **Identify both sides as 1-forms on $M$.** $F^*(dg) \in \Omega^1(M)$ by [[Def - Pullback of a Covector Field]]. $d(F^*g) = d(g \circ F) \in \Omega^1(M)$ by [[Def - The Differential of a Function as a 1-Form]] applied to the smooth function $g \circ F$ on $M$.
   - *Hint:* Both are in $\Omega^1(M)$.
   - *Why needed:* The comparison happens in $\Omega^1(M)$.

2. **Pair $F^*(dg)$ with a tangent vector $v$ at $p$.** Unpack the pullback definition: $F^*(dg)_p(v) = dg_{F(p)}(dF_p(v))$.
   - *Hint:* Pullback definition.
   - *Why needed:* Reduces to a computation involving $dg$ and $dF_p$.

3. **Unpack $dg_{F(p)}(dF_p(v))$.** Use the differential-as-functional definition: $dg_q(w) = w(g)$ for $w \in T_qN$, applied with $q = F(p)$ and $w = dF_p(v)$. Result: $dF_p(v)(g)$.
   - *Hint:* Definition of $dg$.
   - *Why needed:* Recasts the right-hand side as a derivation acting on $g$.

4. **Pair $d(g \circ F)$ with $v$.** Use the differential-as-functional definition: $d(g \circ F)_p(v) = v(g \circ F)$.
   - *Hint:* Definition of $d$ applied to the composite function.
   - *Why needed:* Direct value of the left-hand side.

5. **Apply the chain rule for derivations.** $v(g \circ F) = dF_p(v)(g)$ — the chain rule for tangent vectors states that the directional derivative of $g \circ F$ along $v$ equals the directional derivative of $g$ along the pushforward $dF_p(v)$.
   - *Hint:* Definition of $dF_p$ as the linear map satisfying this property.
   - *Why needed:* Equates the two pairings.

6. **Conclude.** The two 1-forms agree on every tangent vector at every point, hence are equal as 1-forms.

---

# Lemma Decomposition

> [!note]- Lemma 1: $F^*(dg)_p(v) = dF_p(v)(g)$
> **Statement:** For $F : M \to N$ smooth, $g \in C^\infty(N)$, $p \in M$, $v \in T_pM$:
> $$F^*(dg)_p(v) = dF_p(v)(g).$$
>
> **Hint:** Apply the pullback definition followed by the differential-as-functional definition.
>
> **Why needed:** Recasts the pullback of the differential as a derivation acting on $g$.
>
> > [!note]- Full proof
> > By [[Def - Pullback of a Covector Field]], $F^*(dg)_p(v) = dg_{F(p)}(dF_p(v))$. By [[Def - The Differential of a Function as a 1-Form]], $dg_q(w) = w(g)$ for any $q \in N$ and $w \in T_qN$. Applying with $q = F(p)$ and $w = dF_p(v) \in T_{F(p)}N$, we get $dg_{F(p)}(dF_p(v)) = dF_p(v)(g)$.

> [!note]- Lemma 2: $d(g \circ F)_p(v) = v(g \circ F)$
> **Statement:** For $g \circ F \in C^\infty(M)$ and $v \in T_pM$:
> $$d(g \circ F)_p(v) = v(g \circ F).$$
>
> **Hint:** Differential-as-functional definition.
>
> **Why needed:** Direct value of the differential of the pullback function.
>
> > [!note]- Full proof
> > By [[Def - The Differential of a Function as a 1-Form]] applied to the smooth function $g \circ F$ on $M$: $d(g \circ F)_p(v) = v(g \circ F)$, the directional derivative of the composite function in direction $v$.

> [!note]- Lemma 3: Chain rule for derivations
> **Statement:** For $F : M \to N$ smooth, $g \in C^\infty(N)$, $p \in M$, $v \in T_pM$:
> $$v(g \circ F) = dF_p(v)(g).$$
>
> **Hint:** This is the defining property of $dF_p$ — the linear map $T_pM \to T_{F(p)}N$ such that $dF_p(v)(g) = v(g \circ F)$ for all $g \in C^\infty(N)$.
>
> **Why needed:** Equates the two pairings (Lemmas 1 and 2).
>
> > [!note]- Full proof
> > The differential $dF_p$ is defined precisely by this property — see [[Def - The Differential of a Smooth Map]]. The defining equation is $dF_p(v)(g) = v(g \circ F)$, valid for every $v \in T_pM$ and every $g \in C^\infty(N)$. So the lemma is a restatement of this definition.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Identify the comparison space.** $F^*(dg)$ and $d(F^*g) = d(g \circ F)$ are both elements of $\Omega^1(M)$; the comparison happens in this space.
>
> **Step 1 — Pair LHS with a tangent vector.** For $p \in M$ and $v \in T_pM$, by Lemma 1, $F^*(dg)_p(v) = dF_p(v)(g)$.
>
> **Step 2 — Pair RHS with the same tangent vector.** By Lemma 2, $d(g \circ F)_p(v) = v(g \circ F)$.
>
> **Step 3 — Apply the chain rule.** By Lemma 3, $v(g \circ F) = dF_p(v)(g)$.
>
> **Step 4 — Conclude.** The right-hand side of Step 1 equals the right-hand side of Step 3 (both are $dF_p(v)(g)$), so the LHS and RHS of the theorem agree pointwise on every tangent vector $v$ at every point $p$. Two 1-forms agreeing on every tangent vector at every point are equal as elements of $\Omega^1(M)$. So $F^*(dg) = d(F^*g)$ in $\Omega^1(M)$.
> $\qquad\blacksquare$

**Alternative coordinate proof.** In a chart $(U, x^i)$ on $M$ and $(V, y^j)$ on $N$ with $F(U) \subseteq V$ and $F^j = y^j \circ F$, we have $dg = (\partial g/\partial y^j) dy^j$ on $V$. Pulling back: $F^*(dg) = (\partial g/\partial y^j \circ F) F^*(dy^j) = (\partial g/\partial y^j \circ F) dF^j = (\partial g/\partial y^j)(F(x)) (\partial F^j/\partial x^i) dx^i$. On the other hand, $d(g \circ F) = (\partial(g \circ F)/\partial x^i) dx^i$, and by the chain rule $\partial(g \circ F)/\partial x^i = (\partial g/\partial y^j)(F(x)) (\partial F^j/\partial x^i)$. So both sides agree in coordinates, confirming the equation.

---

# Cross-Field Exercise Suggestions

**Algebraic topology: functoriality of de Rham cohomology.** The theorem (extended to higher degrees) makes $F^*$ commute with $d$, so $F^*$ descends to maps $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ on cohomology. Use this to compute the induced map on cohomology by smooth maps between specific manifolds (e.g., the squaring map $S^1 \to S^1$ acts on $H^1_{dR}(S^1) = \mathbb{R}$ by multiplication by $2$).

**Complex analysis: pullback of holomorphic 1-forms.** For a holomorphic function $g : V \subseteq \mathbb{C} \to \mathbb{C}$, the holomorphic 1-form $dg$ pulls back under a holomorphic map $F : U \to V$ to $F^*(dg) = d(g \circ F)$. This is the chain rule for holomorphic 1-forms, and it underlies the contour-integration calculus of Cauchy's integral formula and the residue theorem.

**General relativity: covariant differential of fields.** In GR, smooth maps include the embedding of slices into spacetime and the coordinate transformations relating different reference frames. The theorem says that the differentials of physical quantities (energy, momentum, etc.) transform correctly under all such smooth maps — a consequence of $d$ being natural.

**Gauge theory: covariant derivatives and gauge transformations.** Gauge transformations $g : M \to G$ act on sections by composition; the theorem says that the differentials commute with these transformations in the appropriate sense. The "covariant derivative" $\nabla = d + A$ on a vector bundle generalizes the differential, and the theorem extends to give the naturality of $\nabla$ under bundle morphisms preserving connections.

---

# Bridges

- **[[Def - The Differential of a Smooth Map]]** — The theorem is essentially a restatement of the chain rule for the differential. The differential $dF_p : T_pM \to T_{F(p)}N$ is defined by $dF_p(v)(g) = v(g \circ F)$, and this defining identity is what makes the theorem true.

- **The de Rham complex and cohomology** *(from Differential Geometry X)* — The theorem (extended to all degrees) is what makes the de Rham complex a chain complex of contravariant functors. Without it, $d$ would not commute with pullback, and the cohomology would not be functorial. The de Rham theorem then identifies $H^k_{dR}$ with singular cohomology, giving the topological content.

- **[[Thm - Pullback Commutes with d for Forms on Manifolds]]** *(from Differential Geometry VIII)* — The full version: $F^*(d\omega) = d(F^*\omega)$ for $\omega \in \Omega^k(N)$. The degree-$0$ case proved here is the base of the inductive argument; the higher degrees follow from this case plus the Leibniz rule for $d$ and the multiplicativity of $F^*$ with $\wedge$.

- **Chain rule for derivations** — The theorem's proof reduces to the chain rule $v(g \circ F) = dF_p(v)(g)$, which is itself the chain rule for tangent vectors as derivations. The bridge to ordinary multivariable calculus is via the coordinate version of the chain rule.

---

# Unlocked by This

> [!tip] Pullback Commutes with $d$ for All Forms *(from Differential Geometry VIII)*
> The theorem extends to all $k$-forms: $F^*(d\omega) = d(F^*\omega)$ for $\omega \in \Omega^k(N)$. The full version, [[Thm - Pullback Commutes with d for Forms on Manifolds]], is the structural keystone of differential-forms theory. Combined with multiplicativity of $F^*$ with the wedge product and the Leibniz rule for $d$, the full version makes $F^*$ a chain map of de Rham complexes.

> [!tip] Functoriality of de Rham Cohomology *(from Algebraic Topology / Differential Geometry X)*
> The pullback $F^*$ descends to maps on de Rham cohomology $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ because it commutes with $d$ (so it sends cycles to cycles and boundaries to boundaries). This makes $H^k_{dR}(-)$ a contravariant functor from smooth manifolds to graded vector spaces. The de Rham theorem then matches this functor with the singular cohomology functor, completing the bridge between differential geometry and topology.

> [!tip] Homotopy Invariance *(from Algebraic Topology)*
> A consequence of naturality of $d$ is the **homotopy invariance** of de Rham cohomology: smoothly homotopic maps $F_0, F_1 : M \to N$ induce equal maps $F_0^* = F_1^* : H^k_{dR}(N) \to H^k_{dR}(M)$. The proof uses a smooth homotopy $H : M \times [0, 1] \to N$ and the Poincaré chain homotopy. The result is that de Rham cohomology depends only on the homotopy type of the manifold — a purely topological property.

> [!tip] Connections and Curvature *(from Gauge Theory)*
> The notion of "natural with respect to bundle morphisms" generalizes to connections: a connection-preserving bundle homomorphism commutes with covariant derivatives, just as a smooth map commutes with the differential $d$. The curvature 2-form of a connection is the "first obstruction" to naturality, and gauge theory is the study of connections modulo gauge transformations — which is connection-naturality made explicit.
