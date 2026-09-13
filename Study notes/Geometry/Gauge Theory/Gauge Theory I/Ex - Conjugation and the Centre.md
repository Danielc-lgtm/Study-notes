---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Classical Matrix Groups"
  - "Def - Smooth Action of a Lie Group"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group with neutral element $e$. Besides the action of $G$ on itself by left multiplication, $g \cdot h := gh$, the group acts on itself by **conjugation**,
$$G \times G \to G, \qquad g \cdot h := \alpha_g(h) := g h g^{-1},$$
where $\alpha_g : G \to G$ is the inner automorphism determined by $g$. The **centre** of $G$ is the subset
$$Z(G) := \{g \in G : gh = hg \text{ for all } h \in G\}.$$
For a left action $\theta : G \times M \to M$ of $G$ on a manifold $M$, its **kernel** is the set $\ker\theta := \{g \in G : g \cdot x = x \text{ for all } x \in M\}$ of elements acting as the identity of $M$; the action is effective if and only if $\ker\theta = \{e\}$.

Prove the following.

**(a) Conjugation is a smooth left action, and its kernel is the centre.** The map $(g, h) \mapsto ghg^{-1}$ is a smooth left action of $G$ on $G$. An element $g \in G$ satisfies $ghg^{-1} = h$ for all $h \in G$ if and only if $g \in Z(G)$; so the kernel of the conjugation action is $Z(G)$, and the conjugation action is effective if and only if $Z(G) = \{e\}$. Moreover $Z(G)$ is a closed normal abelian subgroup of $G$, and the conjugation action is transitive only when $G = \{e\}$ (in general, the orbits are the conjugacy classes, and there is more than one of them as soon as $G$ has more than one element).

**(b) The centre of the unitary group.** For every $n \ge 1$,
$$Z(U(n)) = \{\lambda\,1 : \lambda \in \mathbb{C},\ |\lambda| = 1\} = U(1) \cdot 1,$$
the group of unitary scalar matrices; here $1$ denotes the $n \times n$ identity matrix.

**(c) The centre of $SU(2)$.** $Z(SU(2)) = \{1, -1\}$.

**(d) The centre of $SO(3)$.** $Z(SO(3)) = \{1\}$; equivalently, the conjugation action of $SO(3)$ on itself is effective, while those of $U(n)$ and of $SU(2)$ are not.

**Recall:**

The definitions of a smooth action, of effective, free and transitive actions, of the kernel, and of the centre are on the compound definition page of this section; the natural actions of a group on itself (left multiplication and conjugation) are its Example B-D1.5.4, and the centre is its item B-D1.5.6.

