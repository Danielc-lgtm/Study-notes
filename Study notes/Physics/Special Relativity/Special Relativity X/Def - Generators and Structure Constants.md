---
type: definition
subject: special-relativity
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Infinitesimal Lorentz Transformations"
  - "Def - Lie Algebra"
tags: [physics, special-relativity, lie-groups]
---

# Notation

We set $c = 1$, $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - Lie Algebra of the Lorentz Group|Lorentz algebra]] $\mathfrak{so}(1,3)$ has the six **generators** $K_1,K_2,K_3$ (boosts) and $J_1,J_2,J_3$ (rotations), collectively written $G_a$ for $a \in \{1,\dots,6\}$ with $G_1 = K_1$, $G_2 = K_2$, $G_3 = K_3$, $G_4 = J_1$, $G_5 = J_2$, $G_6 = J_3$. The bracket is the matrix commutator $[\,\cdot\,,\,\cdot\,]$. The **structure constants** are the real numbers $C_{ab}{}^c$. The fully antisymmetric symbol $\epsilon_{ijk}$ ($i,j,k \in \{1,2,3\}$) is $+1$ on even permutations of $(1,2,3)$, $-1$ on odd, $0$ otherwise. Full registry on [[Special Relativity X — The Lorentz Group as a Lie Group]].

This is a compound page: it defines two interlocking notions — the **generators** of the Lorentz group and its **structure constants** — because the structure constants are *defined as* the coefficients expressing the brackets of the generators back in terms of the generators, and neither is fully usable without the other.

---

# Axiom Motivation

A [[Def - Lie Algebra|Lie algebra]] is a vector space with a bracket, and the most economical way to record a finite-dimensional Lie algebra is to choose a basis and write down what the bracket does to the basis vectors. Everything else follows by bilinearity. The **generators** are that chosen basis of $\mathfrak{so}(1,3)$; the **structure constants** are the table of bracket-values on the basis. This page introduces both, and the motivation is the recognition that a six-dimensional algebra is not really six dimensions of data — it is the much smaller data of how six things bracket together, and once you have that table you have the entire algebra and (by exponentiation and Baker–Campbell–Hausdorff) the entire local structure of the group.

Why call the basis vectors "generators"? Because each one generates a one-parameter subgroup by exponentiation: $K_i$ generates the boosts in a fixed plane, $J_i$ generates the rotations about a fixed axis, and the finite element $\exp(t\,G_a)$ traces out a curve through the group as $t$ runs over $\mathbb{R}$. So the $G_a$ are "generators" in the literal sense that the whole connected group is built from their exponentials. The choice of *which* six matrices to call the generators is a convention, but a well-motivated one: we pick the matrices that are infinitesimal versions of the boosts and rotations the reader already knows, so that the abstract algebra connects directly to the physical transformations.

The structure constants exist because of a single non-obvious fact: the algebra is **closed under the bracket**. The commutator of any two generators is again an element of $\mathfrak{so}(1,3)$ ([[Def - Lie Algebra of the Lorentz Group|the algebra is bracket-closed]]), hence — being a six-dimensional vector space — a unique linear combination of the six generators. The coefficients in that combination are the structure constants $C_{ab}{}^c$:
$$
[G_a, G_b] \;=\; \sum_{c=1}^{6} C_{ab}{}^{c}\, G_c.
$$
If the algebra were *not* closed under the bracket, there would be no such expansion and no structure constants; closure is exactly what makes the definition well-posed. There are $6 \times 6 \times 6 = 216$ of these coefficients in principle, but antisymmetry of the bracket ($C_{ab}{}^c = -C_{ba}{}^c$) and the simple geometry of the Lorentz algebra make almost all of them zero, and every nonzero one equals $\pm 1$.

Why are the structure constants the *right* invariant to extract, as opposed to, say, the explicit matrices? Because they are **basis-data that determine the group law**. The Baker–Campbell–Hausdorff formula expresses the product $\exp(L_1)\exp(L_2)$ entirely in terms of iterated brackets of $L_1$ and $L_2$, and iterated brackets are computed from the structure constants alone. So the structure constants contain all the information about how $SO^+(1,3)$ multiplies, packaged as a finite table of integers. They are also the data that transfers between algebras: two Lie algebras are isomorphic exactly when there is a change of basis making their structure constants agree, which is how one recognises that $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$ — a fact invisible at the level of the explicit $4\times 4$ matrices but transparent once the structure constants are split by the $(A,B)$ change of basis.

