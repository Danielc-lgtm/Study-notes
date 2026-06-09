---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Module Homomorphism"
  - "Def - Direct Sum of Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules are unital. Let $R$ be a ring and $M, N, L, M_1,\dots,M_k$ be [[Def - Module|R-modules]]. We write $f : M\times N\to L$ for a function on the Cartesian product of the underlying sets, $m_0\in M$, $n_0\in N$ for fixed ("frozen") arguments, and $\operatorname{Bil}_R(M\times N, L)$ for the set of $R$-bilinear maps $M\times N\to L$. An $R$-[[Def - Module Homomorphism|linear map]] is a homomorphism of $R$-modules; $\operatorname{Hom}_R(M, L)$ is the $R$-module of these. The full registry is on [[Commutative Algebra II — Tensor Products]].

This is a compound page: it defines two interlocking notions — the **bilinear map** (two arguments) and the **multilinear map** ($k$ arguments) — because the second is the literal generalisation of the first and they are used interchangeably (a bilinear map is a $2$-multilinear map). The single example to keep in mind throughout is ordinary multiplication $R\times R\to R$, $(a,b)\mapsto ab$, which is bilinear but not linear.

---

# Axiom Motivation

The category of modules has exactly one kind of structure-preserving map: the $R$-linear map, a function $\varphi$ with $\varphi(m+m') = \varphi(m)+\varphi(m')$ and $\varphi(rm) = r\varphi(m)$. This is enough to express addition and scaling, but it cannot express *multiplication*, and multiplication is everywhere. Ring multiplication $ab$, the scalar action $r\cdot m$, an inner product $\langle v, w\rangle$, matrix multiplication, the evaluation $\varphi(v)$ of a functional on a vector, the determinant as a function of the columns of a matrix — every one of these takes *two (or more) inputs* and is linear in each *separately* but not in the pair as a whole. We need a name for this phenomenon, and the name must be chosen so that the objects it picks out are exactly those we can later "linearise" by the tensor product.

**Why "linear in each slot separately" and not "linear on the product".** The naive guess would be to ask $f : M\times N\to L$ to be linear as a map out of the module $M\times N = M\oplus N$. But that is the *wrong* condition — it excludes multiplication. Linearity on $M\oplus N$ would demand $f(m+m', n+n') = f(m,n) + f(m',n')$ and $f(r(m,n)) = rf(m,n)$. Test this on $f(a,b) = ab$ in $R$: linearity would force $f(2a, 2b) = 2f(a,b)$, but in fact $f(2a,2b) = 4ab = 4f(a,b)$. Multiplication is *quadratic*, not linear, on the product. So we must ask for something weaker and asymmetric: linearity in $m$ with $n$ held fixed, and separately linearity in $n$ with $m$ held fixed. Now $f(a,b) = ab$ passes: with $b$ fixed, $a\mapsto ab$ is linear, and symmetrically. This is the **bilinear** condition, and it was forced by the demand that multiplication be an instance.

**Why both slots, and what each axiom buys.** The definition has two independent requirements — linearity in the first slot, linearity in the second — and dropping either is a real loss. Drop linearity in the *first* slot (keep only the second): then $f(a,b) = a^2 b$ qualifies, but it is degree-$2$ in $a$, so $f$ no longer factors through any object built to linearise *both* arguments; the determinant, which is multilinear in *all* columns, would not be captured. Drop linearity in the *second* slot symmetrically and you lose, e.g., the inner product's right-linearity. The two conditions are genuinely separate: a map can be linear in the first argument and nonlinear in the second (take $f(a,b) = ab^2$), so neither implies the other, and both must be imposed. What the *conjunction* buys is the universal property of the tensor product: a map is bilinear exactly when it factors through $M\otimes_R N$ via an honest linear map — bilinearity is *precisely* the input type the [[Thm - Universal Property of the Tensor Product of Modules|tensor product linearises]]. If we strengthened to "linear on $M\oplus N$" we would capture too little (only additive-in-both maps with no cross terms, which the [[Def - Direct Sum of Modules|direct sum]] already handles via $\operatorname{Hom}(M\oplus N, L)\cong\operatorname{Hom}(M,L)\times\operatorname{Hom}(N,L)$); if we weakened to "additive in each slot" we would drop the scalar condition and capture too much ($\mathbb{Z}$-bilinear maps that ignore the $R$-structure).

**Why the scalar can be pulled from either slot, and why it lands on the *same* output.** Bilinearity requires $f(rm, n) = rf(m,n)$ and $f(m, rn) = rf(m,n)$ — the scalar may be extracted from *either* argument, and both give the *same* element $rf(m,n)$. This is not automatic; it is the precise reflection of the relation $r(m\otimes n) = (rm)\otimes n = m\otimes(rn)$ that the tensor product will impose. Over a *noncommutative* ring this symmetry breaks (one must distinguish left and right modules, and "$rf(m,n)$" is ambiguous), which is exactly why the clean theory of tensor products lives over commutative rings. The commutativity of $R$ is silently doing the work that lets a scalar slide freely across the two arguments.

