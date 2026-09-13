---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Holonomy Group of a Connection"
  - "Thm - Properties of Parallel Transport"
  - "Def - Euclidean Vector Bundle and Metric Connection"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Def - Classical Matrix Groups"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a smooth real vector bundle of rank $k$ over a connected manifold $M$, let $\nabla$ be a connection on $E$, fix a base point $m\in M$, and let
$$\operatorname{Hol}_m(\nabla)=\{PT_\gamma\in GL(E_m):\gamma\text{ a piecewise smooth loop based at }m\}$$
be its holonomy group at $m$. Prove the three implications of Haydys's Exercise 102:

1. **(Euclidean.)** If $E$ carries a bundle metric $\langle\cdot,\cdot\rangle$ and $\nabla$ is a metric (Euclidean) connection, then every $PT_\gamma$ is a linear isometry of $E_m$, so, in an orthonormal basis, $\operatorname{Hol}_m(\nabla)\subseteq O(k)$.
2. **(Complex.)** If $E$ carries a complex structure $I\in\Gamma(\operatorname{End}E)$ with $I^2=-\operatorname{id}$ (so $k=2m'$ is even, with complex rank $m'=k/2$) and $\nabla$ is complex — that is, $\nabla I=0$ — then every $PT_\gamma$ is complex-linear, so, in a complex basis, $\operatorname{Hol}_m(\nabla)\subseteq GL_{m'}(\mathbb C)$.
3. **(Hermitian.)** If in addition $E$ carries a Hermitian metric $h$ and $\nabla$ is a Hermitian connection — complex and compatible with $h$ — then every $PT_\gamma$ is unitary, so, in a unitary basis, $\operatorname{Hol}_m(\nabla)\subseteq U(m')$.

The intended route is short: property (6) of [[Thm - Properties of Parallel Transport|the properties of parallel transport]] supplies the structural fact about a single $PT_\gamma$ (isometry, complex-linear, or unitary); the exercise turns each structural fact into membership of a matrix group by choosing an adapted basis of $E_m$, and then into a statement about the whole holonomy group by ranging over loops.

> [!warning] Convention:
> Haydys states the complex conclusions as $\operatorname{Hol}(\nabla)\subseteq GL_{k/2}(\mathbb C)$ and $\operatorname{Hol}(\nabla)\subseteq U(k/2)$, where his $k$ is the **real** rank of $E$; the complex rank is $m'=k/2$. Following the series convention we write $GL_{m'}(\mathbb C)$ and $U(m')$ and note that $GL_{m'}(\mathbb C)$ and $U(m')$ sit inside $GL_k(\mathbb R)=GL_{2m'}(\mathbb R)$ as the real-linear automorphisms commuting with the standard complex structure $I_{\mathrm{st}}$ (and, for $U(m')$, additionally preserving the real inner product).

**Recall:**

The objects in play are the holonomy group of a connection, the properties of parallel transport, and the Euclidean, complex, and Hermitian structures a vector bundle can carry with a compatible connection.

![[Def - Holonomy Group of a Connection#The Definition]]

![[Thm - Properties of Parallel Transport#Statement]]

The single fact this exercise consumes is **property (6)**: for a loop $\gamma$ at $m$ the parallel transport $PT_\gamma\colon E_m\to E_m$ is a linear isomorphism; it is a linear isometry when $\nabla$ is metric (real case) or Hermitian (complex case); and it is complex-linear when $\nabla$ is complex. That property is proved in full on [[Thm - Properties of Parallel Transport|its own page]] by the transported-frame argument, and its mechanism is recalled inside the derivations below so that this page can be read cold.

A [[Def - Euclidean Vector Bundle and Metric Connection|Euclidean structure]] on $E$ is a smooth family $\langle\cdot,\cdot\rangle$ of inner products on the fibres, and a connection $\nabla$ is **metric (compatible)** with it when
$$d\langle s_1,s_2\rangle=\langle\nabla s_1,s_2\rangle+\langle s_1,\nabla s_2\rangle\qquad\text{for all }s_1,s_2\in\Gamma(E).$$
A [[Def - Complex Vector Bundle and Hermitian Structure|complex structure]] is a bundle endomorphism $I$ with $I^2=-\operatorname{id}$, making each fibre a complex vector space by $(a+ib)\cdot v:=av+bI(v)$; $\nabla$ is **complex** when the endomorphism $I$ is parallel, $\nabla I=0$, equivalently $\nabla(Is)=I(\nabla s)$ for every section $s$. A **Hermitian metric** $h$ is a smooth family of Hermitian inner products (complex-linear in the first slot, conjugate-linear in the second, with $h(v,v)>0$ for $v\neq0$); $\nabla$ is **Hermitian** when it is complex and $d\,h(s_1,s_2)=h(\nabla s_1,s_2)+h(s_1,\nabla s_2)$.

The classical matrix groups $O(k)=\{P\in GL_k(\mathbb R):P^{\mathsf T}P=I_k\}$, $GL_{m'}(\mathbb C)$, and $U(m')=\{U\in GL_{m'}(\mathbb C):U^{*}U=I_{m'}\}$ are those of [[Def - Classical Matrix Groups|the classical matrix groups]].

---

# Convergent Strategy

**Problem class.** This is a *structure-transport* problem: a connection compatible with an extra fibrewise structure — an inner product, a complex structure, a Hermitian form — forces its holonomy into the subgroup of $GL_k(\mathbb R)$ that preserves that structure. It is the first and most elementary instance of a theme that runs through the whole subject: the holonomy group of a connection is never larger than the structure group to which the connection reduces, and the reduction theory of connections and the Berger classification of holonomy groups are the deep continuations of exactly this observation.

**Assumption pattern.** Each hypothesis ("metric", "complex", "Hermitian") is used in precisely one way and at precisely one moment: it guarantees that the fibrewise structure is *parallel*, so that parallel transport carries the structure at $\gamma(0)$ to the identical structure at $\gamma(1)$. The recognisable trigger is the phrase "compatible connection", which always unpacks to "the tensor defining the structure has vanishing covariant derivative", and a parallel tensor is preserved by parallel transport because transporting it is solving the homogeneous linear equation it already satisfies.

**Theorem routing.** The route has two links. First, [[Thm - Properties of Parallel Transport|property (6)]] converts each hypothesis into a structural property of the map $PT_\gamma\colon E_m\to E_m$: metric $\Rightarrow$ isometry, complex $\Rightarrow$ complex-linear, Hermitian $\Rightarrow$ unitary. Second, elementary linear algebra converts each structural property into membership of a matrix group once a basis adapted to the structure is fixed — an orthonormal basis makes an isometry an orthogonal matrix, a complex basis makes a complex-linear map a complex matrix, a unitary basis makes a unitary map a unitary matrix. Ranging over all loops then gives the containment of the whole group, because [[Def - Holonomy Group of a Connection|the holonomy group]] is by definition the set of all such $PT_\gamma$.

**Key decision point.** The one genuine decision is *which basis of $E_m$ to fix*. The structural facts of property (6) are basis-free; the matrix groups $O(k)$, $GL_{m'}(\mathbb C)$, $U(m')$ are not — they are the stabilisers of the *standard* inner product, complex structure, or Hermitian form on $\mathbb R^k$ or $\mathbb C^{m'}$. Choosing a basis in which the fibre structure becomes the standard one (orthonormal, complex, or unitary) is exactly what makes an abstract isometry into a concretely orthogonal matrix. Choose the wrong basis and $PT_\gamma$ is represented by a matrix conjugate to an orthogonal one but not orthogonal itself; the containment then holds only up to conjugacy, which is in fact the honest statement once one remembers that the base point and the basis are both arbitrary.

---

# Legal Operations Used

This solution deploys the following legal operations, named descriptively (the topic page's numbered Legal Operations list will absorb them once written):

1. **Read a compatible connection as a parallel tensor.** "Metric", "complex", "Hermitian" each mean that the tensor carrying the structure ($\langle\cdot,\cdot\rangle$, $I$, or $h$) is parallel; pull this identity back along the loop $\gamma$ to get a first-order fact along the curve.

2. **Differentiate a transported quantity and use parallelism to kill the derivative.** For parallel sections $s_1,s_2$ along $\gamma$, compute $\tfrac{d}{dt}\langle s_1,s_2\rangle$ or $\tfrac{d}{dt}h(s_1,s_2)$ and use $\nabla_t s_i=0$ together with compatibility to conclude the quantity is constant along $\gamma$.

3. **Invoke property (6) of the parallel-transport theorem.** Take the structural conclusion — isometry, complex-linearity, unitarity of $PT_\gamma$ — directly from [[Thm - Properties of Parallel Transport|the proved theorem]] rather than re-deriving it each time.

4. **Adapt the basis to the structure.** Choose an orthonormal, complex, or unitary basis of $E_m$ so that the fibre structure is the standard one and the stabiliser subgroup is the standard matrix group.

5. **Translate a structure-preserving map into a matrix identity.** Express "$PT_\gamma$ preserves $\langle\cdot,\cdot\rangle$" as $P^{\mathsf T}P=I_k$, "commutes with $I_m$" as $\mathbb C$-linearity, "preserves $h$" as $U^{*}U=I_{m'}$, by evaluating on basis vectors.

6. **Range over loops to pass from one element to the whole group.** Since every element of $\operatorname{Hol}_m(\nabla)$ is $PT_\gamma$ for some loop and each lies in the matrix group, the whole holonomy group is contained in it.

---

# Hints

> [!note]- Hint 1
> You do not need to compute a single parallel transport. Every claim about the individual map $PT_\gamma$ — that it is an isometry, complex-linear, or unitary — is already property (6) of [[Thm - Properties of Parallel Transport|the properties of parallel transport]]. The whole exercise is the passage from "$PT_\gamma$ preserves a structure" to "$\operatorname{Hol}_m(\nabla)$ is contained in the corresponding matrix group". What is the matrix of a linear isometry in an *orthonormal* basis?

> [!note]- Hint 2
> If you would like to see why $PT_\gamma$ is an isometry rather than only cite it: let $s_1,s_2$ be the parallel sections along $\gamma$ with prescribed initial values, and differentiate $f(t)=\langle s_1(t),s_2(t)\rangle$. Metric compatibility, pulled back to the curve, gives $f'(t)=\langle\nabla_t s_1,s_2\rangle+\langle s_1,\nabla_t s_2\rangle$. What are $\nabla_t s_1$ and $\nabla_t s_2$ for parallel sections?

> [!note]- Hint 3
> For the complex case, the parallel tensor is $I$ itself. If $s$ is parallel along $\gamma$, show that $t\mapsto I_{\gamma(t)}s(t)$ is also parallel, using $\nabla I=0$. Compare initial values and invoke uniqueness of parallel sections to conclude $PT_\gamma(I_m v)=I_m\,PT_\gamma(v)$. A real-linear automorphism commuting with the complex structure is exactly a complex-linear map.

> [!note]- Hint 4
> The Hermitian case is the conjunction of the other two: complex-linear (Hint 3) and $h$-preserving (Hint 2, with $h$ in place of $\langle\cdot,\cdot\rangle$). In a unitary basis $(f_a)$ with $h(f_a,f_b)=\delta_{ab}$, write the coordinate identity $h(u,v)=\hat u^{*}\hat v$ and push $PT_\gamma$ through it to get $U^{*}U=I_{m'}$. Then range over loops.

---

# Solution

The proof consumes property (6) once per clause and then does linear algebra. In each case the compatibility hypothesis makes a fibre tensor parallel, property (6) records that parallel transport preserves it, an adapted basis turns "preserves it" into a defining matrix identity of $O(k)$, $GL_{m'}(\mathbb C)$, or $U(m')$, and ranging over loops upgrades the statement about one $PT_\gamma$ to the containment of the whole holonomy group. We include, inside each derivation, the one-line differentiation that is the mechanism behind property (6), so that the page stands on its own.

**Step 1: The Euclidean case — every $PT_\gamma$ is orthogonal.**

For a metric connection each $PT_\gamma$ is a linear isometry of $(E_m,\langle\cdot,\cdot\rangle_m)$, and in an orthonormal basis a linear isometry is an orthogonal matrix; hence $\operatorname{Hol}_m(\nabla)\subseteq O(k)$.

> [!note]- Derivation
> Fix a piecewise smooth loop $\gamma\colon[0,1]\to M$ based at $m$, and let $u,v\in E_m$. Let $s_1,s_2\in\Gamma(\gamma^{*}E)$ be the parallel sections along $\gamma$ with $s_1(0)=u$, $s_2(0)=v$. A parallel section along $\gamma$ is by definition a solution of the linear ordinary differential equation $\nabla_t s=0$, which in a trivialisation of $\gamma^{*}E$ over the contractible interval $[0,1]$ takes the form $\dot s+B(t)s=0$ with $B$ continuous; by [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness theorem for horizontal lifts]] — a horizontal lift, hence a parallel section, exists and is unique on all of $[0,1]$ for each prescribed initial value in $E_m$ — the sections $s_1,s_2$ exist and are unique, and by definition $PT_\gamma u=s_1(1)$ and $PT_\gamma v=s_2(1)$.
>
> **Differentiate the transported inner product.** Consider the smooth real function $f(t)=\langle s_1(t),s_2(t)\rangle_{\gamma(t)}$ on $[0,1]$. Pulling the metric-compatibility identity $d\langle s_1,s_2\rangle=\langle\nabla s_1,s_2\rangle+\langle s_1,\nabla s_2\rangle$ back along $\gamma$ and pairing with $\dot\gamma$ gives
> $$f'(t)=\langle\nabla_t s_1,s_2\rangle+\langle s_1,\nabla_t s_2\rangle\qquad\text{(metric compatibility of }\nabla\text{, pulled back to }\gamma\text{).}$$
> Since $s_1$ and $s_2$ are **parallel**, $\nabla_t s_1=0$ and $\nabla_t s_2=0$, so
> $$f'(t)=\langle 0,s_2\rangle+\langle s_1,0\rangle=0\qquad\text{(parallelism of }s_1,s_2\text{).}$$
> Hence $f$ is constant, and in particular $f(1)=f(0)$, that is
> $$\langle PT_\gamma u,PT_\gamma v\rangle_m=\langle u,v\rangle_m\qquad\text{(}f(1)=f(0)\text{; }\gamma(1)=\gamma(0)=m\text{).}$$
> This is property (6) in the metric case: $PT_\gamma$ is a **linear isometry** of $(E_m,\langle\cdot,\cdot\rangle_m)$.
>
> **Pass to an orthonormal basis.** Choose an orthonormal basis $(e_1,\dots,e_k)$ of $E_m$, so $\langle e_i,e_j\rangle_m=\delta_{ij}$. For $u=\sum_i u_i e_i$ write $\hat u=(u_1,\dots,u_k)^{\mathsf T}\in\mathbb R^{k}$; then $\langle u,v\rangle_m=\hat u^{\mathsf T}\hat v$. Let $P\in\operatorname{Mat}(k\times k;\mathbb R)$ be the matrix of $PT_\gamma$ in this basis, so $\widehat{PT_\gamma u}=P\hat u$. The isometry identity reads
> $$\hat u^{\mathsf T}\hat v=\langle u,v\rangle_m=\langle PT_\gamma u,PT_\gamma v\rangle_m=(P\hat u)^{\mathsf T}(P\hat v)=\hat u^{\mathsf T}(P^{\mathsf T}P)\hat v\qquad\text{(isometry; }\langle x,y\rangle_m=\hat x^{\mathsf T}\hat y\text{ in an orthonormal basis).}$$
> This holds for all $\hat u,\hat v\in\mathbb R^{k}$. Taking $\hat u=e_i$ and $\hat v=e_j$ (standard basis vectors of $\mathbb R^k$) gives $(P^{\mathsf T}P)_{ij}=\delta_{ij}$ for all $i,j$, that is
> $$P^{\mathsf T}P=I_k,\qquad\text{so}\qquad P\in O(k).$$
> As $\gamma$ was an arbitrary loop and every element of $\operatorname{Hol}_m(\nabla)$ is $PT_\gamma$ for some loop, in the fixed orthonormal basis $\operatorname{Hol}_m(\nabla)\subseteq O(k)$.

**Step 2: The complex case — every $PT_\gamma$ is complex-linear.**

For a complex connection the complex structure $I$ is parallel, so $PT_\gamma$ commutes with $I_m$; a real-linear automorphism commuting with $I_m$ is complex-linear, hence lies in $GL_{m'}(\mathbb C)$. Thus $\operatorname{Hol}_m(\nabla)\subseteq GL_{m'}(\mathbb C)$, where $k=2m'$.

> [!note]- Derivation
> Fix a loop $\gamma$ at $m$ and $v\in E_m$, and let $s\in\Gamma(\gamma^{*}E)$ be the parallel section with $s(0)=v$, so $PT_\gamma v=s(1)$.
>
> **The transport of $Iv$ is $I$ times the transport of $v$.** Consider the section $t\mapsto(Is)(t):=I_{\gamma(t)}s(t)$ of $\gamma^{*}E$. Pulling $\nabla I=0$ back along $\gamma$ gives $\nabla_t I=0$, so by the Leibniz rule for the induced connection on $\operatorname{End}E$ acting on $s$,
> $$\nabla_t(Is)=(\nabla_t I)s+I(\nabla_t s)=0\cdot s+I\cdot 0=0\qquad\text{(}\nabla I=0\text{ pulled back to }\gamma\text{; }s\text{ parallel).}$$
> Hence $Is$ is parallel along $\gamma$, with initial value $(Is)(0)=I_m v$. By the **uniqueness** half of [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness theorem]] — there is exactly one parallel section along $\gamma$ with a prescribed initial value, since $\nabla_t(\,\cdot\,)=0$ is a linear ordinary differential equation with a unique solution for each initial condition — $Is$ is the parallel transport of $I_m v$, so evaluating at $t=1$,
> $$PT_\gamma(I_m v)=(Is)(1)=I_{\gamma(1)}s(1)=I_m\,PT_\gamma(v)\qquad\text{(uniqueness of parallel sections; }\gamma(1)=m\text{).}$$
> As $v\in E_m$ was arbitrary, $PT_\gamma\circ I_m=I_m\circ PT_\gamma$. This is property (6) in the complex case: $PT_\gamma$ **commutes with the complex structure**.
>
> **Commuting with $I_m$ means complex-linear.** The complex structure $I_m$ makes $E_m$ a complex vector space of dimension $m'=k/2$ via $(a+ib)\cdot w=aw+bI_m w$. A real-linear map $P=PT_\gamma$ is complex-linear for this structure precisely when $P((a+ib)\cdot w)=(a+ib)\cdot P(w)$ for all $a,b\in\mathbb R$, $w\in E_m$; since $P$ is already real-linear this reduces to $P(I_m w)=I_m P(w)$, which we have just shown. Fixing a complex basis $(f_1,\dots,f_{m'})$ of $(E_m,I_m)$ represents the complex-linear automorphism $PT_\gamma$ by a matrix in $GL_{m'}(\mathbb C)$; that $PT_\gamma$ is invertible is part of property (6). Ranging over loops, $\operatorname{Hol}_m(\nabla)\subseteq GL_{m'}(\mathbb C)$.

**Step 3: The Hermitian case — every $PT_\gamma$ is unitary.**

A Hermitian connection is complex and $h$-compatible, so $PT_\gamma$ is complex-linear (Step 2) and preserves $h$ (the differentiation of Step 1, with $h$ in place of $\langle\cdot,\cdot\rangle$); a complex-linear map preserving a Hermitian inner product is unitary. Hence $\operatorname{Hol}_m(\nabla)\subseteq U(m')$.

> [!note]- Derivation
> Fix a loop $\gamma$ at $m$ and $u,v\in E_m$, with parallel sections $s_1,s_2$ along $\gamma$, $s_1(0)=u$, $s_2(0)=v$.
>
> **$PT_\gamma$ is complex-linear.** A Hermitian connection is in particular complex ($\nabla I=0$), so Step 2 applies verbatim: $PT_\gamma\circ I_m=I_m\circ PT_\gamma$.
>
> **$PT_\gamma$ preserves $h$.** Consider $g(t)=h_{\gamma(t)}(s_1(t),s_2(t))$, a smooth $\mathbb C$-valued function on $[0,1]$. Pulling the Hermitian-compatibility identity back along $\gamma$ and using parallelism,
> $$g'(t)=h(\nabla_t s_1,s_2)+h(s_1,\nabla_t s_2)=h(0,s_2)+h(s_1,0)=0\qquad\text{(Hermitian compatibility; }s_1,s_2\text{ parallel).}$$
> Hence $g(1)=g(0)$, that is $h(PT_\gamma u,PT_\gamma v)=h(u,v)$: $PT_\gamma$ preserves the Hermitian form. This is property (6) in the Hermitian case.
>
> **Pass to a unitary basis.** Choose a unitary basis $(f_1,\dots,f_{m'})$ of $(E_m,I_m,h_m)$, so $h_m(f_a,f_b)=\delta_{ab}$. For $u=\sum_a u_a f_a$ (with $u_a\in\mathbb C$) write $\hat u=(u_1,\dots,u_{m'})^{\mathsf T}\in\mathbb C^{m'}$; then, with the convention that $h$ is conjugate-linear in its second slot, $h_m(u,v)=\sum_a u_a\overline{v_a}=\hat v^{*}\hat u$, where $\hat v^{*}=\overline{\hat v}^{\mathsf T}$. Let $U\in\operatorname{Mat}(m'\times m';\mathbb C)$ be the matrix of the complex-linear map $PT_\gamma$ in this basis, so $\widehat{PT_\gamma u}=U\hat u$. Preservation of $h$ reads
> $$\hat v^{*}\hat u=h_m(u,v)=h_m(PT_\gamma u,PT_\gamma v)=(U\hat v)^{*}(U\hat u)=\hat v^{*}(U^{*}U)\hat u\qquad\text{(}PT_\gamma\text{ complex-linear and }h\text{-preserving; coordinates in a unitary basis).}$$
> This holds for all $\hat u,\hat v\in\mathbb C^{m'}$; taking $\hat u,\hat v$ to run over the standard basis of $\mathbb C^{m'}$ gives $U^{*}U=I_{m'}$, that is $U\in U(m')$. Ranging over loops, $\operatorname{Hol}_m(\nabla)\subseteq U(m')$.

> [!note]- Complete formal solution
> **Claim.** With the hypotheses of each clause, $\operatorname{Hol}_m(\nabla)\subseteq O(k)$, $\subseteq GL_{m'}(\mathbb C)$, and $\subseteq U(m')$ respectively (in an orthonormal, complex, and unitary basis of $E_m$, with $k=2m'$ in the complex and Hermitian cases).
>
> Let $\gamma$ be a piecewise smooth loop at $m$; every element of $\operatorname{Hol}_m(\nabla)$ has this form. For $u,v\in E_m$ let $s_1,s_2$ be the parallel sections along $\gamma$ with $s_1(0)=u$, $s_2(0)=v$, unique for each initial value by [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness theorem for the linear parallel-transport equation]] $\nabla_t s=0$, so $PT_\gamma u=s_1(1)$, $PT_\gamma v=s_2(1)$.
>
> *Euclidean.* Metric compatibility pulled back to $\gamma$ gives $\tfrac{d}{dt}\langle s_1,s_2\rangle=\langle\nabla_t s_1,s_2\rangle+\langle s_1,\nabla_t s_2\rangle=0$ (the last equality because $s_1,s_2$ are parallel, so $\nabla_t s_1=\nabla_t s_2=0$), so $\langle PT_\gamma u,PT_\gamma v\rangle=\langle u,v\rangle$; this is property (6). In an orthonormal basis, writing $P$ for the matrix of $PT_\gamma$, the identity $\hat u^{\mathsf T}\hat v=\hat u^{\mathsf T}P^{\mathsf T}P\hat v$ for all $\hat u,\hat v$ forces $P^{\mathsf T}P=I_k$, so $P\in O(k)$; ranging over loops, $\operatorname{Hol}_m(\nabla)\subseteq O(k)$.
>
> *Complex.* From $\nabla I=0$, if $s$ is parallel then $Is$ is parallel with initial value $I_m s(0)$, so by uniqueness $PT_\gamma(I_m v)=I_m PT_\gamma(v)$; this is property (6). A real-linear automorphism commuting with $I_m$ is complex-linear, so in a complex basis $PT_\gamma\in GL_{m'}(\mathbb C)$; ranging over loops, $\operatorname{Hol}_m(\nabla)\subseteq GL_{m'}(\mathbb C)$.
>
> *Hermitian.* A Hermitian connection is complex, so $PT_\gamma$ is complex-linear by the previous case; and $\tfrac{d}{dt}h(s_1,s_2)=h(\nabla_t s_1,s_2)+h(s_1,\nabla_t s_2)=0$ (Hermitian compatibility for the first equality, parallelism $\nabla_t s_1=\nabla_t s_2=0$ for the second) gives $h(PT_\gamma u,PT_\gamma v)=h(u,v)$; both together are property (6). In a unitary basis the identity $\hat v^{*}\hat u=\hat v^{*}U^{*}U\hat u$ for all $\hat u,\hat v$ forces $U^{*}U=I_{m'}$, so $U\in U(m')$; ranging over loops, $\operatorname{Hol}_m(\nabla)\subseteq U(m')$. $\blacksquare$

> [!warning] Illegal but tempting: concluding $\operatorname{Hol}_m(\nabla)\subseteq SO(k)$
> A metric connection preserves the inner product, so it is tempting to add "and preserves orientation", landing in $SO(k)$. This is false in general. The transport of a *single* loop can have determinant $-1$: take the Möbius line bundle $E\to S^1$ (real rank $k=1$) with its flat metric connection. Parallel transport once around the circle is multiplication by $-1$, so $\operatorname{Hol}(\nabla)=\{\pm1\}=O(1)$, and $-1\notin SO(1)=\{1\}$. The extra condition that *would* make the conclusion legal is that $E$ be **oriented** and $\nabla$ preserve the orientation (equivalently, that the structure group reduce to $SO(k)$); then, and only then, every $PT_\gamma$ has determinant $+1$. The *restricted* holonomy group $\operatorname{Hol}^0_m(\nabla)$, generated by null-homotopic loops, does always lie in $SO(k)$ when $\nabla$ is metric: it is a connected subgroup of $O(k)$ containing the identity — connected because it is the image of the path-connected space of based null-homotopic loops under the continuous holonomy map, a fact established where the restricted holonomy group is defined — and a connected subset of $O(k)$ through the identity lies in the identity component $SO(k)$. But $\operatorname{Hol}^0_m(\nabla)$ is a different group from the full holonomy $\operatorname{Hol}_m(\nabla)$, which need not be connected, as the Möbius example shows.

# Key Takeaways

**A compatible connection forces its holonomy into the stabiliser of whatever structure it is compatible with, and the proof is always "parallel tensor, therefore preserved by transport".** The three clauses look like three separate computations, but they are one argument applied to three tensors: the metric $\langle\cdot,\cdot\rangle$, the complex structure $I$, and the Hermitian form $h$. In each case "compatible connection" means the tensor is parallel, a parallel tensor satisfies a homogeneous linear equation along every curve, and transporting the tensor is solving that equation with the tensor as initial value — so the tensor comes back to itself. This is the recognisable content of property (6), and it is worth carrying as a slogan: *the holonomy group is contained in the structure group of any reduction the connection respects.* The trigger for using it is any hypothesis of the form "$\nabla$ preserves $\tau$" for a fibre tensor $\tau$; the reaction is to conclude immediately that $\operatorname{Hol}\subseteq\operatorname{Stab}(\tau)$, without a coordinate computation.

**The abstract-to-matrix passage is entirely about choosing a basis adapted to the structure, and it is where the "up to conjugacy" caveat is born.** Property (6) gives basis-free facts; the matrix groups $O(k)$, $GL_{m'}(\mathbb C)$, $U(m')$ are the stabilisers of the *standard* structures on $\mathbb R^k$ and $\mathbb C^{m'}$. Aligning the fibre structure with the standard one — an orthonormal, complex, or unitary basis of $E_m$ — is what turns "isometry" into "$P^{\mathsf T}P=I$". A different admissible basis conjugates the whole holonomy group by a change-of-basis matrix that itself lies in the structure group, so the containment is unchanged; a *non-adapted* basis conjugates it out of the standard subgroup, which is why the honest statement of holonomy is "a subgroup of $GL_k(\mathbb R)$ defined up to conjugacy". This is the same phenomenon proved for base-point changes in [[Ex - Holonomy Groups at Different Base Points are Conjugate|the companion exercise]].

**Orthogonal, not special orthogonal: determinant is a genuinely separate constraint.** The most common error here is to over-read "isometry" as "rotation". Preservation of an inner product controls lengths and angles but not orientation; the determinant of an isometry is $\pm1$, and both signs occur — the Möbius line bundle realises $-1$ on a single loop. Orientation is an *additional* fibre structure (a nowhere-zero section of $\Lambda^k E$), and one gets $\operatorname{Hol}\subseteq SO(k)$ only from a connection that is compatible with an orientation too. The diagnostic to remember: to land in a *special* or *unimodular* subgroup one needs a parallel volume form, not merely a parallel metric, and the presence or absence of that extra parallel tensor is exactly the difference between $O(k)$ and $SO(k)$, or between $U(m')$ and $SU(m')$.