One caution motivates the careful bookkeeping. The structure constants depend on the choice of basis, so they are not intrinsic numbers attached to the algebra — only their orbit under change of basis is. What *is* intrinsic, and what the structure constants compute, is the isomorphism class of the bracket: the Jacobi identity $[G_a,[G_b,G_c]] + \text{cyclic} = 0$ imposes a quadratic constraint $\sum_e (C_{bc}{}^e C_{ae}{}^d + C_{ca}{}^e C_{be}{}^d + C_{ab}{}^e C_{ce}{}^d) = 0$ on the constants, and any table of constants satisfying both antisymmetry and this Jacobi constraint defines a genuine Lie algebra. The Lorentz structure constants satisfy it automatically, since they come from an honest matrix commutator.

---

# The Definition

Let $(G_a)_{a=1}^{6} = (K_1,K_2,K_3,J_1,J_2,J_3)$ be the [[Def - Lie Algebra of the Lorentz Group|generators]] of $\mathfrak{so}(1,3)$, a basis of the algebra. Because $\mathfrak{so}(1,3)$ is closed under the [[Def - Lie Algebra|Lie bracket]] (the commutator), the bracket of any two generators is a linear combination of the generators, defining the **structure constants** $C_{ab}{}^c \in \mathbb{R}$ by
$$
[G_a, G_b] \;=\; \sum_{c=1}^{6} C_{ab}{}^{c}\, G_c,
\qquad a,b \in \{1,\dots,6\}.
$$
For the Lorentz group, with the boost/rotation labelling above, every structure constant is $0$, $+1$, or $-1$, and the full table is encoded in the three vector relations (sums over $k \in \{1,2,3\}$):
$$
[J_i, J_j] = \sum_k \epsilon_{ijk}\, J_k,
\qquad
[J_i, K_j] = \sum_k \epsilon_{ijk}\, K_k,
\qquad
[K_i, K_j] = -\sum_k \epsilon_{ijk}\, J_k.
$$
Written out, the nonzero brackets are
$$
[J_1,J_2]=J_3,\ [J_2,J_3]=J_1,\ [J_3,J_1]=J_2;
$$
$$
[J_1,K_2]=K_3,\ [J_2,K_3]=K_1,\ [J_3,K_1]=K_2,\ \text{and } [J_i,K_i]=0;
$$
$$
[K_1,K_2]=-J_3,\ [K_2,K_3]=-J_1,\ [K_3,K_1]=-J_2,
$$
together with antisymmetry $[G_b,G_a] = -[G_a,G_b]$ and $[G_a,G_a]=0$. The numbers $C_{ab}{}^c$ satisfy two universal constraints inherited from the bracket: **antisymmetry** $C_{ab}{}^c = -C_{ba}{}^c$, and the **Jacobi identity** in the form
$$
\sum_{e}\big(C_{ab}{}^{e}C_{ec}{}^{d} + C_{bc}{}^{e}C_{ea}{}^{d} + C_{ca}{}^{e}C_{eb}{}^{d}\big) = 0.
$$

The three relations have a clean reading. The first says the $J_i$ form a closed subalgebra, a copy of $\mathfrak{so}(3)$ (the rotation generators). The second says the boost generators $K_i$ rotate as a $3$-vector under the $J_i$. The third — that two boost generators commute into *minus* a rotation generator — says the boosts do **not** close into a subalgebra, and is the algebraic origin of the [[Def - Thomas Rotation|Thomas rotation]].

---

# Relate to Other Fields / Compression

Structure constants are the universal language for describing any Lie algebra by a finite table, and they are how gauge theory and particle physics specify their symmetry algebras. In [[Gauge Theory — Series Map|gauge theory]] the field strength of a non-abelian connection is $F = dA + \tfrac12[A,A]$, and the bracket $[A,A]$ is computed component-wise through the structure constants of the gauge algebra; for $\mathfrak{su}(N)$ these are the totally antisymmetric $f_{abc}$, and the Lorentz structure constants $\pm\epsilon_{ijk}$ play the identical role for the spacetime symmetry algebra. The rotation block reproduces the most familiar structure constants in physics: $[J_i,J_j] = \epsilon_{ijk}J_k$ is the angular-momentum algebra, with the $\epsilon_{ijk}$ as its structure constants, and on the quantum side $[\hat L_i,\hat L_j] = i\hbar\,\epsilon_{ijk}\hat L_k$.

**True name:** the structure constants are **"the multiplication table of the bracket on a chosen basis"** — exactly the data $[G_a,G_b]$ for all $a,b$, read off as coefficients in the basis. For the Lorentz group this table is "$\epsilon$ with three signs": rotations bracket to plus a rotation, rotation-with-boost brackets to plus a boost, boost-with-boost brackets to minus a rotation. The single fact worth memorising is the sign pattern $(+,+,-)$ on $([J,J],[J,K],[K,K])$, because it distinguishes the non-compact Lorentz algebra from the compact $\mathfrak{so}(4)$ (which has $(+,+,+)$) and is the difference between a boost rapidity that runs to infinity and a rotation angle that wraps around.

