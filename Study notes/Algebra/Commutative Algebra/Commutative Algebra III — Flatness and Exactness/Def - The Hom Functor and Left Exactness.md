---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module Homomorphism"
  - "Def - Module"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Tensor Product of Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$ and all modules are unital. Let $R$ be a ring and $Q, P, M, N$ be $R$-modules. We write $\operatorname{Hom}_R(Q, P)$ for the set of [[Def - Module Homomorphism|R-linear maps]] $Q \to P$. For an $R$-linear $f : M \to N$:
- $f_* = \operatorname{Hom}_R(Q, f) : \operatorname{Hom}_R(Q, M) \to \operatorname{Hom}_R(Q, N)$, $\varphi \mapsto f \circ \varphi$ (post-composition, **covariant**);
- $f^* = \operatorname{Hom}_R(f, P) : \operatorname{Hom}_R(N, P) \to \operatorname{Hom}_R(M, P)$, $\varphi \mapsto \varphi \circ f$ (pre-composition, **contravariant**, reverses the arrow).

A functor between module categories is **left exact** if it carries $0 \to A \to B \to C$ to $0 \to F(A) \to F(B) \to F(C)$ exact (preserving the leading injection and exactness in the middle), and **right exact** if it carries $A \to B \to C \to 0$ to $F(A) \to F(B) \to F(C) \to 0$ exact. This is a compound page. The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

This is a compound page: it defines three interlocking notions — the **Hom-module** $\operatorname{Hom}_R(Q,P)$, the two **Hom functors** $\operatorname{Hom}_R(Q,-)$ and $\operatorname{Hom}_R(-,P)$, and the property of **left exactness** they share — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

The tensor product was the universal home of *bilinear* maps; $\operatorname{Hom}$ is the home of *linear* maps, and just as we asked how $M \otimes (-)$ treats exact sequences, we must ask the same of $\operatorname{Hom}$. The answer turns out to be the exact mirror image of tensoring, and seeing *why* it is the mirror image — and why that is forced — is the point of the page.

**Why $\operatorname{Hom}_R(Q, P)$ is itself a module.** The set of $R$-linear maps $Q \to P$ is more than a set: maps can be added pointwise, $(f + g)(x) = f(x) + g(x)$, and scaled, $(rf)(x) = r\,f(x)$. One checks $rf$ is again $R$-linear (this uses commutativity of $R$ crucially: $(rf)(sx) = r\,f(sx) = rs\,f(x) = s\,(rf)(x)$, so $rf$ respects scalars only because $rs = sr$). With these operations $\operatorname{Hom}_R(Q, P)$ is an $R$-module, and this is what lets us iterate — to form $\operatorname{Hom}(N, \operatorname{Hom}(M, L))$ — which is exactly the construction the tensor–Hom adjunction needs. Without the module structure on $\operatorname{Hom}$, the adjunction $\operatorname{Hom}(M \otimes N, L) \cong \operatorname{Hom}(N, \operatorname{Hom}(M, L))$ could not even be stated.

**Why two functors, and why one reverses arrows.** Fixing one slot of $\operatorname{Hom}$ and varying the other gives two ways to make a functor. Fix the *source* $Q$ and vary the target: a map $f : M \to N$ should turn maps-into-$M$ into maps-into-$N$, and the only natural way is to *post-compose*, $\varphi \mapsto f \circ \varphi$. This preserves direction — $f : M \to N$ gives $f_* : \operatorname{Hom}(Q, M) \to \operatorname{Hom}(Q, N)$ — so $\operatorname{Hom}(Q, -)$ is **covariant**. Fix the *target* $P$ and vary the source: now $f : M \to N$ should turn maps-out-of-$N$ into maps-out-of-$M$, and the only natural way is to *pre-compose*, $\varphi \mapsto \varphi \circ f$. A map $\varphi : N \to P$ becomes $\varphi \circ f : M \to P$, so $f : M \to N$ gives $f^* : \operatorname{Hom}(N, P) \to \operatorname{Hom}(M, P)$ — the arrow has *reversed*, and $\operatorname{Hom}(-, P)$ is **contravariant**. The arrow-reversal is not a quirk; it is forced by the asymmetry of composition. You can only compose $\varphi : N \to P$ with something landing in $N$, and $f : M \to N$ lands in $N$, so $f$ must go on the *input* side of $\varphi$, flipping the direction.

