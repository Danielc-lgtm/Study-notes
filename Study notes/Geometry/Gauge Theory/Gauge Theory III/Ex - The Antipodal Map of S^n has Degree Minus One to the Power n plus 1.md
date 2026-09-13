---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Def - Brouwer Degree of a Map"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Manifold with Boundary and Induced Orientation"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $n\ge 1$ and let
$$S^n=\{\,x=(x_1,\dots,x_{n+1})\in\mathbb R^{n+1}:\lVert x\rVert=1\,\}$$
be the unit sphere, carrying its **standard orientation** as the boundary of the closed unit ball $\overline{B^{n+1}}$ with the outward-normal-first convention: a basis $(v_1,\dots,v_n)$ of the tangent space $T_pS^n$ is declared positively oriented if and only if $(p,v_1,\dots,v_n)$ is a positively oriented basis of $\mathbb R^{n+1}$ (with $\mathbb R^{n+1}$ given its standard orientation, in which the ordered standard basis $(e_1,\dots,e_{n+1})$ is positive). Here $\lVert\cdot\rVert$ is the Euclidean norm and $p\in S^n$ is the outward unit normal to $S^n$ at $p$.

Let $a\colon S^n\to S^n$ be the **antipodal map**,
$$a(x)=-x .$$

**Prove that** $\deg a=(-1)^{n+1}$, where $\deg$ is the Brouwer degree of a smooth self-map of a closed oriented manifold.

The intended route has two moves. First, show that a single-coordinate reflection $r\colon S^n\to S^n$ — the restriction to the sphere of the linear map that negates one coordinate of $\mathbb R^{n+1}$ — has degree $-1$, by evaluating the regular-value formula for the degree at one point and checking the orientation sign there. Second, observe that the antipodal map is the composition of $n+1$ such reflections, one per coordinate, and apply multiplicativity of the degree under composition to conclude $\deg a=(-1)^{n+1}$.

**Recall:**

The objects in play are the Brouwer degree, its regular-value formula, its behaviour under composition, and the orientation of the sphere. We restate each here so that the page is self-contained.

