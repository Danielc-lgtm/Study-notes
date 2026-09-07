---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation"
  - "Def - Path-Ordered Exponential"
  - "Def - The Pauli Matrices"
tags: [geometry, gauge-theory]
---

# Problem Statement

We work with the parallel-transport equation of a matrix-group connection in a single trivialising chart. For a matrix group $G\subset GL(n;\mathbb{K})$ the horizontal lift of a curve reduces to the linear ordinary differential equation
$$\dot v(t)=-A(t)\,v(t),\qquad v(0)=v_0,$$
whose solution operator is the path-ordered exponential $\mathcal{P}\!\exp\!\big(-\int_0^t A\big)$. Its Dyson series (the ordered-integral expansion proved to solve this equation) begins
$$\mathcal{P}\!\exp\!\Big(-\int_0^t A\Big)=\mathbf{1}-\int_0^t A(\tau_1)\,d\tau_1+\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)-\cdots.$$

Take the smallest genuinely non-commutative example: a **two-level system**, $n=2$ and $\mathbb{K}=\mathbb{C}$, with
$$A(t)=a(t)\,\sigma_1+b(t)\,\sigma_3,$$
where $a,b\colon[0,L]\to\mathbb{R}$ are given continuous functions and $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices.

Do the following.

1. Write the **second-order term** of the Dyson series, $U_2(t):=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)$, explicitly as a $2\times2$ matrix, decomposed into its component along the identity $\mathbf{1}$ and its component along $\sigma_2$.
2. Compare $U_2(t)$ with the term $\tfrac12\big(\int_0^t A\big)^2$ that the *naive* (unordered) exponential $\exp\!\big(-\int_0^t A\big)$ would produce at the same order, and show that
$$U_2(t)-\tfrac12\Big(\int_0^t A\Big)^2=-\,i\,W(t)\,\sigma_2,\qquad W(t):=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,\big(a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1)\big).$$
3. Conclude that $U_2(t)\neq\tfrac12\big(\int_0^t A\big)^2$ in general, and identify exactly when equality holds: the two agree if and only if $W(t)=0$; they agree for *every* $t$ if and only if $a$ and $b$ are proportional as functions — in particular whenever $a\equiv0$ or $b\equiv0$. Exhibit an explicit $(a,b)$ for which $W(t)\neq0$.

**Recall:**

The objects in play are the path-ordered exponential, the theorem that its Dyson series solves the linear transport equation, the Pauli matrices, and the elementary algebra of their products.

