---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Ring Homomorphism"
  - "Def - Tensor Product of Modules"
  - "Def - Restriction and Extension of Scalars"
  - "Thm - Universal Property of the Tensor Product of Modules"
  - "Thm - Standard Isomorphisms of Tensor Products"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; ring homomorphisms send $1\mapsto 1$. Fix a ring homomorphism $f : R\to S$. Let $M, M'$ be [[Def - Module|S-modules]] and $N, N', \{N_i\}_{i\in I}$ be $R$-modules. We write $S\otimes_R N$ for the [[Def - Restriction and Extension of Scalars|extension of scalars]], $M\otimes_R N$ for the $R$-tensor with its $S$-action $s(m\otimes n) = (sm)\otimes n$, and $\operatorname{Hom}_S, \operatorname{Hom}_R$ for $S$- and $R$-linear maps. The full registry is on [[Commutative Algebra II — Tensor Products]].

---

# Statement

> **Theorem (Extension of scalars: factorisation, isomorphisms, adjunction).** Let $f : R\to S$ be a ring homomorphism, $M, M'$ be $S$-modules, $N, N'$ be $R$-modules.
>
> 1. **(Two-step factorisation.)** There is an $S$-module isomorphism
> $$M\otimes_R N\ \cong\ M\otimes_S(S\otimes_R N), \qquad m\otimes n\mapsto m\otimes(1\otimes n),\quad (sm)\otimes n\mapsfrom m\otimes(s\otimes n).$$
> 2. **(Standard isomorphisms over $S$.)** As $S$-modules: $M\otimes_R N\cong N\otimes_R M$; $(M\otimes_R N)\otimes_R N'\cong M\otimes_R(N\otimes_R N')$; $(M\otimes_R N)\otimes_S M'\cong M\otimes_S(N\otimes_R M')$; and $M\otimes_R\big(\bigoplus_i N_i\big)\cong\bigoplus_i(M\otimes_R N_i)$.
> 3. **(Base-change identity.)** $S\otimes_R(N\otimes_R N')\cong(S\otimes_R N)\otimes_S(S\otimes_R N')$ as $S$-modules, $s\otimes(n\otimes n')\mapsto s\big((1\otimes n)\otimes(1\otimes n')\big)$.
> 4. **(Adjunction.)** Extension of scalars is left adjoint to restriction: for an $R$-module $N$ and an $S$-module $M$,
> $$\operatorname{Hom}_S(S\otimes_R N,\ M)\ \cong\ \operatorname{Hom}_R(N,\ M)\qquad\text{naturally},$$
> where on the right $M$ is restricted to an $R$-module.

> **Corollary (algebra form and concrete cases).** For an $R$-algebra $A$ and an $S$-algebra $B$, $A\otimes_R B\cong(A\otimes_R S)\otimes_S B$ as $S$-algebras, and $S\otimes_R R[T_1,\dots,T_n]\cong S[T_1,\dots,T_n]$ via $s\otimes p\mapsto s\tilde f(p)$ (apply $f$ to coefficients). For a free module, $S\otimes_R R^n\cong S^n$; and $\operatorname{id}_S\otimes T$ has the same matrix as $T : R^n\to R^m$.

---

# Motivation

Extension of scalars along $f : R\to S$ — sending the $R$-module $N$ to the $S$-module $S\otimes_R N$ — is the algebra of *base change*: complexifying a real vector space, reducing a $\mathbb{Z}$-module mod $p$, viewing a variety over a larger field. But the general construction $M\otimes_R N$, where $M$ is an $S$-module and we want the result as an $S$-module, can be unwieldy: it mixes the two rings $R$ and $S$ in one tensor. This theorem's first part is the simplification that makes everything tractable: **a complicated extension factors into a *simple* one followed by an ordinary $S$-tensor.** You prepare $N$ once by the simple extension $S\otimes_R N$ — which for a free module just replaces $R^n$ by $S^n$ — and thereafter work entirely over $S$, where the familiar [[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]] apply.

The concrete force of this is visible in the running example. To understand $\mathbb{C}^n\otimes_{\mathbb{R}}\mathbb{R}^\ell$ as a $\mathbb{C}$-module, you could guess and verify; or you factor: $\mathbb{C}^n\otimes_{\mathbb{R}}\mathbb{R}^\ell\cong\mathbb{C}^n\otimes_{\mathbb{C}}(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^\ell)\cong\mathbb{C}^n\otimes_{\mathbb{C}}\mathbb{C}^\ell\cong\mathbb{C}^{n\ell}$, each step mechanical. The factorisation turns base change into a routine.

