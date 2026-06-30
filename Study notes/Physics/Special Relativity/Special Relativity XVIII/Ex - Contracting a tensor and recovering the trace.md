---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Tensor Operations"
  - "Def - Tensors on Minkowski Space"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

Work in mostly-minus signature, $c = 1$.

1. For a type-$(1,1)$ tensor $T^\mu{}_\nu$, define its contraction (trace) and show $T^\mu{}_\mu = C^1_1 T$ is a Lorentz scalar.
2. Compute the traces of the two universal tensors: the Kronecker delta $\delta^\mu{}_\mu$ and the metric contracted with its inverse $g_{\mu\nu}g^{\mu\nu}$.
3. Show that the electromagnetic field strength is traceless: $F^\mu{}_\mu = 0$. Identify exactly which property of $F$ forces this.
4. For a vector $\vec v$ and a one-form $\omega$, verify the identity $C^1_1(\vec v\otimes\omega) = \langle\omega, \vec v\rangle = v^\mu\omega_\mu$.

**Recall:**

![[Def - Tensor Operations#The Definition]]

A type-$(1,1)$ tensor has one contravariant (upper) and one covariant (lower) index; its only [[Def - Tensor Operations|contraction]] is the **trace** $T^\mu{}_\mu$, obtained by setting the two equal and summing. The field strength $F^{\mu\nu}$ is a [[Def - Alternate Forms and the Exterior Product|2-form]], antisymmetric: $F^{\mu\nu} = -F^{\nu\mu}$. The [[Def - Tensors on Minkowski Space|metric]] satisfies $g_{\mu\rho}g^{\rho\nu} = \delta_\mu{}^\nu$.

---

# Convergent Strategy

**Problem class.** A *compute-a-tensor-operation* and *establish-an-invariant* problem, exercising [[Def - Tensor Operations|contraction]]. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]] says: a fully contracted expression (every index paired up-and-down) is a Lorentz scalar.

**Assumption pattern.** Each object's index structure is the only datum needed. The Kronecker delta has components $\delta^\mu{}_\nu$ equal to $1$ on the diagonal; the metric's defining property $g_{\mu\rho}g^{\rho\nu} = \delta_\mu{}^\nu$ relates parts 2; antisymmetry of $F$ drives part 3.

**Theorem routing.** Part 1: the transformation law of a type-$(1,1)$ tensor, with the $P^{-1}$ and $P$ cancelling on contraction, gives invariance. Part 2: $\delta^\mu{}_\mu = \sum_\mu 1 = 4$ (dimension); $g_{\mu\nu}g^{\mu\nu} = \delta^\mu{}_\mu = 4$ by the inverse relation. Part 3: contracting an antisymmetric tensor on its two indices forces zero. Part 4: the [[Def - Tensor Operations|tensor product]] followed by contraction reproduces the form–vector pairing.

**Key decision point.** The crux is part 3: a *symmetric* sum over an antisymmetric object vanishes. The contraction $F^\mu{}_\mu$ sums the diagonal, and the diagonal of an antisymmetric matrix is zero — but the deeper statement is that contracting *any* pair of indices on which a tensor is antisymmetric gives zero, because the symmetric contraction operation annihilates the antisymmetric part. Recognising this "symmetric-times-antisymmetric is zero" pattern is the lesson.

---

# Legal Operations Used

1. **Operation 2 from the topic page (contract an upper against a lower index).** The central operation throughout: the trace in parts 1–3, and the form–vector pairing in part 4, are all up–down contractions.

2. **Operation 3 from the topic page (tensor product).** Used in part 4 to build $\vec v\otimes\omega$, a type-$(1,1)$ tensor, before contracting it.

---

# Hints

> [!note]- Hint 1
> The trace contracts the one upper against the one lower index. Under a change of basis a type-$(1,1)$ tensor transforms by $T'^\mu{}_\nu = (P^{-1})^\mu{}_\alpha P^\beta{}_\nu T^\alpha{}_\beta$; setting $\mu = \nu$ and summing makes $(P^{-1})^\mu{}_\alpha P^\beta{}_\mu = \delta^\beta{}_\alpha$, so $T'^\mu{}_\mu = T^\alpha{}_\alpha$ — invariant.

> [!note]- Hint 2
> $\delta^\mu{}_\mu = \delta^0{}_0 + \delta^1{}_1 + \delta^2{}_2 + \delta^3{}_3 = 4$. For the metric, use $g_{\mu\nu}g^{\mu\nu} = g_{\mu\nu}g^{\nu\mu}$ (metric is symmetric) $= \delta_\mu{}^\mu = 4$. Both equal the spacetime dimension.

