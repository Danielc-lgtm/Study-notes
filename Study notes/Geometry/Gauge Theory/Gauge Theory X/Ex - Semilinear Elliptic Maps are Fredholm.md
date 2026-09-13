---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Fredholm Map and Its Index"
  - "Def - Fredholm Operator and Index"
  - "Thm - Elliptic Operators on Closed Manifolds are Fredholm"
  - "Thm - Sobolev Multiplication Theorem"
  - "Thm - Rellich Compactness Theorem"
  - "Thm - Stability of the Fredholm Property under Small and Compact Perturbations"
  - "Thm - Sobolev Embedding Theorem"
  - "Def - Sobolev Space of Sections"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $M$ is a **closed** (compact, without boundary) smooth manifold of dimension $n$, equipped with a fixed Riemannian metric $g$, and $\Delta$ denotes the associated non-negative Laplace–Beltrami operator on functions, $\Delta = d^{*}d$, a second-order elliptic differential operator that is formally self-adjoint. Sobolev spaces of real-valued functions are written $H_{s} := W^{s,2}(M;\mathbb{R})$, with $H_{s}\subset H_{t}$ continuously for $s\ge t$. We fix an integer $k$ with the standing assumption
$$2k > n .$$

Define the **semilinear map**
$$F : H_{k+2} \longrightarrow H_{k}, \qquad F(u) := \Delta u + u^{3}.$$

Prove all of the following.

1. **($F$ is well-defined and smooth.)** For every $u\in H_{k+2}$ the function $\Delta u + u^{3}$ lies in $H_{k}$, and $F$ is a smooth map between the Banach spaces $H_{k+2}$ and $H_{k}$ in the Fréchet sense, with derivative
$$d_{u}F : H_{k+2}\to H_{k}, \qquad d_{u}F(v) = \Delta v + 3u^{2}v .$$

2. **($d_{u}F$ is $\Delta$ plus a compact operator.)** For each fixed $u\in H_{k+2}$ the multiplication operator $v\mapsto 3u^{2}v$ is a compact linear operator $H_{k+2}\to H_{k}$.

3. **($F$ is Fredholm of index $0$.)** Consequently $d_{u}F$ is a Fredholm operator with $\operatorname{index} d_{u}F = \operatorname{index}\Delta = 0$ for every $u$, so $F$ is a smooth Fredholm map of index $0$.

This map is the finite-degree prototype of the Seiberg–Witten map: a fixed elliptic linear operator plus a lower-order pointwise nonlinearity, whose linearisation is elliptic-plus-compact, hence Fredholm of the index of the elliptic part.

**Recall:**

The objects in play are the Sobolev spaces $H_{s}=W^{s,2}(M;\mathbb{R})$ on a closed manifold, the notion of a Fredholm map between Banach manifolds, the Fredholm property of an elliptic operator, the compactness of the Sobolev inclusion (Rellich), and the multiplicative structure of the top Sobolev spaces.

