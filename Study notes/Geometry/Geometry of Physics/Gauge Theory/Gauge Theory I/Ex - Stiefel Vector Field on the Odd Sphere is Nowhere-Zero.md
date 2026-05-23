---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Field on a Manifold"
  - "Thm - Hairy Ball Theorem"
tags: [geometry, gauge-theory, sphere, parallelizability]
---

# Problem Statement

Consider the odd-dimensional sphere $S^{2k+1} = \{x \in \mathbb{R}^{2k+2} : |x| = 1\}$ for $k \geq 0$.

**(a)** Define the **Stiefel vector field**
$$v(x_1, x_2, x_3, x_4, \dots, x_{2k+1}, x_{2k+2}) = (-x_2, x_1, -x_4, x_3, \dots, -x_{2k+2}, x_{2k+1}).$$
Verify that $v(x) \in T_xS^{2k+1}$ for every $x \in S^{2k+1}$ — i.e., $v$ is tangent to the sphere.

**(b)** Verify that $v$ is nowhere zero on $S^{2k+1}$.

**(c)** Conclude that $\chi(S^{2k+1}) = 0$, completing the proof of **Euler's theorem**: $S^n$ admits a nowhere-vanishing smooth tangent vector field if and only if $n$ is odd.

**Recall:**

A vector field on $M$ assigns to each $p \in M$ a tangent vector $v(p) \in T_pM$. On a sphere $S^n \subset \mathbb{R}^{n+1}$, the tangent space at $x$ is $T_xS^n = \{v \in \mathbb{R}^{n+1} : v \perp x\}$ (with respect to the standard Euclidean inner product).

