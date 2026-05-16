---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Module Homomorphism"
  - "Def - Finitely Generated Module"
  - "Def - Direct Sum of Modules"
  - "Def - Ring"
  - "Def - Unit and Field"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a fixed ring (commutative, with $1$, unless stated otherwise) and all modules are left $R$-modules. Lowercase $m, n$ with subscripts denote module elements; lowercase $r, s$ with subscripts denote ring elements. A subset $S \subseteq M$ is a set of module elements; an expression $\sum_{i} r_i m_i$ with $r_i \in R$ and $m_i \in S$ is an **$R$-linear combination**. The standard free module is $R^n = R \oplus \cdots \oplus R$, the [[Def - Direct Sum of Modules|direct sum]] of $n$ copies of $R$, with **standard basis** $e_1, \dots, e_n$ where $e_i = (0, \dots, 0, 1, 0, \dots, 0)$ carries $1$ in slot $i$. A **set function** $S \to N$ is a map of underlying sets with no algebraic structure required; a **module homomorphism** (written $M \to N$ as an $R$-module map) respects addition and the $R$-action. The full notation registry lives on the parent page [[Modules I — §3.1–3.2]].

---

# Axiom Motivation

The thing we are chasing is the module-theoretic version of a **basis** — a subset of a module so well-behaved that the entire module is captured by it, the way a basis of a vector space captures the whole space. In linear algebra a basis is a spanning, linearly independent set, and its decisive payoff is this: to define a linear map out of the space, you may send the basis vectors *anywhere you like* and the map is then determined and exists. A module is an [[Def - Module|abelian group with a ring acting on it]], "linear algebra over a ring instead of a field", and we would dearly like the same payoff. The trouble is that over a general ring the comfortable linear-algebra picture collapses, and the free module is the definition that isolates exactly the modules for which it survives.

To see why a definition is even needed, watch the linear-algebra picture break. Over a field, any spanning set contains a basis: if a spanning set is dependent, some vector is a combination of the others and may be discarded, and repeating this prunes down to an independent spanning set. Over a ring this fails. Take $R = \mathbb{Z}$ and the module $\mathbb{Z}$ itself. The set $\{2, 3\}$ generates $\mathbb{Z}$, since $3 \cdot 1 + (-1) \cdot 2 \cdot 1 = 1$ — more plainly $(-1)\cdot 2 + 1 \cdot 3 = 1$ — yet it is not independent, because $3 \cdot 2 + (-2) \cdot 3 = 0$ is a nontrivial relation. The linear-algebra reflex says discard a redundant generator; but neither $2$ nor $3$ generates $\mathbb{Z}$ on its own — $\langle 2 \rangle$ and $\langle 3 \rangle$ are proper submodules. You cannot prune a dependent generating set down to a basis. Generating and being-a-basis have come apart, and "spanning + independent" is no longer a property a generating set can be massaged into. So a basis must be *defined*, as a structural property a module either has or lacks, not a thing always extractable.

Which property, exactly? Reverse-engineer it from the payoff we refuse to give up. We want: a subset $S \subseteq M$ such that **defining a module homomorphism out of $M$ is the same as freely choosing where each element of $S$ goes**. Make that the literal definition. Demand of $S$ that for every $R$-module $N$ and every *set function* $\psi : S \to N$ — a completely arbitrary assignment of a target in $N$ to each element of $S$, with no constraint, the data of "where the basis goes" — there is a [[Def - Module Homomorphism|module homomorphism]] $\theta : M \to N$ extending $\psi$. This is the **existence** half: arbitrary choices on $S$ are always realisable by a genuine homomorphism. Pair it with the obvious requirement that $S$ at least reach all of $M$, i.e. $S$ generates $M$, so the homomorphism is determined on enough elements to matter. A subset with both properties — generates, and every set function off it extends to a homomorphism — is said to **generate $M$ freely**, and a module possessing such a subset is **free**, with that subset its **basis**.