**Why generalise to $k$ arguments at all.** Once "linear in each slot separately" is the right idea, there is no reason to stop at two slots. A $k$-multilinear map $f : M_1\times\cdots\times M_k\to L$ is linear in each of its $k$ arguments with the rest fixed. This is forced on us the moment we iterate the tensor product: associativity $(M\otimes N)\otimes P\cong M\otimes N\otimes P$ only makes sense if $M\otimes N\otimes P$ is the universal receptacle for *trilinear* maps, so the trilinear notion has to exist. The determinant of an $n\times n$ matrix, viewed as a function of its $n$ columns, is the archetypal alternating $n$-multilinear map, and it is the reason the exterior power $\Lambda^n$ exists. So the multilinear definition is not gratuitous generality — it is what makes iterated and alternating tensor constructions definable.

---

# The Definition

Let $R$ be a commutative ring and $M, N, L$ be $R$-modules.

## Bilinear map

A function $f : M\times N\to L$ is **$R$-bilinear** if it is $R$-[[Def - Module Homomorphism|linear]] in each argument when the other is held fixed: for all $m, m'\in M$, $n, n'\in N$, $r\in R$,
$$f(m+m', n) = f(m,n) + f(m',n), \qquad f(m, n+n') = f(m,n) + f(m,n'),$$
$$f(rm, n) = r\,f(m,n) = f(m, rn).$$
Equivalently, for every fixed $n_0\in N$ the map $m\mapsto f(m, n_0)$ lies in $\operatorname{Hom}_R(M, L)$, and for every fixed $m_0\in M$ the map $n\mapsto f(m_0, n)$ lies in $\operatorname{Hom}_R(N, L)$. The set $\operatorname{Bil}_R(M\times N, L)$ of all such $f$ is itself an $R$-module under pointwise operations.

An immediate consequence: $f(0, n) = f(0\cdot 0, n) = 0\cdot f(0,n) = 0$, and likewise $f(m, 0) = 0$.

## Multilinear map

A function $f : M_1\times\cdots\times M_k\to L$ is **$k$-multilinear** (or **$R$-multilinear**) if for each index $i$ and all fixed $m_j\in M_j$ ($j\neq i$), the map
$$x\ \longmapsto\ f(m_1,\dots,m_{i-1}, x, m_{i+1},\dots,m_k) : M_i\to L$$
is $R$-linear. The cases $k=1$ (linear), $k=2$ (bilinear), $k=3$ (trilinear) are the common ones. A multilinear map is **alternating** if it vanishes whenever two arguments are equal, and **symmetric** if swapping any two arguments leaves it unchanged.

---

# Categorical / Structural Definition

