---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Kuranishi Model for a Fredholm Map"
  - "Def - Fredholm Map and Its Index"
  - "Thm - Regular Value and Transversality Theorems for Fredholm Maps"
  - "Thm - The Inverse Function Theorem"
tags: [geometry, gauge-theory]
---

# Problem Statement

Carry out the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] explicitly, in finite dimensions, for the two smooth maps
$$F\colon\mathbb{R}^2\to\mathbb{R},\qquad F(x,y)=y-x^{2}\quad\text{(case A)},\qquad\qquad F\colon\mathbb{R}^2\to\mathbb{R},\qquad F(x,y)=xy\quad\text{(case B)},$$
each at the point $p=(0,0)\in F^{-1}(0)$. In both cases:

1. compute the differential $d_pF$, and from it identify the subspaces $X_0=\ker d_pF$ and $Y_0=\operatorname{Im}d_pF$, together with chosen complements $X_1$ (so that $\mathbb{R}^2=X_0\oplus X_1$) and $Y_1$ (so that $\mathbb{R}=Y_0\oplus Y_1$), and the linear isomorphism $T=d_pF|_{X_1}\colon X_1\to Y_0$;
2. construct the diffeomorphism $\phi$ of a neighbourhood of the origin explicitly, and compute the reduced map $f\colon\mathbb{R}^2\to Y_1$ and its restriction $f_0(x_0)=f(x_0,0)\colon X_0\to Y_1$;
3. read off $F^{-1}(0)$ near $p$ from $f_0^{-1}(0)$.

Observe that in case A the differential $d_pF$ is surjective, $0$ is a regular value, $Y_1=0$ and $f_0\equiv0$, so the zero set is a smooth curve; whereas in case B the differential vanishes, $0$ is not a regular value, $Y_1=\mathbb{R}$, and $f_0(x_0)$ is a non-degenerate indefinite **quadratic form**, whose zero set is a pair of crossing lines — a cone. Confirm in both cases that $\dim X_0-\dim Y_1=\operatorname{index}F=\dim\mathbb{R}^2-\dim\mathbb{R}=1$.

**Recall:**

The objects in play are the Kuranishi model of a Fredholm map, the index of a Fredholm map, the regular-value corollary that turns a regular value into a smooth zero-manifold, and the inverse function theorem that underlies the construction of $\phi$.

