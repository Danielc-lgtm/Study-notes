---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Direct and Inverse Limits"
  - "Def - Directed Set and Direct System"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Quotient Ring"
  - "Def - Quotient Module"
  - "Def - Noetherian Ring"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring, $\mathfrak{a}\trianglelefteq R$ an [[Def - Ideal|ideal]], and $M$ an [[Def - Module|$R$-module]]. We write $\mathfrak{a}^n$ for the $n$-th power of $\mathfrak{a}$ (with $\mathfrak{a}^0=R$), $R/\mathfrak{a}^n$ and $M/\mathfrak{a}^n M$ for the [[Def - Quotient Ring|truncation]] [[Def - Quotient Module|quotients]], and the natural projections $R/\mathfrak{a}^{n+1}\twoheadrightarrow R/\mathfrak{a}^n$, $M/\mathfrak{a}^{n+1}M\twoheadrightarrow M/\mathfrak{a}^n M$ as the inverse-system transition maps. The completion is $\widehat{R}=\widehat{R}^{\,\mathfrak{a}}=\varprojlim_n R/\mathfrak{a}^n$ and $\widehat{M}=\widehat{M}^{\,\mathfrak{a}}=\varprojlim_n M/\mathfrak{a}^n M$; the completion map is $\varphi:M\to\widehat{M}$, $m\mapsto(m+\mathfrak{a}^n M)_n$. Standard cases: $\mathbb{Z}_p$ ($R=\mathbb{Z}$, $\mathfrak{a}=(p)$) and $k[[T]]$ ($R=k[T]$, $\mathfrak{a}=(T)$). The full registry is on [[Commutative Algebra X — Completions and Limits]].

This is a compound page: it defines three interlocking notions — the **$\mathfrak{a}$-adic completion of a ring** $\widehat{R}$, the **$\mathfrak{a}$-adic completion of a module** $\widehat{M}$, and the **completion with respect to a general filtration** — because the ring case is the module case at $M=R$ with a multiplication, and the $\mathfrak{a}$-adic case is the filtered case with filtration $(\mathfrak{a}^n M)$.

---

# Axiom Motivation

The goal is to **make an element knowable by its successive approximations and then adjoin the limiting elements those approximations point to but never reach**. We have a ring $R$ and a distinguished ideal $\mathfrak{a}$ that we think of as "the functions vanishing at a point", and we want to manufacture the ring of *Taylor series at that point* — the ring that records the infinitesimal behaviour to all orders. Everything on this page is the [[Def - Direct and Inverse Limits|inverse limit]] construction, specialised to the one tower of approximations that matters. The way to invent it is to ask what "approximation to order $n$" should mean and what "the limit of the approximations" should be.

**Why the truncations $R/\mathfrak{a}^n$ are the right approximations.** An element of $\mathfrak{a}$ is "small" — it vanishes at the point — so an element of $\mathfrak{a}^n$ is "small of order $n$": a product of $n$ small things, vanishing to order $n$. To know a ring element "to order $n$" is to know it *modulo* things that vanish to order $n$, i.e. to know its class in $R/\mathfrak{a}^n$. This is exactly Taylor's idea: knowing $f$ to order $n-1$ means knowing $f\bmod(T^n)$, the truncation of its Taylor series. The choice $\mathfrak{a}^n$ (rather than some other shrinking sequence of ideals) is forced by wanting the approximations to be *multiplicatively coherent*: the product of an order-$m$ datum and an order-$n$ datum is known to order $m+n$, because $\mathfrak{a}^m\cdot\mathfrak{a}^n\subseteq\mathfrak{a}^{m+n}$. No other natural filtration makes truncation a ring map at every level.