![[Thm - Hairy Ball Theorem#Statement]]

---

# Convergent Strategy

**Problem class:** This is a *constructive* counterpart to the obstruction-style [[Thm - Hairy Ball Theorem|Hairy Ball theorem]]. The Hairy Ball says even-dimensional spheres have no nowhere-zero tangent fields ($\chi \ne 0$ is the obstruction); this exercise constructs an *explicit* nowhere-zero field on every odd-dimensional sphere, completing Euler's "iff" statement. The construction is elegant — a single quadratic formula — and the verification is two short calculations.

**Assumption pattern:** The Stiefel field $v$ is defined as a specific linear map on $\mathbb{R}^{2k+2}$, then restricted to $S^{2k+1}$. Two conditions need verification: tangency (the restriction lands in the tangent bundle) and non-vanishing. Tangency reduces to checking $\langle v, x\rangle = 0$ on $S^{2k+1}$. Non-vanishing reduces to checking $|v(x)| > 0$ on $S^{2k+1}$ — in fact $|v(x)| = |x| = 1$, so the field is unit-length everywhere.

**Theorem routing:** The construction is direct: explicit formula → verify two algebraic identities. The conclusion $\chi(S^{2k+1}) = 0$ then follows from [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf]] applied to a nowhere-zero field: the total index of the field is $0$ (vacuously, since there are no zeros), and Poincaré-Hopf equates this to $\chi$.

**Key decision point:** The non-obvious choice is the *specific* form of the field — pairing up consecutive coordinates and applying a $90°$ rotation to each pair. This works because pairs $(x_{2j-1}, x_{2j})$ can be viewed as complex numbers $z_j = x_{2j-1} + ix_{2j}$, and $v$ corresponds to multiplication by $i$. The reason the construction needs an *even* number of coordinates $2k+2$ — equivalently, the sphere dimension $2k+1$ is *odd* — is exactly so that the coordinates can be paired up. For even-dimensional spheres in $\mathbb{R}^{\mathrm{odd}}$, there is an unpaired coordinate and no such construction exists. The decision to pair coordinates is what makes the construction succeed only in the odd-dimensional case.

---

# Legal Operations Used

1. **Choose a local trivialization (chart) and compute in coordinates** (operation 1 of the topic page). Here the "chart" is the embedding $S^{2k+1} \hookrightarrow \mathbb{R}^{2k+2}$, in which the tangent space at $x$ is the perpendicular complement of $x$ and computations are linear algebra in $\mathbb{R}^{2k+2}$.

9. **Detect non-triviality of a bundle by a non-zero topological invariant** (operation 9). Combined with Poincaré-Hopf: a nowhere-zero field has total index $0$, equating to $\chi(S^{2k+1})$ via the theorem. So existence of the field forces $\chi(S^{2k+1}) = 0$ — a topological computation done by a single existence proof.

---

# Hints

> [!note]- Hint 1
> The field $v(x) = (-x_2, x_1, -x_4, x_3, \dots)$ pairs up consecutive coordinates. For each pair $(x_{2j-1}, x_{2j})$, the rule is $(a, b) \mapsto (-b, a)$ — a $90°$ counterclockwise rotation in the $(x_{2j-1}, x_{2j})$-plane.

> [!note]- Hint 2
> To verify tangency $v \perp x$ at each $x \in S^{2k+1}$, compute the dot product $\langle v, x\rangle$ and observe that contributions from each pair cancel.

> [!note]- Hint 3
> To verify $v$ is nowhere zero, compute $|v(x)|^2$ and observe it equals $|x|^2 = 1$ on $S^{2k+1}$. So $v$ has constant unit length, in particular never zero.

> [!note]- Hint 4 (for part c)
> Once you have a nowhere-zero smooth vector field on $S^{2k+1}$, apply Poincaré-Hopf: the total index of *any* field with isolated zeros equals $\chi$. Our field has no zeros at all, hence total index $0$, hence $\chi(S^{2k+1}) = 0$.

> [!note]- Hint 5 (complex interpretation)
> Pairing coordinates as $z_j = x_{2j-1} + ix_{2j}$ identifies $\mathbb{R}^{2k+2}$ with $\mathbb{C}^{k+1}$, and $S^{2k+1}$ with the unit sphere there. The Stiefel field corresponds to **multiplication by $i$**: $v(z_1, \dots, z_{k+1}) = (iz_1, \dots, iz_{k+1})$. This makes it manifest that $v$ is tangent (multiplication by $i$ preserves length, hence preserves the unit sphere infinitesimally) and unit-length (multiplication by $i$ is an isometry).

---

# Solution

The proof has three short steps. Step 1 verifies $v$ is tangent to $S^{2k+1}$ via the orthogonality computation $\langle v, x\rangle = 0$. Step 2 verifies $v$ is nowhere zero via $|v(x)| = |x| = 1$. Step 3 concludes $\chi(S^{2k+1}) = 0$ via Poincaré-Hopf applied to the nowhere-zero field. The complex interpretation makes the construction transparent and shows why it works only in even-real-dimensional ambient space.

**Step 1: Tangency, $\langle v(x), x\rangle = 0$ for $x \in S^{2k+1}$.**

> [!note]- Derivation
> Compute the dot product:
> $$\langle v(x), x\rangle = \sum_{j=1}^{k+1}\bigl[(-x_{2j})(x_{2j-1}) + (x_{2j-1})(x_{2j})\bigr] = \sum_{j=1}^{k+1}\bigl[-x_{2j}x_{2j-1} + x_{2j-1}x_{2j}\bigr] = 0.$$
>
> Each pair of consecutive coordinates contributes $-x_{2j-1}x_{2j} + x_{2j-1}x_{2j} = 0$. The full sum is therefore zero. Hence $v(x) \perp x$ for all $x \in \mathbb{R}^{2k+2}$, and in particular for $x \in S^{2k+1}$, $v(x) \in T_xS^{2k+1}$.

**Step 2: Non-vanishing, $|v(x)|^2 = |x|^2$.**

> [!note]- Derivation
> Compute the squared norm:
> $$|v(x)|^2 = \sum_{j=1}^{k+1}\bigl[(-x_{2j})^2 + (x_{2j-1})^2\bigr] = \sum_{j=1}^{k+1}\bigl[x_{2j}^2 + x_{2j-1}^2\bigr] = \sum_{i=1}^{2k+2}x_i^2 = |x|^2.$$
>
> Each pair contributes $x_{2j}^2 + x_{2j-1}^2$ to both $|v(x)|^2$ and $|x|^2$. Hence $|v(x)| = |x|$ everywhere. On $S^{2k+1}$, $|x| = 1$, so $|v(x)| = 1$ — the field is *unit length* everywhere, in particular nowhere zero.

**Step 3: Conclusion via Poincaré-Hopf.**

> [!note]- Derivation
> $v$ is a smooth tangent vector field on $S^{2k+1}$ with *no* zeros. By [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf]], the total index of any smooth field with isolated zeros equals $\chi(S^{2k+1})$. A field with no zeros has total index $0$ (vacuously — empty sum). Hence
> $$\chi(S^{2k+1}) = 0.$$
>
> Combined with [[Thm - Hairy Ball Theorem|the Hairy Ball theorem]] (no nowhere-zero field on $S^{2k}$ since $\chi(S^{2k}) = 2 \ne 0$), this completes Euler's iff statement: $S^n$ admits a nowhere-zero smooth tangent vector field if and only if $n$ is odd.

