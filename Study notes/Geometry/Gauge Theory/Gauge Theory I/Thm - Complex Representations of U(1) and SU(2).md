---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Representation of a Lie Group"
  - "Def - Representation of a Lie Algebra"
  - "Def - Constructions on Representations"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Thm - The Exponential Map of a Matrix Group is the Matrix Exponential"
  - "Thm - The Exponential Map is a Local Diffeomorphism at the Origin"
  - "Thm - Naturality of the Exponential Map"
  - "Def - Unitary Operator"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is one of the two compact Lie groups $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ and $SU(2) = \{A \in \operatorname{Mat}(2 \times 2; \mathbb{C}) : A^* A = 1,\ \det A = 1\}$, and $V$ is a finite-dimensional complex vector space. A **[[Def - Representation of a Lie Group|representation]]** of $G$ on $V$ is a Lie group homomorphism $\varrho \colon G \to GL(V) = \operatorname{Aut}(V)$; we write $\varrho(g)v$ for the action of $g \in G$ on $v \in V$. Two representations $\varrho \colon G \to GL(V)$ and $\tilde\varrho \colon G \to GL(\tilde V)$ are **equivalent**, written $\varrho \cong \tilde\varrho$, if there is a linear isomorphism $T \colon V \to \tilde V$ with $T \circ \varrho(g) = \tilde\varrho(g) \circ T$ for every $g \in G$; such a $T$ is an **intertwiner** or an equivalence.

A **subrepresentation** of $\varrho$ is a linear subspace $U \subseteq V$ with $\varrho(g)U \subseteq U$ for all $g \in G$ (an **invariant** subspace); the restriction $\varrho|_U \colon G \to GL(U)$ is then a representation. The representation $\varrho$ is **irreducible** if $V \neq 0$ and its only invariant subspaces are $0$ and $V$; it is **completely reducible** if $V$ is a direct sum $V = W_1 \oplus \dots \oplus W_r$ of invariant subspaces on each of which the restriction is irreducible. Given representations $\varrho_i \colon G \to GL(V_i)$, their **[[Def - Constructions on Representations|direct sum]]** acts on $V_1 \oplus \dots \oplus V_r$ by $\varrho(g) = \varrho_1(g) \oplus \dots \oplus \varrho_r(g)$, their **[[Def - Constructions on Representations|tensor product]]** $\varrho_1 \otimes \varrho_2$ acts on $V_1 \otimes V_2$ by $g \mapsto \varrho_1(g) \otimes \varrho_2(g)$, the **[[Def - Constructions on Representations|dual]]** $\varrho^*$ acts on $V^* = \operatorname{Hom}(V, \mathbb{C})$ by $\varrho^*(g) = \varrho(g^{-1})^*$ (the transpose/adjoint precomposition), and the **[[Def - Constructions on Representations|symmetric power]]** $\odot^k \varrho$ acts on the space $\odot^k V$ of symmetric tensors by $g \mapsto \varrho(g)^{\odot k}$, where $u_1 \odot \dots \odot u_k$ denotes the symmetric product and $\varrho(g)^{\odot k}(u_1 \odot \dots \odot u_k) = \varrho(g)u_1 \odot \dots \odot \varrho(g)u_k$. We recall from that page that $\dim_{\mathbb{C}} \odot^k \mathbb{C}^2 = k + 1$.

The **Lie algebra** of $G$ is $\mathfrak{g} = T_e G \subseteq \operatorname{Mat}(2 \times 2; \mathbb{C})$ with bracket the commutator $[X, Y] = XY - YX$; we have $\mathfrak{u}(1) = i\mathbb{R}$ and $\mathfrak{su}(2) = \{A : A^* = -A,\ \operatorname{tr} A = 0\}$, a real $3$-dimensional space. A **[[Def - Representation of a Lie Algebra|representation]]** of a Lie algebra $\mathfrak{g}$ on $V$ is a Lie algebra homomorphism $\lambda \colon \mathfrak{g} \to \operatorname{End}(V)$, that is a linear map with $\lambda([X, Y]) = \lambda(X)\lambda(Y) - \lambda(Y)\lambda(X)$. For a group representation $\varrho$ we write $\varrho_* = d_e \varrho \colon \mathfrak{g} \to \operatorname{End}(V)$ for its **differential**, the induced Lie algebra representation. We use the standard **[[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices|anti-Hermitian Pauli basis]]** of $\mathfrak{su}(2)$,
$$X_1 := -i\sigma_1 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad X_2 := -i\sigma_2 = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}, \qquad X_3 := -i\sigma_3 = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix},$$
whose brackets are $[X_a, X_b] = 2\,\varepsilon_{abc}\, X_c$ (with $\varepsilon_{abc}$ the totally antisymmetric symbol, $\varepsilon_{123} = 1$). The complexification $\mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{su}(2) \otimes_{\mathbb{R}} \mathbb{C} = \mathfrak{sl}(2; \mathbb{C})$ carries the standard $\mathfrak{sl}_2$-triple
$$H = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = -iX_3, \qquad E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \tfrac12(X_1 - iX_2), \qquad F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = -\tfrac12(X_1 + iX_2),$$
with the relations $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. The **[[Thm - Ad is a Smooth Representation and its Differential is ad|adjoint representation]]** is $\operatorname{Ad} \colon G \to GL(\mathfrak{g})$, $\operatorname{Ad}_g X = gXg^{-1}$ for a matrix group, with differential $\operatorname{ad} = \operatorname{Ad}_* \colon \mathfrak{g} \to \operatorname{End}(\mathfrak{g})$, $\operatorname{ad}(X)Y = [X, Y]$. Its complexification $(\operatorname{Ad}_{SU(2)})_{\mathbb{C}} \colon SU(2) \to GL(\mathfrak{su}(2)_{\mathbb{C}})$ is the representation on the complex $3$-dimensional space $\mathfrak{su}(2)_{\mathbb{C}}$ obtained by extending each real-linear $\operatorname{Ad}_g$ complex-linearly; its differential is $(\operatorname{ad})_{\mathbb{C}}$, the adjoint representation of $\mathfrak{sl}(2; \mathbb{C})$ on itself.

The full symbol registry for the chapter is on the parent page **[[Gauge Theory I — Lie Groups, Representations, and Group Actions]]**.

> [!warning] Convention: Bär's Pauli labelling
> The lecture notes we transcribe (Bär–Wernli §1.3) write the anti-Hermitian basis as $-i\sigma_1 = \left(\begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}\right)$, $-i\sigma_2 = \left(\begin{smallmatrix} 0 & i \\ i & 0 \end{smallmatrix}\right)$, $-i\sigma_3 = \left(\begin{smallmatrix} i & 0 \\ 0 & -i \end{smallmatrix}\right)$ (the matrices $X_1, X_2, X_3$ printed above). Solving $\sigma_a = iX_a$ from $X_a = -i\sigma_a$, their Pauli matrices are $\sigma_1 = \left(\begin{smallmatrix} 0 & i \\ -i & 0 \end{smallmatrix}\right)$, $\sigma_2 = \left(\begin{smallmatrix} 0 & -1 \\ -1 & 0 \end{smallmatrix}\right)$, $\sigma_3 = \left(\begin{smallmatrix} -1 & 0 \\ 0 & 1 \end{smallmatrix}\right)$, which are the standard Pauli matrices $\sigma_1^{\mathrm{std}} = \left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$, $\sigma_2^{\mathrm{std}} = \left(\begin{smallmatrix} 0 & -i \\ i & 0 \end{smallmatrix}\right)$, $\sigma_3^{\mathrm{std}} = \left(\begin{smallmatrix} 1 & 0 \\ 0 & -1 \end{smallmatrix}\right)$ with the first two interchanged and all three negated: $\sigma_1 = -\sigma_2^{\mathrm{std}}$, $\sigma_2 = -\sigma_1^{\mathrm{std}}$, $\sigma_3 = -\sigma_3^{\mathrm{std}}$. (The source itself never prints $\sigma_1, \sigma_2$ explicitly — it only lists the three $-i\sigma_a$ and calls them "$-i$ times the Pauli matrices", a nonstandard labelling; we record the exact matrices for definiteness.) Every matrix identity in Part (C) below is stated in the basis $(X_1, X_2, X_3)$ so that our numbers match the source line by line; the bracket relations $[X_a, X_b] = 2\varepsilon_{abc} X_c$ hold verbatim, as recorded on **[[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices]]**.

---

# Statement

