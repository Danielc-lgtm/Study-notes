---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Unit and Field"
  - "Def - Quotient Ring"
  - "Def - Field of Fractions"
  - "Def - Multiplicative Set and Localization"
  - "Def - Extension and Contraction of Ideals"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. A **local ring** is written $(R, \mathfrak{m})$, giving a name $\mathfrak{m}$ to its unique maximal ideal; $R^\times$ denotes the group of units. For a [[Def - Prime and Maximal Ideal|prime]] $\mathfrak{p} \trianglelefteq R$, the localization $R_{\mathfrak{p}} = (R \setminus \mathfrak{p})^{-1}R$ is the [[Def - Multiplicative Set and Localization|localization at 𝔭]]; its maximal ideal is $\mathfrak{p}R_{\mathfrak{p}} = \mathfrak{p}^e$ (the [[Def - Extension and Contraction of Ideals|extension]] of $\mathfrak{p}$). The **residue field** at $\mathfrak{p}$ is $\kappa(\mathfrak{p}) := R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p})$. We use $\mathfrak{m}, \mathfrak{n}$ for maximal ideals and $\mathfrak{q}$ for a general prime. The full registry is on [[Commutative Algebra IV — Localization]].

This is a compound page: it defines three interlocking notions — a **local ring** $(R, \mathfrak{m})$, the **localization $R_{\mathfrak{p}}$ at a prime** (the universal source of local rings), and the **residue field** $\kappa(\mathfrak{p})$ — because the point of introducing local rings is that $R_{\mathfrak{p}}$ produces one from any prime, and $\kappa(\mathfrak{p})$ is the field of "values at the point" that ties together the two operations $R_{\mathfrak{p}}$ and $R/\mathfrak{p}$.

---

# Axiom Motivation

A local ring is the algebraic embodiment of "one point and its infinitesimal neighbourhood". The single axiom — *exactly one maximal ideal* — looks austere, but it is precisely the condition that makes a ring behave like the ring of functions defined *near a single point*, and everything good about local rings flows from unpacking it.

**Why "exactly one maximal ideal" is the right axiom, and what it really says.** A maximal ideal is the set of functions vanishing at a (closed) point. A ring with many maximal ideals is the ring of functions on a space with many points; a ring with *one* maximal ideal is the ring of functions seeing only *one* point. So the axiom is "the space has a single closed point". Its immediate equivalent reformulation is the operational one you actually use: **in a local ring, the non-units form an ideal — and that ideal is $\mathfrak{m}$.** Here is why. In any ring, an element is a non-unit iff it lies in *some* maximal ideal (a non-unit generates a proper ideal, which sits inside a maximal ideal by Zorn). If there is only one maximal ideal $\mathfrak{m}$, then the non-units are exactly the elements of $\mathfrak{m}$, so $R \setminus \mathfrak{m} = R^\times$. Conversely, if the non-units happen to form an ideal $I$, then $I$ is the unique maximal ideal (any proper ideal consists of non-units, hence lies in $I$). This equivalence — *unique maximal ideal $\iff$ non-units are closed under addition* — is the working definition, because it lets you check locality by adding two non-units and confirming the sum is a non-unit, with no reference to the lattice of ideals.

**Why we strengthen "has a maximal ideal" to "has exactly one".** Every nonzero ring has *at least* one maximal ideal — that is Zorn's lemma and requires no hypothesis. The content of "local" is the uniqueness. Drop uniqueness and you lose the entire payoff: with two maximal ideals $\mathfrak{m}_1 \neq \mathfrak{m}_2$, an element can be a non-unit (lying in $\mathfrak{m}_1$) yet invertible "at the other point" (outside $\mathfrak{m}_2$), and the sum of two non-units need not be a non-unit — for example in $\mathbb{Z}$, the non-units $2$ and $3$ sum to the unit $5$, witnessing that $\mathbb{Z}$ is *not* local. Strengthen the axiom the other way — demand *no* maximal ideal — and you have excluded every nonzero ring. So "exactly one" is the unique non-degenerate choice, and it is the precise amount of structure needed for the residue field $R/\mathfrak{m}$ to be canonically attached to the ring rather than to a choice of point.

**Why $R_{\mathfrak{p}}$ is the universal way to manufacture a local ring.** Local rings would be a curiosity if they were rare. The construction $R_{\mathfrak{p}} = (R\setminus\mathfrak{p})^{-1}R$ makes them ubiquitous: it produces a local ring *from any prime of any ring*. The mechanism is the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]]. Localizing inverts everything *outside* $\mathfrak{p}$, and the primes that survive are exactly those disjoint from $S = R\setminus\mathfrak{p}$, i.e. the primes $\mathfrak{q} \subseteq \mathfrak{p}$. Among these, $\mathfrak{p}$ itself is the largest, so $\mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal — locality is *forced* by the choice of $S$. The geometric reading is exact: inverting the functions that do not vanish at $\mathfrak{p}$ leaves a ring that can only distinguish what happens *at and below* $\mathfrak{p}$, i.e. an arbitrarily small neighbourhood of the point. This is why "localize at a prime" and "pass to a local ring" are the same act, and why local rings are the natural home for *local* questions.

