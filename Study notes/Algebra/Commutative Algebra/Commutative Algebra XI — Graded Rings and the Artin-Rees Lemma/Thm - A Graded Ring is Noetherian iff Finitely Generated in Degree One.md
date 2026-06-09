---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Graded Ring and Graded Module"
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Def - Finitely Generated Module"
  - "Thm - Hilbert's Basis Theorem"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A = \bigoplus_{n \geq 0} A_n$ be a [[Def - Graded Ring and Graded Module|graded ring]], with degree-zero subring $A_0$ and **irrelevant ideal** $A_+ = \bigoplus_{n \geq 1} A_n$. A homogeneous element of degree $n$ is an element of $A_n$. "Finitely generated as an $A_0$-algebra" means $A = A_0[x_1, \dots, x_s]$ for finitely many $x_i \in A$ — every element is a polynomial in the $x_i$ with coefficients in $A_0$. We say $A$ is **generated in degree one** (over $A_0$) if these generators can be taken homogeneous of degree one, i.e. $A = A_0[A_1]$. Recall $A$ is [[Def - Noetherian Ring|Noetherian]] if every ascending chain of ideals stabilizes, equivalently every ideal is finitely generated. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

---

# Statement

> **Theorem (Noetherian criterion for graded rings).** Let $A = \bigoplus_{n \geq 0} A_n$ be a graded ring. The following are equivalent:
>
> 1. $A$ is [[Def - Noetherian Ring|Noetherian]];
> 2. $A_0$ is Noetherian and $A$ is finitely generated as an $A_0$-algebra.
>
> Moreover, in either case the generators of $A$ as an $A_0$-algebra may be taken to be finitely many *homogeneous* elements of positive degree (any homogeneous generating set of the irrelevant ideal $A_+$ serves).

The companion, geometric refinement isolates the degree-one case:

> **Corollary (projective embedding).** If $A$ is generated in degree one over a field $A_0 = k$ — that is, $A = k[A_1]$ with $\dim_k A_1 = r+1 < \infty$ — then $A$ is a Noetherian graded $k$-algebra and a quotient of the polynomial ring $k[T_0, \dots, T_r]$; equivalently $\operatorname{Proj} A$ is a closed subvariety of $\mathbb{P}^r_k$. Generation in degree one is precisely the existence of a projective embedding.

The first statement is "Noetherian $\iff$ finitely generated over the base". The corollary specializes to the case relevant for projective geometry, where the generators sit in degree one.

---

# Motivation

The question this answers is the most basic one you can ask about a graded ring: *when is it small enough to do algebra with?* "Small enough" means Noetherian — every ideal finitely generated, every ascending chain stabilizing, Hilbert's basis theorem available. For an ordinary ring this can be hard to check. For a graded ring the theorem says it reduces to two transparent conditions: the bottom layer $A_0$ should be Noetherian, and the whole tower should be built from $A_0$ by finitely many generators. The grading buys you a clean criterion that an arbitrary ring does not enjoy.

The deeper role is that this is the gateway between commutative algebra and projective geometry. A projective variety is, by definition, $\operatorname{Proj}$ of a graded ring, and for that to be a sensible geometric object the graded ring must be Noetherian — otherwise its $\operatorname{Proj}$ is not even of finite type. The theorem tells you that the Noetherian graded $k$-algebras are exactly the finitely generated ones, and the corollary tells you that the ones with a *projective embedding* are exactly those generated in degree one. So "which graded rings are coordinate rings of projective varieties in $\mathbb{P}^r$?" has the answer "those finitely generated in degree one over $k$" — a statement of pure algebra that the theorem makes precise. Without it, the Proj construction would have no finiteness, and projective varieties would not be the well-behaved objects they are.

There is also a structural payoff inside the chapter. The Rees algebra $R^* = \bigoplus \mathfrak{a}^n$ is a graded ring, and the reason it is Noetherian (when $R$ is) is *exactly* this theorem: $R^*$ is generated over $R^* _0 = R$ by the finitely many generators of $\mathfrak{a}$ sitting in degree one. So the entire Artin–Rees machine rests on this criterion, applied to the Rees algebra.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition for the useful direction is "$A_0$ Noetherian and $A$ finitely generated over $A_0$"; recognising when this holds is the skill.

