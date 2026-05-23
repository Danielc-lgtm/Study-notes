---
type: exercise
subject: geometric-mechanics
difficulty: "⭐⭐"
prereqs:
  - "Def - Poisson Bracket"
  - "Def - Hamiltonian Vector Field"
tags: [physics, geometric-mechanics, symplectic-geometry, lie-algebra]
---

# Problem Statement

On $T^*\mathbb{R}^3$ with canonical coordinates $(q^1, q^2, q^3, p_1, p_2, p_3)$ and canonical symplectic form $\omega = \sum_i dp_i \wedge dq^i$, define the **angular momentum** components

$$L^i := \epsilon^{ijk} q^j p_k = \sum_{j, k} \epsilon^{ijk} q^j p_k, \quad i = 1, 2, 3,$$

where $\epsilon^{ijk}$ is the totally antisymmetric Levi-Civita symbol ($\epsilon^{123} = +1$).

(a) Compute the Poisson brackets $\{L^i, L^j\}$ from the canonical brackets $\{q^i, p_j\} = \delta^i_j$ and verify $\{L^i, L^j\} = \epsilon^{ijk} L^k$ (Lie algebra $\mathfrak{so}(3)$).

(b) Define the **squared angular momentum** $L^2 := \sum_i (L^i)^2$. Compute $\{L^2, L^i\}$ for $i = 1, 2, 3$ and verify $L^2$ is a **Casimir** of the angular-momentum subalgebra (Poisson-commutes with each $L^i$).

(c) Show that for any rotationally invariant Hamiltonian $H$ on $T^*\mathbb{R}^3$ (one with $\{L^i, H\} = 0$ for each $i$), the angular momentum vector $\vec L = (L^1, L^2, L^3)$ is conserved, and $L^2$ is also conserved.

**Recall:**

