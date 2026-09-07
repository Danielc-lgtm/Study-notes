---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Exponential Map of a Matrix Group is the Matrix Exponential"
  - "Thm - Lie Algebras and Dimensions of the Classical Matrix Groups"
  - "Def - Classical Matrix Groups"
  - "Def - Exponential Map of a Lie Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $SL(2;\mathbb{R})=\{g\in\operatorname{Mat}(2\times2;\mathbb{R}):\det g=1\}$ be the special linear group, a connected Lie group, and let $\mathfrak{sl}(2;\mathbb{R})=\{X\in\operatorname{Mat}(2\times2;\mathbb{R}):\operatorname{tr}X=0\}$ be its Lie algebra of traceless real $2\times2$ matrices. Prove that the exponential map
$$\exp\colon\mathfrak{sl}(2;\mathbb{R})\longrightarrow SL(2;\mathbb{R}),\qquad \exp(X)=e^{X}=\sum_{k\ge0}\frac{X^{k}}{k!},$$
is **not surjective**. Concretely, show that the diagonal matrix
$$g_0=\begin{pmatrix}-2&0\\[2pt]0&-\tfrac12\end{pmatrix}\in SL(2;\mathbb{R})$$
lies in no image $\exp(X)$ with $X\in\mathfrak{sl}(2;\mathbb{R})$.

This is the standard non-compact counterpart to the surjectivity theorem for compact groups. Because $SL(2;\mathbb{R})$ is connected but **non-compact**, the guarantee that every group element is an exponential — which holds for a compact connected Lie group — fails here, and $g_0$ is an explicit witness to the failure.

**Recall.**

The objects in play are the special linear group and its Lie algebra, the identification of the abstract exponential map of a matrix group with the matrix exponential series, and the description of $\mathfrak{sl}(2;\mathbb{R})$ as the traceless matrices.

