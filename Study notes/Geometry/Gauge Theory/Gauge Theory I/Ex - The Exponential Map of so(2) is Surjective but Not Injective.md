---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - The Exponential Map of a Matrix Group is the Matrix Exponential"
  - "Thm - SO(2) is Isomorphic to U(1)"
  - "Def - Classical Matrix Groups"
tags: [geometry, gauge-theory]
---

# Problem Statement

Consider the rotation group $SO(2)$ and its Lie algebra
$$\mathfrak{so}(2)=\left\{A_\theta:=\begin{pmatrix}0&-\theta\\\theta&0\end{pmatrix}:\theta\in\mathbb{R}\right\},$$
the space of real antisymmetric $2\times 2$ matrices. Prove the following, which is Example 1.4.12 of Bär's *Gauge Theory*:

1. For $A=A_\theta\in\mathfrak{so}(2)$ the matrix powers are
$$A^{2k}=(-1)^k\theta^{2k}\,\mathbf{1}_2,\qquad A^{2k+1}=(-1)^k\theta^{2k+1}\begin{pmatrix}0&-1\\1&0\end{pmatrix}\qquad(k\ge 0),$$
where $\mathbf{1}_2$ is the $2\times 2$ identity matrix.
2. Summing the exponential series gives
$$\exp(A_\theta)=e^{A_\theta}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},$$
the rotation of the plane by angle $\theta$.
3. Consequently $\exp\colon\mathfrak{so}(2)\to SO(2)$ is **surjective** (every rotation is an exponential) but **not injective**; the fibre over the identity is
$$\{A_\theta:\exp(A_\theta)=\mathbf{1}_2\}=\{A_{2\pi k}:k\in\mathbb{Z}\},$$
which corresponds, under the identification $\theta\leftrightarrow A_\theta$ of $\mathbb{R}$ with $\mathfrak{so}(2)$, exactly to the subgroup $2\pi\mathbb{Z}\subset\mathbb{R}$.

**Recall.**

The objects in play are the Lie algebra exponential of a matrix group, the antisymmetric matrices $\mathfrak{so}(2)$, and the rotation-matrix description of $SO(2)$.

