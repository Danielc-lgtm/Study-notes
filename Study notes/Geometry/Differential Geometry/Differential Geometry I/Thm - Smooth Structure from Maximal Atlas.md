---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Topological Manifold"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M$ is a topological $n$-manifold. A [[Def - Smooth Atlas and Smooth Structure|smooth atlas]] is an atlas whose transition functions are diffeomorphisms. Two smooth atlases are **compatible** if their union is a smooth atlas; this is the equivalence relation defining smooth structures. A smooth atlas is **maximal** if no chart smoothly compatible with all of its charts is missing from it. For full notation see [[Differential Geometry I — Smooth Manifolds and Atlases]].

---

# Statement

> **Theorem (Smooth Structure from Maximal Atlas; Lee Proposition 1.17).** Let $M$ be a topological manifold.
>
> (a) Every smooth atlas $\mathcal{A}$ for $M$ is contained in a unique maximal smooth atlas, called the **smooth structure determined by $\mathcal{A}$** and denoted $\overline{\mathcal{A}}$.
>
> (b) Two smooth atlases $\mathcal{A}$ and $\mathcal{B}$ for $M$ determine the same smooth structure if and only if their union $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas.

> **Corollary.** A smooth structure on $M$ can equivalently be defined as (i) an equivalence class of smooth atlases under the compatibility relation, or (ii) a maximal smooth atlas. The bijection sends an equivalence class to the union of all atlases in it (its unique maximal element), and conversely a maximal atlas to the equivalence class of all its sub-atlases.

The point of the corollary is that "smooth structure" is well-defined as either an equivalence class or a maximal atlas, and the two formulations are interchangeable.

---

# Motivation

A smooth structure on $M$ should be an intrinsic *thing*, not an artifact of which specific atlas we chose to describe it. The natural candidate is "an equivalence class of compatible smooth atlases" — but equivalence classes are awkward to work with, and we want a *single object* representing the smooth structure. The maximal atlas is that single object: it is the union of all atlases in the equivalence class, and it contains every chart that is smoothly compatible with any atlas representing the structure. To pick up a chart, we no longer have to ask "with respect to which atlas?" — every smooth chart is simply *in* the maximal atlas.

The theorem closes a small but real conceptual gap: it justifies the practice of specifying a smooth manifold by a *small* atlas (typically two stereographic charts on $S^n$, or $n+1$ affine charts on $\mathbb{RP}^n$) and then freely using any chart smoothly compatible with this atlas. Without the theorem, "specify a smooth structure by a single atlas" would be ambiguous — many atlases would compete, and we would have to keep track of which one we chose. The theorem says: any atlas does, the maximal atlas is uniquely determined, the choice of representative is irrelevant.

Part (b) is the *practical compatibility test*: to verify that two atlases determine the same smooth structure (e.g., the stereographic and graph-coordinate atlases on $S^n$), check that their union is smooth. This is what [[Ex - Compatibility of Two Atlases on the Sphere]] does.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a smooth atlas on $M$. The skill lies in recognizing situations where the smooth atlas is *implicit* rather than given outright.

The first source is **a single chart making an entire space locally Euclidean**. If $M$ is a topological manifold and a single chart $(\widehat{M}, \mathrm{id} \circ \varphi^{-1})$ — equivalently, a homeomorphism $\varphi : M \to \widehat{M} \subseteq \mathbb{R}^n$ for an open $\widehat{M}$ — covers all of $M$, then $\{(M, \varphi)\}$ is automatically a smooth atlas (one chart, no transition functions to verify). The theorem then gives a smooth structure on $M$. This is the source for the standard structure on $\mathbb{R}^n$, on open subsets of $\mathbb{R}^n$, and on graphs of continuous functions $\Gamma(f) \subseteq \mathbb{R}^{n+k}$.