The first disguised source is **$A$ is a Rees algebra $\bigoplus \mathfrak{a}^n$ over a Noetherian ring $R$**. Here $A_0 = R$ is Noetherian by assumption, and $A$ is generated over $R$ by generators of $\mathfrak{a}$ placed in degree one — so $A$ is finitely generated over $A_0$, and the theorem delivers Noetherian-ness. The bridge $B \to A$ is non-obvious because the Rees algebra is presented as an infinite direct sum $\bigoplus \mathfrak{a}^n$, hiding the finite generation; the move is to recognise that *all* of $\mathfrak{a}^n$ is products of $n$ degree-one elements. *Example problem:* prove $R^*$ is Noetherian, the key step in [[Thm - The Artin-Rees Lemma|Artin–Rees]] (see [[Ex - The Rees algebra is Noetherian]]).

The second disguised source is **$A$ is an associated graded ring $\operatorname{gr}_{\mathfrak{a}}(R) = \bigoplus \mathfrak{a}^n/\mathfrak{a}^{n+1}$**. Now $A_0 = R/\mathfrak{a}$, which is Noetherian as a quotient of a Noetherian ring, and $A$ is generated over $R/\mathfrak{a}$ by the images in degree one of generators of $\mathfrak{a}$ — generation in *degree one*. The bridge: a degree-$n$ element of $\operatorname{gr}_{\mathfrak{a}}(R)$ is a sum of products of $n$ degree-one elements, because $\mathfrak{a}^n = \mathfrak{a} \cdot \mathfrak{a}^{n-1}$. *Example problem:* show $\operatorname{gr}_{\mathfrak{a}}(R)$ is Noetherian whenever $R$ is, the finiteness behind every Hilbert-function argument in dimension theory.

The third disguised source is **a graded $k$-algebra given by generators and relations, $A = k[T_0, \dots, T_r]/I$ with $I$ homogeneous**. The generators are the images of the $T_i$, finitely many, in degree one (or whatever degree the $T_i$ carry); $A_0 = k$ is a field, hence Noetherian. The bridge is that a homogeneous quotient of a finitely-generated graded algebra is again finitely generated by the images of the original generators. *Example problem:* the homogeneous coordinate ring of any projective variety is Noetherian — the standing assumption that makes projective geometry work.

**Targets (Output Amplification)**

The conclusion is "$A$ is Noetherian (with finitely many homogeneous generators of positive degree)".

Combine Noetherian-ness with **the graded Nakayama / generation argument** to get a *minimal* homogeneous generating set. Once $A$ is Noetherian and generated in positive degrees, the irrelevant ideal $A_+$ is finitely generated, and a homogeneous generating set of $A_+/A_+^2$ lifts to a generating set of $A$ over $A_0$. The further result $E$: the *number* of degree-one generators needed is $\dim_k A_1$ when $A_0 = k$, giving the embedding dimension of $\operatorname{Proj} A$ into projective space. The combination is non-obvious because it converts an algebra-generation count into a geometric embedding dimension.

Combine Noetherian-ness with **a finitely generated graded module $M$ over $A$**, plus the Hilbert basis theorem. A finitely generated module over a Noetherian graded ring has each graded piece $M_n$ finite over $A_0$ (finite-dimensional over $k$ when $A_0 = k$), so the [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert function]] $n \mapsto \dim_k M_n$ is well-defined and (Hilbert–Serre) eventually polynomial. The further result $E$ is the entire apparatus of Hilbert polynomials and Krull dimension — available only because the ground ring is Noetherian. This is non-obvious because finiteness of each *graded piece* is a strictly stronger and more useful statement than finiteness of $M$ as a whole.

Combine Noetherian-ness with **the Proj construction**. A Noetherian graded $k$-algebra generated in degree one has $\operatorname{Proj} A$ a projective scheme of finite type, embeddable in $\mathbb{P}^r$. The further result $E$: $\operatorname{Proj} A$ is covered by finitely many affine charts $D_+(x_i)$, $x_i \in A_1$, each $\operatorname{Spec}$ of a Noetherian ring — so projective varieties are glued from finitely many Noetherian affines. The combination is non-obvious because it turns the algebraic finiteness into the *topological* finiteness (quasi-compactness) of the projective variety.

---

# Why Is It True

The easy direction — $(2) \Rightarrow (1)$ — is just Hilbert's basis theorem in disguise: if $A_0$ is Noetherian and $A = A_0[x_1, \dots, x_s]$ is finitely generated over it, then $A$ is a quotient of the polynomial ring $A_0[T_1, \dots, T_s]$, which is Noetherian by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]], and quotients of Noetherian rings are Noetherian. No grading is needed for this half.

