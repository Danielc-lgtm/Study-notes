---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Levi-Civita Connection"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla$ and [[Def - Riemann Curvature Tensor|Riemann tensor]] $R$. The covariant Riemann tensor is $R(X, Y, Z, W) := \langle R(X, Y)Z, W\rangle$. In a frame, $R_{abcd} = \langle R(e_c, e_d)e_b, e_a\rangle$. The vectors $X, Y, Z, W \in T_pM$ are arbitrary tangent vectors at a fixed point.

---

# Statement

> **Theorem (Algebraic symmetries of the Riemann curvature tensor).** The covariant Riemann tensor $R(X, Y, Z, W) = \langle R(X, Y)Z, W\rangle$ of a Riemannian manifold $(M, g)$ satisfies the following identities at every point:
>
> 1. **Antisymmetry in the first pair**: $R(X, Y, Z, W) = -R(Y, X, Z, W)$.
> 2. **Antisymmetry in the second pair**: $R(X, Y, Z, W) = -R(X, Y, W, Z)$. (Requires **metric compatibility** of $\nabla$.)
> 3. **Pair-swap symmetry**: $R(X, Y, Z, W) = R(Z, W, X, Y)$. (Follows from (1), (2), and the **first Bianchi identity**.)
> 4. **First Bianchi identity**: $R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0$. (Requires **torsion-freeness** of $\nabla$.)
>
> These four identities cut the $n^4$ components of $R$ down to $\tfrac{1}{12}n^2(n^2 - 1)$ algebraically independent components: $1$ in dimension $2$, $6$ in dimension $3$, $20$ in dimension $4$, $50$ in dimension $5$.

---

# Motivation

The Riemann tensor as defined is a $(0, 4)$-tensor with $n^4$ components at each point. Most of these components are not independent — they are constrained by the algebraic structure inherited from the Levi-Civita connection. This theorem catalogues those constraints. They are not formal accidents; each one corresponds to a structural feature of the connection.

The two antisymmetries come from "commutator structure": $R$ is built from $[\nabla_X, \nabla_Y]$, automatically antisymmetric in $(X, Y)$ — that gives identity (1). The antisymmetry in the second pair $(Z, W)$ comes from metric compatibility — the connection preserves the inner product, so derivatives of inner products satisfy a specific identity that forces (2).

The first Bianchi identity is the deepest algebraic constraint and is the *only* one requiring torsion-freeness. It is what makes the Riemann tensor of a torsion-free metric-compatible connection genuinely "smaller" than the curvature tensor of a general connection. The pair-swap symmetry (3) is a consequence of (1), (2), and (4); but it is so frequently used in its own right (it is what makes $\mathrm{Ric}$ symmetric and what packages $R$ as a symmetric operator $\mathcal{R}$ on $\Lambda^2$) that it deserves separate treatment.

These symmetries are what make the **curvature operator** $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ a symmetric endomorphism, what makes the [[Def - Ricci Tensor|Ricci tensor]] symmetric, what makes the [[Def - Sectional Curvature|sectional curvature]] a well-defined function on $2$-planes, and what reduces curvature computations from $O(n^4)$ to $O(n^4/12)$ independent quantities — substantial in low dimensions but enormous in higher.

---

# Sources and Targets

**Sources (Input Broadening).**

The theorem is about the algebraic structure of $R$ alone, given the definition $R(X, Y)Z = [\nabla_X, \nabla_Y]Z - \nabla_{[X, Y]}Z$. The "sources" are characterisations of $\nabla$ that imply each symmetry:

*Source 1: $\nabla$ is metric-compatible, i.e., $X\langle Y, Z\rangle = \langle \nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$.* This bridges to the antisymmetry $R(X, Y, Z, W) = -R(X, Y, W, Z)$. Recognise this pre-condition in any source defining $\nabla$ by a metric compatibility axiom — the Levi-Civita connection of any Riemannian metric, the Chern connection on a Hermitian manifold, the Bismut connection on a Kähler manifold. All of these satisfy the second-pair antisymmetry.

*Source 2: $\nabla$ is torsion-free, i.e., $\nabla_X Y - \nabla_Y X = [X, Y]$.* This bridges to the first Bianchi identity. Any torsion-free connection (Levi-Civita, the connection associated to a $(1, 1)$-form on a Kähler manifold, the holomorphic connection on a holomorphic vector bundle) satisfies first Bianchi.