**Why the residue field reconciles $R_{\mathfrak{p}}$ and $R/\mathfrak{p}$.** There are two operations one can perform "at a prime $\mathfrak{p}$", and students chronically confuse them. *Quotienting* by $\mathfrak{p}$ keeps the primes $\supseteq \mathfrak{p}$ — geometrically the subvariety $V(\mathfrak{p})$ *through* the point — and yields a domain $R/\mathfrak{p}$. *Localizing* at $\mathfrak{p}$ keeps the primes $\subseteq \mathfrak{p}$ — geometrically a neighbourhood *of* the point — and yields a local ring $R_{\mathfrak{p}}$. They look opposite, and they are; but they meet in one object, the **residue field** $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$, the field "of values at $\mathfrak{p}$". Because localization commutes with quotients (see [[Thm - Localization Commutes with Quotients and Finite Operations]]), one can compute $\kappa(\mathfrak{p})$ either way: localize then quotient, $R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$, or quotient then take fractions, $\operatorname{Frac}(R/\mathfrak{p})$. They agree. The residue field is therefore the canonical "value field" of the point, and it is a field precisely because $\mathfrak{p}R_{\mathfrak{p}}$ is maximal in $R_{\mathfrak{p}}$.

---

# The Definition

## Local ring

A ring $R$ is **local** if it has exactly one maximal ideal $\mathfrak{m}$. One writes $(R, \mathfrak{m})$. Equivalently (any one of these characterises locality):

1. The set $R \setminus R^\times$ of non-units is an ideal — and it then equals $\mathfrak{m}$.
2. There is a proper ideal $\mathfrak{m}$ containing every non-unit; equivalently $R \setminus \mathfrak{m} \subseteq R^\times$.
3. For all $x \in R$, $x \in R^\times$ or $1 - x \in R^\times$ (a one-element test, given a candidate $\mathfrak{m}$: $x$ a non-unit $\Rightarrow 1+x$ a unit).

The quotient $R/\mathfrak{m}$ is a [[Def - Unit and Field|field]], the **residue field** of the local ring.

## Localization at a prime

For a [[Def - Prime and Maximal Ideal|prime ideal]] $\mathfrak{p} \trianglelefteq R$, the [[Def - Multiplicative Set and Localization|localization]] at $\mathfrak{p}$ is
$$R_{\mathfrak{p}} := (R \setminus \mathfrak{p})^{-1}R = \left\{ \tfrac{r}{s} : r \in R,\ s \notin \mathfrak{p} \right\}.$$
The set $S = R \setminus \mathfrak{p}$ is multiplicative precisely because $\mathfrak{p}$ is prime. Then $(R_{\mathfrak{p}}, \mathfrak{p}R_{\mathfrak{p}})$ is a **local ring**, with unique maximal ideal
$$\mathfrak{p}R_{\mathfrak{p}} = \mathfrak{p}^e = \left\{ \tfrac{a}{s} : a \in \mathfrak{p},\ s \notin \mathfrak{p} \right\},$$
and the primes of $R_{\mathfrak{p}}$ are exactly the $\mathfrak{q}R_{\mathfrak{p}}$ for primes $\mathfrak{q} \subseteq \mathfrak{p}$ of $R$. For a module $M$, $M_{\mathfrak{p}} := (R\setminus\mathfrak{p})^{-1}M$ is a module over the local ring $R_{\mathfrak{p}}$.

## Residue field

The **residue field of $R$ at $\mathfrak{p}$** is the field
$$\kappa(\mathfrak{p}) := R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p}) = (R/\mathfrak{p})_{\mathfrak{p}}.$$
The three descriptions agree because localization commutes with quotients. The map $R \to \kappa(\mathfrak{p})$, $r \mapsto r(\mathfrak{p})$, sends each element to its **value at the point $\mathfrak{p}$**.

---

# Categorical / Structural Definition

A local ring is a ring object with a distinguished "point": the data $(R, \mathfrak{m})$ is equivalently the surjection $R \twoheadrightarrow R/\mathfrak{m} = \kappa$ onto a field, universal among ring maps from $R$ to fields that "see only this point". A **local homomorphism** $(R,\mathfrak{m}) \to (R',\mathfrak{m}')$ is a ring map $\varphi$ with $\varphi(\mathfrak{m}) \subseteq \mathfrak{m}'$ (equivalently $\varphi^{-1}(\mathfrak{m}') = \mathfrak{m}$) — the correct notion of morphism, because it is the one geometry forces: a map of pointed spaces must send the point to the point, and on functions that is $\mathfrak{m} \mapsto \mathfrak{m}'$.

