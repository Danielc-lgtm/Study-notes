---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Sobolev Norms on the Torus via Fourier Coefficients"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
  - "Thm - Sobolev Embedding Theorem"
  - "Thm - Convergence of the Lattice Sum"
tags: [geometry, gauge-theory]
---

# Problem Statement

Fix an integer $k$ and an integer $n\geq 1$, and let $T^n=\mathbb{R}^n/2\pi\mathbb{Z}^n$ be the flat torus. Work with the complex Sobolev space $H_k(T^n)=H_k(T^n;\mathbb{C})$ of integer order $k$, with the norm
$$\lVert u\rVert_k^2=\sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^k\,|\hat u(\xi)|^2,\qquad \hat u(\xi)=(2\pi)^{-n}\int_{T^n}u(x)\,e^{-i\langle\xi,x\rangle}\,dx,$$
and the $L^2$ pairing
$$\langle u,v\rangle=(2\pi)^n\sum_{\xi\in\mathbb{Z}^n}\hat u(\xi)\,\overline{\hat v(\xi)},$$
which extends to a continuous map $H_k(T^n)\times H_{-k}(T^n)\to\mathbb{C}$ satisfying $|\langle u,v\rangle|\leq(2\pi)^n\lVert u\rVert_k\,\lVert v\rVert_{-k}$.

Prove the following two statements.

1. **(Duality.)** Every bounded linear functional $\Lambda\colon H_k(T^n)\to\mathbb{C}$ is of the form $\Lambda(u)=\langle u,v\rangle$ for a *unique* $v\in H_{-k}(T^n)$, and the operator norm of $\Lambda$ satisfies
$$\lVert\Lambda\rVert=(2\pi)^n\,\lVert v\rVert_{-k}.$$
Consequently the map $v\mapsto\langle\,\cdot\,,v\rangle$ is a bijective, antilinear, isometry-up-to-the-factor-$(2\pi)^n$ from $H_{-k}(T^n)$ onto the dual space $H_k(T^n)^{\ast}$.

2. **(The Dirac comb is evaluation at the origin.)** Suppose $2k>n$. Show that the *Dirac comb* $\delta:=\sum_{\xi\in\mathbb{Z}^n}e^{i\langle\xi,x\rangle}$ — the element of $H_{-k}(T^n)$ whose every Fourier coefficient equals $1$ — lies in $H_{-k}(T^n)$, and that the bounded linear functional it represents on $H_k(T^n)$ is
$$\langle u,\delta\rangle=(2\pi)^n\,u(0),$$
where $u(0)$ is the value at the origin of the continuous representative of $u$. Thus, under the duality of part 1 and up to the factor $(2\pi)^n$, the Dirac comb *is* the evaluation functional $u\mapsto u(0)$, and this functional is bounded on $H_k$ precisely in the range $2k>n$ where the Sobolev embedding provides a continuous representative.

**Recall:**

The Sobolev spaces on the torus, the identification with weighted sequence spaces, and the pairing bound come from the definition page.