> [!note]- Hint 3
> $F^\mu{}_\mu = \eta_{\mu\nu}F^{\mu\nu}$. Since $F^{\mu\nu}$ is antisymmetric and $\eta_{\mu\nu}$ is symmetric, their full contraction is zero — equivalently, $F^\mu{}_\mu = \sum_\mu F^\mu{}_\mu$ is the sum of diagonal entries, and an antisymmetric matrix has zero diagonal.

---

# Solution

The exercise is a tour of the [[Def - Tensor Operations|contraction]] operation and its invariance. The plan: establish that a trace is a scalar from the transformation law (Step 1), compute the two universal traces $\delta^\mu{}_\mu = g_{\mu\nu}g^{\mu\nu} = 4$ (Step 2), use symmetric-times-antisymmetric to kill the trace of $F$ (Step 3), and recover the form–vector pairing as a contraction of a tensor product (Step 4).

**Step 1: the trace $T^\mu{}_\mu$ is a Lorentz scalar.**

> [!note]- Derivation
> Under a change of basis with matrix $P$, a [[Def - Tensors on Minkowski Space|type-(1,1) tensor]] transforms by
> $$T'^\mu{}_\nu = (P^{-1})^\mu{}_\alpha\, P^\beta{}_\nu\, T^\alpha{}_\beta.$$
> Contract (set $\nu = \mu$, sum):
> $$T'^\mu{}_\mu = (P^{-1})^\mu{}_\alpha\, P^\beta{}_\mu\, T^\alpha{}_\beta = \big(P^\beta{}_\mu(P^{-1})^\mu{}_\alpha\big)T^\alpha{}_\beta = \delta^\beta{}_\alpha\, T^\alpha{}_\beta = T^\alpha{}_\alpha.$$
> The trace is the same number in every basis: a Lorentz scalar. The cancellation $P^\beta{}_\mu(P^{-1})^\mu{}_\alpha = \delta^\beta{}_\alpha$ is exactly the up–down pairing doing its work — this is why only an up–down contraction is invariant.

**Step 2: $\delta^\mu{}_\mu = 4$ and $g_{\mu\nu}g^{\mu\nu} = 4$.**

> [!note]- Derivation
> The Kronecker delta is the identity endomorphism; its trace is the dimension:
> $$\delta^\mu{}_\mu = \delta^0{}_0 + \delta^1{}_1 + \delta^2{}_2 + \delta^3{}_3 = 1 + 1 + 1 + 1 = 4.$$
> For the metric, use the defining inverse relation $g_{\mu\rho}g^{\rho\nu} = \delta_\mu{}^\nu$ and the symmetry $g^{\mu\nu} = g^{\nu\mu}$:
> $$g_{\mu\nu}g^{\mu\nu} = g_{\mu\nu}g^{\nu\mu} = \delta_\mu{}^\mu = 4.$$
> Both contractions return the spacetime dimension $4$. (In an orthonormal frame one can check directly: $\eta_{\mu\nu}\eta^{\mu\nu} = (+1)^2 + (-1)^2 + (-1)^2 + (-1)^2 = 4$.)

**Step 3: $F^\mu{}_\mu = 0$ because $F$ is antisymmetric.**

> [!note]- Derivation
> Write the trace as a full contraction with the metric:
> $$F^\mu{}_\mu = \eta_{\mu\nu}F^{\mu\nu}.$$
> Here $\eta_{\mu\nu}$ is **symmetric** ($\eta_{\mu\nu} = \eta_{\nu\mu}$) and $F^{\mu\nu}$ is **antisymmetric** ($F^{\mu\nu} = -F^{\nu\mu}$). Relabel the summation indices $\mu\leftrightarrow\nu$:
> $$F^\mu{}_\mu = \eta_{\mu\nu}F^{\mu\nu} = \eta_{\nu\mu}F^{\nu\mu} = \eta_{\mu\nu}(-F^{\mu\nu}) = -F^\mu{}_\mu,$$
> using symmetry of $\eta$ and antisymmetry of $F$. Hence $2F^\mu{}_\mu = 0$, so $F^\mu{}_\mu = 0$. Equivalently, $F^\mu{}_\mu = \sum_\mu F^\mu{}_\mu$ is the trace of the mixed-index matrix, whose diagonal entries $F^\mu{}_\mu$ (no sum) come from the antisymmetric $F^{\mu\nu}$ and vanish. The property forced is **antisymmetry**: the full contraction of a symmetric tensor with an antisymmetric one is always zero.

**Step 4: $C^1_1(\vec v\otimes\omega) = \langle\omega, \vec v\rangle$.**

