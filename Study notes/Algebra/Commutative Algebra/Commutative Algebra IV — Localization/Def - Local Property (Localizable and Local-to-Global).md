---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Module"
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For a [[Def - Module|module]] $M$ over $R$ and a [[Def - Prime and Maximal Ideal|prime]] $\mathfrak{p}$, $M_{\mathfrak{p}} = (R\setminus\mathfrak{p})^{-1}M$ is its [[Def - Multiplicative Set and Localization|localization]], a module over the [[Def - Local Ring and Residue Field|local ring]] $R_{\mathfrak{p}}$. We write $\operatorname{Spec} R$ for the primes and $\operatorname{mSpec} R$ for the maximal ideals. A property $P$ may be a property of modules ("$M$ is flat", "$M = 0$") or of $R$-linear maps ("$f$ is injective"); when $f : M \to N$ is a map, $f_{\mathfrak{p}} : M_{\mathfrak{p}} \to N_{\mathfrak{p}}$ is its localization. The full registry is on [[Commutative Algebra IV — Localization]].

This is a compound page: it defines three interlocking notions — **localizable**, **local-to-global**, and **local** (their conjunction) — because "local property" is precisely the two-sided condition, and separating the two halves is what lets you see *which* direction of a local-global theorem is doing the work.

---

# Axiom Motivation

The most powerful technique in commutative algebra is "check it one prime at a time": replace a question about $M$ over a complicated ring $R$ by the *same* question about $M_{\mathfrak{p}}$ over the simple [[Def - Local Ring and Residue Field|local ring]] $R_{\mathfrak{p}}$, solve it there, and conclude globally. This page isolates exactly when that technique is *valid*. The validity is not automatic — some properties survive the reduction and some do not — so the definition's job is to name the two halves of the implication and demand both.

**Why the property must be split into two independent directions.** "Check it locally" is a biconditional: $P$ holds for $M$ *if and only if* $P$ holds for every $M_{\mathfrak{p}}$. But the two directions are logically independent and have different content, so they deserve separate names. The forward direction — *$P$ for $M$ implies $P$ for each $M_{\mathfrak{p}}$* — is called **localizable**: the property *descends* to localizations, it is preserved when you zoom in. The backward direction — *$P$ for every $M_{\mathfrak{p}}$ implies $P$ for $M$* — is called **local-to-global**: local truth *assembles* into global truth, the property *glues*. A property is **local** when both hold. Splitting them matters because the two directions fail for genuinely different reasons, and most of the skill in using local-global arguments is knowing which direction you are relying on.

**Why "localizable" is usually the easy half.** A property descends to localizations when localization, as a functor, *preserves* the structure defining the property. This is almost always the case for the good properties, because $S^{-1}(-)$ is an [[Thm - Localization is Exact and the Localization is Flat|exact functor]]: it preserves kernels, images, injections, surjections, exact sequences, and (by base change) flatness. So "$M$ flat $\Rightarrow M_{\mathfrak{p}}$ flat", "$f$ injective $\Rightarrow f_{\mathfrak{p}}$ injective", "$M = 0 \Rightarrow M_{\mathfrak{p}} = 0$" are all just *functoriality plus exactness*. Localizability is the direction you get "for free" from the machinery of the previous sections — it requires no new idea, only that the property be phrased in terms exactness respects. The genuine content of a local-global theorem is almost never here.

**Why "local-to-global" is the hard half, and where it can fail.** Gluing local truth into global truth is *not* formal. It is the direction that can break, and watching it break is how you learn the boundary of the technique. The engine that makes it work for the good properties is the single theorem "**being zero is local-to-global**": if $M_{\mathfrak{m}} = 0$ for every maximal ideal $\mathfrak{m}$, then $M = 0$. The proof is the annihilator argument — a nonzero $m \in M$ would have a proper annihilator $\operatorname{Ann}(m)$, which lies in some maximal ideal $\mathfrak{m}$; but $M_{\mathfrak{m}} = 0$ forces $um = 0$ for some $u \notin \mathfrak{m}$, putting $u \in \operatorname{Ann}(m) \setminus \mathfrak{m}$, a contradiction. From this one theorem, every other local-to-global statement follows by localizing the appropriate kernel or image and applying it. But the technique has a *boundary*, and the boundary is exactly where the property is *not* detected by exactness-friendly module data. **Freeness is not local-to-global**: a module can be free at every prime (locally free) without being free, because freeness records *global* gluing data — the difference between a trivial bundle and a twisted one — that the individual stalks cannot see. Being an **integral domain** is not local-to-global either: a product of fields is locally a field (hence locally a domain) but has zero-divisors globally. These failures are not pathologies; they are where vector bundles and disconnected spectra live.