> **Theorem (complex representation theory of $U(1)$ and $SU(2)$).**
>
> **(A) The circle group.** For each integer $k \in \mathbb{Z}$ let $\varrho_k \colon U(1) \to GL(1; \mathbb{C}) = \mathbb{C}^\times$ be $\varrho_k(z) = z^k$; here $\varrho_0$ is the trivial representation and $\varrho_1 = \varrho_{\mathrm{st}}$ is the standard representation. Then:
> 1. each $\varrho_k$ is irreducible, and $\varrho_k \not\cong \varrho_l$ for $k \neq l$;
> 2. every finite-dimensional complex representation of $U(1)$ is equivalent to a direct sum $\varrho_{k_1} \oplus \dots \oplus \varrho_{k_n}$ of the $\varrho_k$, and the multiset $\{k_1, \dots, k_n\}$ is uniquely determined by the representation (uniqueness up to the order of the summands);
> 3. $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$ and $\varrho_k^* \cong \varrho_{-k}$.
>
> **(B) The special unitary group.** Let $\varrho_0$ be the trivial representation of $SU(2)$ on $\mathbb{C}$, let $\varrho_1 = \varrho_{\mathrm{st}}$ be the standard representation on $\mathbb{C}^2$, and for $k \geq 2$ let $\varrho_k := \odot^k \varrho_1$ act on $\odot^k \mathbb{C}^2$, a complex vector space of dimension $k + 1$. Then:
> 1. each $\varrho_k$ ($k \geq 0$) is irreducible, and $\varrho_k \not\cong \varrho_l$ for $k \neq l$;
> 2. every finite-dimensional complex representation of $SU(2)$ is equivalent to a direct sum of the $\varrho_k$, uniquely up to the order of the summands.
>
> **(C) The complexified adjoint representation.** For $SU(2)$ one has $\varrho_2 \cong (\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$; among all the $\varrho_k$ only $\varrho_2$ can be equivalent to it, because $(\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ has complex dimension $\dim_{\mathbb{R}} \mathfrak{su}(2) = 3 = \dim_{\mathbb{C}} \varrho_2$. An explicit intertwiner, expressed in the basis $(e_1 \odot e_1,\ e_2 \odot e_2,\ e_2 \odot e_1)$ of $\odot^2 \mathbb{C}^2$ and the basis $(X_1, X_2, X_3)$ of $\mathfrak{su}(2)_{\mathbb{C}}$, is
> $$S = \begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix}, \qquad S \circ \operatorname{Ad}_g = \varrho_2(g) \circ S \quad \text{for every } g \in SU(2).$$

Together, (A) and (B) say that we know the *entire* finite-dimensional complex representation theory of both groups: an irreducible is a $\varrho_k$, and a general representation is a direct sum of these, with the summands read off from invariants of the representation.

---

# Motivation

The theorem is the whole reason gauge theory can compute. A gauge field with structure group $G$ produces, from any representation $\varrho \colon G \to GL(V)$, an associated vector bundle $P \times_\varrho V$ whose sections are the matter fields on which the field acts; the connection and its curvature act on that bundle through $\varrho$. Which bundles arise, and how they multiply and dualise, is exactly the content of the representation theory of $G$. For the two groups that carry almost all of low-dimensional gauge theory — $U(1)$ of electromagnetism and $SU(2)$ of the Seiberg–Witten and Donaldson equations — this theorem hands us a complete and finite catalogue.

The catalogue is as clean as one could hope. For $U(1)$ the irreducibles are indexed by a single integer $k$, the **charge** or **weight**: $\varrho_k(z) = z^k$. The tensor and dual rules $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$ and $\varrho_k^* \cong \varrho_{-k}$ say that charge is additive and that dualising negates it, so the associated line bundles of a principal $U(1)$-bundle $P$ are precisely the integer tensor powers $L^{\otimes k}$ of the single line bundle $L = P \times_{\varrho_1} \mathbb{C}$. This is why a magnetic charge, a first Chern number, or a winding number is one integer. For $SU(2)$ the irreducibles are again indexed by one nonnegative integer $k$ — the physicist's spin $j = k/2$ — with $\dim \varrho_k = k + 1$; the symmetric powers $\odot^k \mathbb{C}^2$ realise them all, and the case $k = 2$ recovers the adjoint (spin-$1$) representation on the Lie algebra itself, which is the representation in which the curvature $F_A$ of an $SU(2)$-connection lives.

The question the theorem answers is therefore not "does a classification exist" but "what forces it to be this simple". Two mechanisms conspire. Compactness (the existence of an invariant integral, the *unitarian trick*) forces every representation to be a direct sum of irreducibles, so we only ever have to understand the irreducibles. And the connectedness of the groups lets us pass to the Lie algebra, where the single relation $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$ of $\mathfrak{sl}(2; \mathbb{C})$ pins the irreducibles down completely by a ladder argument on the eigenvalues of $H$. The classification is simple because a compact connected group of rank one has essentially one knob to turn.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis of each part is mild — a finite-dimensional complex representation of a fixed compact group — so the real question is which problems secretly present such a representation.

The first disguised source is **any natural bundle or tensor construction on a $U(1)$- or $SU(2)$-space**. Whenever one has a principal bundle with one of these structure groups, every functor of vector spaces applied fibrewise — tensor powers, symmetric and exterior powers, duals, homomorphism spaces, the complexified adjoint bundle — is an associated bundle for *some* representation, and the theorem decomposes it. The non-obvious bridge is that a geometric operation one performs without thinking about groups ("take $\operatorname{End}$ of the spinor bundle", "square the determinant line") is the application of a representation, so its irreducible content is dictated by (A) or (B). *Example problem:* decompose the bundle $\operatorname{End}(E)$ of a rank-two $SU(2)$-bundle $E$; since $\operatorname{End}(\mathbb{C}^2) \cong \varrho_1 \otimes \varrho_1^*$ and the Clebsch–Gordan rule $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$ combines with self-duality of $\varrho_1$, one finds $\operatorname{End}(E) \cong (\text{adjoint } \varrho_2) \oplus (\text{trivial line})$, the trace-free and trace parts.

The second disguised source is **a linear action of the group that one can prove is unitary or lands in a compact image**. Any homomorphism $\varrho \colon G \to GL(V)$ from $U(1)$ or $SU(2)$ is automatically a representation to which the theorem applies, but sometimes an action appears as a symmetry of a differential operator, a Hilbert space of states, or a moduli problem, and one must first recognise it as finite-dimensional and continuous. The bridge is that continuity plus compactness already forces the averaged Hermitian inner product of Lemma 1 to exist, so no separate unitarity hypothesis is needed. *Example problem:* the space of harmonic polynomials of degree $k$ on $\mathbb{R}^3$ carries an $SO(3)$-action; pulling back along the double cover $SU(2) \to SO(3)$ gives an $SU(2)$-representation, which the theorem identifies as $\varrho_{2k}$.

The third disguised source is **an abelian symmetry inside a larger group**, through restriction to a maximal torus. Every representation of $SU(2)$ restricts to a representation of the diagonal circle $U(1) \subset SU(2)$, and by (A) that restriction is a sum of characters $z \mapsto z^m$ — the **weights**. The bridge is that the multiset of weights is computable and, by Lemma 4, already determines the $SU(2)$-representation up to equivalence. *Example problem:* to decide whether two $SU(2)$-representations are equivalent, compute and compare their weight multiplicities on the torus; the theorem guarantees this finite check is decisive.

**Targets (Output Amplification).** The classification combines with further data to do more than list irreducibles.

Combine (A) with **a principal $U(1)$-bundle $P$**. Each representation $\varrho_k$ produces an associated line bundle $P \times_{\varrho_k} \mathbb{C}$, and the tensor rule $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$ upgrades to the isomorphism of line bundles $P \times_{\varrho_k} \mathbb{C} \cong L^{\otimes k}$ where $L = P \times_{\varrho_1} \mathbb{C}$; the dual rule gives $L^{\otimes(-k)} = (L^{\otimes k})^*$. The payoff is that the entire tower of line bundles built from a $U(1)$-bundle is generated by one line bundle under tensor product, so that the classification of $U(1)$-bundles reduces to one integer invariant (chapter III).

Combine (B) with **the standard representation and the Clebsch–Gordan problem**. Knowing the irreducibles and complete reducibility, any tensor product $\varrho_k \otimes \varrho_l$ decomposes as $\varrho_{k+l} \oplus \varrho_{k+l-2} \oplus \dots \oplus \varrho_{|k-l|}$, computed purely from weights. The payoff is a complete multiplication table for $SU(2)$-representations, which is what lets one couple spinor fields and read off the field content of a tensor product of matter fields (chapter VIII).

Combine (C) with **the curvature of an $SU(2)$-connection**. Because $\varrho_2 \cong (\operatorname{Ad})_{\mathbb{C}}$, the curvature two-form $F_A$, which is $\mathfrak{su}(2)$-valued and transforms by $\operatorname{Ad}$ under gauge changes, is a section of a bundle built from $\varrho_2$; the intertwiner $S$ identifies it, up to complexification, with a section of $\odot^2 E$. The payoff is that adjoint-valued objects — curvature, the Higgs field of Seiberg–Witten theory, infinitesimal gauge transformations — are all governed by the single irreducible $\varrho_2$, so their pointwise algebra is the algebra of the spin-$1$ representation.

---

# Why Is It True

Two independent forces produce the classification, and it helps to separate them.

The first is **compactness, which makes every representation unitary and hence completely reducible**. On a compact group there is a translation-invariant way to average — the normalised integral $\frac{1}{2\pi}\int_0^{2\pi} d\theta$ on $U(1)$, the normalised round volume on $SU(2) \cong S^3$ — and averaging any Hermitian inner product over the group produces one for which every $\varrho(g)$ is unitary. Once the operators are unitary, the orthogonal complement of an invariant subspace is again invariant, so a representation with a proper invariant subspace splits off that subspace as a direct summand; iterating, every representation is a direct sum of irreducibles. This is the *unitarian trick*, and it reduces the whole problem to classifying irreducibles.

The second force is **connectedness, which lets the single relation of the rank-one Lie algebra pin the irreducibles down by a ladder**. For $U(1)$ the group is abelian, so the operators $\varrho(z)$ all commute and share an eigenvector; the eigenline is invariant, so an irreducible is one-dimensional, and a one-dimensional representation is a continuous character, which the covering $\mathbb{R} \to U(1)$ forces to be $z \mapsto z^k$. For $SU(2)$ the group is connected but not abelian, and here one passes to the complexified Lie algebra $\mathfrak{sl}(2; \mathbb{C})$, where the operators $H, E, F$ obey $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. In an irreducible, $E$ raises the $H$-eigenvalue by $2$ and $F$ lowers it by $2$; starting from a top eigenvector (which exists because the eigenvalue set is finite) and applying $F$ repeatedly produces a finite ladder $n, n-2, \dots, -n$ that must close up, forcing the top weight $n$ to be a nonnegative integer and the whole representation to have dimension $n + 1$. The symmetric powers $\odot^k \mathbb{C}^2$ realise exactly these ladders.

> **The one-sentence mechanism:** compactness collapses every representation into a sum of irreducibles, and the raising–lowering ladder of the rank-one algebra $\mathfrak{sl}_2$ shows each irreducible is a symmetric power of the standard representation, indexed by the length of its ladder.

One numerical fact makes the integrality visible without the ladder. In $SU(2)$ the diagonal one-parameter subgroup satisfies $\exp(2\pi X_3) = \operatorname{diag}(e^{2\pi i}, e^{-2\pi i}) = 1$, and $X_3 = iH$, so $\exp(2\pi i H) = 1$. In any representation $\varrho$ this gives $\exp(2\pi i\, \varrho_*(H)) = \varrho(1) = \operatorname{id}$, which forces every eigenvalue of $\varrho_*(H)$ to be an integer: the weights of $SU(2)$ are integers because a full rotation must act trivially.

---

# What Makes This Hard

The genuine difficulty is not any single step but knowing which of the two forces to invoke where, and not conflating them: complete reducibility is a *global* statement about the compact group and cannot be seen from the Lie algebra alone (the Lie algebra of a compact group need not have completely reducible representations if one forgets the group — the extra input is the invariant integral), whereas the classification of irreducibles is a *local* statement most cleanly proved on the complexified Lie algebra and then transported back by connectedness. The common error is to try to classify irreducibles directly on the group, where the exponential is not surjective onto a coordinate chart, instead of on $\mathfrak{sl}(2; \mathbb{C})$ where the ladder argument lives; the second common error, made even in careful lecture notes, is to verify the adjoint intertwiner of Part (C) only on the diagonal maximal torus and then assert it holds everywhere — it does not, because an intertwiner is constrained by the whole group and the torus determines it only up to a diagonal rescaling that must be fixed by a non-toral element.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce every representation to a sum of irreducibles by averaging an inner product over the compact group (unitarian trick). Classify the irreducibles: for $U(1)$ they are one-dimensional characters $z \mapsto z^k$; for $SU(2)$ pass to $\mathfrak{sl}(2; \mathbb{C})$, run the raising–lowering ladder to get one irreducible $L(n)$ of each dimension $n+1$, and identify $L(n)$ with $\odot^n \mathbb{C}^2$ by computing weights. Transport between group and algebra using connectedness, and settle Part (C) by an explicit intertwiner checked on the three Lie-algebra generators.

**Subgoal decomposition:**

1. **Invariant integral and complete reducibility.** Build a normalised translation-invariant integral on each group and average an inner product; deduce every representation splits into irreducibles.
   - *Hint:* on $SU(2) \cong S^3$ use that left multiplication by a unit quaternion is an isometry of $\mathbb{R}^4$.
   - *Why needed:* it lets us study only irreducibles.

2. **Abelian irreducibles are one-dimensional.** A commuting family of operators on a complex space has a common eigenvector.
   - *Hint:* induct on dimension using an eigenspace of one non-scalar operator.
   - *Why needed:* it reduces $U(1)$ to characters.

3. **Characters of $U(1)$.** Every continuous homomorphism $U(1) \to U(1)$ is $z \mapsto z^k$.
   - *Hint:* lift through the covering $\mathbb{R} \to U(1)$, $\theta \mapsto e^{i\theta}$, to a continuous additive $\Phi \colon \mathbb{R} \to \mathbb{R}$.
   - *Why needed:* it identifies the one-dimensional representations as the $\varrho_k$.

4. **Uniqueness of the decomposition.** Multiplicities are dimensions of weight spaces, intrinsic to the representation.
   - *Hint:* the weight-$k$ space is $\{v : \varrho(z)v = z^k v\}$.
   - *Why needed:* it gives uniqueness up to order.

5. **Group–algebra dictionary.** For connected $G$, invariance and intertwining for the group are equivalent to the same for the Lie algebra.
   - *Hint:* $\varrho(\exp X) = e^{\varrho_*(X)}$ and a connected group is generated by a neighbourhood of the identity.
   - *Why needed:* it moves the classification to $\mathfrak{sl}_2$ and the intertwiner check of (C) to three generators.

6. **Irreducibles of $\mathfrak{sl}(2; \mathbb{C})$.** For each $n \geq 0$ a unique irreducible $L(n)$ of dimension $n+1$, with weights $n, n-2, \dots, -n$.
   - *Hint:* a highest-weight vector $v_0$ with $Ev_0 = 0$; set $v_j = F^j v_0$ and compute $E v_j = j(n - j + 1)v_{j-1}$.
   - *Why needed:* it is the list of $SU(2)$-irreducibles.

7. **Symmetric powers realise them.** $\odot^k \mathbb{C}^2 \cong L(k)$.
   - *Hint:* the basis $e_1^{\odot(k-j)} \odot e_2^{\odot j}$ has $H$-weight $k - 2j$.
   - *Why needed:* it names each $SU(2)$-irreducible as a concrete $\varrho_k$ and gives Part (C) via $\varrho_2 = L(2) = (\operatorname{ad})_{\mathbb{C}}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Unitarian trick — compact groups have completely reducible representations
> **Statement:** Let $G$ be $U(1)$ or $SU(2)$ and $\varrho \colon G \to GL(V)$ a finite-dimensional complex representation. Then $V$ carries a $\varrho$-invariant Hermitian inner product (one with $\langle \varrho(g)v, \varrho(g)w \rangle = \langle v, w \rangle$ for all $g, v, w$), so each $\varrho(g)$ is [[Def - Unitary Operator|unitary]]; consequently $\varrho$ is completely reducible.
>
> **Hint:** average any inner product over the normalised invariant integral of $G$; the orthogonal complement of an invariant subspace is invariant.
>
> **Why needed:** it reduces the classification of all representations to the classification of the irreducibles.
>
> > [!note]- Full proof
> > **Step 0 — a normalised invariant integral on $G$.** We do not need the general Haar theorem, only these two groups, so we exhibit the integral concretely.
> >
> > On $U(1)$, for a continuous function $f \colon U(1) \to \mathbb{C}$ set $\displaystyle \int_{U(1)} f := \frac{1}{2\pi}\int_0^{2\pi} f(e^{i\theta})\, d\theta$. This is normalised, $\int_{U(1)} 1 = 1$, and it is translation-invariant: for fixed $z_0 = e^{i\theta_0}$,
> > $$\int_{U(1)} f(z_0 \cdot) = \frac{1}{2\pi}\int_0^{2\pi} f(e^{i(\theta_0 + \theta)})\, d\theta = \frac{1}{2\pi}\int_{\theta_0}^{\theta_0 + 2\pi} f(e^{i\varphi})\, d\varphi = \int_{U(1)} f \qquad \text{(substitution } \varphi = \theta_0 + \theta \text{, then } 2\pi\text{-periodicity of the integrand).}$$
> >
> > On $SU(2)$, identify $SU(2) \cong S^3 \subset \mathbb{H} = \mathbb{R}^4$ with the unit quaternions (the isomorphism $Sp(1) \to SU(2)$, $z + wj \mapsto \left(\begin{smallmatrix} z & w \\ -\bar w & \bar z \end{smallmatrix}\right)$, of **[[Ex - SU(2) is the Group of Unit Quaternions]]**). Let $\mu$ be the Riemannian volume density of the round metric that $S^3$ inherits from the Euclidean $\mathbb{R}^4$, normalised so that $\mu(S^3) = 1$, and set $\int_{SU(2)} f := \int_{S^3} f\, d\mu$. For a fixed unit quaternion $q_0 \in S^3$, left multiplication $L_{q_0} \colon \mathbb{H} \to \mathbb{H}$, $x \mapsto q_0 x$, is $\mathbb{R}$-linear, and $|q_0 x| = |q_0|\,|x| = |x|$ (the quaternion norm is multiplicative and $|q_0| = 1$), so $L_{q_0} \in O(4)$. An orthogonal linear map of $\mathbb{R}^4$ restricts to an isometry of the unit sphere $S^3$ and therefore preserves its Riemannian volume density $\mu$; hence
> > $$\int_{SU(2)} f(q_0 \cdot) = \int_{S^3} f(q_0 q)\, d\mu(q) = \int_{S^3} f\, d\mu = \int_{SU(2)} f \qquad \text{(change of variables under the } \mu\text{-preserving diffeomorphism } L_{q_0}\text{).}$$
> > Right multiplication $R_{q_0}$ is orthogonal by the same computation, so the integral is invariant under translation on both sides. In either case we write $\int_G$ for the resulting normalised bi-invariant integral, and we note that for a *continuous* $\mathbb{C}$-valued integrand the integral exists because $G$ is compact.
> >
> > **Step 1 — averaging an inner product.** Choose any Hermitian inner product $\langle \cdot, \cdot \rangle_0$ on $V$ (for instance, fix a basis and use the standard one). Define
> > $$\langle v, w \rangle := \int_G \langle \varrho(g)v, \varrho(g)w \rangle_0 \, dg.$$
> > The integrand $g \mapsto \langle \varrho(g)v, \varrho(g)w \rangle_0$ is continuous, being the composition of the continuous map $\varrho$ with the continuous inner product, so the integral exists by Step 0 (compute it in a fixed basis of $V$: it is the integral of a continuous $\mathbb{C}$-valued function on the compact $G$).
> >
> > We verify $\langle \cdot, \cdot \rangle$ is a Hermitian inner product clause by clause. It is linear in the first slot and conjugate-linear in the second because $\langle \cdot, \cdot \rangle_0$ is and the integral is linear. It is conjugate-symmetric: $\langle w, v \rangle = \int_G \langle \varrho(g)w, \varrho(g)v \rangle_0\, dg = \int_G \overline{\langle \varrho(g)v, \varrho(g)w \rangle_0}\, dg = \overline{\langle v, w \rangle}$ (conjugate symmetry of $\langle \cdot, \cdot \rangle_0$; the integral of the complex conjugate is the conjugate of the integral, since $\int_G$ has real values on real integrands). It is positive-definite: $\langle v, v \rangle = \int_G \|\varrho(g)v\|_0^2\, dg \geq 0$, and if $\langle v, v \rangle = 0$ then the continuous nonnegative integrand $g \mapsto \|\varrho(g)v\|_0^2$ has integral zero over a set of positive total measure, so it vanishes identically; evaluating at $g = e$ gives $\|v\|_0^2 = 0$, hence $v = 0$.
> >
> > **Step 2 — invariance.** For $h \in G$,
> > $$\langle \varrho(h)v, \varrho(h)w \rangle = \int_G \langle \varrho(g)\varrho(h)v, \varrho(g)\varrho(h)w \rangle_0\, dg = \int_G \langle \varrho(gh)v, \varrho(gh)w \rangle_0\, dg \qquad \text{(} \varrho \text{ a homomorphism: } \varrho(g)\varrho(h) = \varrho(gh) \text{)}$$
> > $$= \int_G \langle \varrho(g')v, \varrho(g')w \rangle_0\, dg' = \langle v, w \rangle \qquad \text{(right-invariance of } \int_G \text{, substitution } g' = gh \text{).}$$
> > Thus $\langle \cdot, \cdot \rangle$ is $\varrho$-invariant, which is precisely the statement that each $\varrho(h)$ preserves it, i.e. is unitary for $\langle \cdot, \cdot \rangle$.
> >
> > **Step 3 — complete reducibility, by induction on $\dim V$.** If $V = 0$ the empty direct sum works; if $V$ is irreducible it is its own single irreducible summand. Otherwise there is an invariant subspace $U$ with $0 \neq U \neq V$. Let $U^\perp = \{w \in V : \langle w, u \rangle = 0\ \forall u \in U\}$ be the orthogonal complement for the invariant inner product; then $V = U \oplus U^\perp$ as vector spaces. We claim $U^\perp$ is invariant. For $w \in U^\perp$, $g \in G$, and $u \in U$,
> > $$\langle \varrho(g)w, u \rangle = \langle w, \varrho(g)^{-1}u \rangle \qquad \text{(each } \varrho(g) \text{ is unitary, so } \varrho(g)^* = \varrho(g)^{-1} \text{, by Step 2)}$$
> > $$= \langle w, \varrho(g^{-1})u \rangle = 0 \qquad \text{(} \varrho(g^{-1})u \in U \text{ since } U \text{ is invariant, and } w \perp U \text{).}$$
> > As $u \in U$ was arbitrary, $\varrho(g)w \in U^\perp$; so $U^\perp$ is invariant. Now $V = U \oplus U^\perp$ is a direct sum of two invariant subspaces of strictly smaller dimension, and by the induction hypothesis each of $\varrho|_U$ and $\varrho|_{U^\perp}$ is a direct sum of irreducibles. Therefore $V$ is a direct sum of irreducibles. $\blacksquare$

