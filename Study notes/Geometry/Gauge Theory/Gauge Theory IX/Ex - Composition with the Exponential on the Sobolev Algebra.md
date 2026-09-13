---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Composition with Analytic Functions on the Sobolev Algebra"
  - "Thm - Sobolev Multiplication Theorem"
  - "Thm - Sobolev Embedding Theorem"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $M$ is a compact oriented Riemannian $4$-manifold, so the dimension is $n=4$; we fix the Sobolev order $k=3$, for which $2k=6>4=n$. We write $H_3(M;\mathbb{R})$ and $H_3(M;\mathbb{C})$ for the order-$3$, $L^2$-based Sobolev spaces of real- and complex-valued functions on $M$, with norm $\lVert\cdot\rVert_3$; we write $\lVert\cdot\rVert_{C^0}$ for the supremum norm. Because $2k>n$, the space $H_3(M;\mathbb{C})$ is a **commutative Banach algebra** under pointwise multiplication, and because $k-\tfrac n2=3-2=1>0$ there is a continuous embedding $H_3(M;\mathbb{C})\hookrightarrow C^0(M;\mathbb{C})$; both facts are recalled below and are the only analytic inputs.

Prove the following two assertions.

**(A) The exponential map is $C^1$.** The map
$$\Phi:H_3(M;\mathbb{R})\longrightarrow H_3(M;\mathbb{C}),\qquad \Phi(\xi)=e^{i\xi},$$
is well defined (its values lie in $H_3(M;\mathbb{C})$, indeed in $H_3(M;S^1)=\{g\in H_3(M;\mathbb{C}):\lvert g\rvert=1\}$) and is continuously Fréchet differentiable, with derivative at $\xi$ the bounded linear map
$$D\Phi(\xi):H_3(M;\mathbb{R})\to H_3(M;\mathbb{C}),\qquad D\Phi(\xi)v=i\,e^{i\xi}\,v.$$
The differentiability must be proved *directly*, by estimating the remainder
$$\Phi(\xi+v)-\Phi(\xi)-i\,e^{i\xi}v=e^{i\xi}\bigl(e^{iv}-1-iv\bigr)$$
in $H_3$ through the algebra bound, rather than by quoting the general composition theorem.

**(B) The Sobolev sphere is a Banach Lie group.** Deduce that
$$\mathcal{G}:=H_3(M;S^1)=\{g\in H_3(M;\mathbb{C}):\lvert g\rvert=1\}$$
is a group under pointwise multiplication and carries the structure of a smooth Banach Lie group modelled on the real Banach space $H_3(M;\mathbb{R})$, with charts near a point $g_0\in\mathcal{G}$ given by $\xi\mapsto g_0e^{i\xi}$ (the inverse chart being obtained by composing $g\mapsto \bar g_0 g$ with the principal branch of the logarithm near $1\in S^1$).

**Recall.**

The objects in play are the Sobolev algebra $H_3(M;\mathbb{C})$, the algebra bound from the multiplication theorem, the continuous embedding into $C^0$, and — as the general statement this exercise re-proves by hand and then exploits — the composition theorem for entire functions.

