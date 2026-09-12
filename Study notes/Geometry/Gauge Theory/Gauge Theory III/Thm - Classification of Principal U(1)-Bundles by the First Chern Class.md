---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - First Chern Class via the Classifying Map"
  - "Thm - Generic Sections are Transverse to the Zero Section"
  - "Thm - Homogeneity Lemma for Connected Manifolds"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Thm - Clutching Construction for Bundles over a Closed Manifold"
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Def - Constructions on Representations"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth, Hausdorff, second-countable, **compact** manifold, and all bundles are smooth. The circle group is $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$, acting on principal bundles on the **right** (series convention). A **complex line bundle** $L \to M$ is a complex vector bundle of rank one; a **Hermitian line bundle** is such an $L$ with a smoothly varying Hermitian inner product $\langle\cdot,\cdot\rangle$ on its fibres (see [[Def - Complex Vector Bundle and Hermitian Structure]]). A **principal $U(1)$-bundle** $P \to M$ is a principal bundle for $U(1)$; its associated Hermitian line bundle is $P \times_{\varrho_1} \mathbb{C}$, where $\varrho_1 : U(1) \to GL(1,\mathbb{C})$, $\varrho_1(\lambda)v = \lambda v$, is the standard one-dimensional representation ([[Def - Associated Bundle]], [[Def - Constructions on Representations]]).

We write $\underline{\mathbb{C}} = M \times \mathbb{C}$ for the trivial line bundle; $L_1 \otimes L_2$ for the tensor product line bundle, $L^{\vee} = \operatorname{Hom}(L; \underline{\mathbb{C}})$ for the dual, and $\overline{L}$ for the conjugate bundle (the same underlying smooth real bundle with the conjugate complex structure); these are the fibrewise constructions of [[Def - Operations on Vector Bundles and Pull-Back Bundles]]. The symbol $\operatorname{Pic}(M)$ denotes the set of isomorphism classes $[L]$ of complex line bundles over $M$; by the line-bundle/$U(1)$-bundle dictionary recalled below it is the same set as the isomorphism classes of principal $U(1)$-bundles and of Hermitian line bundles.