> [!note]- Lemma 2: An irreducible representation of an abelian group is one-dimensional
> **Statement:** If $G$ is abelian and $\varrho \colon G \to GL(V)$ is an irreducible complex representation on a nonzero finite-dimensional $V$, then $\dim_{\mathbb{C}} V = 1$.
>
> **Hint:** the operators $\varrho(g)$ commute; a commuting family on a complex vector space has a common eigenvector, whose line is invariant.
>
> **Why needed:** it collapses the whole representation theory of $U(1)$ to one-dimensional characters.
>
> > [!note]- Full proof
> > **The operators commute.** Since $G$ is abelian and $\varrho$ is a homomorphism, $\varrho(g)\varrho(h) = \varrho(gh) = \varrho(hg) = \varrho(h)\varrho(g)$ for all $g, h \in G$; so $\mathcal{F} := \{\varrho(g) : g \in G\}$ is a commuting family in $\operatorname{End}(V)$.
> >
> > **A commuting family has a common eigenvector.** We show, by induction on $\dim V \geq 1$, that any commuting family $\mathcal{F} \subseteq \operatorname{End}(V)$ on a nonzero finite-dimensional complex space has a vector $v_0 \neq 0$ that is an eigenvector of every member. If every $A \in \mathcal{F}$ is a scalar multiple of the identity, any nonzero $v_0$ works. Otherwise fix $A \in \mathcal{F}$ that is not scalar. Over $\mathbb{C}$ the characteristic polynomial of $A$ has a root, so $A$ has an eigenvalue $\lambda$; its eigenspace $E_\lambda = \ker(A - \lambda\,\mathrm{id})$ is nonzero, and $E_\lambda \neq V$ because $A$ is not scalar. Every $B \in \mathcal{F}$ preserves $E_\lambda$: for $v \in E_\lambda$,
> > $$A(Bv) = B(Av) = B(\lambda v) = \lambda(Bv) \qquad \text{(} A \text{ and } B \text{ commute),}$$
> > so $Bv \in E_\lambda$. Thus $\{B|_{E_\lambda} : B \in \mathcal{F}\}$ is a commuting family on $E_\lambda$, which has strictly smaller dimension; by the induction hypothesis it has a common eigenvector $v_0 \in E_\lambda$, and $v_0$ is then a common eigenvector of $\mathcal{F}$ on $V$.
> >
> > **Conclusion.** Let $v_0 \neq 0$ be a common eigenvector of $\mathcal{F}$. Then $\varrho(g)v_0 \in \mathbb{C}v_0$ for every $g$, so the line $\mathbb{C}v_0$ is an invariant subspace. Since $\varrho$ is irreducible and $\mathbb{C}v_0 \neq 0$, we must have $\mathbb{C}v_0 = V$, i.e. $\dim_{\mathbb{C}} V = 1$. $\blacksquare$