![[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential#Statement]]

In the case at hand this says: for every $X\in\operatorname{Mat}(2\times2;\mathbb{R})$ the series $e^{X}=\sum_{k\ge0}X^{k}/k!$ converges absolutely; for the closed subgroup $G=SL(2;\mathbb{R})\subset GL(2;\mathbb{R})$ with Lie algebra $\mathfrak{g}=\mathfrak{sl}(2;\mathbb{R})$, the [[Def - Exponential Map of a Lie Group|abstract Lie-group exponential]] $\exp_{G}$ coincides with this matrix exponential, $\exp_{G}(X)=e^{X}$, and $e^{tX}\in G$ for all $t\in\mathbb{R}$. So computing the image of $\exp$ on $\mathfrak{sl}(2;\mathbb{R})$ is computing the set of matrix exponentials $e^{X}$ of traceless real $X$.

![[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups#Statement]]

The one clause we use is $\mathfrak{sl}(2;\mathbb{R})=\{X\in\operatorname{Mat}(2\times2;\mathbb{R}):\operatorname{tr}X=0\}$, of real dimension $2^{2}-1=3$. The [[Def - Classical Matrix Groups|special linear group]] $SL(2;\mathbb{R})$ itself is $\{g:\det g=1\}$.

We also use two standard facts of linear algebra, each recalled and used explicitly below: the **Cayley–Hamilton theorem** (a matrix satisfies its own characteristic polynomial) and **triangularisability over $\mathbb{C}$** (every complex square matrix is similar to an upper-triangular one, whose diagonal entries are its eigenvalues).

---

# Convergent Strategy

**Problem class.** This is a *disprove-surjectivity* problem: we must exhibit a point of the codomain that is not in the image of a map. The map is a matrix power series, which looks intractable term by term, so the whole strategy is to replace "is $g_0$ an infinite series $e^{X}$?" by a finite, checkable invariant. The right invariant is the **spectrum** (the multiset of eigenvalues): the spectrum of $e^{X}$ is completely determined by the spectrum of $X$, and the spectrum of a traceless $2\times2$ matrix is extremely constrained. So the problem collapses to a comparison of two two-element multisets of numbers.

**Assumption pattern.** The single structural hypothesis is $\operatorname{tr}X=0$. Its only role is to force the characteristic polynomial of $X$ to be $t^{2}+\det X$ — a polynomial *with no linear term* — so that the two eigenvalues of $X$ are $\pm\lambda$ for a single number $\lambda$ with $\lambda^{2}=-\det X$. Because $\det X$ is real, $\lambda^{2}$ is real, and therefore $\lambda$ is *either real or purely imaginary*: there is no third possibility. This dichotomy is the entire engine of the obstruction. The recognisable trigger is a target matrix in $SL(2;\mathbb{R})$ that has a **negative real eigenvalue of modulus $\ne1$**; such a spectrum is incompatible with both branches of the dichotomy.

**Theorem routing.** The route is: use [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] to turn $\exp(X)$ into $e^{X}$; use [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the Lie-algebra description]] to know $X$ is traceless; use the **Cayley–Hamilton theorem** to get $X^{2}=-(\det X)\,I$ and hence the eigenvalues $\pm\lambda$; use **triangularisation over $\mathbb{C}$** to deduce that the eigenvalues of $e^{X}$ are $e^{\lambda}$ and $e^{-\lambda}$; and finally compare with the eigenvalues $-2,-\tfrac12$ of $g_0$, ruling out each branch of the real/imaginary dichotomy.

**Key decision point.** Two moves carry the idea. The first is the decision to *pass from the matrix to its spectrum* rather than trying to solve $e^{X}=g_0$ directly: a spectral invariant is preserved by the exponential in a transparent way ($\alpha\mapsto e^{\alpha}$), whereas the matrix equation is a transcendental system. The second is recognising that a *negative real eigenvalue* is the correct obstruction: a positive real $\lambda$ gives $e^{\pm\lambda}>0$, so negativity forces $\lambda$ purely imaginary; but a purely imaginary $\lambda=i\mu$ gives $|e^{\pm i\mu}|=1$, so a negative real eigenvalue can only be $-1$, and it must then be *repeated*. Since $g_0$ has a negative eigenvalue that is neither of modulus one nor repeated, both branches die. The genuine insight is that "$g_0$ has determinant $1$ and could be an exponential on those grounds" is a red herring; the obstruction is not the determinant but the *sign and size of the eigenvalues*.

---

# Legal Operations Used

This solution deploys the following legal operations from the topic page's Legal Operations for §1.4 (the topic page is written after the subpages; the operations are named descriptively here and the orchestrator reconciles the numbering):

1. **Replace the abstract exponential by the matrix exponential series.** Because $SL(2;\mathbb{R})$ is a closed subgroup of $GL(2;\mathbb{R})$, [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] licenses writing $\exp(X)=e^{X}=\sum_{k\ge0}X^{k}/k!$, so the question about a Lie-group map becomes a question about a convergent matrix series.

2. **Read off the Lie algebra as a linear condition.** [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the classification of the classical Lie algebras]] identifies $\mathfrak{sl}(2;\mathbb{R})$ with the traceless real $2\times2$ matrices, turning "$X\in\mathfrak{sl}(2;\mathbb{R})$" into the usable equation $\operatorname{tr}X=0$.

3. **Collapse the matrix power series to a two-term closed form via Cayley–Hamilton.** For traceless $X$, the characteristic polynomial is $t^{2}+\det X$, so $X^{2}=-(\det X)\,I$; every higher power is a scalar multiple of $I$ or of $X$, and the whole series $e^{X}$ reduces to $c_{0}I+c_{1}X$ with explicit scalar coefficients.

4. **Pass to the spectrum through triangularisation.** Over $\mathbb{C}$ conjugate $X$ to an upper-triangular matrix with diagonal $\lambda,-\lambda$; conjugation commutes with the exponential, so $e^{X}$ is conjugate to an upper-triangular matrix with diagonal $e^{\lambda},e^{-\lambda}$, which are therefore its eigenvalues.

5. **Apply the real/purely-imaginary dichotomy for a square root of a real number.** Since $\lambda^{2}=-\det X\in\mathbb{R}$, the number $\lambda$ is real or purely imaginary; test each branch against the required negative eigenvalue.

6. **Extract a contradiction from a spectral invariant.** Compare the forced spectrum $\{e^{\lambda},e^{-\lambda}\}$ of any element of the image with the actual spectrum $\{-2,-\tfrac12\}$ of $g_0$; positivity in one branch and unit modulus in the other make the match impossible.

---

# Hints

> [!note]- Hint 1
> Do not try to solve $e^{X}=g_0$ for $X$. Instead compare an invariant that the exponential transforms in a controlled way. Eigenvalues are ideal: if $Xv=\alpha v$ then $e^{X}v=e^{\alpha}v$, so the eigenvalues of $e^{X}$ are the exponentials of the eigenvalues of $X$. What are the possible eigenvalues of a *traceless* real $2\times2$ matrix?

> [!note]- Hint 2
> A traceless $2\times2$ matrix has characteristic polynomial $t^{2}+\det X$ (no linear term, because the linear coefficient is $-\operatorname{tr}X=0$). Its eigenvalues are therefore $\pm\lambda$ where $\lambda^{2}=-\det X$. Since $\det X$ is a real number, $\lambda^{2}$ is real. What does that force about $\lambda$ itself?

> [!note]- Hint 3
> $\lambda^{2}\in\mathbb{R}$ means $\lambda$ is real (if $\lambda^{2}\ge0$) or purely imaginary (if $\lambda^{2}<0$); there is no other option. So the eigenvalues of $e^{X}$ are either $e^{\pm\lambda}$ with $\lambda\in\mathbb{R}$ — both *positive reals* — or $e^{\pm i\mu}$ with $\mu\in\mathbb{R}$ — both on the *unit circle*. Now look at the eigenvalues of $g_0$, namely $-2$ and $-\tfrac12$. Can a positive real or a unit-modulus number equal $-2$?

> [!note]- Hint 4
> The eigenvalue $-2$ of $g_0$ is a negative real of modulus $2$. In the real branch, $e^{\pm\lambda}>0$, so it cannot be $-2$. In the imaginary branch, $|e^{\pm i\mu}|=1\ne2$, so it cannot be $-2$ either. Both branches fail, so no traceless real $X$ can have $e^{X}=g_0$. (For the sharper statement: a negative eigenvalue in the imaginary branch forces $e^{\pm i\mu}=-1$, i.e. $\lambda\in i\pi\mathbb{Z}$ with both eigenvalues equal to $-1$ — so the *only* elements of the image with a negative eigenvalue are equal to $-I$.)

---

# Solution

The proof turns the surjectivity question into a spectral comparison. We first record that $g_0$ is a legitimate target ($\det g_0=1$), then reduce any candidate $e^{X}$ to its two eigenvalues $e^{\pm\lambda}$, where the traceless hypothesis forces $\lambda$ to be real or purely imaginary. In the real branch both eigenvalues are positive; in the imaginary branch both have modulus one. The eigenvalue $-2$ of $g_0$ is neither positive nor of modulus one, so $g_0$ is not in the image.

**Step 0: $g_0$ is a legitimate target in $SL(2;\mathbb{R})$.**

Before disproving that $g_0$ is an exponential, we confirm that it is an element of $SL(2;\mathbb{R})$ at all, so that the question is non-vacuous.

> [!note]- Derivation
> The matrix $g_0=\operatorname{diag}(-2,-\tfrac12)$ has real entries, and
> $$\det g_0=(-2)\cdot\left(-\tfrac12\right)=1\qquad\text{(product of the diagonal entries of a diagonal matrix)},$$
> so $g_0\in SL(2;\mathbb{R})$ by the definition $SL(2;\mathbb{R})=\{g:\det g=1\}$. Its trace is
> $$\operatorname{tr}g_0=-2+\left(-\tfrac12\right)=-\tfrac52\qquad\text{(sum of the diagonal entries)},$$
> and its two eigenvalues are the diagonal entries $-2$ and $-\tfrac12$ (the eigenvalues of a diagonal matrix are its diagonal entries), each of algebraic multiplicity one. In particular $g_0$ has a negative real eigenvalue, $-2$, of modulus $2$. These two facts — the eigenvalue is negative, and its modulus is not $1$ — are exactly the two features the proof will play off.

**Step 1: reduce a candidate $e^{X}$ to a two-term closed form using tracelessness.**

Assume, for contradiction, that $g_0=\exp(X)=e^{X}$ for some $X\in\mathfrak{sl}(2;\mathbb{R})$. We first express $e^{X}$ in closed form.

> [!note]- Derivation
> By [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the Lie-algebra description]], $X\in\mathfrak{sl}(2;\mathbb{R})$ means $X$ is a real $2\times2$ matrix with $\operatorname{tr}X=0$. Its characteristic polynomial is
> $$\chi_{X}(t)=t^{2}-(\operatorname{tr}X)\,t+\det X=t^{2}+\det X\qquad\text{(since }\operatorname{tr}X=0\text{)}.$$
> By the **Cayley–Hamilton theorem** (every matrix satisfies its own characteristic polynomial), $\chi_{X}(X)=0$, that is
> $$X^{2}=-(\det X)\,I.\tag{1}$$
> Set $\lambda\in\mathbb{C}$ to be a square root of $-\det X$, so that $\lambda^{2}=-\det X$ and, by (1), $X^{2}=\lambda^{2}I$. We record for Step 2 that $\lambda^{2}=-\det X$ is a **real number**, because $\det X\in\mathbb{R}$.
>
> When $\lambda\ne0$, equation (1) lets us sum the exponential series in closed form. Splitting into even and odd powers and using $X^{2m}=\lambda^{2m}I$ and $X^{2m+1}=\lambda^{2m}X$ (immediate from $X^{2}=\lambda^{2}I$ by induction),
> $$e^{X}=\sum_{k\ge0}\frac{X^{k}}{k!}=\Bigl(\sum_{m\ge0}\frac{\lambda^{2m}}{(2m)!}\Bigr)I+\Bigl(\sum_{m\ge0}\frac{\lambda^{2m}}{(2m+1)!}\Bigr)X=\cosh\lambda\,I+\frac{\sinh\lambda}{\lambda}\,X,\tag{2}$$
> where the rearrangement into even and odd parts is legitimate because the series converges *absolutely* (by [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]], which asserts absolute convergence of $\sum_{k}X^{k}/k!$), and $\cosh,\sinh$ are the usual entire functions. When $\lambda=0$, equation (1) reads $X^{2}=0$, so the series terminates: $e^{X}=I+X$. The closed form (2) is convenient but not strictly needed; Step 2 uses only the eigenvalues, which we now extract.