We write $H^k_{dR}(M)$ for the [[Def - de Rham Cohomology|de Rham cohomology]] of $M$ with real coefficients and $h^* : H^k_{dR}(M) \to H^k_{dR}(M')$ for the map induced by a smooth $h : M' \to M$. The **topological first Chern class** $c_1^{\mathrm{top}}(P) := -f_P^*[\omega_N] \in H^2_{dR}(M)$ is the pulled-back positively normalised generator $[\omega_N]$ of $H^2_{dR}(\mathbb{CP}^N)$ along a classifying map $f_P : M \to \mathbb{CP}^N$ (the minus sign is the series convention); the **degree** $\deg(P) := w(g) \in \mathbb{Z}$ of a bundle over a closed oriented surface is the [[Thm - Winding Number of a Map from the Circle to U(1)|winding number]] $w(g)$ of a clutching function $g : \partial D \cong S^1 \to U(1)$. Both are defined, and shown independent of every choice, on [[Def - First Chern Class via the Classifying Map]]; we recall them at each point of use. The **tautological bundle** $\mathcal{O}(-1) \to \mathbb{CP}^N$ is the line bundle whose fibre over $[z]$ is the line $\mathbb{C}\cdot z$ (see [[Def - The Hopf Bundle]]). We write $\Sigma$ for a closed, connected, oriented surface, $D \subset \Sigma$ for an embedded closed disk with interior $D^\circ$ and boundary circle $S := \partial D$, and $\Sigma' := \Sigma \setminus D^\circ$ for the complementary compact surface-with-boundary, $\partial\Sigma' = S$.

> [!warning] Convention: this series proves the $U(1)$ case by clutching, not by the classical route
> Haydys proves the surface classification (part (C) below) by the classical topological route: a map $\Sigma \to \mathbb{CP}^\infty$ is deformed into the $2$-skeleton $\mathbb{CP}^1$ by **cellular approximation**, and $[\Sigma; \mathbb{CP}^1] = [\Sigma; S^2] \cong \mathbb{Z}$ by the **Hopf degree theorem**. Cellular approximation and the Hopf degree theorem are not proved and not used in this series. In their place we give a direct differential-topological proof: a line bundle over a surface is trivial off a disk, and a clutching function on the boundary circle has exactly one invariant, its winding number. The two routes attach the same integer to a bundle — the winding number of the clutching function equals the degree of the classifying map into $S^2 = \mathbb{CP}^1$ — but only the clutching proof is carried out here.

> [!warning] Convention: $\operatorname{Pic}(M)$ in place of $H^2(M;\mathbb{Z})$
> The sources write the classification of line bundles as $\operatorname{Pic}(M) \cong H^2(M; \mathbb{Z})$ (via $[M; \mathbb{CP}^\infty] \cong H^2(M; \mathbb{Z})$). Singular cohomology is available only from chapter XII, so this series works with the group $\operatorname{Pic}(M)$ itself and with de Rham classes plus the integrality established below; the identification with $H^2(M;\mathbb{Z})$ is neither proved nor used before chapter XII. Everything the later chapters need — the group structure, the first Chern class, and the fact that the degree is a complete invariant over a surface — is proved here in these terms.

---

# Statement

> **Theorem (classification of principal $U(1)$-bundles).** Let $M$ be a compact manifold and $\operatorname{Pic}(M)$ the set of isomorphism classes of principal $U(1)$-bundles over $M$, equivalently of Hermitian line bundles over $M$.
>
> **(A) Group structure and classifying-map bijection.** Tensor product of line bundles makes $\operatorname{Pic}(M)$ an abelian group, with identity the trivial bundle $[\underline{\mathbb{C}}]$ and with the dual (equivalently the conjugate) bundle $[L^{\vee}] = [\overline{L}]$ inverse to $[L]$. The assignment $P \mapsto [f_P]$ of a bundle to the homotopy class of a classifying map is a bijection $\operatorname{Pic}(M) \to [M; \mathbb{CP}^\infty]$.
>
> **(B) Properties of the first Chern class.** The map $c_1^{\mathrm{top}} : \operatorname{Pic}(M) \to H^2_{dR}(M)$ is well defined on isomorphism classes and satisfies
> $$c_1^{\mathrm{top}}(\underline{\mathbb{C}}) = 0, \qquad c_1^{\mathrm{top}}(L^{\vee}) = -\,c_1^{\mathrm{top}}(L), \qquad c_1^{\mathrm{top}}(h^*L) = h^*\, c_1^{\mathrm{top}}(L)$$
> for every smooth $h : M' \to M$ and every complex line bundle $L \to M$.
>
> **(C) The surface case.** If $M = \Sigma$ is a closed connected oriented surface, then the degree
> $$\deg : \operatorname{Pic}(\Sigma) \longrightarrow \mathbb{Z}$$
> is a group isomorphism. Explicitly: every principal $U(1)$-bundle over $\Sigma$ is trivial over the complement of a point, hence is a clutching bundle $P_g$; the degree satisfies $\deg(P_1 \otimes P_2) = \deg P_1 + \deg P_2$; for every $d \in \mathbb{Z}$ there is a bundle of degree $d$; and $\deg P = 0$ forces $P$ trivial.

Part (C) makes $\operatorname{Pic}(\Sigma) \cong \mathbb{Z}$ for every closed connected oriented surface, of any genus: the degree is the sole invariant of a line bundle over a surface.

The following is **not part of the theorem** and is proved later; it is stated here as a forward reference. **In chapter VI, on [[Thm - First Chern Class of a Line Bundle from Curvature]], one proves that for a Hermitian line bundle with a compatible connection $\nabla$ one has $c_1^{\mathrm{top}}(L) = \big[\tfrac{i}{2\pi} F_\nabla\big]$, that $\deg P = \int_\Sigma c_1^{\mathrm{top}}(P)$ for a surface, and that $c_1^{\mathrm{top}}(L_1 \otimes L_2) = c_1^{\mathrm{top}}(L_1) + c_1^{\mathrm{top}}(L_2)$ for every base $M$.** The additivity of $c_1^{\mathrm{top}}$ in full generality needs the curvature description; on a surface it is recovered here from the additivity of the degree in part (C).

Finally a **scope remark**, not a theorem and not used before chapter XII: the identification $\operatorname{Pic}(M) \cong H^2(M; \mathbb{Z})$, obtained from $[M; \mathbb{CP}^\infty] \cong H^2(M; \mathbb{Z})$, requires singular cohomology and is neither proved nor used in this series; Haydys' $H^2(M; \mathbb{Z})$-valued Chern class is recovered here only in the de Rham forms of parts (A)–(C).

---

# Motivation

A principal $U(1)$-bundle, or equivalently a complex line bundle, is the simplest bundle that can be nontrivial, and it is the bundle that gauge theory meets first: it is the arena of electromagnetism, where the connection is the electromagnetic potential and its curvature the field strength, and it is the local model for every complex vector bundle after a reduction of the structure group. The classification question is therefore basic: given a manifold $M$, how many line bundles does it carry, and what tells them apart? The answer this theorem gives has three layers, matching the three parts of the statement.

The first layer is algebraic. Line bundles are not merely a set; they can be multiplied by the tensor product and inverted by the dual, and the trivial bundle is a unit. So the isomorphism classes form an abelian group $\operatorname{Pic}(M)$, and to classify line bundles is to compute this group. Part (A) establishes that the group exists and identifies its underlying set with homotopy classes of maps into the infinite projective space $\mathbb{CP}^\infty$, the classifying space of $U(1)$; the group law records that line bundles combine, and the classifying-map bijection records that each is a homotopy class of maps to one universal object.

The second layer is a numerical invariant blind to isomorphism. Part (B) exhibits the first Chern class $c_1^{\mathrm{top}}$, a cohomology class attached to each bundle, and lists the three structural properties every characteristic class must have: it vanishes on the trivial bundle, it changes sign under duality, and it is natural under pullback. These three properties are what make $c_1^{\mathrm{top}}$ *usable*: they let one compute the Chern class of a bundle built from simpler ones, and they let one detect nontriviality by finding a single manifold and a single map on which the class fails to vanish.

The third layer is the completeness of the invariant in the simplest interesting dimension. Over a closed oriented surface — a sphere, a torus, a surface of higher genus — part (C) says the first Chern class, read as an integer through the degree, is a *complete* invariant: two line bundles over a surface are isomorphic if and only if their degrees agree, and every integer is achieved. This is the sharpest form of the classification, and it is the form the later chapters lean on: it is what makes the degree of a line bundle over a Riemann surface a well-defined integer, what pins the tautological bundle $\mathcal{O}(-1)$ over $\mathbb{CP}^1 = S^2$ to degree $-1$, and what underlies the counting of flat $U(1)$-connections in chapter V.

---

# Sources and Targets

**Sources (Input Broadening).**

The theorem's literal input is a principal $U(1)$-bundle over a compact manifold. The classification becomes powerful because several problems that do not mention line bundles secretly produce one.

The first disguised source is **a nowhere-zero complex-valued quantity defined up to phase**: a section of a Hermitian line bundle. Whenever a physical or geometric problem attaches to each point of $M$ a complex number well defined only up to a unit multiple — a wavefunction's phase, an order parameter, a choice of square root — the data is a section of a line bundle, and the bundle's degree obstructs choosing the phase globally. The non-obvious bridge is that "a complex quantity defined up to $U(1)$" is exactly the associated bundle $P \times_{\varrho_1} \mathbb{C}$ of a $U(1)$-bundle, so the classification applies. *Example problem:* on a closed surface, decide whether a smoothly varying complex line of "allowed phases" admits a global nowhere-zero section; part (C) answers it by computing the degree, and $\deg \ne 0$ is the obstruction.

The second disguised source is **a rank-two oriented real vector bundle over a surface**. Such a bundle carries a fibrewise rotation by ninety degrees — a complex structure — turning it into a complex line bundle ([[Def - Complex Vector Bundle and Hermitian Structure]]), so its classification is part (C). The bridge is the identification of oriented real planes with complex lines. *Example problem:* classify the oriented rank-two subbundles of a trivial bundle over $\Sigma$, or count the oriented plane fields; the degree, equal to the Euler number, is the answer, and the tangent bundle $T\Sigma$ realises the degree $\chi(\Sigma) = 2 - 2\mathrm{genus}$.

The third disguised source is **a smooth map into a manifold that is homotopy equivalent to $\mathbb{CP}^\infty$, or a cocycle valued in $U(1)$**. A Čech one-cocycle with values in $U(1)$ — a system of transition functions $g_{\alpha\beta} : U_{\alpha\beta} \to U(1)$ satisfying the cocycle condition — reconstructs a line bundle ([[Thm - Principal Bundles are Classified by Cocycles]]), so any gluing datum of this shape has a well-defined Chern class. The bridge is the cocycle reconstruction theorem. *Example problem:* given an explicit set of $U(1)$-valued transition functions on a surface, compute the degree of the resulting bundle by reading off the winding number of the single transition function on a two-set cover, without ever exhibiting the total space.

**Targets (Output Amplification).**

Combined with further ingredients, the classification produces sharper statements.

Combine part (C) with the **tautological bundle** $\mathcal{O}(-1) \to \mathbb{CP}^1 = S^2$ and a computed clutching function. Its transition function on the equator is $z/|z|$, of winding number one; with the series' complex orientation this gives $\deg \mathcal{O}(-1) = -1$ (worked in [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]]). The payoff is a concrete nontrivial generator of $\operatorname{Pic}(S^2) \cong \mathbb{Z}$ against which every other line bundle over $S^2$ is measured, and the anchor for the whole orientation-and-sign ledger of the series.

Combine parts (B) and (C) with **Chern–Weil theory** (chapter VI). The curvature of a unitary connection represents $c_1^{\mathrm{top}}$, so the integer $\deg P$ becomes the integral $\int_\Sigma \tfrac{i}{2\pi} F_\nabla$ of a differential form. The payoff is that a *topological* invariant is computed by an *analytic* integral, the prototype of every index theorem: the number of zeros of a generic section, the degree, and a curvature integral all coincide.

Combine part (C) with **flat connections** (chapter V). Once the bundle is classified, one asks which bundles admit a flat connection; over a surface the flat $U(1)$-bundles are exactly the degree-zero bundles, and their flat connections are parametrised by the character variety $\operatorname{Hom}(\pi_1(\Sigma), U(1))$. The payoff is the entry point to the moduli theory of flat connections, where the degree selects the topological type on which the moduli space lives.

---

# Why Is It True

Set aside the machinery and picture a line bundle $L$ over a closed surface $\Sigma$. A line bundle is nearly trivial: the only way it can fail to be a product is concentrated in an arbitrarily small region. To see this, take any smooth section $s$ of $L$. Generic sections of a rank-two bundle over a two-dimensional base vanish only at isolated points, finitely many of them, because the zero set has expected dimension $\dim\Sigma - \operatorname{rank} L = 2 - 2 = 0$. Away from those points the section is nowhere zero, and a nowhere-zero section of a line bundle *is* a trivialisation. So $L$ is trivial except at a handful of points. Now slide all those points, by a diffeomorphism that does not change the isomorphism type of the bundle, into a single small disk $D$. The bundle is then trivial over $\Sigma \setminus D^\circ$ and trivial over $D$, and it is completely described by how the two trivialisations disagree on the circle $\partial D$: a single map $g : \partial D \to U(1)$, the clutching function.

Everything now reduces to maps from a circle to the circle group, and such maps have exactly one invariant, the winding number — the net number of times $g$ runs around $U(1)$. This integer is the degree. Two clutching functions give isomorphic bundles precisely when they differ by boundary values of maps defined on $D$ or on $\Sigma \setminus D^\circ$; but such boundary values wind zero times, because a map that extends over a disk cannot wind, and neither can the boundary value of a map defined on the surface with the disk removed. So the winding number, taken modulo those trivial changes, *is* the winding number, and it is a complete invariant.

> **The mechanism in one sentence: a line bundle over a surface is trivial off a disk, so it is glued from two trivial pieces by a single map of the boundary circle into $U(1)$, and such a map has just one invariant — its winding number — which is the degree.**

The group law and its compatibility with the degree are then transparent. Tensoring two line bundles multiplies their clutching functions pointwise (transition functions of a tensor product multiply), and the winding number of a product of circle maps is the sum of the winding numbers because $U(1)$ is abelian. Hence the degree is additive, so it is a homomorphism; it is surjective because $z \mapsto z^d$ winds $d$ times; and it is injective because a degree-zero clutching function winds zero times, so it extends over the disk, which is exactly the condition for the glued bundle to be trivial. The three properties of part (B) inherit from the definition of $c_1^{\mathrm{top}}$ as a pulled-back cohomology class: it vanishes on the trivial bundle because that bundle's classifying map is constant and a constant map kills a positive-degree class; it changes sign under conjugation because complex conjugation reverses the orientation of $\mathbb{CP}^N$ and so negates the generator; and it is natural because pullback of bundles composes classifying maps.

---

# What Makes This Hard

The single non-obvious step is realising that a line bundle over a surface is trivial off a disk, and that this needs three separate inputs, not one: that a *generic* section has only finitely many zeros (transversality and the easy Sard theorem), that the zeros can be *gathered into one disk without changing the bundle* (the homogeneity lemma together with the isotopy-invariance of bundles), and that a bundle trivial on the two pieces is *reconstructed by its clutching function* (the clutching theorem). Omitting any one leaves a gap: a random section can vanish on a curve rather than at points; zeros scattered across the surface do not give a two-piece decomposition; and even two trivial pieces must be glued correctly. The common error is to treat "trivial off a disk" as obvious or to prove it only for the sphere, where a clutching decomposition is visible, and to miss that the homogeneity lemma is what reduces an arbitrary surface to that visible case. A second subtlety is bookkeeping the residual freedom in the clutching function: one must check that the two ways of changing a trivialisation — over the disk and over its complement — both contribute winding number zero, and that the orientations on $\partial D$ induced from the two sides, though opposite, do not disturb the vanishing.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For (A), verify the abelian-group axioms for tensor product on isomorphism classes, the inverse being the dual, and quote the classifying-map bijection. For (B), read the three properties off the definition $c_1^{\mathrm{top}} = -f^*[\omega_N]$ using homotopy invariance, the coordinate fact $c^*\omega_N = -\omega_N$ under conjugation, and functoriality of pullback. For (C), show every bundle over $\Sigma$ is a clutching bundle (generic section, gather zeros, glue), then use the winding number to prove the degree is an additive, surjective, injective map to $\mathbb{Z}$.

**Subgoal decomposition:**

1. **$\operatorname{Pic}(M)$ is an abelian group.** Tensor product is well defined on isomorphism classes, associative, commutative, has unit $[\underline{\mathbb{C}}]$, and $[L]^{-1} = [L^{\vee}]$.
   - *Hint:* Every axiom is a natural fibrewise isomorphism of vector spaces; the only one needing thought is $L \otimes L^{\vee} \cong \underline{\mathbb{C}}$, the evaluation pairing.
   - *Why needed:* Part (A), and the very sense of "$\deg$ is a group homomorphism".

2. **Conjugation negates the generator.** For complex conjugation $c : \mathbb{CP}^N \to \mathbb{CP}^N$, $c^*[\omega_N] = -[\omega_N]$; and a constant map pulls $[\omega_N]$ back to zero.
   - *Hint:* Lift to $S^{2N+1}$ and use $\pi^*\omega_N = \tfrac1\pi \sum dx_j \wedge dy_j$; conjugation sends $y_j \mapsto -y_j$.
   - *Why needed:* Parts (B)(i) and (B)(ii).

3. **Every bundle over $\Sigma$ is a clutching bundle.** There is a disk $D$ with $P$ trivial over $\Sigma \setminus D^\circ$ and over $D$, hence $P \cong P_g$ for a clutching function $g : \partial D \to U(1)$.
   - *Hint:* Take a generic section with finitely many zeros; move the zeros into $D^\circ$ by a diffeomorphism isotopic to the identity; the normalised section trivialises off the disk.
   - *Why needed:* The whole of (C); it is the step Haydys does by cellular approximation.

4. **Tensor product multiplies clutching functions.** $P_{g_1} \otimes P_{g_2} \cong P_{g_1 g_2}$.
   - *Hint:* On the two-set cover the transition function of a tensor product of line bundles is the product of the transition functions.
   - *Why needed:* Additivity of the degree, hence "$\deg$ is a homomorphism".

5. **The degree is additive, surjective, injective.** $\deg(P_1 \otimes P_2) = \deg P_1 + \deg P_2$; $z \mapsto z^d$ realises degree $d$; $\deg P = 0 \Rightarrow P$ trivial.
   - *Hint:* Winding number is additive under pointwise product; $w(z^d) = d$; $w(g) = 0$ makes $g$ extend over the disk, which trivialises $P_g$.
   - *Why needed:* Part (C): a homomorphism that is onto and has trivial kernel is an isomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: Tensor product makes $\operatorname{Pic}(M)$ an abelian group with inverse the dual
> **Statement:** The set $\operatorname{Pic}(M)$ of isomorphism classes of complex line bundles over $M$, with the operation $[L_1] \cdot [L_2] := [L_1 \otimes L_2]$, is an abelian group: the operation is well defined on isomorphism classes, associative and commutative, has identity $[\underline{\mathbb{C}}]$, and each $[L]$ has inverse $[L^{\vee}]$. Moreover $[L^{\vee}] = [\overline{L}]$ for a Hermitian line bundle.
>
> **Hint:** Each axiom is a canonical fibrewise isomorphism of one-dimensional vector spaces, natural hence smooth; the inverse axiom is the evaluation pairing $L \otimes L^{\vee} \to \underline{\mathbb{C}}$.
>
> **Why needed:** It is part (A) and gives meaning to the homomorphism claim in part (C).
>
> > [!note]- Full proof
> > All bundles here are line bundles over $M$, and $\otimes$, $\operatorname{Hom}$, and the natural isomorphisms below are the fibrewise constructions of [[Def - Operations on Vector Bundles and Pull-Back Bundles]], which are smooth because they are polynomial in the entries of any local frames.
> >
> > **Well-definedness on isomorphism classes.** Suppose $\varphi_i : L_i \to L_i'$ are bundle isomorphisms ($i = 1, 2$). Then $\varphi_1 \otimes \varphi_2 : L_1 \otimes L_2 \to L_1' \otimes L_2'$, defined fibrewise by $(\varphi_1 \otimes \varphi_2)(v \otimes w) = \varphi_1(v) \otimes \varphi_2(w)$, is a bundle isomorphism (its fibrewise inverse is $\varphi_1^{-1} \otimes \varphi_2^{-1}$, and it is smooth in any local frames since $\varphi_1, \varphi_2$ are). Hence $L_1 \cong L_1'$ and $L_2 \cong L_2'$ imply $L_1 \otimes L_2 \cong L_1' \otimes L_2'$, so $[L_1] \cdot [L_2]$ depends only on the classes.
> >
> > **Commutativity.** The fibrewise flip $v \otimes w \mapsto w \otimes v$ is a natural isomorphism $L_1 \otimes L_2 \to L_2 \otimes L_1$ of vector spaces in each fibre, smooth in frames, hence a bundle isomorphism. Thus $[L_1] \cdot [L_2] = [L_2] \cdot [L_1]$.
> >
> > **Associativity.** The canonical associator $(u \otimes v) \otimes w \mapsto u \otimes (v \otimes w)$ is a natural fibrewise isomorphism $(L_1 \otimes L_2) \otimes L_3 \to L_1 \otimes (L_2 \otimes L_3)$, hence a bundle isomorphism, giving $([L_1]\cdot[L_2])\cdot[L_3] = [L_1]\cdot([L_2]\cdot[L_3])$.
> >
> > **Identity.** The scalar-multiplication map $v \otimes \lambda \mapsto \lambda v$ is a natural fibrewise isomorphism $L \otimes \underline{\mathbb{C}} \to L$ (its inverse is $v \mapsto v \otimes 1$), so $[L] \cdot [\underline{\mathbb{C}}] = [L]$; commutativity gives the other side.
> >
> > **Inverse.** We claim the evaluation pairing
> > $$\mathrm{ev} : L \otimes L^{\vee} \longrightarrow \underline{\mathbb{C}}, \qquad \mathrm{ev}(v \otimes \phi) = \phi(v),$$
> > is a bundle isomorphism. It is fibrewise linear and, in a local frame $e$ of $L$ with dual frame $e^{\vee}$ of $L^{\vee}$ (so $e^{\vee}(e) = 1$), it sends the local frame $e \otimes e^{\vee}$ of $L \otimes L^{\vee}$ to the constant section $e^{\vee}(e) = 1$ of $\underline{\mathbb{C}}$ (since $\mathrm{ev}$). A bundle map between line bundles that carries a local frame to a nowhere-zero section is a fibrewise isomorphism there, and this holds on every trivialising neighbourhood, so $\mathrm{ev}$ is a global bundle isomorphism (it is smooth because $\phi \mapsto \phi(v)$ is bilinear in frame coordinates). Hence $[L] \cdot [L^{\vee}] = [\underline{\mathbb{C}}]$, so $[L^{\vee}]$ is inverse to $[L]$.
> >
> > **Dual equals conjugate.** For a Hermitian line bundle $L$ with metric $\langle\cdot,\cdot\rangle$ (Hermitian, conjugate-linear in the second slot in the series convention), the map $\Phi : L \to L^{\vee}$, $\Phi(v) = \langle \cdot, v\rangle$, is conjugate-linear in $v$ and a fibrewise bijection (in a unit local frame $e$, $\Phi(e) = \langle\cdot,e\rangle = e^{\vee}$, a frame of $L^{\vee}$), smooth in frames. A conjugate-linear bundle isomorphism $L \to L^{\vee}$ is precisely a complex-linear bundle isomorphism $\overline{L} \to L^{\vee}$, by the definition of the conjugate bundle $\overline{L}$. Hence $\overline{L} \cong L^{\vee}$ and $[L^{\vee}] = [\overline{L}]$.
> >
> > **Conclusion.** All group axioms hold and the operation is abelian, with identity $[\underline{\mathbb{C}}]$ and inverse $[L]^{-1} = [L^{\vee}] = [\overline{L}]$. Therefore $\operatorname{Pic}(M)$ is an abelian group under tensor product.

> [!note]- Lemma 2: Complex conjugation negates the generator of $H^2_{dR}(\mathbb{CP}^N)$
> **Statement:** Let $c : \mathbb{CP}^N \to \mathbb{CP}^N$, $c([z]) = [\overline{z}]$, be complex conjugation, and let $[\omega_N] \in H^2_{dR}(\mathbb{CP}^N)$ be the positively normalised generator, characterised by $\pi^*\omega_N = \tfrac1\pi \sum_{j=0}^N dx_j \wedge dy_j$ on $S^{2N+1}$ (with $z_j = x_j + i y_j$) and $\int_{\mathbb{CP}^1}\omega_1 = 1$. Then $c^*[\omega_N] = -[\omega_N]$. Consequently, if $\kappa : M \to \mathbb{CP}^N$ is a constant map then $\kappa^*[\omega_N] = 0$.
>
> **Hint:** Lift $c$ to the conjugation $\tilde{c}(z) = \overline{z}$ of $S^{2N+1}$, which sends $y_j \mapsto -y_j$; use that $\pi^*$ is injective on forms.
>
> **Why needed:** Parts (B)(i) ($c_1^{\mathrm{top}}(\underline{\mathbb{C}}) = 0$) and (B)(ii) ($c_1^{\mathrm{top}}(L^{\vee}) = -c_1^{\mathrm{top}}(L)$).
>
> > [!note]- Full proof
> > We use the description of $[\omega_N]$ from [[Thm - The de Rham Cohomology of Complex Projective Space]] — restated: *$H^2_{dR}(\mathbb{CP}^N) \cong \mathbb{R}$ is generated by $[\omega_N]$, where $\omega_N$ is the unique closed $2$-form with $\pi^*\omega_N = \tfrac1\pi \sum_{j=0}^{N} dx_j \wedge dy_j$ on $S^{2N+1} \xrightarrow{\pi} \mathbb{CP}^N$, and $\pi^* : \Omega^2(\mathbb{CP}^N) \to \Omega^2(S^{2N+1})$ is injective because $\pi$ is a surjective submersion.*
> >
> > **The lift of conjugation.** Let $\tilde{c} : S^{2N+1} \to S^{2N+1}$, $\tilde{c}(z_0, \dots, z_N) = (\overline{z_0}, \dots, \overline{z_N})$. Conjugation of a unit vector is a unit vector, so $\tilde{c}$ maps the sphere to itself, and $c \circ \pi = \pi \circ \tilde{c}$ because conjugating a vector conjugates its complex line (definition of $c$).
> >
> > **The coordinate computation.** Writing $z_j = x_j + i y_j$, the map $\tilde{c}$ sends $x_j \mapsto x_j$ and $y_j \mapsto -y_j$, so $\tilde{c}^*(dx_j) = dx_j$ and $\tilde{c}^*(dy_j) = -dy_j$, whence
> > $$\tilde{c}^*\!\left(\tfrac1\pi \sum_{j=0}^N dx_j \wedge dy_j\right) = \tfrac1\pi \sum_{j=0}^N dx_j \wedge (-dy_j) = -\,\tfrac1\pi \sum_{j=0}^N dx_j \wedge dy_j \qquad \text{(pullback is linear and commutes with } \wedge \text{).}$$
> >
> > **Descending to the base.** Using $c \circ \pi = \pi \circ \tilde{c}$ and functoriality of pullback,
> > $$\pi^*\big(c^*\omega_N\big) = (c \circ \pi)^*\omega_N = (\pi \circ \tilde{c})^*\omega_N = \tilde{c}^*\big(\pi^*\omega_N\big) = \tilde{c}^*\!\left(\tfrac1\pi \sum_j dx_j \wedge dy_j\right) = -\,\tfrac1\pi \sum_j dx_j \wedge dy_j = \pi^*(-\omega_N),$$
> > where the last equality is the defining property of $\omega_N$ read with a minus sign. Since $\pi^*$ is injective, $c^*\omega_N = -\omega_N$ as forms, hence $c^*[\omega_N] = -[\omega_N]$ in cohomology.
> >
> > **The constant-map clause.** A constant map $\kappa$ factors through a point $\{p\} \hookrightarrow \mathbb{CP}^N$, so $\kappa^* = (\text{inclusion of } p)^* \circ (\text{map to point})^*$; the pullback of any positive-degree form to a point is zero, hence $\kappa^*[\omega_N] = 0$. (Equivalently: a constant map is smoothly homotopic to any constant, and $[\omega_N]$ restricted to a point of the $0$-dimensional space $H^2(\mathrm{pt}) = 0$ vanishes.)
> >
> > **Conclusion.** Conjugation negates the generator, $c^*[\omega_N] = -[\omega_N]$, and a constant map annihilates it. $\blacksquare$

> [!note]- Lemma 3: Every principal $U(1)$-bundle over a closed surface is a clutching bundle
> **Statement:** Let $\Sigma$ be a closed connected oriented surface and $P \to \Sigma$ a principal $U(1)$-bundle. Then there is an embedded closed disk $D \subset \Sigma$ such that $P$ is trivial over $\Sigma' = \Sigma \setminus D^\circ$ and over $D$; consequently $P \cong P_g$ for some smooth clutching function $g : S = \partial D \to U(1)$.
>
> **Hint:** A generic section of the associated real rank-two bundle has finitely many zeros; move them into $D^\circ$ by a diffeomorphism isotopic to the identity; normalise the nowhere-zero part.
>
> **Why needed:** It is the geometric heart of (C) and replaces Haydys' cellular-approximation step.
>
> > [!note]- Full proof
> > Let $L := P \times_{\varrho_1} \mathbb{C}$ be the associated Hermitian line bundle ([[Def - Associated Bundle]]); as a real bundle it has rank two, and its complex structure orients it. Fix once and for all an embedded closed disk $D \subset \Sigma$ (one exists: take the image of the closed unit ball under a chart).
> >
> > **Step 1 — a section with finitely many zeros.** By [[Thm - Generic Sections are Transverse to the Zero Section]] — restated: *for a real vector bundle $E \to M$ of rank $r$ over a compact $m$-manifold there is a section transverse to the zero section, and when $r = m$ such a section has finitely many zeros, each nondegenerate (the vertical derivative $D_x s : T_x M \to E_x$ an isomorphism)* — applied with $E = L$ (as a real bundle), $r = 2 = m = \dim\Sigma$, there is a smooth section $s$ of $L$ transverse to the zero section, with a finite zero set $Z = \{p_1, \dots, p_k\}$.
> >
> > **Step 2 — gather the zeros into the disk.** Since $\Sigma$ is connected and $\dim\Sigma = 2 \ge 2$, by [[Thm - Homogeneity Lemma for Connected Manifolds]] — restated: *any finite subset of a connected manifold of dimension at least two can be carried into any prescribed coordinate disk by a diffeomorphism smoothly isotopic to the identity* — there is a diffeomorphism $\phi : \Sigma \to \Sigma$, isotopic to the identity, with $\phi^{-1}(Z) \subset D^\circ$. By [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]] clauses (d) and (e) — restated: *if $h : M \to M$ is a diffeomorphism isotopic to the identity then $h^*E \cong E$ for every principal or vector bundle $E$* — we have $\phi^* L \cong L$. The pulled-back section $\phi^*s$ (defined by $(\phi^*s)(x) = s(\phi(x))$ under the canonical identification $(\phi^*L)_x = L_{\phi(x)}$) vanishes exactly on $\phi^{-1}(Z) \subset D^\circ$. Replacing $L$ by the isomorphic $\phi^*L$ changes neither the isomorphism class of $P$ nor anything to be proved, so **we may assume $s$ vanishes only inside $D^\circ$.**
> >
> > **Step 3 — trivialise off the disk.** On $\Sigma'$ the section $s$ is nowhere zero, so $u := s/\lvert s\rvert$ (norm from the Hermitian metric) is a smooth section of the unit-sphere subbundle of $L|_{\Sigma'}$, that is, a section of the principal $U(1)$-bundle $P|_{\Sigma'}$. By [[Thm - Sections of a Principal Bundle and Triviality]] — restated: *a principal bundle is trivial over an open set if and only if it admits a smooth section there* — the bundle $P$ is trivial over $\Sigma'$.
> >
> > **Step 4 — trivialise over the disk.** The disk $D$ is diffeomorphic to a closed ball, hence contractible. By [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]] clause (c) — restated: *every principal bundle over a contractible manifold, in particular over a closed disk, is trivial* — the bundle $P$ is trivial over $D$.
> >
> > **Step 5 — assemble the clutching description.** The group $U(1)$ is connected, and $P$ is trivial over both $\Sigma'$ and $D$. By [[Thm - Clutching Construction for Bundles over a Closed Manifold]] clause (b) — restated: *a principal $G$-bundle over a closed manifold $X = D \cup_{S} \Sigma'$ that is trivial over $\Sigma' = X \setminus D^\circ$ and over $D$ is isomorphic to the clutching bundle $P_g$ of some smooth transition function $g : S \to G$ read on a collar of $S = \partial D$* — the bundle $P$ is isomorphic to $P_g$ for a smooth clutching function $g : S \to U(1)$.
> >
> > **Conclusion.** With $D$ the chosen disk, $P$ is trivial over $\Sigma'$ and over $D$, and $P \cong P_g$. $\blacksquare$

