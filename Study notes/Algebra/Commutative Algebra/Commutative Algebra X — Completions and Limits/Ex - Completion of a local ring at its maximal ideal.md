---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Local Ring and Residue Field"
  - "Def - Noetherian Ring"
  - "Def - Direct and Inverse Limits"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $(R,\mathfrak{m})$ be a [[Def - Local Ring and Residue Field|local ring]] and $\widehat{R}=\widehat{R}^{\,\mathfrak{m}}=\varprojlim_n R/\mathfrak{m}^n$ its [[Def - The I-adic Completion|\mathfrak{m}-adic completion]]. Prove:

1. **(Maximal ideal.)** $\widehat{R}$ is a local ring with maximal ideal $\widehat{\mathfrak{m}}=\ker\big(\widehat{R}\to R/\mathfrak{m}\big)=\mathfrak{m}\widehat{R}$; an element of $\widehat{R}$ is a unit iff its image in $R/\mathfrak{m}$ is non-zero.
2. **(Residue field unchanged.)** The completion has the *same* residue field: $\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$.
3. **(Examples.)** Identify the completions $\widehat{\mathbb{Z}_{(p)}}=\mathbb{Z}_p$ and $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$, and observe that completion is invisible to the residue field but resolves the infinitesimal structure (it makes the ring complete and Henselian).

Throughout, assume $R$ is Noetherian where needed (so that $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ are finite-dimensional and $R\hookrightarrow\widehat{R}$).

**Recall:**