**Step 2: the eigenvalues of $e^{X}$ are $e^{\lambda}$ and $e^{-\lambda}$.**

The spectrum of any candidate exponential is $\{e^{\lambda},e^{-\lambda}\}$, and $\lambda$ is real or purely imaginary.

> [!note]- Derivation
> The characteristic polynomial of $X$ factors over $\mathbb{C}$ as
> $$\chi_{X}(t)=t^{2}+\det X=t^{2}-\lambda^{2}=(t-\lambda)(t+\lambda)\qquad\text{(since }\lambda^{2}=-\det X\text{)},$$
> so the eigenvalues of $X$ are exactly $\lambda$ and $-\lambda$. By **triangularisability over $\mathbb{C}$**, there is an invertible complex matrix $P$ with
> $$PXP^{-1}=T=\begin{pmatrix}\lambda&\ast\\[2pt]0&-\lambda\end{pmatrix}\qquad\text{(upper triangular; the diagonal entries of a triangular form are the eigenvalues).}$$
> Conjugation commutes with the exponential: for every partial sum, $P\bigl(\sum_{k=0}^{N}X^{k}/k!\bigr)P^{-1}=\sum_{k=0}^{N}(PXP^{-1})^{k}/k!$ because $PX^{k}P^{-1}=(PXP^{-1})^{k}$, and letting $N\to\infty$ (both sides converge, again by [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]]) gives
> $$P\,e^{X}P^{-1}=e^{T}.$$
> The exponential of an upper-triangular matrix is upper triangular with the exponentiated diagonal (powers of $T$ are upper triangular with diagonal $\lambda^{k},(-\lambda)^{k}$, and the series sums the diagonal to $e^{\lambda},e^{-\lambda}$), so
> $$e^{T}=\begin{pmatrix}e^{\lambda}&\ast\\[2pt]0&e^{-\lambda}\end{pmatrix}.$$
> Since $e^{X}$ is conjugate to $e^{T}$, its eigenvalues are the diagonal entries of $e^{T}$, namely
> $$\operatorname{spec}(e^{X})=\{e^{\lambda},\,e^{-\lambda}\}.\tag{3}$$
> This computation is uniform in $\lambda$: it includes the case $\lambda=0$, where (3) reads $\{1,1\}$, consistent with $e^{X}=I+X$ being unipotent. Finally, because $\lambda^{2}=-\det X$ is real (recorded in Step 1), $\lambda$ is **real or purely imaginary**: if $\lambda^{2}\ge0$ then $\lambda=\pm\sqrt{\lambda^{2}}\in\mathbb{R}$, and if $\lambda^{2}<0$ then $\lambda=\pm i\sqrt{-\lambda^{2}}\in i\mathbb{R}$; these are the only two cases.

