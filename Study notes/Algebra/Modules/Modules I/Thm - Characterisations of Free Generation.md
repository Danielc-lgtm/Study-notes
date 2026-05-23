---
type: theorem
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Module Homomorphism"
  - "Def - Finitely Generated Module"
  - "Def - Free Module"
  - "Def - Direct Sum of Modules"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a commutative ring with identity and $M$ is an [[Def - Module|R-module]]. A finite subset $S = \{m_1, \dots, m_k\} \subseteq M$ is in play throughout. The subset $S$ **generates** $M$ if $M = Rm_1 + \dots + Rm_k = \{\sum_i r_i m_i : r_i \in R\}$, i.e. every element of $M$ is an $R$-linear combination of the $m_i$ (see [[Def - Finitely Generated Module|finitely generated module]]). The subset $S$ is **linearly independent** if $\sum_i r_i m_i = 0$ forces $r_1 = \dots = r_k = 0$. The subset $S$ **generates $M$ freely** if it generates $M$ and, in addition, every set function $\psi : S \to N$ to any $R$-module $N$ extends to an $R$-module homomorphism $\theta : M \to N$ (this extension, when it exists, is automatically unique — see Why Is It True); a module admitting such a generating set is a [[Def - Free Module|free module]] and $S$ is a **basis**. A [[Def - Module Homomorphism|module homomorphism]] is a map of abelian groups commuting with the $R$-action. The full symbol registry is on the parent page [[Modules I — §3.1–3.2]].

---

# Statement

> **Characterisations of Free Generation.** Let $R$ be a commutative ring, $M$ an $R$-module, and $S = \{m_1, \dots, m_k\}$ a finite subset of $M$. The following are equivalent.
>
> 1. $S$ **generates $M$ freely** — $S$ generates $M$, and every set function $\psi : S \to N$ to an $R$-module $N$ extends to an $R$-module homomorphism $\theta : M \to N$.
> 2. $S$ **generates $M$ and is linearly independent**.
> 3. **Every element of $M$ is uniquely expressible** as $r_1 m_1 + \dots + r_k m_k$ with $r_i \in R$.
>
> A finite subset satisfying any (hence all) of these is a **basis**, and a module possessing a basis is **free**.

---

# Motivation

You have just defined the [[Def - Free Module|free module]] through a property that looks unlike anything from linear algebra: $S$ generates $M$ *freely* if every set function out of $S$ — an utterly unconstrained assignment of an element of $N$ to each $m_i$ — extends to a genuine module homomorphism $M \to N$. This is the *universal property* of a basis, and it is the right definition for deep reasons (it is what makes "free" mean "free", with no relations imposed). But it is an uncomfortable definition to *check*: to verify it directly you would have to consider all set functions into all [[Def - Module|modules]] $N$ at once.

Meanwhile, from linear algebra you carry a completely different mental picture of a basis: a spanning set that is linearly independent, equivalently a set in which every vector has *unique* coordinates. These conditions are concrete and finite — you can test linear independence by solving one equation; you can test uniqueness by comparing two expansions. The trouble is that they are stated in coordinate language and say nothing, on their face, about [[Def - Homomorphism|homomorphisms]].

This theorem reconciles the two pictures. It proves that the abstract universal property (i) and the two concrete linear-algebra conditions (ii) and (iii) describe *exactly the same finite subsets*. So you may *define* free generation by the universal property — which is what makes the free module behave correctly in proofs and constructions — and yet *recognise* a basis the way you always have, by spanning plus independence, or by uniqueness of coordinates. The theorem is a translation dictionary between "the categorical way to say basis" and "the linear-algebra way to say basis".

