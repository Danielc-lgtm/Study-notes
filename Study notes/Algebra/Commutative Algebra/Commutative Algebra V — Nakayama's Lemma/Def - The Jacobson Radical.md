---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Unit and Field"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring. We write $\mathfrak m, \mathfrak n$ for [[Def - Prime and Maximal Ideal|maximal ideals]], $R^\times$ for the group of units, and $\operatorname{mSpec} R$ for the set of all maximal ideals of $R$. The **Jacobson radical** is written $J(R)$. We also write $\operatorname{nil} R = \sqrt{(0)}$ for the [[Def - Radical of an Ideal and the Nilradical|nilradical]], the set of nilpotent elements. For a [[Def - Local Ring and Residue Field|local ring]] we write $(R, \mathfrak m)$. The full registry is on [[Commutative Algebra V — Nakayama's Lemma]].

---

# Axiom Motivation

The Jacobson radical is the answer to a single question: **which elements of $R$ are "invisible" to every residue field?** A maximal ideal $\mathfrak m$ comes with a residue field $R/\mathfrak m$, and the quotient map sends each $r \in R$ to its "value" $r + \mathfrak m$ at that maximal ideal. An element lies in $\mathfrak m$ exactly when its value there is zero. So the elements lying in *every* maximal ideal are the elements whose value is zero at *every* point of $\operatorname{mSpec} R$ — the elements that no residue field can detect. That intersection is $J(R)$, and the definition is forced once you decide you want a name for "uniformly undetectable at all closed points".

