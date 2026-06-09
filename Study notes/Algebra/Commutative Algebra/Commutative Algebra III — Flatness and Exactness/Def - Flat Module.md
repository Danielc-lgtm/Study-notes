---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Tensor Product of Modules"
  - "Def - Module Homomorphism"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Free Module"
  - "Thm - Tensoring is Right Exact"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$ and all modules are unital. Let $R$ be a ring and $M$ an [[Def - Module|$R$-module]]. For an $R$-linear map $f : N \to N'$ we write $\operatorname{id}_M \otimes f : M \otimes_R N \to M \otimes_R N'$ for the induced map on [[Def - Tensor Product of Modules|tensor products]], characterised on pure tensors by $(\operatorname{id}_M \otimes f)(m \otimes n) = m \otimes f(n)$. We write $T_M = M \otimes_R (-)$ for the tensor-with-$M$ functor, $\mu_r : R \to R$ for multiplication by an element $r \in R$, and $R^{\oplus I}$ for the [[Def - Free Module|free module]] on an index set $I$. An element $r \in R$ is a **zero-divisor** if $rs = 0$ for some $s \neq 0$, and a **non-zero-divisor** otherwise. The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

---

# Axiom Motivation

The starting observation is a disappointment, and the definition is the cure. We have a perfectly good functor, $T_M = M \otimes_R (-)$, and we have just learned ([[Thm - Tensoring is Right Exact|right-exactness]]) that it respects half of the structure that organises module theory. Given an exact $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ — a surjection $g$ with $\operatorname{im} f = \ker g$ — tensoring keeps it exact: $M \otimes A \to M \otimes B \to M \otimes C \to 0$ is still exact, the surjection survives, the cokernel is computed correctly. But the *other* half — injectivity — is not respected. The single example that ruins it is small and unforgettable: the map $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$ is injective, yet tensoring with $\mathbb{Z}/2$ turns it into $\mathbb{Z}/2 \xrightarrow{\times 2} \mathbb{Z}/2$, which sends every element to $0$. An honest embedding has become the zero map. So $T_M$ can take an injection to a non-injection, and *that specific failure* is the only thing standing between $T_M$ and full exactness.

The definition is now reverse-engineered from the desire to forbid exactly this failure. **Call $M$ flat when $T_M$ never breaks an injection** — when $\operatorname{id}_M \otimes f$ is injective for every injective $f$. This is the minimal demand that buys back the missing left-exactness: since $T_M$ is already right exact, a module that also preserves injections preserves *all* exactness, so flat modules are precisely those for which tensoring is a fully exact functor. The definition could not be weaker without failing to do its job, and it need not be stronger.

**Why phrase it as "preserves injections" rather than "preserves short exact sequences"?** These turn out to be equivalent ([[Thm - Characterization of Flat Modules|the characterization theorem]]), but the injection form is the right *primitive* because it isolates the one thing that can go wrong. Right-exactness already guarantees the right two-thirds of any short exact sequence $0 \to N' \to N \to N'' \to 0$ survive tensoring; the only question is whether the leading injection $N' \hookrightarrow N$ stays an injection. So "flat = preserves injections" names the precise residual obligation, and the broader "preserves short exact sequences" is a consequence, not a separate axiom. Stating the definition with the surplus would hide where the content lives.