![[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation#Statement]]

We use only the first two orders of that series. Writing $U(t)=\mathcal{P}\!\exp\!\big(-\int_0^t A\big)$ for the [[Def - Path-Ordered Exponential|path-ordered exponential]], the theorem gives, for continuous $A\colon[0,L]\to\operatorname{Mat}(n\times n;\mathbb{C})$,
$$U(t)=\sum_{j\ge0}(-1)^j\int_0^t d\tau_j\int_0^{\tau_j}d\tau_{j-1}\cdots\int_0^{\tau_2}d\tau_1\,A(\tau_j)A(\tau_{j-1})\cdots A(\tau_1),$$
the series converging absolutely and uniformly in $C^1([0,L])$; its $j=2$ contribution is the term $U_2(t)$ under study. The **ordering** matters: inside the integral the argument with the larger time-variable stands to the left, and this order cannot be permuted when the matrices $A(\tau_2)$ and $A(\tau_1)$ fail to commute.

![[Def - Path-Ordered Exponential#The Definition]]

![[Def - The Pauli Matrices#The Definition]]

Concretely, the [[Def - The Pauli Matrices|Pauli matrices]] are the three Hermitian, traceless, involutory $2\times2$ complex matrices
$$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
together with the identity $\mathbf{1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$. The only algebra we need is the pair of products that mix $\sigma_1$ and $\sigma_3$. Direct multiplication gives
$$\sigma_1^2=\sigma_3^2=\mathbf{1},\qquad \sigma_1\sigma_3=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-\,i\,\sigma_2,\qquad \sigma_3\sigma_1=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=+\,i\,\sigma_2,$$
so that $\sigma_1$ and $\sigma_3$ **anticommute**, $\sigma_1\sigma_3+\sigma_3\sigma_1=0$, and their **commutator** is
$$[\sigma_1,\sigma_3]=\sigma_1\sigma_3-\sigma_3\sigma_1=-2i\,\sigma_2.$$
These four numbers — two squares equal to $\mathbf{1}$, one commutator equal to $-2i\sigma_2$ — carry the entire computation.

---

# Convergent Strategy

**Problem class.** This is a *compute-and-compare* exercise whose real content is a structural inequality: the ordered (path-ordered) product is not the ordinary exponential, and the exercise measures the exact gap at second order. It belongs to the family "expand a solution operator in a small-time or perturbative series and read off the first correction where non-commutativity enters." The recognisable signature is a linear operator equation $\dot v=-A(t)v$ with $A(t)$ **time-dependent and non-commuting at different times**; whenever those two features are present, the naive substitution $v(t)=\exp(-\int A)v_0$ is *wrong beyond first order*, and the correct object is the path-ordered exponential.

**Assumption pattern.** The hypotheses are minimal and are all used. Continuity of $a,b$ (hence of $A$) is what licenses the theorem that the Dyson series converges and solves the equation, so that "the second-order term" is a well-defined matrix rather than a formal symbol. The two-level ansatz $A(t)=a(t)\sigma_1+b(t)\sigma_3$ is chosen so that $A(t)$ ranges over the *two-dimensional* real span of $\sigma_1$ and $\sigma_3$; the product of two such matrices closes on $\{\mathbf{1},\sigma_2\}$ alone, which is what makes the computation finite and transparent. The absence of a $\sigma_2$ term in $A(t)$ itself is essential: it is precisely why the *symmetric* part of the product lands on $\mathbf{1}$ and the *antisymmetric* (commutator) part lands on $\sigma_2$, cleanly separating the "would-be exponential" piece from the "ordering defect" piece.

**Theorem routing.** The route is short and forced. First, quote the Dyson series from [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation|the path-ordered-exponential theorem]] to obtain $U_2(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)$. Second, expand the integrand $A(\tau_2)A(\tau_1)$ using the Pauli products from the Recall, splitting it into a symmetric part (proportional to $\mathbf{1}$) and an antisymmetric part (proportional to $\sigma_2$). Third, integrate each part over the ordered simplex $0\le\tau_1\le\tau_2\le t$, using the elementary identity $\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,f(\tau_2)f(\tau_1)=\tfrac12\big(\int_0^t f\big)^2$ to recover the identity-part of $\tfrac12(\int A)^2$. Fourth, recognise that the leftover $\sigma_2$-part is exactly the ordered integral of the commutator, and identify it with the *second-order Magnus term* $\tfrac12\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,[A(\tau_2),A(\tau_1)]$.

**Key decision point.** The one genuinely clarifying move is to *not* compute the two double integrals of $U_2$ and of $\tfrac12(\int A)^2$ separately and subtract, but to prove the general operator identity
$$\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)-\tfrac12\Big(\int_0^t A\Big)^2=\tfrac12\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,[A(\tau_2),A(\tau_1)]$$
*first*, valid for any continuous matrix-valued $A$, and only then specialise. This isolates the discrepancy as an integral of a commutator, so the whole question "when do they agree?" reduces to "when does the commutator integrate to zero?", and the two-level structure then makes the commutator a scalar multiple of $\sigma_2$. The alternative — grinding both quadratics into Pauli components and hoping the identity parts cancel — works but hides why the leftover is exactly the ordering defect.

---

# Legal Operations Used

This solution deploys the following operations, whose general forms are recorded on the chapter topic page's Legal Operations list; here we name each descriptively and show how it is applied.

1. **Truncate the path-ordered exponential at a fixed order.** Because the Dyson series converges absolutely and uniformly (by the path-ordered-exponential theorem), each order is an honest matrix and may be isolated; we extract the $j=2$ term $U_2(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)$.

2. **Split a product of Lie-algebra elements into symmetric and antisymmetric parts.** We write $A(\tau_2)A(\tau_1)=\tfrac12\{A(\tau_2),A(\tau_1)\}+\tfrac12[A(\tau_2),A(\tau_1)]$, so that the anticommutator carries the "commuting-approximation" content and the commutator carries the ordering defect.

3. **Reduce a matrix computation to Pauli-basis bookkeeping.** Using $\sigma_1^2=\sigma_3^2=\mathbf{1}$, $\sigma_1\sigma_3=-i\sigma_2$, $\sigma_3\sigma_1=+i\sigma_2$, every product of two elements of $\operatorname{span}\{\sigma_1,\sigma_3\}$ is expressed in the basis $\{\mathbf{1},\sigma_2\}$.

4. **Symmetrise a double integral over the ordered simplex.** The identity $\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,f(\tau_2)g(\tau_1)+\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,g(\tau_2)f(\tau_1)=\big(\int_0^t f\big)\big(\int_0^t g\big)$ converts ordered integrals of symmetric integrands into products of single integrals.

5. **Recognise the second-order Magnus term.** The residual ordered integral of the commutator is identified with the standard first correction of the Magnus expansion, giving the invariant statement of the discrepancy independent of the two-level specialisation.

6. **Read off vanishing from an explicit scalar.** The final discrepancy is a single real number $W(t)$ times $\sigma_2$; equality of ordered and unordered terms is then the arithmetic condition $W(t)=0$, tested on an explicit $(a,b)$.

---

# Hints

> [!note]- Hint 1
> Do not touch $\tfrac12(\int A)^2$ yet. Write only the second-order Dyson term $U_2(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)$ and multiply out $A(\tau_2)A(\tau_1)$ with $A=a\sigma_1+b\sigma_3$. You will meet the four products $\sigma_1\sigma_1,\ \sigma_1\sigma_3,\ \sigma_3\sigma_1,\ \sigma_3\sigma_3$; two of them are $\mathbf{1}$ and two of them are $\pm i\sigma_2$.

> [!note]- Hint 2
> Group the integrand as (symmetric in $\tau_1,\tau_2$) $+$ (antisymmetric in $\tau_1,\tau_2$). The symmetric part is the coefficient of $\mathbf{1}$, namely $a(\tau_2)a(\tau_1)+b(\tau_2)b(\tau_1)$; the antisymmetric part is the coefficient of $\sigma_2$, namely $i\big(b(\tau_2)a(\tau_1)-a(\tau_2)b(\tau_1)\big)$. Why is this split exactly the split into anticommutator and commutator of $A(\tau_2)$ and $A(\tau_1)$?

> [!note]- Hint 3
> For the identity part, use the simplex identity $\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,f(\tau_2)f(\tau_1)=\tfrac12\big(\int_0^t f\big)^2$ with $f=a$ and with $f=b$. Show this makes the $\mathbf{1}$-component of $U_2$ equal to $\tfrac12\big[(\int a)^2+(\int b)^2\big]$ — which is *exactly* the $\mathbf{1}$-component of $\tfrac12(\int A)^2$, because $(\int A)^2=(\alpha\sigma_1+\beta\sigma_3)^2=(\alpha^2+\beta^2)\mathbf{1}$ (the cross term dies since $\sigma_1,\sigma_3$ anticommute). So the discrepancy lives entirely along $\sigma_2$.

> [!note]- Hint 4
> The discrepancy is $-iW(t)\sigma_2$ with $W(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1))$. Rewrite $W$ as a single integral by carrying out the inner integration: with $\alpha(s)=\int_0^s a$ and $\beta(s)=\int_0^s b$, one gets $W(t)=\int_0^t(\dot\alpha\,\beta-\alpha\,\dot\beta)\,ds$, the signed area swept by the planar curve $s\mapsto(\alpha(s),\beta(s))$. To see it is genuinely nonzero, take $a\equiv1$, $b(s)=s$ on $[0,T]$ and compute.

---

# Solution

The plan is to expand the second-order Dyson term for the ansatz $A=a\sigma_1+b\sigma_3$, split the integrand into its symmetric and antisymmetric parts in the two integration variables, and integrate each over the ordered simplex $0\le\tau_1\le\tau_2\le t$. The symmetric part reproduces the identity-component of the naive quadratic $\tfrac12(\int A)^2$ exactly, by the simplex identity; the antisymmetric part is the ordered integral of the commutator $[A(\tau_2),A(\tau_1)]=-2i(a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1))\sigma_2$, which survives as a pure $\sigma_2$-term and is the ordering defect. A single explicit choice of $(a,b)$ then shows this term is nonzero.

Throughout we abbreviate $A_2:=A(\tau_2)$, $A_1:=A(\tau_1)$, $a_2:=a(\tau_2)$, and so on, and we write $\alpha(t):=\int_0^t a(\tau)\,d\tau$ and $\beta(t):=\int_0^t b(\tau)\,d\tau$, so that $\int_0^t A=\alpha(t)\sigma_1+\beta(t)\sigma_3$.

**Step 1: Expand the second-order integrand $A(\tau_2)A(\tau_1)$ in the Pauli basis.**

The product of two elements of $\operatorname{span}\{\sigma_1,\sigma_3\}$ decomposes into an $\mathbf{1}$-part and a $\sigma_2$-part,
$$A_2A_1=(a_2a_1+b_2b_1)\,\mathbf{1}+i\,(b_2a_1-a_2b_1)\,\sigma_2.$$

> [!note]- Derivation
> Multiply out, using bilinearity:
> $$A_2A_1=(a_2\sigma_1+b_2\sigma_3)(a_1\sigma_1+b_1\sigma_3)=a_2a_1\,\sigma_1^2+a_2b_1\,\sigma_1\sigma_3+b_2a_1\,\sigma_3\sigma_1+b_2b_1\,\sigma_3^2\qquad\text{(bilinearity of matrix product).}$$
> Insert the Pauli products from the Recall, $\sigma_1^2=\sigma_3^2=\mathbf{1}$, $\sigma_1\sigma_3=-i\sigma_2$, $\sigma_3\sigma_1=+i\sigma_2$:
> $$A_2A_1=(a_2a_1+b_2b_1)\,\mathbf{1}+a_2b_1\,(-i\sigma_2)+b_2a_1\,(+i\sigma_2)\qquad(\sigma_1^2=\sigma_3^2=\mathbf{1};\ \sigma_1\sigma_3=-i\sigma_2;\ \sigma_3\sigma_1=+i\sigma_2).$$
> Collecting the $\sigma_2$ terms, $-a_2b_1+b_2a_1=b_2a_1-a_2b_1$, gives
> $$A_2A_1=(a_2a_1+b_2b_1)\,\mathbf{1}+i\,(b_2a_1-a_2b_1)\,\sigma_2.$$
> The $\mathbf{1}$-coefficient $a_2a_1+b_2b_1$ is **symmetric** under $\tau_1\leftrightarrow\tau_2$; the $\sigma_2$-coefficient $i(b_2a_1-a_2b_1)$ is **antisymmetric**. This is no accident: the symmetric part of $A_2A_1$ is $\tfrac12\{A_2,A_1\}$ and the antisymmetric part is $\tfrac12[A_2,A_1]$, and indeed $\tfrac12[A_2,A_1]=\tfrac12(a_2b_1-b_2a_1)[\sigma_1,\sigma_3]=\tfrac12(a_2b_1-b_2a_1)(-2i\sigma_2)=i(b_2a_1-a_2b_1)\sigma_2$, matching the $\sigma_2$-term exactly.

**Step 2: Integrate the identity-part over the ordered simplex.**

The $\mathbf{1}$-component of $U_2(t)$ equals $\tfrac12\big(\alpha(t)^2+\beta(t)^2\big)$.

> [!note]- Derivation
> The $\mathbf{1}$-component of $U_2(t)$ is
> $$\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(a_2a_1+b_2b_1)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,a(\tau_2)a(\tau_1)+\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,b(\tau_2)b(\tau_1)\qquad\text{(linearity of the integral).}$$
> For the first term, carry out the inner integral with $\alpha(\tau_2)=\int_0^{\tau_2}a(\tau_1)\,d\tau_1$:
> $$\int_0^t d\tau_2\,a(\tau_2)\!\int_0^{\tau_2}\!a(\tau_1)\,d\tau_1=\int_0^t a(\tau_2)\,\alpha(\tau_2)\,d\tau_2=\int_0^t \alpha'(\tau_2)\,\alpha(\tau_2)\,d\tau_2=\tfrac12\,\alpha(t)^2\qquad(\alpha'=a\text{ by the fundamental theorem of calculus;}\ \alpha(0)=0).$$
> The last equality is $\int_0^t \tfrac{d}{d\tau_2}\big(\tfrac12\alpha(\tau_2)^2\big)\,d\tau_2=\tfrac12\alpha(t)^2-\tfrac12\alpha(0)^2=\tfrac12\alpha(t)^2$. Identically for $b$, $\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,b(\tau_2)b(\tau_1)=\tfrac12\beta(t)^2$. Hence the $\mathbf{1}$-component of $U_2(t)$ is $\tfrac12\alpha(t)^2+\tfrac12\beta(t)^2=\tfrac12\big(\alpha(t)^2+\beta(t)^2\big)$.

**Step 3: Integrate the ordering-defect part.**

The $\sigma_2$-component of $U_2(t)$ equals $-i\,W(t)$, where $W(t):=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(a_2b_1-b_2a_1)$.

> [!note]- Derivation
> From Step 1 the $\sigma_2$-coefficient of the integrand is $i(b_2a_1-a_2b_1)$, so the $\sigma_2$-component of $U_2(t)$ is
> $$i\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(b_2a_1-a_2b_1)=-\,i\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(a_2b_1-b_2a_1)=-\,i\,W(t)\qquad\text{(pulling out the sign; definition of }W).$$
> Combining Steps 2 and 3,
> $$U_2(t)=\tfrac12\big(\alpha(t)^2+\beta(t)^2\big)\,\mathbf{1}-i\,W(t)\,\sigma_2.$$

**Step 4: Compute the naive quadratic $\tfrac12\big(\int_0^t A\big)^2$.**

$\tfrac12\big(\int_0^t A\big)^2=\tfrac12\big(\alpha(t)^2+\beta(t)^2\big)\,\mathbf{1}$, a pure multiple of the identity with no $\sigma_2$-part.

> [!note]- Derivation
> With $\int_0^t A=\alpha\sigma_1+\beta\sigma_3$ (writing $\alpha=\alpha(t)$, $\beta=\beta(t)$),
> $$\Big(\int_0^t A\Big)^2=(\alpha\sigma_1+\beta\sigma_3)^2=\alpha^2\sigma_1^2+\alpha\beta(\sigma_1\sigma_3+\sigma_3\sigma_1)+\beta^2\sigma_3^2\qquad\text{(expand the square).}$$
> The cross term vanishes because $\sigma_1$ and $\sigma_3$ **anticommute**, $\sigma_1\sigma_3+\sigma_3\sigma_1=0$; and $\sigma_1^2=\sigma_3^2=\mathbf{1}$, so
> $$\Big(\int_0^t A\Big)^2=(\alpha^2+\beta^2)\,\mathbf{1},\qquad\text{hence}\qquad \tfrac12\Big(\int_0^t A\Big)^2=\tfrac12(\alpha^2+\beta^2)\,\mathbf{1}.$$
> There is no $\sigma_2$-component: the naive exponential's second-order term is blind to the ordering.

**Step 5: Subtract, and locate the discrepancy.**

Subtracting Step 4 from Step 3 gives the advertised identity, and the discrepancy is a pure $\sigma_2$-term.

> [!note]- Derivation
> The $\mathbf{1}$-components of $U_2(t)$ and of $\tfrac12(\int A)^2$ are *both* $\tfrac12(\alpha^2+\beta^2)$, so they cancel in the difference; only the $\sigma_2$-component of $U_2(t)$ survives:
> $$U_2(t)-\tfrac12\Big(\int_0^t A\Big)^2=-\,i\,W(t)\,\sigma_2,\qquad W(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,\big(a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1)\big).$$
> Equivalently, this is the second-order Magnus term $\tfrac12\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,[A_2,A_1]$, because $\tfrac12[A_2,A_1]=i(b_2a_1-a_2b_1)\sigma_2$ integrates to $-iW(t)\sigma_2$.

**Step 6: Show $W$ is generically nonzero, and pin down when it vanishes.**

Rewriting $W$ as a swept-area integral shows it does not vanish in general; an explicit choice makes it concrete.

> [!note]- Derivation
> Carry out the inner integral in $W$, using $\int_0^{\tau_2}a(\tau_1)\,d\tau_1=\alpha(\tau_2)$ and $\int_0^{\tau_2}b(\tau_1)\,d\tau_1=\beta(\tau_2)$:
> $$W(t)=\int_0^t\big(a(\tau_2)\beta(\tau_2)-b(\tau_2)\alpha(\tau_2)\big)\,d\tau_2=\int_0^t\big(\dot\alpha(s)\,\beta(s)-\alpha(s)\,\dot\beta(s)\big)\,ds\qquad(\dot\alpha=a,\ \dot\beta=b).$$
> This is (twice the signed) area swept out by the planar curve $s\mapsto(\alpha(s),\beta(s))$ starting at the origin. It is not zero unless that curve stays on a fixed line through the origin.
>
> *Explicit nonvanishing example.* Take $a(s)\equiv1$ and $b(s)=s$ on $[0,T]$. Then $\alpha(s)=s$, $\beta(s)=\tfrac12 s^2$, $\dot\alpha=1$, $\dot\beta=s$, and
> $$W(T)=\int_0^T\big(1\cdot\tfrac12 s^2-s\cdot s\big)\,ds=\int_0^T\big(-\tfrac12 s^2\big)\,ds=-\tfrac{T^3}{6}\neq0.$$
> Hence $U_2(T)-\tfrac12(\int_0^T A)^2=-i\big(-\tfrac{T^3}{6}\big)\sigma_2=\tfrac{iT^3}{6}\,\sigma_2\neq0$: the ordered and naive second-order terms genuinely differ.
>
> *When they agree.* For a fixed $t$, equality holds if and only if $W(t)=0$. They agree for **every** $t\in[0,L]$ if and only if the integrand's kernel vanishes identically, $a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1)\equiv0$ for all $\tau_1,\tau_2$, which is exactly the statement that $a$ and $b$ are linearly dependent as functions (the vector $(a(t),b(t))$ keeps a constant direction). This is the same condition as $[A(\tau_2),A(\tau_1)]\equiv0$, i.e. that $t\mapsto A(t)$ takes values in the fixed abelian line $\mathbb{R}\,(a_0\sigma_1+b_0\sigma_3)$, in which case the path-ordered exponential collapses to the ordinary exponential. The simplest instances are $a\equiv0$ (then $A=b\sigma_3$) or $b\equiv0$ (then $A=a\sigma_1$); in either case one factor of every product $a_2b_1-b_2a_1$ is zero, so $W\equiv0$.

> [!note]- Complete formal solution
> **Claim.** For $A(t)=a(t)\sigma_1+b(t)\sigma_3$ with $a,b\colon[0,L]\to\mathbb{R}$ continuous, the second-order Dyson term $U_2(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)$ satisfies
> $$U_2(t)=\tfrac12\big(\alpha(t)^2+\beta(t)^2\big)\,\mathbf{1}-i\,W(t)\,\sigma_2,\qquad U_2(t)-\tfrac12\Big(\int_0^t A\Big)^2=-\,i\,W(t)\,\sigma_2,$$
> where $\alpha(t)=\int_0^t a$, $\beta(t)=\int_0^t b$, and $W(t)=\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1))$. In particular $U_2(t)\neq\tfrac12(\int_0^t A)^2$ whenever $W(t)\neq0$.
>
> *Proof.* Write $a_i=a(\tau_i)$, $b_i=b(\tau_i)$. Expanding and using $\sigma_1^2=\sigma_3^2=\mathbf{1}$, $\sigma_1\sigma_3=-i\sigma_2$, $\sigma_3\sigma_1=+i\sigma_2$,
> $$A(\tau_2)A(\tau_1)=a_2a_1\sigma_1^2+a_2b_1\sigma_1\sigma_3+b_2a_1\sigma_3\sigma_1+b_2b_1\sigma_3^2=(a_2a_1+b_2b_1)\mathbf{1}+i(b_2a_1-a_2b_1)\sigma_2.$$
> Integrate over $0\le\tau_1\le\tau_2\le t$. For the $\mathbf{1}$-part, with $\alpha'=a$ (fundamental theorem of calculus, $\alpha(0)=0$),
> $$\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,a_2a_1=\int_0^t a(\tau_2)\alpha(\tau_2)\,d\tau_2=\tfrac12\alpha(t)^2,$$
> and likewise $\int\int b_2b_1=\tfrac12\beta(t)^2$, so the $\mathbf{1}$-component of $U_2(t)$ is $\tfrac12(\alpha(t)^2+\beta(t)^2)$. For the $\sigma_2$-part,
> $$i\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,(b_2a_1-a_2b_1)=-i\,W(t).$$
> Hence $U_2(t)=\tfrac12(\alpha(t)^2+\beta(t)^2)\mathbf{1}-iW(t)\sigma_2$.
>
> Separately, $\int_0^t A=\alpha(t)\sigma_1+\beta(t)\sigma_3$, and since $\sigma_1\sigma_3+\sigma_3\sigma_1=0$ and $\sigma_1^2=\sigma_3^2=\mathbf{1}$,
> $$\Big(\int_0^t A\Big)^2=(\alpha^2+\beta^2)\mathbf{1},\qquad \tfrac12\Big(\int_0^t A\Big)^2=\tfrac12(\alpha^2+\beta^2)\mathbf{1}.$$
> Subtracting, the identity-parts cancel and $U_2(t)-\tfrac12(\int_0^t A)^2=-iW(t)\sigma_2$.
>
> Finally, $W$ is not identically zero: for $a\equiv1$, $b(s)=s$ on $[0,T]$ one has $\alpha(s)=s$, $\beta(s)=\tfrac12 s^2$, and $W(T)=\int_0^T(\tfrac12 s^2-s^2)\,ds=-\tfrac{T^3}{6}\neq0$, so $U_2(T)-\tfrac12(\int_0^T A)^2=\tfrac{iT^3}{6}\sigma_2\neq0$. The discrepancy $-iW(t)\sigma_2$ vanishes for a given $t$ exactly when $W(t)=0$, and vanishes for all $t$ exactly when the kernel $a(\tau_2)b(\tau_1)-b(\tau_2)a(\tau_1)$ is identically zero, i.e. when $a$ and $b$ are proportional (in particular when either vanishes), which is the commuting case where the path-ordered exponential reduces to the ordinary exponential. $\blacksquare$