Notice what is *not* in the definition: independence is never mentioned. It is not an axiom; it is a *theorem*. Once $S$ generates freely, $S$ is automatically independent — and here is the argument that forces it, because it shows why the extension property does the work of independence. Suppose, for $S = \{m_1, \dots, m_k\}$ generating $M$ freely, that some relation $r_1 m_1 + \cdots + r_k m_k = 0$ held with, say, $r_1 \neq 0$. Build the set function $\psi : S \to R$ sending $m_1 \mapsto 1_R$ and $m_i \mapsto 0$ for $i \neq 1$. By free generation it extends to a homomorphism $\theta : M \to R$. Now apply $\theta$ to the relation: $0 = \theta(0) = \theta(\sum_i r_i m_i) = \sum_i r_i \theta(m_i) = r_1 \cdot 1_R + 0 + \cdots + 0 = r_1$, contradicting $r_1 \neq 0$. The relation cannot exist; $S$ is independent. The extension property is *strictly stronger* than independence — it knows about all target modules at once — and independence falls out as a free consequence. (Why uniqueness of the extension also comes free: if $\theta_1, \theta_2$ both extend $\psi$, then $\theta_1 - \theta_2$ kills every element of $S$, so $S \subseteq \ker(\theta_1 - \theta_2)$; but a kernel is a [[Def - Submodule|submodule]], and the submodule generated by $S$ is all of $M$, so $\ker(\theta_1 - \theta_2) = M$ and $\theta_1 = \theta_2$.)

Now test the calibration — what breaks under perturbation. *Weaken* the definition by asking only that $S$ generate $M$ (drop the extension property): then $\{2,3\} \subseteq \mathbb{Z}$ qualifies, and we have already seen $\mathbb{Z}$ has the relation $3 \cdot 2 - 2 \cdot 3 = 0$, so the set function $2 \mapsto 1, 3 \mapsto 0$ would force $0 = \theta(3\cdot 2 - 2 \cdot 3) = 3 \cdot 1 - 2 \cdot 0 = 3 \neq 0$, no extension exists, and the payoff is lost — generating alone is too weak. *Strengthen* the definition by demanding *every* generating set be a basis: then $\mathbb{Z}$ itself, an unmistakably free module with basis $\{1\}$, would be disqualified by its bad generating set $\{2,3\}$ — too strong, it excludes a module we certainly want. The definition is pinned exactly at "*some* subset generates freely", an existential, and that is the calibration: free generation is a property of a *witnessing subset*, and a module is free if at least one such witness exists.

The reason to fix precisely this definition is the theorem it is built to serve, the [[Thm - Characterisations of Free Generation|characterisation of free generation]]: for a finite subset $S = \{m_1, \dots, m_k\}$, the three conditions "$S$ generates $M$ freely", "$S$ generates and is independent", and "every element of $M$ is *uniquely* an $R$-linear combination of $S$" all coincide. The unique-expression form is the working face of a basis — coordinates exist and are unambiguous — and it is *equivalent* to the extension property only because we defined free generation by the extension property. Had we defined "basis" as merely "independent generating set" without insisting such sets exist, or by some condition not equivalent to unique representation, the bridge between "has a basis" and "has well-defined coordinates" would snap. The free module is exactly the module-class on which coordinates exist, maps out are unconstrained choices, and linear algebra still runs.

---

# The Definition

This is a compound definition: it builds **linear independence**, **free generation**, and the **free module with its basis** in sequence, each resting on the previous. Fix a ring $R$ and an $R$-module $M$.

**Linear independence.** A finite subset $\{m_1, m_2, \dots, m_k\} \subseteq M$ is **linearly independent** when the only $R$-linear combination of its elements equal to zero is the trivial one: for $r_1, \dots, r_k \in R$,

$$r_1 m_1 + r_2 m_2 + \cdots + r_k m_k = 0 \quad \Longrightarrow \quad r_1 = r_2 = \cdots = r_k = 0.$$

A subset that is not linearly independent is **linearly dependent**: there is then a relation $\sum_i r_i m_i = 0$ with at least one coefficient $r_i$ nonzero. (For an infinite subset $S$, the condition is imposed on every finite subset of $S$.)

**Free generation.** A subset $S \subseteq M$ **generates $M$ freely** when both of the following hold.