**What if we demanded only that $M$ be torsion-free instead?** This is the tempting near-miss. A module is *torsion-free* when $rm = 0$ forces $m = 0$ whenever $r$ is a non-zero-divisor — that is, when multiplication $\mu_r$ acts injectively on $M$ for each non-zero-divisor $r$. Every flat module is torsion-free, because a torsion element is *exactly* a witness that tensoring breaks an injection: if $r$ is a non-zero-divisor then $\mu_r : R \to R$ is injective, so flatness forces $\operatorname{id}_M \otimes \mu_r$ — which under $M \otimes R \cong M$ is just multiplication by $r$ on $M$ — to be injective, i.e. no torsion. But the converse fails: torsion-free is strictly weaker. The maximal ideal $(X,Y) \trianglelefteq k[X,Y]$ has no torsion (it sits inside a domain) yet is not flat. So "torsion-free" only checks injectivity of $\operatorname{id}_M \otimes f$ for the very special maps $f = \mu_r$, multiplication by ring elements; flatness demands it for *all* injections $f$, and over rings of dimension $\geq 2$ there are injections not of the form $\mu_r$ that detect the difference. Weakening flat to torsion-free would let in modules that break injections coming from genuinely two-dimensional relations.

**What if we strengthened, demanding $M$ be free?** Then we would have a clean, easy class — free modules are flat for the cheapest reason, since tensoring with $R^{\oplus I}$ is taking $I$ copies and a direct sum of injections is injective — but we would have thrown away exactly the modules the theory exists to study. Localizations $S^{-1}R$ are flat and almost never free; finitely generated projective modules (vector bundles) are flat and need not be free; $\mathbb{Q}$ is a flat $\mathbb{Z}$-module and is not free. Flatness is the right level of generality because it is the *exactness* property — what you actually need for tensoring to behave — stripped of the much stronger and much rarer structural property of having a basis. The whole point is to capture "tensoring is safe" without paying for "has a basis."

One subtlety deserves emphasis because it trips everyone once: **flatness is a property of $M$ relative to its base ring $R$, not an intrinsic property of $M$ as an abelian group.** The same set with the same addition can be flat over one ring and not over another. $\mathbb{Z}/2$ is *not* flat over $\mathbb{Z}$ (our opening example), but it *is* flat over $\mathbb{Z}/2$ — there it is the free module of rank one. Changing the base ring changes which injections exist to be tested, and hence changes the answer. Always read "flat" as "flat over $R$" with $R$ named.

---

# The Definition

Let $R$ be a commutative ring and $M$ an $R$-module.

## Flat module

$M$ is **flat** if for every injective $R$-linear map $f : N \to N'$, the induced map
$$\operatorname{id}_M \otimes f : M \otimes_R N \longrightarrow M \otimes_R N'$$
is again injective. Equivalently (using that [[Thm - Tensoring is Right Exact|$T_M$ is already right exact]]), $M$ is flat if and only if the functor $T_M = M \otimes_R (-)$ is **exact** — it preserves every exact sequence, and in particular sends short exact sequences to short exact sequences.

## Torsion-free module

$M$ is **torsion-free** if $rm \neq 0$ whenever $r \in R$ is a non-zero-divisor and $m \neq 0$; equivalently, for each non-zero-divisor $r$, multiplication by $r$ on $M$ is injective. For $R = \mathbb{Z}$ this is the usual notion of a torsion-free abelian group, since the only zero-divisor of $\mathbb{Z}$ is $0$.

Every flat module is torsion-free; the converse holds over a [[Def - Principal Ideal Domain|principal ideal domain]] but fails in general (see [[Ex - The maximal ideal (X,Y) is torsion-free but not flat]]).

---

# Categorical / Structural Definition

The structural definition is the one that explains the name's behaviour: **$M$ is flat exactly when $T_M = M \otimes_R (-)$ is an exact functor on the category of $R$-modules.** A functor between abelian categories is *exact* when it preserves exact sequences; $T_M$ is always *right* exact (a consequence of $T_M$ being a left adjoint — its right adjoint is $\operatorname{Hom}_R(M, -)$, via the adjunction $\operatorname{Hom}(M \otimes N, L) \cong \operatorname{Hom}(N, \operatorname{Hom}(M, L))$), and flatness is precisely the extra hypothesis that makes it *fully* exact. In this language flatness is the acyclicity condition for the [[Def - Tensor Product of Modules|tensor functor]]: the **derived functors** $\operatorname{Tor}_n^R(M, -)$ measure the failure of left-exactness, $\operatorname{Tor}_0 = T_M$, and $M$ is flat if and only if $\operatorname{Tor}_n^R(M, -) = 0$ for all $n \geq 1$. The flat modules are thus the $T_M$-acyclic objects, the exact analogue of how projective modules are the $\operatorname{Hom}(-, P)$-acyclic objects. The full homological development is downstream; what matters here is the clean statement *flat = tensoring is exact*.