There is a sharper reason the dictionary matters here, and the source is blunt about it. In linear algebra, every spanning set *contains* a basis: if a spanning set is dependent, you discard redundant vectors until what is left is independent. **In modules this is false.** The source's example is $\{2, 3\} \subseteq \mathbb{Z}$: the set $\{2,3\}$ generates $\mathbb{Z}$ (because $\gcd(2,3) = 1$), yet it is *not* independent, since $3 \cdot 2 + (-2) \cdot 3 = 0$ — and you cannot fix this by throwing an element away, because *neither* $2$ alone *nor* $3$ alone generates $\mathbb{Z}$. So a generating set can fail to be a basis with no basis hiding inside it. This means the equivalence (i)$\iff$(ii)$\iff$(iii) is not a free lunch inherited from vector spaces: free generation is a genuine, checkable, *all-or-nothing* property of a specific finite set, and the theorem is what tells you the three ways of testing it agree. It is also why "free" is a real restriction on modules — the source notes $\mathbb{Z}/2\mathbb{Z}$ is not a free $\mathbb{Z}$-module at all — whereas over a field every module is free.

---

# Sources and Targets

**Sources (Input Broadening)**

Each of the three equivalent conditions is a different *entry point*: the theorem's value is that whichever form a problem hands you, you may immediately switch to whichever form is easiest to use.

The disguised source feeding **(i), the universal property**, is **any situation where you must build a homomorphism out of $M$**. If you know $S$ generates $M$ freely, then to construct a module homomorphism $M \to N$ you need only *decide where each $m_i$ goes* — any choice whatsoever extends, uniquely. The non-obvious recognition is that "I need a homomorphism out of $M$, and $M$ is free on $S$" reduces an infinite verification (respecting all of $M$'s structure) to a finite *free* choice (one image per basis element). *Example problem:* given a free module $M$ on $\{m_1, \dots, m_k\}$ and arbitrary targets $n_1, \dots, n_k \in N$, assert without further ado that the homomorphism $m_i \mapsto n_i$ exists — this is exactly how the projection in the proof below is built.

The disguised source feeding **(ii), spanning plus independence**, is **a generating set you suspect has no relations**. Independence is the most mechanically checkable of the three: set one linear combination to zero and see whether the coefficients are forced to vanish. The non-obvious recognition is that establishing this *one* equation, together with spanning, certifies the *full* universal property of (i) — you get the categorical strength of a basis from a single independence check. *Example problem:* the standard generators $e_1, \dots, e_k$ of $R^k$ are visibly a spanning set, and $\sum r_i e_i = (r_1, \dots, r_k) = 0$ forces all $r_i = 0$, so by (ii)$\Rightarrow$(i) they freely generate $R^k$ — establishing $R^k$ is free with no need to verify any universal property by hand.

The disguised source feeding **(iii), uniqueness of expansion**, is **a module whose elements come with canonical coordinates**. Whenever a module is presented so that each element has one and only one coordinate tuple — polynomials written in the monomial basis, tuples in $R^k$, formal $R$-linear combinations of an indexing set — condition (iii) holds *by inspection of the presentation*. The non-obvious recognition is that "this object is described by unique coordinates" is *itself* the statement that the coordinate set is a basis. *Example problem:* the monomials $1, X, \dots, X^{n}$ form a basis of the $R$-module of polynomials of degree $\leq n$, because every such polynomial has unique coefficients — condition (iii) verbatim.

**Targets (Output Amplification)**

The conclusion is an isomorphism of three properties. Combining it with other facts produces structural payoffs.

Combine **the equivalence with the existence of a basis of size $k$**. If $M$ has a basis of size $k$, then by (i) the universal property gives, for any $R$-module $N$, a bijection between $R$-module homomorphisms $M \to N$ and set functions $\{m_1, \dots, m_k\} \to N$, i.e. between $\operatorname{Hom}_R(M, N)$ and $N^k$. Taking $N = R$ this says the dual $\operatorname{Hom}_R(M, R) \cong R^k$. The further result is that free modules of finite rank are self-dual in this precise sense; this is non-obvious because the universal property is a statement about *all* targets at once, yet specialising the target manufactures concrete identifications.

Combine **the equivalence with [[Thm - Finitely Generated Modules and Surjections from a Free Module|the free-quotient theorem]]**. A basis of size $k$ means $M \cong R^k$ (the universal property builds mutually inverse homomorphisms between $M$ and $R^k$ matching bases). Every [[Def - Finitely Generated Module|finitely generated]] module is then a quotient of such a free module, $M \cong R^k/K$. The further result: free modules are the "coordinate patches" out of which all finitely generated modules are assembled by quotienting — and the theorem is what licenses calling a spanning-independent set a coordinate system.

Combine **(iii), uniqueness, with the failure of basis extraction**. Uniqueness of expansion is a *rigid* condition: it can hold for one generating set and fail for another generating set of the *same* module. The further result, made concrete by $\{2,3\} \subseteq \mathbb{Z}$, is that being a basis is a property of the *set*, not merely of the module — so the theorem must be applied to a specific candidate set, never to "the module" abstractly. This is the precise sense in which module bases are subtler than vector-space bases.

---

# Why Is It True

Hold the three conditions side by side and notice they are three views of the single phenomenon: *the coordinate map is a bijection*.

A finite set $S = \{m_1, \dots, m_k\}$ that generates $M$ gives a surjective "coordinate" map $R^k \to M$, $(r_1, \dots, r_k) \mapsto \sum r_i m_i$ — surjective is exactly what "generates" means. The three conditions are three ways of saying this surjection is *also injective*, i.e. an isomorphism.

**(ii) $\iff$ (iii)** is the easiest pairing, and the source says outright that it is "the same as what we know from linear algebra". Two expansions $\sum r_i m_i$ and $\sum r_i' m_i$ of the same element are equal exactly when their difference $\sum (r_i - r_i') m_i$ is zero. So *uniqueness of expansion* (iii) — no element has two different coordinate tuples — is literally the same statement as *the only way to write $0$ is with all-zero coefficients* (independence, the non-trivial half of (ii)); spanning is common to both. In coordinate-map language: (iii) says the coordinate map is injective, (ii) says its kernel is trivial, and for a homomorphism those are the same thing.