---

# Examples / Corollaries

**Is an instance — the rotation structure constants.** Restricting to $G_4,G_5,G_6 = J_1,J_2,J_3$, the structure constants are $C_{ij}{}^k = \epsilon_{ijk}$ (with indices in the rotation block), the structure constants of $\mathfrak{so}(3) \cong (\mathbb{R}^3,\times)$. This is the sub-table that the rotation subalgebra carries, identical to the cross-product structure constants of [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]].

**Is an instance — a vanishing structure constant.** $[J_1, K_1] = 0$ because $\epsilon_{11k} = 0$: a rotation about $x$ commutes with a boost along $x$, since the rotation fixes the $x$-axis along which the boost acts. Hence $C_{4,1}{}^c = 0$ for all $c$ (with $G_4 = J_1$, $G_1 = K_1$). Many of the $216$ structure constants vanish this way.

**Is an instance — a structure constant equal to $-1$.** $[K_1, K_2] = -J_3$ means $C_{1,2}{}^{6} = -1$ (with $G_1 = K_1$, $G_2 = K_2$, $G_6 = J_3$). The minus sign is the signature of non-compactness, and it is the *only* place the boost-boost relation differs from the rotation-rotation relation.

**Is NOT an instance — a symmetric "structure constant" table.** Structure constants are antisymmetric in their lower indices, $C_{ab}{}^c = -C_{ba}{}^c$. A table with $C_{ab}{}^c = +C_{ba}{}^c$ for some $a\ne b$ cannot come from a Lie bracket, since the bracket is antisymmetric. This rules out, for instance, ever writing $[K_1,K_2] = +[K_2,K_1]$.

**Corollary — the Killing form and non-compactness.** The Killing form $B(G_a,G_b) = \sum_{c,d} C_{ac}{}^d C_{bd}{}^c$ is computed from the structure constants alone. For $\mathfrak{so}(1,3)$ it is non-degenerate (the algebra is *simple*) but **indefinite** — it has signature $(3,3)$, with the boosts contributing the opposite sign to the rotations — which is the structure-constant fingerprint of the group's non-compactness. A *compact* simple algebra such as $\mathfrak{so}(4)$ has a negative-definite Killing form.

**Corollary — the algebra is perfect.** Every generator appears on the right-hand side of some bracket: $J_k$ from $[J_i,J_j]$, $K_k$ from $[J_i,K_j]$. So $\mathfrak{so}(1,3) = [\mathfrak{so}(1,3),\mathfrak{so}(1,3)]$ — the algebra equals its own derived algebra, the property of being **perfect**, which holds for any simple Lie algebra.

**Calibration check.** You should be able to: (1) write $[K_2,K_3]$ from the relations and get $-J_1$; (2) state which structure constants vanish and why (any bracket of a $J$ or $K$ with the like-indexed partner); (3) explain why the sign pattern $(+,+,-)$ distinguishes $\mathfrak{so}(1,3)$ from the compact $\mathfrak{so}(4)$.

---

# Unlocked by This

> [!tip] The Baker–Campbell–Hausdorff Composition Law *(from §10.3)*
> Because the product $\exp(L_1)\exp(L_2) = \exp\!\big(L_1 + L_2 + \tfrac12[L_1,L_2] + \cdots\big)$ is built from iterated brackets, and iterated brackets are computed from the structure constants, **all the information about the group law of $SO^+(1,3)$ is contained in the $C_{ab}{}^c$**. The composition of two non-collinear boosts, evaluated this way, produces the Thomas rotation; see [[Thm - The Exponential Map Generates the Restricted Lorentz Group]].

> [!tip] The (A,B) Change of Basis *(from §10.3)*
> Changing basis from $(J_i, K_i)$ to $A_i = \tfrac12(J_i + iK_i)$, $B_i = \tfrac12(J_i - iK_i)$ transforms the structure constants into two *decoupled* copies of the $\mathfrak{su}(2)$ table: $[A_i,A_j]=\epsilon_{ijk}A_k$, $[B_i,B_j]=\epsilon_{ijk}B_k$, $[A_i,B_j]=0$. The structure constants make the isomorphism $\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{su}(2)_{\mathbb{C}}\oplus\mathfrak{su}(2)_{\mathbb{C}}$ explicit; see [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]].

> [!tip] Casimir Invariants *(from Quantum Field Theory)*
> From the structure constants one builds the **Casimir operators** — combinations of generators commuting with the whole algebra. For the Lorentz algebra these are $J^2 - K^2$ and $\mathbf{J}\cdot\mathbf{K}$; adjoining translations gives the Poincaré Casimirs $P^2 = m^2$ and the Pauli–Lubanski square, the **mass and spin** of Wigner's classification. See [[Special Relativity XII — Inertial Observers and the Poincaré Group]].