The deepest content is part 4, the **adjunction** $\operatorname{Hom}_S(S\otimes_R N, M)\cong\operatorname{Hom}_R(N, M)$: extension of scalars is the *left adjoint* of restriction. This says $S\otimes_R N$ is the *universal* (free) $S$-module on the $R$-module $N$ — an $S$-linear map out of it is exactly an $R$-linear map out of $N$. Adjunction is why extension behaves predictably: it preserves direct sums and cokernels (left adjoints preserve colimits), it commutes with base change, and it is the algebraic skeleton of the pullback–pushforward adjunction $f^*\dashv f_*$ that runs through all of geometry. The whole apparatus of base change is coherent *because* of this one adjunction.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "I have a tensor mixing two rings $R$ and $S$, or a base-change computation".

The first disguised source is **an $S$-module structure wanted on an $R$-tensor**. The property $B$ is "I have $M\otimes_R N$ with $M$ an $S$-module and want to understand it over $S$". The bridge is part 1: factor as $M\otimes_S(S\otimes_R N)$, reducing to a single simple extension plus an $S$-tensor. *Example problem:* $\mathbb{C}^n\otimes_{\mathbb{R}}\mathbb{R}^\ell\cong\mathbb{C}^{n\ell}$ as a $\mathbb{C}$-module. See [[Ex - Extension of scalars of a free module]].

The second disguised source is **a free or quotient $R$-module to base-change**. The property $B$ is "$N = R^n$ or $N = R/I$ or $N = M$ over $R$". The bridge: $S\otimes_R R^n\cong S^n$ (distributivity + $S\otimes_R R\cong S$), and $S\otimes_R R/I\cong S/IS$ (quotient rule), and $R/I\otimes_R M\cong M/IM$. *Example problem:* reduction mod $n$ as $(\mathbb{Z}/n)\otimes_{\mathbb{Z}}\mathbb{Z}^k\cong(\mathbb{Z}/n)^k$. See [[Ex - Tensoring with R over I gives M over IM]].

The third disguised source is **an $S$-linear map to be defined out of $S\otimes_R N$**. The property $B$ is "I want a map $S\otimes_R N\to M$ for an $S$-module $M$". The bridge is the adjunction (part 4): such a map is *the same data* as an $R$-linear map $N\to M$, so define the easier $R$-linear map and let the adjunction extend it. *Example problem:* the counit $S\otimes_R M\to M$, $s\otimes m\mapsto sm$, comes from $\operatorname{id}_M : M\to M$ viewed $R$-linearly.

**Targets (Output Amplification)**

The conclusions are the factorisation, the $S$-isomorphisms, and the adjunction.

Combine the **factorisation** with **a free module**. $S\otimes_R R^n\cong S^n$ keeps the basis $\{1\otimes e_i\}$ and the matrices, so $\operatorname{id}_S\otimes T$ has the *same matrix* as $T$. The result $E$ is that complexification (or any base change) of a linear map is "read the matrix over the new ring" — the matrix is a base-change invariant. Nonobvious because the abstract extension turns out to do nothing to the bookkeeping, only to the scalars the entries live in.

Combine the **adjunction** with **left adjoints preserve colimits**. Since extension is a left adjoint, it preserves direct sums and cokernels (right exactness), so it commutes with quotients and finite presentations. The result $E$ is that base change is *right exact*, and it is *exact* exactly when $f$ is flat. Nonobvious because exactness of base change — crucial for everything in [[Commutative Algebra III — Flatness and Exactness]] — is a formal consequence of the adjunction plus flatness.

