---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Infinitesimal Lorentz Transformations"
  - "Def - Lie Algebra"
  - "Def - The Lie Algebra of a Lie Group"
tags: [physics, special-relativity, lie-groups]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. [[Def - Minkowski Space and the Metric|Minkowski space]] carries coordinates $x^\mu = (t,x,y,z)$, $\mu = 0,1,2,3$; Latin indices $i,j,k$ run over the spatial values $1,2,3$. A [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda$ is a real $4\times 4$ matrix obeying $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; the restricted (proper orthochronous) group is $SO^+(1,3)$. The Lie algebra is written $\mathfrak{so}(1,3)$, lower-case, and its elements are $4\times 4$ real matrices $\omega, L, M$. The six generators are the boost generators $K_1, K_2, K_3$ and the rotation generators $J_1, J_2, J_3$. The matrix commutator is $[A,B] = AB - BA$. The fully antisymmetric symbol $\epsilon_{ijk}$ is $+1$ on even permutations of $(1,2,3)$, $-1$ on odd, $0$ otherwise. Full registry on [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!warning] Convention: opposite signature and a different generator-sign in Gourgoulhon
> Gourgoulhon's *Special Relativity in General Frames* (Chapter 7) uses the mostly-**plus** signature $\eta = \mathrm{diag}(-1,1,1,1)$, writes the group $O(3,1)$, and defines the boost generators as $K_i = -\mathscr{J}_{0i}$. The combination of the metric flip and that sign choice makes his commutators (his Eq. 7.44) read $[K_i,K_j] = -\epsilon_{ijk}J_k$, $[K_i,J_j] = -\epsilon_{ijk}K_k$, $[J_i,J_j] = \epsilon_{ijk}J_k$. We follow the mostly-**minus** convention of Giulini (his Eq. 51), in which the boost generators are $K_i = +\mathscr{J}_{i0}$ and the structure relations come out as the $J,K$ relations stated below — the form most standard in the physics literature. The two conventions describe the *same* Lie algebra; only the labelling of the boost generator (an overall sign on $K_i$) and the placement of one minus sign differ.

> [!warning] Convention: mathematicians' versus physicists' generators
> We define the generators so that a finite Lorentz transformation is $\Lambda = \exp(\omega)$ with $\omega \in \mathfrak{so}(1,3)$ — **no factor of $i$**, real generators, real Lie algebra. This is the mathematics convention used by Gourgoulhon, Giulini, and the vault's [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie-theory chapter]]. Quantum-field-theory texts instead write $\Lambda = \exp(i\theta^a T_a)$ with **Hermitian** generators $T_a = -iG_a$, which inserts an $i$ into every structure constant: their relations read $[T_i^{(J)}, T_j^{(J)}] = i\epsilon_{ijk}T_k^{(J)}$. To convert, multiply each of our generators by $i$. We flag this because the $(A,B)$ decomposition below is usually quoted in the physicists' form $[A_i,A_j] = i\epsilon_{ijk}A_k$.

---

# Axiom Motivation

The [[Def - The Lorentz Group|Lorentz group]] $SO^+(1,3)$ is a continuous group: its elements depend smoothly on six parameters (three rotation angles, three rapidities). The single most powerful idea in the theory of continuous groups, due to Sophus Lie, is that almost everything about such a group is already encoded in its behaviour *infinitesimally close to the identity* — in the tangent space at the identity, made into an algebra by a bracket. This page builds that object for the Lorentz group. The desideratum is a finite-dimensional vector space, with a bilinear bracket, that captures the group multiplication of $SO^+(1,3)$ to first order, and from which the whole group can be recovered by exponentiation.

Why expect such a linearisation to exist and to be useful? Because the group is a manifold and the multiplication is smooth, the set of velocities of curves through the identity — the tangent space $T_{\mathrm{Id}}SO^+(1,3)$ — is a genuine vector space of dimension $6$, the dimension of the group. The content of [[Def - The Lie Algebra of a Lie Group|the general construction]] is that this vector space carries a canonical bracket, and that the bracket remembers the *non-commutativity* of the group: if two group elements fail to commute, their generators fail to bracket-commute, and the leading-order discrepancy $\Lambda_1\Lambda_2\Lambda_1^{-1}\Lambda_2^{-1} = \mathrm{Id} + \varepsilon^2[L_1,L_2] + O(\varepsilon^3)$ is exactly the Lie bracket. So the bracket is not an arbitrary decoration; it is forced on the tangent space the moment you ask it to record how the group multiplies.

The construction has two pieces to pin down, and each is a design decision worth dwelling on. The first is the **underlying vector space**: which $4\times 4$ matrices $\omega$ are tangent to $SO^+(1,3)$ at the identity? This is settled by [[Def - Infinitesimal Lorentz Transformations|differentiating the defining equation]] $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ along a curve $\Lambda(s) = \mathrm{Id} + s\,\omega + O(s^2)$. Substituting and collecting the order-$s$ term gives $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ — the matrices that are *antisymmetric once an index is lowered by $\eta$*. If we dropped this condition and allowed all $4\times 4$ matrices, we would get $\mathfrak{gl}(4,\mathbb{R})$, the Lie algebra of $GL(4,\mathbb{R})$ — a $16$-dimensional algebra whose group does not preserve the interval, so a free particle would appear to accelerate under a "Lorentz" change of frame. The condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ is precisely what cuts the $16$ down to $6$ and keeps the metric fixed; it is the infinitesimal shadow of "preserves $\eta$".

The second decision is the **bracket**. One might hope that $\mathfrak{so}(1,3)$ is closed under ordinary matrix multiplication — that the product $L_1 L_2$ of two infinitesimal generators is again a generator. It is not: a direct check (carried out on the topic page) shows $L_1 L_2$ generally fails the condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$. What *is* preserved is the **commutator** $[L_1, L_2] = L_1 L_2 - L_2 L_1$: the asymmetric combination cancels exactly the terms that spoil closure under the product. This is why the natural algebraic operation on the tangent space of a matrix group is the commutator, not the product — see [[Thm - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]. If we had insisted on the product we would have no algebra at all; the commutator is the unique bilinear operation that both stays inside the tangent space and records the group's non-commutativity.

Why these three bracket axioms — bilinearity, antisymmetry, the Jacobi identity — and not some other list? Bilinearity is forced because the commutator is built from the bilinear matrix product. Antisymmetry, $[L_1,L_2] = -[L_2,L_1]$, is immediate from the definition and encodes that swapping two infinitesimal transformations reverses the sign of their leading discrepancy. The Jacobi identity $[L_1,[L_2,L_3]] + [L_2,[L_3,L_1]] + [L_3,[L_1,L_2]] = 0$ is the infinitesimal residue of the *associativity* of group multiplication; dropping it would mean the group law was not associative, which is impossible. So the three axioms are not chosen — they are the inevitable infinitesimal print of "group", and an abstract vector space satisfying them is what we call a [[Def - Lie Algebra|Lie algebra]]. The Lorentz algebra is the concrete instance attached to the Lorentz group.

The payoff, and the deepest reason to build this object, is that the bracket structure of $\mathfrak{so}(1,3)$ — six generators and their commutators — turns out to *be* the classification of relativistic fields. Splitting the algebra over the complex numbers (the $(A,B)$ decomposition) reveals it as two commuting copies of the rotation algebra $\mathfrak{su}(2)$, and the representation theory of $\mathfrak{su}(2) \oplus \mathfrak{su}(2)$ is the Wigner programme: scalars, spinors, vectors, and tensors are all labelled by a pair $(j_A, j_B)$ of half-integers. So the modest-looking question "what is the tangent space of the Lorentz group at the identity?" is the gateway to the entire field content of relativistic physics.

---

# The Definition

The **Lie algebra of the Lorentz group**, written $\mathfrak{so}(1,3)$, is the tangent space to the [[Def - The Lorentz Group|restricted Lorentz group]] $SO^+(1,3)$ at the identity, equipped with the matrix commutator as its [[Def - Lie Algebra|Lie bracket]]. Concretely it is the real vector space of $4\times 4$ real matrices $\omega$ satisfying
$$
\omega^{\mathsf T}\,\eta + \eta\,\omega \;=\; 0,
\qquad
\eta = \mathrm{diag}(1,-1,-1,-1),
$$
equivalently the matrices for which $\eta\,\omega$ is antisymmetric (see [[Def - Infinitesimal Lorentz Transformations]]), with bracket
$$
[L_1, L_2] \;=\; L_1 L_2 - L_2 L_1.
$$
It has **dimension $6$**, matching the dimension of the group.

**The basis of generators.** A general element of $\mathfrak{so}(1,3)$ is parametrised by six real numbers $(k_1,k_2,k_3,j_1,j_2,j_3)$ as
$$
\omega \;=\; k_1 K_1 + k_2 K_2 + k_3 K_3 + j_1 J_1 + j_2 J_2 + j_3 J_3,
$$
where the **boost generators** $K_i$ and **rotation generators** $J_i$ are the matrices
$$
K_1 = \begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix},\
K_2 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&0\\ 1&0&0&0\\ 0&0&0&0 \end{pmatrix},\
K_3 = \begin{pmatrix} 0&0&0&1\\ 0&0&0&0\\ 0&0&0&0\\ 1&0&0&0 \end{pmatrix},
$$
$$
J_1 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&0\\ 0&0&0&-1\\ 0&0&1&0 \end{pmatrix},\
J_2 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&1\\ 0&0&0&0\\ 0&-1&0&0 \end{pmatrix},\
J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&-1&0\\ 0&1&0&0\\ 0&0&0&0 \end{pmatrix}.
$$
The $K_i$ are **symmetric** matrices that mix the time direction with the $i$-th space direction; the $J_i$ are **antisymmetric** matrices that act on the spatial part as the cross product by $\mathbf{e}_i$, that is $J_i\,\mathbf{v} = \mathbf{e}_i \times \mathbf{v}$ on the spatial block, so $J_i$ generates rotations in the plane orthogonal to $\mathbf{e}_i$. (One checks that each satisfies $\omega^{\mathsf T}\eta + \eta\,\omega = 0$: for the $K_i$, $\eta K_i$ is antisymmetric because the symmetric $K_i$ has its single nonzero pair across the time row/column, which $\eta$ flips in sign; for the $J_i$, $\eta J_i = -J_i$ on the purely spatial block, still antisymmetric.)

**The commutation relations** are the entire algebraic content. Writing all sums over the repeated index $k$ from $1$ to $3$,
$$
[J_i, J_j] = \sum_k \epsilon_{ijk}\, J_k,
\qquad
[J_i, K_j] = \sum_k \epsilon_{ijk}\, K_k,
\qquad
[K_i, K_j] = -\sum_k \epsilon_{ijk}\, J_k.
$$
Explicitly, $[J_1,J_2] = J_3$, $[J_1,K_2] = K_3$, $[K_1,K_2] = -J_3$, and cyclically. The first relation says the $J_i$ close into the rotation subalgebra $\mathfrak{so}(3)$. The second says the boost generators transform as a vector under rotations. The third — **the crucial one** — says that the commutator of two boost generators is a *rotation* generator, with a minus sign: this is the algebraic seed of the [[Def - Thomas Rotation|Thomas rotation]] and the reason the boosts do not form a subgroup.

---

# Categorical / Structural Definition

The Lie algebra of the Lorentz group is an object of the category of finite-dimensional real [[Def - Lie Algebra|Lie algebras]], and it is the value at $SO^+(1,3)$ of the **Lie functor** $\mathrm{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ that sends each [[Def - Lie Group|Lie group]] $G$ to its tangent space at the identity with the commutator bracket, and each Lie group homomorphism $F : G \to H$ to its derivative $dF_{\mathrm{Id}} : \mathfrak{g} \to \mathfrak{h}$ (a Lie algebra homomorphism). Under this functor, structural facts about the group become structural facts about the algebra: the group's dimension is the algebra's dimension, and a covering map of groups becomes an isomorphism of algebras — which is exactly why the double cover $SL(2,\mathbb{C}) \to SO^+(1,3)$ induces an *isomorphism* $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$ of (real six-dimensional) Lie algebras even though the groups differ.

Intrinsically — without choosing a basis — $\mathfrak{so}(1,3)$ is the algebra of **$\eta$-skew endomorphisms** of $(\mathbb{R}^4,\eta)$: the linear maps $L$ with $\eta(L\,X, Y) + \eta(X, L\,Y) = 0$ for all $X,Y$. This is the indefinite-signature cousin of $\mathfrak{so}(n)$, the antisymmetric (genuinely skew) endomorphisms of Euclidean space, and it sits inside the uniform family $\mathfrak{so}(p,q)$ of skew endomorphisms of a signature-$(p,q)$ form. The defining condition $\eta(L\,X,Y) = -\eta(X,L\,Y)$ is the infinitesimal form of "$\Lambda$ preserves $\eta$": differentiate $\eta(\Lambda X, \Lambda Y) = \eta(X,Y)$ at $\Lambda = \mathrm{Id}$ and the product rule gives exactly skewness. Two further structural labels matter downstream. The algebra is **simple** — it has no proper nonzero ideal — which is why it cannot be split into independent pieces over the reals and why its Killing form is non-degenerate. And its **complexification** $\mathfrak{so}(1,3)_{\mathbb{C}}$ is isomorphic to $\mathfrak{sl}(2,\mathbb{C}) \oplus \mathfrak{sl}(2,\mathbb{C})$, a fact developed in [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]] and the organising principle of all Lorentz representations.

---

# Relate to Other Fields / Compression

The Lorentz algebra is the rotation algebra with three of its six generators "rotated into imaginary angles". Concretely, $\mathfrak{so}(4)$ — the algebra of four-dimensional Euclidean rotations — has six antisymmetric generators and splits cleanly as $\mathfrak{so}(4) \cong \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ over the reals. The Lorentz algebra $\mathfrak{so}(1,3)$ is obtained by the single sign flip $\eta = \mathrm{diag}(1,1,1,1) \to \mathrm{diag}(1,-1,-1,-1)$, which turns the three rotations-into-time of $\mathfrak{so}(4)$ into the three boosts of $\mathfrak{so}(1,3)$, and the consequence is that the real direct-sum split of $\mathfrak{so}(4)$ becomes a split only after **complexifying** $\mathfrak{so}(1,3)$. This is the precise sense in which Minkowski geometry is "Euclidean geometry with one imaginary axis": $\mathfrak{so}(1,3)$ is the real form of $\mathfrak{so}(4)_{\mathbb{C}} = \mathfrak{su}(2)_{\mathbb{C}} \oplus \mathfrak{su}(2)_{\mathbb{C}}$ in which the two summands are exchanged by complex conjugation rather than each being real on its own.

**True name:** $\mathfrak{so}(1,3)$ is **"three rotation generators that close among themselves, plus three boost generators that the rotations spin as a vector and whose mutual commutators are rotations with a minus sign"**. That single sentence reconstructs all the commutators: $[J,J] = J$ (rotations close), $[J,K] = K$ ($K$ is a vector under rotations), $[K,K] = -J$ (boosts fail to close, and the failure is a rotation, oppositely signed). The minus sign in $[K,K] = -J$ is the operational heart of the algebra — it is what distinguishes the non-compact Lorentz algebra from the compact $\mathfrak{so}(4)$, where the corresponding relation has a plus sign. When you need to remember the algebra, do not memorise nine bracket tables; remember "boosts almost-close, into minus a rotation", and the rest is the vector and subalgebra structure.

The same construction recurs across physics. In [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]] the angular-momentum components obey $\{L_i, L_j\} = \epsilon_{ijk}L_k$ under the Poisson bracket — the same relation as $[J_i,J_j] = \epsilon_{ijk}J_k$, so the rotational part of the Lorentz algebra is literally the algebra of angular momentum, and on the quantum side it becomes $[\hat L_i, \hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$. The cross product on $\mathbb{R}^3$ is yet another incarnation, $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ via the hat map (see [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]]). So the rotation block of $\mathfrak{so}(1,3)$ is an object the reader already knows under three names — angular momentum, the cross product, $\mathfrak{su}(2)$ — and the new content is only how the boosts attach to it.

