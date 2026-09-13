---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Def - Self-Dual and Anti-Self-Dual Forms"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - The Induced Inner Product and Volume Form are Well-Defined"
tags: [geometry, gauge-theory, four-manifolds, hodge-star]
---

# Notation

Throughout this page $V$ is a real vector space of dimension $n = 4$, oriented, and equipped with a Euclidean (positive-definite) inner product $\langle\cdot,\cdot\rangle$, so that its index is $p = 0$. We fix a positively oriented orthonormal basis $e_1, e_2, e_3, e_4$ of $V$ and write $e_1^*, e_2^*, e_3^*, e_4^*$ for the dual basis of $V^*$, defined by $e_i^*(e_j) = \delta_{ij}$. The space of alternating $k$-linear forms on $V$ is $\Lambda^k V^*$ (see [[Def - Alternating Tensor and Lambda k V Dual|the definition of $\Lambda^k V^*$]]); on a four-dimensional $V$ the middle degree is $k = 2$, and $\dim \Lambda^2 V^* = \binom{4}{2} = 6$. To keep displays short we write $\omega_{ij} := e_i^* \wedge e_j^*$ for $1 \le i < j \le 4$; the six forms $\omega_{12}, \omega_{13}, \omega_{14}, \omega_{23}, \omega_{24}, \omega_{34}$ are the standard basis of $\Lambda^2 V^*$.

The inner product $\langle\cdot,\cdot\rangle$ on $V$ induces one on each $\Lambda^k V^*$, characterised on the basis by declaring $\{e_{i_1}^* \wedge \dots \wedge e_{i_k}^*\}_{i_1 < \dots < i_k}$ orthonormal in the Euclidean case; concretely, by part (ii) of [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem for the induced inner product and volume form]], $\langle \omega_{ij}, \omega_{kl}\rangle = \delta_{(ij),(kl)}$ for $p = 0$, so the six $\omega_{ij}$ form an orthonormal basis of $\Lambda^2 V^*$. We write $|\omega|^2 := \langle \omega, \omega\rangle$ for $\omega \in \Lambda^2 V^*$. The **volume form** determined by the orientation and inner product is
$$\mathrm{vol} := e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^* \in \Lambda^4 V^*,$$
the wedge of the positively oriented orthonormal coframe; reversing the orientation of $V$ replaces $\mathrm{vol}$ by $-\mathrm{vol}$.

The **Hodge star** $\star : \Lambda^k V^* \to \Lambda^{n-k} V^*$ is, in the convention used throughout this series, the unique linear map determined by
$$\omega \wedge \eta = \langle \star\omega, \eta\rangle \, \mathrm{vol} \qquad \text{for all } \omega \in \Lambda^k V^*,\ \eta \in \Lambda^{n-k} V^*, \tag{3.1}$$
its existence and uniqueness being the content of [[Def - Hodge Star in Arbitrary Signature|the definition of the Hodge star in arbitrary signature]]. For $n = 4$ and $k = 2$ the star maps $\Lambda^2 V^*$ to itself, and it is this endomorphism that the present theorem studies. We call a $2$-form $\omega \in \Lambda^2 V^*$ **self-dual** if $\star\omega = \omega$ and **anti-self-dual** if $\star\omega = -\omega$, and set
$$\Lambda^2_\pm V^* := \{\omega \in \Lambda^2 V^* : \star\omega = \pm\omega\}.$$
The vector-space content of these two notions is exactly the fibrewise version of the manifold definition:

![[Def - Self-Dual and Anti-Self-Dual Forms#The Definition]]

Reading that definition at a single tangent space $V = T_x M$, with $\Omega^2_\pm(M)$ replaced by $\Lambda^2_\pm V^*$ and the Riemannian pointwise inner product by $\langle\cdot,\cdot\rangle$, gives precisely the objects of this page; here we prove, purely linear-algebraically, that the decomposition it names exists and has the stated bases.

> [!warning] Convention: three sign conventions for $\star$, and why they coincide here
> Three normalisations of the Hodge star appear in the literature. This series uses Bär's, $\star = \star_B$, defined by $(3.1)$: $\omega \wedge \eta = \langle \star\omega, \eta\rangle\,\mathrm{vol}$. The vault's earlier operator [[Def - The Hodge Star Operator|$\star_V$]] is defined by $\alpha \wedge \star\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$; the two are related by $\star_B = (-1)^p \star_V$ on $\Lambda^k$, and a third common convention $\star' = (-1)^{k(n-k)}\star_V$ also occurs. On a four-dimensional Euclidean $V$ ($p = 0$) and on $2$-forms ($k = n - k = 2$, so $(-1)^{k(n-k)} = (-1)^4 = 1$), all three agree: $\star_B = \star_V = \star'$. Every statement on this page therefore holds verbatim in any of the three conventions, and the companion Riemannian result [[Thm - Properties of the Hodge Star|the properties of the Hodge star]] (proved for $\star_V$ with $p = 0$) may be quoted directly. Outside dimension four on $2$-forms the conventions differ and the recipe above must be applied.

---

# Statement

> **Theorem (self-dual decomposition of $2$-forms in four dimensions).** Let $V$ be an oriented four-dimensional real vector space with a Euclidean inner product $\langle\cdot,\cdot\rangle$ (index $p = 0$), and let $\star : \Lambda^2 V^* \to \Lambda^2 V^*$ be the associated Hodge star, defined by $(3.1)$.
>
> **(I) The star is an involutive isometry.** On $\Lambda^2 V^*$ one has $\star \circ \star = \mathrm{id}$, and $\star$ is an isometry: $\langle \star\omega, \star\eta\rangle = \langle \omega, \eta\rangle$ for all $\omega, \eta \in \Lambda^2 V^*$.
>
> **(II) Orthogonal eigenspace decomposition.** Consequently $\Lambda^2 V^*$ splits as the orthogonal direct sum of the $\pm 1$ eigenspaces of $\star$,
> $$\Lambda^2 V^* = \Lambda^2_+ V^* \oplus \Lambda^2_- V^*, \qquad \Lambda^2_\pm V^* = \{\omega : \star\omega = \pm\omega\},$$
> with $\dim \Lambda^2_+ V^* = \dim \Lambda^2_- V^* = 3$. Explicit orthogonal bases are
> $$\Lambda^2_\pm V^*: \quad e_1^* \wedge e_2^* \pm e_3^* \wedge e_4^*, \quad e_1^* \wedge e_3^* \mp e_2^* \wedge e_4^*, \quad e_1^* \wedge e_4^* \pm e_2^* \wedge e_3^*,$$
> the upper signs giving a basis of $\Lambda^2_+ V^*$ and the lower signs a basis of $\Lambda^2_- V^*$.
>
> **(III) Wedge identities.** For $\omega \in \Lambda^2_\pm V^*$,
> $$\omega \wedge \omega = \pm\, |\omega|^2 \, \mathrm{vol},$$
> and for $\omega_+ \in \Lambda^2_+ V^*$, $\omega_- \in \Lambda^2_- V^*$,
> $$\omega_+ \wedge \omega_- = 0.$$
>
> **(IV) Behaviour under orientation reversal.** Reversing the orientation of $V$ replaces $\star$ by $-\star$ on $\Lambda^2 V^*$ and interchanges $\Lambda^2_+ V^*$ and $\Lambda^2_- V^*$.

---

# Motivation

The Hodge star is defined in every dimension and every degree, and in general it maps $\Lambda^k V^*$ to the *different* space $\Lambda^{n-k} V^*$; there is then nothing for it to be self-dual with respect to, and no decomposition to speak of. Two coincidences must happen at once before $\star$ can act as a symmetry of a single space and cut it into invariant pieces. First, the source and target degrees must agree, $k = n - k$, which forces $n = 2k$: the star must act in the *middle* degree. Second, applied twice it must return to the identity rather than to minus the identity, so that its eigenvalues are real and it genuinely diagonalises over $\mathbb{R}$; by [[Thm - Properties of the Hodge Star in Arbitrary Signature|the general double-star formula]] $\star\star = (-1)^{k(n-k)+p}$, and in the middle degree this is $(-1)^{k^2 + p} = (-1)^{k+p}$, which equals $+1$ exactly when $k + p$ is even. The smallest dimension in which both coincidences hold with a definite metric ($p = 0$) is $n = 4$, $k = 2$: there $\star\star = (-1)^{2 \cdot 2 + 0} = 1$. This is the algebraic origin of the special role of four dimensions in gauge theory, and this theorem is the precise statement of it.

What the theorem buys is a canonical, metric-determined splitting of $2$-forms into two three-dimensional halves that no lower-dimensional geometry possesses. The curvature of a connection on a bundle over a four-manifold is a $2$-form with values in a Lie algebra, and once we can decompose $2$-forms we can decompose curvatures: $F = F^+ + F^-$. The self-dual and anti-self-dual parts turn out to carry the physics. The Yang–Mills energy $\tfrac12\|F\|^2$ splits as $\tfrac12(\|F^+\|^2 + \|F^-\|^2)$, while the difference $\|F^+\|^2 - \|F^-\|^2$ is a topological invariant (a characteristic number); the wedge identities of part (III) are exactly the pointwise facts that make this split and this invariant computable, and they are the algebraic heart of the energy identity and the topological bound $\int L_{YM} \ge \tfrac{2\pi^2}{N}|p_1|$ for Yang–Mills fields (see [[Thm - Energy Identity and the Topological Bound for Yang-Mills|the energy identity and topological bound]]). The connections that saturate that bound are those whose curvature lies entirely in one summand, $\star F = \pm F$ — the [[Def - Instanton|instantons]]. The whole apparatus rests on the four-line linear-algebra statement below.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is austere — an oriented four-dimensional Euclidean vector space — but the theorem is invoked from settings that provide such a space only implicitly.

The first disguised source is **an oriented Riemannian four-manifold $(M, g)$ together with a chosen point**. Each tangent space $T_x M$, with the metric $g_x$ and the orientation restricted to it, is an oriented four-dimensional Euclidean vector space, so the theorem applies fibrewise and, because the constructions are natural in $(V, \langle\cdot,\cdot\rangle)$, assemble into a smooth splitting $\Lambda^2 T^* M = \Lambda^2_+ \oplus \Lambda^2_-$ of vector bundles. The non-obvious bridge is that a pointwise linear-algebra decomposition varies smoothly with the point: it does so here because the projections $\tfrac12(\mathrm{id} \pm \star)$ are built from the metric and orientation, which vary smoothly. *Example problem:* show that on a Kähler surface the Kähler form is a section of $\Lambda^2_+$, so that $b^+_2 \ge 1$.

The second disguised source is **any Lie-algebra-valued or vector-valued $2$-form on such a space**. The star extends to $W$-valued forms by $\star(\omega \otimes w) := (\star\omega)\otimes w$ (the extension defined on [[Def - Hodge Star in Arbitrary Signature|the Hodge-star definition page]]), and this extension is again an involutive isometry on the middle degree because it acts only on the form factor. The bridge is that tensoring with a fixed inner-product space $W$ preserves every hypothesis of the theorem verbatim. *Example problem:* decompose the $\mathfrak{su}(2)$-valued curvature of an $SU(2)$-connection into $F^+ \otimes$ and $F^- \otimes$ parts and read off when the connection is an instanton.

The third disguised source is **a four-dimensional oriented inner-product space that is not presented as $\mathbb{R}^4$ at all** — for instance the imaginary-quaternion-augmented spinor spaces of dimension four, or $\Lambda^2$ of a complex surface's real tangent space. Whenever such a space carries a positive-definite inner product and an orientation, the theorem furnishes its $2$-forms with the $\pm$ splitting. The bridge is that the theorem depends on $V$ only through its dimension, orientation, and inner product, never through any coordinate presentation. *Example problem:* identify $\Lambda^2_+ V^*$ with $\mathfrak{su}(2)$ acting on a positive spinor space, used in [[Def - Self-Dual and Anti-Self-Dual Connections|the definition of (anti-)self-dual connections]] and in Seiberg–Witten theory.

**Targets (Output Amplification).** The bare output is a splitting with explicit bases; combined with further ingredients it produces the central results of four-manifold gauge theory.

Combine the decomposition with **a connection and its curvature $F$**. The identity $\|F\|^2 = \|F^+\|^2 + \|F^-\|^2$ (from orthogonality) together with $\tfrac{1}{8\pi^2}\int \operatorname{tr}(F \wedge F) = \tfrac{1}{8\pi^2}(\|F^+\|^2 - \|F^-\|^2)$ (from the wedge identities of part (III)) yields the topological energy bound and its equality case. The extra ingredient is [[Thm - Chern-Weil Theorem|Chern–Weil theory]], which reads the difference as a characteristic number; the payoff is the existence of an absolute lower bound on the Yang–Mills energy in each topological sector, attained only by instantons.

Combine the decomposition with **the intersection form of a closed four-manifold**. Restricting the splitting to harmonic $2$-forms and integrating $\omega \wedge \omega = \pm|\omega|^2\,\mathrm{vol}$ shows the intersection form is positive-definite on $H^2_+$ and negative-definite on $H^2_-$; the extra ingredient is [[Thm - Homotopy Invariance of de Rham Cohomology|Hodge theory identifying cohomology with harmonic forms]], and the payoff is the Hodge signature identity $\sigma(M) = b^+_2 - b^-_2$, the entry point to Donaldson theory.

Combine the decomposition with **the second-order Yang–Mills equation and the Bianchi identity**. The wedge identities make the first-order equation $\star F = \pm F$ imply $d^\omega \star F = \pm d^\omega F = 0$, so (anti-)self-dual connections are automatically Yang–Mills (see [[Thm - Self-Dual Connections are Yang-Mills|self-dual connections are Yang–Mills]]). The extra ingredient is [[Thm - Bianchi Identity for a Principal Connection|the Bianchi identity]]; the payoff is that a nonlinear first-order equation replaces a nonlinear second-order one, which is what makes the instanton moduli space tractable.

---

# Why Is It True

The single mechanism behind every part is this:

> **An involution that is also an isometry splits an inner-product space into the mutually orthogonal $+1$ and $-1$ eigenspaces of the involution, and in dimension four on $2$-forms the Hodge star is exactly such an involution.**

The reasoning runs entirely through that one fact. Any linear map $T$ with $T^2 = \mathrm{id}$ has minimal polynomial dividing $x^2 - 1 = (x-1)(x+1)$, so it is diagonalisable with eigenvalues among $\pm 1$; the projections $\tfrac12(\mathrm{id} + T)$ and $\tfrac12(\mathrm{id} - T)$ send every vector into the $+1$ and $-1$ eigenspaces and sum to the identity, so the space is the direct sum of the two eigenspaces. If in addition $T$ preserves the inner product, then for a $+1$ eigenvector $u$ and a $-1$ eigenvector $v$ we have $\langle u, v\rangle = \langle Tu, Tv\rangle = \langle u, -v\rangle = -\langle u, v\rangle$, so $\langle u, v\rangle = 0$ and the two eigenspaces are orthogonal. This is all of part (II) in the abstract; the theorem is the observation that on $\Lambda^2 V^*$ with $n = 4$, $p = 0$ the star $\star$ *is* such a $T$, which is part (I).

That the two eigenspaces are each three-dimensional is not forced by the abstract argument alone; it is a genuine feature of the star. It follows from writing down six honest eigenvectors — the combinations $\omega_{12} \pm \omega_{34}$ and their cousins — three with eigenvalue $+1$ and three with eigenvalue $-1$, checking they are pairwise orthogonal (hence linearly independent), and noticing that six independent vectors in a six-dimensional space must be a basis; the three-plus-three split of the basis then pins each eigenspace to dimension three.

The wedge identities of part (III) are the same phenomenon read multiplicatively. The defining relation says $\omega \wedge \star\omega = |\omega|^2\,\mathrm{vol}$; for a self-dual $\omega$ the star does nothing, so $\omega \wedge \omega = |\omega|^2\,\mathrm{vol}$, while for an anti-self-dual $\omega$ the star flips the sign, so $\omega \wedge \omega = -\omega\wedge\star\omega = -|\omega|^2\,\mathrm{vol}$. That a self-dual and an anti-self-dual form wedge to zero is orthogonality of the eigenspaces wearing the disguise of the pairing $(3.1)$. Finally, part (IV) is immediate once one sees that $\star$ is built from $\mathrm{vol}$ through $(3.1)$ and that reversing orientation flips the sign of $\mathrm{vol}$: flipping $\mathrm{vol}$ flips $\star$, and flipping $\star$ turns each $+1$ eigenvector into a $-1$ eigenvector and vice versa.

---

# What Makes This Hard

The conceptual step that is easy to state and easy to bungle is the dimension count: exhibiting three self-dual and three anti-self-dual forms shows only $\dim\Lambda^2_\pm \ge 3$, and one must invoke $\dim\Lambda^2 V^* = 6$ together with the fact that the two eigenspaces meet only in $0$ to conclude the dimensions are *exactly* three; skipping this leaves open the possibility (ruled out only by the count) that the listed forms fail to span. The second trap is signature-dependence: every part of this theorem is false in Lorentzian signature, where $\star\star = -1$ on $2$-forms, the eigenvalues are $\pm i$, and no real decomposition exists — so the hypothesis $p = 0$ is not decorative and must be invoked at the exact line where $\star\star = 1$ is used. The third, subtler point is that the isometry property, not mere involutivity, is what makes the decomposition *orthogonal*; an involution alone gives a direct sum but not an orthogonal one, and the orthogonality is precisely what the energy identity $\|F\|^2 = \|F^+\|^2 + \|F^-\|^2$ later needs.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First establish that $\star$ is an involution and an isometry on $\Lambda^2 V^*$, by specialising the general double-star and isometry properties of the Hodge star to $n = 4$, $k = 2$, $p = 0$. Then invoke the abstract fact that an involutive isometry splits the space orthogonally into $\pm 1$ eigenspaces. Nail the dimensions by exhibiting six explicit eigenforms, computing the three star values $\star\omega_{12}, \star\omega_{13}, \star\omega_{14}$ directly from the defining relation, checking orthogonality, and counting against $\dim\Lambda^2 V^* = 6$. Finally read the wedge identities off the defining relation and the eigenvalue equations, and read orientation reversal off the sign of $\mathrm{vol}$ in $(3.1)$.

**Subgoal decomposition:**

1. **Star is an involution and an isometry on $\Lambda^2 V^*$.**
   - *Hint:* Put $n = 4$, $k = 2$, $p = 0$ into $\star\star = (-1)^{k(n-k)+p}$ and into $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$.
   - *Why needed:* These are the two hypotheses of the abstract splitting lemma; without them there is no real eigenspace decomposition and no orthogonality.

2. **Abstract splitting of an involutive isometry.**
   - *Hint:* Use the projections $P_\pm = \tfrac12(\mathrm{id} \pm \star)$; show they are complementary idempotents onto the eigenspaces, and use the isometry to get orthogonality.
   - *Why needed:* It converts the two properties of subgoal 1 into the direct-sum statement of part (II), before any dimension is known.

3. **The three fundamental star values.**
   - *Hint:* For $\omega = \omega_{1j}$, test $(3.1)$ against each basis $2$-form $\eta = \omega_{kl}$; only the complementary $\eta$ gives a nonzero wedge, and its sign is the sign of the reordering to $\mathrm{vol}$.
   - *Why needed:* They identify which explicit combinations are eigenforms with which eigenvalue.

4. **Six eigenforms, orthogonality, and the dimension count.**
   - *Hint:* Apply $\star$ to each $\omega_{12} \pm \omega_{34}$ etc. using subgoal 3 and $\star\star = 1$; check pairwise orthogonality via the orthonormal basis $\{\omega_{ij}\}$; then use $3 + 3 = 6 = \dim\Lambda^2 V^*$.
   - *Why needed:* It upgrades $\dim\Lambda^2_\pm \ge 3$ to equality and produces the stated bases.

5. **Wedge identities.**
   - *Hint:* From $(3.1)$, $\omega\wedge\star\omega = |\omega|^2\,\mathrm{vol}$; substitute $\star\omega = \pm\omega$. For the cross term use $\omega_+\wedge\omega_- = \langle\star\omega_+,\omega_-\rangle\mathrm{vol}$ and self-duality plus orthogonality.
   - *Why needed:* These are the multiplicative identities the energy identity and topological bound consume.

6. **Orientation reversal.**
   - *Hint:* Reversal sends $\mathrm{vol} \mapsto -\mathrm{vol}$; read off from $(3.1)$ that $\star \mapsto -\star$, then track what happens to each eigenspace.
   - *Why needed:* It is part (IV), and it explains why the sign of an instanton's (anti-)self-duality is orientation-dependent.

---

# Lemma Decomposition

> [!note]- Lemma 1: On $\Lambda^2 V^*$ in four Euclidean dimensions, $\star$ is an involution and an isometry
> **Statement:** Let $V$ be oriented, four-dimensional, with Euclidean inner product ($p = 0$), and let $\star : \Lambda^2 V^* \to \Lambda^2 V^*$ be the associated Hodge star. Then $\star\circ\star = \mathrm{id}$, and $\langle\star\omega, \star\eta\rangle = \langle\omega, \eta\rangle$ for all $\omega, \eta \in \Lambda^2 V^*$.
>
> **Hint:** Specialise the general properties $\star\star\omega = (-1)^{k(n-k)+p}\omega$ and $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$ to $n = 4$, $k = 2$, $p = 0$.
>
> **Why needed:** These are the two hypotheses (involutivity, isometry) fed to the abstract splitting Lemma 2; involutivity gives real eigenvalues $\pm 1$ and the direct sum, the isometry gives orthogonality.
>
> > [!note]- Full proof
> > We quote the general behaviour of the Hodge star in arbitrary signature, restated at the point of use. By [[Thm - Properties of the Hodge Star in Arbitrary Signature|the properties of the Hodge star in arbitrary signature]], on an oriented $n$-dimensional real vector space with a non-degenerate inner product of index $p$, the following hold for every $\omega, \eta \in \Lambda^k V^*$:
> > $$\star\star\omega = (-1)^{k(n-k)+p}\,\omega, \tag{property 2}$$
> > $$\langle\star\omega, \star\eta\rangle = (-1)^{p}\,\langle\omega, \eta\rangle. \tag{property 3}$$
> >
> > **Involutivity.** We have $n = 4$, $k = 2$, and, since $\langle\cdot,\cdot\rangle$ is Euclidean, $p = 0$. Substituting into property 2,
> > $$\star\star\omega = (-1)^{\,2\cdot(4-2)+0}\,\omega = (-1)^{4}\,\omega = \omega \qquad \text{(property 2 with } n = 4,\ k = 2,\ p = 0\text{)}.$$
> > Since this holds for every $\omega \in \Lambda^2 V^*$, $\star\circ\star = \mathrm{id}$ on $\Lambda^2 V^*$. (In Lorentzian signature, $p = 1$, the exponent is $4 + 1 = 5$ and $\star\star = -\mathrm{id}$; this is exactly the step where the hypothesis $p = 0$ is used.)
> >
> > **Isometry.** Substituting $p = 0$ into property 3,
> > $$\langle\star\omega, \star\eta\rangle = (-1)^{0}\,\langle\omega, \eta\rangle = \langle\omega, \eta\rangle \qquad \text{(property 3 with } p = 0\text{)}$$
> > for all $\omega, \eta \in \Lambda^2 V^*$. Therefore $\star$ preserves the induced inner product on $\Lambda^2 V^*$, that is, $\star$ is an isometry. $\blacksquare$

> [!note]- Lemma 2: An involutive isometry splits an inner-product space orthogonally into its $\pm 1$ eigenspaces
> **Statement:** Let $(W, \langle\cdot,\cdot\rangle)$ be a finite-dimensional real inner-product space and $T : W \to W$ a linear map with $T \circ T = \mathrm{id}$ (an involution) that is also an isometry, $\langle Tu, Tv\rangle = \langle u, v\rangle$ for all $u, v \in W$. Put $W_\pm := \{w \in W : Tw = \pm w\}$. Then $W = W_+ \oplus W_-$, the sum is orthogonal, and the maps $P_\pm := \tfrac12(\mathrm{id} \pm T)$ are the orthogonal projections of $W$ onto $W_\pm$.
>
> **Hint:** Show $P_\pm$ land in $W_\pm$, that $P_+ + P_- = \mathrm{id}$ and $W_+ \cap W_- = \{0\}$; then use the isometry to force orthogonality.
>
> **Why needed:** It is the abstract mechanism of the theorem; part (II) is this lemma applied to $W = \Lambda^2 V^*$ and $T = \star$, with the concrete dimensions supplied separately by Lemma 4.
>
> > [!note]- Full proof
> > **The projections land in the eigenspaces.** Fix $w \in W$ and set $w_\pm := P_\pm w = \tfrac12(w \pm Tw)$. Applying $T$ and using $T^2 = \mathrm{id}$,
> > $$T w_+ = \tfrac12(Tw + T^2 w) = \tfrac12(Tw + w) = w_+ \qquad \text{(since } T^2 w = w\text{)},$$
> > $$T w_- = \tfrac12(Tw - T^2 w) = \tfrac12(Tw - w) = -\,w_- \qquad \text{(since } T^2 w = w\text{)}.$$
> > Hence $w_+ \in W_+$ and $w_- \in W_-$.
> >
> > **The eigenspaces span $W$.** For every $w \in W$,
> > $$w_+ + w_- = \tfrac12(w + Tw) + \tfrac12(w - Tw) = w \qquad \text{(the } Tw \text{ terms cancel),}$$
> > so $w = w_+ + w_-$ with $w_+ \in W_+$, $w_- \in W_-$; thus $W = W_+ + W_-$. Equivalently $P_+ + P_- = \mathrm{id}$.
> >
> > **The sum is direct.** Suppose $w \in W_+ \cap W_-$. Then $Tw = w$ and $Tw = -w$, so $w = -w$, giving $2w = 0$ and $w = 0$. Hence $W_+ \cap W_- = \{0\}$, and with $W = W_+ + W_-$ this makes the sum direct: $W = W_+ \oplus W_-$.
> >
> > **The sum is orthogonal.** Let $u \in W_+$ and $v \in W_-$, so $Tu = u$ and $Tv = -v$. Using that $T$ is an isometry,
> > $$\langle u, v\rangle = \langle Tu, Tv\rangle = \langle u, -v\rangle = -\langle u, v\rangle \qquad \text{(isometry of } T\text{, then } Tu = u,\ Tv = -v\text{)}.$$
> > Therefore $2\langle u, v\rangle = 0$, so $\langle u, v\rangle = 0$: every vector of $W_+$ is orthogonal to every vector of $W_-$, and $W = W_+ \oplus W_-$ is an orthogonal direct sum.
> >
> > **The $P_\pm$ are the orthogonal projections.** We have shown $P_\pm$ map $W$ into $W_\pm$ and $P_+ + P_- = \mathrm{id}$; moreover $P_\pm$ restrict to the identity on $W_\pm$, since for $w \in W_+$, $P_+ w = \tfrac12(w + Tw) = \tfrac12(w + w) = w$, and likewise $P_- w = w$ for $w \in W_-$. A linear map equal to the identity on a subspace, zero on its orthogonal complement, and with image that subspace is the orthogonal projection onto it; here $\ker P_+ = W_-$ (as $P_+ w = \tfrac12(w + Tw) = 0 \iff Tw = -w$) is the orthogonal complement of $W_+$ by the orthogonality just proved, so $P_+$ is the orthogonal projection onto $W_+$, and symmetrically for $P_-$. $\blacksquare$

> [!note]- Lemma 3: The three fundamental star values
> **Statement:** With the fixed positively oriented orthonormal basis and the shorthand $\omega_{ij} = e_i^* \wedge e_j^*$,
> $$\star\,\omega_{12} = \omega_{34}, \qquad \star\,\omega_{13} = -\,\omega_{24}, \qquad \star\,\omega_{14} = \omega_{23}.$$
>
> **Hint:** Expand $\star\omega_{1j}$ in the basis $\{\omega_{kl}\}$ and evaluate the coefficient by testing the defining relation $(3.1)$ against each $\eta = \omega_{kl}$; only the complementary index pair contributes.
>
> **Why needed:** These three values, together with $\star\star = 1$ (Lemma 1), determine $\star$ on all six basis $2$-forms and hence identify the explicit eigenforms of Lemma 4.
>
> > [!note]- Full proof
> > Because $\{\omega_{kl}\}_{k<l}$ is an orthonormal basis of $\Lambda^2 V^*$ (Notation), for any $\omega \in \Lambda^2 V^*$ the coefficients of $\star\omega = \sum_{k<l} c_{kl}\,\omega_{kl}$ are recovered by pairing: $c_{kl} = \langle\star\omega, \omega_{kl}\rangle$, and by the defining relation $(3.1)$, $\langle\star\omega, \omega_{kl}\rangle\,\mathrm{vol} = \omega \wedge \omega_{kl}$. Thus $\star\omega$ is completely determined by the four-forms $\omega \wedge \omega_{kl}$, one for each basis $2$-form $\omega_{kl}$.
> >
> > **Value on $\omega_{12}$.** For each $k < l$ we compute $\omega_{12} \wedge \omega_{kl} = e_1^* \wedge e_2^* \wedge e_k^* \wedge e_l^*$. This vanishes whenever $\{k, l\}$ meets $\{1, 2\}$, because a repeated $e_i^*$ makes the wedge zero; the only surviving case is $\{k, l\} = \{3, 4\}$, where
> > $$\omega_{12} \wedge \omega_{34} = e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^* = \mathrm{vol} \qquad \text{(definition of } \mathrm{vol}\text{)}.$$
> > Hence $\langle\star\omega_{12}, \omega_{34}\rangle = 1$ and $\langle\star\omega_{12}, \omega_{kl}\rangle = 0$ for every other basis $2$-form, so $\star\omega_{12} = \omega_{34}$.
> >
> > **Value on $\omega_{13}$.** By the same test, $\omega_{13} \wedge \omega_{kl} = e_1^* \wedge e_3^* \wedge e_k^* \wedge e_l^*$ is nonzero only for $\{k, l\} = \{2, 4\}$, and there
> > $$\omega_{13} \wedge \omega_{24} = e_1^* \wedge e_3^* \wedge e_2^* \wedge e_4^* = -\,e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^* = -\,\mathrm{vol} \qquad \text{(one transposition } e_3^* \leftrightarrow e_2^* \text{)}.$$
> > Hence $\langle\star\omega_{13}, \omega_{24}\rangle = -1$ and all other pairings vanish, so $\star\omega_{13} = -\,\omega_{24}$.
> >
> > **Value on $\omega_{14}$.** Finally $\omega_{14} \wedge \omega_{kl} = e_1^* \wedge e_4^* \wedge e_k^* \wedge e_l^*$ is nonzero only for $\{k, l\} = \{2, 3\}$, and
> > $$\omega_{14} \wedge \omega_{23} = e_1^* \wedge e_4^* \wedge e_2^* \wedge e_3^* = e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^* = \mathrm{vol} \qquad \text{(two transpositions: } e_4^* \leftrightarrow e_2^*,\ \text{then } e_4^* \leftrightarrow e_3^*\text{)}.$$
> > Indeed, moving $e_4^*$ past $e_2^*$ then past $e_3^*$ introduces $(-1)^2 = +1$. Hence $\langle\star\omega_{14}, \omega_{23}\rangle = 1$ and all other pairings vanish, so $\star\omega_{14} = \omega_{23}$. $\blacksquare$

> [!note]- Lemma 4: Six explicit eigenforms, their orthogonality, and the dimension count
> **Statement:** The three forms $\omega_{12} + \omega_{34}$, $\omega_{13} - \omega_{24}$, $\omega_{14} + \omega_{23}$ lie in $\Lambda^2_+ V^*$, and the three forms $\omega_{12} - \omega_{34}$, $\omega_{13} + \omega_{24}$, $\omega_{14} - \omega_{23}$ lie in $\Lambda^2_- V^*$. All six are pairwise orthogonal and nonzero; consequently they form an orthogonal basis of $\Lambda^2 V^*$, and $\dim\Lambda^2_+ V^* = \dim\Lambda^2_- V^* = 3$, with the three "$+$" forms an orthogonal basis of $\Lambda^2_+ V^*$ and the three "$-$" forms an orthogonal basis of $\Lambda^2_- V^*$.
>
> **Hint:** Use Lemma 3 and $\star\star = 1$ to compute $\star$ on each combination; use that $\{\omega_{ij}\}$ is orthonormal for the pairwise orthogonality; then count against $\dim\Lambda^2 V^* = 6$.
>
> **Why needed:** It supplies the concrete dimensions and bases in part (II) that the abstract Lemma 2 cannot provide.
>
> > [!note]- Full proof
> > **The six values of $\star$ on the basis.** From Lemma 3, $\star\omega_{12} = \omega_{34}$, $\star\omega_{13} = -\omega_{24}$, $\star\omega_{14} = \omega_{23}$. Applying $\star$ again and using $\star\star = \mathrm{id}$ on $\Lambda^2 V^*$ (Lemma 1),
> > $$\star\omega_{34} = \star\star\omega_{12} = \omega_{12}, \quad \star\omega_{24} = -\star\star\omega_{13} = -\omega_{13} \ \Rightarrow\ \star\omega_{24} = -\omega_{13}, \quad \star\omega_{23} = \star\star\omega_{14} = \omega_{14}.$$
> > (For the middle one: $\star\omega_{13} = -\omega_{24}$ gives $\star(-\omega_{24}) = \star\star\omega_{13} = \omega_{13}$, hence $\star\omega_{24} = -\omega_{13}$.)
> >
> > **The "$+$" combinations are self-dual.** Using linearity of $\star$ and the six values,
> > $$\star(\omega_{12} + \omega_{34}) = \omega_{34} + \omega_{12} = +(\omega_{12} + \omega_{34}),$$
> > $$\star(\omega_{13} - \omega_{24}) = -\omega_{24} - (-\omega_{13}) = \omega_{13} - \omega_{24} = +(\omega_{13} - \omega_{24}),$$
> > $$\star(\omega_{14} + \omega_{23}) = \omega_{23} + \omega_{14} = +(\omega_{14} + \omega_{23}).$$
> > Each has eigenvalue $+1$, so all three lie in $\Lambda^2_+ V^*$.
> >
> > **The "$-$" combinations are anti-self-dual.** Likewise,
> > $$\star(\omega_{12} - \omega_{34}) = \omega_{34} - \omega_{12} = -(\omega_{12} - \omega_{34}),$$
> > $$\star(\omega_{13} + \omega_{24}) = -\omega_{24} + (-\omega_{13}) = -(\omega_{13} + \omega_{24}),$$
> > $$\star(\omega_{14} - \omega_{23}) = \omega_{23} - \omega_{14} = -(\omega_{14} - \omega_{23}).$$
> > Each has eigenvalue $-1$, so all three lie in $\Lambda^2_- V^*$.
> >
> > **Pairwise orthogonality.** All computations use that $\{\omega_{ij}\}_{i<j}$ is orthonormal, so $\langle\omega_{ij}, \omega_{kl}\rangle$ is $1$ if $(i,j) = (k,l)$ and $0$ otherwise. Two of the six combinations built from *disjoint* index pairs — for instance $\omega_{12} \pm \omega_{34}$ against $\omega_{13} \pm \omega_{24}$ — involve four distinct basis $2$-forms, so their inner product is a sum of vanishing cross terms and is $0$. The only combinations sharing basis forms are the two built from the *same* pair; for these,
> > $$\langle\omega_{12} + \omega_{34},\ \omega_{12} - \omega_{34}\rangle = \langle\omega_{12},\omega_{12}\rangle - \langle\omega_{34},\omega_{34}\rangle = 1 - 1 = 0,$$
> > and identically for $\omega_{13} \pm \omega_{24}$ and for $\omega_{14} \pm \omega_{23}$. Hence all six combinations are pairwise orthogonal. (The cross-family orthogonality is also forced abstractly by Lemma 2, since the "$+$" forms lie in $\Lambda^2_+$ and the "$-$" forms in $\Lambda^2_-$.)
> >
> > **They are nonzero and form a basis.** Each combination has squared norm $\|\omega_{ij} \pm \omega_{kl}\|^2 = 1 + 1 = 2 \ne 0$, so all six are nonzero. A pairwise-orthogonal set of nonzero vectors is linearly independent: if $\sum_m a_m u_m = 0$ then pairing with $u_{m_0}$ gives $a_{m_0}\|u_{m_0}\|^2 = 0$, whence $a_{m_0} = 0$. We thus have six linearly independent vectors in $\Lambda^2 V^*$, which has dimension $\binom{4}{2} = 6$; therefore they form a basis of $\Lambda^2 V^*$.
> >
> > **The dimension count.** The three "$+$" forms lie in $\Lambda^2_+ V^*$ and are linearly independent, so $\dim\Lambda^2_+ V^* \ge 3$; likewise $\dim\Lambda^2_- V^* \ge 3$. By Lemma 2 (with $W = \Lambda^2 V^*$, $T = \star$, using Lemma 1), $\Lambda^2 V^* = \Lambda^2_+ V^* \oplus \Lambda^2_- V^*$, so $\dim\Lambda^2_+ V^* + \dim\Lambda^2_- V^* = 6$. Two integers each at least $3$ summing to $6$ are both equal to $3$. Hence $\dim\Lambda^2_\pm V^* = 3$, and the three "$+$" forms (respectively "$-$" forms), being three independent vectors in a three-dimensional space, are an orthogonal basis of $\Lambda^2_+ V^*$ (respectively $\Lambda^2_- V^*$). $\blacksquare$

> [!note]- Lemma 5: The wedge identities
> **Statement:** For $\omega \in \Lambda^2_\pm V^*$ one has $\omega \wedge \omega = \pm\,|\omega|^2\,\mathrm{vol}$; and for $\omega_+ \in \Lambda^2_+ V^*$, $\omega_- \in \Lambda^2_- V^*$ one has $\omega_+ \wedge \omega_- = 0$.
>
> **Hint:** Use the defining relation $(3.1)$ in the form $\omega \wedge \star\eta = \langle\omega,\eta\rangle\,\mathrm{vol}$ or directly $\omega\wedge\eta = \langle\star\omega,\eta\rangle\,\mathrm{vol}$, then substitute the eigenvalue equation $\star\omega = \pm\omega$ and the orthogonality of the eigenspaces (Lemma 2).
>
> **Why needed:** These are the pointwise multiplicative identities behind the Yang–Mills energy identity and topological bound; they are used silently in the four-manifold literature and are made explicit here.
>
> > [!note]- Full proof
> > **Self-wedge of an eigenform.** Let $\omega \in \Lambda^2 V^*$. The defining relation $(3.1)$ with the second slot $\eta = \star\omega$, together with property 3 applied once, is unnecessary; we argue directly. By $(3.1)$ applied with $\omega$ in the first slot and $\omega$ itself in the second slot,
> > $$\omega \wedge \omega = \langle\star\omega, \omega\rangle\,\mathrm{vol} \qquad \text{(defining relation } (3.1) \text{ with } \eta = \omega\text{)}.$$
> > Now suppose $\omega \in \Lambda^2_+ V^*$, so $\star\omega = \omega$. Then
> > $$\omega \wedge \omega = \langle\omega, \omega\rangle\,\mathrm{vol} = |\omega|^2\,\mathrm{vol} \qquad \text{(} \star\omega = \omega \text{)}.$$
> > If instead $\omega \in \Lambda^2_- V^*$, so $\star\omega = -\omega$, then
> > $$\omega \wedge \omega = \langle -\omega, \omega\rangle\,\mathrm{vol} = -\langle\omega,\omega\rangle\,\mathrm{vol} = -\,|\omega|^2\,\mathrm{vol} \qquad \text{(} \star\omega = -\omega \text{, bilinearity)}.$$
> > Together these give $\omega \wedge \omega = \pm\,|\omega|^2\,\mathrm{vol}$ for $\omega \in \Lambda^2_\pm V^*$. (Equivalently, since $\star\omega = \pm\omega$ makes $\omega\wedge\star\omega = |\omega|^2\,\mathrm{vol}$ read $\pm\,\omega\wedge\omega = |\omega|^2\,\mathrm{vol}$.)
> >
> > **Cross-wedge of opposite types.** Let $\omega_+ \in \Lambda^2_+ V^*$ and $\omega_- \in \Lambda^2_- V^*$. By $(3.1)$ with $\omega_+$ in the first slot and $\omega_-$ in the second,
> > $$\omega_+ \wedge \omega_- = \langle\star\omega_+, \omega_-\rangle\,\mathrm{vol} = \langle\omega_+, \omega_-\rangle\,\mathrm{vol} \qquad \text{(} (3.1) \text{, then } \star\omega_+ = \omega_+ \text{)}.$$
> > By the orthogonality of the eigenspaces $\Lambda^2_+ V^* \perp \Lambda^2_- V^*$ (Lemma 2, whose hypotheses hold by Lemma 1), $\langle\omega_+, \omega_-\rangle = 0$. Therefore
> > $$\omega_+ \wedge \omega_- = 0. \qquad \blacksquare$$

> [!note]- Lemma 6: Orientation reversal negates the star and swaps the two eigenspaces
> **Statement:** Let $\bar V$ denote $V$ with the opposite orientation, and $\bar\star$ the Hodge star on $\Lambda^2 V^*$ associated with $\bar V$ (same inner product, reversed orientation). Then $\bar\star = -\star$ on $\Lambda^2 V^*$, and consequently the self-dual space of $\bar V$ equals the anti-self-dual space of $V$, and vice versa: $\Lambda^2_+(\bar V)^* = \Lambda^2_- V^*$ and $\Lambda^2_-(\bar V)^* = \Lambda^2_+ V^*$.
>
> **Hint:** Reversing orientation sends $\mathrm{vol}$ to $-\mathrm{vol}$; feed this into the defining relation $(3.1)$, which determines $\star$ uniquely.
>
> **Why needed:** It is part (IV); it also explains why "self-dual" and "anti-self-dual" are interchanged by an orientation flip, so that the instanton condition $\star F = \pm F$ has an orientation-dependent sign.
>
> > [!note]- Full proof
> > **The volume form flips sign.** The volume form is $\mathrm{vol} = e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^*$ for a positively oriented orthonormal basis. If $e_1, e_2, e_3, e_4$ is positively oriented for $V$, then it is negatively oriented for $\bar V$, and any positively oriented orthonormal basis for $\bar V$ is obtained by an odd permutation or reflection of it; the associated top form is therefore $\overline{\mathrm{vol}} = -\mathrm{vol}$. (This is the defining property of the volume form: it changes sign precisely when the orientation is reversed.)
> >
> > **The star flips sign.** The star $\bar\star$ of $\bar V$ is the unique linear map with $\omega \wedge \eta = \langle\bar\star\omega, \eta\rangle\,\overline{\mathrm{vol}}$ for all $\omega, \eta$. Substituting $\overline{\mathrm{vol}} = -\mathrm{vol}$ and comparing with $(3.1)$,
> > $$\langle\bar\star\omega, \eta\rangle\,(-\mathrm{vol}) = \omega \wedge \eta = \langle\star\omega, \eta\rangle\,\mathrm{vol} \qquad \text{(defining relations of } \bar\star \text{ and } \star\text{)},$$
> > so $\langle\bar\star\omega, \eta\rangle = -\langle\star\omega, \eta\rangle = \langle -\star\omega, \eta\rangle$ for all $\eta \in \Lambda^{n-k} V^*$. Since the inner product on $\Lambda^{n-k} V^*$ is non-degenerate, $\bar\star\omega = -\star\omega$ for all $\omega$, that is, $\bar\star = -\star$.
> >
> > **The eigenspaces are interchanged.** For $\omega \in \Lambda^2 V^*$,
> > $$\bar\star\,\omega = \omega \iff -\star\omega = \omega \iff \star\omega = -\omega,$$
> > so the $+1$ eigenspace of $\bar\star$ is the $-1$ eigenspace of $\star$: $\Lambda^2_+(\bar V)^* = \Lambda^2_- V^*$. Interchanging the roles of $+$ and $-$ gives $\Lambda^2_-(\bar V)^* = \Lambda^2_+ V^*$. Reversing the orientation of $V$ therefore negates $\star$ and interchanges the self-dual and anti-self-dual subspaces. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be an oriented four-dimensional real vector space with a Euclidean inner product $\langle\cdot,\cdot\rangle$ (index $p = 0$), fix a positively oriented orthonormal basis $e_1, \dots, e_4$ with dual basis $e_1^*, \dots, e_4^*$, and write $\omega_{ij} = e_i^* \wedge e_j^*$ and $\mathrm{vol} = e_1^* \wedge e_2^* \wedge e_3^* \wedge e_4^*$. Let $\star : \Lambda^2 V^* \to \Lambda^2 V^*$ be the Hodge star defined by $(3.1)$.
>
> **Step 0 — the induced inner product and the star exist.** By [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem]], the inner product $\langle\cdot,\cdot\rangle$ on $V$ induces a well-defined non-degenerate inner product on $\Lambda^2 V^*$ for which $\{\omega_{ij}\}_{i<j}$ is orthonormal (with $p = 0$, $\langle\omega_{ij}, \omega_{ij}\rangle = \epsilon_i\epsilon_j = 1$), and $\mathrm{vol}$ is a well-defined generator of $\Lambda^4 V^*$ determined by the orientation. By [[Def - Hodge Star in Arbitrary Signature|the definition of the Hodge star]], the map $\star$ satisfying $(3.1)$ exists and is unique. All objects in the statement are therefore well-posed.
>
> **Step 1 — Part (I).** By **Lemma 1**, on $\Lambda^2 V^*$ the star satisfies $\star\circ\star = \mathrm{id}$ (from $\star\star = (-1)^{k(n-k)+p} = (-1)^{4} = 1$ with $n = 4$, $k = 2$, $p = 0$) and is an isometry, $\langle\star\omega, \star\eta\rangle = (-1)^p\langle\omega,\eta\rangle = \langle\omega,\eta\rangle$. This is exactly Part (I).
>
> **Step 2 — Part (II).** Apply **Lemma 2** to the inner-product space $W = \Lambda^2 V^*$ and the map $T = \star$, whose two hypotheses (involutivity and isometry) are supplied by Step 1. Lemma 2 gives the orthogonal direct sum
> $$\Lambda^2 V^* = \Lambda^2_+ V^* \oplus \Lambda^2_- V^*, \qquad \Lambda^2_\pm V^* = \{\omega : \star\omega = \pm\omega\},$$
> with orthogonal projections $\tfrac12(\mathrm{id} \pm \star)$. The dimensions and explicit bases come from **Lemma 4**: $\dim\Lambda^2_+ V^* = \dim\Lambda^2_- V^* = 3$, with orthogonal bases
> $$\Lambda^2_+ V^*:\quad \omega_{12} + \omega_{34},\ \ \omega_{13} - \omega_{24},\ \ \omega_{14} + \omega_{23},$$
> $$\Lambda^2_- V^*:\quad \omega_{12} - \omega_{34},\ \ \omega_{13} + \omega_{24},\ \ \omega_{14} - \omega_{23},$$
> which written with the upper/lower sign convention of the statement are $\omega_{12} \pm \omega_{34}$, $\omega_{13} \mp \omega_{24}$, $\omega_{14} \pm \omega_{23}$. (Lemma 4 rests on **Lemma 3** for the three fundamental star values.) This is Part (II).
>
> **Step 3 — Part (III).** By **Lemma 5**, for $\omega \in \Lambda^2_\pm V^*$,
> $$\omega \wedge \omega = \pm\,|\omega|^2\,\mathrm{vol},$$
> and for $\omega_+ \in \Lambda^2_+ V^*$, $\omega_- \in \Lambda^2_- V^*$,
> $$\omega_+ \wedge \omega_- = \langle\star\omega_+, \omega_-\rangle\,\mathrm{vol} = \langle\omega_+, \omega_-\rangle\,\mathrm{vol} = 0,$$
> the last equality by the orthogonality established in Step 2. This is Part (III).
>
> **Step 4 — Part (IV).** By **Lemma 6**, reversing the orientation of $V$ sends $\mathrm{vol}$ to $-\mathrm{vol}$, hence (through the defining relation $(3.1)$, whose right side carries $\mathrm{vol}$) replaces $\star$ by $-\star$ on $\Lambda^2 V^*$; consequently the $+1$ eigenspace of the reversed star is the $-1$ eigenspace of the original, so $\Lambda^2_+ V^*$ and $\Lambda^2_- V^*$ are interchanged. This is Part (IV).
>
> **Conclusion.** Parts (I)–(IV) are exactly the four assertions of the theorem, so on an oriented four-dimensional Euclidean vector space the Hodge star is an involutive isometry of $\Lambda^2 V^*$, its $\pm 1$ eigenspaces give the orthogonal self-dual/anti-self-dual decomposition into two three-dimensional subspaces with the stated bases, the wedge identities hold, and orientation reversal swaps the two halves. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the curvature operator of a four-manifold.** On an oriented Riemannian four-manifold the Riemann curvature tensor is a symmetric endomorphism of $\Lambda^2 T^* M$, the curvature operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$. The self-dual decomposition of this theorem, applied fibrewise, block-decomposes $\mathcal{R}$ into $\Lambda^2_+$ and $\Lambda^2_-$ pieces, and the off-diagonal block is the traceless Ricci tensor while the diagonal blocks split the Weyl tensor into its self-dual and anti-self-dual parts $W^+, W^-$. The theorem applies because each tangent space is oriented four-dimensional Euclidean; the non-obvious content is that a purely algebraic $3 + 3$ splitting of $2$-forms organises the twenty components of curvature into geometrically meaningful blocks, and that $W^+ = 0$ characterises anti-self-dual (half-conformally-flat) manifolds.

**Representation theory: $\mathfrak{so}(4)$ and the two $SU(2)$ factors.** The Lie algebra $\mathfrak{so}(4)$ of skew endomorphisms of $\mathbb{R}^4$ is canonically isomorphic to $\Lambda^2 (\mathbb{R}^4)^*$ (via the metric), and the theorem's decomposition $\Lambda^2 = \Lambda^2_+ \oplus \Lambda^2_-$ is exactly the splitting $\mathfrak{so}(4) = \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ into two commuting three-dimensional ideals. The theorem applies because $\Lambda^2$ carries the induced inner product and the star; the non-obvious payoff is that the exceptional isomorphism $\mathrm{Spin}(4) = SU(2) \times SU(2)$ and the whole self-dual/anti-self-dual language of four-manifold topology are visible already at the level of this six-dimensional linear algebra, with each $SU(2)$ acting on one eigenspace.

**Mathematical physics: real versus complex self-dual Maxwell fields.** Repeat the theorem's analysis in Lorentzian signature ($p = 1$), where $\star\star = -1$ on $2$-forms, and show that no nonzero *real* $2$-form is self-dual, so the Euclidean decomposition has no real Lorentzian analogue; the eigenvalues are $\pm i$ and the decomposition exists only over $\mathbb{C}$, giving the complex combination $F + i\star F$ of the electromagnetic field. This is a genuine application because the four-dimensional structure is the same but the index has changed; the non-obvious lesson is that the "miracle of four dimensions" is really a miracle of four *Riemannian* dimensions, and that the instanton story has no direct Lorentzian counterpart.

---

# Bridges

- **[[Def - Self-Dual and Anti-Self-Dual Connections|Self-dual and anti-self-dual connections]].** Tensoring the star with the adjoint bundle (the $W$-valued extension $\star(\omega \otimes w) = (\star\omega)\otimes w$) transports this theorem to $\mathfrak{g}$-valued $2$-forms, so the curvature $F$ of a connection on a bundle over a Riemannian four-manifold decomposes as $F = F^+ + F^-$ with $F^\pm = \tfrac12(F \pm \star F)$. A connection is self-dual when $F^- = 0$ and anti-self-dual when $F^+ = 0$; the present theorem is the fibrewise linear algebra that makes those conditions well-posed and each half three-dimensional in the form indices.

- **[[Thm - Energy Identity and the Topological Bound for Yang-Mills|The energy identity and topological bound for Yang–Mills]].** The orthogonality of Part (II) gives $\|F\|^2 = \|F^+\|^2 + \|F^-\|^2$, and the wedge identity of Part (III), integrated against the trace pairing, gives the characteristic number as $\|F^+\|^2 - \|F^-\|^2$ up to a constant. Combining these two is the entire content of the Yang–Mills bound $\int L_{YM} \ge \tfrac{2\pi^2}{N}|p_1|$, saturated exactly by instantons; the sign facts $\omega \wedge \omega = \pm|\omega|^2\mathrm{vol}$ and $\omega_+ \wedge \omega_- = 0$ proved here are the ones used silently in the four-manifold literature at that point.

- **[[Def - Instanton|Instantons]].** An instanton is a connection whose curvature lies entirely in one eigenspace of the star. Part (IV) explains why the sign in $\star F = \pm F$ is a matter of orientation: reversing the orientation of the base turns instantons into anti-instantons, which is why the literature fixes an orientation before declaring which of $\Lambda^2_+$, $\Lambda^2_-$ carries the "self-dual" label.

- **Quaternions and the imaginary quaternions.** Identifying $V = \mathbb{R}^4$ with the quaternions $\mathbb{H}$, each three-dimensional eigenspace $\Lambda^2_\pm$ is isomorphic to the imaginary quaternions $\operatorname{Im}\mathbb{H} = \operatorname{span}(i, j, k)$, with the three basis forms of each eigenspace matching $i, j, k$; left and right quaternion multiplication act on the two eigenspaces separately. This is the concrete manifestation of the $\mathfrak{so}(4) = \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ splitting and the reason the BPST instanton is written most cleanly in quaternionic coordinates.

---

# Unlocked by This

> [!tip] The intersection form and the Hodge signature theorem *(from Differential Topology)*
> On a closed oriented Riemannian four-manifold, restricting the self-dual decomposition to harmonic $2$-forms and integrating $\omega \wedge \omega = \pm|\omega|^2\,\mathrm{vol}$ shows the intersection form $Q([\alpha],[\beta]) = \int_M \alpha \wedge \beta$ is positive-definite on the self-dual harmonic forms and negative-definite on the anti-self-dual ones. The dimensions $b^\pm_2 = \dim H^2_\pm$ are metric-independent topological invariants, and $\sigma(M) = b^+_2 - b^-_2$ is the signature. This is the algebraic doorway to **Donaldson's diagonalisation theorem** and to the whole gauge-theoretic study of four-manifolds.

> [!tip] The splitting $\mathfrak{so}(4) = \mathfrak{so}(3) \oplus \mathfrak{so}(3)$ *(from Lie Theory)*
> Under the metric identification $\mathfrak{so}(4) \cong \Lambda^2(\mathbb{R}^4)^*$, this theorem's decomposition is the Lie-algebra splitting $\mathfrak{so}(4) = \mathfrak{so}(3) \oplus \mathfrak{so}(3)$ into two commuting ideals, each $\cong \mathfrak{su}(2)$. It is the infinitesimal form of the exceptional isomorphism $\mathrm{Spin}(4) = SU(2) \times SU(2)$ and underlies the spinorial description of four-dimensional geometry developed in the Clifford-algebra and Seiberg–Witten chapters, where $\Lambda^2_+ V^* \cong \mathfrak{su}(\slashed{S}^+)$ identifies self-dual forms with the traceless endomorphisms of the positive spinor space.