> [!note]- Lemma 3: Every continuous homomorphism $U(1) \to U(1)$ is $z \mapsto z^k$
> **Statement:** Let $\chi \colon U(1) \to U(1)$ be a continuous group homomorphism. Then there is a unique integer $k \in \mathbb{Z}$ with $\chi(z) = z^k$ for all $z$. Consequently every one-dimensional complex representation of $U(1)$ is equivalent to exactly one $\varrho_k$.
>
> **Hint:** lift $t \mapsto \chi(e^{it})$ through the universal covering $p \colon \mathbb{R} \to U(1)$, $p(t) = e^{it}$, to a continuous additive $\Phi \colon \mathbb{R} \to \mathbb{R}$.
>
> **Why needed:** it identifies the one-dimensional representations of $U(1)$, which by Lemmas 1 and 2 are all the irreducibles.
>
> > [!note]- Full proof
> > **Step 0 — reduce a one-dimensional representation to a character.** A one-dimensional complex representation of $U(1)$ is a continuous homomorphism $\chi \colon U(1) \to GL(1; \mathbb{C}) = \mathbb{C}^\times$. By Lemma 1 it preserves some Hermitian inner product on $\mathbb{C}$; a Hermitian inner product on $\mathbb{C}$ is $\langle a, b \rangle = c\,a\bar b$ with $c > 0$, and preservation forces $|\chi(z)|^2 = 1$, so $\chi(z) \in U(1)$ for all $z$. Thus it suffices to treat homomorphisms $\chi \colon U(1) \to U(1)$.
> >
> > **Step 1 — lift through the covering.** The map $p \colon \mathbb{R} \to U(1)$, $p(t) = e^{it}$, is a smooth [[Def - Covering Space|covering map]]. Consider the continuous map $\gamma \colon \mathbb{R} \to U(1)$, $\gamma(t) = \chi(e^{it})$. By the [[Thm - Path Lifting and Homotopy Lifting|path-lifting property]] of a covering — *for a covering $p \colon \tilde X \to X$, a path $\gamma \colon [0, T] \to X$, and a point $\tilde x_0 \in \tilde X$ with $p(\tilde x_0) = \gamma(0)$, there is a unique continuous $\tilde\gamma \colon [0, T] \to \tilde X$ with $p \circ \tilde\gamma = \gamma$ and $\tilde\gamma(0) = \tilde x_0$* — we lift $\gamma$ on each interval $[0, T]$ starting from $\Phi(0) = 0$; uniqueness of lifts makes these agree on overlaps, so they assemble into a single continuous $\Phi \colon \mathbb{R} \to \mathbb{R}$ with $\Phi(0) = 0$ and
> > $$e^{i\Phi(t)} = \chi(e^{it}) \qquad \text{for all } t \in \mathbb{R}.$$
> >
> > **Step 2 — $\Phi$ is additive.** Fix $s \in \mathbb{R}$ and consider the two continuous functions $t \mapsto \Phi(s + t) - \Phi(s)$ and $t \mapsto \Phi(t)$. Both vanish at $t = 0$, and both are lifts through $p$ of the same map $t \mapsto \chi(e^{it})$: for the first,
> > $$e^{i(\Phi(s+t) - \Phi(s))} = \frac{\chi(e^{i(s+t)})}{\chi(e^{is})} = \frac{\chi(e^{is})\chi(e^{it})}{\chi(e^{is})} = \chi(e^{it}) \qquad \text{(} \chi \text{ a homomorphism),}$$
> > and for the second $e^{i\Phi(t)} = \chi(e^{it})$ by construction. By the uniqueness of lifts with a given initial value, the two functions coincide: $\Phi(s + t) - \Phi(s) = \Phi(t)$, i.e. $\Phi(s + t) = \Phi(s) + \Phi(t)$ for all $s, t$.
> >
> > **Step 3 — a continuous additive map is linear.** Set $c := \Phi(1)$. Additivity gives $\Phi(n) = n c$ for $n \in \mathbb{Z}$ (induction and $\Phi(-t) = -\Phi(t)$), and $q\,\Phi(p/q) = \Phi(p) = pc$ so $\Phi(p/q) = (p/q)c$ for $p/q \in \mathbb{Q}$. Every real $t$ is a limit of rationals $r_n \to t$, and $\Phi$ is continuous, so $\Phi(t) = \lim_n \Phi(r_n) = \lim_n r_n c = tc$. Hence $\Phi(t) = ct$.
> >
> > **Step 4 — integrality and conclusion.** Since $e^{2\pi i} = 1$, we have $\chi(e^{2\pi i}) = \chi(1) = 1$, so $e^{i\Phi(2\pi)} = 1$, giving $\Phi(2\pi) = 2\pi c \in 2\pi\mathbb{Z}$; therefore $c = k$ is an integer. Then for all $t$,
> > $$\chi(e^{it}) = e^{i\Phi(t)} = e^{ikt} = (e^{it})^k,$$
> > i.e. $\chi(z) = z^k = \varrho_k(z)$ for all $z \in U(1)$. Uniqueness of $k$: if $z^k = z^l$ for all $z \in U(1)$ then $z^{k-l} = 1$ for all $z$; taking $z = e^{i\pi/(k-l)}$ when $k \neq l$ gives $e^{i\pi} = -1 = 1$, a contradiction, so $k = l$. Finally, an equivalence of the one-dimensional representations $\varrho_k$ and $\varrho_l$ is a nonzero scalar $T$ with $T z^k = z^l T$ for all $z$, i.e. $z^k = z^l$, so $\varrho_k \cong \varrho_l$ if and only if $k = l$. $\blacksquare$

> [!note]- Lemma 4: Multiplicities are weight-space dimensions, hence the decomposition is unique
> **Statement:** Let $\varrho \colon G \to GL(V)$ be a finite-dimensional complex representation.
> (i) If $G = U(1)$ and $V \cong \bigoplus_i \varrho_{k_i}$, then for each $k$ the number of indices $i$ with $k_i = k$ equals $\dim V_k$, where $V_k := \{v \in V : \varrho(z)v = z^k v\ \forall z \in U(1)\}$; the multiset $\{k_i\}$ is therefore determined by $\varrho$.
> (ii) If $G = SU(2)$ and $V \cong \bigoplus_k \varrho_k^{\oplus m_k}$, then $m_k = \dim V_k^{T} - \dim V_{k+2}^{T}$ for $k \geq 0$, where $V_j^{T} := \{v \in V : \varrho(\operatorname{diag}(e^{i\theta}, e^{-i\theta}))v = e^{ij\theta} v\ \forall \theta\}$; the multiplicities are therefore determined by $\varrho$.
>
> **Hint:** a weight space is cut out by the representation and does not see the chosen decomposition; for $SU(2)$ restrict to the diagonal circle and use the weights of each $\varrho_k$ from Lemma 7.
>
> **Why needed:** it upgrades "a direct sum of $\varrho_k$'s exists" to "unique up to the order of the summands".
>
> > [!note]- Full proof
> > **(i) The circle.** Suppose $V = \bigoplus_i W_i$ with $W_i \cong \varrho_{k_i}$, so $\varrho(z)$ acts on $W_i$ as multiplication by $z^{k_i}$. Fix $k$. We claim $V_k = \bigoplus_{i : k_i = k} W_i$. The inclusion "$\supseteq$" is immediate: on each $W_i$ with $k_i = k$, $\varrho(z)$ is multiplication by $z^k$. For "$\subseteq$", take $v \in V_k$ and write $v = \sum_i w_i$ with $w_i \in W_i$. Then
> > $$\sum_i z^{k_i} w_i = \varrho(z)v = z^k v = \sum_i z^k w_i \qquad \text{for all } z,$$
> > and by directness of the sum, $z^{k_i} w_i = z^k w_i$ for every $i$ and every $z$; if $k_i \neq k$ this forces $w_i = 0$. Hence $v \in \bigoplus_{i : k_i = k} W_i$. Taking dimensions, $\dim V_k = \#\{i : k_i = k\}$. Since $V_k$ is defined purely from $(V, \varrho)$, this count does not depend on the chosen decomposition, proving uniqueness up to order.
> >
> > **(ii) The special unitary group.** Restrict $\varrho$ to the diagonal circle $T = \{\operatorname{diag}(e^{i\theta}, e^{-i\theta})\} \subset SU(2)$. By Lemma 7 (proved below), the representation $\varrho_n$ restricted to $T$ has the weights $n, n-2, \dots, -n$, each with multiplicity one; that is, $\varrho_n|_T \cong \bigoplus_{j=0}^{n} \varrho^T_{\,n-2j}$ where $\varrho^T_m(\operatorname{diag}(e^{i\theta}, e^{-i\theta})) = e^{im\theta}$. Applying part (i) to the $U(1)$-representation $\varrho|_T$ (parametrising $T \cong U(1)$ by $\theta$), the multiplicity of the torus-weight $k \geq 0$ is
> > $$\dim V_k^{T} = \sum_{n \geq k,\ n \equiv k \ (\mathrm{mod}\ 2)} m_n \qquad \text{(each } \varrho_n \text{ contributes the weight } k \text{ exactly once, and only when } n \geq k \text{ and } n \equiv k \bmod 2 \text{).}$$
> > The analogous sum for $k + 2$ is $\dim V_{k+2}^{T} = \sum_{n \geq k+2,\ n \equiv k\ (2)} m_n$, and subtracting the two telescoping sums leaves the single term $m_k$:
> > $$\dim V_k^{T} - \dim V_{k+2}^{T} = m_k \qquad (k \geq 0).$$
> > Only nonnegative $k$ occur among the $\varrho_k$, so every multiplicity is recovered from the intrinsic torus-weight dimensions $\dim V_j^T$; the decomposition is unique up to order. $\blacksquare$