![[Def - Free, Transitive, Effective, and Proper Group Actions#The Definition]]

A smooth left action of a Lie group $G$ on a manifold $M$ is a smooth map $\theta : G \times M \to M$, written $(g, x) \mapsto g \cdot x$, such that $e \cdot x = x$ for all $x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$ for all $g_1, g_2, x$ (this is the definition on [[Def - Smooth Action of a Lie Group]], which the compound page restates); for each $g$ the map $\theta_g := \theta(g, \cdot) : M \to M$ is then a diffeomorphism with inverse $\theta_{g^{-1}}$, and $g \mapsto \theta_g$ is a group homomorphism $G \to \operatorname{Diff}(M)$. The action is **effective** if $\theta_g = \mathrm{id}_M$ implies $g = e$, that is, if $g \mapsto \theta_g$ is injective; **free** if $g \cdot x = x$ for some $x$ implies $g = e$; **transitive** if for all $x, y \in M$ there is $g$ with $g \cdot x = y$. The **orbit** of $x$ is $G \cdot x = \{g \cdot x : g \in G\}$, and $M$ is the disjoint union of the orbits.

The classical groups appearing in (b)–(d) are, with $A^* = \bar A^{\top}$ the conjugate transpose,
$$U(n) = \{A \in GL(n; \mathbb{C}) : A^* A = 1\}, \qquad SU(2) = \{A \in U(2) : \det A = 1\}, \qquad SO(3) = \{A \in GL(3; \mathbb{R}) : A^{\top} A = 1,\ \det A = 1\};$$
see [[Def - Classical Matrix Groups]]. In the algebra part of the vault, the centre is [[Def - Centraliser and Centre]], where it is also identified with the kernel of $G \to \operatorname{Aut}(G)$, $g \mapsto \alpha_g$; the present exercise is the Lie-theoretic version of that observation, with the three explicit computations that the gauge-theory chapters use (the centre of $U(n)$ governs which gauge transformations act trivially on a unitary bundle, and $Z(SU(2)) = \{\pm 1\}$ is the kernel of the double cover $SU(2) \to SO(3)$ recorded on [[Thm - SU(2) is the Double Cover of SO(3)]]).

---

# Convergent Strategy

**Problem class:** This is a *compute-the-kernel* problem for a group action, in two layers: an abstract layer (the kernel of the conjugation action of any group is its centre, essentially by unwinding the definitions) and a concrete layer (the centre of three specific matrix groups). The concrete layer is a *commutation-with-test-matrices* problem: one shows that a matrix commuting with every element of the group must be diagonal (by commuting it with suitable diagonal group elements) and then that its diagonal entries must all be equal (by commuting it with suitable permutation-like group elements), and one finishes with the constraints that membership in the group imposes on a scalar matrix.

**Assumption pattern:** The hypothesis "$A$ commutes with every element of $G$" is far stronger than needed; the art is to *choose a few elements of $G$* that already force the conclusion. Two kinds of test elements suffice for every classical group: diagonal elements whose diagonal entries are pairwise distinct in the relevant positions (commuting with such a $D$ forces $A_{ij}(D_{jj} - D_{ii}) = 0$, hence $A_{ij} = 0$ off the diagonal), and elements that permute two basis vectors up to sign (commuting with such a $Q$ forces two diagonal entries of $A$ to coincide). The recognisable trigger is "commutes with all of $G$" for a group $G$ that contains enough diagonal and (signed) permutation matrices — which every one of $U(n)$, $SU(n)$, $O(n)$, $SO(n)$ does, provided the signs are arranged so that the test matrices have determinant one when the group requires it.

**Theorem routing:** Part (a) is pure definition-chasing: the action axioms for $ghg^{-1}$ are $e h e^{-1} = h$ and $g_1 (g_2 h g_2^{-1}) g_1^{-1} = (g_1 g_2) h (g_1 g_2)^{-1}$; smoothness comes from the smoothness of multiplication and inversion on a Lie group ([[Def - Lie Group]]); the kernel computation is the chain $ghg^{-1} = h \iff gh = hg$; closedness of $Z(G)$ is closedness of an intersection of preimages of the closed set $\{e\}$ under continuous maps; normality and commutativity are two-line verifications. For (b)–(d) no theorem is routed: the argument is the explicit test-matrix computation above, with the test matrices $D_k = \operatorname{diag}(1, \dots, -1, \dots, 1)$ and the transpositions for $U(n)$; $\operatorname{diag}(i, -i)$ and $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ for $SU(2)$; and the half-turns $\operatorname{diag}(-1, -1, 1)$, $\operatorname{diag}(1, -1, -1)$ together with the quarter-turns about the $z$-axis and the $x$-axis for $SO(3)$. The reverse inclusions (scalars are central; $\pm 1$ are central) are immediate from $\lambda 1 \cdot A = A \cdot \lambda 1$.

**Key decision point:** The one place where care is needed is the choice of test matrices *inside the group*. In $U(n)$ any diagonal unitary matrix and any permutation matrix are available. In $SU(2)$ the transposition $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has determinant $-1$ and is not available; one uses instead $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, which has determinant $1$ and still swaps the diagonal entries under conjugation. In $SO(3)$ the diagonal matrix $\operatorname{diag}(-1, 1, 1)$ has determinant $-1$; one uses the half-turns $\operatorname{diag}(-1, -1, 1)$ and $\operatorname{diag}(1, -1, -1)$, each of which has determinant $1$, and one needs *two* of them because a single half-turn leaves one pair of off-diagonal positions unconstrained. The final step in each case — a scalar matrix in the group — is where the group's defining conditions are read off: $|\lambda| = 1$ from unitarity, $\lambda^2 = 1$ from $\det = 1$ in dimension two, and $\lambda \in \{\pm 1\}$ with $\lambda^3 = 1$, hence $\lambda = 1$, in $SO(3)$.

---

# Legal Operations Used

The topic page of this chapter is written after its subpages; the operations below are named descriptively, and the orchestrator reconciles the numbering with the topic page's Legal Operations list.

1. **Verify the two action axioms and smoothness directly from the group axioms.** Applied in Step 1: identity and compatibility for $g \cdot h = ghg^{-1}$ are consequences of $e h e^{-1} = h$ and of associativity together with $(g_1 g_2)^{-1} = g_2^{-1} g_1^{-1}$; smoothness of $(g, h) \mapsto ghg^{-1}$ is the composition of the smooth structure maps of the Lie group.

2. **Compute the kernel of an action by solving $g \cdot x = x$ for all $x$.** Applied in Step 2: $ghg^{-1} = h$ for all $h$ is, after right multiplication by $g$, the condition $gh = hg$ for all $h$, which is the definition of $Z(G)$. Effectiveness is then the statement that the kernel is trivial.

3. **Show a subgroup is closed by writing it as an intersection of preimages of a closed set under continuous maps.** Applied in Step 2: $Z(G) = \bigcap_{h \in G} c_h^{-1}(\{e\})$ with $c_h(g) = g h g^{-1} h^{-1}$ continuous.

4. **Force a commuting matrix to be diagonal by commuting it with a diagonal group element with distinct entries.** Applied in Steps 3–5: the $(i, j)$ entry of $AD - DA$ is $A_{ij}(D_{jj} - D_{ii})$, so $AD = DA$ with $D_{ii} \neq D_{jj}$ gives $A_{ij} = 0$.

5. **Force the diagonal entries to coincide by commuting with a (signed) permutation matrix in the group.** Applied in Steps 3–5: if $Q$ maps $e_i \mapsto \pm e_j$ and $e_j \mapsto \pm e_i$ and $A$ is diagonal, then comparing the $(j, i)$ entries of $QA$ and $AQ$ gives $A_{ii} = A_{jj}$.

6. **Read the group's defining conditions off a scalar matrix.** Applied in Steps 3–5: $(\lambda 1)^*(\lambda 1) = |\lambda|^2 1$, $\det(\lambda 1_n) = \lambda^n$, and a real diagonal orthogonal matrix has entries $\pm 1$.

---

# Hints

> [!note]- Hint 1
> For (a), write out what "$g$ acts as the identity" means for the conjugation action: $ghg^{-1} = h$ for every $h$. Multiply on the right by $g$. For closedness of $Z(G)$, fix $h$ and consider the map $g \mapsto ghg^{-1}h^{-1}$; the centre is the set of $g$ at which *all* these maps take the value $e$.

> [!note]- Hint 2
> For (b), suppose $A \in U(n)$ commutes with every unitary matrix. It commutes in particular with the diagonal unitary matrix $D_k$ having $-1$ in position $k$ and $1$ elsewhere. Compute the $(i, j)$ entry of $AD_k - D_kA$: it is $A_{ij}\big((D_k)_{jj} - (D_k)_{ii}\big)$. Choose $k$ to make the bracket non-zero when $i \neq j$.

> [!note]- Hint 3
> Once $A = \operatorname{diag}(a_1, \dots, a_n)$, commute it with the permutation matrix $P$ that swaps $e_i$ and $e_j$ (which is real orthogonal, hence unitary). Compute $PAP^{-1}$: it is $A$ with $a_i$ and $a_j$ exchanged. Conclude $a_i = a_j$ for all $i, j$, so $A = \lambda 1$, and use $A^*A = 1$ to see $|\lambda| = 1$.

> [!note]- Hint 4
> For (c), the same two moves work with $D = \operatorname{diag}(i, -i)$ (determinant $-i^2 = 1$) and $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (determinant $1$). Then $A = \lambda 1$ with $\det A = \lambda^2 = 1$. For (d), use the half-turns $\operatorname{diag}(-1, -1, 1)$ and $\operatorname{diag}(1, -1, -1)$ to make $A$ diagonal, the quarter-turns about the $z$-axis and about the $x$-axis to equalise the diagonal entries, and finally $\det(\lambda 1_3) = \lambda^3$.

---

# Solution

The plan has an abstract half and a concrete half. Steps 1 and 2 treat an arbitrary Lie group: conjugation is a smooth action, and unwinding "$g$ acts trivially" gives exactly "$g$ commutes with everything", so the kernel is the centre; the structural properties of the centre (closed, normal, abelian) and the non-transitivity of conjugation are verified in the same step. Steps 3 to 5 compute the centres of $U(n)$, $SU(2)$ and $SO(3)$ by one uniform method — commute the unknown central element with a diagonal test matrix to make it diagonal, then with a permutation-like test matrix to make it scalar, then apply the group's defining conditions to a scalar matrix — the only variation being the choice of test matrices that lie in the group.

**Step 1: Conjugation is a smooth left action of $G$ on itself.**

The map $\theta : G \times G \to G$, $\theta(g, h) = ghg^{-1}$, satisfies $\theta(e, h) = h$ and $\theta(g_1, \theta(g_2, h)) = \theta(g_1 g_2, h)$, and it is smooth.

> [!note]- Derivation
> We must verify the two axioms of a left action and smoothness (the Recall above).
>
> **Identity axiom.** For every $h \in G$, $\theta(e, h) = e h e^{-1} = h$, because $e$ is the neutral element and $e^{-1} = e$.
>
> **Compatibility axiom.** For $g_1, g_2, h \in G$,
> $$\theta(g_1, \theta(g_2, h)) = g_1 (g_2 h g_2^{-1}) g_1^{-1} = (g_1 g_2)\, h\, (g_2^{-1} g_1^{-1}) = (g_1 g_2)\, h\, (g_1 g_2)^{-1} = \theta(g_1 g_2, h) \qquad \text{(associativity; } (g_1 g_2)^{-1} = g_2^{-1} g_1^{-1}\text{)}.$$
>
> **Smoothness.** In a Lie group the multiplication $m : G \times G \to G$ and the inversion $\iota : G \to G$ are smooth ([[Def - Lie Group]]). The map $\theta$ is the composition
> $$G \times G \xrightarrow{(g, h) \mapsto (g, h, g)} G \times G \times G \xrightarrow{(g, h, g') \mapsto (m(g, h), \iota(g'))} G \times G \xrightarrow{m} G,$$
> in which the first map is smooth (its components are projections), the second is smooth (its components are $m$ and $\iota$ composed with projections), and the third is $m$. A composition of smooth maps is smooth, so $\theta$ is smooth.
>
> Hence conjugation is a smooth left action. (For each $g$, the map $\theta_g = \alpha_g$ is a diffeomorphism of $G$ with inverse $\alpha_{g^{-1}}$, and it is also a group homomorphism: $\alpha_g(hh') = ghh'g^{-1} = (ghg^{-1})(gh'g^{-1}) = \alpha_g(h)\alpha_g(h')$. So each $\alpha_g$ is an automorphism of the Lie group $G$, an *inner* automorphism.)

**Step 2: The kernel of the conjugation action is $Z(G)$; structural properties of the centre; non-transitivity.**

$\{g \in G : ghg^{-1} = h \text{ for all } h \in G\} = Z(G)$. Consequently the conjugation action is effective if and only if $Z(G) = \{e\}$. The centre is a closed normal abelian subgroup of $G$, and the conjugation action is transitive if and only if $G = \{e\}$.

> [!note]- Derivation
> **The kernel.** Fix $g \in G$. Then
> $$g \in \ker\theta \iff \forall h \in G:\ ghg^{-1} = h \iff \forall h \in G:\ gh = hg \iff g \in Z(G),$$
> where the middle equivalence is obtained, from left to right, by multiplying $ghg^{-1} = h$ on the right by $g$ (using $g^{-1}g = e$ and $he = h$), and from right to left by multiplying $gh = hg$ on the right by $g^{-1}$; the last equivalence is the definition of $Z(G)$. So $\ker\theta = Z(G)$.
>
> **Effectiveness.** By definition, the action is effective if and only if $\theta_g = \mathrm{id}_G$ implies $g = e$, that is, if and only if $\ker\theta \subset \{e\}$; since $e \in \ker\theta$ always (identity axiom), this says $\ker\theta = \{e\}$, that is $Z(G) = \{e\}$. Hence the conjugation action is effective if and only if the centre is trivial, and it is *not* effective if and only if $Z(G) \neq \{e\}$, which is the form in which Bär states it.
>
> **$Z(G)$ is a subgroup.** $e \in Z(G)$ since $eh = h = he$. If $g, g' \in Z(G)$ then for all $h$, $(gg')h = g(g'h) = g(hg') = (gh)g' = (hg)g' = h(gg')$ (associativity and the centrality of $g'$, then of $g$), so $gg' \in Z(G)$. If $g \in Z(G)$ then from $gh = hg$ for all $h$ we get, multiplying by $g^{-1}$ on both sides, $hg^{-1} = g^{-1}h$ for all $h$, so $g^{-1} \in Z(G)$.
>
> **$Z(G)$ is closed.** For $h \in G$ let $c_h : G \to G$, $c_h(g) := ghg^{-1}h^{-1}$; it is continuous (indeed smooth), being built from multiplication and inversion as in Step 1. Since $ghg^{-1}h^{-1} = e$ if and only if $gh = hg$ (indeed $ghg^{-1}h^{-1} = e \iff ghg^{-1} = h \iff gh = hg$, the first equivalence by right multiplication by $h$ and by $h^{-1}$, the second by right multiplication by $g$ and by $g^{-1}$),
> $$Z(G) = \bigcap_{h \in G} c_h^{-1}(\{e\}).$$
> The singleton $\{e\}$ is closed because a manifold is Hausdorff; each preimage $c_h^{-1}(\{e\})$ is closed by continuity of $c_h$; and an arbitrary intersection of closed sets is closed. So $Z(G)$ is a closed subgroup of $G$ (and therefore an embedded Lie subgroup by [[Thm - The Closed Subgroup Theorem]], which states that a subgroup of a Lie group that is a closed subset is an embedded submanifold and a Lie group in the induced structure; we record this consequence without using it below).
>
> **$Z(G)$ is normal.** For $g \in Z(G)$ and $x \in G$, $xgx^{-1} = gxx^{-1} = g \in Z(G)$ (centrality of $g$), so $xZ(G)x^{-1} \subset Z(G)$ for every $x$; this is normality ([[Def - Normal Subgroup]]). Equivalently, $Z(G)$ is the kernel of the homomorphism $g \mapsto \alpha_g$ from $G$ to the automorphism group of $G$, and kernels are normal.
>
> **$Z(G)$ is abelian.** For $g, g' \in Z(G)$, $gg' = g'g$ because $g$ commutes with every element of $G$, in particular with $g'$.
>
> **Non-transitivity.** The orbit of $h$ under conjugation is its conjugacy class $\{ghg^{-1} : g \in G\}$. The orbit of $e$ is $\{geg^{-1} : g \in G\} = \{e\}$. If the action were transitive, every $h \in G$ would lie in the orbit of $e$, so $G = \{e\}$. Conversely, if $G = \{e\}$ the action is trivially transitive. Hence the conjugation action is transitive if and only if $G = \{e\}$; in Bär's words, it is not transitive unless the group has only one conjugacy class, and the only group with one conjugacy class is the trivial group, since $\{e\}$ is always a class of its own.

**Step 3: $Z(U(n)) = U(1) \cdot 1$.**

A matrix $A \in U(n)$ commutes with every unitary matrix if and only if $A = \lambda 1$ for some $\lambda \in \mathbb{C}$ with $|\lambda| = 1$.

> [!note]- Derivation
> **Scalars are central.** If $\lambda \in \mathbb{C}$ with $|\lambda| = 1$, then $\lambda 1 \in U(n)$ because $(\lambda 1)^*(\lambda 1) = \bar\lambda\lambda\, 1 = |\lambda|^2 1 = 1$, and $(\lambda 1)B = \lambda B = B(\lambda 1)$ for every matrix $B$ (scalar multiplication commutes with matrix multiplication). So $U(1) \cdot 1 \subset Z(U(n))$.
>
> **A central element is diagonal.** Let $A \in Z(U(n))$, and for $k \in \{1, \dots, n\}$ let $D_k := \operatorname{diag}(d_1, \dots, d_n)$ with $d_k = -1$ and $d_j = 1$ for $j \neq k$. Then $D_k$ is real and diagonal with $D_k^{\top} D_k = D_k^2 = 1$, so $D_k \in U(n)$, and therefore $AD_k = D_kA$. For any $i, j$ the $(i, j)$ entries are
> $$(AD_k)_{ij} = \sum_{l} A_{il}(D_k)_{lj} = A_{ij}\, d_j, \qquad (D_kA)_{ij} = \sum_{l} (D_k)_{il} A_{lj} = d_i\, A_{ij} \qquad \text{(} D_k \text{ is diagonal)},$$
> so $AD_k = D_kA$ gives $A_{ij}(d_j - d_i) = 0$. Now fix $i \neq j$ and take $k = i$: then $d_i = -1$ and $d_j = 1$, so $d_j - d_i = 2 \neq 0$ and hence $A_{ij} = 0$. Thus every off-diagonal entry of $A$ vanishes: $A = \operatorname{diag}(a_1, \dots, a_n)$ for some $a_1, \dots, a_n \in \mathbb{C}$. (When $n = 1$ there are no off-diagonal entries and the statement is empty; the argument below is likewise empty and $A = a_1 1$ directly.)
>
> **A central diagonal element is scalar.** For $i \neq j$ let $P \in GL(n; \mathbb{C})$ be the permutation matrix of the transposition $(i\ j)$: $Pe_i = e_j$, $Pe_j = e_i$, $Pe_l = e_l$ for $l \notin \{i, j\}$. It is real with orthonormal columns, so $P^{\top}P = 1$, hence $P \in U(n)$ and $P^{-1} = P^{\top} = P$. Since $A$ is central, $PAP^{-1} = A$. But $PAP^{-1}$ is the diagonal matrix with the entries $a_i$ and $a_j$ exchanged: for $l \notin \{i, j\}$, $PAP^{-1}e_l = PAe_l = P(a_l e_l) = a_l e_l$; and $PAP^{-1} e_j = PA e_i = P(a_i e_i) = a_i e_j$, $PAP^{-1}e_i = PAe_j = a_j e_i$. Comparing the $j$-th columns of $PAP^{-1}$ and $A$ gives $a_i e_j = a_j e_j$, so $a_i = a_j$. As $i \neq j$ were arbitrary, all diagonal entries are equal to a common value $\lambda$, and $A = \lambda 1$.
>
> **The scalar is unimodular.** From $A \in U(n)$: $1 = A^*A = (\bar\lambda 1)(\lambda 1) = |\lambda|^2 1$, so $|\lambda|^2 = 1$ and $|\lambda| = 1$.
>
> Therefore $Z(U(n)) \subset U(1) \cdot 1$, and with the first paragraph $Z(U(n)) = U(1) \cdot 1 = \{\lambda 1 : |\lambda| = 1\}$. In particular the conjugation action of $U(n)$ on itself is not effective for any $n \ge 1$: its kernel is a circle. For $n = 1$ the result says $Z(U(1)) = U(1)$, which is correct because $U(1)$ is abelian.

**Step 4: $Z(SU(2)) = \{\pm 1\}$.**

A matrix $A \in SU(2)$ commutes with every element of $SU(2)$ if and only if $A = 1$ or $A = -1$.

> [!note]- Derivation
> **$\pm 1$ are central.** $1 \in SU(2)$ trivially; $-1 \in SU(2)$ because $(-1)^*(-1) = 1$ and $\det(-1_2) = (-1)^2 = 1$; and $\pm 1$ commute with every matrix. So $\{\pm 1\} \subset Z(SU(2))$.
>
> **A central element is diagonal.** Let $A \in Z(SU(2))$ and $D := \operatorname{diag}(i, -i)$. Then $D^*D = \operatorname{diag}(\bar i\, i, \overline{(-i)}(-i)) = \operatorname{diag}(1, 1) = 1$ and $\det D = i \cdot (-i) = -i^2 = 1$, so $D \in SU(2)$ and $AD = DA$. As in Step 3, the $(i, j)$ entry of $AD - DA$ is $A_{ij}(D_{jj} - D_{ii})$; for $(i, j) = (1, 2)$ this is $A_{12}(-i - i) = -2i A_{12}$, and for $(i, j) = (2, 1)$ it is $A_{21}(i - (-i)) = 2i A_{21}$. Both vanish, so $A_{12} = A_{21} = 0$ and $A = \operatorname{diag}(a, b)$ with $a, b \in \mathbb{C}$.
>
> **A central diagonal element is scalar.** Let $J := \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. It is real with $J^{\top}J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $\det J = 0 \cdot 0 - (-1)(1) = 1$, so $J \in SU(2)$ (note that the transposition matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has determinant $-1$ and is *not* in $SU(2)$, which is why the sign is needed). Centrality gives $JA = AJ$; computing both products,
> $$JA = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix} = \begin{pmatrix} 0 & -b \\ a & 0 \end{pmatrix}, \qquad AJ = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -a \\ b & 0 \end{pmatrix} \qquad \text{(matrix multiplication)}.$$
> Comparing the $(2, 1)$ entries gives $a = b$. So $A = a 1$.
>
> **The scalar is a square root of one.** From $A \in SU(2)$: $\det A = \det(a 1_2) = a^2 = 1$, so $a \in \{1, -1\}$. (Unitarity gives only $|a| = 1$; it is the determinant condition that cuts the circle down to two points.)
>
> Therefore $Z(SU(2)) \subset \{\pm 1\}$, and with the first paragraph $Z(SU(2)) = \{1, -1\}$. The conjugation action of $SU(2)$ on itself is not effective: its kernel is the two-element group $\{\pm 1\}$.