![[Def - Brouwer Degree of a Map#The Definition]]

For closed oriented $n$-manifolds $M,N$ with $N$ connected and a smooth map $f\colon M\to N$, the **[[Def - Brouwer Degree of a Map|Brouwer degree]]** is $\deg f=\int_M f^*\omega$ for any $\omega\in\Omega^n(N)$ with $\int_N\omega=1$; it is an integer independent of the choice of $\omega$.

![[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant#Statement]]

The two clauses this exercise uses are the following. **The regular-value formula (b):** for every regular value $y\in N$ of $f$, the preimage $f^{-1}(y)$ is finite and
$$\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x ,$$
where each sign $\operatorname{sign}\det df_x$ is computed by writing the linear isomorphism $df_x\colon T_xM\to T_yN$ in a positively oriented basis of $T_xM$ and a positively oriented basis of $T_yN$ and taking the sign of the determinant of the resulting matrix — equivalently, the sign is $+1$ if $df_x$ carries positive bases to positive bases and $-1$ if it reverses orientation. **Multiplicativity (e):** if $P$ is a further closed connected oriented $n$-manifold and $g\colon N\to P$ is smooth, then $\deg(g\circ f)=\deg g\cdot\deg f$.

![[Def - Orientation of a Smooth Manifold#The Definition]]

The sphere's orientation is fixed by the **induced boundary orientation** of $S^n=\partial\overline{B^{n+1}}$; the outward-normal-first rule stated in the problem is exactly the convention of [[Def - Manifold with Boundary and Induced Orientation|the induced boundary orientation]] applied to the unit ball, and it is the standing orientation of every sphere in this series (it is also the orientation under which $S^3=SU(2)$ is oriented as the boundary of the unit ball in $\mathbb H=\mathbb R^4$).

---

# Convergent Strategy

**Problem class.** This is a *compute-an-invariant* problem: we are asked for the exact value of a topological invariant, the degree, of a specific map. The productive stance for such problems is never to compute the defining integral $\int_{S^n}a^*\omega$ directly — that requires choosing a form and pushing it through the antipodal map — but to reach for the *combinatorial* formula for the degree, the signed count of preimages of a regular value, and to decompose the map into pieces whose degrees are transparent. The degree of a diffeomorphism is the simplest instance: a diffeomorphism has exactly one preimage over any point and its differential is everywhere invertible, so the entire invariant collapses to a single orientation sign, $\pm 1$.

**Assumption pattern.** The recognisable trigger is that $a$ is an *orthogonal linear map restricted to the sphere*, hence a diffeomorphism of $S^n$, and that it *factors through simpler orthogonal maps*. Whenever a map whose degree we want is a diffeomorphism, the regular-value formula degenerates to a one-term sum and the problem is purely a question of orientation. Whenever such a map factors as a composition, multiplicativity turns one hard degree into a product of easy ones. The antipodal map $x\mapsto-x$ is the linear map $-I_{n+1}$ restricted to $S^n$, and $-I_{n+1}=R_1R_2\cdots R_{n+1}$ where $R_i$ negates the $i$-th coordinate; both triggers fire.

**Theorem routing.** The route is: (i) identify the coordinate reflection $r=R_1|_{S^n}$ as a diffeomorphism of $S^n$, so that every point is a regular value with a single preimage; (ii) apply the *regular-value formula* — clause (b) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] — at that one preimage, reducing $\deg r$ to the single sign $\operatorname{sign}\det dr_x$; (iii) compute that sign from the *outward-normal-first orientation convention* by comparing the orientations of $\mathbb R^{n+1}$ before and after applying $R_1$, obtaining $\deg r=-1$; (iv) write $a=r_1\circ\cdots\circ r_{n+1}$ as a composition of $n+1$ coordinate reflections and apply *multiplicativity* — clause (e) — to get $\deg a=(-1)^{n+1}$.

**Key decision point.** The single non-obvious move is *how the orientation sign of a reflection on the sphere is read off from the reflection of the ambient space*. A reflection $R_1$ of $\mathbb R^{n+1}$ has $\det R_1=-1$; the temptation is to declare "so its restriction reverses the orientation of $S^n$" without argument. That inference is correct but needs the boundary-orientation convention to be made explicit, because the tangent map $dr_p$ acts on the $n$-dimensional space $T_pS^n$, not on $\mathbb R^{n+1}$, and the missing dimension is the *normal* direction, which $R_1$ also acts on. The decisive computation is that $R_1$ sends the outward normal $p$ at a point to the outward normal $R_1p$ at the image point (since $R_1$ is orthogonal, $R_1p$ is again a unit vector and it is the position vector of $r(p)$, hence the outward normal there), so the $-1$ in $\det R_1$ lands entirely on the tangential part. That is why a coordinate reflection reverses the sphere's orientation and has degree $-1$.

---

# Legal Operations Used

The topic page for this section is not yet written; the operations are named descriptively and the orchestrator will reconcile the numbering with the topic page's Legal Operations list.

1. **Reduce the degree of a diffeomorphism to a single orientation sign.** When the map $f$ whose degree is wanted is a diffeomorphism, every point of the target is a regular value (the differential is everywhere an isomorphism) and has exactly one preimage; the regular-value formula therefore collapses from a sum to the single term $\operatorname{sign}\det df_x$. Here $f$ is a coordinate reflection or the antipodal map, both diffeomorphisms of $S^n$.

2. **Read a tangential orientation sign off the ambient linear map via the outward-normal-first convention.** For a map of the sphere induced by an orthogonal linear map $A$ of $\mathbb R^{n+1}$, prepend the (image) outward normal to a tangent basis, use that $A$ carries the outward normal at $p$ to the outward normal at the image point, and factor the determinant so that the ambient sign $\det A$ equals the tangential sign. This converts $\det A$ on $\mathbb R^{n+1}$ into $\operatorname{sign}\det (dA|_{T_pS^n})$ on the sphere.

3. **Factor an orthogonal map into a product of coordinate reflections.** The map $-I_{n+1}$ is the product $R_1\cdots R_{n+1}$ of the $n+1$ single-coordinate reflections; restricting to the sphere, $a=r_1\circ\cdots\circ r_{n+1}$. This exhibits the target map as a composition of maps of known degree.

4. **Apply multiplicativity of the degree under composition.** Clause (e) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] gives $\deg(g\circ f)=\deg g\cdot\deg f$; iterating over the $n+1$ reflection factors turns the product of degrees into $(-1)^{n+1}$.

---

# Hints

> [!note]- Hint 1
> Do not try to integrate. The degree of a diffeomorphism is computed by the *regular-value formula*: pick any point $y$, look at its preimages, and add up $\operatorname{sign}\det df_x$ over them. How many preimages does a diffeomorphism have over a point, and is every point a regular value?

> [!note]- Hint 2
> The antipodal map $x\mapsto-x$ is $-I_{n+1}$ restricted to the sphere. The linear map $-I_{n+1}$ factors as $R_1R_2\cdots R_{n+1}$, where $R_i$ flips the sign of the $i$-th coordinate and fixes the rest. Each $R_i$ restricts to a diffeomorphism $r_i$ of $S^n$. If you knew $\deg r_i$, what would multiplicativity of the degree give you for $\deg a$?

> [!note]- Hint 3
> Compute $\deg r$ for a single coordinate reflection $r=R_1|_{S^n}$. At a fixed point $p\in S^n$, take a positively oriented basis $(v_1,\dots,v_n)$ of $T_pS^n$; by the outward-normal-first convention this means $(p,v_1,\dots,v_n)$ is positive in $\mathbb R^{n+1}$. Apply $R_1$ to the whole list. Two facts: $R_1p$ is the outward normal at $r(p)$, and $\det R_1=-1$. What is the orientation of $(dr_p v_1,\dots,dr_p v_n)$ in $T_{r(p)}S^n$?

> [!note]- Hint 4
> Applying the linear map $R_1$ to the ordered basis $(p,v_1,\dots,v_n)$ multiplies its orientation by $\det R_1=-1$, so $(R_1p,R_1v_1,\dots,R_1v_n)$ is *negatively* oriented in $\mathbb R^{n+1}$. But $R_1p$ is the outward normal at $r(p)$, so by the same convention $(R_1v_1,\dots,R_1v_n)=(dr_p v_1,\dots,dr_p v_n)$ is a *negatively* oriented basis of $T_{r(p)}S^n$. Hence $dr_p$ carries a positive basis to a negative one: $\operatorname{sign}\det dr_p=-1$, so $\deg r=-1$. Now feed this into multiplicativity across $n+1$ factors.

---

# Solution

The plan is to compute the degree of one coordinate reflection and then assemble the antipodal map out of $n+1$ of them. A coordinate reflection is a diffeomorphism of the sphere, so its degree is a single orientation sign, which the outward-normal-first convention pins to $-1$; the antipodal map factors as the composition of the $n+1$ coordinate reflections, so multiplicativity of the degree returns the product $(-1)^{n+1}$. Every step uses only clauses (b) and (e) of the degree theorem, restated in the Recall.

**Step 1: The coordinate reflections are diffeomorphisms of the sphere, so each is a one-preimage, everywhere-regular map.**

For $i\in\{1,\dots,n+1\}$ let $R_i\colon\mathbb R^{n+1}\to\mathbb R^{n+1}$ negate the $i$-th coordinate and fix the others. Each $R_i$ is orthogonal, restricts to a diffeomorphism $r_i=R_i|_{S^n}\colon S^n\to S^n$, and has the property that every point of $S^n$ is a regular value of $r_i$ with a single preimage.

> [!note]- Derivation
> Fix $i$ and write $R=R_i$, $r=r_i$. In coordinates $R(x_1,\dots,x_{n+1})=(x_1,\dots,-x_i,\dots,x_{n+1})$. The map $R$ is linear with matrix $\operatorname{diag}(1,\dots,1,-1,1,\dots,1)$ (the $-1$ in position $i$), so it is smooth, invertible, and orthogonal: for all $x$,
> $$\lVert Rx\rVert^2=\sum_{j\ne i}x_j^2+(-x_i)^2=\sum_{j=1}^{n+1}x_j^2=\lVert x\rVert^2\qquad\text{(the sign on }x_i\text{ is squared away).}$$
> In particular $\lVert x\rVert=1$ implies $\lVert Rx\rVert=1$, so $R$ maps $S^n$ into $S^n$; and $R^2=\operatorname{id}$ (negating twice restores the coordinate), so $R$ is its own inverse and $r=R|_{S^n}$ is a smooth bijection of $S^n$ with smooth inverse $r$ itself. Hence $r$ is a **diffeomorphism** of $S^n$.
>
> Because $r$ is a diffeomorphism, its differential $dr_p\colon T_pS^n\to T_{r(p)}S^n$ is a linear isomorphism at every $p\in S^n$ (a diffeomorphism has invertible differential everywhere, by the chain rule applied to $r\circ r^{-1}=\operatorname{id}$). Therefore *every* point $y\in S^n$ is a regular value of $r$ (there are no critical points at all), and since $r$ is a bijection the preimage $r^{-1}(y)$ is the single point $\{r^{-1}(y)\}=\{r(y)\}$ (using $r^{-1}=r$). The regular-value formula (b) thus reduces to a single summand for $r$.

**Step 2: A single coordinate reflection has degree $-1$.**

Evaluating the regular-value formula at any point and computing the one orientation sign from the outward-normal-first convention gives $\deg r_i=-1$ for each $i$.

> [!note]- Derivation
> Fix $i$, write $R=R_i$ and $r=r_i$, and fix any point $p\in S^n$; set $q=r(p)=Rp\in S^n$, so that $p$ is the unique preimage $r^{-1}(q)$ (Step 1, using $r^{-1}=r$ and $r(q)=R^2p=p$). By clause (b) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] evaluated at the regular value $q$,
> $$\deg r=\sum_{x\in r^{-1}(q)}\operatorname{sign}\det dr_x=\operatorname{sign}\det dr_p\qquad\text{(single preimage, by Step 1).}$$
> It remains to compute this one sign. The differential of the *linear* map $R$ at any point is $R$ itself, and it carries $T_pS^n$ isomorphically onto $T_qS^n$, so $dr_p=R|_{T_pS^n}\colon T_pS^n\to T_qS^n$.
>
> Choose a **positively oriented** basis $(v_1,\dots,v_n)$ of $T_pS^n$. By the outward-normal-first convention (the standing orientation of $S^n$; see [[Def - Manifold with Boundary and Induced Orientation|the induced boundary orientation]]), this is equivalent to the statement
> $$(p,v_1,\dots,v_n)\ \text{is a positively oriented basis of }\mathbb R^{n+1}\qquad\text{(normal }p\text{ prepended).}$$
> Apply the linear map $R$ to this entire ordered $(n+1)$-tuple. A linear map multiplies the orientation of any ordered basis by the sign of its determinant, so
> $$(Rp,Rv_1,\dots,Rv_n)\ \text{has orientation}\ \det R\cdot(+1)=-1\ \text{in }\mathbb R^{n+1}\qquad\text{(since }\det R=-1\text{; the tuple }(p,v_1,\dots,v_n)\text{ was positive).}$$
> Now read this back on the sphere. First, $Rp=q$ is the *outward normal* at $q$: it is a unit vector (Step 1, $R$ orthogonal) and it is the position vector of the point $q=Rp\in S^n$, and the outward normal to $S^n$ at a point is exactly that point's position vector. Second, $Rv_j=dr_p v_j\in T_qS^n$ for each $j$, because $R$ maps $T_pS^n$ onto $T_qS^n$ and its restriction is $dr_p$. So the tuple $(Rp,Rv_1,\dots,Rv_n)$ is precisely
> $$(\text{outward normal at }q,\ dr_p v_1,\dots,dr_p v_n),$$
> and it is negatively oriented in $\mathbb R^{n+1}$. By the outward-normal-first convention *again*, this says that
> $$(dr_p v_1,\dots,dr_p v_n)\ \text{is a negatively oriented basis of }T_qS^n .$$
> Thus $dr_p$ sends the positively oriented basis $(v_1,\dots,v_n)$ of $T_pS^n$ to a negatively oriented basis of $T_qS^n$: its determinant relative to positive bases is negative, i.e. $\operatorname{sign}\det dr_p=-1$. Combining with the displayed reduction,
> $$\deg r=\operatorname{sign}\det dr_p=-1 .$$
> The sign is the same at every point $p$, as it must be, since the degree is a single number; the computation used no special feature of $p$.

**Step 3: The antipodal map is the composition of the $n+1$ coordinate reflections.**

The map $a\colon S^n\to S^n$, $a(x)=-x$, equals $r_1\circ r_2\circ\cdots\circ r_{n+1}$.

> [!note]- Derivation
> The antipodal map is the restriction to $S^n$ of the linear map $-I_{n+1}\colon\mathbb R^{n+1}\to\mathbb R^{n+1}$, $x\mapsto-x$, which does map $S^n$ to $S^n$ since $\lVert-x\rVert=\lVert x\rVert$. As linear maps,
> $$-I_{n+1}=\operatorname{diag}(-1,-1,\dots,-1)=R_1R_2\cdots R_{n+1},$$
> because the right-hand side is the diagonal matrix whose $j$-th entry is the product of the $j$-th diagonal entries of the $R_i$: only $R_j$ contributes a $-1$ in position $j$ and every other $R_i$ contributes $+1$ there, so the $(j,j)$ entry of the product is $-1$ for each $j$. The $R_i$ are diagonal, hence commute, so the order of the product is immaterial. Restricting the identity $-I_{n+1}=R_1\cdots R_{n+1}$ of linear maps to the invariant subset $S^n$ gives the identity of self-maps of the sphere
> $$a=r_1\circ r_2\circ\cdots\circ r_{n+1}\qquad\text{(restriction of a composition is the composition of restrictions).}$$

**Step 4: Multiplicativity of the degree over the $n+1$ factors gives $(-1)^{n+1}$.**

Applying clause (e) $n$ times to the composition of Step 3 and inserting $\deg r_i=-1$ from Step 2 yields $\deg a=(-1)^{n+1}$.

> [!note]- Derivation
> Each $r_i$ is a smooth self-map of the closed connected oriented $n$-manifold $S^n$ (connected since $n\ge 1$), so clause (e) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] — $\deg(g\circ f)=\deg g\cdot\deg f$ for smooth maps between closed connected oriented $n$-manifolds — applies to any two of them and, by induction on the number of factors, to their composition. Writing $a=r_1\circ(r_2\circ\cdots\circ r_{n+1})$ and peeling one factor at a time,
> $$\deg a=\deg r_1\cdot\deg r_2\cdots\deg r_{n+1}\qquad\text{(multiplicativity (e), applied }n\text{ times).}$$
> By Step 2 every factor equals $-1$, and there are $n+1$ of them, so
> $$\deg a=(-1)^{n+1}\qquad\text{(product of }n+1\text{ copies of }-1\text{).}$$

> [!note]- Complete formal solution
> **Claim.** For $n\ge 1$ the antipodal map $a\colon S^n\to S^n$, $a(x)=-x$, has $\deg a=(-1)^{n+1}$.
>
> For $i\in\{1,\dots,n+1\}$ let $R_i\colon\mathbb R^{n+1}\to\mathbb R^{n+1}$ negate the $i$-th coordinate and fix the rest; it is orthogonal, satisfies $R_i^2=\operatorname{id}$, and preserves $\lVert\cdot\rVert$, so it restricts to a diffeomorphism $r_i=R_i|_{S^n}$ of $S^n$ with $r_i^{-1}=r_i$.
>
> *Degree of one reflection.* Fix $i$; write $R=R_i$, $r=r_i$. Since $r$ is a diffeomorphism, its differential is an isomorphism at every point, so every $q\in S^n$ is a regular value with the single preimage $r^{-1}(q)=\{r(q)\}$. By the regular-value formula (clause (b) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the Brouwer degree theorem]]), for $p=r(q)$,
> $$\deg r=\operatorname{sign}\det dr_p,\qquad dr_p=R|_{T_pS^n}\colon T_pS^n\to T_{q}S^n\ \ (q=Rp).$$
> Take a positively oriented basis $(v_1,\dots,v_n)$ of $T_pS^n$; by the outward-normal-first convention $(p,v_1,\dots,v_n)$ is positive in $\mathbb R^{n+1}$. Applying $R$ multiplies the orientation by $\det R=-1$, so $(Rp,Rv_1,\dots,Rv_n)$ is negative in $\mathbb R^{n+1}$. But $Rp=q$ is the outward normal at $q$ (a unit vector equal to the position vector of $q$) and $Rv_j=dr_p v_j\in T_qS^n$; hence, by the same convention, $(dr_pv_1,\dots,dr_pv_n)$ is a negatively oriented basis of $T_qS^n$. Therefore $\operatorname{sign}\det dr_p=-1$ and $\deg r=-1$.
>
> *Factorisation.* As linear maps $-I_{n+1}=R_1\cdots R_{n+1}$, since the $(j,j)$ entry of the product is the single $-1$ contributed by $R_j$. Restricting to $S^n$, the antipodal map factors as $a=r_1\circ\cdots\circ r_{n+1}$.
>
> *Conclusion.* Each $r_i$ is a smooth self-map of the closed connected oriented $n$-manifold $S^n$, so multiplicativity (clause (e)) applied $n$ times gives $\deg a=\prod_{i=1}^{n+1}\deg r_i=(-1)^{n+1}$. $\blacksquare$