![[Def - Fredholm Map and Its Index#The Definition]]

A smooth map $F\in C^{\infty}(X;Y)$ between [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifolds]] is a [[Def - Fredholm Map and Its Index|Fredholm map]] if its differential $d_{x}F : T_{x}X\to T_{F(x)}Y$ is a [[Def - Fredholm Operator and Index|Fredholm operator]] — a bounded linear map with finite-dimensional kernel and cokernel, hence closed range — for every $x\in X$; the integer $\operatorname{index} d_{x}F = \dim\ker d_{x}F - \dim\operatorname{coker} d_{x}F$ is locally constant in $x$, so on a connected $X$ it is a single integer $\operatorname{index}F$.

![[Thm - Elliptic Operators on Closed Manifolds are Fredholm#Statement]]

The result we lean on for the linear part is that on a closed manifold every elliptic operator is Fredholm as a map of Sobolev spaces: if $L:\Gamma(E)\to\Gamma(F)$ is an [[Def - Elliptic Differential Operator and Principal Symbol|elliptic]] differential operator of order $\ell\ge 1$, then for every $k$ the extension $L:H_{k+\ell}(M;E)\to H_{k}(M;F)$ is Fredholm, its kernel consists of smooth sections and is independent of $k$, its cokernel is canonically the finite-dimensional kernel $\ker L^{*}$ of the [[Thm - Existence and Ellipticity of the Formal Adjoint|formal adjoint]], and $\operatorname{index}L = \dim\ker L - \dim\ker L^{*}$ is independent of $k$. (See the full theorem, proved on [[Thm - Elliptic Operators on Closed Manifolds are Fredholm]].)

![[Thm - Rellich Compactness Theorem#Statement]]

The [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]] states that on a compact manifold, for integers $s>t$, the inclusion $H_{s}(M;E)\hookrightarrow H_{t}(M;E)$ is a compact operator: every sequence bounded in $H_{s}$ has a subsequence converging in $H_{t}$.

![[Thm - Sobolev Multiplication Theorem#Statement]]

The [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] provides two facts we use. First, if $2k>n$ then pointwise multiplication is a bounded bilinear map $H_{k}(M)\times H_{k}(M)\to H_{k}(M)$, with $\lVert uv\rVert_{k}\le C\lVert u\rVert_{k}\lVert v\rVert_{k}$; that is, $H_{k}(M)$ is a Banach algebra after renorming. Second, for integers $k_{1},k_{2}\ge k\ge 0$ with $k_{1}+k_{2}-k>\tfrac n2$, multiplication extends to a bounded bilinear map $H_{k_{1}}(M)\times H_{k_{2}}(M)\to H_{k}(M)$.

![[Thm - Stability of the Fredholm Property under Small and Compact Perturbations#Statement]]

Finally, the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]] states that if $T:H\to H'$ is a Fredholm operator between Hilbert spaces and $K:H\to H'$ is compact, then $T+K$ is Fredholm with $\operatorname{index}(T+K) = \operatorname{index}T$.

---

# Convergent Strategy

**Problem class.** This is a *verify-the-structural-hypotheses* problem for the abstract machinery of Chapter X: to feed a nonlinear elliptic equation into the Sard–Smale theorem, the transversality theorems, and the degree, one must first certify that the map defining the equation is a *smooth Fredholm map* between Banach manifolds. The recognisable shape is "a fixed elliptic linear operator plus a lower-order nonlinear term", of which $u\mapsto \Delta u + u^{3}$ is the simplest genuinely nonlinear instance and the exact template for the Seiberg–Witten map $(\mathcal{A},\Phi)\mapsto (F_{\mathcal{A}}^{+}-\sigma(\Phi),\slashed D_{\mathcal{A}}\Phi)$ of Chapter XI.

**Assumption pattern.** The single numerical hypothesis $2k>n$ does all the analytic work, and it is used in exactly two ways. It makes the *top* Sobolev space $H_{k}$ a Banach algebra (through the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] part (a)), which is what lets the pointwise cube $u^{3}$ land back in $H_{k}$ instead of leaving the scale; and, being equivalent to $k>\tfrac n2$, it verifies the numerical side condition $k_{1}+k_{2}-k>\tfrac n2$ of the mixed multiplication estimate that makes the linearised multiplication operator bounded. The recognisable trigger for "$2k>n$" is precisely the appearance of a *pointwise product* of Sobolev functions: products of functions of low regularity need not be integrable, and the assumption $2k>n$ (equivalently, $H_{k}\hookrightarrow C^{0}$ by the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]]) buys the boundedness the product needs.

**Theorem routing.** The route has two independent strands that meet at the end. For *smoothness*, we observe that cubing is the diagonal restriction of the bounded trilinear map $(a,b,c)\mapsto abc$ on the Banach algebra $H_{k+2}$ (here $2(k+2)>n$ too), and a bounded multilinear map between Banach spaces is $C^{\infty}$ with an explicitly computable derivative; the linear term $\Delta$ is a [[Thm - Differential Operators are Bounded between Sobolev Spaces|bounded linear operator]], hence smooth. For the *Fredholm* property, we split the derivative $d_{u}F = \Delta + 3u^{2}\,\cdot$: the first summand is Fredholm by [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|the elliptic Fredholm theorem]], and the second is shown compact by factoring $H_{k+2}\hookrightarrow H_{k+1}\xrightarrow{\,3u^{2}\cdot\,}H_{k}$ — the inclusion is compact by [[Thm - Rellich Compactness Theorem|Rellich]] and the multiplication is bounded by the mixed [[Thm - Sobolev Multiplication Theorem|Sobolev estimate]]. The [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]] then hands us "Fredholm of index $\operatorname{index}\Delta$", and $\operatorname{index}\Delta=0$ because $\Delta$ is formally self-adjoint.

**Key decision point.** The one genuinely creative move is *the choice of intermediate space $H_{k+1}$* in the compactness argument. Multiplication by $3u^{2}$ is bounded from $H_{k+2}$ to $H_{k+2}$ but not compact there, and Rellich alone (the inclusion $H_{k+2}\hookrightarrow H_{k}$ is compact) does not by itself say anything about a multiplication operator. The insight is that the linearised nonlinearity is *lower order than the elliptic operator by exactly the amount Rellich needs*: one factors off a single derivative's worth of compactness, $H_{k+2}\hookrightarrow H_{k+1}$, and spends it against the elliptic gain, leaving a bounded multiplication $H_{k+1}\to H_{k}$. This "the nonlinearity is a compact perturbation because it is of strictly lower order" pattern is the whole reason index computations for nonlinear elliptic problems reduce to index computations for the linear symbol.

---

# Legal Operations Used

The following operations are drawn from the Legal Operations of the topic page [[Gauge Theory X — Fredholm Maps, Transversality, and Degree]]; until that page fixes their numbering they are named descriptively here.

1. **Read off the differential of a polynomial nonlinearity on a Banach algebra.** For a bounded trilinear map $B$ on a Banach algebra, the diagonal map $u\mapsto B(u,u,u)$ is smooth and its Fréchet derivative at $u$ is $v\mapsto B(v,u,u)+B(u,v,u)+B(u,u,v)$; for the commutative product this is $3u^{2}v$.

2. **Certify that a pointwise product stays in the Sobolev scale via the algebra property.** When $2k>n$, invoke part (a) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] to keep $u^{2}$ and $u^{3}$ inside $H_{k}$.

