---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Classical Matrix Groups"
  - "Def - Lie Group"
  - "Def - Lie Group Homomorphism"
  - "Thm - Product of Smooth Manifolds is a Smooth Manifold"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

This exercise records the two most basic ways of manufacturing new Lie groups out of ones already in hand: taking a Cartesian product, and specialising that product to the $n$-fold power of the circle. Both are used constantly in the sequel — the maximal torus $T^n=U(1)^n$ is the structure group of a diagonal $U(1)^n$-bundle and the model for every gauge theory built out of independent electromagnetic phases, and the covering $\mathbb R^n\to T^n$ is the exponential map of the torus written out by hand.

Let $G$ and $G'$ be Lie groups. Give $G\times G'$ the product smooth structure and the componentwise group operations
$$(g_1,g_1')\cdot(g_2,g_2'):=(g_1g_2,\,g_1'g_2'),\qquad (g,g')^{-1}:=(g^{-1},g'^{-1}),\qquad e_{G\times G'}:=(e_G,e_{G'}).$$

**Part A.** Prove that $G\times G'$ with this structure is a Lie group, and that $\dim(G\times G')=\dim G+\dim G'$.

**Part B.** Define the $n$-torus as the $n$-fold product $T^n:=U(1)^n=U(1)\times\cdots\times U(1)$, where $U(1)=\{z\in\mathbb C:\lvert z\rvert=1\}$ is the unit circle. Prove that $T^n$ is a compact abelian Lie group of dimension $n$, and that the map
$$\phi:\mathbb R^n\longrightarrow T^n,\qquad \phi(x_1,\dots,x_n)=\bigl(e^{2\pi ix_1},\dots,e^{2\pi ix_n}\bigr),$$
where $\mathbb R^n$ carries its additive Lie group structure, is a surjective Lie group homomorphism with kernel $\ker\phi=\mathbb Z^n$.