![[Thm - Kuranishi Model for a Fredholm Map#Statement]]

Unwound for the reader landing cold: given a smooth [[Def - Fredholm Map and Its Index|Fredholm map]] $F\colon X\to Y$ between Banach spaces and a point $p\in F^{-1}(0)$, set $X_0=\ker d_pF$ and $Y_0=\operatorname{Im}d_pF$, pick closed complements $X=X_0\oplus X_1$ and $Y=Y_0\oplus Y_1$ (finite-dimensional $X_0$ and $Y_1$), let $T=d_pF|_{X_1}\colon X_1\to Y_0$ (an isomorphism), and there is a local diffeomorphism $\phi$ with $\phi(0)=p$ and a smooth $f$ valued in $Y_1$ with $f(0)=0$, $d_0f=0$, such that
$$F\big(\phi(x_0,x_1)\big)=Tx_1+f(x_0,x_1).$$
Writing $f_0(x_0)=f(x_0,0)$, the piece of the zero set $F^{-1}(0)$ near $p$ is carried homeomorphically by $\phi$ onto the piece of $f_0^{-1}(0)\subseteq X_0$ near the origin. The construction is the **Lyapunov–Schmidt reduction**: with $\pi_{Y_0},\pi_{Y_1}$ the projections onto $Y_0,Y_1$, the map $\Phi(x_0,x_1)=(x_0,\pi_{Y_0}F(p+x_0+x_1))$ has differential $(x_0,x_1)\mapsto(x_0,Tx_1)$ at the origin, an isomorphism, so by the [[Thm - The Inverse Function Theorem|inverse function theorem]] it has a smooth local inverse $\Psi$; one sets $\phi(x_0,x_1):=p+\Psi(x_0,Tx_1)$ and $f:=\pi_{Y_1}\circ F\circ\phi$.

![[Def - Fredholm Map and Its Index#The Definition]]

For a smooth map between finite-dimensional manifolds the differential $d_pF\colon\mathbb{R}^m\to\mathbb{R}^n$ is automatically a Fredholm operator, with
$$\operatorname{index}d_pF=\dim\ker d_pF-\dim\operatorname{coker}d_pF=\dim\mathbb{R}^m-\dim\mathbb{R}^n=m-n$$
by the rank–nullity theorem (kernel dimension minus cokernel dimension is $(m-\operatorname{rank})-(n-\operatorname{rank})=m-n$, independent of the rank). So both maps here are Fredholm of index $2-1=1$, and this common value is $\operatorname{index}F$.

The regular-value case is closed by the following corollary, which we invoke in case A.

> [!note] Invoked result — regular value gives a smooth zero-manifold
> **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|Regular-value corollary]], part (i).** Let $F\colon X\to Y$ be a smooth Fredholm map between Banach manifolds. If $y$ is a regular value of $F$ (that is, $d_xF$ is surjective for every $x\in F^{-1}(y)$), then $F^{-1}(y)$ is a smooth embedded submanifold of $X$ of dimension $\operatorname{index}F$, with $T_xF^{-1}(y)=\ker d_xF$. In the Kuranishi picture this is the case $Y_1=0$: then $f\equiv0$, and $F^{-1}(0)$ is locally $\phi(X_0\times\{0\})$, a manifold of dimension $\dim X_0=\operatorname{index}F$.

---

# Convergent Strategy

**Problem class.** This is a *compute-the-normal-form* exercise: it takes an abstract structural theorem — that near a zero every Fredholm map is, after a change of coordinates on the source, the sum of an invertible linear map on a complement and a finite-dimensional "obstruction map" $f_0$ on the kernel — and instantiates it in the smallest cases where one can see every subspace and every formula by hand. The value of doing it in $\mathbb{R}^2\to\mathbb{R}$ is that the two qualitatively different outcomes of the theorem, a regular value (obstruction absent) and a maximally degenerate value (obstruction a full quadratic form), both occur, and the difference is visible entirely in the rank of $d_pF$.

**Assumption pattern.** The Kuranishi model applies to any Fredholm map at any point of the zero set; the input that selects the *shape* of the answer is the rank of $d_pF$. When $d_pF$ is surjective the cokernel is zero, so $Y_1=0$ and the reduction is empty — the theorem degenerates into the ordinary implicit/regular-value statement. When $d_pF$ has a large kernel and small image the obstruction map $f_0$ carries all the information, and its leading (quadratic) term governs the local shape of the zero set. The recognisable trigger is thus: to find the local model of a zero set, compute the rank of the differential there; the corank tells you the dimension of $Y_1$ and hence how many scalar equations $f_0=0$ cut out the reduced zero set.

**Theorem routing.** The route in each case is mechanical once the theorem is in hand: compute $\nabla F(0)$ to get $d_pF$; read $X_0=\ker d_pF$ and $Y_0=\operatorname{Im}d_pF$ off it; choose the orthogonal complements $X_1,Y_1$; form $\Phi(x_0,x_1)=(x_0,\pi_{Y_0}F(x_0+x_1))$ (here $p=0$), invert it by hand using the [[Thm - The Inverse Function Theorem|inverse function theorem]] to get $\Psi$; set $\phi(x_0,x_1)=\Psi(x_0,Tx_1)$; and compute $f=\pi_{Y_1}\circ F\circ\phi$ and $f_0(x_0)=f(x_0,0)$. In case A the regular-value corollary confirms the smooth-curve conclusion; in case B the vanishing differential forces $\phi=\operatorname{id}$ and $f_0=F$, and one reads the cone off directly.

**Key decision point.** The one genuine choice is the splitting: which complements $X_1$ and $Y_1$ to take. The theorem allows any closed complements; the cleanest choice is the orthogonal complement with respect to the standard inner product, which makes the projections $\pi_{Y_0},\pi_{Y_1}$ into coordinate projections and turns the abstract construction into an explicit change of variables. The second decision, in case A, is to notice that surjectivity of $d_pF$ makes $Y_1=0$ *before* computing anything, so that $f$ is forced to be the zero map (it takes values in the zero space) and no work remains beyond exhibiting $\phi$.

---

# Legal Operations Used

This solution deploys the following legal operations (numbering to be reconciled with the topic page's Legal Operations once it is written):

1. **Compute the differential and split source and target along it.** Evaluate $\nabla F(p)$, set $X_0=\ker d_pF$, $Y_0=\operatorname{Im}d_pF$, and choose orthogonal complements $X_1=X_0^{\perp}$, $Y_1=Y_0^{\perp}$; this is the data the Kuranishi model requires.

2. **Recognise a zero cokernel and short-circuit the reduction.** When $d_pF$ is surjective, $Y_0=Y$ forces $Y_1=0$, so the reduced map $f$ takes values in the trivial space and is identically zero; the model collapses to the regular-value corollary.

3. **Form the Lyapunov–Schmidt map $\Phi$ and invert it with the inverse function theorem.** Build $\Phi(x_0,x_1)=(x_0,\pi_{Y_0}F(p+x_0+x_1))$, check $d_0\Phi=(x_0,x_1)\mapsto(x_0,Tx_1)$ is an isomorphism, and solve $\Phi=\operatorname{id}$ explicitly to obtain the local inverse $\Psi$; then $\phi=p+\Psi(\cdot,T\cdot)$.

4. **Compute the obstruction map by projecting $F\circ\phi$ onto the cokernel complement.** Evaluate $f=\pi_{Y_1}\circ F\circ\phi$ and restrict to the kernel to get $f_0(x_0)=f(x_0,0)$; its leading term determines the local shape of the zero set.

5. **Read the local zero set off $f_0^{-1}(0)$.** Use the homeomorphism $\phi\colon f_0^{-1}(0)\to F^{-1}(0)$ near the origin: a point where $f_0=0$ is a smooth manifold gives a smooth zero set (case A), a quadratic $f_0$ with indefinite Hessian gives a nodal cone (case B).

---

# Hints

> [!note]- Hint 1
> Everything begins with the differential. Compute $\nabla F(0,0)$ in each case. In case A it is non-zero, so $d_pF$ is surjective (a non-zero linear functional $\mathbb{R}^2\to\mathbb{R}$ is onto); in case B it is zero, so $d_pF=0$. The corank of $d_pF$ — the dimension of the cokernel $Y_1$ — is what decides whether the Kuranishi reduction is trivial or carries all the content.

> [!note]- Hint 2
> Case A is a regular value: $d_pF$ surjective means $Y_0=\mathbb{R}$, so $Y_1=\{0\}$. A map into $\{0\}$ is the zero map, so $f\equiv0$ and $f_0\equiv0$ *before any computation*. All that remains is to exhibit $\phi$: solve $\pi_{Y_0}F=$ (coordinate) explicitly. Since $Y_0=\mathbb{R}$, the map $\Phi(x,y)=(x,\,F(x,y))=(x,\,y-x^2)$ is what you invert.

> [!note]- Hint 3
> In case A, invert $\Phi(x,y)=(x,y-x^2)$: from $(a,b)=(x,y-x^2)$ you get $x=a$, $y=b+a^2$, so $\Psi(a,b)=(a,b+a^2)$. With $X_0$ the $x$-axis, $X_1$ the $y$-axis, $T=\operatorname{id}$, this gives $\phi(x_0,x_1)=\Psi(x_0,x_1)=(x_0,x_1+x_0^2)$. Check $F(\phi(x_0,x_1))=x_1$, confirming $F\circ\phi=Tx_1+0$.

> [!note]- Hint 4
> Case B has $d_pF=0$, so $X_0=\mathbb{R}^2$ (everything), $X_1=\{0\}$, $Y_0=\{0\}$, $Y_1=\mathbb{R}$. With $X_1=\{0\}$ and $Y_0=\{0\}$ the map $\Phi(x_0)=(x_0,\pi_{Y_0}F(x_0))=(x_0,0)$ is essentially the identity, so $\phi=\operatorname{id}$. Then $f=\pi_{Y_1}\circ F\circ\phi=F$, and $f_0(a,b)=F(a,b)=ab$. What is the zero set of $ab=0$?

---

# Solution

The plan in both cases is the same: compute $d_pF$, split $\mathbb{R}^2$ and $\mathbb{R}$ into kernel-plus-complement and image-plus-complement, build the Lyapunov–Schmidt map and invert it by hand, and read off $f_0$. The contrast is entirely driven by the rank of $d_pF$: rank one (case A) gives a trivial cokernel and an empty obstruction, so the zero set is a smooth curve; rank zero (case B) gives a two-dimensional kernel and a one-dimensional cokernel, so $f_0$ is a full quadratic form on the plane and its zero locus is a cone.

## Case A: $F(x,y)=y-x^2$

**Step A1: Differential and splitting.**

> [!note]- Derivation
> The partial derivatives are $\partial_xF=-2x$ and $\partial_yF=1$, so
> $$\nabla F(x,y)=(-2x,\,1),\qquad \nabla F(0,0)=(0,1),\qquad d_pF(u,v)=\nabla F(0,0)\cdot(u,v)=v\qquad\text{(evaluation of the gradient at }p=0\text{).}$$
> Thus $d_pF\colon\mathbb{R}^2\to\mathbb{R}$, $(u,v)\mapsto v$. Its kernel and image are
> $$X_0=\ker d_pF=\{(u,0):u\in\mathbb{R}\}=\mathbb{R}\times\{0\}\quad(\text{the }x\text{-axis},\ \dim 1),\qquad Y_0=\operatorname{Im}d_pF=\mathbb{R}\quad(\text{since }v\mapsto v\text{ is onto}).$$
> Choose the orthogonal complements
> $$X_1=X_0^{\perp}=\{(0,v):v\in\mathbb{R}\}=\{0\}\times\mathbb{R}\quad(\text{the }y\text{-axis}),\qquad Y_1=Y_0^{\perp}=\{0\}.$$
> The distinguished isomorphism is $T=d_pF|_{X_1}\colon X_1\to Y_0$, $(0,v)\mapsto v$; identifying $X_1\cong\mathbb{R}$ by $v$ and $Y_0=\mathbb{R}$, it is $T=\operatorname{id}_{\mathbb{R}}$. Since $Y_1=\{0\}$, the map $F$ has $0$ as a **regular value** at $p$: $d_pF$ is surjective. Note $\dim X_0-\dim Y_1=1-0=1=\operatorname{index}F$.

**Step A2: The obstruction is empty.**

> [!note]- Derivation
> By the Kuranishi model, $f=\pi_{Y_1}\circ F\circ\phi$ takes values in $Y_1=\{0\}$, hence $f\equiv0$ and in particular
> $$f_0(x_0)=f(x_0,0)=0\qquad\text{for all }x_0\in X_0.$$
> This is the promised "$f_0=0$ in the regular case." It is not a coincidence but the structural fact that a surjective differential has trivial cokernel, so there is no room for an obstruction.

**Step A3: Construct $\phi$ explicitly.**

> [!note]- Derivation
> With $p=0$ and $\pi_{Y_0}=\operatorname{id}$ (as $Y_0=\mathbb{R}$), the Lyapunov–Schmidt map is
> $$\Phi(x_0,x_1)=(x_0,\ \pi_{Y_0}F(x_0+x_1))=(x,\ F(x,y))=(x,\ y-x^{2}),$$
> where we write a general point of $\mathbb{R}^2=X_0\oplus X_1$ as $(x,y)$ with $x\in X_0$, $y\in X_1$. Its differential at the origin is
> $$d_0\Phi(u,v)=(u,\ d_0F(u,v))=(u,v)\qquad\text{(since }d_0F(u,v)=v\text{)},$$
> the identity, an isomorphism. By the **[[Thm - The Inverse Function Theorem|inverse function theorem]]** — a smooth map whose differential at a point is a linear isomorphism restricts to a smooth diffeomorphism of a neighbourhood of that point onto a neighbourhood of its image — $\Phi$ has a smooth local inverse $\Psi$. Here we invert globally by hand: solving $(a,b)=(x,\,y-x^2)$ gives $x=a$ and $y=b+a^2$, so
> $$\Psi(a,b)=(a,\ b+a^{2}).$$
> Following the recipe $\phi(x_0,x_1)=p+\Psi(x_0,Tx_1)=\Psi(x_0,x_1)$ (as $p=0$, $T=\operatorname{id}$),
> $$\boxed{\ \phi(x_0,x_1)=(x_0,\ x_1+x_0^{2})\ }\qquad(x_0,x_1)\in X_0\oplus X_1\cong\mathbb{R}^2.$$
> **Verification of the normal form.** Compute, with $\phi(x_0,x_1)=(x_0,x_1+x_0^2)$,
> $$F(\phi(x_0,x_1))=(x_1+x_0^{2})-(x_0)^{2}=x_1=Tx_1+0=Tx_1+f(x_0,x_1)\qquad\text{(direct substitution into }F(x,y)=y-x^2\text{),}$$
> confirming $f\equiv0$, $f(0)=0$, and $d_0f=0$, exactly as the theorem requires.

**Step A4: Read off the zero set.**

> [!note]- Derivation
> Since $f_0\equiv0$, the reduced zero set is all of $X_0$: $f_0^{-1}(0)=X_0=\mathbb{R}\times\{0\}$. The Kuranishi homeomorphism carries a neighbourhood of $0$ in $f_0^{-1}(0)$ onto a neighbourhood of $p$ in $F^{-1}(0)$, and explicitly
> $$\phi\big(X_0\times\{0\}\big)=\{\phi(x_0,0):x_0\in\mathbb{R}\}=\{(x_0,\ x_0^{2}):x_0\in\mathbb{R}\},$$
> which is exactly the parabola $\{(x,y):y=x^2\}=F^{-1}(0)$. Thus $F^{-1}(0)$ is a smooth $1$-dimensional submanifold, of dimension $\operatorname{index}F=1$, in agreement with the **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value corollary]]** (part (i)): $0$ regular $\Rightarrow$ $F^{-1}(0)$ a smooth manifold of dimension $\operatorname{index}F$, with tangent space $\ker d_pF=X_0$ at $p$ — indeed the parabola $y=x^2$ has horizontal tangent (the $x$-axis) at the origin.

## Case B: $F(x,y)=xy$

**Step B1: Differential and splitting.**

> [!note]- Derivation
> The partial derivatives are $\partial_xF=y$ and $\partial_yF=x$, so
> $$\nabla F(x,y)=(y,\,x),\qquad \nabla F(0,0)=(0,0),\qquad d_pF=0\qquad\text{(the gradient vanishes at the origin).}$$
> Hence the differential is the zero map $d_pF\colon\mathbb{R}^2\to\mathbb{R}$, $(u,v)\mapsto0$. Its kernel and image are
> $$X_0=\ker d_pF=\mathbb{R}^2\quad(\dim 2),\qquad Y_0=\operatorname{Im}d_pF=\{0\}.$$
> The complements are forced:
> $$X_1=X_0^{\perp}=\{0\},\qquad Y_1=Y_0^{\perp}=\mathbb{R}\quad(\dim 1).$$
> The isomorphism $T=d_pF|_{X_1}\colon X_1\to Y_0$ is the unique map $\{0\}\to\{0\}$, trivially an isomorphism. Here $0$ is **not** a regular value: $d_pF=0$ is not surjective onto $\mathbb{R}$. Note again $\dim X_0-\dim Y_1=2-1=1=\operatorname{index}F$, the same index as case A even though the local picture will be entirely different.

**Step B2: Construct $\phi$ (it is the identity).**

> [!note]- Derivation
> With $Y_0=\{0\}$ the projection $\pi_{Y_0}$ is the zero map, so the Lyapunov–Schmidt map is
> $$\Phi(x_0)=(x_0,\ \pi_{Y_0}F(x_0))=(x_0,\ 0)\in X_0\oplus Y_0=\mathbb{R}^2\oplus\{0\},$$
> i.e. under the identification $X_0\oplus Y_0=X_0=\mathbb{R}^2$ the map $\Phi$ is the identity of $\mathbb{R}^2$, whose differential $d_0\Phi=\operatorname{id}$ is an isomorphism. Its inverse is $\Psi=\operatorname{id}$. Because $X_1=\{0\}$, the variable $x_1$ ranges only over $0$ and $Tx_1=0$, so
> $$\phi(x_0)=p+\Psi(x_0,\ Tx_1)=\Psi(x_0,0)=x_0,\qquad\text{that is}\qquad \boxed{\ \phi=\operatorname{id}_{\mathbb{R}^2}.\ }$$
> There is nothing to straighten: with a vanishing differential the inverse function theorem gives no coordinate change, and the entire content of the map is pushed into the obstruction $f_0$.

**Step B3: Compute the obstruction $f_0$.**

> [!note]- Derivation
> Since $Y_1=\mathbb{R}=Y$, the projection $\pi_{Y_1}=\operatorname{id}$, so
> $$f=\pi_{Y_1}\circ F\circ\phi=F\circ\operatorname{id}=F.$$
> Writing a point of $X_0=\mathbb{R}^2$ as $x_0=(a,b)$, and remembering $x_1\in X_1=\{0\}$ contributes nothing,
> $$f_0(a,b)=f\big((a,b),0\big)=F(a,b)=ab\qquad\text{(definition }F(x,y)=xy\text{).}$$
> This is the promised quadratic form. In symmetric-matrix form,
> $$f_0(a,b)=ab=\begin{pmatrix}a&b\end{pmatrix}\begin{pmatrix}0&\tfrac12\\[2pt]\tfrac12&0\end{pmatrix}\begin{pmatrix}a\\ b\end{pmatrix},$$
> whose matrix has eigenvalues $\pm\tfrac12$, hence signature $(1,1)$: the form is **non-degenerate and indefinite**. Diagonalising by the rotation $a=\tfrac{1}{\sqrt2}(s+t)$, $b=\tfrac{1}{\sqrt2}(s-t)$ gives $f_0=\tfrac12(s^2-t^2)$, the standard saddle. The normal form of the theorem reads
> $$F(\phi(x_0,x_1))=Tx_1+f(x_0,x_1)=0+ab=ab,$$
> and indeed $d_0f=0$ since $f=F$ has vanishing gradient at the origin, as the theorem demands.

**Step B4: Read off the zero set — a cone.**

> [!note]- Derivation
> The reduced zero set is
> $$f_0^{-1}(0)=\{(a,b)\in\mathbb{R}^2:ab=0\}=\big(\{0\}\times\mathbb{R}\big)\ \cup\ \big(\mathbb{R}\times\{0\}\big),$$
> the union of the two coordinate axes — two lines crossing transversally at the origin. Since $\phi=\operatorname{id}$, this *is* $F^{-1}(0)$ near $p$:
> $$F^{-1}(0)=\{(x,y):xy=0\}=(\{x=0\})\cup(\{y=0\}).$$
> This is a one-dimensional real algebraic cone (the zero set of an indefinite quadratic form; the ordinary double point, or node). It is **not** a smooth manifold at the origin: any neighbourhood of $0$ in it, with $0$ removed, has four components (the four half-axes), whereas a $1$-manifold minus a point is locally two components. The failure is precisely the failure of $0$ to be a regular value: the [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value corollary]] does not apply, and the Kuranishi model reveals the singularity as the zero set of the leading quadratic obstruction $f_0$. The index equals $\dim X_0-\dim Y_1=2-1=1$, but here it is the *virtual* (expected) dimension: the actual zero set is the union of two $1$-dimensional pieces meeting at a point, not a smooth $1$-manifold.