3. **Trade one derivative of regularity for compactness (Rellich).** Factor an inclusion $H_{s}\hookrightarrow H_{s-1}$ and record it as a compact operator by [[Thm - Rellich Compactness Theorem|Rellich]].

4. **Bound a variable-coefficient multiplication with the mixed multiplication estimate.** Use part (b) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] with the specific exponents $(k_{1},k_{2},k)=(k,k+1,k)$, checking $k_{1}+k_{2}-k>\tfrac n2$.

5. **Use the ideal property of compact operators.** The composite of a bounded operator with a compact operator (in either order) is compact; apply it to (multiplication) $\circ$ (inclusion).

6. **Perturb a Fredholm operator by a compact one without changing the index.** Invoke the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]].

7. **Compute the index of a formally self-adjoint elliptic operator as zero.** Use $\operatorname{index}L = \dim\ker L - \dim\ker L^{*}$ from [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|the elliptic Fredholm theorem]] together with $L^{*}=L$.

---

# Hints

> [!note]- Hint 1
> There are two entirely separate things to prove: that $F$ is *smooth*, and that its differential is *Fredholm of index $0$*. Do not entangle them. For smoothness, note that $u\mapsto u^{3}$ is a cubic polynomial in $u$ — think about what "polynomial map on a Banach algebra" means, and why $2k>n$ makes $H_{k+2}$ a Banach algebra. For the Fredholm property, first guess the derivative: differentiate $\Delta u + u^{3}$ formally.

> [!note]- Hint 2
> The derivative is $d_{u}F(v) = \Delta v + 3u^{2}v$. The operator $\Delta$ is elliptic of order $2$ on a closed manifold, so you already have a theorem that says $\Delta:H_{k+2}\to H_{k}$ is Fredholm. The whole problem is therefore: *what kind of operator is $v\mapsto 3u^{2}v$, and how does adding it to a Fredholm operator affect the index?* Which stability theorem do you know for Fredholm operators?

> [!note]- Hint 3
> Adding a *compact* operator to a Fredholm operator keeps it Fredholm and does not move the index. So it suffices to show $v\mapsto 3u^{2}v$ is compact from $H_{k+2}$ to $H_{k}$. Compactness is never free — you need Rellich. But Rellich is a statement about *inclusions*, not multiplications. Can you insert an inclusion into the multiplication operator so that Rellich applies to one factor while the other factor stays merely bounded?

> [!note]- Hint 4
> Factor $H_{k+2}\xrightarrow{\ \iota\ }H_{k+1}\xrightarrow{\ 3u^{2}\cdot\ }H_{k}$. The inclusion $\iota$ is compact by Rellich because $k+2>k+1$. The multiplication $H_{k+1}\to H_{k}$ is bounded by the mixed Sobolev multiplication estimate: put $u^{2}\in H_{k}$ (algebra), $v\in H_{k+1}$, target $H_{k}$, and check the side condition $k+(k+1)-k = k+1>\tfrac n2$, which holds because $2k>n$. Then (bounded) $\circ$ (compact) is compact. Finally $\operatorname{index}\Delta=0$ because $\Delta$ is formally self-adjoint, so $\ker\Delta^{*}=\ker\Delta$.

