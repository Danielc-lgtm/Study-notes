---
type: exercise
subject: ring-theory
difficulty: "⭐"
prereqs:
  - "Def - Integral Domain"
  - "Def - Field of Fractions"
  - "Thm - Existence of the Field of Fractions"
  - "Def - Polynomial Ring"
  - "Def - Unit and Field"
tags: [algebra, ring-theory]
---

# Problem Statement

For an integral domain $R$, write $\operatorname{Frac}(R)$ for its field of fractions — the field of formal quotients $a/b$ with $a,b\in R$ and $b\neq 0$.

Identify the field of fractions in the following two cases:

1. The **Gaussian integers** $\mathbb{Z}[i]=\{\,a+bi : a,b\in\mathbb{Z}\,\}\subseteq\mathbb{C}$. Show $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)=\{\,p+qi : p,q\in\mathbb{Q}\,\}$, the field of *Gaussian rationals*.
2. The **polynomial [[Def - Ring|ring]]** $F[X]$ over a field $F$. Show $\operatorname{Frac}(F[X])=F(X)$, the field of **rational functions** in $X$ — formal quotients $p(X)/q(X)$ of polynomials with $q\neq 0$.

In each case, "identify" means: name a concrete field $K$, check that it qualifies as a field of fractions of $R$, and conclude $\operatorname{Frac}(R)\cong K$.

**Recall:**

An [[Def - Integral Domain|integral domain]] is a non-zero commutative ring with no zero divisors: $ab=0\Rightarrow a=0$ or $b=0$. Both $\mathbb{Z}[i]$ and $F[X]$ are integral domains — $\mathbb{Z}[i]$ because it is a [[Def - Subring|subring]] of the field $\mathbb{C}$, and $F[X]$ because the [[Def - Polynomial Ring|polynomial ring]] over an integral domain is again an integral domain (the leading coefficient of a product is the product of the leading coefficients, hence non-zero).

The notion we are computing is the **field of fractions**:

![[Def - Field of Fractions#The Definition]]

The key fact licensing the whole exercise is that the field of fractions exists *and is unique* — any two fields of fractions of the same domain are canonically isomorphic:

> **Existence and uniqueness of the field of fractions.** Every integral domain $R$ has a field of fractions $\operatorname{Frac}(R)$, constructed as equivalence classes of pairs $(a,b)$ with $b\neq 0$ under $(a,b)\sim(c,d)\iff ad=bc$. It satisfies a **universal property**: it is the *smallest* field containing $R$ — more precisely, any injective ring homomorphism from $R$ into a field $K$ extends uniquely to a homomorphism $\operatorname{Frac}(R)\to K$. Consequently, if $K$ is *any* field that contains (a copy of) $R$ and in which every element can be written as $ab^{-1}$ with $a,b\in R$, then $K$ is *the* field of fractions of $R$, i.e. $K\cong\operatorname{Frac}(R)$.

See [[Thm - Existence of the Field of Fractions]]. This last sentence is the working tool: to identify $\operatorname{Frac}(R)$ it suffices to exhibit a field $K$ with the two properties (it contains $R$; every element is a ratio of elements of $R$).

---

# Convergent Strategy

**Problem class.** This is an *identify a universal construction* problem: a field of fractions is defined by an abstract construction (or, equivalently, by a universal property), and the task is to recognise that an already-familiar field *is* that construction in disguise. As the [[Rings II — §2.3–2.4#Problem-Solving Strategy|topic page's strategy]] records, the move for "identify the object defined by a universal property" is *not* to unfold the construction — it is to **verify the defining properties on a candidate** and let uniqueness do the rest.

**Assumption pattern.** In both parts the domain $R$ already sits inside a field: $\mathbb{Z}[i]$ inside $\mathbb{C}$, and $F[X]$ inside the obvious field of rational functions. The recognisable pattern is: *the domain $R$ is given as a [[Def - Subring|subring]] of a known field $K$, and one suspects $K$ is "just big enough"*. When that is the situation, you never construct anything — you cut $K$ down to the smallest subfield containing $R$ and check it equals the candidate.

**Theorem routing.** The route is the **uniqueness clause** of [[Thm - Existence of the Field of Fractions|the field-of-fractions theorem]]. The theorem says a field of fractions is unique up to isomorphism, and gives a checkable criterion: a field $K$ is the field of fractions of $R$ precisely when (i) $R\le K$ and (ii) every element of $K$ has the form $ab^{-1}$ with $a,b\in R$, $b\neq 0$. So the entire solution is: propose $K$ ($\mathbb{Q}(i)$, then $F(X)$), verify (i) and (ii), conclude $K\cong\operatorname{Frac}(R)$.

**Key decision point.** The one genuine subtlety, and the reason this is worth doing rather than trivial, is property (ii): one must show the candidate field is *no bigger than necessary* — that every element really is a ratio of elements of $R$, with both numerator and denominator drawn from $R$ itself. For $\mathbb{Q}(i)$ this means clearing denominators so that a Gaussian *rational* $p+qi$ becomes (Gaussian integer)$/$(integer); the slick move is to multiply by a common integer denominator. For $F(X)$ it is immediate by definition. The decision is to recognise that property (ii) is the only thing with content and to spend the effort there.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings II — §2.3–2.4#Legal Operations|the topic page's Legal Operations]]:

1. **Identify a universal object by checking the defining property on a candidate** (operation: *do not build the universal object — verify a guess satisfies its characterisation, then invoke uniqueness*). We guess $\mathbb{Q}(i)$ and $F(X)$ and check each is a field of fractions of the relevant domain.

2. **Use the uniqueness clause of the field-of-fractions theorem** (operation: *any field containing $R$ in which every element is a ratio from $R$ equals $\operatorname{Frac}(R)$*; see [[Thm - Existence of the Field of Fractions]]). This is the criterion verified in both parts.

3. **Clear denominators to write an element as a ratio of elements of the subring** (operation: *multiply numerator and denominator by a common factor to move both into $R$*). To show $p+qi\in\mathbb{Q}(i)$ is a ratio of Gaussian integers, multiply through by a common integer denominator $n$ of $p$ and $q$.

4. **Recognise a subring of a field as a domain automatically** (operation: *a subring of an integral domain — in particular of a field — is an integral domain*). This is how we know $\mathbb{Z}[i]$ is a domain and so *has* a field of fractions in the first place.

5. **Use that the polynomial ring over a domain is a domain** (the degree/leading-coefficient operation in $F[X]$). This is how we know $F[X]$ is a domain, hence has a field of fractions $F(X)$.

---

# Hints

> [!note]- Hint 1
> You are not asked to *construct* anything. The field of fractions is unique up to isomorphism, so the task is only to *recognise* it. If you can write down a field $K$ that (a) contains a copy of $R$ and (b) consists entirely of ratios $ab^{-1}$ of elements of $R$, then $K$ is the field of fractions of $R$. Which familiar field contains $\mathbb{Z}[i]$? Which contains $F[X]$?

> [!note]- Hint 2
> For the Gaussian integers, the natural candidate is $\mathbb{Q}(i)=\{p+qi : p,q\in\mathbb{Q}\}$. Check first that this is a field (it is a subfield of $\mathbb{C}$ — closed under the operations and under inverses). It obviously contains $\mathbb{Z}[i]$. The only real work is property (b): show every $p+qi$ with $p,q$ rational is a *ratio of Gaussian integers*.

> [!note]- Hint 3
> To clear denominators in $p+qi$: write $p=a/n$ and $q=b/n$ over a *common* positive integer denominator $n$ ($a,b,n\in\mathbb{Z}$). Then $p+qi=(a+bi)/n$, a Gaussian integer $a+bi$ divided by the Gaussian integer $n$. That exhibits $p+qi$ as a ratio of elements of $\mathbb{Z}[i]$, so $\mathbb{Q}(i)=\operatorname{Frac}(\mathbb{Z}[i])$.

> [!note]- Hint 4
> For $F[X]$, the candidate is the field of **rational functions** $F(X)=\{p(X)/q(X) : p,q\in F[X],\,q\neq 0\}$ — formal quotients of polynomials. Here property (b) is true *by the very definition* of $F(X)$: every element is already a ratio of two polynomials. So $F(X)$ is built to be exactly $\operatorname{Frac}(F[X])$; you only need to confirm it is a field and contains $F[X]$.

---

# Solution

The field of fractions is characterised up to isomorphism by a universal property — it is the smallest field containing the domain. So we do not construct it; we guess a familiar field and verify the characterisation. In both parts the candidate field is "the domain $R$ with denominators allowed", and the one substantive check is that every element really is a ratio of two elements of $R$.

**Step 1: The criterion — what it takes to be the field of fractions.**

A field $K$ is the field of fractions of an integral domain $R$ if and only if $R$ embeds in $K$ and every element of $K$ is a ratio $ab^{-1}$ with $a,b\in R$, $b\neq 0$.

> [!note]- Derivation
> By [[Def - Field of Fractions|definition]], a field of fractions of $R$ is a field $K$ such that (i) $R\le K$ (there is an injective ring homomorphism $R\hookrightarrow K$, so $K$ contains a copy of $R$), and (ii) every $x\in K$ can be written $x=ab^{-1}$ for some $a,b\in R$ with $b\neq 0$, where $b^{-1}$ is the inverse computed *in $K$*.
>
> The theorem [[Thm - Existence of the Field of Fractions|existence and uniqueness of the field of fractions]] guarantees such a $K$ exists and is *unique up to isomorphism*: any two fields satisfying (i) and (ii) for the same $R$ are isomorphic by an isomorphism fixing $R$. The conceptual reason is the universal property — $\operatorname{Frac}(R)$ is the *smallest* field containing $R$, so any field satisfying (i)–(ii) is squeezed: it contains $R$, hence contains $\operatorname{Frac}(R)$ (smallness), yet by (ii) it is generated as a field by $R$, hence is contained in $\operatorname{Frac}(R)$. The two inclusions force equality.
>
> So the practical test is: **to identify $\operatorname{Frac}(R)$, exhibit any field $K$ satisfying (i) and (ii).** That is all the rest of the solution does.

**Step 2: $\mathbb{Q}(i)$ is a field containing $\mathbb{Z}[i]$.**

The set $\mathbb{Q}(i)=\{p+qi : p,q\in\mathbb{Q}\}$ is a subfield of $\mathbb{C}$, and it contains the Gaussian integers $\mathbb{Z}[i]$.

> [!note]- Derivation
> $\mathbb{Q}(i)$ is closed under addition and multiplication: $(p+qi)+(p'+q'i)=(p+p')+(q+q')i$ and $(p+qi)(p'+q'i)=(pp'-qq')+(pq'+qp')i$, with all coordinates rational. It contains $0$ and $1$. For inverses, if $p+qi\neq 0$ then $p^2+q^2\neq 0$ (a sum of squares of rationals, not both zero), and
> $$(p+qi)^{-1}=\frac{p-qi}{p^2+q^2}=\frac{p}{p^2+q^2}-\frac{q}{p^2+q^2}\,i\in\mathbb{Q}(i),$$
> since the two coordinates are rational. So $\mathbb{Q}(i)$ is a [[Def - Unit and Field|field]] — indeed a subfield of $\mathbb{C}$.
>
> And $\mathbb{Z}[i]\subseteq\mathbb{Q}(i)$: a Gaussian integer $a+bi$ has $a,b\in\mathbb{Z}\subseteq\mathbb{Q}$. So property (i) of Step 1 holds with $R=\mathbb{Z}[i]$, $K=\mathbb{Q}(i)$.

**Step 3: every Gaussian rational is a ratio of Gaussian integers.**

Every element $p+qi\in\mathbb{Q}(i)$ can be written as $(a+bi)/n$ with $a+bi\in\mathbb{Z}[i]$ and $n\in\mathbb{Z}\setminus\{0\}\subseteq\mathbb{Z}[i]$. Hence property (ii) holds, and $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)$.

> [!note]- Derivation
> Take $p+qi\in\mathbb{Q}(i)$ with $p,q\in\mathbb{Q}$. Write the rationals over a **common denominator**: there is a positive integer $n$ and integers $a,b$ with
> $$p=\frac{a}{n},\qquad q=\frac{b}{n}.$$
> (Concretely, if $p=a'/n'$ and $q=b'/n''$ in lowest terms, take $n=n'n''$, $a=a'n''$, $b=b'n'$.) Then
> $$p+qi=\frac{a}{n}+\frac{b}{n}i=\frac{a+bi}{n}.$$
> The numerator $a+bi$ is a Gaussian integer, and the denominator $n$ is a non-zero integer, which is also a Gaussian integer (with zero imaginary part). So $p+qi=(a+bi)\cdot n^{-1}$ is a ratio of two elements of $\mathbb{Z}[i]$, the inverse $n^{-1}$ taken in $\mathbb{Q}(i)$.
>
> Thus $\mathbb{Q}(i)$ satisfies both (i) and (ii) of Step 1 for $R=\mathbb{Z}[i]$. By the uniqueness clause of [[Thm - Existence of the Field of Fractions|the field-of-fractions theorem]],
> $$\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i).$$
> The picture: passing from $\mathbb{Z}[i]$ to its field of fractions does to the Gaussian integers exactly what passing from $\mathbb{Z}$ to $\mathbb{Q}$ does to the integers — it adjoins all denominators. Adjoining denominators to $\mathbb{Z}[i]$ promotes the integer coordinates to rational coordinates, and $\mathbb{Q}(i)$ is the result.

**Step 4: $\operatorname{Frac}(F[X])=F(X)$, the field of rational functions.**

The field of rational functions $F(X)=\{p(X)/q(X) : p,q\in F[X],\,q\neq 0\}$ is a field containing $F[X]$, and every element is by construction a ratio of two polynomials. Hence $\operatorname{Frac}(F[X])=F(X)$.

> [!note]- Derivation
> The ring $F[X]$ is an [[Def - Integral Domain|integral domain]]: $F$ is a field, hence a domain, and the [[Def - Polynomial Ring|polynomial ring]] over a domain is a domain — the leading coefficient of a product is the product of the leading coefficients, which is non-zero. So $F[X]$ *has* a field of fractions.
>
> The candidate is $F(X)$, the **field of rational functions**: formal quotients $p(X)/q(X)$ of polynomials with $q\neq 0$, with two quotients identified when they cross-multiply equal, and the usual addition $\frac{p}{q}+\frac{r}{s}=\frac{ps+rq}{qs}$ and multiplication $\frac{p}{q}\cdot\frac{r}{s}=\frac{pr}{qs}$. This is genuinely a field: it is non-zero, commutative, and a non-zero element $p/q$ (so $p\neq 0$) has inverse $q/p\in F(X)$.
>
> Now verify Step 1's two properties for $R=F[X]$, $K=F(X)$:
> - **(i) $F[X]\le F(X)$.** A polynomial $p$ is the rational function $p/1$, so $F[X]$ embeds in $F(X)$.
> - **(ii) every element is a ratio from $F[X]$.** By the very definition of $F(X)$, every element is $p(X)/q(X)$ with $p,q\in F[X]$ and $q\neq 0$ — already a ratio of two elements of $F[X]$. There is nothing to clear: $F(X)$ is *built* as the set of such ratios.
>
> So $F(X)$ satisfies (i) and (ii); by the uniqueness clause of [[Thm - Existence of the Field of Fractions|the field-of-fractions theorem]],
> $$\operatorname{Frac}(F[X])=F(X).$$

> [!note]- Complete formal solution
> **Claim.** $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)$ and $\operatorname{Frac}(F[X])=F(X)$.
>
> A field of fractions of an integral domain $R$ is a field $K$ with $R\le K$ such that every element of $K$ is $ab^{-1}$ for $a,b\in R$, $b\neq 0$; by [[Thm - Existence of the Field of Fractions|the theorem]] it is unique up to isomorphism, so it suffices to exhibit such a $K$ in each case.
>
> *Gaussian integers.* Let $K=\mathbb{Q}(i)=\{p+qi : p,q\in\mathbb{Q}\}$. It is a subfield of $\mathbb{C}$: closed under $+$ and $\times$, and $(p+qi)^{-1}=\frac{p}{p^2+q^2}-\frac{q}{p^2+q^2}i\in\mathbb{Q}(i)$ for $p+qi\neq 0$. It contains $\mathbb{Z}[i]$. Given $p+qi\in K$, write $p=a/n$, $q=b/n$ over a common integer denominator $n>0$; then $p+qi=(a+bi)/n$, a ratio of the Gaussian integers $a+bi$ and $n$. So $K$ is a field of fractions of $\mathbb{Z}[i]$, hence $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)$.
>
> *Polynomial ring.* $F[X]$ is an integral domain (polynomial ring over a field). Let $K=F(X)$, the field of rational functions $p(X)/q(X)$, $q\neq 0$. It is a field, with $(p/q)^{-1}=q/p$ for $p\neq 0$. It contains $F[X]$ via $p\mapsto p/1$, and by definition every element is a ratio of two polynomials. So $K$ is a field of fractions of $F[X]$, hence $\operatorname{Frac}(F[X])=F(X)$. $\blacksquare$

---

# Key Takeaways

**To identify an object defined by a universal property, verify the property on a candidate — do not run the construction.** The field of fractions is *defined* by a construction (equivalence classes of pairs) but *characterised* up to isomorphism by a property: smallest field containing $R$, equivalently "contains $R$ and every element is a ratio from $R$". The construction proves *existence*; the characterisation is what you *use*. The reusable pattern: when an object is given by a universal property — field of fractions, free [[Def - Group|group]], tensor product, completion, localisation — never manipulate the construction's internal data. Guess the answer from familiarity, then check it satisfies the universal property, and let the uniqueness clause finish. Here the guesses $\mathbb{Q}(i)$ and $F(X)$ are immediate, and the verification is short, because the universal property reduces to two checkable properties.

**The field of fractions is "the domain with all denominators adjoined" — and the content is always the *smallest* clause.** Both properties matter, but they have very different weight. "Contains $R$" is usually free. "Every element is a ratio of elements of $R$" is the property with teeth: it says the candidate field is *no larger than necessary*. For $\mathbb{Q}(i)$ this forced the denominator-clearing computation $p+qi=(a+bi)/n$; for $F(X)$ it was free only because $F(X)$ is *defined* as the set of such ratios. The general lesson for "smallest object containing $X$" problems — smallest [[Def - Subgroup|subgroup]], smallest subfield, smallest [[Def - Ideal|ideal]] — is that proving "small enough" (every element is reachable from $X$) is where the work lives, while "big enough" (it does contain $X$) is typically immediate. When you must show a set is the smallest something, budget your effort for the smallness direction.

**$\operatorname{Frac}$ is a functorial recipe: it takes a domain and returns "the same arithmetic with division allowed", and the answer is read off coordinate-wise.** The two computations are the same phenomenon at different sites. $\operatorname{Frac}(\mathbb{Z})=\mathbb{Q}$ adjoins denominators to integers. $\operatorname{Frac}(\mathbb{Z}[i])=\mathbb{Q}(i)$ does the identical thing one coordinate at a time: integer coordinates become rational coordinates. $\operatorname{Frac}(F[X])=F(X)$ adjoins denominators to polynomials, producing rational functions. The mental model "field of fractions = allow division" predicts the answer before any computation: whatever the domain is built from, the field of fractions is built from the *field of fractions of those ingredients*. This is also why $\operatorname{Frac}$ is the standard route to *manufacture* fields — function fields $F(X)$, number fields like $\mathbb{Q}(i)$, and the field $\mathbb{Q}(X_1,\dots,X_n)$ all arise this way — and the field $F(X)$ in particular is the foundational object of algebraic geometry, where it appears as the function field of a curve.

**A subring of a field is automatically a domain, which is exactly the hypothesis the field-of-fractions construction needs.** It is worth isolating why $\mathbb{Z}[i]$ even *has* a field of fractions: the construction requires an integral domain (the proof of transitivity of the equivalence relation cancels a non-zero denominator, which is only valid with no zero divisors). $\mathbb{Z}[i]$ qualifies because it is a subring of the field $\mathbb{C}$, and any [[Def - Subring|subring]] of a domain — in particular of any field — inherits "no zero divisors". This is a small but constantly used trigger-reaction: "is this ring a domain?" is answered instantly with "yes" whenever the ring sits inside a field, and "yes" again whenever it is a polynomial ring over a domain. Recognising a domain quickly is the precondition for reaching for $\operatorname{Frac}$ at all, and these two sources — subring of a field, polynomial ring over a domain — cover the overwhelming majority of cases.