**Why an inverse limit, with the projections as transition maps.** The approximations form a tower: knowing $f$ to order $n+1$ determines knowing it to order $n$, via the projection $R/\mathfrak{a}^{n+1}\twoheadrightarrow R/\mathfrak{a}^n$ that forgets the top-order term. So we have an inverse system, and "the element determined by all its approximations at once, consistently" is by definition the inverse limit $\widehat{R}=\varprojlim R/\mathfrak{a}^n$ — the set of compatible threads of truncations. A thread is precisely a formal Taylor series: a choice of $n$-truncation for every $n$, each refining the last. The reason this *adjoins new elements* — the reason $\widehat{R}$ is bigger than $R$ — is that there are consistent threads with no single $R$-element behind them: the geometric series $1+T+T^2+\cdots$ is a perfectly consistent thread in $\varprojlim k[T]/(T^n)$ but is not a polynomial. The inverse limit *completes* the ring by filling in these limiting elements, exactly as Cauchy sequences fill in $\mathbb{R}$ from $\mathbb{Q}$. Had we taken a *direct* limit instead, we would have unioned the truncations into the divisible torsion debris of a Prüfer-type group — the opposite, and useless, construction. The arrows must point *down* (projections), and the limit must be inverse.

**Why the module version, and why $\widehat{M}$ is an $\widehat{R}$-module.** Modules carry the geometry too — a module is a "vector bundle's worth of functions" — so we complete them the same way: approximate $m$ to order $n$ by its class in $M/\mathfrak{a}^n M$, and set $\widehat{M}=\varprojlim M/\mathfrak{a}^n M$. The submodule $\mathfrak{a}^n M$ is the correct notion of "order-$n$-small elements of $M$" because $\mathfrak{a}$ acts as the small scalars. The completed module is naturally a module over the completed ring: a thread of scalars $(r_n)\in\widehat{R}$ acts on a thread of module elements $(m_n)\in\widehat{M}$ levelwise, $(r_n)\cdot(m_n)=(r_n m_n)$, and this is well-defined because $r_n m_n\bmod\mathfrak{a}^n M$ depends only on $r_n\bmod\mathfrak{a}^n$ and $m_n\bmod\mathfrak{a}^n M$. So completion turns $R$-modules into $\widehat{R}$-modules; it is a *base change* to the formal disk, and the precise statement $\widehat{M}\cong\widehat{R}\otimes_R M$ for finitely generated $M$ is proved on [[Thm - The Completion of a Noetherian Ring is Noetherian]].

**Why the general-filtration definition, and what the completion map records.** The only structural input was a descending chain of submodules $M=M_0\supseteq M_1\supseteq\cdots$ with $M_n=\mathfrak{a}^n M$; nothing forced the chain to be the $\mathfrak{a}$-adic one. So the construction generalises verbatim to any [[Def - Filtration and Stable Filtration|filtration]] $(M_n)$: $\widehat{M}=\varprojlim M/M_n$. The $\mathfrak{a}$-adic case is the one this chapter needs, but the general definition is what makes the comparison theorems (different filtrations giving the same completion) statable. Finally, the bridge back to $M$ is the completion map $\varphi:M\to\widehat{M}$, $m\mapsto(m+\mathfrak{a}^n M)_n$, sending each element to the thread of *its own* truncations. Reading off the inverse-limit definition, $\varphi(m)=0$ iff $m\in\mathfrak{a}^n M$ for *every* $n$, so
$$\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M.$$
This intersection — the elements "infinitely divisible by $\mathfrak{a}$", invisible to all finite approximations — is the exact measure of how much information completion destroys, and the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]] says it vanishes in the Noetherian local world, so $\varphi$ is injective and $M\hookrightarrow\widehat{M}$ is an honest enlargement.

---

# The Definition

Let $R$ be a commutative ring, $\mathfrak{a}\trianglelefteq R$ an ideal, $M$ an $R$-module.

## $\mathfrak{a}$-adic completion of a ring

