---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Chern-Simons Functional"
  - "Thm - Critical Points of the Chern-Simons Functional are the Flat Connections"
  - "Def - Flat Connection"
  - "Thm - Structure Equation for the Curvature"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M=T^3=\mathbb R^3/(2\pi\mathbb Z)^3$ be the flat three-torus, with global angular coordinates $x^1,x^2,x^3$ and the globally defined closed one-forms $dx^1,dx^2,dx^3$; the flat volume form is $dx^1\wedge dx^2\wedge dx^3$ and $\operatorname{vol}(T^3)=\int_{T^3}dx^1\wedge dx^2\wedge dx^3=(2\pi)^3$. Every principal $SU(2)$-bundle over a three-manifold is trivial, so fix the trivialisation $P=T^3\times SU(2)$ and identify a connection with its gauge potential $A\in\Omega^1(T^3;\mathfrak{su}(2))$. For fixed matrices $a_1,a_2,a_3\in\mathfrak{su}(2)$ consider the **constant connection**
$$A=\sum_{j=1}^{3}a_j\,dx^j\in\Omega^1(T^3;\mathfrak{su}(2)),$$
whose coefficient matrices do not depend on the point of $T^3$. Prove the following.

1. **(Curvature.)** The curvature is $F_A=\sum_{1\le j<k\le3}[a_j,a_k]\,dx^j\wedge dx^k$; hence $A$ is flat if and only if the $a_j$ pairwise commute, in which case they span (at most) a one-dimensional abelian subalgebra of $\mathfrak{su}(2)$ — a Cartan subalgebra, or maximal torus at the Lie-algebra level.
2. **(Commuting case.)** If the $a_j$ pairwise commute, then $F_A=0$ and $\vartheta(A)=0$.
3. **(Non-commuting case.)** If the $a_j$ do not pairwise commute, then $A$ is not flat, and, since $dA=0$ makes only the cubic term of the Chern–Simons form survive, $\operatorname{tr}(A\wedge A\wedge A)=3\operatorname{tr}(a_1[a_2,a_3])\,dx^1\wedge dx^2\wedge dx^3$, so
$$\vartheta(A)=\frac{2\operatorname{tr}\!\big(a_1[a_2,a_3]\big)}{8\pi^2}\,\operatorname{vol}(T^3)=\frac{\operatorname{tr}\!\big(a_1[a_2,a_3]\big)}{4\pi^2}\,\operatorname{vol}(T^3)\quad\in\ \mathbb R/\mathbb Z.$$
Evaluate this in the concrete case $a_j=-\tfrac i2\sigma_j$ (the standard generators, $\sigma_j$ the Pauli matrices).

**Recall:**

The objects in play are the Chern–Simons functional in a trivialisation, the local curvature of a connection, a flat connection, and the structure of $\mathfrak{su}(2)$.

