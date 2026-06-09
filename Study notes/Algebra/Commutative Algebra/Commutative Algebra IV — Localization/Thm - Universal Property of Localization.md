---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ring Homomorphism"
  - "Def - Unit and Field"
  - "Def - Multiplicative Set and Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$ (the target ring $B$ in the statement need not be commutative). Let $S$ be the multiplicative closure of a subset $U \subseteq R$, and let $\iota = \iota_{S^{-1}R} : R \to S^{-1}R$, $r \mapsto \tfrac{r}{1}$, be the [[Def - Multiplicative Set and Localization|localization map]]. We write $B^\times$ for the group of units of $B$, $\operatorname{Hom}_{\mathbf{Ring}}(-,-)$ for ring-homomorphism sets, and $\ker\iota$ for the kernel of $\iota$. A morphism $f$ in a category is an **epimorphism** if $g \circ f = h \circ f \Rightarrow g = h$. The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (Universal property of localization; Becker Prop. 4.4).** Let $S$ be the multiplicative closure of a subset $U \subseteq R$. For every ring $B$ and every ring homomorphism $f : R \to B$ such that $f(u) \in B^\times$ for all $u \in U$, there is a **unique** ring homomorphism $h : S^{-1}R \to B$ with $f = h \circ \iota$, given explicitly by
> $$h\!\left(\tfrac{r}{s}\right) = f(s)^{-1} f(r).$$
> The map $\iota$ inverts $S$, and $(S^{-1}R, \iota)$ is determined up to unique isomorphism by this property: if $(A, j)$ is another ring with a map $j : R \to A$ satisfying the same universal property, then $\varphi : S^{-1}R \to A$, $\varphi(\tfrac{r}{s}) = j(s)^{-1}j(r)$, is an isomorphism with $\varphi \circ \iota = j$.

> **Corollary (the universal property as a natural bijection).** For every ring $B$,
> $$\operatorname{Hom}_{\mathbf{Ring}}(S^{-1}R, B) \;\cong\; \{\varphi \in \operatorname{Hom}_{\mathbf{Ring}}(R, B) : \varphi(U) \subseteq B^\times\}, \qquad h \mapsto h \circ \iota.$$

> **Corollary (properties of $\iota$).** (1) $\tfrac{r}{s} = 0 \iff ur = 0$ for some $u \in S$; (2) $\ker\iota = \{r \in R : ur = 0 \text{ for some } u \in S\}$; (3) $\ker\iota = 0 \iff S$ contains no zero-divisor; (4) $\iota$ is always a ring **epimorphism**, but usually not surjective (model: $\mathbb{Z} \hookrightarrow \mathbb{Q}$).

---

# Motivation

The fraction model of $S^{-1}R$ is concrete but parochial: it tells you what the elements *are*, not what the ring *is for*. The universal property fixes this by describing $S^{-1}R$ entirely through its relationship to other rings, and that description is what makes the construction canonical and what you actually use in proofs. The role it plays is the same one the universal property of the tensor product or the quotient plays: it converts every question about *maps out of* the object into a question about *maps out of the simpler object* $R$, subject to a side condition.

The point of building $S^{-1}R$ was to make the elements of $S$ invertible while disturbing $R$ as little as possible. "As little as possible" is exactly a universality statement: $S^{-1}R$ should be the *most economical* ring inverting $S$, meaning any *other* ring $B$ that inverts $S$ (via some $f : R \to B$) must receive a map *from* $S^{-1}R$ accounting for it. The theorem says this is so, and uniquely. So the universal property is not an extra fact about localization — it is the *definition that does not mention fractions*, and the fraction construction is merely one proof that an object with this property exists.

The downstream importance is enormous. To build a homomorphism out of $S^{-1}R$ you never chase fractions and check well-definedness; you produce a map out of $R$ inverting $S$ and read off the extension. To prove two constructions of a localization agree — the fraction model and the quotient model $R[T]/(uT-1)$, say — you show both satisfy the property and invoke uniqueness. And the slightly surprising corollary that $\iota$ is always an *epimorphism* (cancellable on the right) even when far from surjective is what places localization among the "epimorphisms of rings", the maps that, like $\mathbb{Z}\hookrightarrow\mathbb{Q}$, add no new relations a map out of the source could detect.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition $A$ is: *a ring homomorphism $f : R \to B$ that sends $S$ (equivalently $U$) into the units of $B$*. The art is recognising this precondition in disguise.