> [!note]- Lemma 4: The tensor product multiplies clutching functions
> **Statement:** Let $\Sigma = D \cup_S \Sigma'$ as above, and let $P_{g_1}, P_{g_2}$ be the clutching bundles of smooth $g_1, g_2 : S \to U(1)$ on the common cover $\{D, \Sigma'\}$. Then the tensor-product bundle satisfies $P_{g_1} \otimes P_{g_2} \cong P_{g_1 g_2}$, where $g_1 g_2$ is the pointwise product in $U(1)$; equivalently, the associated line bundles satisfy $L_1 \otimes L_2 \cong P_{g_1 g_2} \times_{\varrho_1} \mathbb{C}$.
>
> **Hint:** On a two-set cover the transition function of a tensor product of line bundles is the product of the transition functions.
>
> **Why needed:** It converts the group law on $\operatorname{Pic}(\Sigma)$ into pointwise multiplication of clutching functions, which the winding number turns into addition.
>
> > [!note]- Full proof
> > Work with the associated line bundles $L_i = P_{g_i} \times_{\varrho_1} \mathbb{C}$, since tensor product and the group law live there and pass back to $U(1)$-bundles by the dictionary of Lemma 1 and [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group]]. Use the open cover $\mathcal{U} = \{U_0, U_1\}$ with $U_0$ a neighbourhood of $\Sigma'$ and $U_1$ a neighbourhood of $D$, on which each $P_{g_i}$ carries the two global sections built from the trivialisations of Lemma 3; the single transition function of $P_{g_i}$ on the overlap $U_0 \cap U_1$ (a collar of $S$) is $g_i$, by [[Thm - Principal Bundles are Classified by Cocycles]] — restated: *a principal $U(1)$-bundle with local sections $s_\alpha$ over $\{U_\alpha\}$ is determined up to isomorphism by the smooth transition functions $g_{\alpha\beta} : U_{\alpha\beta} \to U(1)$ with $s_\beta = s_\alpha \, g_{\alpha\beta}$, and two cocycles give isomorphic bundles if and only if they are cohomologous.*
> >
> > **Transition functions of a tensor product.** Let $e^{(i)}_0, e^{(i)}_1$ be the unit local frames of $L_i$ over $U_0, U_1$ corresponding to the sections above, so that on the overlap $e^{(i)}_1 = e^{(i)}_0 \, g_i$ (the frame changes by the transition function, a scalar in $U(1) \subset \mathbb{C}^\times$). Then $e^{(1)}_\alpha \otimes e^{(2)}_\alpha$ is a local frame of $L_1 \otimes L_2$ over $U_\alpha$, and on the overlap
> > $$e^{(1)}_1 \otimes e^{(2)}_1 = \big(e^{(1)}_0 g_1\big) \otimes \big(e^{(2)}_0 g_2\big) = \big(e^{(1)}_0 \otimes e^{(2)}_0\big)\, g_1 g_2 \qquad \text{(scalars pull out of each tensor factor and, being scalars, multiply).}$$
> > Hence the transition function of $L_1 \otimes L_2$ on the cover $\mathcal{U}$ is the pointwise product $g_1 g_2 : U_0 \cap U_1 \to U(1)$, restricting to $g_1 g_2$ on the collar of $S$.
> >
> > **Reassembly.** By the cocycle classification theorem just quoted, the line bundle with transition function $g_1 g_2$ on the cover $\{U_0, U_1\}$ is $P_{g_1 g_2} \times_{\varrho_1} \mathbb{C}$, the associated line bundle of the clutching bundle of $g_1 g_2$. Therefore $L_1 \otimes L_2 \cong P_{g_1 g_2} \times_{\varrho_1}\mathbb{C}$, and passing back through the dictionary, $P_{g_1} \otimes P_{g_2} \cong P_{g_1 g_2}$.
> >
> > **Conclusion.** Tensoring the bundles multiplies their clutching functions. $\blacksquare$

