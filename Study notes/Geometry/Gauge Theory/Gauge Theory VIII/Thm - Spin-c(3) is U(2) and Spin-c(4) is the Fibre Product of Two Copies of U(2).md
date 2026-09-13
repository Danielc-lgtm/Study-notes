---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Spin Structure and Spin-c Structure"
  - "Thm - Spin Groups in Dimensions Three and Four via Quaternions"
  - "Def - SU(2) Action on Spinors"
  - "Def - Quaternions"
tags: [geometry, gauge-theory, spin-geometry, lie-groups]
---

# Notation

Throughout, $n$ is a positive integer, and all Lie groups act on the left where not otherwise stated. We use the following standing objects of the series.

The **spin group** $Spin(n) \subset \mathrm{Cl}^0(\mathbb{R}^n)^\times$ is the subgroup of even products of unit vectors, and $\xi : Spin(n) \to SO(n)$ is the double cover $\xi(a)u = aua^{-1}$ (equivalently the twisted adjoint, which agrees with $\xi$ on even elements), with $\ker\xi = \{\pm 1\}$; the element $-1 \in Spin(n)$ is central. In the two dimensions this page treats, the [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|quaternionic model]] gives concrete descriptions: $Spin(3) \cong Sp(1)$ and $Spin(4) \cong Sp(1) \times Sp(1)$, where $Sp(1) = \{q \in \mathbb{H} : |q| = 1\}$ is the group of unit [[Def - Quaternions|quaternions]].

The **special unitary group** $SU(2) = \{A \in M_2(\mathbb{C}) : A^\dagger A = I,\ \det A = 1\}$ and the **unitary group** $U(2) = \{B \in M_2(\mathbb{C}) : B^\dagger B = I\}$ are the matrix groups of $2\times 2$ complex unitary matrices with determinant $1$, respectively arbitrary unimodular determinant; $A^\dagger = \bar A^{\mathsf T}$ is the conjugate transpose. The circle group $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ is embedded in $U(2)$ as the central scalar matrices $z \mapsto zI$. We write $[[Def - Determinant|\det]] : U(2) \to U(1)$ for the determinant, a group homomorphism with image $U(1)$ (every unitary matrix has $|\det| = 1$, and $\det(zI) = z^2$ realises every value).

We use the identification $Sp(1) \cong SU(2)$ throughout. Concretely, viewing $\slashed{S} = \mathbb{H}$ as a complex vector space through right multiplication by $\bar i = -i$ (which commutes with left quaternion multiplication by associativity, hence makes left multiplication complex-linear), the algebra isomorphism
$$a + bi + cj + dk \;\longmapsto\; \begin{pmatrix} a + bi & c + di \\ -c + di & a - bi \end{pmatrix}$$
of [[Def - Quaternions|the quaternions]] with a subalgebra of $M_2(\mathbb{C})$ carries $\mathbb{H}$ isomorphically onto that subalgebra and restricts to a Lie group isomorphism $Sp(1) \xrightarrow{\ \cong\ } SU(2)$ (see [[Def - SU(2) Action on Spinors|the fundamental representation of SU(2)]]). Under it, left multiplication by a unit quaternion $q$ on $\slashed{S} = \mathbb{H} \cong \mathbb{C}^2$ is the fundamental action of the matrix $A \in SU(2)$ on $\mathbb{C}^2$. From here on we freely write $Spin(3) \cong SU(2)$ and $Spin(4) \cong SU(2) \times SU(2)$.

The **complex spinᶜ group** and its two standard homomorphisms are recalled from the definition page:

![[Def - Spin Structure and Spin-c Structure#Spinc group anchor]]

For reference on this page: $Spin^c(n) := \big(Spin(n) \times U(1)\big)/\{\pm 1\}$, where $\{\pm 1\}$ is the two-element subgroup $\{(1,1), (-1,-1)\}$ embedded diagonally (using the central $-1 \in Spin(n)$ and $-1 \in U(1)$); the class of $(g, z)$ is written $[g, z]$, so $[g, z] = [-g, -z]$. The map $\rho_0 : Spin^c(n) \to SO(n)$, $\rho_0([g,z]) = \xi(g)$, and the map $\rho_{\det} : Spin^c(n) \to U(1)$, $\rho_{\det}([g,z]) = z^2$, are group homomorphisms fitting into the exact sequence (Haydys's equation (120))
$$1 \longrightarrow \{\pm 1\} \longrightarrow Spin^c(n) \xrightarrow{\ (\rho_0,\, \rho_{\det})\ } SO(n) \times U(1) \longrightarrow 1 .$$

We follow Haydys's Clifford sign convention $u \cdot u = -|u|^2$ throughout the chapter; it plays no direct role on this page, which is pure group theory once the quaternionic models of $Spin(3)$ and $Spin(4)$ are in hand.

> [!warning] Convention: the identification $Sp(1) = SU(2)$
> Haydys writes $Sp(1)$ for the unit quaternions and $SU(2)$ for the $2\times 2$ special unitary matrices, using the two names interchangeably (his footnote 3). They are the *same* Lie group under the explicit isomorphism displayed above, and the whole statement of this theorem is Haydys's Example 121 with $Sp(1)$ rewritten as $SU(2)$. We state and prove everything in $SU(2)$-matrix language, because the conclusion is a statement about the matrix groups $U(2)$; the quaternionic side is used only to import the models of $Spin(3)$ and $Spin(4)$.

---

# Statement

> **Theorem (spinᶜ groups in dimensions three and four).**
>
> **(a) Dimension three.** The map
> $$\Phi : Spin^c(3) = \big(SU(2) \times U(1)\big)/\{\pm 1\} \longrightarrow U(2), \qquad \Phi([A, z]) = zA,$$
> is a well-defined isomorphism of Lie groups. Under it:
> - $\rho_{\det} : U(2) \to U(1)$ becomes the determinant, $\rho_{\det}(B) = \det B$;
> - $\rho_0 : U(2) \to SO(3)$ becomes the natural projection $U(2) \twoheadrightarrow PU(2) = U(2)/\{zI : z \in U(1)\}$ followed by the isomorphism $PU(2) \cong SO(3)$ induced by the double cover $\alpha : SU(2) \to SO(3)$;
> - the exact sequence (120) reads
> $$1 \longrightarrow \{\pm I\} \longrightarrow U(2) \xrightarrow{\ (\rho_0,\, \det)\ } SO(3) \times U(1) \longrightarrow 1 .$$
>
> **(b) Dimension four.** The map
> $$\Psi : Spin^c(4) = \big(SU(2) \times SU(2) \times U(1)\big)/\{\pm 1\} \longrightarrow U(2) \times U(2), \qquad \Psi([(A_+, A_-), z]) = (zA_+,\, zA_-),$$
> is a well-defined isomorphism of Lie groups onto the **fibre product**
> $$U(2) \times_{U(1)} U(2) := \big\{ (B_+, B_-) \in U(2) \times U(2) : \det B_+ = \det B_- \big\} .$$
> Under it:
> - $\rho_{\det}(B_+, B_-) = \det B_+ = \det B_-$;
> - the two projections $\rho_\pm : Spin^c(4) \to U(2)$, $\rho_\pm([(A_+,A_-),z]) = zA_\pm$, become the coordinate projections $(B_+, B_-) \mapsto B_\pm$, and are surjective group homomorphisms with $\rho_{\det} = \det \circ \rho_\pm$;
> - the half-spinor representations $\slashed{S}^\pm$ of $Spin^c(4)$ are $\mathbb{C}^2$ with $Spin^c(4)$ acting through $\rho_\pm$ followed by the fundamental representation of $U(2)$.

The two parts are one phenomenon read in two dimensions: in each case the extra central circle of $Spin^c$ merges with the special unitary factor(s) of $Spin(n)$ to fill out the full unitary group $U(2)$, the merger being modulo the single shared element $-1$. Part (a) is the case of one $SU(2)$ factor; part (b) is the case of two, tied together by the requirement that both copies see the *same* circle, which is exactly the determinant condition $\det B_+ = \det B_-$.

---

# Motivation

The Seiberg–Witten equations are written on a spinᶜ four-manifold, and their unknowns are a connection on the determinant line bundle together with a section of the positive half-spinor bundle. To manipulate these objects concretely — to compute the differential of the Seiberg–Witten map, to see how a gauge transformation acts, to read off the curvature that enters the Weitzenböck identity — one must know the structure group $Spin^c(4)$ not as an abstract quotient but as an explicit matrix group with explicit representations. The abstract definition $Spin^c(n) = (Spin(n) \times U(1))/\{\pm 1\}$ is unusable for calculation: its elements are equivalence classes of pairs, and its spinor representation is defined by the formula $[g,z]\cdot s = z\rho(g)s$ that still refers to the abstract spin representation $\rho$.

This theorem removes the abstraction in the only two dimensions the series uses. It says that $Spin^c(3)$ is *literally* the unitary group $U(2)$, and $Spin^c(4)$ is *literally* the subgroup of $U(2) \times U(2)$ cut out by one determinant equation. Once this is known, everything downstream becomes matrix computation: a spinᶜ spinor is a pair of $\mathbb{C}^2$-valued objects, $\rho_{\det}$ is the determinant, and the central circle acts by scalar multiplication with a transparent weight. The half-spinor representations $\slashed{S}^\pm$, which the definition page could only name, are pinned down here as $\mathbb{C}^2$ with $U(2)$ acting fundamentally through the projection $\rho_\pm$; this is precisely the datum the Seiberg–Witten construction consumes.

There is a second reason the identification matters. The map $U(2) \hookrightarrow Spin^c(4)$ coming from part (b) — or rather the diagonal-type embedding it makes visible — is the group-theoretic shadow of the fact that an almost complex structure, that is, a reduction of the frame bundle to $U(2)$, determines a canonical spinᶜ structure. The unitary group is the structure group of a complex rank-two bundle; that it *is* $Spin^c(3)$, and sits inside $Spin^c(4)$, is why complex and almost-complex four-manifolds are automatically spinᶜ. Understanding the theorem is the first step to understanding that dictionary.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem is a bijection between two descriptions of one group, so the "source" question is: when does a problem hand you $Spin^c(3)$ or $Spin^c(4)$ in disguise, so that this theorem lets you replace it by a unitary matrix group you can compute in?

The first disguised source is **an almost complex structure, or a $U(2)$-structure, on a four-manifold.** A reduction of the oriented orthonormal frame bundle $\mathrm{Fr}_{SO}$ of a four-manifold to the subgroup $U(2) \subset SO(4)$ is by definition an almost complex structure compatible with the metric and orientation. The non-obvious bridge is that $U(2)$, sitting inside $Spin^c(4)$ by part (b) as $\{(B, \zeta I) : \det B = \zeta^2\}$ for a suitable circle-valued $\zeta$, lifts the frame bundle to a $Spin^c(4)$-bundle: the $U(2)$-structure *is* a spinᶜ structure, with determinant line the anticanonical line $\Lambda^{2,0}$. So a problem that presents an almost complex structure has secretly presented a spinᶜ structure, and part (b) is the conversion. *Example problem:* show that $\mathbb{CP}^2$, which carries a complex (hence $U(2)$-) structure, admits a spinᶜ structure although it is not spin — the $U(2)$-reduction lifts through $\rho_0 : U(2) \to SO(3)$-type data by this theorem, with no need for the Stiefel–Whitney obstruction to vanish.

The second disguised source is **a rank-two complex Hermitian bundle with a chosen square root of its determinant, or the pair of half-spinor bundles of a spinᶜ four-manifold.** Whenever one is handed two Hermitian rank-two bundles $E_+, E_-$ with $\det E_+ \cong \det E_-$, part (b) recognises the pair as an associated bundle of a principal $Spin^c(4)$-bundle, because the fibrewise data lands in the fibre product $U(2) \times_{U(1)} U(2)$. The non-obvious step is the matching-determinant condition: it is exactly the closure condition that makes the two $U(2)$-cocycles glue to a single $Spin^c(4)$-cocycle. *Example problem:* given the two half-spinor bundles $\slashed{S}^\pm$ of a spinᶜ structure, verify $\det \slashed{S}^+ \cong \det \slashed{S}^- \cong L_{\det}$ and reconstruct the structure group as $Spin^c(4)$.

The third disguised source is **a central extension of $SO(n) \times U(1)$ by $\mathbb{Z}/2$ realised by unitary matrices.** Any time a group $\Gamma$ is presented together with a two-to-one homomorphism onto $SO(3) \times U(1)$ whose kernel is central and whose restriction to a determinant-one subgroup double-covers $SO(3)$, the exact sequence (120) identifies $\Gamma$ with $Spin^c(3) = U(2)$. The bridge is the uniqueness of the connected double cover of $SO(3) \times U(1)$ with the prescribed restriction. *Example problem:* recognise the group of unit-determinant-times-scalar operators appearing in a physical spin-charge coupling as $U(2)$ by exhibiting the projection onto $SO(3) \times U(1)$ and its two-element kernel.

**Targets (Output Amplification)**

The bare conclusion is an isomorphism of groups. Combined with other structure it produces the working objects of Seiberg–Witten theory.

Combine the conclusion with **the classification of principal $U(1)$-bundles by the first Chern class.** Part (a)/(b) turn $\rho_{\det}$ into the determinant, so the determinant line bundle $L_{\det} = P \times_{\rho_{\det}} \mathbb{C}$ of a spinᶜ structure is $\det$ of the half-spinor bundle, and its isomorphism class is a class in $H^2(M;\mathbb{Z})$. The further result is that the set of spinᶜ structures becomes a torsor over $H^2(M;\mathbb{Z})$ (proved on [[Thm - Classification of Spin-c Structures|the classification page]]), because tensoring the $U(2)$-data by a line bundle shifts the determinant by its square — a statement one can only phrase once $\rho_{\det}$ is the determinant.

Combine the conclusion with **the representation theory of $U(2)$ on $\mathbb{C}^2$ and its exterior powers.** Because $\rho_\pm$ is a genuine homomorphism to $U(2)$ and $\slashed{S}^\pm = \mathbb{C}^2$ is the fundamental representation, the top exterior power $\Lambda^2 \slashed{S}^\pm = \mathbb{C}$ carries the determinant representation, i.e. $\rho_{\det}$. The payoff is the identification $\Lambda^2 \slashed{S}^\pm \cong L_{\det}$ of line bundles and the description of the quadratic map $\psi \mapsto \mu(\psi)$ of the Seiberg–Witten equations as a map into the imaginary self-dual two-forms via the traceless part of $\psi \otimes \psi^\dagger$; both are computations inside $U(2)$ made legitimate by this theorem.

Combine the conclusion with **the weight of the central circle.** Since $\rho_{\det}([g,z]) = z^2$ but the spinor action is $[g,z]\cdot s = z\rho(g)s$, the central circle acts on spinors with weight one and on the determinant line with weight two. The further result is the factor $\tfrac12$ in the variation of the spinᶜ Dirac operator with the connection on $L_{\det}$ (proved on [[Thm - Variation of the Twisted and Spin-c Dirac Operators with the Connection|the variation page]]) and the $2\,g^{-1}dg$ appearing in the gauge action in Seiberg–Witten theory: a change of the determinant connection by $a$ changes the spinor connection by $\tfrac12 a$, exactly because the circle one sees on $L_{\det}$ is the square of the one acting on spinors.

---

# Why Is It True

Forget the exact sequences and picture what a unitary matrix is. A matrix $B \in U(2)$ has a determinant $\det B$, a point on the unit circle. If $\det B$ happened to be $1$, then $B$ would be special unitary. It is not, in general — but it is only off by a scalar: pick any square root $z$ of $\det B$ on the circle, and $A := \bar z B$ has $\det A = \bar z^2 \det B = 1$, so $A$ is special unitary. Thus every unitary matrix factors as
$$B = z A, \qquad z \in U(1),\ A \in SU(2),$$
a scalar times a special unitary matrix. This is the polar-type decomposition, and it is the whole engine of the theorem.

> Every element of $U(2)$ is a circle-scalar times an $SU(2)$-matrix, and this factorisation is unique except for simultaneously flipping the signs of the scalar and of the matrix.

The sign ambiguity is forced and unremovable: if $z$ is one square root of $\det B$, then $-z$ is the other, and $-z$ goes with $A' = -A$, giving the same product $(-z)(-A) = zA = B$. So the honest statement is not "$U(2) = U(1) \times SU(2)$" — that would be false, because the two factors overlap in the two scalar matrices $\pm I$ — but "$U(2) = (U(1) \times SU(2))$ with $(z,A)$ and $(-z,-A)$ identified". That identification is exactly the diagonal $\{\pm 1\}$ in the definition of $Spin^c(3)$. The map $[A,z]\mapsto zA$ simply performs the multiplication, and the quotient by $\{\pm 1\}$ is there precisely to make the multiplication injective.

**The mechanism in one sentence: $U(2)$ is the special unitary group and the circle of scalars fused along the two matrices $\pm I$ they share, and the fusion is the diagonal $\{\pm 1\}$ that defines $Spin^c$.**

In dimension four the same thing happens twice, with one constraint. $Spin(4)$ is *two* copies of $SU(2)$, one acting on each half-spinor space. Attaching the central circle would naively give two independent copies of $U(2)$; but there is only *one* central circle in $Spin^c(4)$, shared by both factors, so the same scalar $z$ multiplies both $A_+$ and $A_-$. Two matrices $B_\pm = zA_\pm$ built from the *same* $z$ have the same determinant, $\det B_\pm = z^2$. Conversely, if two unitary matrices have equal determinant, that common value has a square root $z$ that reconstructs the shared scalar. So the image is not all of $U(2)\times U(2)$ but exactly the pairs with equal determinant — the fibre product over the determinant. The determinant equation is the visible trace of the single shared circle.

---

# What Makes This Hard

Three points trip people up. First, the factorisation $B = zA$ is *not* a direct product decomposition: the naive map $U(1)\times SU(2)\to U(2)$, $(z,A)\mapsto zA$, is two-to-one, not injective, and forgetting the quotient by $\{\pm 1\}$ gives a "theorem" with a factor-of-two error in every kernel computation. The quotient is the content, not a formality. Second, the equal-determinant condition in part (b) is easy to *state* and easy to overlook *why* it is exactly right: it is not an extra hypothesis one imposes but the precise image of a single circle acting diagonally, and one must check both that the image lands in the fibre product and that the whole fibre product is hit. Third, upgrading a bijective continuous homomorphism to an *isomorphism of Lie groups* is not automatic from set theory: a bijective smooth homomorphism can in principle fail to have smooth inverse. It does not here, but the reason — constancy of rank forced by homogeneity — has to be invoked, not assumed; skipping it leaves the manifold structure unmatched.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** In both parts, write down the multiplication map from the abstract quotient to the matrix group, check it is a well-defined homomorphism, then prove it is bijective using the polar-type factorisation $B = zA$ (with a shared $z$ in dimension four). Upgrade bijection to Lie isomorphism by the constant-rank argument. Finally read off $\rho_{\det}$, $\rho_0$/$\rho_\pm$ and the exact sequence by direct substitution.

**Subgoal decomposition:**

1. **Quotient is a Lie group; $\rho_0$, $\rho_{\det}$ well-defined.** Show $\{\pm 1\}$ is a closed central subgroup so the quotient is a Lie group, and that $\xi(g)$ and $z^2$ are unchanged under $(g,z)\mapsto(-g,-z)$.
   - *Hint:* $-1$ is central in $Spin(n)$ and in $U(1)$; $\xi(-1)=1$ and $(-z)^2=z^2$.
   - *Why needed:* Without this there is no group to map out of and no target for $\rho_0,\rho_{\det}$.

2. **Polar-type factorisation lemma.** Every $B\in U(2)$ is $zA$ with $z\in U(1)$, $A\in SU(2)$, $z^2=\det B$, unique up to $(z,A)\mapsto(-z,-A)$.
   - *Hint:* $\det B\in U(1)$ has a square root $z$; set $A=\bar z B$ and check $\det A=1$. For uniqueness compare two factorisations and take determinants.
   - *Why needed:* It is simultaneously the surjectivity and the injectivity of $\Phi$; applied with a shared $z$ it gives part (b).

3. **Bijective smooth homomorphism is a Lie isomorphism.** A smooth bijective homomorphism of Lie groups is a diffeomorphism.
   - *Hint:* Left translations force constant rank; a bijective constant-rank map is a local diffeomorphism everywhere, hence a diffeomorphism.
   - *Why needed:* It converts the set-level bijection into an isomorphism of Lie groups, which is the assertion.

4. **Read off $\rho_{\det}$ and the projections.** Substitute $B=zA$ into $z^2$ and into $\xi(g)$; substitute $(B_+,B_-)=(zA_+,zA_-)$ into the coordinate maps.
   - *Hint:* $z^2=\det B$; $\xi$ factors through $SU(2)/\{\pm I\}=PU(2)$.
   - *Why needed:* These are the explicit forms of the standard homomorphisms claimed in the statement.

5. **Identify $\slashed{S}^\pm$.** Combine the abstract action $[g,z]\cdot s=z\rho(g)s$ with the quaternionic model to see it is $B_\pm$ acting fundamentally.
   - *Hint:* On $\slashed{S}^\pm$, $\rho(g)$ is left multiplication by $q_\pm$, i.e. the $SU(2)$-matrix $A_\pm$; then $z\rho(g)=zA_\pm=B_\pm$.
   - *Why needed:* It pins down the half-spinor representations as $\mathbb{C}^2$ through $\rho_\pm$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $Spin^c(n)$ is a Lie group and $\rho_0$, $\rho_{\det}$ are well-defined homomorphisms
> **Statement:** The diagonal subgroup $\{\pm 1\} = \{(1,1),(-1,-1)\}$ of $Spin(n)\times U(1)$ is closed and central, so $Spin^c(n) = (Spin(n)\times U(1))/\{\pm 1\}$ is a Lie group with $[g,z][g',z']=[gg',zz']$. The maps $\rho_0([g,z])=\xi(g)$ and $\rho_{\det}([g,z])=z^2$ are well-defined group homomorphisms.
>
> **Hint:** Centrality of $-1\in Spin(n)$ and of $-1\in U(1)$; then $\xi(-g)=\xi(g)$ and $(-z)^2=z^2$.
>
> **Why needed:** It supplies the group structure on the source and the well-definedness of the two homomorphisms the theorem describes; it is Step 0 for both parts.
>
> > [!note]- Full proof
> > **The subgroup is closed and central.** The set $\{\pm 1\} = \{(1,1),(-1,-1)\}$ is finite, hence closed in the Lie group $Spin(n)\times U(1)$. Its two elements are central: $-1\in U(1)$ is central because $U(1)$ is abelian, and $-1\in Spin(n)$ is central by the [[Thm - Spin(n) inside the Clifford Algebra is a Double Cover of SO(n)|double-cover theorem]] (which shows $\ker\xi=\{\pm 1\}$ lies in the centre of $Spin(n)$; for $n=3,4$ this is immediate, since $-1$ corresponds to $-I\in SU(2)$, a central matrix). A product of central elements in the two factors is central in the direct product, so $(-1,-1)$ is central in $Spin(n)\times U(1)$; hence $\{\pm 1\}$ is a central, therefore normal, closed subgroup.
> >
> > **The quotient is a Lie group.** A closed normal subgroup $H$ of a Lie group $G$ has $G/H$ a Lie group with the quotient smooth structure (the quotient of a Lie group by a closed normal subgroup is a Lie group). Applying this with $G = Spin(n)\times U(1)$ and $H=\{\pm 1\}$ gives the Lie group $Spin^c(n)$, and the multiplication descends from the direct product: $[g,z][g',z']=[gg',zz']$.
> >
> > **$\rho_{\det}$ is well-defined and a homomorphism.** Define $\tilde\rho_{\det}:Spin(n)\times U(1)\to U(1)$ by $\tilde\rho_{\det}(g,z)=z^2$. This is a homomorphism (since $U(1)$ is abelian, $(zz')^2=z^2z'^2$), and it kills $\{\pm 1\}$ because $\tilde\rho_{\det}(-1,-1)=(-1)^2=1$. A homomorphism that is trivial on $H$ factors uniquely through $G/H$; the factored map is $\rho_{\det}([g,z])=z^2$, well-defined and a homomorphism.
> >
> > **$\rho_0$ is well-defined and a homomorphism.** Define $\tilde\rho_0:Spin(n)\times U(1)\to SO(n)$ by $\tilde\rho_0(g,z)=\xi(g)$. It is a homomorphism because $\xi$ is (double-cover theorem) and the $U(1)$-slot is ignored. It kills $\{\pm 1\}$ because $\tilde\rho_0(-1,-1)=\xi(-1)=1$ (as $-1\in\ker\xi$). Factoring through the quotient gives the well-defined homomorphism $\rho_0([g,z])=\xi(g)$. $\qquad\square$

> [!note]- Lemma 2: A smooth bijective homomorphism of Lie groups is a Lie group isomorphism
> **Statement:** Let $F : G \to H$ be a smooth homomorphism of Lie groups that is bijective as a map of sets. Then $F$ is a diffeomorphism, so $F^{-1}$ is smooth and $F$ is an isomorphism of Lie groups.
>
> **Hint:** Homogeneity ($F\circ L_g = L_{F(g)}\circ F$) forces $F$ to have the same rank at every point; a bijective constant-rank map is a diffeomorphism.
>
> **Why needed:** It upgrades the set-theoretic bijections $\Phi$, $\Psi$ (which we build by hand) to isomorphisms of Lie groups, which is what the theorem asserts.
>
> > [!note]- Full proof
> > **$F$ has constant rank.** For $g\in G$ let $L_g$ and $L_{F(g)}$ denote left translations on $G$ and $H$; these are diffeomorphisms. Because $F$ is a homomorphism, $F(gx)=F(g)F(x)$, i.e. $F\circ L_g = L_{F(g)}\circ F$. Differentiating at the identity $e\in G$ and using the chain rule,
> > $$(dF)_g \circ (dL_g)_e = (dL_{F(g)})_e \circ (dF)_e \qquad \text{(chain rule applied to } F\circ L_g = L_{F(g)}\circ F\text{)} .$$
> > Since $(dL_g)_e$ and $(dL_{F(g)})_e$ are linear isomorphisms (differentials of diffeomorphisms), the two sides show $\operatorname{rank}(dF)_g = \operatorname{rank}(dF)_e$ for every $g$. Thus $F$ has constant rank $r := \operatorname{rank}(dF)_e$.
> >
> > **The rank is full and $F$ is a local diffeomorphism.** By the [[Thm - The Rank Theorem|constant-rank theorem]] — if a smooth map has constant rank $r$ near a point, there are charts in which it looks like $(x_1,\dots,x_m)\mapsto(x_1,\dots,x_r,0,\dots,0)$ — a constant-rank map with $r<\dim G$ is locally non-injective (it collapses the $x_{r+1},\dots,x_m$ directions), and one with $r<\dim H$ is locally non-surjective (its image lies in the slice $x_{r+1}=\dots=0$). Our $F$ is globally injective and globally surjective, hence locally so at every point; therefore $r=\dim G$ and $r=\dim H$, so $\dim G=\dim H=r$ and $(dF)_g$ is a linear isomorphism for every $g$. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $F$ is a local diffeomorphism at every point.
> >
> > **Conclusion.** A bijective local diffeomorphism is a diffeomorphism: it is a continuous bijection with a local smooth inverse near every point, and these local inverses agree on overlaps (they all invert the single global bijection $F$), so they glue to a global smooth inverse $F^{-1}$. Hence $F$ is a diffeomorphism, and being also a group isomorphism it is an isomorphism of Lie groups. $\qquad\square$

> [!note]- Lemma 3: Polar-type factorisation in $U(2)$
> **Statement:** Every $B \in U(2)$ can be written $B = zA$ with $z \in U(1)$ and $A \in SU(2)$, and necessarily $z^2 = \det B$. The factorisation is unique up to the simultaneous sign change $(z, A) \mapsto (-z, -A)$: if $zA = z'A'$ with $z,z'\in U(1)$ and $A,A'\in SU(2)$, then $(z',A') = (z,A)$ or $(z',A') = (-z,-A)$.
>
> **Hint:** For existence, take a square root $z$ of $\det B$ on the unit circle and set $A = \bar z B$. For uniqueness, compare two factorisations and take determinants to pin $z' = \pm z$.
>
> **Why needed:** It is at once the surjectivity and the injectivity of $\Phi$ in part (a), and — applied to two matrices sharing one square root $z$ — of $\Psi$ in part (b).
>
> > [!note]- Full proof
> > **Existence.** Let $B\in U(2)$. Since $B$ is unitary, $|\det B| = 1$, so $d := \det B \in U(1)$. Writing $d = e^{i\phi}$ with $\phi\in\mathbb{R}$, the number $z := e^{i\phi/2}$ satisfies $z\in U(1)$ and $z^2 = e^{i\phi} = d$ (square roots exist on the circle). Set $A := \bar z B = z^{-1}B$ (as $z^{-1}=\bar z$ for $|z|=1$). Then
> > $$A^\dagger A = (\bar z B)^\dagger(\bar z B) = z\,\bar z\, B^\dagger B = |z|^2 I = I \qquad \text{(} B \text{ unitary, } |z|=1\text{)},$$
> > so $A$ is unitary, and
> > $$\det A = \det(\bar z B) = \bar z^{\,2}\det B = \bar z^{\,2} z^2 = |z|^4 = 1 \qquad \text{(} \det(\lambda I \cdot B)=\lambda^2\det B \text{ for } 2\times 2\text{; } z^2=\det B\text{)} .$$
> > Hence $A\in SU(2)$ and $B = zA$. Taking determinants of $B=zA$ gives $\det B = z^2\det A = z^2$, confirming $z^2=\det B$.
> >
> > **Uniqueness up to simultaneous sign.** Suppose $zA = z'A'$ with $z,z'\in U(1)$ and $A,A'\in SU(2)$. Then $A = (z^{-1}z')A'$, so taking determinants,
> > $$1 = \det A = (z^{-1}z')^2\det A' = (z^{-1}z')^2 \qquad \text{(} \det A = \det A' = 1\text{)} .$$
> > Thus $(z^{-1}z')^2 = 1$, i.e. $z^{-1}z' = \pm 1$, so $z' = \pm z$. If $z' = z$, then $A' = (z^{-1}z')^{-1}A = A$; wait — from $zA=z'A'=zA'$ we get $A'=A$. If $z' = -z$, then $zA = z'A' = -zA'$ gives $A' = -A$. In both cases $(z',A')\in\{(z,A),(-z,-A)\}$. $\qquad\square$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $Spin^c(3) = (SU(2)\times U(1))/\{\pm 1\}$ and $Spin^c(4) = (SU(2)\times SU(2)\times U(1))/\{\pm 1\}$ are Lie groups (using $Spin(3)\cong SU(2)$ and $Spin(4)\cong SU(2)\times SU(2)$ from the [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|quaternionic model]], under which $\xi$ becomes $\alpha$ respectively $\beta$), and $\rho_0,\rho_{\det}$ are well-defined homomorphisms. Here the diagonal $\{\pm 1\}$ is $\{(I,1),(-I,-1)\}$ in dimension three and $\{((I,I),1),((-I,-I),-1)\}$ in dimension four, since the nontrivial central element $-1\in Spin(4)$ corresponds to $(-I,-I)$ (the [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|quaternionic model]] gives $\ker\beta = \{\pm(1,1)\}$).
>
> ---
>
> **Part (a): $Spin^c(3)\cong U(2)$.**
>
> **Step a1 — $\Phi$ is a well-defined homomorphism into $U(2)$.** Define $\tilde\Phi : SU(2)\times U(1)\to U(2)$ by $\tilde\Phi(A,z) = zA$. This lands in $U(2)$: $(zA)^\dagger(zA) = \bar z z\, A^\dagger A = |z|^2 I = I$ (since $A$ is unitary and $|z|=1$). It is a homomorphism, because scalars are central in $M_2(\mathbb{C})$:
> $$\tilde\Phi\big((A,z)(A',z')\big) = \tilde\Phi(AA',zz') = (zz')(AA') = (zA)(z'A') = \tilde\Phi(A,z)\,\tilde\Phi(A',z') \qquad \text{(scalar } z' \text{ commutes with } A\text{)} .$$
> It kills $\{\pm 1\}$: $\tilde\Phi(-I,-1) = (-1)(-I) = I$. Factoring through the quotient (a homomorphism trivial on the normal subgroup descends) gives the well-defined homomorphism $\Phi([A,z]) = zA$, which is smooth because $\tilde\Phi$ is smooth and the quotient projection is a smooth submersion.
>
> **Step a2 — $\Phi$ is bijective, hence a Lie isomorphism.** *Surjectivity:* given $B\in U(2)$, Lemma 3 provides $z\in U(1)$ and $A\in SU(2)$ with $B = zA$, so $B = \Phi([A,z])$. *Injectivity:* suppose $\Phi([A,z]) = \Phi([A',z'])$, i.e. $zA = z'A'$. By the uniqueness clause of Lemma 3, $(z',A') = (z,A)$ or $(z',A') = (-z,-A)$; in the first case $[A',z']=[A,z]$, in the second $[A',z'] = [-A,-z] = [A,z]$ (definition of the quotient). Hence $\Phi$ is injective. Being a smooth bijective homomorphism of Lie groups, $\Phi$ is an isomorphism of Lie groups by Lemma 2.
>
> **Step a3 — $\rho_{\det}$ is the determinant.** Transport $\rho_{\det}$ across $\Phi$: for $B = zA = \Phi([A,z])$,
> $$\rho_{\det}(B) = \rho_{\det}([A,z]) = z^2 = \det B \qquad \text{(} \rho_{\det}([A,z])=z^2 \text{ by definition; } z^2=\det B \text{ by Lemma 3)} .$$
> So under $\Phi$ the homomorphism $\rho_{\det} : U(2)\to U(1)$ is exactly the determinant.
>
> **Step a4 — $\rho_0$ is the natural projection to $PU(2)\cong SO(3)$.** Transport $\rho_0$ across $\Phi$: for $B = zA$,
> $$\rho_0(B) = \rho_0([A,z]) = \xi(A) = \alpha(A) \qquad \text{(} \rho_0([A,z])=\xi(g)\text{; } \xi=\alpha \text{ on } Spin(3)\cong SU(2)\text{)},$$
> where $\alpha : SU(2)\to SO(3)$ is the double cover with $\ker\alpha = \{\pm I\}$ ([[Thm - SU(2) is the Double Cover of SO(3)|the statement that SU(2) double-covers SO(3)]]: $\alpha$ is a surjective Lie homomorphism with kernel $\{\pm I\}$). We now identify this with the natural projection. Let $Z = \{\zeta I : \zeta\in U(1)\}$ be the centre of $U(2)$ (the scalar matrices) and $\pi : U(2)\to PU(2) := U(2)/Z$ the quotient. The composite $SU(2)\hookrightarrow U(2)\xrightarrow{\pi} PU(2)$ is surjective, because any $B\in U(2)$ equals $zA$ with $A\in SU(2)$ (Lemma 3) and $\pi(B) = \pi(zI\cdot A) = \pi(A)$ (as $zI\in Z$), so every class is hit by an $SU(2)$-element; and its kernel is $SU(2)\cap Z = \{\zeta I : \zeta^2 = \det(\zeta I) = 1\} = \{\pm I\}$. Therefore $\pi|_{SU(2)}$ induces an isomorphism $SU(2)/\{\pm I\}\xrightarrow{\cong} PU(2)$, and composing with $\alpha^{-1}$-induced $SU(2)/\{\pm I\}\cong SO(3)$ yields an isomorphism $j : PU(2)\xrightarrow{\cong} SO(3)$ with $j(\pi(A)) = \alpha(A)$ for $A\in SU(2)$. Finally, for general $B=zA$,
> $$j(\pi(B)) = j(\pi(A)) = \alpha(A) = \rho_0(B) \qquad \text{(} \pi(B)=\pi(A)\text{; definition of } j\text{; Step a4 first line)} ,$$
> so $\rho_0 = j\circ\pi$: the natural projection $U(2)\to PU(2)$ followed by $PU(2)\cong SO(3)$, as claimed.
>
> **Step a5 — the exact sequence (120).** We must show $1\to\{\pm I\}\to U(2)\xrightarrow{(\rho_0,\det)}SO(3)\times U(1)\to 1$ is exact, i.e. $(\rho_0,\det)$ is surjective with kernel $\{\pm I\}$. *Kernel:* if $\rho_0(B)=e$ and $\det B = 1$, then $\det B = z^2 = 1$ forces $z=\pm 1$, so $B = zA = \pm A\in SU(2)$, and $\rho_0(B) = \alpha(A) = e$ forces $A\in\ker\alpha = \{\pm I\}$, hence $B\in\{\pm I\}$; conversely $\rho_0(\pm I) = \alpha(\pm I) = e$ and $\det(\pm I) = 1$, so the kernel is exactly $\{\pm I\}$. *Surjectivity:* given $(R,w)\in SO(3)\times U(1)$, pick $A\in SU(2)$ with $\alpha(A)=R$ ($\alpha$ surjective) and $z\in U(1)$ with $z^2 = w$ (square root on the circle), and set $B = zA$; then $\det B = z^2 = w$ and $\rho_0(B) = \alpha(A) = R$, so $(\rho_0,\det)(B) = (R,w)$. Exactness follows. This is Haydys's sequence (120) in the form (a).
>
> ---
>
> **Part (b): $Spin^c(4)\cong U(2)\times_{U(1)}U(2)$.**
>
> Write $\mathcal{F} := \{(B_+,B_-)\in U(2)\times U(2) : \det B_+ = \det B_-\}$ for the fibre product.
>
> **Step b0 — $\mathcal{F}$ is a Lie subgroup.** The map $\delta : U(2)\times U(2)\to U(1)$, $\delta(B_+,B_-) = (\det B_+)(\det B_-)^{-1}$, is a smooth group homomorphism (a quotient of two determinants), and $\mathcal{F} = \delta^{-1}(1)$ is the kernel. A closed subgroup of a Lie group is an embedded Lie subgroup by the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]] (a subgroup that is topologically closed is an embedded Lie subgroup); $\mathcal{F}$ is closed as the preimage of the closed point $\{1\}$ under the continuous $\delta$. Hence $\mathcal{F}$ is a Lie group.
>
> **Step b1 — $\Psi$ is a well-defined homomorphism into $\mathcal{F}$.** Define $\tilde\Psi : SU(2)\times SU(2)\times U(1)\to U(2)\times U(2)$ by $\tilde\Psi(A_+,A_-,z) = (zA_+,zA_-)$. Each coordinate lands in $U(2)$ (Step a1 reasoning applied to each factor), and the image lands in $\mathcal{F}$ because
> $$\det(zA_+) = z^2\det A_+ = z^2 = z^2\det A_- = \det(zA_-) \qquad \text{(} \det A_\pm = 1\text{)} .$$
> It is a homomorphism (each coordinate is, by Step a1), and it kills $\{\pm 1\} = \{((I,I),1),((-I,-I),-1)\}$ since $\tilde\Psi((-I,-I),-1) = ((-1)(-I),(-1)(-I)) = (I,I)$. Factoring through the quotient gives the well-defined smooth homomorphism $\Psi([(A_+,A_-),z]) = (zA_+,zA_-)$ into $\mathcal{F}$.
>
> **Step b2 — $\Psi$ is bijective, hence a Lie isomorphism.** *Surjectivity:* let $(B_+,B_-)\in\mathcal{F}$, so $\det B_+ = \det B_- =: d\in U(1)$. Choose one square root $z\in U(1)$ with $z^2 = d$, and set $A_\pm := \bar z B_\pm$. By the existence argument of Lemma 3 (with this single common $z$, legitimate precisely because the two determinants agree), $A_\pm\in SU(2)$ and $B_\pm = zA_\pm$; hence $(B_+,B_-) = \Psi([(A_+,A_-),z])$. *Injectivity:* suppose $\Psi([(A_+,A_-),z]) = \Psi([(A_+',A_-'),z'])$, i.e. $zA_+ = z'A_+'$ and $zA_- = z'A_-'$. The first equality and Lemma 3's uniqueness give $z' = \pm z$. If $z' = z$, both equalities give $A_\pm' = A_\pm$, so the classes agree. If $z' = -z$, both give $A_\pm' = -A_\pm$, so $[(A_+',A_-'),z'] = [(-A_+,-A_-),-z] = [(A_+,A_-),z]$ in the quotient. Hence $\Psi$ is injective. Being a smooth bijective homomorphism of Lie groups, $\Psi$ is an isomorphism by Lemma 2.
>
> **Step b3 — $\rho_{\det}$ and the projections $\rho_\pm$.** Transport across $\Psi$: for $(B_+,B_-) = (zA_+,zA_-)$,
> $$\rho_{\det}(B_+,B_-) = z^2 = \det B_+ = \det B_- \qquad \text{(} \rho_{\det}([g,z])=z^2\text{; } z^2=\det B_\pm \text{ by Step b1)} .$$
> The homomorphisms $\rho_\pm : Spin^c(4)\to U(2)$, $\rho_\pm([(A_+,A_-),z]) = zA_\pm$, are well-defined (each is a single coordinate of $\tilde\Psi$, which kills $\{\pm 1\}$) and become the coordinate projections $(B_+,B_-)\mapsto B_\pm$ under $\Psi$. Each is surjective: given $B\in U(2)$ with $\det B = d$ and any square root $z$ of $d$, the element $(B, zA_-)$ with $A_- := \bar z B_-$ chosen so that $\det(zA_-)=d$ — concretely take $B_- := B$ — lies in $\mathcal{F}$ and projects to $B$; more simply, $(B,B)\in\mathcal{F}$ and $\rho_\pm(B,B) = B$. Finally $\det(\rho_\pm(B_+,B_-)) = \det B_\pm = \rho_{\det}(B_+,B_-)$, so $\rho_{\det} = \det\circ\rho_\pm$.
>
> **Step b4 — the half-spinor representations $\slashed{S}^\pm$.** By the [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|quaternionic model]], the half-spinor spaces are $\slashed{S}^\pm = \mathbb{H}$ with the complex structure given by right multiplication by $\bar i$, and $Spin(4)\cong Sp(1)\times Sp(1)$ acts so that an element $g = (q_+,q_-)$ acts on $\slashed{S}^\pm$ by left multiplication by $q_\pm$; under $Sp(1)\cong SU(2)$ this left multiplication is the fundamental action of the matrix $A_\pm\in SU(2)$ on $\mathbb{C}^2$. The $Spin^c(4)$-action on $\slashed{S}^\pm$ is, by definition ([[Def - Spin Structure and Spin-c Structure|the spinᶜ spinor representation]]), $[g,z]\cdot s = z\rho(g)s$; restricted to $\slashed{S}^\pm$ this is
> $$[(A_+,A_-),z]\cdot s = z\,(A_\pm s) = (zA_\pm)\,s = \rho_\pm([(A_+,A_-),z])\, s \qquad \text{(} \rho(g)|_{\slashed{S}^\pm}=A_\pm\cdot\text{; scalar-matrix product; Step b3)} .$$
> Therefore $\slashed{S}^\pm = \mathbb{C}^2$ with $Spin^c(4)$ acting through $\rho_\pm$ followed by the fundamental representation of $U(2)$, as claimed.
>
> ---
>
> **Conclusion.** In dimension three $\Phi([A,z])=zA$ is an isomorphism $Spin^c(3)\cong U(2)$ carrying $\rho_{\det}$ to $\det$, $\rho_0$ to the projection $U(2)\to PU(2)\cong SO(3)$, and (120) to $1\to\{\pm I\}\to U(2)\to SO(3)\times U(1)\to 1$. In dimension four $\Psi([(A_+,A_-),z])=(zA_+,zA_-)$ is an isomorphism $Spin^c(4)\cong U(2)\times_{U(1)}U(2)$ carrying $\rho_{\det}$ to the common determinant, $\rho_\pm$ to the coordinate projections, and the half-spinor representations to $\mathbb{C}^2$ through $\rho_\pm$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Charged spin in quantum mechanics.** The state space of a spin-$\tfrac12$ particle carrying a $U(1)$ charge transforms under both a rotation (an $SU(2)$ acting on the two-component spinor) and a phase (a $U(1)$ acting by scalar multiplication), but a rotation by $2\pi$ and a charge phase of $\pi$ are physically indistinguishable — both send $\psi\mapsto -\psi$. The symmetry group is therefore not $SU(2)\times U(1)$ but its quotient by the diagonal $\{\pm 1\}$, which this theorem identifies as $U(2)$. The exercise is to recognise that the "spin-charge" symmetry group of such a particle is $U(2) = Spin^c(3)$ and to read the total angular-momentum-plus-charge operator as living in $\mathfrak{u}(2)$; it is non-obvious because the physical identification of the two $2\pi$-type operations is exactly the quotient no one writes down.

**Reduction of structure group and almost complex four-manifolds.** Show that an almost complex structure on an oriented Riemannian four-manifold — a reduction of $\mathrm{Fr}_{SO}$ to $U(2)\subset SO(4)$ — canonically determines a spinᶜ structure, by lifting the $U(2)$-cocycle through the theorem's identification of $U(2)$-data with $Spin^c(4)$-data whose determinant line is the anticanonical line. The theorem applies because part (b) exhibits $U(2)$ inside $Spin^c(4)$ via the equal-determinant fibre product; the step is non-obvious because one must see the canonical bundle appear as $\rho_{\det}$ of the reduced cocycle rather than as an independent choice.

**Projective representations and the obstruction to lifting.** A projective unitary representation of $SO(3)$ is a homomorphism $SO(3)\to PU(2)$; the theorem's Step a4 says $PU(2)\cong SO(3)$, so such a representation is a homomorphism $SO(3)\to SO(3)$, and the question of whether it lifts to an honest $U(2)$-representation is governed by the two-element kernel of $U(2)\to SO(3)$. The exercise is to use the exact sequence (120) to compute the lifting obstruction as a class in $H^2$ with $\mathbb{Z}/2$-coefficients; it applies because the theorem turns the abstract central extension into the concrete $U(2)\to SO(3)$, and it is non-obvious because the obstruction is invisible until the extension is made explicit.

---

# Bridges

- **The determinant line bundle.** Because part (a)/(b) make $\rho_{\det}$ the determinant, the determinant line bundle $L_{\det} = P\times_{\rho_{\det}}\mathbb{C}$ of a spinᶜ structure is the top exterior power $\det\slashed{S}^\pm = \Lambda^2\slashed{S}^\pm$ of a half-spinor bundle. This is the construction that lets the [[Thm - Classification of Spin-c Structures|classification of spinᶜ structures]] proceed: tensoring the $U(2)$-valued transition data of $P$ by a line bundle $Q$ multiplies each $B_\pm$ by a scalar, hence multiplies $L_{\det}$ by $Q^2$, so the map "spinᶜ structure $\mapsto c_1(L_{\det})$" shifts by $2c_1(Q)$ under the $H^2(M;\mathbb{Z})$-action. The whole torsor structure is visible only once $\rho_{\det}$ is the determinant, which is what this page establishes.

- **The half-spinor bundles and the quadratic map of Seiberg–Witten theory.** Step b4 makes $\slashed{S}^\pm$ the fundamental $U(2)$-representation $\mathbb{C}^2$ through $\rho_\pm$. Given a positive spinor $\psi\in\slashed{S}^+ = \mathbb{C}^2$, the traceless part of the Hermitian endomorphism $\psi\psi^\dagger$ is an element of $\mathfrak{su}(2) = \mathfrak{su}(\slashed{S}^+)$, and under the identification $\Lambda^2_+\mathbb{R}^4\cong\mathfrak{su}(\slashed{S}^+)$ ([[Thm - Spinor Representations of Spin(4) and the Self-Dual Forms|the linear-algebra backbone]]) it becomes an imaginary self-dual two-form. This is the quadratic term $\mu(\psi)$ of [[Def - Seiberg-Witten Equations|the Seiberg–Witten equations]]; it can be written down as a matrix computation only because this page identifies $\slashed{S}^+$ with $\mathbb{C}^2$ and the structure group with $U(2)$.

- **The weight-two central circle.** The definition $\rho_{\det}([g,z]) = z^2$ against the spinor action $[g,z]\cdot s = z\rho(g)s$ says the same circle acts on $L_{\det}$ with weight two and on spinors with weight one. Transported through the theorem, this is the statement that the scalar $z\in U(1)\subset U(2)$ acts on $\slashed{S}^\pm=\mathbb{C}^2$ by $z$ and on $\det\slashed{S}^\pm=\mathbb{C}$ by $z^2$. This factor of two is the origin of the $\tfrac12$ in [[Thm - Variation of the Twisted and Spin-c Dirac Operators with the Connection|the variation of the spinᶜ Dirac operator]]: a change of the connection on $L_{\det}$ by an imaginary one-form $a$ changes the connection on the spinor bundle by $\tfrac12 a$.

---

# Unlocked by This

> [!tip] Almost Complex Structures Are Spinᶜ *(from Complex Geometry)*
> The inclusion $U(2)\hookrightarrow SO(4)$ makes every almost complex four-manifold spinᶜ, with determinant line the anticanonical bundle $K^{-1} = \Lambda^{2,0}$. This is the group-theoretic reason complex surfaces come with a canonical Seiberg–Witten setup, and it rests on identifying $U(2)$ with a subgroup of $Spin^c(4)$ as on this page. See **Def - Canonical Spinᶜ Structure of an Almost Complex Manifold**.

> [!tip] Spinᶜ Structures Form a Torsor *(from Gauge Theory)*
> Once $\rho_{\det}$ is the determinant, the set of spinᶜ structures on $M$ becomes a torsor over $H^2(M;\mathbb{Z})$, with the action given by tensoring by a line bundle and squaring on the determinant line. See [[Thm - Classification of Spin-c Structures]].