**Step 5: $Z(SO(3)) = \{1\}$.**

A matrix $A \in SO(3)$ commutes with every element of $SO(3)$ if and only if $A = 1$.

> [!note]- Derivation
> **$1$ is central**, trivially. So $\{1\} \subset Z(SO(3))$.
>
> **A central element is diagonal.** Let $A \in Z(SO(3))$. Consider the two half-turns
> $$D := \operatorname{diag}(-1, -1, 1), \qquad D' := \operatorname{diag}(1, -1, -1).$$
> Each is real diagonal with square $1$, hence orthogonal, and each has determinant $(-1)(-1)(1) = 1$, so $D, D' \in SO(3)$. (The reflection $\operatorname{diag}(-1, 1, 1)$ has determinant $-1$ and is not available; this is why two half-turns are used.) Centrality gives $AD = DA$ and $AD' = D'A$. As in Step 3, the $(i, j)$ entry of $AD - DA$ is $A_{ij}(D_{jj} - D_{ii})$. For $D$: the pairs $(i, j) \in \{(1, 3), (3, 1), (2, 3), (3, 2)\}$ have $D_{jj} - D_{ii} = \pm 2 \neq 0$, so $A_{13} = A_{31} = A_{23} = A_{32} = 0$; the pair $(1, 2)$ has $D_{22} - D_{11} = 0$ and gives no information. For $D'$: the pairs $(i, j) \in \{(1, 2), (2, 1), (1, 3), (3, 1)\}$ have $D'_{jj} - D'_{ii} = \pm 2 \neq 0$, so $A_{12} = A_{21} = 0$ (and again $A_{13} = A_{31} = 0$). Together, every off-diagonal entry of $A$ vanishes, and $A = \operatorname{diag}(a, b, c)$ with $a, b, c \in \mathbb{R}$. Orthogonality $A^{\top}A = \operatorname{diag}(a^2, b^2, c^2) = 1$ forces $a, b, c \in \{1, -1\}$.
>
> **A central diagonal element is scalar.** Consider the quarter-turn about the $z$-axis and the quarter-turn about the $x$-axis,
> $$Q_z := \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad Q_x := \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}.$$
> Each has orthonormal columns (the columns of $Q_z$ are $e_2, -e_1, e_3$; those of $Q_x$ are $e_1, e_3, -e_2$), so each is orthogonal; and $\det Q_z = 1 \cdot \det\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = 1$ (expanding along the third row), $\det Q_x = 1 \cdot \det\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = 1$ (expanding along the first row). So $Q_z, Q_x \in SO(3)$. Centrality gives $Q_zA = AQ_z$:
> $$Q_zA = \begin{pmatrix} 0 & -b & 0 \\ a & 0 & 0 \\ 0 & 0 & c \end{pmatrix}, \qquad AQ_z = \begin{pmatrix} 0 & -a & 0 \\ b & 0 & 0 \\ 0 & 0 & c \end{pmatrix} \qquad \text{(matrix multiplication with } A = \operatorname{diag}(a, b, c)\text{)},$$
> and comparing the $(2, 1)$ entries gives $a = b$. Centrality also gives $Q_xA = AQ_x$; writing out both products in the same way,
> $$Q_xA = \begin{pmatrix} a & 0 & 0 \\ 0 & 0 & -c \\ 0 & b & 0 \end{pmatrix}, \qquad AQ_x = \begin{pmatrix} a & 0 & 0 \\ 0 & 0 & -b \\ 0 & c & 0 \end{pmatrix} \qquad \text{(matrix multiplication)},$$
> and comparing the $(3, 2)$ entries gives $b = c$. Hence $a = b = c =: \lambda \in \{1, -1\}$ and $A = \lambda 1$.
>
> **The scalar is one.** From $A \in SO(3)$: $\det A = \det(\lambda 1_3) = \lambda^3 = 1$; since $\lambda \in \{1, -1\}$ and $(-1)^3 = -1 \neq 1$, we get $\lambda = 1$. (This is the step that distinguishes $SO(3)$ from $SU(2)$: in odd dimension $-1$ has determinant $-1$ and is excluded.)
>
> Therefore $Z(SO(3)) = \{1\}$, and by Step 2 the conjugation action of $SO(3)$ on itself is effective. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** (a) Conjugation $\theta(g, h) = ghg^{-1}$ is a smooth left action of the Lie group $G$ on itself with kernel $Z(G)$; it is effective if and only if $Z(G) = \{e\}$; $Z(G)$ is a closed normal abelian subgroup; conjugation is transitive only for $G = \{e\}$. (b) $Z(U(n)) = U(1) \cdot 1$. (c) $Z(SU(2)) = \{\pm 1\}$. (d) $Z(SO(3)) = \{1\}$.
>
> **Part (a).** *Action axioms.* $\theta(e, h) = ehe^{-1} = h$; and $\theta(g_1, \theta(g_2, h)) = g_1 g_2 h g_2^{-1} g_1^{-1} = (g_1 g_2) h (g_1 g_2)^{-1} = \theta(g_1 g_2, h)$ by associativity and $(g_1 g_2)^{-1} = g_2^{-1} g_1^{-1}$. *Smoothness.* $\theta = m \circ (m \times \iota) \circ \big((g, h) \mapsto (g, h, g)\big)$ with $m$ the multiplication and $\iota$ the inversion of $G$, both smooth; hence $\theta$ is smooth. *Kernel.* For $g \in G$: $ghg^{-1} = h$ for all $h$ $\iff$ $gh = hg$ for all $h$ (right-multiply by $g$, respectively by $g^{-1}$) $\iff$ $g \in Z(G)$. Effectiveness means $\ker\theta = \{e\}$, that is $Z(G) = \{e\}$. *Subgroup.* $e \in Z(G)$; if $g, g' \in Z(G)$ then $gg'h = ghg' = hgg'$ for all $h$; if $g \in Z(G)$ then $gh = hg$ for all $h$ gives $hg^{-1} = g^{-1}h$ for all $h$. *Closed.* $Z(G) = \bigcap_{h} c_h^{-1}(\{e\})$ with $c_h(g) = ghg^{-1}h^{-1}$ continuous and $\{e\}$ closed (Hausdorff), so $Z(G)$ is closed. *Normal.* For $g \in Z(G)$, $xgx^{-1} = g$ for every $x$. *Abelian.* Elements of $Z(G)$ commute with everything, in particular with each other. *Transitivity.* The orbit of $e$ is $\{e\}$; transitivity forces $G = \{e\}$, and conversely.
>
> **Part (b).** For $|\lambda| = 1$, $\lambda 1 \in U(n)$ (as $(\lambda 1)^*(\lambda 1) = |\lambda|^2 1 = 1$) and $\lambda 1$ commutes with everything; so $U(1) \cdot 1 \subset Z(U(n))$. Conversely let $A \in Z(U(n))$. For $k = 1, \dots, n$, $D_k := \operatorname{diag}(1, \dots, 1, -1, 1, \dots, 1)$ (the $-1$ in position $k$) lies in $U(n)$, and $(AD_k - D_kA)_{ij} = A_{ij}(d_j - d_i)$; for $i \neq j$ and $k = i$ this is $2A_{ij} = 0$. So $A = \operatorname{diag}(a_1, \dots, a_n)$. For $i \neq j$ the transposition matrix $P = P_{(i\,j)}$ lies in $U(n)$ and $PAP^{-1}$ is $A$ with $a_i, a_j$ exchanged (columns computed on the basis vectors); centrality gives $PAP^{-1} = A$, so $a_i = a_j$. Hence $A = \lambda 1$, and $A^*A = |\lambda|^2 1 = 1$ gives $|\lambda| = 1$. Therefore $Z(U(n)) = U(1) \cdot 1$.
>
> **Part (c).** $\pm 1 \in SU(2)$ and commute with everything. Conversely let $A \in Z(SU(2))$. $D = \operatorname{diag}(i, -i) \in SU(2)$ ($D^*D = 1$, $\det D = 1$), and $(AD - DA)_{12} = -2iA_{12}$, $(AD - DA)_{21} = 2iA_{21}$ vanish, so $A = \operatorname{diag}(a, b)$. $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in SU(2)$ ($J^{\top}J = 1$, $\det J = 1$), and $JA = \begin{pmatrix} 0 & -b \\ a & 0 \end{pmatrix}$, $AJ = \begin{pmatrix} 0 & -a \\ b & 0 \end{pmatrix}$; their equality gives $a = b$. So $A = a1$ with $\det A = a^2 = 1$, hence $a = \pm 1$. Therefore $Z(SU(2)) = \{\pm 1\}$.
>
> **Part (d).** Let $A \in Z(SO(3))$. The half-turns $D = \operatorname{diag}(-1, -1, 1)$ and $D' = \operatorname{diag}(1, -1, -1)$ lie in $SO(3)$; $AD = DA$ gives $A_{13} = A_{31} = A_{23} = A_{32} = 0$ and $AD' = D'A$ gives $A_{12} = A_{21} = 0$ (in each case the $(i, j)$ entry of the commutator is $A_{ij}(D_{jj} - D_{ii})$ with $D_{jj} - D_{ii} = \pm 2$ for the listed pairs). So $A = \operatorname{diag}(a, b, c)$, and $A^{\top}A = 1$ gives $a, b, c \in \{\pm 1\}$. The quarter-turns $Q_z$ (columns $e_2, -e_1, e_3$) and $Q_x$ (columns $e_1, e_3, -e_2$) lie in $SO(3)$; $(Q_zA)_{21} = a$ and $(AQ_z)_{21} = b$ give $a = b$; $(Q_xA)_{32} = b$ and $(AQ_x)_{32} = c$ give $b = c$. So $A = \lambda 1$ with $\lambda \in \{\pm 1\}$ and $\det A = \lambda^3 = 1$, hence $\lambda = 1$. Therefore $Z(SO(3)) = \{1\}$, and the conjugation action of $SO(3)$ on itself is effective, whereas those of $U(n)$ (kernel $U(1) \cdot 1$) and $SU(2)$ (kernel $\{\pm 1\}$) are not. $\blacksquare$

