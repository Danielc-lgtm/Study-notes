---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Ring Homomorphism"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is a [[Def - Ring|ring]] with identities $0$ and $1$, and $I \trianglelefteq R$ is an [[Def - Ideal|ideal]]. The **quotient ring** is written $R/I$, read "$R$ mod $I$". Its elements are the additive cosets $r + I = \{r + a : a \in I\}$; two cosets are equal, $r + I = r' + I$, exactly when $r' - r \in I$. The **quotient map** (or canonical projection) is $\pi : R \to R/I$, $r \mapsto r + I$. We write $\cong$ for ring isomorphism. The full symbol registry is on [[Rings I — §2.1–2.2]].

---

# Axiom Motivation

The quotient ring is the construction the entire notion of an [[Def - Ideal|ideal]] was built to support, so the motivation is short and pointed: we want to "divide" a ring $R$ by a piece of itself, collapsing that piece to zero, and obtain a new ring. The model is the [[Def - Quotient Group|quotient group]] — and the model is also the integers modulo $n$, where we throw away the distinction between numbers differing by a multiple of $n$ and are left with a smaller, cleaner ring $\mathbb{Z}/n\mathbb{Z}$. The desideratum is to generalise that: given any ideal, produce a ring in which the ideal has been set to zero.

The elements of the quotient are forced. To collapse $I$ to zero we identify two elements of $R$ whenever they differ by something in $I$; the resulting equivalence classes are exactly the additive cosets $r + I$, and the class of $0$ is $I$ itself. Addition is then also forced — it is just the addition of the [[Def - Quotient Group|quotient group]] of the [[Def - Abelian Group|abelian group]] $(R, +)$ by the subgroup $I$, namely $(r_1 + I) + (r_2 + I) = (r_1 + r_2) + I$, and this is well-defined because every subgroup of an abelian group is normal. Nothing new there.

The whole content is the multiplication. We need a product of cosets, and there is exactly one formula with any hope of being natural — multiply representatives, then take the coset:
$$(r_1 + I)(r_2 + I) := r_1 r_2 + I.$$
And now the well-definedness problem bites, exactly as it did for [[Def - Normal Subgroup|normal subgroups]] in group theory. A coset has many names. If we re-name the factors as $r_1' = r_1 + a_1$ and $r_2' = r_2 + a_2$ with $a_1, a_2 \in I$, the formula must return the *same* coset. Compute:
$$r_1' r_2' = (r_1 + a_1)(r_2 + a_2) = r_1 r_2 + \underbrace{r_1 a_2 + a_1 r_2 + a_1 a_2}_{\text{must lie in } I}.$$
The product is representative-independent precisely when those three correction terms land in $I$. And here is the punchline: $r_1 a_2$ and $a_1 r_2$ are products of an element of $I$ with an *arbitrary* element of $R$, so they lie in $I$ if and only if $I$ is closed under multiplication by everything in $R$ — the **strong (absorbing) closure** axiom of an ideal. The term $a_1 a_2$ then also lies in $I$ for the same reason. The quotient ring construction works *exactly* for ideals, and it fails for any subset that is not one. This is not a coincidence to be checked afterwards; it is the reason the ideal axioms read the way they do. The absorbing axiom *is* the well-definedness of quotient multiplication.

What if we tried to weaken the requirement and quotient by a mere [[Def - Subring|subring]]? Then $a_1 a_2$ would still be absorbed (subring closure handles products of two elements of the subring), but $r_1 a_2$ would escape, since a subring is not closed under multiplication by outside elements. Multiplication of cosets would depend on the representative, and $R/I$ would carry no ring structure — only the additive group would survive. So the ideal hypothesis is not decoration: it is the precise dividing line between "the quotient is a ring" and "the quotient is merely an abelian group". This is also why the quotient map $\pi : R \to R/I$ then turns out to be a [[Def - Ring Homomorphism|ring homomorphism]] — once the operations on $R/I$ are defined by acting on representatives, $\pi$ respects them by definition, and $\pi(1) = 1 + I$ is the identity of $R/I$.

---

# The Definition