Combine the **base-change identity** (part 3) with **iteration**. Repeatedly applying $S\otimes_R(N_1\otimes\cdots\otimes N_\ell)\cong(S\otimes_R N_1)\otimes_S\cdots\otimes_S(S\otimes_R N_\ell)$ shows base change is *monoidal* — it commutes with the whole tensor structure. The result $E$ is that base-changing a tensor product of modules is the $S$-tensor of the base changes, the algebraic reason pullback of sheaves is monoidal. Nonobvious because it requires the simple extension to distribute over $\otimes$, which fails for a general $S$-module $M$ in place of $S$ (the corollary's caveat $\mathbb{C}^n\otimes_{\mathbb{R}}(-)$ is not monoidal).

---

# Why Is It True

Everything rests on part 1, the two-step factorisation, and part 1 is the universal property used to build $S$-linear maps both ways. **The one idea: $S\otimes_R N$ is "$N$ with $S$-scalars freely adjoined", so tensoring an $S$-module $M$ with $N$ over $R$ is the same as first adjoining the $S$-scalars to $N$, then tensoring over $S$ — the $S$-scalars only need to be added once.**

*Forward map.* The map $M\times N\to M\otimes_S(S\otimes_R N)$, $(m,n)\mapsto m\otimes(1\otimes n)$, is $R$-bilinear, so induces an $R$-linear $\varphi : M\otimes_R N\to M\otimes_S(S\otimes_R N)$ with $\varphi(m\otimes n) = m\otimes(1\otimes n)$. It is in fact $S$-linear: $\varphi(s(m\otimes n)) = \varphi((sm)\otimes n) = (sm)\otimes(1\otimes n) = s(m\otimes(1\otimes n)) = s\varphi(m\otimes n)$, using the $S$-action on the first factor.

*Backward map.* This is the delicate direction and is built in stages. Fix $m\in M$: the map $S\times N\to M\otimes_R N$, $(s,n)\mapsto(sm)\otimes n$, is $R$-bilinear, inducing $H_m : S\otimes_R N\to M\otimes_R N$ with $H_m(s\otimes n) = (sm)\otimes n$. Now unfix $m$: the map $M\times(S\otimes_R N)\to M\otimes_R N$, $(m, x)\mapsto H_m(x)$, is $S$-bilinear, so induces an $S$-linear $\psi : M\otimes_S(S\otimes_R N)\to M\otimes_R N$ with $\psi(m\otimes(s\otimes n)) = (sm)\otimes n$.

*Inverse check.* On pure tensors: $\psi\varphi(m\otimes n) = \psi(m\otimes(1\otimes n)) = (1\cdot m)\otimes n = m\otimes n$, and $\varphi\psi(m\otimes(s\otimes n)) = \varphi((sm)\otimes n) = (sm)\otimes(1\otimes n) = m\otimes(s\otimes n)$ (sliding $s$ across the inner $\otimes$). Generators are fixed, so $\varphi, \psi$ are mutually inverse $S$-isomorphisms.

**Part 2** follows by combining part 1 with the [[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]] over $S$ (associativity, distributivity, commutativity now applied to $S$-tensors), as in Becker's proof of (3): $(M\otimes_R N)\otimes_S M'\cong(M\otimes_S(S\otimes_R N))\otimes_S M'\cong M\otimes_S((S\otimes_R N)\otimes_S M')\cong M\otimes_S(N\otimes_R M')$ — the last step is part 1 in reverse applied to $M'$.

**Part 3** combines part 2(2) ($(S\otimes_R N)\otimes_R N'\cong S\otimes_R(N\otimes_R N')$) with part 1 ($(S\otimes_R N)\otimes_R N'\cong(S\otimes_R N)\otimes_S(S\otimes_R N')$): chaining gives $S\otimes_R(N\otimes_R N')\cong(S\otimes_R N)\otimes_S(S\otimes_R N')$.

**Part 4, the adjunction.** An $R$-bilinear map $S\times N\to M$ that is "$S$-linear in the first slot" is the same as an $R$-linear map $N\to M$ (restrict to $1\times N$, recover by $s$-action); spelled out via the universal property, an $S$-linear $S\otimes_R N\to M$ restricts along $n\mapsto 1\otimes n$ to an $R$-linear $N\to M$, and this is a natural bijection with inverse "extend $S$-linearly". This is the unit/counit description: unit $N\to S\otimes_R N$, $n\mapsto 1\otimes n$; counit $S\otimes_R M\to M$, $s\otimes m\mapsto sm$.

**The corollary.** $S\otimes_R R^n\cong\bigoplus_1^n(S\otimes_R R)\cong S^n$ by distributivity and $S\otimes_R R\cong S$; the basis $1\otimes e_i$ maps to the standard basis, and $\operatorname{id}_S\otimes T$ sends $1\otimes e_i\mapsto 1\otimes Te_i = \sum_\ell[T]_{\ell i}(1\otimes f_\ell)$, so its matrix is $[T]$ over $S$. The algebra form is part 1 with $M = A$, $N = B$ in the algebra category, upgraded via the upgrading lemma.

