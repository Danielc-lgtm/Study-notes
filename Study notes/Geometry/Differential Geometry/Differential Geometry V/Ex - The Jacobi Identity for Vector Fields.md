---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Smooth Vector Field"
  - "Thm - Lie Bracket Properties"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $X, Y, Z \in \mathfrak{X}(M)$ be smooth vector fields on a smooth manifold $M$. Prove the **Jacobi identity**:

$$[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0.$$

Interpret this identity as the statement that $\mathrm{ad}_X := [X, \cdot\,] : \mathfrak{X}(M) \to \mathfrak{X}(M)$ is a **derivation of the Lie bracket**:

$$\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z].$$

**Recall:**

![[Def - The Lie Bracket of Vector Fields#The Definition]]

The bracket is $\mathbb{R}$-bilinear and antisymmetric: $[X, Y] = -[Y, X]$. It is the commutator of derivations: $[X, Y]f = X(Yf) - Y(Xf)$ on smooth functions.

A **Lie algebra** is a vector space $\mathfrak{g}$ with a bracket $[\cdot, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ that is bilinear, antisymmetric, and satisfies the Jacobi identity above. Proving Jacobi makes $(\mathfrak{X}(M), [\cdot, \cdot])$ a Lie algebra.

A **derivation of a Lie algebra** $\mathfrak{g}$ is a linear map $D : \mathfrak{g} \to \mathfrak{g}$ satisfying $D[Y, Z] = [DY, Z] + [Y, DZ]$ — the Leibniz rule for the bracket. The Jacobi identity says exactly that $\mathrm{ad}_X = [X, \cdot]$ is a derivation.

---

# Convergent Strategy

**Problem class:** Prove an algebraic identity by direct calculation using the commutator definition. The class is "verify a Lie algebra axiom"; the computation is mechanical but requires careful bookkeeping of the twelve cubic terms.

**Assumption pattern:** Three smooth vector fields $X, Y, Z$ acting as derivations on $C^\infty(M)$, with $[X, Y] = XY - YX$ as a commutator of operators. The strategy is to expand each nested bracket as a difference of products of three operators and observe cancellation in the sum.

**Theorem routing:** $[X, Y] = XY - YX$ ⟶ expand the three nested brackets ⟶ enumerate the twelve cubic terms ⟶ check they cancel in pairs.

**Key decision point:** The non-obvious step is the **enumeration of cubic terms and their cancellation**. There are six possible orderings of three operators (the permutations of $X, Y, Z$ acting on a function), each appearing twice in the sum (with opposite signs). Tracking the signs is the substance of the proof; the cancellation is automatic once the enumeration is correct.

---

# Legal Operations Used

1. **Operation 6 from the topic page (recognize a bracket via the derivation commutator).** Use $[X, Y] = XY - YX$ as the operator definition and expand the nested brackets accordingly.

2. **Operation 5 from the topic page (compute a Lie bracket coordinatewise), as an alternative route.** Compute each component of the Jacobi sum using the coordinate formula and verify the cancellation — works but is much messier than the operator route.

---

# Hints

> [!note]- Hint 1
> Apply the commutator definition to each nested bracket. For instance, $[X, [Y, Z]] = X[Y, Z] - [Y, Z]X = X(YZ - ZY) - (YZ - ZY)X = XYZ - XZY - YZX + ZYX$.

> [!note]- Hint 2
> Repeat for $[Y, [Z, X]]$ and $[Z, [X, Y]]$. Each gives four cubic terms in $X, Y, Z$ in some order. Add up all twelve terms.

> [!note]- Hint 3
> The six possible orderings of $X, Y, Z$ acting on a function are $XYZ, XZY, YXZ, YZX, ZXY, ZYX$. Each appears twice in the sum, with opposite signs. Check by enumeration.

---

# Solution

The proof is a direct expansion using the commutator structure. Plan: expand each of the three nested brackets as a sum of four cubic operator products; sum the twelve terms; observe that each of the six orderings of $X, Y, Z$ appears exactly twice with opposite signs, hence everything cancels. The substance is in the bookkeeping.

**Step 1: Expand the three nested brackets.**

The first nested bracket:
$$[X, [Y, Z]] = X[Y, Z] - [Y, Z]X = X(YZ - ZY) - (YZ - ZY)X = XYZ - XZY - YZX + ZYX.$$

The second nested bracket (cyclic permutation $X \to Y, Y \to Z, Z \to X$):
$$[Y, [Z, X]] = Y(ZX - XZ) - (ZX - XZ)Y = YZX - YXZ - ZXY + XZY.$$

The third nested bracket (cyclic permutation $Y \to Z, Z \to X, X \to Y$):
$$[Z, [X, Y]] = Z(XY - YX) - (XY - YX)Z = ZXY - ZYX - XYZ + YXZ.$$

> [!note]- Derivation (Step 1)
> Each nested bracket is expanded as a difference of products.
>
> $[X, [Y, Z]] = X \circ [Y, Z] - [Y, Z] \circ X$.
> - $X \circ [Y, Z] = X(YZ - ZY) = XYZ - XZY$.
> - $[Y, Z] \circ X = (YZ - ZY)X = YZX - ZYX$.
> - Difference: $XYZ - XZY - YZX + ZYX$.
>
> $[Y, [Z, X]] = Y \circ [Z, X] - [Z, X] \circ Y$.
> - $Y \circ [Z, X] = Y(ZX - XZ) = YZX - YXZ$.
> - $[Z, X] \circ Y = (ZX - XZ)Y = ZXY - XZY$.
> - Difference: $YZX - YXZ - ZXY + XZY$.
>
> $[Z, [X, Y]] = Z \circ [X, Y] - [X, Y] \circ Z$.
> - $Z \circ [X, Y] = Z(XY - YX) = ZXY - ZYX$.
> - $[X, Y] \circ Z = (XY - YX)Z = XYZ - YXZ$.
> - Difference: $ZXY - ZYX - XYZ + YXZ$.

**Step 2: Sum the twelve terms.**

Adding the three expansions:
$$\begin{aligned}
[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] &= XYZ - XZY - YZX + ZYX \\
&+ YZX - YXZ - ZXY + XZY \\
&+ ZXY - ZYX - XYZ + YXZ.
\end{aligned}$$

> [!note]- Derivation (Step 2)
> Collect terms by which ordering of $X, Y, Z$ they involve.
>
> *Ordering $XYZ$:* appears with $+$ in line 1 and with $-$ in line 3. Sum: $0$.
>
> *Ordering $XZY$:* appears with $-$ in line 1 and with $+$ in line 2. Sum: $0$.
>
> *Ordering $YXZ$:* appears with $-$ in line 2 and with $+$ in line 3. Sum: $0$.
>
> *Ordering $YZX$:* appears with $-$ in line 1 and with $+$ in line 2. Sum: $0$.
>
> *Ordering $ZXY$:* appears with $-$ in line 2 and with $+$ in line 3. Sum: $0$.
>
> *Ordering $ZYX$:* appears with $+$ in line 1 and with $-$ in line 3. Sum: $0$.
>
> All six orderings cancel in pairs; the total sum is zero.

**Step 3: Reinterpret as $\mathrm{ad}_X$ is a derivation.**

The Jacobi identity rewrites as
$$[X,[Y,Z]]=[[X,Y],Z]+[Y,[X,Z]]. \tag{*}$$

Starting from Jacobi $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$, move the second and third terms to the right and apply antisymmetry:
$$[X, [Y, Z]] = -[Y, [Z, X]] - [Z, [X, Y]] = [Y, [X, Z]] + [[X, Y], Z].$$
(Using $[Y, [Z, X]] = -[Y, [X, Z]]$ and $[Z, [X, Y]] = -[[X, Y], Z]$.) This rearrangement says
$$\mathrm{ad}_X([Y, Z]) = [Y, [X, Z]] + [[X, Y], Z] = [Y, \mathrm{ad}_X Z] + [\mathrm{ad}_X Y, Z],$$
which is the Leibniz rule for $\mathrm{ad}_X$ acting on the bracket — i.e. $\mathrm{ad}_X$ is a derivation of the Lie bracket.

> [!note]- Derivation (Step 3)
> Start from $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$. Use antisymmetry:
> - $[Y, [Z, X]] = [Y, -[X, Z]] = -[Y, [X, Z]]$.
> - $[Z, [X, Y]] = -[[X, Y], Z]$ (this is just the same expression; antisymmetry says $[Z, W] = -[W, Z]$, so $[Z, [X, Y]] = -[[X, Y], Z]$).
>
> Substituting:
> $$[X, [Y, Z]] - [Y, [X, Z]] - [[X, Y], Z] = 0,$$
> hence
> $$[X, [Y, Z]] = [Y, [X, Z]] + [[X, Y], Z] = [[X, Y], Z] + [Y, [X, Z]].$$
>
> Reading $\mathrm{ad}_X(\cdot) := [X, \cdot]$:
> $$\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z].$$
>
> This is the Leibniz rule for $\mathrm{ad}_X$ acting on the bracket, expressing that $\mathrm{ad}_X$ is a derivation of the Lie algebra $\mathfrak{X}(M)$.

> [!note]- Complete formal solution
> Compute each nested bracket using the commutator definition $[A, B] = AB - BA$:
> $$[X, [Y, Z]] = XYZ - XZY - YZX + ZYX,$$
> $$[Y, [Z, X]] = YZX - YXZ - ZXY + XZY,$$
> $$[Z, [X, Y]] = ZXY - ZYX - XYZ + YXZ.$$
>
> Summing, each of the six orderings of $X, Y, Z$ acting on a function appears exactly twice with opposite signs:
> - $XYZ$: $+1$ (first row) $- 1$ (third row) $= 0$.
> - $XZY$: $-1$ (first) $+ 1$ (second) $= 0$.
> - $YXZ$: $-1$ (second) $+ 1$ (third) $= 0$.
> - $YZX$: $-1$ (first) $+ 1$ (second) $= 0$.
> - $ZXY$: $-1$ (second) $+ 1$ (third) $= 0$.
> - $ZYX$: $+1$ (first) $- 1$ (third) $= 0$.
>
> Hence $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$, the Jacobi identity.
>
> Rearranging using antisymmetry: $[X, [Y, Z]] = [[X, Y], Z] + [Y, [X, Z]]$, equivalently $\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z]$. This is the Leibniz rule, so $\mathrm{ad}_X$ is a derivation of the bracket. $\qquad\blacksquare$

---

# Key Takeaways

**The Jacobi identity is the operator-commutator cancellation of cubic terms.** The proof boils down to an enumeration: three nested commutators of three operators produce twelve cubic terms, the six orderings of $X, Y, Z$ each appearing twice with opposite signs, so everything cancels. There is no clever rearrangement, no deeper algebraic trick — it is direct verification. The same proof works for *any* associative algebra (vector fields on $M$, matrices, operators on a Hilbert space, etc.) with the bracket defined as the commutator: every commutator-bracket on an associative algebra automatically satisfies Jacobi. The trigger pattern: whenever you have a bracket defined as $[A, B] = AB - BA$, Jacobi is automatic.

**The Jacobi identity is the integrability condition of the Lie algebra.** Without Jacobi, the bracket would still be antisymmetric and bilinear, but it would not be a *Lie algebra* — and the deep structural theorems (Lie's theorems, the existence of the exponential map, the integration of $\mathfrak{g}$ to a Lie [[Def - Group|group]]) all use Jacobi. In particular, Lie's third theorem (every finite-dimensional Lie algebra is the Lie algebra of some Lie group) crucially requires Jacobi: the proof builds a distribution whose involutivity is *exactly* Jacobi, and Frobenius's theorem integrates it.

**$\mathrm{ad}_X$ is a derivation, and this is the adjoint representation.** The reinterpretation of Jacobi as $\mathrm{ad}_X[Y, Z] = [\mathrm{ad}_X Y, Z] + [Y, \mathrm{ad}_X Z]$ says that $\mathrm{ad}_X$ acts on the Lie algebra as a derivation. The map $\mathrm{ad} : \mathfrak{g} \to \mathrm{Der}(\mathfrak{g})$, $X \mapsto \mathrm{ad}_X$, is a Lie algebra homomorphism (also a consequence of Jacobi), giving the **adjoint representation** of $\mathfrak{g}$ on itself. This is the foundational representation in Lie algebra structure theory: the Killing form is $\mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$, and semisimplicity of $\mathfrak{g}$ is the non-degeneracy of the Killing form. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Jacobi extends from $\mathfrak{X}(M)$ to many other settings.** The same proof — commutator on an associative algebra gives a Jacobi-satisfying bracket — applies to: (i) $\mathfrak{gl}(n)$ with the matrix commutator; (ii) Poisson brackets on a symplectic manifold (after some work; Jacobi here is equivalent to closedness of the symplectic form); (iii) quantum commutators $[\hat A, \hat B] = \hat A \hat B - \hat B \hat A$ on Hilbert space; (iv) brackets of derivations on any commutative [[Def - Ring|ring]]. In every case the Jacobi identity is automatic from the underlying associative structure, and the *Lie algebra* axioms are extracted by anti-symmetrizing. The Lie bracket on $\mathfrak{X}(M)$ is just the most geometric instance of this universal pattern.