> [!note]- Lemma 5: The winding number as a complete invariant of clutching functions
> **Statement:** With $\Sigma = D \cup_S \Sigma'$ and $S \cong S^1$: (i) for smooth $g_1, g_2 : S \to U(1)$, $w(g_1 g_2) = w(g_1) + w(g_2)$; (ii) the map $g_d : S \to U(1)$, $g_d(e^{i\theta}) = e^{i d \theta}$, has $w(g_d) = d$ for every $d \in \mathbb{Z}$; (iii) if $w(g) = 0$ then the clutching bundle $P_g$ is trivial.
>
> **Hint:** Parts (i), (ii) are the winding-number theorem; for (iii), $w(g) = 0$ makes $g$ extend over the disk, which is exactly the clutching triviality criterion.
>
> **Why needed:** It supplies additivity, surjectivity, and triviality of the kernel for the degree in (C).
>
> > [!note]- Full proof
> > We quote [[Thm - Winding Number of a Map from the Circle to U(1)]] — restated: *for smooth $g : S^1 \to U(1)$ the winding number $w(g) = \tfrac1{2\pi i}\int_{S^1} g^{-1}\,dg$ is an integer equal to $\deg g$; it is additive, $w(g_1 g_2) = w(g_1) + w(g_2)$; it is a homotopy invariant; $w(g) = 0$ if and only if $g$ extends to a smooth map $D^2 \to U(1)$; and $w(z \mapsto z^k) = k$* — and [[Thm - Clutching Construction for Bundles over a Closed Manifold]] clause (d) — restated: *the clutching bundle $P_g$ over $X = D \cup_S \Sigma'$ is trivial if and only if $g = (a|_S)\,(b|_S)$ for smooth maps $a : \Sigma' \to G$ and $b : D \to G$.*
> >
> > **(i) Additivity.** Immediate from the additivity clause of the winding-number theorem: $w(g_1 g_2) = w(g_1) + w(g_2)$ (identifying $S \cong S^1$; the identification is fixed once and shared by all clutching functions on this cover).
> >
> > **(ii) Surjectivity of the invariant.** By the last clause of the winding-number theorem, $w(g_d) = w(z \mapsto z^d) = d$; every integer is attained.
> >
> > **(iii) Kernel is trivial.** Suppose $w(g) = 0$. By the winding-number theorem, $g$ extends to a smooth map $b : D \to U(1)$ with $b|_S = g$. Take $a : \Sigma' \to U(1)$ to be the constant map $a \equiv 1$, so $a|_S \equiv 1$. Then
> > $$(a|_S)\,(b|_S) = 1 \cdot g = g \qquad \text{(pointwise product in the abelian group } U(1)\text{),}$$
> > which is exactly the triviality criterion of clutching clause (d) with $G = U(1)$. Hence $P_g$ is trivial.
> >
> > **Conclusion.** The winding number is additive, surjects onto $\mathbb{Z}$ through the power maps, and vanishes precisely on clutching functions of trivial bundles. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a compact manifold. We prove parts (A), (B), (C) in turn. Throughout, "line bundle" means complex line bundle, and the dictionary between complex line bundles, Hermitian line bundles, and principal $U(1)$-bundles (each a bijection on isomorphism classes) is that of [[Def - First Chern Class via the Classifying Map]] and [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group]]; we use it silently to pass between $P$ and $L = P \times_{\varrho_1} \mathbb{C}$.
>
> **Part (A) — group structure and bijection.**
>
> By **Lemma 1**, $\operatorname{Pic}(M)$ with tensor product is an abelian group, with identity $[\underline{\mathbb{C}}]$ and inverse $[L]^{-1} = [L^{\vee}] = [\overline{L}]$. For the bijection with $[M; \mathbb{CP}^\infty]$ we quote [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]] — restated: *for a compact manifold $M$, the assignment sending a principal $U(1)$-bundle $P$ to the homotopy class $[f_P]$ of a classifying map $f_P : M \to \mathbb{CP}^N$ with $f_P^*\mathcal{O}(-1) \cong P \times_{\varrho_1}\mathbb{C}$ (stabilised over $N$) is a bijection from isomorphism classes of principal $U(1)$-bundles onto $[M; \mathbb{CP}^\infty] = \varinjlim_N [M; \mathbb{CP}^N]$.* This is exactly the map $P \mapsto [f_P]$ and it is a bijection. (No group structure on $[M; \mathbb{CP}^\infty]$ is asserted; the claim is a bijection of sets, one side of which is a group.) This proves (A).
>
> **Part (B) — properties of $c_1^{\mathrm{top}}$.**
>
> That $c_1^{\mathrm{top}}$ is well defined on isomorphism classes — independent of classifying map, of $N$, and of the Hermitian structure — is proved on [[Def - First Chern Class via the Classifying Map]]; we use it and the definition $c_1^{\mathrm{top}}(P) = -f_P^*[\omega_N]$.
>
> **Vanishing on the trivial bundle.** The trivial bundle $\underline{\mathbb{C}}$ has a nowhere-zero global section, hence a constant classifying map $\kappa$ (it is pulled back from a point). By **Lemma 2**, $\kappa^*[\omega_N] = 0$, so
> $$c_1^{\mathrm{top}}(\underline{\mathbb{C}}) = -\kappa^*[\omega_N] = 0.$$
>
> **Behaviour under duality.** By Lemma 1, $L^{\vee} \cong \overline{L}$, so it suffices to compute $c_1^{\mathrm{top}}(\overline{L})$. If $f : M \to \mathbb{CP}^N$ classifies $L$, then $c \circ f$ classifies $\overline{L}$, where $c$ is complex conjugation: indeed the classifying map of [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]] is built from unitary frames, $f(m) = \{(\langle s_0(m), v\rangle, \dots, \langle s_N(m), v\rangle) : v \in L_m\}$, and conjugating the complex structure of $L$ (which is what passing to $\overline{L}$ does) conjugates every inner product, sending the line $f(m)$ to its conjugate line $\overline{f(m)} = c(f(m))$; hence $f_{\overline{L}} = c \circ f$. Therefore, using functoriality of pullback and **Lemma 2** ($c^*[\omega_N] = -[\omega_N]$),
> $$c_1^{\mathrm{top}}(L^{\vee}) = c_1^{\mathrm{top}}(\overline{L}) = -(c \circ f)^*[\omega_N] = -f^*\big(c^*[\omega_N]\big) = -f^*\big(-[\omega_N]\big) = f^*[\omega_N] = -\,c_1^{\mathrm{top}}(L).$$
>
> **Naturality under pullback.** Let $h : M' \to M$ be smooth and $L \to M$ a line bundle with classifying map $f : M \to \mathbb{CP}^N$, so $f^*\mathcal{O}(-1) \cong L$. Then $(f \circ h)^*\mathcal{O}(-1) = h^*(f^*\mathcal{O}(-1)) \cong h^*L$ (pullback of bundles is functorial), so $f \circ h$ classifies $h^*L$, that is $f_{h^*L} = f \circ h$. Hence
> $$c_1^{\mathrm{top}}(h^*L) = -(f \circ h)^*[\omega_N] = -h^*\big(f^*[\omega_N]\big) = h^*\big(-f^*[\omega_N]\big) = h^*\,c_1^{\mathrm{top}}(L),$$
> using functoriality of pullback on cohomology and its linearity. This proves (B).
>
> **Part (C) — the surface case.**
>
> Let $\Sigma$ be a closed connected oriented surface and $D \subset \Sigma$ a fixed embedded closed disk with $S = \partial D$, $\Sigma' = \Sigma \setminus D^\circ$. The degree $\deg(P) = w(g)$ is well defined on isomorphism classes by [[Def - First Chern Class via the Classifying Map]] — restated: *the winding number of a clutching function of $P$ is independent of the two trivialisations and of the disk, because changing them multiplies $g$ by boundary values of maps on $D$ and on $\Sigma'$, each of winding number zero.* We show $\deg$ is a surjective, injective homomorphism.
>
> **Step 0 — the domain is meaningful.** By **Lemma 3**, every $P \in \operatorname{Pic}(\Sigma)$ is trivial over $\Sigma'$ and over $D$, hence is a clutching bundle $P_g$; so $\deg(P) = w(g)$ is defined for every class, and by moving zeros into the *fixed* disk $D$ (Lemma 3, Step 2) all bundles may be described by clutching functions on the *same* cover $\{D, \Sigma'\}$.
>
> **Step 1 — $\deg$ is a homomorphism.** Let $P_1, P_2 \in \operatorname{Pic}(\Sigma)$, described on the common cover as $P_1 \cong P_{g_1}$, $P_2 \cong P_{g_2}$. By **Lemma 4**, $P_1 \otimes P_2 \cong P_{g_1 g_2}$, so by the definition of the degree and **Lemma 5(i)**,
> $$\deg(P_1 \otimes P_2) = w(g_1 g_2) = w(g_1) + w(g_2) = \deg(P_1) + \deg(P_2).$$
> Thus $\deg : \operatorname{Pic}(\Sigma) \to \mathbb{Z}$ is a homomorphism of abelian groups (from tensor product to addition).
>
> **Step 2 — $\deg$ is surjective.** Fix $d \in \mathbb{Z}$ and let $g_d : S \cong S^1 \to U(1)$, $g_d(e^{i\theta}) = e^{i d\theta}$. By **Lemma 5(ii)**, $w(g_d) = d$, so the clutching bundle $P_{g_d}$ (which exists by [[Thm - Clutching Construction for Bundles over a Closed Manifold]] clause (a)) has $\deg(P_{g_d}) = d$. Every integer is a degree.
>
> **Step 3 — $\deg$ is injective.** Since $\deg$ is a homomorphism (Step 1), it suffices to show its kernel is trivial. Suppose $\deg(P) = 0$. Write $P \cong P_g$ (Step 0); then $w(g) = 0$, and by **Lemma 5(iii)** the clutching bundle $P_g$ is trivial, so $[P] = [\underline{\mathbb{C}}]$ is the identity of $\operatorname{Pic}(\Sigma)$. Hence $\ker\deg = \{[\underline{\mathbb{C}}]\}$, and a homomorphism with trivial kernel is injective.
>
> **Step 4 — conclude.** The map $\deg : \operatorname{Pic}(\Sigma) \to \mathbb{Z}$ is a homomorphism (Step 1) that is surjective (Step 2) and injective (Step 3), hence a group isomorphism. The four explicit assertions of (C) are Step 0 (every $P$ is a clutching bundle, trivial off a point since the disk shrinks to any point in $D^\circ$), Step 1 (additivity), Step 2 (existence for each $d$), and Step 3 ($\deg P = 0 \Rightarrow P$ trivial). This proves (C).
>
> Parts (A), (B), (C) together establish the theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemann surfaces and holomorphic line bundles (complex geometry).** On a compact Riemann surface, holomorphic line bundles form a group under tensor product, and forgetting the holomorphic structure lands in $\operatorname{Pic}(\Sigma)$ as classified here; the degree of a holomorphic line bundle equals the number of zeros minus poles of a meromorphic section. The theorem applies because a holomorphic line bundle is in particular a smooth complex line bundle, and the exercise — showing the degree of the canonical bundle $K_\Sigma$ is $2\mathrm{genus} - 2$ — is non-obvious because it must reconcile the topological degree of part (C) with the Riemann–Roch count, the two being forced equal by the completeness of the invariant.