**Step 3: neither branch can produce the eigenvalue $-2$.**

Matching the forced spectrum $\{e^{\lambda},e^{-\lambda}\}$ against the actual spectrum $\{-2,-\tfrac12\}$ of $g_0$ is impossible in both branches.

> [!note]- Derivation
> Suppose $g_0=e^{X}$. Then by (3) and Step 0 the multisets of eigenvalues agree:
> $$\{e^{\lambda},\,e^{-\lambda}\}=\{-2,\,-\tfrac12\}.$$
> In particular one of $e^{\lambda},e^{-\lambda}$ equals $-2$; without loss of generality $e^{\lambda}=-2$ (the other case, $e^{-\lambda}=-2$, is identical after replacing $\lambda$ by $-\lambda$, which leaves the traceless matrix $X$ and the pair $\{\pm\lambda\}$ unchanged). We derive a contradiction in each branch of Step 2's dichotomy.
>
> **Real branch ($\lambda\in\mathbb{R}$).** The real exponential is strictly positive: $e^{\lambda}>0$ for every real $\lambda$. But $-2<0$, so $e^{\lambda}=-2$ is impossible. This branch is void.
>
> **Purely imaginary branch ($\lambda=i\mu$, $\mu\in\mathbb{R}$).** Then $e^{\lambda}=e^{i\mu}=\cos\mu+i\sin\mu$ has modulus
> $$|e^{i\mu}|=\sqrt{\cos^{2}\mu+\sin^{2}\mu}=1\qquad\text{(Pythagorean identity)}.$$
> But $|-2|=2\ne1$, so $e^{\lambda}=-2$ is impossible here as well. This branch is void.
>
> Both branches are exhausted (Step 2 established that no third possibility for $\lambda$ exists), so the assumption $g_0=e^{X}$ is untenable. Naming the contradiction: we assumed $g_0=\exp(X)$ for some $X\in\mathfrak{sl}(2;\mathbb{R})$ and derived that $-2$ must simultaneously be a positive real (real branch) or a number of modulus one (imaginary branch), each of which is false. Therefore
> $$g_0=\begin{pmatrix}-2&0\\[2pt]0&-\tfrac12\end{pmatrix}\notin\exp\!\bigl(\mathfrak{sl}(2;\mathbb{R})\bigr).$$
> Since $g_0\in SL(2;\mathbb{R})$ (Step 0), the exponential map $\exp\colon\mathfrak{sl}(2;\mathbb{R})\to SL(2;\mathbb{R})$ misses $g_0$ and hence is not surjective.