The interesting pairing is **(i) $\iff$ (ii)**, and here is the intuition for each direction.

*(i) $\Rightarrow$ (ii): a free generating set cannot have a relation.* Suppose, for contradiction, that $S$ generates freely but is dependent — there is a relation $r_1 m_1 + \dots + r_k m_k = 0$ with some coefficient, say $r_1$, non-zero. The universal property lets you build a homomorphism that *detects* this relation and exposes the contradiction. Send $m_1$ to $1 \in R$ and every other $m_i$ to $0 \in R$ — a perfectly legal set function $S \to R$, hence (by freeness) it extends to a homomorphism $\theta : M \to R$. Now apply $\theta$ to the relation: the left side, $\theta(0)$, is $0$; the right side, $\theta(\sum r_i m_i) = \sum r_i \theta(m_i)$, collapses to $r_1 \cdot 1 = r_1$ because $\theta$ kills every $m_i$ with $i \neq 1$. So $r_1 = 0$ — contradicting the choice of relation. The moral: freeness is so strong that it lets you build a "coordinate-reading" homomorphism that would be impossible if there were any relation, because the relation would force the coordinate functional to assign two values to the same element.

*(ii) $\Rightarrow$ (i): unique coordinates let you define the extension by formula.* Suppose $S$ generates $M$ and is independent — equivalently (by (ii)$\iff$(iii)) every element of $M$ has unique coordinates. You must show an arbitrary set function $\psi : S \to N$ extends to a homomorphism. There is only one possible candidate, and uniqueness of coordinates is exactly the licence to *write it down*: define
$$\theta(r_1 m_1 + \dots + r_k m_k) = r_1 \psi(m_1) + \dots + r_k \psi(m_k).$$
This is *well-defined* precisely because each element of $M$ has *one* coordinate tuple $(r_1, \dots, r_k)$ — without uniqueness, two tuples for the same element could give two different right-hand sides and $\theta$ would be ill-defined. Granted well-definedness, $\theta$ is a homomorphism because the coordinates of a sum are the sum of coordinates and the coordinates of $r \cdot x$ are $r$ times the coordinates (the coordinate map is itself a homomorphism), so the formula respects both operations. And $\theta$ extends $\psi$ because $m_i$ has coordinate tuple $e_i$, so $\theta(m_i) = \psi(m_i)$. The moral: **a basis is exactly a coordinate system, and a coordinate system is exactly what lets you define a map by specifying it on coordinates** — uniqueness of coordinates is the well-definedness of "define $\theta$ by its values on the $m_i$".