The powers $R=\mathfrak{a}^0\supseteq\mathfrak{a}^1\supseteq\mathfrak{a}^2\supseteq\cdots$ give an [[Def - Directed Set and Direct System|inverse system]] $\big(R/\mathfrak{a}^n\big)_{n\geq0}$ over $(\mathbb{N},\leq)$, with transition maps the natural projections $h_{mn}:R/\mathfrak{a}^n\to R/\mathfrak{a}^m$ for $m\leq n$. The **$\mathfrak{a}$-adic completion** of $R$ is the [[Def - Direct and Inverse Limits|inverse limit]]
$$\widehat{R}\;=\;\widehat{R}^{\,\mathfrak{a}}\;=\;\varprojlim_{n}R/\mathfrak{a}^{n}\;=\;\Big\{(r_n)_n\in\textstyle\prod_n R/\mathfrak{a}^n : r_m\equiv r_n\!\!\pmod{\mathfrak{a}^m}\ \text{for } m\leq n\Big\},$$
a commutative ring under coordinatewise operations.

## $\mathfrak{a}$-adic completion of a module

With transition maps the projections $M/\mathfrak{a}^n M\to M/\mathfrak{a}^m M$, the **$\mathfrak{a}$-adic completion** of $M$ is
$$\widehat{M}\;=\;\widehat{M}^{\,\mathfrak{a}}\;=\;\varprojlim_{n}M/\mathfrak{a}^{n}M,$$
an $\widehat{R}$-module via $(r_n)\cdot(m_n)=(r_n m_n)$.

## Completion with respect to a filtration

A [[Def - Filtration and Stable Filtration|filtration]] of $M$ is a descending chain of submodules $M=M_0\supseteq M_1\supseteq\cdots$. The **completion of $M$ with respect to $(M_n)$** is $\varprojlim_n M/M_n$. The $\mathfrak{a}$-adic completion is the case $M_n=\mathfrak{a}^n M$.

## The completion map

The **completion map** is the homomorphism
$$\varphi=\varphi_M:M\to\widehat{M},\qquad \varphi(m)=(m+\mathfrak{a}^n M)_n,$$
sending each element to the thread of its truncations. Its kernel is
$$\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M.$$

---

# Categorical / Structural Definition

The completion is, by construction, the [[Def - Direct and Inverse Limits|inverse limit]] of the truncation system, so it inherits that universal property directly: **$\widehat{M}=\varprojlim M/\mathfrak{a}^n M$ is the universal $R$-module $B$ equipped with compatible maps $g_n:B\to M/\mathfrak{a}^n M$** (compatible meaning each $g_{n}$ followed by the projection gives $g_{n-1}$). The completion map $\varphi$ is the unique such universal map out of $M$ itself, induced by the truncations $M\to M/\mathfrak{a}^n M$.

Structurally, completion is a **functor** $\widehat{(-)}:R\text{-Mod}\to\widehat{R}\text{-Mod}$, and on finitely generated modules over a Noetherian ring it is naturally isomorphic to the **base-change functor** $\widehat{R}\otimes_R(-)$: there is a natural map $\widehat{R}\otimes_R M\to\widehat{M}$, $x\otimes m\mapsto xm$, which is an isomorphism for finitely generated $M$ (see [[Thm - The Completion of a Noetherian Ring is Noetherian]]). This identifies completion with the same kind of operation as [[Commutative Algebra IV — Localization|localization]] — both are "tensor up to a more local ring" — and is why completion, like localization, is exact in the good cases. The difference is the target: localization passes to the Zariski-local ring $R_{\mathfrak{p}}$, completion passes to the analytic-local (formal) ring $\widehat{R}$, which is strictly finer.

---

# Relate to Other Fields / Compression

The cleanest compression: **the $\mathfrak{a}$-adic completion is the ring of formal Taylor series along the locus $\mathfrak{a}=0$ — the inverse limit of the truncation tower $R/\mathfrak{a}^n$, which adjoins every limiting element that the finite truncations point to.** Set $R=\mathbb{Z}$, $\mathfrak{a}=(p)$ and you get $\mathbb{Z}_p$; set $R=k[T]$, $\mathfrak{a}=(T)$ and you get $k[[T]]$.