---

# Relate to Other Fields / Compression

The cleanest compression: **flat means tensoring with $M$ never creates a linear relation that was not already present.** Tensoring inevitably identifies *some* elements — that is what the defining relations $rm \otimes n = m \otimes rn$ of the tensor product do — and flatness is the guarantee that it identifies *only* what it is forced to, never collapsing two genuinely distinct elements of a submodule into one. Torsion is the prototypical relation tensoring wrongly creates: a torsion equation $rm_0 = 0$ (with $r$ a non-zero-divisor) is a distinction in $R$ — namely $r \neq 0$ — that tensoring with $M$ destroys, sending $m_0 \otimes r \mapsto rm_0 \otimes 1 = 0$.

**True name:** the true name of flatness is *not* "$\operatorname{id}_M \otimes f$ injective for all injective $f$" but the operational **"for every submodule inclusion $N' \hookrightarrow N$, the map $M \otimes N' \to M \otimes N$ is again an inclusion — distinct tensors stay distinct."** This is the form you reach for: to refute flatness, find two tensors in some $M \otimes N'$ that become equal in $M \otimes N$; to prove it, show no such collapse can occur, usually by reducing to finitely generated $N'$ via [[Thm - Characterization of Flat Modules|the finitely generated criterion]].

In algebraic geometry the compression is geometric: **a flat module is a flat family — a family of fibres that varies continuously, with no fibre jumping in dimension.** A ring map $A \to B$ makes $B$ a family over $\operatorname{Spec} A$, and flatness of $B$ over $A$ is exactly the condition that the fibres do not tear. This is the analogue of a *continuous* (indeed, in the smooth case, a *submersion-like*) map in differential topology, where fibres vary without collapsing — flatness is the algebraic substitute for that continuity, and it is what makes deformation theory possible.

---

# Examples / Corollaries

**Is an instance — free modules.** Any [[Def - Free Module|free module]] $R^{\oplus I}$ is flat. Tensoring an injection $f : N \to N'$ with $R^{\oplus I}$ gives, under the isomorphism $R^{\oplus I} \otimes N \cong N^{\oplus I}$, the map $(n_i)_i \mapsto (f(n_i))_i$, which is injective because $f$ is. In particular $R$ itself is flat. This is the bottom of the tower: free $\Rightarrow$ flat.

**Is an instance — localizations.** For a multiplicative set $S \subseteq R$, the localization $S^{-1}R$ is a flat $R$-module, because $S^{-1}M \cong S^{-1}R \otimes_R M$ and localization is exact (passing to fractions never breaks an injection). $\mathbb{Q} = S^{-1}\mathbb{Z}$ with $S = \mathbb{Z} \setminus \{0\}$ is the prototype: $\mathbb{Q}$ is flat over $\mathbb{Z}$ (see [[Ex - Q is a flat but not projective Z-module]]), and notably flat without being free or projective.

**Is an instance — extension of scalars of a flat module.** If $M$ is flat over $R$ and $R \to S$ is any ring map, then $S \otimes_R M$ is flat over $S$ ([[Thm - Extension of Scalars Preserves Flatness]]). So flatness propagates along base change.