> [!note]- Lemma 5: For a connected group, invariance and intertwining are Lie-algebra conditions
> **Statement:** Let $G$ be a connected matrix Lie group with Lie algebra $\mathfrak{g}$, and let $\varrho \colon G \to GL(V)$, $\sigma \colon G \to GL(W)$ be representations with differentials $\varrho_* = d_e\varrho$, $\sigma_* = d_e\sigma$.
> (a) A subspace $U \subseteq V$ is $\varrho(G)$-invariant if and only if it is $\varrho_*(\mathfrak{g})$-invariant.
> (b) A linear map $S \colon V \to W$ satisfies $S\varrho(g) = \sigma(g)S$ for all $g \in G$ if and only if $S\varrho_*(X) = \sigma_*(X)S$ for all $X \in \mathfrak{g}$.
>
> **Hint:** use $\varrho(\exp X) = e^{\varrho_*(X)}$ and that a connected group is generated by any neighbourhood of the identity.
>
> **Why needed:** it lets the classification of $SU(2)$-irreducibles happen on $\mathfrak{sl}_2$, and reduces the intertwiner check of Part (C) to the three generators $X_1, X_2, X_3$.
>
> > [!note]- Full proof
> > **Sublemma A — $\varrho(\exp X) = e^{\varrho_*(X)}$.** Since $\varrho \colon G \to GL(V)$ is a Lie group homomorphism, [[Thm - Naturality of the Exponential Map|naturality of the exponential map]] — *for a homomorphism of Lie groups $\varphi \colon G \to H$, $\varphi \circ \exp_G = \exp_H \circ \varphi_*$* — gives $\varrho(\exp_G X) = \exp_{GL(V)}(\varrho_* X)$. The exponential of the matrix group $GL(V)$ is the [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|matrix exponential]] $\exp_{GL(V)}(A) = e^A = \sum_{m \geq 0} A^m/m!$. Hence $\varrho(\exp X) = e^{\varrho_*(X)}$ for all $X \in \mathfrak{g}$.
> >
> > **Sublemma B — a connected group is generated by $\exp(\mathfrak{g})$.** By the [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin|local-diffeomorphism theorem]] — *$d_0\exp = \operatorname{id}_{\mathfrak{g}}$, so there are neighbourhoods $\mathcal{U} \ni 0$ in $\mathfrak{g}$ and $\Omega \ni e$ in $G$ with $\exp|_{\mathcal{U}} \colon \mathcal{U} \to \Omega$ a diffeomorphism* — the set $\Omega = \exp(\mathcal{U})$ is an open neighbourhood of $e$. Let $H = \bigcup_{n \geq 1}(\Omega \cup \Omega^{-1})^n$ be the subgroup of $G$ generated by $\Omega$. Then $H$ is open, since for $h \in H$ the set $h\Omega \subseteq H$ is an open neighbourhood of $h$. An open subgroup is also closed, because its complement is the union of the remaining cosets, each of which is open (a translate of $H$). As $G$ is connected and $H$ is nonempty and both open and closed, $H = G$. Thus every $g \in G$ is a finite product $\exp(X_1)\cdots\exp(X_m)$ with $X_i \in \mathfrak{g}$.
> >
> > **(b), direction "$\Leftarrow$".** Assume $S\varrho_*(X) = \sigma_*(X)S$ for all $X$. Fix $X$. By induction on $m$, $S\,\varrho_*(X)^m = \sigma_*(X)^m S$ (the base case $m = 0$ is $S = S$, and $S\,\varrho_*(X)^{m+1} = \sigma_*(X)^m S \varrho_*(X) = \sigma_*(X)^{m+1}S$). Summing the exponential series (which converges absolutely, so term-by-term application of the bounded operator $S$ is valid),
> > $$S\, e^{\varrho_*(X)} = \sum_{m \geq 0}\frac{1}{m!} S\,\varrho_*(X)^m = \sum_{m \geq 0}\frac{1}{m!}\sigma_*(X)^m S = e^{\sigma_*(X)} S,$$
> > and by Sublemma A this reads $S\varrho(\exp X) = \sigma(\exp X)S$. The set $N := \{g \in G : S\varrho(g) = \sigma(g)S\}$ is a subgroup: it contains $e$; if $g, h \in N$ then $S\varrho(gh) = S\varrho(g)\varrho(h) = \sigma(g)S\varrho(h) = \sigma(g)\sigma(h)S = \sigma(gh)S$; and if $g \in N$ then, multiplying $S\varrho(g) = \sigma(g)S$ by $\sigma(g)^{-1}$ on the left and $\varrho(g)^{-1}$ on the right, $\sigma(g)^{-1}S = S\varrho(g)^{-1}$, so $g^{-1} \in N$. Since $N$ contains $\exp(\mathfrak{g})$, it contains the subgroup it generates, which is all of $G$ by Sublemma B. Hence $S\varrho(g) = \sigma(g)S$ for all $g$.
> >
> > **(b), direction "$\Rightarrow$".** Assume $S\varrho(g) = \sigma(g)S$ for all $g$. For $X \in \mathfrak{g}$ the curve $t \mapsto \exp(tX)$ has velocity $X$ at $t = 0$, and by definition of the differential $\frac{d}{dt}\big|_{0}\varrho(\exp tX) = \varrho_*(X)$. Differentiating the identity $S\varrho(\exp tX) = \sigma(\exp tX)S$ at $t = 0$ (both sides are smooth curves of operators, and $S$ is a constant linear map) gives $S\varrho_*(X) = \sigma_*(X)S$.
> >
> > **(a).** We argue both inclusions directly, using the same two ingredients as in (b): that a smooth curve lying in a closed subspace has its velocity in that subspace, and that $G$ is generated by $\exp(\mathfrak{g})$ (Sublemma B). "$\Rightarrow$": if $U$ is $\varrho(G)$-invariant, then for $u \in U$ and $X \in \mathfrak{g}$ the curve $t \mapsto \varrho(\exp tX)u$ lies in the subspace $U$, which is closed, so its derivative at $t = 0$, namely $\varrho_*(X)u$, also lies in $U$; hence $U$ is $\varrho_*(\mathfrak{g})$-invariant. "$\Leftarrow$": if $U$ is $\varrho_*(\mathfrak{g})$-invariant, then for $X \in \mathfrak{g}$ the operator $e^{\varrho_*(X)}$ preserves $U$ (each power $\varrho_*(X)^m$ does, and $U$ is closed under the convergent series), so by Sublemma A $\varrho(\exp X)$ preserves $U$; the subgroup $\{g : \varrho(g)U \subseteq U\}$ then contains $\exp(\mathfrak{g})$ and hence all of $G$ by Sublemma B. $\blacksquare$