![[Def - Poisson Bracket#The Definition]]

The fundamental Poisson brackets on $T^*\mathbb{R}^n$ are $\{q^i, q^j\} = 0$, $\{p_i, p_j\} = 0$, $\{q^i, p_j\} = \delta^i_j$. The Poisson bracket is bilinear, antisymmetric, satisfies Leibniz ($\{f, gh\} = \{f, g\}h + g\{f, h\}$), and satisfies Jacobi.

The Levi-Civita symbol satisfies $\epsilon^{ijk}\epsilon^{ilm} = \delta^j_l\delta^k_m - \delta^j_m\delta^k_l$ (sum over $i$).

---

# Convergent Strategy

**Problem class:** This is a **direct Poisson-bracket computation** for a system of three functions ($L^1, L^2, L^3$), with the result being a Lie-algebraic identity ($\mathfrak{so}(3)$ closure). The technique applies to any system of functions whose Poisson brackets you want to compute: expand in coordinates and use the fundamental brackets plus bilinearity and Leibniz.

**Assumption pattern:** We're given the angular momentum components as polynomial functions on $T^*\mathbb{R}^3$. The Poisson algebra of polynomial functions is completely determined by the fundamental brackets $\{q^i, p_j\} = \delta^i_j$ via bilinearity and Leibniz — no further input needed. The Jacobi identity for the Poisson bracket is in the background (it ensures the $\mathfrak{so}(3)$ closure is self-consistent).

**Theorem routing:** Apply the [[Def - Poisson Bracket|Poisson bracket formula]] (canonical coordinate version: $\{f, g\} = \sum_i (\partial_{q^i}f \partial_{p_i}g - \partial_{p_i}f \partial_{q^i}g)$) directly to $L^i, L^j$. The result is a polynomial in $q, p$, which simplifies via Levi-Civita identities to $\epsilon^{ijk}L^k$. For $\{L^2, L^i\}$, use Leibniz: $\{L^2, L^i\} = \{L^j L^j, L^i\} = 2L^j\{L^j, L^i\}$, then substitute the $\mathfrak{so}(3)$ relation and use antisymmetry of $\epsilon$.

**Key decision point:** The non-obvious step is the **simplification** of $\{L^i, L^j\}$ to $\epsilon^{ijk}L^k$. The brute-force computation gives a sum of terms like $\epsilon^{ija}\epsilon^{jlk}q^l p_k$ — a mess of Levi-Civita symbols. The slick approach uses the identity $\epsilon^{ijk}\epsilon^{ilm} = \delta^j_l\delta^k_m - \delta^j_m\delta^k_l$ to collapse the indices. The other key step is recognizing that $\{L^2, L^i\} = 0$ comes from the **antisymmetry of $\epsilon$ in two indices** combined with the **symmetry of $L^jL^j$** — these are dual to each other, and their pairing vanishes.

---

# Legal Operations Used

1. **Operation 3 from the topic page (check $\{f, H\} = 0$).** The end-goal is to identify conserved quantities: the angular momentum vector $\vec L$ is conserved iff $\{L^i, H\} = 0$ for each $i$, and $L^2$ is conserved as a Casimir of the angular-momentum subalgebra.

2. **Operation 10 from the topic page (Jacobi for conservation laws).** Implicit in the structure: the Poisson algebra closure $\{L^i, L^j\} = \epsilon^{ijk}L^k$ is consistent with Jacobi for $\{\cdot, \cdot\}$, and the conservation of $L^i$'s individually combined with closure implies conservation of any function of them (including $L^2$).

3. **Bilinearity and Leibniz of the Poisson bracket.** Used throughout to expand $\{L^i, L^j\} = \{\epsilon^{iab}q^a p_b, \epsilon^{jcd}q^c p_d\}$ and reduce to the fundamental brackets.

---

# Hints

> [!note]- Hint 1
> Expand $L^i = \epsilon^{iab}q^a p_b$ and $L^j = \epsilon^{jcd}q^c p_d$. Compute $\{L^i, L^j\}$ by bilinearity: $\{q^ap_b, q^cp_d\}$. Use Leibniz: $\{q^ap_b, q^cp_d\} = q^a\{p_b, q^cp_d\} + \{q^a, q^cp_d\}p_b$.

> [!note]- Hint 2
> Use the fundamental brackets: $\{q^a, p_d\} = \delta^a_d$ and $\{p_b, q^c\} = -\delta^c_b$. The result $\{q^ap_b, q^cp_d\} = q^a\delta^c_b p_d - p_b\delta^a_d q^c$ — but be careful with index placement.

> [!note]- Hint 3
> Sum over $a, b, c, d$ with $\epsilon^{iab}\epsilon^{jcd}$ in front. The Levi-Civita contraction identity $\epsilon^{iab}\epsilon^{jcd}\delta^c_b = \epsilon^{iab}\epsilon^{jbd} = \delta^{ij}\delta^{ad} - \delta^{id}\delta^{aj}$ (after summing $b$ over the second index of each $\epsilon$). Use this to reduce.

> [!note]- Hint 4
> For $\{L^2, L^i\}$: use Leibniz on $L^2 = \sum_j L^jL^j$, getting $\{L^2, L^i\} = 2L^j\{L^j, L^i\}$. Substitute $\{L^j, L^i\} = \epsilon^{jik}L^k$. Then $2L^j\epsilon^{jik}L^k = 2\epsilon^{jik}L^jL^k$. The expression $\epsilon^{jik}L^jL^k$ is antisymmetric in $(j, k)$ but $L^jL^k$ is symmetric in $(j, k)$, so the contraction vanishes.

---

# Solution

The proof breaks into three steps. Step 1 derives the $\mathfrak{so}(3)$ Poisson brackets. Step 2 verifies $L^2$ is a Casimir. Step 3 deduces conservation for rotational-invariant Hamiltonians.

**Step 1: $\{L^i, L^j\} = \epsilon^{ijk}L^k$.**

Direct computation from canonical brackets gives $\{L^i, L^j\} = \epsilon^{ijk}L^k$ — the $\mathfrak{so}(3)$ Lie algebra structure.

> [!note]- Derivation
> Write $L^i = \epsilon^{iab}q^a p_b$ (with summation implied). Then
> $$\{L^i, L^j\} = \{\epsilon^{iab}q^a p_b, \epsilon^{jcd}q^c p_d\} = \epsilon^{iab}\epsilon^{jcd}\{q^a p_b, q^c p_d\}.$$
>
> By bilinearity and Leibniz, expand $\{q^a p_b, q^c p_d\}$:
> $$\{q^a p_b, q^c p_d\} = q^a\{p_b, q^c p_d\} + \{q^a, q^c p_d\}p_b.$$
> Continue Leibniz:
> $$\{p_b, q^c p_d\} = q^c\{p_b, p_d\} + \{p_b, q^c\}p_d = 0 + (-\delta^c_b)p_d = -\delta^c_b p_d.$$
> $$\{q^a, q^c p_d\} = q^c\{q^a, p_d\} + \{q^a, q^c\}p_d = q^c\delta^a_d + 0 = q^c\delta^a_d.$$
>
> So:
> $$\{q^a p_b, q^c p_d\} = -q^a \delta^c_b p_d + q^c \delta^a_d p_b.$$
>
> Now compute:
> $$\{L^i, L^j\} = \epsilon^{iab}\epsilon^{jcd}(-q^a \delta^c_b p_d + q^c \delta^a_d p_b).$$
>
> First term: $-\epsilon^{iab}\epsilon^{jcd}q^a \delta^c_b p_d = -\epsilon^{iab}\epsilon^{jbd}q^a p_d$ (sum $c = b$).
>
> Apply the Levi-Civita identity: $\epsilon^{iab}\epsilon^{jbd} = \epsilon^{ab i}\epsilon^{b d j} = \delta^{a}_d \delta^i_j - \delta^a_j\delta^i_d$ (after cyclic permutations and the standard identity $\epsilon^{abc}\epsilon^{abd} = 2\delta^c_d$ — let me be careful). Actually, the right identity is: for sums over one index, $\sum_b \epsilon^{iab}\epsilon^{jcb} = \delta^{ij}\delta^{ac} - \delta^{ic}\delta^{aj}$. So $\sum_b \epsilon^{iab}\epsilon^{jbd}$. Note $\epsilon^{jbd} = -\epsilon^{bjd}$, so $\sum_b \epsilon^{iab}(-\epsilon^{bjd}) = -\sum_b \epsilon^{iab}\epsilon^{bjd}$. Using $\sum_b \epsilon^{iab}\epsilon^{bjd} = \delta^{ij}\delta^{ad} - \delta^{id}\delta^{aj}$ (a standard identity in the literature), we get $\sum_b \epsilon^{iab}\epsilon^{jbd} = -(\delta^{ij}\delta^{ad} - \delta^{id}\delta^{aj}) = -\delta^{ij}\delta^{ad} + \delta^{id}\delta^{aj}$.
>
> Hmm, the sign conventions are getting tangled. Let me just compute symbolically and check at the end. The first term becomes (after applying the Levi-Civita identity):
> $$-(-\delta^{ij}\delta^{ad} + \delta^{id}\delta^{aj})q^a p_d = (\delta^{ij}\delta^{ad} - \delta^{id}\delta^{aj})q^a p_d = \delta^{ij}q^a p_a - q^j p_i.$$
>
> Second term: $\epsilon^{iab}\epsilon^{jcd}q^c \delta^a_d p_b = \epsilon^{iab}\epsilon^{jcb}q^c p_b$ wait this isn't right either. Let me redo using $\delta^a_d$: this sets $a = d$, giving $\epsilon^{idb}\epsilon^{jcd}q^c p_b$. Hmm, I'm making bookkeeping errors. Let me restart this calculation more carefully.
>
> **Cleaner approach: use cross-product identity.** Recognize $L^i = (\vec q \times \vec p)^i$ as the $i$-th component of the cross product. The angular-momentum Poisson algebra is a standard result; the cleanest derivation is:
> $$\{L_x, L_y\} = \{yp_z - zp_y, zp_x - xp_z\}.$$
> Expand: $\{yp_z, zp_x\} = y\{p_z, z\}p_x + \{y, p_x\}p_z z = y(-1)p_x + 0 \cdot z = -yp_x$. Wait, $\{p_z, z\} = -\delta^z_z = -1$, so $\{yp_z, zp_x\} = y(-1)p_x + 0 = -yp_x$. Hmm, but Leibniz: $\{yp_z, zp_x\} = y\{p_z, zp_x\} + \{y, zp_x\}p_z = y(z\{p_z, p_x\} + \{p_z, z\}p_x) + (z\{y, p_x\} + \{y, z\}p_x)p_z = y(0 + (-1)p_x) + (0 + 0)p_z = -yp_x$. ✓
>
> Continue: $\{yp_z, -xp_z\} = -y\{p_z, xp_z\} - \{y, xp_z\}p_z = -y(x\{p_z, p_z\} + \{p_z, x\}p_z) - (x\{y, p_z\} + \{y, x\}p_z)p_z = 0$.
> $\{-zp_y, zp_x\} = -\{zp_y, zp_x\} = -[z\{p_y, zp_x\} + \{z, zp_x\}p_y] = -[z(z\{p_y, p_x\} + \{p_y, z\}p_x) + (z\{z, p_x\} + \{z, z\}p_x)p_y] = -[z(0 + 0) + 0] = 0$.
> $\{-zp_y, -xp_z\} = \{zp_y, xp_z\} = z\{p_y, xp_z\} + \{z, xp_z\}p_y = z(x\{p_y, p_z\} + \{p_y, x\}p_z) + (x\{z, p_z\} + \{z, x\}p_z)p_y = z(0 + 0) + (x \cdot 1 + 0)p_y = xp_y$.
>
> So $\{L_x, L_y\} = -yp_x + 0 + 0 + xp_y = xp_y - yp_x = L_z$. ✓
>
> By cyclic permutation: $\{L_y, L_z\} = L_x$ and $\{L_z, L_x\} = L_y$. These are summarized as $\{L^i, L^j\} = \epsilon^{ijk}L^k$ — the **angular-momentum Lie algebra $\mathfrak{so}(3)$**.

**Step 2: $\{L^2, L^i\} = 0$ ($L^2$ is a Casimir).**

$\{L^2, L^i\} = 2L^j\{L^j, L^i\} = 2\epsilon^{jik}L^jL^k = 0$ by symmetry-antisymmetry.

> [!note]- Derivation
> Use Leibniz: $L^2 = \sum_j (L^j)^2 = L^j L^j$, so
> $$\{L^2, L^i\} = \{L^j L^j, L^i\} = L^j\{L^j, L^i\} + \{L^j, L^i\}L^j = 2L^j\{L^j, L^i\}$$
> (since $L^j$ and $\{L^j, L^i\}$ commute as functions on phase space).
>
> Substitute $\{L^j, L^i\} = \epsilon^{jik}L^k$:
> $$\{L^2, L^i\} = 2L^j\epsilon^{jik}L^k = 2\epsilon^{jik}L^jL^k.$$
>
> Now: $L^jL^k$ is **symmetric** in $(j, k)$ (multiplication of functions commutes), while $\epsilon^{jik}$ is **antisymmetric** in $(j, k)$ (since swapping the first and third indices of $\epsilon$ gives a sign, and the middle index $i$ is fixed). The contraction of a symmetric and an antisymmetric tensor in the same pair of indices vanishes:
> $$\epsilon^{jik}L^jL^k = -\epsilon^{kij}L^jL^k = -\epsilon^{kij}L^kL^j = -\epsilon^{jik}L^jL^k,$$
> where the first step is antisymmetry of $\epsilon$, the second is commutativity of multiplication, and the third is relabeling. So $\epsilon^{jik}L^jL^k = -\epsilon^{jik}L^jL^k$, hence $\epsilon^{jik}L^jL^k = 0$.
>
> Therefore $\{L^2, L^i\} = 0$ for $i = 1, 2, 3$. **$L^2$ is a Casimir of the angular-momentum subalgebra** — it Poisson-commutes with each $L^i$.

**Step 3: Conservation under rotational-invariant Hamiltonians.**

For $H$ with $\{L^i, H\} = 0$, both $\vec L$ (vector of components) and $L^2$ are conserved.

> [!note]- Derivation
> If $H$ is rotationally invariant — meaning invariant under the $SO(3)$ action on $T^*\mathbb{R}^3$ generated by $\vec L$ — then by Noether's theorem (symplectic form), $\{L^i, H\} = 0$ for each $i$. This means $L^i$ is conserved along the flow of $H$:
> $$\frac{dL^i}{dt} = X_H(L^i) = -X_{L^i}(H) = -\{H, L^i\} \cdot \text{(sign)} = -\{L^i, H\} = 0.$$
> Wait, more carefully: along the flow of $H$, $df/dt = X_H(f) = \{f, H\}$. So $dL^i/dt = \{L^i, H\} = 0$. ✓
>
> For $L^2$: $dL^2/dt = \{L^2, H\}$. By Leibniz, $\{L^2, H\} = 2L^j\{L^j, H\}$. If $\{L^j, H\} = 0$ for each $j$, then $\{L^2, H\} = 0$ too. So $L^2$ is also conserved.
>
> Alternatively: $L^2$ commutes with each $L^i$ (Casimir property), and by Jacobi $\{f, \{g, h\}\} = -\{g, \{h, f\}\} - \{h, \{f, g\}\}$. Specifically, $L^2$ is conserved because it's a polynomial in the conserved $L^i$'s.
>
> **Physical interpretation:** for a particle in a **central potential** $V = V(|q|)$, the Hamiltonian $H = |p|^2/(2m) + V(|q|)$ is invariant under rotations of $q$ (and consequently of $p$, since $L^i$ generates the rotation). So $\vec L$ and $L^2$ are conserved. **The conservation of angular momentum in central-force problems (Kepler, harmonic oscillator in 3D, hydrogen atom) is a special case of this general fact**.

> [!note]- Complete formal solution
> **Setup:** $L^i = \epsilon^{ijk}q^j p_k$ on $T^*\mathbb{R}^3$ with canonical $\omega = \sum dp_i \wedge dq^i$, hence fundamental Poisson brackets $\{q^i, p_j\} = \delta^i_j$.
>
> **Step 1: Lie algebra closure.** Direct computation:
> $$\{L^x, L^y\} = \{yp_z - zp_y, zp_x - xp_z\} = xp_y - yp_x = L^z,$$
> and cyclic. In tensor notation: $\{L^i, L^j\} = \epsilon^{ijk}L^k$. **This is the Poisson-algebraic realization of $\mathfrak{so}(3)$.**
>
> **Step 2: $L^2$ is a Casimir.** $\{L^2, L^i\} = 2L^j\{L^j, L^i\} = 2\epsilon^{jik}L^jL^k$. Since $L^jL^k$ is symmetric in $(j, k)$ and $\epsilon^{jik}$ is antisymmetric in $(j, k)$, the contraction vanishes. So $\{L^2, L^i\} = 0$ for $i = 1, 2, 3$.
>
> **Step 3: Conservation.** For any Hamiltonian $H$ with $\{L^i, H\} = 0$ (rotationally invariant), each $L^i$ and $L^2 = \sum (L^i)^2$ are conserved along the Hamiltonian flow.

---

# Key Takeaways

**The Lie algebra structure of conserved quantities.** Whenever a Hamiltonian system has a continuous symmetry group $G$, the conserved quantities corresponding to that symmetry (the moment-map components) form a Lie subalgebra of $(C^\infty(M), \{\cdot, \cdot\})$ isomorphic to $\mathfrak{g}$. For $G = SO(3)$, this is the angular-momentum subalgebra $\mathfrak{so}(3)$, with the bracket $\{L^i, L^j\} = \epsilon^{ijk}L^k$. The Casimir functions of this subalgebra (functions Poisson-commuting with all $L^i$) are functions of $L^2$ alone — by the structure of $\mathfrak{so}(3)$. These Casimirs are conserved automatically for any rotational-invariant Hamiltonian, **without further computation**. The general principle: **identify the symmetry group, find the moment-map subalgebra, and the Casimirs of that subalgebra are automatic conserved quantities.** For $SO(3)$ symmetry, this gives $L^2$ free; for $SU(2)$ symmetry in quantum mechanics, this gives the spin-squared $\hat S^2$ free.

**The Poisson bracket is the classical limit of the commutator.** The angular-momentum Poisson brackets $\{L^i, L^j\} = \epsilon^{ijk}L^k$ are the **classical limit** of the quantum-mechanical angular momentum commutators $[\hat L^i, \hat L^j] = i\hbar\epsilon^{ijk}\hat L^k$. The classical-quantum correspondence is $\{f, g\} \leftrightarrow [\hat f, \hat g]/i\hbar$, so the algebra $\mathfrak{so}(3)$ structure persists from classical to quantum, with $i\hbar$ appearing as the proportionality constant. **The Lie algebra of observables is the universal structure, and it survives quantization.** This is why the same Lie group $SO(3)$ controls both classical and quantum angular momentum: at the classical level it controls the Poisson algebra; at the quantum level it controls the commutator algebra; the deformation between them is parametrized by $\hbar$. This pattern — Lie algebra structure persisting from classical to quantum — is the foundation of **representation theory's role in quantum mechanics**.

**Casimirs and the structure of integrable systems.** The Casimir $L^2$ is more than a curiosity: it is a **conserved quantity that needs no specific Hamiltonian to be conserved**. As long as the Hamiltonian respects the $SO(3)$ symmetry, $L^2$ is conserved. This is the **strongest possible form of conservation** — built into the geometry of the phase space rather than requiring a specific dynamics. **For integrable systems**, the existence of $n$ functionally independent involutive integrals (where $2n$ is the phase-space dimension) is the central structural feature, and **Casimirs are the prototype** of such "always conserved" quantities. For the 3D Kepler problem, the Casimirs are $L^2$ and $E$ (energy), giving $2 + 1 = 3$ functionally independent conserved quantities — enough to integrate the system. For more complex systems, finding the Casimirs of the relevant Lie subalgebras is the first step in identifying integrable structure.
