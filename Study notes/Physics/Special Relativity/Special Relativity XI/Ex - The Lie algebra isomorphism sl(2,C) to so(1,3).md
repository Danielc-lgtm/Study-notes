---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Lie Algebra sl(2,C) and the Exponential Map"
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

The differential of the [[Def - The Spinor Map and SL(2,C)|spinor map]] is $\mathscr{S}' : \mathfrak{sl}(2,\mathbb{C}) \to \mathfrak{so}(1,3)$, $\mathscr{S}'(B) = \mathscr{H}^{-1}\circ\Phi_B'\circ\mathscr{H}$ with $\Phi_B'(\underline X) = B\underline X + \underline X B^\dagger$ (obtained by differentiating $A\underline X A^\dagger$ along $A = \exp(\varepsilon B)$).

1. Compute $\mathscr{S}'(\sigma_1)$ by acting with $\Phi_{\sigma_1}'$ on the basis Hermitian matrices and reading off the resulting Lorentz generator; show $\mathscr{S}'(\sigma_1) = 2K_1$ (a boost generator). State the analogous results $\mathscr{S}'(\sigma_i) = 2K_i$ and $\mathscr{S}'(i\sigma_i) = -2J_i$.
2. Verify that $\mathscr{S}'$ preserves the Lie bracket on one nontrivial example: check that $\mathscr{S}'([\sigma_1, \sigma_2]) = [\mathscr{S}'(\sigma_1), \mathscr{S}'(\sigma_2)]$, recovering the Lorentz commutator $[K_1, K_2] = -J_3$.
3. Conclude that $\mathscr{S}'$ is a Lie-algebra isomorphism $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$, and relate this to the complexified splitting $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ and the two Weyl-spinor representations.

**Recall:**

![[Def - Lie Algebra sl(2,C) and the Exponential Map#The Definition]]

The [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]] $\mathfrak{so}(1,3)$ has rotation generators $J_i$ and boost generators $K_i$ with $[J_i, J_j] = \varepsilon_{ijk}J_k$, $[J_i, K_j] = \varepsilon_{ijk}K_k$, $[K_i, K_j] = -\varepsilon_{ijk}J_k$. The boost generator $K_1$ acts on a four-vector by mixing $x^0$ and $x^1$: $K_1$ has matrix entries $(K_1)^0{}_1 = (K_1)^1{}_0 = 1$, all others zero, so $\exp(\psi K_1)$ is the $x$-boost.

---

# Convergent Strategy

**Problem class.** A *Lie-algebra isomorphism by generator-matching* — the infinitesimal version of the double cover, establishing $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$ explicitly. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Sources and Targets|topic target list]] names "verify an algebra isomorphism by matching generators" as a recurring goal; this is the case that proves $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$.

**Assumption pattern.** The input is the differential formula $\Phi_B'(\underline X) = B\underline X + \underline X B^\dagger$ (a *sum* of two terms, the Leibniz derivative of the product $A\underline X A^\dagger$). The signpost is that, unlike the finite congruence, the infinitesimal action is additive — and the two terms are what produce the factor of two in $\mathscr{S}'(\sigma_i) = 2K_i$.

**Theorem routing.** This proves the generator identities asserted on [[Def - Lie Algebra sl(2,C) and the Exponential Map|the exponential-map page]] and uses the Lorentz commutators from [[Def - Lie Algebra of the Lorentz Group|the Lorentz Lie algebra]]. Establishing that $\mathscr{S}'$ sends a basis to a basis and preserves one bracket suffices (with linearity) for the isomorphism.