> [!note]- Lemma 6: The irreducible representations of $\mathfrak{sl}(2; \mathbb{C})$
> **Statement:** Let $\mathfrak{sl}(2; \mathbb{C})$ have the basis $H, E, F$ with $[H, E] = 2E$, $[H, F] = -2F$, $[E, F] = H$. For each integer $n \geq 0$ there is a representation $L(n)$ of dimension $n + 1$ with a basis $v_0, \dots, v_n$ on which
> $$H v_j = (n - 2j)v_j, \qquad F v_j = v_{j+1}\ (j < n),\ Fv_n = 0, \qquad E v_0 = 0,\ E v_j = j(n - j + 1)v_{j-1}\ (j \geq 1);$$
> $L(n)$ is irreducible, and every finite-dimensional irreducible complex representation of $\mathfrak{sl}(2; \mathbb{C})$ is isomorphic to exactly one $L(n)$. In particular two finite-dimensional irreducibles of the same dimension are isomorphic.
>
> **Hint:** in an irreducible, take an $H$-eigenvector of top weight (so $E$ kills it) and apply $F$ repeatedly; the ladder must terminate, which forces the top weight to be a nonnegative integer.
>
> **Why needed:** it is the complete list of $SU(2)$-irreducibles once one passes to the complexified Lie algebra.
>
> > [!note]- Full proof
> > Write $\lambda \colon \mathfrak{sl}(2; \mathbb{C}) \to \operatorname{End}(V)$ for a representation and abbreviate $H = \lambda(H)$, $E = \lambda(E)$, $F = \lambda(F)$; these obey the same bracket relations as operators.
> >
> > **Step 1 — weight shifting.** If $w$ is an $H$-eigenvector with $Hw = \mu w$, then
> > $$H(Ew) = (HE)w = ([H, E] + EH)w = (2E + \mu E)w = (\mu + 2)Ew \qquad \text{(bracket relation } [H,E] = 2E \text{),}$$
> > so $Ew$ is either $0$ or an $H$-eigenvector of weight $\mu + 2$; likewise $H(Fw) = (\mu - 2)Fw$, so $Fw$ is $0$ or has weight $\mu - 2$. Thus $E$ raises the weight by $2$ and $F$ lowers it by $2$.
> >
> > **Step 2 — a highest-weight vector.** Let $V$ be a finite-dimensional irreducible representation. Over $\mathbb{C}$ the operator $H$ has an eigenvalue, and its (finite, nonempty) set of eigenvalues $\Lambda$ contains one, call it $\mu$, of maximal real part. Then $\mu + 2 \notin \Lambda$. Choose $v_0 \neq 0$ with $Hv_0 = \mu v_0$; by Step 1, $Ev_0$ has weight $\mu + 2 \notin \Lambda$, so $Ev_0 = 0$. We call $v_0$ a highest-weight vector of weight $\mu$.
> >
> > **Step 3 — the descending ladder.** Set $v_j := F^j v_0$ for $j \geq 0$ (with $v_{-1} := 0$). By Step 1, $Hv_j = (\mu - 2j)v_j$. We claim
> > $$E v_j = j(\mu - j + 1)v_{j-1} \qquad (j \geq 0),$$
> > by induction on $j$. For $j = 0$ this reads $Ev_0 = 0$, true by Step 2. Assume it for $j - 1$. Then, using $EF = [E, F] + FE = H + FE$,
> > $$E v_j = E F v_{j-1} = (H + FE)v_{j-1} = (\mu - 2(j-1))v_{j-1} + F\big((j-1)(\mu - j + 2)v_{j-2}\big) \qquad \text{(} Hv_{j-1} = (\mu - 2(j-1))v_{j-1} \text{; inductive hypothesis)}$$
> > $$= \big[(\mu - 2j + 2) + (j-1)(\mu - j + 2)\big]v_{j-1} \qquad \text{(} Fv_{j-2} = v_{j-1} \text{).}$$
> > Expanding the bracket, $(\mu - 2j + 2) + (j-1)(\mu - j + 2) = j\mu + \big[(-2j + 2) - (j-1)(j-2)\big] = j\mu + (j - j^2) = j(\mu - j + 1)$, which proves the claim.
> >
> > **Step 4 — termination forces $\mu = n \in \mathbb{Z}_{\geq 0}$.** The nonzero $v_j$ have distinct $H$-weights $\mu - 2j$, hence are linearly independent; as $V$ is finite-dimensional there is a least $n \geq 0$ with $v_{n+1} = 0$ while $v_0, \dots, v_n \neq 0$. Applying $E$ to $v_{n+1} = 0$ and using Step 3 with $j = n + 1$,
> > $$0 = E v_{n+1} = (n+1)(\mu - n)v_n.$$
> > Since $v_n \neq 0$ and $n + 1 \neq 0$, we get $\mu = n$. Thus the highest weight is a nonnegative integer $n$, and the weights are $n, n-2, \dots, -n$.
> >
> > **Step 5 — irreducibility pins the dimension.** The span $W = \operatorname{span}(v_0, \dots, v_n)$ is invariant: it is closed under $H$ and $F$ by construction, and under $E$ by the formula of Step 3. Since $W \neq 0$ and $V$ is irreducible, $W = V$; so $\dim V = n + 1$ and the action of $H, E, F$ is exactly the stated formulas with the top weight $n$. This is $L(n)$.
> >
> > **Step 6 — existence of $L(n)$.** Conversely, on a space with basis $v_0, \dots, v_n$ define operators $H, E, F$ by the displayed formulas (with $n$ the given integer). We verify the three bracket relations on each basis vector $v_j$: $[H, E]v_j = (HE - EH)v_j = (n - 2(j-1))\,j(n-j+1)v_{j-1} - (n - 2j)\,j(n-j+1)v_{j-1} = 2\,j(n-j+1)v_{j-1} = 2Ev_j$; $[H, F]v_j = (n - 2(j+1))v_{j+1} - (n - 2j)v_{j+1} = -2v_{j+1} = -2Fv_j$; and $[E, F]v_j = E v_{j+1} - F\big(j(n-j+1)v_{j-1}\big) = (j+1)(n-j)v_j - j(n-j+1)v_j = (n - 2j)v_j = H v_j$ (the coefficient simplifies as $(j+1)(n-j) - j(n-j+1) = n - 2j$). So the formulas define a representation.
> >
> > **Step 7 — $L(n)$ is irreducible and equal dimension implies equivalence.** Let $U \subseteq L(n)$ be a nonzero invariant subspace. Because $H$ acts diagonally with the distinct eigenvalues $n - 2j$, the subspace $U$ is a direct sum of some of the eigenlines $\mathbb{C}v_j$; in particular $U$ contains some $v_j$. Applying $E$ repeatedly, $E^j v_j = \Big(\prod_{i=1}^{j} i(n - i + 1)\Big)v_0$, and each factor $i(n - i + 1) > 0$ for $1 \leq i \leq j \leq n$, so the scalar is nonzero and $v_0 \in U$; then $v_i = F^i v_0 \in U$ for all $i$, so $U = L(n)$. Hence $L(n)$ is irreducible. Finally, if $V, V'$ are irreducibles of the same dimension $n + 1$, then by Steps 4–5 both have top weight $n$ (the top weight equals $\dim - 1$) and both carry the basis of Step 3 with identical structure constants; the linear map matching the two bases $v_j \leftrightarrow v_j'$ intertwines $H, E, F$ because the formulas coincide, so $V \cong V' \cong L(n)$. $\blacksquare$