The localization $R_{\mathfrak{p}}$ has a universal property as a local ring: among all *local* $R$-algebras $(A, \mathfrak{m}_A)$ receiving a local map from $R$ "centred at $\mathfrak{p}$" (i.e. $\mathfrak{m}_A$ contracts to $\mathfrak{p}$), the ring $R_{\mathfrak{p}}$ is initial. Equivalently, $R \to R_{\mathfrak{p}}$ is the universal map inverting everything *not* in $\mathfrak{p}$, by the [[Thm - Universal Property of Localization|universal property of localization]]. The structural slogan: **$R_{\mathfrak{p}}$ is the stalk of $\operatorname{Spec} R$'s structure sheaf at the point $\mathfrak{p}$**, the colimit of the rings $R_f$ over all $f \notin \mathfrak{p}$ (all neighbourhoods of $\mathfrak{p}$), and $\kappa(\mathfrak{p})$ is the field of germs evaluated at the point.

---

# Relate to Other Fields / Compression

The cleanest compression: **a local ring is the ring of functions near a single point, with $\mathfrak{m}$ the functions vanishing there; $R_{\mathfrak{p}}$ manufactures one by inverting every function nonzero at $\mathfrak{p}$; and $\kappa(\mathfrak{p})$ is the field of values at the point.**

**True name:** the true name of "local ring" is "**a ring in which the non-units form an ideal**" — equivalently, "you can always invert anything outside $\mathfrak{m}$". This is what you check in practice (add two non-units, stay a non-unit) and what you exploit (Nakayama's lemma, residue-field reductions). The "unique maximal ideal" phrasing is the definition; "non-units form an ideal" is the tool.

This is the precise algebraic analogue of a **germ** in analysis and topology. A germ of a function at a point $x$ is its equivalence class under "agree on some neighbourhood of $x$", and the ring of germs is local: a germ is invertible iff the function is nonzero at $x$, so the non-invertible germs (those vanishing at $x$) form the unique maximal ideal. The localization $R_{\mathfrak{p}}$ *is* the ring of germs of regular functions at $\mathfrak{p}$, and the localization equivalence relation "$u(s_2 r_1 - s_1 r_2) = 0$ for some $u \notin \mathfrak{p}$" is exactly "the two functions agree on a neighbourhood of $\mathfrak{p}$". In differential geometry the same structure appears as the local ring $C^\infty_x$ of germs of smooth functions, whose maximal ideal $\mathfrak{m}_x$ and quotient $\mathfrak{m}_x/\mathfrak{m}_x^2$ give the cotangent space — the cotangent-space construction of [[Commutative Algebra V — Nakayama's Lemma|Nakayama's chapter]] is the same idea in algebra.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}_{(p)}$.** With $\mathfrak{p} = (p)$, $\mathbb{Z}_{(p)} = \{\tfrac{a}{b} : p \nmid b\} \subseteq \mathbb{Q}$ is local with maximal ideal $(p)\mathbb{Z}_{(p)} = \{\tfrac{a}{b} : p \mid a,\ p \nmid b\}$. Its units are the fractions $\tfrac{a}{b}$ with $p \nmid a$ and $p \nmid b$; everything else is in $\mathfrak{m}$. The residue field is $\kappa((p)) = \mathbb{Z}_{(p)}/(p)\mathbb{Z}_{(p)} = \mathbb{F}_p$, recovering "the value mod $p$".

**Is an instance — every field, and the formal power series ring.** A field $k$ is local with $\mathfrak{m} = (0)$ and $\kappa = k$. The power series ring $k[[X]]$ is local with $\mathfrak{m} = (X)$: a power series is a unit iff its constant term is nonzero, so the non-units (zero constant term) form the ideal $(X)$, and $\kappa = k[[X]]/(X) = k$. This is the local ring of a smooth point on a curve.

**Is an instance — the residue field computed two ways.** For $R = k[X,Y]$ and $\mathfrak{p} = (Y)$ (a non-maximal prime, the $X$-axis), $R/\mathfrak{p} = k[X]$ is a domain, and $\kappa(\mathfrak{p}) = \operatorname{Frac}(k[X]) = k(X)$ — the *function field of the axis*, a field of transcendence degree $1$, not a finite field. The same field arises as $R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$. The residue field at a generic point is a function field, not a number field.