The second source is **a level set of a smooth function with regular value**. By the implicit function theorem, $\Phi^{-1}(c) \subseteq U \subseteq \mathbb{R}^n$ has graph coordinates at every point when $\Phi$ has a regular value at $c$; these graph charts overlap on open sets, and their transition functions are smooth (since each is a smooth coordinate-rearrangement). The level set inherits a smooth atlas, hence a smooth structure. This is the source for $S^n$ (level set of $|x|^2 = 1$), $\mathrm{SL}(n)$ (level set of $\det = 1$), $\mathrm{O}(n)$ (level set of $A^T A = I$).

The third source is **a quotient of a smooth manifold by a smooth proper free action**. If a discrete group $\Gamma$ acts on a smooth manifold $\widetilde{M}$ smoothly, freely, and properly discontinuously, then the quotient $\widetilde{M}/\Gamma$ admits a smooth atlas whose charts are lifted from charts on $\widetilde{M}$ on open sets where the quotient map is a homeomorphism. This is the source for $T^n = \mathbb{R}^n/\mathbb{Z}^n$ (see [[Ex - The Torus is a Smooth Manifold via Quotient]]) and $\mathbb{RP}^n = S^n/\{\pm 1\}$.

The fourth source is **a finite product of smooth manifolds**. The product atlas $\{(U_\alpha \times V_\beta, \varphi_\alpha \times \psi_\beta)\}$ is smooth, with transition functions $(\varphi_\alpha \times \psi_\beta) \circ (\varphi_{\alpha'} \times \psi_{\beta'})^{-1} = (\varphi_\alpha \circ \varphi_{\alpha'}^{-1}) \times (\psi_\beta \circ \psi_{\beta'}^{-1})$, which is smooth as a product of smooth maps (see [[Thm - Product of Smooth Manifolds is a Smooth Manifold]]).

The fifth source is **a set with the smooth manifold chart lemma applied to it** (Lee 1.35). When the candidate smooth structure is specified by an explicit family of maps to $\mathbb{R}^n$ satisfying the lemma's hypotheses, the lemma produces a topology and a smooth atlas, and this theorem (Lee 1.17) extends the atlas to a maximal atlas. This is the source for the Grassmannian (see [[Ex - The Grassmannian is a Smooth Manifold]]).

**Targets (Output Amplification)**

The conclusion is a uniquely determined smooth structure. Combined with other facts, this enables:

The first target: **any chart smoothly compatible with the atlas is in the smooth structure**. Once you have specified a smooth structure by an atlas, you can freely add any new chart you have checked is smoothly compatible (it is then in the maximal atlas). For example: spherical coordinates on $S^2$ are smoothly compatible with stereographic coordinates, so they are part of the standard smooth structure on $S^2$, and one may freely use them. This is the source of the practical phrase "without loss of generality, we work in [convenient] coordinates."

The second target: **two atlases give the same smooth structure iff their union is smooth**. This is the *test for atlas-equivalence*, used to show that competing constructions (stereographic vs. graph coordinates on $S^n$; product vs. quotient on $T^n$) give the same manifold. Combined with the easy direction (atlases in one equivalence class trivially have smooth pairwise overlaps), this gives a complete classification of atlases up to equivalence.

The third target: **a smooth function or smooth map is determined by smoothness in a single representative atlas**. Once the smooth structure is fixed, $f : M \to N$ is smooth iff $\psi \circ f \circ \varphi^{-1}$ is smooth for some pair of charts $(U, \varphi), (V, \psi)$ around each point — equivalently for every pair of charts in the maximal atlas. The theorem ensures consistency: if $f$ is smooth with respect to the *atlas*, it is smooth with respect to the maximal atlas, hence smooth as a map between smooth manifolds. This is the foundation of [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]].

The fourth target: **two competing smooth structures on the same topological manifold determine the same smooth manifold iff they have a common refinement that is smooth**. The non-standard smooth structure on $\mathbb{R}$ given by the chart $\psi(x) = x^3$ (Lee Example 1.23) and the standard one cannot be combined into a single smooth atlas (the transition is not smooth), so they are genuinely different smooth structures — even though both are smooth manifolds diffeomorphic to standard $\mathbb{R}$ via the diffeomorphism $x \mapsto x^3$.