> [!note]- Lemma 7: The symmetric powers $\odot^k \mathbb{C}^2$ are the $SU(2)$-irreducibles
> **Statement:** For $k \geq 0$, the representation $\varrho_k = \odot^k\varrho_1$ of $SU(2)$ on $\odot^k \mathbb{C}^2$ has, as a representation of $\mathfrak{sl}(2; \mathbb{C}) = \mathfrak{su}(2)_{\mathbb{C}}$, the $H$-weights $k, k-2, \dots, -k$, each with multiplicity one; hence $(\varrho_k)_* \cong L(k)$, so $\varrho_k$ is an irreducible representation of $SU(2)$ of dimension $k + 1$, and $\varrho_k \not\cong \varrho_l$ for $k \neq l$.
>
> **Hint:** on the symmetric basis $e_1^{\odot(k-j)} \odot e_2^{\odot j}$ the operator $(\varrho_k)_*(H)$ acts as $k - 2j$; the vector $e_1^{\odot k}$ is a highest-weight vector.
>
> **Why needed:** it names each abstract irreducible $L(k)$ as a concrete $\varrho_k$, and yields Part (C) at $k = 2$.
>
> > [!note]- Full proof
> > **Step 0 — the differential of a symmetric power.** From [[Def - Constructions on Representations|the constructions page]], $\varrho_k(g) = g^{\odot k}$ acts by $g^{\odot k}(u_1 \odot \dots \odot u_k) = gu_1 \odot \dots \odot gu_k$. Differentiating the curve $t \mapsto \varrho_k(\exp tX)$ at $t = 0$ with the product (Leibniz) rule — each factor $\exp(tX)u_i$ contributes its derivative $Xu_i$ while the others are frozen at $u_i$ — gives the derivation formula
> > $$(\varrho_k)_*(X)(u_1 \odot \dots \odot u_k) = \sum_{i=1}^{k} u_1 \odot \dots \odot (Xu_i) \odot \dots \odot u_k, \qquad X \in \mathfrak{su}(2),$$
> > extended complex-linearly to $X \in \mathfrak{sl}(2; \mathbb{C})$.
> >
> > **Step 1 — weights.** A basis of $\odot^k \mathbb{C}^2$ is $w_j := e_1^{\odot(k-j)} \odot e_2^{\odot j}$ for $j = 0, \dots, k$ (there are $k + 1$ of them, matching $\dim_{\mathbb{C}} \odot^k \mathbb{C}^2 = k + 1$). With $H = \operatorname{diag}(1, -1)$ we have $He_1 = e_1$ and $He_2 = -e_2$, so by Step 0,
> > $$(\varrho_k)_*(H) w_j = \big[(k - j)\cdot(+1) + j\cdot(-1)\big]w_j = (k - 2j)w_j.$$
> > Hence the $H$-weights are $k, k-2, \dots, -k$, each occurring exactly once.
> >
> > **Step 2 — highest-weight vector and identification with $L(k)$.** The vector $w_0 = e_1^{\odot k}$ has weight $k$, and since $Ee_1 = 0$ (as $E = \left(\begin{smallmatrix} 0 & 1 \\ 0 & 0 \end{smallmatrix}\right)$ kills $e_1$), Step 0 gives $(\varrho_k)_*(E)w_0 = \sum_i e_1 \odot \dots \odot (Ee_1) \odot \dots \odot e_1 = 0$. So $w_0$ is a highest-weight vector of weight $k$ for the $\mathfrak{sl}(2; \mathbb{C})$-action $(\varrho_k)_*$. By the structure established in Lemma 6, the subrepresentation generated by $w_0$ is a copy of $L(k)$, of dimension $k + 1$; but $\dim \odot^k \mathbb{C}^2 = k + 1$, so it is the whole space. Therefore $(\varrho_k)_* \cong L(k)$, which is irreducible as an $\mathfrak{sl}(2; \mathbb{C})$-representation.
> >
> > **Step 3 — irreducibility as an $SU(2)$-representation.** Let $U \subseteq \odot^k \mathbb{C}^2$ be a $\varrho_k(SU(2))$-invariant complex subspace. Since $SU(2)$ is connected, Lemma 5(a) makes $U$ invariant under $(\varrho_k)_*(\mathfrak{su}(2))$; being a complex subspace, it is then invariant under the complex span $(\varrho_k)_*(\mathfrak{su}(2) + i\,\mathfrak{su}(2)) = (\varrho_k)_*(\mathfrak{sl}(2; \mathbb{C}))$. By Step 2 the latter representation is irreducible, so $U = 0$ or $U = \odot^k \mathbb{C}^2$. Hence $\varrho_k$ is an irreducible $SU(2)$-representation.
> >
> > **Step 4 — distinctness.** If $\varrho_k \cong \varrho_l$ then their dimensions agree, $k + 1 = l + 1$, so $k = l$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove (A), (B), (C) in turn. Throughout, "representation" means finite-dimensional over $\mathbb{C}$, and we freely use Lemmas 1–7.
>
> ## Part (A) — the circle group $U(1)$
>
> **Step A0 — the $\varrho_k$ are representations, irreducible, and pairwise inequivalent.** Each $\varrho_k(z) = z^k$ is a smooth homomorphism $U(1) \to \mathbb{C}^\times$ (since $(zz')^k = z^k z'^k$), hence a one-dimensional representation. A one-dimensional representation has no subspace other than $0$ and the whole line, so it is irreducible. By Lemma 3 (uniqueness clause), $\varrho_k \cong \varrho_l$ if and only if $k = l$; so the $\varrho_k$ are pairwise inequivalent. This is statement (A.1).
>
> **Step A1 — every representation is a sum of the $\varrho_k$.** Let $\varrho \colon U(1) \to GL(V)$ be any representation. By Lemma 1 (unitarian trick, $U(1)$ compact) $\varrho$ is completely reducible: $V = W_1 \oplus \dots \oplus W_r$ with each $\varrho|_{W_i}$ irreducible. Since $U(1)$ is abelian, Lemma 2 gives $\dim W_i = 1$, so $\varrho|_{W_i}$ is a one-dimensional representation, which by Lemma 3 equals $\varrho_{k_i}$ for a unique $k_i \in \mathbb{Z}$. Hence $\varrho \cong \varrho_{k_1} \oplus \dots \oplus \varrho_{k_r}$.
>
> **Step A2 — uniqueness up to order.** By Lemma 4(i), the number of indices $i$ with $k_i = k$ equals $\dim V_k$, an invariant of $(V, \varrho)$; so the multiset $\{k_1, \dots, k_r\}$ is determined by $\varrho$. This is statement (A.2).
>
> **Step A3 — tensor and dual rules.** For the tensor product, the linear isomorphism $\mu \colon \mathbb{C} \otimes \mathbb{C} \to \mathbb{C}$, $u \otimes w \mapsto uw$, intertwines $\varrho_k \otimes \varrho_l$ with $\varrho_{k+l}$: for $z \in U(1)$,
> $$\mu\big((\varrho_k \otimes \varrho_l)(z)(u \otimes w)\big) = \mu\big((z^k u) \otimes (z^l w)\big) = z^{k+l} uw = \varrho_{k+l}(z)\,\mu(u \otimes w) \qquad \text{(definitions of } \otimes\text{-representation, } \mu \text{, and } \varrho_{k+l} \text{).}$$
> Hence $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$. For the dual, identify $\mathbb{C}^* = \operatorname{Hom}(\mathbb{C}, \mathbb{C})$ with $\mathbb{C}$ via $\eta \leftrightarrow \eta(1)$. By definition $\varrho_k^*(z) = \varrho_k(z^{-1})^*$, so for $\eta \in \mathbb{C}^*$ and $a \in \mathbb{C}$,
> $$\big(\varrho_k^*(z)\eta\big)(a) = \eta\big(\varrho_k(z^{-1})a\big) = \eta(z^{-k}a) = z^{-k}\eta(a) \qquad \text{(} \varrho_k(z^{-1}) = z^{-k}\cdot \text{, and } \eta \text{ linear),}$$
> so under the identification $\varrho_k^*(z)$ is multiplication by $z^{-k}$, that is $\varrho_k^* \cong \varrho_{-k}$. This is statement (A.3), completing (A).
>
> ## Part (B) — the special unitary group $SU(2)$
>
> **Step B0 — the $\varrho_k$ are irreducible, of dimension $k+1$, and pairwise inequivalent.** This is exactly Lemma 7: each $\varrho_k = \odot^k\varrho_1$ is an irreducible $SU(2)$-representation of dimension $k + 1$, and $\varrho_k \not\cong \varrho_l$ for $k \neq l$. This is statement (B.1).
>
> **Step B1 — every representation is a sum of irreducibles.** By Lemma 1 (unitarian trick, $SU(2)$ compact), any representation $\varrho \colon SU(2) \to GL(V)$ is completely reducible: $V$ is a direct sum of $SU(2)$-irreducibles.
>
> **Step B2 — every irreducible of $SU(2)$ is some $\varrho_k$.** Let $V$ be an irreducible $SU(2)$-representation. Its differential $\varrho_*$ makes $V$ a representation of $\mathfrak{su}(2)$, and since $V$ is already a complex vector space, $\varrho_*$ extends complex-linearly to a representation of $\mathfrak{sl}(2; \mathbb{C}) = \mathfrak{su}(2)_{\mathbb{C}}$ on $V$. This $\mathfrak{sl}(2; \mathbb{C})$-representation is irreducible: a complex subspace $U \subseteq V$ invariant under $\mathfrak{sl}(2; \mathbb{C})$ is in particular invariant under $\mathfrak{su}(2)$, hence — as $SU(2)$ is connected — invariant under $\varrho(SU(2))$ by Lemma 5(a), hence $0$ or $V$ by irreducibility of $\varrho$. By Lemma 6, $V \cong L(n)$ as an $\mathfrak{sl}(2; \mathbb{C})$-representation for a unique $n \geq 0$, where $n + 1 = \dim V$. By Lemma 7, $(\varrho_n)_* \cong L(n)$ as well, so there is a complex-linear isomorphism $T \colon \odot^n \mathbb{C}^2 \to V$ intertwining the two $\mathfrak{sl}(2; \mathbb{C})$-representations; restricting scalars, $T$ intertwines the $\mathfrak{su}(2)$-representations $(\varrho_n)_*$ and $\varrho_*$. Since $SU(2)$ is connected, Lemma 5(b) upgrades $T$ to an intertwiner of the group representations $\varrho_n$ and $\varrho$. Hence $V \cong \varrho_n$.
>
> **Step B3 — assembling the decomposition and its uniqueness.** By Step B1 and Step B2, every representation of $SU(2)$ is a direct sum of the $\varrho_k$. By Lemma 4(ii) the multiplicities $m_k = \dim V_k^T - \dim V_{k+2}^T$ are determined by $\varrho$, so the decomposition is unique up to the order of the summands. This is statement (B.2), completing (B).
>
> ## Part (C) — the complexified adjoint representation
>
> **Step C0 — dimension count.** The adjoint representation $\operatorname{Ad}_{SU(2)}$ acts on the real $3$-dimensional space $\mathfrak{su}(2)$ (from **[[Thm - Ad is a Smooth Representation and its Differential is ad]]**, with $\dim_{\mathbb{R}}\mathfrak{su}(2) = 3$), so its complexification $(\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ is a complex $3$-dimensional representation. Among the $\varrho_k$, only $\varrho_2$ has $\dim = k + 1 = 3$; so $\varrho_2$ is the sole candidate to be equivalent to it. This is Remark 1.3.4 of the source.
>
> **Step C1 — it suffices to intertwine the Lie-algebra representations.** The differential of $(\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ is $(\operatorname{ad})_{\mathbb{C}}$, the complexified adjoint representation of $\mathfrak{sl}(2; \mathbb{C})$ on itself. By Lemma 5(b) (with $SU(2)$ connected), a complex-linear $S \colon \mathfrak{su}(2)_{\mathbb{C}} \to \odot^2 \mathbb{C}^2$ satisfies $S\operatorname{Ad}_g = \varrho_2(g)S$ for all $g \in SU(2)$ if and only if it satisfies $S\operatorname{ad}(X) = (\varrho_2)_*(X)S$ for all $X \in \mathfrak{sl}(2; \mathbb{C})$; and since both sides are complex-linear in $X$, it is enough to check this on the real basis $X_1, X_2, X_3$ of $\mathfrak{su}(2)$, which spans $\mathfrak{su}(2)_{\mathbb{C}}$ over $\mathbb{C}$.
>
> **Step C2 — the two Lie-algebra representations in coordinates.** In the basis $(X_1, X_2, X_3)$ of $\mathfrak{su}(2)_{\mathbb{C}}$, the matrices of $\operatorname{ad}(X_a)Y = [X_a, Y]$ follow from $[X_a, X_b] = 2\varepsilon_{abc}X_c$:
> $$\operatorname{ad}(X_1) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix}, \quad \operatorname{ad}(X_2) = \begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \\ -2 & 0 & 0 \end{pmatrix}, \quad \operatorname{ad}(X_3) = \begin{pmatrix} 0 & -2 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
> In the basis $(f_1, f_2, f_3) = (e_1 \odot e_1,\ e_2 \odot e_2,\ e_2 \odot e_1)$ of $\odot^2 \mathbb{C}^2$, the operator $(\varrho_2)_*(X)$ acts by the derivation rule $(\varrho_2)_*(X)(u \odot w) = (Xu)\odot w + u\odot(Xw)$ (Lemma 7, Step 0). We use $X_1 e_1 = -e_2,\ X_1 e_2 = e_1$; $X_2 e_1 = i e_2,\ X_2 e_2 = i e_1$; $X_3 e_1 = i e_1,\ X_3 e_2 = -i e_2$ (read off the three matrices $X_a$ acting on $e_1, e_2$) and the symmetry $e_1 \odot e_2 = e_2 \odot e_1 = f_3$. Each column below is the image of $f_1, f_2, f_3$ in turn, expressed in the basis $(f_1, f_2, f_3)$; no computation is abbreviated.
>
> **The generator $X_1$.**
> $$(\varrho_2)_*(X_1)f_1 = (X_1 e_1)\odot e_1 + e_1 \odot (X_1 e_1) = -e_2 \odot e_1 - e_1 \odot e_2 = -2 f_3,$$
> $$(\varrho_2)_*(X_1)f_2 = (X_1 e_2)\odot e_2 + e_2 \odot (X_1 e_2) = e_1 \odot e_2 + e_2 \odot e_1 = 2 f_3,$$
> $$(\varrho_2)_*(X_1)f_3 = (X_1 e_2)\odot e_1 + e_2 \odot (X_1 e_1) = e_1 \odot e_1 - e_2 \odot e_2 = f_1 - f_2,$$
> so that $(\varrho_2)_*(X_1) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & -1 \\ -2 & 2 & 0 \end{pmatrix}$.
>
> **The generator $X_2$.**
> $$(\varrho_2)_*(X_2)f_1 = (X_2 e_1)\odot e_1 + e_1 \odot (X_2 e_1) = i\,e_2 \odot e_1 + i\,e_1 \odot e_2 = 2i f_3,$$
> $$(\varrho_2)_*(X_2)f_2 = (X_2 e_2)\odot e_2 + e_2 \odot (X_2 e_2) = i\,e_1 \odot e_2 + i\,e_2 \odot e_1 = 2i f_3,$$
> $$(\varrho_2)_*(X_2)f_3 = (X_2 e_2)\odot e_1 + e_2 \odot (X_2 e_1) = i\,e_1 \odot e_1 + i\,e_2 \odot e_2 = i f_1 + i f_2,$$
> so that $(\varrho_2)_*(X_2) = \begin{pmatrix} 0 & 0 & i \\ 0 & 0 & i \\ 2i & 2i & 0 \end{pmatrix}$.
>
> **The generator $X_3$.**
> $$(\varrho_2)_*(X_3)f_1 = (X_3 e_1)\odot e_1 + e_1 \odot (X_3 e_1) = i\,e_1 \odot e_1 + i\,e_1 \odot e_1 = 2i f_1,$$
> $$(\varrho_2)_*(X_3)f_2 = (X_3 e_2)\odot e_2 + e_2 \odot (X_3 e_2) = -i\,e_2 \odot e_2 - i\,e_2 \odot e_2 = -2i f_2,$$
> $$(\varrho_2)_*(X_3)f_3 = (X_3 e_2)\odot e_1 + e_2 \odot (X_3 e_1) = -i\,e_2 \odot e_1 + i\,e_2 \odot e_1 = 0,$$
> so that $(\varrho_2)_*(X_3) = \begin{pmatrix} 2i & 0 & 0 \\ 0 & -2i & 0 \\ 0 & 0 & 0 \end{pmatrix}$. Collecting the three,
> $$(\varrho_2)_*(X_1) = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & -1 \\ -2 & 2 & 0 \end{pmatrix}, \quad (\varrho_2)_*(X_2) = \begin{pmatrix} 0 & 0 & i \\ 0 & 0 & i \\ 2i & 2i & 0 \end{pmatrix}, \quad (\varrho_2)_*(X_3) = \begin{pmatrix} 2i & 0 & 0 \\ 0 & -2i & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
>
> **Step C3 — the intertwiner $S$ and the three checks.** Take $S = \begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix}$ (columns are $S(X_1), S(X_2), S(X_3)$ in the basis $(f_1, f_2, f_3)$). We verify $S\operatorname{ad}(X_a) = (\varrho_2)_*(X_a)S$ for $a = 1, 2, 3$.
>
> For $a = 3$:
> $$S\operatorname{ad}(X_3) = \begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix}\begin{pmatrix} 0 & -2 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} -2i & 2 & 0 \\ 2i & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 2i & 0 & 0 \\ 0 & -2i & 0 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix} = (\varrho_2)_*(X_3)S.$$
> For $a = 1$:
> $$S\operatorname{ad}(X_1) = \begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix}\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -2 \\ 0 & 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 2i \\ 0 & 0 & -2i \\ 0 & 4i & 0 \end{pmatrix},$$
> $$(\varrho_2)_*(X_1)S = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & -1 \\ -2 & 2 & 0 \end{pmatrix}\begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix} = \begin{pmatrix} 0 & 0 & 2i \\ 0 & 0 & -2i \\ 0 & 4i & 0 \end{pmatrix},$$
> so $S\operatorname{ad}(X_1) = (\varrho_2)_*(X_1)S$.
> For $a = 2$:
> $$S\operatorname{ad}(X_2) = \begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix}\begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \\ -2 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & -2 \\ 0 & 0 & -2 \\ -4i & 0 & 0 \end{pmatrix},$$
> $$(\varrho_2)_*(X_2)S = \begin{pmatrix} 0 & 0 & i \\ 0 & 0 & i \\ 2i & 2i & 0 \end{pmatrix}\begin{pmatrix} -1 & -i & 0 \\ -1 & i & 0 \\ 0 & 0 & 2i \end{pmatrix} = \begin{pmatrix} 0 & 0 & -2 \\ 0 & 0 & -2 \\ -4i & 0 & 0 \end{pmatrix},$$
> so $S\operatorname{ad}(X_2) = (\varrho_2)_*(X_2)S$. (In each product the $(3,1)$ and $(1,3)$ entries are the ones that would fail for a wrong intertwiner; here all nine entries match.)
>
> **Step C4 — conclusion.** The complex-linear map $S$ is invertible ($\det S = 2i\cdot\det\left(\begin{smallmatrix} -1 & -i \\ -1 & i \end{smallmatrix}\right) = 2i(-2i) = 4 \neq 0$) and intertwines $\operatorname{ad}(X_a)$ with $(\varrho_2)_*(X_a)$ on a basis, hence on all of $\mathfrak{su}(2)_{\mathbb{C}}$ by complex-linearity. By Step C1 (Lemma 5(b)), $S\operatorname{Ad}_g = \varrho_2(g)S$ for every $g \in SU(2)$; therefore $S$ is an equivalence and
> $$\varrho_2 \cong (\operatorname{Ad}_{SU(2)})_{\mathbb{C}}. \qquad \blacksquare$$