![[Def - Local Ring and Residue Field#The Definition]]

A [[Def - Local Ring and Residue Field|local ring]] $(R,\mathfrak{m})$ has a unique maximal ideal $\mathfrak{m}$; then $R^\times=R\setminus\mathfrak{m}$ and the residue field is $R/\mathfrak{m}$.

![[Def - The I-adic Completion#The Definition]]

The $\mathfrak{m}$-adic completion is $\widehat{R}=\varprojlim R/\mathfrak{m}^n$; the completion map $\varphi:R\to\widehat{R}$ is injective when $R$ is Noetherian (since $\bigcap\mathfrak{m}^n=0$ by [[Thm - The Krull Intersection Theorem|Krull]]).

---

# Convergent Strategy

**Problem class.** This is a *compare-completion-with-the-original-ring* problem, the fifth target type of the chapter. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, completion and localization are both "pass to a more local ring", and the comparison questions — same residue field? finer? what is $\widehat{\mathfrak{m}}$? — are settled by tracking what happens to $\mathfrak{m}$ and the quotients $R/\mathfrak{m}^n$.

**Assumption pattern.** The trigger is *a local ring being completed at its own maximal ideal*. The decisive structural fact is that $\widehat{R}\to R/\mathfrak{m}$ (the level-$1$ projection) is surjective with a kernel $\widehat{\mathfrak{m}}$ that turns out to be the *unique* maximal ideal, because everything outside it is a unit. The locality of $\widehat{R}$ is inherited from the locality of $R$ via the unit criterion.

**Theorem routing.** The route is: (1) show $x\in\widehat{R}$ is a unit iff $x\bmod\mathfrak{m}\neq0$, by inverting level-by-level (geometric series) exactly as for $\mathbb{Z}_p$ and $k[[T]]$, so the non-units form the single ideal $\widehat{\mathfrak{m}}$ — this is [[Def - The I-adic Completion|"units detected mod \mathfrak{a}"]]; (2) the level-$1$ projection induces $\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$ since truncating the completion to order $1$ recovers $R/\mathfrak{m}$ ([[Thm - The Inverse Limit and Completeness|Lemma 2]]); (3) the examples are instances of [[Ex - The p-adic integers as an inverse limit]] and [[Ex - The formal power series ring as a completion]] with $R$ already local.

**Key decision point.** The non-obvious content is that completion *enlarges the unit group but not the residue field*. One might expect that adding all the limiting elements changes the "value at the point", but the residue field $R/\mathfrak{m}$ is order-$1$ data, and completion only adds higher-order ($\mathfrak{m}^n$, $n\geq2$) information. So the point looks identical ($\widehat{R}/\widehat{\mathfrak{m}}=R/\mathfrak{m}$) while its infinitesimal neighbourhood is resolved into a complete, Henselian ring. Recognising that the residue field is "order-$1$" and hence untouched is the key insight.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise units by their residue (operation 9).** $x\in\widehat{R}$ is a unit iff $x\bmod\mathfrak{m}\neq0$; inverse built level by level.

2. **Reduce modulo $\mathfrak{m}^n$ and take the limit (operation 3).** Locality and the residue-field identity are checked at the finite levels $R/\mathfrak{m}^n$, then lifted.

3. **Transport finiteness through the safety package (operation 7).** $R$ Noetherian $\Rightarrow\widehat{R}$ Noetherian and $R\hookrightarrow\widehat{R}$, used to make $\widehat{R}$ a well-behaved local ring.

4. **Present a completion as a power-series quotient (operation 8).** $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$, the formal disk of the plane at the origin.

---

# Hints

> [!note]- Hint 1
> Mimic the $\mathbb{Z}_p$ proof. Show $x=(x_n)\in\widehat{R}$ is a unit iff $x_1\in R/\mathfrak{m}$ is non-zero, by building the inverse $y=(y_n)$ with $x_n y_n\equiv1\pmod{\mathfrak{m}^n}$ inductively.

> [!note]- Hint 2
> If the non-units are exactly the set where $x_1=0$ — i.e. the kernel $\widehat{\mathfrak{m}}$ of the projection $\widehat{R}\to R/\mathfrak{m}$ — then $\widehat{\mathfrak{m}}$ is the *unique* maximal ideal (every proper ideal consists of non-units, hence lies in $\widehat{\mathfrak{m}}$). That is locality.

> [!note]- Hint 3
> The residue field: the level-$1$ projection $\widehat{R}\to R/\mathfrak{m}$ is surjective with kernel $\widehat{\mathfrak{m}}$, so $\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$. Completion adds no order-$0$ information.

> [!note]- Hint 4
> $\mathbb{Z}_{(p)}$ is already local with maximal ideal $p\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$; its $\mathfrak{m}$-adic completion is $\varprojlim\mathbb{Z}_{(p)}/p^n\mathbb{Z}_{(p)}=\varprojlim\mathbb{Z}/p^n=\mathbb{Z}_p$, with the *same* residue field $\mathbb{F}_p$.

---

# Solution

The proof transports the unit criterion from $\mathbb{Z}_p$ to a general complete local ring: an element is a unit iff its residue is non-zero, so the non-units form a single maximal ideal $\widehat{\mathfrak{m}}$. The residue field is order-$1$ data, untouched by completion. The examples are the two model cases.

**Step 1: $\widehat{R}$ is local with maximal ideal $\widehat{\mathfrak{m}}=\mathfrak{m}\widehat{R}$.**

$x\in\widehat{R}$ is a unit iff its image in $R/\mathfrak{m}$ is non-zero; the non-units form the unique maximal ideal $\widehat{\mathfrak{m}}=\ker(\widehat{R}\to R/\mathfrak{m})$.

> [!note]- Derivation
> Write $x=(x_n)\in\widehat{R}=\varprojlim R/\mathfrak{m}^n$, so $x_n\in R/\mathfrak{m}^n$ and $x_{n+1}\equiv x_n\pmod{\mathfrak{m}^n}$. Let $\bar{x}=x_1\in R/\mathfrak{m}$ be the residue.
>
> *If $\bar{x}\neq0$,* then $x_1\in(R/\mathfrak{m})^\times$ (a field), so there is $y_1$ with $x_1 y_1=1$ in $R/\mathfrak{m}$. Inductively, suppose $y_n\in R/\mathfrak{m}^n$ with $x_n y_n\equiv1\pmod{\mathfrak{m}^n}$. Lift to $R/\mathfrak{m}^{n+1}$: write $x_{n+1}y_n=1+e$ with $e\in\mathfrak{m}^n/\mathfrak{m}^{n+1}$ (the error is order $n$). Set $y_{n+1}=y_n(1-e)$; then $x_{n+1}y_{n+1}=(1+e)(1-e)=1-e^2\equiv1\pmod{\mathfrak{m}^{n+1}}$ since $e^2\in\mathfrak{m}^{2n}\subseteq\mathfrak{m}^{n+1}$. The $y_n$ are compatible, so $y=(y_n)\in\widehat{R}$ and $xy=1$: $x$ is a unit. (This is the geometric-series/Newton correction, identical to the $\mathbb{Z}_p$ case.)
>
> *If $\bar{x}=0$,* then $x\in\widehat{\mathfrak{m}}:=\ker(\pi_1:\widehat{R}\to R/\mathfrak{m})$, a proper ideal, and a unit cannot lie in a proper ideal. So non-units $=\widehat{\mathfrak{m}}$. Any proper ideal of $\widehat{R}$ consists of non-units, hence $\subseteq\widehat{\mathfrak{m}}$, so $\widehat{\mathfrak{m}}$ is the unique maximal ideal and $\widehat{R}$ is local. Finally $\widehat{\mathfrak{m}}=\mathfrak{m}\widehat{R}$: an element with $\bar{x}=0$ has $x_1=0$, so $x\in\widehat{\mathfrak{m}}$ is a thread of elements of $\mathfrak{m}$, expressible as an $\widehat{R}$-combination of generators of $\mathfrak{m}$ (using $R$ Noetherian, $\mathfrak{m}=(t_1,\dots,t_r)$, and $\widehat{R}$-coefficients built level by level).

**Step 2: The residue field is unchanged.**

$\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$.

> [!note]- Derivation
> The level-$1$ projection $\pi_1:\widehat{R}\to R/\mathfrak{m}$, $x=(x_n)\mapsto x_1$, is a surjective ring homomorphism: surjective because any $\bar{a}\in R/\mathfrak{m}$ is the residue of the constant thread $\varphi(a)$ for a lift $a\in R$. Its kernel is $\widehat{\mathfrak{m}}$ by definition. By the first isomorphism theorem,
> $$\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}.$$
> Equivalently, this is [[Thm - The Inverse Limit and Completeness|Lemma 2]] ("$\widehat{R}/\mathfrak{m}^n\widehat{R}\cong R/\mathfrak{m}^n$") at $n=1$: truncating the completion to order $1$ recovers the order-$1$ data $R/\mathfrak{m}$. Completion adds only higher-order ($\geq2$) infinitesimal information, so the value at the point — the residue field — is identical.

**Step 3: The two model examples.**

$\widehat{\mathbb{Z}_{(p)}}=\mathbb{Z}_p$ and $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$, both with residue field unchanged.

> [!note]- Derivation
> *$\mathbb{Z}_{(p)}$.* The localization $\mathbb{Z}_{(p)}=\{\frac{a}{b}:p\nmid b\}$ is local with maximal ideal $\mathfrak{m}=p\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$. Since $\mathbb{Z}_{(p)}/p^n\mathbb{Z}_{(p)}\cong\mathbb{Z}/p^n\mathbb{Z}$ (the elements with denominator prime to $p$ reduce isomorphically mod $p^n$), the completion is
> $$\widehat{\mathbb{Z}_{(p)}}=\varprojlim\mathbb{Z}_{(p)}/p^n\mathbb{Z}_{(p)}=\varprojlim\mathbb{Z}/p^n\mathbb{Z}=\mathbb{Z}_p,$$
> with residue field still $\mathbb{F}_p$. So localization-then-completion at $p$ gives $\mathbb{Z}_p$, the same as completing $\mathbb{Z}$ directly — completion already localizes.
>
> *$k[x,y]_{(x,y)}$.* This is the local ring of the affine plane at the origin, with maximal ideal $\mathfrak{m}=(x,y)$ and residue field $k$. Its $\mathfrak{m}$-adic completion is $k[[x,y]]$ (the localization does not change the $\mathfrak{m}$-adic truncations, since denominators are units mod $\mathfrak{m}^n$), with residue field still $k$. By [[Ex - The formal power series ring as a completion]] this is the formal disk of the plane at the origin — a complete regular local ring of dimension $2$.
>
> *The moral.* In both cases the residue field is untouched ($\mathbb{F}_p$, resp. $k$) while the ring is replaced by its complete, Henselian version. Completion is invisible at order $1$ (the point looks the same) but resolves all higher-order structure: $\mathbb{Z}_{(p)}\subsetneq\mathbb{Z}_p$ and $k[x,y]_{(x,y)}\subsetneq k[[x,y]]$ are dense embeddings into complete rings where Hensel's lemma holds.

> [!note]- Complete formal solution
> **(1)** For $x=(x_n)\in\widehat{R}$ with residue $\bar{x}=x_1$: if $\bar{x}\neq0$, invert level by level via $y_{n+1}=y_n(1-e)$ where $x_{n+1}y_n=1+e$, $e\in\mathfrak{m}^n/\mathfrak{m}^{n+1}$, using $e^2\in\mathfrak{m}^{n+1}$; this builds $x^{-1}\in\widehat{R}$. If $\bar{x}=0$, $x\in\widehat{\mathfrak{m}}=\ker(\widehat{R}\to R/\mathfrak{m})$, a non-unit. So non-units $=\widehat{\mathfrak{m}}$, every proper ideal lies in $\widehat{\mathfrak{m}}$, and $\widehat{R}$ is local with maximal ideal $\widehat{\mathfrak{m}}=\mathfrak{m}\widehat{R}$.
>
> **(2)** The level-$1$ projection $\widehat{R}\to R/\mathfrak{m}$ is surjective (constant threads) with kernel $\widehat{\mathfrak{m}}$, so $\widehat{R}/\widehat{\mathfrak{m}}\cong R/\mathfrak{m}$ — the residue field is unchanged.
>
> **(3)** $\widehat{\mathbb{Z}_{(p)}}=\varprojlim\mathbb{Z}/p^n=\mathbb{Z}_p$ (residue field $\mathbb{F}_p$); $\widehat{k[x,y]_{(x,y)}}=k[[x,y]]$ (residue field $k$). Completion preserves the residue field and produces a complete, Henselian local ring resolving the infinitesimal structure. $\blacksquare$

> [!warning] Illegal but tempting: expecting completion to change the residue field
> Because $\widehat{R}$ is much larger than $R$ (uncountably so for $\mathbb{Z}_p$), one might expect the "value at the point" $\widehat{R}/\widehat{\mathfrak{m}}$ to grow too. It does not: the residue field is *order-$1$ data*, and completion only adds information at orders $\geq2$ (the kernel $\mathfrak{m}/\mathfrak{m}^2,\mathfrak{m}^2/\mathfrak{m}^3,\dots$ of the higher truncations). So $\widehat{R}/\widehat{\mathfrak{m}}=R/\mathfrak{m}$ always. The mistake is to conflate "the ring got bigger" with "the point got richer"; what got richer is the *infinitesimal neighbourhood*, not the point. This is exactly why completion is the tool for *local-analytic* questions (singularity type, Hensel lifting) but says nothing new about the residue field.

---

# Key Takeaways

**Completion preserves the residue field and the maximal ideal's generation, while enlarging the unit group — it resolves infinitesimal structure without moving the point.** The clean statement of "what completion does to a local ring" is: $\widehat{R}/\widehat{\mathfrak{m}}=R/\mathfrak{m}$ and $\widehat{\mathfrak{m}}=\mathfrak{m}\widehat{R}$, but $\widehat{R}$ has many new units (every element with non-zero residue) and many new elements (limiting threads). The point — the residue field — is fixed; the formal neighbourhood is resolved into something complete and Henselian. The trigger to carry: when you complete a local ring, expect the residue field and the *number* of generators of $\mathfrak{m}$ to be invariant (so dimension and embedding dimension are preserved), while completeness and Hensel's lemma are gained. This is why $\widehat{\mathcal{O}_{X,x}}$ has the same residue field and dimension as $\mathcal{O}_{X,x}$ but is far more tractable.

**The unit criterion "non-zero residue" makes every complete local ring local, by the same level-by-level inversion as $\mathbb{Z}_p$.** The locality of $\widehat{R}$ is not assumed — it is proved by showing the non-units form a single ideal, and the proof is the geometric-series correction that inverts any element with invertible residue. This is the unifying mechanism across $\mathbb{Z}_p$, $k[[T]]$, and general complete local rings: "is it a unit?" reduces to a residue check, and the inverse is built as a convergent thread of corrections $y_{n+1}=y_n(1-e)$. The transferable diagnostic: any time you have a complete (or just $\mathfrak{a}$-adically complete) ring, the unit group is "everything with a unit residue", and this single fact gives locality, the structure of the maximal ideal, and the foothold for Hensel's lemma. See the parallel computations in [[Ex - The p-adic integers as an inverse limit]] and [[Ex - The formal power series ring as a completion]].

**Localizing then completing at a prime equals completing directly — completion already includes the localization.** The example $\widehat{\mathbb{Z}_{(p)}}=\mathbb{Z}_p=\widehat{\mathbb{Z}}^{(p)}$ shows that the completion does not care whether you localized first: the $\mathfrak{m}$-adic truncations $R/\mathfrak{m}^n$ are the same as the $\mathfrak{a}$-adic truncations $R_{\mathfrak{p}}/\mathfrak{p}^n R_{\mathfrak{p}}$, because everything outside $\mathfrak{m}$ becomes a unit anyway. The trigger: to compute the completion of a ring at a prime, you may freely localize first (often simplifying to a local ring) without changing the answer; this is the precise sense in which completion is *finer than* localization — it factors through it. The dictionary "$R_{\mathfrak{p}}$ = Zariski-local, $\widehat{R}$ = analytic-local" from the topic page's [[Commutative Algebra X — Completions and Limits#Insights|Insights]] is exactly this containment made concrete.