The substance is $(1) \Rightarrow (2)$, and here the grading does all the work. The first observation costs nothing: $A_0 \cong A/A_+$ is a quotient of the Noetherian ring $A$, hence Noetherian. The real claim is that $A$ is finitely generated over $A_0$, and the mechanism is a **degree induction powered by Noetherian finiteness of one ideal**.

The key idea is to look at the irrelevant ideal $A_+ = \bigoplus_{n \geq 1} A_n$. Because $A$ is Noetherian, $A_+$ is finitely generated; and because $A_+$ is a *homogeneous* ideal, it has a finite generating set of *homogeneous* elements $x_1, \dots, x_s$, say $x_i \in A_{k_i}$ with each $k_i \geq 1$. These $s$ elements — the homogeneous generators of the irrelevant ideal — are claimed to generate *all* of $A$ as an $A_0$-algebra.

**The whole proof is the single sentence: the homogeneous generators of the irrelevant ideal generate the whole ring over $A_0$, because every positive-degree element lies in $A_+$ and degree induction strips one generator at a time.**

To see why, take a homogeneous element $y \in A_n$ with $n > 0$. Then $y \in A_+$, so $y = \sum_i r_i x_i$ for some $r_i \in A$. Now project this equation onto degree $n$: since $x_i$ has degree $k_i$, the degree-$n$ part of $r_i x_i$ is $(r_i)_{n - k_i} x_i$ — only the degree-$(n - k_i)$ component of $r_i$ contributes. So $y = \sum_i a_i x_i$ with $a_i \in A_{n - k_i}$, each of strictly smaller degree than $y$ (because $k_i \geq 1$). By induction on degree, each $a_i$ is already a polynomial in $x_1, \dots, x_s$ over $A_0$ — the base case $A_0$ being trivially in $A_0[x_1, \dots, x_s]$ — and therefore so is $y$. The induction terminates precisely because the generators have *positive* degree, so each step reduces the degree by at least one. The grading is what lets us "project onto degree $n$" and thereby replace the ring coefficients $r_i$ by the lower-degree coefficients $a_i$, and that single move is the engine.

The reason this is unsurprising in hindsight: Noetherian-ness gives you finiteness for *one* ideal (the irrelevant ideal), and the grading lets you *bootstrap* that single finiteness up the entire tower by induction on degree. Finiteness at the bottom propagates to finiteness everywhere because the bottom (degree-one and higher generators) multiplies up to reach every degree.

---

# What Makes This Hard

The non-obvious step is realising that the *homogeneous generators of the single ideal $A_+$* are enough to generate the *whole ring as an algebra* — most people expect to need generators in every degree. The crux is the degree-projection move: from $y = \sum r_i x_i$ in $A$, project onto degree $n$ to replace the unknown ring elements $r_i$ by *lower-degree* coefficients $a_i$, enabling the induction. The common error is to forget that the generators must have *positive* degree for the induction to terminate (a degree-zero generator would not reduce the degree), and to conflate "finitely generated as an $A_0$-algebra" with "finitely generated as an $A_0$-module" — the latter is far stronger and usually false.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** The hard direction is $(1) \Rightarrow (2)$. Get $A_0$ Noetherian for free from $A_0 \cong A/A_+$. For the generation, take finitely many *homogeneous* generators of the irrelevant ideal $A_+$ (possible because $A$ is Noetherian and $A_+$ is homogeneous), and prove by induction on degree that they generate $A$ as an $A_0$-algebra, using the degree-projection trick to lower the degree of the coefficients at each step. The reverse $(2) \Rightarrow (1)$ is Hilbert's basis theorem.

**Subgoal decomposition:**

1. **$(2) \Rightarrow (1)$.** Show: $A_0$ Noetherian and $A = A_0[x_1, \dots, x_s]$ imply $A$ Noetherian.
   - *Hint:* $A$ is a quotient of $A_0[T_1, \dots, T_s]$; apply [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] and "quotients of Noetherian are Noetherian".
   - *Why needed:* It is the cheap half and motivates that "finitely generated over a Noetherian base" is the right target.

2. **$A_0$ is Noetherian.** Show: if $A$ is Noetherian then so is $A_0$.
   - *Hint:* The projection $A \to A_0$ killing $A_+$ is surjective with kernel $A_+$, so $A_0 \cong A/A_+$.
   - *Why needed:* It is half of condition $(2)$, and free.