> [!note]- Sanity check: the three centres against the double cover
> The three answers are consistent with the relation between $SU(2)$ and $SO(3)$. The theorem on [[Thm - SU(2) is the Double Cover of SO(3)]] — the map $\operatorname{Ad} : SU(2) \to SO(3)$, $u \mapsto (X \mapsto uXu^{-1})$ on the three-dimensional real space of traceless Hermitian matrices, is a surjective Lie group homomorphism with kernel $\{\pm 1\}$ — exhibits $SO(3) \cong SU(2)/\{\pm 1\} = SU(2)/Z(SU(2))$. A surjective homomorphism $\pi : G \to H$ maps $Z(G)$ into $Z(H)$ (if $g$ commutes with all of $G$ then $\pi(g)$ commutes with all of $\pi(G) = H$), so $\pi(Z(SU(2))) = \pi(\{\pm 1\}) = \{1\} \subset Z(SO(3))$; and Step 5 shows that nothing else is central in $SO(3)$. Likewise $Z(SU(2)) = SU(2) \cap Z(U(2)) = \{\lambda 1 : |\lambda| = 1, \lambda^2 = 1\} = \{\pm 1\}$, in agreement with Steps 3 and 4.

> [!warning] Illegal but tempting: "$A$ commutes with the generators, so it is central" without checking the generators lie in the group
> The method of Steps 3–5 is only valid when every test matrix belongs to the group in question. Commuting with $\operatorname{diag}(-1, 1, 1)$ would immediately kill all off-diagonal entries of a $3 \times 3$ matrix in one stroke, but this reflection has determinant $-1$ and is not in $SO(3)$; a central element of $SO(3)$ is under no obligation to commute with it. The extra condition that makes the shortcut legal is that the test matrices generate, or at least lie in, the group; in $SO(3)$ the half-turns and quarter-turns do, and two half-turns are needed where one reflection would have sufficed in $O(3)$. The same care is required in $SU(2)$, where the transposition $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is replaced by the signed transposition $J$.