Why is this the right notion to isolate, rather than, say, the nilradical $\operatorname{nil} R = \bigcap_{\mathfrak p \text{ prime}} \mathfrak p$? The two differ by which ideals you intersect over — *all primes* for the nilradical, only the *maximal* ones for the Jacobson radical — and the difference matters. The nilradical is the intersection over the whole spectrum and detects genuine nilpotence ($x \in \operatorname{nil} R \iff x^n = 0$). The Jacobson radical intersects over a smaller set, so it is *larger*, $\operatorname{nil} R \subseteq J(R)$, and the extra elements need not be nilpotent. The reason to single out the maximal-ideal version is its behaviour under "$1 - {}$": as the theorem [[Thm - The Jacobson Radical via Units|on this very page's neighbour]] shows, $x \in J(R)$ precisely when $1 - xy$ is a unit for every $y$. That unit-producing property is exactly what [[Thm - Nakayama's Lemma|Nakayama's lemma]] needs, and it is *not* shared by the nilradical's defining property. So the Jacobson radical is defined the way it is because intersecting over maximal ideals — not all primes — is what makes "$1 + (\text{radical})$ is invertible" come out true.

There is a second motivation that explains why the definition is *useful* rather than merely nameable. The whole strategy of commutative algebra is to study a ring through its quotients by maximal ideals (its fields of values) and its localizations (its points). The Jacobson radical is the obstruction to that strategy seeing everything: it is the part of $R$ that *all* the field-of-values quotients agree to ignore. When $J(R) = (0)$ — and one calls such a ring **Jacobson-semisimple** — the maximal ideals "separate" the ring, and an element is determined by its values at closed points; $\mathbb Z$ and $k[x_1,\dots,x_n]$ are like this. When $J(R)$ is large — and the extreme case is a [[Def - Local Ring and Residue Field|local ring]], where there is only one maximal ideal so $J(R) = \mathfrak m$ is as large as a proper ideal can be — the single field of values $R/\mathfrak m$ is blind to a great deal, and that blindness is exactly the room in which Nakayama operates. So the size of $J(R)$ measures how much of the ring is hidden from its closed points, and the usefulness of Nakayama grows with it.

A final point on why no further axioms are wanted. One might ask for $J(R)$ to be defined intrinsically, without reference to maximal ideals — and indeed it can be, by the unit characterisation, which is the content of the companion theorem. But the *intersection-of-maximal-ideals* definition is the one that makes the geometry transparent ("vanishing at all closed points") and that immediately gives $J(R)$ as an ideal (an intersection of ideals is an ideal, with no checking required). Defining it as "$\{x : 1 - xy \in R^\times\ \forall y\}$" would make the unit property a tautology but would obscure the geometric meaning and would require proving that the set is even an ideal. The two descriptions are equivalent, and the convention is to *define* by intersection and *prove* the unit characterisation, exactly because the intersection makes ideal-hood free.

---

# The Definition

Let $R$ be a commutative ring.

The **Jacobson radical** of $R$ is the intersection of all its maximal ideals:
$$J(R) = \bigcap_{\mathfrak m \in \operatorname{mSpec} R} \mathfrak m.$$
By convention, if $R = 0$ there are no maximal ideals and $J(R) = R = 0$. As an intersection of ideals, $J(R)$ is an ideal of $R$, and it is a proper ideal whenever $R \neq 0$ (since each $\mathfrak m$ is proper).

**Equivalent characterisation (proved separately).** $x \in J(R)$ if and only if $1 - xy \in R^\times$ for every $y \in R$; see [[Thm - The Jacobson Radical via Units]].

---

# Relate to Other Fields / Compression

The cleanest compression: **$J(R)$ is "everything that vanishes at every closed point", and it sits one notch above the nilradical, which is "everything that vanishes at every point".** Both are intersections of ideals; the nilradical $\operatorname{nil} R = \bigcap_{\mathfrak p} \mathfrak p$ runs over *all* primes, $J(R) = \bigcap_{\mathfrak m} \mathfrak m$ runs over *maximal* primes only, so $\operatorname{nil} R \subseteq J(R)$ always, with equality in important cases (e.g. finitely generated algebras over a field — these are **Jacobson rings**, where every prime is an intersection of maximal ideals).

**True name:** the true name of $J(R)$ is *not* "the intersection of maximal ideals" but "**the set of $x$ such that $1 + x \cdot (\text{anything})$ is a unit**". This is the form you use in every proof: it is precisely what licenses the inversion in [[Thm - Nakayama's Lemma|Nakayama]], where an element $1 - a$ with $a \in J(R)$ must be a unit. The intersection description is for recognising $J(R)$ in examples; the unit description is for using it.

In the geometric reading, $J(R)$ is the algebraic shadow of the fact that **the closed points may fail to be dense**. Over a ring whose maximal ideals are "everywhere" (a Jacobson ring), the only thing vanishing at all of them is the nilpotents, so $J(R) = \operatorname{nil} R$. Over a [[Def - Local Ring and Residue Field|local ring]] there is a single closed point and a function can vanish there without being nilpotent — the maximal ideal $\mathfrak m$ itself — so $J(R) = \mathfrak m$ is enormous. The Jacobson radical thus measures the gap between "vanishes at the closed points" and "vanishes everywhere".

---

# Examples / Corollaries

**Is an instance — a local ring.** For a [[Def - Local Ring and Residue Field|local ring]] $(R, \mathfrak m)$ there is exactly one maximal ideal, so $J(R) = \mathfrak m$. This is the maximal possible Jacobson radical (the largest proper ideal), and it is why Nakayama is most powerful over local rings: the hypothesis "$\mathfrak a \subseteq J(R)$" is satisfied by $\mathfrak a = \mathfrak m$, the biggest ideal available. Concretely, $J(\mathbb Z_{(p)}) = (p)\mathbb Z_{(p)}$ and $J(k[[x]]) = (x)$.

**Is an instance — $\mathbb Z$ has trivial Jacobson radical.** $J(\mathbb Z) = \bigcap_p (p) = (0)$: a nonzero integer divisible by every prime cannot exist, so only $0$ lies in all maximal ideals. Hence $\mathbb Z$ is Jacobson-semisimple. Note $\operatorname{nil}\mathbb Z = (0)$ too, so here $J = \operatorname{nil}$. This is the example that *disables* Nakayama over $\mathbb Z$: the only ideal $\subseteq J(\mathbb Z)$ is $(0)$, so the lemma says nothing about $\mathfrak a = (p)$.

**Is an instance — a polynomial ring over a field.** $J(k[x]) = (0)$ for $k$ a field: the maximal ideals include all $(x - a)$ for $a \in k$ (when $k$ is infinite, already these intersect to $(0)$), so no nonzero polynomial lies in every maximal ideal. More generally $J(k[x_1,\dots,x_n]) = (0)$; this is the **Jacobson** property and is closely tied to the Nullstellensatz.

**Is NOT an instance — the nilradical is generally smaller, so an element of $J(R)$ need not be in $\operatorname{nil} R$.** Take a local ring $(R, \mathfrak m)$ that is a domain, say $R = k[[x]]$. Then $J(R) = (x)$ contains $x$, but $x$ is not nilpotent ($x^n \neq 0$ for all $n$ in a domain). So $x \in J(R) \setminus \operatorname{nil} R$: membership in the Jacobson radical does *not* imply nilpotence. This separates the two radicals and shows $J(R)$ genuinely records more than nilpotence.

**Corollary — $J(R)$ contains no unit, hence is proper.** If $u \in J(R)$ were a unit, then $u$ would lie in some maximal ideal $\mathfrak m$ (every element of $J(R)$ does), but a maximal ideal contains no unit. So $J(R) \cap R^\times = \varnothing$, and $J(R) \neq R$ whenever $R \neq 0$. This is the calibration that $J(R)$ is a genuine obstruction, not the whole ring.

**Calibration check.** Verify that $J(R)$ is an ideal directly from "intersection of ideals is an ideal". Confirm $J(\mathbb Z) = (0)$ and $J(\mathbb Z_{(p)}) = (p)\mathbb Z_{(p)}$ from the definition. Check that $\operatorname{nil} R \subseteq J(R)$ always (a nilpotent lies in every prime, hence in every maximal ideal). Finally, exhibit an element of $J(R) \setminus \operatorname{nil} R$ in $k[[x]]$ to confirm the inclusion can be strict.

---

# Unlocked by This

> [!tip] The cotangent space and the embedding dimension *(from Algebraic Geometry)*
> For a [[Def - Local Ring and Residue Field|local ring]] $(R,\mathfrak m)$, the Jacobson radical $J(R) = \mathfrak m$ is the ideal whose reduction $\mathfrak m/\mathfrak m^2$ is the **cotangent space** at the point — see [[Def - Minimal Generating Set and the Cotangent Space]]. Its dimension over $k = R/\mathfrak m$ is the **embedding dimension**, the minimal number of functions needed to cut the point out, and a point is **smooth** exactly when this equals the Krull dimension of the ring.

> [!tip] Jacobson rings and the Nullstellensatz *(from Algebraic Geometry)*
> A ring in which $J(R/I) = \operatorname{nil}(R/I)$ for every ideal $I$ — equivalently, every prime is an intersection of maximal ideals — is a **Jacobson ring**. Finitely generated algebras over a field are Jacobson, and this is the structural form of the **Nullstellensatz**: the radical of an ideal equals the intersection of the maximal ideals containing it. The theory is developed in **Commutative Algebra VII — Noether Normalization and the Nullstellensatz**.