Finally, the *uniqueness* of the extension (mentioned in the definition) is itself forced and worth seeing: if $\theta_1$ and $\theta_2$ both extend $\psi$, then $\theta_1 - \theta_2$ is a homomorphism killing every element of $S$, so it kills the entire [[Def - Submodule|submodule]] generated by $S$ — which is $M$. Hence $\theta_1 = \theta_2$. Generation alone forces uniqueness; freeness is the extra promise that *some* extension exists.

---

# What Makes This Hard

The (ii)$\iff$(iii) equivalence is routine linear algebra, so the entire difficulty concentrates in (i)$\iff$(ii), and specifically in *using the universal property as a tool rather than a passive description*. In (i)$\Rightarrow$(ii) the non-obvious step is realising you must *manufacture a homomorphism* — the coordinate functional $m_1 \mapsto 1, m_i \mapsto 0$ — purely to extract a contradiction from a relation; people get stuck waiting for a homomorphism to be given instead of building one. In (ii)$\Rightarrow$(i) the non-obvious step is that the *formula* for $\theta$ is forced, and the entire content of the proof is the *well-definedness* check; the most common error is to write down the formula and call $\theta$ "obviously a homomorphism" while skipping the verification that it does not depend on the choice of coordinate tuple — which is the one place uniqueness of expansion is used.

---

# Rederivation Scaffold

**High-level strategy:**
Prove the cycle by closing two implications and citing one. Treat (ii)$\iff$(iii) as the linear-algebra fact it is (uniqueness of expansion = trivial kernel of the coordinate map). Then prove (i)$\Rightarrow$(ii) by *contraposition* — build a coordinate functional that turns a relation into a contradiction — and (ii)$\Rightarrow$(i) by *defining the extension on coordinates* and checking it is well-defined.

**Subgoal decomposition:**

1. **(ii) $\iff$ (iii).** Show: $S$ generates and is independent $\iff$ every element has a unique expansion.
   - *Hint:* Two expansions of one element are equal if and only if their difference is a relation; uniqueness $\iff$ the only relation is the zero one. Spanning is shared.
   - *Why needed:* Lets the rest of the proof freely use whichever of (ii), (iii) is convenient; (iii) supplies the well-definedness in step 3.

2. **(i) $\Rightarrow$ (ii).** Assume $S$ generates $M$ freely. Show $S$ is independent.
   - *Hint:* Suppose a relation $\sum r_i m_i = 0$ with $r_1 \neq 0$. Use freeness to extend the set function $m_1 \mapsto 1_R$, $m_i \mapsto 0$ ($i \neq 1$) to $\theta : M \to R$; apply $\theta$ to the relation to get $r_1 = 0$, a contradiction.
   - *Why needed:* One half of the cycle; shows the universal property forces no relations.

3. **(ii) $\Rightarrow$ (i).** Assume $S$ generates $M$ and is independent. Show $S$ generates freely.
   - *Hint:* Given $\psi : S \to N$, define $\theta(\sum r_i m_i) = \sum r_i \psi(m_i)$. Well-defined by uniqueness of expansion (step 1); a homomorphism because coordinates are additive and $R$-linear; extends $\psi$ since $m_i$ has coordinates $e_i$.
   - *Why needed:* Closes the cycle; shows unique coordinates deliver the universal property.