**True name:** the true name of $\widehat{R}$ is **"the ring of compatible truncation-threads"**, equivalently **"$R$ with all $\mathfrak{a}$-adic Cauchy sequences given their limits"**. This is the operational form: to specify an element you give its reduction mod $\mathfrak{a}^n$ for each $n$ compatibly; to invert an element you check it is a unit mod $\mathfrak{a}$ and sum a geometric series; to solve an equation you solve it mod $\mathfrak{a}^n$ for each $n$ and thread the solutions (Hensel). The "fractions/series" picture is for computation; the universal property is for identification.

The construction is the algebraic form of **Cauchy completion** in analysis: the metric $d(x,y)=2^{-\sup\{n:x-y\in\mathfrak{a}^n\}}$ makes a sequence Cauchy exactly when its differences sink into ever-higher powers of $\mathfrak{a}$, and $\widehat{R}$ is the completed metric space turned into a ring — $\mathbb{Z}_p$ is literally the metric completion of $\mathbb{Z}$ under $|\cdot|_p$. It is finer than [[Commutative Algebra IV — Localization|localization]]: $R_{\mathfrak{p}}$ keeps a Zariski neighbourhood, $\widehat{R}$ keeps only the formal/infinitesimal neighbourhood, and there is a map $R_{\mathfrak{p}}\to\widehat{R}$ factoring the comparison. In number theory $\mathbb{Z}_p$ is the *other* completion of $\mathbb{Q}$ beside $\mathbb{R}$; in geometry $\widehat{\mathcal{O}_{X,x}}$ is the coordinate ring of the formal disk.

---

# Examples / Corollaries

**Is an instance — the $p$-adic integers.** $R=\mathbb{Z}$, $\mathfrak{a}=(p)$: $\widehat{\mathbb{Z}}^{(p)}=\varprojlim\mathbb{Z}/p^n\mathbb{Z}=\mathbb{Z}_p$. An element is a base-$p$ expansion with infinitely many digits to the left; $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$ injectively because $\bigcap_n(p^n)=0$ in the domain $\mathbb{Z}$. The thread for $-1$ in $\mathbb{Z}_5$ is $(4,24,124,624,\dots)$, i.e. $\dots4444_5$.

**Is an instance — formal power series in one variable.** $R=k[T]$, $\mathfrak{a}=(T)$: $\widehat{k[T]}^{(T)}=\varprojlim k[T]/(T^n)=k[[T]]$. A thread is a compatible family of polynomial truncations, i.e. a single formal power series $\sum a_m T^m$. The element $\sum_m T^m=\frac{1}{1-T}$ lives in $k[[T]]$ but not in $k[T]$ — a limiting element adjoined by completion.

**Is an instance — formal power series in several variables.** $R=k[T_1,\dots,T_n]$, $\mathfrak{a}=(T_1,\dots,T_n)$: then $\mathfrak{a}^i=\mathrm{span}_k\{T_1^{e_1}\cdots T_n^{e_n}:e_1+\cdots+e_n\geq i\}$, so the truncation $R/\mathfrak{a}^i$ keeps monomials of total degree $<i$, and the completion is $k[[T_1,\dots,T_n]]$, the ring of formal power series in $n$ variables — the local ring of the formal disk in $n$-dimensional space.

**Is NOT an instance — completion need not enlarge.** If $\mathfrak{a}$ is nilpotent, say $\mathfrak{a}^N=0$, then $\mathfrak{a}^n=0$ for $n\geq N$, the tower stabilises, and $\widehat{R}=R/\mathfrak{a}^N=R$: completion does nothing because there are no genuinely-limiting threads. More generally $\widehat{R}=R$ exactly when $R$ is already $\mathfrak{a}$-adically complete; completing $\mathbb{Z}_p$ at $(p)$ again gives $\mathbb{Z}_p$.