---

# Key Takeaways

**The kernel of the conjugation action is the centre, and this is the exact obstruction to effectiveness — the pattern "kernel of an induced action = a named subgroup" recurs throughout the series.** Unwinding "$g$ acts as the identity" for conjugation gives "$g$ commutes with everything", so the conjugation action of $G$ on itself is effective precisely when $Z(G) = \{e\}$, and in general the action descends to an effective action of the quotient $G/Z(G)$ (the inner automorphism group). The same unwinding governs every action induced from conjugation: the adjoint representation of $G$ on its Lie algebra has kernel containing $Z(G)$ (because $\operatorname{Ad}_g$ is the differential at $e$ of $\alpha_g$, and $\alpha_g = \mathrm{id}_G$ for central $g$), and in chapter III the structure group of a principal bundle acts on the bundle through the fibres, so that central elements act on associated bundles by scalars. The trigger for this takeaway is any question of the form "which elements act trivially"; the transferable diagnostic is to solve $g \cdot x = x$ for all $x$ explicitly rather than to reason about the action abstractly, because the solution set is invariably a familiar subgroup — the centre for conjugation, the stabiliser of a point for a transitive action, the trivial group for a free action.

**To compute the centre of a matrix group, commute the unknown with a diagonal test element to make it diagonal, then with a permutation-like test element to make it scalar, then read the group's defining conditions off the scalar.** This three-move method computed $Z(U(n))$, $Z(SU(2))$ and $Z(SO(3))$ with no theory at all, and it computes the centre of every classical group: the first move uses the identity $(AD - DA)_{ij} = A_{ij}(D_{jj} - D_{ii})$, so any diagonal group element with distinct entries in positions $i$ and $j$ kills $A_{ij}$; the second uses that conjugating a diagonal matrix by a signed permutation matrix permutes its diagonal entries; the third is a one-line computation with $\det(\lambda 1_n) = \lambda^n$ and $(\lambda 1)^*(\lambda 1) = |\lambda|^2 1$. The point at which the method must be adapted to the group is the availability of the test elements: the determinant-one condition of $SU(n)$ and $SO(n)$ removes the transpositions and the single-entry reflections, which are replaced by signed transpositions and half-turns. The final scalar condition is where the answers diverge: $\lambda \in U(1)$ for $U(n)$, $\lambda^n = 1$ with $|\lambda| = 1$ for $SU(n)$ (which for $n = 2$ is $\pm 1$), and $\lambda = \pm 1$ with $\lambda^n = 1$ for $SO(n)$, which is $\{1\}$ in odd dimension and $\{\pm 1\}$ in even dimension. The reader who remembers only "diagonal test, permutation test, scalar condition" can regenerate all of these.