The first disguised source is **"I want to define a map out of $S^{-1}R$"**. Property $B$: you have a localization as the *source* of a desired homomorphism. The bridge $B \to A$ is to forget the localization and define instead a map $f : R \to B$ from the base ring, then check the one condition $f(S) \subseteq B^\times$. The non-obvious part is that this is *strictly easier* — $R$ is concrete, $S^{-1}R$ is a quotient of formal symbols — and that the side condition is usually trivial to verify. *Example problem:* to define the evaluation $\mathbb{Z}_{(p)} \to \mathbb{F}_p$, define $\mathbb{Z} \to \mathbb{F}_p$ (reduction mod $p$) and check every $b$ with $p \nmid b$ becomes a unit mod $p$ — it does.

The second disguised source is **"I want to prove two rings are isomorphic, one of them a localization"**. Property $B$: a candidate ring $A$ is conjectured equal to $S^{-1}R$. The bridge is to show $A$ *also* receives a universal $S$-inverting map $j : R \to A$; then uniqueness of universal objects hands you the isomorphism $\varphi(\tfrac rs) = j(s)^{-1}j(r)$ for free, with no fraction bookkeeping. The non-obviousness: you prove an isomorphism *without constructing it by hand*. *Example problem:* show $R_f \cong R[T]/(fT-1)$ — both invert $f$ universally, so they are uniquely isomorphic ([[Thm - Localization Commutes with Quotients and Finite Operations|the quotient presentation]]).

The third disguised source is **"$B$ already contains the inverses I need"**. Property $B$: a sub-object or quotient $B$ of some larger ring happens to make every $s \in S$ invertible. The bridge is that the inclusion/projection $f : R \to B$ then automatically inverts $S$, so $S^{-1}R$ maps to $B$. The non-obvious value: localizations appear as *images*, letting you recognise a familiar ring as a localization. *Example problem:* the subring $\{\tfrac{a}{b} : p\nmid b\} \subseteq \mathbb{Q}$ receives $\mathbb{Z} \to \mathbb{Q}$ inverting $\mathbb{Z}\setminus(p)$, so it is $\mathbb{Z}_{(p)}$.

**Targets (Output Amplification)**

The conclusion $C$ is *the existence and uniqueness of $h$ with $h \circ \iota = f$, given by $f(s)^{-1}f(r)$*.

Combine $C$ with **the structure-ring map of an endomorphism ring**. Becker uses exactly this in the construction itself: to make $S^{-1}M$ a module over $S^{-1}R$, one needs a ring map $S^{-1}R \to \operatorname{End}(S^{-1}M)$, and it is produced by applying the universal property to the structure map $\rho : R \to \operatorname{End}(S^{-1}M)$ (which sends $S$ to units because $\tfrac xt \mapsto \tfrac{sx}{t}$ has inverse $\tfrac xt \mapsto \tfrac{x}{st}$). The further result $E$: *$S^{-1}M$ is an $S^{-1}R$-module*, the foundation of everything modular. Nonobvious because the target $B = \operatorname{End}(S^{-1}M)$ is *noncommutative* — and the theorem still applies, which is why the statement allows non-commutative $B$.

Combine $C$ with **"$\iota$ is an epimorphism"**. Two ring maps out of $S^{-1}R$ that agree on the image of $\iota$ must be equal (uniqueness in $C$ with the same $f$). The further result $E$: localization adds no relations detectable downstream, so any equation between elements of $S^{-1}R$ that you can verify after applying any homomorphism, and that holds on $\iota(R)$, holds outright. Nonobvious because epimorphism $\neq$ surjection here — the standard intuition "epi means onto" fails for rings.

Combine $C$ with **flatness/exactness**. Once you know $S^{-1}M \cong S^{-1}R \otimes_R M$ (proved using the module universal property, the analogue of this theorem for modules), the universal property is what identifies localization with *base change along $\iota$*. The further result $E$: localization is an exact, flat functor ([[Thm - Localization is Exact and the Localization is Flat]]). Nonobvious because it turns a property *about morphisms out of $S^{-1}R$* into a property *about the functor $S^{-1}(-)$*.

---

# Why Is It True