3. **$A_+$ has finitely many homogeneous generators of positive degree.** Show: the irrelevant ideal admits a finite homogeneous generating set $x_1, \dots, x_s$, $x_i \in A_{k_i}$, $k_i \geq 1$.
   - *Hint:* $A$ Noetherian makes $A_+$ finitely generated; split each generator into homogeneous components — the components still lie in $A_+$ and still generate.
   - *Why needed:* These are the algebra generators; positivity of $k_i$ is what makes the next induction terminate.

4. **Degree induction.** Show: $A_n \subseteq A_0[x_1, \dots, x_s]$ for all $n$, by induction on $n$.
   - *Hint:* For $y \in A_n$, $n > 0$, write $y = \sum r_i x_i \in A_+$, project onto degree $n$ to get $y = \sum a_i x_i$ with $a_i \in A_{n - k_i}$, then apply the inductive hypothesis to each lower-degree $a_i$.
   - *Why needed:* It is the conclusion — $A$ is generated by $x_1, \dots, x_s$ over $A_0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A homogeneous ideal has a homogeneous finite generating set
> **Statement:** If $A$ is Noetherian and $I \trianglelefteq A$ is a homogeneous ideal (closed under taking homogeneous components: $a \in I \Rightarrow$ each $a_n \in I$), then $I$ is generated by finitely many homogeneous elements.
>
> **Hint:** Take any finite generating set (Noetherian), then replace each generator by its homogeneous components.
>
> **Why needed:** It supplies the homogeneous generators $x_1, \dots, x_s$ of $A_+$ that serve as the algebra generators; homogeneity is what makes the degree-projection trick available.
>
> > [!note]- Full proof
> > Since $A$ is Noetherian, $I = (g_1, \dots, g_m)$ for some $g_j$. Write each $g_j = \sum_n (g_j)_n$ as a sum of homogeneous components. Because $I$ is a homogeneous ideal, every component $(g_j)_n$ lies in $I$. The finite set $\{(g_j)_n : 1 \leq j \leq m,\ (g_j)_n \neq 0\}$ consists of homogeneous elements of $I$ and generates $I$: any $g_j$ is the sum of its components, so the original generators lie in the ideal generated by the components, hence the components generate everything the $g_j$ did. The irrelevant ideal $A_+ = \bigoplus_{n \geq 1} A_n$ is homogeneous, so this applies; its homogeneous generators all have degree $\geq 1$ since $A_+$ contains no nonzero degree-zero element.

> [!note]- Lemma 2: Degree projection lowers coefficient degrees
> **Statement:** Let $x_1, \dots, x_s$ be homogeneous with $x_i \in A_{k_i}$. If $y \in A_n$ and $y = \sum_i r_i x_i$ with $r_i \in A$, then also $y = \sum_i a_i x_i$ with $a_i = (r_i)_{n - k_i} \in A_{n - k_i}$ the degree-$(n-k_i)$ component of $r_i$ (and $a_i = 0$ if $n < k_i$).
>
> **Hint:** Apply the degree-$n$ projection to both sides; since $x_i$ is homogeneous of degree $k_i$, the degree-$n$ part of $r_i x_i$ is $(r_i)_{n-k_i} x_i$.
>
> **Why needed:** This is the heart of the induction — it replaces arbitrary ring coefficients $r_i$ by coefficients of strictly smaller degree $n - k_i < n$, enabling descent.
>
> > [!note]- Full proof
> > The grading gives a projection $\pi_n : A \to A_n$ onto the degree-$n$ component, which is additive. Apply $\pi_n$ to $y = \sum_i r_i x_i$. The left side $y \in A_n$ is fixed by $\pi_n$. On the right, $r_i x_i = \big(\sum_d (r_i)_d\big) x_i = \sum_d (r_i)_d x_i$, and since $(r_i)_d \in A_d$ and $x_i \in A_{k_i}$, the product $(r_i)_d x_i \in A_{d + k_i}$. The degree-$n$ part picks out $d + k_i = n$, i.e. $d = n - k_i$. Hence $\pi_n(r_i x_i) = (r_i)_{n - k_i} x_i$, with the convention that $(r_i)_{n-k_i} = 0$ when $n - k_i < 0$. Summing, $y = \pi_n(y) = \sum_i (r_i)_{n-k_i} x_i = \sum_i a_i x_i$ with $a_i \in A_{n - k_i}$. Since each $k_i \geq 1$, every $a_i$ has degree $< n$.