> [!note]- Complete formal solution
> **Claim.** $\exp\colon\mathfrak{sl}(2;\mathbb{R})\to SL(2;\mathbb{R})$ is not surjective; specifically $g_0=\operatorname{diag}(-2,-\tfrac12)$ is not in its image.
>
> First, $g_0\in SL(2;\mathbb{R})$ because $\det g_0=(-2)(-\tfrac12)=1$; its eigenvalues are $-2$ and $-\tfrac12$.
>
> Suppose $g_0=\exp(X)=e^{X}$ with $X\in\mathfrak{sl}(2;\mathbb{R})$; here $\exp(X)=e^{X}$ by [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]] for the closed subgroup $SL(2;\mathbb{R})\subset GL(2;\mathbb{R})$, and $X$ is a real $2\times2$ matrix with $\operatorname{tr}X=0$ by [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups|the Lie-algebra description]].
>
> Because $\operatorname{tr}X=0$, the characteristic polynomial of $X$ is $\chi_{X}(t)=t^{2}+\det X$. Let $\lambda\in\mathbb{C}$ satisfy $\lambda^{2}=-\det X$; then $\chi_{X}(t)=(t-\lambda)(t+\lambda)$, so $X$ has eigenvalues $\pm\lambda$. Since $\det X\in\mathbb{R}$, the number $\lambda^{2}$ is real, hence $\lambda$ is real or purely imaginary.
>
> Triangularise over $\mathbb{C}$: $PXP^{-1}$ is upper triangular with diagonal $\lambda,-\lambda$. As conjugation commutes with the (absolutely convergent) exponential series, $P e^{X}P^{-1}=e^{PXP^{-1}}$ is upper triangular with diagonal $e^{\lambda},e^{-\lambda}$. Therefore the eigenvalues of $e^{X}$ are $e^{\lambda}$ and $e^{-\lambda}$.
>
> Matching spectra, $\{e^{\lambda},e^{-\lambda}\}=\{-2,-\tfrac12\}$, so (after possibly swapping $\lambda\leftrightarrow-\lambda$) $e^{\lambda}=-2$. If $\lambda\in\mathbb{R}$ then $e^{\lambda}>0\ne-2$, a contradiction. If $\lambda=i\mu$ with $\mu\in\mathbb{R}$ then $|e^{\lambda}|=|e^{i\mu}|=1\ne2=|-2|$, a contradiction. No third case for $\lambda$ exists, so the assumption $g_0=e^{X}$ is false.
>
> Hence $g_0\notin\exp(\mathfrak{sl}(2;\mathbb{R}))$, while $g_0\in SL(2;\mathbb{R})$; the exponential map is not surjective. $\blacksquare$