**Why left exactness, and why it is the mirror of tensor's right exactness.** Now apply the functors to an exact sequence and watch which arrows survive. Take $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ exact (so $f$ injective, $\operatorname{im} f = \ker g$) and apply the covariant $\operatorname{Hom}(Q, -)$. A map $\psi : Q \to A$ is killed by $f_*$ only if $f \circ \psi = 0$, but $f$ is injective so $\psi = 0$: thus $f_*$ is **injective**, the leading $0 \to$ survives. And a map $Q \to B$ landing in $\ker g_* = \{$maps into $\ker g\} = \{$maps into $\operatorname{im} f\}$ factors through $f$ because $f$ is injective onto its image — giving exactness in the middle. What is *not* preserved is the surjection at the back: a map $Q \to C$ need not lift to $Q \to B$ even when $g$ is onto, because lifting requires choosing preimages compatibly, which can fail. So $\operatorname{Hom}(Q, -)$ keeps the *front injection* and may lose the *back surjection* — it is **left exact**. This is the precise mirror of [[Thm - Tensoring is Right Exact|tensoring]], which keeps the *back surjection* and may lose the *front injection*. The contravariant $\operatorname{Hom}(-, P)$ is also left exact, but because it reverses arrows, it converts the *surjection* $B \twoheadrightarrow C$ at the back of $A \to B \to C \to 0$ into an *injection* $0 \to \operatorname{Hom}(C, P) \to \operatorname{Hom}(B, P)$ at the front — left-exactness with the ends swapped by the arrow-reversal.

**Why the failures of left and right exactness are the same phenomenon viewed twice.** The deep reason $\operatorname{Hom}$ is left exact and $\otimes$ is right exact, in lockstep, is the **tensor–Hom adjunction**: $\operatorname{Hom}(M \otimes N, L) \cong \operatorname{Hom}(N, \operatorname{Hom}(M, L))$, natural in all variables, which says $T_M = M \otimes (-)$ and $\operatorname{Hom}(M, -)$ form an adjoint pair with $T_M$ the left adjoint. The general principle — a left adjoint preserves colimits and is right exact, a right adjoint preserves limits and is left exact — explains *both* exactness directions at once and is not a coincidence to be checked twice. This is also why the right-exactness of tensor is *proved* by applying the left-exactness of $\operatorname{Hom}$ and the adjunction: the two facts are one fact, seen through the adjunction from the two sides.

---

# The Definition

Let $R$ be a commutative ring and $Q, P$ be $R$-modules.

## The Hom-module

$\operatorname{Hom}_R(Q, P)$ is the set of all [[Def - Module Homomorphism|R-linear maps]] $Q \to P$, made an $R$-module by
$$(f + g)(x) = f(x) + g(x), \qquad (rf)(x) = r\,f(x) \qquad (r \in R,\ x \in Q).$$
That $rf$ is again $R$-linear uses commutativity of $R$. The zero element is the zero map.

## The covariant Hom functor

For a fixed module $Q$, $\operatorname{Hom}_R(Q, -)$ sends a module $M$ to $\operatorname{Hom}_R(Q, M)$ and an $R$-linear map $f : M \to N$ to
$$f_* = \operatorname{Hom}_R(Q, f) : \operatorname{Hom}_R(Q, M) \to \operatorname{Hom}_R(Q, N), \qquad \varphi \mapsto f \circ \varphi.$$
It is **covariant** (preserves the direction of arrows) and respects identities and composition.

## The contravariant Hom functor

For a fixed module $P$, $\operatorname{Hom}_R(-, P)$ sends a module $M$ to $\operatorname{Hom}_R(M, P)$ and an $R$-linear map $f : M \to N$ to
$$f^* = \operatorname{Hom}_R(f, P) : \operatorname{Hom}_R(N, P) \to \operatorname{Hom}_R(M, P), \qquad \varphi \mapsto \varphi \circ f.$$
It is **contravariant** (reverses the direction of arrows) and satisfies $(g \circ f)^* = f^* \circ g^*$.

## Left exactness