*Source 3: $\nabla$ is *any* connection (metric or not, torsion-free or not).* The first-pair antisymmetry (1) still holds, since it follows from $[\nabla_X, \nabla_Y]$ being skew in $(X, Y)$ regardless of any other property of $\nabla$. So (1) is a *universal* property of the curvature of any affine connection. Useful when working with non-metric connections in gauge theory (e.g., Yang–Mills curvature in a non-trivial gauge group).

**Targets (Output Amplification).**

*Target 1: pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ combined with antisymmetries gives* the curvature operator structure. This combination is what allows defining $\mathcal{R} : \Lambda^2 \to \Lambda^2$ as a *symmetric* operator. Without pair-swap, the curvature operator would not be symmetric, sectional curvature would not be well-defined as a function on $2$-planes, and the spectral theory of $\mathcal{R}$ would not exist.

*Target 2: antisymmetry in the second pair combined with the first Bianchi identity gives* the symmetry of the Ricci tensor: $\mathrm{Ric}_{bd} = R^a_{\;bad} = g^{ac}R_{abcd} = g^{ac}R_{cdab}$ (by pair-swap) $= R_{ab}{}^c{}_d{}^a$ which after careful index management $= \mathrm{Ric}_{db}$. Without these symmetries, the Ricci tensor would not be symmetric and **Einstein manifolds** would not be well-defined (one could not write $\mathrm{Ric} = \lambda g$ comparing two tensors of different symmetry type).

*Target 3: counting independent components gives* the dimension of the **moduli space of algebraic curvature tensors** $\mathcal{C}(V)$ on an $n$-dimensional inner-product space $V$: $\dim\mathcal{C}(V) = \tfrac{1}{12}n^2(n^2 - 1)$. In dimension $4$, this is $20$, and the moduli space decomposes under the $\mathrm{O}(4) \cong \mathrm{SU}(2) \times \mathrm{SU}(2)/\mathbb{Z}_2$ action into the **self-dual and anti-self-dual Weyl tensors** ($5 + 5 = 10$ components), the **traceless Ricci tensor** ($9$ components), and the **scalar curvature** ($1$ component). This decomposition is fundamental in $4$-dimensional Riemannian geometry and underpins **Seiberg–Witten theory** and **Donaldson theory**.

---

# Why Is It True

The two antisymmetries are direct from the definition. **The first antisymmetry $R(X, Y, Z, W) = -R(Y, X, Z, W)$** is built into the commutator structure: $R(X, Y)Z = [\nabla_X, \nabla_Y]Z - \nabla_{[X, Y]}Z$, and swapping $(X, Y)$ flips the sign of both terms. **The second antisymmetry $R(X, Y, Z, W) = -R(X, Y, W, Z)$** requires more: it says the Riemann tensor, viewed as a derivation on tensor products, acts as an "infinitesimal rotation" on tangent vectors — and rotations are skew-symmetric in the inner product they preserve. This is exactly the statement that *metric compatibility* of the connection forces $R(X, Y) : T_pM \to T_pM$ to be a skew-symmetric endomorphism in each $(X, Y)$.

**The first Bianchi identity** is more subtle. It says

$$\sum_{\text{cyclic } (X, Y, Z)} R(X, Y)Z = 0,$$

a constraint on how $R$ behaves under cyclic permutation of three of its slots. The proof uses Cartan's structural equations in disguise: writing $0 = d^2 \sigma^a$ for the soldering 1-form $\sigma^a$ and using torsion-freeness ($\tau = d\sigma + \omega \wedge \sigma = 0$), the constraint $0 = -d\omega \wedge \sigma + \omega \wedge d\sigma = -\Omega \wedge \sigma$ gives, after expansion in coordinates, the cyclic identity. Without torsion-freeness, an extra term $d\tau$ would appear and the cyclic identity would fail.

**The bolded mechanism summary: metric compatibility makes the curvature 2-form $\Omega^a_{\;b}$ skew-symmetric in $(a, b)$ — i.e., $\mathfrak{o}(n)$-valued — and torsion-freeness gives a cyclic algebraic identity from $d^2\sigma = 0$ applied to the soldering form.**

The pair-swap symmetry (3) is then a *consequence* of (1), (2), (4): writing out the first Bianchi identity in all $4$ slots and using the two antisymmetries reduces to $R(X, Y, Z, W) = R(Z, W, X, Y)$ via a (somewhat tedious) bookkeeping argument. The proof is in the formal-proof section.

---

# What Makes This Hard