---

# Why Is It True

The intuition is straightforward: **smooth compatibility is *transitive*, by composition of transition functions on triple overlaps**.

Take any chart $(U, \varphi)$ smoothly compatible with every chart in $\mathcal{A}$, and any chart $(V, \psi)$ similarly. We need to show $(U, \varphi)$ and $(V, \psi)$ are themselves smoothly compatible. Pick a point $p \in U \cap V$ (assuming nonempty overlap). Since $\mathcal{A}$ covers $M$, there is a chart $(W, \theta) \in \mathcal{A}$ with $p \in W$. On the triple overlap $U \cap V \cap W$, the transition $\psi \circ \varphi^{-1}$ factors as

$$\psi \circ \varphi^{-1} = (\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1}).$$

Both factors are smooth — the first because $(W, \theta)$ and $(V, \psi)$ are smoothly compatible, the second because $(W, \theta)$ and $(U, \varphi)$ are. The composition of smooth maps is smooth, so $\psi \circ \varphi^{-1}$ is smooth in a neighbourhood of $\varphi(p)$. Since $p$ was arbitrary, $\psi \circ \varphi^{-1}$ is smooth on $\varphi(U \cap V)$. By symmetry (swapping the roles of $\varphi$ and $\psi$), the inverse is smooth too. So $(U, \varphi)$ and $(V, \psi)$ are smoothly compatible.

This argument is the *transitivity of smooth compatibility relative to a covering atlas*, and it is the engine of the entire proof. Once we know that "the set of all charts smoothly compatible with $\mathcal{A}$" is itself smoothly compatible, it is a smooth atlas — and it is maximal by construction.

**The one-liner mechanism: a triple-overlap factorization $\psi \circ \varphi^{-1} = (\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1})$ — where $\theta$ is an "interpolating" chart from the reference atlas $\mathcal{A}$ — converts pairwise smooth compatibility with $\mathcal{A}$ into pairwise smooth compatibility between any two extensions.**

For part (b), the bidirectional reasoning: if $\overline{\mathcal{A}} = \overline{\mathcal{B}}$, then trivially $\mathcal{A} \cup \mathcal{B} \subseteq \overline{\mathcal{A}}$, which is a smooth atlas — so $\mathcal{A} \cup \mathcal{B}$ is. Conversely, if $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas, then $\mathcal{A} \cup \mathcal{B} \subseteq \overline{\mathcal{A}}$ (every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$, hence in $\overline{\mathcal{A}}$), and similarly $\mathcal{A} \cup \mathcal{B} \subseteq \overline{\mathcal{B}}$. The maximal atlas containing $\mathcal{A} \cup \mathcal{B}$ is then both $\overline{\mathcal{A}}$ and $\overline{\mathcal{B}}$ (by uniqueness in part (a)), so $\overline{\mathcal{A}} = \overline{\mathcal{B}}$.

---

# What Makes This Hard

The triple-overlap factorization is the entire content of the proof, but it is the kind of step that beginners often skip or get backwards. The most common error is to try to show smooth compatibility between two charts $\varphi$ and $\psi$ *directly* without invoking a third chart $\theta$ from $\mathcal{A}$ — and direct verification of smoothness of $\psi \circ \varphi^{-1}$ is not possible from the hypothesis (which is about compatibility *with $\mathcal{A}$*, not with each other). The other error is to forget that the factorization is only valid on the triple overlap, and to declare smoothness on the entire double overlap $U \cap V$ without restricting to neighbourhoods.