Bilinear maps are exactly the maps that the tensor product is *built to represent*. The assignment $L\mapsto\operatorname{Bil}_R(M\times N, L)$ is a functor from $R$-modules to $R$-modules (a linear map $L\to L'$ post-composes to send bilinear maps to bilinear maps), and the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]] is the statement that this functor is **represented** by $M\otimes_R N$:
$$\operatorname{Bil}_R(M\times N, L)\ \cong\ \operatorname{Hom}_R(M\otimes_R N,\ L),$$
naturally in $L$. In words: a bilinear map out of $M\times N$ is *the same data* as a linear map out of the single module $M\otimes_R N$. This is the categorical content of "bilinearity is linearity in disguise": the tensor product is the universal object that converts the bifunctor $\operatorname{Bil}_R(M\times N, -)$ into the representable functor $\operatorname{Hom}_R(M\otimes N, -)$. Multilinear maps are represented the same way by the iterated tensor product $M_1\otimes\cdots\otimes M_k$.

---

# Relate to Other Fields / Compression

The cleanest compression: **a bilinear map is "multiplication", abstracted away from any particular product.** Wherever two things are multiplied to give a third, linearly in each — scalars times vectors, functionals on vectors, vectors paired by a form, matrices composed — there is a bilinear map, and the tensor product is the universal place that multiplication happens.

**True name:** the true name of bilinearity is *"the input type of the tensor product"*. You rarely care about the $\varepsilon$–$\delta$ of "linear in each slot" for its own sake; you care that a bilinear map is exactly a linear map out of $M\otimes N$, so that recognising a map as bilinear is the trigger to deploy the universal property. When you must build a map *from* a tensor product, the operational reflex is "find the bilinear map on the factors".

In **multilinear and exterior algebra**, the alternating multilinear maps are represented by the exterior powers $\Lambda^k M$, and the symmetric ones by the symmetric powers $\operatorname{Sym}^k M$ — each is a quotient of $M^{\otimes k}$ that forces the corresponding symmetry. The determinant is *the* alternating $n$-multilinear form, basis-free. In **differential geometry**, a tensor field is a section of a bundle whose fibres are multilinear maps on the tangent space, and a differential form is an alternating one; the entire calculus of forms is multilinear algebra done fibrewise over the ring of smooth functions. In **physics**, the metric tensor, the stress tensor, and the curvature tensor are all multilinear maps on tangent spaces.

---

# Examples / Corollaries

**Is an instance — ring multiplication.** For any $R$-algebra $A$, the multiplication $A\times A\to A$, $(a,b)\mapsto ab$, is $R$-bilinear: $(a+a')b = ab+a'b$, $a(b+b') = ab+ab'$, and $(ra)b = r(ab) = a(rb)$. This is the bilinear map that the algebra tensor product $A\otimes_R A\to A$ linearises, and the reason algebra multiplications can be encoded as linear maps $A\otimes A\to A$.

**Is an instance — the evaluation pairing and inner products.** For a vector space $V$ over a field $k$, the evaluation $V^*\times V\to k$, $(\varphi, v)\mapsto\varphi(v)$, is $k$-bilinear. So is any inner product $\langle\,,\rangle : V\times V\to k$ (over $\mathbb{R}$; over $\mathbb{C}$ it is *sesquilinear*, conjugate-linear in one slot, which is *not* bilinear — a useful non-example). The bilinear evaluation pairing is what gives the isomorphism $V^*\otimes W\cong\operatorname{Hom}(V,W)$.

**Is an instance — the determinant is multilinear.** Viewing an $n\times n$ matrix as a list of its $n$ columns $v_1,\dots,v_n\in k^n$, the determinant $\det(v_1,\dots,v_n)$ is $n$-multilinear and alternating: linear in each column separately, and zero if two columns coincide. This is the defining multilinear map of $\Lambda^n k^n$.

**Is NOT an instance — squaring.** The map $f : R\times R\to R$, $f(a,b) = a^2 b$, is *not* bilinear: in the first slot, $f(a+a', b) = (a+a')^2 b = (a^2 + 2aa' + a'^2)b\neq a^2 b + a'^2 b = f(a,b)+f(a',b)$ in general (the cross term $2aa'b$ spoils additivity). It *is* linear in the second slot but not the first; this shows the two slot-conditions are independent and both are needed.

**Is NOT an instance — a constant nonzero map.** The map $f(m,n) = c$ for a fixed $0\neq c\in L$ is not bilinear: $f(0,n) = c\neq 0$, but bilinearity forces $f(0,n) = 0$. More generally any map with nonzero "constant term" fails, because bilinear maps kill $0$ in each slot.

**Corollary — bilinear maps form a module isomorphic to a Hom.** By the universal property, $\operatorname{Bil}_R(M\times N, L)\cong\operatorname{Hom}_R(M\otimes N, L)$; and currying gives $\operatorname{Bil}_R(M\times N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}_R(N, L))$ — a bilinear map is a linear map sending each $m$ to a linear map $n\mapsto f(m,n)$. This **tensor–hom adjunction** $\operatorname{Hom}_R(M\otimes N, L)\cong\operatorname{Hom}_R(M, \operatorname{Hom}(N,L))$ is one of the most reused identities in module theory.

**Calibration check.** Verify that $(a,b)\mapsto ab$ is bilinear but $(a,b)\mapsto a^2b$ is not, by testing additivity in the first slot. Confirm that any bilinear $f$ satisfies $f(0,n) = f(m,0) = 0$. Check that a $\mathbb{C}$-inner product, conjugate-linear in one argument, is *not* $\mathbb{C}$-bilinear but *is* $\mathbb{R}$-bilinear. Finally, convince yourself that "linear on $M\oplus N$" and "bilinear on $M\times N$" are different conditions by noting that the former forces $f(2m,2n) = 2f(m,n)$ while the latter forces $f(2m,2n) = 4f(m,n)$.

---

# Unlocked by This

> [!tip] The tensor, symmetric, and exterior algebras *(from Multilinear Algebra)*
> Multilinear maps of each symmetry type get their own universal receptacle: unrestricted multilinear maps by $M^{\otimes k}$, symmetric ones by $\operatorname{Sym}^k M$, alternating ones by $\Lambda^k M$. Assembling all degrees gives the **tensor algebra** $T(M)$, the **symmetric algebra** $\operatorname{Sym}(M)$ (a polynomial ring when $M$ is free), and the **exterior algebra** $\Lambda(M)$, whose top piece defines the determinant without choosing a basis.

> [!tip] The determinant and orientation, basis-free *(from Linear Algebra / Geometry)*
> Because the alternating $n$-multilinear forms on an $n$-dimensional space form a $1$-dimensional space $\Lambda^n V^*$, the determinant is the *unique* such form up to scale, and a choice of nonzero element of $\Lambda^n V$ is an **orientation**. This is the multilinear-algebra origin of volume forms and orientation in differential geometry.

> [!tip] Tensor fields and differential forms *(from Differential Geometry)*
> A **tensor field** on a manifold assigns to each point a multilinear map on the tangent space; a **differential form** assigns an alternating one. The pointwise multilinear algebra developed here, applied to the cotangent space and varied smoothly, is the entire algebraic substrate of the exterior derivative, the wedge product, and the de Rham complex.