---

# What Makes This Hard

The technically delicate point is the *backward map* in part 1: it must be built in two stages — first $H_m : S\otimes_R N\to M\otimes_R N$ for fixed $m$, then assemble over $m$ into an *$S$-bilinear* map $M\times(S\otimes_R N)\to M\otimes_R N$ — and verifying the $S$-bilinearity (not just $R$-bilinearity) of the second stage is the step most people botch. The conceptual hurdle is part 4: seeing "an $S$-linear map out of the extension = an $R$-linear map out of $N$" as an *adjunction*, and recognising that this is *why* extension preserves colimits. The common error is to expect the base-change identity (part 3) to hold for a general $S$-module $M$ in place of $S$ — it does not; $\mathbb{C}^n\otimes_{\mathbb{R}}(N\otimes_R N')\not\cong(\mathbb{C}^n\otimes_R N)\otimes_{\mathbb{C}}(\mathbb{C}^n\otimes_R N')$ (dimensions $n\cdot mℓ$ versus $n^2 mℓ$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove part 1 by building $S$-linear maps both ways via universal properties — the forward map directly, the backward map in two stages (fix $m$, then assemble $S$-bilinearly) — and checking inverses on pure tensors. Get parts 2–3 by chaining part 1 with the standard $S$-isomorphisms. Get part 4 by restricting an $S$-linear map along $n\mapsto 1\otimes n$ and extending back. Derive the corollary from distributivity + $S\otimes_R R\cong S$.

**Subgoal decomposition:**

1. **Forward map of part 1.** Build $S$-linear $\varphi : M\otimes_R N\to M\otimes_S(S\otimes_R N)$.
   - *Hint:* $(m,n)\mapsto m\otimes(1\otimes n)$ is $R$-bilinear; check $S$-linearity via the action on the first factor.
   - *Why needed:* It is one direction of the key isomorphism.

2. **Backward map of part 1.** Build $S$-linear $\psi$ in two stages.
   - *Hint:* Fix $m$ to get $H_m : S\otimes_R N\to M\otimes_R N$; then $(m, x)\mapsto H_m(x)$ is $S$-bilinear.
   - *Why needed:* It is the inverse; the $S$-bilinearity is the delicate point.

3. **Inverses.** Check $\psi\varphi$, $\varphi\psi$ fix pure tensors.
   - *Hint:* Slide $s$ across the inner $\otimes$ to match $m\otimes(s\otimes n) = (sm)\otimes(1\otimes n)$.
   - *Why needed:* It completes part 1.

4. **Parts 2–3.** Chain part 1 with the standard $S$-isomorphisms.
   - *Hint:* Replace each $\otimes_R$-into-$S$ by a simple extension, then use associativity/distributivity over $S$.
   - *Why needed:* They are the catalogue of base-change isomorphisms.

5. **Adjunction (part 4) and corollary.** Restrict-and-extend; then $S\otimes_R R^n\cong S^n$.
   - *Hint:* An $S$-map out of $S\otimes_R N$ restricts along $n\mapsto 1\otimes n$ to an $R$-map; distributivity gives the free case.
   - *Why needed:* Part 4 is the structural heart; the corollary is the concrete payoff.

---

# Lemma Decomposition

> [!note]- Lemma 1: The forward map is $S$-linear
> **Statement:** $(m,n)\mapsto m\otimes(1\otimes n)$ induces an $S$-linear $\varphi : M\otimes_R N\to M\otimes_S(S\otimes_R N)$.
>
> **Hint:** It is $R$-bilinear by construction; for $S$-linearity use the $S$-action $s(m\otimes n) = (sm)\otimes n$.
>
> **Why needed:** It is one half of the two-step factorisation, on which all of parts 2–3 depend.
>
> > [!note]- Full proof
> > The map $b(m,n) = m\otimes(1\otimes n)$ is $R$-bilinear: additive in each slot and $b(rm, n) = (rm)\otimes(1\otimes n) = r(m\otimes(1\otimes n)) = m\otimes(1\otimes rn) = b(m, rn)$ (the inner $1\otimes rn = r(1\otimes n)$ slides $r\in R$ via $f$). By the [[Thm - Universal Property of the Tensor Product of Modules|module universal property]], $b$ induces $R$-linear $\varphi$ with $\varphi(m\otimes n) = m\otimes(1\otimes n)$. It is $S$-linear: $\varphi(s(m\otimes n)) = \varphi((sm)\otimes n) = (sm)\otimes(1\otimes n) = s(m\otimes(1\otimes n)) = s\varphi(m\otimes n)$, where the $S$-action sits on the first factor on both sides.

> [!note]- Lemma 2: The backward map exists and is $S$-linear
> **Statement:** There is an $S$-linear $\psi : M\otimes_S(S\otimes_R N)\to M\otimes_R N$ with $\psi(m\otimes(s\otimes n)) = (sm)\otimes n$.
>
> **Hint:** Build $H_m : S\otimes_R N\to M\otimes_R N$ for fixed $m$, then assemble $(m,x)\mapsto H_m(x)$, which is $S$-bilinear.
>
> **Why needed:** It is the inverse of $\varphi$; the two-stage construction and the $S$-bilinearity are the crux.
>
> > [!note]- Full proof
> > **Stage 1.** Fix $m\in M$. The map $S\times N\to M\otimes_R N$, $(s,n)\mapsto(sm)\otimes n$, is $R$-bilinear (in $s$: $((s+s')m)\otimes n = (sm)\otimes n + (s'm)\otimes n$ and $((rs)m)\otimes n = r((sm)\otimes n)$; in $n$: clear). By the universal property of $S\otimes_R N$ it induces $R$-linear $H_m : S\otimes_R N\to M\otimes_R N$ with $H_m(s\otimes n) = (sm)\otimes n$.
> >
> > **Stage 2.** The map $M\times(S\otimes_R N)\to M\otimes_R N$, $(m, x)\mapsto H_m(x)$, is $S$-bilinear: additive in $m$ (since $H_{m+m'} = H_m + H_{m'}$ on pure tensors, hence everywhere) and $S$-homogeneous in $m$ ($H_{sm}(s'\otimes n) = (ss'm)\otimes n = s((s'm)\otimes n) = s H_m(s'\otimes n)$); and $S$-linear in $x$ since each $H_m$ is additive and $H_m(s\cdot(s'\otimes n)) = H_m((ss')\otimes n) = (ss'm)\otimes n = s H_m(s'\otimes n)$. By the universal property of $M\otimes_S(S\otimes_R N)$ this induces $S$-linear $\psi$ with $\psi(m\otimes(s\otimes n)) = H_m(s\otimes n) = (sm)\otimes n$.

> [!note]- Lemma 3: $\varphi$ and $\psi$ are mutually inverse
> **Statement:** $\psi\varphi = \operatorname{id}_{M\otimes_R N}$ and $\varphi\psi = \operatorname{id}_{M\otimes_S(S\otimes_R N)}$.
>
> **Hint:** Check on pure tensors, sliding $s$ across the inner $\otimes$ so that $m\otimes(s\otimes n) = (sm)\otimes(1\otimes n)$.
>
> **Why needed:** It completes the two-step factorisation (part 1).
>
> > [!note]- Full proof
> > $\psi\varphi(m\otimes n) = \psi(m\otimes(1\otimes n)) = (1\cdot m)\otimes n = m\otimes n$; pure tensors generate $M\otimes_R N$, so $\psi\varphi = \operatorname{id}$.
> >
> > For the other composite, take a pure tensor $m\otimes\big(\sum_i s_i\otimes n_i\big)$. Then $\psi(m\otimes(\sum_i s_i\otimes n_i)) = \sum_i(s_i m)\otimes n_i$, and $\varphi(\sum_i(s_i m)\otimes n_i) = \sum_i(s_i m)\otimes(1\otimes n_i) = \sum_i m\otimes(s_i\otimes n_i) = m\otimes(\sum_i s_i\otimes n_i)$, using $(s_i m)\otimes(1\otimes n_i) = m\otimes(s_i\otimes n_i)$ ($S$-action slides $s_i$ onto the inner factor). Such tensors generate, so $\varphi\psi = \operatorname{id}$.

> [!note]- Lemma 4: The adjunction
> **Statement:** $\operatorname{Hom}_S(S\otimes_R N, M)\cong\operatorname{Hom}_R(N, M)$ naturally, by $\Phi\mapsto(n\mapsto\Phi(1\otimes n))$ with inverse $\theta\mapsto(s\otimes n\mapsto s\theta(n))$.
>
> **Hint:** Restrict an $S$-map along the unit $n\mapsto 1\otimes n$; extend an $R$-map $S$-linearly.
>
> **Why needed:** It exhibits extension as left adjoint to restriction — the structural heart and the source of right-exactness.
>
> > [!note]- Full proof
> > Given $S$-linear $\Phi : S\otimes_R N\to M$, define $\theta = \Phi\circ(n\mapsto 1\otimes n) : N\to M$, which is $R$-linear ($\theta(rn) = \Phi(1\otimes rn) = \Phi(r(1\otimes n)) = \Phi(f(r)(1\otimes n))$... more directly, $1\otimes rn = r\cdot(1\otimes n)$ as $R$-action, and $\Phi$ is $R$-linear by restriction, so $\theta(rn) = r\theta(n)$). Conversely, given $R$-linear $\theta : N\to M$, the map $S\times N\to M$, $(s,n)\mapsto s\theta(n)$, is $R$-bilinear, inducing $R$-linear $\Phi : S\otimes_R N\to M$ with $\Phi(s\otimes n) = s\theta(n)$; $\Phi$ is $S$-linear since $\Phi(s'(s\otimes n)) = \Phi((s's)\otimes n) = s's\theta(n) = s'\Phi(s\otimes n)$. These assignments are mutually inverse: $\Phi(1\otimes n) = 1\cdot\theta(n) = \theta(n)$, and $(s\otimes n\mapsto s\Phi(1\otimes n)) = (s\otimes n\mapsto\Phi(s\otimes n)) = \Phi$ on generators. Naturality in $N$ and $M$ is routine.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1.** **Lemma 1** gives $S$-linear $\varphi$, **Lemma 2** gives $S$-linear $\psi$, **Lemma 3** shows them mutually inverse; hence $M\otimes_R N\cong M\otimes_S(S\otimes_R N)$ as $S$-modules.
>
> **Part 2.** (1) and (2) are the module [[Thm - Standard Isomorphisms of Tensor Products|standard isomorphisms]] read as $S$-module statements (the $S$-action sits on the $S$-module factor and is respected by each isomorphism). For (3), using part 1 and associativity of $\otimes_S$:
> $$(M\otimes_R N)\otimes_S M'\cong\big(M\otimes_S(S\otimes_R N)\big)\otimes_S M'\cong M\otimes_S\big((S\otimes_R N)\otimes_S M'\big)\cong M\otimes_S(N\otimes_R M'),$$
> the last step being part 1 applied to $M'$ (with $N$ and $M'$ swapping roles). (4) is distributivity over direct sums.
>
> **Part 3.** By part 2(2), $(S\otimes_R N)\otimes_R N'\cong S\otimes_R(N\otimes_R N')$; by part 1, $(S\otimes_R N)\otimes_R N'\cong(S\otimes_R N)\otimes_S(S\otimes_R N')$. Chaining, $S\otimes_R(N\otimes_R N')\cong(S\otimes_R N)\otimes_S(S\otimes_R N')$, with the stated effect on pure tensors.
>
> **Part 4.** This is **Lemma 4**.
>
> ---
> **Corollary.** $S\otimes_R R^n\cong\bigoplus_1^n(S\otimes_R R)\cong S^n$ (distributivity, then $S\otimes_R R\cong S$, $s\otimes r\mapsto sr$), with $S$-basis $\{1\otimes e_i\}$. For $T : R^n\to R^m$, $(\operatorname{id}_S\otimes T)(1\otimes e_i) = 1\otimes Te_i = \sum_\ell[T]_{\ell i}(1\otimes f_\ell)$, so $\operatorname{id}_S\otimes T$ has matrix $[T]$ over $S$. The algebra isomorphism $A\otimes_R B\cong(A\otimes_R S)\otimes_S B$ is part 1 in the algebra category (upgrade by the upgrading lemma), and $S\otimes_R R[T_*]\cong S[T_*]$ via $s\otimes p\mapsto s\tilde f(p)$ is its instance with $A = R[T_*]$, $B = S$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complexification of a real representation (representation theory).** For a real representation $\rho : G\to\operatorname{GL}(V)$, the complexification $\mathbb{C}\otimes_{\mathbb{R}}V$ is the extension of scalars along $\mathbb{R}\hookrightarrow\mathbb{C}$, and $\operatorname{id}_{\mathbb{C}}\otimes\rho(g)$ has the same matrices — so character computations transfer verbatim. The adjunction is Frobenius reciprocity in the field-extension case. Nonobvious because base-changing the representation does nothing to the matrices, only to the field. See [[Ex - Extension of scalars of a free module]].