Let $R$ be a [[Def - Ring|ring]] and $I \trianglelefteq R$ an [[Def - Ideal|ideal]]. The **quotient ring** $R/I$ is the set of additive cosets
$$R/I = \{\, r + I : r \in R \,\},$$
equipped with the operations
$$(r_1 + I) + (r_2 + I) := (r_1 + r_2) + I, \qquad (r_1 + I)\cdot(r_2 + I) := r_1 r_2 + I,$$
with additive identity $0_{R/I} = 0 + I = I$ and multiplicative identity $1_{R/I} = 1 + I$.

Both operations are **well-defined** — independent of the choice of coset representatives — precisely because $I$ is an ideal: additive well-definedness uses that $I$ is an additive subgroup, and multiplicative well-definedness uses the absorbing property $a \in I,\ b \in R \Rightarrow ab \in I$. With these operations $R/I$ is a ring.

The **quotient map** (canonical projection)
$$\pi : R \to R/I, \qquad \pi(r) = r + I,$$
is a surjective [[Def - Ring Homomorphism|ring homomorphism]] with $\ker\pi = I$ and $\operatorname{im}\pi = R/I$. In particular, every ideal is the kernel of a ring homomorphism — namely the quotient map onto its own quotient.

---

# Relate to Other Fields / Compression

The quotient ring is the [[Def - Quotient Group|quotient group]] construction with a multiplication carried along for the ride. Strip away multiplication and $R/I$ is *literally* the quotient of the abelian group $(R,+)$ by the subgroup $I$ — same cosets, same addition. The ring theory adds exactly one thing: a coset multiplication, well-defined exactly when $I$ is an ideal rather than merely a subgroup. So "quotient ring" compresses to "quotient group of the additive structure, plus a compatible product", and every proof about $R/I$ splits accordingly into a free additive part and a multiplicative part that must be checked.

There is a difference in *flavour* worth internalising, because it inverts the group-theoretic intuition. In finite group theory one usually forms a [[Def - Quotient Group|quotient]] to get a *simpler* group — to peel off a normal subgroup and study a smaller object. In ring theory one usually forms a quotient to get a *more interesting* ring. The [[Def - Polynomial Ring|polynomial ring]] $\mathbb{R}[X]$ is, in itself, a fairly dull infinite-dimensional object; but $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$ is the complex numbers. Quotienting did not simplify $\mathbb{R}[X]$, it *built* something new by imposing a relation. This is the operative idea behind every "adjoin a root" construction: to manufacture a ring in which $X^2 + 1 = 0$, take $\mathbb{R}[X]$ and quotient by the ideal $(X^2+1)$, which forces precisely that equation and nothing more.

Categorically, $R/I$ together with the quotient map $\pi$ has a universal property: any ring homomorphism $\varphi : R \to S$ that kills $I$ (meaning $I \subseteq \ker\varphi$) factors *uniquely* through $\pi$, as $\varphi = \bar\varphi \circ \pi$ for a unique $\bar\varphi : R/I \to S$. This is the engine of the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]]: take $\varphi$ with $I = \ker\varphi$ exactly, and the induced $\bar\varphi$ is an isomorphism onto $\operatorname{im}\varphi$. The quotient ring is the universal recipient of homomorphisms out of $R$ that annihilate $I$.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}/n\mathbb{Z}$, the integers modulo $n$.** Taking $R = \mathbb{Z}$ and the [[Def - Ideal|ideal]] $I = n\mathbb{Z}$, the quotient ring $\mathbb{Z}/n\mathbb{Z}$ has elements $0 + n\mathbb{Z},\ 1 + n\mathbb{Z},\ \dots,\ (n-1) + n\mathbb{Z}$ — the $n$ residue classes. Its addition and multiplication are exactly addition and multiplication modulo $n$. This is the founding example: it shows the quotient construction recovers an object every reader already knows, and it certifies that the abstract coset arithmetic is the familiar clock arithmetic.

**Is an instance — $\mathbb{C}[X]/(X) \cong \mathbb{C}$.** Take $R = \mathbb{C}[X]$ and the ideal $(X)$ of polynomials with zero constant term. A general element $a_0 + a_1 X + \cdots + a_n X^n + (X)$ has all terms except $a_0$ inside $(X)$, so it equals $a_0 + (X)$; every coset is represented by a unique constant. The map $a_0 + (X) \leftrightarrow a_0$ is a ring isomorphism $\mathbb{C}[X]/(X) \cong \mathbb{C}$. Conceptually, quotienting by $(X)$ sets $X = 0$, and a polynomial with $X$ set to zero is just its constant term — so this quotient is evaluation-at-$0$ in disguise, and indeed it is the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] applied to $\operatorname{ev}_0 : \mathbb{C}[X] \to \mathbb{C}$.