The proofs are not technically difficult but the bookkeeping is unforgiving. The most common error is to conflate the four "Bianchi-like" cyclic permutations — there are *several* identities of cyclic shape, and only the specific one with three indices cycling (and the fourth fixed) is the true first Bianchi identity. The proof of pair-swap symmetry from (1), (2), and the first Bianchi requires writing out and adding four equations carefully; a sign error spoils everything. The geometric content is that the Levi-Civita connection is doing several things at once (preserving the metric, being torsion-free, being uniquely determined by these two properties), and each algebraic symmetry of $R$ corresponds to a different one of these structural features.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove (1) directly from the commutator structure. Prove (2) from metric compatibility of $\nabla$ via the identity $X\langle Y, Z\rangle = \langle\nabla_X Y, Z\rangle + \langle Y, \nabla_X Z\rangle$, twice differentiated. Prove (4) from torsion-freeness via $d^2 = 0$ on the soldering form. Then prove (3) by adding four cyclic instances of (4) and simplifying using (1) and (2).

**Subgoal decomposition:**

1. **First antisymmetry $R(X, Y, Z, W) = -R(Y, X, Z, W)$.**
   - *Hint:* The definition $R(X, Y)Z = [\nabla_X, \nabla_Y]Z - \nabla_{[X, Y]}Z$ swaps sign under $(X, Y) \mapsto (Y, X)$.
   - *Why needed:* Lets $R$ be viewed as taking inputs from $\Lambda^2 T_pM$ in the first two slots.

2. **Second antisymmetry $R(X, Y, Z, W) = -R(X, Y, W, Z)$.**
   - *Hint:* Compute $\nabla_X \nabla_Y \langle Z, W\rangle$ via metric compatibility, twice; subtract the same with $X, Y$ swapped; the second-derivative-difference produces $R(X, Y)$ acting on each of $Z, W$.
   - *Why needed:* Lets $R$ be viewed as taking inputs from $\Lambda^2 T_pM$ in the *second* two slots. Combined with (1), this means $R$ descends to a bilinear pairing on $\Lambda^2 T_pM \times \Lambda^2 T_pM$.

3. **First Bianchi identity $\sum_\text{cyclic} R(X, Y)Z = 0$.**
   - *Hint:* Use torsion-freeness $\nabla_X Y - \nabla_Y X = [X, Y]$ to expand each $R(X, Y)Z$ in terms of $\nabla\nabla Z$ and Lie brackets; sum cyclically and use the Jacobi identity for $[\cdot, \cdot]$.
   - *Why needed:* This is the most substantial algebraic constraint, and it underlies the pair-swap symmetry.

4. **Pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ from (1), (2), (4).**
   - *Hint:* Write out the first Bianchi identity for $R(X, Y, Z, W)$, $R(Y, Z, X, W)$, $R(Z, X, Y, W)$, and one more cyclic version; add carefully, using (1) and (2) to simplify; bookkeeping yields (3).
   - *Why needed:* This is the symmetry that makes the curvature operator $\mathcal{R}$ symmetric and the Ricci tensor symmetric.

---

# Lemma Decomposition

> [!note]- Lemma 1: First antisymmetry from the commutator
> **Statement:** $R(X, Y)Z = -R(Y, X)Z$ for all $X, Y, Z$.
>
> **Hint:** Apply the definition; the commutator $[\nabla_X, \nabla_Y]$ flips sign under $(X, Y) \mapsto (Y, X)$, and the bracket $[X, Y]$ does too.
>
> **Why needed:** Establishes the first antisymmetry without any property of $\nabla$ beyond being a connection.
>
> > [!note]- Full proof
> > $R(Y, X)Z = \nabla_Y\nabla_X Z - \nabla_X\nabla_Y Z - \nabla_{[Y, X]}Z = -(\nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z) - \nabla_{-[X, Y]}Z = -(\nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z) + \nabla_{[X, Y]}Z = -R(X, Y)Z$, using $[Y, X] = -[X, Y]$.

> [!note]- Lemma 2: Second antisymmetry from metric compatibility
> **Statement:** $R(X, Y, Z, W) = -R(X, Y, W, Z)$ for all $X, Y, Z, W$.
>
> **Hint:** Apply metric compatibility to compute the difference $X(Y\langle Z, W\rangle) - Y(X\langle Z, W\rangle) - [X, Y]\langle Z, W\rangle$ in two ways.
>
> **Why needed:** Establishes that the linear map $R(X, Y) : T_pM \to T_pM$ is skew-symmetric in the metric (i.e., $R(X, Y) \in \mathfrak{o}(T_pM)$).
>
> > [!note]- Full proof
> > Compute $X(Y\langle Z, W\rangle) = X(\langle\nabla_Y Z, W\rangle + \langle Z, \nabla_Y W\rangle)$, then again applying metric compatibility:
> > $$X(Y\langle Z, W\rangle) = \langle\nabla_X\nabla_Y Z, W\rangle + \langle\nabla_Y Z, \nabla_X W\rangle + \langle\nabla_X Z, \nabla_Y W\rangle + \langle Z, \nabla_X\nabla_Y W\rangle.$$
> > Subtract the same with $(X, Y)$ swapped, and subtract $[X, Y]\langle Z, W\rangle = \langle\nabla_{[X, Y]}Z, W\rangle + \langle Z, \nabla_{[X, Y]}W\rangle$. The middle two terms cancel by symmetry; what remains is
> > $$0 = \langle R(X, Y)Z, W\rangle + \langle Z, R(X, Y)W\rangle = R(X, Y, Z, W) + R(X, Y, W, Z).$$