> [!warning] Illegal but tempting route: "$\det$ and connectedness force surjectivity"
> A tempting shortcut is to note $\det e^{X}=e^{\operatorname{tr}X}=e^{0}=1$, so every $e^{X}$ has determinant $1$; and $g_0$ also has determinant $1$; and $SL(2;\mathbb{R})$ is connected and $\exp$ covers a neighbourhood of $I$; therefore (the false leap) $\exp$ is onto. **This is invalid.** Matching the determinant is a *necessary* condition — the image of $\exp$ certainly lands in $SL(2;\mathbb{R})$ — but it is not sufficient, and covering a neighbourhood of the identity of a connected group does not force surjectivity, because the image of $\exp$ need not be a subgroup (a product $e^{X}e^{Y}$ need not be an exponential when $X,Y$ do not commute). The extra condition that *would* make the leap legal is **compactness**: for a *compact* connected Lie group the exponential is onto ([[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|the surjectivity theorem]], via a bi-invariant Riemannian metric whose geodesics through $e$ are one-parameter subgroups). $SL(2;\mathbb{R})$ is connected but not compact, so exactly this ingredient is missing, and the theorem does not apply.

> [!note]- Independent sanity check: which negative-eigenvalue elements *are* exponentials
> The proof says a bit more than non-membership of $g_0$: in the imaginary branch, an eigenvalue $e^{i\mu}$ that is a negative real forces $\sin\mu=0$ and $\cos\mu<0$, i.e. $\mu\in\pi+2\pi\mathbb{Z}$, whence $\lambda=i\mu\in i\pi\mathbb{Z}$ and *both* eigenvalues equal $e^{\pm i\mu}=-1$. By formula (2) with $\lambda=i\mu$ and $\sin\mu=0$, $e^{X}=\cos\mu\,I=-I$. So the only elements of $\exp(\mathfrak{sl}(2;\mathbb{R}))$ with a negative eigenvalue are equal to $-I$. As a concrete confirmation, take
> $$X=\begin{pmatrix}0&\pi\\[2pt]-\pi&0\end{pmatrix}\in\mathfrak{sl}(2;\mathbb{R})\qquad(\operatorname{tr}X=0,\ \det X=\pi^{2},\ \lambda^{2}=-\pi^{2},\ \lambda=i\pi).$$
> Then (2) gives $e^{X}=\cos\pi\,I+\dfrac{\sin\pi}{\pi}X=-I$, so $-I$ is indeed an exponential, whereas $g_0\ne-I$ has distinct negative eigenvalues and is not. This matches the theorem exactly.

