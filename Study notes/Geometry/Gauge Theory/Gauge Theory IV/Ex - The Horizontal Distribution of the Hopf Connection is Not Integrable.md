---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Thm - The Frobenius Theorem"
  - "Def - Involutive Distribution"
  - "Def - Distribution on a Manifold"
tags: [geometry, gauge-theory]
---

# Problem Statement

Consider the Hopf bundle in its lowest-dimensional case, $\pi\colon S^3\to\mathbb{CP}^1\cong S^2$, where
$$S^3=\{x=(x_0,x_1,x_2,x_3)\in\mathbb R^4:|x|^2=x_0^2+x_1^2+x_2^2+x_3^2=1\},$$
and $U(1)$ acts diagonally on $S^3\subset\mathbb C^2$ by $z\mapsto e^{i\vartheta}z$, with complex coordinates $z_0=x_0+ix_1$, $z_1=x_2+ix_3$. Equip $S^3$ with the round metric induced from $\mathbb R^4$, with real inner product $\langle\cdot,\cdot\rangle$. Let $a\in\Omega^1(S^3;\mathfrak u(1))$, $\mathfrak u(1)=i\mathbb R$, be the standard Hopf connection
$$a_x(u)=\langle v(x),u\rangle\,i,\qquad u\in T_xS^3,\quad v(x)=ix,$$
where $v$ is the fundamental vector field of the generator $i\in\mathfrak u(1)$. Its horizontal distribution is $H=\ker a$, a rank-$2$ distribution on $S^3$.