> [!note]- Complete formal solution
> Define $v : \mathbb{R}^{2k+2} \to \mathbb{R}^{2k+2}$ by $v(x_1, \dots, x_{2k+2}) = (-x_2, x_1, -x_4, x_3, \dots, -x_{2k+2}, x_{2k+1})$.
>
> **Tangency:** $\langle v(x), x\rangle = \sum_{j=1}^{k+1}[(-x_{2j})(x_{2j-1}) + (x_{2j-1})(x_{2j})] = 0$ for all $x$, so $v(x) \in T_xS^{2k+1}$ for $x \in S^{2k+1}$.
>
> **Non-vanishing:** $|v(x)|^2 = \sum_{j=1}^{k+1}[x_{2j}^2 + x_{2j-1}^2] = |x|^2$. On $S^{2k+1}$, $|v(x)| = 1 \ne 0$, so $v$ is nowhere zero.
>
> **Conclusion:** $v$ is a smooth nowhere-zero tangent vector field on $S^{2k+1}$. By Poincaré-Hopf, $0 = \sum j_v(p) = \chi(S^{2k+1})$. $\blacksquare$
>
> **Complex-coordinate restatement.** Identifying $\mathbb{R}^{2k+2}$ with $\mathbb{C}^{k+1}$ via $z_j = x_{2j-1} + ix_{2j}$, the Stiefel field is $v(z) = iz = (iz_1, \dots, iz_{k+1})$ — multiplication by $i$. Since multiplication by $i$ is an isometry of $\mathbb{C}^{k+1}$, it preserves $|z| = 1$ (tangency: $\langle iz, z\rangle_{\mathbb{R}} = 0$ since $\mathrm{Re}(i|z|^2) = 0$) and preserves length ($|iz| = |z| = 1$).

> [!warning] Why this construction needs *even* ambient dimension
> The construction works because the coordinates of $\mathbb{R}^{2k+2}$ can be paired up — each pair $(x_{2j-1}, x_{2j})$ undergoing a $90°$ rotation. For *odd* ambient dimension $2k+1$ (corresponding to even-dimensional spheres $S^{2k}$), there is one unpaired coordinate, and no analogous quadratic field can be defined — confirming the *non*-existence direction of Euler's theorem from the constructive side. The pairing is the structural reason for the even/odd dichotomy.

---

# Key Takeaways

**Pairing coordinates and using multiplication by $i$ is the universal source of nowhere-zero fields on odd spheres.**

The Stiefel field is best understood through its complex interpretation: $v(z) = iz$ on $S^{2k+1} \subset \mathbb{C}^{k+1}$. This makes both verifications trivial (multiplication by $i$ is an isometry, hence preserves both tangency and length) and reveals the structural reason for the construction. For $S^{2k+1}$ to admit such a field, we need $S^{2k+1}$ to sit inside an *even*-dimensional ambient space — equivalently, $2k+1$ odd. Even-dimensional spheres sit in odd-dimensional ambient space, so the pairing argument fails. The pattern "use multiplication by elements of a division algebra ($\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$) to construct vector fields on spheres" generalizes to the question of which spheres are parallelizable.

**Constructive existence proofs vs. obstruction proofs.**

The Hairy Ball theorem proves *non-existence* of nowhere-zero fields on even spheres via a topological obstruction ($\chi \ne 0$). This exercise proves *existence* on odd spheres via an explicit construction. Together they give the *iff* statement. This pattern — existence by construction, non-existence by topology — recurs throughout mathematics. In algebraic topology one constructs maps (cells, attaching maps) to prove existence, and uses cohomology to prove non-existence. In number theory one constructs solutions (e.g., Hensel lifting) to prove existence, and uses class field theory or local-global principles to prove non-existence. The two halves are complementary and equally important.

**Cross-link to companion exercise.** See [[Ex - Index of the Source-Sink Vector Field on the Sphere]] for the explicit computation of indices for fields on $S^2$ (the even-dimensional case where nowhere-zero fields are forbidden). The contrast between the two exercises is instructive: $S^2$ requires zeros (with total index $+2$); $S^3$ admits nowhere-zero fields (Stiefel's construction). The structural difference is the pairing argument, and Euler's theorem is the dichotomy it gives.

**Connection to parallelizability and division algebras.**

The Stiefel field uses *one* division-algebra element ($i$) to construct *one* nowhere-zero field. The question of when one can construct an *entire frame* of nowhere-zero fields — making the sphere **parallelizable** — is the Hopf-Adams theorem: only $S^1$, $S^3$, $S^7$ are parallelizable, corresponding to the existence of multiplicative structures on $\mathbb{R}^2$ (complex numbers), $\mathbb{R}^4$ (quaternions), $\mathbb{R}^8$ (octonions). The Stiefel field on $S^{2k+1}$ uses only the complex structure, hence gives only one vector field. For $S^3 \subset \mathbb{H}$ one can also use *multiplication by $j$* and *multiplication by $k$* to get three linearly independent nowhere-zero fields, parallelizing $S^3$. Same for $S^7 \subset \mathbb{O}$ with the seven imaginary octonion units.