**Dirac monopoles and quantised charge (mathematical physics).** A magnetic monopole on $S^2$ is a $U(1)$-connection on a line bundle over the sphere whose curvature integrates to the magnetic charge; Dirac's quantisation is precisely the statement that the charge is $2\pi$ times the degree, an integer. The theorem applies because the monopole's bundle is a $U(1)$-bundle over $\Sigma = S^2$, and the exercise — deriving charge quantisation from the classification — is non-obvious because the physical input (a singular potential defined on two patches) is exactly a clutching function, and its winding number is the charge.

**Vortices and the Ginzburg–Landau functional (partial differential equations).** A finite-energy section of a line bundle over a surface has isolated zeros (vortices), and the total vortex number is the degree. The theorem applies through the associated bundle of the order parameter, and the exercise — showing that a configuration with a prescribed net vortex number cannot be deformed to the vacuum unless that number is zero — is non-obvious because it turns a variational obstruction (energy cannot be lowered to zero) into the topological statement $\deg P \ne 0 \Rightarrow P$ nontrivial from part (C).

---

# Bridges

- **The tautological bundle and the orientation ledger.** The bundle $\mathcal{O}(-1) \to \mathbb{CP}^1 = S^2$ is the concrete generator of $\operatorname{Pic}(S^2) \cong \mathbb{Z}$. Its clutching function on the equator is $z/|z|$ (from the explicit local sections of [[Def - The Hopf Bundle]]), of winding number one, and with the series' complex orientation of $\mathbb{CP}^1$ this yields $\deg\mathcal{O}(-1) = -1$; the full sign bookkeeping is carried out in [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]]. This is the point at which the abstract classification acquires a normalisation the rest of the series can compute against.