**Is NOT an instance — the completion map can fail to be injective.** Injectivity is *not* automatic: $\ker\varphi=\bigcap_n\mathfrak{a}^n M$, and without the Noetherian-local hypotheses this can be non-zero. The cleanest failure is non-finitely-generated or non-Noetherian: in $R=\prod_{n\geq1}k$ with $\mathfrak{a}=\bigoplus_n k$ one has $\mathfrak{a}^2=\mathfrak{a}$, so $\bigcap\mathfrak{a}^n=\mathfrak{a}\neq0$, and $\varphi$ kills all of $\mathfrak{a}$. This non-example is exactly what the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]] rules out under its hypotheses.

**Corollary — units of $\widehat{R}$ are detected at level $1$.** For the $\mathfrak{a}$-adic completion, $(r_n)\in\widehat{R}$ is a unit iff $r_1\in R/\mathfrak{a}$ is a unit, because an inverse can be built level by level (geometric series). In $k[[T]]$ this says $f$ is a unit iff $f(0)\neq0$; in $\mathbb{Z}_p$, iff the first $p$-adic digit is non-zero.

**Calibration check.** Verify that the thread condition for $R=\mathbb{Z}$, $\mathfrak{a}=(p)$ is "$r_{n+1}\equiv r_n\pmod{p^n}$", and write the threads for $0,1,-1$ in $\mathbb{Z}_5$. Confirm $\ker\varphi=\bigcap_n\mathfrak{a}^n M$ directly from the inverse-limit definition. Check that for $\mathfrak{a}$ nilpotent the completion is just $R/\mathfrak{a}^N$, and that $\frac{1}{1-T}=\sum T^m\in k[[T]]$ is a unit with inverse $1-T$.

---

# Unlocked by This

> [!tip] The formal disk and complete local rings *(from Algebraic Geometry)*
> Completing the [[Def - Local Ring and Residue Field|local ring]] $\mathcal{O}_{X,x}$ at its maximal ideal gives $\widehat{\mathcal{O}_{X,x}}$, the **complete local ring**, whose spectrum is the **formal neighbourhood** (formal disk) of $X$ at $x$ — an infinitesimal thickening seeing only how $X$ behaves to all orders at the point. A smooth $d$-dimensional point has $\widehat{\mathcal{O}_{X,x}}\cong k[[T_1,\dots,T_d]]$, so completion is the algebraic statement that *every smooth point looks formally like affine space*; a plane node has $k[[x,y]]/(xy)$, the formal picture of two branches crossing. Two singularities are "the same type" precisely when their complete local rings agree, which is why this construction is the foundation of the local classification of singularities and of deformation theory.

> [!tip] Hensel's lemma and Henselian rings *(from Number Theory / Algebraic Geometry)*
> Because $\widehat{R}$ is complete, a simple root of a polynomial modulo $\mathfrak{a}$ lifts to an exact root in $\widehat{R}$ by successive approximation — **Hensel's lemma**, the algebraic implicit function theorem. A ring in which this lifting holds is **Henselian**; complete local rings are Henselian, which is what makes $\mathbb{Z}_p$ and $k[[T]]$ behave like rings of convergent functions and underlies the étale-local structure theory of schemes. The construction on this page is the source of every Henselian ring used in practice.

> [!tip] $p$-adic numbers and the local-global principle *(from Number Theory)*
> Taking fractions of $\mathbb{Z}_p$ gives the **$p$-adic field** $\mathbb{Q}_p$, a complete non-archimedean field with its own analysis; assembling $\mathbb{R}$ and all the $\mathbb{Q}_p$ into the **adeles** turns "solve over $\mathbb{Q}$" into "solve over every completion and glue", the Hasse local-global principle. The $\mathfrak{a}$-adic completion is the first construction on this road, and $v_p$, the $p$-adic valuation, is the [[Def - Discrete Valuation and Valuation Ring|discrete valuation]] whose valuation ring is $\mathbb{Z}_p$.