**Key decision point.** The crux is computing $\Phi_{\sigma_1}'(\underline X) = \sigma_1\underline X + \underline X\sigma_1^\dagger = \sigma_1\underline X + \underline X\sigma_1$ (since $\sigma_1^\dagger = \sigma_1$) and reading the result as a Lorentz generator. The decisive simplification is to act on the basis matrices $\sigma_0, \sigma_3$ (which mix into the $x^0, x^1$ directions) and use the anticommutator $\{\sigma_1, \sigma_\mu\}$: $\{\sigma_1, \sigma_0\} = 2\sigma_1$ and $\{\sigma_1, \sigma_1\} = 2I = 2\sigma_0$, so $\Phi_{\sigma_1}'$ swaps the $\sigma_0$ and $\sigma_1$ directions with a factor $2$ — exactly $2K_1$. Recognising that the *anticommutator* (Hermitian $B = \sigma_1$) gives a boost while the *commutator* (anti-Hermitian $B = i\sigma_1$) gives a rotation is the structural insight.

---

# Legal Operations Used

1. **Match generators to prove an algebra isomorphism** (operation 8 from the topic page): the entire exercise computes $\mathscr{S}'$ on basis elements and checks it sends a basis to a basis and preserves brackets.

2. **Use the Pauli multiplication law to collapse a product** (operation 3 from the topic page): the computations of $\Phi_B'(\sigma_\nu) = B\sigma_\nu + \sigma_\nu B^\dagger$ reduce to anticommutators and commutators of Pauli matrices.

3. **Recast a four-vector as a Hermitian matrix** (operation 1 from the topic page): the result $\Phi_B'(\sigma_\nu)$, expanded in the Pauli basis, is read as a column of the Lorentz generator matrix.

---

# Hints

> [!note]- Hint 1
> $\sigma_1^\dagger = \sigma_1$, so $\Phi_{\sigma_1}'(\underline X) = \sigma_1\underline X + \underline X\sigma_1 = \{\sigma_1, \underline X\}$, the anticommutator. Act on $\underline X = \sigma_0 = I$: $\{\sigma_1, I\} = 2\sigma_1$, so the $\sigma_0$-direction maps to $2\sigma_1$ (i.e. $e_0 \mapsto 2e_1$). Act on $\sigma_1$: $\{\sigma_1, \sigma_1\} = 2I = 2\sigma_0$ (i.e. $e_1 \mapsto 2e_0$).

> [!note]- Hint 2
> The map sending $e_0 \mapsto 2e_1$, $e_1 \mapsto 2e_0$, $e_2 \mapsto 0$, $e_3 \mapsto 0$ is $2K_1$, the boost generator (which mixes time and $x$ with coefficient $1$, doubled here). For $i\sigma_1$: $(i\sigma_1)^\dagger = -i\sigma_1$, so $\Phi_{i\sigma_1}'(\underline X) = i\sigma_1\underline X - \underline X i\sigma_1 = i[\sigma_1, \underline X]$, the commutator — which gives a rotation generator.

> [!note]- Hint 3
> For part 2: $[\sigma_1, \sigma_2] = 2i\sigma_3$, so $\mathscr{S}'([\sigma_1,\sigma_2]) = \mathscr{S}'(2i\sigma_3) = 2\mathscr{S}'(i\sigma_3) = 2(-2J_3) = -4J_3$. Separately $[\mathscr{S}'(\sigma_1), \mathscr{S}'(\sigma_2)] = [2K_1, 2K_2] = 4[K_1, K_2]$, and the Lorentz relation $[K_1, K_2] = -J_3$ gives $-4J_3$. They agree.

> [!note]- Hint 4
> The complexified splitting: $N_i^{\pm} = \tfrac12(J_i \pm iK_i)$ satisfy $[N_i^+, N_j^+] = \varepsilon_{ijk}N_k^+$, $[N_i^-, N_j^-] = \varepsilon_{ijk}N_k^-$, $[N_i^+, N_j^-] = 0$ — two commuting copies of $\mathfrak{su}(2)$. The Weyl spinors are the representations on which one copy acts trivially.

---

# Solution

The exercise computes the differential of the spinor map on the Pauli basis, finds it sends boosts-from-Hermitian and rotations-from-anti-Hermitian generators, checks one bracket, and concludes the isomorphism. The plan: act with $\Phi_B'(\underline X) = B\underline X + \underline X B^\dagger$ on the basis, identifying the result with $\pm 2$ times a Lorentz generator; verify the bracket; assemble the isomorphism and connect to the Weyl-spinor splitting.