---

# Examples / Corollaries

**Is an instance — a pure boost generator.** $K_1$ generates boosts in the $t$–$x$ plane. Its exponential is $\exp(\psi K_1) = \mathrm{Id} + \sinh\psi\,K_1 + (\cosh\psi - 1)K_1^2$, the boost of rapidity $\psi$ with $\cosh\psi$ and $\sinh\psi$ in the time–space corner (computed in [[Ex - Exponentiating a boost generator gives a hyperbolic boost]]). Here $K_1^2 = \mathrm{diag}(1,1,0,0)$, the projector onto the $t$–$x$ plane, which truncates the exponential series into the hyperbolic functions.

**Is an instance — a pure rotation generator.** $J_3$ generates rotations in the $x$–$y$ plane. Its exponential $\exp(\varphi J_3)$ is the ordinary rotation by angle $\varphi$ in the $x$–$y$ block, with $\cos\varphi$, $\sin\varphi$ entries, because $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ and the series resums to circular functions (see [[Ex - Exponentiating a rotation generator gives a rotation]]). Note the contrast with $K_1$: $K_1^2$ has a $+1$ where $J_3^2$ has a $-1$, and that single sign is the whole difference between hyperbolic and circular trigonometry.

**Is an instance — a general element with both boost and rotation parts.** $\omega = \psi K_1 + \varphi J_3$ is a perfectly good element of $\mathfrak{so}(1,3)$, but $\exp(\omega) \ne \exp(\psi K_1)\exp(\varphi J_3)$ in general, because $K_1$ and $J_3$ do not commute ($[K_1,J_3] = [J_3,K_1]\cdot(-1)$, and $[J_3,K_1] = \epsilon_{312}K_2\cdot$... $= K_2 \ne 0$ in fact $[J_3,K_1]=\epsilon_{31k}K_k = -\epsilon_{13k}K_k = K_2$). The exponential of the sum mixes them via the Baker–Campbell–Hausdorff formula, which is exactly the origin of the [[Def - Thomas Rotation|Thomas rotation]].