Following Haydys, introduce the three globally defined vector fields on $S^3$ (Haydys's Example 51 frame)
$$v_1:=(-x_1,\,x_0,\,-x_3,\,x_2),\qquad v_2:=(-x_2,\,x_3,\,x_0,\,-x_1),\qquad v_3:=(-x_3,\,-x_2,\,x_1,\,x_0),$$
each viewed as the restriction to $S^3$ of a linear vector field on $\mathbb R^4$; note $v_1=v$ is the fundamental field of Example 42.

**Prove the following.**

1. At every $x\in S^3$ the triple $(v_1,v_2,v_3)$ is an orthonormal basis of $T_xS^3$; consequently $v_2,v_3$ are horizontal ($a(v_2)=a(v_3)=0$) and $v_1$ is vertical.
2. The Lie bracket of the two horizontal fields is
$$[v_2,v_3]=-2\,v_1,$$
which is a nonzero *vertical* field.
3. Hence $H$ is **not involutive**, and therefore, by the **Frobenius theorem**, $H$ is **not integrable**: there is no surface through a point of $S^3$ tangent to $H$ everywhere.
4. Interpret the failure through the curvature: the vertical part of $[v_2,v_3]$ is precisely (minus) the value of the curvature, $\Omega(v_2,v_3)=-a([v_2,v_3])=2i\neq0$, so the obstruction to integrability *is* the nonvanishing of the curvature (a fact made general in §4.3).

**Recall:**

The objects in play are the standard Hopf connection and its horizontal distribution, involutivity of a distribution, and the Frobenius theorem equating involutivity with integrability.

![[Thm - The Standard Connection on the Hopf Bundle#Statement]]

We use the theorem **[[Thm - The Standard Connection on the Hopf Bundle]]**: on $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ with $\mathfrak u(1)=i\mathbb R$ and $v(x)=ix$, the $1$-form $a_x(u)=\langle v(x),u\rangle\,i$ is the unique connection whose horizontal distribution is $H=\ker a=v^\perp$; explicitly $H_x=\{u\in T_xS^{2n+1}:\langle v(x),u\rangle=0\}$.

![[Def - Distribution on a Manifold#The Definition]]

A **distribution** $H$ of rank $k$ on a manifold $N$ assigns to each point $x$ a $k$-dimensional subspace $H_x\subseteq T_xN$, smoothly: locally there is a smooth frame $(w_1,\dots,w_k)$ of vector fields spanning $H_x$ at each point. A vector field $W$ is a **(local) section** of $H$ if $W_x\in H_x$ for every $x$; we write $W\in\Gamma(H)$.

![[Def - Involutive Distribution#The Definition]]

A distribution $H$ is **involutive** if $[X,Y]\in\Gamma(H)$ for every pair of smooth local sections $X,Y\in\Gamma(H)$. Equivalently, it suffices that some local frame $(w_1,\dots,w_k)$ of $H$ near every point has all pairwise brackets $[w_i,w_j]$ again sections of $H$; if a single such bracket fails to lie in $H$, the distribution is not involutive.

![[Thm - The Frobenius Theorem#Statement]]

The **Frobenius theorem** states that for a smooth distribution $H$ the three conditions are equivalent: $H$ is involutive ($[X,Y]\in\Gamma(H)$ for all $X,Y\in\Gamma(H)$); $H$ is integrable (through every point passes an integral manifold, a submanifold whose tangent space is $H$ at each of its points); and $H$ is completely integrable (every point has a flat chart for $H$). We use the direction *not involutive $\Rightarrow$ not integrable*, the contrapositive of *integrable $\Rightarrow$ involutive*.

> [!note] Convention: action side, Lie algebra, and the fundamental field
> The series takes right actions on principal bundles; here $U(1)$ is abelian, so its left (Haydys's) and right actions coincide and no sign ambiguity arises. We identify $\mathfrak u(1)=i\mathbb R\subset\mathbb C$, and the fundamental vector field of $\xi=i$ under the action $z\mapsto e^{i\vartheta}z$ is $v(x)=\frac{d}{d\vartheta}\big|_0 e^{i\vartheta}x=ix$, matching Haydys's $v_1$. The vector fields $v_1,v_2,v_3$ are written as tuples in the ambient coordinates $(x_0,x_1,x_2,x_3)$, i.e. $v_a=\sum_\mu (v_a)_\mu\,\partial_{x_\mu}$ with the listed components; each is linear in $x$, so $v_a(x)=A_a x$ for a constant $4\times4$ matrix $A_a$ read off below.

---

# Convergent Strategy

**Problem class.** This is a *disprove-a-closure-property* problem: we must show a distribution fails to be closed under the Lie bracket. The generic strategy for "show $H$ is not involutive" is to *exhibit one explicit pair of sections whose bracket escapes $H$* — a single counterexample suffices, because involutivity is a universally quantified statement. The Frobenius theorem then upgrades the algebraic failure (non-involutivity) into the geometric conclusion we actually want (non-integrability), so no integral surfaces need be searched for or ruled out by hand.

**Assumption pattern.** Two hypotheses do the work. First, the connection is *the standard Hopf connection*, so its horizontal space is the metric orthogonal complement $H_x=v(x)^\perp$; this is what lets us test horizontality by an inner product, $a(w)=\langle v,w\rangle i$. Second, the frame $(v_1,v_2,v_3)$ is *orthonormal* at every point (a computation), so that $v_2,v_3$ span $H$ and $v_1$ spans the vertical. The recognisable trigger is that we are given an explicit global frame adapted to the splitting $T S^3=H\oplus\text{vertical}$: whenever such a frame is available, involutivity of $H$ reduces to a single bracket computation among the horizontal frame fields.

**Theorem routing.** The route is: (i) verify $(v_1,v_2,v_3)$ is orthonormal and tangent to $S^3$, so by [[Thm - The Standard Connection on the Hopf Bundle]] the fields $v_2,v_3$ are sections of $H=v_1^\perp$ and $v_1$ is vertical; (ii) compute $[v_2,v_3]=-2v_1$ using that linear vector fields $X_A(x)=Ax$ bracket by $[X_A,X_B]=X_{BA-AB}$; (iii) observe $-2v_1\notin\Gamma(H)$ because $a(-2v_1)=-2i\neq0$, so by [[Def - Involutive Distribution]] $H$ is not involutive; (iv) apply [[Thm - The Frobenius Theorem]] to conclude $H$ is not integrable; (v) recompute the vertical part through the invariant formula for $d$ to identify it with the curvature $\Omega(v_2,v_3)=2i$.

**Key decision point.** The one genuinely non-obvious move is *choosing to compute a single bracket among the two horizontal frame fields* rather than attempting to describe the (nonexistent) integral surfaces directly. The equivalence in [[Def - Involutive Distribution]] — that involutivity can be tested on a local frame — is what licenses this shortcut, and the orthonormal frame $(v_2,v_3)$ of $H$ makes the test a finite computation. The second decision is *which representation of the fields to bracket in*: writing $v_a(x)=A_ax$ as linear vector fields on $\mathbb R^4$ turns the Lie bracket into a matrix commutator, avoiding coordinate charts on $S^3$ entirely; one must only check afterwards that the ambient bracket, taken between fields tangent to $S^3$, restricts to the intrinsic bracket on $S^3$ (it does, because the bracket of $\iota$-related fields is $\iota$-related).

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic page's Legal Operations section will assign them numbers):

1. **Test horizontality of a vector field by pairing with the fundamental field.** For the standard Hopf connection, $w$ is horizontal exactly when $\langle v(x),w\rangle=0$; this is the operation "read the horizontal space off the metric", from [[Thm - The Standard Connection on the Hopf Bundle]].

2. **Reduce involutivity to a bracket among frame fields.** Using the frame criterion in [[Def - Involutive Distribution]], check involutivity of the rank-$2$ distribution $H$ by computing the single bracket $[v_2,v_3]$ of its global orthonormal frame.

3. **Bracket linear vector fields as a matrix commutator.** For $X_A(x)=Ax$ and $X_B(x)=Bx$ on $\mathbb R^4$, use $[X_A,X_B]=X_{BA-AB}$; this makes $[v_2,v_3]$ a $4\times4$ matrix computation.

4. **Restrict an ambient bracket to a submanifold.** Since $v_2,v_3$ are tangent to $S^3$, their ambient Lie bracket is tangent to $S^3$ and equals their intrinsic bracket on $S^3$ (brackets of $\iota$-related fields are $\iota$-related).

5. **Convert non-involutivity into non-integrability by Frobenius.** Apply the contrapositive of [[Thm - The Frobenius Theorem]] (integrable $\Rightarrow$ involutive) to conclude $H$ has no integral surfaces.

6. **Identify the vertical defect with the curvature via the invariant $d$-formula.** Compute $\Omega(v_2,v_3)=da(v_2,v_3)=-a([v_2,v_3])$ using $d\alpha(X,Y)=X\alpha(Y)-Y\alpha(X)-\alpha([X,Y])$, from [[Thm - Coordinate Expression for the Exterior Derivative]].

---

# Hints

> [!note]- Hint 1
> To show a distribution is *not* involutive you do not need to understand all its sections — you need *one* pair of sections whose bracket leaves it. You are handed an orthonormal frame $(v_1,v_2,v_3)$ with $v_1$ pointing along the fibre. Which two of the three fields lie in $H=\ker a$, and what is the natural pair to bracket?

> [!note]- Hint 2
> First establish the geometry: check each $v_a$ is tangent to $S^3$ (i.e. $\langle v_a,x\rangle=0$) and that $(v_1,v_2,v_3)$ is orthonormal. Then $a(v_a)=\langle v_1,v_a\rangle i$ tells you at once that $v_2,v_3$ are horizontal and $v_1$ is vertical. So the only bracket that can detect non-involutivity is $[v_2,v_3]$.

> [!note]- Hint 3
> Each $v_a$ is *linear*: $v_a(x)=A_ax$ for a constant matrix $A_a$. For linear vector fields the Lie bracket is a commutator: $[X_A,X_B]=X_{BA-AB}$. Write down $A_2,A_3$, compute $A_3A_2-A_2A_3$, and compare with $A_1$.

> [!note]- Hint 4
> You should find $A_3A_2-A_2A_3=-2A_1$, so $[v_2,v_3]=-2v_1$. Now $v_1$ is *vertical*, so $-2v_1\notin H$: the bracket of two horizontal fields has left the horizontal distribution. That is the failure of involutivity. Feed it to Frobenius. For the curvature interpretation, use $da(v_2,v_3)=v_2(a(v_3))-v_3(a(v_2))-a([v_2,v_3])$ and note the first two terms vanish because $v_2,v_3$ are horizontal.

---

# Solution

The proof exhibits an explicit pair of horizontal fields whose bracket escapes the horizontal distribution. We first fix the geometry (the frame is orthonormal, so two of its members are horizontal and one is vertical), then compute the offending bracket as a matrix commutator, conclude non-involutivity from a single frame bracket, invoke Frobenius for non-integrability, and finally recognise the vertical defect as the curvature.

**Notation for the solution.** Coordinates on $\mathbb R^4$ are $(x_0,x_1,x_2,x_3)$, indices running $0$–$3$; $\langle\cdot,\cdot\rangle$ is the Euclidean inner product; $S^3=\{|x|=1\}$ with $T_xS^3=x^\perp$. A linear vector field is $X_A(x)=Ax=\sum_{\mu}(Ax)_\mu\partial_{x_\mu}$ for a constant $4\times4$ matrix $A$; the fields $v_a=X_{A_a}$ have
$$A_1=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad A_2=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad A_3=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},$$
each read off directly from the component list (row $\mu$ of $A_a$ has the $x$-coefficients of the $\mu$-th component of $v_a$; rows and columns are indexed $0$–$3$).

**Step 1: The frame is tangent to $S^3$ and orthonormal, so $v_2,v_3$ are horizontal and $v_1$ is vertical.**

Each $v_a(x)$ is orthogonal to $x$ and to the other two, and has unit length; hence $(v_1,v_2,v_3)$ is an orthonormal basis of $T_xS^3$, and pairing with $v_1=v$ shows $v_2,v_3\in H$, $v_1\notin H$.

> [!note]- Derivation
> **Tangency.** For each $a$ we compute $\langle v_a(x),x\rangle$:
> $$\langle v_1,x\rangle=(-x_1)x_0+x_0x_1+(-x_3)x_2+x_2x_3=0\qquad\text{(terms cancel in pairs),}$$
> $$\langle v_2,x\rangle=(-x_2)x_0+x_3x_1+x_0x_2+(-x_1)x_3=0,\qquad\langle v_3,x\rangle=(-x_3)x_0+(-x_2)x_1+x_1x_2+x_0x_3=0.$$
> So $v_a(x)\in x^\perp=T_xS^3$ for every $x\in S^3$: the three fields are tangent to $S^3$.
>
> **Unit length.** Each component list is a signed permutation of $(x_0,x_1,x_2,x_3)$, so $|v_a(x)|^2=x_0^2+x_1^2+x_2^2+x_3^2=|x|^2=1$ on $S^3$ (definition of $S^3$).
>
> **Orthogonality.** Pairwise,
> $$\langle v_1,v_2\rangle=(-x_1)(-x_2)+x_0x_3+(-x_3)x_0+x_2(-x_1)=x_1x_2+x_0x_3-x_3x_0-x_2x_1=0,$$
> $$\langle v_2,v_3\rangle=(-x_2)(-x_3)+x_3(-x_2)+x_0x_1+(-x_1)x_0=x_2x_3-x_3x_2+x_0x_1-x_1x_0=0,$$
> $$\langle v_1,v_3\rangle=(-x_1)(-x_3)+x_0(-x_2)+(-x_3)x_1+x_2x_0=x_1x_3-x_0x_2-x_3x_1+x_2x_0=0.$$
> Hence $(v_1(x),v_2(x),v_3(x))$ is an orthonormal triple in the $3$-dimensional space $T_xS^3$, so it is an orthonormal basis of $T_xS^3$ at every point.
>
> **Horizontality and verticality.** By [[Thm - The Standard Connection on the Hopf Bundle]], $a_x(u)=\langle v(x),u\rangle i$ with $v=v_1$. Therefore
> $$a(v_2)=\langle v_1,v_2\rangle i=0,\qquad a(v_3)=\langle v_1,v_3\rangle i=0,\qquad a(v_1)=\langle v_1,v_1\rangle i=|v_1|^2\,i=i\neq0.$$
> Thus $v_2,v_3\in\ker a=H$ and $v_1$ is not horizontal; indeed $v_1=v$ is the fundamental (vertical) field. Because $H_x$ is $2$-dimensional (the theorem gives $\dim H=\dim\mathbb{CP}^1=2$) and $v_2(x),v_3(x)$ are two orthonormal vectors in it, $(v_2,v_3)$ is a **global smooth frame for $H$**: $H_x=\operatorname{span}\{v_2(x),v_3(x)\}$ for every $x\in S^3$.

**Step 2: The bracket of the horizontal frame fields is $[v_2,v_3]=-2v_1$.**

Writing the fields as linear vector fields and bracketing by the commutator rule gives $A_3A_2-A_2A_3=-2A_1$, hence $[v_2,v_3]=-2v_1$.

> [!note]- Derivation
> **The commutator rule for linear vector fields.** For $X_A(x)=Ax$ and $X_B(x)=Bx$ on $\mathbb R^4$, the $k$-th component of the Lie bracket is
> $$[X_A,X_B]_k=\sum_\mu (Ax)_\mu\,\partial_{x_\mu}(Bx)_k-\sum_\mu (Bx)_\mu\,\partial_{x_\mu}(Ax)_k\qquad\text{(definition of the Lie bracket in coordinates).}$$
> Since $\partial_{x_\mu}(Bx)_k=B_{k\mu}$ and $\partial_{x_\mu}(Ax)_k=A_{k\mu}$ (the entries are constant), the first sum is $\sum_\mu B_{k\mu}(Ax)_\mu=(BAx)_k$ and the second is $(ABx)_k$; therefore
> $$[X_A,X_B]=X_{BA-AB}\qquad\text{(collecting the two matrix products).}$$
> **The two products, computed row by row.** Both $A_2$ and $A_3$ are signed permutation matrices: each of their rows has exactly one nonzero entry, equal to $\pm1$. Consequently row $\mu$ of a product $A_2A_3$ is $\sigma\cdot(\text{row }c\text{ of }A_3)$, where $c$ is the column of the single nonzero entry $\sigma\in\{\pm1\}$ in row $\mu$ of $A_2$; the same holds for $A_3A_2$ with the roles exchanged. We record the rows of $A_2$ as $(0,0,-1,0),(0,0,0,1),(1,0,0,0),(0,-1,0,0)$ (for $\mu=0,1,2,3$) and the rows of $A_3$ as $(0,0,0,-1),(0,0,-1,0),(0,1,0,0),(1,0,0,0)$.
>
> For $A_2A_3$, each row of $A_2$ selects a row of $A_3$:
> $$\begin{aligned}
> \text{row }0:&\ (0,0,-1,0)\ \text{selects}\ -1\cdot(\text{row }2\text{ of }A_3)=-1\cdot(0,1,0,0)=(0,-1,0,0),\\
> \text{row }1:&\ (0,0,0,1)\ \text{selects}\ +1\cdot(\text{row }3\text{ of }A_3)=+1\cdot(1,0,0,0)=(1,0,0,0),\\
> \text{row }2:&\ (1,0,0,0)\ \text{selects}\ +1\cdot(\text{row }0\text{ of }A_3)=+1\cdot(0,0,0,-1)=(0,0,0,-1),\\
> \text{row }3:&\ (0,-1,0,0)\ \text{selects}\ -1\cdot(\text{row }1\text{ of }A_3)=-1\cdot(0,0,-1,0)=(0,0,1,0),
> \end{aligned}$$
> so that, assembling the four rows,
> $$A_2A_3=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}=A_1\qquad\text{(comparison with the matrix }A_1\text{ of the Notation).}$$
> For $A_3A_2$, each row of $A_3$ selects a row of $A_2$:
> $$\begin{aligned}
> \text{row }0:&\ (0,0,0,-1)\ \text{selects}\ -1\cdot(\text{row }3\text{ of }A_2)=-1\cdot(0,-1,0,0)=(0,1,0,0),\\
> \text{row }1:&\ (0,0,-1,0)\ \text{selects}\ -1\cdot(\text{row }2\text{ of }A_2)=-1\cdot(1,0,0,0)=(-1,0,0,0),\\
> \text{row }2:&\ (0,1,0,0)\ \text{selects}\ +1\cdot(\text{row }1\text{ of }A_2)=+1\cdot(0,0,0,1)=(0,0,0,1),\\
> \text{row }3:&\ (1,0,0,0)\ \text{selects}\ +1\cdot(\text{row }0\text{ of }A_2)=+1\cdot(0,0,-1,0)=(0,0,-1,0),
> \end{aligned}$$
> so that, assembling the four rows,
> $$A_3A_2=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}=-A_1\qquad\text{(comparison with }-A_1\text{).}$$
> Hence
> $$A_3A_2-A_2A_3=-A_1-A_1=-2A_1\qquad\text{(subtracting the two displayed matrices).}$$
> **The bracket on $\mathbb R^4$ and its restriction to $S^3$.** By the commutator rule with $A=A_2$, $B=A_3$,
> $$[v_2,v_3]=[X_{A_2},X_{A_3}]=X_{A_3A_2-A_2A_3}=X_{-2A_1}=-2\,v_1\qquad\text{(commutator rule, then the previous line).}$$
> This is an identity of vector fields on $\mathbb R^4$. Since $v_2,v_3$ are tangent to $S^3$ (Step 1), they are $\iota$-related to vector fields on $S^3$ for the inclusion $\iota\colon S^3\hookrightarrow\mathbb R^4$; the Lie bracket of $\iota$-related fields is $\iota$-related, so the intrinsic bracket of $v_2,v_3$ on $S^3$ is the restriction of $-2v_1$, which is again tangent to $S^3$. Thus $[v_2,v_3]=-2v_1$ holds as vector fields on $S^3$.

**Step 3: $H$ is not involutive.**

The bracket $[v_2,v_3]=-2v_1$ is not a section of $H$, so the horizontal distribution fails the involutivity closure property.

> [!note]- Derivation
> By Step 2, $[v_2,v_3]=-2v_1$. Testing horizontality of this field with the connection form,
> $$a([v_2,v_3])=a(-2v_1)=-2\,a(v_1)=-2i\neq0\qquad\text{(linearity of }a\text{, and }a(v_1)=i\text{ from Step 1),}$$
> so $[v_2,v_3]\notin\ker a=H$; that is, $[v_2,v_3]\notin\Gamma(H)$.
>
> Now suppose, for contradiction, that $H$ were involutive. By [[Def - Involutive Distribution]], involutivity means $[X,Y]\in\Gamma(H)$ for *every* pair of sections $X,Y\in\Gamma(H)$. Since $v_2,v_3\in\Gamma(H)$ (Step 1), involutivity would force $[v_2,v_3]\in\Gamma(H)$, contradicting the displayed line $[v_2,v_3]\notin\Gamma(H)$. The named contradiction — "$[v_2,v_3]$ both must and cannot lie in $H$" — shows the supposition is false. Therefore $H$ is **not involutive**.

**Step 4: $H$ is not integrable.**

By the Frobenius theorem, an integrable distribution is involutive; since $H$ is not involutive, it is not integrable.

> [!note]- Derivation
> By [[Thm - The Frobenius Theorem]] — restated: for a smooth distribution the conditions *involutive*, *integrable*, and *completely integrable* are equivalent — integrability implies involutivity. Taking the contrapositive: a distribution that is not involutive is not integrable.
>
> By Step 3, $H$ is not involutive; hence $H$ is not integrable. Concretely, there is **no** embedded surface $N\subseteq S^3$ with $T_xN=H_x$ for every $x\in N$: if such an integral surface existed through a point, $H$ would be integrable, hence involutive, contradicting Step 3. The two horizontal directions $v_2,v_3$ cannot be knitted into surfaces; moving along $v_2$ then $v_3$ and back leaves a first-order-nonzero displacement in the fibre direction $v_1$, which is exactly the failure the bracket $[v_2,v_3]=-2v_1$ records.

**Step 5 (interpretation): the vertical defect is the curvature.**

The vertical part of $[v_2,v_3]$ equals $-\Omega(v_2,v_3)$; explicitly $\Omega(v_2,v_3)=2i\neq0$, so the obstruction to integrability is the nonvanishing of the curvature.

> [!note]- Derivation
> The curvature of a principal connection, restricted to horizontal vectors, is $\Omega(X,Y)=da(\pi_H X,\pi_H Y)$; for the already-horizontal fields $v_2,v_3$ this is $\Omega(v_2,v_3)=da(v_2,v_3)$ (this description is developed in [[Def - Curvature of a Principal Connection]]; we use only the case of horizontal arguments). By the invariant formula for the exterior derivative of a $1$-form, [[Thm - Coordinate Expression for the Exterior Derivative]] — restated: $d\alpha(X,Y)=X\alpha(Y)-Y\alpha(X)-\alpha([X,Y])$ —
> $$\Omega(v_2,v_3)=da(v_2,v_3)=v_2\big(a(v_3)\big)-v_3\big(a(v_2)\big)-a([v_2,v_3])\qquad\text{(invariant }d\text{-formula).}$$
> By Step 1, $a(v_2)=a(v_3)=0$ identically on $S^3$, so the first two terms vanish (they are directional derivatives of the zero function). By Steps 2–3, $a([v_2,v_3])=-2i$. Hence
> $$\Omega(v_2,v_3)=0-0-(-2i)=2i\qquad\text{(the two horizontal terms vanish; the bracket term from Step 3).}$$
> This is nonzero, and it agrees with Haydys's computation $F_a(\pi_*v_2,\pi_*v_3)=2i$ from the ambient formula $\pi^*F_a=da=2(dx_0\wedge dx_1+dx_2\wedge dx_3)i$. The identity $\Omega(v_2,v_3)=-a([v_2,v_3])$ exhibits the general principle, proved in full in §4.3, that **the curvature measures the vertical part of the bracket of horizontal lifts**: $H$ is integrable if and only if $\Omega$ vanishes, and here $\Omega\neq0$ is exactly why $H$ is not integrable.

> [!note]- Complete formal solution
> **Claim.** The horizontal distribution $H=\ker a$ of the standard Hopf connection on $S^3\to S^2$ is not integrable.
>
> Let $v_1=(-x_1,x_0,-x_3,x_2)$, $v_2=(-x_2,x_3,x_0,-x_1)$, $v_3=(-x_3,-x_2,x_1,x_0)$, restricted to $S^3$.
>
> *Geometry.* Each satisfies $\langle v_a,x\rangle=0$ (tangency), $|v_a|^2=|x|^2=1$ (unit length), and $\langle v_a,v_b\rangle=0$ for $a\neq b$ (orthogonality), by the componentwise computations of Step 1; so $(v_1,v_2,v_3)$ is an orthonormal basis of $T_xS^3$. Since $a_x(u)=\langle v_1,u\rangle i$ by [[Thm - The Standard Connection on the Hopf Bundle]], we get $a(v_2)=a(v_3)=0$ and $a(v_1)=i$; thus $v_2,v_3$ span the rank-$2$ distribution $H$ and $v_1$ is vertical.
>
> *Bracket.* Writing $v_a(x)=A_ax$ with the matrices $A_a$ of the Notation, and using $[X_A,X_B]=X_{BA-AB}$ for linear vector fields, we compute $A_2A_3=A_1$ and $A_3A_2=-A_1$, so $A_3A_2-A_2A_3=-2A_1$ and $[v_2,v_3]=-2v_1$ on $\mathbb R^4$; as $v_2,v_3$ are tangent to $S^3$, this holds on $S^3$.
>
> *Non-involutivity.* Then $a([v_2,v_3])=a(-2v_1)=-2i\neq0$, so $[v_2,v_3]\notin\Gamma(H)$. Were $H$ involutive, the sections $v_2,v_3\in\Gamma(H)$ would force $[v_2,v_3]\in\Gamma(H)$ ([[Def - Involutive Distribution]]) — a contradiction. So $H$ is not involutive.
>
> *Non-integrability.* By [[Thm - The Frobenius Theorem]], integrable distributions are involutive; contrapositively, $H$ is not integrable. There is no surface tangent to $H$ through any point.
>
> *Curvature.* Using the horizontal-argument description $\Omega(v_2,v_3)=da(v_2,v_3)$ and the invariant formula $da(v_2,v_3)=v_2(a(v_3))-v_3(a(v_2))-a([v_2,v_3])$ with $a(v_2)=a(v_3)=0$, we get $\Omega(v_2,v_3)=-a([v_2,v_3])=2i\neq0$, so the obstruction to integrability is precisely the nonvanishing of the curvature. $\blacksquare$

> [!warning] Illegal but tempting: concluding non-integrability from $\dim H<\dim S^3$ or from "the fibres are circles"
> It is tempting to argue "$H$ is $2$-dimensional inside a $3$-manifold, and the fibres are the vertical circles, so of course $H$ has no integral surfaces." This is a non-argument. A rank-$2$ distribution on a $3$-manifold can perfectly well be integrable — for the *trivial* $U(1)$-bundle $S^2\times S^1$ with the product connection, the horizontal distribution *is* integrable, its integral surfaces being the slices $S^2\times\{\vartheta\}$. Dimension count and the presence of circle fibres say nothing; integrability is a *differential* condition, detected by the bracket. The extra ingredient that makes the Hopf case non-integrable is that its connection has *nonzero curvature*, $\Omega(v_2,v_3)=2i\neq0$ — equivalently, the bundle is nontrivial and the connection twists. The correct diagnostic is always the bracket computation of Step 2, never the dimension.

---

# Key Takeaways

**To disprove involutivity, exhibit one bracket of frame fields that leaves the distribution; Frobenius then hands you non-integrability for free.** Involutivity is a universally quantified statement ("*every* bracket of sections stays in $H$"), so its negation needs only a single witness. The efficient path is to find an adapted frame — here the orthonormal $(v_2,v_3)$ spanning $H$ and $v_1$ spanning the vertical — and compute one bracket. The frame criterion in [[Def - Involutive Distribution]] guarantees this single computation is decisive: if $[v_2,v_3]$ escapes $H$, no re-choice of sections can rescue involutivity. Then [[Thm - The Frobenius Theorem]] converts the algebraic failure into the geometric one we actually care about — the nonexistence of integral surfaces — with no need to hunt for or rule out surfaces directly. The trigger for this whole pattern is any question of the form "does this distribution have integral submanifolds?"; the reaction is "compute brackets of a spanning frame".

**Linear vector fields bracket by matrix commutators, and this turns bracket computations on spheres and Lie groups into linear algebra.** The fields $v_a(x)=A_ax$ are restrictions of linear vector fields, and the identity $[X_A,X_B]=X_{BA-AB}$ reduces their Lie bracket to $A_3A_2-A_2A_3$, a finite matrix computation done without ever choosing a chart on $S^3$. The one subtlety — that an ambient bracket restricts correctly to the submanifold — is handled once and for all by tangency plus the naturality of the bracket under $\iota$-relatedness. This is a broadly reusable device: whenever the manifold sits inside $\mathbb R^N$ and the relevant fields are linear (rotations, the standard frames on spheres, right- or left-invariant fields on matrix groups written in the ambient matrix space), prefer the commutator computation to coordinate charts. In the present case the deeper structure is that $v_1,v_2,v_3$ are the left-translates $iq,jq,kq$ of the unit quaternion $q=x_0+x_1i+x_2j+x_3k$; they are right-invariant fields on $S^3=Sp(1)$, whose bracket is *minus* the quaternion commutator, so $[v_2,v_3]=[X_j,X_k]_{\text{right-inv}}=-[j,k]\!\cdot q=-2i\cdot q=-2v_1$ — the same answer, now visibly a Lie-algebra fact.

**Curvature is the vertical part of the bracket of horizontal lifts, and non-integrability of the horizontal distribution is the geometric face of nonzero curvature.** The computation $\Omega(v_2,v_3)=-a([v_2,v_3])=2i$ is not a coincidence of this example; it is the local shadow of the general identity $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$ for horizontal lifts, developed in §4.3. It says the curvature *is* the obstruction to closing horizontal directions into surfaces: $H$ is integrable exactly when $\Omega\equiv0$ (a flat connection), and each nonzero component of $\Omega$ is a first-order failure of two horizontal flows to commute, deposited into the fibre. This is the conceptual payoff of the exercise and the reason it is placed to foreshadow curvature: it lets one *see* curvature before defining it, as the amount by which the Hopf horizontal planes refuse to fit together. The companion exercise [[Ex - The Curvature is the Obstruction to Integrability of the Horizontal Distribution]] proves the equivalence "$\Omega=0\iff H$ involutive $\iff H$ integrable" in general, and [[Ex - Curvature of the Standard Hopf Connection]] computes the same $\Omega=2i$ from the structure equation, so that a returning reader can triangulate the number $2i$ from three independent routes: the bracket, the invariant $d$-formula, and $da$ in ambient coordinates.