---

# Solution

The proof separates cleanly into an algebraic-smoothness half and an elliptic-Fredholm half. In the first, cubing is recognised as a bounded trilinear form restricted to the diagonal, which is automatically $C^{\infty}$, and this both proves smoothness and reads off the derivative $d_{u}F(v)=\Delta v + 3u^{2}v$. In the second, the derivative is written as the elliptic operator $\Delta$ plus the zeroth-order multiplication $3u^{2}\cdot$; the multiplication is shown to be compact by spending one Rellich derivative against a bounded Sobolev product, and the stability theorem converts "Fredholm plus compact" into "Fredholm of index $\operatorname{index}\Delta$", which is $0$ by self-adjointness.

**Step 0: Well-posedness — every value $F(u)$ lies in $H_{k}$.**

Because $2k>n$, the space $H_{k}$ is a Banach algebra, so $u^{3}\in H_{k}$; and $\Delta$ maps $H_{k+2}$ into $H_{k}$. Hence $F(u)=\Delta u+u^{3}\in H_{k}$ is defined for every $u\in H_{k+2}$.

> [!note]- Derivation
> Fix $u\in H_{k+2}$. Since $k+2\ge k$, the [[Thm - Sobolev Embedding Theorem|continuous inclusion]] $H_{k+2}\hookrightarrow H_{k}$ gives $u\in H_{k}$ with $\lVert u\rVert_{k}\le \lVert u\rVert_{k+2}$.
>
> By part (a) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]], valid because $2k>n$, pointwise multiplication is bounded $H_{k}\times H_{k}\to H_{k}$ with $\lVert ab\rVert_{k}\le C\lVert a\rVert_{k}\lVert b\rVert_{k}$. Applying it twice,
> $$\lVert u^{3}\rVert_{k}=\lVert u\cdot u\cdot u\rVert_{k}\le C\lVert u\rVert_{k}\,\lVert u^{2}\rVert_{k}\le C^{2}\lVert u\rVert_{k}^{3}\le C^{2}\lVert u\rVert_{k+2}^{3}<\infty \qquad \text{(multiplication estimate, twice; then the inclusion } H_{k+2}\hookrightarrow H_{k}\text{)},$$
> so $u^{3}\in H_{k}$.
>
> The Laplace–Beltrami operator $\Delta$ is a differential operator of order $2$, so by [[Thm - Differential Operators are Bounded between Sobolev Spaces|the mapping theorem for differential operators on a compact manifold]] its extension $\Delta:H_{k+2}\to H_{k}$ is bounded, $\lVert\Delta u\rVert_{k}\le C'\lVert u\rVert_{k+2}$ (since differentiation costs exactly $\ell=2$ orders). Therefore $F(u)=\Delta u+u^{3}$ is a well-defined element of $H_{k}$.

**Step 1: $F$ is smooth, with derivative $d_{u}F(v)=\Delta v+3u^{2}v$.**

The linear part $\Delta$ is bounded, hence smooth. The cubic part is the diagonal of a bounded trilinear map on a Banach algebra, hence smooth, and its derivative is $v\mapsto 3u^{2}v$.