**Why we may always check on maximal (not all prime) ideals.** A convenient strengthening: for the local-to-global direction it suffices to check at *maximal* ideals, because the annihilator argument only ever needs a maximal ideal (every proper ideal sits inside one). So "local-to-global" really means "$P$ holds for $M$ whenever $P$ holds for every $M_{\mathfrak{m}}$, $\mathfrak{m}$ maximal". This is strictly easier to verify — maximal ideals are the closed points, the most concrete primes — and it is why local-global proofs invariably say "it suffices to check at an arbitrary maximal ideal". The reason this restriction is legitimate is structural: any "reasonable" module property (one invariant under isomorphism of modules and of base rings) automatically passes from "holds at all maximal ideals" to "holds at all primes", because a prime $\mathfrak{p}$ sits inside some maximal ideal of $R_{\mathfrak{p}}$ and localizing again does no harm.

**Why this is the algebraic form of a pervasive mathematical pattern.** "Local property" is the algebraic name for *local-to-global propagation*, which organises much of geometry and analysis: a manifold property holds globally iff it holds in every chart; a sheaf is zero iff every stalk is zero; a differential equation has a global solution iff local solutions glue. The definition here makes the pattern precise in algebra and, crucially, *delimits* it — by naming local-to-global as a separate, falsifiable condition, it forces you to confront the cases (freeness, domain) where local data does *not* glue, which is exactly where the interesting global invariants (the [[Def - The Prime Spectrum (Spec)|Picard group]], cohomology) come from.

---

# The Definition

Let $P$ be a property of $R$-modules (or of $R$-linear maps).

## Localizable

$P$ is **localizable** if: whenever $M$ has $P$, then $M_{\mathfrak{p}}$ has $P$ (as an $R_{\mathfrak{p}}$-module) for every prime $\mathfrak{p} \in \operatorname{Spec} R$. (Equivalently, $P$ descends along every localization $R \to S^{-1}R$.)

## Local-to-global

$P$ is **local-to-global** if: whenever $M_{\mathfrak{p}}$ has $P$ for every prime $\mathfrak{p} \in \operatorname{Spec} R$, then $M$ has $P$. For a *reasonable* property it is equivalent to require this only for maximal $\mathfrak{p} = \mathfrak{m}$.

## Local

$P$ is a **local property** if it is both localizable and local-to-global; equivalently, for every $M$,
$$M \text{ has } P \;\iff\; M_{\mathfrak{p}} \text{ has } P \text{ for all } \mathfrak{p} \in \operatorname{Spec} R \;\iff\; M_{\mathfrak{m}} \text{ has } P \text{ for all } \mathfrak{m} \in \operatorname{mSpec} R.$$

## The standard local properties

The following are local properties (see [[Thm - The Local-Global Principle]]):
$$M = 0; \qquad f \text{ injective}; \qquad f \text{ surjective}; \qquad A \xrightarrow{f} B \xrightarrow{g} C \text{ exact}; \qquad M \text{ flat}.$$
A ring property analogue: $R$ **reduced** is local. The following are **localizable but not local-to-global**, hence *not* local: $M$ **free**, $R$ an **integral domain**.

---

# Categorical / Structural Definition