---

# Key Takeaways

**To disprove that a map is surjective, transport the question to an invariant the map transforms transparently, then land the target outside the invariant's reach.** The exponential of a matrix is an intractable infinite series, but its action on *eigenvalues* is the one-line rule $\alpha\mapsto e^{\alpha}$. The strategic move here is to stop looking at the matrix equation $e^{X}=g_0$ and to look only at what the exponential does to the spectrum. The trigger for this move is any surjectivity question about a map built out of a scalar function applied to a linear operator — matrix exponentials, resolvents, functional calculus generally — where the operator's spectrum is constrained. The diagnostic to carry forward is: *find the invariant the map acts on by a known scalar rule, compute the constraint the domain places on that invariant, and check whether the target's invariant satisfies it.* Here the domain constraint is "eigenvalues come in the pattern $e^{\pm\lambda}$ with $\lambda$ real or purely imaginary", and the target $g_0$ violates it through its eigenvalue $-2$.

**The traceless condition is a spectral symmetry, and it is the whole reason the obstruction exists.** Setting $\operatorname{tr}X=0$ removes the linear term of the characteristic polynomial, forcing the eigenvalues into the symmetric pair $\pm\lambda$ and forcing $\lambda^{2}=-\det X$ to be real. Realness of $\lambda^{2}$ is what splits $\lambda$ into "real, giving positive $e^{\pm\lambda}$" or "imaginary, giving unit-modulus $e^{\pm\lambda}$", and it is precisely this dichotomy that a negative eigenvalue of modulus $\ne1$ cannot satisfy. The general principle: a *trace-zero* hypothesis on a small matrix is best read as a statement about the *symmetry of the spectrum*, not as an abstract linear constraint. Whenever a problem hands you traceless $2\times2$ (or, more generally, a matrix whose characteristic polynomial has controlled coefficients), reach for Cayley–Hamilton to collapse powers and for the spectrum to encode everything the exponential can produce. The same computation shows $e^{X}$ for traceless real $X$ always has $\operatorname{tr}e^{X}=e^{\lambda}+e^{-\lambda}=2\cosh\lambda\ge2$ (real branch) or $=2\cos\mu\in[-2,2]$ (imaginary branch), which is another way to see that a matrix with trace $-\tfrac52<-2$ is unreachable.

**Non-compactness is exactly what breaks surjectivity of the exponential, and this exercise is the standard witness.** For a compact connected Lie group the exponential is onto: a bi-invariant metric makes one-parameter subgroups into geodesics, and completeness plus the Hopf–Rinow theorem connect the identity to every point by such a geodesic. That argument needs compactness (to get a bi-invariant metric and completeness with the right geodesics), and $SL(2;\mathbb{R})$ has neither a bi-invariant metric nor compactness, so the conclusion genuinely fails. Recognising this frames the result correctly for later use: whenever a proof wants to write a group element as $\exp(\text{something})$ and the group is non-compact, the step is *not free* and must be justified separately (often one instead writes elements as *products* of exponentials, since $\exp(\mathfrak{g})$ generates a connected group even when it does not exhaust it). The contrast pair to keep together in memory is this exercise, where $\exp$ misses $\operatorname{diag}(-2,-\tfrac12)$ in the non-compact $SL(2;\mathbb{R})$, and the companion computation on $SU(2)$ — see [[Ex - Computing exp on su(2) via the Quaternion Formula]] — where the compact group *is* exhausted by the exponential, the two results together drawing the exact line that compactness controls.