**Step 1: $\mathscr{S}'(\sigma_i) = 2K_i$ and $\mathscr{S}'(i\sigma_i) = -2J_i$.**

> [!note]- Derivation
> Since $\sigma_1^\dagger = \sigma_1$, the differential action is the anticommutator:
> $$\Phi_{\sigma_1}'(\underline X) = \sigma_1\underline X + \underline X\sigma_1^\dagger = \sigma_1\underline X + \underline X\sigma_1 = \{\sigma_1, \underline X\}.$$
> Act on the basis Hermitian matrices using $\{\sigma_1, \sigma_\nu\}$:
> - $\{\sigma_1, \sigma_0\} = \{\sigma_1, I\} = 2\sigma_1$, so $e_0 \mapsto 2e_1$.
> - $\{\sigma_1, \sigma_1\} = 2\sigma_1^2 = 2I = 2\sigma_0$, so $e_1 \mapsto 2e_0$.
> - $\{\sigma_1, \sigma_2\} = \sigma_1\sigma_2 + \sigma_2\sigma_1 = i\sigma_3 - i\sigma_3 = 0$, so $e_2 \mapsto 0$.
> - $\{\sigma_1, \sigma_3\} = \sigma_1\sigma_3 + \sigma_3\sigma_1 = -i\sigma_2 + i\sigma_2 = 0$, so $e_3 \mapsto 0$.
>
> The linear map $e_0 \mapsto 2e_1$, $e_1 \mapsto 2e_0$, $e_2, e_3 \mapsto 0$ is $2K_1$: the boost generator $K_1$ has $K_1(e_0) = e_1$, $K_1(e_1) = e_0$ (mixing time and $x$), and the rest zero, so doubling gives exactly $\Phi_{\sigma_1}'$. Hence $\mathscr{S}'(\sigma_1) = 2K_1$. By the same computation with $\sigma_2, \sigma_3$, $\mathscr{S}'(\sigma_i) = 2K_i$.
>
> For the anti-Hermitian generators, $(i\sigma_1)^\dagger = -i\sigma_1^\dagger = -i\sigma_1$, so
> $$\Phi_{i\sigma_1}'(\underline X) = i\sigma_1\underline X - \underline X i\sigma_1 = i[\sigma_1, \underline X],$$
> the commutator. Act on the basis using $[\sigma_1, \sigma_\nu]$:
> - $[\sigma_1, \sigma_0] = 0$, so $e_0 \mapsto 0$.
> - $[\sigma_1, \sigma_2] = 2i\sigma_3$, so $\Phi_{i\sigma_1}'(\sigma_2) = i(2i\sigma_3) = -2\sigma_3$, i.e. $e_2 \mapsto -2e_3$.
> - $[\sigma_1, \sigma_3] = -2i\sigma_2$, so $\Phi_{i\sigma_1}'(\sigma_3) = i(-2i\sigma_2) = 2\sigma_2$, i.e. $e_3 \mapsto 2e_2$.
> - $e_1 \mapsto 0$.
>
> The map $e_2 \mapsto -2e_3$, $e_3 \mapsto 2e_2$, fixing $e_0, e_1$, is $-2J_1$: the rotation generator $J_1$ rotates the $(y,z)$-plane, $J_1(e_2) = e_3$, $J_1(e_3) = -e_2$, so $-2J_1$ matches. Hence $\mathscr{S}'(i\sigma_1) = -2J_1$, and generally $\mathscr{S}'(i\sigma_i) = -2J_i$.

**Step 2: $\mathscr{S}'$ preserves the bracket $[\sigma_1,\sigma_2] \mapsto [K_1,K_2] = -J_3$.**