A covariant functor $F$ is **left exact** if every exact $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ yields an exact $0 \to F(A) \to F(B) \to F(C)$. A contravariant functor $G$ is **left exact** if every exact $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ yields an exact $0 \to G(C) \to G(B) \to G(A)$. The full statement that both Hom functors are left exact, with proofs, is [[Thm - Hom is Left Exact]].

---

# Categorical / Structural Definition

The structural fact is the **tensor–Hom adjunction**: for $R$-modules $M, N, L$ there is a natural isomorphism
$$\operatorname{Hom}_R(M \otimes_R N,\, L) \;\cong\; \operatorname{Hom}_R\!\big(N,\, \operatorname{Hom}_R(M, L)\big),$$
sending an $R$-linear $\Phi : M \otimes N \to L$ to $n \mapsto (m \mapsto \Phi(m \otimes n))$. Naturality in $N$ and $L$ says $T_M = M \otimes_R(-)$ is **left adjoint** to $\operatorname{Hom}_R(M, -)$. In category theory an adjunction $F \dashv G$ forces $F$ to preserve colimits (hence to be right exact) and $G$ to preserve limits (hence to be left exact); kernels are limits and cokernels are colimits, so the abstract theorem delivers, in one stroke, both that [[Thm - Tensoring is Right Exact|tensoring is right exact]] and that $\operatorname{Hom}$ is left exact. The covariant $\operatorname{Hom}(Q, -)$ being a right adjoint (its left adjoint is $Q \otimes (-)$) is the reason it is left exact; the contravariant $\operatorname{Hom}(-, P)$ is left exact because it sends colimits to limits. This adjunction is also the engine of the proof of right-exactness of tensor in [[Thm - Tensoring is Right Exact]].

---

# Relate to Other Fields / Compression

The cleanest compression: **$\operatorname{Hom}$ and $\otimes$ are a left/right-exact pair, mirror images forced to agree by adjunction.** Tensoring keeps the surjection at the back of an exact sequence and may lose the injection at the front; $\operatorname{Hom}$ keeps the injection at the front and may lose the surjection at the back. The contravariant $\operatorname{Hom}(-,P)$ additionally flips the ends, turning back-surjections into front-injections.

**True name:** the true name of "left exact" for these functors is operational — **"$\operatorname{Hom}$ sees injections but not surjections."** $\operatorname{Hom}(Q, -)$ turns an injection into an injection (a map into a submodule is determined and stays distinct) but a surjection need not become a surjection (you cannot always lift); $\operatorname{Hom}(-, P)$ turns a surjection into an injection (distinct quotient-maps stay distinct after pulling back) but an injection need not become a surjection (a map out of a submodule need not extend). The whole apparatus of [[Def - Projective Module|projective]] and injective modules exists to name the situations where the missing direction is restored.

The construction is the algebraic core of **duality**. Taking $P = R$ gives the dual module $\operatorname{Hom}_R(M, R) = M^*$, the algebraic analogue of the dual vector space; the contravariance of $\operatorname{Hom}(-, R)$ is exactly why dualizing reverses arrows, and the failure of left-exactness to be exactness is why $M \to M^{**}$ need not be an isomorphism. In topology and geometry the same contravariance appears as the reason cohomology is contravariant while homology is covariant — cohomology is built from $\operatorname{Hom}(-, A)$, homology from $(-) \otimes A$, and they inherit the left/right-exact mirror structure of this page.

---

# Examples / Corollaries

**Is an instance (left exact) — $\operatorname{Hom}(\mathbb{Z}, -)$.** For $Q = \mathbb{Z}$ over $R = \mathbb{Z}$, $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}, M) \cong M$ naturally ($\varphi \mapsto \varphi(1)$), so $\operatorname{Hom}(\mathbb{Z}, -)$ is the identity functor — trivially exact, hence left exact. More generally $\operatorname{Hom}(R, M) \cong M$ and $\operatorname{Hom}(R^n, M) \cong M^n$: the Hom functor out of a free module is just taking coordinates.

**Is an instance — left exactness failing to be exactness.** Apply the covariant $\operatorname{Hom}(\mathbb{Z}/2, -)$ to the surjection $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$. We get $\operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}) \to \operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}) \to \operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}/2)$. Now $\operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}) = 0$ (no non-zero map from a torsion group to a torsion-free one) while $\operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2 \neq 0$, so the map on the right is not surjective: the back surjection was *not* preserved. This is left-exactness in action — the front is fine, the back is lost.