4. **Assemble.** (i)$\Rightarrow$(ii), (ii)$\Rightarrow$(i), and (ii)$\iff$(iii) together give (i)$\iff$(ii)$\iff$(iii).
   - *Hint:* (i)$\Rightarrow$(ii)$\Rightarrow$(i) is the loop for the first two; (ii)$\iff$(iii) attaches the third.
   - *Why needed:* Produces the full three-way equivalence.

---

# Lemma Decomposition

> [!note]- Lemma 1: Unique expansion is equivalent to spanning plus independence
> **Statement:** Let $S = \{m_1, \dots, m_k\} \subseteq M$. Then "$S$ generates $M$ and is linearly independent" holds if and only if "every element of $M$ is uniquely expressible as $\sum_i r_i m_i$".
>
> **Hint:** The difference of two expansions of the same element is a linear combination equal to $0$.
>
> **Why needed:** It is the (ii)$\iff$(iii) edge of the theorem, and condition (iii) supplies the well-definedness used in Lemma 3.
>
> > [!note]- Full proof
> > Both sides include the assertion that $S$ generates $M$, i.e. that *at least one* expansion exists for every element; so it suffices to show, granting existence, that "independence" is equivalent to "the expansion is unique".
> >
> > ($\Rightarrow$) Assume $S$ is independent. Suppose an element $x \in M$ has two expansions, $x = \sum_i r_i m_i = \sum_i r_i' m_i$. Subtracting, $\sum_i (r_i - r_i') m_i = 0$. By independence every coefficient vanishes: $r_i - r_i' = 0$, i.e. $r_i = r_i'$ for all $i$. So the expansion is unique.
> >
> > ($\Leftarrow$) Assume every element has a unique expansion. The element $0 \in M$ has the expansion $0 = \sum_i 0 \cdot m_i$ with all coefficients zero. If $\sum_i r_i m_i = 0$ is any expansion of $0$, then by uniqueness it must coincide with the all-zero one: $r_i = 0$ for all $i$. So $S$ is independent.

> [!note]- Lemma 2: A free generating set is linearly independent
> **Statement:** If $S = \{m_1, \dots, m_k\}$ generates $M$ freely, then $S$ is linearly independent.
>
> **Hint:** From a hypothetical non-trivial relation, use freeness to build a homomorphism $M \to R$ that reads off the offending coefficient.
>
> **Why needed:** It is the (i)$\Rightarrow$(ii) edge: it shows the universal property forbids relations.
>
> > [!note]- Full proof
> > Suppose, for contradiction, that $S$ is *not* independent. Then there is a relation
> > $$r_1 m_1 + r_2 m_2 + \dots + r_k m_k = 0$$
> > with at least one non-zero coefficient; relabel so that $r_1 \neq 0$.
> >
> > Define a set function $\psi : S \to R$ (with $R$ viewed as a module over itself) by
> > $$\psi(m_1) = 1_R, \qquad \psi(m_i) = 0 \quad \text{for } i \neq 1.$$
> > Because $S$ generates $M$ *freely*, $\psi$ extends to an $R$-module homomorphism $\theta : M \to R$ with $\theta(m_i) = \psi(m_i)$.
> >
> > Apply $\theta$ to the relation. Since $\theta$ is a module homomorphism,
> > $$0 = \theta(0) = \theta\Big(\sum_i r_i m_i\Big) = \sum_i r_i\, \theta(m_i) = r_1 \theta(m_1) + \sum_{i \neq 1} r_i \theta(m_i) = r_1 \cdot 1_R + \sum_{i \neq 1} r_i \cdot 0 = r_1.$$
> > Hence $r_1 = 0$, contradicting $r_1 \neq 0$. Therefore no non-trivial relation exists and $S$ is linearly independent.