> [!warning] Illegal but tempting: replacing $\mathcal{P}\exp$ by $\exp(-\int A)$
> The seductive error is to solve $\dot v=-A(t)v$ by $v(t)=\exp\!\big(-\int_0^t A\big)v_0$, in analogy with the scalar equation $\dot v=-a(t)v$. This is correct to **first** order and correct to all orders only when the values $A(t)$ commute among themselves. The computation above is precisely the second-order witness to its failure: the two differ by $-iW(t)\sigma_2$, and $W$ measures the area swept by $(\alpha,\beta)$, which is nonzero as soon as $A(t)$ changes direction in the $(\sigma_1,\sigma_3)$-plane. The extra condition that would make the naive formula legal is that $[A(s),A(t)]=0$ for all $s,t$ — equivalently, that $a$ and $b$ be proportional.

> [!note]- Independent sanity check: the trace
> Every ordered product $A(\tau_2)A(\tau_1)$ has $\operatorname{tr}\big(A_2A_1\big)=2(a_2a_1+b_2b_1)$ because $\operatorname{tr}\mathbf{1}=2$ and $\operatorname{tr}\sigma_2=0$. Hence $\operatorname{tr}U_2(t)=2\cdot\tfrac12(\alpha^2+\beta^2)=\alpha^2+\beta^2$, while $\operatorname{tr}\big[\tfrac12(\int A)^2\big]=\tfrac12\cdot 2(\alpha^2+\beta^2)=\alpha^2+\beta^2$. The traces match, consistent with the discrepancy being traceless (it is a multiple of $\sigma_2$). This is a genuine check: had we mislabelled the $\mathbf{1}$-coefficient, the traces would disagree.