> [!note]- Complete formal solution
> **Case A: $F(x,y)=y-x^2$ at $p=0$.** Here $\nabla F(0,0)=(0,1)$, so $d_pF(u,v)=v$, giving $X_0=\ker d_pF=\mathbb{R}\times\{0\}$, $Y_0=\operatorname{Im}d_pF=\mathbb{R}$, and orthogonal complements $X_1=\{0\}\times\mathbb{R}$, $Y_1=\{0\}$; $T=d_pF|_{X_1}$ is $(0,v)\mapsto v$, the identity after the obvious identifications. Since $Y_1=0$, the reduced map $f=\pi_{Y_1}\circ F\circ\phi$ is valued in $\{0\}$, hence $f\equiv0$ and $f_0\equiv0$: $0$ is a regular value. The Lyapunov–Schmidt map $\Phi(x,y)=(x,\,y-x^2)$ has $d_0\Phi=\operatorname{id}$, so by the inverse function theorem it is a local diffeomorphism; inverting, $\Psi(a,b)=(a,b+a^2)$, hence $\phi(x_0,x_1)=(x_0,\,x_1+x_0^2)$, and $F(\phi(x_0,x_1))=(x_1+x_0^2)-x_0^2=x_1=Tx_1+0$. The zero set near $p$ is $\phi(X_0\times\{0\})=\{(x_0,x_0^2)\}$, the parabola $y=x^2$, a smooth submanifold of dimension $\operatorname{index}F=2-1=1$, tangent to $X_0$ at $p$, as the regular-value corollary predicts.
>
> **Case B: $F(x,y)=xy$ at $p=0$.** Here $\nabla F(0,0)=(0,0)$, so $d_pF=0$, giving $X_0=\ker d_pF=\mathbb{R}^2$, $Y_0=\operatorname{Im}d_pF=\{0\}$, and forced complements $X_1=\{0\}$, $Y_1=\mathbb{R}$; $T\colon\{0\}\to\{0\}$ is trivial. The Lyapunov–Schmidt map $\Phi(x_0)=(x_0,\pi_{Y_0}F(x_0))=(x_0,0)$ is the identity, so $\phi=\operatorname{id}_{\mathbb{R}^2}$, and $f=\pi_{Y_1}\circ F\circ\phi=F$, so with $x_0=(a,b)$,
> $$f_0(a,b)=F(a,b)=ab,$$
> a non-degenerate indefinite quadratic form of signature $(1,1)$ (in rotated coordinates $\tfrac12(s^2-t^2)$), with $d_0f_0=0$. The zero set near $p$ is $f_0^{-1}(0)=\{ab=0\}=\{x=0\}\cup\{y=0\}$, the pair of coordinate axes — a cone (nodal singularity), not a smooth manifold at the origin, reflecting that $0$ is not a regular value. Both maps are Fredholm of index $\dim X_0-\dim Y_1=1$; case A realises this index as the true dimension of a smooth curve, case B only as the virtual dimension of a singular zero set. $\blacksquare$