> [!note]- Derivation
> **The linear summand.** The map $u\mapsto \Delta u$ is a bounded linear operator $H_{k+2}\to H_{k}$ (Step 0). A bounded linear operator $T$ between Banach spaces is $C^{\infty}$ in the Fréchet sense: it satisfies $T(u+h)=Tu+Th$ exactly, so $d_{u}T=T$ for every $u$ and $d^{2}T=0$. Thus the linear summand contributes $v\mapsto\Delta v$ to the derivative.
>
> **The cubic summand as a trilinear diagonal.** Because $2(k+2)=2k+4>n$, part (a) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] makes $H_{k+2}$ a Banach algebra; after renorming we may take the product to be submultiplicative, $\lVert ab\rVert_{k+2}\le\lVert a\rVert_{k+2}\lVert b\rVert_{k+2}$. Define
> $$B:H_{k+2}\times H_{k+2}\times H_{k+2}\to H_{k+2},\qquad B(a,b,c):=abc .$$
> This is trilinear (multiplication is bilinear and associative) and bounded: $\lVert B(a,b,c)\rVert_{k+2}\le\lVert a\rVert_{k+2}\lVert b\rVert_{k+2}\lVert c\rVert_{k+2}$ (submultiplicativity, twice). Let $C(u):=B(u,u,u)=u^{3}$ be its diagonal restriction.
>
> **A bounded multilinear map is smooth.** For $h\in H_{k+2}$, expand by trilinearity:
> $$C(u+h)=B(u+h,u+h,u+h)=B(u,u,u)+\big[B(h,u,u)+B(u,h,u)+B(u,u,h)\big]+\big[B(h,h,u)+B(h,u,h)+B(u,h,h)\big]+B(h,h,h) \qquad \text{(trilinearity, collecting by the number of } h\text{-slots).}$$
> The bracketed degree-one term is linear in $h$; call it $L_{u}(h):=B(h,u,u)+B(u,h,u)+B(u,u,h)$, a bounded linear map with $\lVert L_{u}(h)\rVert_{k+2}\le 3\lVert u\rVert_{k+2}^{2}\lVert h\rVert_{k+2}$. The remaining terms satisfy
> $$\lVert C(u+h)-C(u)-L_{u}(h)\rVert_{k+2}\le \big(3\lVert u\rVert_{k+2}+\lVert h\rVert_{k+2}\big)\lVert h\rVert_{k+2}^{2}=o(\lVert h\rVert_{k+2}) \qquad \text{(bound each remaining term by submultiplicativity, then } \lVert h\rVert_{k+2}^{2}/\lVert h\rVert_{k+2}\to 0\text{),}$$
> so $C$ is Fréchet differentiable at $u$ with $d_{u}C=L_{u}$. As $u\mapsto L_{u}$ is itself a bounded *quadratic* (hence smooth) map into $\operatorname{Hom}(H_{k+2},H_{k+2})$, and its own derivative is bounded bilinear, and the third derivative is the constant symmetrisation of $B$ while all derivatives of order $\ge 4$ vanish, $C$ is $C^{\infty}$. For the commutative product, $L_{u}(v)=3u^{2}v$.
>
> **Compose with the inclusion into the target.** The inclusion $\iota:H_{k+2}\hookrightarrow H_{k}$ is bounded linear (Step 0), hence smooth. Therefore $u\mapsto\iota(u^{3})=u^{3}\in H_{k}$ is smooth with derivative $v\mapsto\iota(3u^{2}v)=3u^{2}v$. (Equivalently, this smoothness is the case $f(t)=t^{3}$ of [[Thm - Composition with Analytic Functions on the Sobolev Algebra|the composition theorem for entire functions on the Sobolev algebra]], whose derivative is $v\mapsto (f'\circ u)v = 3u^{2}v$.)
>
> **Assemble.** As a sum of two smooth maps, $F$ is smooth, and by linearity of the differential
> $$d_{u}F(v)=\Delta v+3u^{2}v \qquad \text{(derivative of the linear summand plus derivative of the cubic summand).}$$

**Step 2: The multiplication operator $v\mapsto 3u^{2}v$ is compact from $H_{k+2}$ to $H_{k}$.**

Factor it through $H_{k+1}$: the inclusion $H_{k+2}\hookrightarrow H_{k+1}$ is compact by Rellich, and multiplication by the fixed function $3u^{2}\in H_{k}$ is bounded $H_{k+1}\to H_{k}$ by the mixed Sobolev estimate; the composite is compact.

> [!note]- Derivation
> Fix $u\in H_{k+2}$ and set $w:=3u^{2}$. By part (a) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] (again $2k>n$, and $u\in H_{k+2}\subset H_{k}$), $w=3u^{2}\in H_{k}$ with $\lVert w\rVert_{k}\le 3C\lVert u\rVert_{k}^{2}$.
>
> **The multiplication factor is bounded $H_{k+1}\to H_{k}$.** Apply part (b) of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] with exponents $k_{1}=k$ (the regularity of $w$), $k_{2}=k+1$ (the regularity of the variable factor), and target $k$. The hypotheses of part (b) require $k_{1},k_{2}\ge k\ge 0$ and $k_{1}+k_{2}-k>\tfrac n2$:
> $$k_{1}=k\ge k,\qquad k_{2}=k+1\ge k,\qquad k_{1}+k_{2}-k=k+1>\tfrac n2 \qquad \text{(the last since } 2k>n\Rightarrow k>\tfrac n2\Rightarrow k+1>\tfrac n2\text{).}$$
> Hence multiplication is bounded $H_{k}\times H_{k+1}\to H_{k}$, and freezing the first slot at $w$ gives a bounded linear operator
> $$m_{w}:H_{k+1}\to H_{k},\qquad m_{w}(v)=wv,\qquad \lVert wv\rVert_{k}\le C\lVert w\rVert_{k}\lVert v\rVert_{k+1}.$$
>
> **The inclusion factor is compact.** By the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]], applied with $s=k+2>k+1=t$, the inclusion $\iota:H_{k+2}\hookrightarrow H_{k+1}$ is a compact operator.
>
> **Compose.** The operator in question is $v\mapsto 3u^{2}v = w v = m_{w}(\iota(v))$, that is, $m_{w}\circ\iota:H_{k+2}\to H_{k}$. By the ideal property of compact operators — the composite of a bounded operator with a compact operator is compact (part (ii) of [[Thm - Basic Properties of Compact Operators|the basic properties of compact operators]]) — the composite $m_{w}\circ\iota$ of the bounded $m_{w}$ with the compact $\iota$ is compact. Therefore $K_{u}:v\mapsto 3u^{2}v$ is a compact operator $H_{k+2}\to H_{k}$.