Localization is a family of functors $(-)_{\mathfrak{p}} : R\text{-}\mathbf{Mod} \to R_{\mathfrak{p}}\text{-}\mathbf{Mod}$, one for each prime, and "localizable" is the statement that the property $P$ is *preserved* by every functor in the family. The collection of all these functors assembles into a single faithful functor $M \mapsto (M_{\mathfrak{p}})_{\mathfrak{p}}$ into the product $\prod_{\mathfrak{p}} R_{\mathfrak{p}}\text{-}\mathbf{Mod}$, and "local-to-global" is the statement that $P$ is *reflected* by this combined functor — $P$ holds upstairs whenever it holds in every component. A **local property** is thus one both *preserved and reflected* by the localization family: the family is "$P$-conservative". The base theorem that makes the combined functor reflect isomorphisms (and hence reflects "$= 0$") is that **localization at all maximal ideals is jointly faithful**: $M = 0 \iff M_{\mathfrak{m}} = 0$ for all $\mathfrak{m}$, the precise sense in which "the maximal-ideal localizations see everything". Geometrically this is the statement that a quasicoherent sheaf is zero iff all its stalks vanish — the conservativity of the stalk functors that founds sheaf-theoretic local-to-global arguments.

---

# Relate to Other Fields / Compression

The cleanest compression: **a local property is one you may verify one prime at a time — localizable means it survives zooming in, local-to-global means local truths glue, and "local" demands both.** The first is free from exactness; the second is the content, powered by "being zero is local".

**True name:** the operational true name is "**check it at every maximal ideal**". When a property is known to be local, the entire technique it licenses is the sentence "it suffices to prove this after localizing at an arbitrary maximal ideal $\mathfrak{m}$", after which you work over the simple ring $R_{\mathfrak{m}}$. The biconditional definition is the justification; "check at each $\mathfrak{m}$" is the move.

This is the algebraic form of **local-to-global propagation**, the organising principle of sheaf theory and geometry. A sheaf $\mathcal{F}$ on a space is zero iff every stalk $\mathcal{F}_x$ is zero — *exactly* "being zero is a local property", with stalks $\mathcal{F}_x = M_{\mathfrak{p}}$. The failure of *freeness* to be local-to-global is the algebraic seed of **vector bundles**: a locally free sheaf that is not free is a nontrivial bundle, and the obstruction to gluing local trivialisations into a global one is measured by cohomology (the Picard group $\operatorname{Pic}$, $H^1$ with values in the units sheaf). So this page draws the exact line between properties that geometry can ignore (the local ones) and properties that generate global invariants (the non-local ones, where bundles, the Brauer group, and obstruction theory live). The **Hasse principle** of number theory is the same dichotomy: a Diophantine property that is "local-to-global" holds over $\mathbb{Q}$ iff it holds over every $\mathbb{Q}_p$ and $\mathbb{R}$, and the famous *failures* of the Hasse principle are non-local-to-global properties.

---

# Examples / Corollaries

**Is an instance — "$M = 0$" is local.** Localizable: $M = 0 \Rightarrow M_{\mathfrak{p}} = S^{-1}0 = 0$ trivially. Local-to-global: the annihilator argument. So a module is zero iff all its localizations are — the base case under every other local-global theorem.

**Is an instance — "$f$ injective" is local.** Localizable because $S^{-1}(-)$ is exact (it preserves injections: $S^{-1}(\ker f) = \ker(S^{-1}f)$, so $\ker f = 0 \Rightarrow \ker f_{\mathfrak{p}} = 0$). Local-to-global because $\ker f = 0 \iff (\ker f)_{\mathfrak{m}} = 0$ for all $\mathfrak{m}$ by the zero-case. The identical argument handles "surjective" and "exact".

**Is an instance — "$M$ flat" is local.** Localizable because flatness is preserved by base change ($M_{\mathfrak{p}} = R_{\mathfrak{p}} \otimes_R M$ and base change preserves flatness). Local-to-global by a tensor-and-localize argument reducing to "injectivity is local". This is the deepest of the standard local properties.

**Is an instance (ring property) — "reduced" is local.** $R$ is reduced iff $\operatorname{nil} R = 0$ iff $R_{\mathfrak{p}}$ is reduced for all $\mathfrak{p}$. Localizable because $\operatorname{nil}(R_{\mathfrak{p}}) = (\operatorname{nil} R)_{\mathfrak{p}}$; local-to-global because $\operatorname{nil} R = 0 \iff (\operatorname{nil} R)_{\mathfrak{m}} = 0$ for all $\mathfrak{m}$ — see [[Ex - Being reduced is a local property]].