> [!warning]- Illegal but tempting: reading the index as the dimension of $F^{-1}(0)$ in case B
> It is tempting to conclude from $\operatorname{index}F=1$ that $F^{-1}(0)$ is a $1$-manifold in *both* cases. This is false in case B: the index is only the **virtual dimension**, equal to the true dimension of the zero set exactly when $0$ is a regular value (so that the obstruction $f_0$ is absent, or at least submersive). When $0$ is critical, as in case B where $d_pF=0$, the zero set is $f_0^{-1}(0)$ for a genuinely nonlinear $f_0$, and its topology is whatever that reduced equation dictates — here a cone. The extra condition that would license "dimension $=\operatorname{index}$" is regularity of the value (or, more weakly, that $f_0$ be a submersion near the origin); it is precisely the hypothesis of the regular-value corollary, and it is violated in case B.

---

# Key Takeaways

**The Kuranishi model reduces the local study of a Fredholm zero set to a finite-dimensional equation $f_0=0$ on the kernel, valued in the cokernel, and the rank of the differential decides everything.** The reusable content is the dictionary: at a point $p$ of the zero set, $\dim\ker d_pF$ counts the source directions the linearisation cannot control and $\dim\operatorname{coker}d_pF$ counts the target directions the linearisation cannot reach; the invertible part $T$ solves the equation in the remaining directions once and for all, leaving only the map $f_0\colon\ker d_pF\to\operatorname{coker}d_pF$ whose zero set models $F^{-1}(0)$ near $p$. When the cokernel is zero (a regular value) there is nothing left to solve and the zero set is a smooth manifold of dimension $\dim\ker d_pF=\operatorname{index}F$; when the cokernel is non-zero the leading Taylor term of $f_0$ — here a quadratic form — governs the singularity. The trigger for reaching for this reduction is any question about the *local structure* of a solution set of a nonlinear equation between (possibly infinite-dimensional) spaces near a point where the linearisation degenerates; the transferable diagnostic is to compute the kernel and cokernel of the linearisation first, because their dimensions are the shape of the answer.