The other subtle point: the argument shows the *existence* of a maximal smooth atlas containing $\mathcal{A}$. Uniqueness is a separate claim: if $\mathcal{B}$ is another maximal smooth atlas containing $\mathcal{A}$, every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$ (since $\mathcal{B}$ is smooth and contains $\mathcal{A}$), so every chart of $\mathcal{B}$ is in $\overline{\mathcal{A}}$ (by definition); hence $\mathcal{B} \subseteq \overline{\mathcal{A}}$. By maximality of $\mathcal{B}$, equality holds.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $\overline{\mathcal{A}}$ as the set of all charts smoothly compatible with every chart in $\mathcal{A}$. Show $\overline{\mathcal{A}}$ is a smooth atlas by checking pairwise smooth compatibility, using a triple-overlap factorization through a chart of $\mathcal{A}$. Show $\overline{\mathcal{A}}$ is maximal and unique.

**Subgoal decomposition:**

1. **Define the candidate maximal atlas $\overline{\mathcal{A}}$.** Set $\overline{\mathcal{A}}$ to be the collection of all charts $(U, \varphi)$ on $M$ that are smoothly compatible with every chart in $\mathcal{A}$.
   - *Hint:* This is the obvious candidate — by definition it contains every chart compatible with $\mathcal{A}$.
   - *Why needed:* The maximal atlas, if it exists, must contain this set; the work is showing this set is itself a smooth atlas.

2. **Show that any two charts of $\overline{\mathcal{A}}$ are smoothly compatible.** Take $(U, \varphi), (V, \psi) \in \overline{\mathcal{A}}$ and a point $p \in U \cap V$; produce a chart $(W, \theta) \in \mathcal{A}$ with $p \in W$ (using that $\mathcal{A}$ covers $M$). Use the factorization $\psi \circ \varphi^{-1} = (\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1})$ on the triple overlap $U \cap V \cap W$.
   - *Hint:* Both factors are smooth by hypothesis. Composition of smooth maps is smooth.
   - *Why needed:* This is the transitivity argument; it establishes that $\overline{\mathcal{A}}$ is a smooth atlas.

3. **Show $\overline{\mathcal{A}}$ is maximal.** Any chart smoothly compatible with all charts in $\overline{\mathcal{A}}$ is, in particular, smoothly compatible with all charts in $\mathcal{A}$ (since $\mathcal{A} \subseteq \overline{\mathcal{A}}$); hence it is in $\overline{\mathcal{A}}$ by definition.
   - *Hint:* Maximality is a direct consequence of the definition of $\overline{\mathcal{A}}$.
   - *Why needed:* Establishes the "maximal" property of the smooth structure.

4. **Show $\overline{\mathcal{A}}$ is the unique maximal smooth atlas containing $\mathcal{A}$.** If $\mathcal{B}$ is another maximal smooth atlas containing $\mathcal{A}$, then every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$, so $\mathcal{B} \subseteq \overline{\mathcal{A}}$; maximality of $\mathcal{B}$ forces equality.
   - *Hint:* Compare $\mathcal{B}$ with $\overline{\mathcal{A}}$ using maximality.
   - *Why needed:* Establishes uniqueness; closes part (a).

5. **For (b), forward direction:** Assume $\overline{\mathcal{A}} = \overline{\mathcal{B}}$. Then $\mathcal{A} \cup \mathcal{B} \subseteq \overline{\mathcal{A}}$, which is a smooth atlas, so $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas (every pair of charts smoothly compatible).
   - *Hint:* A subset of a smooth atlas is a smooth atlas (if it still covers).
   - *Why needed:* Half of the equivalence.

6. **For (b), reverse direction:** Assume $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas. Then every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$, so $\mathcal{B} \subseteq \overline{\mathcal{A}}$; similarly $\mathcal{A} \subseteq \overline{\mathcal{B}}$. By symmetry and the uniqueness of maximal atlases, $\overline{\mathcal{A}} = \overline{\mathcal{B}}$.
   - *Hint:* Use the definition of $\overline{\mathcal{A}}$ as the set of charts compatible with $\mathcal{A}$.
   - *Why needed:* The other half of the equivalence.

---

# Lemma Decomposition