![[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order#The Definition]]

The precise duality statement that this exercise reproves by hand, together with the norm on $H_k$ and the pairing, is part (iv) of the following theorem; the exercise establishes exactly that statement from first principles rather than quoting it.

![[Thm - Sobolev Norms on the Torus via Fourier Coefficients#Statement]]

For part 2 we need the endpoint of the embedding scale, which produces the continuous representative, and the convergence criterion for the lattice weight that decides when $\delta\in H_{-k}$.

![[Thm - Sobolev Embedding Theorem#Statement]]

![[Thm - Convergence of the Lattice Sum#Statement]]

Throughout, $e_\xi$ denotes the exponential $e_\xi(x)=e^{i\langle\xi,x\rangle}$ for $\xi\in\mathbb{Z}^n$; its Fourier coefficients are $\hat e_\xi(\eta)=\delta_{\xi\eta}$ (the Kronecker delta), so $\lVert e_\xi\rVert_k^2=(1+|\xi|^2)^k$. A *trigonometric polynomial* is a finite complex-linear combination $\sum_{\xi\in S}a_\xi e_\xi$ over a finite set $S\subset\mathbb{Z}^n$; these are smooth, hence lie in every $H_k(T^n)$.

---

# Convergent Strategy

**Problem class.** This is a *represent-the-dual* problem: it identifies the dual of one Hilbert space in a scale, $H_k$, with another member of the same scale, $H_{-k}$, through a fixed pairing. Such problems are the workhorse of elliptic theory, where the negative-order spaces are introduced precisely so that a differential operator and its formal adjoint become genuine bounded maps in duality. The structural fact behind every such identification is that the norm $\lVert\cdot\rVert_k$ is realised on the Fourier side as a *weighted* $\ell^2$ norm, and the dual of a weighted $\ell^2$ space is the oppositely weighted $\ell^2$ space. Recognising the whole problem as "weighted $\ell^2$ duality in disguise" is the first move.

**Assumption pattern.** The only analytic hypothesis is that $\Lambda$ is *bounded*, that is, $\lVert\Lambda\rVert=\sup\{|\Lambda(u)|:\lVert u\rVert_k\leq 1\}<\infty$. Boundedness is used in exactly one place, and it is used quantitatively: it bounds a growing family of finite partial sums uniformly, and the uniform bound is what forces the candidate representative into $H_{-k}$. There is no completeness argument and no appeal to the infinite-dimensional Riesz representation theorem — the finiteness of $\lVert\Lambda\rVert$ does all the work by itself. For part 2 the hypothesis $2k>n$ is the exact numerical threshold at which the lattice weight $(1+|\xi|^2)^{-k}$ becomes summable, which is simultaneously what puts $\delta$ into $H_{-k}$ and, through the embedding theorem, what makes point evaluation bounded.

**Theorem routing.** For part 1 no external theorem is needed: the representative is constructed explicitly from the values $\Lambda(e_\xi)$, its membership in $H_{-k}$ is proved by a finite-sum-then-supremum argument using only the Cauchy–Schwarz pairing bound stated on [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]], and equality of functionals is closed by density of trigonometric polynomials. For part 2 the route runs $2k>n$ $\Rightarrow$ (by [[Thm - Convergence of the Lattice Sum]]) the weight is summable $\Rightarrow$ $\delta\in H_{-k}$ and (by [[Thm - Sobolev Embedding Theorem]]) $H_k\hookrightarrow C^0$ with the Fourier series converging uniformly to the continuous representative; evaluating that series at $x=0$ then reads off $\langle u,\delta\rangle=(2\pi)^n u(0)$.

**Key decision point.** The decisive idea in part 1 is to *test $\Lambda$ against a cleverly weighted finite trigonometric polynomial*. If one guesses that the representative must have Fourier coefficients $\hat v(\xi)=(2\pi)^{-n}\overline{\Lambda(e_\xi)}$ — forced by plugging $u=e_\xi$ into $\Lambda(u)=\langle u,v\rangle$ — then the problem reduces to proving $\sum_\xi(1+|\xi|^2)^{-k}|\Lambda(e_\xi)|^2<\infty$. The single trick that yields this is to feed $\Lambda$ the polynomial $u_S=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\overline{\Lambda(e_\xi)}\,e_\xi$: for this exact choice of coefficients the value $\Lambda(u_S)$ and the squared norm $\lVert u_S\rVert_k^2$ turn out to be *the same nonnegative number* $\Sigma_S$, so boundedness gives $\Sigma_S\leq\lVert\Lambda\rVert\,\Sigma_S^{1/2}$, hence $\Sigma_S\leq\lVert\Lambda\rVert^2$ uniformly in $S$. Everything else is bookkeeping.

---

# Legal Operations Used

This solution deploys the following legal operations; the numbering will be reconciled with the topic page's Legal Operations once that page is written, so each is named descriptively here.

1. **Pass to Fourier coefficients and read the norm as a weighted $\ell^2$ norm.** The whole calculation lives on the sequence side, where $\lVert u\rVert_k^2=\sum(1+|\xi|^2)^k|\hat u(\xi)|^2$ and the pairing is $\langle u,v\rangle=(2\pi)^n\sum\hat u(\xi)\overline{\hat v(\xi)}$. This is the operation that turns an analytic duality question into an elementary sequence-space computation.

2. **Test a functional against basis vectors to recover its representative.** Evaluating $\Lambda$ on each exponential $e_\xi$ produces the numbers $\Lambda(e_\xi)$, and the requirement $\Lambda=\langle\,\cdot\,,v\rangle$ forces $\hat v(\xi)=(2\pi)^{-n}\overline{\Lambda(e_\xi)}$. This is the standard "evaluate on a basis to guess the kernel" operation.

3. **Bound an infinite sum by the supremum of its finite partial sums.** The membership $v\in H_{-k}$ is not proved directly; it is proved by showing every finite partial sum is bounded by $\lVert\Lambda\rVert^2$ and taking the supremum. This is the monotone-truncation operation that converts a boundedness hypothesis into an $\ell^2$ estimate.

4. **Close an identity of continuous functionals by checking it on a dense set.** Two bounded functionals that agree on all trigonometric polynomials agree everywhere, because those polynomials are dense in $H_k$. This is the density-and-continuity operation.

5. **Use the Cauchy–Schwarz pairing bound in both directions to pin the operator norm.** One inequality comes from the pairing bound $|\langle u,v\rangle|\leq(2\pi)^n\lVert u\rVert_k\lVert v\rVert_{-k}$ of [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]]; the reverse comes from the finite-sum estimate of operation 3. Their coincidence gives the exact norm identity.

---

# Hints

> [!note]- Hint 1
> Do the entire problem on the Fourier side. A bounded linear functional $\Lambda$ on $H_k$ is determined by the sequence of numbers $c_\xi:=\Lambda(e_\xi)$. If $\Lambda$ is going to equal $u\mapsto\langle u,v\rangle$, what must $\hat v(\xi)$ be? Plug $u=e_\xi$ into the pairing and solve.

> [!note]- Hint 2
> The one thing to prove is that the guessed $v$ actually lies in $H_{-k}$, i.e. that $\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2<\infty$. You are only allowed to use that $\Lambda$ is bounded. Try feeding $\Lambda$ a *finite* trigonometric polynomial whose coefficients you choose, and pick those coefficients so that $\Lambda$ of the polynomial and the squared $H_k$-norm of the polynomial come out to the same expression.

> [!note]- Hint 3
> With $u_S=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\overline{c_\xi}\,e_\xi$ over a finite set $S$, compute both $\Lambda(u_S)$ and $\lVert u_S\rVert_k^2$. You will find they equal the same number $\Sigma_S=\sum_{\xi\in S}(1+|\xi|^2)^{-k}|c_\xi|^2$. Boundedness gives $\Sigma_S=\Lambda(u_S)\leq\lVert\Lambda\rVert\,\lVert u_S\rVert_k=\lVert\Lambda\rVert\,\Sigma_S^{1/2}$. Cancel and let $S$ exhaust $\mathbb{Z}^n$.

> [!note]- Hint 4
> For uniqueness, subtract two representatives and evaluate the difference-pairing on $e_\xi$. For the norm identity, combine the finite-sum bound (which gives $(2\pi)^n\lVert v\rVert_{-k}\leq\lVert\Lambda\rVert$) with the Cauchy–Schwarz pairing bound (which gives $\lVert\Lambda\rVert\leq(2\pi)^n\lVert v\rVert_{-k}$).

> [!note]- Hint 5
> For part 2, note $\hat\delta(\xi)=1$ for all $\xi$, so $\lVert\delta\rVert_{-k}^2=\sum_\xi(1+|\xi|^2)^{-k}$; convergence is exactly $2k>n$ by [[Thm - Convergence of the Lattice Sum]]. Then $\langle u,\delta\rangle=(2\pi)^n\sum_\xi\hat u(\xi)$. When $2k>n$, why does $\sum_\xi\hat u(\xi)$ converge absolutely, and what continuous function is it the value of at $x=0$?

---

# Solution

The plan for part 1 is to construct the candidate $v$ from the numbers $c_\xi=\Lambda(e_\xi)$, prove $v\in H_{-k}$ by bounding every finite partial sum of $\sum(1+|\xi|^2)^{-k}|c_\xi|^2$ by $\lVert\Lambda\rVert^2$, verify $\Lambda=\langle\,\cdot\,,v\rangle$ by agreement on the dense set of trigonometric polynomials, and pin the norm by two matching Cauchy–Schwarz inequalities; uniqueness is a one-line coefficient comparison. The plan for part 2 is to identify $\delta$ as the element with all Fourier coefficients $1$, use the lattice-sum criterion to place it in $H_{-k}$, and use the embedding theorem to sum the Fourier series of $u$ at the origin.

**Step 1: Construct the candidate representative and record its intended Fourier coefficients.**

For each $\xi\in\mathbb{Z}^n$ set $c_\xi:=\Lambda(e_\xi)\in\mathbb{C}$, and define a formal Fourier series by prescribing $\hat v(\xi):=(2\pi)^{-n}\overline{c_\xi}$.

> [!note]- Derivation
> If a representative $v$ exists with $\Lambda(u)=\langle u,v\rangle=(2\pi)^n\sum_\eta\hat u(\eta)\overline{\hat v(\eta)}$ for all $u\in H_k$, then in particular for $u=e_\xi$, whose coefficients are $\hat e_\xi(\eta)=\delta_{\xi\eta}$, we obtain
> $$c_\xi=\Lambda(e_\xi)=(2\pi)^n\sum_\eta\delta_{\xi\eta}\,\overline{\hat v(\eta)}=(2\pi)^n\,\overline{\hat v(\xi)}\qquad\text{(pairing formula; }\hat e_\xi(\eta)=\delta_{\xi\eta}\text{).}$$
> Solving for $\hat v(\xi)$ forces $\hat v(\xi)=(2\pi)^{-n}\overline{c_\xi}$. We therefore *define* $v$ to be the sequence $(\hat v(\xi))_\xi$ with these coefficients, viewing it a priori only as an element of the space of all complex sequences on $\mathbb{Z}^n$; Step 2 shows it is genuinely in the weighted sequence space $H_{-k}$.

**Step 2: Prove $v\in H_{-k}$ by bounding all finite partial sums.**

Using only that $\Lambda$ is bounded with operator norm $\lVert\Lambda\rVert$, we show $\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2\leq\lVert\Lambda\rVert^2$, so $\lVert v\rVert_{-k}^2=(2\pi)^{-2n}\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2\leq(2\pi)^{-2n}\lVert\Lambda\rVert^2<\infty$.

> [!note]- Derivation
> Let $S\subset\mathbb{Z}^n$ be an arbitrary finite set, and define the trigonometric polynomial
> $$u_S:=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\,\overline{c_\xi}\;e_\xi,$$
> which is smooth and hence lies in $H_k(T^n)$. Its Fourier coefficients are $\hat u_S(\xi)=(1+|\xi|^2)^{-k}\overline{c_\xi}$ for $\xi\in S$ and $0$ otherwise. Write
> $$\Sigma_S:=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\,|c_\xi|^2\;\geq 0.$$
>
> **Compute $\Lambda(u_S)$.** By linearity of $\Lambda$ and the definition $c_\xi=\Lambda(e_\xi)$,
> $$\Lambda(u_S)=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\,\overline{c_\xi}\;\Lambda(e_\xi)=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\,\overline{c_\xi}\,c_\xi=\Sigma_S\qquad\text{(linearity of }\Lambda\text{; }\overline{c_\xi}c_\xi=|c_\xi|^2\text{).}$$
>
> **Compute $\lVert u_S\rVert_k^2$.** By the definition of the $H_k$-norm on the Fourier side,
> $$\lVert u_S\rVert_k^2=\sum_{\xi\in S}(1+|\xi|^2)^{k}\,|\hat u_S(\xi)|^2=\sum_{\xi\in S}(1+|\xi|^2)^{k}\,(1+|\xi|^2)^{-2k}\,|c_\xi|^2=\sum_{\xi\in S}(1+|\xi|^2)^{-k}|c_\xi|^2=\Sigma_S\qquad\text{(norm formula; }|\hat u_S(\xi)|^2=(1+|\xi|^2)^{-2k}|c_\xi|^2\text{).}$$
>
> **Combine via boundedness.** Since $\Lambda(u_S)=\Sigma_S$ is real and nonnegative, $\Sigma_S=|\Lambda(u_S)|$, and boundedness of $\Lambda$ gives
> $$\Sigma_S=|\Lambda(u_S)|\leq\lVert\Lambda\rVert\;\lVert u_S\rVert_k=\lVert\Lambda\rVert\;\Sigma_S^{1/2}\qquad\text{(definition of }\lVert\Lambda\rVert\text{; }\lVert u_S\rVert_k=\Sigma_S^{1/2}\text{).}$$
> If $\Sigma_S=0$ the bound $\Sigma_S\leq\lVert\Lambda\rVert^2$ is immediate; if $\Sigma_S>0$, dividing by $\Sigma_S^{1/2}>0$ gives $\Sigma_S^{1/2}\leq\lVert\Lambda\rVert$, hence $\Sigma_S\leq\lVert\Lambda\rVert^2$. Either way,
> $$\sum_{\xi\in S}(1+|\xi|^2)^{-k}|c_\xi|^2=\Sigma_S\leq\lVert\Lambda\rVert^2\qquad\text{for every finite }S\subset\mathbb{Z}^n.$$
>
> **Take the supremum.** The full sum $\sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^{-k}|c_\xi|^2$ is the supremum of its finite partial sums $\Sigma_S$ (all terms are nonnegative), so it is bounded by $\lVert\Lambda\rVert^2<\infty$. Therefore
> $$\lVert v\rVert_{-k}^2=\sum_\xi(1+|\xi|^2)^{-k}|\hat v(\xi)|^2=(2\pi)^{-2n}\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2\leq(2\pi)^{-2n}\lVert\Lambda\rVert^2,$$
> which shows $v\in H_{-k}(T^n)$ and, taking square roots, $(2\pi)^n\lVert v\rVert_{-k}\leq\lVert\Lambda\rVert$.

**Step 3: Prove $\Lambda(u)=\langle u,v\rangle$ for all $u\in H_k$.**

The two bounded linear functionals $\Lambda$ and $\langle\,\cdot\,,v\rangle$ agree on every exponential $e_\xi$, hence on every trigonometric polynomial, and trigonometric polynomials are dense in $H_k$; by continuity they agree everywhere.

> [!note]- Derivation
> **Agreement on exponentials.** Since $v\in H_{-k}$ by Step 2, the pairing $\langle e_\xi,v\rangle$ is defined, and
> $$\langle e_\xi,v\rangle=(2\pi)^n\sum_\eta\hat e_\xi(\eta)\,\overline{\hat v(\eta)}=(2\pi)^n\,\overline{\hat v(\xi)}=(2\pi)^n\,\overline{(2\pi)^{-n}\overline{c_\xi}}=c_\xi=\Lambda(e_\xi)\qquad\text{(pairing formula; }\hat e_\xi(\eta)=\delta_{\xi\eta}\text{; definition of }\hat v(\xi)\text{).}$$
> **Agreement on polynomials.** Both $\Lambda$ and $\langle\,\cdot\,,v\rangle$ are linear, so they agree on every finite linear combination of exponentials, i.e. on every trigonometric polynomial.
>
> **Density.** For $u\in H_k$, the truncations $T_R u:=\sum_{|\xi|\leq R}\hat u(\xi)e_\xi$ are trigonometric polynomials, and
> $$\lVert u-T_R u\rVert_k^2=\sum_{|\xi|>R}(1+|\xi|^2)^k|\hat u(\xi)|^2\longrightarrow 0\quad(R\to\infty)\qquad\text{(tail of the convergent series }\lVert u\rVert_k^2\text{),}$$
> so $T_R u\to u$ in $H_k$; the trigonometric polynomials are dense in $H_k(T^n)$.
>
> **Continuity closes the identity.** Both functionals are bounded, hence continuous. Fixing $u\in H_k$ and applying the agreement on the polynomials $T_R u$,
> $$\Lambda(u)=\lim_{R\to\infty}\Lambda(T_R u)=\lim_{R\to\infty}\langle T_R u,v\rangle=\langle u,v\rangle\qquad\text{(continuity of }\Lambda\text{; agreement on polynomials; continuity of }\langle\,\cdot\,,v\rangle\text{).}$$
> Since $u$ was arbitrary, $\Lambda=\langle\,\cdot\,,v\rangle$ on all of $H_k$.

**Step 4: Uniqueness of $v$, and the norm identity $\lVert\Lambda\rVert=(2\pi)^n\lVert v\rVert_{-k}$.**

If $v_1,v_2\in H_{-k}$ both represent $\Lambda$ then $v_1=v_2$; and the operator norm equals $(2\pi)^n\lVert v\rVert_{-k}$.

> [!note]- Derivation
> **Uniqueness.** Suppose $\langle u,v_1\rangle=\langle u,v_2\rangle$ for all $u\in H_k$. Then $\langle u,v_1-v_2\rangle=0$ for all $u$; taking $u=e_\xi$ gives $(2\pi)^n\overline{\hat v_1(\xi)-\hat v_2(\xi)}=0$, so $\hat v_1(\xi)=\hat v_2(\xi)$ for every $\xi\in\mathbb{Z}^n$. Two elements of $H_{-k}$ with the same Fourier coefficients are equal, so $v_1=v_2$.
>
> **Upper bound on $\lVert\Lambda\rVert$.** For every $u\in H_k$, the Cauchy–Schwarz pairing bound stated on [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|the definition page]] gives $|\Lambda(u)|=|\langle u,v\rangle|\leq(2\pi)^n\lVert u\rVert_k\lVert v\rVert_{-k}$, whence $\lVert\Lambda\rVert=\sup_{\lVert u\rVert_k\leq 1}|\Lambda(u)|\leq(2\pi)^n\lVert v\rVert_{-k}$.
>
> **Lower bound on $\lVert\Lambda\rVert$.** Step 2 established $(2\pi)^n\lVert v\rVert_{-k}\leq\lVert\Lambda\rVert$.
>
> **Combine.** The two inequalities give $\lVert\Lambda\rVert=(2\pi)^n\lVert v\rVert_{-k}$, as claimed.

This proves part 1: $v\mapsto\langle\,\cdot\,,v\rangle$ carries $H_{-k}$ *onto* $H_k^\ast$ (surjectivity is Steps 1–3, that every $\Lambda$ is represented), *injectively* (uniqueness, Step 4), *antilinearly* (the pairing is conjugate-linear in $v$, since $\langle u,\lambda v\rangle=\overline{\lambda}\langle u,v\rangle$), and with $\lVert\Lambda\rVert=(2\pi)^n\lVert v\rVert_{-k}$ (Step 4).

**Step 5: The Dirac comb lies in $H_{-k}$ when $2k>n$.**

The Dirac comb $\delta$ has $\hat\delta(\xi)=1$ for all $\xi$, so its $H_{-k}$-norm is the square root of a lattice sum that converges precisely when $2k>n$.

> [!note]- Derivation
> By definition $\delta=\sum_\xi e_\xi$ is the element with $\hat\delta(\xi)=1$ for every $\xi\in\mathbb{Z}^n$. Hence
> $$\lVert\delta\rVert_{-k}^2=\sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^{-k}\,|\hat\delta(\xi)|^2=\sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^{-k}\qquad\text{(norm formula; }|\hat\delta(\xi)|^2=1\text{).}$$
> Setting $t=k$ in [[Thm - Convergence of the Lattice Sum|the lattice-sum theorem]] — which asserts that $\sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^{-t}$ converges if and only if $2t>n$ — the sum converges exactly when $2k>n$. Under the standing hypothesis $2k>n$ we conclude $\lVert\delta\rVert_{-k}^2=\sum_\xi(1+|\xi|^2)^{-k}<\infty$, so $\delta\in H_{-k}(T^n)$.

**Step 6: The functional represented by $\delta$ is $(2\pi)^n$ times evaluation at the origin.**

For $2k>n$ and $u\in H_k$, the Fourier series of $u$ converges absolutely and uniformly to the continuous representative of $u$, and its value at $x=0$ is $\sum_\xi\hat u(\xi)$; therefore $\langle u,\delta\rangle=(2\pi)^n u(0)$.

> [!note]- Derivation
> **The pairing is the sum of the Fourier coefficients.** For $u\in H_k$ and $\delta\in H_{-k}$ (Step 5),
> $$\langle u,\delta\rangle=(2\pi)^n\sum_\xi\hat u(\xi)\,\overline{\hat\delta(\xi)}=(2\pi)^n\sum_\xi\hat u(\xi)\qquad\text{(pairing formula; }\hat\delta(\xi)=1\text{).}$$
> The series $\sum_\xi\hat u(\xi)$ converges absolutely: by the Cauchy–Schwarz inequality on $\mathbb{Z}^n$, splitting the weight as $1=(1+|\xi|^2)^{k/2}(1+|\xi|^2)^{-k/2}$,
> $$\sum_\xi|\hat u(\xi)|=\sum_\xi(1+|\xi|^2)^{k/2}|\hat u(\xi)|\cdot(1+|\xi|^2)^{-k/2}\leq\Big(\sum_\xi(1+|\xi|^2)^{k}|\hat u(\xi)|^2\Big)^{1/2}\Big(\sum_\xi(1+|\xi|^2)^{-k}\Big)^{1/2}=\lVert u\rVert_k\,\lVert\delta\rVert_{-k}<\infty$$
> (Cauchy–Schwarz for $\ell^2$-sequences; the first factor is $\lVert u\rVert_k$, the second is finite by Step 5 since $2k>n$).
>
> **The continuous representative and its value at $0$.** By [[Thm - Sobolev Embedding Theorem|the Sobolev embedding theorem]], for integers $k,r\geq 0$ with $k-\tfrac n2>r$ the space $H_k(T^n)$ embeds continuously in $C^r(T^n)$; taking $r=0$ (the hypothesis $2k>n$ is exactly $k-\tfrac n2>0$) every $u\in H_k$ has a continuous representative $\tilde u\in C^0(T^n)$ with $\lVert\tilde u\rVert_{C^0}\leq C\lVert u\rVert_k$. This representative is the uniform limit of the Fourier partial sums: since $\sum_\xi|\hat u(\xi)|<\infty$, the series $\sum_\xi\hat u(\xi)e_\xi$ converges uniformly (Weierstrass $M$-test with $M_\xi=|\hat u(\xi)|$) to a continuous function; that continuous function has the same Fourier coefficients as $u$ (termwise integration of a uniformly convergent series), hence agrees with $\tilde u$. Evaluating the uniformly convergent series at $x=0$, where $e_\xi(0)=1$,
> $$\tilde u(0)=\sum_\xi\hat u(\xi)\,e_\xi(0)=\sum_\xi\hat u(\xi)\qquad\text{(uniform convergence permits termwise evaluation; }e_\xi(0)=1\text{).}$$
>
> **Conclude.** Combining the two displays, $\langle u,\delta\rangle=(2\pi)^n\sum_\xi\hat u(\xi)=(2\pi)^n\,\tilde u(0)$. Writing $u(0)$ for the value of the continuous representative, $\langle u,\delta\rangle=(2\pi)^n u(0)$.

> [!note]- Complete formal solution
> **Part 1.** Let $\Lambda\in H_k(T^n)^\ast$ with operator norm $\lVert\Lambda\rVert$, and set $c_\xi=\Lambda(e_\xi)$ for $\xi\in\mathbb{Z}^n$, where $e_\xi(x)=e^{i\langle\xi,x\rangle}$.
>
> Define $v$ by $\hat v(\xi)=(2\pi)^{-n}\overline{c_\xi}$. For any finite $S\subset\mathbb{Z}^n$ put $u_S=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\overline{c_\xi}\,e_\xi\in H_k$ and $\Sigma_S=\sum_{\xi\in S}(1+|\xi|^2)^{-k}|c_\xi|^2$. Then $\Lambda(u_S)=\sum_{\xi\in S}(1+|\xi|^2)^{-k}\overline{c_\xi}c_\xi=\Sigma_S$ by linearity, and $\lVert u_S\rVert_k^2=\sum_{\xi\in S}(1+|\xi|^2)^k(1+|\xi|^2)^{-2k}|c_\xi|^2=\Sigma_S$ by the norm formula. Boundedness gives $\Sigma_S=|\Lambda(u_S)|\leq\lVert\Lambda\rVert\,\Sigma_S^{1/2}$, so $\Sigma_S\leq\lVert\Lambda\rVert^2$ for every finite $S$. Taking the supremum over $S$ (nonnegative terms), $\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2\leq\lVert\Lambda\rVert^2$, hence $\lVert v\rVert_{-k}^2=(2\pi)^{-2n}\sum_\xi(1+|\xi|^2)^{-k}|c_\xi|^2\leq(2\pi)^{-2n}\lVert\Lambda\rVert^2$; so $v\in H_{-k}$ and $(2\pi)^n\lVert v\rVert_{-k}\leq\lVert\Lambda\rVert$.
>
> Now $\langle e_\xi,v\rangle=(2\pi)^n\overline{\hat v(\xi)}=c_\xi=\Lambda(e_\xi)$ for all $\xi$, so $\Lambda$ and $\langle\,\cdot\,,v\rangle$ agree on all trigonometric polynomials by linearity. For $u\in H_k$ the truncations $T_R u=\sum_{|\xi|\leq R}\hat u(\xi)e_\xi$ satisfy $\lVert u-T_R u\rVert_k^2=\sum_{|\xi|>R}(1+|\xi|^2)^k|\hat u(\xi)|^2\to 0$, so $T_R u\to u$ in $H_k$; by continuity of both functionals, $\Lambda(u)=\lim_R\Lambda(T_R u)=\lim_R\langle T_R u,v\rangle=\langle u,v\rangle$. Thus $\Lambda=\langle\,\cdot\,,v\rangle$.
>
> If $\langle\,\cdot\,,v_1\rangle=\langle\,\cdot\,,v_2\rangle$, evaluating on $e_\xi$ gives $\hat v_1(\xi)=\hat v_2(\xi)$ for all $\xi$, so $v_1=v_2$: $v$ is unique. Finally the pairing bound $|\langle u,v\rangle|\leq(2\pi)^n\lVert u\rVert_k\lVert v\rVert_{-k}$ gives $\lVert\Lambda\rVert\leq(2\pi)^n\lVert v\rVert_{-k}$, and combined with $(2\pi)^n\lVert v\rVert_{-k}\leq\lVert\Lambda\rVert$ yields $\lVert\Lambda\rVert=(2\pi)^n\lVert v\rVert_{-k}$. Since $\langle u,\lambda v\rangle=\overline\lambda\langle u,v\rangle$, the representation map $v\mapsto\langle\,\cdot\,,v\rangle$ is a bijective antilinear map $H_{-k}\to H_k^\ast$ preserving the norm up to $(2\pi)^n$.
>
> **Part 2.** The Dirac comb has $\hat\delta(\xi)=1$ for all $\xi$, so $\lVert\delta\rVert_{-k}^2=\sum_\xi(1+|\xi|^2)^{-k}$, which converges if and only if $2k>n$ by [[Thm - Convergence of the Lattice Sum]]; under $2k>n$, $\delta\in H_{-k}$. For $u\in H_k$, $\langle u,\delta\rangle=(2\pi)^n\sum_\xi\hat u(\xi)$. By Cauchy–Schwarz, $\sum_\xi|\hat u(\xi)|\leq\lVert u\rVert_k(\sum_\xi(1+|\xi|^2)^{-k})^{1/2}<\infty$, so the Fourier series converges absolutely and uniformly (Weierstrass $M$-test) to a continuous function equal, by [[Thm - Sobolev Embedding Theorem]] (with $r=0$, since $2k>n$ means $k-\tfrac n2>0$), to the continuous representative $\tilde u$ of $u$; evaluating at $x=0$ (where $e_\xi(0)=1$) gives $\tilde u(0)=\sum_\xi\hat u(\xi)$. Hence $\langle u,\delta\rangle=(2\pi)^n\tilde u(0)=(2\pi)^n u(0)$: the functional represented by $\delta$ is $(2\pi)^n$ times evaluation at the origin. This functional is bounded on $H_k$ exactly when $2k>n$, the same threshold at which the embedding $H_k\hookrightarrow C^0$ makes point evaluation meaningful. $\blacksquare$

> [!warning] Illegal but tempting shortcut: quoting the infinite-dimensional Riesz representation theorem
> It is tempting to say "$H_k$ is a Hilbert space, so by the Riesz representation theorem every bounded functional is an inner product with a fixed element, and then convert that element to $H_{-k}$." This is true but is *not* a legal move here for two reasons. First, the vault proves the Riesz representation theorem only in the finite-dimensional setting ([[Thm - Riesz Representation Theorem (Finite-Dimensional)]]); the infinite-dimensional statement is not available as a proved page, so citing it would violate the rule that every invoked result be wikilinked to a complete proof. Second, the point of the exercise is precisely to prove the negative-order representation *directly* from boundedness, which is what makes the argument self-contained and reusable in the elliptic theory to come. The finite-partial-sum estimate of Step 2 is the honest replacement for the completeness/projection argument that the abstract theorem would hide.

---

# Key Takeaways

**A Sobolev norm is a weighted $\ell^2$ norm, and duality in such a scale is realised by flipping the sign of the weight exponent.** The single most transferable fact in this exercise is that once one passes to Fourier coefficients, $\lVert u\rVert_k^2=\sum(1+|\xi|^2)^k|\hat u(\xi)|^2$ is nothing more than a weighted $\ell^2$ norm with weight $(1+|\xi|^2)^k$, and the pairing $\langle u,v\rangle=(2\pi)^n\sum\hat u(\xi)\overline{\hat v(\xi)}$ couples the weight $k$ to the weight $-k$ so that Cauchy–Schwarz produces a finite number. The dual of a weighted $\ell^2$ space is the oppositely weighted $\ell^2$ space, and that is the whole content of $H_k^\ast\cong H_{-k}$. The trigger for reaching for this picture is any statement that pairs a positive-order and a negative-order Sobolev space, or that asks whether a functional defined by a series is bounded; the reusable diagnostic is to write the functional's action as $\sum\hat u(\xi)\overline{w(\xi)}$ and ask whether $\sum(1+|\xi|^2)^{-k}|w(\xi)|^2<\infty$. This is exactly why negative-order spaces are introduced in elliptic theory: they are the receptacles that make the formal adjoint of a differential operator a bounded map, and this exercise is the prototype of the pairing that every such adjoint uses.

**Boundedness of a functional becomes an $\ell^2$ estimate through a self-testing polynomial.** The heart of the argument is the choice of the finite test function $u_S$ whose coefficients are tuned so that $\Lambda(u_S)$ and $\lVert u_S\rVert_k^2$ collapse to the *same* nonnegative number $\Sigma_S$; the operator-norm inequality then reads $\Sigma_S\leq\lVert\Lambda\rVert\,\Sigma_S^{1/2}$, and the square root cancels to give a uniform bound $\Sigma_S\leq\lVert\Lambda\rVert^2$ that survives the passage to the supremum. This "test against the object you are trying to control, weighted so that the two sides match" manoeuvre is a recurring device: it is the discrete cousin of the way one proves $L^p$–$L^{p'}$ duality by testing against $|f|^{p-1}\operatorname{sgn} f$, and it recurs whenever a boundedness hypothesis must be turned into a norm bound on a candidate representative. The trigger is a functional whose values on basis elements are known but whose representative's membership in a space is in doubt; the pattern is to feed the functional a finite combination engineered so that the input norm equals the output value. It replaces, honestly and constructively, any appeal to abstract completeness.

**A distribution is bounded on a Sobolev space exactly when the embedding provides enough continuity, and the Dirac comb is the sharpest example.** The second part exhibits the general principle in its cleanest instance: point evaluation $u\mapsto u(0)$ is a bounded functional on $H_k(T^n)$ if and only if $2k>n$, which is precisely the Sobolev threshold $k>n/2$ at which $H_k$ embeds into $C^0$ and elements acquire genuine pointwise values. The Dirac comb is the negative-order element that *represents* this evaluation, and its membership $\delta\in H_{-k}\iff 2k>n$ mirrors the embedding threshold exactly, because the same lattice sum $\sum(1+|\xi|^2)^{-k}$ controls both — it is $\lVert\delta\rVert_{-k}^2$ on one side and the Cauchy–Schwarz factor that bounds $\sum|\hat u(\xi)|$ on the other. The reusable lesson is that the order of a distribution (here, the comb has order $-k$ for any $k>n/2$) measures how much smoothness a test function must have before the distribution can be applied to it pointwise; the trigger, in the elliptic theory ahead, is any Green's-function or fundamental-solution computation where one must decide in which negative Sobolev space a delta-type source lives, and the answer is always read off from the same lattice-sum dimension count. A companion drill is [[Ex - The Lattice Sum Converges iff 2t Exceeds n]], which isolates the convergence criterion used here, and [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]], which shows what fails at the borderline $2k=n$.