> [!warning] ⚠️ Correction to the source's intertwiner $T$
> Bär–Wernli (Example 1.3.15) print the intertwiner $T = \left(\begin{smallmatrix} -i & 1 & 0 \\ 1 & -i & 0 \\ 0 & 0 & 1 \end{smallmatrix}\right)$ and verify $T\operatorname{Ad}_g T^{-1} = \varrho_2(g)$ **only for diagonal $g = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi})$**, then assert it "can be checked" for all $g$. It cannot: their $T$ is not a global intertwiner. Taking the non-toral element $g = \left(\begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}\right) \in SU(2)$ one has $\operatorname{Ad}_g = \operatorname{diag}(1, -1, -1)$ and $\varrho_2(g) = \left(\begin{smallmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & -1 \end{smallmatrix}\right)$, whereas
> $$T\operatorname{Ad}_g T^{-1} = \begin{pmatrix} 0 & -i & 0 \\ i & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix} \neq \varrho_2(g).$$
> The reason is structural: on the maximal torus both representations are diagonal, and any matrix conjugating one torus family to the other is determined only up to a diagonal rescaling $\operatorname{diag}(a, b, c)$; the source fixed this freedom by the torus check alone, which does not fix it. Fixing it with the non-toral generators $X_1, X_2$ (equivalently, solving $S\operatorname{ad}(X_a) = (\varrho_2)_*(X_a)S$ as in Step C3) yields the correct global intertwiner $S$ above, which is *not* a scalar multiple of $T$ — indeed $S = \operatorname{diag}(-i, -1, 2i)\,T$. We therefore use $S$, not $T$; on the diagonal torus $S$ reproduces the source's computation.

---

# Cross-Field Exercise Suggestions

**Spherical harmonics and the spectrum of the Laplacian on $S^2$ (analysis / mathematical physics).** The space $\mathcal{H}_\ell$ of degree-$\ell$ spherical harmonics on $S^2$ carries the natural $SO(3)$-action, which pulls back along the double cover $SU(2) \to SO(3)$ to an $SU(2)$-representation of dimension $2\ell + 1$. Deciding that this representation is irreducible, and hence must be $\varrho_{2\ell}$, is exactly an application of Part (B); the theorem then predicts $\dim\mathcal{H}_\ell = 2\ell + 1$, the multiplicity of the $\ell$-th Laplace eigenvalue. The application is non-obvious because nothing in the differential equation $\Delta Y = -\ell(\ell+1)Y$ mentions a group; the representation-theoretic content has to be recognised behind the eigenspace.

**Addition of angular momenta and the Clebsch–Gordan series (quantum mechanics).** Two quantum spins of spins $j_1, j_2$ live in $\varrho_{2j_1} \otimes \varrho_{2j_2}$, and the physical question "what total spins occur" is the decomposition of this tensor product into irreducibles. Using complete reducibility (Lemma 1) and the weight bookkeeping of Lemma 4, one derives $\varrho_a \otimes \varrho_b \cong \varrho_{a+b} \oplus \varrho_{a+b-2} \oplus \dots \oplus \varrho_{|a-b|}$. The application is non-obvious because the physicist's coupling coefficients are usually presented as a table to be looked up, whereas the theorem shows they are forced by the one-integer classification.

**Line bundles on a Riemann surface and their tensor powers (complex geometry).** A holomorphic Hermitian line bundle $L$ over a compact Riemann surface has structure group $U(1)$, and Part (A)'s tensor rule $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$ says that the associated line bundles $L^{\otimes k}$ form a cyclic tower under tensor product with $L^{\otimes(-k)} = (L^{\otimes k})^*$. Recognising the Picard group's tensor structure as the additive structure of the integers $k$ is precisely the representation-theoretic input; the theorem is what guarantees there are no other one-dimensional representations to produce exotic associated bundles.

---

# Bridges

- **Restriction to the maximal torus and weights.** Every construction in Part (B) is controlled by the diagonal circle $T = \{\operatorname{diag}(e^{i\theta}, e^{-i\theta})\} \subset SU(2)$: restricting an $SU(2)$-representation to $T$ turns it, by Part (A), into a sum of characters $\theta \mapsto e^{im\theta}$, the weights. The bridge is that this restriction loses no information (Lemma 4 recovers the $SU(2)$-multiplicities from the torus weights), which is the rank-one shadow of the general Weyl character theory; it is the computational engine behind every Clebsch–Gordan decomposition and behind the identification $\varrho_2 \cong (\operatorname{Ad})_{\mathbb{C}}$.

- **The universal cover $\mathbb{R} \to U(1)$ and the integrality of charge.** Lemma 3 traded the classification of characters for a lifting problem through the covering $p(\theta) = e^{i\theta}$, and the integer $k$ appeared as the value $\Phi(2\pi)/2\pi$ of the lifted additive map. This is the same mechanism that makes magnetic charge, the winding number of a gauge transformation, and the first Chern number integers: each is the degree of a map to $U(1)$, read off from the covering. The construction reappears in chapter V when the holonomy of a flat $U(1)$-connection is described by a homomorphism $\pi_1 \to U(1)$.

- **Associated bundles as the geometric image of a representation.** A principal $G$-bundle $P$ and a representation $\varrho \colon G \to GL(V)$ produce the associated bundle $P \times_\varrho V = (P \times V)/G$ with $(p, v) \sim (pg, \varrho(g)^{-1}v)$; the classification here says which such bundles a $U(1)$- or $SU(2)$-bundle can carry. For $U(1)$ the bundles $P \times_{\varrho_k}\mathbb{C} = L^{\otimes k}$ are the tensor powers of one line bundle (chapter III); for $SU(2)$ the bundles $P \times_{\varrho_k}\odot^k\mathbb{C}^2$ are the higher-spin bundles, and $P \times_{\varrho_2}\mathbb{C}^3 \cong (\operatorname{ad} P)_{\mathbb{C}}$ is the complexified adjoint bundle in which curvature lives (chapters IV, VIII).

---

# Unlocked by This

> [!tip] Associated line bundles and the first Chern class *(from Gauge Theory III)*
> Part (A)'s tensor rule makes the associated bundles of a principal $U(1)$-bundle the integer tensor powers $L^{\otimes k}$ of one line bundle $L$. This is the representation-theoretic half of the statement that principal $U(1)$-bundles are classified by a single integer, the first Chern number, developed on **Thm - Classification of Principal U(1)-Bundles by the First Chern Class**.

> [!tip] Spinor bundles and higher-spin fields *(from Gauge Theory VIII)*
> Part (B) supplies the higher symmetric powers $\varrho_k = \odot^k\varrho_1$; applied to a spin structure's principal $SU(2)$-bundle they give the spinor bundle ($k = 1$) and its symmetric powers, the higher-spin fields, used in the construction of the Dirac operator and the Seiberg–Witten equations.

> [!tip] The curvature lives in the adjoint representation *(from Gauge Theory IV)*
> Part (C)'s equivalence $\varrho_2 \cong (\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ identifies the spin-$1$ representation with the adjoint, which is the representation in which the curvature $F_A$ of an $SU(2)$-connection and every infinitesimal gauge transformation take values; the pointwise algebra of these objects is thereby the algebra of $\varrho_2$.