![[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential#Statement]]

The content used here is: for a closed subgroup $G\subseteq GL(n;\mathbb{K})$ with Lie algebra $\mathfrak{g}\subseteq\operatorname{Mat}(n\times n;\mathbb{K})$, the Lie-group exponential of $X\in\mathfrak{g}$ coincides with the **matrix exponential**
$$e^{X}=\sum_{n=0}^{\infty}\frac{X^{n}}{n!},$$
a series that converges absolutely in any submultiplicative matrix norm (so its terms may be rearranged freely), and $e^{X}\in G$. Since $SO(2)$ is a closed subgroup of $GL(2;\mathbb{R})$ (a [[Def - Classical Matrix Groups|classical matrix group]]) with Lie algebra $\mathfrak{so}(2)$, this identifies $\exp\colon\mathfrak{so}(2)\to SO(2)$ with $A\mapsto e^{A}$.

![[Thm - SO(2) is Isomorphic to U(1)#Statement]]

The content used here is the explicit description of the rotation group as
$$SO(2)=\left\{R_\varphi:=\begin{pmatrix}\cos\varphi&-\sin\varphi\\\sin\varphi&\cos\varphi\end{pmatrix}:\varphi\in\mathbb{R}\right\},$$
with $R_\varphi=R_{\varphi'}$ if and only if $\varphi-\varphi'\in 2\pi\mathbb{Z}$ (the angle is defined modulo $2\pi$). Write $J:=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, so that $A_\theta=\theta J$ and $R_\varphi=\cos\varphi\,\mathbf{1}_2+\sin\varphi\,J$.

---

# Convergent Strategy

**Problem class.** This is a *direct computation with a structural conclusion*: evaluate a matrix exponential in closed form, then read off the qualitative behaviour (surjectivity, failure of injectivity) of the map it defines. The computational half is a drill; the conceptual half is the recognition that a *non-injective* exponential is the generic situation for a compact group, and that its failure of injectivity is measured by a lattice — here $2\pi\mathbb{Z}$ — that is the "integral lattice" of the torus $SO(2)\cong S^1$.

**Assumption pattern.** The only special feature of $\mathfrak{so}(2)$ exploited is that its generator $J$ squares to $-\mathbf{1}_2$. That single relation, $J^2=-\mathbf{1}_2$, collapses all powers of $A_\theta=\theta J$ into two families (even powers proportional to $\mathbf{1}_2$, odd powers proportional to $J$) and thereby splits the exponential series into the Taylor series of $\cos$ and $\sin$. Whenever a matrix satisfies a low-degree polynomial relation like $J^2=-\mathbf{1}_2$ (or $N^2=0$ for a nilpotent, or $P^2=P$ for an idempotent), its exponential has a closed form obtained by folding the series along that relation.

**Theorem routing.** The route is: identify $\exp$ on $\mathfrak{so}(2)$ with the matrix exponential via [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-group exponential theorem]]; compute $A_\theta^n$ using $J^2=-\mathbf{1}_2$; split the absolutely convergent series into even and odd parts and recognise $\cos\theta$ and $\sin\theta$; identify the result with the rotation $R_\theta$ using [[Thm - SO(2) is Isomorphic to U(1)|the rotation-matrix description of $SO(2)$]]; from $\exp(A_\theta)=R_\theta$ read off surjectivity (every $R_\varphi$ is $\exp(A_\varphi)$) and non-injectivity (the fibre over $\mathbf{1}_2=R_0$ is $\theta\in 2\pi\mathbb{Z}$).

**Key decision point.** The one point requiring care is the *rearrangement* of the exponential series into its even-indexed and odd-indexed subseries. This regrouping is legitimate only because the matrix exponential converges *absolutely* (in a submultiplicative norm), which is part of the cited theorem; absolute convergence licenses reordering and regrouping the terms without changing the sum. Skipping this justification is the usual gap in a first pass; stating it is what makes the computation a proof rather than a formal manipulation.

---

# Legal Operations Used

The solution deploys the following operations; when the chapter's topic page is assembled these are the Legal Operations it will list for §1.4, and the numbering will be reconciled to it.

1. **Replace the Lie-group exponential by the matrix exponential on a matrix group.** Because $SO(2)$ is a closed subgroup of $GL(2;\mathbb{R})$, apply the matrix-group exponential theorem to compute $\exp$ as the convergent power series $\sum A^n/n!$.

2. **Fold a power series along a polynomial relation of the generator.** Use $J^2=-\mathbf{1}_2$ to reduce every power $A_\theta^n=\theta^n J^n$ to one of two matrices, sorting the series into even and odd index families.

3. **Split an absolutely convergent series into subseries and re-sum.** Since the matrix exponential converges absolutely, regroup the even- and odd-index terms and recognise the scalar Taylor series of $\cos\theta$ and $\sin\theta$.

4. **Match a computed matrix against a normal form.** Identify $\cos\theta\,\mathbf{1}_2+\sin\theta\,J$ with the rotation $R_\theta$ from the standard description of $SO(2)$.

5. **Read surjectivity and non-injectivity off an explicit formula.** From $\exp(A_\theta)=R_\theta$ and the parametrisation of $SO(2)$ by angle modulo $2\pi$, extract that $\exp$ is onto and that its fibres are cosets of $2\pi\mathbb{Z}$.

---

# Hints

> [!note]- Hint 1
> Write $A_\theta=\theta J$ with $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. Compute $J^2$. You should find $J^2=-\mathbf{1}_2$. Now every power $J^n$ is $\pm\mathbf{1}_2$ or $\pm J$ depending only on the parity of $n$.

> [!note]- Hint 2
> Separate the exponential series $e^{A_\theta}=\sum_{n\ge0}\frac{\theta^n J^n}{n!}$ into even $n=2k$ and odd $n=2k+1$. The even terms are scalar multiples of $\mathbf{1}_2$; the odd terms are scalar multiples of $J$. What scalar series do the two families reproduce?

> [!note]- Hint 3
> The even family is $\sum_k\frac{(-1)^k\theta^{2k}}{(2k)!}=\cos\theta$ and the odd family is $\sum_k\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}=\sin\theta$. Hence $e^{A_\theta}=\cos\theta\,\mathbf{1}_2+\sin\theta\,J$. Write this out as a $2\times2$ matrix and compare it to a rotation.

> [!note]- Hint 4
> You now have $\exp(A_\theta)=R_\theta$, the rotation by $\theta$. Since every element of $SO(2)$ is some $R_\varphi$, is $\exp$ onto? And when is $R_\theta=\mathbf{1}_2$? Solve $\cos\theta=1$, $\sin\theta=0$. The solutions are $\theta\in 2\pi\mathbb{Z}$, so distinct $\theta$'s differing by a multiple of $2\pi$ give the same rotation — $\exp$ is not injective.

---

# Solution

The plan is to reduce the powers of $A_\theta=\theta J$ using the single relation $J^2=-\mathbf{1}_2$, split the absolutely convergent exponential series into its even and odd halves to recover $\cos\theta$ and $\sin\theta$, and identify the result as the rotation $R_\theta$. Surjectivity and the failure of injectivity then follow immediately from the closed form together with the parametrisation of $SO(2)$ by angle modulo $2\pi$.

**Step 1: The powers of $A_\theta$ (the relation $J^2=-\mathbf{1}_2$).**

With $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $A_\theta=\theta J$, we have $J^2=-\mathbf{1}_2$, and hence $A_\theta^{2k}=(-1)^k\theta^{2k}\mathbf{1}_2$ and $A_\theta^{2k+1}=(-1)^k\theta^{2k+1}J$.

> [!note]- Derivation
> Compute the square of $J$ directly:
> $$J^2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}0\cdot0+(-1)\cdot1 & 0\cdot(-1)+(-1)\cdot0\\ 1\cdot0+0\cdot1 & 1\cdot(-1)+0\cdot0\end{pmatrix}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-\mathbf{1}_2.$$
> Because $J^2=-\mathbf{1}_2$ and $\mathbf{1}_2$ is central, the even and odd powers of $J$ follow by induction:
> $$J^{2k}=(J^2)^k=(-\mathbf{1}_2)^k=(-1)^k\mathbf{1}_2\qquad\text{(by }J^2=-\mathbf{1}_2\text{),}$$
> $$J^{2k+1}=J^{2k}\cdot J=(-1)^k\mathbf{1}_2\cdot J=(-1)^k J\qquad\text{(by the previous line).}$$
> Since $A_\theta=\theta J$ and $\theta\in\mathbb{R}$ is a scalar commuting with every matrix, $A_\theta^{n}=\theta^{n}J^{n}$. Substituting $n=2k$ and $n=2k+1$:
> $$A_\theta^{2k}=\theta^{2k}J^{2k}=(-1)^k\theta^{2k}\mathbf{1}_2,\qquad A_\theta^{2k+1}=\theta^{2k+1}J^{2k+1}=(-1)^k\theta^{2k+1}J.$$
> Explicitly, $A_\theta^2=\begin{pmatrix}-\theta^2&0\\0&-\theta^2\end{pmatrix}=-\theta^2\mathbf{1}_2$, matching the case $k=1$ of the even formula. This is exactly the claim in part 1 of the problem.

**Step 2: Summing the exponential series to $\cos\theta\,\mathbf{1}_2+\sin\theta\,J$.**

Splitting the absolutely convergent matrix-exponential series into even and odd index parts yields $\exp(A_\theta)=\cos\theta\,\mathbf{1}_2+\sin\theta\,J$.

> [!note]- Derivation
> Because $SO(2)$ is a closed subgroup of $GL(2;\mathbb{R})$ with Lie algebra $\mathfrak{so}(2)$, [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-group exponential theorem]] — restated: *on a closed matrix subgroup the Lie-group exponential equals the matrix exponential $e^{X}=\sum_{n\ge0}X^{n}/n!$, and this series converges absolutely* — gives
> $$\exp(A_\theta)=e^{A_\theta}=\sum_{n=0}^{\infty}\frac{A_\theta^{\,n}}{n!}.$$
> The series converges **absolutely** (in, say, the operator norm, since $\sum_n\lVert A_\theta\rVert^{n}/n!=e^{\lVert A_\theta\rVert}<\infty$), so we may reorder and regroup its terms without changing the sum. Separate the terms of even and odd index:
> $$e^{A_\theta}=\sum_{k=0}^{\infty}\frac{A_\theta^{\,2k}}{(2k)!}+\sum_{k=0}^{\infty}\frac{A_\theta^{\,2k+1}}{(2k+1)!}\qquad\text{(regrouping, licensed by absolute convergence).}$$
> Insert the power formulas from **Step 1**:
> $$e^{A_\theta}=\left(\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k}}{(2k)!}\right)\mathbf{1}_2+\left(\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}\right)J\qquad\text{(by Step 1, factoring the constant matrices }\mathbf{1}_2,J\text{).}$$
> The two scalar series are the classical Taylor expansions
> $$\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k}}{(2k)!}=\cos\theta,\qquad \sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}=\sin\theta\qquad\text{(Taylor series of }\cos\text{ and }\sin\text{, convergent for all }\theta\in\mathbb{R}\text{),}$$
> both absolutely convergent, so the regrouping above is justified term by term. Therefore
> $$\exp(A_\theta)=\cos\theta\,\mathbf{1}_2+\sin\theta\,J.$$