**Step 3: $\Delta:H_{k+2}\to H_{k}$ is Fredholm of index $0$.**

The Laplace–Beltrami operator is elliptic of order $2$ on a closed manifold, so it is Fredholm; and being formally self-adjoint, its cokernel matches its kernel, forcing index $0$.

> [!note]- Derivation
> The Laplace–Beltrami operator $\Delta=d^{*}d$ has principal symbol $\sigma_{\Delta}(x,\xi)=-|\xi|_{g}^{2}$, invertible for $\xi\ne 0$, so $\Delta$ is [[Thm - Laplacians and Dirac Operators are Elliptic|elliptic]] of order $\ell=2$. By [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|the elliptic Fredholm theorem]], the extension $\Delta:H_{k+2}\to H_{k}$ is Fredholm, its cokernel is canonically $\ker\Delta^{*}$, and
> $$\operatorname{index}\Delta=\dim\ker\Delta-\dim\ker\Delta^{*} \qquad \text{(part (iii) of the elliptic Fredholm theorem).}$$
> The operator $\Delta$ is [[Thm - Existence and Ellipticity of the Formal Adjoint|formally self-adjoint]]: for $u,v\in C^{\infty}(M)$, $\langle\Delta u,v\rangle_{L^{2}}=\langle d^{*}du,v\rangle_{L^{2}}=\langle du,dv\rangle_{L^{2}}=\langle u,d^{*}dv\rangle_{L^{2}}=\langle u,\Delta v\rangle_{L^{2}}$ (definition of the formal adjoint $d^{*}$, twice). Hence $\Delta^{*}=\Delta$, so $\ker\Delta^{*}=\ker\Delta$ and
> $$\operatorname{index}\Delta=\dim\ker\Delta-\dim\ker\Delta=0.$$
> (Concretely $\ker\Delta$ is the constants, of dimension $1$ on a connected closed $M$, and $\ker\Delta^{*}$ is the same one-dimensional space; the index is their difference, $0$.)

**Step 4: Assemble — $F$ is a smooth Fredholm map of index $0$.**

Adding the compact $K_{u}$ of Step 2 to the Fredholm $\Delta$ of Step 3 keeps the derivative Fredholm and fixes the index at $\operatorname{index}\Delta=0$; this holds at every $u$, and $F$ is smooth by Step 1.