> [!note]- Independent sanity check — a direct one-map computation
> One can avoid the factorisation and compute $\deg a$ in a single stroke, which is a useful cross-check on the sign. The antipodal map is the diffeomorphism $-I_{n+1}|_{S^n}$, so as in Step 2 the regular-value formula gives $\deg a=\operatorname{sign}\det da_p$ at any $p$, with $da_p=(-I_{n+1})|_{T_pS^n}$. Take a positive basis $(v_1,\dots,v_n)$ of $T_pS^n$, so $(p,v_1,\dots,v_n)$ is positive in $\mathbb R^{n+1}$; applying $-I_{n+1}$ multiplies the orientation by $\det(-I_{n+1})=(-1)^{n+1}$, giving that $(-p,-v_1,\dots,-v_n)$ has orientation $(-1)^{n+1}$. Now $-p=a(p)$ is the outward normal at $a(p)$, so $(-v_1,\dots,-v_n)=(da_pv_1,\dots,da_pv_n)$ is a basis of $T_{a(p)}S^n$ of orientation $(-1)^{n+1}$. Hence $\operatorname{sign}\det da_p=(-1)^{n+1}=\deg a$, agreeing with the factorised computation.

> [!warning] Illegal but tempting shortcut: "$a$ reverses orientation because $\det(-I_{n+1})=(-1)^{n+1}$."
> The equality $\det(-I_{n+1})=(-1)^{n+1}$ is a statement about the $(n+1)$-dimensional ambient space, not about the $n$-dimensional tangent space of the sphere on which $da_p$ acts. Writing "$\deg a=\det(-I_{n+1})$" skips the essential point that the differential lives on $T_pS^n$, whose dimension is $n$, so a priori the sphere sign could differ from the ambient sign by the action of $-I_{n+1}$ on the missing normal direction. It happens that the ambient and tangential signs *coincide* here — but only because $-I_{n+1}$ sends the outward normal $p$ to the outward normal $-p=a(p)$, so the normal direction contributes an orientation factor of $+1$ (mapping "outward normal at $p$" to "outward normal at $a(p)$", both prepended positively) and the whole ambient sign $(-1)^{n+1}$ falls on the tangential part. The shortcut is legitimate *only after* this normal-direction bookkeeping is done; the extra condition that makes it legal is precisely that the orthogonal map carries the outward normal at each point to the outward normal at its image, which holds for every $A\in O(n+1)$ because $Ap$ is the position vector of the image point.