**Is an instance (contravariant, ends swapped) — $\operatorname{Hom}(-, \mathbb{Z})$.** Apply the contravariant $\operatorname{Hom}(-, \mathbb{Z})$ to $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$. The surjection $\mathbb{Z} \to \mathbb{Z}/2$ at the *back* becomes an injection $0 \to \operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}) \to \operatorname{Hom}(\mathbb{Z}, \mathbb{Z})$ at the *front* — and indeed $\operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}) = 0$ injects into $\operatorname{Hom}(\mathbb{Z}, \mathbb{Z}) = \mathbb{Z}$. The arrow-reversal moved the preserved injection to the other end.

**Is NOT an instance (right exactness) — $\operatorname{Hom}$ is not right exact.** The previous examples already show it: $\operatorname{Hom}(\mathbb{Z}/2, -)$ does not preserve the surjection $\mathbb{Z} \twoheadrightarrow \mathbb{Z}/2$. So neither Hom functor is right exact in general; right-exactness of $\operatorname{Hom}(M,-)$ is *exactly* [[Def - Projective Module|projectivity]] of $M$, and right-exactness of the contravariant $\operatorname{Hom}(-, P)$ is injectivity of $P$.

**Corollary — $\operatorname{Hom}$ converts finite direct sums to products in each variable.** $\operatorname{Hom}(\bigoplus_i Q_i, P) \cong \prod_i \operatorname{Hom}(Q_i, P)$ and $\operatorname{Hom}(Q, \prod_i P_i) \cong \prod_i \operatorname{Hom}(Q, P_i)$. The first uses that a map out of a direct sum is determined by its restrictions; this is the limit-preservation a right adjoint must have.

**Calibration check.** Verify $\operatorname{Hom}(R^n, M) \cong M^n$ and use it to confirm $\operatorname{Hom}(R, -)$ is exact (free source $\Rightarrow$ projective $\Rightarrow$ $\operatorname{Hom}$ exact). Check that $\operatorname{Hom}(\mathbb{Z}/2, -)$ fails to preserve the surjection $\mathbb{Z} \twoheadrightarrow \mathbb{Z}/2$, isolating *which* end of exactness left-exactness drops. Finally, trace through how the contravariant functor's arrow-reversal turns a back-surjection into a front-injection on the example $\mathbb{Z} \xrightarrow{\times 2}\mathbb{Z} \to \mathbb{Z}/2 \to 0$.

---

# Unlocked by This

> [!tip] Projective and injective modules *(from Homological Algebra)*
> $\operatorname{Hom}(M, -)$ is left exact always; it is *fully* exact exactly when $M$ is **[[Def - Projective Module|projective]]**, and the contravariant $\operatorname{Hom}(-, P)$ is fully exact exactly when $P$ is **injective**. These two classes are the building blocks of projective and injective resolutions, from which the derived functors $\operatorname{Ext}^n$ are computed — the systematic measurement of how far $\operatorname{Hom}$ is from exact.

> [!tip] Ext and the tensor–Hom adjunction *(from Homological Algebra)*
> Deriving the left-exact $\operatorname{Hom}$ produces $\operatorname{Ext}^n_R(M, N)$, the mirror of the $\operatorname{Tor}_n$ that derive the right-exact tensor. The adjunction $\operatorname{Hom}(M \otimes N, L) \cong \operatorname{Hom}(N, \operatorname{Hom}(M, L))$ persists to a spectral relationship between $\operatorname{Tor}$ and $\operatorname{Ext}$, the structural reason flatness and projectivity (the acyclicity conditions for the two functors) are dual notions.

> [!tip] Cohomology is contravariant *(from Algebraic Topology)*
> The arrow-reversal of $\operatorname{Hom}(-, A)$ is the source of the contravariance of **cohomology**: cochains are $\operatorname{Hom}(\text{chains}, A)$, so a map of spaces induces a *backward* map on cohomology, while homology (built from $(-) \otimes A$) stays covariant. The universal coefficient theorem is exactly the failure of these functors to be fully exact, measured by $\operatorname{Ext}$ and $\operatorname{Tor}$.