- *(i) Spanning.* $S$ **generates** $M$: the smallest [[Def - Submodule|submodule]] of $M$ containing $S$ is $M$ itself; equivalently, every element of $M$ is a finite $R$-linear combination of elements of $S$.
- *(ii) Universal extension property.* For **every** $R$-module $N$ and **every** set function $\psi : S \to N$, there exists an $R$-module homomorphism $\theta : M \to N$ with $\theta|_S = \psi$ — that is, $\theta(s) = \psi(s)$ for all $s \in S$.

When (i) and (ii) hold, the extending homomorphism $\theta$ in (ii) is moreover **unique**: if $\theta_1, \theta_2$ both extend $\psi$, their difference $\theta_1 - \theta_2$ vanishes on $S$, hence $S \subseteq \ker(\theta_1 - \theta_2)$; since $\ker(\theta_1 - \theta_2)$ is a submodule and $S$ generates $M$, the kernel is all of $M$, so $\theta_1 = \theta_2$. Thus free generation says precisely: **giving a module homomorphism $M \to N$ is the same as giving a set function $S \to N$** — a homomorphism out of $M$ is an unconstrained, element-by-element choice of where each member of $S$ goes.

**Free module and basis.** An $R$-module $M$ is **free** when it is generated freely by *some* subset $S \subseteq M$. Any such subset $S$ is called a **basis** of $M$. (A module may have many bases; the cardinality common to all of them, when $R$ is nonzero, is the **rank** — see [[Thm - Invariance of Rank|invariance of rank]].)

**Equivalent characterisation.** For a *finite* subset $S = \{m_1, \dots, m_k\} \subseteq M$, the following are equivalent, and any one may serve as the definition of $S$ being a basis (this is the [[Thm - Characterisations of Free Generation|characterisation of free generation]]):

1. $S$ generates $M$ freely;
2. $S$ generates $M$ **and** $S$ is linearly independent;
3. every element of $M$ is **uniquely** expressible as an $R$-linear combination $r_1 m_1 + \cdots + r_k m_k$ with $r_i \in R$.

Form 3 is the working face of a basis: a basis equips $M$ with **coordinates** — the tuple $(r_1, \dots, r_k)$ — and they are unambiguous.

**The standard example.** The module $R^n = R \oplus \cdots \oplus R$, the [[Def - Direct Sum of Modules|direct sum]] of $n$ copies of $R$, is free with **standard basis** $\{e_1, \dots, e_n\}$, where $e_i$ is the tuple with $1_R$ in slot $i$ and $0$ elsewhere. Every $(a_1, \dots, a_n) \in R^n$ is uniquely $\sum_i a_i e_i$, so condition 3 holds. More generally, for any set $S$ the **free module on $S$**, written $R^{(S)}$, is the direct sum of copies of $R$ indexed by $S$ — the tuples $(r_s)_{s \in S}$ with only finitely many nonzero entries — and $S$, identified with the standard tuples, is its basis.

---

# Categorical Definition

The free module is the prime example of a structure defined by a **universal property**: free generation, condition (ii) above, *is* a universal property, stated directly. A universal property characterises an object by how maps behave around it, and pins it down up to unique isomorphism. Here is the free module's, phrased categorically.

The free module on a set $S$ is an $R$-module $F$ together with a set function $\eta : S \to F$ (the inclusion of $S$ as the basis) which is **universal among modules receiving a set function from $S$**. That is: for every $R$-module $N$ and every set function $f : S \to N$, there is a **unique** $R$-module homomorphism $\bar f : F \to N$ with $\bar f \circ \eta = f$.

$$
\begin{array}{ccc}
S & \xrightarrow{\ \ \eta\ \ } & F \\[2pt]
 & {\scriptstyle f}\searrow & \big\downarrow{\scriptstyle \exists !\, \bar f} \\[2pt]
 & & N
\end{array}
$$

Read the diagram: any way of placing the elements of $S$ into a module $N$ factors *uniquely* through the placement of $S$ into $F$. The set function $f$ carries no structure; the homomorphism $\bar f$ carries all of it; the universal property says the structure-free choice determines the structured map, and conversely. This is exactly free generation: $S$ (via $\eta$) generates $F$ freely.