---

# Key Takeaways

**The degree of a diffeomorphism is a single orientation sign, and every orientation-reversing self-map of a connected manifold has degree $-1$.** The reusable principle is that the regular-value formula $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$ is at its most powerful when $f$ is a diffeomorphism: there are no critical points, so every point is a regular value; there is exactly one preimage, so the sum has one term; and that term is $+1$ or $-1$ according as $f$ preserves or reverses orientation. The trigger condition is "the map whose degree I want is a diffeomorphism (or a covering) of the target". When it fires, the entire topological invariant is decided by an orientation comparison at one point, and one never touches an integral. This is exactly why the antipodal map, the coordinate reflections, and rotations all have degrees that are computed by hand in a line or two, whereas a genuinely non-injective map like $z\mapsto z^k$ on $S^1$ needs the several-preimage version of the same formula.

**Read tangential orientation signs by prepending the outward normal, and factor maps into pieces whose signs you can see.** The transferable diagnostic here is the two-move recipe for the degree of an orthogonally induced sphere map. First, to convert a determinant on the ambient $\mathbb R^{n+1}$ into an orientation sign on the $n$-dimensional tangent space $T_pS^n$, prepend the outward unit normal — which for the sphere is the position vector $p$ itself — to a tangent basis; the outward-normal-first convention is precisely the device that makes "positive in $T_pS^n$" and "positive in $\mathbb R^{n+1}$ after prepending $p$" the same statement, and for an orthogonal map $A$ the normal direction always contributes $+1$ because $A$ carries $p$ to the position vector $Ap$ of the image point. Second, when the map factors — here $-I_{n+1}=R_1\cdots R_{n+1}$ — multiplicativity of the degree turns the product of maps into the product of degrees. Both moves recur throughout gauge theory: the degree of $q\mapsto q^k$ on $S^3=SU(2)$, the winding number of a product $g_1g_2\colon S^1\to U(1)$, and the additivity of clutching invariants under tensor products of line bundles are all instances of "factor the map, multiply (or add) the invariants".