**Step 3: Identifying the exponential as the rotation $R_\theta$.**

Writing the matrix $\cos\theta\,\mathbf{1}_2+\sin\theta\,J$ in coordinates identifies $\exp(A_\theta)$ with the rotation of the plane by angle $\theta$.

> [!note]- Derivation
> Substitute $\mathbf{1}_2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ into the result of Step 2:
> $$\exp(A_\theta)=\cos\theta\begin{pmatrix}1&0\\0&1\end{pmatrix}+\sin\theta\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}=R_\theta.$$
> By [[Thm - SO(2) is Isomorphic to U(1)|the rotation-matrix description of $SO(2)$]] — restated: *$SO(2)=\{R_\varphi:\varphi\in\mathbb{R}\}$ where $R_\varphi=\begin{pmatrix}\cos\varphi&-\sin\varphi\\\sin\varphi&\cos\varphi\end{pmatrix}$, and $R_\varphi=R_{\varphi'}$ if and only if $\varphi\equiv\varphi'\pmod{2\pi}$* — the matrix $R_\theta$ is exactly the element of $SO(2)$ of angle $\theta$. This proves part 2 of the problem. As a consistency check the exponential lands in $SO(2)$, as the general theorem promises: $R_\theta^{\mathsf T}R_\theta=\mathbf{1}_2$ (the columns are orthonormal) and $\det R_\theta=\cos^2\theta+\sin^2\theta=1$.

**Step 4: Surjectivity.**

Every element of $SO(2)$ is a value of $\exp$.

> [!note]- Derivation
> Let $R\in SO(2)$ be arbitrary. By the description of $SO(2)$ used in Step 3, $R=R_\varphi$ for some $\varphi\in\mathbb{R}$. Take $A_\varphi=\varphi J\in\mathfrak{so}(2)$. By Steps 2–3,
> $$\exp(A_\varphi)=R_\varphi=R\qquad\text{(by the closed form of Step 3).}$$
> Hence every $R\in SO(2)$ has a preimage under $\exp$, so $\exp\colon\mathfrak{so}(2)\to SO(2)$ is surjective.

**Step 5: Failure of injectivity and the fibre $2\pi\mathbb{Z}$.**

The map $\exp$ is not injective; its fibre over the identity is $\{A_{2\pi k}:k\in\mathbb{Z}\}$, identified with the subgroup $2\pi\mathbb{Z}\subset\mathbb{R}$ under $\theta\leftrightarrow A_\theta$.

> [!note]- Derivation
> By Step 3, $\exp(A_\theta)=\mathbf{1}_2=R_0$ if and only if $R_\theta=R_0$, which by the modulo-$2\pi$ clause of the $SO(2)$ description holds if and only if $\theta\equiv 0\pmod{2\pi}$, that is
> $$\exp(A_\theta)=\mathbf{1}_2\iff \cos\theta=1\text{ and }\sin\theta=0\iff \theta\in 2\pi\mathbb{Z}.$$
> In particular the two *distinct* algebra elements $A_0=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ and $A_{2\pi}=\begin{pmatrix}0&-2\pi\\2\pi&0\end{pmatrix}\ne A_0$ satisfy
> $$\exp(A_0)=\mathbf{1}_2=\exp(A_{2\pi}),$$
> so $\exp$ is **not injective**. Under the linear isomorphism $\mathbb{R}\xrightarrow{\sim}\mathfrak{so}(2)$, $\theta\mapsto A_\theta$, the fibre $\{A_\theta:\exp(A_\theta)=\mathbf{1}_2\}$ corresponds precisely to $2\pi\mathbb{Z}\subset\mathbb{R}$. More generally, the closed form of Step 3 makes $\exp$ a group homomorphism directly, with no appeal to any exponential-of-a-sum identity: the rotation matrices obey the angle-addition law
> $$R_\theta R_{\theta'}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}\begin{pmatrix}\cos\theta'&-\sin\theta'\\\sin\theta'&\cos\theta'\end{pmatrix}=\begin{pmatrix}\cos(\theta+\theta')&-\sin(\theta+\theta')\\\sin(\theta+\theta')&\cos(\theta+\theta')\end{pmatrix}=R_{\theta+\theta'}\qquad\text{(by the addition formulas }\cos(\theta+\theta')=\cos\theta\cos\theta'-\sin\theta\sin\theta'\text{ and }\sin(\theta+\theta')=\sin\theta\cos\theta'+\cos\theta\sin\theta'\text{, computed entrywise).}$$
> Hence, using $\exp(A_\theta)=R_\theta$ from Step 3,
> $$\exp(A_\theta)\exp(A_{\theta'})=R_\theta R_{\theta'}=R_{\theta+\theta'}=\exp(A_{\theta+\theta'})\qquad\text{(by Step 3 and the angle-addition law),}$$
> so $\exp\colon(\mathfrak{so}(2),+)\to SO(2)$ is a group homomorphism. Two algebra elements have the same image if and only if $\exp(A_\theta)=\exp(A_{\theta'})$, that is $R_\theta=R_{\theta'}$, which by the modulo-$2\pi$ clause of the $SO(2)$ description holds if and only if $\theta-\theta'\in2\pi\mathbb{Z}$; hence the fibres of $\exp$ are exactly the cosets of the kernel $2\pi\mathbb{Z}$. This is the sense in which $SO(2)\cong\mathbb{R}/2\pi\mathbb{Z}\cong S^1$ and the exponential is the covering $\mathbb{R}\to S^1$. This proves part 3. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For $A_\theta=\theta J\in\mathfrak{so}(2)$ with $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, one has $\exp(A_\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$, and $\exp\colon\mathfrak{so}(2)\to SO(2)$ is surjective but not injective, with fibre over $\mathbf{1}_2$ equal to $2\pi\mathbb{Z}$.
>
> Since $J^2=-\mathbf{1}_2$, induction gives $J^{2k}=(-1)^k\mathbf{1}_2$ and $J^{2k+1}=(-1)^kJ$, so $A_\theta^{2k}=(-1)^k\theta^{2k}\mathbf{1}_2$ and $A_\theta^{2k+1}=(-1)^k\theta^{2k+1}J$.
>
> As $SO(2)$ is a closed subgroup of $GL(2;\mathbb{R})$, the matrix-group exponential theorem gives $\exp(A_\theta)=\sum_{n\ge0}A_\theta^{n}/n!$, absolutely convergent. Regrouping into even and odd indices (licensed by absolute convergence) and inserting the power formulas,
> $$\exp(A_\theta)=\Big(\sum_{k\ge0}\tfrac{(-1)^k\theta^{2k}}{(2k)!}\Big)\mathbf{1}_2+\Big(\sum_{k\ge0}\tfrac{(-1)^k\theta^{2k+1}}{(2k+1)!}\Big)J=\cos\theta\,\mathbf{1}_2+\sin\theta\,J=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}=R_\theta.$$
>
> By the rotation-matrix description of $SO(2)$, every element is $R_\varphi=\exp(A_\varphi)$, so $\exp$ is surjective. And $\exp(A_\theta)=\mathbf{1}_2=R_0$ iff $\cos\theta=1,\ \sin\theta=0$ iff $\theta\in2\pi\mathbb{Z}$; thus $A_0\ne A_{2\pi}$ but $\exp(A_0)=\exp(A_{2\pi})=\mathbf{1}_2$, so $\exp$ is not injective, with fibre over $\mathbf{1}_2$ the subgroup $2\pi\mathbb{Z}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: splitting the series before establishing convergence
> It is tempting to split $\sum_n A_\theta^n/n!$ into even and odd parts "because that is what the pattern suggests," without noting why the split is valid. Reordering the terms of a series can change its sum for series that are only conditionally convergent; the regrouping here is legitimate *only* because the matrix exponential converges absolutely, a fact supplied by the cited theorem ($\sum_n\lVert A_\theta\rVert^n/n!=e^{\lVert A_\theta\rVert}<\infty$). The extra condition that makes the manipulation legal is absolute convergence; without invoking it the computation is a formal calculation, not a proof.

> [!note]- Independent sanity check via the isomorphism $SO(2)\cong U(1)$
> Under [[Thm - SO(2) is Isomorphic to U(1)|the isomorphism $SO(2)\cong U(1)$]], $R_\varphi\mapsto e^{i\varphi}$, and the corresponding Lie algebra map sends $A_\theta=\theta J$ to $i\theta\in\mathfrak{u}(1)=i\mathbb{R}$. The exponential of $U(1)$ is $i\theta\mapsto e^{i\theta}$, whose surjectivity onto the unit circle and $2\pi\mathbb{Z}$-periodic non-injectivity are the familiar properties of the complex exponential. This matches the matrix computation exactly: $\exp(A_\theta)=R_\theta\leftrightarrow e^{i\theta}$, surjective onto $U(1)$, with kernel $2\pi\mathbb{Z}$. The whole exercise is the matrix incarnation of "$e^{i\theta}$ wraps the line onto the circle."

---

# Key Takeaways

**A single polynomial relation on a generator collapses its exponential into a closed form, and $J^2=-\mathbf{1}_2$ is the archetype producing $\cos$ and $\sin$.** The entire computation turns on the observation that $J$ squares to $-\mathbf{1}_2$, which sorts the infinitely many powers $J^n$ into just two matrices according to the parity of $n$. This is a completely general mechanism: whenever the generator satisfies a low-degree relation — $J^2=-\mathbf{1}_2$ here, $N^2=0$ for a nilpotent (giving $e^{tN}=\mathbf{1}+tN$), $P^2=P$ for a projection (giving $e^{tP}=\mathbf{1}+(e^t-1)P$) — the exponential series folds along that relation into a finite combination of a few fixed matrices with scalar coefficients, and those coefficients are the sub-series of $e^t$ selected by the relation. The trigger to look for is a generator whose square (or cube) is a scalar times the identity or is zero; the reaction is to fold the series and read off the resulting elementary functions. Here the even sub-series of $e^\theta$ with alternating signs is $\cos\theta$ and the odd one is $\sin\theta$, so the rotation matrix drops out with no further work.

**The exponential map of a compact group is surjective but has a kernel lattice, and that lattice measures the group's topology.** $SO(2)\cong S^1$ is the simplest compact Lie group, and its exponential exhibits both phenomena in their cleanest form: surjectivity (guaranteed in general for compact connected groups — see [[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|the surjectivity theorem]]) and a non-trivial kernel $2\pi\mathbb{Z}$. The kernel is not an accident of the parametrisation; it is the *integral lattice* of the maximal torus, and its quotient $\mathfrak{so}(2)/2\pi\mathbb{Z}\cong SO(2)$ realises the circle as a line modulo a lattice. The transferable diagnostic: on any torus $T^n=\mathbb{R}^n/\Lambda$ the exponential is the quotient map $\mathbb{R}^n\to\mathbb{R}^n/\Lambda$, surjective with kernel the lattice $\Lambda$, and the failure of injectivity is exactly the fundamental group $\pi_1(T^n)\cong\Lambda$. The circle case is where one first sees that a non-injective exponential encodes the fact that the group is not simply connected — the covering $\mathbb{R}\to S^1$ is the universal cover, and $2\pi\mathbb{Z}$ is its deck group.

**Injectivity of the exponential is the exception, not the rule, and this example is the standard counterexample to keep at hand.** For a *nilpotent* or simply-connected-solvable group the exponential can be a global diffeomorphism, but for any group containing a circle subgroup it cannot be injective, because that circle already forces a $2\pi\mathbb{Z}$ periodicity. When a general claim about Lie groups tacitly assumes $\exp$ is injective or a bijection, $SO(2)$ is the immediate refutation: $\exp$ here is a local diffeomorphism near $0$ (its differential at $0$ is the identity) yet globally many-to-one, so "local diffeomorphism" and "global bijection" are genuinely different and $SO(2)$ separates them. Retain this example as the two-line certificate that the exponential map, while always a local diffeomorphism at the origin, is in general neither injective nor a covering with trivial deck group; the size of its kernel is a topological invariant of the group, and for $SO(2)$ that invariant is the lattice $2\pi\mathbb{Z}$.