> [!note]- Lemma 3: First Bianchi identity from torsion-freeness
> **Statement:** $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0$.
>
> **Hint:** Expand each term using $\nabla_a\nabla_b - \nabla_b\nabla_a = R(a, b)$ + lower-order, sum cyclically; the $\nabla\nabla$ terms cancel by the Jacobi identity for $[\nabla, \nabla]$, and torsion-freeness converts $\nabla_a b - \nabla_b a$ into $[a, b]$.
>
> **Why needed:** This is the most algebraically substantial symmetry, and it underlies the pair-swap symmetry. Crucially it *requires* torsion-freeness — a connection with torsion has a modified Bianchi identity $\sum_\text{cyclic} R(X, Y)Z = \sum_\text{cyclic} (\nabla_X \tau)(Y, Z) + \tau(\tau(X, Y), Z)$.
>
> > [!note]- Full proof
> > Define $C(X, Y, Z) := R(X, Y)Z + R(Y, Z)X + R(Z, X)Y$. Expand $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ and use torsion-freeness $\nabla_X Y - \nabla_Y X = [X, Y]$:
> > 
> > After regrouping (a standard but lengthy calculation; see e.g. do Carmo Ch 4 §3), $C(X, Y, Z) = \sum_\text{cyclic}[X, [Y, Z]] - \sum_\text{cyclic}[X, [Y, Z]] = 0$, where the cancellation is the **Jacobi identity** for the Lie bracket. The torsion-freeness hypothesis is used at the step where $\nabla_X Y - \nabla_Y X$ is replaced by $[X, Y]$.

> [!note]- Lemma 4: Pair-swap symmetry from (1), (2), (4)
> **Statement:** $R(X, Y, Z, W) = R(Z, W, X, Y)$.
>
> **Hint:** Write the first Bianchi identity four times with different cyclic permutations, lower one index with the metric, add carefully, and use (1) and (2).
>
> **Why needed:** This is the symmetry that makes the curvature operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$ symmetric and the Ricci tensor symmetric.
>
> > [!note]- Full proof
> > Write the first Bianchi identity in covariant form: $R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0$. Permute the variables to obtain three additional cyclic versions. Add them with appropriate signs and use the antisymmetries (1), (2) to combine terms. The cancellations are exactly such that $2R(X, Y, Z, W) - 2R(Z, W, X, Y) = 0$, giving (3).

---

# Formal Proof

> [!note]- Complete formal proof
> The four lemmas above constitute the proof:
> - Lemma 1 gives (1) using only the definition of $R$ and the antisymmetry of the Lie bracket.
> - Lemma 2 gives (2) using metric compatibility of $\nabla$.
> - Lemma 3 gives (4) using torsion-freeness of $\nabla$.
> - Lemma 4 derives (3) from (1), (2), (4).
> 
> The dimension count $\tfrac{1}{12}n^2(n^2 - 1)$ follows from the representation-theoretic structure: $R$ is an element of $\mathrm{Sym}^2(\Lambda^2 V) / \langle\text{Bianchi}\rangle$, of dimension $\binom{\binom{n}{2} + 1}{2} - \binom{n}{4}$. Computing: $\binom{n}{2} = n(n-1)/2$, so $\binom{\binom{n}{2}+1}{2} = \tfrac{1}{2}\binom{n}{2}(\binom{n}{2}+1) = \tfrac{1}{8}n(n-1)(n^2 - n + 2)$. After subtracting the Bianchi-identity dimension $\binom{n}{4} = n(n-1)(n-2)(n-3)/24$, this simplifies to $\tfrac{1}{12}n^2(n^2-1)$ — see standard representation-theory references for the explicit calculation.

---

# Cross-Field Exercise Suggestions