**The centres $U(1) \cdot 1$, $\{\pm 1\}$ and $\{1\}$ are the numbers that reappear when the series counts reducible connections and covers.** In chapter III, $SU(2)$-bundles and $SO(3)$-bundles are related by the double cover of [[Thm - SU(2) is the Double Cover of SO(3)]], whose kernel is exactly $Z(SU(2)) = \{\pm 1\}$ computed here; in chapter V the gauge group of a principal $G$-bundle always contains the constant central gauge transformations, which act trivially on every connection, so that the *effective* gauge group is a quotient by (a group related to) $Z(G)$; and in chapters XI and XIII the stabiliser of a connection under the gauge group contains $Z(G)$ for every connection and equals it exactly for the irreducible ones, so that $U(1) \cdot 1 \subset U(n)$ and $\{\pm 1\} \subset SU(2)$ are the groups by which the moduli spaces are quotiented "for free" and the reducible connections are those with a strictly larger stabiliser. The diagnostic to carry forward is that whenever a construction is "well defined up to the centre", the answers of this exercise say exactly how much ambiguity that is: a circle's worth for $U(n)$, a sign for $SU(2)$, none for $SO(3)$. The companion exercises for this page are the compound definition page's own examples (left multiplication is free and transitive; the trivial action; the action induced by a representation) on [[Def - Free, Transitive, Effective, and Proper Group Actions]], and [[Ex - Inner automorphisms and the centre]] in the group-theory part of the vault, which proves the abstract statement $\operatorname{Inn}(G) \cong G/Z(G)$ that the present exercise instantiates.