The proof writes itself once you ask "what *must* $h$ do?". The compatibility $h \circ \iota = f$ pins down $h$ on the image of $\iota$: $h(\tfrac{r}{1}) = f(r)$. But $\tfrac{r}{s} = \tfrac{r}{1}\cdot(\tfrac{s}{1})^{-1}$ — every fraction is an element of $\iota(R)$ times the inverse of another — so $h$ is *forced* everywhere the moment it is forced on $\iota(R)$ and required to respect inverses. Apply $h$ to $\tfrac{s}{1}\cdot\tfrac{1}{s} = 1$: $f(s)\, h(\tfrac1s) = 1$, so $h(\tfrac1s) = f(s)^{-1}$ (legal because $f(s)$ is a unit — *this is where the hypothesis is used*), and then $h(\tfrac rs) = h(\tfrac r1)h(\tfrac1s) = f(r)f(s)^{-1}$. There is no choice: uniqueness is automatic, and existence is just checking this forced formula is well-defined and multiplicative.

**The mechanism in one line: $\tfrac{r}{s} = \iota(r)\cdot\iota(s)^{-1}$, so $h$ is determined by $f$ and the requirement to invert $S$, and the only thing that can go wrong — dividing by $f(s)$ — is exactly what the hypothesis $f(S)\subseteq B^\times$ prevents.**

Well-definedness is the one substantive check: if $\tfrac{r_1}{s_1} = \tfrac{r_2}{s_2}$ then some $t \in S$ has $t s_2 r_1 = t s_1 r_2$ in $R$; apply $f$ and divide by the *units* $f(t)f(s_1)f(s_2)$ to get $f(s_1)^{-1}f(r_1) = f(s_2)^{-1}f(r_2)$. The clearing factor $t$ from the localization equivalence relation becomes, under $f$, a unit you can cancel — the fraction relation and the unit hypothesis are perfectly matched.

The uniqueness-of-the-universal-object half is the standard abstract-nonsense argument: challenge $S^{-1}R$ with $j$ to get $\varphi$, challenge $A$ with $\iota$ to get $\psi$, and observe $\psi\varphi$ solves the same challenge as $\operatorname{id}_{S^{-1}R}$, so by uniqueness $\psi\varphi = \operatorname{id}$, and symmetrically — the two maps are mutually inverse. This is why *any* object satisfying a universal property is unique up to unique isomorphism: the property determines the object as a representing object.

The epimorphism corollary is the same uniqueness read differently: if $g, h : S^{-1}R \to B$ agree on $\iota(R)$, then both extend the single map $g\iota = h\iota$, so by uniqueness $g = h$. Cancellability is just "uniqueness of the extension".

---

# What Makes This Hard

The conceptual hurdle is *not* the proof — which is forced — but believing that "maps out of $S^{-1}R$" and "maps out of $R$ inverting $S$" are the same data, and reaching for that translation instead of manipulating fractions. The one non-obvious technical point is recognising that the hypothesis $f(S) \subseteq B^\times$ is used in exactly two places: to make $f(s)^{-1}$ meaningful (existence) and to cancel $f(t)f(s_1)f(s_2)$ in the well-definedness check. The most common error is to think $\iota$ epimorphism implies $\iota$ surjective — it does not, and $\mathbb{Z}\hookrightarrow\mathbb{Q}$ is the standing counterexample.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Force the formula for $h$ from the compatibility condition and the requirement to invert $S$; this gives both the candidate $h(\tfrac rs) = f(s)^{-1}f(r)$ and its uniqueness. Then verify the forced formula is well-defined (using the unit hypothesis to cancel the clearing factor) and a ring homomorphism. For uniqueness of $(S^{-1}R, \iota)$ as a universal object, run the standard two-challenge argument.

**Subgoal decomposition:**

1. **Force the formula.** Show any valid $h$ must satisfy $h(\tfrac rs) = f(s)^{-1}f(r)$.
   - *Hint:* $h(\tfrac r1) = f(r)$ from $h\iota = f$; then $h(\tfrac1s) = f(s)^{-1}$ from $h(\tfrac s1)h(\tfrac1s)=1$ and $f(s)$ a unit; multiply.
   - *Why needed:* simultaneously gives uniqueness and the only candidate for existence.

2. **Well-definedness.** Show the formula respects $\tfrac{r_1}{s_1}=\tfrac{r_2}{s_2}$.
   - *Hint:* the relation gives $ts_2 r_1 = ts_1 r_2$; apply $f$ and divide by the units $f(t)f(s_1)f(s_2)$.
   - *Why needed:* without it $h$ is not a function; this is the one place beyond formal nonsense.