> [!note]- Lemma 1: Triple-overlap factorization of transition functions
> **Statement:** Let $(U, \varphi), (V, \psi), (W, \theta)$ be charts on a topological manifold $M$ with $U \cap V \cap W \neq \emptyset$. Then on the overlap, $\psi \circ \varphi^{-1} = (\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1})$.
>
> **Hint:** Insert $\mathrm{id} = \theta^{-1} \circ \theta$ into the middle of the composition $\psi \circ \varphi^{-1}$.
>
> **Why needed:** This is the algebraic identity that makes the transitivity argument work — it expresses the transition $\psi \circ \varphi^{-1}$ as a composition of two transitions that go through an intermediate chart.
>
> > [!note]- Full proof
> > For any $x \in \varphi(U \cap V \cap W)$, let $p = \varphi^{-1}(x) \in U \cap V \cap W$. Then
> > $$(\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1})(x) = (\psi \circ \theta^{-1})(\theta(p)) = \psi(p) = (\psi \circ \varphi^{-1})(x).$$
> > So the two functions agree on $\varphi(U \cap V \cap W)$.

> [!note]- Lemma 2: Composition of smooth maps between open subsets of Euclidean space is smooth
> **Statement:** Let $f : A \to B$ and $g : B \to C$ be smooth maps between open subsets of Euclidean spaces $\mathbb{R}^m$, $\mathbb{R}^n$, $\mathbb{R}^p$. Then $g \circ f : A \to C$ is smooth.
>
> **Hint:** Apply the chain rule to compute derivatives of all orders; each partial derivative of $g \circ f$ is a polynomial in the partial derivatives of $f$ and $g$ evaluated at appropriate points, hence smooth.
>
> **Why needed:** This is the elementary calculus fact used to conclude smoothness of $\psi \circ \varphi^{-1}$ from smoothness of its two factors.
>
> > [!note]- Full proof
> > By the chain rule, $D(g \circ f)_x = Dg_{f(x)} \circ Df_x$ as linear maps. By the smoothness of $f$ and $g$, both $Df$ and $Dg$ are smooth functions of their arguments. By induction, the $k$-th derivative of $g \circ f$ is a polynomial in the derivatives of $f$ up to order $k$ and the derivatives of $g$ up to order $k$, all smooth functions of $x$. Hence $g \circ f$ has continuous partial derivatives of all orders.