**Reduction of a variety modulo $p$ (number theory / arithmetic geometry).** Base-changing an arithmetic scheme over $\mathbb{Z}$ along $\mathbb{Z}\to\mathbb{F}_p$ is extension of scalars $\mathbb{F}_p\otimes_{\mathbb{Z}}(-)$; the two-step factorisation and the right-exactness from the adjunction control how generators and relations reduce. Nonobvious because the geometry over $\mathbb{F}_p$ is computed by the *same* algebra, with coefficients reduced.

**Frobenius reciprocity for induced representations (representation theory).** For $H\leq G$, induction $\operatorname{Ind}_H^G = k[G]\otimes_{k[H]}(-)$ is extension of scalars along $k[H]\to k[G]$, and the adjunction $\operatorname{Hom}_G(\operatorname{Ind}V, W)\cong\operatorname{Hom}_H(V, \operatorname{Res}W)$ *is* part 4 of this theorem. Nonobvious because the cornerstone of character theory is literally the extension–restriction adjunction in disguise.

---

# Bridges

- **[[Def - Restriction and Extension of Scalars|Restriction and Extension of Scalars]]** — this theorem is the operational content of that definition: part 1 makes extension computable, and part 4 is the adjunction that the definition's "compound" framing anticipates. Extension is the left adjoint $f^*$, restriction the right adjoint $f_*$.

