---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fibre Bundle"
  - "Thm - Regular Value Theorem on Manifolds"
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Embedded Submanifold"
  - "Def - Principal G-Bundle"
  - "Def - Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, all manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$. Lie groups act on principal bundles on the **right**: $R_g(p) = p \cdot g$, and $(p \cdot g)\cdot h = p \cdot (gh)$.

We are given a [[Def - Fibre Bundle|fibre bundle]] $(E, \pi, B)$ with typical fibre $F$: that is, a surjective smooth map $\pi : E \to B$ such that each point of $B$ has an open neighbourhood $U \subseteq B$ over which there is a diffeomorphism $\psi_U : \pi^{-1}(U) \to U \times F$ with $\operatorname{pr}_1 \circ \psi_U = \pi$, where $\operatorname{pr}_1 : U \times F \to U$ is the projection onto the first factor. Such a $\psi_U$ is a **local trivialisation** over $U$. We write $m = \dim B$ and $f = \dim F$, so that $\dim E = m + f$ (the local trivialisation identifies a neighbourhood in $E$ with an open subset of $U \times F$). The **fibre of $E$ over $x \in B$** is $E_x := \pi^{-1}(x)$; every fibre is diffeomorphic to $F$.

We are also given a smooth map $\lambda : B' \to B$, where $B'$ is another manifold. The object we study is the set
$$E' := \{(b', p) \in B' \times E : \lambda(b') = \pi(p)\} \subseteq B' \times E,$$
the **fibre product** of $\lambda$ and $\pi$. We write $\operatorname{pr}_1 : B' \times E \to B'$ and $\operatorname{pr}_2 : B' \times E \to E$ for the two projections of the product, and $\pi' := \operatorname{pr}_1|_{E'} : E' \to B'$. The triple $\lambda^*(E, \pi, B) := (E', \pi', B')$ is the **pull-back of $(E, \pi, B)$ along $\lambda$**, and we write $\lambda^*E := E'$ for its total space. The fibre of the pull-back over $b' \in B'$ is $E'_{b'} := \pi'^{-1}(b')$.

In the principal-bundle part of the statement we write $P$ in place of $E$ and $G$ for the structure group; $\lambda^*P$ carries the right $G$-action $(b', p)\cdot g := (b', p\cdot g)$.

> [!warning] Convention: the direction of $\lambda$
> Bär (Definition 2.1.11 and Remark 2.2.8) prints the pull-back map as "$\lambda : B \to B'$" while simultaneously writing $E' = \{(b', p) : \lambda(b') = \pi(p)\}$ and constructing a bundle over $B'$. These are inconsistent: for $\lambda(b')$ to be a point of $B$ comparable with $\pi(p)$, and for the result to live over $B'$, the map must go $\lambda : B' \to B$. We use the corrected direction $\lambda : B' \to B$ throughout; this is the direction in which the pull-back is contravariant (a map $B' \to B$ produces a bundle over $B'$ from a bundle over $B$), and it is the direction the fibre-product formula forces.

> [!warning] Convention: Haydys' notation
> Haydys (Definition 2.2.17, Remark 2.2.9) writes the same construction for a map $f : N \to M$ and a bundle $P \to M$ as $f^*P = \{(p, n) \in P \times N : f(n) = \pi(p)\}$, ordering the factors as $(p, n)$ rather than $(b', p)$ and using the projection $\varpi(p, n) = n$. This is our $E'$ with the two factors of the product transposed; the transposition $(b', p) \leftrightarrow (p, b')$ is a diffeomorphism $B' \times E \to E \times B'$ carrying one convention to the other, so the two constructions are canonically identified and every statement below holds verbatim under either ordering. Haydys' $G$-equivariant map $\hat f : f^*P \to P$ covering $f$ is our $\operatorname{pr}_2$.

---

# Statement

> **Theorem (the pull-back of a fibre bundle is a fibre bundle).** Let $(E, \pi, B)$ be a fibre bundle with typical fibre $F$, and let $\lambda : B' \to B$ be a smooth map. Set
> $$E' = \{(b', p) \in B' \times E : \lambda(b') = \pi(p)\}, \qquad \pi' = \operatorname{pr}_1|_{E'} : E' \to B'.$$
> Then:
> 1. $E'$ is a properly embedded smooth submanifold of $B' \times E$, of dimension $\dim B' + \dim F$.
> 2. $(E', \pi', B')$ is a fibre bundle with typical fibre $F$.
> 3. For each $b' \in B'$, the restriction of $\operatorname{pr}_2$ to the fibre is a diffeomorphism
> $$\operatorname{pr}_2|_{E'_{b'}} : E'_{b'} \xrightarrow{\ \cong\ } E_{\lambda(b')}.$$
> 4. The square
> $$\begin{array}{ccc} \lambda^*E & \xrightarrow{\ \operatorname{pr}_2\ } & E \\ \pi' \big\downarrow & & \big\downarrow \pi \\ B' & \xrightarrow{\ \lambda\ } & B \end{array}$$
> commutes, that is $\pi \circ \operatorname{pr}_2 = \lambda \circ \pi'$.

The construction respects extra fibrewise structure. Two refinements record this.

> **Theorem (principal refinement).** Suppose $E = P$ is a [[Def - Principal G-Bundle|principal G-bundle]] $\pi : P \to B$ with right $G$-action. Equip $\lambda^*P$ with the right $G$-action $(b', p)\cdot g = (b', p\cdot g)$. Then $\lambda^*P$ is a principal $G$-bundle over $B'$, and $\operatorname{pr}_2 : \lambda^*P \to P$ is $G$-equivariant, $\operatorname{pr}_2((b', p)\cdot g) = \operatorname{pr}_2(b', p)\cdot g$.

> **Theorem (vector refinement).** Suppose $E$ is a real or complex [[Def - Vector Bundle|vector bundle]] of rank $n$ over $B$, with $\mathbb K = \mathbb R$ or $\mathbb C$. Then each fibre $E'_{b'}$ carries a unique $\mathbb K$-vector-space structure making $\operatorname{pr}_2|_{E'_{b'}} : E'_{b'} \to E_{\lambda(b')}$ a linear isomorphism, and with these structures $\lambda^*E$ is a $\mathbb K$-vector bundle of rank $n$ over $B'$. This vector bundle coincides with the fibrewise pull-back $(\lambda^*E)_{b'} = E_{\lambda(b')}$ of the operations-on-bundles construction, the identification being exactly $\operatorname{pr}_2$.

The three statements are one construction seen at three levels of structure: the bare fibre-bundle statement builds the total space and its local product structure; the principal and vector refinements observe that the fibrewise identification $\operatorname{pr}_2$ transports whatever structure the fibres of $E$ carry — a free transitive $G$-action, or a vector-space structure — to the fibres of $\lambda^*E$, and that the local trivialisations respect it.

---

# Motivation

The pull-back is the operation that lets a bundle *travel along a map*. A fibre bundle $(E, \pi, B)$ organises a family of copies of $F$, one over each point of $B$. If we are handed a map $\lambda : B' \to B$ — a reparametrisation, an inclusion of a submanifold, a curve, a homotopy, a classifying map — we very often want the corresponding family over $B'$: the copy of $F$ that sits over $b' \in B'$ should be the copy that $E$ already has over the image point $\lambda(b')$. Writing this wish as a formula, the fibre we want over $b'$ is $E_{\lambda(b')}$, and the total space is the disjoint union of these, which is precisely the fibre product $E' = \{(b', p) : \lambda(b') = \pi(p)\}$: the pair $(b', p)$ records "the point $b'$ downstairs and the point $p$ of $E$ living over $\lambda(b')$". The theorem is the assertion that this naive wish is legitimate — that the set-theoretic family really is a smooth fibre bundle, with the same fibre $F$, and that it maps back to $E$ in the only sensible way.

This is not a technical afterthought; it is one of the load-bearing constructions of the whole subject, and the reason is that most of the ways bundles are compared and classified are pull-backs in disguise. The restriction $E|_{B'}$ of a bundle to a submanifold $B' \hookrightarrow B$ is the pull-back along the inclusion. A bundle "along a curve" $\gamma : (-\varepsilon, \varepsilon) \to B$ — the setting for parallel transport and horizontal lifts in the next chapters — is the pull-back $\gamma^*E$, whose sections are exactly the fields along $\gamma$. The statement that homotopic maps pull back isomorphic bundles, which underlies the entire homotopy classification of bundles and the naturality of characteristic classes, is a statement about pull-backs and presupposes that they exist and are bundles. So before any of that machinery can start, one needs the present theorem: that $\lambda^*E$ is a bundle at all.

There are two things that could go wrong, and naming them shows what the theorem must control. First, $E'$ is defined as a subset of the product $B' \times E$ cut out by an equation, $\lambda(b') = \pi(p)$; an equation cutting out a subset of a manifold need not cut out a *submanifold* — the solution set of $xy = 0$ in the plane is not a manifold at the origin. The theorem must show that this particular equation is non-degenerate, and the non-degeneracy comes from a single structural fact about $E$: its projection $\pi$ is a submersion. Second, even granting that $E'$ is a manifold, it must be checked to be *locally a product* $U' \times F$ — otherwise it is a manifold mapping to $B'$ but not a bundle. Both checks are local over $B$, and both are settled by pulling back a local trivialisation of $E$ along $\lambda$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild: any fibre bundle $(E, \pi, B)$ and any smooth $\lambda : B' \to B$. The skill is recognising, in a problem that never says "pull-back", that a pull-back is exactly what is present.

The first disguised source is **a submanifold or a subspace inclusion**. Whenever $B' \subseteq B$ is an embedded submanifold and $\iota : B' \hookrightarrow B$ is the inclusion, the restriction $E|_{B'} := \pi^{-1}(B')$ is the pull-back $\iota^*E$: the fibre product $\{(b', p) : \iota(b') = \pi(p)\}$ is $\{(b', p) : p \in E_{b'}\} \cong \pi^{-1}(B')$. The bridge $B \Rightarrow A$ is "an inclusion is a smooth map", so restriction is a pull-back and inherits the bundle structure for free. *Example problem:* show that the restriction of the tautological line bundle over $\mathbb{CP}^n$ to a linearly embedded $\mathbb{CP}^1$ is the tautological line bundle over $\mathbb{CP}^1$, by identifying the restriction as a pull-back along the inclusion.

The second disguised source is **a curve or a path in the base**. A smooth curve $\gamma : I \to B$ on an interval $I$ is a smooth map, so $\gamma^*E$ is a bundle over $I$, and its sections are the "fields along $\gamma$". The bridge is that a curve is the special case $B' = I$; the payoff is that constructions which are awkward to phrase on $E$ directly — parallel transport, the velocity field, Jacobi fields — become ordinary sections of a bundle over an interval. The non-obvious part is that a one-dimensional base is enough for the theorem to apply, so the entire apparatus of local trivialisations is available along a mere curve. *Example problem:* show that a vector field along a curve $\gamma$ in a Riemannian manifold is a section of $\gamma^*TB$, and that the velocity $\dot\gamma$ is a distinguished such section.

The third disguised source is **a homotopy or a family of maps**. A smooth homotopy $H : B' \times [0,1] \to B$ is a single smooth map on the manifold-with-boundary $B' \times [0,1]$, so $H^*E$ is a bundle over $B' \times [0,1]$. The bridge is "a homotopy is one map with an extra parameter"; the payoff is that comparing $\lambda_0^*E$ and $\lambda_1^*E$ for homotopic $\lambda_0, \lambda_1$ becomes the study of a single bundle over the cylinder, restricted to its two ends. This is the source that makes the homotopy classification of bundles possible. *Example problem:* deduce that a bundle over a contractible base is trivial by pulling back along the homotopy contracting the base to a point.

**Targets (Output Amplification)**

The bare conclusion is that $\lambda^*E$ is a bundle. Combined with other facts it does far more.

Combine the conclusion with **a section or a connection on $E$**. A section $s$ of $E$ pulls back to the section $\lambda^*s := (\mathrm{id}, s\circ\lambda)$ of $\lambda^*E$ (the pair $(b', s(\lambda(b')))$ lies in $E'$ since $\pi(s(\lambda(b'))) = \lambda(b')$), and a connection on $E$ pulls back to a connection on $\lambda^*E$ with $F_{\lambda^*A} = \lambda^*F_A$. The extra ingredient is the structure carried by $E$; the payoff is that differential-geometric data is natural in the base, which is what lets curvature be computed downstairs and pushed along maps. This is the mechanism behind horizontal lifts of curves in chapter V, where $\gamma^*A$ turns a connection into an ordinary linear ODE on $\gamma^*P$.

Combine the conclusion with **homotopy invariance**. Once pull-back is known to be a bundle operation, the theorem that $\lambda_0 \simeq \lambda_1$ implies $\lambda_0^*E \cong \lambda_1^*E$ turns the isomorphism class of $\lambda^*E$ into a homotopy invariant of $\lambda$. The extra ingredient is the sliding lemma over a cylinder; the payoff is the classification of bundles by homotopy classes of maps into a classifying space, and — via Chern–Weil — the statement that characteristic classes are natural, $\lambda^*c(E) = c(\lambda^*E)$. Without the present theorem there is nothing for homotopy invariance to be invariant of.

Combine the conclusion with **the principal and vector refinements** and **transition-function data**. Because $\lambda^*$ preserves the structure group (principal refinement) and pulls back trivialisations, the transition functions of $\lambda^*E$ are $g'_{ij} = g_{ij}\circ\lambda$ where $g_{ij}$ are those of $E$. The extra ingredient is the cocycle description of bundles; the payoff is that every construction phrased through transition functions — associated bundles, reductions of the structure group, characteristic classes computed from a cocycle — is natural under pull-back, computed simply by precomposing the cocycle with $\lambda$.

---

# Why Is It True

Set the whole construction inside one map. Define
$$\Phi : B' \times E \longrightarrow B \times B, \qquad \Phi(b', p) = (\lambda(b'),\ \pi(p)),$$
and let $\Delta_B = \{(x, x) : x \in B\} \subseteq B \times B$ be the diagonal. By definition $E' = \Phi^{-1}(\Delta_B)$: a pair $(b', p)$ lies in $E'$ exactly when its two images $\lambda(b')$ and $\pi(p)$ agree, which is exactly when $\Phi(b', p)$ lands on the diagonal. So $E'$ is the preimage of a submanifold under a smooth map, and the theory of transversality tells us precisely when such a preimage is again a submanifold: when the map is **transverse** to the submanifold, meaning that at every solution point the image of the differential together with the tangent space of the target submanifold spans the whole tangent space of the ambient target.

Why is $\Phi$ transverse to $\Delta_B$? Because $\pi$ is a submersion. At a solution point $(b', p)$ with $\lambda(b') = \pi(p) = x$, we may already reach *every* direction of the second factor $T_xB$ by moving $p$ alone, since $d\pi_p$ is surjective; the diagonal supplies all the "equal-in-both-factors" directions; and between the two we reach all of $T_xB \times T_xB$. The submersivity of the bundle projection is thus the single hypothesis doing all the work, and it is a hypothesis $E$ satisfies automatically, because a fibre bundle looks locally like a product $U \times F$ whose projection to $U$ is a submersion.

**The pull-back is a bundle because the bundle projection $\pi$ is a submersion: this makes the fibre-product equation $\lambda(b') = \pi(p)$ non-degenerate, so its solution set is a manifold, and it makes the fibres of $E$ vary in locally trivial families, so that a local trivialisation of $E$ over $U$ pulls back to one of $\lambda^*E$ over $\lambda^{-1}(U)$.**

Once $E'$ is known to be a manifold, its bundle structure is visible without any further idea. Over a set $U \subseteq B$ where $E$ is a product $U \times F$, the equation $\lambda(b') = \pi(p)$ becomes "the $U$-coordinate of $p$ equals $\lambda(b')$", which pins the $U$-coordinate to a function of $b'$ and leaves the $F$-coordinate entirely free. So over $U' = \lambda^{-1}(U)$ the pull-back is $U' \times F$: a point of it is a point $b' \in U'$ together with a free choice of $F$-coordinate. That is the local product structure, and it is nothing more than the observation that pinning one coordinate to a function of the others does not touch the remaining free coordinate. The fibre over $b'$ is the single copy $\{b'\} \times E_{\lambda(b')}$, and $\operatorname{pr}_2$ carries it isomorphically to $E_{\lambda(b')}$ because forgetting the constant first coordinate is a bijection. The refinements are then automatic: a bijection between fibres transports any structure the fibres carry, and the local products $U' \times F$ inherit the linear or equivariant structure of the local products $U \times F$ they are built from.

---

# What Makes This Hard

The one genuinely non-trivial step is the submanifold claim, and its subtlety is that it does not follow from cutting out $E'$ by an equation alone — a level set is a manifold only when the value is *regular*, and here regularity is exactly the submersivity of $\pi$, which must be located and used. The common error is to assert "$E'$ is a submanifold because it is defined by an equation", which is false in general (the solution set of a degenerate equation can be singular), or to prove only the local product identification and quietly assume it already gives an embedded submanifold of $B' \times E$; the local identification does give the bundle structure, but to speak of $\operatorname{pr}_2$ as a *smooth* map on $E'$ and of $E'$ as a manifold in its own right one must first know $E'$ is a submanifold, which is the regular-value computation. A second, smaller trap is direction: the pull-back is contravariant, a map $B' \to B$ producing a bundle over $B'$, and the fibre-product equation must pair $\lambda$ with $\pi$ in the one order that makes $\lambda(b')$ and $\pi(p)$ comparable — the printed sources get this backwards (see the convention callout).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First record that a fibre bundle projection is a submersion. Use this to run the regular value theorem on the equation $\lambda(b') = \pi(p)$, read in a chart of $B$, and conclude $E'$ is an embedded submanifold. Then pull back a local trivialisation of $E$ over $U$ along $\lambda$ to get a local trivialisation of $E'$ over $\lambda^{-1}(U)$, which gives the fibre-bundle structure and identifies the fibres via $\operatorname{pr}_2$. Finally observe that this fibrewise identification and these local trivialisations transport the principal or vector structure.

**Subgoal decomposition:**

1. **Bundle projections are submersions.** Show $d\pi_p$ is surjective for every $p \in E$.
   - *Hint:* Near $p$, write $\pi = \operatorname{pr}_1 \circ \psi_U$ with $\psi_U$ a diffeomorphism; both factors are submersions.
   - *Why needed:* Submersivity of $\pi$ is the sole regularity hypothesis; without it the fibre-product equation can be degenerate and $E'$ need not be a manifold.

2. **$E'$ is an embedded submanifold.** Show $E' = \{(b', p) : \lambda(b') = \pi(p)\}$ is a properly embedded submanifold of $B' \times E$ of codimension $m = \dim B$.
   - *Hint:* Locally, in a chart $\varphi$ of $B$, $E'$ is the zero set of $g(b', p) = \varphi(\lambda(b')) - \varphi(\pi(p))$; use subgoal 1 to see $0$ is a regular value, then apply the regular value theorem.
   - *Why needed:* It makes $E'$ a manifold, so that "$(E', \pi', B')$ is a bundle" and "$\operatorname{pr}_2$ is smooth on $E'$" are meaningful.

3. **Local trivialisation of the pull-back.** For $U \subseteq B$ trivialising $E$, with $U' = \lambda^{-1}(U)$, produce a diffeomorphism $\Psi : \pi'^{-1}(U') \to U' \times F$ over $U'$.
   - *Hint:* Define $\Psi(b', p) = (b', q(\psi_U(p)))$ with $q : U \times F \to F$ the second projection; its inverse is $(b', y) \mapsto (b', \psi_U^{-1}(\lambda(b'), y))$.
   - *Why needed:* This is the fibre-bundle structure of $\lambda^*E$ and the typical fibre $F$; it also exhibits $\pi'$ as a submersion with the local product form.

4. **Fibrewise identification.** Show $\operatorname{pr}_2$ restricts to a diffeomorphism $E'_{b'} \to E_{\lambda(b')}$ and the square commutes.
   - *Hint:* $E'_{b'} = \{b'\} \times E_{\lambda(b')}$; $\operatorname{pr}_2$ drops the constant first coordinate, with inverse $p \mapsto (b', p)$.
   - *Why needed:* It is clause 3 of the theorem and the vehicle by which the refinements transport structure.

5. **Principal and vector refinements.** Show the action $(b', p)g = (b', pg)$ is free and fibrewise transitive with equivariant trivialisations, and that fibrewise linear structure transports.
   - *Hint:* Freeness and transitivity descend from $P$ through $\operatorname{pr}_2$; equivariance of $\Psi$ is equivariance of $\psi_U$; transport the vector-space structure across the linear isomorphism $\operatorname{pr}_2|_{E'_{b'}}$.
   - *Why needed:* They are the second and third theorems, and the reason the pull-back is used for principal and vector bundles at all.

---

# Lemma Decomposition

> [!note]- Lemma 1: A fibre bundle projection is a surjective submersion
> **Statement:** Let $(E, \pi, B)$ be a fibre bundle. Then $\pi : E \to B$ is surjective and a submersion: for every $p \in E$ the differential $d\pi_p : T_pE \to T_{\pi(p)}B$ is surjective.
>
> **Hint:** Locally $\pi$ factors as $\operatorname{pr}_1 \circ \psi_U$ through a diffeomorphism and the projection of a product.
>
> **Why needed:** Submersivity of $\pi$ is the regularity hypothesis that makes $E' = \Phi^{-1}(\Delta_B)$ a manifold (Lemma 2). Surjectivity is used to show $\pi'$ is surjective.
>
> > [!note]- Full proof
> > Surjectivity of $\pi$ is part of the definition of a fibre bundle. For submersivity, fix $p \in E$ and set $x = \pi(p)$. Choose an open neighbourhood $U \ni x$ in $B$ and a local trivialisation $\psi_U : \pi^{-1}(U) \to U \times F$, which is a diffeomorphism satisfying $\operatorname{pr}_1 \circ \psi_U = \pi$ on $\pi^{-1}(U)$, where $\operatorname{pr}_1 : U \times F \to U$ is projection onto the first factor. Differentiating this identity at $p$,
> > $$d\pi_p = d(\operatorname{pr}_1)_{\psi_U(p)} \circ (d\psi_U)_p \qquad \text{(chain rule applied to } \pi = \operatorname{pr}_1\circ\psi_U \text{).}$$
> > Now $(d\psi_U)_p : T_pE \to T_{\psi_U(p)}(U \times F)$ is a linear isomorphism, because $\psi_U$ is a diffeomorphism. And $d(\operatorname{pr}_1)_{\psi_U(p)} : T_x U \times T_{y}F \to T_xU$ is surjective, because $\operatorname{pr}_1$ is the projection of a product of manifolds, whose differential is the corresponding projection of tangent spaces $(v, w) \mapsto v$ (here $y \in F$ is the second coordinate of $\psi_U(p)$). A composition of a surjection after an isomorphism is surjective, so $d\pi_p$ is surjective. Since $p$ was arbitrary, $\pi$ is a submersion. This is exactly the corollary "$\pi$ is a submersion" recorded on [[Def - Fibre Bundle|the fibre bundle page]]; we reprove it here to keep the argument self-contained.

> [!note]- Lemma 2: The fibre product is an embedded submanifold
> **Statement:** With $\Phi : B' \times E \to B \times B$, $\Phi(b', p) = (\lambda(b'), \pi(p))$, and $\Delta_B = \{(x,x)\}$ the diagonal, the set $E' = \Phi^{-1}(\Delta_B) = \{(b', p) : \lambda(b') = \pi(p)\}$ is a properly embedded smooth submanifold of $B' \times E$ of codimension $m = \dim B$, hence of dimension $\dim B' + \dim F$. Its tangent space at $(b', p) \in E'$ is
> $$T_{(b',p)}E' = \{(u, w) \in T_{b'}B' \times T_pE : d\lambda_{b'}(u) = d\pi_p(w)\}.$$
>
> **Hint:** In a chart $\varphi$ of $B$ near $x = \lambda(b') = \pi(p)$, $E'$ is locally the zero set of $g(b', p) = \varphi(\lambda(b')) - \varphi(\pi(p)) \in \mathbb R^m$; use Lemma 1 to see $0$ is a regular value.
>
> **Why needed:** It is clause 1 of the theorem, and it is what makes $E'$ a manifold so that everything downstream — the local trivialisation, the smoothness of $\operatorname{pr}_2|_{E'}$ — has meaning.
>
> > [!note]- Full proof
> > **Step 0 — the ambient objects.** $B' \times E$ is a smooth manifold of dimension $\dim B' + \dim E = \dim B' + m + f$, and $\Phi(b', p) = (\lambda(b'), \pi(p))$ is smooth, being built from the smooth maps $\lambda$ and $\pi$ and the projections. The diagonal $\Delta_B = \{(x, x) : x \in B\}$ is a closed embedded submanifold of $B \times B$: it is the image of the smooth proper embedding $\delta : B \to B \times B$, $x \mapsto (x, x)$ (an embedding because $\operatorname{pr}_1\circ\delta = \mathrm{id}_B$ makes $\delta$ a section, hence an immersion and a homeomorphism onto its image, and proper because it is closed). We prove submanifoldhood locally, since being an embedded submanifold is a local property of a subset.
> >
> > **Step 1 — a local defining equation.** Fix $(b'_0, p_0) \in E'$ and put $x_0 = \lambda(b'_0) = \pi(p_0) \in B$. Choose a smooth chart $\varphi : V \to \mathbb R^m$ of $B$ with $x_0 \in V$. Since $\lambda$ and $\pi$ are continuous, the set
> > $$W = (\lambda\circ\operatorname{pr}_1)^{-1}(V) \cap (\pi\circ\operatorname{pr}_2)^{-1}(V) \subseteq B' \times E$$
> > is an open neighbourhood of $(b'_0, p_0)$, on which $\lambda(b') \in V$ and $\pi(p) \in V$, so $\varphi$ may be applied to both. Define the smooth map
> > $$g : W \to \mathbb R^m, \qquad g(b', p) = \varphi(\lambda(b')) - \varphi(\pi(p)).$$
> > For $(b', p) \in W$ we have $(b', p) \in E'$ if and only if $\lambda(b') = \pi(p)$, which (as $\varphi$ is injective) holds if and only if $\varphi(\lambda(b')) = \varphi(\pi(p))$, that is $g(b', p) = 0$. Hence
> > $$E' \cap W = g^{-1}(0). \qquad \text{(} \varphi \text{ injective on } V \text{)}$$
> >
> > **Step 2 — $0$ is a regular value of $g$.** Fix $(b', p) \in g^{-1}(0)$, so $\lambda(b') = \pi(p) = x \in V$. The differential is
> > $$dg_{(b',p)}(u, w) = d\varphi_x\big(d\lambda_{b'}(u)\big) - d\varphi_x\big(d\pi_p(w)\big) \qquad \text{(chain rule and linearity of } d\varphi_x \text{),}$$
> > for $(u, w) \in T_{b'}B' \times T_pE$. Restrict to the directions $(0, w)$ tangent to the $E$-factor:
> > $$dg_{(b',p)}(0, w) = -\,d\varphi_x\big(d\pi_p(w)\big) \qquad \text{(setting } u = 0 \text{).}$$
> > As $w$ ranges over $T_pE$, $d\pi_p(w)$ ranges over all of $T_xB$, because $d\pi_p$ is surjective (by Lemma 1, $\pi$ is a submersion); and $d\varphi_x : T_xB \to \mathbb R^m$ is a linear isomorphism, because $\varphi$ is a chart. Therefore $\{dg_{(b',p)}(0, w) : w \in T_pE\} = d\varphi_x(T_xB) = \mathbb R^m$, so already the restriction $w \mapsto dg_{(b',p)}(0, w)$ is surjective, and a fortiori $dg_{(b',p)}$ is surjective. Thus every point of $g^{-1}(0)$ is a regular point, so $0 \in \mathbb R^m$ is a regular value of $g$.
> >
> > **Step 3 — apply the regular value theorem.** We invoke the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]]: *if $\Psi : M \to N$ is smooth and $c \in N$ is a regular value, then $\Psi^{-1}(c)$, if nonempty, is a properly embedded smooth submanifold of $M$ of codimension $\dim N$, with $T_q\Psi^{-1}(c) = \ker d\Psi_q$ at each $q$.* Applying it to $g : W \to \mathbb R^m$ with the regular value $0$ (Step 2), the set $E' \cap W = g^{-1}(0)$ is a properly embedded submanifold of $W$ of codimension $m$, and
> > $$T_{(b',p)}(E'\cap W) = \ker dg_{(b',p)} = \{(u, w) : d\varphi_x(d\lambda_{b'}u) = d\varphi_x(d\pi_p w)\} = \{(u, w) : d\lambda_{b'}u = d\pi_p w\},$$
> > the last equality because $d\varphi_x$ is injective. As $(b'_0, p_0) \in E'$ was arbitrary, $E'$ is covered by open sets $W$ in each of which it is an embedded submanifold of codimension $m$; being an embedded submanifold is local, so $E'$ is an embedded submanifold of $B' \times E$ of codimension $m$. Its dimension is $(\dim B' + m + f) - m = \dim B' + f = \dim B' + \dim F$.
> >
> > **Step 4 — proper embedding.** $E' = \Phi^{-1}(\Delta_B)$ is a closed subset of $B' \times E$, because $\Delta_B$ is closed in $B \times B$ and $\Phi$ is continuous. A closed embedded submanifold is properly embedded (the inclusion of a closed subset is a proper map). Therefore $E'$ is a properly embedded submanifold. $\blacksquare$

> [!note]- Lemma 3: The pull-back of a local trivialisation is a local trivialisation
> **Statement:** Let $U \subseteq B$ be open with a local trivialisation $\psi_U : \pi^{-1}(U) \to U \times F$, and let $q : U \times F \to F$ be projection onto the second factor. Put $U' = \lambda^{-1}(U) \subseteq B'$. Then $\pi'^{-1}(U') = E' \cap (U' \times E)$, and the map
> $$\Psi : \pi'^{-1}(U') \to U' \times F, \qquad \Psi(b', p) = \big(b',\, q(\psi_U(p))\big)$$
> is a diffeomorphism with $\operatorname{pr}_1 \circ \Psi = \pi'$. As $U$ ranges over a trivialising cover of $B$, the sets $U' = \lambda^{-1}(U)$ cover $B'$.
>
> **Hint:** The inverse is $(b', y) \mapsto (b', \psi_U^{-1}(\lambda(b'), y))$; check it lands in $E'$ and that the two composites are the identity.
>
> **Why needed:** It supplies the local product structure of clause 2, exhibits the typical fibre $F$, and makes $\pi'$ locally a projection.
>
> > [!note]- Full proof
> > **Step 0 — the domain.** For $(b', p) \in E'$ we have $(b', p) \in \pi'^{-1}(U')$ iff $\pi'(b', p) = b' \in U' = \lambda^{-1}(U)$, iff $\lambda(b') \in U$. Since $(b', p) \in E'$ means $\pi(p) = \lambda(b')$, the condition $\lambda(b') \in U$ is equivalent to $\pi(p) \in U$, i.e. $p \in \pi^{-1}(U)$, the domain of $\psi_U$. Hence $\pi'^{-1}(U') = \{(b', p) \in E' : b' \in U'\} = E' \cap (U' \times E)$, and on it $\psi_U(p)$ is defined. That the $U' = \lambda^{-1}(U)$ cover $B'$ is immediate: if the $U$ cover $B$ and $b' \in B'$, then $\lambda(b') \in U$ for some $U$, so $b' \in \lambda^{-1}(U) = U'$.
> >
> > **Step 1 — $\Psi$ is well defined and smooth.** For $(b', p) \in \pi'^{-1}(U')$, $\psi_U(p) \in U \times F$, so $q(\psi_U(p)) \in F$ and $\Psi(b', p) = (b', q(\psi_U(p))) \in U' \times F$. The map $(b', p) \mapsto (b', q(\psi_U(p)))$ is smooth on the open subset $U' \times \pi^{-1}(U)$ of $B' \times E$ as a composite of smooth maps ($\psi_U$, $q$, projections); its restriction to the embedded submanifold $\pi'^{-1}(U') \subseteq E'$ is smooth, because restriction of a smooth map to an embedded submanifold is smooth (Lemma 2 makes $E'$ embedded).
> >
> > **Step 2 — the candidate inverse.** Define $\Theta : U' \times F \to B' \times E$ by
> > $$\Theta(b', y) = \big(b',\, \psi_U^{-1}(\lambda(b'), y)\big).$$
> > This is smooth ($\lambda$, $\psi_U^{-1}$, and the pairing are smooth). Its image lies in $E'$: setting $p := \psi_U^{-1}(\lambda(b'), y)$, we have $\psi_U(p) = (\lambda(b'), y)$, so $\pi(p) = \operatorname{pr}_1(\psi_U(p)) = \lambda(b')$ (using $\operatorname{pr}_1\circ\psi_U = \pi$), whence $(b', p) \in E'$; and $b' \in U'$, so $(b', p) \in \pi'^{-1}(U')$. As $E'$ is embedded, $\Theta$ is smooth as a map into $E'$.
> >
> > **Step 3 — $\Psi$ and $\Theta$ are mutually inverse.** For $(b', y) \in U' \times F$, with $p = \psi_U^{-1}(\lambda(b'), y)$,
> > $$\Psi(\Theta(b', y)) = \Psi(b', p) = \big(b',\, q(\psi_U(p))\big) = \big(b',\, q(\lambda(b'), y)\big) = (b', y) \qquad \text{(} \psi_U(p) = (\lambda(b'), y),\ q(\lambda(b'), y) = y \text{).}$$
> > Conversely, for $(b', p) \in \pi'^{-1}(U')$, write $\psi_U(p) = (\pi(p), q(\psi_U(p))) = (\lambda(b'), q(\psi_U(p)))$, using $\operatorname{pr}_1\circ\psi_U = \pi$ and $\pi(p) = \lambda(b')$. Then
> > $$\Theta(\Psi(b', p)) = \Theta\big(b',\, q(\psi_U(p))\big) = \big(b',\, \psi_U^{-1}(\lambda(b'), q(\psi_U(p)))\big) = \big(b',\, \psi_U^{-1}(\psi_U(p))\big) = (b', p).$$
> > So $\Psi$ is a bijection with smooth inverse $\Theta$, hence a diffeomorphism.
> >
> > **Step 4 — $\Psi$ is over $U'$.** By construction the first coordinate of $\Psi(b', p)$ is $b' = \pi'(b', p)$, so $\operatorname{pr}_1 \circ \Psi = \pi'$. Thus $\Psi$ is a local trivialisation of $(E', \pi', B')$ over $U'$ with typical fibre $F$. $\blacksquare$

> [!note]- Lemma 4: The second projection identifies the fibres
> **Statement:** For each $b' \in B'$, the fibre is $E'_{b'} = \{b'\} \times E_{\lambda(b')}$, and the restriction $\operatorname{pr}_2|_{E'_{b'}} : E'_{b'} \to E_{\lambda(b')}$, $(b', p) \mapsto p$, is a diffeomorphism. Moreover $\pi \circ \operatorname{pr}_2 = \lambda \circ \pi'$ on $E'$.
>
> **Hint:** The fibre is a slice with constant first coordinate; $\operatorname{pr}_2$ forgets it, with inverse $p \mapsto (b', p)$.
>
> **Why needed:** It is clauses 3 and 4, and the isomorphism through which the refinements transport structure.
>
> > [!note]- Full proof
> > **Fibre computation.** By definition $E'_{b'} = \pi'^{-1}(b') = \{(c, p) \in E' : \operatorname{pr}_1(c, p) = b'\} = \{(b', p) : \lambda(b') = \pi(p)\} = \{b'\} \times \{p \in E : \pi(p) = \lambda(b')\} = \{b'\} \times E_{\lambda(b')}$, where $E_{\lambda(b')} = \pi^{-1}(\lambda(b'))$ is the fibre of $E$ over $\lambda(b')$.
> >
> > **$\operatorname{pr}_2$ on the fibre is a diffeomorphism.** The fibre $E_{\lambda(b')} = \pi^{-1}(\lambda(b'))$ is an embedded submanifold of $E$ (a fibre of a submersion is a regular level set, by Lemma 1 and the regular value theorem), and $E'_{b'}$ is an embedded submanifold of $E'$ (a fibre of the submersion $\pi'$, which is a submersion by Lemma 3, its local form being a projection). The map $\operatorname{pr}_2|_{E'_{b'}} : (b', p) \mapsto p$ is smooth (restriction of the smooth $\operatorname{pr}_2$) and bijective onto $E_{\lambda(b')}$ with inverse $p \mapsto (b', p)$; this inverse is smooth because $p \mapsto (b', p)$ is the restriction of the smooth map $E \to B' \times E$, $p \mapsto (b', p)$, and it lands in the embedded submanifold $E'$. Hence $\operatorname{pr}_2|_{E'_{b'}}$ is a diffeomorphism $E'_{b'} \xrightarrow{\cong} E_{\lambda(b')}$.
> >
> > **Commutativity.** For $(b', p) \in E'$ we have $\pi(\operatorname{pr}_2(b', p)) = \pi(p) = \lambda(b') = \lambda(\pi'(b', p))$, using the defining relation $\pi(p) = \lambda(b')$ of $E'$ and $\pi'(b', p) = b'$. Thus $\pi \circ \operatorname{pr}_2 = \lambda \circ \pi'$. $\blacksquare$

> [!note]- Lemma 5: The principal refinement
> **Statement:** If $\pi : P \to B$ is a principal $G$-bundle, then the right action $(b', p)\cdot g = (b', p\cdot g)$ on $\lambda^*P$ is smooth, free, and transitive on each fibre $\pi'^{-1}(b')$, the local trivialisations $\Psi$ of Lemma 3 are $G$-equivariant, and $\operatorname{pr}_2$ is $G$-equivariant. Consequently $\lambda^*P$ is a principal $G$-bundle over $B'$.
>
> **Hint:** Every clause descends from the corresponding clause for $P$ through the fibrewise identification $\operatorname{pr}_2$ of Lemma 4.
>
> **Why needed:** It is the principal refinement; it is what makes the pull-back usable in gauge theory, where the objects of interest are principal bundles.
>
> > [!note]- Full proof
> > Recall a principal $G$-bundle is a fibre bundle $\pi : P \to B$ with a smooth right $G$-action that is free, transitive on each fibre, and admits $G$-equivariant local trivialisations $\psi_U(p\cdot g) = \psi_U(p)\cdot g$, where $G$ acts on $U \times G$ by $(x, h)\cdot g = (x, hg)$.
> >
> > **Step 0 — the map $\lambda^*P$ is a fibre bundle.** By the base theorem (clauses 1–4, Lemmas 2–4), $\lambda^*P$ is a fibre bundle over $B'$ with fibre $G$ (the typical fibre of $P$).
> >
> > **Step 1 — the action is smooth and fibre-preserving.** The map $\lambda^*P \times G \to \lambda^*P$, $((b', p), g) \mapsto (b', p\cdot g)$, is the restriction of the smooth map $(B' \times P) \times G \to B' \times P$, $((b', p), g) \mapsto (b', p\cdot g)$ (built from the smooth $G$-action on $P$), and it maps $\lambda^*P$ to itself because $\pi(p\cdot g) = \pi(p) = \lambda(b')$ (the $G$-action preserves fibres of $P$), so $(b', p\cdot g) \in \lambda^*P$. As $\lambda^*P$ is embedded, the action is smooth into it. It satisfies the action axioms because the $P$-action does: $(b', p)\cdot e = (b', p\cdot e) = (b', p)$ and $((b', p)\cdot g)\cdot h = (b', (p\cdot g)\cdot h) = (b', p\cdot(gh)) = (b', p)\cdot(gh)$. It preserves fibres of $\pi'$: $\pi'((b', p)\cdot g) = \pi'(b', p\cdot g) = b'$.
> >
> > **Step 2 — freeness.** Suppose $(b', p)\cdot g = (b', p)$. Then $(b', p\cdot g) = (b', p)$, so $p\cdot g = p$; since the $G$-action on $P$ is free, $g = e$. Hence the action on $\lambda^*P$ is free.
> >
> > **Step 3 — transitivity on fibres.** Fix $b' \in B'$ and two points $(b', p_1), (b', p_2)$ of the fibre $\pi'^{-1}(b') = \{b'\} \times P_{\lambda(b')}$ (Lemma 4). Then $p_1, p_2 \in P_{\lambda(b')}$, and since $G$ acts transitively on the fibre $P_{\lambda(b')}$ of $P$, there is $g \in G$ with $p_2 = p_1\cdot g$. Then $(b', p_2) = (b', p_1\cdot g) = (b', p_1)\cdot g$. So $G$ acts transitively on $\pi'^{-1}(b')$.
> >
> > **Step 4 — equivariant trivialisations.** With $\Psi(b', p) = (b', q(\psi_U(p)))$ from Lemma 3 (here $q : U \times G \to G$ is the second projection and $\psi_U$ is a $G$-equivariant trivialisation of $P$), compute for $g \in G$:
> > $$\Psi\big((b', p)\cdot g\big) = \Psi(b', p\cdot g) = \big(b',\, q(\psi_U(p\cdot g))\big) = \big(b',\, q(\psi_U(p)\cdot g)\big) \qquad \text{(equivariance } \psi_U(p\cdot g) = \psi_U(p)\cdot g \text{).}$$
> > Writing $\psi_U(p) = (\lambda(b'), h)$ with $h = q(\psi_U(p)) \in G$, the $G$-action on $U \times G$ gives $\psi_U(p)\cdot g = (\lambda(b'), hg)$, so $q(\psi_U(p)\cdot g) = hg = q(\psi_U(p))\cdot g$. Therefore
> > $$\Psi\big((b', p)\cdot g\big) = \big(b',\, q(\psi_U(p))\cdot g\big) = \Psi(b', p)\cdot g,$$
> > where on the right $G$ acts on $U' \times G$ by $(b', h)\cdot g = (b', hg)$. So $\Psi$ is $G$-equivariant. This is the last defining clause, so $\lambda^*P$ is a principal $G$-bundle.
> >
> > **Step 5 — $\operatorname{pr}_2$ is equivariant.** For $(b', p) \in \lambda^*P$ and $g \in G$, $\operatorname{pr}_2((b', p)\cdot g) = \operatorname{pr}_2(b', p\cdot g) = p\cdot g = \operatorname{pr}_2(b', p)\cdot g$. Hence $\operatorname{pr}_2$ is $G$-equivariant. $\blacksquare$

> [!note]- Lemma 6: The vector refinement
> **Statement:** If $E$ is a $\mathbb K$-vector bundle of rank $n$ (with $\mathbb K = \mathbb R$ or $\mathbb C$), then transporting the vector-space structure of $E_{\lambda(b')}$ across the bijection $\operatorname{pr}_2|_{E'_{b'}}$ makes each fibre $E'_{b'}$ a $\mathbb K$-vector space, and with these structures $\lambda^*E$ is a $\mathbb K$-vector bundle of rank $n$ whose local trivialisations $\Psi$ are fibrewise linear. The identification $(\lambda^*E)_{b'} = E_{\lambda(b')}$ via $\operatorname{pr}_2$ is the fibrewise pull-back of the operations-on-bundles construction.
>
> **Hint:** A vector bundle is a fibre bundle with fibre $\mathbb K^n$ whose trivialisations are fibrewise linear; pull those trivialisations back and check linearity survives.
>
> **Why needed:** It is the vector refinement and the compatibility with chapter II's fibrewise definition of the pull-back vector bundle.
>
> > [!note]- Full proof
> > Recall a $\mathbb K$-vector bundle of rank $n$ is a fibre bundle with typical fibre $\mathbb K^n$ whose fibres carry $\mathbb K$-vector-space structures such that the local trivialisations $\psi_U : \pi^{-1}(U) \to U \times \mathbb K^n$ are fibrewise linear isomorphisms $E_x \to \{x\} \times \mathbb K^n \cong \mathbb K^n$.
> >
> > **Step 1 — the transported structure.** Fix $b' \in B'$. By Lemma 4, $\operatorname{pr}_2|_{E'_{b'}} : E'_{b'} \to E_{\lambda(b')}$ is a bijection (indeed a diffeomorphism). Declare, for $(b', p_1), (b', p_2) \in E'_{b'}$ and $c \in \mathbb K$,
> > $$(b', p_1) + (b', p_2) := (b',\, p_1 + p_2), \qquad c\cdot(b', p_1) := (b',\, c\,p_1),$$
> > the operations on the right taken in the $\mathbb K$-vector space $E_{\lambda(b')}$. This is the unique vector-space structure on $E'_{b'}$ making $\operatorname{pr}_2|_{E'_{b'}}$ linear, since a bijection has at most one vector-space structure on its source turning it into a linear isomorphism, and this one does.
> >
> > **Step 2 — the trivialisations are fibrewise linear.** With $\Psi(b', p) = (b', q(\psi_U(p)))$ from Lemma 3, its restriction to the fibre $E'_{b'}$ is the composite
> > $$E'_{b'} \xrightarrow{\ \operatorname{pr}_2\ } E_{\lambda(b')} \xrightarrow{\ \psi_U|_{\text{fibre}}\ } \{\lambda(b')\}\times \mathbb K^n \xrightarrow{\ q\ } \mathbb K^n, \qquad (b', p) \mapsto q(\psi_U(p)).$$
> > The first arrow is linear by Step 1 (that is how the structure was defined), the second is linear because $\psi_U$ is a fibrewise-linear trivialisation of the vector bundle $E$, and the third is a linear isomorphism $\{\lambda(b')\}\times\mathbb K^n \cong \mathbb K^n$. A composite of linear maps is linear, and each is a bijection, so $\Psi|_{E'_{b'}} : E'_{b'} \to \{b'\}\times\mathbb K^n$ is a linear isomorphism. Hence $\Psi$ is a fibrewise-linear local trivialisation, and $\lambda^*E$ is a $\mathbb K$-vector bundle of rank $n$.
> >
> > **Step 3 — agreement with the fibrewise construction.** The operations-on-bundles pull-back defines $\lambda^*E$ so that its fibre over $b'$ *is* $E_{\lambda(b')}$, the identification being the projection $(b', p)\mapsto p$. By Steps 1–2 this projection is precisely the linear isomorphism $\operatorname{pr}_2|_{E'_{b'}}$. Thus the two constructions have the same total space $E'$, the same projection $\pi'$, and the same fibrewise vector-space structure identified through $\operatorname{pr}_2$; they are equal as vector bundles. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(E, \pi, B)$ be a fibre bundle with typical fibre $F$, and $\lambda : B' \to B$ smooth. Write $E' = \{(b', p) \in B' \times E : \lambda(b') = \pi(p)\}$ and $\pi' = \operatorname{pr}_1|_{E'}$.
>
> **Step 0 — $\pi$ is a submersion.** By Lemma 1, the bundle projection $\pi$ is a surjective submersion. This is the regularity fact every later step rests on.
>
> **Step 1 — clause 1: $E'$ is a properly embedded submanifold.** By Lemma 2, using the submersivity of $\pi$ from Step 0, the set $E' = \Phi^{-1}(\Delta_B)$ (with $\Phi(b', p) = (\lambda(b'), \pi(p))$) is a properly embedded smooth submanifold of $B' \times E$ of codimension $m = \dim B$, hence of dimension $\dim B' + \dim F$, with tangent space $T_{(b',p)}E' = \{(u, w) : d\lambda_{b'}u = d\pi_p w\}$. This proves clause 1.
>
> **Step 2 — clause 2: $(E', \pi', B')$ is a fibre bundle with fibre $F$.** The map $\pi' = \operatorname{pr}_1|_{E'} : E' \to B'$ is smooth (restriction of the smooth $\operatorname{pr}_1$ to the embedded submanifold $E'$). It is surjective: given $b' \in B'$, the fibre $E_{\lambda(b')} = \pi^{-1}(\lambda(b'))$ is nonempty because $\pi$ is surjective (Step 0), so choosing $p \in E_{\lambda(b')}$ gives $(b', p) \in E'$ with $\pi'(b', p) = b'$. Let $\{U_\alpha\}$ be a cover of $B$ by trivialising open sets with local trivialisations $\psi_{U_\alpha}$. By Lemma 3, the sets $U'_\alpha = \lambda^{-1}(U_\alpha)$ cover $B'$, and over each $U'_\alpha$ the map $\Psi_\alpha : \pi'^{-1}(U'_\alpha) \to U'_\alpha \times F$ is a diffeomorphism with $\operatorname{pr}_1\circ\Psi_\alpha = \pi'$. These are local trivialisations of $(E', \pi', B')$ with typical fibre $F$; hence it is a fibre bundle with fibre $F$. This proves clause 2.
>
> **Step 3 — clauses 3 and 4: fibre identification and commuting square.** By Lemma 4, for each $b' \in B'$ the fibre is $E'_{b'} = \{b'\}\times E_{\lambda(b')}$, the restriction $\operatorname{pr}_2|_{E'_{b'}} : E'_{b'} \to E_{\lambda(b')}$ is a diffeomorphism, and $\pi\circ\operatorname{pr}_2 = \lambda\circ\pi'$ on $E'$. These are clauses 3 and 4.
>
> **Step 4 — the principal refinement.** Suppose $E = P$ is a principal $G$-bundle. By Lemma 5, the action $(b', p)\cdot g = (b', p\cdot g)$ on $\lambda^*P$ is smooth, free, transitive on the fibres of $\pi'$, and admits the $G$-equivariant trivialisations $\Psi_\alpha$; together with Step 2 (that $\lambda^*P$ is a fibre bundle) these are exactly the defining clauses of a principal $G$-bundle, so $\lambda^*P$ is a principal $G$-bundle over $B'$. By the same lemma $\operatorname{pr}_2 : \lambda^*P \to P$ is $G$-equivariant.
>
> **Step 5 — the vector refinement.** Suppose $E$ is a $\mathbb K$-vector bundle of rank $n$. By Lemma 6, transporting the vector-space structure of $E_{\lambda(b')}$ across $\operatorname{pr}_2|_{E'_{b'}}$ makes $\lambda^*E$ a $\mathbb K$-vector bundle of rank $n$ with fibrewise-linear trivialisations $\Psi_\alpha$, and this vector bundle coincides with the fibrewise pull-back $(\lambda^*E)_{b'} = E_{\lambda(b')}$ under the identification $\operatorname{pr}_2$.
>
> **Conclusion.** The bare fibre-bundle statement (clauses 1–4) holds for every fibre bundle and every smooth $\lambda$, and the construction upgrades to a principal $G$-bundle when $E$ is principal and to a rank-$n$ vector bundle when $E$ is a vector bundle, in each case with $\operatorname{pr}_2$ preserving the extra structure fibrewise. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fields along a curve and the geodesic equation (Riemannian geometry).** Let $(M, g)$ be a Riemannian manifold, $\gamma : (-\varepsilon, \varepsilon) \to M$ a smooth curve, and consider $\gamma^*TM$. The theorem makes this a rank-$n$ vector bundle over an interval, hence trivial, and its sections are exactly the vector fields along $\gamma$; the velocity $\dot\gamma$ is the distinguished section $t \mapsto (t, \dot\gamma(t))$. The theorem applies because $\gamma$ is a smooth map and $TM$ is a vector bundle; it is non-obvious that "field along a curve", usually introduced by hand as an assignment $t \mapsto V(t) \in T_{\gamma(t)}M$, is literally a section of a genuine bundle, which is what lets the covariant derivative along $\gamma$ and the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ be treated with the full section calculus.

**Restriction of the determinant line bundle to a subvariety (algebraic and complex geometry).** Let $L \to X$ be a holomorphic line bundle and $Y \hookrightarrow X$ a complex submanifold. The restriction $L|_Y$ is the pull-back of $L$ along the inclusion, so by the theorem it is a line bundle over $Y$; combined with the naturality of the first Chern class this gives $c_1(L|_Y) = \iota^* c_1(L)$, the restriction of the class. The theorem applies because an inclusion is smooth; the non-obvious payoff is that intersection numbers on $X$ can be computed by restricting bundles to subvarieties, the engine of many degree computations.

**Bundles over a covering space (topology and gauge theory).** Let $p : \tilde X \to X$ be a smooth covering map and $E \to X$ a bundle. The pull-back $p^*E$ is a bundle over $\tilde X$ on which the deck group acts; this is the standard way to trivialise a bundle by passing to a cover, and, run in reverse, it realises flat bundles as quotients of trivial bundles over the universal cover. The theorem applies because a covering map is a smooth (indeed local-diffeomorphism) map; the non-obvious point is that the deck-group symmetry of $\tilde X$ lifts to $p^*E$ precisely because pull-back is natural, which is what connects flat connections to monodromy representations in chapter V.

---

# Bridges

- **Restriction of a bundle to a submanifold.** For an embedded submanifold $\iota : B' \hookrightarrow B$, the restriction $E|_{B'} := \pi^{-1}(B')$ is canonically the pull-back $\iota^*E$: the fibre product $\{(b', p) : \iota(b') = \pi(p)\}$ maps by $\operatorname{pr}_2$ diffeomorphically onto $\pi^{-1}(B')$, since $\iota$ is injective, so the two total spaces agree. Thus every statement about pull-backs specialises to restrictions, and "restrict then do X" equals "do X then restrict" whenever X is natural.

- **Bundles along curves and horizontal lifts (chapter V).** For a curve $\gamma : I \to B$ the pull-back $\gamma^*P$ of a principal bundle is a principal bundle over an interval, and a connection $A$ on $P$ pulls back to $\gamma^*A$ on $\gamma^*P$; because a bundle over an interval is trivial, the horizontal-lift equation becomes a linear ordinary differential equation $\dot h + A(\dot\gamma)h = 0$ in a trivialisation. The present theorem is what guarantees $\gamma^*P$ is a bundle to begin with, so that parallel transport is defined; the identity $F_{\gamma^*A} = \gamma^*F_A$ (proved from the local curvature formula and the naturality of the exterior derivative) is what makes holonomy computable from the curvature downstairs.

- **Naturality of characteristic classes (chapter VI).** Chern–Weil theory assigns to a connection $A$ on $P$ the forms $f(F_A)$ for invariant polynomials $f$; because $F_{\lambda^*A} = \lambda^*F_A$ and $\lambda^*$ commutes with $f$ and with the exterior derivative, the cohomology classes satisfy $\lambda^* c(P) = c(\lambda^*P)$. The pull-back theorem supplies the bundle $\lambda^*P$ on which this equation lives; naturality of characteristic classes is the assertion that these invariants are computed in the base and transported along maps, which is the foundation of the homotopy classification and of the four-manifold invariants of the later chapters.

- **Homotopy invariance and classifying maps.** Because pull-back is a bundle operation, the isomorphism class of $\lambda^*E$ depends only on the homotopy class of $\lambda$ (proved by pulling back over the cylinder $B'\times[0,1]$ and sliding a trivialisation along the interval direction). This turns the assignment $[\lambda] \mapsto [\lambda^*E]$ into a functor on homotopy classes, and represents every bundle over $B'$ as $\lambda^* E_{\mathrm{univ}}$ for a classifying map $\lambda$ into a classifying space — the organising principle of bundle classification.

---

# Unlocked by This

> [!tip] Pull-back connection and curvature *(from Gauge Theory IV)*
> A connection on $E$ (or $P$) pulls back to a connection on $\lambda^*E$ (or $\lambda^*P$) with $F_{\lambda^*A} = \lambda^*F_A$. This is the mechanism behind horizontal lifts and the naturality of curvature; see **Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles** and the pull-back of a connection.

> [!tip] Homotopic maps pull back isomorphic bundles *(from Gauge Theory III)*
> Once $\lambda^*E$ is a bundle, homotopic maps $\lambda_0 \simeq \lambda_1$ yield $\lambda_0^*E \cong \lambda_1^*E$. See [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]], whose proof pulls the bundle back over $B'\times[0,1]$ and slides a trivialisation along the cylinder.
