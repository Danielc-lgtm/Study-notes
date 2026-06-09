---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - The Associated Graded Ring and the Rees Algebra"
  - "Def - Graded Ring and Graded Module"
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Thm - Hilbert's Basis Theorem"
  - "Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]] and $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]]. Prove that the [[Def - The Associated Graded Ring and the Rees Algebra|Rees algebra]]
$$R^* = \bigoplus_{n \geq 0} \mathfrak{a}^n = R \oplus \mathfrak{a} \oplus \mathfrak{a}^2 \oplus \cdots$$
is a Noetherian (graded) ring. Deduce that the [[Def - The Associated Graded Ring and the Rees Algebra|associated graded ring]] $\operatorname{gr}_{\mathfrak{a}}(R) = \bigoplus_n \mathfrak{a}^n/\mathfrak{a}^{n+1}$ is also Noetherian. (This is the finiteness fact on which the whole proof of the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]] rests.)

**Recall:**

![[Def - The Associated Graded Ring and the Rees Algebra#The Definition]]

The **Rees algebra** $R^* = \bigoplus_n \mathfrak{a}^n$ has its multiplication "by slots": $x \in \mathfrak{a}^m$ in slot $m$ times $y \in \mathfrak{a}^n$ in slot $n$ gives $xy \in \mathfrak{a}^{m+n}$ in slot $m+n$. It is a [[Def - Graded Ring and Graded Module|graded ring]] with $(R^*)_0 = R$ and $(R^*)_1 = \mathfrak{a}$. The key structural fact: when $\mathfrak{a} = (x_1, \dots, x_r)$, the Rees algebra is *generated in degree one* over $R$ by $x_1, \dots, x_r$ (each placed in slot $1$). The two recall tools:

![[Thm - Hilbert's Basis Theorem#Statement]]

![[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *prove-a-graded-ring-is-Noetherian* problem, and the topic page's strategy gives the canonical route: exhibit the ring as finitely generated over a Noetherian base and apply Hilbert's basis theorem (equivalently, the graded Noetherian criterion). The only real content is identifying the finitely many generators, which the grading hands you.

**Assumption pattern.** The two assumptions split cleanly: "$R$ Noetherian" gives both the Noetherian base $(R^*)_0 = R$ *and* (via Noetherian-ness) the finite generation $\mathfrak{a} = (x_1, \dots, x_r)$. The trigger is that the degree-one piece $(R^*)_1 = \mathfrak{a}$ generates everything: a degree-$n$ element lives in $\mathfrak{a}^n = \mathfrak{a}\cdot\mathfrak{a}^{n-1}$, a product of degree-one elements, so the $x_i$ in slot one generate the whole Rees algebra as an $R$-algebra.

**Theorem routing.** The route is short: $R$ Noetherian $\Rightarrow$ $\mathfrak{a} = (x_1, \dots, x_r)$ finitely generated $\Rightarrow$ $R^* = R[x_1, \dots, x_r]$ generated in degree one $\Rightarrow$ ($R^*$ is a quotient of the polynomial ring $R[T_1, \dots, T_r]$, Noetherian by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]]) $\Rightarrow$ $R^*$ Noetherian; equivalently apply [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded Noetherian criterion]] directly. The deduction for $\operatorname{gr}_{\mathfrak{a}}(R)$: it is the quotient $R^*/\mathfrak{a}R^*$, and quotients of Noetherian rings are Noetherian.

**Key decision point.** The non-obvious move is the surjection $R[T_1, \dots, T_r] \twoheadrightarrow R^*$, $T_i \mapsto x_i$ (in slot one). The subtlety, easy to overlook, is *why this is surjective* — one must see that *every* element of $\mathfrak{a}^n$, not just products of exactly the generators, is hit. This holds because $\mathfrak{a}^n$ is *spanned* by length-$n$ products $x_{i_1}\cdots x_{i_n}$ with $R$-coefficients, which are exactly the degree-$n$ monomials in the $T_i$ with coefficients in $R = (R^*)_0$. The decision to present $R^*$ as a homogeneous quotient of a polynomial ring — rather than wrestling with the infinite direct sum directly — is what makes Hilbert's basis theorem applicable.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Generate a graded ring from its degree-one piece (operation 3).** Recognise that $(R^*)_1 = \mathfrak{a} = (x_1, \dots, x_r)$ generates $R^*$ over $(R^*)_0 = R$.

2. **Present a finitely generated algebra as a polynomial-ring quotient (operation 2).** Build the surjection $R[T_1, \dots, T_r] \twoheadrightarrow R^*$, $T_i \mapsto x_i$, in degree one.

3. **Invoke Hilbert's basis theorem on the polynomial ring (operation 2, finishing move).** Conclude $R[T_1, \dots, T_r]$ is Noetherian, hence so is its quotient $R^*$.

4. **Pass Noetherian-ness to a quotient (operation 1).** Deduce $\operatorname{gr}_{\mathfrak{a}}(R) = R^*/\mathfrak{a}R^*$ is Noetherian.

---

# Hints

> [!note]- Hint 1
> The standard way to show a ring is Noetherian is to exhibit it as finitely generated over a Noetherian base and apply Hilbert's basis theorem. What is the natural base ring inside $R^*$, and is it Noetherian?

> [!note]- Hint 2
> The base is $(R^*)_0 = R$, Noetherian by hypothesis. Now find finitely many generators of $R^*$ as an $R$-algebra. Since $R$ is Noetherian, $\mathfrak{a} = (x_1, \dots, x_r)$ is finitely generated. Put each $x_i$ in slot $1$ of $R^*$. Why do these generate all of $R^*$? Think about what $\mathfrak{a}^n$ is in terms of the $x_i$.

> [!note]- Hint 3
> $\mathfrak{a}^n$ is spanned over $R$ by products $x_{i_1}\cdots x_{i_n}$ of $n$ generators, which sit in slot $n$. So every homogeneous element of $R^*$ is an $R$-polynomial in $x_1, \dots, x_r$. This gives a surjection $R[T_1, \dots, T_r] \to R^*$, $T_i \mapsto x_i$. Now apply [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] to $R[T_1, \dots, T_r]$ and use "quotients of Noetherian rings are Noetherian".

> [!note]- Hint 4
> For the associated graded ring: $\operatorname{gr}_{\mathfrak{a}}(R) = \bigoplus_n \mathfrak{a}^n/\mathfrak{a}^{n+1}$ is the quotient of $R^*$ by the ideal $\mathfrak{a}R^* = \bigoplus_{n \geq 1}\mathfrak{a}^{n}$ shifted... more precisely $\operatorname{gr}_{\mathfrak{a}}(R) = R^*/\mathfrak{a}R^*$ where $\mathfrak{a}R^* = \bigoplus_n \mathfrak{a}^{n+1}$ in slot $n$. Quotients of Noetherian rings are Noetherian.

---

# Solution

The proof presents the Rees algebra as a homogeneous quotient of a polynomial ring over $R$ and applies Hilbert's basis theorem. Step 1 identifies the degree-one generators. Step 2 builds the surjection from the polynomial ring and verifies surjectivity. Step 3 applies Hilbert's basis theorem. Step 4 deduces Noetherian-ness of the associated graded ring as a quotient.

**Step 1: The Rees algebra is generated in degree one by generators of $\mathfrak{a}$.**

Since $R$ is Noetherian, $\mathfrak{a} = (x_1, \dots, x_r)$, and these $x_i$, placed in slot $1$, generate $R^*$ as an $R$-algebra.

> [!note]- Derivation
> Because $R$ is Noetherian, every ideal is finitely generated, so $\mathfrak{a} = (x_1, \dots, x_r)$ for some $x_1, \dots, x_r \in \mathfrak{a}$. View each $x_i$ as a degree-one element of $R^*$, i.e. $x_i \in \mathfrak{a} = (R^*)_1$.
>
> Claim: $R^* = R[x_1, \dots, x_r]$, the $R$-subalgebra generated by $x_1, \dots, x_r$. It suffices to show each homogeneous slot $\mathfrak{a}^n = (R^*)_n$ lies in $R[x_1, \dots, x_r]$. By definition of the ideal power, $\mathfrak{a}^n$ is generated as an $R$-module by the products $x_{i_1}\cdots x_{i_n}$ of $n$ of the generators (every element of $\mathfrak{a}^n$ is a finite $R$-combination of such length-$n$ products). Each such product is a degree-$n$ monomial in $x_1, \dots, x_r$, hence lies in $R[x_1, \dots, x_r]$ in slot $n$. So $\mathfrak{a}^n \subseteq R[x_1, \dots, x_r]$, and since $n$ was arbitrary, $R^* = R[x_1, \dots, x_r]$, generated in degree one.

**Step 2: Present $R^*$ as a quotient of a polynomial ring.**

The assignment $T_i \mapsto x_i$ defines a surjective $R$-algebra homomorphism $R[T_1, \dots, T_r] \twoheadrightarrow R^*$.

> [!note]- Derivation
> Define $\psi : R[T_1, \dots, T_r] \to R^*$ by $\psi|_R = \operatorname{id}_R$ (the inclusion $R = (R^*)_0 \hookrightarrow R^*$) and $\psi(T_i) = x_i \in (R^*)_1$, extended as an $R$-algebra homomorphism. Grading $R[T_1, \dots, T_r]$ by total degree in the $T_i$ and $R^*$ by slot, $\psi$ is a *graded* homomorphism: it sends the degree-$n$ part $\bigoplus_{|e| = n} R\,T^e$ to slot $n$, since $\psi(T^e) = x^e \in \mathfrak{a}^{|e|}$.
>
> $\psi$ is surjective: by Step 1, $R^*$ is generated over $R$ by $x_1, \dots, x_r = \psi(T_1), \dots, \psi(T_r)$, and $\psi$ hits all of $R = (R^*)_0$; an $R$-algebra is the image of a polynomial algebra exactly when the images of the variables generate it, which holds here. Hence $R^* \cong R[T_1, \dots, T_r]/\ker\psi$, a homogeneous quotient (since $\psi$ is graded, $\ker\psi$ is a homogeneous ideal).

**Step 3: Hilbert's basis theorem makes $R^*$ Noetherian.**

The polynomial ring $R[T_1, \dots, T_r]$ is Noetherian, so its quotient $R^*$ is Noetherian.

> [!note]- Derivation
> By [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]], if $R$ is Noetherian then $R[T]$ is Noetherian; applying this $r$ times, $R[T_1, \dots, T_r]$ is Noetherian. A quotient of a Noetherian ring is Noetherian (the ideals of $R[T_1, \dots, T_r]/\ker\psi$ correspond to ideals of $R[T_1, \dots, T_r]$ containing $\ker\psi$, and an ascending chain of the former lifts to an ascending chain of the latter, which stabilizes). By Step 2, $R^* \cong R[T_1, \dots, T_r]/\ker\psi$, so $R^*$ is Noetherian.
>
> *Alternatively*, this is the easy direction of [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded Noetherian criterion]]: $(R^*)_0 = R$ is Noetherian and $R^*$ is finitely generated over it (Step 1), so $R^*$ is Noetherian.

**Step 4: The associated graded ring is Noetherian.**

$\operatorname{gr}_{\mathfrak{a}}(R) = R^*/\mathfrak{a}R^*$ is a quotient of the Noetherian ring $R^*$, hence Noetherian.

> [!note]- Derivation
> The associated graded ring $\operatorname{gr}_{\mathfrak{a}}(R) = \bigoplus_n \mathfrak{a}^n/\mathfrak{a}^{n+1}$ is the quotient of the Rees algebra $R^*$ by the homogeneous ideal $\mathfrak{a}R^*$, whose slot-$n$ component is $\mathfrak{a}\cdot\mathfrak{a}^n = \mathfrak{a}^{n+1}$. Indeed
> $$R^*/\mathfrak{a}R^* = \bigoplus_n \mathfrak{a}^n/\mathfrak{a}^{n+1} = \operatorname{gr}_{\mathfrak{a}}(R),$$
> the slot-$n$ quotient being $\mathfrak{a}^n/\mathfrak{a}^{n+1}$. Since $R^*$ is Noetherian (Step 3) and a quotient of a Noetherian ring is Noetherian, $\operatorname{gr}_{\mathfrak{a}}(R)$ is Noetherian. (One can also see it directly: $\operatorname{gr}_{\mathfrak{a}}(R)$ is generated over $(R/\mathfrak{a})$ — Noetherian as a quotient of $R$ — by the degree-one images $\bar{x}_i \in \mathfrak{a}/\mathfrak{a}^2$, so the graded criterion applies.)

> [!note]- Complete formal solution
> Since $R$ is Noetherian, $\mathfrak{a} = (x_1, \dots, x_r)$. Placing each $x_i$ in slot $1$, the slot $\mathfrak{a}^n = (R^*)_n$ is $R$-spanned by length-$n$ products $x_{i_1}\cdots x_{i_n}$, so $R^* = R[x_1, \dots, x_r]$ is generated in degree one over $(R^*)_0 = R$.
>
> The graded $R$-algebra map $\psi : R[T_1, \dots, T_r] \to R^*$, $T_i \mapsto x_i$, is surjective, so $R^* \cong R[T_1, \dots, T_r]/\ker\psi$. By [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]], $R[T_1, \dots, T_r]$ is Noetherian, and quotients of Noetherian rings are Noetherian; hence $R^*$ is Noetherian.
>
> Finally $\operatorname{gr}_{\mathfrak{a}}(R) = R^*/\mathfrak{a}R^*$ is a quotient of the Noetherian ring $R^*$, hence Noetherian. $\blacksquare$