**Is NOT an instance — "$M$ free" is localizable but NOT local-to-global.** Over $R = \mathbb{C}\times\mathbb{C}$, every localization is a field, so every module is locally free; yet the ideal $M = \mathbb{C}\times\{0\}$ is *not* free (it is annihilated by $(0,1)$, so has no basis). Freeness descends but does not glue. This is [[Ex - Freeness is not a local property]], and it is the algebraic origin of nontrivial vector bundles.

**Is NOT an instance — "$R$ is a domain" is not local.** The same $R = \mathbb{C}\times\mathbb{C}$ has every $R_{\mathfrak{p}} \cong \mathbb{C}$ a domain, but $R$ itself has zero-divisors $(1,0)(0,1) = 0$. "Domain" descends to localizations but does not glue across a disconnected spectrum.

**Corollary — the reasonable-property meta-theorem.** For any property invariant under module isomorphism and under base-ring isomorphism, "holds at every maximal ideal" already implies "holds at every prime". So in practice one only ever checks maximal ideals, and the prime/maximal distinction in the definition is harmless for sensible $P$.

**Calibration check.** State, for "$M = 0$", which direction is localizable and which is local-to-global, and identify which one needs the annihilator argument. Confirm that "$f$ injective" is local by reducing it to "$\ker f = 0$" and citing the zero-case. Finally, explain in one sentence why freeness fails the local-to-global direction but passes the localizable direction — i.e. why a vector bundle is locally trivial yet possibly globally twisted.

---

# Unlocked by This

> [!tip] Sheaves and stalks: a sheaf vanishes iff all stalks vanish *(from Algebraic Geometry / Sheaf Theory)*
> "Being zero is a local property" is, under the structure-sheaf dictionary "$M_{\mathfrak{p}}$ is the stalk at $\mathfrak{p}$", the foundational theorem of sheaf theory: a quasicoherent sheaf $\widetilde{M}$ on $\operatorname{Spec} R$ is zero iff all its stalks are zero, and a morphism is injective/surjective/an isomorphism iff it is so on every stalk. Every local-to-global argument in algebraic geometry — checking that a map of sheaves is an isomorphism, that a sequence is exact, that a sheaf is flat over the base — is an instance of the [[Thm - The Local-Global Principle|local–global principle]] proved here by pure algebra. The conservativity of the stalk functors *is* the local-to-global half of this page's definition.

> [!tip] Locally free sheaves are vector bundles; non-local-to-global properties carry global invariants *(from Algebraic Geometry)*
> The fact that **freeness is not local-to-global** is exactly why **vector bundles** exist as nontrivial objects: a finitely generated module that is free at every prime (locally free) corresponds to a vector bundle on $\operatorname{Spec} R$, which is locally trivial but may be globally twisted. The obstruction to gluing the local frames into a global basis is a cohomology class — the **Picard group** $\operatorname{Pic}(R) = H^1(\operatorname{Spec} R, \mathcal{O}^\times)$ for line bundles — and the non-free locally-free ideal $(2, 1+\sqrt{-5})$ over $\mathbb{Z}[\sqrt{-5}]$ is a generator of a nontrivial $\operatorname{Pic}$. This is the **Serre–Swan** correspondence in embryo: finitely generated projective modules $=$ vector bundles, and the failure of "projective $\Rightarrow$ free" is the existence of bundles.

> [!tip] The Hasse principle and local-global in number theory *(from Number Theory)*
> The same localizable/local-to-global split governs the **Hasse principle**: a property of equations over $\mathbb{Q}$ is "local-to-global" when its solvability over $\mathbb{Q}$ is equivalent to solvability over every completion $\mathbb{Q}_p$ and $\mathbb{R}$. Quadratic forms satisfy it (Hasse–Minkowski); the celebrated *counterexamples* (Selmer's cubic $3X^3 + 4Y^3 + 5Z^3 = 0$) are properties that are *not* local-to-global, and the obstruction is again a cohomology class (the Brauer–Manin obstruction) — the arithmetic analogue of a nontrivial bundle.
