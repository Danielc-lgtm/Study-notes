---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sobolev Multiplication Theorem"
  - "Thm - Sobolev Embedding Theorem"
  - "Def - Sobolev Space of Sections"
tags: [geometry, gauge-theory, analysis]
---

# Notation

Throughout, $M$ is a compact smooth manifold of dimension $n$ (smooth, Hausdorff, second countable, as always in this series), equipped with a fixed Riemannian metric, and $k$ is a positive integer with $2k > n$. For a finite-dimensional real or complex vector space $V$ we write $H_k(M; V) := W^{k,2}(M; M \times V)$ for the [[Def - Sobolev Space of Sections|Sobolev space]] of $V$-valued functions of Sobolev class $k$ in $L^2$, with norm $\lVert u \rVert_k := \big(\sum_{i \le k} \lVert \nabla^i u \rVert_{L^2}^2\big)^{1/2}$, where $\nabla^i u$ is the $i$-th iterated covariant derivative. We abbreviate $H_k(M; \mathbb{C})$ and $H_k(M; \mathbb{R})$ and, for the sphere $S^1 = \{z \in \mathbb{C} : |z| = 1\}$, write $H_k(M; S^1) := \{g \in H_k(M; \mathbb{C}) : |g(x)| = 1 \text{ for all } x \in M\}$; the pointwise condition is meaningful because, as recorded below, every element of $H_k(M; \mathbb{C})$ has a continuous representative when $2k > n$.

A function $f : \mathbb{C} \to \mathbb{C}$ is **entire** if it is holomorphic on all of $\mathbb{C}$; equivalently it is given by a power series $f(z) = \sum_{j \ge 0} a_j z^j$ with $a_j \in \mathbb{C}$ whose radius of convergence is infinite, so that $\sum_{j \ge 0} |a_j|\, t^j < \infty$ for every real $t \ge 0$. Its derivative is $f'(z) = \sum_{j \ge 1} j a_j z^{j-1}$, again entire. The leading example is $f = \exp$, with $a_j = 1/j!$ and $f' = \exp$.

We recall the differential calculus of maps between Banach spaces, since it is the language of the statement and is used throughout without a separate vault page. Let $X, Y$ be real Banach spaces and $U \subseteq X$ open. A map $F : U \to Y$ is **Fréchet differentiable** at $x \in U$ if there is a bounded linear operator $DF(x) \in \mathcal{L}(X, Y)$ (the space of bounded linear maps $X \to Y$, with the operator norm $\lVert T \rVert = \sup_{\lVert v \rVert \le 1} \lVert Tv \rVert$) such that
$$\frac{\lVert F(x + v) - F(x) - DF(x)\,v \rVert_Y}{\lVert v \rVert_X} \longrightarrow 0 \qquad \text{as } \lVert v \rVert_X \to 0 ;$$
we write this remainder condition as $F(x+v) - F(x) - DF(x)v = o(\lVert v \rVert)$. The map $F$ is of class $C^1$ if it is Fréchet differentiable at every point and the derivative map $DF : U \to \mathcal{L}(X, Y)$ is continuous; it is of class $C^{r+1}$ if $DF$ is of class $C^r$ (its values lie in the Banach space $\mathcal{L}(X,Y)$), and it is **smooth**, written $C^\infty$, if it is of class $C^r$ for every $r \ge 0$. All the spaces here — $H_k(M; \mathbb{C})$ included — are regarded as real Banach spaces; the derivatives we obtain turn out to be complex-linear regardless.

A **Banach algebra** is a Banach space $\mathcal{A}$ carrying an associative bilinear multiplication that is submultiplicative, $\lVert ab \rVert \le \lVert a \rVert\,\lVert b \rVert$; it is **unital** if it has a multiplicative identity $1$ and **commutative** if $ab = ba$. For $w \in \mathcal{A}$ the **multiplication operator** $M_w : \mathcal{A} \to \mathcal{A}$, $M_w x = wx$, is bounded with $\lVert M_w \rVert \le \lVert w \rVert$ by submultiplicativity.

> [!warning] Convention: renorming to submultiplicativity
> Haydys's Theorem 136 (iv)(a) and the vault [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] give a bounded bilinear product with $\lVert uv \rVert_k \le C \lVert u \rVert_k \lVert v \rVert_k$ for a fixed constant $C = C(M, k) \ge 1$, which is not literally submultiplicative. We use the equivalent norm $\lVert u \rVert_{\mathcal{A}} := C \lVert u \rVert_k$; then $\lVert uv \rVert_{\mathcal{A}} = C\lVert uv\rVert_k \le C \cdot C\lVert u\rVert_k \lVert v\rVert_k = \lVert u\rVert_{\mathcal{A}} \lVert v\rVert_{\mathcal{A}}$, so $(H_k(M; \mathbb{C}), \lVert\cdot\rVert_{\mathcal{A}})$ is a genuine submultiplicative Banach algebra. Because $\lVert\cdot\rVert_{\mathcal{A}}$ and $\lVert\cdot\rVert_k$ are equivalent norms, they define the same topology and the same bounded linear maps, hence the same notion of Fréchet smoothness; every smoothness statement below is therefore norm-independent, and we pass freely between the two norms.

The full symbol registry for the chapter is on the parent page **Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes**.

---

# Statement