The slogan is a **bijection of Hom-sets**, natural in $N$:

$$\operatorname{Hom}_R(F,\ N) \ \cong \ \operatorname{Hom}_{\mathbf{Set}}(S,\ N), \qquad \bar f \longmapsto \bar f \circ \eta.$$

Module homomorphisms *out of* the free module are the same thing as plain functions out of its basis. In categorical language the free-module construction $S \mapsto R^{(S)}$ is a **functor** $\mathbf{Set} \to R\text{-}\mathbf{Mod}$ that is **left adjoint to the forgetful functor** $R\text{-}\mathbf{Mod} \to \mathbf{Set}$ which discards the module structure and returns the underlying set: the Hom-set bijection above is the adjunction. "Free" is the generic name, across all of algebra, for the left adjoint to a forgetful functor — free groups, free monoids, polynomial rings as free commutative algebras — and the free module is that pattern for modules.

How does this relate to the concrete definition? They are the *same statement*. Free generation as defined above is "$S$ generates and every set function off $S$ extends uniquely to a homomorphism", which is verbatim the universal property with $\eta$ the inclusion $S \hookrightarrow M$. And the universal property's connection to the [[Def - Direct Sum of Modules|direct sum]] is exact: the free module $R^{(S)} = \bigoplus_{s \in S} R$ inherits its universal property from the direct sum's *maps-out* (coproduct) universal property, specialised to every summand being $R$. A map out of $\bigoplus_{s} R$ is a choice of map $R \to N$ per summand; a map $R \to N$ is a choice of image for $1 \in R$; so a map out of $R^{(S)}$ is a choice of one element of $N$ per $s \in S$ — which is a set function $S \to N$. The free module is the direct sum of copies of $R$, and its universal property is the direct sum's, read through "a homomorphism $R \to N$ is an element of $N$".

---

# Relate to Other Fields / Compression

A free module is, when $R = k$ is a **field**, exactly a **vector space with a chosen basis** — and the reason every vector space is free is the same reason every vector space has a basis. Over a field, condition 2 of the characterisation is always achievable: take any spanning set and prune dependent vectors until independent, the pruning step legitimate because over a field a dependent vector is genuinely a combination of the others *and removing it preserves spanning*. So every $k$-module is free, every vector space has a basis, and the theory of vector spaces is precisely the theory of free $R$-modules with $R$ a field. Module theory over a general ring is "linear algebra where not every module has a basis", and the free modules are the ones where the vector-space intuition still holds without correction.

A free module on a set $S$ is, in the broader pattern of universal algebra, **the same construction as the free group on $S$, the free monoid on $S$, or the polynomial ring $R[x_s : s \in S]$** as the free commutative $R$-algebra. In each case "free on $S$" is the left adjoint to the forgetful functor: the object built so that maps out of it are unconstrained set functions out of $S$, with no relations imposed beyond those the axioms force. The free module is this pattern in the category of $R$-modules; the free abelian group on $S$ is the special case $R = \mathbb{Z}$, namely $\mathbb{Z}^{(S)}$.

One sharp compression: **a free module is a direct sum of copies of the ring**. Everything else is consequence. $R^{(S)} = \bigoplus_{s \in S} R$; the basis is the family of standard tuples; the universal property is the direct sum's coproduct property with all summands $R$; the rank is the number of copies. The single non-formal input is the [[Thm - Invariance of Rank|invariance of rank]], that the number of copies is an isomorphism invariant — true for $R$ nonzero, proved by reducing modulo a maximal ideal to the field case. Free $=$ "$\bigoplus R$" is the whole content.

The contrast that defines the concept: **over a general ring, most modules are not free.** The obstruction is **torsion**. An element $m$ of an $R$-module is a torsion element if $r m = 0$ for some nonzero $r \in R$; a basis element can never be torsion, since $\{m\}$ being part of a basis forces $r m = 0 \Rightarrow r = 0$. So any module with a torsion element it cannot avoid is non-free. The $\mathbb{Z}$-module $\mathbb{Z}/2$ is the cleanest case: its only nonzero element $1$ satisfies $2 \cdot 1 = 0$, every element is torsion, and there is no torsion-free element to be a basis vector — $\mathbb{Z}/2$ is not free. Freeness is special; it is exactly the absence of any obstruction to coordinatising the module.