**Is NOT an instance — $\mathbb{Z}/n$ over $\mathbb{Z}$ for $n \geq 2$.** The module $\mathbb{Z}/n$ is not flat over $\mathbb{Z}$. Tensoring the injection $\mathbb{Z} \xrightarrow{\times n} \mathbb{Z}$ with $\mathbb{Z}/n$ yields $\mathbb{Z}/n \xrightarrow{\times n = 0} \mathbb{Z}/n$, the zero map on a non-zero module — injectivity destroyed. Equivalently $\mathbb{Z}/n$ has torsion ($n \cdot 1 = 0$ with $n$ a non-zero-divisor), and flat modules are torsion-free. This is the defining failure that motivates the whole notion.

**Is NOT an instance — $R/I$ for a proper non-zero ideal of a domain.** If $R$ is an [[Def - Integral Domain|integral domain]] and $(0) \subsetneq I \subsetneq R$, then $R/I$ is not flat. Pick $0 \neq r \in I$: since $R$ is a domain, $r$ is a non-zero-divisor, but multiplication by $r$ on $R/I$ is the zero map (as $r \in I$), while $R/I \neq 0$. So $R/I$ has torsion and is not flat.

**Is NOT an instance — torsion-free but not flat.** Torsion-freeness is not enough: the maximal ideal $(X,Y) \trianglelefteq k[X,Y]$ is torsion-free yet not flat ([[Ex - The maximal ideal (X,Y) is torsion-free but not flat]]). This is the example that proves the bottom two links of the tower are distinct.

**Corollary — flatness is preserved under direct sums and summands.** $\bigoplus_i M_i$ is flat iff each $M_i$ is flat, because tensoring commutes with direct sums and a direct sum of injections is an injection. In particular a direct summand of a flat module is flat — the reason [[Def - Projective Module|projective]] (summand of free) modules are flat.

**Calibration check.** Verify directly that tensoring $\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$ with $\mathbb{Z}/2$ gives the zero map, so $\mathbb{Z}/2$ is not flat over $\mathbb{Z}$ — and confirm $\mathbb{Z}/2$ *is* flat over $\mathbb{Z}/2$, so flatness is base-ring-dependent. Confirm that "flat $\Rightarrow$ torsion-free" is exactly the statement "$\operatorname{id}_M \otimes \mu_r$ injective for non-zero-divisors $r$", and explain why this only tests the maps $\mu_r$, not all injections. Finally, check that $R^{\oplus I}$ is flat by writing out $R^{\oplus I} \otimes f$ as a componentwise injection.

---

# Unlocked by This

> [!tip] Flat families and flat morphisms *(from Algebraic Geometry)*
> A ring map $A \to B$ with $B$ flat over $A$ is a **flat morphism** $\operatorname{Spec} B \to \operatorname{Spec} A$, the algebraic encoding of a family of spaces whose fibres vary continuously — no fibre jumping in dimension or length. This is the standard hypothesis under which one builds **deformations** and **moduli spaces**: allowing only flat families is exactly what prevents the geometry from tearing. A monic-polynomial quotient $A[T]/(f)$ is the model finite flat family of points; $k[X,Y]/(XY)$ over $k[X]$ is the model non-flat family whose fibre jumps at the origin.

> [!tip] Tor and the derived theory *(from Homological Algebra)*
> The failure of $T_M$ to be left exact is measured by the **Tor functors** $\operatorname{Tor}_n^R(M, -)$, and $M$ is flat exactly when $\operatorname{Tor}_n^R(M, -) = 0$ for all $n \geq 1$ — equivalently $\operatorname{Tor}_1^R(R/I, M) = 0$ for every finitely generated ideal $I$. The long exact sequence of Tor is the systematic accounting of how badly injectivity breaks, and flat modules are the acyclic objects of this theory.

> [!tip] Faithfully flat descent *(from Algebraic Geometry)*
> A flat module that is moreover **faithfully flat** ($M \otimes N = 0 \Rightarrow N = 0$) lets properties be checked after base change and *descended* back down: faithfully flat descent is the technical engine that glues local algebraic data into global geometric objects, underpinning the étale and fppf topologies. Flatness here is the entry point to that machinery.
