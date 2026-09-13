---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - A Covariant Derivative Determines a Connection on the Frame Bundle"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Christoffel Symbols"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Covariant Derivative along a Curve"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a smooth $n$-manifold with an affine connection (covariant derivative) $\nabla$ on its tangent bundle $TM$, and let $(x^1,\dots,x^n)$ be local coordinates on an open set $U\subseteq M$ with coordinate frame $\partial_k=\partial/\partial x^k$. The **Christoffel symbols** of $\nabla$ in this chart are the $n^3$ smooth functions $\Gamma^j_{ik}\colon U\to\mathbb R$ recording the second-order data of $\nabla$; we use Bär's index order,
$$\nabla_{\partial_k}\partial_i=\sum_{j=1}^{n}\Gamma^j_{ik}\,\partial_j,$$
so that the lower indices are, in order, the **differentiated** slot $i$ and the **direction** slot $k$, and $j$ is the component slot.

Let $\operatorname{Fr}(TM)\xrightarrow{\pi}M$ be the frame bundle of $TM$, a principal $GL(n;\mathbb R)$-bundle, and let $\omega\in\Omega^1(\operatorname{Fr}(TM);\mathfrak{gl}(n;\mathbb R))$ be the connection $1$-form on $\operatorname{Fr}(TM)$ that the covariant derivative $\nabla$ determines. The coordinate frame assembles into a local section
$$s=(\partial_1,\dots,\partial_n)\colon U\longrightarrow\operatorname{Fr}(TM),\qquad s(x)=\big(\partial_1|_x,\dots,\partial_n|_x\big),$$
which is a local gauge for $\operatorname{Fr}(TM)$ over $U$. Its pullback $A_s:=s^*\omega\in\Omega^1(U;\mathfrak{gl}(n;\mathbb R))$ is a matrix-valued $1$-form: for each $x$ and each tangent direction, $A_s$ returns an $n\times n$ real matrix with entries $(A_s)^j{}_i$.

**Prove that the entries of this local connection form are exactly the Christoffel symbols:**
$$\boxed{\big(s^*\omega(\partial_k)\big)^j{}_i=\Gamma^j_{ik}\qquad\text{for all }i,j,k\in\{1,\dots,n\}.}$$

In words: the object that Riemannian geometry calls "the Christoffel symbols" and the object that gauge theory calls "the gauge potential of the frame bundle" are the same $\mathfrak{gl}(n;\mathbb R)$-valued $1$-form, read off in the coordinate gauge. This is the identity that makes the Levi-Civita connection a special case of a principal connection.

**Recall:**

The objects in play are the frame bundle and its induced connection, the local connection form (gauge potential) of a principal connection, the connection matrix of a vector-bundle connection, and the Christoffel symbols.