- **From degree to curvature integral (Chern–Weil).** Chapter VI proves on [[Thm - First Chern Class of a Line Bundle from Curvature]] that a unitary connection's curvature represents $c_1^{\mathrm{top}}$, so that $\deg P = \int_\Sigma \tfrac{i}{2\pi} F_\nabla$. Composing that identity with part (C) gives a three-way equality — the number of zeros of a generic section, the winding-number degree, and a curvature integral all agree — which is the one-dimensional prototype of the Chern–Weil theorem and, beyond it, of the index theorem.

- **From classification to flat connections (chapter V).** Once the degree is a complete invariant, one identifies which bundles admit flat connections: over a surface these are exactly the degree-zero bundles, and their flat connections are governed by the monodromy representation $\pi_1(\Sigma) \to U(1)$ studied on the flat-connection pages of chapter V. The bridge is that a flat $U(1)$-connection forces the curvature integral, hence the degree, to vanish.

- **The cocycle picture and tensor products.** The additivity of the degree rests on the fact that transition functions of a tensor product multiply, a corollary of the cocycle classification [[Thm - Principal Bundles are Classified by Cocycles]]. This is the same mechanism that gives $\operatorname{Pic}(M)$ its group law in Čech-cohomological terms, and it is the reason the first Chern class is additive once curvature is available.

---

# Unlocked by This

> [!tip] Degree of a line bundle over a Riemann surface *(from Complex Geometry)*
> The topological degree classified here is the smooth shadow of the holomorphic degree; the Riemann–Roch theorem computes the dimension of the space of sections from it, and the completeness of the invariant (part (C)) is what lets one speak of "the" line bundle of a given degree.

> [!tip] The Picard group and its higher analogues *(from Algebraic Topology)*
> Part (A) presents $\operatorname{Pic}(M)$ as an abelian group in bijection with $[M; \mathbb{CP}^\infty]$; when singular cohomology becomes available in chapter XII this is upgraded to $\operatorname{Pic}(M) \cong H^2(M; \mathbb{Z})$, the first instance of the general principle that characteristic classes are pullbacks of universal classes on classifying spaces.
