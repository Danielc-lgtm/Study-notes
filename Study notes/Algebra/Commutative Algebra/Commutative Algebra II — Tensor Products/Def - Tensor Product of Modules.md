---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Free Module"
  - "Def - Module Homomorphism"
  - "Def - Bilinear and Multilinear Maps"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Let $R$ be a ring and $M, N$ be [[Def - Module|$R$-modules]]. We write $F = R^{\oplus(M\times N)}$ for the [[Def - Free Module|free $R$-module]] on the *set* $M\times N$, with standard basis $\{e_{m,n} : (m,n)\in M\times N\}$; $K\leq F$ for the [[Def - Submodule|submodule]] of bilinearity relations; $M\otimes_R N = F/K$ for the tensor product; $m\otimes n$ for the image of $e_{m,n}$ (a **pure tensor**); and $i_{M\otimes N} : M\times N\to M\otimes N$, $(m,n)\mapsto m\otimes n$, for the canonical [[Def - Bilinear and Multilinear Maps|bilinear map]]. When $R$ is clear we write $M\otimes N$. The full registry is on [[Commutative Algebra II — Tensor Products]].

This generalises the vector-space construction [[Def - Tensor Product of Vector Spaces|$V\otimes_k W$]] from a field $k$ to an arbitrary commutative ring $R$; everything below specialises to that page when $R = k$ is a field and $M, N$ are vector spaces.

---

# Axiom Motivation

We have a supply of [[Def - Bilinear and Multilinear Maps|bilinear maps]] $M\times N\to L$ — multiplication, pairings, scalar actions — and the category of modules only understands *linear* maps. We want a single module $M\otimes_R N$ and a single bilinear map $i : M\times N\to M\otimes_R N$ so universal that *every* bilinear map factors through it as an honest linear map. The construction below is the brute-force way to manufacture exactly such an object; the point of watching it being built is to see that nothing is put in by hand except the bilinearity relations themselves.

**Why start with the free module on the set $M\times N$.** We want the pure tensors $m\otimes n$ to be as *unconstrained* as possible to begin with — we will impose constraints later, and we must not accidentally impose any others. The freest possible object containing a symbol for each pair $(m,n)$ is the [[Def - Free Module|free module]] $F = R^{\oplus(M\times N)}$, which has a basis vector $e_{m,n}$ for every pair and *no relations at all* among them. This is deliberately enormous and stupid: in $F$, $e_{m,0}$ and $e_{0,0}$ are independent, $e_{2m,n}$ and $2e_{m,n}$ are unrelated, $e_{m,n} + e_{m,n'}$ has nothing to do with $e_{m,n+n'}$. None of the things we *want* to be true are true yet. That is the correct starting point precisely because it forces us to declare every desired identity explicitly, so we can be sure we have imposed *only* bilinearity.

**Why quotient by exactly these four relation families.** Now we impose bilinearity, and only bilinearity. The defining property of $i(m,n) = m\otimes n$ should be that it is bilinear: linear in $m$, linear in $n$, with scalars sliding either way. Writing out what "bilinear" demands of the symbols $e_{m,n}$ gives four families of relations, and we kill exactly the submodule $K$ they generate:
$$e_{m,n_1} + e_{m,n_2} - e_{m,n_1+n_2}, \quad e_{m_1,n} + e_{m_2,n} - e_{m_1+m_2,n}, \quad re_{m,n} - e_{rm,n}, \quad re_{m,n} - e_{m,rn}.$$
The first two impose additivity in each slot; the last two impose that a scalar may be pulled out of either slot. In the quotient $F/K$, writing $m\otimes n$ for the class of $e_{m,n}$, these become precisely $m\otimes(n_1+n_2) = m\otimes n_1 + m\otimes n_2$, $(m_1+m_2)\otimes n = m_1\otimes n + m_2\otimes n$, $r(m\otimes n) = (rm)\otimes n = m\otimes(rn)$ — the bilinearity laws and nothing else. Drop the additivity families and $i$ is not additive; drop the scalar families and a scalar cannot cross the $\otimes$, so $i$ is merely $\mathbb{Z}$-bilinear, not $R$-bilinear. Each family earns its place: it is the exact relation needed for one clause of the [[Def - Bilinear and Multilinear Maps|bilinearity]] definition, and the quotient is the universal object because $K$ is *generated* by these and contains no surplus relations.

