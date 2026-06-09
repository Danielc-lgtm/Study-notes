---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Graded Ring and Graded Module"
  - "Def - The Associated Graded Ring and the Rees Algebra"
  - "Def - Polynomial Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R = k[x_1, \dots, x_d]$ be the [[Def - Polynomial Ring|polynomial ring]] over a field $k$, and let $\mathfrak{m} = (x_1, \dots, x_d)$ be the maximal ideal of the origin. Prove that the [[Def - The Associated Graded Ring and the Rees Algebra|associated graded ring]] is the polynomial ring itself:
$$\operatorname{gr}_{\mathfrak{m}}(R) = \bigoplus_{n \geq 0} \mathfrak{m}^n/\mathfrak{m}^{n+1} \;\cong\; k[x_1, \dots, x_d],$$
as graded $k$-algebras. Then compute the contrasting case $R = k[x,y]/(y^2 - x^3)$ (the cuspidal cubic) at $\mathfrak{m} = (x,y)$ and show that $\operatorname{gr}_{\mathfrak{m}}(R) \cong k[x,y]/(y^2)$, exhibiting a *nonreduced* tangent cone — a "doubled line".

**Recall:**

![[Def - The Associated Graded Ring and the Rees Algebra#The Definition]]

![[Def - Graded Ring and Graded Module#The Definition]]

For $R = k[x_1, \dots, x_d]$ and $\mathfrak{m} = (x_1, \dots, x_d)$, the power $\mathfrak{m}^n$ is the [[Def - Ideal|ideal]] of all polynomials with no terms of degree $< n$ — i.e. the span of all monomials of degree $\geq n$. The quotient $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ therefore isolates the *degree-exactly-$n$* part. The **associated graded ring** $\operatorname{gr}_{\mathfrak{m}}(R) = \bigoplus_n \mathfrak{m}^n/\mathfrak{m}^{n+1}$ carries the multiplication $\bar{x}\cdot\bar{y} = \overline{xy}$, the image of $xy$ in the next layer, well-defined because $\mathfrak{m}^{a+1}\mathfrak{m}^b \subseteq \mathfrak{m}^{a+b+1}$.

Geometrically (forward reference, bold plain text): $\operatorname{gr}_{\mathfrak{m}}(R)$ is the coordinate ring of the **tangent cone** of $\operatorname{Spec} R$ at the point $\mathfrak{m}$, the cone of limiting secant directions. The claim $\operatorname{gr}_{\mathfrak{m}}(k[x_1,\dots,x_d]) \cong k[x_1, \dots, x_d]$ says affine space is its own tangent cone at the origin; the cusp computation shows a singular point has a degenerate, nonreduced tangent cone.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-quotient-construction-and-identify-it* problem: build $\operatorname{gr}_{\mathfrak{m}}(R)$ layer by layer and recognise the result as a known graded ring. As the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Problem-Solving Strategy|topic-page strategy]] notes, the associated graded ring is computed by identifying each layer $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ as a vector space *and* pinning down the multiplication that glues the layers — both are needed, because the layers alone do not determine the ring.

**Assumption pattern.** The decisive structural feature of a polynomial ring is that it is *already graded by total degree*, $R = \bigoplus_d R_d$ with $R_d$ the degree-$d$ homogeneous polynomials. The recognisable trigger is that $\mathfrak{m}$ is the *irrelevant ideal* of this existing grading: $\mathfrak{m} = \bigoplus_{d \geq 1} R_d = R_+$, so $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$. This identifies $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ with the single graded piece $R_n$ — the layer is exactly the degree-$n$ homogeneous polynomials.

**Theorem routing.** The route is: recognise $\mathfrak{m}^n = \bigoplus_{d \geq n}R_d$ from the existing grading; deduce $\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong R_n$ as $k$-vector spaces; check the $\operatorname{gr}$-multiplication on layers matches the polynomial multiplication on the $R_n$ (degree-$m$ times degree-$n$ lands in degree $m+n$, with *no* lower-degree contamination because there are no lower degrees to fall into); assemble $\bigoplus_n R_n = R$. For the cusp, the same machine runs but the relation $y^2 = x^3$ corrupts the top layer: $y^2$ and $x^3$ have different $\mathfrak{m}$-orders ($2$ vs $3$), so the relation forces $\bar{y}^2 = 0$ in $\operatorname{gr}$, not $\bar{y}^2 = \bar{x}^3$.

**Key decision point.** The non-obvious move is to *exploit the pre-existing total-degree grading* rather than computing $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ by brute force. A polynomial ring is the one case where the $\mathfrak{m}$-adic filtration *splits* — $\mathfrak{m}^n = \bigoplus_{d \geq n}R_d$ is a direct sum of graded pieces — so the quotient $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ has a *canonical lift* back to $R_n \subseteq R$. The subtle point, easy to get wrong, is the multiplication: one must verify that no degree-dropping occurs, which is automatic here because the leading form of a product of forms is their product. In the cusp, the genuine insight is that the tangent cone is cut out by the **lowest-degree part** (the *initial form*) of the defining equation, $y^2 - x^3 \rightsquigarrow y^2$, not the whole equation.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Compare homogeneous components degree by degree (operation 1).** The entire identification rests on projecting onto a fixed degree: $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ is the degree-$n$ projection of the existing grading.

2. **Read $\mathfrak{m}^n$ off the irrelevant ideal of an existing grading (operation 3).** Recognise $\mathfrak{m} = R_+$ so that $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$ splits as a direct sum of graded pieces, giving the canonical lift of each layer.

3. **Compute $\operatorname{gr}$-multiplication via leading forms (operation 5).** The product $\bar{f}\cdot\bar{g}$ in $\operatorname{gr}_{\mathfrak{m}}(R)$ is the leading form of $fg$; for homogeneous $f, g$ this is just $fg$, so the multiplication on layers is the polynomial multiplication.

4. **Extract the tangent cone from the initial form of the defining ideal (operation 6).** For the cusp, replace $y^2 - x^3$ by its lowest-degree part $y^2$ to compute $\operatorname{gr}_{\mathfrak{m}}(R)$.

---

# Hints

> [!note]- Hint 1
> The polynomial ring is *already* graded, $R = \bigoplus_d R_d$ by total degree. How does the maximal ideal $\mathfrak{m} = (x_1, \dots, x_d)$ relate to that grading? Write $\mathfrak{m}$, and then $\mathfrak{m}^n$, in terms of the $R_d$.

> [!note]- Hint 2
> $\mathfrak{m} = \bigoplus_{d \geq 1} R_d$ (every polynomial vanishing at the origin), so $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$. Now form the quotient $\mathfrak{m}^n/\mathfrak{m}^{n+1}$. Which single graded piece $R_d$ survives?

> [!note]- Hint 3
> $\mathfrak{m}^n/\mathfrak{m}^{n+1} = \big(\bigoplus_{d \geq n}R_d\big)/\big(\bigoplus_{d \geq n+1}R_d\big) \cong R_n$, the degree-$n$ forms. You have identified the layers; now check the multiplication. Take $\bar{f} \in \mathfrak{m}^m/\mathfrak{m}^{m+1}$ and $\bar{g} \in \mathfrak{m}^n/\mathfrak{m}^{n+1}$ lifting to homogeneous $f \in R_m$, $g \in R_n$. What is $\overline{fg}$, and why is there no contamination from lower degrees?

> [!note]- Hint 4
> For the cusp $R = k[x,y]/(y^2 - x^3)$: the order of $x$ is $1$, of $y$ is $1$, so $y^2$ has order $2$ and $x^3$ has order $3$. In $\mathfrak{m}^2/\mathfrak{m}^3$ the relation $y^2 = x^3$ becomes $\bar{y}^2 = \overline{x^3}$, but $x^3 \in \mathfrak{m}^3$, so $\overline{x^3} = 0$ in $\mathfrak{m}^2/\mathfrak{m}^3$. What relation does $\operatorname{gr}_{\mathfrak{m}}(R)$ therefore satisfy?

---

# Solution

The proof exploits that a polynomial ring is already graded by total degree, so the $\mathfrak{m}$-adic filtration splits as a direct sum of graded pieces and each layer $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ lifts canonically to the degree-$n$ forms $R_n$. Step 1 identifies the layers as vector spaces; Step 2 checks the $\operatorname{gr}$-multiplication is the polynomial multiplication; Step 3 assembles the isomorphism. The cusp computation (Step 4) runs the same machine but with the initial form of the relation replacing the relation.

**Step 1: Each layer is the space of degree-$n$ forms, $\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong R_n$.**

Using the total-degree grading $R = \bigoplus_d R_d$, one has $\mathfrak{m}^n = \bigoplus_{d \geq n}R_d$, so $\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong R_n$ as $k$-vector spaces.

> [!note]- Derivation
> The polynomial ring carries its standard grading $R = \bigoplus_{d \geq 0} R_d$, where $R_d$ is the $k$-span of monomials of total degree exactly $d$. The maximal ideal of the origin is $\mathfrak{m} = (x_1, \dots, x_d) = \{f : f(0) = 0\} = \bigoplus_{d \geq 1} R_d$, the irrelevant ideal of this grading.
>
> Claim: $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$, the forms of degree $\geq n$. Indeed $\mathfrak{m}^n$ is generated by products $x_{i_1}\cdots x_{i_n}$ of $n$ variables, each of which is a degree-$n$ monomial; multiplying by arbitrary polynomials gives all polynomials whose every term has degree $\geq n$. Conversely any monomial of degree $d \geq n$ is divisible by a product of $n$ variables, hence lies in $\mathfrak{m}^n$. So $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$.
>
> Therefore
> $$\frac{\mathfrak{m}^n}{\mathfrak{m}^{n+1}} = \frac{\bigoplus_{d \geq n}R_d}{\bigoplus_{d \geq n+1}R_d} \cong R_n,$$
> the isomorphism sending the class of a degree-$\geq n$ polynomial $f$ to its degree-$n$ part $f_n \in R_n$ (all higher-degree parts lie in $\mathfrak{m}^{n+1}$ and are killed). In particular $\dim_k \mathfrak{m}^n/\mathfrak{m}^{n+1} = \dim_k R_n = \binom{n + d - 1}{d - 1}$.

**Step 2: The $\operatorname{gr}$-multiplication is the polynomial multiplication on forms.**

Under the identification of Step 1, the product $\bar{f}\cdot\bar{g}$ in $\operatorname{gr}_{\mathfrak{m}}(R)$ corresponds to the polynomial product $fg$ of the homogeneous representatives.

> [!note]- Derivation
> Take $\bar{f} \in \mathfrak{m}^m/\mathfrak{m}^{m+1}$ and $\bar{g} \in \mathfrak{m}^n/\mathfrak{m}^{n+1}$, with canonical lifts $f \in R_m$, $g \in R_n$ (homogeneous, by Step 1). By definition of the associated-graded multiplication, $\bar{f}\cdot\bar{g}$ is the image of $fg \in \mathfrak{m}^{m+n}$ in $\mathfrak{m}^{m+n}/\mathfrak{m}^{m+n+1}$.
>
> Now $f \in R_m$ and $g \in R_n$ are homogeneous, so $fg \in R_{m+n}$ is *purely* of degree $m+n$ — there is no lower-degree part and no higher-degree part to worry about. Under the Step-1 identification $\mathfrak{m}^{m+n}/\mathfrak{m}^{m+n+1} \cong R_{m+n}$, the class $\overline{fg}$ corresponds to exactly $fg \in R_{m+n}$. Hence the multiplication on $\bigoplus_n R_n$ induced from $\operatorname{gr}$ is the ordinary polynomial multiplication of homogeneous forms. (This is where it matters that there is no degree-dropping: in a polynomial ring the leading form of a product is the product of the leading forms, because $R_m R_n = R_{m+n}$ with no spillover into lower degrees.)

**Step 3: Assemble the isomorphism of graded $k$-algebras.**

The degree-preserving bijections $\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong R_n$ assemble into a graded $k$-algebra isomorphism $\operatorname{gr}_{\mathfrak{m}}(R) \cong \bigoplus_n R_n = R = k[x_1, \dots, x_d]$.

> [!note]- Derivation
> Define $\Phi : \operatorname{gr}_{\mathfrak{m}}(R) \to R$ degree by degree, sending $\bar{f} \in \mathfrak{m}^n/\mathfrak{m}^{n+1}$ to its associated form $f_n \in R_n$ (Step 1). Each component is a $k$-vector-space isomorphism, so $\Phi$ is a graded $k$-linear bijection. By Step 2 it is multiplicative: $\Phi(\bar{f}\cdot\bar{g}) = fg = \Phi(\bar f)\Phi(\bar g)$ for homogeneous representatives, and bilinearity extends this to all elements. It sends $1 = \bar{1} \in \mathfrak{m}^0/\mathfrak{m}^1 = R/\mathfrak{m} = k$ to $1 \in R_0 = k$. Hence $\Phi$ is an isomorphism of graded $k$-algebras:
> $$\operatorname{gr}_{\mathfrak{m}}(k[x_1, \dots, x_d]) \cong k[x_1, \dots, x_d].$$
> Geometrically, the tangent cone of affine $d$-space at the origin is affine $d$-space — as it must be, since affine space is smooth and equals its own tangent cone at every point.

**Step 4: The cuspidal cubic has a doubled-line tangent cone.**

For $R = k[x,y]/(y^2 - x^3)$ at $\mathfrak{m} = (x,y)$, the relation contributes its *initial form* $y^2$, giving $\operatorname{gr}_{\mathfrak{m}}(R) \cong k[x,y]/(y^2)$ — a nonreduced ring whose Spec is the doubled line $\{y^2 = 0\}$.

> [!note]- Derivation
> Write $\bar{R} = k[x,y]/(y^2 - x^3)$, $\mathfrak{m} = (x,y)$. Both $x$ and $y$ have $\mathfrak{m}$-order $1$, so $y^2$ has order $2$ and $x^3$ has order $3$. Consider the surjection $\pi : k[X, Y] \to \operatorname{gr}_{\mathfrak{m}}(\bar R)$ sending $X \mapsto \bar{x} \in \mathfrak{m}/\mathfrak{m}^2$ and $Y \mapsto \bar{y} \in \mathfrak{m}/\mathfrak{m}^2$ (well-defined and surjective because $\operatorname{gr}_{\mathfrak{m}}(\bar R)$ is generated in degree one by $\bar x, \bar y$, the images of the generators of $\mathfrak{m}$).
>
> To find the kernel, examine the relation $y^2 = x^3$ in $\bar{R}$. Pass to the layer $\mathfrak{m}^2/\mathfrak{m}^3$ where $\bar{y}^2$ lives: there $\bar{y}^2 = \overline{y^2} = \overline{x^3}$, but $x^3 \in \mathfrak{m}^3$, so $\overline{x^3} = 0$ in $\mathfrak{m}^2/\mathfrak{m}^3$. Hence $\bar{y}^2 = 0$ in $\operatorname{gr}_{\mathfrak{m}}(\bar R)$, i.e. $Y^2 \in \ker \pi$. A degree count (the Hilbert function of $k[X,Y]/(Y^2)$ matches $\dim_k \mathfrak{m}^n/\mathfrak{m}^{n+1}$ for the cusp, both equal to $n+1$ for $n \geq 1$, since $1, \bar x, \dots, \bar x^n, \bar y \bar x^{n-1}$ span each layer with the single relation $\bar y^2 = 0$) shows $\ker \pi = (Y^2)$. Therefore
> $$\operatorname{gr}_{\mathfrak{m}}\big(k[x,y]/(y^2 - x^3)\big) \cong k[X,Y]/(Y^2).$$
> This is *not* reduced — it has the nilpotent $Y$ — and $\operatorname{Spec}$ of it is the line $Y = 0$ with multiplicity two, the "doubled line". The tangent cone of the cusp is a single line counted twice: the two analytic branches of $y = \pm x^{3/2}$ have collided into one tangent direction, and the doubling records the second-order tangency. Contrast the node $y^2 = x^2 + x^3$ of [[Def - The Associated Graded Ring and the Rees Algebra|the definition page]], whose initial form $y^2 - x^2 = (y-x)(y+x)$ gives a *reduced* tangent cone of two distinct lines.

> [!note]- Complete formal solution
> **Smooth case.** Let $R = k[x_1, \dots, x_d]$, $\mathfrak{m} = (x_1, \dots, x_d)$, with standard grading $R = \bigoplus_d R_d$. Then $\mathfrak{m}^n = \bigoplus_{d \geq n} R_d$ (the forms of degree $\geq n$), so
> $$\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong R_n \quad (\text{degree-}n\text{ forms}).$$
> Define $\Phi : \operatorname{gr}_{\mathfrak{m}}(R) \to R$ sending the class of $f$ in $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ to its degree-$n$ part $f_n$. Each graded component is a $k$-isomorphism. For homogeneous $f \in R_m$, $g \in R_n$, $\bar f \cdot \bar g = \overline{fg}$ with $fg \in R_{m+n}$ purely homogeneous, so $\Phi(\bar f \bar g) = fg = \Phi(\bar f)\Phi(\bar g)$. Thus $\Phi$ is a graded $k$-algebra isomorphism and $\operatorname{gr}_{\mathfrak{m}}(R) \cong k[x_1, \dots, x_d]$.
>
> **Cusp.** Let $\bar R = k[x,y]/(y^2 - x^3)$, $\mathfrak{m} = (x,y)$. The degree-one generators $\bar x, \bar y$ generate $\operatorname{gr}_{\mathfrak{m}}(\bar R)$, giving a surjection $k[X,Y] \twoheadrightarrow \operatorname{gr}_{\mathfrak{m}}(\bar R)$, $X \mapsto \bar x$, $Y \mapsto \bar y$. Since $y^2 = x^3$ with $x^3 \in \mathfrak{m}^3$, in $\mathfrak{m}^2/\mathfrak{m}^3$ we get $\bar y^2 = \overline{x^3} = 0$, so $Y^2$ lies in the kernel; a Hilbert-function count (each layer has dimension $n+1$, matched by $k[X,Y]/(Y^2)$) shows the kernel is exactly $(Y^2)$. Hence $\operatorname{gr}_{\mathfrak{m}}(\bar R) \cong k[X,Y]/(Y^2)$, the nonreduced doubled line. $\blacksquare$

---

# Key Takeaways

**The associated graded ring is computed from the *initial (lowest-degree) forms*, not the full equations.** This is the single most transferable lesson. To find $\operatorname{gr}_{\mathfrak{m}}(R)$ for $R = k[x_1, \dots, x_n]/I$ localized at the origin, you do not carry the whole defining ideal $I$ — you take the **initial ideal** $\operatorname{in}(I)$ generated by the *lowest-degree parts* of the elements of $I$, and $\operatorname{gr}_{\mathfrak{m}}(R) \cong k[x_1, \dots, x_n]/\operatorname{in}(I)$. The cusp shows why the discarded higher-degree terms matter: $y^2 - x^3$ has initial form $y^2$, so the tangent cone forgets the $-x^3$ entirely. The trigger to recognise this technique: whenever you must compute a tangent cone, a multiplicity, or an associated graded ring of a hypersurface or complete intersection, reach first for the leading forms of the defining equations. A subtlety worth remembering — $\operatorname{in}(I)$ can need *more* generators than $I$ (the initial forms of a generating set need not generate $\operatorname{in}(I)$), which is exactly the phenomenon Gröbner/standard bases were invented to handle.

**A pre-existing grading makes the $\mathfrak{m}$-adic filtration split, and splitting is what makes $\operatorname{gr}$ trivial to compute.** The polynomial ring is special precisely because it is *already* graded, so $\mathfrak{m}^n = \bigoplus_{d \geq n}R_d$ is a direct sum and each layer $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ has a *canonical lift* $R_n$ back into $R$. In a general local ring there is no such lift — the layers are genuine quotients with no preferred representatives, and $\operatorname{gr}$ genuinely loses information (this is why $\operatorname{gr}_{\mathfrak{m}}(R)$ can be singular even when... well, it detects singularity). The diagnostic: when you see a graded ring and an ideal that is its irrelevant ideal $A_+$, the associated graded recovers the original ring, because the filtration was already split. When the ideal is *not* the irrelevant ideal of a grading, expect genuine collapse.

**$\operatorname{gr}_{\mathfrak{m}}(R)$ detects singularity: smooth points give polynomial rings, singular points give degenerate cones.** The smooth case $\operatorname{gr}_{\mathfrak{m}}(k[x_1,\dots,x_d]) \cong k[x_1, \dots, x_d]$ is the calibration: a regular local ring of dimension $d$ has $\operatorname{gr}_{\mathfrak{m}}(R) \cong k[t_1, \dots, t_d]$, a clean polynomial ring, and this *characterizes* regularity. A singular point breaks this — the node gives two crossing lines $(y-x)(y+x)$, the cusp gives a nonreduced doubled line $y^2$. The reusable principle: to test whether a point is smooth, compute the associated graded ring and ask whether it is a polynomial ring; the failure mode (reducible cone = several branches, nonreduced cone = tangential collision) diagnoses the *type* of singularity. This is the algebraic engine behind the classification of curve singularities by their tangent cones and multiplicities, and it connects forward to [[Def - Krull Dimension and Height|dimension theory]], where $\dim R = \dim \operatorname{gr}_{\mathfrak{m}}(R)$ lets dimension be read off the simpler graded ring. Compare the smooth computation here with [[Ex - A nonstandard grading and its Hilbert function]], where the grading itself (not the ring) is altered.