**Is NOT an instance — a generic symmetric matrix.** A symmetric $4\times 4$ matrix such as $\mathrm{diag}(0,1,1,1)$ does *not* lie in $\mathfrak{so}(1,3)$: for it $\eta\,\omega = \mathrm{diag}(0,-1,-1,-1)$ is symmetric, not antisymmetric, so $\omega^{\mathsf T}\eta + \eta\,\omega = 2\eta\,\omega \ne 0$. The boost generators are symmetric, but symmetry alone is not the criterion — the criterion is that $\eta\,\omega$ be antisymmetric, which the $K_i$ satisfy precisely because their symmetric nonzero entries straddle the time index.

**Is NOT an instance — the product of two generators.** $K_1 K_2$ is *not* in $\mathfrak{so}(1,3)$. Compute: $K_1 K_2$ has a single nonzero entry, $(K_1 K_2)_{21}\ne 0$ region, and $\eta(K_1 K_2) + (K_1 K_2)^{\mathsf T}\eta \ne 0$. This is the concrete failure of closure under the matrix product, and the reason the bracket must be the *commutator* $[K_1,K_2] = K_1 K_2 - K_2 K_1 = -J_3$, which *is* in the algebra.

**Corollary — the dimension count.** The condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ says $\eta\,\omega$ is one of the $\binom{4}{2} = 6$ independent antisymmetric $4\times 4$ matrices, so $\dim\mathfrak{so}(1,3) = 6$, matching $\dim SO^+(1,3) = 6$. This is the infinitesimal version of the parameter count $16 - 10 = 6$ for the group.

