---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Covering Space"
  - "Def - Universal Cover"
  - "Def - Lie Group"
  - "Ex - SU(2) is Diffeomorphic to S^3"
  - "Thm - Galois Correspondence for Covering Spaces"
tags: [geometry, algebraic-topology, lie-groups]
---

# Problem Statement

Show that the **spin double cover** $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$, defined explicitly as follows, is a covering map, a Lie-group homomorphism, and identifies $\mathrm{SU}(2) \cong S^3$ as the universal cover of $\mathrm{SO}(3)$.

**Explicit definition of $\rho$.** Identify $\mathbb{R}^3$ with the space of *traceless* skew-Hermitian $2 \times 2$ matrices, i.e., $\mathfrak{su}(2)$:
$$\mathbb{R}^3 \cong \mathfrak{su}(2) = \mathrm{span}_{\mathbb{R}}\{i\sigma_1, i\sigma_2, i\sigma_3\}$$
where $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices. For $q \in \mathrm{SU}(2)$, define
$$\rho(q) : \mathbb{R}^3 \to \mathbb{R}^3, \qquad \rho(q)(v) := q v q^{-1}$$
(conjugation by $q$). This is a real linear map $\mathbb{R}^3 \to \mathbb{R}^3$ preserving the inner product $\langle v, w \rangle = -\tfrac12 \mathrm{tr}(vw)$, hence an element of $\mathrm{O}(3)$. Show $\rho(q) \in \mathrm{SO}(3)$ for all $q$, so $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$.

**Tasks.**

(a) Show $\rho$ is a Lie-group homomorphism with kernel $\{\pm I\}$.
(b) Show $\rho$ is surjective.
(c) Conclude $\rho$ is a 2-sheeted covering map.
(d) Show $\mathrm{SU}(2) \cong S^3$ is simply connected, so $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is the universal cover, giving $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$.

**Recall:**

The diffeomorphism $\mathrm{SU}(2) \cong S^3$:

![[Ex - SU(2) is Diffeomorphic to S^3#Problem Statement]]

The Galois correspondence:

![[Thm - Galois Correspondence for Covering Spaces#Statement]]

---

# Convergent Strategy

**Problem class:** Construction and verification of a universal cover for a Lie group. The pattern is the most important Lie-group-theoretic example in the chapter: a compact non-simply-connected Lie group ($\mathrm{SO}(3)$) is the quotient of a *simply-connected* Lie group ($\mathrm{SU}(2) \cong S^3$) by a finite central subgroup ($\{\pm I\}$). This gives $\pi_1$ of the bottom group as the central subgroup of the top.

**Assumption pattern:** $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are connected Lie groups; $\mathrm{SU}(2) \cong S^3$ (already proved in DG XI, see [[Ex - SU(2) is Diffeomorphic to S^3]]), so simply connected. The Lie algebras are isomorphic: $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ (both 3-dimensional, both with the bracket $[X, Y] = X \times Y$ once identified with $\mathbb{R}^3$). So the two groups have the same local structure but differ globally — $\mathrm{SU}(2)$ has trivial $\pi_1$, $\mathrm{SO}(3)$ has $\pi_1 = \mathbb{Z}/2$.

**Theorem routing:** Construct the explicit map $\rho(q)(v) = qvq^{-1}$; verify it lands in $\mathrm{SO}(3)$; compute the kernel ($\{\pm I\}$ by elementary algebra); verify surjectivity (count dimensions and use connectedness + closed-subgroup theorem). Conclude $\mathrm{SO}(3) = \mathrm{SU}(2)/\{\pm I\}$ as a Lie group. Apply $\mathrm{SU}(2) \cong S^3$ (DG XI) to get simply-connected; then [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] gives $\pi_1(\mathrm{SO}(3)) = \{\pm I\} = \mathbb{Z}/2$.

**Key decision point:** Why $\rho$ has kernel $\{\pm I\}$ and not, say, $\{I\}$. Conjugation $v \mapsto qvq^{-1}$ is invariant under $q \to \lambda q$ for any scalar $\lambda$ commuting with everything. For $q \in \mathrm{SU}(2)$, the centre is $\{\pm I\}$ (a unit complex scalar $\lambda$ in the centre must satisfy $\lambda \bar\lambda = 1$ and commute with all of $\mathrm{SU}(2)$, forcing $\lambda = \pm 1$). So $\rho(q) = \rho(-q)$ trivially, and the kernel is exactly the centre $\{\pm I\}$. The non-obvious step is making this rigorous via a direct computation: a 2-sheeted cover, not just a generic quotient.

---

# Legal Operations Used

1. **Operation 6 from the topic page (pass to the universal cover).** $\mathrm{SU}(2) \cong S^3$ is simply connected, so it is the universal cover of any quotient $\mathrm{SU}(2)/H$ for a discrete normal subgroup $H$. Choosing $H = \{\pm I\}$ gives $\mathrm{SO}(3)$.

2. **Operation 4 from the topic page (identify $\pi_1$ via a quotient by a free properly discontinuous action).** $\{\pm I\}$ acts on $\mathrm{SU}(2)$ freely (the only fixed point of $-I$ would be a $q$ with $-q = q$, i.e., $q = 0$, but $q \in \mathrm{SU}(2)$ has $|q| = 1$, so no fixed points) and properly discontinuously. So $\pi_1(\mathrm{SO}(3)) = \pi_1(\mathrm{SU}(2)/\{\pm I\}) = \{\pm I\} = \mathbb{Z}/2$.

3. **Operation 8 from the topic page (deck-transformation symmetry).** The deck transformation $q \mapsto -q$ on $\mathrm{SU}(2)$ commutes with $\rho$ and generates the deck group $\mathbb{Z}/2$. The fibre over $\rho(q) \in \mathrm{SO}(3)$ is $\{q, -q\}$.

---

# Hints

> [!note]- Hint 1
> First verify that $\rho(q)$ really preserves the inner product on $\mathbb{R}^3 \cong \mathfrak{su}(2)$. The inner product is $\langle v, w \rangle = -\tfrac12 \mathrm{tr}(vw)$. Check that $\mathrm{tr}(qvq^{-1} qwq^{-1}) = \mathrm{tr}(vw)$ by cyclicity of trace.

> [!note]- Hint 2
> For $\rho(q) \in \mathrm{SO}(3)$ (not just $\mathrm{O}(3)$), use connectedness of $\mathrm{SU}(2)$: $\rho$ is continuous from connected $\mathrm{SU}(2)$ to $\mathrm{O}(3)$; the image contains the identity ($\rho(I) = \mathrm{id}$), which lies in the identity component $\mathrm{SO}(3)$. So the whole image lies in $\mathrm{SO}(3)$.

> [!note]- Hint 3
> Kernel computation: $\rho(q) = \mathrm{id}$ means $qvq^{-1} = v$ for all $v \in \mathfrak{su}(2)$, i.e., $q$ commutes with every traceless skew-Hermitian matrix. By Schur's lemma (or direct check), $q$ must be a scalar: $q = \lambda I$. For $q \in \mathrm{SU}(2)$ (unit determinant, unitary), $\lambda \in \{\pm 1\}$.

> [!note]- Hint 4
> Surjectivity: $\rho$ is a Lie-group homomorphism between *connected* Lie groups of the same dimension (both 3-dimensional). Compute $d\rho_I : \mathfrak{su}(2) \to \mathfrak{so}(3)$ and verify it is an isomorphism (in fact, by the explicit identification, $\mathfrak{su}(2) \cong \mathfrak{so}(3)$). Hence $\rho$ is a local diffeomorphism near $I$, and by connectedness + Lie-group-homomorphism-machinery, surjective.

> [!note]- Hint 5
> Once you have kernel $\{\pm I\}$ and surjectivity, $\rho$ factors as $\mathrm{SU}(2)/\{\pm I\} \cong \mathrm{SO}(3)$. The quotient $\mathrm{SU}(2)/\{\pm I\}$ inherits a covering structure (since the action of $\{\pm I\}$ on $\mathrm{SU}(2) \cong S^3$ is the antipodal action). So $\rho$ is a 2-sheeted covering. Simple connectedness of $S^3$ then makes this the universal cover.

---

# Solution

**Plan:** Verify each piece in turn. (1) $\rho(q) \in \mathrm{SO}(3)$. (2) $\rho$ is a Lie-group homomorphism. (3) $\ker \rho = \{\pm I\}$. (4) $\rho$ is surjective. (5) $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a 2-sheeted covering. (6) $\mathrm{SU}(2) \cong S^3$ simply connected → $\rho$ is universal cover → $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$.

**Step 1: $\rho(q) \in \mathrm{SO}(3)$.**

> [!note]- Derivation
> Identify $\mathfrak{su}(2) \cong \mathbb{R}^3$ with inner product $\langle v, w \rangle := -\tfrac12 \mathrm{tr}(vw)$. (For $v = iv_k\sigma_k$, $w = iw_k\sigma_k$, we have $vw = -v_iw_j\sigma_i\sigma_j$, and $\mathrm{tr}(\sigma_i\sigma_j) = 2\delta_{ij}$, so $\mathrm{tr}(vw) = -2 \langle v, w \rangle_{\mathbb{R}^3}$ if $\langle, \rangle_{\mathbb{R}^3}$ is the standard inner product. Hence $-\tfrac12 \mathrm{tr}(vw)$ recovers $\langle, \rangle_{\mathbb{R}^3}$.)
>
> For $q \in \mathrm{SU}(2)$: $\rho(q)(v) = qvq^{-1}$. This preserves the inner product:
> $$\langle \rho(q)v, \rho(q)w \rangle = -\tfrac12 \mathrm{tr}(qvq^{-1} qwq^{-1}) = -\tfrac12 \mathrm{tr}(qvwq^{-1}) = -\tfrac12 \mathrm{tr}(vw) = \langle v, w \rangle$$
> by cyclicity of trace. So $\rho(q) \in \mathrm{O}(3)$.
>
> $\rho$ is continuous (entries of $\rho(q)$ are continuous functions of entries of $q$). $\mathrm{SU}(2)$ is connected (it is $S^3$, path-connected). $\rho(I) = \mathrm{id} \in \mathrm{SO}(3)$. So the continuous image $\rho(\mathrm{SU}(2))$ is connected and contains $\mathrm{id}$, hence is contained in the identity component $\mathrm{SO}(3)$ of $\mathrm{O}(3)$.

**Step 2: $\rho$ is a Lie-group homomorphism.**

> [!note]- Derivation
> $\rho(q_1 q_2)(v) = (q_1 q_2)v(q_1 q_2)^{-1} = q_1 q_2 v q_2^{-1} q_1^{-1} = q_1 (\rho(q_2)v) q_1^{-1} = \rho(q_1)(\rho(q_2)v) = (\rho(q_1) \circ \rho(q_2))(v)$.
>
> So $\rho(q_1 q_2) = \rho(q_1) \rho(q_2)$. Smoothness of $\rho$ as a map of Lie groups is clear (composition and conjugation are smooth in matrix entries).

**Step 3: $\ker \rho = \{\pm I\}$.**

> [!note]- Derivation
> $q \in \ker \rho$ iff $qvq^{-1} = v$ for all $v \in \mathfrak{su}(2)$ iff $q$ commutes with every traceless skew-Hermitian matrix.
>
> Take $v = i\sigma_3 = \mathrm{diag}(i, -i)$. The condition $qvq^{-1} = v$ means $q$ commutes with $\mathrm{diag}(i, -i)$. So $q$ is diagonal (off-diagonal entries must commute with both $i$ and $-i$, hence be zero). So $q = \mathrm{diag}(\alpha, \beta)$ with $|\alpha| = |\beta| = 1$ (unitary) and $\alpha\beta = 1$ ($\det q = 1$). Hence $\beta = 1/\alpha = \bar\alpha$.
>
> Now take $v = i\sigma_1 = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ (a traceless skew-Hermitian matrix). $qvq^{-1} = v$ becomes $\mathrm{diag}(\alpha, \bar\alpha) \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} \mathrm{diag}(\bar\alpha, \alpha) = \begin{pmatrix} 0 & i\alpha\alpha \\ i\bar\alpha\bar\alpha & 0 \end{pmatrix}$, which equals $v$ iff $\alpha^2 = 1$. So $\alpha = \pm 1$, hence $q = \pm I$.
>
> So $\ker \rho = \{I, -I\} = \{\pm I\}$.

**Step 4: $\rho$ is surjective.**

> [!note]- Derivation
> Differentiate $\rho$ at $I$. For $X \in \mathfrak{su}(2)$, the curve $q(t) = e^{tX}$ has $\rho(e^{tX})(v) = e^{tX} v e^{-tX}$, with $t = 0$ giving $\frac{d}{dt}\big|_{t=0} \rho(e^{tX})(v) = Xv - vX = [X, v]$.
>
> So $d\rho_I : \mathfrak{su}(2) \to \mathfrak{so}(3)$ is $X \mapsto \mathrm{ad}_X = [X, -]$ (the adjoint representation).
>
> Is this an isomorphism? Inject: $\ker \mathrm{ad}_X = \{X : [X, v] = 0 \,\forall v\}$ = centre of $\mathfrak{su}(2)$. The centre of $\mathfrak{su}(2)$ is trivial (no non-zero traceless skew-Hermitian matrix commutes with all of $\mathfrak{su}(2)$). So $\mathrm{ad}$ is injective on $\mathfrak{su}(2)$. Both $\mathfrak{su}(2)$ and $\mathfrak{so}(3)$ are 3-dimensional, so injective implies bijective. Hence $d\rho_I$ is an isomorphism.
>
> By the inverse function theorem, $\rho$ is a local diffeomorphism near $I$. By Lie-group theory: a Lie-group homomorphism that is a local diffeomorphism at the identity is open. The image $\rho(\mathrm{SU}(2))$ is an open subgroup of $\mathrm{SO}(3)$, hence a closed-open subgroup of connected $\mathrm{SO}(3)$, hence all of $\mathrm{SO}(3)$.

**Step 5: $\rho$ is a 2-sheeted covering map.**

> [!note]- Derivation
> $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a surjective Lie-group homomorphism with kernel $\{\pm I\}$ (discrete, two elements). By the first isomorphism theorem for Lie groups, $\rho$ factors as $\mathrm{SU}(2)/\{\pm I\} \cong \mathrm{SO}(3)$.
>
> The quotient by a discrete normal subgroup of a Lie group is a covering: locally, $\rho$ is the quotient by the trivial action of $\{\pm I\}$ on a small neighbourhood (since $\pm I$ act by isolated points on $\mathrm{SU}(2)$), and globally the quotient is a 2-fold cover.
>
> So $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ is a 2-sheeted covering map. Fibres are $\{q, -q\}$ for each $q$.

**Step 6: $\rho$ is the universal cover, so $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$.**

> [!note]- Derivation
> By [[Ex - SU(2) is Diffeomorphic to S^3]], $\mathrm{SU}(2) \cong S^3$ as smooth manifolds. By Step 2 of [[Ex - Pi_1 of RP^n is Z over 2 for n at least 2]] (or directly), $S^3$ is simply connected for $n = 3 \geq 2$.
>
> So $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ has simply-connected total space — by definition, it is the universal cover of $\mathrm{SO}(3)$.
>
> By [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], $\pi_1(\mathrm{SO}(3)) \cong \mathrm{Deck}(\mathrm{SU}(2) / \mathrm{SO}(3))$. The deck transformations of $\mathrm{SU}(2) \to \mathrm{SO}(3)$ are exactly multiplication by elements of $\ker \rho = \{\pm I\}$, so the deck group is $\{\pm I\} \cong \mathbb{Z}/2$.
>
> Hence $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$.

> [!note]- Complete formal solution
> **Theorem.** The map $\rho : \mathrm{SU}(2) \to \mathrm{SO}(3)$ defined by $\rho(q)(v) = qvq^{-1}$ (with $\mathbb{R}^3$ identified with $\mathfrak{su}(2)$) is a Lie-group homomorphism with kernel $\{\pm I\}$, surjective, and a 2-sheeted covering map. $\mathrm{SU}(2) \cong S^3$ is simply connected, making $\rho$ the universal cover of $\mathrm{SO}(3)$. Hence $\pi_1(\mathrm{SO}(3)) \cong \mathbb{Z}/2$.
>
> *Proof.* As in the steps above.
>
> $\qquad\blacksquare$

> [!warning] Sanity-check via independent route: explicit non-trivial loop in $\mathrm{SO}(3)$
> The non-trivial element of $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ has a famous concrete realisation: the "belt trick" or "Dirac string." Take the 1-parameter family of rotations about a fixed axis by angle $t \cdot 2\pi$ for $t \in [0, 1]$. This is a loop in $\mathrm{SO}(3)$ starting and ending at the identity (rotation by $0$ = identity = rotation by $2\pi$). It is *not* null-homotopic — physically, a belt twisted by $2\pi$ cannot be un-twisted without translating its endpoints. Traversing the loop twice (rotation by $4\pi$) *is* null-homotopic — the "Dirac belt trick" demonstrates this physically: a belt with a $4\pi$ twist can be un-twisted by rotating one end through the belt's body. The full lift of this $2\pi$-rotation loop to $\mathrm{SU}(2)$ is a path from $I$ to $-I$ (not closed), confirming $\pi_1 = \mathbb{Z}/2$ generated by this loop, with order 2.

---

# Key Takeaways

**The "universal covering group" construction is the structural pattern for Lie groups.** For any connected Lie group $G$, there is a unique simply-connected Lie group $\widetilde G$ — the **universal covering group** — with the same Lie algebra, and $G$ arises as a quotient $\widetilde G / Z$ for $Z$ a discrete central subgroup. Equivalently, the Lie groups with a given Lie algebra are in bijection with discrete central subgroups of the unique simply-connected one. The trigger condition: a connected Lie group $G$. The transferable diagnostic: to compute $\pi_1(G)$, find the universal covering group $\widetilde G$ (often a simply-connected sphere or matrix group), then identify the kernel of $\widetilde G \to G$. Examples: $\mathrm{SU}(n) \to \mathrm{PSU}(n) = \mathrm{SU}(n)/Z_n$ ($\pi_1(\mathrm{PSU}(n)) = \mathbb{Z}/n$); $\widetilde{\mathrm{SL}_2(\mathbb{R})} \to \mathrm{SL}_2(\mathbb{R})$ ($\pi_1 = \mathbb{Z}$, infinite-sheeted!); $\mathrm{Spin}(n) \to \mathrm{SO}(n)$ ($\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$).

**$\pi_1$ of a Lie group is always finite and central in the universal cover.** The kernel of the universal-covering-group projection $\widetilde G \to G$ is a discrete central subgroup of $\widetilde G$. By [[Ex - Pi_1 of a Topological Group is Abelian]], $\pi_1(G)$ is abelian; the central condition strengthens this — $\pi_1$ is in the centre of the universal cover. For compact connected Lie groups, $\pi_1$ is always finite (because the centre of the simply-connected cover is finite — a consequence of $\widetilde G$ being compact, which holds when $G$ is). So for compact $G$, $\pi_1(G)$ is a finite abelian group, often $\mathbb{Z}/n$ or $\mathbb{Z}/2$. For $\mathrm{SO}(3)$ specifically, $\pi_1 = \mathbb{Z}/2$.

**The spin double cover is the gateway to spinors.** The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ generalises to $\mathrm{Spin}(n) \to \mathrm{SO}(n)$ for all $n \geq 3$. The total space $\mathrm{Spin}(n)$ is the simply-connected double cover of $\mathrm{SO}(n)$ — the **spin group**. The 2-dimensional complex representation of $\mathrm{SU}(2)$ (the defining representation) does *not* descend to $\mathrm{SO}(3)$ — because $-I$ in $\mathrm{SU}(2)$ acts non-trivially as $-\mathrm{id}$ on $\mathbb{C}^2$, while it must act as the identity on any $\mathrm{SO}(3)$-representation. The trigger: representations of $\mathrm{Spin}(n)$ that do not descend to $\mathrm{SO}(n)$ are called **spinor representations**, and they exist precisely because the cover is non-trivial. This is the topological origin of spin- $\frac{1}{2}$ particles in physics; see [[Spinors and the Dirac Equation]].

**The orientation-double-cover and the spin-double-cover are part of a tower of covers.** The "orientation cover" corresponds to $w_1 = 0$ (orientability); the "spin cover" corresponds to $w_2 = 0$ (spin structure exists); higher Stiefel-Whitney classes give higher covers (string structures, fivebrane structures). Each step adds one more layer of "homotopy-theoretic obstruction," and the corresponding cover trivialises that obstruction. The trigger: any obstruction theory in topology has an associated cover that classifies its trivialisation. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