> [!note]- Lemma 3: A generating, independent set generates freely
> **Statement:** If $S = \{m_1, \dots, m_k\}$ generates $M$ and is linearly independent, then $S$ generates $M$ freely.
>
> **Hint:** Define the extension by its values on coordinates; uniqueness of expansion (Lemma 1) is exactly what makes the definition unambiguous.
>
> **Why needed:** It is the (ii)$\Rightarrow$(i) edge, closing the cycle.
>
> > [!note]- Full proof
> > Since $S$ generates $M$, the "generates" half of "generates freely" holds. It remains to show every set function $\psi : S \to N$ to an $R$-module $N$ extends to a module homomorphism $\theta : M \to N$.
> >
> > By Lemma 1, every element of $M$ has a *unique* expansion $x = r_1 m_1 + \dots + r_k m_k$. Define
> > $$\theta(x) = \theta(r_1 m_1 + \dots + r_k m_k) := r_1\, \psi(m_1) + \dots + r_k\, \psi(m_k) \;\in N.$$
> >
> > **Well-defined.** The value $\theta(x)$ is computed from the coefficient tuple $(r_1, \dots, r_k)$; by uniqueness of expansion that tuple is determined by $x$ alone, so $\theta(x)$ does not depend on any choice. This is the only place independence is used.
> >
> > **Homomorphism.** Let $x = \sum_i r_i m_i$ and $y = \sum_i s_i m_i$ be the (unique) expansions of two elements, and let $r \in R$. Then $x + y = \sum_i (r_i + s_i) m_i$ and $r \cdot x = \sum_i (r r_i) m_i$ are the (unique) expansions of $x + y$ and $r \cdot x$. Therefore
> > $$\theta(x + y) = \sum_i (r_i + s_i)\psi(m_i) = \sum_i r_i \psi(m_i) + \sum_i s_i \psi(m_i) = \theta(x) + \theta(y),$$
> > $$\theta(r \cdot x) = \sum_i (r r_i)\psi(m_i) = r \sum_i r_i \psi(m_i) = r \cdot \theta(x).$$
> > So $\theta$ is an $R$-module homomorphism.
> >
> > **Extends $\psi$.** The element $m_j$ has expansion $m_j = \sum_i r_i m_i$ with $r_j = 1_R$ and $r_i = 0$ for $i \neq j$. Hence $\theta(m_j) = 1_R \cdot \psi(m_j) + \sum_{i \neq j} 0 \cdot \psi(m_i) = \psi(m_j)$.
> >
> > So $\psi$ extends to the module homomorphism $\theta$, and $S$ generates $M$ freely.