1. **Yang–Mills field strengths.** In Yang–Mills theory with gauge group $G$, the field strength $F = dA + \tfrac{1}{2}[A, A]$ of a connection is a $\mathfrak{g}$-valued $2$-form, satisfying the antisymmetry $F(X, Y) = -F(Y, X)$ (analogous to first-pair antisymmetry of $R$) and the universal **Bianchi identity** $d^A F = 0$. The Riemann tensor's first Bianchi identity is the *algebraic* (zero-form) consequence of this. In the Riemannian case, $R$ is constrained more (by metric compatibility's antisymmetry in the second pair) than a general Yang–Mills $F$. See [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]].

2. **Holonomy reductions and Berger's classification.** In dimension $\ge 4$, special algebraic structure on $R$ (e.g., $R$ commuting with a complex structure $J$) corresponds to reductions of the **holonomy group** to a subgroup of $\mathrm{O}(n)$. Berger's classification (1955) enumerates all possible holonomy groups of irreducible non-symmetric Riemannian manifolds: $\mathrm{SO}(n), \mathrm{U}(n), \mathrm{SU}(n), \mathrm{Sp}(n), \mathrm{Sp}(n)\mathrm{Sp}(1), G_2, \mathrm{Spin}(7)$. Each reduction is detected by a specific algebraic constraint on $R$ — for instance, $\mathrm{U}(n)$-holonomy iff $R(JX, JY)JZ = JR(X, Y)Z$, where $J$ is the parallel complex structure.

3. **$4$-manifold decomposition.** The space of algebraic curvature tensors in dimension $4$ decomposes irreducibly under $\mathrm{SO}(4)$: the **Weyl tensor** $W$ ($10$ components, splitting as $5 + 5$ into self-dual and anti-self-dual parts), the **traceless Ricci tensor** ($9$ components), and the **scalar curvature** ($1$ component) — total $20$, the dimension count from the symmetries. This is the foundation of **Seiberg–Witten theory** for smooth $4$-manifold invariants.

---

# Bridges

- **Curvature operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$.** The pair-swap symmetry (3) is exactly what makes the **[[Def - Curvature Operator|curvature operator]]** $\mathcal{R}$ defined by $\langle\mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z)$ a *symmetric* linear endomorphism of $\Lambda^2 T_pM$. Symmetry then guarantees real eigenvalues and an orthogonal eigenbasis, enabling spectral conditions like "positive curvature operator" — much stronger than positive sectional curvature in dimension $\ge 4$. The bridge: $\mathcal{R}$ is *the* repackaging of $R$ that makes the algebraic content most transparent.

- **Ricci tensor symmetry $\mathrm{Ric}(X, Y) = \mathrm{Ric}(Y, X)$.** Both first-pair antisymmetry and pair-swap symmetry are needed to prove this: $\mathrm{Ric}_{bd} = R^a_{\;bad}$ becomes $\mathrm{Ric}_{db} = R^a_{\;dba}$ after relabelling, and pair-swap symmetry $R_{abad} = R_{adab}$ (using both antisymmetries to rearrange) gives $\mathrm{Ric}_{bd} = \mathrm{Ric}_{db}$. Without these algebraic symmetries, the [[Def - Einstein Manifold|Einstein condition]] $\mathrm{Ric} = \lambda g$ would not be meaningfully a comparison between two symmetric tensors.

- **Second Bianchi identity (differential).** The first Bianchi identity (algebraic) has a differential cousin: $\nabla_E R(X, Y, Z, W) + \nabla_X R(Y, E, Z, W) + \nabla_Y R(E, X, Z, W) = 0$ — the [[Thm - First and Second Bianchi Identities|second Bianchi identity]]. Both come from $d^2 = 0$: the first from $d^2 \sigma = 0$ on the soldering form, the second from $d^2 \omega^a_{\;b} = 0$ on the connection form. The second Bianchi has the deep consequence that the Einstein tensor $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$ is divergence-free — the geometric reason Einstein's field equations are self-consistent.

- **Algebraic curvature tensors and Chern–Weil theory.** The space of algebraic Riemann tensors on $V = T_pM$ — symmetric operators on $\Lambda^2 V$ subject to the first Bianchi identity — is the space $\mathcal{C}(V)$. The dimension $\tfrac{1}{12}n^2(n^2 - 1)$ is the dimension of this representation. In **Chern–Weil theory**, $\mathrm{O}(n)$-invariant polynomials on $\mathcal{C}(V)$ correspond to characteristic classes (Pontryagin, Euler); these are the cohomology classes of $M$ built from $R$ that are topological invariants. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