**Is NOT an instance — $\mathbb{Z}$ is not local.** The integers have infinitely many maximal ideals $(p)$, and the non-units do not form an ideal: $2$ and $3$ are non-units but $2 + 3 = 5$ is... still a non-unit, but $2$ and $-1$ are non-unit and unit, while $4$ and $-3$ are both non-units summing to the unit $1$. Concretely $4, -3 \notin \mathbb{Z}^\times$ yet $4 + (-3) = 1 \in \mathbb{Z}^\times$, so the non-units are not closed under addition. To study $\mathbb{Z}$ near one prime, you *must* localize: $\mathbb{Z}_{(p)}$ is local, $\mathbb{Z}$ is not.

**Is NOT an instance — $R/\mathfrak{p}$ is generally not local.** Confusing $R_{\mathfrak{p}}$ with $R/\mathfrak{p}$: for $R = k[X,Y]$, $\mathfrak{p} = (0)$ (the zero ideal, prime since $R$ is a domain), $R/\mathfrak{p} = R = k[X,Y]$ has *many* maximal ideals — it is the whole plane, not local. By contrast $R_{(0)} = \operatorname{Frac}(R) = k(X,Y)$ *is* local (it is a field). Quotient by $\mathfrak{p}$ and localize at $\mathfrak{p}$ are opposite operations.

**Corollary — calibration via Nakayama-readiness.** In a local ring $(R,\mathfrak{m})$, a finitely generated module $M$ has $M = \mathfrak{m}M \Rightarrow M = 0$ ([[Commutative Algebra V — Nakayama's Lemma|Nakayama]]), and a set $x_1,\dots,x_n \in M$ generates $M$ iff its images span the $\kappa$-vector space $M/\mathfrak{m}M$. This is the single most useful consequence of locality and the reason local rings are where module theory simplifies.

**Calibration check.** Verify that $R_{\mathfrak{p}}$ is local by exhibiting its unique maximal ideal as $\mathfrak{p}R_{\mathfrak{p}}$ and checking that any $\tfrac{r}{s}$ with $r \notin \mathfrak{p}$ is a unit (its inverse is $\tfrac{s}{r}$). Confirm that in $\mathbb{Z}_{(p)}$ the non-units form an ideal but in $\mathbb{Z}$ they do not (find two non-units summing to a unit). Finally compute $\kappa((p))$ for $\mathbb{Z}$ both as $\mathbb{Z}_{(p)}/(p)\mathbb{Z}_{(p)}$ and as $\operatorname{Frac}(\mathbb{Z}/(p))$, confirming both give $\mathbb{F}_p$.

---

# Unlocked by This

> [!tip] The stalk of the structure sheaf and the local ring of a point *(from Algebraic Geometry)*
> $R_{\mathfrak{p}}$ is the **stalk** $\mathcal{O}_{\operatorname{Spec} R, \mathfrak{p}}$ of the structure sheaf at the point $\mathfrak{p}$: the ring of germs of regular functions defined on *some* neighbourhood of $\mathfrak{p}$, two functions identified when they agree near $\mathfrak{p}$. Its maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$ is the germs vanishing at the point. A scheme is, by definition, a locally ringed space whose stalks are local rings, and the morphisms are *local* homomorphisms — so the entire category of schemes is built on the local rings this page constructs. The local ring of a point captures the *local geometry*: whether the point is smooth or singular, the dimension and embedding dimension, the multiplicity, are all read off $R_{\mathfrak{p}}$.

> [!tip] The cotangent space and the Zariski tangent space *(from Algebraic Geometry / Differential Geometry)*
> For a local ring $(R, \mathfrak{m})$ with residue field $\kappa = R/\mathfrak{m}$, the quotient $\mathfrak{m}/\mathfrak{m}^2$ is a $\kappa$-vector space, the **cotangent space** at the point, and its dual is the **Zariski tangent space** — the algebraic definition of the tangent space at a point of a variety, valid even at singular points. A point is **smooth** exactly when $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2$ equals the dimension of the local ring (a regular local ring). This is developed in [[Commutative Algebra V — Nakayama's Lemma]], where Nakayama's lemma shows a minimal generating set of $\mathfrak{m}$ has size $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2$, matching the smooth-manifold count of coordinate functions.

> [!tip] Residue fields and the points of a scheme *(from Algebraic Geometry)*
> The residue field $\kappa(\mathfrak{p})$ is the field in which a function takes its *value* at the point $\mathfrak{p}$, and a $K$-point of $\operatorname{Spec} R$ (for a field $K$) is a ring map $R \to K$, equivalently a prime $\mathfrak{p}$ together with an embedding $\kappa(\mathfrak{p}) \hookrightarrow K$. Over a non-algebraically-closed field the residue fields can be nontrivial extensions of the base — this is how arithmetic geometry encodes, e.g., that the closed point $(X^2+1)$ of $\operatorname{Spec}\mathbb{R}[X]$ has residue field $\mathbb{C}$, a "point with two conjugate geometric points hidden inside it".