---

# Key Takeaways

**The ordered exponential and the ordinary exponential first part company at second order, and the gap is an integrated commutator.** The single most transferable fact here is the operator identity, valid for any continuous matrix-valued $A$,
$$\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,A(\tau_2)A(\tau_1)-\tfrac12\Big(\int_0^t A\Big)^2=\tfrac12\int_0^t d\tau_2\int_0^{\tau_2}d\tau_1\,[A(\tau_2),A(\tau_1)].$$
It says that the second-order Dyson term equals the naive quadratic *plus* a correction that is purely the ordered integral of the commutator — the second term of the Magnus expansion. The trigger for reaching for it is any time-dependent linear operator equation $\dot v=-A(t)v$ in which the $A(t)$ do not commute at different times: expanding in the small parameter (short time, weak field, high frequency) one may always use the unordered exponential through first order, but the first correction is this commutator integral. The diagnostic to remember is: *if you are ever tempted to write $\exp(-\int A)$ for a genuinely time-dependent non-commuting generator, the size of your error is set by how much $A$ rotates its direction as $t$ advances, measured by $\int[A,A]$.*

**Non-commutativity in a two-level system is one-dimensional, and it always points along the missing Pauli direction.** Because $A$ was built from $\sigma_1$ and $\sigma_3$ only, its self-products close on $\{\mathbf{1},\sigma_2\}$: the symmetric (commuting-approximation) content lands on $\mathbf{1}$ and the antisymmetric (ordering) content lands on $\sigma_2$, the one generator absent from $A$ itself. This is the general phenomenon that in $\mathfrak{su}(2)$ the commutator of two directions is the third direction, $[\sigma_j,\sigma_k]=2i\epsilon_{jk\ell}\sigma_\ell$; a field confined to a plane in the Lie algebra generates holonomy out of the plane. The reusable recognition is that whenever a generator lives in a two-dimensional subspace of $\mathfrak{su}(2)$, its ordering corrections are automatically scalar multiples of a single fixed matrix, so the entire "how much does ordering matter?" question reduces to computing one real number — here $W(t)$, the swept area of $(\int a,\int b)$.

**The vanishing locus of the correction is a geometric, not algebraic, condition: zero swept area.** The correction $-iW(t)\sigma_2$ is zero for a fixed endpoint precisely when the planar curve $s\mapsto\big(\int_0^s a,\int_0^s b\big)$ encloses zero signed area up to time $t$, and zero for all endpoints precisely when that curve is a straight ray, i.e. when $a\propto b$. This is why "$a$ or $b$ vanishes" is only the *simplest* sufficient condition and not the full story: constant nonzero $a,b$ also give a straight ray and hence no ordering defect, whereas an $(a,b)$ that changes direction always produces one. The transferable principle is that the commuting case is exactly the case of a constant-direction generator, and the failure of commutativity is quantitatively the geometry (enclosed area) of the trajectory the generator traces in its Lie algebra. This same picture governs the small-loop holonomy expansion — where the curvature appears as the area-density of the ordering defect — treated in [[Thm - Curvature is the Infinitesimal Holonomy|the infinitesimal-holonomy theorem]] and drilled in [[Ex - Second-Order Holonomy Expansion for a Small Square in the Plane]].