---

# Examples / Corollaries

**Is an instance: $R^n$, the standard free module.** The [[Def - Direct Sum of Modules|direct sum]] $R^n = R \oplus \cdots \oplus R$ is free with basis $\{e_1, \dots, e_n\}$, the standard tuples. Every element $(a_1, \dots, a_n)$ is uniquely $\sum_i a_i e_i$, so characterisation 3 holds outright. For $R = \mathbb{Z}$ this is the free abelian group $\mathbb{Z}^n$ of rank $n$; for $R = k$ a field it is the coordinate space $k^n$. This is the template every free module is isomorphic to (for finite bases): a free module of rank $n$ is *defined up to isomorphism* as a module isomorphic to $R^n$.

**Is an instance: every vector space, over any field $k$.** A module over a field is a vector space, and every vector space has a basis — obtained by pruning any spanning set down to an independent one, a step legitimate over a field. Hence **every module over a field is free.** This is the precise sense in which "free module" generalises "vector space": the free modules are exactly the modules for which the existence-of-a-basis theorem, automatic over a field, continues to hold over a general ring.

**Is an instance: $R$ itself, as a module over itself.** The ring $R$ is a free $R$-module of rank $1$, with basis the singleton $\{1_R\}$: every $r \in R$ is uniquely $r \cdot 1_R$. This is the $n = 1$ case of $R^n$, and it is the reason "a homomorphism $R \to N$ is an element of $N$" — the image of the basis element $1_R$ — which is the building block of the whole free-module universal property.

**Is NOT an instance: the $\mathbb{Z}$-module $\mathbb{Z}/2$.** The cyclic group of order $2$, regarded as a $\mathbb{Z}$-module, is **not free.** The argument isolates the extension property. Any generating set of $\mathbb{Z}/2$ must (after discarding $0$) be the singleton $S = \{1\}$, since $1$ generates and $0$ generates nothing. If $S$ generated freely, the set function $\psi : S \to \mathbb{Z}$ sending $1 \mapsto 1$ would extend to a $\mathbb{Z}$-module homomorphism $\theta : \mathbb{Z}/2 \to \mathbb{Z}$. But $0 = 1 + 1$ in $\mathbb{Z}/2$, so a homomorphism must send it to $\theta(1) + \theta(1) = 1 + 1 = 2$; yet a homomorphism sends $0$ to $0$. From $2 = 0$ in $\mathbb{Z}$, false, no such $\theta$ exists, and $\mathbb{Z}/2$ is not free. The underlying reason is **torsion**: $2 \cdot 1 = 0$ with $2 \neq 0$, and a basis element can carry no such relation.

**Is NOT an instance: $\mathbb{Q}$ as a $\mathbb{Z}$-module.** The rationals under addition form a $\mathbb{Z}$-module that is torsion-*free* — no nonzero rational satisfies $n q = 0$ — yet still **not free**, which shows torsion-freeness is necessary but not sufficient for freeness over $\mathbb{Z}$. If $\mathbb{Q}$ had a basis $S$, then $|S| \geq 2$ is impossible: any two rationals $a, b$ are $\mathbb{Z}$-dependent, since $a = p/q$, $b = r/s$ give the nontrivial relation $(ps)\cdot a - (rq) \cdot b$... — more carefully, $qa = p$ and $sb = r$ are integers, so $(sr)(qa) - (pq)(sb) = sr p - pq r$, and choosing the relation $(rs q)\,a - (p s)\,b$ — the cleanest statement is that $\mathbb{Q}$ has no two-element independent set because it is **divisible** and not finitely generated. And $|S| = 1$ fails too: a single rational $q$ generates only $\mathbb{Z} q = \{n q : n \in \mathbb{Z}\}$, which is *not* all of $\mathbb{Q}$ (it misses $q/2$). With no basis of any size, $\mathbb{Q}$ is not a free $\mathbb{Z}$-module. The lesson: over a general ring, even torsion-free modules can fail to be free.