> [!note]- Derivation
> The [[Def - Tensor Operations|tensor product]] $\vec v\otimes\omega$ is the type-$(1,1)$ tensor with components $(\vec v\otimes\omega)^\mu{}_\nu = v^\mu\omega_\nu$. Its contraction (trace) is
> $$C^1_1(\vec v\otimes\omega) = (\vec v\otimes\omega)^\mu{}_\mu = v^\mu\omega_\mu = \langle\omega, \vec v\rangle,$$
> the action of the form $\omega$ on the vector $\vec v$. This is the prototype contraction: every "form eats vector" pairing is the trace of a tensor product, and it shows that contraction generalises the dual pairing $\langle\cdot, \cdot\rangle$.

> [!note]- Complete formal solution
> **(1)** Under $P$, $T'^\mu{}_\mu = (P^{-1})^\mu{}_\alpha P^\beta{}_\mu T^\alpha{}_\beta = \delta^\beta{}_\alpha T^\alpha{}_\beta = T^\alpha{}_\alpha$, so the trace is a scalar.
> **(2)** $\delta^\mu{}_\mu = 4$; and $g_{\mu\nu}g^{\mu\nu} = g_{\mu\nu}g^{\nu\mu} = \delta_\mu{}^\mu = 4$.
> **(3)** $F^\mu{}_\mu = \eta_{\mu\nu}F^{\mu\nu}$; relabelling and using $\eta$ symmetric, $F$ antisymmetric gives $F^\mu{}_\mu = -F^\mu{}_\mu = 0$. The driving property is antisymmetry (symmetric $\times$ antisymmetric, fully contracted, $= 0$).
> **(4)** $(\vec v\otimes\omega)^\mu{}_\nu = v^\mu\omega_\nu$, so $C^1_1(\vec v\otimes\omega) = v^\mu\omega_\mu = \langle\omega, \vec v\rangle$. $\blacksquare$

---

# Key Takeaways

**Contraction is invariant precisely because it pairs an upper with a lower index.** The proof that the trace is a Lorentz scalar is the proof that any legal contraction is: the factor $P^{-1}$ from the upper index and the factor $P$ from the lower index meet and cancel, $P(P^{-1}) = \mathbb{1}$, leaving a basis-independent number. This is the structural reason the chapter insists on the up–down rule. The reusable diagnostic: to see whether a contracted quantity is invariant, check that the summed index is once up and once down; if so, the $P$ and $P^{-1}$ cancel and you have a scalar, no computation needed. This single observation is what lets one write down Lorentz-invariant quantities ($X^\mu X_\mu$, $F_{\mu\nu}F^{\mu\nu}$, $\partial_\mu J^\mu$) by inspection.

**Symmetric times antisymmetric, fully contracted, is always zero.** The vanishing of $F^\mu{}_\mu$ is an instance of a constantly-used identity: if $S^{\mu\nu}$ is symmetric and $A_{\mu\nu}$ is antisymmetric, then $S^{\mu\nu}A_{\mu\nu} = 0$. The proof is one relabelling: $S^{\mu\nu}A_{\mu\nu} = S^{\nu\mu}A_{\nu\mu} = S^{\mu\nu}(-A_{\mu\nu}) = -S^{\mu\nu}A_{\mu\nu}$. This kills enormous numbers of terms in relativistic computations — whenever a symmetric object (the metric, the energy-momentum tensor, a symmetric derivative) is contracted against an antisymmetric one (the field strength, the angular-momentum tensor), the result is zero. The trigger to internalise: spot a symmetric and an antisymmetric tensor sharing both contracted indices, and write down zero immediately. It is the fastest simplification in the toolkit.

**Universal traces equal the dimension, and they recur everywhere.** The facts $\delta^\mu{}_\mu = 4$ and $g_{\mu\nu}g^{\mu\nu} = 4$ are trivial but ubiquitous: they appear whenever a trace is taken in four dimensions — in the trace of the energy-momentum tensor, in the contraction of the metric in dimensional regularisation, in the normalisation of projectors. The general statement is that the trace of the identity on an $n$-dimensional space is $n$, so in $d$ spacetime dimensions $\delta^\mu{}_\mu = d$ — a fact one carries into any dimension. Knowing these by reflex saves a recomputation every time, and the appearance of a stray $4$ in a relativistic formula is very often one of these traces. The companion fact, that contraction generalises the form–vector pairing $\langle\omega, \vec v\rangle = C^1_1(\vec v\otimes\omega)$, is the conceptual anchor: contraction is "evaluation," the same operation that lets a form act on a vector, threaded through a tensor of any rank.