**Is an instance — $\mathbb{R}[X]/(X^2 + 1) \cong \mathbb{C}$.** Take $R = \mathbb{R}[X]$ and the ideal $(X^2 + 1)$. By the [[Thm - Euclidean Algorithm for Polynomials|Euclidean algorithm]] every polynomial $f$ can be written $f = q(X^2+1) + r$ with $\deg r < 2$, so every coset is represented by a unique linear polynomial $a + bX + (X^2+1)$. Uniqueness holds because a nonzero multiple of $X^2+1$ has degree at least $2$ and so cannot equal a degree-$<2$ difference. In this quotient $X^2 + 1 = 0$, i.e. $X^2 = -1$, so $X$ behaves exactly like the imaginary unit $i$; the map $a + bX + (X^2+1) \mapsto a + bi$ is a ring isomorphism $\mathbb{R}[X]/(X^2+1) \cong \mathbb{C}$. This is the cleanest construction of the complex numbers: they are $\mathbb{R}$ with a root of $X^2+1$ adjoined, and "adjoin a root" *means* "quotient the polynomial ring by the ideal that root generates".

**Is NOT an instance — you cannot form $R/S$ for a subring $S$ that is not an ideal.** The integers $\mathbb{Z}$ are a [[Def - Subring|subring]] of $\mathbb{Q}$, but $\mathbb{Q}/\mathbb{Z}$ is *not* a quotient ring — only a quotient abelian group. Coset multiplication fails: $\tfrac12 + \mathbb{Z} = \tfrac32 + \mathbb{Z}$, yet $\tfrac12 \cdot \tfrac12 = \tfrac14$ and $\tfrac32 \cdot \tfrac12 = \tfrac34$ give different cosets. This non-example pins down that the ideal hypothesis is exactly what licenses the construction; a subring is not enough.

**Corollary — $R/\{0\} \cong R$ and $R/R \cong 0$.** Quotienting by the zero ideal identifies nothing, so $R/\{0\} \cong R$ via $r + \{0\} \mapsto r$. Quotienting by the whole ring collapses everything to a single coset, giving the zero ring $R/R = \{0\}$. These are the two extreme quotients; every other quotient lies strictly between, "smaller than $R$ but not trivial".

**Calibration check.** Verify directly that $0 + I$ and $1 + I$ are the additive and multiplicative identities of $R/I$, and that the quotient map $\pi$ is a [[Def - Ring Homomorphism|ring homomorphism]] with kernel exactly $I$. Check that if $R$ is commutative then so is $R/I$, and that the quotient $R/I$ can have *better* properties than $R$ — for instance $\mathbb{Z}$ has no element squaring to $-1$, but $\mathbb{Z}/5\mathbb{Z}$ does ($2^2 = 4 = -1$). If you can explain why multiplicative well-definedness needs the *absorbing* axiom and not merely subring closure, you have understood the construction.

---

# Unlocked by This

> [!tip] The Isomorphism Theorems for Rings *(from this topic)*
> Quotient rings are the codomain of the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] $R/\ker\varphi \cong \operatorname{im}\varphi$, and the subject of the [[Thm - Second Isomorphism Theorem for Rings|second]] and [[Thm - Third Isomorphism Theorem for Rings|third]] theorems. They turn coset bookkeeping into a one-line identification of a quotient.

> [!tip] The Ideal Correspondence *(from this topic)*
> For $I \trianglelefteq R$ there is an inclusion-preserving bijection between ideals of the quotient $R/I$ and ideals of $R$ containing $I$. See [[Thm - Ideal Correspondence]] — it lets you transfer interesting ideals up and down a quotient.

> [!tip] Adjoining Roots, Field Extensions and $\mathbb{C}$ *(from Rings II onward)*
> Quotienting $F[X]$ by an ideal generated by an irreducible polynomial manufactures a [[Def - Unit and Field|field]] containing a root of that polynomial. This is the universal "adjoin a root" construction and the gateway to field extensions and Galois theory. See [[Rings II — §2.3–2.4]].