- **[[Thm - Standard Isomorphisms of Tensor Products|Standard Isomorphisms]]** — parts 2 and 3 are the standard isomorphisms transported to the base-change setting; the proofs *are* the standard isomorphisms over $S$ chained with the two-step factorisation. The free case $S\otimes_R R^n\cong S^n$ is the identity and distributivity laws.

- **[[Ex - Tensoring with R over I gives M over IM|R/I⊗ᵣM≅M/IM]]** — the simplest instance of extension, along $R\to R/I$: $S\otimes_R N$ with $S = R/I$, $N = M$ gives $(R/I)\otimes_R M\cong M/IM$. The adjunction here is the universal property of the quotient module.

- **Flat base change** — because extension is a left adjoint (part 4), it is right exact; it is *exact* precisely when $f : R\to S$ is **flat**, and then base change preserves exact sequences, kernels, and finite limits. This is the homological backbone of [[Commutative Algebra III — Flatness and Exactness]] and of localization (where $R\to S^{-1}R$ is flat), tying the adjunction to the exactness theory.

---

# Unlocked by This

> [!tip] Pullback–pushforward adjunction for sheaves *(from Algebraic Geometry)*
> Along a map of spaces $\mathbf{Spec}\,S\to\mathbf{Spec}\,R$, extension of scalars is the **pullback** $f^*$ and restriction the **pushforward** $f_*$ of quasi-coherent sheaves; part 4 is the adjunction $f^*\dashv f_*$ that organises sheaf cohomology, base-change theorems, and the projection formula. The two-step factorisation is the statement that pullback is computed fibrewise, and the base-change identity (part 3) is the monoidality of $f^*$ — pullback commutes with tensor products of sheaves.

> [!tip] Frobenius reciprocity and induced representations *(from Representation Theory)*
> Induction of representations along $H\leq G$ is extension of scalars $k[G]\otimes_{k[H]}(-)$, and part 4 specialises to **Frobenius reciprocity** $\operatorname{Hom}_G(\operatorname{Ind}_H^G V, W)\cong\operatorname{Hom}_H(V, \operatorname{Res}^G_H W)$ — the adjunction between induction and restriction at the heart of character theory and the theory of induced representations.

> [!tip] Flat and faithfully flat descent *(from Commutative Algebra)*
> When $f : R\to S$ is flat, the right-exact extension functor becomes exact, so base change preserves all finite limits — the property that makes localization, completion, and smooth/étale morphisms well-behaved. When $f$ is **faithfully flat**, descent theory reconstructs $R$-modules from their base changes plus gluing data. Flatness is developed in [[Commutative Algebra III — Flatness and Exactness]].