3. **Homomorphism.** Check $h$ preserves $+$, $\cdot$, $1$.
   - *Hint:* mechanical, using $f$ a homomorphism and $f(s)^{-1}$ multiplicative; $h(\tfrac11)=1$.
   - *Why needed:* completes existence.

4. **Uniqueness of the universal object.** Show any $(A,j)$ with the same property is uniquely isomorphic.
   - *Hint:* get $\varphi : S^{-1}R \to A$ and $\psi : A \to S^{-1}R$ from the two universal properties; $\psi\varphi$ and $\operatorname{id}$ both solve "challenge $S^{-1}R$ with $\iota$", so are equal; symmetrically.
   - *Why needed:* makes $S^{-1}R$ canonical, licensing "identify a ring as a localization by checking the property".

---

# Lemma Decomposition

> [!note]- Lemma 1: The extension is forced
> **Statement:** Any ring map $h : S^{-1}R \to B$ with $h\circ\iota = f$ satisfies $h(\tfrac rs) = f(s)^{-1}f(r)$.
>
> **Hint:** Use $\tfrac rs = \tfrac r1 \cdot (\tfrac s1)^{-1}$ and that $h$ preserves products and the unit.
>
> **Why needed:** It is uniqueness *and* it produces the only possible existence candidate in one stroke.
>
> > [!note]- Full proof
> > From $h\circ\iota = f$, $h(\tfrac r1) = f(r)$ for all $r$, and in particular $h(\tfrac s1) = f(s)$. In $S^{-1}R$ we have $\tfrac s1 \cdot \tfrac1s = \tfrac11 = 1$, so applying the homomorphism $h$: $f(s)\, h(\tfrac1s) = 1$. Since $f(s) \in B^\times$ by hypothesis, multiply on the left by $f(s)^{-1}$ to get $h(\tfrac1s) = f(s)^{-1}$. Finally $\tfrac rs = \tfrac r1\cdot\tfrac1s$, so $h(\tfrac rs) = h(\tfrac r1)\,h(\tfrac1s) = f(r)f(s)^{-1} = f(s)^{-1}f(r)$ (the last equality because $B$ may be noncommutative but $f(s)^{-1}$ and $f(r)$ — we keep the order $f(s)^{-1}f(r)$ as stated). Hence $h$ is uniquely determined.

> [!note]- Lemma 2: The forced formula is well-defined
> **Statement:** If $\tfrac{r_1}{s_1} = \tfrac{r_2}{s_2}$ in $S^{-1}R$ then $f(s_1)^{-1}f(r_1) = f(s_2)^{-1}f(r_2)$.
>
> **Hint:** Pull the fraction equality back to an honest equation in $R$ with a clearing factor $t \in S$, apply $f$, and cancel the units.
>
> **Why needed:** Defines $h$ as a genuine function; the only step using the localization equivalence relation.
>
> > [!note]- Full proof
> > By the [[Def - Multiplicative Set and Localization|definition of equality of fractions]], $\tfrac{r_1}{s_1} = \tfrac{r_2}{s_2}$ means there is $t \in S$ with $t(s_2 r_1 - s_1 r_2) = 0$, i.e. $t s_2 r_1 = t s_1 r_2$ in $R$. Apply $f$: $f(t)f(s_2)f(r_1) = f(t)f(s_1)f(r_2)$. Each of $f(t), f(s_1), f(s_2)$ lies in $B^\times$ (as $t, s_1, s_2 \in S$), so multiply both sides by $f(t)^{-1}f(s_1)^{-1}f(s_2)^{-1}$ to obtain $f(s_1)^{-1}f(r_1) = f(s_2)^{-1}f(r_2)$, as required.