> **Theorem (composition with entire functions is smooth on the Sobolev algebra).** Let $M$ be a compact $n$-manifold, let $k$ be a positive integer with $2k > n$, and let $f : \mathbb{C} \to \mathbb{C}$ be entire, $f(z) = \sum_{j \ge 0} a_j z^j$. Then the composition (Nemytskii) operator
> $$F_f : H_k(M; \mathbb{C}) \longrightarrow H_k(M; \mathbb{C}), \qquad F_f(u) = f \circ u,$$
> is a well-defined smooth map between Banach spaces. It is given by the absolutely convergent series $F_f(u) = \sum_{j \ge 0} a_j u^j$, and its Fréchet derivative at $u$ is multiplication by $f' \circ u$:
> $$DF_f(u)\,v = (f' \circ u)\,v \qquad \text{for all } v \in H_k(M; \mathbb{C}).$$

> **Corollary (the exponential and the Sobolev sphere).** With the same hypotheses, the map $\xi \mapsto e^{i\xi}$ is a smooth map $H_k(M; \mathbb{R}) \to H_k(M; \mathbb{C})$, with derivative $v \mapsto i\,e^{i\xi}\,v$, and its image lies in $H_k(M; S^1) = \{g \in H_k(M; \mathbb{C}) : |g| = 1\}$. Moreover, for $2k > n$ the set $\mathcal{G}^{k} := H_k(M; S^1)$ is a group under pointwise multiplication, with the inverse of $g$ given by its complex conjugate $g^{-1} = \bar g \in H_k(M; \mathbb{C})$.

The two blockquotes are tied together as follows: the corollary is the theorem applied to $f = \exp$ precomposed with the bounded linear map $\xi \mapsto i\xi$, together with the algebra property, and it is exactly the input the Seiberg–Witten construction needs — it is what makes the Sobolev gauge group $\mathcal{G}^{k,p}$ a Banach Lie group (Haydys's unnumbered definition on p. 63, our **Def - Sobolev Gauge Group and Configuration Space** in Gauge Theory XI) and what makes the gauge action smooth in the slice theorem.

---

# Motivation

The Seiberg–Witten equations, and gauge theory generally, are studied on a *configuration space* and a *gauge group* completed in a Sobolev norm rather than in the smooth category, because only in a Banach space does one have the implicit and inverse function theorems, transversality, and the Fredholm theory that the moduli-space construction rests on (this is the reason for the entire elliptic chapter). Haydys states the passage to Sobolev completions in one sentence on p. 63: the gauge group $\mathcal{G}^{k,p}$ of maps $M \to S^1$ of Sobolev class $W^{k,p}$ is, for $kp > \dim M$, "a Banach Lie group by the Sobolev multiplication theorem", with Lie algebra $W^{k,p}(M; \mathbb{R}i)$. That single sentence hides two analytic facts, and this page supplies the second of them.

The first fact is that $\mathcal{G}^{k,p}$ is a *group* at all: the product of two $S^1$-valued Sobolev maps must again be a Sobolev map. This is immediate from the [[Thm - Sobolev Multiplication Theorem|multiplication theorem]] once one knows the target is closed under multiplication, and we prove it in the corollary. The second, deeper, fact is that $\mathcal{G}^{k,p}$ is a *smooth Banach manifold* whose charts are the exponential maps $\xi \mapsto g_0\, e^{i\xi}$ — and for this to define a smooth atlas one must know that $\xi \mapsto e^{i\xi}$ is a *smooth* map between the Banach spaces $H_k(M; \mathbb{R})$ and $H_k(M; \mathbb{C})$, not merely a continuous one. Continuity is not enough: a Lie group needs its multiplication, inversion, and chart transitions to be differentiable to all orders, and the chart transitions here are built out of the exponential and its inverse. The question this page answers is therefore precise and unavoidable: *is post-composition with a fixed analytic function of the values a smooth operation on a Sobolev space?*

The alternative one might hope for — that composition with *any* smooth $f : \mathbb{C} \to \mathbb{C}$ is smooth on $H_k$ — is more delicate and is not what the applications need; the clean and complete answer is available precisely for *entire* $f$, and it is clean for a structural reason. When $2k > n$ the [[Thm - Sobolev Multiplication Theorem|multiplication theorem]] makes $H_k(M; \mathbb{C})$ a Banach algebra, and in *any* Banach algebra a convergent power series behaves exactly like a convergent power series of one scalar variable: it converges, and it may be differentiated term by term. The composition operator $F_f$ is nothing but the power series $\sum a_j u^j$ evaluated at the algebra element $u$, so its smoothness is a fact about Banach algebras with no reference to manifolds, Sobolev norms, or Fourier series at all. The Sobolev theory contributes exactly one thing — that $H_k$ *is* such an algebra — and the rest is the holomorphic functional calculus.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypotheses are that $2k > n$ and that $f$ is entire, so the real question is: when does a problem hand you a composition operator of this shape, even when no power series is written down?

The first disguised source is **a group-valued or sphere-valued field appearing as a gauge degree of freedom**. Whenever a construction has a $U(1) = S^1$ symmetry — electromagnetism, the determinant line bundle of a $\mathrm{spin}^c$ structure, any abelian gauge theory — the gauge transformations are maps into $S^1$, and near the identity every such map is $e^{i\xi}$ for a real function $\xi$. The bridge $B \Rightarrow A$ is the observation that $S^1 \subset \mathbb{C}$ and $e^{i\,\cdot} = \exp \circ (i\,\cdot\,)$, so a manifestly geometric object (a phase field) is secretly the value of the entire function $\exp$ on a scalar field. *Example problem:* show that the Sobolev gauge group $\mathcal{G}^{k} = H_k(M; S^1)$ is a Banach Lie group modelled on $H_k(M; \mathbb{R}i)$, by using $\xi \mapsto g_0 e^{i\xi}$ as charts.

The second disguised source is **a polynomial or analytic nonlinearity in a partial differential equation**. Nonlinear terms such as the Seiberg–Witten quadratic $\mu(\psi) = \psi\psi^* - \tfrac12 |\psi|^2$, or reaction terms like $e^u$ in a semilinear equation, are compositions of the unknown with a fixed entire (here even polynomial) function. The bridge is that a polynomial is a terminating — hence entire — power series, so the theorem applies verbatim and shows the nonlinear map is smooth on $H_k$ once $2k > n$. The non-obvious part is recognising that "the nonlinearity is polynomial in the field and its conjugate" is exactly the hypothesis "$f$ entire" in disguise. *Example problem:* show that $\psi \mapsto |\psi|^2 \psi$ is a smooth self-map of $H_k(M; \mathbb{C})$ for $2k > n$.

The third, and most abstract, disguised source is **any Banach space that also carries a continuous bilinear multiplication** — that is, any Banach algebra after renorming. The bridge $B \Rightarrow A$ is the elementary renorming recorded in the convention callout: a continuous product $\lVert ab \rVert \le C \lVert a \rVert \lVert b \rVert$ becomes literally submultiplicative under $\lVert \cdot \rVert' := C\lVert \cdot \rVert$, and Fréchet smoothness is insensitive to the equivalent norm. Every conclusion of this page therefore transfers unchanged to the algebra of bounded operators $\mathcal{L}(X)$, to $C^0(M)$, to matrix-valued Sobolev functions $H_k(M; \mathfrak{gl}_r(\mathbb{C}))$ (a *non-commutative* algebra), and to Wiener-type algebras. *Example problem:* show that $A \mapsto e^{A}$ is smooth on the Banach algebra $H_k(M; \mathfrak{gl}_r(\mathbb{C}))$ of matrix-valued Sobolev functions, with derivative $B \mapsto \sum_{j\ge1}\tfrac1{j!}\sum_{i=0}^{j-1} A^i B A^{j-1-i}$.

**Targets (Output Amplification)**

The bare conclusion is that $F_f$ is smooth with a known derivative. Combined with other results it does far more.

Combine the smoothness of $\xi \mapsto e^{i\xi}$ with the **inverse function theorem in Banach spaces**. The derivative of $\xi \mapsto e^{i\xi}$ at $\xi = 0$ is $v \mapsto iv$, an isomorphism onto its image, so near the identity the exponential is a diffeomorphism from a neighbourhood of $0$ in $H_k(M; \mathbb{R})$ onto a neighbourhood of $1$ in $H_k(M; S^1)$. The payoff $E$ is a smooth chart at the identity, and translating it by group multiplication gives charts everywhere: this is precisely the statement that $\mathcal{G}^{k} = H_k(M; S^1)$ is a Banach Lie group with Lie algebra $H_k(M; \mathbb{R}i)$.

Combine the smoothness of $F_f$ with the **implicit function theorem and the equivariance of the Seiberg–Witten map**. The gauge action $(\psi, A) \cdot g = (\bar g \psi, A + 2 g^{-1} dg)$ involves multiplication by $g$ and by $g^{-1} dg$, both smooth by this theorem and the multiplication theorem; the extra ingredient is the ellipticity of the linearised operator, and the payoff is that the action of $\mathcal{G}^{k+1}$ on the configuration space is smooth and admits local slices (Haydys's Proposition 207). This is the analytic backbone of the slice theorem and hence of the manifold structure on the moduli space.

Combine the derivative formula $DF_f(u) = M_{f'(u)}$ with the **algebra bound and a fixed-point or continuation argument** to solve nonlinear equations. Because $DF_f$ is itself a composition operator, one can bootstrap regularity: if $u \in H_k$ solves a semilinear elliptic equation with analytic nonlinearity, the derivative is a multiplication operator with $H_k$ coefficients, elliptic estimates apply, and $u$ gains regularity. The payoff is the smoothness of solutions and of the solution map, the mechanism behind [[Thm - Elliptic Regularity and the Elliptic Estimate|elliptic regularity]] for nonlinear equations.

---

# Why Is It True

Forget the Sobolev norm for a moment and picture the space $H_k(M; \mathbb{C})$ purely as an algebra: an associative, commutative ring of "numbers" $u$ that happens to be a complete normed space in which the product is continuous. In the field $\mathbb{C}$ itself, an entire function $f(z) = \sum a_j z^j$ is evaluated at a number $z$ by summing its power series, and it is differentiated by summing the term-by-term derivative $\sum j a_j z^{j-1}$. The claim of this page is that *the same two operations work when the number $z$ is replaced by an algebra element $u$*, and they work for the same reason.

Why does the series converge? Because the algebra norm is submultiplicative (after renorming), $\lVert u^j \rVert \le \lVert u \rVert^j$, so the tail of $\sum a_j u^j$ is dominated by the tail of the scalar series $\sum |a_j| \lVert u \rVert^j$, which converges because $f$ is entire; a series in a Banach space that converges absolutely converges. Why can it be differentiated term by term? Because the *only* algebraic facts used to differentiate the scalar monomial $z^j$ — the binomial expansion $(z+h)^j = \sum_i \binom{j}{i} z^{j-i} h^i$ and the observation that the terms of order $h^2$ and higher are negligible — survive verbatim when $z$ and $h$ are commuting algebra elements $u$ and $v$ and $|\cdot|$ is replaced by the submultiplicative norm. The size of the quadratic-and-higher remainder is controlled, uniformly over all the monomials at once, by the same *scalar* second-order Taylor remainder of the majorant series $\phi(t) = \sum |a_j| t^j$, and that is $O(\lVert v \rVert^2)$.

> **The mechanism in one sentence: in a Banach algebra a power series that converges on a scalar disc converges on the corresponding "disc" of algebra elements and may be differentiated term by term, because absolute convergence transports the scalar convergence and the scalar Taylor remainder bounds the algebra remainder monomial by monomial.**

The passage from "differentiable once" to "smooth" is then the cleanest part. The derivative of $F_f$ at $u$ is multiplication by $f'(u)$, where $f'$ is *again* an entire function; so the derivative map $u \mapsto DF_f(u)$ is the composition of the *same kind of map* $F_{f'}$ with the harmless bounded-linear operation "turn an algebra element into the operator of multiplication by it". Each differentiation replaces $f$ by $f'$ and leaves us with a map of exactly the same shape, so a single induction pushes the regularity up to $C^\infty$.

---

# What Makes This Hard

The genuine subtleties are three, and each is a place where a hurried argument goes wrong. First, $H_k$ is a Banach algebra only *after renorming*: the raw Sobolev norm satisfies $\lVert uv \rVert_k \le C \lVert u \rVert_k \lVert v \rVert_k$ with $C > 1$, so one may not write $\lVert u^j \rVert_k \le \lVert u \rVert_k^j$; the correct bound is $\lVert u^j \rVert_k \le C^{j-1} \lVert u \rVert_k^j$, and dropping the factors of $C$ silently gives a false convergence radius. Second, the composition operator $F_f(u) = \sum a_j u^j$ produced by the algebra must be *identified* with the honest pointwise composition $x \mapsto f(u(x))$; this identification is exactly where the [[Thm - Sobolev Embedding Theorem|Sobolev embedding]] $H_k \hookrightarrow C^0$ (valid because $2k > n$) is indispensable, since without a continuous representative "$f \circ u$ pointwise" has no meaning and $H_k(M; S^1)$ cannot even be defined. Third, and most commonly botched, is the step from $C^1$ to $C^\infty$: it is tempting to assert smoothness because "power series are smooth", but the honest argument is the induction on the shape $DF_f = (\text{multiplication representation}) \circ F_{f'}$, and it must be written out, since it is the only place the entirety of $f'$ (not just of $f$) is used.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Renorm $H_k(M; \mathbb{C})$ to a submultiplicative commutative unital Banach algebra using the multiplication theorem. Show the power series $\sum a_j u^j$ converges absolutely and equals the pointwise composition $f \circ u$ (this uses the Sobolev embedding). Prove that a convergent power series in a commutative Banach algebra is Fréchet differentiable with derivative equal to multiplication by the term-by-term-differentiated series, by bounding the algebra remainder with the scalar Taylor remainder of the majorant. Finally, bootstrap from $C^1$ to $C^\infty$ by noting that the derivative map is again a power-series map of the same kind, composed with a bounded linear operator.

**Subgoal decomposition:**

1. **The algebra and the power series.** Show $(H_k(M; \mathbb{C}), C\lVert\cdot\rVert_k)$ is a commutative unital Banach algebra, that $\lVert u^j \rVert_k \le C^{j-1} \lVert u \rVert_k^j$, and that $\sum a_j u^j$ converges absolutely and equals $f \circ u$ as a continuous function.
   - *Hint:* Induct on $j$ using the multiplication bound; dominate by the scalar series $\sum |a_j| t^j$; identify the sum with the pointwise composition through the $C^0$ embedding, where the partial sums converge uniformly.
   - *Why needed:* Without this, $F_f$ is not even a well-defined map into $H_k$, and $H_k(M; S^1)$ is not defined.

2. **First derivative.** Show that in a commutative unital Banach algebra $\mathcal{A}$, the map $F_f(u) = \sum a_j u^j$ is Fréchet differentiable everywhere with $DF_f(u) = M_{f'(u)}$, and that $F_f$ is $C^1$.
   - *Hint:* Expand $(u+v)^j$ by the binomial theorem (valid since $u, v$ commute); the linear term reassembles $f'(u)v$; bound the remainder by $\phi(\lVert u\rVert+\lVert v\rVert) - \phi(\lVert u\rVert) - \phi'(\lVert u\rVert)\lVert v\rVert$ with $\phi = \sum|a_j|t^j$, which is $O(\lVert v\rVert^2)$ by the scalar Taylor remainder.
   - *Why needed:* This is the analytic core; everything else is bookkeeping around it.

3. **Bootstrap to smoothness.** Show that $F_f$ is $C^\infty$.
   - *Hint:* Write $DF_f = \Lambda \circ F_{f'}$, where $\Lambda(w) = M_w$ is bounded linear and $f'$ is entire; a bounded linear map post-composed with a $C^r$ map is $C^r$, so induct on $r$.
   - *Why needed:* Lie-group charts and the implicit function theorem need all derivatives, not just the first.

4. **The exponential and the group.** Deduce the corollary: $\xi \mapsto e^{i\xi}$ is smooth $H_k(M; \mathbb{R}) \to H_k(M; \mathbb{C})$ with image in $H_k(M; S^1)$, and $H_k(M; S^1)$ is a group.
   - *Hint:* Precompose with the bounded linear $\xi \mapsto i\xi$; $|e^{i\xi}| = 1$ pointwise for real $\xi$; conjugation is a norm-preserving map, so $\bar g \in H_k$, and $g\bar g = |g|^2 = 1$.
   - *Why needed:* This is the statement the gauge-theory applications actually invoke.

---

# Lemma Decomposition

> [!note]- Lemma 1: $H_k(M;\mathbb C)$ is a Banach algebra and the power series converges to the pointwise composition
> **Statement:** Let $M$ be compact and $2k > n$. Then, with the norm $\lVert u \rVert_{\mathcal{A}} := C \lVert u \rVert_k$ (with $C = C(M,k) \ge 1$ the constant of the multiplication theorem), $H_k(M; \mathbb{C})$ is a commutative unital Banach algebra: the pointwise product is associative, commutative, submultiplicative in $\lVert\cdot\rVert_{\mathcal{A}}$, and has unit the constant function $1$. Moreover $\lVert u^j \rVert_k \le C^{j-1} \lVert u \rVert_k^j$ for every $j \ge 1$; and for any entire $f(z) = \sum_j a_j z^j$ and any $u \in H_k(M; \mathbb{C})$, the series $\sum_{j \ge 0} a_j u^j$ converges absolutely in $H_k(M; \mathbb{C})$, and its sum is the continuous function $x \mapsto f(u(x))$.
>
> **Hint:** Induct for the power bound; dominate by the scalar majorant series; use $H_k \hookrightarrow C^0$ so partial sums converge uniformly and the sum is the honest composition.
>
> **Why needed:** It makes $F_f$ a well-defined map into $H_k$, identifies it with the composition operator, and supplies the estimate every later argument leans on.
>
> > [!note]- Full proof
> > **Step 0 — the multiplication theorem provides the product.** Since $2k > n$, i.e. $k \cdot 2 > n$, the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] (part (a): *for $2k > n$, pointwise multiplication extends to a bounded bilinear map $H_k(M) \times H_k(M) \to H_k(M)$ with $\lVert uv \rVert_k \le C \lVert u \rVert_k \lVert v \rVert_k$*) applies. It is stated there for real-valued functions; for complex-valued $u, v$ we apply it to the smooth $\mathbb{R}$-bilinear bundle map $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \to \mathbb{C}$ given by complex multiplication (equivalently, expand $uv$ into products of the four real functions $\operatorname{Re} u, \operatorname{Im} u, \operatorname{Re} v, \operatorname{Im} v$ and add), obtaining a constant $C = C(M, k) \ge 1$ with
> > $$\lVert uv \rVert_k \le C \lVert u \rVert_k \lVert v \rVert_k \qquad (u, v \in H_k(M; \mathbb{C})) \qquad \text{(multiplication theorem, complex version).}$$
> >
> > **Step 1 — the algebra axioms.** Pointwise multiplication of complex-valued functions is associative and commutative, and the constant function $1$ (smooth, hence in every $H_k$ because $M$ is compact) is its identity; these identities hold on the dense subspace of smooth sections and extend by continuity of the product to all of $H_k$. With $\lVert u \rVert_{\mathcal{A}} := C \lVert u \rVert_k$ we compute, as in the convention callout,
> > $$\lVert uv \rVert_{\mathcal{A}} = C \lVert uv \rVert_k \le C \cdot C \lVert u \rVert_k \lVert v \rVert_k = (C \lVert u \rVert_k)(C \lVert v \rVert_k) = \lVert u \rVert_{\mathcal{A}} \lVert v \rVert_{\mathcal{A}} \qquad \text{(by Step 0),}$$
> > so $\lVert\cdot\rVert_{\mathcal{A}}$ is submultiplicative. As $H_k$ is complete (it is a [[Def - Sobolev Space of Sections|Sobolev space]], a completion by construction) and $\lVert\cdot\rVert_{\mathcal{A}} = C\lVert\cdot\rVert_k$ is equivalent to $\lVert\cdot\rVert_k$, it is a Banach norm; hence $(H_k(M;\mathbb{C}), \lVert\cdot\rVert_{\mathcal{A}})$ is a commutative unital Banach algebra.
> >
> > **Step 2 — the power bound.** We show $\lVert u^j \rVert_k \le C^{j-1} \lVert u \rVert_k^j$ by induction on $j \ge 1$. **Base case** $j = 1$: $\lVert u^1 \rVert_k = \lVert u \rVert_k = C^0 \lVert u \rVert_k$. **Inductive step:** assuming the bound for $j$,
> > $$\lVert u^{j+1} \rVert_k = \lVert u \cdot u^j \rVert_k \le C \lVert u \rVert_k \lVert u^j \rVert_k \le C \lVert u \rVert_k \cdot C^{j-1} \lVert u \rVert_k^j = C^{j} \lVert u \rVert_k^{j+1} \qquad \text{(Step 0, then inductive hypothesis),}$$
> > which is the bound for $j+1$. Equivalently, in the renormed algebra, $\lVert u^j \rVert_{\mathcal{A}} = C\lVert u^j\rVert_k \le C \cdot C^{j-1}\lVert u\rVert_k^j = (C\lVert u\rVert_k)^j = \lVert u \rVert_{\mathcal{A}}^j$, which is just submultiplicativity iterated.
> >
> > **Step 3 — absolute convergence.** For fixed $u$, using Step 2,
> > $$\sum_{j \ge 0} \lVert a_j u^j \rVert_k = |a_0|\,\lVert 1\rVert_k + \sum_{j \ge 1} |a_j|\, \lVert u^j \rVert_k \le |a_0|\,\lVert 1\rVert_k + \sum_{j \ge 1} |a_j|\, C^{j-1} \lVert u \rVert_k^j = |a_0|\,\lVert 1\rVert_k + C^{-1}\!\sum_{j \ge 1} |a_j|\,(C \lVert u \rVert_k)^j .$$
> > The last series is $C^{-1}\big(\phi(C\lVert u\rVert_k) - |a_0|\big)$, where $\phi(t) := \sum_{j \ge 0} |a_j| t^j$; since $f$ is entire, its majorant series $\phi$ has infinite radius of convergence, so $\phi(C\lVert u\rVert_k) < \infty$ (justification: the radius of convergence of $\sum |a_j| t^j$ equals that of $\sum a_j z^j$, namely $+\infty$). Hence $\sum_j \lVert a_j u^j \rVert_k < \infty$: the series is absolutely convergent. In a Banach space an absolutely convergent series converges (the partial sums $S_N = \sum_{j \le N} a_j u^j$ satisfy $\lVert S_N - S_{N'}\rVert_k \le \sum_{j = N'+1}^{N} \lVert a_j u^j\rVert_k \to 0$ as $N, N' \to \infty$ by the Cauchy criterion for the convergent scalar tail, so $(S_N)$ is Cauchy and converges by completeness). Denote the sum $F_f(u) \in H_k(M; \mathbb{C})$.
> >
> > **Step 4 — identification with the pointwise composition.** Because $2k > n$, i.e. $k - \tfrac n2 > 0$, the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] (part (ii) with $r = 0$: *for $k - \tfrac n2 > r$ there is a continuous injection $H_k(M; E) \hookrightarrow C^r(M; E)$ with $\lVert u \rVert_{C^r} \le C' \lVert u \rVert_k$*) gives a bounded inclusion $H_k(M; \mathbb{C}) \hookrightarrow C^0(M; \mathbb{C})$; we take $u$ to be its continuous representative. Convergence of $S_N \to F_f(u)$ in $H_k$ then implies $\lVert S_N - F_f(u) \rVert_{C^0} \le C' \lVert S_N - F_f(u) \rVert_k \to 0$, i.e. $S_N \to F_f(u)$ uniformly on $M$. On the other hand, for each fixed $x \in M$ the scalar value $u(x) \in \mathbb{C}$ satisfies $S_N(x) = \sum_{j \le N} a_j\, u(x)^j \to f(u(x))$ (definition of $f$ as its power series, evaluated at the number $u(x)$; convergent because $\phi(|u(x)|) < \infty$). A uniform limit and a pointwise limit of the same sequence of continuous functions agree, so $F_f(u)(x) = f(u(x))$ for every $x$. Therefore the algebra element $F_f(u)$ is exactly the continuous function $x \mapsto f(u(x))$, and $F_f(u) = f \circ u$ as claimed. $\blacksquare$

> [!note]- Lemma 2: A convergent power series in a commutative Banach algebra is $C^1$ with the term-by-term derivative
> **Statement:** Let $\mathcal{A}$ be a commutative unital Banach algebra with submultiplicative norm $\lVert\cdot\rVert$, and let $f(z) = \sum_{j \ge 0} a_j z^j$ be entire. Define $F_f : \mathcal{A} \to \mathcal{A}$, $F_f(u) = \sum_{j \ge 0} a_j u^j$ (convergent by the argument of Lemma 1, Step 3, which uses only submultiplicativity). Then $F_f$ is Fréchet differentiable at every $u \in \mathcal{A}$ with derivative the multiplication operator
> $$DF_f(u) = M_{f'(u)}, \qquad M_{f'(u)}\,v = f'(u)\,v, \quad f'(u) := F_{f'}(u) = \sum_{j \ge 1} j a_j u^{j-1},$$
> and $F_f$ is of class $C^1$.
>
> **Hint:** Binomial-expand $(u+v)^j$; the linear-in-$v$ terms sum to $f'(u)v$; the higher terms are bounded, monomial by monomial, by the scalar Taylor remainder of the majorant $\phi(t) = \sum |a_j| t^j$.
>
> **Why needed:** It is the analytic heart of the theorem; applied to $\mathcal{A} = H_k(M;\mathbb{C})$ it gives the first derivative, and applied repeatedly (Lemma 3) it gives all of them.
>
> > [!note]- Full proof
> > **Step 0 — the candidate derivative is a bounded operator, and it is well-defined.** Since $f' (z)= \sum_{j \ge 1} j a_j z^{j-1}$ is entire (its coefficients $j a_j$ define a series of the same infinite radius of convergence, because $\limsup_j |j a_j|^{1/j} = \limsup_j |a_j|^{1/j} = 0$), the element $f'(u) = F_{f'}(u) \in \mathcal{A}$ is defined by an absolutely convergent series exactly as in Lemma 1. Multiplication by any $w \in \mathcal{A}$ is bounded, $\lVert M_w v \rVert = \lVert wv \rVert \le \lVert w \rVert \lVert v \rVert$, so $\lVert M_w \rVert \le \lVert w \rVert$; in particular $M_{f'(u)} \in \mathcal{L}(\mathcal{A})$.
> >
> > **Step 1 — the increment, term by term.** Fix $u \in \mathcal{A}$ and let $v \in \mathcal{A}$. Because $\mathcal{A}$ is commutative, $u$ and $v$ commute, and the binomial theorem holds:
> > $$(u + v)^j = \sum_{i=0}^{j} \binom{j}{i} u^{j-i} v^i \qquad \text{(binomial theorem, valid since } uv = vu\text{).}$$
> > Isolating the $i = 0$ and $i = 1$ terms, $u^j$ and $j u^{j-1} v$,
> > $$(u+v)^j - u^j - j u^{j-1} v = \sum_{i=2}^{j} \binom{j}{i} u^{j-i} v^i \qquad (j \ge 1),$$
> > with the convention that the right-hand side is $0$ for $j = 1$ (and for $j = 0$ the whole left-hand side is $0$). All three series $\sum a_j (u+v)^j$, $\sum a_j u^j$, $\sum j a_j u^{j-1} v = \big(\sum_{j\ge1} j a_j u^{j-1}\big) v = f'(u)v$ converge absolutely (Lemma 1, Step 3, applied to $f$, to $f$, and to $f'$ together with continuity of $M_{(\cdot)}v$), so we may subtract them term by term and interchange the summation with the subtraction:
> > $$F_f(u + v) - F_f(u) - M_{f'(u)} v = \sum_{j \ge 2} a_j \sum_{i=2}^{j} \binom{j}{i} u^{j-i} v^i \qquad \text{(term-by-term, justified by absolute convergence).}$$
> >
> > **Step 2 — the remainder is bounded by a scalar Taylor remainder.** Taking norms and using submultiplicativity $\lVert u^{j-i} v^i \rVert \le \lVert u \rVert^{j-i} \lVert v \rVert^i$ together with the triangle inequality,
> > $$\big\lVert F_f(u+v) - F_f(u) - M_{f'(u)}v \big\rVert \le \sum_{j \ge 2} |a_j| \sum_{i=2}^{j} \binom{j}{i} \lVert u \rVert^{j-i} \lVert v \rVert^{i} \qquad \text{(triangle inequality, submultiplicativity).}$$
> > For each $j$ the inner scalar sum is, by the binomial theorem for the real numbers $\lVert u\rVert, \lVert v\rVert \ge 0$,
> > $$\sum_{i=2}^{j} \binom{j}{i} \lVert u \rVert^{j-i} \lVert v \rVert^{i} = (\lVert u \rVert + \lVert v \rVert)^j - \lVert u \rVert^j - j \lVert u \rVert^{j-1} \lVert v \rVert \qquad \text{(subtracting the } i=0,1 \text{ terms).}$$
> > Write $s := \lVert u \rVert$ and $t := \lVert u \rVert + \lVert v \rVert$, so $t - s = \lVert v \rVert$, and recall the majorant $\phi(\tau) := \sum_{j \ge 0} |a_j| \tau^j$, an entire real-analytic function with $\phi'(\tau) = \sum_{j \ge 1} j |a_j| \tau^{j-1}$ and $\phi''(\tau) = \sum_{j \ge 2} j(j-1) |a_j| \tau^{j-2}$, both finite for all $\tau \ge 0$. Summing the previous display against $|a_j|$ gives
> > $$\big\lVert F_f(u+v) - F_f(u) - M_{f'(u)}v \big\rVert \le \sum_{j\ge 0}|a_j|\big[(t)^j - (s)^j - j (s)^{j-1}(t-s)\big] = \phi(t) - \phi(s) - \phi'(s)(t - s),$$
> > where the $j = 0$ and $j = 1$ summands vanish and so may be included freely. By Taylor's theorem for the scalar function $\phi$ with the integral form of the remainder,
> > $$\phi(t) - \phi(s) - \phi'(s)(t-s) = \int_s^t (t - \tau)\, \phi''(\tau)\, d\tau \le \tfrac12 (t - s)^2 \sup_{\tau \in [s,t]} \phi''(\tau) = \tfrac12 \lVert v \rVert^2\, \phi''(\lVert u \rVert + \lVert v \rVert),$$
> > using $t - s = \lVert v\rVert \ge 0$, that $\phi'' \ge 0$ is nondecreasing on $[0,\infty)$ (its coefficients are nonnegative), and $\int_s^t (t-\tau)\,d\tau = \tfrac12 (t-s)^2$.
> >
> > **Step 3 — conclude Fréchet differentiability.** As $\lVert v \rVert \to 0$, $\phi''(\lVert u \rVert + \lVert v \rVert) \to \phi''(\lVert u \rVert)$ by continuity of $\phi''$, hence stays bounded, say by $2K$ for $\lVert v \rVert \le 1$. Then $\big\lVert F_f(u+v) - F_f(u) - M_{f'(u)} v \big\rVert \le K \lVert v \rVert^2$ for $\lVert v \rVert \le 1$, so
> > $$\frac{\big\lVert F_f(u+v) - F_f(u) - M_{f'(u)} v \big\rVert}{\lVert v \rVert} \le K \lVert v \rVert \longrightarrow 0 .$$
> > Therefore $F_f$ is Fréchet differentiable at $u$ with $DF_f(u) = M_{f'(u)}$, a bounded operator by Step 0.
> >
> > **Step 4 — the derivative map is continuous, so $F_f \in C^1$.** For $u, u' \in \mathcal{A}$,
> > $$\lVert DF_f(u) - DF_f(u') \rVert = \lVert M_{f'(u)} - M_{f'(u')} \rVert = \lVert M_{f'(u) - f'(u')} \rVert \le \lVert f'(u) - f'(u') \rVert = \lVert F_{f'}(u) - F_{f'}(u') \rVert,$$
> > using linearity of $w \mapsto M_w$ and the bound $\lVert M_w \rVert \le \lVert w \rVert$ of Step 0. The map $F_{f'} : \mathcal{A} \to \mathcal{A}$ is continuous: indeed it is Fréchet differentiable everywhere (apply Steps 1–3 to the entire function $f'$ in place of $f$), and a Fréchet differentiable map is continuous (from $\lVert F_{f'}(u') - F_{f'}(u) \rVert \le \lVert DF_{f'}(u)\rVert\,\lVert u' - u\rVert + o(\lVert u'-u\rVert) \to 0$). Hence $u \mapsto DF_f(u)$ is continuous into $\mathcal{L}(\mathcal{A})$, and $F_f$ is of class $C^1$. $\blacksquare$

> [!note]- Lemma 3: A power-series map in a Banach algebra is smooth
> **Statement:** With $\mathcal{A}$ and $f$ as in Lemma 2, the map $F_f : \mathcal{A} \to \mathcal{A}$ is of class $C^\infty$.
>
> **Hint:** $DF_f = \Lambda \circ F_{f'}$ where $\Lambda(w) = M_w$ is bounded linear and $f'$ is entire; post-composition by a fixed bounded linear operator preserves $C^r$; induct on $r$.
>
> **Why needed:** The Lie-group charts and the implicit function theorem require every derivative of the exponential, not only the first.
>
> > [!note]- Full proof
> > **Step 0 — the multiplication representation is bounded linear, and preserves regularity.** Let $\Lambda : \mathcal{A} \to \mathcal{L}(\mathcal{A})$, $\Lambda(w) = M_w$. It is linear ($M_{w + w'} = M_w + M_{w'}$ and $M_{cw} = c M_w$ from bilinearity of the product) and bounded, $\lVert \Lambda(w) \rVert = \lVert M_w \rVert \le \lVert w \rVert$ (Lemma 2, Step 0). We first record a general fact.
> >
> > **Claim.** *If $\Phi : \mathcal{A} \to Y$ is of class $C^r$ into a Banach space $Y$, and $L : Y \to Z$ is a bounded linear map into a Banach space $Z$, then $L \circ \Phi$ is of class $C^r$, and $D(L \circ \Phi)(u) = L \circ D\Phi(u)$.* We prove the claim by induction on $r$. For $r = 0$, continuity of $L \circ \Phi$ is immediate from continuity of $\Phi$ and boundedness of $L$. For the differentiability, fix $u$ and compute, for any increment $v$,
> > $$L\Phi(u+v) - L\Phi(u) - L\big(D\Phi(u)v\big) = L\big[\Phi(u+v) - \Phi(u) - D\Phi(u)v\big],$$
> > and since $L$ is bounded, $\big\lVert L[\,\cdot\,] \big\rVert \le \lVert L \rVert \cdot \big\lVert \Phi(u+v) - \Phi(u) - D\Phi(u)v \big\rVert = \lVert L\rVert\, o(\lVert v\rVert) = o(\lVert v \rVert)$; hence $L \circ \Phi$ is Fréchet differentiable with $D(L\circ\Phi)(u) = L \circ D\Phi(u) = L_* \big(D\Phi(u)\big)$, where $L_* : \mathcal{L}(\mathcal{A}, Y) \to \mathcal{L}(\mathcal{A}, Z)$, $T \mapsto L \circ T$, is itself bounded linear with $\lVert L_* \rVert \le \lVert L \rVert$. Thus $D(L \circ \Phi) = L_* \circ D\Phi$. If $\Phi$ is of class $C^r$ with $r \ge 1$, then $D\Phi$ is of class $C^{r-1}$, and by the inductive hypothesis (applied to the bounded linear map $L_*$ and the $C^{r-1}$ map $D\Phi$) the composite $L_* \circ D\Phi = D(L\circ\Phi)$ is of class $C^{r-1}$; hence $L \circ \Phi$ is of class $C^r$. This proves the claim.
> >
> > **Step 1 — the induction on smoothness.** We show by induction on $r \ge 1$ that $F_g$ is of class $C^r$ for *every* entire function $g$. **Base case** $r = 1$: this is Lemma 2. **Inductive step:** suppose that for a fixed $r \ge 1$, $F_g$ is of class $C^r$ for every entire $g$. Let $f$ be entire. Its derivative $f'$ is entire, so by the inductive hypothesis $F_{f'}$ is of class $C^r$. By Lemma 2, $DF_f(u) = M_{f'(u)} = \Lambda\big(F_{f'}(u)\big)$, i.e.
> > $$DF_f = \Lambda \circ F_{f'} .$$
> > Applying the Claim of Step 0 with $\Phi = F_{f'}$ (of class $C^r$) and $L = \Lambda$ (bounded linear), the composite $\Lambda \circ F_{f'} = DF_f$ is of class $C^r$. By definition, a map whose derivative is of class $C^r$ is of class $C^{r+1}$; hence $F_f$ is of class $C^{r+1}$. This completes the induction: $F_f$ is of class $C^r$ for every $r$, i.e. $F_f \in C^\infty$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be compact, $k$ a positive integer with $2k > n$, and $f(z) = \sum_{j\ge0} a_j z^j$ entire. We prove the theorem and then the corollary.
>
> **Step 0 — the setting is well-posed.** By Lemma 1, $\mathcal{A} := H_k(M; \mathbb{C})$, renormed by $\lVert u \rVert_{\mathcal{A}} = C \lVert u \rVert_k$, is a commutative unital Banach algebra, and for each $u \in \mathcal{A}$ the series $\sum_j a_j u^j$ converges absolutely in $H_k$. Hence the map
> $$F_f : H_k(M; \mathbb{C}) \longrightarrow H_k(M; \mathbb{C}), \qquad F_f(u) := \sum_{j \ge 0} a_j u^j$$
> is defined. By Lemma 1, Step 4, $F_f(u)$ is the continuous function $x \mapsto f(u(x))$; that is, $F_f(u) = f \circ u$, so $F_f$ is exactly the composition operator, and it is well-defined and single-valued (the value in $H_k$ is the sum of a convergent series and does not depend on any choice). This establishes well-definedness.
>
> **Step 1 — smoothness.** Because smoothness is unchanged under the equivalent norms $\lVert\cdot\rVert_k$ and $\lVert\cdot\rVert_{\mathcal{A}}$ (convention callout), it suffices to prove $F_f$ smooth as a map of the Banach algebra $(\mathcal{A}, \lVert\cdot\rVert_{\mathcal{A}})$ to itself. This is exactly Lemma 3: a power-series map in a commutative Banach algebra is of class $C^\infty$. Therefore $F_f$ is a smooth map $H_k(M; \mathbb{C}) \to H_k(M; \mathbb{C})$.
>
> **Step 2 — the derivative formula.** By Lemma 2 (the base case supplying the first derivative), $DF_f(u) = M_{f'(u)}$, where $f'(u) = F_{f'}(u) = f' \circ u$ by Lemma 1, Step 4, applied to the entire function $f'$. Thus for every $v \in H_k(M; \mathbb{C})$,
> $$DF_f(u)\,v = M_{f'(u)}\,v = f'(u)\,v = (f' \circ u)\,v \qquad \text{(Lemma 2; Lemma 1, Step 4 for } f'\text{).}$$
> This is the asserted derivative. The theorem is proved.
>
> **Step 3 — the corollary: the exponential is smooth into $H_k(M; S^1)$.** Let $\iota_{\mathbb{R}} : H_k(M; \mathbb{R}) \to H_k(M; \mathbb{C})$ be the inclusion of real- into complex-valued Sobolev functions; it is bounded and linear (indeed norm-preserving, since $\nabla^i$ of a real function is real and its $L^2$ norm is unchanged when viewed in $\mathbb{C}$), hence smooth with constant derivative $\iota_{\mathbb{R}}$. Multiplication by $i$, $\mu_i : w \mapsto iw$, is bounded linear on $H_k(M; \mathbb{C})$ (it is $M_{i\cdot 1}$, or simply scalar multiplication), hence smooth. The exponential $\exp$ is entire with $\exp' = \exp$, so by the theorem $F_{\exp}$ is smooth $H_k(M; \mathbb{C}) \to H_k(M; \mathbb{C})$. The map in question is the composite
> $$H_k(M; \mathbb{R}) \xrightarrow{\ \iota_{\mathbb{R}}\ } H_k(M; \mathbb{C}) \xrightarrow{\ \mu_i\ } H_k(M; \mathbb{C}) \xrightarrow{\ F_{\exp}\ } H_k(M; \mathbb{C}), \qquad \xi \longmapsto e^{i\xi},$$
> a composition of smooth maps (two of them bounded linear), hence smooth. By the chain rule — established for the special case of an outer/inner bounded linear factor inside Lemma 3, Step 0, and applied here to the linear pieces — its derivative at $\xi$ is
> $$D(\xi \mapsto e^{i\xi})\,v = DF_{\exp}(i\xi)\,(iv) = M_{\exp(i\xi)}(iv) = e^{i\xi}\,(iv) = i\,e^{i\xi}\,v \qquad \text{(Step 2 with } f = \exp,\ \exp' = \exp\text{).}$$
> Finally, for real-valued $\xi$ its continuous representative (Sobolev embedding, $2k > n$) satisfies $\xi(x) \in \mathbb{R}$, so $|e^{i\xi(x)}| = 1$ for every $x \in M$; hence $e^{i\xi} \in H_k(M; S^1)$. This proves the first half of the corollary.
>
> **Step 4 — the corollary: $\mathcal{G}^{k} = H_k(M; S^1)$ is a group under pointwise multiplication.** We verify the group axioms clause by clause; throughout, elements of $H_k(M; \mathbb{C})$ are taken with their continuous representatives (Sobolev embedding), so that the pointwise conditions defining $H_k(M; S^1)$ are meaningful.
> >
> **(Closure under multiplication.)** Let $g, h \in H_k(M; S^1)$. By Lemma 1 (the multiplication theorem), $gh \in H_k(M; \mathbb{C})$, and pointwise $|g(x)h(x)| = |g(x)|\,|h(x)| = 1 \cdot 1 = 1$, so $gh \in H_k(M; S^1)$.
> >
> **(Conjugation and inverses.)** Complex conjugation $c : H_k(M; \mathbb{C}) \to H_k(M; \mathbb{C})$, $g \mapsto \bar g$, is well-defined and bounded: it is $\mathbb{R}$-linear and, since $\nabla^i \bar g = \overline{\nabla^i g}$ (the covariant derivative is real, acting on real and imaginary parts separately) and $|\overline{\nabla^i g}| = |\nabla^i g|$ pointwise, it preserves the norm, $\lVert \bar g \rVert_k = \lVert g \rVert_k$. Hence for $g \in H_k(M; S^1)$ we have $\bar g \in H_k(M; \mathbb{C})$, and $|\bar g(x)| = |g(x)| = 1$, so $\bar g \in H_k(M; S^1)$. Moreover, pointwise, $g(x)\,\bar g(x) = |g(x)|^2 = 1$ for every $x$, so $g\,\bar g = 1$ (the constant function $1$, the algebra unit); by commutativity $\bar g\, g = 1$ as well. Thus $\bar g$ is a two-sided multiplicative inverse of $g$ inside $H_k(M; S^1)$, and $g^{-1} = \bar g$.
> >
> **(Associativity, unit.)** Pointwise multiplication of functions is associative, and the constant function $1 \in H_k(M; S^1)$ (it is smooth, $|1| = 1$) is a two-sided identity: $1 \cdot g = g \cdot 1 = g$.
> >
> Therefore $H_k(M; S^1)$ is closed under multiplication and inversion, contains the identity, and is associative: it is a group under pointwise multiplication, with $g^{-1} = \bar g$. This completes the corollary and the proof. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The matrix exponential on a Sobolev loop group.** Replace the abelian target $S^1$ by a matrix Lie group $G \subseteq GL_r(\mathbb{C})$ and consider maps $M \to \mathfrak{g} \subseteq \mathfrak{gl}_r(\mathbb{C})$ of Sobolev class $H_k$, $2k > n$. The algebra $H_k(M; \mathfrak{gl}_r(\mathbb{C}))$ is a *non-commutative* Banach algebra, yet the theorem's Lemmas 1 and 3 apply after the derivative formula in Lemma 2 is replaced by its non-commutative form $DF_f(u)v = \sum_{j\ge1} a_j \sum_{i=0}^{j-1} u^i v u^{j-1-i}$. This shows the exponential $A \mapsto e^A$ is smooth on $H_k(M; \mathfrak{gl}_r)$ and provides charts for the Sobolev gauge group of a non-abelian structure group (relevant to $SU(2)$ instanton gauge theory). The theorem applies because the only property of $H_k$ used is that it is a Banach algebra; it is non-obvious that the abelian derivative formula must be modified while the smoothness argument is untouched.

**Nemytskii operators in semilinear elliptic PDE.** In the analysis of a semilinear equation $\Delta u = f(u)$ with analytic nonlinearity $f$ on a compact manifold, one studies the map $u \mapsto f(u)$ on a Sobolev space to set up a Banach-space fixed-point or Newton scheme. The theorem shows this map is smooth precisely when $2k > n$, so that $H_k$ is an algebra, and gives the linearisation $v \mapsto f'(u)v$ that the Newton iteration and the implicit function theorem require. The application is non-obvious because the analyst usually meets the superposition operator as a pointwise nonlinearity, not as a power series in a Banach algebra, and the algebra viewpoint is what makes its smoothness transparent.

**Holomorphic functional calculus for a bounded operator.** Take $\mathcal{A} = \mathcal{L}(X)$, the bounded operators on a Banach space $X$, and $f$ entire. The theorem (in its non-commutative Banach-algebra generality) shows $T \mapsto f(T)$ is a smooth map $\mathcal{L}(X) \to \mathcal{L}(X)$ with the term-by-term derivative; this is the germ of the holomorphic functional calculus and of the smooth dependence of $e^{tT}$ on $T$, used throughout the theory of $C_0$-semigroups and evolution equations. It applies because $\mathcal{L}(X)$ is a Banach algebra, and it is non-obvious because functional calculus is usually developed by contour integrals rather than by differentiating a power series.

---

# Bridges

- **The Banach Lie group structure of the Sobolev gauge group.** Combining the smoothness of $\xi \mapsto e^{i\xi}$ (this page) with the [[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)|open mapping]] circle of ideas and the inverse function theorem in Banach spaces, one builds a smooth atlas on $\mathcal{G}^{k} = H_k(M; S^1)$: the chart at $g_0$ is $\xi \mapsto g_0\, e^{i\xi}$, defined on a neighbourhood of $0$ in $H_k(M; \mathbb{R})$, and the transition maps are smooth because they are built from the exponential, its local inverse (a branch of $\log$ near $1 \in S^1$, itself analytic), and pointwise multiplication. This is exactly Haydys's unnumbered construction on p. 63, made rigorous; the group operations are smooth by the multiplication theorem, so $\mathcal{G}^{k}$ is a Banach Lie group with Lie algebra $H_k(M; \mathbb{R}i)$.

- **The slice theorem and the moduli space.** The gauge action on the Seiberg–Witten configuration space involves the maps $g \mapsto \bar g \psi$ and $g \mapsto g^{-1} dg$, both smooth by this page and the multiplication theorem; smoothness of the action is the input to the construction of a local slice $(\psi, A) + \ker R^*_{(\psi,A)}$ (Haydys's Proposition 207), which endows the quotient $\mathcal{C}^{5,2}_{\mathrm{irr}} / \mathcal{G}^{6,2}$ with a manifold structure near irreducible configurations. Thus this analytic lemma is a prerequisite for the moduli space being a manifold at all.

- **The renorming principle for Banach algebras.** The single line "a continuous bilinear product becomes submultiplicative under $\lVert \cdot \rVert' = C \lVert \cdot \rVert$" bridges the Sobolev multiplication theorem, which delivers only $\lVert uv \rVert_k \le C \lVert u \rVert_k \lVert v \rVert_k$, to the abstract theory of Banach algebras, which assumes $\lVert ab \rVert \le \lVert a\rVert \lVert b \rVert$. Because Fréchet smoothness is a property of the topology, not of the particular norm, every theorem of Banach-algebra calculus — functional calculus, the spectral radius formula, the smoothness of inversion — becomes available on $H_k$ for $2k > n$ once this renorming is performed.

---

# Unlocked by This

> [!tip] Banach Lie group *(from Global Analysis)*
> A **Banach Lie group** is a group that is also a smooth Banach manifold whose multiplication and inversion are smooth. This page's corollary is precisely the statement that produces the charts, via the exponential $\xi \mapsto g_0 e^{i\xi}$, making the Sobolev gauge group $\mathcal{G}^{k} = H_k(M; S^1)$ such a group, modelled on $H_k(M; \mathbb{R})$. See **Def - Sobolev Gauge Group and Configuration Space** (Gauge Theory XI).

> [!tip] Holomorphic functional calculus *(from Functional Analysis)*
> In any Banach algebra $\mathcal{A}$, an entire function $f$ acts on elements $a \in \mathcal{A}$ by the convergent power series $f(a) = \sum a_j a^j$, and this action is smooth with the term-by-term derivative. This is the entry point to the full **holomorphic functional calculus**, in which $f$ is allowed to be holomorphic only on a neighbourhood of the spectrum of $a$ and $f(a)$ is defined by a Cauchy contour integral; the entire case proved here is the special case needing no spectral theory.