> [!note]- Lemma 3: Generation by degree induction
> **Statement:** With $x_1, \dots, x_s$ as in Lemma 1, $A_n \subseteq A_0[x_1, \dots, x_s]$ for every $n \geq 0$; hence $A = A_0[x_1, \dots, x_s]$.
>
> **Hint:** Induct on $n$. Base case $A_0 \subseteq A_0[\dots]$ is trivial. For $n > 0$, write $y \in A_n$ via Lemma 2 and apply the inductive hypothesis to the lower-degree coefficients.
>
> **Why needed:** It is the conclusion of the hard direction: $A$ is finitely generated over $A_0$.
>
> > [!note]- Full proof
> > Induct on $n$. For $n = 0$, $A_0 \subseteq A_0[x_1, \dots, x_s]$ trivially. Suppose $n > 0$ and $A_m \subseteq A_0[x_1, \dots, x_s]$ for all $m < n$. Let $y \in A_n$. Since $n > 0$, $y \in A_+$, and $A_+ = (x_1, \dots, x_s)$ (Lemma 1), so $y = \sum_i r_i x_i$ for some $r_i \in A$. By Lemma 2, $y = \sum_i a_i x_i$ with $a_i \in A_{n - k_i}$ and $n - k_i < n$ (as $k_i \geq 1$). By the inductive hypothesis each $a_i \in A_{n - k_i} \subseteq A_0[x_1, \dots, x_s]$. Therefore $y = \sum_i a_i x_i$ is a polynomial in $x_1, \dots, x_s$ with coefficients in $A_0$, i.e. $y \in A_0[x_1, \dots, x_s]$. This completes the induction, and since $A = \bigoplus_n A_n$, we get $A = A_0[x_1, \dots, x_s]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A = \bigoplus_{n \geq 0} A_n$ be a graded ring.
>
> ---
> **$(2) \Rightarrow (1)$.** Suppose $A_0$ is Noetherian and $A = A_0[x_1, \dots, x_s]$ for finitely many $x_i$. Then the $A_0$-algebra surjection $A_0[T_1, \dots, T_s] \twoheadrightarrow A$, $T_i \mapsto x_i$, exhibits $A$ as a quotient of the polynomial ring $A_0[T_1, \dots, T_s]$. By [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] (applied $s$ times), $A_0[T_1, \dots, T_s]$ is Noetherian, and a quotient of a Noetherian ring is Noetherian. Hence $A$ is Noetherian.
>
> ---
> **$(1) \Rightarrow (2)$.** Suppose $A$ is Noetherian.
>
> *$A_0$ is Noetherian.* The projection $\pi : A \to A_0$, $\sum_n a_n \mapsto a_0$, is a surjective ring homomorphism with kernel $A_+ = \bigoplus_{n \geq 1} A_n$, so $A_0 \cong A/A_+$ is a quotient of the Noetherian ring $A$, hence Noetherian.
>
> *$A$ is finitely generated over $A_0$.* The irrelevant ideal $A_+$ is generated by the set of all homogeneous elements of positive degree, and is therefore a homogeneous ideal. Since $A$ is Noetherian, $A_+$ is finitely generated; by Lemma 1 we may take finitely many *homogeneous* generators $x_1, \dots, x_s$ with $x_i \in A_{k_i}$, $k_i \geq 1$. By Lemma 3 (degree induction, using the degree-projection of Lemma 2), $A_n \subseteq A_0[x_1, \dots, x_s]$ for every $n$, so $A = A_0[x_1, \dots, x_s]$. Thus $A$ is finitely generated as an $A_0$-algebra by homogeneous elements of positive degree.
>
> ---
> **Corollary (degree one over a field).** If $A_0 = k$ is a field and $A = k[A_1]$ with $\dim_k A_1 = r + 1 < \infty$, pick a $k$-basis $x_0, \dots, x_r$ of $A_1$. Then $A = k[x_0, \dots, x_r]$, so the graded surjection $k[T_0, \dots, T_r] \twoheadrightarrow A$, $T_i \mapsto x_i$ (with $\deg T_i = 1$), realizes $A$ as a homogeneous quotient of the polynomial ring. By $(2) \Rightarrow (1)$, $A$ is Noetherian, and $\operatorname{Proj} A \hookrightarrow \operatorname{Proj} k[T_0, \dots, T_r] = \mathbb{P}^r_k$ is a closed embedding. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Rees algebra of any ideal in a Noetherian ring.** Given a Noetherian ring $R$ and an ideal $\mathfrak{a} = (a_1, \dots, a_r)$, the Rees algebra $R^* = \bigoplus_n \mathfrak{a}^n$ has $R^*_0 = R$ Noetherian and is generated over $R$ by $a_1, \dots, a_r$ in degree one, so the theorem makes $R^*$ Noetherian. The recognition is non-obvious because $R^*$ is presented as an infinite direct sum; the application is the linchpin of [[Thm - The Artin-Rees Lemma|Artin–Rees]] (see [[Ex - The Rees algebra is Noetherian]]).