![[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle#Statement]]

The single result this exercise is built on is the theorem **[[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]]**. Its content that we use: for every connection $\nabla$ on a vector bundle $E\to M$ there is a unique connection $1$-form $\omega$ on the frame bundle $\operatorname{Fr}(E)$ such that, for **every** local frame $e=(e_1,\dots,e_k)$ regarded as a local section $e\colon U\to\operatorname{Fr}(E)$,
$$e^*\omega=A(\nabla,e),$$
where $A(\nabla,e)$ is the connection matrix of $\nabla$ in the frame $e$. Equivalently (Bär's construction of the same $\omega$): for $X\in T_p\operatorname{Fr}(E)$ and any curve $t\mapsto p(t)=(p_1(t),\dots,p_k(t))$ of frames with $p(0)=p$ and $\dot p(0)=X$, the matrix $\omega(X)$ is determined by its action on the basis $p(0)$ through the covariant derivative along $c(t)=\pi(p(t))$,
$$\frac{\nabla}{dt}\Big|_{0}p_i(t)=\big(p(0)\cdot\omega(X)\big)_i=\sum_{j}p_j(0)\,\omega(X)^j{}_i,$$
and this value is independent of the chosen curve.

![[Def - Local Connection Form and Gauge Potential#The Definition]]

For a principal $G$-bundle $P\to M$ with connection $1$-form $\omega$ and a local section (gauge) $s\colon U\to P$, the **local connection form** is $A_s:=s^*\omega\in\Omega^1(U;\mathfrak g)$, so that $A_s(Y)=\omega(ds(Y))$ for $Y\in T_xU$. Here $G=GL(n;\mathbb R)$ and $\mathfrak g=\mathfrak{gl}(n;\mathbb R)=\operatorname{Mat}(n\times n;\mathbb R)$, so $A_s(Y)$ is an $n\times n$ matrix and $(A_s)^j{}_i$ denotes its $(j,i)$ entry.

![[Def - Connection Matrix and Local Form of a Connection#The Definition]]

For a connection $\nabla$ on a vector bundle $E\to M$ and a local frame $e=(e_1,\dots,e_k)$ (a row of sections), the **connection matrix** $A(\nabla,e)\in\Omega^1(U;\mathfrak{gl}(k))$ is defined by
$$\nabla e=e\cdot A(\nabla,e),\qquad\text{that is}\qquad \nabla e_i=\sum_{j}e_j\,A(\nabla,e)^j{}_i.$$
So the $(j,i)$ entry of $A(\nabla,e)$, evaluated on a vector field $Y$, is the coefficient of $e_j$ in $\nabla_Y e_i$.

![[Def - Christoffel Symbols#The Definition]]

The **Christoffel symbols** are the coordinate-frame components of $\nabla$. We write them with Bär's index convention $\nabla_{\partial_k}\partial_i=\sum_j\Gamma^j_{ik}\partial_j$; this is the same data as the Riemannian-geometry page's $\Gamma^k_{ij}$ (defined there by $\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k$) with the two lower indices in the opposite order — see the Convention callout in the Notation of the solution below.

> [!note] Convention: index order of the Christoffel symbols
> The page [[Def - Christoffel Symbols]] uses $\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k$ (direction slot first, differentiated slot second). Bär, whose theorem we are proving, uses $\nabla_{\partial_k}\partial_i=\Gamma^j_{ik}\partial_j$ (differentiated slot first, direction slot second). The two agree after swapping the two lower indices, that is Bär's $\Gamma^j_{ik}$ equals the other page's $\Gamma^j_{ki}$. For a torsion-free connection (in particular the Levi-Civita connection) the lower indices are symmetric and the distinction disappears; for a connection with torsion it must be tracked. We work in Bär's order throughout, so that the entry $(s^*\omega(\partial_k))^j{}_i$ carries the direction $k$ in the argument slot and the pair $(j,i)$ as the matrix indices.

---

# Convergent Strategy

**Problem class.** This is an *identification* problem: two constructions built in different languages — a Riemannian-geometry object (the array $\Gamma^j_{ik}$) and a gauge-theory object (the matrix-valued $1$-form $s^*\omega$) — are asserted to be equal, and the task is to unwind both definitions until the equality is a triviality. Problems of this kind are never solved by computation; they are solved by *correctly stating what each side means* and matching index for index. The whole difficulty is bookkeeping discipline: keeping the differentiated slot, the direction slot, and the component slot straight through two different notational systems.

**Assumption pattern.** The one substantive hypothesis is that the connection $1$-form $\omega$ on $\operatorname{Fr}(TM)$ is *the one induced by $\nabla$*, not some unrelated principal connection. This hypothesis enters through the defining property $e^*\omega=A(\nabla,e)$ of [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]], valid for every local frame. The recognisable trigger is that we are handed a specific frame — the coordinate frame $s=(\partial_1,\dots,\partial_n)$ — and asked for the components of $s^*\omega$; the response is to apply the "for every frame" property to *this* frame and then translate the connection matrix into coordinates.

**Theorem routing.** The route is a two-link chain. First, [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] converts $s^*\omega$ into the connection matrix $A(\nabla,s)$ of $\nabla$ in the coordinate frame: $s^*\omega=A(\nabla,s)$. Second, the definition [[Def - Connection Matrix and Local Form of a Connection]] converts the entries of $A(\nabla,s)$ into coefficients of $\nabla\partial_i$ in the coordinate basis: $A(\nabla,s)^j{}_i(\partial_k)$ is the coefficient of $\partial_j$ in $\nabla_{\partial_k}\partial_i$, which by [[Def - Christoffel Symbols]] is $\Gamma^j_{ik}$. Composing the two links gives the claim. As an independent check we also run Bär's alternative construction of $\omega$ (through the covariant derivative along a coordinate curve), which reaches the same entries without ever naming the connection matrix.

**Key decision point.** The one place a reader can go wrong is the *order of indices and the placement of the direction slot*. The connection matrix $A(\nabla,e)^j{}_i$ is defined by $\nabla e_i=\sum_j e_j A^j{}_i$, so the **lower** index $i$ of the matrix is the *differentiated* frame vector and the **upper** index $j$ is the *component*; the *direction* of differentiation is fed to the $1$-form separately, as its argument $\partial_k$. Matching this against $\Gamma^j_{ik}$ requires holding Bär's convention $\nabla_{\partial_k}\partial_i=\Gamma^j_{ik}\partial_j$ fixed. Get the convention right and the proof is three lines; get it wrong and the indices will appear transposed or the direction slot will land in the wrong place. Everything genuinely at stake in this exercise is that alignment.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic page's Legal Operations section will assign them numbers):

1. **Pull a principal connection back along a local gauge.** Given the connection $1$-form $\omega$ on the frame bundle and the coordinate section $s\colon U\to\operatorname{Fr}(TM)$, form the local connection form $A_s=s^*\omega$ over $U$. This is the operation "read a global principal connection in a chosen gauge", from [[Def - Local Connection Form and Gauge Potential]].

2. **Invoke the frame-bundle correspondence to replace $s^*\omega$ by a connection matrix.** Because $\omega$ is *the connection induced by $\nabla$*, the theorem [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] applies to the frame $s$ and gives $s^*\omega=A(\nabla,s)$. This is the load-bearing step: it is where the hypothesis "$\omega$ comes from $\nabla$" is used.

3. **Unwind a connection matrix into basis coefficients.** By the definition [[Def - Connection Matrix and Local Form of a Connection]], the entry $A(\nabla,s)^j{}_i(\partial_k)$ is the coefficient of $\partial_j$ in $\nabla_{\partial_k}\partial_i$.

4. **Read off Christoffel symbols from covariant derivatives of coordinate fields.** By the definition [[Def - Christoffel Symbols]] (in Bär's order), that coefficient is exactly $\Gamma^j_{ik}$.

5. **Cross-check with the covariant-derivative-along-a-curve construction.** As an independent verification, use the second (Bär) description of the same $\omega$ from [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]], evaluating $\omega$ on the velocity of the lifted coordinate curve $t\mapsto s(x_0+te_k)$ via [[Def - Covariant Derivative along a Curve]].

---

# Hints

> [!note]- Hint 1
> You are asked for the components of $s^*\omega$ in the coordinate gauge $s=(\partial_1,\dots,\partial_n)$. You are *not* expected to compute anything about the total space $\operatorname{Fr}(TM)$ directly. The connection $\omega$ is the one *induced by $\nabla$*; there is a theorem that says exactly what $e^*\omega$ is for any frame $e$. What does that theorem give when $e=s$?

> [!note]- Hint 2
> The theorem gives $s^*\omega=A(\nabla,s)$, the connection matrix of $\nabla$ in the coordinate frame. Now recall how the connection matrix is defined: $\nabla e=e\cdot A(\nabla,e)$, i.e. $\nabla e_i=\sum_j e_j A^j{}_i$. Apply this with $e_i=\partial_i$ and differentiate in the direction $\partial_k$. Which coefficient is $A^j{}_i(\partial_k)$?

> [!note]- Hint 3
> $A(\nabla,s)^j{}_i(\partial_k)$ is the coefficient of $\partial_j$ in $\nabla_{\partial_k}\partial_i$. By the very definition of the Christoffel symbols (in the convention $\nabla_{\partial_k}\partial_i=\sum_j\Gamma^j_{ik}\partial_j$), that coefficient is $\Gamma^j_{ik}$. That is the whole proof — the only thing to be careful about is the index order (see the Convention callout).

> [!note]- Hint 4
> If you want a proof that does not quote the connection-matrix identity but builds $\omega$ from scratch, use Bär's construction: take the coordinate curve $c(t)=x_0+te_k$ in the chart, lift it to the curve of frames $p(t)=s(c(t))$, and compute $\omega(\dot p(0))$ from $\frac{\nabla}{dt}\big|_0 p_i(t)=\nabla_{\partial_k}\partial_i$. Expanding in the basis $p(0)=(\partial_1,\dots,\partial_n)$ recovers the same entries $\Gamma^j_{ik}$.

---

# Solution

The proof is a chain of three definitional substitutions. The frame-bundle correspondence turns $s^*\omega$ into the connection matrix of $\nabla$ in the coordinate frame; the definition of the connection matrix turns its entries into coefficients of $\nabla_{\partial_k}\partial_i$ in the coordinate basis; and the definition of the Christoffel symbols names those coefficients $\Gamma^j_{ik}$. We then re-derive the same result directly from Bär's curve construction of $\omega$, so that the identity is seen to hold independently of the connection-matrix formalism.

**Notation for the solution.** Throughout, $\nabla$ is a connection on $TM$; $(x^1,\dots,x^n)$ are coordinates on $U$ with coordinate frame $\partial_k=\partial/\partial x^k$; $\Gamma^j_{ik}$ are the Christoffel symbols in Bär's order $\nabla_{\partial_k}\partial_i=\sum_j\Gamma^j_{ik}\partial_j$; $\operatorname{Fr}(TM)\xrightarrow{\pi}M$ is the frame bundle, a principal $GL(n;\mathbb R)$-bundle; $\omega\in\Omega^1(\operatorname{Fr}(TM);\mathfrak{gl}(n;\mathbb R))$ is the connection $1$-form induced by $\nabla$; $s=(\partial_1,\dots,\partial_n)\colon U\to\operatorname{Fr}(TM)$ is the coordinate section; and $A_s=s^*\omega$. For an $n\times n$ matrix $B$ we write $B^j{}_i$ for its $(j,i)$ entry (row $j$, column $i$).

**Step 1: Replace $s^*\omega$ by the connection matrix of $\nabla$ in the coordinate frame.**

Because $\omega$ is the connection induced by $\nabla$, the frame-bundle correspondence applies to the coordinate frame $s$ and gives $s^*\omega=A(\nabla,s)$.

> [!note]- Derivation
> We must show $\big(s^*\omega(\partial_k)\big)^j{}_i=\Gamma^j_{ik}$ for all $i,j,k$, given that $\omega$ is the connection $1$-form on $\operatorname{Fr}(TM)$ *induced by* the covariant derivative $\nabla$.
>
> By the theorem [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] — restated: for every connection $\nabla$ on $E\to M$ there is a unique connection $\omega$ on $\operatorname{Fr}(E)$ with $e^*\omega=A(\nabla,e)$ for **every** local frame $e$ — applied to the tangent bundle $E=TM$ and to the frame $e=s=(\partial_1,\dots,\partial_n)$, we obtain
> $$s^*\omega=A(\nabla,s)\qquad\text{(defining property of the induced connection, applied to the coordinate frame }s\text{).}$$
> This is the only step in which the hypothesis "$\omega$ is induced by $\nabla$" is used; without it the left-hand side would be an arbitrary $\mathfrak{gl}(n;\mathbb R)$-valued form with no relation to $\nabla$.

**Step 2: Unwind the connection matrix into coefficients of $\nabla_{\partial_k}\partial_i$.**

The $(j,i)$ entry of the connection matrix, evaluated on the direction $\partial_k$, is the coefficient of $\partial_j$ in $\nabla_{\partial_k}\partial_i$.

> [!note]- Derivation
> By the definition of the connection matrix, [[Def - Connection Matrix and Local Form of a Connection]] — restated: $A(\nabla,e)$ is characterised by $\nabla e_i=\sum_j e_j\,A(\nabla,e)^j{}_i$ — applied to the coordinate frame $e=s$, whose $i$-th member is $s_i=\partial_i$, we have for each direction $Y\in\mathfrak X(U)$
> $$\nabla_Y\partial_i=\sum_{j=1}^{n}\partial_j\,A(\nabla,s)^j{}_i(Y)\qquad\text{(definition of the connection matrix in the frame }s\text{).}$$
> Setting $Y=\partial_k$ and reading off the coefficient of $\partial_j$ on both sides,
> $$A(\nabla,s)^j{}_i(\partial_k)=\big[\text{coefficient of }\partial_j\text{ in }\nabla_{\partial_k}\partial_i\big]\qquad\text{(comparing coefficients in the basis }(\partial_1,\dots,\partial_n)\text{, which is legitimate because a coordinate frame is pointwise a basis).}$$
> The comparison of coefficients is valid because $(\partial_1|_x,\dots,\partial_n|_x)$ is a basis of $T_xM$ at every $x\in U$, so the expansion of the vector $\nabla_{\partial_k}\partial_i$ in this basis is unique.

**Step 3: Name the coefficient the Christoffel symbol.**

That coefficient is, by definition, $\Gamma^j_{ik}$; combining with Steps 1–2 gives the claim.

> [!note]- Derivation
> By the definition of the Christoffel symbols, [[Def - Christoffel Symbols]], in Bär's index order,
> $$\nabla_{\partial_k}\partial_i=\sum_{j=1}^{n}\Gamma^j_{ik}\,\partial_j\qquad\text{(definition of }\Gamma^j_{ik}\text{),}$$
> so the coefficient of $\partial_j$ in $\nabla_{\partial_k}\partial_i$ is exactly $\Gamma^j_{ik}$. Substituting this into the conclusion of Step 2,
> $$A(\nabla,s)^j{}_i(\partial_k)=\Gamma^j_{ik}\qquad\text{(Step 2 and the definition of }\Gamma^j_{ik}\text{).}$$
> Finally, combining with the identity $s^*\omega=A(\nabla,s)$ from Step 1,
> $$\big(s^*\omega(\partial_k)\big)^j{}_i=A(\nabla,s)^j{}_i(\partial_k)=\Gamma^j_{ik}\qquad\text{(Step 1, then the previous line).}$$
> This holds for all $i,j,k\in\{1,\dots,n\}$, which is the required identity.

**Step 4 (independent check): the same entries from the curve construction of $\omega$.**

Without invoking the connection-matrix identity, evaluate $\omega$ directly on the velocity of the lifted coordinate curve; the entries come out as $\Gamma^j_{ik}$ again.

> [!note]- Derivation
> The theorem [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] gives a second description of the same $\omega$: for $X\in T_p\operatorname{Fr}(TM)$ and any curve $t\mapsto p(t)=(p_1(t),\dots,p_n(t))$ of frames with $p(0)=p$ and $\dot p(0)=X$, the matrix $\omega(X)$ is fixed by
> $$\frac{\nabla}{dt}\Big|_{0}p_i(t)=\big(p(0)\cdot\omega(X)\big)_i=\sum_{j}p_j(0)\,\omega(X)^j{}_i,$$
> where $\frac{\nabla}{dt}$ is the covariant derivative along the base curve $c(t)=\pi(p(t))$, and $\omega(X)$ does not depend on the choice of curve.
>
> Fix $x_0\in U$ and the direction $\partial_k|_{x_0}$. Take the coordinate curve in the chart,
> $$c(t)=x_0+t\,e_k\in U\qquad(\text{so }\dot c(0)=\partial_k|_{x_0}),$$
> and lift it through the section $s$ to the curve of frames
> $$p(t):=s(c(t))=\big(\partial_1|_{c(t)},\dots,\partial_n|_{c(t)}\big),\qquad\dot p(0)=ds(\partial_k|_{x_0})=:X.$$
> Here $p_i(t)=\partial_i|_{c(t)}$ is a section of $c^*TM$, whose covariant derivative along $c$ is, by [[Def - Covariant Derivative along a Curve]] and the compatibility of $\frac{\nabla}{dt}$ with $\nabla$ on the extended field $\partial_i$,
> $$\frac{\nabla}{dt}\Big|_{0}p_i(t)=\nabla_{\dot c(0)}\partial_i=\nabla_{\partial_k}\partial_i\qquad\text{(covariant derivative along a curve equals }\nabla_{\dot c}\text{ of an extending field; }\dot c(0)=\partial_k\text{).}$$
> By the definition of $\Gamma^j_{ik}$ this equals $\sum_j\Gamma^j_{ik}\partial_j|_{x_0}=\sum_j\Gamma^j_{ik}\,p_j(0)$. Comparing with the defining relation $\frac{\nabla}{dt}\big|_0 p_i=\sum_j p_j(0)\,\omega(X)^j{}_i$ and using that $(p_1(0),\dots,p_n(0))=(\partial_1|_{x_0},\dots,\partial_n|_{x_0})$ is a basis, we read off
> $$\omega(X)^j{}_i=\Gamma^j_{ik}\qquad\text{(uniqueness of the expansion in the basis }p(0)\text{).}$$
> Since $X=ds(\partial_k|_{x_0})$ we have $\omega(X)=\omega(ds(\partial_k))=s^*\omega(\partial_k)$, so $\big(s^*\omega(\partial_k)\big)^j{}_i=\Gamma^j_{ik}$, in agreement with Step 3. This confirms the identity through the geometric definition of $\omega$, independently of the connection-matrix bookkeeping.

> [!note]- Complete formal solution
> **Claim.** Let $\nabla$ be a connection on $TM$ with Christoffel symbols $\Gamma^j_{ik}$ (Bär's order, $\nabla_{\partial_k}\partial_i=\sum_j\Gamma^j_{ik}\partial_j$) in coordinates $(x^1,\dots,x^n)$ on $U$, let $\omega$ be the connection $1$-form induced by $\nabla$ on the frame bundle $\operatorname{Fr}(TM)$, and let $s=(\partial_1,\dots,\partial_n)$ be the coordinate section. Then $\big(s^*\omega(\partial_k)\big)^j{}_i=\Gamma^j_{ik}$ for all $i,j,k$.
>
> By [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]], the induced connection $\omega$ satisfies $e^*\omega=A(\nabla,e)$ for every local frame $e$; applying this to $e=s$ gives
> $$s^*\omega=A(\nabla,s).$$
> By the definition of the connection matrix, $\nabla\partial_i=\sum_j\partial_j\,A(\nabla,s)^j{}_i$; evaluating on the direction $\partial_k$ and comparing coefficients in the basis $(\partial_1,\dots,\partial_n)$,
> $$A(\nabla,s)^j{}_i(\partial_k)=\big[\text{coefficient of }\partial_j\text{ in }\nabla_{\partial_k}\partial_i\big]=\Gamma^j_{ik},$$
> the last equality by the definition of $\Gamma^j_{ik}$. Combining,
> $$\big(s^*\omega(\partial_k)\big)^j{}_i=A(\nabla,s)^j{}_i(\partial_k)=\Gamma^j_{ik}.$$
> This holds for all $i,j,k\in\{1,\dots,n\}$, so the coordinate-frame local connection form of $\operatorname{Fr}(TM)$ has the Christoffel symbols as its matrix entries. $\blacksquare$

> [!warning] Illegal but tempting: forgetting that $\omega$ must be *the induced* connection
> One is tempted to prove the identity from the definition of $s^*\omega$ alone: "$s^*\omega(\partial_k)=\omega(ds(\partial_k))$, and $\omega$ is a $\mathfrak{gl}(n)$-valued form, so its entries are some functions — call them $\Gamma^j_{ik}$." This is circular: it *names* the entries $\Gamma^j_{ik}$ but never connects them to $\nabla_{\partial_k}\partial_i$. The identity is a *theorem*, not a definition, precisely because $\omega$ on $\operatorname{Fr}(TM)$ is an object built from $\nabla$ by [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]]; if one took an *arbitrary* principal connection $\omega'$ on $\operatorname{Fr}(TM)$ (of which there are many, an affine space's worth), its coordinate-gauge entries would be some other functions with no relation to $\nabla$'s Christoffel symbols. The hypothesis that must appear is "$\omega$ is induced by $\nabla$", and it appears exactly once, in Step 1.

An independent sanity check on the abelian toy case: on $\mathbb R^n$ with the flat connection in Cartesian coordinates, $\nabla_{\partial_k}\partial_i=0$, so all $\Gamma^j_{ik}=0$; correspondingly the coordinate frame $s$ is $\nabla$-parallel, so $\nabla s_i=0$, the connection matrix $A(\nabla,s)$ vanishes, and $s^*\omega=0$ — both sides are zero, as they must be.

---

# Key Takeaways

**The Christoffel symbols are not a three-index tensor; they are the matrix entries of a gauge potential, and this exercise is the identity that says so.** The array $\Gamma^j_{ik}$ transforms inhomogeneously under a change of coordinates — the offending $\partial^2 x/\partial x'^2$ term — which is exactly the behaviour of a local connection form $A_s=s^*\omega$ under a change of gauge, $A_{s'}=\operatorname{Ad}_{g^{-1}}A_s+g^*\theta$ (the pure-gauge term $g^*\theta$ being the source of the second-derivative piece). Once one has proved $\big(s^*\omega(\partial_k)\big)^j{}_i=\Gamma^j_{ik}$, the mysterious transformation law of the Christoffel symbols is demystified: it *is* the transformation law of the frame-bundle connection under the coordinate-frame change $s'=s\cdot(\partial x/\partial x')$ (the transition matrix has entries $(\partial x^a/\partial x'^i)$, because $\partial'_i=\sum_a(\partial x^a/\partial x'^i)\,\partial_a$), specialised to $G=GL(n;\mathbb R)$. The trigger for using this identity is any moment when a Riemannian-geometry computation (geodesics, curvature, parallel transport) needs to be recognised as a gauge-theory computation, or vice versa: the dictionary entry is "Christoffel symbols $=$ gauge potential of $\operatorname{Fr}(TM)$".

**The reusable move is: to compute a principal connection in a chosen gauge, pull it back through the section and quote the correspondence theorem, never wrestle with the total space.** A connection $1$-form $\omega$ lives on the total space $\operatorname{Fr}(TM)$, an $n+n^2$-dimensional manifold; computing with it directly is unpleasant. The section $s$ collapses that computation onto the base: $A_s=s^*\omega$ is an ordinary matrix-valued $1$-form on $U\subseteq M$, and every downstream object (curvature $F_s=dA_s+\tfrac12[A_s\wedge A_s]$, gauge transformations, parallel transport) is computed from $A_s$. The identity $s^*\omega=A(\nabla,s)$ is what makes the pullback tractable in the frame-bundle case: it says the pullback in the coordinate gauge is *already computed for you* — it is the connection matrix, i.e. the Christoffel symbols. Whenever a problem asks for "the local connection form of the frame bundle in such-and-such frame", the diagnostic is to write down the connection matrix of $\nabla$ in that frame; no bundle-theoretic labour is needed.

**Index discipline is the entire content of an identification proof, and the safe habit is to fix one convention and name the three slots.** This proof has no analytic difficulty; its only failure mode is an index transposition. The durable lesson is to name the roles — differentiated slot, direction slot, component slot — rather than trusting the raised/lowered pattern, because different sources permute them. Bär's $\Gamma^j_{ik}$ places (component, differentiated, direction); the Riemannian-geometry page's $\Gamma^k_{ij}$ places (component, direction, differentiated); the connection matrix $A^j{}_i$ hides the direction in the $1$-form's argument. Getting the identity right is exactly the discipline of matching these role-by-role, and the Convention callout at the top of the solution exists precisely so that a reader returning to this page after months re-establishes the alignment in one glance. The transferable diagnostic: whenever two "obviously equal" tensors refuse to match, the culprit is almost always an unstated index-order convention, not a mathematical error. The companion exercise [[Ex - Curvature of the Connection Induced on the Frame Bundle by the Levi-Civita Connection]] carries the same identification one derivative further, matching the frame-bundle curvature form to Cartan's curvature $2$-forms.
