---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Euler Class of an Oriented Vector Bundle"
  - "Def - Pfaffian"
  - "Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix"
  - "Ex - Cartan Structural Equations on S^2"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory, characteristic-classes, euler-class]
---

# Problem Statement

Let $S^{2}=\{x\in\mathbb{R}^{3}:|x|=1\}$ be the unit round two-sphere, carrying the round metric $g=d\theta^{2}+\sin^{2}\theta\,d\varphi^{2}$ in the spherical coordinates $(\theta,\varphi)\in(0,\pi)\times(0,2\pi)$, and let $E=TS^{2}$ be its tangent bundle. Equip $E$ with its Levi-Civita connection and orient $S^{2}$ by the outward normal, so that the coframe $(\sigma^{1},\sigma^{2})=(d\theta,\sin\theta\,d\varphi)$ is a **positively oriented orthonormal coframe** and the Riemannian area form is $dA=\sigma^{1}\wedge\sigma^{2}=\sin\theta\,d\theta\wedge d\varphi$.

**(a)** In this oriented orthonormal frame, write down the $\mathfrak{so}(2)$-valued connection matrix and compute the curvature matrix
$$F=\begin{pmatrix}0&\Omega^{1}{}_{2}\\[2pt]-\Omega^{1}{}_{2}&0\end{pmatrix},\qquad \Omega^{1}{}_{2}=K\,dA,$$
identifying the Gaussian curvature $K$.

**(b)** Compute the Chern–Weil form $\operatorname{Pf}(F/2\pi)$ representing the Euler class and show that
$$\operatorname{Pf}\!\Big(\frac{F}{2\pi}\Big)=\frac{K\,dA}{2\pi}=\frac{dA}{2\pi}.$$

**(c)** Integrate over the sphere to obtain the Euler number
$$e(TS^{2})[S^{2}]=\int_{S^{2}}\operatorname{Pf}\!\Big(\frac{F}{2\pi}\Big)=2,$$
and discuss the sign: explain which orientation and frame-ordering conventions make the answer $+2$ rather than $-2$, and cross-check the value against the Euler characteristic $\chi(S^{2})=2$.

Throughout, $dA$ is a **single symbol** denoting the area two-form $\sin\theta\,d\theta\wedge d\varphi$ (it is not the exterior derivative of anything); the connection matrix is written $\omega$, never $A$, to avoid any clash. The symbol $F$ is a $2\times2$ matrix whose entries are two-forms on $S^{2}$; $\Omega^{1}{}_{2}$ is its upper-right entry, a two-form; $\mathfrak{so}(2)=\{X\in\operatorname{Mat}(2\times2;\mathbb{R}):X^{t}=-X\}$ is the Lie algebra of $SO(2)$.

**Recall:**

The objects in play are the Euler class of an oriented even-rank bundle, the Pfaffian of a $\mathfrak{so}(2)$ matrix, and the Levi-Civita connection and curvature of the round sphere in an orthonormal frame.