> [!warning] Convention: source labelling
> Bär states the product construction twice — once as Definition 1.1.3 (the group structure on $G\times G'$) and once as the worked Example 1.1.5 / Exercise 1.1.6, both on p. 8, which are the source items **B-D1.1.3** and **B-E1.1.6** covered here. Neither source spells out the torus $T^n$ or the covering $\mathbb R^n\to T^n$ in §1.1; that material is standard and is supplied in full below. Throughout, $U(1)$, $G\times G'$, and $T^n$ are as fixed on **[[Def - Classical Matrix Groups|the classical-groups page]]**.

**Recall:**

The objects in play are a Lie group, a Lie group homomorphism, the product smooth structure on a Cartesian product of manifolds, and the unit circle $U(1)$.

![[Def - Lie Group#The Definition]]

A [[Def - Lie Group|Lie group]] is a smooth manifold $G$ that is also a group, whose multiplication $m:G\times G\to G$, $m(g,h)=gh$, and inversion $i:G\to G$, $i(g)=g^{-1}$, are both smooth maps of manifolds; its dimension as a Lie group is its dimension as a manifold.

![[Def - Lie Group Homomorphism#The Definition]]

A [[Def - Lie Group Homomorphism|Lie group homomorphism]] $F:G\to H$ is a map that is simultaneously smooth and a group homomorphism, $F(g_1g_2)=F(g_1)F(g_2)$; its **kernel** is $\ker F=\{g\in G:F(g)=e_H\}$.

![[Thm - Product of Smooth Manifolds is a Smooth Manifold#Statement]]

The product theorem supplies more than a smooth structure: it establishes the **characteristic property** of that structure (proved in its Lemma Decomposition). The projections $\pi_i:M_1\times\cdots\times M_k\to M_i$ are smooth; a map $F:N\to M_1\times\cdots\times M_k$ into a product is smooth **if and only if** each component $\pi_i\circ F:N\to M_i$ is smooth; and consequently a product of smooth maps $f_1\times\cdots\times f_k:M_1\times\cdots\times M_k\to N_1\times\cdots\times N_k$ is smooth. We use exactly these three facts. The circle $U(1)=\{z\in\mathbb C:\bar zz=1\}\subset GL(1;\mathbb C)$ is, as established on **[[Def - Classical Matrix Groups|the classical-groups page]]**, a one-dimensional compact abelian Lie group, diffeomorphic to $S^1$.

---

# Convergent Strategy

**Problem class.** Both parts are *verify-the-axioms* problems for a manufactured structure: an object is handed to us pre-assembled (the product manifold, the product group operations, the exponential-style map $\phi$), and the task is to check that it lands inside a known category — Lie groups in Part A, and additionally *compact abelian* Lie groups plus a *homomorphism with prescribed kernel* in Part B. The whole difficulty is bookkeeping: keeping the manifold structure and the group structure aligned so that "smooth" and "homomorphism" are checked against the *same* product decomposition.

**Assumption pattern.** The recognisable trigger for Part A is that every ingredient of "Lie group" splits along the product: the manifold splits (product smooth structure), the group operations split (componentwise), and therefore the *smoothness of the operations* should split too. The one hypothesis that is not automatic is smoothness of the multiplication map, because its domain $(G\times G')\times(G\times G')$ has its two "$G$-slots" and two "$G'$-slots" interleaved; the pattern is to *un-interleave them with a shuffle diffeomorphism* and then apply "product of smooth maps is smooth". Part B is Part A iterated ($T^n$ is a product), plus three independent one-line checks — compactness, commutativity, and the analysis of $\phi$ — each of which reduces to a single standard fact about the complex exponential.

**Theorem routing.** Part A routes entirely through **[[Thm - Product of Smooth Manifolds is a Smooth Manifold|the product-manifold theorem]]** and its characteristic property: the manifold structure and dimension come from the theorem itself; smoothness of inversion is "product of two smooth maps is smooth"; smoothness of multiplication is "compose the shuffle diffeomorphism with the product of the two multiplications, each factor smooth". Part B routes through Part A (by induction, $T^n$ is a Lie group of dimension $n$), through Heine–Borel and the finite-product-of-compacts fact (compactness), through commutativity of $U(1)$ (abelian), and through the single identity $e^{2\pi it}=1\iff t\in\mathbb Z$ (surjectivity and kernel of $\phi$).

**Key decision point.** The one genuinely non-mechanical move is the **shuffle diffeomorphism** $\sigma$ in Part A. The multiplication of the product group is *not* directly a product of maps, because its two arguments each carry a $G$-component and a $G'$-component; written naively it is a map $(G\times G')^2\to G\times G'$ with no evident product structure. Recognising that $(G\times G')^2$ is canonically diffeomorphic to $(G\times G)\times(G'\times G')$ — grouping the two $G$-slots together and the two $G'$-slots together — is what turns the multiplication into $(m\times m')\circ\sigma$, a composite of smooth maps. Everything else is componentwise verification.

---

# Legal Operations Used

This solution deploys the following operations from **[[Gauge Theory I — Lie Groups, Representations, and Group Actions#Legal Operations|the topic page's Legal Operations]]**; where the topic page is not yet assembled, each is named descriptively.

1. **Build a Lie group as a product (the product construction).** Assemble a new Lie group from two given ones by giving the Cartesian product the product smooth structure and componentwise operations; the manifold structure and dimension are supplied by the product-manifold theorem.

2. **Split a group axiom along the factors.** Verify associativity, identity, and inverses one coordinate at a time, using that each holds in $G$ and in $G'$ separately.

3. **Reduce smoothness into a product to smoothness of the components (characteristic property).** A map into $G\times G'$ is smooth precisely when each of its two components is smooth; a product of smooth maps is smooth.

4. **Un-interleave a product-of-products with a shuffle diffeomorphism.** Rewrite $(G\times G')\times(G\times G')$ as $(G\times G)\times(G'\times G')$ by the canonical coordinate permutation, so that the componentwise multiplication becomes a product of the two factor multiplications.

5. **Iterate a binary construction to an $n$-fold one (induction on the number of factors).** Extend "product of two Lie groups is a Lie group" to "finite product of Lie groups is a Lie group" by induction, so that $T^n=U(1)^n$ is a Lie group of dimension $n$.

6. **Inherit topological and algebraic properties factorwise.** A finite product of compact spaces is compact, and a finite product of abelian groups is abelian; read these off the factors.

7. **Analyse a homomorphism through a single scalar identity.** Reduce the homomorphism property, surjectivity, and kernel of $\phi$ to the componentwise behaviour of $t\mapsto e^{2\pi it}$, governed by $e^{2\pi it}=1\iff t\in\mathbb Z$.

---

# Hints

> [!note]- Hint 1
> For Part A the manifold and its dimension are not yours to build — they are exactly what **[[Thm - Product of Smooth Manifolds is a Smooth Manifold|the product-manifold theorem]]** delivers. The only thing left to prove is that the two *group operations* are smooth. Which two maps are those, and what are their domains and codomains?

> [!note]- Hint 2
> Inversion on $G\times G'$ is $(g,g')\mapsto(g^{-1},g'^{-1})$, i.e. it is literally $i\times i'$ where $i,i'$ are the (smooth) inversions of $G,G'$. A product of smooth maps is smooth — that closes inversion in one line. Multiplication is the harder one: write out its domain and notice that the two $G$-entries and two $G'$-entries are interleaved.

> [!note]- Hint 3
> To un-interleave, use the *shuffle*
> $$\sigma\bigl((g_1,g_1'),(g_2,g_2')\bigr)=\bigl((g_1,g_2),(g_1',g_2')\bigr),$$
> a diffeomorphism $(G\times G')^2\to(G\times G)\times(G'\times G')$. Check it is smooth with smooth inverse using the characteristic property (each component is a composition of projections). Then the product multiplication is $(m\times m')\circ\sigma$. Why is that smooth?

> [!note]- Hint 4
> For Part B, $T^n=U(1)^n$ is a *product*, so Part A (iterated $n-1$ times) already makes it a Lie group of dimension $n\cdot\dim U(1)=n$. Compactness: $U(1)\cong S^1$ is compact by Heine–Borel, and a finite product of compact spaces is compact. Abelian: each factor $U(1)$ is abelian and the operation is componentwise. What remains is only $\phi$.

> [!note]- Hint 5
> Everything about $\phi(x)=(e^{2\pi ix_1},\dots,e^{2\pi ix_n})$ reduces to one fact about a single circle. The homomorphism property is $e^{2\pi i(x_j+y_j)}=e^{2\pi ix_j}e^{2\pi iy_j}$. Surjectivity is: every $z$ with $\lvert z\rvert=1$ is $e^{i\theta}$ for some real $\theta$. The kernel is governed by $e^{2\pi it}=1\iff t\in\mathbb Z$ — prove that last equivalence from $e^{i\alpha}=\cos\alpha+i\sin\alpha$.

---

# Solution

The plan is to prove Part A first and then reuse it. In Part A the manifold, its dimension, and the three pieces of the characteristic property are imported from the product-manifold theorem; the only labour is smoothness of the two group operations, which we obtain by expressing inversion as a product of smooth maps and multiplication as the product of the two factor multiplications precomposed with a shuffle. Part B then observes that $T^n$ is an $n$-fold product, so it is a Lie group of dimension $n$ by Part A, reads compactness and commutativity off the factors, and finishes by analysing $\phi$ componentwise through the single identity $e^{2\pi it}=1\iff t\in\mathbb Z$.

**Step 1: Import the manifold structure and dimension of $G\times G'$.**

By the product-manifold theorem, $G\times G'$ is a smooth manifold of dimension $\dim G+\dim G'$, and it comes equipped with smooth projections and the characteristic property of smooth maps into a product.

> [!note]- Derivation
> Let $G$ and $G'$ be [[Def - Lie Group|Lie groups]], hence in particular smooth manifolds, of dimensions $\dim G$ and $\dim G'$. By **[[Thm - Product of Smooth Manifolds is a Smooth Manifold|the product-manifold theorem]]** — *the product $M_1\times\cdots\times M_k$ of smooth manifolds, with the product topology and the product atlas $\{(U_{\alpha_1}\times\cdots\times U_{\alpha_k},\varphi_{\alpha_1}\times\cdots\times\varphi_{\alpha_k})\}$, is a smooth manifold of dimension $n_1+\cdots+n_k$* — applied with $k=2$, $M_1=G$, $M_2=G'$, the space $G\times G'$ with the product smooth structure is a smooth manifold and
> $$\dim(G\times G')=\dim G+\dim G'\qquad\text{(dimension clause of the product-manifold theorem)}.$$
> The same theorem records the **characteristic property** of this smooth structure, which we invoke repeatedly below: the projections $\pi_1:G\times G'\to G$ and $\pi_2:G\times G'\to G'$ are smooth, and a map $F:N\to G\times G'$ from any smooth manifold $N$ is smooth if and only if both components $\pi_1\circ F$ and $\pi_2\circ F$ are smooth. A consequence, also from the theorem, is that a product of smooth maps is smooth. This settles the manifold half of "Lie group"; the dimension claim of Part A is already proved.

**Step 2: Verify the group axioms componentwise.**

With the componentwise operations, associativity, the identity law, and the inverse law each hold coordinate by coordinate because they hold in $G$ and in $G'$.

> [!note]- Derivation
> Write elements of $G\times G'$ as pairs $(g,g')$ with $g\in G$, $g'\in G'$. The operation is $(g_1,g_1')(g_2,g_2')=(g_1g_2,g_1'g_2')$, the proposed identity is $(e_G,e_{G'})$, and the proposed inverse of $(g,g')$ is $(g^{-1},g'^{-1})$.
>
> *Associativity.* For $(g_i,g_i')$, $i=1,2,3$,
> $$\bigl[(g_1,g_1')(g_2,g_2')\bigr](g_3,g_3')=(g_1g_2,g_1'g_2')(g_3,g_3')=\bigl((g_1g_2)g_3,\,(g_1'g_2')g_3'\bigr)\qquad\text{(definition of the product operation, twice)},$$
> $$(g_1,g_1')\bigl[(g_2,g_2')(g_3,g_3')\bigr]=(g_1,g_1')(g_2g_3,g_2'g_3')=\bigl(g_1(g_2g_3),\,g_1'(g_2'g_3')\bigr)\qquad\text{(definition of the product operation, twice)}.$$
> These agree because $(g_1g_2)g_3=g_1(g_2g_3)$ (associativity in the group $G$) and $(g_1'g_2')g_3'=g_1'(g_2'g_3')$ (associativity in the group $G'$).
>
> *Identity.* $(e_G,e_{G'})(g,g')=(e_Gg,e_{G'}g')=(g,g')$ (identity law in $G$ and in $G'$), and symmetrically on the right.
>
> *Inverses.* $(g,g')(g^{-1},g'^{-1})=(gg^{-1},g'g'^{-1})=(e_G,e_{G'})$ (inverse law in $G$ and in $G'$), and symmetrically on the left.
>
> Hence $(G\times G',\,\cdot\,)$ is a group, each of the three axioms reduced to the corresponding axiom holding simultaneously in the two factors $G$ and $G'$.

**Step 3: Inversion on $G\times G'$ is smooth.**

The inversion map of the product group is the product of the two factor inversions, hence smooth.

> [!note]- Derivation
> Let $i:G\to G$, $i(g)=g^{-1}$, and $i':G'\to G'$, $i'(g')=g'^{-1}$, be the inversion maps of $G$ and $G'$; both are smooth because $G$ and $G'$ are Lie groups (smoothness of inversion is part of the definition of a Lie group). The inversion of the product group is
> $$I:G\times G'\to G\times G',\qquad I(g,g')=(g^{-1},g'^{-1})=(i(g),i'(g'))=(i\times i')(g,g').$$
> Thus $I=i\times i'$ is a product of two smooth maps, and a product of smooth maps is smooth (**characteristic property**, Step 1). Therefore $I$ is smooth.

**Step 4: Multiplication on $G\times G'$ is smooth.**

Un-interleaving the two arguments with a shuffle diffeomorphism exhibits the product multiplication as $(m\times m')\circ\sigma$, a composite of smooth maps.

> [!note]- Derivation
> Let $m:G\times G\to G$ and $m':G'\times G'\to G'$ be the (smooth) multiplications of $G$ and $G'$. The multiplication of the product group is
> $$M:(G\times G')\times(G\times G')\to G\times G',\qquad M\bigl((g_1,g_1'),(g_2,g_2')\bigr)=(g_1g_2,\,g_1'g_2').$$
> Its domain interleaves the two $G$-entries $g_1,g_2$ with the two $G'$-entries $g_1',g_2'$, so $M$ is not *directly* a product of maps. Introduce the **shuffle**
> $$\sigma:(G\times G')\times(G\times G')\to(G\times G)\times(G'\times G'),\qquad \sigma\bigl((g_1,g_1'),(g_2,g_2')\bigr)=\bigl((g_1,g_2),(g_1',g_2')\bigr).$$
>
> *$\sigma$ is smooth.* Both the source and target are iterated products, so all projections in sight are smooth. Write $P_1,P_2:(G\times G')\times(G\times G')\to G\times G'$ for the two outer projections, and $\pi_1,\pi_2:G\times G'\to G,G'$ for the inner ones (all smooth, Step 1). By the characteristic property, $\sigma$ is smooth if and only if its two components into $G\times G$ and $G'\times G'$ are smooth; and each of *those* is smooth if and only if its two $G$- (respectively $G'$-) valued components are smooth. Those components are
> $$(g_1,g_2)\text{-part: }\pi_1\circ P_1\ \text{and}\ \pi_1\circ P_2,\qquad (g_1',g_2')\text{-part: }\pi_2\circ P_1\ \text{and}\ \pi_2\circ P_2,$$
> each a composition of smooth projections, hence smooth. Therefore $\sigma$ is smooth. (Its inverse is the same shuffle read backwards, smooth by the identical argument, so $\sigma$ is in fact a diffeomorphism, though we need only its smoothness.)
>
> *Factor as a composite.* Directly from the definitions,
> $$(m\times m')\circ\sigma\bigl((g_1,g_1'),(g_2,g_2')\bigr)=(m\times m')\bigl((g_1,g_2),(g_1',g_2')\bigr)=(m(g_1,g_2),\,m'(g_1',g_2'))=(g_1g_2,\,g_1'g_2')=M\bigl((g_1,g_1'),(g_2,g_2')\bigr).$$
> Hence $M=(m\times m')\circ\sigma$. The map $m\times m'$ is a product of the two smooth maps $m,m'$, hence smooth (**characteristic property**); $\sigma$ is smooth; and a composition of smooth maps is smooth. Therefore $M$ is smooth.

**Step 5: Conclude Part A.**

$G\times G'$ is a smooth manifold and a group whose multiplication and inversion are smooth: it is a Lie group, of dimension $\dim G+\dim G'$.

> [!note]- Derivation
> By Step 1 it is a smooth manifold of dimension $\dim G+\dim G'$; by Step 2 it is a group; by Steps 3 and 4 the group operations $I$ and $M$ are smooth. The three requirements in the definition of a [[Def - Lie Group|Lie group]] — smooth manifold, group, smooth structure maps — are met. Hence $G\times G'$ is a Lie group, and its Lie-group dimension equals its manifold dimension $\dim G+\dim G'$. This proves Part A.

**Step 6: $T^n=U(1)^n$ is a Lie group of dimension $n$.**

Iterating Part A across the $n$ factors makes the $n$-torus a Lie group, and the dimensions add to $n$.

> [!note]- Derivation
> As fixed on **[[Def - Classical Matrix Groups|the classical-groups page]]**, $U(1)=\{z\in\mathbb C:\lvert z\rvert=1\}$ is a Lie group of dimension $1$. We prove by induction on $k\ge1$ that the $k$-fold product $U(1)^k$ is a Lie group of dimension $k$.
>
> *Base case $k=1$.* $U(1)^1=U(1)$ is a Lie group of dimension $1$.
>
> *Inductive step.* Suppose $U(1)^k$ is a Lie group of dimension $k$. Then $U(1)^{k+1}=U(1)^k\times U(1)$ is a product of two Lie groups, so by Part A it is a Lie group of dimension $\dim U(1)^k+\dim U(1)=k+1$. (Here the product manifold $U(1)^k\times U(1)$ carries the same smooth structure as the iterated product $U(1)\times\cdots\times U(1)$: the product-manifold theorem's atlas is associative up to the canonical identification of $(U(1)^k)\times U(1)$ with $U(1)^{k+1}$, since a product of product charts is again a product chart in the $(k+1)$-fold atlas.)
>
> By induction, $T^n=U(1)^n$ is a Lie group of dimension $n$. Its group operation is componentwise multiplication of unit-modulus complex numbers, $(z_1,\dots,z_n)(w_1,\dots,w_n)=(z_1w_1,\dots,z_nw_n)$.

**Step 7: $T^n$ is abelian and compact.**

Commutativity is inherited factorwise, and compactness follows from Heine–Borel on each circle together with the finite-product-of-compacts theorem.

> [!note]- Derivation
> *Abelian.* Fix $(z_1,\dots,z_n),(w_1,\dots,w_n)\in T^n$. Then
> $$(z_1,\dots,z_n)(w_1,\dots,w_n)=(z_1w_1,\dots,z_nw_n)=(w_1z_1,\dots,w_nz_n)=(w_1,\dots,w_n)(z_1,\dots,z_n)\qquad\text{(componentwise, since }z_jw_j=w_jz_j\text{ in }\mathbb C\text{ for each }j\text{)}.$$
> The interchange $z_jw_j=w_jz_j$ is commutativity of multiplication in $\mathbb C$, which restricts to $U(1)$. Hence $T^n$ is abelian.
>
> *Compact.* The circle $U(1)=\{z\in\mathbb C:\lvert z\rvert=1\}$ is a closed and bounded subset of $\mathbb C\cong\mathbb R^2$: bounded because every point has modulus $1$, and closed because it is the preimage $\lvert\cdot\rvert^{-1}(\{1\})$ of the closed set $\{1\}$ under the continuous modulus map. By the Heine–Borel theorem a closed and bounded subset of $\mathbb R^2$ is compact, so $U(1)$ is compact. A finite product of compact topological spaces is compact (the finite case of Tychonoff's theorem, which needs no choice). Therefore $T^n=U(1)^n$, carrying the product topology, is compact.

**Step 8: $\phi$ is a smooth homomorphism.**

Each component $x\mapsto e^{2\pi ix_j}$ is smooth and the exponential turns addition into multiplication, so $\phi$ is a Lie group homomorphism.

> [!note]- Derivation
> Give $\mathbb R^n$ its additive Lie group structure (a Lie group: $\mathbb R^n$ is a smooth manifold and $(x,y)\mapsto x+y$, $x\mapsto-x$ are smooth). Consider
> $$\phi:\mathbb R^n\to T^n,\qquad \phi(x)=\bigl(e^{2\pi ix_1},\dots,e^{2\pi ix_n}\bigr),\qquad x=(x_1,\dots,x_n).$$
>
> *Well-defined into $T^n$.* For each real $x_j$, $\lvert e^{2\pi ix_j}\rvert=\lvert\cos(2\pi x_j)+i\sin(2\pi x_j)\rvert=\sqrt{\cos^2(2\pi x_j)+\sin^2(2\pi x_j)}=1$, so $e^{2\pi ix_j}\in U(1)$ and $\phi(x)\in T^n$.
>
> *Smooth.* By the **characteristic property** (Step 1), $\phi$ is smooth if and only if each component $\phi_j:\mathbb R^n\to U(1)$, $\phi_j(x)=e^{2\pi ix_j}$, is smooth. Now $U(1)$ is an embedded submanifold of $\mathbb C\cong\mathbb R^2$, and the map $\mathbb R^n\to\mathbb R^2$, $x\mapsto(\cos(2\pi x_j),\sin(2\pi x_j))$, is smooth (each coordinate is a composition of the smooth linear map $x\mapsto 2\pi x_j$ with the smooth functions $\cos,\sin$). A smooth map into $\mathbb R^2$ whose image lies in the embedded submanifold $U(1)$ is smooth as a map into $U(1)$. Hence each $\phi_j$ is smooth, and therefore $\phi$ is smooth.
>
> *Homomorphism.* For $x,y\in\mathbb R^n$, using $e^{a+b}=e^ae^b$ in each slot,
> $$\phi(x+y)=\bigl(e^{2\pi i(x_j+y_j)}\bigr)_{j=1}^n=\bigl(e^{2\pi ix_j}e^{2\pi iy_j}\bigr)_{j=1}^n=\bigl(e^{2\pi ix_j}\bigr)_{j=1}^n\bigl(e^{2\pi iy_j}\bigr)_{j=1}^n=\phi(x)\phi(y),$$
> where the third equality is the definition of componentwise multiplication in $T^n$. So $\phi(x+y)=\phi(x)\phi(y)$: $\phi$ is a group homomorphism. Being also smooth, $\phi$ is a [[Def - Lie Group Homomorphism|Lie group homomorphism]].

**Step 9: $\phi$ is surjective with kernel $\mathbb Z^n$.**

Polar form gives surjectivity; the identity $e^{2\pi it}=1\iff t\in\mathbb Z$, applied in each slot, gives the kernel.

> [!note]- Derivation
> *The scalar identity.* For $t\in\mathbb R$,
> $$e^{2\pi it}=1\iff\cos(2\pi t)=1\ \text{and}\ \sin(2\pi t)=0\iff 2\pi t\in 2\pi\mathbb Z\iff t\in\mathbb Z,$$
> where the first equivalence is $e^{2\pi it}=\cos(2\pi t)+i\sin(2\pi t)$ together with equality of complex numbers meaning equality of real and imaginary parts, and the second is the fact that $\cos\alpha=1$ (equivalently $\sin\alpha=0$ with $\cos\alpha\ge0$) holds exactly at the integer multiples of $2\pi$.
>
> *Surjective.* Let $(z_1,\dots,z_n)\in T^n$, so $\lvert z_j\rvert=1$ for each $j$. By the polar representation of a unit-modulus complex number, each $z_j=e^{i\theta_j}$ for some $\theta_j\in\mathbb R$ (concretely $\theta_j=\operatorname{atan2}(\operatorname{Im}z_j,\operatorname{Re}z_j)$). Put $x_j:=\theta_j/(2\pi)$ and $x:=(x_1,\dots,x_n)\in\mathbb R^n$. Then
> $$\phi(x)=\bigl(e^{2\pi ix_j}\bigr)_{j=1}^n=\bigl(e^{i\theta_j}\bigr)_{j=1}^n=(z_1,\dots,z_n)\qquad\text{(by the choice }2\pi x_j=\theta_j\text{)}.$$
> Hence $\phi$ is surjective.
>
> *Kernel.* The identity element of $T^n$ is $(1,\dots,1)$. For $x\in\mathbb R^n$,
> $$x\in\ker\phi\iff\phi(x)=(1,\dots,1)\iff e^{2\pi ix_j}=1\ \text{for every }j\iff x_j\in\mathbb Z\ \text{for every }j\iff x\in\mathbb Z^n,$$
> where the third equivalence applies the scalar identity in each slot separately. Therefore $\ker\phi=\mathbb Z^n$, completing Part B.

> [!note]- Complete formal solution
> **Part A.** Let $G,G'$ be Lie groups. By **[[Thm - Product of Smooth Manifolds is a Smooth Manifold|the product-manifold theorem]]**, $G\times G'$ is a smooth manifold of dimension $\dim G+\dim G'$, with smooth projections and the characteristic property: a map into $G\times G'$ is smooth iff its two components are, and a product of smooth maps is smooth.
>
> With $(g_1,g_1')(g_2,g_2')=(g_1g_2,g_1'g_2')$, identity $(e_G,e_{G'})$, and inverse $(g,g')^{-1}=(g^{-1},g'^{-1})$, the group axioms hold coordinatewise: associativity, the identity law, and the inverse law each follow from the corresponding axiom in $G$ and in $G'$.
>
> Inversion is $I=i\times i'$ with $i,i'$ the smooth inversions of $G,G'$; a product of smooth maps is smooth, so $I$ is smooth. Multiplication is $M=(m\times m')\circ\sigma$, where $m,m'$ are the smooth multiplications and $\sigma((g_1,g_1'),(g_2,g_2'))=((g_1,g_2),(g_1',g_2'))$ is the shuffle; $\sigma$ is smooth because each of its components is a composition of smooth projections (characteristic property), $m\times m'$ is smooth as a product of smooth maps, and a composite of smooth maps is smooth, so $M$ is smooth. Thus $G\times G'$ is a smooth manifold and a group with smooth operations: a Lie group of dimension $\dim G+\dim G'$.
>
> **Part B.** By induction on $k$ using Part A, $U(1)^k$ is a Lie group of dimension $k$ (base $U(1)$ of dimension $1$; step $U(1)^{k+1}=U(1)^k\times U(1)$). Hence $T^n=U(1)^n$ is a Lie group of dimension $n$, with componentwise multiplication. It is abelian because $z_jw_j=w_jz_j$ in each slot, and compact because $U(1)$ is closed and bounded in $\mathbb C\cong\mathbb R^2$ (Heine–Borel) and a finite product of compact spaces is compact.
>
> Define $\phi:\mathbb R^n\to T^n$ by $\phi(x)=(e^{2\pi ix_1},\dots,e^{2\pi ix_n})$. Each $e^{2\pi ix_j}$ has modulus $1$, so $\phi$ maps into $T^n$; each component is smooth (composition of $x\mapsto 2\pi x_j$ with $\cos,\sin$, landing in the embedded submanifold $U(1)$), so $\phi$ is smooth by the characteristic property. From $e^{a+b}=e^ae^b$, $\phi(x+y)=\phi(x)\phi(y)$, so $\phi$ is a Lie group homomorphism. Given $(z_1,\dots,z_n)\in T^n$, write $z_j=e^{i\theta_j}$ (polar form) and set $x_j=\theta_j/(2\pi)$; then $\phi(x)=(z_1,\dots,z_n)$, so $\phi$ is surjective. Finally, using $e^{2\pi it}=1\iff\cos(2\pi t)=1$ and $\sin(2\pi t)=0\iff t\in\mathbb Z$ in each slot, $\phi(x)=(1,\dots,1)\iff x_j\in\mathbb Z\ \forall j\iff x\in\mathbb Z^n$, so $\ker\phi=\mathbb Z^n$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "componentwise, so obviously smooth"
> It is tempting to declare the multiplication of $G\times G'$ smooth "because it is componentwise", skipping the shuffle. This is the one place the argument can go wrong. Smoothness into a product is checked component by component, but each component of $M$ — say $(g_1,g_1')\times(g_2,g_2')\mapsto g_1g_2$ — is a map *out of* the interleaved space $(G\times G')^2$, and to see it is smooth one must factor it through the projection $(G\times G')^2\to G\times G$ and then $m$. That factorisation *is* the shuffle. Omitting it leaves the key smoothness claim unjustified; the shortcut becomes legal only once $\sigma$ is exhibited and shown smooth.

---

# Key Takeaways

**The direct product is the "free" way to combine Lie groups, and its only non-automatic check is smoothness of multiplication, which a shuffle diffeomorphism reduces to the factors.** The reusable principle is that *every* structural requirement of "Lie group" is compatible with Cartesian products — the manifold structure (product-manifold theorem), the group axioms (coordinatewise), inversion (a product of maps), and finally multiplication. The trigger to reach for this construction is any situation where two independent symmetries act simultaneously and one wants a single group carrying both; the diagnostic that the construction will succeed is that the operations are defined coordinatewise. The transferable subtlety, worth remembering across the whole subject, is that "coordinatewise operation" does **not** immediately mean "smooth operation", because multiplication has *two* arguments and its domain interleaves the factors; the fix is always the same shuffle $((a,b),(c,d))\mapsto((a,c),(b,d))$ that regroups like with like, after which "product of smooth maps is smooth" finishes the job. This same regrouping recurs when one checks that the multiplication of a matrix group, or of a semidirect product, is smooth.

**Compactness and commutativity are *inherited* properties: a finite product has them exactly when every factor does, so they are read off, never re-proved.** The pattern is that topological and algebraic adjectives which are preserved by finite products — compact, Hausdorff, abelian, connected — need no work on the product beyond citing the factor and the corresponding product theorem (finite Tychonoff for compactness, coordinatewise commutativity for abelian). The trigger is a product structure plus a property one recognises as "productive". The reason $T^n$ is *the* model compact abelian Lie group is precisely this: it is the $n$-fold product of the smallest positive-dimensional compact abelian Lie group $U(1)$, and every compact connected abelian Lie group turns out to be such a torus. When a later chapter asks for the structure group of a bundle of independent electromagnetic phases, or the maximal torus inside a larger compact group, this factorwise inheritance is what makes $T^n$ immediately available with all its properties in hand.

**A homomorphism built out of a single scalar map is understood entirely through that scalar map, and $\mathbb R^n\to T^n$ is the exponential of the torus made explicit.** The covering $\phi(x)=(e^{2\pi ix_j})$ has all three of its features — homomorphism, surjectivity, kernel — reduced to properties of $t\mapsto e^{2\pi it}$: the functional equation $e^{a+b}=e^ae^b$ gives the homomorphism, polar form gives surjectivity, and $e^{2\pi it}=1\iff t\in\mathbb Z$ gives the kernel. The reusable diagnostic is that whenever a map between products is defined slot by slot from one and the same function, every question about it collapses to that one function analysed on a single factor. The payoff here is structural: $\phi$ is a surjective homomorphism with kernel the discrete subgroup $\mathbb Z^n\subset\mathbb R^n$, so the first isomorphism theorem for Lie groups presents the torus as the quotient $T^n\cong\mathbb R^n/\mathbb Z^n$, and $\phi$ itself is the universal covering map of $T^n$ and the Lie-group exponential $\exp:\mathfrak t=\mathbb R^n\to T^n$ written in coordinates. Every later statement about characters of the torus, about $U(1)^n$-connections, and about the lattice $\mathbb Z^n$ of the torus rests on exactly this presentation. Companion exercises: **[[Ex - The Classical Groups are Closed Subgroups of GL(n)|the closed-subgroup verifications]]** build the other classical Lie groups, and **[[Thm - SO(2) is Isomorphic to U(1)|the SO(2) ≅ U(1) identification]]** analyses the single circle factor that this exercise raised to the $n$-th power.