**Corollary — the trace vanishes.** Every $\omega \in \mathfrak{so}(1,3)$ has $\mathrm{tr}\,\omega = 0$. From $\eta\,\omega$ antisymmetric, $\omega = \eta(\eta\,\omega)$ has $\mathrm{tr}\,\omega = \mathrm{tr}(\eta\cdot\text{antisym})$, and a direct check on the basis gives $\mathrm{tr}\,K_i = \mathrm{tr}\,J_i = 0$. Hence $\det\exp(\omega) = e^{\mathrm{tr}\,\omega} = 1$, confirming that exponentials land in the *proper* ($\det = +1$) Lorentz group.

**Calibration check.** You should be able to: (1) verify $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ for $K_1$ and for $J_3$ by a $4\times 4$ multiplication; (2) compute $[K_1,K_2]$ directly from the matrices and obtain $-J_3$; (3) state, without computing, why $\exp(\psi K_1)$ uses $\cosh,\sinh$ while $\exp(\varphi J_3)$ uses $\cos,\sin$ — namely the sign of the square of the generator.

---

# Unlocked by This

> [!tip] The Exponential Map onto SO⁺(1,3) *(from §10.3)*
> The generators are the infinitesimal data; the **exponential map** $\exp : \mathfrak{so}(1,3) \to SO^+(1,3)$, $\omega \mapsto \exp(\omega)$, recovers the finite transformations and is *surjective* onto the restricted Lorentz group ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]]). Every boost is $\exp(\psi\,\mathbf{n}\cdot\mathbf{K})$ and every rotation is $\exp(\varphi\,\mathbf{n}\cdot\mathbf{J})$.