![[Def - Euler Class of an Oriented Vector Bundle#The Definition]]

For an oriented real vector bundle $E\to M$ of rank $2m$ with a Euclidean structure and a metric connection whose curvature $F$ is skew-symmetric in oriented orthonormal frames, the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] is $e(E):=\big[\operatorname{Pf}(F/2\pi)\big]\in H^{2m}_{\mathrm{dR}}(M)$, where $\operatorname{Pf}$ is the Chern–Weil form of the Pfaffian invariant polynomial on $\mathfrak{so}(2m)$. The class is independent of the choices (metric and connection), and the series normalisation is fixed so that $e(TS^{2})[S^{2}]=2$. For $M=S^{2}$ closed and oriented, evaluation on the fundamental class is integration, $e(E)[S^{2}]=\int_{S^{2}}\operatorname{Pf}(F/2\pi)$.

![[Def - Pfaffian#The Definition]]

For $m=1$ the [[Def - Pfaffian|Pfaffian]] of a $2\times2$ skew matrix is its upper-right entry:
$$\operatorname{Pf}\begin{pmatrix}0&x\\-x&0\end{pmatrix}=x.$$
Applied entrywise to a matrix of two-forms, $\operatorname{Pf}\!\begin{pmatrix}0&\beta\\-\beta&0\end{pmatrix}=\beta$; this is exactly the substitution of the curvature into the degree-$1$ invariant polynomial $\operatorname{Pf}$, which is what the Chern–Weil construction does.

From [[Ex - Cartan Structural Equations on S^2|the Cartan computation on the round sphere]]: in the orthonormal coframe $\sigma^{1}=d\theta$, $\sigma^{2}=\sin\theta\,d\varphi$, the single independent connection one-form is
$$\omega^{1}{}_{2}=-\cos\theta\,d\varphi,$$
and the curvature two-form is $\Omega^{1}{}_{2}=\sigma^{1}\wedge\sigma^{2}=\sin\theta\,d\theta\wedge d\varphi$, so that the Gaussian curvature is $K=1$. The companion coordinate-frame computation in [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix]] reaches the same $K=1$ and matches this orthonormal-frame result after the change of frame.

---

# Convergent Strategy

**Problem class.** This is a *characteristic-number evaluation*: we take a specific oriented even-rank bundle with a known connection, feed its curvature through the Pfaffian invariant polynomial to build the Chern–Weil representative of the Euler class, and integrate to get an integer. It is the Euler-class analogue of "compute the first Chern number of a line bundle from its curvature", and it is the smallest nontrivial instance in which the Pfaffian, rather than the trace, is the relevant invariant polynomial. The one genuine subtlety, and the reason for the second star, is the sign bookkeeping tying the frame ordering, the orientation, and the Pfaffian together.

**Assumption pattern.** The bundle is $TS^{2}$, rank $2m=2$, oriented; the recognisable trigger for "use the Pfaffian" is precisely that the rank is *even* and the bundle is *oriented*, so that the structure group reduces to $SO(2)$ and the curvature is $\mathfrak{so}(2)$-valued (skew) in an oriented orthonormal frame. Metric-compatibility of the Levi-Civita connection is what makes the curvature matrix skew in the first place, and orientability is what lets us choose the frame *positively*, which fixes the sign of the Pfaffian.

**Theorem routing.** The route is: import the orthonormal-frame connection and curvature forms from [[Ex - Cartan Structural Equations on S^2]] (this replaces a Christoffel-symbol computation with a two-line moving-frame calculation); assemble the $\mathfrak{so}(2)$ curvature matrix $F$; apply the definition of the Euler class from [[Def - Euler Class of an Oriented Vector Bundle]], whose Pfaffian for a $2\times2$ skew matrix is the single upper-right entry, [[Def - Pfaffian]]; and integrate the resulting area form using $\int_{S^{2}}dA=4\pi$, the total area computed in [[Ex - Volume of the n-Sphere via the Volume Form]]. The value is finally cross-checked against the Gauss–Bonnet identity $\int_{S^{2}}K\,dA=2\pi\chi(S^{2})$, recorded in [[Thm - Gauss-Bonnet Theorem for Surfaces]].

**Key decision point.** The decisive move is *choosing the orthonormal frame to be positively oriented and keeping its order fixed through the Pfaffian*. The Pfaffian is not invariant under all frame changes: under an orientation-reversing change (swapping $e_{1}\leftrightarrow e_{2}$) it changes sign, since $\operatorname{Pf}$ is $SO(2)$-invariant but $O(2)\setminus SO(2)$-anti-invariant. This is exactly why the Euler class needs an orientation to be defined, and it is where the ambiguous "$\pm$" in the naive curvature matrix $F=K\,dA\!\begin{pmatrix}0&\mp1\\\pm1&0\end{pmatrix}$ is resolved: the positively oriented frame produces the entry $+K\,dA$ in the $(1,2)$ slot, hence $+2$. Reading the sign off carelessly — from a frame whose orientation one has not checked — is the classic error and would return $-2$.

---

# Legal Operations Used

1. **Compute the curvature in a moving orthonormal frame (the "Cartan structural equations" operation from the topic page).** Rather than differentiate Christoffel symbols, we take the orthonormal coframe $(\sigma^{1},\sigma^{2})=(d\theta,\sin\theta\,d\varphi)$, read the connection one-form $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$ off the first structural equation, and obtain the curvature from $\Omega^{1}{}_{2}=d\omega^{1}{}_{2}$ (the $\omega\wedge\omega$ term vanishes in two dimensions because $SO(2)$ is abelian). This is imported wholesale from [[Ex - Cartan Structural Equations on S^2]].

2. **Assemble the $\mathfrak{so}(2m)$ curvature matrix and substitute it into the Pfaffian (the "evaluate an invariant polynomial on the curvature" operation).** The skew curvature matrix in the oriented orthonormal frame is $F=\begin{pmatrix}0&\Omega^{1}{}_{2}\\-\Omega^{1}{}_{2}&0\end{pmatrix}$, and the Chern–Weil form of the Euler class is $\operatorname{Pf}(F/2\pi)$, which for rank $2$ is simply the rescaled $(1,2)$ entry.

3. **Fix the sign by orienting the frame (the "use the orientation to pin down the Pfaffian's sign" operation).** Because $\operatorname{Pf}$ changes sign under an orientation-reversing frame change, we take the frame positively oriented for the outward orientation of $S^{2}$; this makes the area form $dA=\sigma^{1}\wedge\sigma^{2}$ positive and the Euler number $+2$.

4. **Integrate a top-degree form over the closed oriented manifold.** With $\operatorname{Pf}(F/2\pi)=dA/2\pi$ a positive multiple of the area form, the Euler number is $\tfrac{1}{2\pi}\int_{S^{2}}dA=\tfrac{1}{2\pi}\cdot4\pi=2$, using the total area from [[Ex - Volume of the n-Sphere via the Volume Form]] and that the coordinate chart covers all of $S^{2}$ up to a set of measure zero.

---

# Hints

> [!note]- Hint 1
> You do not need Christoffel symbols. Borrow the orthonormal-frame result from [[Ex - Cartan Structural Equations on S^2]]: the connection one-form is $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$ and the curvature two-form is $\Omega^{1}{}_{2}=\sin\theta\,d\theta\wedge d\varphi$. What is the $2\times2$ skew matrix $F$ built from this single independent entry?

> [!note]- Hint 2
> For a rank-$2$ oriented bundle, $2m=2$ so $m=1$, and the Pfaffian of a $2\times2$ skew matrix $\begin{pmatrix}0&\beta\\-\beta&0\end{pmatrix}$ is just $\beta$. So $\operatorname{Pf}(F)$ is literally $\Omega^{1}{}_{2}$, and $\operatorname{Pf}(F/2\pi)=\Omega^{1}{}_{2}/2\pi$ because $\operatorname{Pf}$ is homogeneous of degree $m=1$. Write $\Omega^{1}{}_{2}$ in the form $K\,dA$ and read off $K$.

> [!note]- Hint 3
> The area form is $dA=\sin\theta\,d\theta\wedge d\varphi$. Integrate it over $\theta\in(0,\pi)$, $\varphi\in(0,2\pi)$; you should get $4\pi$. Hence $\tfrac{1}{2\pi}\int_{S^{2}}dA=2$.

> [!note]- Hint 4
> For the sign: the Pfaffian is $SO(2)$-invariant but flips sign if you swap the two frame vectors (an orientation-reversing change). So the *ordered* frame matters. Choose $(e_{1},e_{2})$ dual to $(d\theta,\sin\theta\,d\varphi)$; check that this frame is positively oriented for the outward orientation (equivalently that $dA=\sigma^{1}\wedge\sigma^{2}>0$). With that choice the $(1,2)$ entry of $F$ is $+K\,dA$ and the answer is $+2$; the opposite frame ordering would give the matrix $K\,dA\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $-2$.

> [!note]- Hint 5
> Sanity check via Gauss–Bonnet: $\int_{S^{2}}K\,dA=2\pi\chi(S^{2})=2\pi\cdot2=4\pi$, so $e(TS^{2})[S^{2}]=\tfrac{1}{2\pi}\int_{S^{2}}K\,dA=\chi(S^{2})=2$. The Euler *number* of the tangent bundle of a closed oriented surface is its Euler *characteristic* — that is the content of the name.

---

# Solution

**Plan.** We first assemble the $\mathfrak{so}(2)$ curvature matrix $F$ from the orthonormal-frame connection form of the round sphere, reading off $K=1$. We then apply the Pfaffian, which in rank $2$ is the upper-right entry, to get $\operatorname{Pf}(F/2\pi)=dA/2\pi$. Integrating over the sphere gives $2$. Finally we spell out the sign convention — why the positively oriented frame yields $+2$ and not $-2$ — and confirm the value against $\chi(S^{2})=2$ through Gauss–Bonnet.

**Step 1: Assemble the connection and curvature matrices in the oriented orthonormal frame.**

The $\mathfrak{so}(2)$ connection matrix has the single independent entry $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$, and its curvature is $F=d\omega+\omega\wedge\omega$ with the $\omega\wedge\omega$ term vanishing, giving $\Omega^{1}{}_{2}=\sin\theta\,d\theta\wedge d\varphi=K\,dA$ with $K=1$.

> [!note]- Derivation
> Take the positively oriented orthonormal coframe $\sigma^{1}=d\theta$, $\sigma^{2}=\sin\theta\,d\varphi$; that it is orthonormal is the identity $(\sigma^{1})^{2}+(\sigma^{2})^{2}=d\theta^{2}+\sin^{2}\theta\,d\varphi^{2}=g$ (the round metric). For a metric connection in an orthonormal frame the connection matrix is skew, so in rank $2$ it has one independent entry:
> $$\omega=\begin{pmatrix}\omega^{1}{}_{1}&\omega^{1}{}_{2}\\ \omega^{2}{}_{1}&\omega^{2}{}_{2}\end{pmatrix}=\begin{pmatrix}0&\omega^{1}{}_{2}\\ -\omega^{1}{}_{2}&0\end{pmatrix},\qquad \omega^{1}{}_{2}=-\cos\theta\,d\varphi\qquad\text{(skew-symmetry of a metric connection; value from the Cartan structural equations).}$$
> The value $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$ is exactly the connection one-form derived in [[Ex - Cartan Structural Equations on S^2]].
> The curvature matrix is $F=d\omega+\omega\wedge\omega$ (the local curvature of a connection, in the series convention $F=d\omega+\omega\wedge\omega$ with the matrix product carrying the wedge). Its $\omega\wedge\omega$ part vanishes because every entry of that matrix product is a wedge of the one-form $\omega^{1}{}_{2}$ with itself or with a zero diagonal entry: the $(1,2)$ entry is $\omega^{1}{}_{1}\wedge\omega^{1}{}_{2}+\omega^{1}{}_{2}\wedge\omega^{2}{}_{2}=0+0=0$ (since $\omega^{1}{}_{1}=\omega^{2}{}_{2}=0$). Hence
> $$\Omega^{1}{}_{2}=(F)_{12}=d\omega^{1}{}_{2}=d(-\cos\theta\,d\varphi)=\sin\theta\,d\theta\wedge d\varphi\qquad\text{(Leibniz rule for }d\text{, and }d(d\varphi)=0\text{).}$$
> Writing the area form $dA=\sigma^{1}\wedge\sigma^{2}=d\theta\wedge(\sin\theta\,d\varphi)=\sin\theta\,d\theta\wedge d\varphi$, this reads $\Omega^{1}{}_{2}=dA$, that is $\Omega^{1}{}_{2}=K\,dA$ with Gaussian curvature $K=1$. Assembling,
> $$F=\begin{pmatrix}0&\Omega^{1}{}_{2}\\ -\Omega^{1}{}_{2}&0\end{pmatrix}=\begin{pmatrix}0&dA\\ -dA&0\end{pmatrix}=dA\begin{pmatrix}0&1\\ -1&0\end{pmatrix}.$$

**Step 2: Apply the Pfaffian to obtain the Euler-class representative.**

For a $2\times2$ skew matrix the Pfaffian is the upper-right entry, and by homogeneity $\operatorname{Pf}(F/2\pi)=\tfrac{1}{2\pi}\Omega^{1}{}_{2}=dA/2\pi$.

> [!note]- Derivation
> The Euler class is represented by $\operatorname{Pf}(F/2\pi)$, where $\operatorname{Pf}$ is the Chern–Weil form of the degree-$m$ Pfaffian invariant polynomial on $\mathfrak{so}(2m)$; here $2m=2$, so $m=1$. For a $2\times2$ skew matrix of two-forms, substituting into $\operatorname{Pf}$ returns the upper-right entry:
> $$\operatorname{Pf}(F)=\operatorname{Pf}\begin{pmatrix}0&\Omega^{1}{}_{2}\\ -\Omega^{1}{}_{2}&0\end{pmatrix}=\Omega^{1}{}_{2}\qquad\text{(the }m=1\text{ Pfaffian is the upper-right entry).}$$
> This is the rank-$2$ Pfaffian from [[Def - Pfaffian]].
> Since $\operatorname{Pf}$ is homogeneous of degree $m=1$, scaling the matrix by $\tfrac{1}{2\pi}$ scales its Pfaffian by $\tfrac{1}{2\pi}$:
> $$\operatorname{Pf}\!\Big(\frac{F}{2\pi}\Big)=\frac{1}{2\pi}\operatorname{Pf}(F)=\frac{\Omega^{1}{}_{2}}{2\pi}=\frac{K\,dA}{2\pi}=\frac{dA}{2\pi}\qquad\text{(homogeneity of degree }1\text{, then }\Omega^{1}{}_{2}=K\,dA\text{ with }K=1\text{).}$$
> This is a closed two-form representing $e(TS^{2})\in H^{2}_{\mathrm{dR}}(S^{2})$; it is closed because it is a top-degree form on a surface (every $2$-form on a $2$-manifold is closed), and the general closedness and connection-independence are established once and for all on [[Def - Euler Class of an Oriented Vector Bundle]] via the Chern–Weil theorem.

**Step 3: Integrate over the sphere.**

Integrating the positive multiple $dA/2\pi$ of the area form over $S^{2}$ gives $\tfrac{1}{2\pi}\cdot4\pi=2$.

> [!note]- Derivation
> The Euler number is the integral of the representative over the closed oriented surface,
> $$e(TS^{2})[S^{2}]=\int_{S^{2}}\operatorname{Pf}\!\Big(\frac{F}{2\pi}\Big)=\frac{1}{2\pi}\int_{S^{2}}dA\qquad\text{(Step 2, and linearity of the integral).}$$
> The spherical chart $(\theta,\varphi)\in(0,\pi)\times(0,2\pi)$ covers $S^{2}$ up to the two poles and one meridian, a set of measure zero, so the integral of the smooth top form is computed there:
> $$\int_{S^{2}}dA=\int_{0}^{2\pi}\!\!\int_{0}^{\pi}\sin\theta\,d\theta\,d\varphi=\Big(\int_{0}^{2\pi}d\varphi\Big)\Big(\int_{0}^{\pi}\sin\theta\,d\theta\Big)=2\pi\cdot\big[-\cos\theta\big]_{0}^{\pi}=2\pi\cdot(1-(-1))=4\pi\qquad\text{(Fubini on the product region; }\int_{0}^{\pi}\sin\theta\,d\theta=2\text{).}$$
> The same total area $4\pi$ is computed intrinsically in [[Ex - Volume of the n-Sphere via the Volume Form]] for $n=2$. Therefore
> $$e(TS^{2})[S^{2}]=\frac{1}{2\pi}\cdot4\pi=2.$$

**Step 4: Discuss the sign, and cross-check against $\chi(S^{2})=2$.**

The value is $+2$ precisely because the frame was taken positively oriented; the Pfaffian changes sign under an orientation-reversing frame change, and the orientation of $TS^{2}$ is what removes the ambiguity. Gauss–Bonnet confirms $+2=\chi(S^{2})$.

> [!note]- Derivation
> **Why the sign is fixed, and where the ambiguity lives.** The Pfaffian invariant polynomial on $\mathfrak{so}(2m)$ is invariant under $\operatorname{Ad}(SO(2m))$ but changes sign under $\operatorname{Ad}$ of an element of $O(2m)\setminus SO(2m)$; concretely, in rank $2$, conjugating the skew matrix $\begin{pmatrix}0&x\\-x&0\end{pmatrix}$ by the reflection $\operatorname{diag}(1,-1)$ (which swaps the roles of $e_{1}$ and $-e_{2}$ and reverses orientation) sends $x\mapsto-x$. So the value of $\operatorname{Pf}(F)$ depends on the *ordered, oriented* frame, not merely on the metric connection. This is not a defect: it is the reason the Euler class is defined only for *oriented* bundles, and it is what the orientation is spent on.
>
> Had we ordered the two orthonormal frame vectors the other way — a frame $(e_{2},e_{1})$, negatively oriented for the outward orientation — the same connection would have presented its curvature matrix as $F=K\,dA\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$, with upper-right entry $-K\,dA$, and the computation would have returned $\operatorname{Pf}(F/2\pi)=-dA/2\pi$ and $e[S^{2}]=-2$. The two answers $\pm2$ are the two ways of reading the "$\pm$" in $F=K\,dA\begin{pmatrix}0&\mp1\\\pm1&0\end{pmatrix}$; the series convention (recorded in the conventions ledger and on [[Def - Euler Class of an Oriented Vector Bundle]]) selects the *positively oriented* frame, for which $dA=\sigma^{1}\wedge\sigma^{2}>0$ and the $(1,2)$ entry of $F$ is $+K\,dA$, giving $e(TS^{2})[S^{2}]=+2$.
>
> That the chosen frame is positively oriented is checked directly: for the outward orientation of $S^{2}\subset\mathbb{R}^{3}$, the ordered pair of unit vectors $(\partial_{\theta},\tfrac{1}{\sin\theta}\partial_{\varphi})$ dual to $(\sigma^{1},\sigma^{2})$ has $(\hat r,\partial_{\theta},\tfrac{1}{\sin\theta}\partial_{\varphi})$ right-handed in $\mathbb{R}^{3}$ (the spherical frame satisfies $\hat r\times\hat\theta=\hat\varphi$), so $(\sigma^{1},\sigma^{2})$ is positively oriented and $dA=\sin\theta\,d\theta\wedge d\varphi$ is the positive area form.
>
> **Cross-check by Gauss–Bonnet.** The [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]] states, for a closed oriented Riemannian surface $\Sigma$ with Gaussian curvature $K$ and area form $dA$, that $\int_{\Sigma}K\,dA=2\pi\,\chi(\Sigma)$. For $\Sigma=S^{2}$, $\chi(S^{2})=2$, so $\int_{S^{2}}K\,dA=4\pi$, and
> $$e(TS^{2})[S^{2}]=\frac{1}{2\pi}\int_{S^{2}}K\,dA=\frac{1}{2\pi}\cdot2\pi\,\chi(S^{2})=\chi(S^{2})=2,$$
> in agreement with the direct computation. This is the surface case of the general fact that the Euler number of the tangent bundle of a closed oriented manifold equals its Euler characteristic.

> [!note]- Complete formal solution
> **Claim.** With $S^{2}$ outward-oriented and its Levi-Civita connection, $\operatorname{Pf}(F/2\pi)=dA/2\pi$ and $e(TS^{2})[S^{2}]=\int_{S^{2}}\operatorname{Pf}(F/2\pi)=2$.
>
> In the positively oriented orthonormal coframe $\sigma^{1}=d\theta$, $\sigma^{2}=\sin\theta\,d\varphi$, the metric connection is skew with single entry $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$ (from the Cartan structural equations). Its curvature is $F=d\omega+\omega\wedge\omega$; the $\omega\wedge\omega$ term vanishes in rank $2$ (all its entries are $\omega^{1}{}_{2}$ wedged with itself or with a zero diagonal entry), so
> $$F=\begin{pmatrix}0&\Omega^{1}{}_{2}\\ -\Omega^{1}{}_{2}&0\end{pmatrix},\qquad \Omega^{1}{}_{2}=d\omega^{1}{}_{2}=\sin\theta\,d\theta\wedge d\varphi=dA,$$
> i.e. $K=1$. For the rank-$2$ Pfaffian, $\operatorname{Pf}(F)=\Omega^{1}{}_{2}$, and by degree-$1$ homogeneity $\operatorname{Pf}(F/2\pi)=\Omega^{1}{}_{2}/2\pi=dA/2\pi$.
>
> Integrating, and using $\int_{S^{2}}dA=\int_{0}^{2\pi}\!\int_{0}^{\pi}\sin\theta\,d\theta\,d\varphi=4\pi$ (the chart covers $S^{2}$ up to measure zero),
> $$e(TS^{2})[S^{2}]=\frac{1}{2\pi}\int_{S^{2}}dA=\frac{4\pi}{2\pi}=2.$$
> The sign is $+2$ because $\operatorname{Pf}$ is $SO(2)$-invariant but orientation-reversal-anti-invariant, and the frame was taken positively oriented (so $dA>0$ and the $(1,2)$ entry of $F$ is $+K\,dA$); the opposite ordering would give $-2$. Gauss–Bonnet confirms $\tfrac{1}{2\pi}\int_{S^{2}}K\,dA=\chi(S^{2})=2$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to skip the orientation check and just declare $\operatorname{Pf}(F)=|\Omega^{1}{}_{2}|$ or to take the sign from whatever order the frame happened to be written in. This is wrong on two counts. First, $\operatorname{Pf}$ is a signed polynomial, not an absolute value; its whole reason for existing (over the trace or the determinant) is that it carries the orientation-sensitive sign, which is exactly the information the Euler class records. Second, taking the sign from an unexamined frame will return $-2$ half the time. The correct discipline is to *fix an orientation of $E$ first, choose the frame positively for it, and never reorder the frame inside the Pfaffian*. Only then is $\operatorname{Pf}(F/2\pi)$ a well-defined representative of $e(E)$; reversing the orientation of $E$ genuinely negates $e(E)$, and the sign is not an artefact to be discarded but the answer.

---

# Key Takeaways

**The Euler number of the tangent bundle of a closed oriented surface is its Euler characteristic, and this computation is the prototype.** The single scalar $\int_{S^{2}}\operatorname{Pf}(F/2\pi)=2$ is not an accident of the round metric: the Euler class is independent of the connection and the metric, so any metric on $S^{2}$ gives the same integer, and that integer is $\chi(S^{2})=2$. The mechanism is the Chern–Weil construction specialised to the Pfaffian invariant polynomial on $\mathfrak{so}(2m)$; for a surface the Pfaffian of the $2\times2$ curvature is just the Gaussian-curvature two-form $K\,dA$, and dividing by $2\pi$ and integrating turns the local curvature into the global topological count. Whenever one meets "integrate a curvature over a closed surface and get an integer", the invariant polynomial being used is either the trace (giving a Chern number of a complex line bundle) or the Pfaffian (giving the Euler number of an oriented real plane bundle), and on an oriented surface these agree because $TS^{2}$ is simultaneously a real oriented rank-$2$ bundle and a complex line bundle, with $e=c_{1}$.

**The Pfaffian carries the orientation, and that is the entire reason it, rather than the trace or determinant, defines the Euler class.** The trace and the determinant are invariant under the full orthogonal group, so classes built from them (Pontryagin classes) see no orientation. The Pfaffian is invariant only under $SO(2m)$ and flips sign under orientation reversal; consequently it descends to a well-defined form only after an orientation of the bundle is chosen, and it changes sign when that orientation is reversed. The transferable diagnostic: if a characteristic number is expected to change sign when the manifold or bundle is re-oriented (as the Euler number of $\overline{S^{2}}$ is $-2$), the invariant polynomial in play must be orientation-anti-invariant, hence the Pfaffian; if it is orientation-blind, it is built from traces and determinants. This is also why the identity $\operatorname{Pf}^{2}=\det$ from [[Ex - Pfaffian of a 4 by 4 Skew Matrix and the Identity Pf Squared Equals det]] translates into $e(E)^{2}=p_{m}(E)$ at the level of classes: squaring kills the sign, and the top Pontryagin class is the orientation-blind shadow of the Euler class.

**The moving-frame method is the efficient engine for characteristic-number computations, and the sign discipline is the only hard part.** The entire curvature computation collapsed to two lines because the orthonormal-coframe Cartan equations gave $\omega^{1}{}_{2}=-\cos\theta\,d\varphi$ and $\Omega^{1}{}_{2}=d\omega^{1}{}_{2}$ directly, with the nonlinear $\omega\wedge\omega$ term vanishing because $SO(2)$ is abelian. In higher rank the $\omega\wedge\omega$ term returns and the Pfaffian becomes a genuine degree-$m$ polynomial in the curvature entries, but the strategic shape is identical: build the skew curvature matrix in an oriented orthonormal frame, substitute into the Pfaffian, integrate. The recurring trap, worth internalising from this smallest case, is the sign: always orient the bundle first and keep the frame's order fixed through the Pfaffian, because the answer legitimately depends on it. The companion drill [[Ex - Pfaffian of a 4 by 4 Skew Matrix and the Identity Pf Squared Equals det]] fixes the algebraic sign conventions of the Pfaffian itself, and this exercise fixes the geometric orientation conventions that turn those signs into a topological invariant.