> [!note]- Lemma 4: An extension of a set function on a generating set is unique
> **Statement:** If $S$ generates $M$ and $\theta_1, \theta_2 : M \to N$ are module homomorphisms agreeing on $S$, then $\theta_1 = \theta_2$.
>
> **Hint:** The difference $\theta_1 - \theta_2$ is a homomorphism killing all of $S$, hence killing the submodule $S$ generates.
>
> **Why needed:** It justifies the word "the" in "the extension" — generation alone forces uniqueness of any extension, so freeness only has to supply *existence*.
>
> > [!note]- Full proof
> > Consider $\delta = \theta_1 - \theta_2 : M \to N$, defined by $\delta(x) = \theta_1(x) - \theta_2(x)$; a difference of module homomorphisms is a module homomorphism. For each $m_i \in S$, $\delta(m_i) = \theta_1(m_i) - \theta_2(m_i) = 0$ since $\theta_1, \theta_2$ agree on $S$. Thus $S \subseteq \ker\delta$, and $\ker\delta$ is a submodule of $M$. The smallest submodule containing $S$ is $Rm_1 + \dots + Rm_k = M$ (as $S$ generates $M$), so $M \subseteq \ker\delta \subseteq M$, forcing $\ker\delta = M$. Hence $\delta = 0$ and $\theta_1 = \theta_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be a commutative ring, $M$ an $R$-module, and $S = \{m_1, \dots, m_k\} \subseteq M$ a finite subset. We prove (i) $\Rightarrow$ (ii) $\Rightarrow$ (i) and (ii) $\iff$ (iii); together these give the full equivalence.
>
> ---
> **(ii) $\iff$ (iii).** This is Lemma 1: "$S$ generates $M$ and is linearly independent" holds if and only if "every element of $M$ is uniquely expressible as $\sum_i r_i m_i$". The proof is the linear-algebra argument — two expansions of an element are equal if and only if their difference is a relation, so uniqueness of expansion is equivalent to the only relation being trivial.
>
> ---
> **(i) $\Rightarrow$ (ii).** Assume $S$ generates $M$ freely. By definition this includes that $S$ generates $M$, so only linear independence needs proof; this is Lemma 2. In outline: a non-trivial relation $\sum_i r_i m_i = 0$ with $r_1 \neq 0$ would, via the universal property, extend the set function $m_1 \mapsto 1_R$, $m_i \mapsto 0$ $(i \neq 1)$ to a homomorphism $\theta : M \to R$; applying $\theta$ to the relation yields $0 = \theta(0) = \sum_i r_i \theta(m_i) = r_1$, contradicting $r_1 \neq 0$. So $S$ is independent, and (ii) holds.
>
> ---
> **(ii) $\Rightarrow$ (i).** Assume $S$ generates $M$ and is linearly independent. By definition $S$ generates $M$; it remains to show every set function $\psi : S \to N$ extends to a module homomorphism. This is Lemma 3. In outline: by Lemma 1 every $x \in M$ has a *unique* expansion $x = \sum_i r_i m_i$, so
> $$\theta(x) := \sum_i r_i\, \psi(m_i)$$
> is well-defined (the coefficient tuple is determined by $x$); it is a module homomorphism because coordinates are additive and $R$-linear; and it extends $\psi$ because $m_j$ has coordinate tuple $e_j$, giving $\theta(m_j) = \psi(m_j)$. So $S$ generates $M$ freely, and (i) holds.
>
> (By Lemma 4 this extension $\theta$ is moreover the *unique* homomorphism extending $\psi$, since generation alone forces any two extensions to agree.)
>
> ---
> **Conclusion.** We have shown (i) $\Rightarrow$ (ii), (ii) $\Rightarrow$ (i), and (ii) $\iff$ (iii). Hence (i), (ii), (iii) are equivalent: a finite subset $S$ generates $M$ freely if and only if it generates $M$ and is linearly independent, if and only if every element of $M$ is uniquely an $R$-linear combination of $S$. Such a subset is a basis, and a module with a basis is free. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Proving $R^k$ is free without touching the universal property.** Show that the standard generators $e_1, \dots, e_k$ form a basis of $R^k$. Verifying the universal property directly would mean checking all set functions into all modules; instead use (ii). The $e_i$ visibly span ($\sum r_i e_i = (r_1, \dots, r_k)$), and $\sum r_i e_i = 0$ reads coordinatewise as every $r_i = 0$, so they are independent. By (ii)$\Rightarrow$(i) they freely generate $R^k$. The non-obvious payoff: the entire universal property of $R^k$ — the property that makes $R^k$ the *free* module and underwrites [[Thm - Finitely Generated Modules and Surjections from a Free Module|every surjection Rᵏ twoheadrightarrow M]] — is certified by one trivial independence check.

**Polynomial [[Def - Ring|rings]] as free modules.** Show that the $R$-module $R[X]$ is free with basis the monomials $\{1, X, X^2, \dots\}$ (and the degree-$\leq n$ polynomials are free of rank $n+1$). Use (iii): every polynomial has a unique tuple of coefficients, which is condition (iii) verbatim. The non-obvious recognition is that "a polynomial is determined by its coefficients" — a fact so familiar it is rarely named — is exactly the statement that the monomials are a basis, hence (by the theorem) that $R[X]$ satisfies the universal property of a free module: a module map out of $R[X]$ is a free choice of image for each monomial.