**The value $(-1)^{n+1}$ is the source of the sphere's even–odd dichotomy, and it is what powers the hairy ball theorem.** The parity of $\deg a=(-1)^{n+1}$ is not a curiosity: it is the exact mechanism separating even- and odd-dimensional spheres. For odd $n$ the antipodal map has degree $+1$ and is in fact homotopic to the identity (rotate each orthogonal pair of coordinates by $\pi$), which is why odd spheres admit nowhere-vanishing vector fields; for even $n$ the antipodal map has degree $-1$ and is therefore *not* homotopic to the identity — a homotopy would force equal degrees by clause (c). This last fact is precisely the contradiction that proves the [[Thm - Hairy Ball Theorem|hairy ball theorem]]: a nowhere-vanishing tangent field on $S^{2n}$ produces, by the normalised straight-line homotopy $x\mapsto\cos(t)x+\sin(t)v(x)/\lVert v(x)\rVert$, a homotopy from the identity (degree $+1$) to the antipodal map (degree $(-1)^{2n+1}=-1$), which is impossible. So this exercise is the computational heart of an obstruction theorem: whenever you meet a claim that even spheres behave differently from odd ones — no nowhere-zero field, no free action of a positive-dimensional Lie group, the non-triviality of $TS^{2n}$ — expect $\deg a=(-1)^{n+1}$ to be doing the work underneath. The companion exercises [[Ex - Degree of the Power Maps on the Circle and on SU(2)|Ex - Degree of the Power Maps on the Circle and on SU(2)]] and [[Ex - A Map Extending over a Bounding Manifold has Degree Zero|Ex - A Map Extending over a Bounding Manifold has Degree Zero]] drill the same regular-value-count technique on maps that are no longer diffeomorphisms.