**Index is virtual dimension: it equals the true dimension of the zero set only at regular values, and otherwise measures the expected dimension of a possibly singular space.** The two cases share the index $1$ yet produce a smooth curve and a cone respectively, which is the whole moral. In gauge theory this is not a pathology but the central mechanism: the dimension formulas for instanton and Seiberg–Witten moduli spaces are index computations, and they give the *expected* dimension, correct wherever the relevant operator is surjective (the moduli space is then a smooth manifold of that dimension) and merely a lower bound or a virtual count where reducible or obstructed solutions make the linearisation fail to be surjective. Recognising when an index is the honest dimension and when it is only virtual is exactly the recognition that separates case A from case B, and it is why so much analytic work in gauge theory goes into arranging transversality — perturbing to make the relevant value regular — so that the virtual dimension becomes the actual one. The diagnostic to carry: whenever a dimension is quoted as an index, ask whether the linearisation is surjective at every point of the set, for only then is the quoted number the true dimension.

**The obstruction map $f_0$ is intrinsically defined up to the choices, and its Hessian at a critical point is the first invariant of the singularity.** In case B the reduced map was $f_0(a,b)=ab$, and its Hessian — the symmetric matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ up to a factor — is non-degenerate and indefinite, which is what makes the zero set a transverse pair of lines rather than, say, a single point or a cusp. This is the entry point to the Morse-theoretic and singularity-theoretic analysis of moduli spaces: when $f_0$ has a non-degenerate Hessian the singularity is a standard quadratic cone, understood completely by the signature of that Hessian; when the Hessian degenerates one must look to higher-order terms. For spaced practice, the pattern to retain is that after performing a Kuranishi reduction the next move at a critical point is to compute the Hessian of $f_0$ and read its rank and signature, because those two numbers classify the generic (Morse) singularity and tell you, for instance, whether a reducible solution sits at the vertex of a cone whose link is a sphere — the structure that drives the counting argument in Donaldson's theorem.