> [!note]- Derivation
> Compute both sides of $\mathscr{S}'([\sigma_1,\sigma_2]) = [\mathscr{S}'(\sigma_1), \mathscr{S}'(\sigma_2)]$.
>
> *Left side.* $[\sigma_1, \sigma_2] = 2i\sigma_3$ (Pauli commutator), so
> $$\mathscr{S}'([\sigma_1,\sigma_2]) = \mathscr{S}'(2i\sigma_3) = 2\,\mathscr{S}'(i\sigma_3) = 2(-2J_3) = -4J_3,$$
> using linearity of $\mathscr{S}'$ and $\mathscr{S}'(i\sigma_3) = -2J_3$.
>
> *Right side.* $[\mathscr{S}'(\sigma_1), \mathscr{S}'(\sigma_2)] = [2K_1, 2K_2] = 4[K_1, K_2]$, and the [[Def - Lie Algebra of the Lorentz Group|Lorentz commutator]] $[K_1, K_2] = -J_3$ (two boosts commute to a rotation — the algebraic root of the Thomas precession) gives
> $$[2K_1, 2K_2] = 4(-J_3) = -4J_3.$$
> The two sides agree: $\mathscr{S}'([\sigma_1, \sigma_2]) = [\mathscr{S}'(\sigma_1), \mathscr{S}'(\sigma_2)] = -4J_3$. So $\mathscr{S}'$ preserves this bracket, and (by linearity and the same computation on all basis pairs) it is a Lie-algebra homomorphism.

**Step 3: Isomorphism and the Weyl-spinor splitting.**

> [!note]- Derivation
> The image of the basis $\{\sigma_1, \sigma_2, \sigma_3, i\sigma_1, i\sigma_2, i\sigma_3\}$ of $\mathfrak{sl}(2,\mathbb{C})$ under $\mathscr{S}'$ is $\{2K_1, 2K_2, 2K_3, -2J_1, -2J_2, -2J_3\}$, which (rescaled) is the basis $\{K_i, J_i\}$ of $\mathfrak{so}(1,3)$. A linear map sending a basis to a basis is a vector-space isomorphism, and Step 2 shows it preserves brackets, so $\mathscr{S}'$ is a **Lie-algebra isomorphism**:
> $$\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3).$$
> *Connection to the Weyl spinors.* Form the complex combinations $N_i^{\pm} = \tfrac12(J_i \pm iK_i)$ in the complexified algebra $\mathfrak{so}(1,3)_{\mathbb C}$. Using the Lorentz commutators, $[N_i^+, N_j^+] = \varepsilon_{ijk}N_k^+$, $[N_i^-, N_j^-] = \varepsilon_{ijk}N_k^-$, and $[N_i^+, N_j^-] = 0$ — two *commuting* copies of $\mathfrak{su}(2)_{\mathbb C}$:
> $$\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{su}(2) \oplus \mathfrak{su}(2).$$
> Under $\mathscr{S}'$ these correspond to combinations of $\sigma_i$ and $i\sigma_i$, and the two factors act on the two [[Def - Weyl Spinors (Left and Right Handed)|Weyl spinors]]: the **left** spinor $(\tfrac12, 0)$ is the representation on which $N^+$ acts as spin-½ and $N^-$ trivially, the **right** spinor $(0, \tfrac12)$ the reverse. This is the representation-theoretic meaning of the isomorphism: $\mathfrak{sl}(2,\mathbb{C})$, whose defining representation is the left Weyl spinor, *is* the Lorentz algebra, with the two $\mathfrak{su}(2)$'s built from $J_i \pm iK_i$.

> [!note]- Complete formal solution
> Since $\sigma_i^\dagger = \sigma_i$, $\Phi_{\sigma_1}'(\underline X) = \{\sigma_1, \underline X\}$; acting on the basis gives $e_0 \mapsto 2e_1$, $e_1 \mapsto 2e_0$, $e_2, e_3 \mapsto 0$, which is $2K_1$, so $\mathscr{S}'(\sigma_i) = 2K_i$. Since $(i\sigma_i)^\dagger = -i\sigma_i$, $\Phi_{i\sigma_1}'(\underline X) = i[\sigma_1, \underline X]$; acting on the basis gives $e_2 \mapsto -2e_3$, $e_3 \mapsto 2e_2$, $e_0, e_1 \mapsto 0$, which is $-2J_1$, so $\mathscr{S}'(i\sigma_i) = -2J_i$. The bracket is preserved: $\mathscr{S}'([\sigma_1,\sigma_2]) = \mathscr{S}'(2i\sigma_3) = -4J_3 = 4[K_1,K_2] = [2K_1, 2K_2] = [\mathscr{S}'(\sigma_1),\mathscr{S}'(\sigma_2)]$. As $\mathscr{S}'$ sends a basis to a basis and preserves brackets, it is a Lie-algebra isomorphism $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$. The combinations $N_i^\pm = \tfrac12(J_i \pm iK_i)$ give $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$, the two factors acting on the left and right Weyl spinors. $\blacksquare$