> [!tip] The (A,B) Decomposition and the Classification of Fields *(from §10.3 and Quantum Field Theory)*
> Complexifying and forming $A_i = \tfrac12(J_i + iK_i)$, $B_i = \tfrac12(J_i - iK_i)$ splits the algebra into two commuting copies of $\mathfrak{su}(2)$ ([[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]]). The irreducible representations are then labelled by a pair $(j_A, j_B)$ of half-integers: the scalar $(0,0)$, the left and right **Weyl spinors** $(\tfrac12,0)$ and $(0,\tfrac12)$, the four-vector $(\tfrac12,\tfrac12)$, the Dirac spinor $(\tfrac12,0)\oplus(0,\tfrac12)$, and the electromagnetic field strength $(1,0)\oplus(0,1)$. This $(A,B)$ labelling is the backbone of all relativistic **field representations**.

> [!tip] The Double Cover and Spinors *(from Spinors)*
> Because $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$ as real Lie algebras but $SO^+(1,3)$ is not simply connected ([[Thm - Topology of the Lorentz Group]]), the algebra has *more* representations than the group: those of the universal cover $SL(2,\mathbb{C})$, which include the half-integer-spin **spinor** representations on which a $2\pi$ rotation acts as $-1$. See [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

> [!tip] The Poincaré Algebra and the Casimir Invariants *(from Quantum Field Theory)*
> Adjoining the four translation generators $P_\mu$ to the six $J_i, K_i$ gives the **Poincaré algebra** ([[Def - The Poincaré Group]]). Its two Casimir invariants — $P^\mu P_\mu = m^2$ and the square of the Pauli–Lubanski vector $= -m^2 s(s+1)$ — are the **mass and spin** that Wigner showed label every elementary particle. The Lorentz algebra built here is the homogeneous part of that structure; see [[Special Relativity XII — Inertial Observers and the Poincaré Group]].