---

# Key Takeaways

**To prove a graded ring is Noetherian, present it as finitely generated over a Noetherian base and invoke Hilbert's basis theorem — the grading hands you the generators.** This is the universal recipe, and the Rees algebra is its cleanest instance. The pattern: identify the degree-zero subring (here $R$), confirm it is Noetherian, then find finitely many generators — which for a graded ring are always sought in *low degree*, since high-degree elements are products of low-degree ones. For the Rees algebra the generators are literally the generators of $\mathfrak{a}$, sitting in degree one. The transferable diagnostic: whenever you meet a graded $R$-algebra presented as an infinite direct sum, do not panic at the infinitude — ask "is it generated in finitely many degrees over the bottom?", and if so it is a quotient of a polynomial ring and Hilbert's basis theorem finishes. This recipe certifies the Noetherian-ness of every blow-up algebra in the chapter (Rees algebra, associated graded ring, extended Rees algebra).

**Generation "in degree one" is the special feature that the Rees algebra and tangent-cone constructions all share, and it is exactly what makes their Proj a projective variety.** Notice that the generators of $R^*$ all live in slot $1$ — this is not an accident but the structural signature of blow-up algebras. Degree-one generation is precisely the condition under which $\operatorname{Proj} R^*$ (the blowup) embeds in a relative projective space $\mathbb{P}^{r-1}_R$, with the $x_i$ as homogeneous coordinates. The same fact for $\operatorname{gr}_{\mathfrak{a}}(R)$, generated in degree one by $\bar{x}_i \in \mathfrak{a}/\mathfrak{a}^2$, is why $\operatorname{Proj}\operatorname{gr}_{\mathfrak{m}}(R)$ (the exceptional divisor / projectivized tangent cone) embeds in $\mathbb{P}(\mathfrak{m}/\mathfrak{m}^2)$, the projectivized cotangent space. The reusable insight: when a graded ring is generated in degree one, its degree-one piece *is* the ambient projective space's coordinates, so finiteness of that piece (here $\dim \mathfrak{m}/\mathfrak{m}^2 < \infty$, the embedding dimension) controls the geometry.

**This single finiteness fact is the foundation of the entire Artin–Rees machine.** It is worth recognising that this unassuming exercise is the load-bearing lemma under [[Thm - The Artin-Rees Lemma|Artin–Rees]], [[Thm - The Krull Intersection Theorem|Krull intersection]], and all of dimension theory. The logical chain is: $R^*$ Noetherian $\Rightarrow$ finitely generated $R^*$-modules are Noetherian $\Rightarrow$ submodules of the Rees module $M^*$ are finitely generated $\Rightarrow$ induced filtrations are stable (Artin–Rees) $\Rightarrow$ stable submodules vanish (Krull). Every one of those implications uses "submodules of Noetherian modules are finitely generated", which needs the *ring* $R^*$ to be Noetherian — exactly this exercise. The meta-lesson for spaced practice: when a deep theorem (Artin–Rees) reduces to "this auxiliary ring is Noetherian", that reduction *is* the theorem's real content, and the rest is bookkeeping. Trace any hard finiteness theorem back to the one ring whose Noetherian-ness it secretly rests on, and you have found its engine. See [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One]] for the general criterion this exercise instantiates.