> [!note]- Derivation
> By Step 1, $d_{u}F=\Delta+K_{u}$ where $K_{u}(v)=3u^{2}v$. By Step 3, $\Delta:H_{k+2}\to H_{k}$ is Fredholm with $\operatorname{index}\Delta=0$; by Step 2, $K_{u}:H_{k+2}\to H_{k}$ is compact. By the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability of the Fredholm property under compact perturbations]],
> $$d_{u}F=\Delta+K_{u}\ \text{is Fredholm, with}\ \operatorname{index}d_{u}F=\operatorname{index}\Delta=0 \qquad \text{(stability theorem, with the compact perturbation } K_{u}\text{).}$$
> This holds for every $u\in H_{k+2}$. Therefore $d_{u}F$ is a [[Def - Fredholm Operator and Index|Fredholm operator]] for all $u$, which is exactly the definition of $F$ being a [[Def - Fredholm Map and Its Index|Fredholm map]]; and since $H_{k+2}$ is connected (a vector space), the locally constant index is the single value $\operatorname{index}F=0$. Together with the smoothness established in Step 1, $F$ is a smooth Fredholm map of index $0$.

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a closed Riemannian $n$-manifold, $\Delta$ its Laplace–Beltrami operator, and $2k>n$. Then $F:H_{k+2}\to H_{k}$, $F(u)=\Delta u+u^{3}$, is a smooth Fredholm map of index $0$.
>
> *Well-posedness.* Since $2k>n$, part (a) of the Sobolev multiplication theorem makes $H_{k}$ a Banach algebra, so for $u\in H_{k+2}\subset H_{k}$ we have $u^{3}\in H_{k}$ with $\lVert u^{3}\rVert_{k}\le C^{2}\lVert u\rVert_{k+2}^{3}$; and $\Delta:H_{k+2}\to H_{k}$ is bounded as a differential operator of order $2$. Hence $F(u)\in H_{k}$.
>
> *Smoothness and derivative.* The map $u\mapsto\Delta u$ is bounded linear, hence $C^{\infty}$ with derivative $\Delta$. As $2(k+2)>n$, $H_{k+2}$ is a Banach algebra; the trilinear map $B(a,b,c)=abc$ is bounded, and its diagonal $C(u)=u^{3}$ is $C^{\infty}$ with $d_{u}C(v)=3u^{2}v$ (expand $C(u+h)$ by trilinearity; the degree-one part is linear, the rest is $O(\lVert h\rVert^{2})$; higher derivatives are the constant symmetrisations of $B$ and vanish beyond order $3$). Composing with the bounded inclusion $H_{k+2}\hookrightarrow H_{k}$, $u\mapsto u^{3}$ is smooth $H_{k+2}\to H_{k}$ with derivative $v\mapsto 3u^{2}v$. Thus $F$ is smooth and $d_{u}F(v)=\Delta v+3u^{2}v$.
>
> *The zeroth-order term is compact.* Set $w=3u^{2}\in H_{k}$. By part (b) of the Sobolev multiplication theorem with $(k_{1},k_{2},k)=(k,k+1,k)$ — legal since $k,k+1\ge k$ and $k_{1}+k_{2}-k=k+1>\tfrac n2$ — multiplication by $w$ is bounded $H_{k+1}\to H_{k}$. By Rellich, $H_{k+2}\hookrightarrow H_{k+1}$ is compact. Their composite $v\mapsto wv$, $H_{k+2}\to H_{k}$, is compact by the ideal property of compact operators.
>
> *The elliptic part is Fredholm of index $0$.* $\Delta$ is elliptic of order $2$, so $\Delta:H_{k+2}\to H_{k}$ is Fredholm by the elliptic Fredholm theorem, with $\operatorname{index}\Delta=\dim\ker\Delta-\dim\ker\Delta^{*}$. Being formally self-adjoint, $\Delta^{*}=\Delta$, so $\operatorname{index}\Delta=0$.
>
> *Conclusion.* $d_{u}F=\Delta+(v\mapsto 3u^{2}v)$ is a Fredholm operator by stability of the Fredholm property under compact perturbations, with $\operatorname{index}d_{u}F=\operatorname{index}\Delta=0$, for every $u$. Hence $F$ is a smooth Fredholm map of index $0$. $\blacksquare$

> [!warning] Illegal but tempting route
> It is tempting to argue "index of a sum is the sum of the indices, so $\operatorname{index}d_{u}F=\operatorname{index}\Delta+\operatorname{index}(3u^{2}\cdot)$", and then to try to give the multiplication operator an index of its own. This is illegal on two counts. First, the index is *not* additive over sums of operators; it is additive over *compositions* of Fredholm operators, which is a different statement. Second, the multiplication operator $v\mapsto 3u^{2}v$ is generally *not* Fredholm as a map $H_{k+2}\to H_{k}$ (it is compact, and a compact operator between infinite-dimensional spaces is never Fredholm, since its range is not closed of finite codimension). The correct principle is the *perturbation* statement — Fredholm plus compact is Fredholm of the *same* index — not any additivity of indices.