**Is NOT an instance (subtle): $\{2, 3\} \subseteq \mathbb{Z}$ is a generating set that is not a basis.** The pair $\{2, 3\}$ *generates* the $\mathbb{Z}$-module $\mathbb{Z}$, since $(-1)\cdot 2 + 1 \cdot 3 = 1$. But it does not generate $\mathbb{Z}$ *freely*: it is linearly dependent, exhibiting the relation $3 \cdot 2 + (-2) \cdot 3 = 0$. By the [[Thm - Characterisations of Free Generation|characterisation]], failing independence means it is not a basis. Crucially — and this is the phenomenon that *forces* "free" to be defined rather than extracted — you **cannot prune** $\{2,3\}$ to a basis: neither $\{2\}$ nor $\{3\}$ generates $\mathbb{Z}$. So $\mathbb{Z}$ is free (basis $\{1\}$) yet possesses a generating set with no basis inside it. Over a field this never happens; over a ring it is routine.

**Corollary (free generation forces independence).** If $S = \{m_1, \dots, m_k\}$ generates $M$ freely, then $S$ is linearly independent. Given a relation $\sum_i r_i m_i = 0$, apply the homomorphism $\theta : M \to R$ extending the set function $m_1 \mapsto 1_R$, $m_i \mapsto 0$ ($i \neq 1$): then $r_1 = \sum_i r_i \theta(m_i) = \theta(\sum_i r_i m_i) = \theta(0) = 0$, and likewise every $r_j = 0$. *Calibration check:* reproducing this confirms you see why the extension property is strictly stronger than independence — it has independence as a corollary.

**Corollary (a homomorphism out of a free module is its values on a basis).** If $M$ is free with basis $S$, a module homomorphism $M \to N$ is determined by, and freely specifiable as, an arbitrary set function $S \to N$. In particular $\operatorname{Hom}_R(R^n, N) \cong N^n$ via $\theta \mapsto (\theta(e_1), \dots, \theta(e_n))$. *Calibration check:* this is the universal property restated, and it is the single most-used fact about free modules — every construction of a map out of $R^n$ is an instance.

**Corollary (every module is a quotient of a free module).** For any module $M$, pick a generating set $S$ (for instance $S = M$); the free module $R^{(S)}$ on $S$ admits, by the universal property applied to the inclusion $S \hookrightarrow M$, a surjective homomorphism $R^{(S)} \twoheadrightarrow M$. If $M$ is [[Def - Finitely Generated Module|finitely generated]] this can be done with $R^k$ for finite $k$ — this is the [[Thm - Finitely Generated Modules and Surjections from a Free Module|surjection theorem]]. *Calibration check:* this shows free modules are the "presentations" through which every module is reached, and it is the gateway to [[Def - Finitely Presented Module|finitely presented modules]].

---

# Unlocked by This

> [!tip] Finitely Presented Module *(from Modules I — §3.2)*
> A surjection $R^k \twoheadrightarrow M$ from a free module exhibits $M$ by *generators*; its kernel records the *relations*. When that kernel is itself finitely generated, $M$ is **finitely presented** — describable by finitely many generators and finitely many relations, a matrix. See [[Def - Finitely Presented Module]].

> [!tip] Invariance of Rank *(from Modules I — §3.2)*
> For free modules to have a well-defined *rank*, the number of basis elements must be an isomorphism invariant: $R^n \cong R^m \Rightarrow n = m$ for $R$ nonzero. The proof reduces modulo a maximal ideal to invariance of dimension for vector spaces. See [[Thm - Invariance of Rank]].

> [!tip] Projective Module *(from Modules II)*
> Free modules are the modules where maps out are unconstrained. Relaxing "is a direct sum of copies of $R$" to "is a direct *summand* of a free module" gives the **projective modules** — the modules through which surjections always lift — the next class out, and the natural home of the lifting property.

> [!tip] Structure Theorem for Modules over a PID *(from Modules II)*
> Over a principal ideal domain, the structure theorem decomposes every finitely generated module as a free part $R^r$ plus cyclic torsion pieces $R/(d_i)$. The free part is exactly the free submodule the module would be if it had no torsion; the theorem measures the failure of freeness by the torsion summands.