**Why this forces the universal property, and why that is the real definition.** The payoff of imposing *only* bilinearity is that a linear map $h : M\otimes N\to L$ is the same as a linear map $F\to L$ that vanishes on $K$, which is the same as a function on the basis $\{e_{m,n}\}$ — i.e. a function $M\times N\to L$ — that respects the four relation families, which is *exactly* a bilinear map. So $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Bil}_R(M\times N, L)$, the [[Thm - Universal Property of the Tensor Product of Modules|universal property]]. This is why the fractions are a *model* and the universal property is the *meaning*: had we imposed one relation too many, some bilinear maps would fail to factor; one too few, and $h$ would not be well-defined. The construction is calibrated so that "linear out of $M\otimes N$" and "bilinear out of $M\times N$" coincide on the nose.

**Why not every tensor is pure, and why vanishing is subtle.** The pure tensors $m\otimes n$ generate $M\otimes N$ (they are the images of the basis of $F$), and since $r(m\otimes n) = (rm)\otimes n$ they generate it even as an abelian group: every element is a *finite sum* $\sum_i m_i\otimes n_i$. But the relations can both fail to simplify a sum into a single pure tensor *and* collapse a pure tensor to zero unexpectedly. The element $e_1\otimes e_1 + 2e_1\otimes e_2 + 3e_2\otimes e_1 + 4e_2\otimes e_2$ in $R^2\otimes R^2$ is not pure (its coefficient matrix has rank $2$); meanwhile $\mathbb{Z}/2\otimes\mathbb{Z}/3 = 0$ because every pure tensor slides to zero. This is the price of imposing relations by quotient: you cannot read off membership in $K$ from the symbols, so deciding whether $\sum m_i\otimes n_i = 0$ requires either pushing the relations (to prove zero) or producing a bilinear map that survives (to prove nonzero). The subtlety is not a defect — it is the content.

---

# The Definition

Let $R$ be a commutative ring and $M, N$ be $R$-modules.

## The construction

Let $F = R^{\oplus(M\times N)}$ be the free $R$-module on the set $M\times N$, with basis $\{e_{m,n} : (m,n)\in M\times N\}$. Let $K\leq F$ be the submodule generated by the union of the four families
$$\{\,e_{m,n_1} + e_{m,n_2} - e_{m,n_1+n_2}\,\}, \quad \{\,e_{m_1,n} + e_{m_2,n} - e_{m_1+m_2,n}\,\},$$
$$\{\,r\,e_{m,n} - e_{rm,n}\,\}, \quad \{\,r\,e_{m,n} - e_{m,rn}\,\},$$
ranging over all $m, m_1, m_2\in M$, $n, n_1, n_2\in N$, $r\in R$. The **tensor product** of $M$ and $N$ over $R$ is the quotient module
$$M\otimes_R N := F/K.$$
The image of $e_{m,n}$ in $M\otimes_R N$ is written $m\otimes n$ and called a **pure tensor**; the canonical map
$$i_{M\otimes N} : M\times N\to M\otimes_R N, \qquad i_{M\otimes N}(m,n) = m\otimes n,$$
is $R$-[[Def - Bilinear and Multilinear Maps|bilinear]] by construction.

## Computational rules

The relations translate, for all $m,m_i\in M$, $n,n_i\in N$, $r\in R$, into
$$m\otimes(n_1+n_2) = m\otimes n_1 + m\otimes n_2, \qquad (m_1+m_2)\otimes n = m_1\otimes n + m_2\otimes n,$$
$$r(m\otimes n) = (rm)\otimes n = m\otimes(rn), \qquad 0\otimes n = m\otimes 0 = 0.$$
Pure tensors generate $M\otimes_R N$ as an $R$-module, and (since $r(m\otimes n) = (rm)\otimes n$) even as an abelian group: every element has the form $\sum_{i=1}^{\ell} m_i\otimes n_i$. A general element need **not** be a pure tensor.

---

# Categorical / Structural Definition

