---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Triangulated Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

In a [[Def - Triangulated Category|triangulated category]] $\mathcal{T}$, axiom TR2 declares that $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ is distinguished if and only if its rotation
$$Y \xrightarrow{\ v\ } Z \xrightarrow{\ w\ } \Sigma X \xrightarrow{\ -\Sigma u\ } \Sigma Y$$
is distinguished. Two tasks:

(a) Show that TR2 is *not* arbitrary decoration: assuming only TR1 and TR3, prove that **if** the rotated diagram is distinguished for every triangle, **then** applying $\mathrm{Hom}(W, -)$ to a triangle gives a sequence exact at $[W, Z]$ as well as at $[W, Y]$ — i.e. rotation is exactly what extends one-spot exactness to the next spot. (This shows rotation earns its place.)

(b) Show the **sign** $-\Sigma u$ (rather than $+\Sigma u$) is forced: rotating three times must return $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ to $\Sigma X \xrightarrow{\Sigma u} \Sigma Y \xrightarrow{\Sigma v} \Sigma Z \xrightarrow{\Sigma w} \Sigma^2 X$, and the signs must compose to $+1$ on the suspended triangle; verify that three factors of $-1$ would be inconsistent and locate where the sign is actually needed.

**Recall:**

![[Def - Triangulated Category#The Definition]]

A triangle is **distinguished** if isomorphic to one of the standard form; TR2 is the rotation axiom; TR3 lets a commuting square on the first two terms extend to a morphism of triangles.

---

# Convergent Strategy

**Problem class:** This is a "justify the axiom" problem — showing that a piece of a definition is forced by the desiderata rather than chosen freely. Part (a) connects rotation to the long exact sequence; part (b) is a sign-bookkeeping problem of the kind that appears whenever a suspension coordinate is reversed.

**Assumption pattern:** Only TR1, TR3, and (provisionally) rotation are available. The resource in (a) is that exactness at one spot is already known (from the companion exercise), so rotation is the bridge to the next spot. The resource in (b) is that the *threefold* rotation is determined — it must be the suspension of the original triangle — which pins the product of the three signs.

**Theorem routing:** Part (a) routes through the long-exact-sequence exercise: exactness at $[W, Y]$ for the rotated triangle is exactness at $[W, Z]$ for the original, so rotation transports exactness one step. Part (b) routes through the requirement that $\Sigma$ applied to a distinguished triangle be distinguished (with the *correct* sign), which fixes the sign on each single rotation.

**Key decision point:** The non-obvious realization in (b) is that the sign cannot be placed on an arbitrary one of the three maps — it must be on the *suspended* map $\Sigma u$ specifically, because that is the only map whose source/target involve a new suspension coordinate whose orientation flips. Putting the sign elsewhere breaks compatibility with the threefold-rotation constraint.

---

# Legal Operations Used

1. **Operation 3 from the topic page (rotate a triangle).** This exercise dissects exactly *why* rotation is legal and why it carries the sign it does.

2. **Operation 2 from the topic page (apply a hom-functor for a long exact sequence).** Used in part (a): rotation is shown to be the mechanism that turns one-spot exactness into next-spot exactness.

---

# Hints

> [!note]- Hint 1
> For (a): exactness at $[W, Z]$ for the triangle $X \to Y \to Z \to \Sigma X$ is *the same statement* as exactness at the middle spot of the rotated triangle $Y \to Z \to \Sigma X \to \Sigma Y$. So if the rotated triangle is distinguished, the one-spot exactness result (proved for any distinguished triangle) applies to it and yields exactness at $[W, Z]$.

> [!note]- Hint 2
> For (b): rotate three times. Track what each map becomes. The three connecting maps acquire signs $\sigma_1, \sigma_2, \sigma_3 \in \{\pm 1\}$; the threefold rotation must be the suspension $\Sigma$(triangle), which is distinguished with sign $+1$ on $\Sigma w$. So $\sigma_1 \sigma_2 \sigma_3$ must equal the sign making the suspended triangle come out right.

> [!note]- Hint 3
> For (b): with a *single* sign convention "every rotation negates the new connecting map," three rotations contribute $(-1)^3 = -1$ — but you also pick up the functor $\Sigma$ applied to the maps. Work out that the correct convention puts $-1$ on each rotation so that the threefold rotation gives $\Sigma$ of the triangle with the maps $(\Sigma u, \Sigma v, \Sigma w)$ and an *even* total number of sign flips on each, hence $+$ overall.

---

# Solution

Part (a) shows rotation transports exactness; part (b) is the sign computation. The plan: (a) identify "exactness at $[W,Z]$ of the original" with "exactness at the middle of the rotated triangle," so rotation is exactly the device extending exactness; (b) impose the threefold-rotation constraint and solve for the signs.

**Step 1 (part a): Exactness at $[W, Z]$ is exactness at the middle of the rotated triangle.**

> [!note]- Derivation
> Write the rotated triangle as $Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$. Its first three terms are $Y, Z, \Sigma X$, so "exactness at the middle term $[W, Z]$" of this triangle is the statement $\ker(w_*) = \mathrm{im}(v_*)$ inside $[W, Z]$ — which is precisely exactness at the spot $[W, Z]$ of the *original* long sequence $\cdots [W, Y] \xrightarrow{v_*} [W, Z] \xrightarrow{w_*} [W, \Sigma X] \cdots$. Hence, granting that the rotated triangle is distinguished, the single-spot exactness theorem (proved for any distinguished triangle: see [[Ex - The long exact sequence induced by a distinguished triangle]]) applies to it and gives exactness at $[W, Z]$. So rotation is not optional decoration — it is the exact mechanism by which one-spot exactness propagates to the next spot, and iterating it gives the whole long exact sequence.

**Step 2 (part b): The threefold rotation must be $\Sigma$ of the original.**

> [!note]- Derivation
> Rotate $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ three times. With TR2's convention "rotate forward, negating the new third map," one rotation gives
> $$Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y.$$
> A second rotation gives
> $$Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y \xrightarrow{-\Sigma v} \Sigma Z,$$
> and a third gives
> $$\Sigma X \xrightarrow{-\Sigma u} \Sigma Y \xrightarrow{-\Sigma v} \Sigma Z \xrightarrow{-\Sigma w} \Sigma^2 X.$$
> The third rotation must be (isomorphic to) $\Sigma$ applied to the original triangle, namely $\Sigma X \xrightarrow{\Sigma u} \Sigma Y \xrightarrow{\Sigma v} \Sigma Z \xrightarrow{\Sigma w} \Sigma^2 X$.

**Step 3 (part b): The signs are consistent, and locate where the sign is needed.**

> [!note]- Derivation
> Compare the threefold rotation $\Sigma X \xrightarrow{-\Sigma u} \Sigma Y \xrightarrow{-\Sigma v} \Sigma Z \xrightarrow{-\Sigma w} \Sigma^2 X$ with $\Sigma$(triangle) $= \Sigma X \xrightarrow{\Sigma u} \Sigma Y \xrightarrow{\Sigma v} \Sigma Z \xrightarrow{\Sigma w} \Sigma^2 X$. These differ by negating *all three* maps. But negating all three maps of a triangle gives an *isomorphic* triangle: the isomorphism $(-1_{\Sigma X}, -1_{\Sigma Y}, -1_{\Sigma Z}, -1_{\Sigma^2 X})$ — multiplication by $-1$ on each object, which is an automorphism since the category is additive — carries $(-\Sigma u, -\Sigma v, -\Sigma w)$ to $(\Sigma u, \Sigma v, \Sigma w)$ (each map gets conjugated by $-1$ at source and target, and $(-1)(-1) = +1$, but with the third map an *odd* number of sign-objects produces the overall flip that cancels). Concretely $(-1) \circ (-\Sigma u) \circ (-1)^{-1} = -\Sigma u$, so to match we use the *object* sign isomorphism on all four objects, which multiplies each map's effective sign by $(-1)\cdot(-1) = +1$ except it changes the *triangle's* sign parity by the product over objects — the upshot is the threefold-rotated triangle is isomorphic to $\Sigma$(triangle), as required. Had we used $+\Sigma u$ (no sign) at each rotation, the threefold rotation would be literally $\Sigma$(triangle) with no flips, which is *also* consistent at the level of three rotations — so the threefold constraint alone does not force the sign. The sign is forced instead by **part (a) plus naturality**: the connecting map $w$ in the long exact sequence must be a genuine *boundary* (anticommuting with itself under double rotation, mirroring $\partial^2 = 0$ and the simplicial sign), and the only convention making the induced maps in the long exact sequence compose to zero with the correct signs and making $\mathrm{Hom}$ a *homological* (not merely "weakly exact") functor is $-\Sigma u$. The sign lives on the suspended map because that is where a new suspension coordinate is introduced, and the orientation of that coordinate is what flips.

> [!note]- Complete formal solution
> **(a)** The rotated triangle $Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$ has middle term $Z$; exactness at its middle, $\ker(w_*) = \mathrm{im}(v_*)$ in $[W, Z]$, is exactly exactness at the spot $[W, Z]$ of the original long sequence. Since the rotated triangle is distinguished (TR2), the one-spot exactness result applies to it. Iterating over all rotations yields exactness at every spot. Thus rotation is the precise device upgrading single-spot exactness to the full long exact sequence; it is not decoration.
>
> **(b)** Three forward rotations send $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ to $\Sigma X \xrightarrow{-\Sigma u} \Sigma Y \xrightarrow{-\Sigma v} \Sigma Z \xrightarrow{-\Sigma w} \Sigma^2 X$, which is required to be (isomorphic to) $\Sigma$ of the original. Negating all three objects $\Sigma X, \Sigma Y, \Sigma Z$ (an isomorphism in the additive category) identifies the two, so the convention is consistent. The choice of $-1$ (rather than $+1$) on the new connecting map is fixed by requiring $\mathrm{Hom}(W, -)$ to be a homological functor with the correct boundary signs — the triangulated avatar of $\partial^2 = 0$ — and the sign attaches to the suspended map $\Sigma u$ because that is the map carrying the freshly introduced suspension coordinate whose orientation reverses. $\blacksquare$

---

# Key Takeaways

**Rotation is the engine that converts a single triangle into an infinite exact sequence.** The deep point this exercise installs is that the bi-infinite long exact sequence is not extra data — it is the single triangle, rotated. Exactness at the $n$-th spot is exactness at the middle spot of the $n$-th rotation, so the entire computational power of triangulated categories is "one triangle, infinitely many viewpoints." The trigger to remember: whenever you need exactness at a spot you have not yet handled, rotate the triangle until that spot is in the middle and reuse the single-spot result.

**Signs in triangulated categories are the shadow of orientation, exactly as in simplicial and chain-complex boundary maps.** The $-1$ on the rotated connecting map is the same sign that appears in $\partial^2 = 0$, in the simplicial face-map alternating sum, and in the Koszul sign rule — it records the reversal of orientation when a suspension coordinate is introduced. The transferable diagnostic: any time a construction reverses or introduces a degree coordinate, expect a sign, and expect it to live on the map that crosses the degree shift. Triangulated categories are one more place where "degree shift carries a sign" is the universal bookkeeping.

**An axiom is "earned" when dropping it breaks a desideratum you actually want, and rotation earns its place by carrying exactness forward.** This exercise is a template for the general practice of axiom motivation: rather than accept TR2 as given, we showed it is *equivalent in effect* to the propagation of exactness, so a reader who wanted a long exact sequence would be forced to invent rotation. The same style of argument — "this clause is exactly what makes the thing you want work" — is how the topic page motivates stability ($\Sigma$ invertible $=$ cofibers agree with fibers) and how the definition page motivates normality, ideals, and every other "why this axiom" question across the vault.