![[Thm - Sobolev Multiplication Theorem#Statement]]

In dimension $n=4$ with $k=3$ the hypothesis $2k>n$ reads $6>4$, so part **(a)** applies: there is a constant $C\ge 1$, depending only on $M$ and the chosen norm, with
$$\lVert uv\rVert_3\le C\,\lVert u\rVert_3\,\lVert v\rVert_3\qquad\text{for all }u,v\in H_3(M;\mathbb{C}).$$
Although part (a) is phrased for real-valued functions, complex multiplication $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\to\mathbb{C}$ is a smooth (real-)bilinear bundle map, so the bundle-valued form of part **(b)** gives the same bound on $H_3(M;\mathbb{C})$, with the constant $C$ absorbing the fixed bilinear map. We fix this $C$ once and for all and call it the **algebra constant**.

![[Thm - Sobolev Embedding Theorem#Statement]]

For $n=4$, $k=3$, $r=0$ the hypothesis $k-\tfrac n2>r$ reads $1>0$, so part **(ii)** provides a continuous injection $H_3(M;\mathbb{C})\hookrightarrow C^0(M;\mathbb{C})$: there is a constant $C_{\mathrm{emb}}\ge 1$ with
$$\lVert u\rVert_{C^0}\le C_{\mathrm{emb}}\,\lVert u\rVert_3\qquad\text{for all }u\in H_3(M;\mathbb{C}).$$
Every element of $H_3$ is therefore represented by a genuine continuous function, and $H_3$-convergence implies uniform convergence; we use both facts silently to identify $H_3$-elements with their continuous representatives and to read off pointwise values such as $\lvert g\rvert=1$.

![[Thm - Composition with Analytic Functions on the Sobolev Algebra#Statement]]

This is the theorem the exercise drills. Part (A) is exactly its corollary in the case $f=\exp$, $\xi\mapsto i\xi$, $n=4$, $k=3$, but with the differentiability supplied by an explicit remainder estimate; part (B) is the promised construction of the Banach Lie group $\mathcal{G}^{k}=H_k(M;S^1)$ that the theorem's tie-remark forecasts. We will also need the group facts recorded in the corollary — that $\mathcal{G}$ is closed under products and that $g^{-1}=\bar g$ — which we prove from scratch below.

---

# Convergent Strategy

**Problem class.** This is a *smoothness-of-a-nonlinear-map-between-Banach-spaces* problem, of the kind that recurs whenever an infinite-dimensional configuration space is given a manifold structure. The nonlinear map is a Nemytskii (composition) operator $\xi\mapsto f\circ\xi$, and the target regularity is $C^1$ in the Fréchet sense. The universal engine for such problems, once the underlying Sobolev space is a **Banach algebra**, is *term-by-term control of a power series*: an analytic function is a convergent power series, powers are estimated by the algebra bound, and the derivative is the termwise derivative. The second half of the problem — building a manifold out of the map — is a *chart-construction* problem: produce a homeomorphism from an open set of the model space onto a neighbourhood of each point, and check the transition maps are smooth.

**Assumption pattern.** Two hypotheses do all the work, and each enters in exactly one way. First, $2k>n$ (here $6>4$): this is the *sole* reason $H_3$ is an algebra, and it is used every time two elements are multiplied — in the power series for $e^{i\xi}$, in the remainder, in the derivative $ie^{i\xi}v$, and in the multiplicativity that makes $\mathcal{G}$ a group. Second, $k-\tfrac n2>0$ (here $1>0$): this is the *sole* reason $H_3\hookrightarrow C^0$, and it is used only to see pointwise values — that $\lvert e^{i\xi}\rvert=1$, that a small $\xi$ gives $e^{i\xi}$ close to $1$ uniformly (so a single branch of $\log$ applies), and that the logarithm series converges to the actual principal logarithm rather than to some other sum.

**Theorem routing.** For (A): fix the candidate derivative $L_\xi v:=ie^{i\xi}v$ (bounded linear by the [[Thm - Sobolev Multiplication Theorem|algebra bound]]); write the remainder as $e^{i\xi}(e^{iv}-1-iv)$ using $e^{i(\xi+v)}=e^{i\xi}e^{iv}$; bound $\lVert e^{iv}-1-iv\rVert_3$ by summing the tail $\sum_{j\ge2}\lVert v^j\rVert_3/j!$ with the power-of-the-algebra-bound $\lVert v^j\rVert_3\le C^{j-1}\lVert v\rVert_3^{\,j}$, obtaining $O(\lVert v\rVert_3^2)$; conclude Fréchet differentiability, then prove $\xi\mapsto L_\xi$ is continuous (indeed the map factors as $L=iM\circ\Phi$ with $M$ bounded linear), which upgrades to $C^1$ and, by a one-line bootstrap, to $C^\infty$. For (B): use the [[Thm - Sobolev Embedding Theorem|embedding]] to define chart domains by a small-$H_3$-ball condition, invert $\xi\mapsto g_0e^{i\xi}$ with the principal logarithm, and prove the log side is $C^\infty$ by the very same power-series estimate applied to $\operatorname{Log}$ about $1$.

**Key decision point.** The one genuinely creative move is *organising every estimate around the scalar inequality $e^t-1-t\le\tfrac{t^2}{2}e^t$ transported to the Banach algebra*. Once the remainder is written as $e^{i\xi}(e^{iv}-1-iv)$ and the inner factor as the tail $\sum_{j\ge2}(iv)^j/j!$, the entire proof of (A) is the observation that the algebra bound turns this Banach-space tail into a scalar tail in $\lVert v\rVert_3$, whose second-order smallness is elementary calculus. The second decision — subtler — is to *cut the chart neighbourhood by the $H_3$-norm, not the $C^0$-norm*: the logarithm's power series about $1$ converges in the algebra only when $C\lVert h-1\rVert_3<1$, so the domain must be an $H_3$-ball; the $C^0$-smallness needed to pin down the branch is then a free consequence of the embedding.

---

# Legal Operations Used

These operations are the ones the topic page for this chapter records for the Sobolev algebra; here they are named descriptively and applied to the exponential.

1. **Convert an entire function of a Sobolev element into an absolutely convergent series in the algebra.** For $u\in H_3(M;\mathbb{C})$ and an entire $f=\sum a_j z^j$, the series $\sum a_j u^j$ converges absolutely in $H_3$ because $\lVert u^j\rVert_3\le C^{j-1}\lVert u\rVert_3^{\,j}$; its sum is the continuous function $f\circ u$. Applied with $f=\exp$ to $u=i\xi$, this produces $e^{i\xi}\in H_3$.

2. **Raise the algebra bound to a power.** From $\lVert uv\rVert_3\le C\lVert u\rVert_3\lVert v\rVert_3$ deduce by induction $\lVert u^j\rVert_3\le C^{j-1}\lVert u\rVert_3^{\,j}$ for $j\ge 1$. This is the single estimate behind every convergence and remainder bound on the page.

3. **Recognise multiplication by a fixed algebra element as a bounded linear operator.** For fixed $w\in H_3(M;\mathbb{C})$, the map $M(w):v\mapsto wv$ satisfies $\lVert M(w)v\rVert_3\le C\lVert w\rVert_3\lVert v\rVert_3$, so $M(w)\in\mathcal{L}(H_3,H_3)$ with $\lVert M(w)\rVert\le C\lVert w\rVert_3$, and $w\mapsto M(w)$ is itself bounded linear. This is how the candidate derivative $L_\xi=iM(e^{i\xi})$ is seen to be bounded, and how $L$ inherits the regularity of $\Phi$.

4. **Use the $C^0$-embedding to read pointwise information.** Because $\lVert u\rVert_{C^0}\le C_{\mathrm{emb}}\lVert u\rVert_3$, an $H_3$-small function is uniformly small; this pins the branch of the logarithm and shows $\lvert e^{i\xi}\rvert=1$.

5. **Transport a scalar power-series inequality into the algebra.** The elementary bound $e^t-1-t\le\tfrac{t^2}{2}e^t$ ($t\ge0$), applied to $t=C\lVert v\rVert_3$, converts the Banach-space tail $\sum_{j\ge2}(iv)^j/j!$ into a genuinely second-order remainder.

6. **Bootstrap $C^1$ to $C^\infty$ through a linear post-composition.** Since $D\Phi=iM\circ\Phi$ and $M$ is bounded linear, $M\circ\Phi$ is exactly as regular as $\Phi$; hence $\Phi\in C^p\Rightarrow D\Phi\in C^p\Rightarrow\Phi\in C^{p+1}$.

---

# Hints

> [!note]- Hint 1
> The target derivative is $v\mapsto ie^{i\xi}v$. Before proving anything, check it is even a legal object: is $v\mapsto ie^{i\xi}v$ a *bounded* linear map $H_3(M;\mathbb{R})\to H_3(M;\mathbb{C})$? The multiplication theorem answers this in one line. Differentiability is then the statement that the remainder $\Phi(\xi+v)-\Phi(\xi)-ie^{i\xi}v$ is $o(\lVert v\rVert_3)$.

> [!note]- Hint 2
> Use the functional equation. In the algebra, $e^{i(\xi+v)}=e^{i\xi}e^{iv}$ (both sides are the continuous function with the same pointwise values, and the algebra product is pointwise). Therefore the remainder factors as $e^{i\xi}\bigl(e^{iv}-1-iv\bigr)$. The algebra bound peels off the fixed factor $e^{i\xi}$; everything now depends on estimating $\lVert e^{iv}-1-iv\rVert_3$.

> [!note]- Hint 3
> Expand the inner factor as a series that *starts at $j=2$*: $e^{iv}-1-iv=\sum_{j\ge2}\frac{(iv)^j}{j!}$. Bound each term by $\lVert v^j\rVert_3\le C^{j-1}\lVert v\rVert_3^{\,j}$ and sum. You will meet $\sum_{j\ge2}\frac{(C\lVert v\rVert_3)^j}{j!}=e^{C\lVert v\rVert_3}-1-C\lVert v\rVert_3$. Now recall the scalar inequality $e^t-1-t\le\tfrac{t^2}{2}e^t$.

> [!note]- Hint 4
> For $C^1$ you must show $\xi\mapsto D\Phi(\xi)$ is continuous into $\mathcal{L}(H_3(M;\mathbb{R}),H_3(M;\mathbb{C}))$. Since $\lVert L_{\xi_1}-L_{\xi_2}\rVert\le C\lVert e^{i\xi_1}-e^{i\xi_2}\rVert_3$, it is enough to show $\Phi$ is continuous — and $e^{i\xi_1}-e^{i\xi_2}=e^{i\xi_2}(e^{i(\xi_1-\xi_2)}-1)$ reduces this to the same tail estimate with the sum starting at $j=1$.

> [!note]- Hint 5
> For the group $\mathcal{G}$: products stay in $\mathcal{G}$ by the algebra bound and pointwise modulus $1$; the inverse of $g$ is $\bar g$, and conjugation is bounded on $H_3$. For the charts near $g_0$, do not cut the neighbourhood by the $C^0$-norm. Cut it by the $H_3$-norm: require $\lVert\bar g_0 g-1\rVert_3<r$ with $Cr<1$, so that the logarithm's power series about $1$ converges in the algebra; the embedding then makes $\bar g_0 g$ uniformly close to $1$ for free, so the *principal* branch is the one you are summing.

> [!note]- Hint 6
> To promote the $C^1$ atlas to a *smooth* Banach Lie group, observe that the transition map is $\xi\mapsto -i\operatorname{Log}(\bar g_1 g_0 e^{i\xi})$, a composition of $\Phi$ (smooth), a bounded linear multiplication (smooth), and $-i\operatorname{Log}$. The last is smooth by the *same* power-series argument applied to the holomorphic function $\operatorname{Log}$ about $1$; its derivative is multiplication by $\operatorname{Log}'\circ h=1/h$, and the $C^1$-to-$C^\infty$ bootstrap runs verbatim.

---

# Solution

The plan is to prove (A) by an explicit second-order remainder estimate and (B) by turning the map $\Phi$ of (A) into a chart. Everything reduces to one inequality — the algebra bound raised to a power, $\lVert v^j\rVert_3\le C^{j-1}\lVert v\rVert_3^{\,j}$ — combined with the elementary scalar fact $e^t-1-t\le\tfrac{t^2}{2}e^t$. We first record the powered algebra bound (Step 1), establish well-definedness and the pointwise interpretation (Step 2), prove Fréchet differentiability (Step 3), upgrade to $C^1$ and then $C^\infty$ (Step 4), and finally assemble the group and its charts (Steps 5–7).

**Step 1: The algebra bound raised to a power.**

For every $u\in H_3(M;\mathbb{C})$ and every integer $j\ge 1$,
$$\lVert u^j\rVert_3\le C^{\,j-1}\,\lVert u\rVert_3^{\,j},$$
where $C\ge 1$ is the algebra constant.

> [!note]- Derivation
> We argue by induction on $j$. **Base case $j=1$:** $\lVert u^1\rVert_3=\lVert u\rVert_3=C^0\lVert u\rVert_3^1$, an equality. **Inductive step:** assume $\lVert u^j\rVert_3\le C^{j-1}\lVert u\rVert_3^{\,j}$. Then
> $$\lVert u^{j+1}\rVert_3=\lVert u\cdot u^{j}\rVert_3\le C\,\lVert u\rVert_3\,\lVert u^{j}\rVert_3\qquad\text{(by the algebra bound, part (a) of the multiplication theorem)}$$
> $$\le C\,\lVert u\rVert_3\cdot C^{\,j-1}\lVert u\rVert_3^{\,j}=C^{\,j}\lVert u\rVert_3^{\,j+1}\qquad\text{(by the inductive hypothesis).}$$
> This closes the induction, so the bound holds for all $j\ge 1$.

**Step 2: $\Phi$ is well defined, with values in $H_3(M;S^1)$.**

For $\xi\in H_3(M;\mathbb{R})$ the series $\sum_{j\ge0}\frac{(i\xi)^j}{j!}$ converges absolutely in $H_3(M;\mathbb{C})$, and its sum is the continuous function $x\mapsto e^{i\xi(x)}$, which has modulus $1$ everywhere. Hence $\Phi(\xi)=e^{i\xi}\in H_3(M;S^1)$.

> [!note]- Derivation
> **Absolute convergence in $H_3$.** Let $\kappa:=\lVert 1\rVert_3=\operatorname{vol}(M)^{1/2}$ be the $H_3$-norm of the constant function $1$ (all its derivatives vanish, so only the $L^2$-term survives). Using Step 1 with $u=i\xi$ (and $\lVert i\xi\rVert_3=\lVert\xi\rVert_3$),
> $$\sum_{j\ge0}\frac{\lVert(i\xi)^j\rVert_3}{j!}=\kappa+\sum_{j\ge1}\frac{\lVert(i\xi)^j\rVert_3}{j!}\le\kappa+\sum_{j\ge1}\frac{C^{\,j-1}\lVert\xi\rVert_3^{\,j}}{j!}=\kappa+\frac1C\bigl(e^{C\lVert\xi\rVert_3}-1\bigr)<\infty\qquad\text{(Step 1; }\sum_{j\ge1}t^j/j!=e^t-1\text{).}$$
> Since $H_3(M;\mathbb{C})$ is complete (it is a Hilbert space), an absolutely convergent series converges; call its sum $w\in H_3$, with $\lVert w\rVert_3\le\kappa+\tfrac1C(e^{C\lVert\xi\rVert_3}-1)$.
>
> **Identification of the sum with the pointwise exponential.** By the embedding $H_3\hookrightarrow C^0$, convergence in $H_3$ implies uniform convergence of the same partial sums; so $w$ is the uniform limit of $\sum_{j\le N}\frac{(i\xi(x))^j}{j!}$. For each fixed $x\in M$ the scalar series $\sum_{j\ge0}\frac{(i\xi(x))^j}{j!}$ converges to $e^{i\xi(x)}$ (the ordinary exponential series, valid for every complex number). A uniform limit and a pointwise limit of the same sequence of continuous functions agree, so $w(x)=e^{i\xi(x)}$ for all $x$; that is, $\Phi(\xi)=e^{i\xi}$ is (represented by) the continuous function $x\mapsto e^{i\xi(x)}$.
>
> **Modulus one.** Since $\xi$ is real-valued, $\lvert e^{i\xi(x)}\rvert=1$ for every $x$, so $\Phi(\xi)\in H_3(M;S^1)$. This proves $\Phi$ maps into the Sobolev sphere.

**Step 3: Fréchet differentiability, with derivative $v\mapsto ie^{i\xi}v$.**

For each fixed $\xi\in H_3(M;\mathbb{R})$ the map $L_\xi:v\mapsto ie^{i\xi}v$ is bounded linear $H_3(M;\mathbb{R})\to H_3(M;\mathbb{C})$, and
$$\bigl\lVert\Phi(\xi+v)-\Phi(\xi)-L_\xi v\bigr\rVert_3\le \tfrac12\,C^2\,\lVert e^{i\xi}\rVert_3\,e^{C\lVert v\rVert_3}\,\lVert v\rVert_3^{\,2}=o(\lVert v\rVert_3)\qquad(\lVert v\rVert_3\to0),$$
so $\Phi$ is Fréchet differentiable at $\xi$ with $D\Phi(\xi)=L_\xi$.

> [!note]- Derivation
> **$L_\xi$ is bounded linear.** Linearity in $v$ is clear. For boundedness, by the algebra bound applied to the product $e^{i\xi}\cdot v$,
> $$\lVert L_\xi v\rVert_3=\lVert i e^{i\xi}v\rVert_3=\lVert e^{i\xi}v\rVert_3\le C\,\lVert e^{i\xi}\rVert_3\,\lVert v\rVert_3\qquad\text{(algebra bound; }\lvert i\rvert=1\text{ leaves the norm unchanged),}$$
> so $L_\xi\in\mathcal{L}(H_3(M;\mathbb{R}),H_3(M;\mathbb{C}))$ with $\lVert L_\xi\rVert\le C\lVert e^{i\xi}\rVert_3$.
>
> **Factorisation of the remainder.** Fix $v\in H_3(M;\mathbb{R})$. The functions $e^{i(\xi+v)}$ and $e^{i\xi}e^{iv}$ are, by Step 2, the continuous functions $x\mapsto e^{i(\xi(x)+v(x))}$ and $x\mapsto e^{i\xi(x)}e^{iv(x)}$; these agree pointwise (the scalar functional equation), and the algebra product of the $H_3$-elements is the pointwise product of their continuous representatives, so
> $$e^{i(\xi+v)}=e^{i\xi}e^{iv}\qquad\text{in }H_3(M;\mathbb{C})\qquad\text{(functional equation, holding pointwise, hence in the algebra).}$$
> Therefore
> $$\Phi(\xi+v)-\Phi(\xi)-L_\xi v=e^{i\xi}e^{iv}-e^{i\xi}-ie^{i\xi}v=e^{i\xi}\bigl(e^{iv}-1-iv\bigr)\qquad\text{(factor out }e^{i\xi}\text{).}$$
>
> **Second-order bound on the inner factor.** The function $e^{iv}-1-iv$ is, again by Step 2, the sum in $H_3$ of the tail series $\sum_{j\ge2}\frac{(iv)^j}{j!}$ (the $j=0$ and $j=1$ terms are exactly the subtracted $1$ and $iv$). Hence
> $$\lVert e^{iv}-1-iv\rVert_3\le\sum_{j\ge2}\frac{\lVert v^j\rVert_3}{j!}\le\sum_{j\ge2}\frac{C^{\,j-1}\lVert v\rVert_3^{\,j}}{j!}=\frac1C\Bigl(e^{C\lVert v\rVert_3}-1-C\lVert v\rVert_3\Bigr)\qquad\text{(triangle inequality in }H_3\text{; Step 1; }\sum_{j\ge2}t^j/j!=e^t-1-t\text{).}$$
> Now use the elementary scalar inequality $e^t-1-t\le\tfrac{t^2}{2}e^t$ for $t\ge0$ — valid because $e^t-1-t=\sum_{j\ge2}\frac{t^j}{j!}=\frac{t^2}{2}\sum_{j\ge0}\frac{2\,t^j}{(j+2)!}\le\frac{t^2}{2}\sum_{j\ge0}\frac{t^j}{j!}=\frac{t^2}{2}e^t$, since $\frac{2}{(j+2)!}\le\frac{1}{j!}$. With $t=C\lVert v\rVert_3$,
> $$\lVert e^{iv}-1-iv\rVert_3\le\frac1C\cdot\frac{(C\lVert v\rVert_3)^2}{2}e^{C\lVert v\rVert_3}=\frac{C}{2}\,e^{C\lVert v\rVert_3}\,\lVert v\rVert_3^{\,2}.$$
>
> **Assembling the estimate.** By the algebra bound on the factorisation,
> $$\bigl\lVert\Phi(\xi+v)-\Phi(\xi)-L_\xi v\bigr\rVert_3=\lVert e^{i\xi}(e^{iv}-1-iv)\rVert_3\le C\,\lVert e^{i\xi}\rVert_3\,\lVert e^{iv}-1-iv\rVert_3\qquad\text{(algebra bound)}$$
> $$\le C\,\lVert e^{i\xi}\rVert_3\cdot\frac{C}{2}e^{C\lVert v\rVert_3}\lVert v\rVert_3^{\,2}=\frac{C^2}{2}\,\lVert e^{i\xi}\rVert_3\,e^{C\lVert v\rVert_3}\,\lVert v\rVert_3^{\,2}\qquad\text{(previous line).}$$
> Dividing by $\lVert v\rVert_3$ gives an upper bound $\tfrac{C^2}{2}\lVert e^{i\xi}\rVert_3\,e^{C\lVert v\rVert_3}\lVert v\rVert_3\to0$ as $\lVert v\rVert_3\to0$ (the exponential tends to $1$ and the last factor to $0$). Therefore the remainder is $o(\lVert v\rVert_3)$, which is the definition of Fréchet differentiability with derivative $L_\xi$. Hence $D\Phi(\xi)=L_\xi$, that is, $D\Phi(\xi)v=ie^{i\xi}v$.

**Step 4: Continuity of the derivative, hence $C^1$, and then $C^\infty$.**

The map $\xi\mapsto D\Phi(\xi)$ is continuous from $H_3(M;\mathbb{R})$ into $\mathcal{L}(H_3(M;\mathbb{R}),H_3(M;\mathbb{C}))$; thus $\Phi\in C^1$. In fact $\Phi\in C^\infty$.

> [!note]- Derivation
> **$\Phi$ is continuous.** For $\xi_1,\xi_2\in H_3(M;\mathbb{R})$, the functional equation of Step 3 gives $e^{i\xi_1}-e^{i\xi_2}=e^{i\xi_2}\bigl(e^{i(\xi_1-\xi_2)}-1\bigr)$, so by the algebra bound,
> $$\lVert\Phi(\xi_1)-\Phi(\xi_2)\rVert_3\le C\,\lVert e^{i\xi_2}\rVert_3\,\bigl\lVert e^{i(\xi_1-\xi_2)}-1\bigr\rVert_3\qquad\text{(algebra bound; functional equation).}$$
> The inner factor is the tail $\sum_{j\ge1}\frac{(i(\xi_1-\xi_2))^j}{j!}$, so by Step 1,
> $$\bigl\lVert e^{i(\xi_1-\xi_2)}-1\bigr\rVert_3\le\sum_{j\ge1}\frac{C^{\,j-1}\lVert\xi_1-\xi_2\rVert_3^{\,j}}{j!}=\frac1C\bigl(e^{C\lVert\xi_1-\xi_2\rVert_3}-1\bigr)\xrightarrow[\ \lVert\xi_1-\xi_2\rVert_3\to0\ ]{}0\qquad(e^0-1=0).$$
> As $\lVert e^{i\xi_2}\rVert_3$ stays bounded when $\xi_2$ is fixed (Step 2), $\Phi$ is continuous at $\xi_2$; since $\xi_2$ was arbitrary, $\Phi$ is continuous.
>
> **Continuity of $D\Phi$.** For any $\xi_1,\xi_2$ and any $v$ with $\lVert v\rVert_3\le1$,
> $$\lVert(L_{\xi_1}-L_{\xi_2})v\rVert_3=\lVert i(e^{i\xi_1}-e^{i\xi_2})v\rVert_3\le C\,\lVert e^{i\xi_1}-e^{i\xi_2}\rVert_3\,\lVert v\rVert_3\le C\,\lVert\Phi(\xi_1)-\Phi(\xi_2)\rVert_3\qquad\text{(algebra bound; }\lVert v\rVert_3\le1\text{).}$$
> Taking the supremum over such $v$ gives $\lVert D\Phi(\xi_1)-D\Phi(\xi_2)\rVert\le C\lVert\Phi(\xi_1)-\Phi(\xi_2)\rVert_3$, which tends to $0$ as $\xi_1\to\xi_2$ by the continuity of $\Phi$. Hence $\xi\mapsto D\Phi(\xi)$ is continuous, and $\Phi\in C^1$.
>
> **Bootstrap to $C^\infty$.** Let $M(w):v\mapsto wv$ be multiplication by $w\in H_3(M;\mathbb{C})$; by operation 3 the assignment $\mathsf{M}:w\mapsto M(w)$ is a *bounded linear* map $H_3(M;\mathbb{C})\to\mathcal{L}(H_3(M;\mathbb{R}),H_3(M;\mathbb{C}))$, with $\lVert\mathsf{M}(w)\rVert\le C\lVert w\rVert_3$. Step 3 says $D\Phi(\xi)=i\,\mathsf{M}(\Phi(\xi))$, i.e. $D\Phi=i\,\mathsf{M}\circ\Phi$. For a bounded linear map $\mathsf{M}$ and any $C^p$ map $\Phi$, the composite $\mathsf{M}\circ\Phi$ is again $C^p$ with $D(\mathsf{M}\circ\Phi)=\mathsf{M}\circ D\Phi$: indeed $\mathsf{M}(\Phi(\xi+v))-\mathsf{M}(\Phi(\xi))-\mathsf{M}(D\Phi(\xi)v)=\mathsf{M}\bigl(\Phi(\xi+v)-\Phi(\xi)-D\Phi(\xi)v\bigr)$ has norm $\le\lVert\mathsf{M}\rVert\cdot o(\lVert v\rVert_3)=o(\lVert v\rVert_3)$, giving the base case, and the derivative formula $D(\mathsf{M}\circ\Phi)=\mathsf{M}\circ D\Phi$ then propagates regularity inductively. Consequently, if $\Phi\in C^p$ then $D\Phi=i\,\mathsf{M}\circ\Phi\in C^p$, whence $\Phi\in C^{p+1}$. Since $\Phi\in C^1$, induction gives $\Phi\in C^p$ for every $p$, that is $\Phi\in C^\infty$. This completes part (A) with room to spare: $\Phi$ is smooth, and in particular $C^1$.

**Step 5: $\mathcal{G}=H_3(M;S^1)$ is a group under pointwise multiplication.**

$\mathcal{G}$ is closed under products, contains the constant $1$, and each $g\in\mathcal{G}$ has inverse $g^{-1}=\bar g\in\mathcal{G}$.

> [!note]- Derivation
> **Closure under products.** If $g,h\in\mathcal{G}$ then $gh\in H_3(M;\mathbb{C})$ by the algebra bound ($\lVert gh\rVert_3\le C\lVert g\rVert_3\lVert h\rVert_3<\infty$), and its continuous representative satisfies $\lvert g(x)h(x)\rvert=\lvert g(x)\rvert\lvert h(x)\rvert=1$ for all $x$, so $gh\in\mathcal{G}$. **Identity.** The constant function $1$ lies in $H_3$ with $\lvert 1\rvert=1$, so $1\in\mathcal{G}$, and it is the multiplicative unit of the algebra. **Inverses.** Complex conjugation $g\mapsto\bar g$ is a bounded $\mathbb{R}$-linear map on $H_3(M;\mathbb{C})$ (it fixes the real part and negates the imaginary part, each an isometry on the corresponding real Sobolev space), so $\bar g\in H_3(M;\mathbb{C})$; moreover $\lvert\bar g\rvert=\lvert g\rvert=1$, so $\bar g\in\mathcal{G}$, and $g\bar g$ is the continuous function $x\mapsto\lvert g(x)\rvert^2=1$, i.e. $g\bar g=1$ in the algebra. Hence $g^{-1}=\bar g$. Associativity and commutativity are inherited from pointwise multiplication of functions. Thus $\mathcal{G}$ is an abelian group.

**Step 6: Charts near $g_0\in\mathcal{G}$.**

Fix the algebra constant $C\ge1$ and the embedding constant $C_{\mathrm{emb}}\ge1$, and set $r:=\tfrac12\min(1/C,\,1/C_{\mathrm{emb}})$, so that $Cr<1$ and $C_{\mathrm{emb}}r<1$. For $g_0\in\mathcal{G}$ define
$$U_{g_0}:=\{g\in\mathcal{G}:\lVert\bar g_0 g-1\rVert_3<r\},\qquad \chi_{g_0}(g):=-i\operatorname{Log}(\bar g_0 g)=-i\sum_{j\ge1}\frac{(-1)^{j-1}}{j}(\bar g_0 g-1)^j,$$
where $\operatorname{Log}$ is the principal branch of the logarithm. Then $\chi_{g_0}$ is a homeomorphism from the open set $U_{g_0}\subset\mathcal{G}$ onto the open set $\Omega_{g_0}:=\{\xi\in H_3(M;\mathbb{R}):g_0e^{i\xi}\in U_{g_0}\}\subset H_3(M;\mathbb{R})$, with inverse $\eta_{g_0}(\xi):=g_0e^{i\xi}$, and the $U_{g_0}$ cover $\mathcal{G}$.

> [!note]- Derivation
> **$U_{g_0}$ is open and covers $\mathcal{G}$.** The map $g\mapsto\bar g_0 g-1$ is continuous $\mathcal{G}\to H_3(M;\mathbb{C})$ (multiplication by the fixed element $\bar g_0$, operation 3, followed by a translation), so $U_{g_0}$, the preimage of the open $H_3$-ball of radius $r$, is open in $\mathcal{G}$. Each $g_0\in U_{g_0}$ since $\lVert\bar g_0 g_0-1\rVert_3=\lVert 1-1\rVert_3=0<r$; hence $\{U_{g_0}\}_{g_0\in\mathcal{G}}$ covers $\mathcal{G}$.
>
> **The logarithm series converges and gives the principal branch.** For $g\in U_{g_0}$ put $h:=\bar g_0 g\in\mathcal{G}$, so $\lVert h-1\rVert_3<r$. By Step 1, $\sum_{j\ge1}\frac1j\lVert(h-1)^j\rVert_3\le\sum_{j\ge1}\frac1j C^{\,j-1}\lVert h-1\rVert_3^{\,j}=\frac1C\sum_{j\ge1}\frac{(C\lVert h-1\rVert_3)^j}{j}$, which converges because $C\lVert h-1\rVert_3<Cr<1$ (the scalar series $\sum t^j/j$ converges for $t<1$). Thus $\operatorname{Log}(h):=\sum_{j\ge1}\frac{(-1)^{j-1}}{j}(h-1)^j$ converges absolutely in $H_3(M;\mathbb{C})$. Moreover $\lVert h-1\rVert_{C^0}\le C_{\mathrm{emb}}\lVert h-1\rVert_3<C_{\mathrm{emb}}r<1$, so pointwise $\lvert h(x)-1\rvert<1$; the scalar series $\sum_{j\ge1}\frac{(-1)^{j-1}}{j}(z-1)^j$ converges to the principal logarithm $\operatorname{Log}z$ on the disc $\lvert z-1\rvert<1$, so the $H_3$-sum agrees pointwise (via the $C^0$-embedding, as in Step 2) with $x\mapsto\operatorname{Log}(h(x))$. Since $\lvert h(x)\rvert=1$, the principal logarithm is purely imaginary, $\operatorname{Log}(h(x))=i\arg h(x)$ with $\arg h(x)\in(-\tfrac\pi3,\tfrac\pi3)$ (because $\lvert h(x)-1\rvert<1$ forces the argument into that arc); therefore $\chi_{g_0}(g)=-i\operatorname{Log}(h)$ is the real-valued function $x\mapsto\arg h(x)$, an element of $H_3(M;\mathbb{R})$.
>
> **$\eta_{g_0}$ and $\chi_{g_0}$ are mutually inverse.** The set $\Omega_{g_0}=\eta_{g_0}^{-1}(U_{g_0})$ is open in $H_3(M;\mathbb{R})$ because $\eta_{g_0}(\xi)=g_0e^{i\xi}=g_0\Phi(\xi)$ is continuous (Step 4, followed by multiplication by the fixed $g_0$). For $\xi\in\Omega_{g_0}$: $g_0e^{i\xi}\in U_{g_0}$ means $\lVert\bar g_0 g_0 e^{i\xi}-1\rVert_3=\lVert e^{i\xi}-1\rVert_3<r$, so $\lVert e^{i\xi}-1\rVert_{C^0}<C_{\mathrm{emb}}r<1$, giving $\xi(x)\in(-\tfrac\pi3,\tfrac\pi3)$ pointwise; hence $\operatorname{Log}(e^{i\xi(x)})=i\xi(x)$ (principal branch on that arc) and
> $$\chi_{g_0}(\eta_{g_0}(\xi))=-i\operatorname{Log}(\bar g_0 g_0 e^{i\xi})=-i\operatorname{Log}(e^{i\xi})=-i\cdot i\xi=\xi.$$
> Conversely, for $g\in U_{g_0}$ with $h=\bar g_0 g$ and $\xi:=\chi_{g_0}(g)=-i\operatorname{Log}(h)$ (so $\xi(x)=\arg h(x)$), we have $e^{i\xi}=e^{\operatorname{Log}(h)}=h$ pointwise (exponential of the principal logarithm recovers $h$), hence in the algebra, so
> $$\eta_{g_0}(\chi_{g_0}(g))=g_0e^{i\xi}=g_0 h=g_0\bar g_0 g=g\qquad(g_0\bar g_0=\lvert g_0\rvert^2=1).$$
> Thus $\chi_{g_0}$ and $\eta_{g_0}$ are inverse bijections between $U_{g_0}$ and $\Omega_{g_0}$.
>
> **Both are continuous.** $\eta_{g_0}$ is continuous by Step 4. For $\chi_{g_0}$, continuity is the statement that $h\mapsto\operatorname{Log}(h)$ is continuous on $\{\lVert h-1\rVert_3<r\}$; this is proved exactly as the continuity of $\Phi$ in Step 4, using $\operatorname{Log}(h_1)-\operatorname{Log}(h_2)$ estimated through the power series and the algebra bound (the geometric-type tail $\sum_{j\ge1}\frac1j(\cdots)$ is dominated because $Cr<1$). Hence $\chi_{g_0}:U_{g_0}\to\Omega_{g_0}$ is a homeomorphism.

**Step 7: The transition maps are smooth; $\mathcal{G}$ is a smooth Banach Lie group.**

The charts $(U_{g_0},\chi_{g_0})$ form a smooth atlas modelled on $H_3(M;\mathbb{R})$, and multiplication and inversion are smooth. Hence $\mathcal{G}$ is a Banach Lie group modelled on $H_3(M;\mathbb{R})$.

> [!note]- Derivation
> **Transition maps.** Let $g_0,g_1\in\mathcal{G}$ with $U_{g_0}\cap U_{g_1}\ne\varnothing$. On the corresponding open subset of $\Omega_{g_0}$ the transition map is
> $$\tau:=\chi_{g_1}\circ\eta_{g_0}:\ \xi\longmapsto -i\operatorname{Log}\bigl(\bar g_1 g_0\,e^{i\xi}\bigr),$$
> a composition of three maps: (1) $\xi\mapsto e^{i\xi}=\Phi(\xi)$, smooth by Step 4; (2) multiplication by the fixed element $\bar g_1 g_0\in H_3(M;\mathbb{C})$, a bounded linear map (operation 3), hence smooth; (3) $h\mapsto-i\operatorname{Log}(h)$ on a neighbourhood of the range. The third map is smooth by the *same* argument as Steps 3–4 applied to the holomorphic function $\operatorname{Log}$ in place of $\exp$: its power series about $1$ converges in the algebra on $\{\lVert h-1\rVert_3<r\}$ (shown in Step 6), the identical second-order remainder estimate — now organised around the scalar bound for $\lvert\operatorname{Log}(1+s)-s\rvert$ — gives Fréchet differentiability with derivative $w\mapsto(\operatorname{Log}'\circ h)\,w=(1/h)\,w$ (note $1/h=\bar h\in H_3$ since $\lvert h\rvert=1$, so the multiplier lies in the algebra), and the bootstrap $D=\mathsf{M}\circ(\cdot)$ through the bounded linear $\mathsf{M}$ (operation 6) upgrades this to $C^\infty$. A composition of smooth maps between Banach spaces is smooth, so $\tau\in C^\infty$. As $g_0,g_1$ were arbitrary, all transition maps are smooth, and the atlas $\{(U_{g_0},\chi_{g_0})\}$ makes $\mathcal{G}$ a smooth Banach manifold modelled on $H_3(M;\mathbb{R})$.
>
> **Smoothness of the group operations.** Read in the charts near $g_0,g_1$ and $g_0g_1$, multiplication $\mu(g,h)=gh$ becomes $(\xi,\zeta)\mapsto\chi_{g_0g_1}\bigl((g_0e^{i\xi})(g_1e^{i\zeta})\bigr)=-i\operatorname{Log}\bigl(e^{i\xi}e^{i\zeta}\bigr)$, a composition of the smooth maps $(\xi,\zeta)\mapsto e^{i\xi}e^{i\zeta}$ (products and multiplication of smooth $\Phi$-values) and $-i\operatorname{Log}$; it is therefore smooth. Likewise inversion $g\mapsto\bar g$ becomes $\xi\mapsto\chi_{\bar g_0}(\overline{g_0e^{i\xi}})=-i\operatorname{Log}(e^{-i\xi})=-\xi$ near $g_0$, which is (the restriction of) the bounded linear map $\xi\mapsto-\xi$, manifestly smooth. Hence $\mu$ and inversion are smooth, and $\mathcal{G}$ is a Banach Lie group.
>
> **The model and the Lie algebra.** The model space is the real Banach space $H_3(M;\mathbb{R})$, so $\mathcal{G}$ has "dimension" $H_3(M;\mathbb{R})$ in the Banach sense; its tangent space at the identity — the Lie algebra — is $T_1\mathcal{G}=D\eta_1(0)\,H_3(M;\mathbb{R})=iH_3(M;\mathbb{R})$, identified with $H_3(M;\mathbb{R})$ via $\xi\mapsto i\xi$, and the bracket is trivial because $\mathcal{G}$ is abelian (Step 5). This is exactly the modelling asserted in the statement.

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a compact $4$-manifold and $k=3$ (so $2k=6>4=n$ and $k-\tfrac n2=1>0$). Then $\Phi(\xi)=e^{i\xi}$ is a smooth (in particular $C^1$) map $H_3(M;\mathbb{R})\to H_3(M;\mathbb{C})$ with $D\Phi(\xi)v=ie^{i\xi}v$, and $\mathcal{G}=H_3(M;S^1)$ is a Banach Lie group modelled on $H_3(M;\mathbb{R})$.
>
> **Analytic inputs.** By [[Thm - Sobolev Multiplication Theorem|the Sobolev multiplication theorem]], part (a), $2k>n$ makes $H_3(M;\mathbb{C})$ a Banach algebra: $\lVert uv\rVert_3\le C\lVert u\rVert_3\lVert v\rVert_3$ for a fixed $C\ge1$; by induction $\lVert u^j\rVert_3\le C^{j-1}\lVert u\rVert_3^{\,j}$ for $j\ge1$. By [[Thm - Sobolev Embedding Theorem|the Sobolev embedding theorem]], part (ii) with $r=0$, $H_3\hookrightarrow C^0$ continuously: $\lVert u\rVert_{C^0}\le C_{\mathrm{emb}}\lVert u\rVert_3$, and $H_3$-convergence gives uniform convergence.
>
> **Well-definedness.** For $\xi\in H_3(M;\mathbb{R})$, $\sum_{j\ge0}\frac{(i\xi)^j}{j!}$ converges absolutely in $H_3$ since $\sum_j\frac{\lVert(i\xi)^j\rVert_3}{j!}\le\lVert1\rVert_3+\frac1C(e^{C\lVert\xi\rVert_3}-1)<\infty$; by the embedding its sum is the continuous function $x\mapsto e^{i\xi(x)}$, of modulus $1$. So $\Phi(\xi)\in H_3(M;S^1)$.
>
> **Differentiability.** $L_\xi v:=ie^{i\xi}v$ is bounded linear ($\lVert L_\xi v\rVert_3\le C\lVert e^{i\xi}\rVert_3\lVert v\rVert_3$). Using $e^{i(\xi+v)}=e^{i\xi}e^{iv}$ (pointwise, hence in the algebra), the remainder is $e^{i\xi}(e^{iv}-1-iv)$, and
> $$\lVert e^{iv}-1-iv\rVert_3\le\sum_{j\ge2}\frac{C^{j-1}\lVert v\rVert_3^{\,j}}{j!}=\tfrac1C(e^{C\lVert v\rVert_3}-1-C\lVert v\rVert_3)\le\tfrac{C}{2}e^{C\lVert v\rVert_3}\lVert v\rVert_3^{\,2},$$
> the last step by $e^t-1-t\le\tfrac{t^2}{2}e^t$. Hence $\lVert\Phi(\xi+v)-\Phi(\xi)-L_\xi v\rVert_3\le\tfrac{C^2}{2}\lVert e^{i\xi}\rVert_3e^{C\lVert v\rVert_3}\lVert v\rVert_3^{\,2}=o(\lVert v\rVert_3)$, so $D\Phi(\xi)=L_\xi$.
>
> **$C^1$ and $C^\infty$.** $\Phi$ is continuous ($e^{i\xi_1}-e^{i\xi_2}=e^{i\xi_2}(e^{i(\xi_1-\xi_2)}-1)$ and $\lVert e^{i(\xi_1-\xi_2)}-1\rVert_3\le\tfrac1C(e^{C\lVert\xi_1-\xi_2\rVert_3}-1)\to0$), and $\lVert D\Phi(\xi_1)-D\Phi(\xi_2)\rVert\le C\lVert\Phi(\xi_1)-\Phi(\xi_2)\rVert_3\to0$, so $\Phi\in C^1$. Writing $D\Phi=i\,\mathsf{M}\circ\Phi$ with $\mathsf{M}(w)v=wv$ bounded linear, and using that post-composition with a bounded linear map preserves $C^p$, we get $\Phi\in C^p\Rightarrow\Phi\in C^{p+1}$, hence $\Phi\in C^\infty$.
>
> **Group.** $\mathcal{G}$ is closed under products (algebra bound; modulus $1$), contains $1$, and $g^{-1}=\bar g$ (conjugation bounded on $H_3$; $g\bar g=\lvert g\rvert^2=1$); it is abelian.
>
> **Charts.** With $r=\tfrac12\min(1/C,1/C_{\mathrm{emb}})$, set $U_{g_0}=\{g\in\mathcal{G}:\lVert\bar g_0 g-1\rVert_3<r\}$ and $\chi_{g_0}(g)=-i\operatorname{Log}(\bar g_0 g)$, using the principal-branch series about $1$; it converges in $H_3$ ($Cr<1$) and, by the embedding ($C_{\mathrm{emb}}r<1$), sums pointwise to the principal logarithm, which is $i\arg(\bar g_0 g)$, real after the factor $-i$. Its inverse is $\eta_{g_0}(\xi)=g_0e^{i\xi}$; the two are mutually inverse homeomorphisms between the open sets $U_{g_0}$ and $\Omega_{g_0}=\eta_{g_0}^{-1}(U_{g_0})$, and the $U_{g_0}$ cover $\mathcal{G}$. Transition maps $\xi\mapsto-i\operatorname{Log}(\bar g_1 g_0 e^{i\xi})$ are compositions of $\Phi$ (smooth), a bounded linear multiplication, and $-i\operatorname{Log}$ (smooth by the same power-series argument applied to $\operatorname{Log}$), hence smooth; multiplication and inversion are smooth in these charts. Therefore $\mathcal{G}$ is a smooth Banach Lie group modelled on $H_3(M;\mathbb{R})$, with abelian Lie algebra $iH_3(M;\mathbb{R})\cong H_3(M;\mathbb{R})$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: cutting the chart by the $C^0$-norm
> It is tempting to define the chart domain by $\lVert\bar g_0 g-1\rVert_{C^0}<1$ (or even by $\bar g_0 g$ taking values in a half-circle), reasoning that this is what pins down the branch of $\log$. But the logarithm's power series $\sum\frac1j(h-1)^j$ converges *in the algebra* only when $C\lVert h-1\rVert_3<1$, an $H_3$-condition; a $C^0$-small $h-1$ can have arbitrarily large $H_3$-norm, so the series need not converge in $H_3$ and $\operatorname{Log}(h)$ need not be an $H_3$-element at all. The domain must be cut by the *stronger* $H_3$-norm; the $C^0$-smallness (and hence the choice of branch) is then a free consequence of the embedding. This is the exact place where the strength of the algebra norm over the sup-norm is indispensable.

> [!note]- Independent sanity check: the one-point manifold analogue and the finite-dimensional model
> When $M$ is a point, $H_3(M;\mathbb{R})=\mathbb{R}$, $H_3(M;\mathbb{C})=\mathbb{C}$, the algebra bound holds with $C=1$, and the statement collapses to: $\xi\mapsto e^{i\xi}$ is a smooth map $\mathbb{R}\to\mathbb{C}$ with derivative $v\mapsto ie^{i\xi}v$, and $S^1$ is a $1$-dimensional Lie group with charts $\xi\mapsto e^{i\theta_0}e^{i\xi}$ and inverse chart the principal argument near $1$. This is precisely the standard atlas on the circle, and our chart domain $\lVert\bar g_0 g-1\rVert<r$ becomes an arc around $g_0$ — reassuringly, the same construction that gives $S^1$ its Lie-group structure, now performed uniformly over all of $M$ in the Banach algebra $H_3$.

---

# Key Takeaways

**When the underlying Sobolev space is a Banach algebra, composition with an analytic function is smooth for one reason only: powers are controlled and the derivative is the termwise derivative.** The entire proof of part (A) is the transport of a scalar power-series identity into the algebra. The organising inequality is $\lVert u^j\rVert_3\le C^{j-1}\lVert u\rVert_3^{\,j}$ — the algebra bound raised to a power — which turns any Banach-space series $\sum a_j u^j$ into a scalar series $\sum\lvert a_j\rvert C^{j-1}\lVert u\rVert_3^{\,j}$ whose convergence and remainders are ordinary calculus. The trigger to reach for this pattern is the conjunction *"a nonlinear map defined by an analytic function"* and *"a function space with $2k>n$"*: the moment those coincide, expect smoothness, and expect the derivative to be multiplication by the derivative of the scalar function. The transferable diagnostic is the remainder factorisation $f(\xi+v)-f(\xi)-f'(\xi)v = $ (algebra element)$\cdot$(second-order tail): if you can peel the fixed part off and recognise the remaining factor as a tail starting at $j=2$, the $O(\lVert v\rVert^2)$ estimate is automatic.

**The two Sobolev hypotheses do disjoint jobs, and knowing which is which is the key to reconstructing the proof.** The multiplication hypothesis $2k>n$ is *algebraic*: it is used every time two elements are multiplied, and it is what makes convergence, remainders, and the group operation even make sense. The embedding hypothesis $k-\tfrac n2>0$ is *pointwise*: it is used only to see values — that $\lvert e^{i\xi}\rvert=1$, that small functions are uniformly small, that a single branch of the logarithm applies, and that an $H_3$-limit is the actual continuous function it should be. In four dimensions both happen to hold at $k=3$ ($6>4$ and $1>0$), which is exactly why $H_3(M^4)$ is the natural home for the Seiberg–Witten gauge group. When you meet a new smoothness-on-Sobolev problem, separate these two roles first: ask which steps multiply (needing the algebra) and which steps look at points (needing the embedding). The recurrent error is to try to run the logarithm's convergence off the sup-norm — the illegal shortcut above — precisely because one has failed to keep the two roles apart.

**Building an infinite-dimensional Lie group out of a nonlinear map is a chart problem, and the chart is always "exponentiate off the identity, take logarithms to come back".** The construction of $\mathcal{G}=H_3(M;S^1)$ is the template for every gauge group in the notes: translate to the identity by the fixed group element $g_0$, use the exponential of the model space to sweep out a neighbourhood, and invert with a logarithm on a small enough domain. The single technical subtlety — the transferable one — is *the domain of the inverse chart is dictated by where the logarithm's series converges in the strong norm, not by where the branch is single-valued*. Once that is respected, smoothness of the transition maps and of the group operations is automatic, because they are all built from the same two smooth Nemytskii operators ($\exp$ and $\log$) and bounded linear multiplications. This is why the Sobolev gauge group $\mathcal{G}^{k}=H_k(M;S^1)$ is a Banach Lie group whenever $2k>n$: the model is the abelian Banach space $H_k(M;\mathbb{R})$, the exponential chart is smooth by the composition theorem, and the whole structure is the pointwise circle group promoted, uniformly over $M$, into function space. The companion drill [[Ex - W-3-2 is an Algebra in Dimension Four]] establishes the algebra property this construction rests on, and the general statement lives on [[Thm - Composition with Analytic Functions on the Sobolev Algebra]].