The fractions-and-relations construction is a *model*; the object's real definition is by a [[Thm - Universal Property of the Tensor Product of Modules|universal property]]. The tensor product is the $R$-module $M\otimes_R N$ together with a bilinear map $i : M\times N\to M\otimes_R N$ that is **initial** among bilinear maps out of $M\times N$: for every $R$-module $L$ and bilinear $f : M\times N\to L$, there is a unique linear $h : M\otimes_R N\to L$ with $f = h\circ i$. Equivalently, $M\otimes_R N$ **represents** the functor $L\mapsto\operatorname{Bil}_R(M\times N, L)$:
$$\operatorname{Bil}_R(M\times N, L)\ \cong\ \operatorname{Hom}_R(M\otimes_R N, L)\qquad\text{naturally in }L.$$
Any two pairs $(T, j)$ with this property are uniquely isomorphic, so the universal property determines $M\otimes_R N$ up to unique isomorphism — the free-module model merely *exhibits* one. As a bifunctor, $-\otimes_R -$ is the [[Thm - Functoriality of the Tensor Product|left adjoint]] of the internal $\operatorname{Hom}$: the **tensor–hom adjunction** $\operatorname{Hom}_R(M\otimes_R N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$ holds naturally. This adjunction is the structural reason $\otimes$ is right exact, taken up in [[Commutative Algebra III — Flatness and Exactness]].

---

# Relate to Other Fields / Compression

The cleanest compression: **$M\otimes_R N$ is the universal place where elements of $M$ and $N$ can be "multiplied", with the only laws being those a product must obey.** It is the free module on formal products $m\otimes n$ modulo the rules that make $\otimes$ bilinear, and nothing more.

**True name:** the true name of $M\otimes_R N$ is *not* "formal sums $\sum m_i\otimes n_i$" but "**the receptacle through which every bilinear map factors uniquely**". The fraction model is for computation (collapsing, bases, reduction mod $I$); the universal property is for everything structural (building maps, proving isomorphisms, certifying non-vanishing). When you need to map *out of* a tensor product, the reflex is "give the bilinear map".

This generalises [[Def - Tensor Product of Vector Spaces|$V\otimes_k W$]] from fields to rings; over a field every module is free, so $\dim(V\otimes W) = \dim V\cdot\dim W$ and no tensor surprises occur, whereas over a general ring the relations can collapse things ($\mathbb{Z}/2\otimes\mathbb{Z}/3 = 0$) and tensors can be hard to evaluate. In **homological algebra** $M\otimes_R N$ is the degree-zero piece of the derived tensor product, with higher $\operatorname{Tor}^R_i(M,N)$ measuring the failure of exactness. In **physics and quantum information** $\mathcal{H}_A\otimes\mathcal{H}_B$ is the state space of a composite system, pure tensors are unentangled product states, and non-pure tensors are entangled states.

---

# Examples / Corollaries

**Is an instance — free modules multiply dimensions.** $R^m\otimes_R R^n\cong R^{mn}$, with basis the pure tensors $\{e_i\otimes f_j : 1\leq i\leq m, 1\leq j\leq n\}$. For vector spaces over a field $k$, $\dim_k(V\otimes W) = \dim V\cdot\dim W$. This follows from distributivity over [[Def - Direct Sum of Modules|direct sums]] plus $R\otimes_R R\cong R$, and is the prototype computation.

**Is an instance — reduction mod an ideal.** $R/I\otimes_R M\cong M/IM$, the module $M$ with its $I$-multiples killed. In particular $\mathbb{Z}/n\otimes_{\mathbb{Z}}\mathbb{Z}^k\cong(\mathbb{Z}/n)^k$, and $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^n\cong\mathbb{C}^n$. This is the single most common concrete tensor computation.

**Is an instance of collapse — coprime cyclic groups.** $\mathbb{Z}/2\otimes_{\mathbb{Z}}\mathbb{Z}/3 = 0$, even though neither factor is zero. Reason: $a\otimes b = 3(a\otimes b) - 2(a\otimes b) = a\otimes 3b - (2a)\otimes b = a\otimes 0 - 0\otimes b = 0$, using $3b = 0$ in $\mathbb{Z}/3$ and $2a = 0$ in $\mathbb{Z}/2$. Generally $\mathbb{Z}/m\otimes\mathbb{Z}/n\cong\mathbb{Z}/\gcd(m,n)$ (see [[Ex - Z mod m tensor Z mod n is Z mod gcd]]).

**Is NOT an instance of a pure tensor — a rank-$2$ tensor.** In $R^2\otimes_R R^2$, the tensor $e_1\otimes e_1 + 2e_1\otimes e_2 + 3e_2\otimes e_1 + 4e_2\otimes e_2$ is *not* pure. A pure tensor $(\alpha e_1+\beta e_2)\otimes(\gamma e_1+\delta e_2)$ has coefficient matrix $\begin{pmatrix}\alpha\gamma&\alpha\delta\\\beta\gamma&\beta\delta\end{pmatrix}$ of rank $\leq 1$, but $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ has rank $2$. By contrast $3e_1\otimes e_1 + 4e_1\otimes e_2 + 6e_2\otimes e_1 + 8e_2\otimes e_2 = (e_1+2e_2)\otimes(3e_1+4e_2)$ *is* pure (rank-$1$ matrix), despite appearances.

**Is NOT preserved — vanishing in a submodule.** The symbol $2\otimes\bar 1$ is $0$ in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$ but *nonzero* in $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$: the computation $2\otimes\bar1 = 1\otimes\overline{2} = 0$ used $2 = 2\cdot 1$, illegal in $2\mathbb{Z}$ where $1\notin 2\mathbb{Z}$, and the bilinear map $b(2x,\bar y) = \overline{xy}$ certifies $2\otimes\bar1\neq 0$ there (see [[Ex - A pure tensor that is zero without either factor being zero]]). Tensor vanishing is not inherited from submodules.

**Corollary — the base ring controls the size.** $\mathbb{C}^2\otimes_{\mathbb{C}}\mathbb{C}^3\cong\mathbb{C}^6$, but $\mathbb{C}^2\otimes_{\mathbb{R}}\mathbb{C}^3\cong\mathbb{R}^4\otimes_{\mathbb{R}}\mathbb{R}^6\cong\mathbb{R}^{24}$: over the smaller ring $\mathbb{R}$ fewer scalars cross the $\otimes$, so fewer identifications are made and the result is larger. Over $\mathbb{C}$, $i(v\otimes w) = v\otimes(iw)$; over $\mathbb{R}$ this is illegal.

**Calibration check.** Derive $0\otimes n = m\otimes 0 = 0$ from the four rules. Show $\mathbb{Z}/2\otimes\mathbb{Z}/3 = 0$ by sliding scalars. Verify that a tensor in $R^2\otimes R^2$ is pure if and only if its $2\times 2$ coefficient matrix has rank $\leq 1$. Finally, confirm that $\mathbb{C}^2\otimes_{\mathbb{R}}\mathbb{C}^3$ has $\mathbb{R}$-dimension $24$ while $\mathbb{C}^2\otimes_{\mathbb{C}}\mathbb{C}^3$ has $\mathbb{R}$-dimension $12$, and explain the gap in one sentence ("over $\mathbb{R}$, $i$ does not slide across $\otimes$").

---

# Unlocked by This

> [!tip] Right exactness, Tor, and flat modules *(from Homological Algebra)*
> The functor $M\otimes_R -$ is **right exact** but not left exact; the obstruction is measured by the derived functors $\operatorname{Tor}^R_i(M, -)$, and $M$ is **flat** exactly when $M\otimes_R -$ is exact (all higher Tor vanish). The collapse $\mathbb{Z}/p\otimes(\times p) = 0$ is the canonical witness of non-flatness. This is the content of [[Commutative Algebra III — Flatness and Exactness]].

> [!tip] Composite quantum systems and entanglement *(from Quantum Information)*
> The Hilbert space of a system made of parts $A$ and $B$ is $\mathcal{H}_A\otimes_{\mathbb{C}}\mathcal{H}_B$. **Pure tensors** are unentangled product states; the fact that most tensors are not pure is exactly the existence of **entangled** states, with the tensor (Schmidt) rank measuring the entanglement.

> [!tip] The structure sheaf and base change *(from Algebraic Geometry)*
> Tensoring modules is the algebra of **base change** for quasi-coherent sheaves: pulling a module back along a map of spaces is $S\otimes_R(-)$, and the product of varieties has coordinate ring the tensor product of algebras. The construction here is the affine-local model for these global operations.