> [!note]- Independent sanity check: the linear model $u\mapsto\Delta u+\lambda u$
> Replace $u^{3}$ by the linear term $\lambda u$ ($\lambda\in\mathbb{R}$), giving the genuinely linear map $L_{\lambda}=\Delta+\lambda\,\mathrm{id}:H_{k+2}\to H_{k}$. Here $\lambda\,\mathrm{id}$ is exactly $v\mapsto \lambda v$ with the constant coefficient $\lambda\in H_{k}$, and the same factorisation $H_{k+2}\hookrightarrow H_{k+1}\xrightarrow{\lambda\cdot}H_{k}$ shows $\lambda\,\mathrm{id}$ is compact $H_{k+2}\to H_{k}$ (Rellich then boundedness). So $L_{\lambda}$ is Fredholm of index $0$ for every $\lambda$ — as it must be, since $L_{\lambda}$ is itself elliptic of order $2$ and self-adjoint, with index $0$ directly from the elliptic Fredholm theorem. The two computations agree, confirming that the compact-perturbation route reproduces the direct elliptic answer. The nonlinear $3u^{2}\cdot$ behaves exactly like a variable-coefficient version of $\lambda\,\mathrm{id}$.

---

# Key Takeaways

**The Fredholm index of a nonlinear elliptic map is the index of its linear symbol, because the nonlinearity is a compact perturbation of the elliptic part.** This is the reusable principle, and it is the reason the entire index bookkeeping of gauge theory reduces to symbol computations. The linearisation of a map "elliptic operator $+$ lower-order nonlinearity" is "the same elliptic operator $+$ a variable-coefficient operator of strictly lower order", and *strictly lower order on a compact manifold means compact* — one derivative of order gap is precisely one application of Rellich. Adding a compact operator to a Fredholm operator changes neither the Fredholm property nor the index. So whenever you meet a nonlinear elliptic equation on a closed manifold and are asked for the dimension of its solution space or the index of its linearisation, the trigger is: *identify the top-order linear part, compute its symbol index, and dismiss everything of lower order as compact.* The transferable diagnostic is to count orders — the elliptic operator has order $\ell$, the nonlinearity differentiates to order $\le\ell-1$, and the gap is what Rellich spends.

**The condition $2k>n$ is the price of admission for pointwise nonlinearities in Sobolev spaces, and it appears exactly where a product is formed.** Below this threshold, the product of two $H_{k}$ functions need not lie in any $H_{k}$; at or above it, $H_{k}$ is a Banach algebra and, equivalently by Sobolev embedding, $H_{k}\hookrightarrow C^{0}$, so functions have honest pointwise values that can be multiplied and cubed. The trigger for invoking "$2k>n$" is the literal appearance of a *product of Sobolev functions* — $u^{2}$, $u^{3}$, $u^{2}v$, or the quadratic $\sigma(\Phi)$ of the Seiberg–Witten map. The mixed multiplication estimate (part (b)) is the finer tool: it says a product of an $H_{k_{1}}$ and an $H_{k_{2}}$ function lands in $H_{k}$ as long as $k_{1}+k_{2}-k>\tfrac n2$, which is exactly what lets a variable coefficient of regularity $k$ act boundedly on functions of regularity $k+1$ while losing only one derivative. Learn to choose the three exponents so that the coefficient sits at its natural regularity, the variable factor sits one above the target, and the side condition is met.

**Smoothness of a polynomial nonlinearity on a Banach algebra is free, and its derivative is read off by the product rule.** A pointwise polynomial such as $u\mapsto u^{3}$ is the diagonal restriction of a bounded multilinear map, and a bounded multilinear map between Banach spaces is automatically $C^{\infty}$: its Taylor expansion is finite, its derivatives of each order are the symmetrisations of the multilinear form, and everything beyond the polynomial degree vanishes. This is worth internalising because it removes any apparent analytic difficulty from the smoothness half of such problems — the only thing that can go wrong is that the product fails to stay in the space, which is the $2k>n$ issue of the previous takeaway. Once boundedness of the product is secured, differentiability is a one-line expansion, and the derivative $d_{u}(u^{3})=3u^{2}\cdot$ is the ordinary product rule read in the algebra. The same remark upgrades to entire functions $f$ through their power series (the composition theorem for the Sobolev algebra), with derivative $v\mapsto (f'\circ u)v$; the cube is simply the case $f(t)=t^{3}$.

This exercise is the analytic groundwork for the Sard–Smale machine: having certified that $u\mapsto\Delta u+u^{3}$ is a smooth Fredholm map of index $0$, one may apply the parametric transversality package to the family $\mathcal F(u,w)=\Delta u+u^{3}-w$, which is worked in the companion exercise [[Ex - Parametric Transversality for a Family of Elliptic Equations]]; the finite-dimensional model of the transversality condition itself is drilled in [[Ex - Transversality in Finite Dimensions]].