> [!note]- Lemma 3: Pairwise compatibility extends to global compatibility relative to a covering atlas
> **Statement:** Let $\mathcal{A}$ be a smooth atlas on $M$ and let $(U, \varphi), (V, \psi)$ be two charts each smoothly compatible with every chart of $\mathcal{A}$. Then $(U, \varphi)$ and $(V, \psi)$ are smoothly compatible.
>
> **Hint:** Pick a point $p \in U \cap V$, choose $(W, \theta) \in \mathcal{A}$ containing $p$, apply Lemma 1's factorization.
>
> **Why needed:** This is the heart of the existence part of Lee Proposition 1.17 — it shows that the set $\overline{\mathcal{A}}$ is indeed a smooth atlas, not just a set of charts.
>
> > [!note]- Full proof
> > Suppose $U \cap V \neq \emptyset$; otherwise compatibility is vacuous. For $p \in U \cap V$, choose $(W, \theta) \in \mathcal{A}$ with $p \in W$ (possible since $\mathcal{A}$ covers $M$). On the triple overlap $U \cap V \cap W$ (nonempty since it contains $p$), by Lemma 1,
> > $$\psi \circ \varphi^{-1} = (\psi \circ \theta^{-1}) \circ (\theta \circ \varphi^{-1}).$$
> > Both factors are smooth (the first because $(V, \psi)$ and $(W, \theta)$ are smoothly compatible; the second because $(U, \varphi)$ and $(W, \theta)$ are smoothly compatible). By Lemma 2, the composition is smooth in a neighbourhood of $\varphi(p)$. Since $p \in U \cap V$ was arbitrary, $\psi \circ \varphi^{-1}$ is smooth on $\varphi(U \cap V)$. By symmetry, $\varphi \circ \psi^{-1}$ is smooth on $\psi(U \cap V)$. So $(U, \varphi)$ and $(V, \psi)$ are smoothly compatible.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M$ be a topological manifold.
>
> **(a)** Every smooth atlas $\mathcal{A}$ for $M$ is contained in a unique maximal smooth atlas $\overline{\mathcal{A}}$.
>
> **(b)** Two smooth atlases $\mathcal{A}, \mathcal{B}$ determine the same smooth structure iff $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas.
>
> *Proof of (a).* Define
> $$\overline{\mathcal{A}} = \{(U, \varphi) : (U, \varphi) \text{ is a chart on } M \text{ smoothly compatible with every chart in } \mathcal{A}\}.$$
>
> **Step 0 — well-posedness:** $\mathcal{A} \subseteq \overline{\mathcal{A}}$ (each chart of $\mathcal{A}$ is smoothly compatible with every chart of $\mathcal{A}$, since $\mathcal{A}$ is a smooth atlas). In particular, the domains of charts in $\overline{\mathcal{A}}$ cover $M$.
>
> **Step 1 — $\overline{\mathcal{A}}$ is a smooth atlas.** By Lemma 3 above, any two charts $(U, \varphi), (V, \psi) \in \overline{\mathcal{A}}$ are smoothly compatible. Combined with Step 0, $\overline{\mathcal{A}}$ is a smooth atlas on $M$.
>
> **Step 2 — $\overline{\mathcal{A}}$ is maximal.** Suppose $(U, \varphi)$ is a chart smoothly compatible with every chart in $\overline{\mathcal{A}}$. Since $\mathcal{A} \subseteq \overline{\mathcal{A}}$, in particular $(U, \varphi)$ is smoothly compatible with every chart in $\mathcal{A}$. So $(U, \varphi) \in \overline{\mathcal{A}}$ by definition. Hence $\overline{\mathcal{A}}$ is not properly contained in any larger smooth atlas.
>
> **Step 3 — Uniqueness.** Suppose $\mathcal{B}$ is another maximal smooth atlas containing $\mathcal{A}$. Then every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$ (since $\mathcal{B}$ is smooth and $\mathcal{A} \subseteq \mathcal{B}$), hence in $\overline{\mathcal{A}}$ by definition. So $\mathcal{B} \subseteq \overline{\mathcal{A}}$. By maximality of $\mathcal{B}$, $\mathcal{B} = \overline{\mathcal{A}}$.
>
> *Proof of (b).* Suppose $\overline{\mathcal{A}} = \overline{\mathcal{B}}$. Then $\mathcal{A} \cup \mathcal{B} \subseteq \overline{\mathcal{A}}$, which is a smooth atlas. So $\mathcal{A} \cup \mathcal{B}$, as a sub-collection of a smooth atlas whose domains cover $M$, is itself a smooth atlas.
>
> Conversely, suppose $\mathcal{A} \cup \mathcal{B}$ is a smooth atlas. Then every chart of $\mathcal{B}$ is smoothly compatible with every chart of $\mathcal{A}$ (since both lie in the smooth atlas $\mathcal{A} \cup \mathcal{B}$). So $\mathcal{B} \subseteq \overline{\mathcal{A}}$, and by the same argument $\mathcal{A} \subseteq \overline{\mathcal{B}}$. The maximal atlas containing both $\mathcal{A}$ and $\mathcal{B}$ is then both $\overline{\mathcal{A}}$ and $\overline{\mathcal{B}}$ — by uniqueness from (a), $\overline{\mathcal{A}} = \overline{\mathcal{B}}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Topology — refining a covering.** A standard topological technique is to *refine* an open cover — replace it with a (locally) finer open cover with better properties. The same idea recurs here: a smooth atlas may be replaced by an equivalent atlas with charts of more convenient shape (coordinate balls, regular coordinate balls), and the smooth-structure equivalence makes this refinement valid. Lee Proposition 1.19 (every smooth manifold has a basis of regular coordinate balls) is essentially an application of this theorem.