> [!note]- Lemma 3: Uniqueness of a universal object
> **Statement:** If $(A, j)$ also satisfies the universal property, there is a unique isomorphism $\varphi : S^{-1}R \to A$ with $\varphi\circ\iota = j$.
>
> **Hint:** Use each object's universal property to produce maps both ways, then show the round trips are identities by uniqueness.
>
> **Why needed:** It is what lets you *identify* an unknown ring as $S^{-1}R$ by verifying the property — the second source above.
>
> > [!note]- Full proof
> > Challenge $S^{-1}R$ with the $S$-inverting map $j : R \to A$: the universal property of $S^{-1}R$ gives a unique $\varphi : S^{-1}R \to A$ with $\varphi\circ\iota = j$. Challenge $A$ with $\iota : R \to S^{-1}R$ (which inverts $S$): the universal property of $A$ gives a unique $\psi : A \to S^{-1}R$ with $\psi\circ j = \iota$. Then $\psi\circ\varphi\circ\iota = \psi\circ j = \iota$, so $\psi\circ\varphi$ is a solution to "challenge $S^{-1}R$ with $\iota$"; but $\operatorname{id}_{S^{-1}R}$ is also such a solution, and the solution is unique, so $\psi\circ\varphi = \operatorname{id}_{S^{-1}R}$. Symmetrically $\varphi\circ\psi = \operatorname{id}_A$. Hence $\varphi$ is an isomorphism; its formula is $\varphi(\tfrac rs) = j(s)^{-1}j(r)$ by Lemma 1 applied with $f = j$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : R \to B$ be a ring homomorphism with $f(u) \in B^\times$ for all $u \in U$. Since the units of $B$ are closed under products and contain $1$, $f$ sends the entire multiplicative closure $S$ of $U$ into $B^\times$.
>
> **Step 0 — $f$ inverts all of $S$, not just $U$.** Any $s \in S$ is a finite product $u_1\cdots u_n$ of elements of $U$, so $f(s) = f(u_1)\cdots f(u_n) \in B^\times$. Good: the formula below never divides by a non-unit.
>
> **Existence and uniqueness of $h$.** Define $h(\tfrac rs) := f(s)^{-1}f(r)$. By Lemma 2 this is well-defined (independent of the chosen representative). It is a ring homomorphism: $h(\tfrac11) = f(1)^{-1}f(1) = 1$; for products, $h(\tfrac{r_1}{s_1}\cdot\tfrac{r_2}{s_2}) = h(\tfrac{r_1r_2}{s_1s_2}) = f(s_1s_2)^{-1}f(r_1r_2) = f(s_2)^{-1}f(s_1)^{-1}f(r_1)f(r_2)$, which equals $h(\tfrac{r_1}{s_1})h(\tfrac{r_2}{s_2})$ (using commutativity of $R$ so that $f(s_1)^{-1}f(r_1)f(s_2)^{-1}f(r_2)$ rearranges correctly via $f$ of commuting elements); addition is checked the same way after clearing to a common denominator. And $h(\iota(r)) = h(\tfrac r1) = f(1)^{-1}f(r) = f(r)$, so $h\circ\iota = f$. Uniqueness is Lemma 1: any $h$ with $h\circ\iota = f$ is forced to equal this formula.
>
> **The natural bijection.** The assignment $h \mapsto h\circ\iota$ sends $\operatorname{Hom}(S^{-1}R, B)$ into $\{\varphi : R\to B : \varphi(U)\subseteq B^\times\}$ (since $h\circ\iota$ inverts $U$ because $\iota$ does and $h$ preserves units). It is injective because $\iota$ has dense image in the sense that a map out of $S^{-1}R$ is determined by its restriction to $\iota(R)$ (Lemma 1), and surjective because every such $\varphi$ extends (existence). Hence it is a bijection, natural in $B$.
>
> **Uniqueness of $(S^{-1}R, \iota)$.** This is Lemma 3.
>
> **The corollaries on $\iota$.** From the [[Def - Multiplicative Set and Localization|fraction model]]: $\tfrac r1 = \tfrac01 \iff \exists u\in S,\ u r = 0$, giving $\ker\iota = \{r : ur = 0,\ \exists u\in S\}$ and hence $\ker\iota = 0 \iff S$ has no zero-divisor. For the epimorphism claim, suppose $g, h : S^{-1}R \to B$ satisfy $g\circ\iota = h\circ\iota =: f$. Then both $g$ and $h$ are ring maps out of $S^{-1}R$ extending $f$ along $\iota$, and the uniqueness just proved forces $g = h$. So $\iota$ is right-cancellable, i.e. an epimorphism; it is not surjective in general, as $\mathbb{Z}\hookrightarrow\mathbb{Q}$ shows. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Field of fractions as the maximal localization.** For a domain $R$, $\operatorname{Frac}(R) = (R\setminus\{0\})^{-1}R$, and the universal property specialises to: every injection of $R$ into a field extends uniquely to $\operatorname{Frac}(R)$. So $\operatorname{Frac}(R)$ is the smallest field containing $R$ — the universal property *is* the defining property of the field of fractions ([[Thm - Existence of the Field of Fractions]]). Nonobvious recognition: the field-of-fractions universal property students learn in ring theory is the $S = R\setminus\{0\}$ case of this one.