**Cohomology rings of compact Lie groups and spaces.** The singular cohomology $H^*(X; k)$ of a nice space is a graded $k$-algebra, and finite generation in the sense of this theorem is the statement that $X$ has "finite topological complexity" — e.g. $H^*(\mathbb{CP}^\infty; k) = k[x]$ is generated in degree two, $H^*(BU(n); k) = k[c_1, \dots, c_n]$ by Chern classes. The theorem-shaped question "is this cohomology ring Noetherian?" is exactly the question of whether the space has finitely generated cohomology, central to the theory of finite group cohomology (Evens–Venkov). The application is non-obvious because it exports a commutative-algebra finiteness criterion to algebraic topology.

**Invariant rings and Hilbert's fourteenth problem.** For a linearly reductive group $G$ acting on $V$, the invariant ring $k[V]^G$ is a graded subalgebra of $k[V]$, and Hilbert's theorem that it is finitely generated is *precisely* the statement that it satisfies condition $(2)$, hence is Noetherian. Whether finite generation holds for general $G$ is Hilbert's fourteenth problem (false in general, Nagata). The application is non-obvious because it frames a deep invariant-theory question as the graded-Noetherian criterion applied to a ring of invariants.

---

# Bridges

- **[[Thm - Hilbert's Basis Theorem|Hilbert's Basis Theorem]]** — the engine of the easy direction. Hilbert's basis theorem says $R$ Noetherian implies $R[T]$ Noetherian; iterating gives $R[T_1, \dots, T_s]$ Noetherian, and since a finitely generated $A_0$-algebra is a quotient of such a polynomial ring, finite generation over a Noetherian base forces Noetherian-ness. This theorem is the graded *converse*-and-refinement: it pins down that, for graded rings, Noetherian-ness is *equivalent* to finite generation over the base, not merely implied by it.

- **[[Def - The Associated Graded Ring and the Rees Algebra|The Rees algebra and associated graded ring]]** — the two graded rings to which this criterion is applied. The Rees algebra $R^* = \bigoplus \mathfrak{a}^n$ is generated in degree one by generators of $\mathfrak{a}$, so it is Noetherian when $R$ is; the associated graded ring $\operatorname{gr}_{\mathfrak{a}}(R) = R^*/\mathfrak{a}R^*$ inherits Noetherian-ness as a quotient. This theorem is what certifies both, and so it is the algebraic foundation under Artin–Rees and dimension theory.

- **[[Def - The Hilbert Function and Hilbert Polynomial|Hilbert function and Hilbert polynomial]]** — the downstream payoff. Once $A$ is a Noetherian graded $k$-algebra and $M$ a finitely generated graded module, each $M_n$ is finite-dimensional over $k$, so the Hilbert function $n \mapsto \dim_k M_n$ exists and (Hilbert–Serre) is eventually polynomial. The finiteness of each graded piece — which this theorem guarantees — is exactly what makes the Hilbert function defined and the Krull dimension extractable.

# Unlocked by This

> [!tip] Projective varieties as Proj of graded rings *(from Algebraic Geometry)*
> This theorem is the algebraic licence for the entire **Proj** construction. A **projective variety** over $k$ is $\operatorname{Proj} A$ for $A$ a Noetherian graded $k$-algebra generated in degree one; the theorem says these are exactly the finitely-generated-in-degree-one $k$-algebras, and the corollary says such an $A$ embeds $\operatorname{Proj} A$ as a closed subvariety of $\mathbb{P}^r$ where $r + 1 = \dim_k A_1$. **Generation in degree one is the existence of a projective embedding** — the degree-one piece supplies the homogeneous coordinates. A Veronese re-embedding (replace $A$ by its $d$-th Veronese subring $\bigoplus_n A_{nd}$) can force generation in degree one, which is why every projective variety, after re-embedding, sits in some $\mathbb{P}^r$. The Noetherian-ness this theorem provides is what makes $\operatorname{Proj} A$ quasi-compact and of finite type — a genuine algebraic variety rather than an infinite-dimensional object.