**Algebra — Zorn's lemma and maximal objects.** The argument of Lee 1.17 is constructive — we exhibit $\overline{\mathcal{A}}$ directly — but it could alternatively be proved by Zorn's lemma: the set of smooth atlases containing $\mathcal{A}$, ordered by inclusion, has chains with upper bounds (the union of a chain of smooth atlases is a smooth atlas), so a maximal element exists. The constructive approach avoids Zorn and is cleaner. Compare with the construction of maximal [[Def - Ideal|ideals]] in a [[Def - Ring|ring]], where Zorn is essential.

**Differential equations — equivalence of solution methods.** Many problems in ODEs can be approached by different parametrizations of the solution space; the choice of parametrization corresponds to a chart, and two parametrizations are "compatible" in our sense iff the change of parametrization is smooth. The smooth structure of the solution manifold is invariant under this choice — much like Lee 1.17.

**Algebraic geometry — schemes and affine open covers.** A scheme is locally affine; the choice of affine open cover is the analogue of a smooth atlas. Two affine open covers give the *same* scheme iff their union is also a covering by affine open sets — the analogue of part (b). The categorical pattern is identical.

---

# Bridges

- **[[Def - Smooth Atlas and Smooth Structure]]** — this theorem is the bridge between the two equivalent formulations of "smooth structure" (equivalence class of atlases vs. maximal atlas). The maximal-atlas formulation is the one we use in practice, and this theorem justifies it.

- **Sheaf-theoretic formulation of smooth structure** — the maximal atlas is equivalent to the *sheaf* of smooth functions $C^\infty_M$ on $M$. A chart $(U, \varphi) \in \overline{\mathcal{A}}$ is precisely an open set $U$ together with a local isomorphism $(U, C^\infty_M|_U) \cong (\widehat{U}, C^\infty_{\widehat{U}})$ in the category of locally ringed spaces. Hence the maximal atlas is the entire sheaf-theoretic structure of $M$.

- **[[Thm - The Inverse Function Theorem]]** — by Corollary C.36 of Lee, a smooth injective map with nonsingular Jacobian at every point is a diffeomorphism onto its image. This is the *practical test* for whether two charts are smoothly compatible: compute the Jacobian of the transition function and check that it is nonsingular. The inverse function theorem powers this verification.

- **The Smooth Manifold Chart Lemma (Lee 1.35)** — when starting from a *set* with maps to $\mathbb{R}^n$ rather than from an already-topologized manifold, the chart lemma manufactures both topology and smooth structure simultaneously, and this theorem (Lee 1.17) is what extends the chart-lemma atlas to a maximal atlas. The two theorems together are the "smooth structure constructor" toolkit.

---

# Unlocked by This

> [!tip] Smooth Charts and Coordinate-Independent Definitions *(from this chapter onwards)*
> Once a smooth structure is in place, every later definition (smooth function, smooth map, tangent vector, vector field, differential form, integral) is *coordinate-independent* — defined in terms of the maximal smooth atlas, equivalently any representative. This is the structural reason every theorem of differential geometry takes the form "such-and-such is well-defined on $M$ regardless of the chart."

> [!tip] The Sheaf $C^\infty_M$ as the Smooth Structure *(from Algebraic Geometry / Differential Geometry)*
> The smooth structure on $M$ can be encoded entirely by the sheaf $C^\infty_M$ of smooth real-valued functions. Two manifolds $M$ and $N$ are diffeomorphic iff there is an isomorphism of locally ringed spaces $(M, C^\infty_M) \cong (N, C^\infty_N)$. This is the *sheaf-theoretic* formulation of smooth structure, and it is the gateway to algebraic-geometric techniques in differential geometry.