**Inverting a single operator in functional analysis.** Given a commutative Banach algebra and an element $f$ you wish to invert, the algebraic localization $R_f$ models the smallest extension making $f$ invertible; the universal property says any representation sending $f$ to an invertible operator factors through $R_f$. This is the algebraic skeleton beneath the holomorphic functional calculus's handling of the resolvent $(f - \lambda)^{-1}$. Nonobvious because the analytic completion adds structure, but the *algebraic* universal property is exactly localization.

**Gluing the structure sheaf.** In algebraic geometry one must check that the rings $R_f$ on overlapping basic opens $D(f) \cap D(g) = D(fg)$ are compatible. The universal property provides the canonical restriction maps $R_f \to R_{fg}$ (invert $g$ in $R_f$) and proves they satisfy the cocycle condition automatically — the sheaf axioms reduce to uniqueness statements. Nonobvious because it turns a geometric gluing problem into repeated application of one algebraic universal property.

---

# Bridges

- **[[Thm - Universal Property of the Tensor Product of Modules|Universal property of the tensor product]]** — the module analogue. Just as $S^{-1}R$ is universal among rings inverting $S$, the module localization $S^{-1}M$ is universal among $S^{-1}R$-modules receiving an $R$-map from $M$, and the identification $S^{-1}M \cong S^{-1}R\otimes_R M$ realises localization as base change. Both are representing objects for a $\operatorname{Hom}$-functor, and the proof technique — "force the map on generators, then check well-definedness" — is identical.

- **[[Thm - Localization Commutes with Quotients and Finite Operations|Quotient presentation Rꜰ ≅ R[T] over (fT−1)]]** — the cleanest application. Both $R_f$ and $R[T]/(fT-1)$ are universal among rings inverting $f$ (the quotient adds a formal inverse $T = \tfrac1f$ via the relation $fT = 1$), so uniqueness of the universal object identifies them with no fraction computation — see [[Ex - A localization as a quotient R[T] over (uT-1)|the quotient-presentation exercise]].

- **[[Def - Ring Homomorphism|Epimorphisms of rings]]** — the corollary places $\iota$ among ring epimorphisms, the maps right-cancellable in $\mathbf{Ring}$. Unlike sets, groups, or modules, ring epimorphisms need not be surjective: $\mathbb{Z}\hookrightarrow\mathbb{Q}$ is the prototype, and *every* localization map is an example. This is a genuine subtlety of the category of rings.

- **[[Def - Multiplicative Set and Localization|The fraction construction]]** — this theorem is the abstract identity the fractions merely *model*. The fraction model proves *existence* of an object with the property; the universal property is what the object *is*, and is what you use for everything structural.

---

# Unlocked by This

> [!tip] The structure sheaf of an affine scheme *(from Algebraic Geometry)*
> The universal property provides the restriction maps $R_f \to R_{fg}$ that glue the rings of functions on basic opens $D(f)$ into the **structure sheaf** $\mathcal{O}_{\operatorname{Spec} R}$, turning the bare space $\operatorname{Spec} R$ into an **affine scheme**. The sheaf axioms (separation and gluing) become uniqueness statements from the universal property, and compatibility on triple overlaps $D(fgh)$ is automatic. This is the precise mechanism by which "inverting $f$ $=$ restricting to the open set $D(f)$" assembles into a global geometric object, developed fully alongside [[Def - The Prime Spectrum (Spec)]].

> [!tip] Localization as a left adjoint / flat base change *(from Homological Algebra)*
> The natural bijection $\operatorname{Hom}(S^{-1}R, B) \cong \{R\to B \text{ inverting } S\}$ exhibits localization as the **left adjoint** to the inclusion of $S$-inverting algebras, and the module version $S^{-1}M \cong S^{-1}R\otimes_R M$ makes it a **flat base change**. This is the entry point to computing $\operatorname{Tor}$ and $\operatorname{Ext}$ locally: because localization is an exact left adjoint, it commutes with these derived functors, so homological invariants can be computed one prime at a time — the homological face of the [[Thm - The Local-Global Principle|local–global principle]].