---

# Key Takeaways

**The infinitesimal spinor map is a sum (Leibniz), and its two terms produce the factor of two.** The finite congruence $A\underline X A^\dagger$ is a *product* of three factors; differentiating it along $A = \exp(\varepsilon B)$ gives, by the Leibniz rule, the *sum* $B\underline X + \underline X B^\dagger$ — one term from differentiating the left factor, one from the right. This is why $\mathscr{S}'(\sigma_i) = 2K_i$ carries a factor of two: the generator $\sigma_i$ acts "twice," once on each side, exactly as the half-angle in the finite group reflected two factors of $A$. The lesson is that the half-angle (group level) and the factor of two (algebra level) are the same phenomenon — the two factors of $A$ in the congruence — seen at two scales, and tracking which side a generator acts on is the bookkeeping that produces it. When you differentiate any conjugation or congruence action, expect a sum of left and right contributions, and expect the resulting algebra map to carry a factor that the finite map hides as a half-parameter.

**Hermitian generator → boost (anticommutator), anti-Hermitian generator → rotation (commutator).** The single most useful structural observation here is that the *type* of the $\mathfrak{sl}(2,\mathbb{C})$ generator dictates the *type* of the Lorentz generator, through the form $B\underline X + \underline X B^\dagger$. When $B$ is Hermitian ($B^\dagger = B$, the $\sigma_i$), the action is the anticommutator $\{B, \underline X\}$, which mixes the time direction with a spatial one — a boost. When $B$ is anti-Hermitian ($B^\dagger = -B$, the $i\sigma_i$), the action is $i[\,\cdot\,]$ the commutator, which rotates two spatial directions into each other — a rotation. So the split of $\mathfrak{sl}(2,\mathbb{C})$ into Hermitian and anti-Hermitian traceless matrices is exactly the split of $\mathfrak{so}(1,3)$ into boosts and rotations, and the anticommutator-versus-commutator distinction is the mechanism. This is the algebra-level version of "Hermitian matrix = boost, unitary matrix = rotation," and it explains *why* that finite-group fact holds: the generators of the unitary subgroup $SU(2)$ are precisely the anti-Hermitian $i\sigma_i$, which give rotations.

**Two commuting $\mathfrak{su}(2)$'s from $J \pm iK$ is the source of the two Weyl spinors, and hence of all spin labels.** The complex combinations $N_i^\pm = \tfrac12(J_i \pm iK_i)$ decouple the Lorentz algebra into two independent angular momenta, $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$, and this is the deep reason every Lorentz representation is labelled by a *pair* of spins $(A, B)$. The two Weyl spinors are the two simplest nontrivial cases — $(\tfrac12, 0)$ where the first $\mathfrak{su}(2)$ acts and the second is trivial, and $(0, \tfrac12)$ the reverse — and the isomorphism $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(1,3)$ of this exercise is what makes the defining representation of $\mathfrak{sl}(2,\mathbb{C})$ (a left Weyl spinor) into a Lorentz representation. The transferable structural insight is that decomposing a Lie algebra into commuting subalgebras decomposes its representation theory into a product, and finding such a decomposition (here via the clever complex combination $J \pm iK$) is the master technique for classifying representations of a group — the same move that organises the representation theory of every semisimple Lie algebra, and the foundation on which Wigner's classification of particles in [[Special Relativity XII — Inertial Observers and the Poincaré Group|the next chapter]] is built.