**Detecting non-freeness of a torsion module.** Show $\mathbb{Z}/n\mathbb{Z}$ ($n \geq 2$) is not a free $\mathbb{Z}$-module by exhibiting the failure of (ii). Any single element $m$ satisfies the relation $n \cdot m = 0$ with $n \neq 0$, so no set containing a non-zero element is independent; and $\{0\}$ generates nothing but $0$. By the theorem, no subset can generate freely. The non-obvious application is using the *contrapositive* of (i)$\iff$(ii): to prove the universal property *fails* — a statement about all homomorphisms — it suffices to exhibit *one* relation, because (ii) is equivalent to (i).

**Why a spanning set need not contain a basis.** Analyse $S = \{2, 3\} \subseteq \mathbb{Z}$ as a $\mathbb{Z}$-module. $S$ generates $\mathbb{Z}$ (since $\gcd(2,3)=1$, e.g. $(-1)\cdot 2 + 1 \cdot 3 = 1$) but fails (ii): $3 \cdot 2 + (-2)\cdot 3 = 0$ is a non-trivial relation. By the theorem $S$ is not a basis, and — unlike in a vector space — no sub-collection of $S$ is a basis either, since neither $\{2\}$ nor $\{3\}$ generates $\mathbb{Z}$. The non-obvious point this drills: the theorem characterises a *specific finite set*, and the linear-algebra reflex "discard dependent vectors to reach a basis" is invalid for modules — basis-hood is a rigid property that a generating set may simply lack.

---

# Bridges

- **[[Def - Free Module|Free Module]]** — the object this theorem characterises. The definition takes route (i), the universal property; this theorem proves (i), (ii), (iii) define the same finite subsets, so a free module may be recognised by any of the three. The universal property is the "categorical" definition, while (ii) and (iii) are the linear-algebra definitions.

- **[[Thm - Finitely Generated Modules and Surjections from a Free Module|Finitely Generated Modules as Quotients of Free Modules]]** — the immediate consumer. A basis of size $k$ yields $M \cong R^k$ via the universal property, and that theorem then writes every finitely generated module as a quotient $R^k/K$ of a free module. This theorem certifies that a spanning, independent set is a genuine coordinate system; the free-quotient theorem uses such coordinate systems as the building blocks of all finitely generated modules.

- **Bases of Vector Spaces** — the special case $R = F$ a field. Over a field, (ii) is the textbook definition of a basis (spanning plus independent) and (iii) is the unique-coordinates characterisation. The equivalence (ii)$\iff$(iii) here is *literally* the linear-algebra fact, which the source notes explicitly; what is genuinely new for modules is (i)$\iff$(ii) and the failure of basis extraction from a spanning set — phenomena invisible over a field, where every module is free.

- **[[Thm - Invariance of Rank|Invariance of Rank]]** — the natural follow-up question. Once "basis" is pinned down by this theorem, one asks whether the *number of basis elements* is an invariant of the module; invariance of rank confirms that for $R^n \cong R^m$ over a non-zero commutative ring, $n = m$, so "rank" is well-defined.

- **Universal Properties and Adjoint Functors** — the categorical frame. Condition (i) says the free module on $S$ is the universal recipient of $S$: module homomorphisms out of it correspond to set functions out of $S$. This is the statement that the free-module construction is *left adjoint* to the forgetful functor from $R$-modules to sets — the same pattern as free groups, free rings, and tensor algebras.

---

# Unlocked by This

> [!tip] Projective Modules *(from Homological Algebra)*
> A free module is the universal solution to "extend a map off a generating set"; weakening this — asking only that the module be a direct summand of a free module — gives the notion of a projective module. The equivalence proved here is the prototype the projective definition is measured against, and projectives are exactly the modules for which surjections onto them split.

> [!tip] Smith Normal Form and Canonical Forms *(from Linear Algebra over a PID)*
> Because a basis is a coordinate system, a homomorphism between finite-rank free modules over a ring is a matrix once bases are chosen. When $R$ is a principal ideal domain, changing bases reduces such a matrix to Smith normal form, which decomposes finitely generated modules into cyclic pieces — yielding the classification of finitely generated abelian groups and the rational and Jordan canonical forms of a linear map.