![[Def - Chern-Simons Functional#The Definition]]

In the trivialisation, a connection on $P\to M^3$ is $A\in\Omega^1(M;\mathfrak{su}(2))$, the [[Def - Chern-Simons Functional|Chern–Simons three-form]] is $\operatorname{cs}(A)=\operatorname{tr}\!\big(A\wedge dA+\tfrac23A\wedge A\wedge A\big)\in\Omega^3(M)$, and the [[Def - Chern-Simons Functional|Chern–Simons functional]] is $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)\in\mathbb R/\mathbb Z$; the real number is trivialisation-dependent, its class modulo $\mathbb Z$ is not. Here $\operatorname{tr}$ is the matrix trace in the defining representation of $\mathfrak{su}(2)\subset\mathfrak{gl}_2(\mathbb C)$.

![[Thm - Structure Equation for the Curvature#Statement]]

In a trivialisation, the [[Thm - Structure Equation for the Curvature|structure equation]] $F_A=dA+\tfrac12[A\wedge A]$ becomes $F_A=dA+A\wedge A$ for a matrix Lie algebra, because $\tfrac12[A\wedge A]=A\wedge A$ for the commutator bracket of one-forms. A connection is [[Def - Flat Connection|flat]] when its curvature vanishes, $F_A=0$.

![[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections#Statement]]

By the [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|critical-point theorem]], the flat connections are exactly the critical points of $\vartheta$; the flat constant connections found in part 1 are therefore critical points, and — as in [[Ex - Flat U(1)-Connections on the Torus|the flat U(1)-connections on the torus]] — they realise the abelian points of the representation variety of $\pi_1(T^3)=\mathbb Z^3$.

The two Lie-algebra facts used are: the entries of $\mathfrak{su}(2)$ are the trace-free anti-Hermitian $2\times2$ matrices, so the Pauli matrices $\sigma_j$ (Hermitian, $\sigma_j^2=I$, $\operatorname{tr}\sigma_j=0$) give the basis $-\tfrac i2\sigma_1,-\tfrac i2\sigma_2,-\tfrac i2\sigma_3$ of $\mathfrak{su}(2)$; and the commutation relations $\sigma_j\sigma_k=\delta_{jk}I+i\sum_l\varepsilon_{jkl}\sigma_l$, where $\varepsilon_{jkl}$ is the totally antisymmetric symbol with $\varepsilon_{123}=1$.

---

# Convergent Strategy

**Problem class.** This is an *explicit-evaluation* problem: a distinguished family of connections is presented, and both a topological/differential quantity (the curvature, hence flatness) and a numerical invariant (the Chern–Simons functional) are to be computed in closed form. It belongs to the class of "test the functional on the simplest connections" exercises, whose purpose is to turn the abstract definition of $\vartheta$ into a formula one can compute by hand and to exhibit both a family on which it vanishes (the flat connections) and a family on which it does not. The special structure that makes the class tractable is that the coefficients are *constant*, so $dA=0$ and the entire functional reduces to a single algebraic trace.

**Assumption pattern.** The decisive simplification is constancy of the $a_j$: it forces $dA=0$, which does two things at once — it makes the curvature purely quadratic, $F_A=A\wedge A$, and it makes the Chern–Simons form purely cubic, $\operatorname{cs}(A)=\tfrac23\operatorname{tr}(A^{\wedge3})$. Recognise the pattern: whenever a connection is written with covariantly constant or literally constant coefficients on a parallelisable manifold (a torus, a Lie group), the exterior-derivative terms drop and every curvature or Chern–Simons computation collapses to Lie-algebra bracket and trace arithmetic. The three-torus is the cleanest such manifold because its coordinate one-forms are globally defined and closed.

**Theorem routing.** The route is: compute $dA=0$ from constancy; compute $A\wedge A$ and read off $F_A=\sum_{j<k}[a_j,a_k]dx^j\wedge dx^k$, using the [[Thm - Structure Equation for the Curvature|structure equation]]; deduce flatness $\iff$ all brackets vanish $\iff$ commuting, from linear independence of the two-forms $dx^j\wedge dx^k$. For the functional, insert $dA=0$ into $\operatorname{cs}(A)$ from [[Def - Chern-Simons Functional|the definition]], compute the single surviving cubic trace via the antisymmetry of the wedge and the cyclicity of the matrix trace, and integrate the constant top-form over $T^3$. The [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|critical-point theorem]] then labels the commuting family as critical points, and the vanishing $\vartheta=0$ there is consistent with (though stronger than) criticality.

**Key decision point.** The one genuine computation is the cubic trace $\operatorname{tr}(A\wedge A\wedge A)$, and the decision is *whether to expand it as an unordered sum over all index triples or to build it as $(A\wedge A)\wedge A$ and keep only the $\{1,2,3\}$ triples with $j<k$*. The second route is far shorter: $A\wedge A=\sum_{j<k}[a_j,a_k]dx^{jk}$ is already known from the curvature computation, so wedging with $A=\sum_l a_l dx^l$ leaves exactly three surviving terms, one for each way of choosing the missing index. The subtlety that must not be skipped is the reduction of the three trace terms $\operatorname{tr}([a_1,a_2]a_3)$, $\operatorname{tr}([a_1,a_3]a_2)$, $\operatorname{tr}([a_2,a_3]a_1)$ to the single expression $\operatorname{tr}(a_1[a_2,a_3])$ by cyclicity of the matrix trace; getting the middle sign right (it carries a minus from $dx^{132}=-dx^{123}$) is what produces the clean factor $3$ rather than an accidental cancellation.

---

# Legal Operations Used

The topic page for this chapter organises these under its Legal Operations; until it is written they are named descriptively.

1. **Kill exterior-derivative terms using constancy of the coefficients.** Because each $a_j$ is a constant matrix, $da_j=0$ and $d(dx^j)=0$, so $dA=\sum_j da_j\wedge dx^j=0$. This is the operation of exploiting a parallelisation to reduce a differential expression to an algebraic one.

2. **Compute the local curvature from the structure equation.** Apply $F_A=dA+A\wedge A$ (the matrix-group form of the [[Thm - Structure Equation for the Curvature|structure equation]]) and antisymmetrise the double sum into commutators.

3. **Detect flatness from the linear independence of the curvature basis.** Read $F_A=0\iff[a_j,a_k]=0$ off the independence of the two-forms $dx^j\wedge dx^k$ over $C^\infty(T^3)$.

4. **Reduce a Lie-algebra trace by cyclicity of the matrix trace.** Use $\operatorname{tr}(MN)=\operatorname{tr}(NM)$ to collapse $\operatorname{tr}([a_i,a_j]a_k)$-type expressions to a single $\operatorname{tr}(a_1[a_2,a_3])$.

5. **Integrate a constant top-form over the torus.** Since the surviving integrand is $(\text{constant})\cdot dx^1\wedge dx^2\wedge dx^3$, the integral is that constant times $\operatorname{vol}(T^3)=(2\pi)^3$.

---

# Hints

> [!note]- Hint 1
> The coefficient matrices are *constant*. What does that immediately say about $dA$? Once you know $dA$, the structure equation $F_A=dA+A\wedge A$ has only one surviving term.

> [!note]- Hint 2
> Compute $A\wedge A=\sum_{j,k}a_ja_k\,dx^j\wedge dx^k$ and group the terms with $j<k$, using $dx^k\wedge dx^j=-dx^j\wedge dx^k$. The matrix coefficient of $dx^j\wedge dx^k$ becomes $a_ja_k-a_ka_j=[a_j,a_k]$. The two-forms $dx^j\wedge dx^k$ ($j<k$) are linearly independent, so $F_A=0$ if and only if every bracket vanishes.

> [!note]- Hint 3
> For the functional, $dA=0$ makes $A\wedge dA=0$, so $\operatorname{cs}(A)=\tfrac23\operatorname{tr}(A\wedge A\wedge A)$. You already have $A\wedge A=\sum_{j<k}[a_j,a_k]dx^{jk}$; wedge it with $A=\sum_l a_l\,dx^l$ and keep only the terms where $\{j,k,l\}=\{1,2,3\}$. There are exactly three, from $(j,k,l)=(1,2,3),(1,3,2),(2,3,1)$, and $dx^{132}=-dx^{123}$, $dx^{231}=+dx^{123}$.

> [!note]- Hint 4
> After taking the trace, cyclicity of the matrix trace ($\operatorname{tr}(a_ia_ja_k)=\operatorname{tr}(a_ja_ka_i)$) collapses the three terms to $3\operatorname{tr}(a_1[a_2,a_3])$. Then $\vartheta(A)=\tfrac1{8\pi^2}\cdot\tfrac23\cdot 3\operatorname{tr}(a_1[a_2,a_3])\cdot\operatorname{vol}(T^3)$. For the concrete case, use $[-\tfrac i2\sigma_2,-\tfrac i2\sigma_3]=-\tfrac i2\sigma_1$ and $\operatorname{tr}\big((-\tfrac i2\sigma_1)^2\big)=\operatorname{tr}(-\tfrac14 I)=-\tfrac12$.

---

# Solution

The computation has two halves. The curvature half puts $dA=0$ into $F_A=dA+A\wedge A$, computes $A\wedge A=\sum_{j<k}[a_j,a_k]dx^{jk}$, and reads off flatness $\iff$ commuting. The functional half puts $dA=0$ into $\operatorname{cs}(A)$, so only the cubic term survives, computes the single trace $\operatorname{tr}(A^{\wedge3})=3\operatorname{tr}(a_1[a_2,a_3])dx^{123}$, and integrates over $T^3$. The commuting case then gives $\vartheta=0$ (the bracket vanishes), and the non-commuting case gives the stated closed form.

**Step 1: The connection has vanishing exterior derivative.**

Because the coefficient matrices are constant, $dA=0$.

> [!note]- Derivation
> Each $a_j\in\mathfrak{su}(2)$ is a fixed matrix, so its entries are constant functions on $T^3$ and $da_j=0$; the coordinate one-forms are closed, $d(dx^j)=0$. By the Leibniz rule applied entrywise,
> $$dA=\sum_{j=1}^{3}d\big(a_j\,dx^j\big)=\sum_{j=1}^{3}\Big(da_j\wedge dx^j+a_j\,d(dx^j)\Big)=0\qquad\text{(}da_j=0\text{, }d(dx^j)=0\text{)}.$$
> Thus the differential part of both the curvature and the Chern–Simons form drops out.

**Step 2: The curvature is $F_A=\sum_{j<k}[a_j,a_k]\,dx^j\wedge dx^k$.**

With $dA=0$, the structure equation leaves $F_A=A\wedge A$, which antisymmetrises into commutators.

> [!note]- Derivation
> In a trivialisation the [[Thm - Structure Equation for the Curvature|structure equation]] reads $F_A=dA+\tfrac12[A\wedge A]$, and for the matrix commutator bracket of one-forms $\tfrac12[A\wedge A]=A\wedge A$; with Step 1,
> $$F_A=dA+A\wedge A=A\wedge A\qquad\text{(Step 1, }dA=0\text{)}.$$
> Now expand, remembering that the product of matrix-valued forms multiplies the matrices and wedges the form parts:
> $$A\wedge A=\Big(\sum_j a_j\,dx^j\Big)\wedge\Big(\sum_k a_k\,dx^k\Big)=\sum_{j,k}a_ja_k\,dx^j\wedge dx^k\qquad\text{(bilinearity of the product)}.$$
> Split the double sum into $j<k$, $j>k$, and $j=k$. The diagonal $j=k$ contributes $a_j^2\,dx^j\wedge dx^j=0$ since $dx^j\wedge dx^j=0$. For the off-diagonal part, relabel the $j>k$ terms and use $dx^k\wedge dx^j=-dx^j\wedge dx^k$:
> $$A\wedge A=\sum_{j<k}\big(a_ja_k\,dx^j\wedge dx^k+a_ka_j\,dx^k\wedge dx^j\big)=\sum_{j<k}\big(a_ja_k-a_ka_j\big)\,dx^j\wedge dx^k=\sum_{j<k}[a_j,a_k]\,dx^j\wedge dx^k.$$
> Hence $F_A=\sum_{1\le j<k\le3}[a_j,a_k]\,dx^j\wedge dx^k$, as claimed.

**Step 3: Flatness holds if and only if the $a_j$ pairwise commute, and then they span a Cartan subalgebra.**

> [!note]- Derivation
> The three two-forms $dx^1\wedge dx^2$, $dx^1\wedge dx^3$, $dx^2\wedge dx^3$ are linearly independent over $C^\infty(T^3)$ (they are distinct basis elements of $\Lambda^2$ at each point). Therefore the $\mathfrak{su}(2)$-valued two-form $F_A=\sum_{j<k}[a_j,a_k]dx^j\wedge dx^k$ vanishes if and only if each coefficient vanishes:
> $$F_A=0\iff[a_1,a_2]=[a_1,a_3]=[a_2,a_3]=0\iff\text{the }a_j\text{ pairwise commute.}$$
> Suppose the $a_j$ pairwise commute and are not all zero; say $a_1\ne0$. In $\mathfrak{su}(2)$ the centraliser of a non-zero element is the line through it: $\mathfrak{su}(2)$ is three-dimensional with $[\,\cdot\,,\cdot\,]$ isomorphic to the cross product on $\mathbb R^3$ (identify $-\tfrac i2\sigma_j\leftrightarrow e_j$, so $[-\tfrac i2\sigma_j,-\tfrac i2\sigma_k]=-\tfrac i2\sum_l\varepsilon_{jkl}\sigma_l\leftrightarrow e_j\times e_k$), and the cross product $v\times w=0$ with $v\ne0$ forces $w\in\mathbb R v$. Hence $[a_1,a_2]=0$ gives $a_2\in\mathbb R a_1$ and $[a_1,a_3]=0$ gives $a_3\in\mathbb R a_1$, so all three lie in the one-dimensional subspace $\mathbb R a_1$. A one-dimensional subspace of $\mathfrak{su}(2)$ is a maximal abelian subalgebra, that is, a Cartan subalgebra — the Lie-algebra of a maximal torus $U(1)\subset SU(2)$. This is the sense in which the commuting constant connections "live in a maximal torus".

**Step 4: The commuting case gives $\vartheta(A)=0$.**

> [!note]- Derivation
> By the [[Def - Chern-Simons Functional|definition]] and Step 1 ($dA=0$, so $A\wedge dA=0$),
> $$\operatorname{cs}(A)=\operatorname{tr}\!\big(A\wedge dA+\tfrac23A\wedge A\wedge A\big)=\tfrac23\operatorname{tr}(A\wedge A\wedge A).$$
> When the $a_j$ pairwise commute, Step 2 gives $A\wedge A=\sum_{j<k}[a_j,a_k]dx^{jk}=0$, hence $A\wedge A\wedge A=0$ and $\operatorname{cs}(A)=0$. Therefore
> $$\vartheta(A)=\frac1{8\pi^2}\int_{T^3}\operatorname{cs}(A)=0\qquad\text{(commuting case)}.$$
> Consistency check: these $A$ are flat by Step 3, so by the [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|critical-point theorem]] they are critical points of $\vartheta$; the value $0$ is the value $\vartheta$ takes on the trivial connection $A=0$ (also flat), and every flat constant connection here is gauge-connected to it within the maximal torus, so it is unsurprising that the invariant is $0$ rather than merely critical.

**Step 5: The cubic term of the Chern–Simons form for a constant connection.**

For any constant $A$ (commuting or not), $\operatorname{tr}(A\wedge A\wedge A)=3\operatorname{tr}(a_1[a_2,a_3])\,dx^1\wedge dx^2\wedge dx^3$.

> [!note]- Derivation
> From Step 2, $A\wedge A=\sum_{j<k}[a_j,a_k]dx^{jk}$. Wedge on the right with $A=\sum_l a_l\,dx^l$; a term survives only when $\{j,k,l\}=\{1,2,3\}$, since otherwise a coordinate one-form repeats and the three-fold wedge vanishes. Writing $dx^{jkl}:=dx^j\wedge dx^k\wedge dx^l$, the three surviving triples are $(j,k,l)=(1,2,3),(1,3,2),(2,3,1)$:
> $$A\wedge A\wedge A=[a_1,a_2]a_3\,dx^{123}+[a_1,a_3]a_2\,dx^{132}+[a_2,a_3]a_1\,dx^{231}.$$
> Reorder the volume forms: $dx^{132}=-dx^{123}$ (one transposition) and $dx^{231}=+dx^{123}$ (an even, cyclic permutation), giving
> $$A\wedge A\wedge A=\big([a_1,a_2]a_3-[a_1,a_3]a_2+[a_2,a_3]a_1\big)\,dx^{123}.$$
> Take the matrix trace of the bracketed matrix and reduce each term by cyclicity $\operatorname{tr}(MN)=\operatorname{tr}(NM)$ of the matrix trace [[Def - Trace|trace]]:
> $$\operatorname{tr}([a_1,a_2]a_3)=\operatorname{tr}(a_1a_2a_3)-\operatorname{tr}(a_2a_1a_3)=\operatorname{tr}(a_1a_2a_3)-\operatorname{tr}(a_1a_3a_2)=\operatorname{tr}(a_1[a_2,a_3])\qquad(\operatorname{tr}(a_2a_1a_3)=\operatorname{tr}(a_1a_3a_2)),$$
> $$\operatorname{tr}([a_2,a_3]a_1)=\operatorname{tr}(a_1[a_2,a_3])\qquad(\text{cyclicity: }\operatorname{tr}([a_2,a_3]a_1)=\operatorname{tr}(a_1[a_2,a_3])),$$
> $$\operatorname{tr}([a_1,a_3]a_2)=\operatorname{tr}(a_1a_3a_2)-\operatorname{tr}(a_3a_1a_2)=\operatorname{tr}(a_1a_3a_2)-\operatorname{tr}(a_1a_2a_3)=-\operatorname{tr}(a_1[a_2,a_3])\qquad(\operatorname{tr}(a_3a_1a_2)=\operatorname{tr}(a_1a_2a_3)).$$
> Substituting, with the middle term carrying a minus sign from $dx^{132}=-dx^{123}$,
> $$\operatorname{tr}(A\wedge A\wedge A)=\Big(\operatorname{tr}(a_1[a_2,a_3])-\big(-\operatorname{tr}(a_1[a_2,a_3])\big)+\operatorname{tr}(a_1[a_2,a_3])\Big)dx^{123}=3\operatorname{tr}\!\big(a_1[a_2,a_3]\big)\,dx^{123}.$$
> The "fixed multiple" requested in the problem is therefore $3$.

**Step 6: The functional in the non-commuting case, and the concrete evaluation.**

> [!note]- Derivation
> If the $a_j$ do not pairwise commute, then some $[a_j,a_k]\ne0$, and by Step 2 (linear independence of the $dx^{jk}$) the curvature $F_A\ne0$, so $A$ is not flat. For the functional, combine Step 4's reduction $\operatorname{cs}(A)=\tfrac23\operatorname{tr}(A^{\wedge3})$ with Step 5:
> $$\operatorname{cs}(A)=\tfrac23\cdot 3\operatorname{tr}\!\big(a_1[a_2,a_3]\big)\,dx^{123}=2\operatorname{tr}\!\big(a_1[a_2,a_3]\big)\,dx^{123}.$$
> The coefficient $2\operatorname{tr}(a_1[a_2,a_3])$ is a constant, so integrating over $T^3$ multiplies it by $\operatorname{vol}(T^3)$:
> $$\vartheta(A)=\frac1{8\pi^2}\int_{T^3}\operatorname{cs}(A)=\frac{2\operatorname{tr}\!\big(a_1[a_2,a_3]\big)}{8\pi^2}\,\operatorname{vol}(T^3)=\frac{\operatorname{tr}\!\big(a_1[a_2,a_3]\big)}{4\pi^2}\,\operatorname{vol}(T^3)\quad\in\ \mathbb R/\mathbb Z.$$
> (In the commuting case $[a_2,a_3]=0$ and this reduces to $\vartheta=0$, recovering Step 4.)
>
> **Concrete case $a_j=-\tfrac i2\sigma_j$.** Using $\sigma_2\sigma_3=i\sigma_1$ and $\sigma_3\sigma_2=-i\sigma_1$, the bracket is
> $$[a_2,a_3]=\Big[-\tfrac i2\sigma_2,-\tfrac i2\sigma_3\Big]=-\tfrac14[\sigma_2,\sigma_3]=-\tfrac14\cdot 2i\sigma_1=-\tfrac i2\sigma_1=a_1.$$
> Then $a_1[a_2,a_3]=a_1^2=\big(-\tfrac i2\sigma_1\big)^2=-\tfrac14\sigma_1^2=-\tfrac14 I$, whose trace is $\operatorname{tr}(-\tfrac14 I)=-\tfrac14\cdot 2=-\tfrac12$. Therefore
> $$\operatorname{tr}\!\big(a_1[a_2,a_3]\big)=-\tfrac12,\qquad \vartheta(A)=\frac{-\tfrac12}{4\pi^2}\,\operatorname{vol}(T^3)=\frac{-\tfrac12\cdot(2\pi)^3}{4\pi^2}=\frac{-4\pi^3}{4\pi^2}=-\pi\quad\in\ \mathbb R/\mathbb Z.$$
> The real number $-\pi$ is trivialisation-dependent; its class $-\pi\bmod\mathbb Z\approx0.8584$ is the well-defined Chern–Simons invariant of this connection, an irrational point of the circle, in visible contrast to the flat connections of Step 4, whose invariant is $0$.

> [!note]- Complete formal solution
> **Claim.** For the constant connection $A=\sum_j a_j\,dx^j$ on $T^3\times SU(2)$ with $a_j\in\mathfrak{su}(2)$: (1) $F_A=\sum_{j<k}[a_j,a_k]dx^j\wedge dx^k$, and $A$ is flat iff the $a_j$ pairwise commute; (2) commuting $\Rightarrow\vartheta(A)=0$; (3) otherwise $A$ is not flat and $\vartheta(A)=\tfrac{\operatorname{tr}(a_1[a_2,a_3])}{4\pi^2}\operatorname{vol}(T^3)$.
>
> Since each $a_j$ is constant and each $dx^j$ closed, $dA=\sum_j da_j\wedge dx^j=0$. By the structure equation for a matrix group, $F_A=dA+A\wedge A=A\wedge A$. Expanding, $A\wedge A=\sum_{j,k}a_ja_k\,dx^j\wedge dx^k=\sum_{j<k}[a_j,a_k]\,dx^j\wedge dx^k$ (diagonal terms vanish; off-diagonal terms pair up via $dx^k\wedge dx^j=-dx^j\wedge dx^k$). As the two-forms $dx^j\wedge dx^k$ ($j<k$) are linearly independent, $F_A=0$ iff every $[a_j,a_k]=0$, i.e. iff the $a_j$ pairwise commute; and commuting non-zero elements of $\mathfrak{su}(2)\cong(\mathbb R^3,\times)$ are collinear, so they span at most a one-dimensional (Cartan) subalgebra. This proves (1).
>
> With $dA=0$, $\operatorname{cs}(A)=\operatorname{tr}(A\wedge dA+\tfrac23A^{\wedge3})=\tfrac23\operatorname{tr}(A^{\wedge3})$. Computing $A^{\wedge3}=(A\wedge A)\wedge A$ and keeping the $\{1,2,3\}$-triples,
> $$A^{\wedge3}=\big([a_1,a_2]a_3-[a_1,a_3]a_2+[a_2,a_3]a_1\big)\,dx^{123},$$
> using $dx^{132}=-dx^{123}$, $dx^{231}=+dx^{123}$. Taking the trace and reducing each summand by matrix cyclicity gives $\operatorname{tr}([a_1,a_2]a_3)=\operatorname{tr}(a_1[a_2,a_3])$, $\operatorname{tr}([a_1,a_3]a_2)=-\operatorname{tr}(a_1[a_2,a_3])$, $\operatorname{tr}([a_2,a_3]a_1)=\operatorname{tr}(a_1[a_2,a_3])$, so $\operatorname{tr}(A^{\wedge3})=3\operatorname{tr}(a_1[a_2,a_3])\,dx^{123}$ and $\operatorname{cs}(A)=2\operatorname{tr}(a_1[a_2,a_3])\,dx^{123}$. Integrating the constant coefficient over $T^3$,
> $$\vartheta(A)=\frac1{8\pi^2}\int_{T^3}\operatorname{cs}(A)=\frac{2\operatorname{tr}(a_1[a_2,a_3])}{8\pi^2}\operatorname{vol}(T^3)=\frac{\operatorname{tr}(a_1[a_2,a_3])}{4\pi^2}\operatorname{vol}(T^3).$$
> If the $a_j$ commute, $[a_2,a_3]=0$ and $\vartheta(A)=0$, which is (2). Otherwise some bracket is non-zero, so $F_A\ne0$ ($A$ not flat), and the displayed formula is (3). In the concrete case $a_j=-\tfrac i2\sigma_j$: $[a_2,a_3]=a_1$, $\operatorname{tr}(a_1^2)=\operatorname{tr}(-\tfrac14 I)=-\tfrac12$, and with $\operatorname{vol}(T^3)=(2\pi)^3$ one gets $\vartheta(A)=-\pi\in\mathbb R/\mathbb Z$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to argue "$\operatorname{tr}(A\wedge A\wedge A)=0$ because $\operatorname{tr}$ of a commutator vanishes, and $A\wedge A$ is built from commutators". This is false, and the reason is instructive: $\operatorname{tr}(A^{\wedge3})$ is a trace of a *product of three* matrix-valued forms, not a trace of a single commutator. It is true that $\operatorname{tr}([a_j,a_k])=0$, but the surviving quantity is $\operatorname{tr}(a_1[a_2,a_3])$, the trace of a matrix times a commutator, which is generically non-zero (it is, up to a factor, the Killing-type invariant that detects the non-abelian structure). The vanishing $\operatorname{tr}(A^{\wedge4})=0$ that holds for the four-form (by the graded-cyclicity argument of [[Ex - The Chern-Simons Form Transgresses the Second Chern Form|the transgression exercise]]) has *no* analogue for the three-form on a three-manifold; conflating the two is the standard error here.

---

# Key Takeaways

**Constant connections on a torus turn Chern–Simons theory into finite-dimensional Lie-algebra arithmetic, and the invariant they carry is the single cubic trace $\operatorname{tr}(a_1[a_2,a_3])$.** The reusable principle is that on a parallelisable manifold — a torus, or any Lie group — a connection written with constant coefficients has $dA=0$, so its curvature is the purely algebraic $A\wedge A$ and its Chern–Simons form is the purely algebraic $\tfrac23\operatorname{tr}(A^{\wedge3})$. Every question about such a connection (is it flat? what is its energy? what is its Chern–Simons invariant?) reduces to brackets and traces of the coefficient matrices, with no differential geometry left. The trigger for this reduction is the phrase "constant/invariant connection on a torus or group manifold"; the payoff is that the infinite-dimensional functional $\vartheta$ becomes the explicit function $(a_1,a_2,a_3)\mapsto\tfrac{\operatorname{tr}(a_1[a_2,a_3])}{4\pi^2}\operatorname{vol}(T^3)$ of nine real parameters, whose zero set (the commuting triples) is exactly the flat locus.

**Flatness of a constant connection is the commutativity of its holonomy generators, and this is the differential-geometric face of the representation variety.** The condition $F_A=0\iff[a_j,a_k]=0$ is not an accident of the torus; it says that the holonomies around the three generating loops of $\pi_1(T^3)=\mathbb Z^3$ must commute, because $\pi_1(T^3)$ is abelian and a flat connection is a homomorphism $\pi_1(T^3)\to SU(2)$. The commuting constant connections thus enumerate the abelian representations, which — as in [[Ex - Flat U(1)-Connections on the Torus|the flat U(1)-connections on the torus]] — factor through a maximal torus $U(1)\subset SU(2)$ and form the bulk of the moduli space of flat connections. The transferable diagnostic: whenever a flatness computation on a manifold with abelian fundamental group reduces to "the coefficient matrices commute", one is looking at the representation variety $\operatorname{Hom}(\pi_1,G)/G$ through the lens of connections, and the maximal-torus reduction is the statement that commuting elements of a compact group are simultaneously conjugate into a maximal torus.

**The Chern–Simons invariant separates the flat connections (value $0$) from the non-flat ones (a genuine number), which is why it is a useful function on the space of connections rather than a topological constant.** In this family the invariant is $0$ exactly on the flat/commuting locus and a non-trivial real number modulo $\mathbb Z$ off it — an irrational $-\pi\bmod\mathbb Z$ in the standard-generator case. This is the concrete manifestation of the [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|critical-point theorem]]: the flat connections are the critical points of $\vartheta$, so $\vartheta$ is "flat to first order" there, and here it in fact attains the base value $0$. The lesson to carry forward is that $\vartheta$ is a *secondary* invariant: unlike the second Chern number, which is an integer determined by the bundle alone, $\vartheta$ depends on the actual connection and takes a continuum of values, so it can distinguish connections that share the same underlying topology — precisely what is needed for it to serve as the action of three-dimensional gauge theory and, after refinement, as the grading of instanton Floer homology. The companion drills are [[Ex - The Chern-Simons Form Transgresses the Second Chern Form]], which supplies the transgression identity underlying the very definition of $\vartheta$, and [[Ex - The Differential of the Chern-Simons Functional]], which computes the first variation whose vanishing is flatness.
