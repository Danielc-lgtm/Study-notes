---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
  - "Thm - Complex Representations of U(1) and SU(2)"
  - "Def - Associated Bundle"
  - "Def - The Hopf Bundle"
  - "Def - Complex Vector Bundle and Hermitian Structure"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $G=U(1)=\{\lambda\in\mathbb{C}:|\lambda|=1\}$ acts on principal bundles on the **right**, written $p\cdot\lambda$ or $p\lambda$; for $k\in\mathbb{Z}$ let $\varrho_k\colon U(1)\to GL(1;\mathbb{C})$ be the representation $\varrho_k(\lambda)v=\lambda^k v$ of chapter I. Let $\pi\colon P\to M$ be a smooth principal $U(1)$-bundle over a smooth manifold $M$, and for each $k$ form the associated complex line bundle $P\times_{\varrho_k}\mathbb{C}=(P\times\mathbb{C})/U(1)$, whose points are the equivalence classes $[p,v]_k$ of the diagonal right action $(p,v)\cdot\lambda=(p\lambda,\varrho_k(\lambda^{-1})v)=(p\lambda,\lambda^{-k}v)$. Write $L:=P\times_{\varrho_1}\mathbb{C}$ for the case $k=1$.

Prove the following three statements.

1. **(Equivariant-function description.)** For every $k\in\mathbb{Z}$ the smooth sections of $P\times_{\varrho_k}\mathbb{C}$ are in natural bijection with the smooth functions $\hat s\colon P\to\mathbb{C}$ satisfying the homogeneity law
$$\hat s(p\lambda)=\lambda^{-k}\,\hat s(p)\qquad\text{for all }p\in P,\ \lambda\in U(1).$$

2. **(Tensor powers.)** For every $k\in\mathbb{Z}$ there is a canonical isomorphism of complex line bundles
$$P\times_{\varrho_k}\mathbb{C}\;\cong\;L^{\otimes k},$$
where $L^{\otimes 0}$ denotes the trivial line bundle $\underline{\mathbb{C}}=M\times\mathbb{C}$, $L^{\otimes k}=L\otimes\cdots\otimes L$ ($k$ factors) for $k>0$, and $L^{\otimes k}=(L^*)^{\otimes(-k)}$ for $k<0$, with $L^*$ the dual line bundle.

3. **(Coordinate functions on the Hopf bundle.)** Let $P=S^{2n+1}\subset\mathbb{C}^{n+1}$ with the Hopf action $z\cdot\lambda=z\lambda=(z_0\lambda,\dots,z_n\lambda)$, so that $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z\mapsto[z]$, is the Hopf bundle and $L\cong\mathcal{O}(-1)$ is the tautological line bundle. Taking $k=-1$, so that $P\times_{\varrho_{-1}}\mathbb{C}\cong L^{\otimes(-1)}=L^*\cong\mathcal{O}(-1)^*=:\mathcal{O}(1)$, show that each ambient coordinate function
$$z_j\colon S^{2n+1}\to\mathbb{C},\qquad z\mapsto z_j\qquad(j=0,\dots,n),$$
satisfies the homogeneity law for $k=-1$ and therefore defines a global smooth section $s_j$ of $\mathcal{O}(1)$; identify $s_j$ concretely as the restriction of the linear coordinate functional $w_j\colon\mathbb{C}^{n+1}\to\mathbb{C}$ to the tautological lines, and observe that the $n+1$ sections $s_0,\dots,s_n$ have no common zero.

**Recall:**

The objects in play are the associated bundle of a principal $U(1)$-bundle, the equivariant-function description of its sections, the classification of the representations $\varrho_k$ of $U(1)$, and the Hopf bundle with its tautological line bundle.

![[Def - Associated Bundle#The Definition]]

For a principal $G$-bundle $\pi\colon P\to M$ and a representation $\rho\colon G\to GL(V)$, the [[Def - Associated Bundle|associated bundle]] is $P\times_\rho V:=(P\times V)/G$ for the right action $(p,v)\cdot g=(p g,\rho(g^{-1})v)$; its points are classes $[p,v]$, its projection is $[p,v]\mapsto\pi(p)$, and for a fixed $p\in P_m:=\pi^{-1}(m)$ the map $[p,\cdot]\colon V\to(P\times_\rho V)_m$, $v\mapsto[p,v]$, is a linear isomorphism onto the fibre over $m=\pi(p)$. The defining relation between representatives is $[pg,v]=[p,\rho(g)v]$, obtained from $(pg,\rho(g^{-1})w)\sim(p,w)$ by setting $w=\rho(g)v$.

![[Thm - Sections of an Associated Bundle are Equivariant Functions#Statement]]

Explicitly, [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]] states: writing $C^\infty(P;V)^G:=\{\hat s\in C^\infty(P;V):\hat s(pg)=\rho(g^{-1})\hat s(p)\ \forall p,g\}$ for the space of $G$-equivariant $V$-valued functions on $P$, the map $C^\infty(P;V)^G\to\Gamma(P\times_\rho V)$, $\hat s\mapsto s$, defined by the requirement
$$s(\pi(p))=[p,\hat s(p)]\qquad\text{for all }p\in P,$$
is a bijection, and indeed an isomorphism of $C^\infty(M)$-modules. Its inverse sends a section $s$ to the function $\hat s$ whose value $\hat s(p)$ is the unique $v\in V$ with $s(\pi(p))=[p,v]$ (unique because $[p,\cdot]$ is injective, which is freeness and transitivity of the fibre action).

![[Thm - Complex Representations of U(1) and SU(2)#Statement]]

For the present exercise we need only part (A) of [[Thm - Complex Representations of U(1) and SU(2)|the classification]]: the representations $\varrho_k\colon U(1)\to GL(1;\mathbb{C})$, $\varrho_k(\lambda)v=\lambda^k v$ ($k\in\mathbb{Z}$), are pairwise inequivalent irreducible complex representations, and they satisfy $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ and $\varrho_k^*\cong\varrho_{-k}$, where $\otimes$ and $(\cdot)^*$ are the tensor product and dual constructions on representations. Here the dual representation is $\varrho_k^*(\lambda)=\varrho_k(\lambda^{-1})^*=(\lambda^{-k})^*$, which under the canonical identification $\mathbb{C}^*\cong\mathbb{C}$ is multiplication by $\lambda^{-k}$, that is $\varrho_{-k}$.

![[Def - The Hopf Bundle#The Definition]]

The [[Def - The Hopf Bundle|Hopf bundle]] is the principal $U(1)$-bundle $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z=(z_0,\dots,z_n)\mapsto[z]=[z_0:\cdots:z_n]$, with $S^{2n+1}=\{z\in\mathbb{C}^{n+1}:\sum_{i=0}^n|z_i|^2=1\}$ and right action $z\cdot\lambda=z\lambda$. Its associated line bundle for $\varrho_1$ is the tautological (universal) line bundle
$$\mathcal{O}(-1)=\{([z],\ell)\in\mathbb{CP}^n\times\mathbb{C}^{n+1}:\ell\in\mathbb{C}\,z\},$$
the sub-line-bundle of the trivial bundle $\mathbb{CP}^n\times\mathbb{C}^{n+1}$ whose fibre over $[z]$ is the very line $\mathbb{C}\,z\subset\mathbb{C}^{n+1}$ that the point $[z]$ names; the isomorphism $L=S^{2n+1}\times_{\varrho_1}\mathbb{C}\xrightarrow{\ \sim\ }\mathcal{O}(-1)$, $[z,v]_1\mapsto([z],vz)$, is established in [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the companion exercise]] and is recalled in Step 5 below. We write $\mathcal{O}(1):=\mathcal{O}(-1)^*$ for its dual.

---

# Convergent Strategy

**Problem class.** This is a *translate-and-identify* problem in the theory of associated bundles: it asks us to move a computation from the geometric side (sections of a bundle over $M$) to the representation-theoretic side (equivariant functions on the total space $P$), and then back again to a completely explicit model (the tautological line bundle over projective space). The whole point of the associated-bundle formalism is that this dictionary exists; the exercise is a drill in *reading the dictionary in both directions* and watching a single sign — the $\lambda^{-k}$ in the homogeneity law — propagate consistently from the abstract theorem through the tensor-power bookkeeping to the concrete coordinate functions.

**Assumption pattern.** The structure group is *abelian* and *one-dimensional*, and this is used at every turn. Because $U(1)$ is abelian its irreducible complex representations are one-dimensional, so associated bundles $P\times_{\varrho_k}\mathbb{C}$ are line bundles; because they are classified by a single integer $k$ with $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ and $\varrho_k^*\cong\varrho_{-k}$, the assignment $k\mapsto P\times_{\varrho_k}\mathbb{C}$ turns addition of integers into tensor product of line bundles. The recognisable trigger for the entire method is: *a line bundle presented as an associated bundle of a circle bundle, together with a question about its sections or its tensor powers.*

**Theorem routing.** Part 1 is a direct specialisation of [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]] with $V=\mathbb{C}$ and $\rho=\varrho_k$: we substitute $\rho(\lambda^{-1})=\varrho_k(\lambda^{-1})=\lambda^{-k}$ into the equivariance condition and read off the homogeneity law. Part 2 routes through [[Thm - Complex Representations of U(1) and SU(2)|the classification of $U(1)$-representations]]: the two representation identities $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ and $\varrho_k^*\cong\varrho_{-k}$ become two bundle isomorphisms, and an induction on $|k|$ assembles them into $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$. Part 3 combines Part 1 (with $k=-1$) and the tautological-bundle identification $L\cong\mathcal{O}(-1)$ to test the machine on the Hopf bundle.

**Key decision point.** The one genuinely non-obvious move is the direction of the exponent. A reader who is casual about the placement of the inverse in $(p,v)\cdot\lambda=(p\lambda,\varrho_k(\lambda^{-1})v)$ will produce sections of $P\times_{\varrho_{-k}}\mathbb{C}$ while believing they are working with $P\times_{\varrho_k}\mathbb{C}$, and will conclude that the coordinate functions $z_j$ are sections of $\mathcal{O}(-1)$ rather than of $\mathcal{O}(1)$. The decision that keeps everything straight is to *fix the representative convention once* — $[pg,v]=[p,\rho(g)v]$ — and to derive every homogeneity law and every isomorphism from it mechanically, never guessing a sign.

---

# Legal Operations Used

The numbering refers to the Legal Operations of the chapter topic page [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|Gauge Theory III]]; where that page is not yet assembled, each operation is named descriptively and the orchestrator will reconcile the numbers.

1. **Pass to the equivariant-function model of a section (operation: "trivialise a section along the principal bundle").** Replace a section $s\in\Gamma(P\times_\rho V)$ by the unique equivariant function $\hat s\colon P\to V$ with $s\circ\pi=[\,\cdot\,,\hat s(\cdot)]$, using [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]]. Applied here to convert "section of $P\times_{\varrho_k}\mathbb{C}$" into "$\lambda^{-k}$-homogeneous function on $P$".

2. **Specialise a representation identity to an associated-bundle identity (operation: "the associated-bundle construction is a monoidal functor").** Turn $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ into the line-bundle isomorphism $(P\times_{\varrho_k}\mathbb{C})\otimes(P\times_{\varrho_l}\mathbb{C})\cong P\times_{\varrho_{k+l}}\mathbb{C}$, and $\varrho_k^*\cong\varrho_{-k}$ into $(P\times_{\varrho_k}\mathbb{C})^*\cong P\times_{\varrho_{-k}}\mathbb{C}$, each verified from the representative convention.

3. **Check a bundle map is well defined on classes (operation: "descend a map through the diagonal action").** For every construction $[p,v]\mapsto(\text{something})$, verify that replacing $(p,v)$ by $(p\lambda,\lambda^{-k}v)$ leaves the value unchanged, so that the map descends to the quotient $P\times_{\varrho_k}\mathbb{C}$.

4. **Assemble by induction on the degree (operation: "generate the Picard subgroup from one generator").** Use the trivial base case $k=0$, the tensor step $L^{\otimes(k+1)}=L^{\otimes k}\otimes L$, and the dual step for negative $k$ to reach every integer power from the single generator $L$.

5. **Read off a section from an ambient global object (operation: "restrict a global tensor to a subbundle").** Exhibit the sections of $\mathcal{O}(1)=\mathcal{O}(-1)^*$ by restricting the constant-coefficient linear functionals $w_j$ on $\mathbb{C}^{n+1}$ to the tautological lines, and match them to the equivariant functions $z_j$.

---

# Hints

> [!note]- Hint 1
> Part 1 asks for nothing new: it is the sections theorem with a specific representation plugged in. Write out what $\rho(g^{-1})\hat s(p)$ becomes when $\rho=\varrho_k$ and $g=\lambda\in U(1)$. What is $\varrho_k(\lambda^{-1})$ as a number?

> [!note]- Hint 2
> For Part 2, do not try to build one clever isomorphism for all $k$ at once. The classification theorem hands you two facts about representations, $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ and $\varrho_k^*\cong\varrho_{-k}$. Each becomes an isomorphism of the corresponding associated bundles. Then $L^{\otimes k}$ is built from $L$ by repeated tensoring (and dualising for $k<0$), so an induction on $|k|$ finishes the job.

> [!note]- Hint 3
> To turn $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ into a bundle isomorphism, fix a point $p$ in the fibre and define $[p,v]_k\otimes[p,w]_l\mapsto[p,vw]_{k+l}$. The only thing to check is that this is independent of the choice of $p$: replace $p$ by $p\lambda$ and use the class relation $[p\lambda,u]_k=[p,\lambda^k u]_k$ (equivalently $[p,u]_k=[p\lambda,\lambda^{-k}u]_k$). The exponents $-k$ and $-l$ must add up to $-(k+l)$; watch them cancel.

> [!note]- Hint 4
> For Part 3, you already know from Part 1 (with $k=-1$) that a section of $P\times_{\varrho_{-1}}\mathbb{C}$ is a function $\hat s$ with $\hat s(z\lambda)=\lambda^{-(-1)}\hat s(z)=\lambda\,\hat s(z)$. Test the candidate $\hat s=z_j$: what is $z_j(z\lambda)$? A function that scales by $\lambda^{+1}$ is exactly a linear (degree-one homogeneous) function of $z$; that is the algebraic shadow of a section of $\mathcal{O}(1)$, the bundle of linear forms.

> [!note]- Hint 5
> To see the section $s_j$ *as a geometric object* on $\mathbb{CP}^n$, remember $\mathcal{O}(1)=\mathcal{O}(-1)^*$, so a value $s_j([z])$ is a linear functional on the tautological line $\mathbb{C}z\subset\mathbb{C}^{n+1}$. The $j$-th coordinate functional $w_j$ on $\mathbb{C}^{n+1}$ restricts to a functional on every line at once. Show that this restriction is exactly the section produced by $z_j$, and note where it vanishes.

---

# Solution

The argument is a straight run through the associated-bundle dictionary. Part 1 substitutes $\varrho_k$ into the sections theorem and reads the homogeneity law off the definition of the diagonal action. Part 2 converts the two representation identities of the classification theorem into two bundle isomorphisms — one for tensor products, one for duals — each proved by fixing a point in the fibre and checking independence of that choice, and then inducts on $|k|$. Part 3 specialises Part 1 to $k=-1$ on the Hopf bundle, checks that the ambient coordinate functions obey the resulting homogeneity law, and matches them to the restriction of the linear coordinate functionals to the tautological lines.

**Step 1: Specialise the sections theorem to $V=\mathbb{C}$, $\rho=\varrho_k$ (proves Part 1).**

A section of $P\times_{\varrho_k}\mathbb{C}$ corresponds under the sections theorem to an equivariant function $\hat s\colon P\to\mathbb{C}$, and the equivariance condition specialises exactly to the homogeneity law $\hat s(p\lambda)=\lambda^{-k}\hat s(p)$.

> [!note]- Derivation
> We invoke [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]] with structure group $G=U(1)$, representation space $V=\mathbb{C}$, and representation $\rho=\varrho_k$. The theorem provides a bijection
> $$C^\infty(P;\mathbb{C})^{U(1)}\longrightarrow\Gamma(P\times_{\varrho_k}\mathbb{C}),\qquad \hat s\mapsto s,\qquad s(\pi(p))=[p,\hat s(p)]_k,$$
> an isomorphism of $C^\infty(M)$-modules, where by definition
> $$C^\infty(P;\mathbb{C})^{U(1)}=\{\hat s\in C^\infty(P;\mathbb{C}):\hat s(p\lambda)=\varrho_k(\lambda^{-1})\,\hat s(p)\ \text{ for all }p\in P,\ \lambda\in U(1)\}\qquad\text{(definition of equivariant functions)}.$$
> Now $\varrho_k(\lambda^{-1})$ is, by the definition of $\varrho_k$, multiplication by $(\lambda^{-1})^k=\lambda^{-k}$ (since $\varrho_k(\mu)v=\mu^k v$). Substituting,
> $$\hat s(p\lambda)=\varrho_k(\lambda^{-1})\,\hat s(p)=\lambda^{-k}\,\hat s(p)\qquad\text{(definition of }\varrho_k\text{)}.$$
> Thus the equivariant functions are precisely the smooth $\hat s\colon P\to\mathbb{C}$ obeying the homogeneity law, and the sections theorem's bijection is the required natural bijection between them and $\Gamma(P\times_{\varrho_k}\mathbb{C})$. Because the correspondence is the module isomorphism of the sections theorem, addition of sections corresponds to addition of functions and multiplication by $f\in C^\infty(M)$ corresponds to multiplication by $f\circ\pi$; this last remark is not needed below but records that the bijection is structural, not merely set-theoretic.

**Step 2: The tensor step — $(P\times_{\varrho_k}\mathbb{C})\otimes(P\times_{\varrho_l}\mathbb{C})\cong P\times_{\varrho_{k+l}}\mathbb{C}$.**

Fixing a point of the fibre and sending $[p,v]_k\otimes[p,w]_l$ to $[p,vw]_{k+l}$ gives a well-defined isomorphism of line bundles, because the exponents $-k$ and $-l$ add to $-(k+l)$.

> [!note]- Derivation
> Fix $m\in M$ and a point $p\in P_m$. For a representation $\varrho_j$, the map $[p,\cdot]_j\colon\mathbb{C}\to(P\times_{\varrho_j}\mathbb{C})_m$, $v\mapsto[p,v]_j$, is a linear isomorphism (this is the recalled property of the associated bundle: for fixed $p$ the map is linear, and it is bijective by freeness and transitivity of the fibre action). Consequently the fibre of the tensor product bundle over $m$ has the basis $[p,1]_k\otimes[p,1]_l$, and the bilinear map
> $$B_p\colon\mathbb{C}\times\mathbb{C}\to(P\times_{\varrho_{k+l}}\mathbb{C})_m,\qquad B_p(v,w)=[p,vw]_{k+l}$$
> induces a unique linear map $(P\times_{\varrho_k}\mathbb{C})_m\otimes(P\times_{\varrho_l}\mathbb{C})_m\to(P\times_{\varrho_{k+l}}\mathbb{C})_m$ sending $[p,v]_k\otimes[p,w]_l\mapsto[p,vw]_{k+l}$ (by the universal property of the tensor product, using that $B_p$ is bilinear over $\mathbb{C}$). Call this map $\Theta_p$.
>
> **Independence of the chosen $p$.** We must check that $\Theta_p=\Theta_{p\lambda}$ for every $\lambda\in U(1)$, so that the fibrewise maps glue into a bundle map. From the class relation $[p\lambda,u]_j=[p,\lambda^j u]_j$ (which is $[pg,u]=[p,\varrho_j(g)u]$ with $g=\lambda$), equivalently $[p,u]_j=[p\lambda,\lambda^{-j}u]_j$, we express a fixed pair of vectors in the two representatives:
> $$[p,v]_k=[p\lambda,\lambda^{-k}v]_k,\qquad [p,w]_l=[p\lambda,\lambda^{-l}w]_l\qquad\text{(class relation for }\varrho_k,\varrho_l\text{)}.$$
> Applying $\Theta_{p\lambda}$ to the right-hand representatives and applying $\Theta_p$ to the left-hand ones,
> $$\Theta_{p\lambda}\big([p\lambda,\lambda^{-k}v]_k\otimes[p\lambda,\lambda^{-l}w]_l\big)=[p\lambda,(\lambda^{-k}v)(\lambda^{-l}w)]_{k+l}=[p\lambda,\lambda^{-(k+l)}vw]_{k+l}\qquad\text{(definition of }\Theta_{p\lambda}\text{)},$$
> $$[p\lambda,\lambda^{-(k+l)}vw]_{k+l}=[p,vw]_{k+l}=\Theta_p\big([p,v]_k\otimes[p,w]_l\big)\qquad\text{(class relation for }\varrho_{k+l}\text{, then definition of }\Theta_p\text{)}.$$
> Since $[p,v]_k\otimes[p,w]_l$ and $[p\lambda,\lambda^{-k}v]_k\otimes[p\lambda,\lambda^{-l}w]_l$ are the *same* element of the fibre, the two maps agree on it, hence on all of the (one-dimensional-over-$\mathbb{C}$, so single-basis-vector-spanned) fibre. Therefore $\Theta:=\Theta_p$ is independent of $p$ and defines a bundle map $\Theta\colon(P\times_{\varrho_k}\mathbb{C})\otimes(P\times_{\varrho_l}\mathbb{C})\to P\times_{\varrho_{k+l}}\mathbb{C}$.
>
> **Isomorphism and smoothness.** On each fibre $\Theta$ carries the basis vector $[p,1]_k\otimes[p,1]_l$ to the basis vector $[p,1]_{k+l}$, so it is a linear isomorphism fibrewise. For smoothness, choose a smooth local section $s\colon U\to P$ of the principal bundle (these exist by local triviality); then $m\mapsto[s(m),1]_j$ is a smooth nowhere-zero local frame of $P\times_{\varrho_j}\mathbb{C}$ over $U$, and in these frames $\Theta$ is the constant map $[s,1]_k\otimes[s,1]_l\mapsto[s,1]_{k+l}$, which is smooth. A fibrewise-linear bundle map that is a smooth isomorphism on every trivialising chart is a bundle isomorphism. This proves the tensor step. (Representation-theoretically, $\Theta$ is nothing but the associated-bundle image of the canonical isomorphism $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ of [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]], realised by $\mathbb{C}\otimes\mathbb{C}\cong\mathbb{C}$, $v\otimes w\mapsto vw$.)

**Step 3: The dual step — $(P\times_{\varrho_k}\mathbb{C})^*\cong P\times_{\varrho_{-k}}\mathbb{C}$.**

A class $[p,\alpha]_{-k}$ names the linear functional $[p,v]_k\mapsto\alpha v$ on the fibre of $P\times_{\varrho_k}\mathbb{C}$, and this is independent of the representative $p$; the assignment is a bundle isomorphism onto the dual.

> [!note]- Derivation
> Fix $m\in M$. Define, for $p\in P_m$ and $\alpha\in\mathbb{C}$, the linear functional
> $$\phi_p(\alpha)\in(P\times_{\varrho_k}\mathbb{C})_m^*,\qquad \phi_p(\alpha)\big([p,v]_k\big):=\alpha v\qquad(v\in\mathbb{C}).$$
> This is well posed because every element of $(P\times_{\varrho_k}\mathbb{C})_m$ is uniquely $[p,v]_k$ for the fixed $p$ (the map $[p,\cdot]_k$ is a linear isomorphism), and $v\mapsto\alpha v$ is linear.
>
> **Independence of the chosen $p$.** For the assignment $[p,\alpha]_{-k}\mapsto\phi_p(\alpha)$ to descend to the quotient $P\times_{\varrho_{-k}}\mathbb{C}$, we must check it takes the same value on the two representatives of one class. By the class relation for $\varrho_{-k}$, namely $[p,\alpha]_{-k}=[p\lambda,\lambda^{-(-k)}\alpha]_{-k}=[p\lambda,\lambda^{k}\alpha]_{-k}$, consistency requires $\phi_{p\lambda}(\lambda^{k}\alpha)=\phi_p(\alpha)$. Evaluate the left side on an arbitrary element, written in the representative $p\lambda$ as $[p\lambda,u]_k$:
> $$\phi_{p\lambda}(\lambda^{k}\alpha)\big([p\lambda,u]_k\big)=(\lambda^{k}\alpha)\,u\qquad\text{(definition of }\phi_{p\lambda}\text{)}.$$
> The same element in the representative $p$ is $[p\lambda,u]_k=[p,\lambda^{k}u]_k$ (class relation for $\varrho_k$: $[pg,u]=[p,\varrho_k(g)u]=[p,\lambda^{k}u]$), so
> $$\phi_p(\alpha)\big([p\lambda,u]_k\big)=\phi_p(\alpha)\big([p,\lambda^{k}u]_k\big)=\alpha\,(\lambda^{k}u)=\lambda^{k}\alpha u\qquad\text{(class relation, then definition of }\phi_p\text{)}.$$
> The two values agree for every $u$, so $\phi_{p\lambda}(\lambda^{k}\alpha)=\phi_p(\alpha)$, and the map $\Xi\colon P\times_{\varrho_{-k}}\mathbb{C}\to(P\times_{\varrho_k}\mathbb{C})^*$, $[p,\alpha]_{-k}\mapsto\phi_p(\alpha)$, is well defined.
>
> **Isomorphism and smoothness.** Fibrewise $\Xi$ is linear in $\alpha$ and injective (if $\phi_p(\alpha)=0$ then $\alpha v=0$ for all $v$, so $\alpha=0$); both fibres are one-dimensional over $\mathbb{C}$, so $\Xi$ is a fibrewise linear isomorphism. In the local frames coming from a local section $s\colon U\to P$ — namely $[s,1]_{-k}$ of $P\times_{\varrho_{-k}}\mathbb{C}$ and the dual coframe of $[s,1]_k$ — the map $\Xi$ sends $[s,1]_{-k}$ to the functional $[s,1]_k\mapsto 1$, which is exactly that dual coframe; so $\Xi$ is the identity in these frames and hence smooth. Therefore $\Xi$ is a bundle isomorphism $P\times_{\varrho_{-k}}\mathbb{C}\cong(P\times_{\varrho_k}\mathbb{C})^*$, equivalently $(P\times_{\varrho_k}\mathbb{C})^*\cong P\times_{\varrho_{-k}}\mathbb{C}$. (This is the associated-bundle image of $\varrho_k^*\cong\varrho_{-k}$ from [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]].)

**Step 4: Induction on $|k|$ (completes Part 2).**

The base case $k=0$ is the trivial bundle; the tensor step raises $k$ by one; the dual step reaches negative $k$. Together they give $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ for every $k\in\mathbb{Z}$.

> [!note]- Derivation
> **Base case $k=0$.** The representation $\varrho_0$ is trivial, $\varrho_0(\lambda)=1$, so the diagonal action on $P\times\mathbb{C}$ is $(p,v)\cdot\lambda=(p\lambda,v)$, and $[p,v]_0\mapsto(\pi(p),v)$ is a well-defined isomorphism $P\times_{\varrho_0}\mathbb{C}\cong M\times\mathbb{C}=\underline{\mathbb{C}}=L^{\otimes 0}$: it is well defined because the value $(\pi(p),v)$ is unchanged when $(p,v)$ is replaced by $(p\lambda,v)$, it is fibrewise linear and bijective, and it is smooth in a local section frame. This settles $k=0$.
>
> **Case $k=1$.** By definition $L=P\times_{\varrho_1}\mathbb{C}$ and $L^{\otimes 1}=L$, so the identity is the required isomorphism.
>
> **Induction for $k\ge 1$.** Assume $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$. By the tensor step (Step 2 with $l=1$),
> $$P\times_{\varrho_{k+1}}\mathbb{C}\cong(P\times_{\varrho_k}\mathbb{C})\otimes(P\times_{\varrho_1}\mathbb{C})\cong L^{\otimes k}\otimes L=L^{\otimes(k+1)}\qquad\text{(Step 2, then the inductive hypothesis and }L=P\times_{\varrho_1}\mathbb{C}\text{)}.$$
> By induction, $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ for all $k\ge 0$.
>
> **Negative $k$.** For $k<0$ write $k=-m$ with $m>0$. By the dual step (Step 3) and the case $m\ge 0$ just proved,
> $$P\times_{\varrho_{-m}}\mathbb{C}\cong(P\times_{\varrho_m}\mathbb{C})^*\cong(L^{\otimes m})^*=(L^*)^{\otimes m}=L^{\otimes(-m)}\qquad\text{(Step 3 with }k=m\text{, then the case }m\ge0\text{, then the definition of negative tensor powers)}.$$
> Here $(L^{\otimes m})^*=(L^*)^{\otimes m}$ is the standard identification of the dual of a tensor power with the tensor power of the dual for line bundles, and $L^{\otimes(-m)}:=(L^*)^{\otimes m}$ is the definition given in the problem. Hence $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ for every $k\in\mathbb{Z}$, proving Part 2.

**Step 5: The Hopf bundle and the coordinate functions (proves Part 3).**

On the Hopf bundle $L\cong\mathcal{O}(-1)$, so $P\times_{\varrho_{-1}}\mathbb{C}\cong\mathcal{O}(1)$; the coordinate function $z_j$ satisfies $z_j(z\lambda)=\lambda\,z_j(z)$, hence defines a section $s_j$ of $\mathcal{O}(1)$; concretely $s_j$ is the restriction of the linear functional $w_j$ to the tautological lines, and $s_0,\dots,s_n$ have no common zero.

> [!note]- Derivation
> **The bundle is $\mathcal{O}(1)$.** By [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the companion exercise]], the map $L=S^{2n+1}\times_{\varrho_1}\mathbb{C}\to\mathcal{O}(-1)$, $[z,v]_1\mapsto([z],vz)$, is an isomorphism of complex line bundles; it is well defined because $[z\lambda,\lambda^{-1}v]_1\mapsto([z\lambda],\lambda^{-1}v\cdot z\lambda)=([z],vz)$, and it is a fibrewise isomorphism onto the tautological line $\mathbb{C}z$. Hence $L\cong\mathcal{O}(-1)$, and by Part 2 with $k=-1$,
> $$P\times_{\varrho_{-1}}\mathbb{C}\cong L^{\otimes(-1)}=L^*\cong\mathcal{O}(-1)^*=\mathcal{O}(1)\qquad\text{(Part 2, then }L\cong\mathcal{O}(-1)\text{, then the definition }\mathcal{O}(1):=\mathcal{O}(-1)^*\text{)}.$$
>
> **The coordinate functions are homogeneous of the right degree.** By Part 1 with $k=-1$, a section of $P\times_{\varrho_{-1}}\mathbb{C}\cong\mathcal{O}(1)$ is a smooth $\hat s\colon S^{2n+1}\to\mathbb{C}$ with
> $$\hat s(z\lambda)=\lambda^{-(-1)}\hat s(z)=\lambda\,\hat s(z)\qquad\text{(Part 1, }k=-1\text{)}.$$
> Take $\hat s=z_j$, the restriction to $S^{2n+1}$ of the $j$-th coordinate $w_j\colon\mathbb{C}^{n+1}\to\mathbb{C}$; it is smooth (a restriction of a $\mathbb{C}$-linear, hence smooth, map). Then
> $$z_j(z\lambda)=(z\lambda)_j=z_j\lambda=\lambda\,z_j=\lambda\,z_j(z)\qquad\text{(the Hopf action is }z\cdot\lambda=z\lambda\text{, componentwise multiplication)}.$$
> This is exactly the homogeneity law for $k=-1$, so $z_j\in C^\infty(S^{2n+1};\mathbb{C})^{U(1)}$ and defines, by Part 1, a global smooth section $s_j\in\Gamma(\mathcal{O}(1))$, characterised by $s_j(\pi(z))=[z,z_j]_{-1}$.
>
> **Concrete identification with the restricted functional.** We show $s_j([z])$ is the linear functional $w_j|_{\mathbb{C}z}$ on the tautological line $\mathcal{O}(-1)_{[z]}=\mathbb{C}z$. Under the isomorphism $\Xi$ of Step 3 (with $k=1$, so $P\times_{\varrho_{-1}}\mathbb{C}\cong(P\times_{\varrho_1}\mathbb{C})^*=L^*$) and the isomorphism $L\cong\mathcal{O}(-1)$, the class $[z,z_j]_{-1}$ becomes the functional on $\mathcal{O}(-1)_{[z]}$ that acts on $[z,v]_1\leftrightarrow([z],vz)$ by
> $$s_j([z])\big([z,v]_1\big)=\Xi([z,z_j]_{-1})\big([z,v]_1\big)=z_j\,v\qquad\text{(definition of }\Xi\text{ in Step 3)}.$$
> Now the vector $\ell:=vz\in\mathbb{C}z=\mathcal{O}(-1)_{[z]}$ has $j$-th coordinate $\ell_j=vz_j=z_j v$, so
> $$s_j([z])(\ell)=z_j v=\ell_j=w_j(\ell)\qquad(\ell=vz\in\mathbb{C}z).$$
> Thus $s_j([z])$ is precisely the restriction to the line $\mathbb{C}z$ of the ambient coordinate functional $w_j$. Since $w_j$ is a single global linear functional on $\mathbb{C}^{n+1}$, restricting it to every tautological line at once gives a global section of $\mathcal{O}(-1)^*=\mathcal{O}(1)$, independently confirming that $s_j$ is a well-defined smooth section.
>
> **No common zero.** Suppose $s_j([z])=0$ for all $j$. By the identification, $s_j([z])$ vanishes as a functional iff $\ell_j=vz_j=0$ for all $v$, iff $z_j=0$. So $s_0([z])=\cdots=s_n([z])=0$ would force $z_0=\cdots=z_n=0$, contradicting $z\in S^{2n+1}$ (which requires $\sum|z_i|^2=1$, so not all $z_i$ vanish). Hence the sections $s_0,\dots,s_n$ have no common zero on $\mathbb{CP}^n$. This is the statement that $\mathcal{O}(1)$ is globally generated (base-point free): the $n+1$ coordinate sections trivialise it away from each coordinate hyperplane $\{z_j=0\}$.

> [!note]- Complete formal solution
> Let $\pi\colon P\to M$ be a principal $U(1)$-bundle, $\varrho_k(\lambda)v=\lambda^k v$, and $P\times_{\varrho_k}\mathbb{C}=(P\times\mathbb{C})/U(1)$ with $(p,v)\cdot\lambda=(p\lambda,\lambda^{-k}v)$ and classes $[p,v]_k$; recall $[pg,v]_k=[p,\varrho_k(g)v]_k$, i.e. $[p\lambda,u]_k=[p,\lambda^k u]_k$. Write $L=P\times_{\varrho_1}\mathbb{C}$.
>
> **Part 1.** Apply [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]] with $V=\mathbb{C}$, $\rho=\varrho_k$: sections $s\in\Gamma(P\times_{\varrho_k}\mathbb{C})$ correspond bijectively (as $C^\infty(M)$-modules) to $\hat s\in C^\infty(P;\mathbb{C})$ with $\hat s(p\lambda)=\varrho_k(\lambda^{-1})\hat s(p)$, via $s(\pi(p))=[p,\hat s(p)]_k$. Since $\varrho_k(\lambda^{-1})=\lambda^{-k}$, the equivariance condition is $\hat s(p\lambda)=\lambda^{-k}\hat s(p)$, as claimed.
>
> **Part 2.** *Tensor step.* Fix $p\in P_m$; the map $[p,\cdot]_j\colon\mathbb{C}\to(P\times_{\varrho_j}\mathbb{C})_m$ is a linear isomorphism. Define $\Theta([p,v]_k\otimes[p,w]_l)=[p,vw]_{k+l}$. It is well defined independently of $p$: with $[p,v]_k=[p\lambda,\lambda^{-k}v]_k$ and $[p,w]_l=[p\lambda,\lambda^{-l}w]_l$, one has $[p\lambda,(\lambda^{-k}v)(\lambda^{-l}w)]_{k+l}=[p\lambda,\lambda^{-(k+l)}vw]_{k+l}=[p,vw]_{k+l}$. It carries a basis vector to a basis vector, so it is a fibrewise isomorphism, and it is the identity in local frames from a local section, hence a smooth bundle isomorphism $(P\times_{\varrho_k}\mathbb{C})\otimes(P\times_{\varrho_l}\mathbb{C})\cong P\times_{\varrho_{k+l}}\mathbb{C}$.
>
> *Dual step.* Define $\Xi([p,\alpha]_{-k})=\phi_p(\alpha)$ where $\phi_p(\alpha)([p,v]_k)=\alpha v$. Independence of $p$: writing $[p,\alpha]_{-k}=[p\lambda,\lambda^{k}\alpha]_{-k}$, we check $\phi_{p\lambda}(\lambda^{k}\alpha)=\phi_p(\alpha)$: on $[p\lambda,u]_k=[p,\lambda^{k}u]_k$, the left side gives $\lambda^{k}\alpha u$ and the right side gives $\alpha\lambda^{k}u$, equal. $\Xi$ is a fibrewise isomorphism (injective, equal dimensions) and the identity in dual local frames, hence a bundle isomorphism $(P\times_{\varrho_k}\mathbb{C})^*\cong P\times_{\varrho_{-k}}\mathbb{C}$.
>
> *Induction.* For $k=0$, $\varrho_0$ trivial gives $P\times_{\varrho_0}\mathbb{C}\cong\underline{\mathbb{C}}=L^{\otimes 0}$; for $k=1$, $P\times_{\varrho_1}\mathbb{C}=L$. If $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ then the tensor step gives $P\times_{\varrho_{k+1}}\mathbb{C}\cong L^{\otimes k}\otimes L=L^{\otimes(k+1)}$, so the claim holds for all $k\ge 0$. For $k=-m<0$, the dual step and the non-negative case give $P\times_{\varrho_{-m}}\mathbb{C}\cong(P\times_{\varrho_m}\mathbb{C})^*\cong(L^{\otimes m})^*=(L^*)^{\otimes m}=L^{\otimes(-m)}$. Hence $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ for all $k\in\mathbb{Z}$.
>
> **Part 3.** For the Hopf bundle $S^{2n+1}\to\mathbb{CP}^n$ with $z\cdot\lambda=z\lambda$, the map $[z,v]_1\mapsto([z],vz)$ is an isomorphism $L\cong\mathcal{O}(-1)$ (well defined since $[z\lambda,\lambda^{-1}v]_1\mapsto([z],vz)$). By Part 2 with $k=-1$, $P\times_{\varrho_{-1}}\mathbb{C}\cong L^*\cong\mathcal{O}(-1)^*=\mathcal{O}(1)$. By Part 1 with $k=-1$, a section corresponds to $\hat s$ with $\hat s(z\lambda)=\lambda\,\hat s(z)$. The coordinate function $z_j$ satisfies $z_j(z\lambda)=z_j\lambda=\lambda z_j(z)$, so it defines a section $s_j\in\Gamma(\mathcal{O}(1))$ with $s_j(\pi(z))=[z,z_j]_{-1}$. Under $\Xi$ and $L\cong\mathcal{O}(-1)$, $s_j([z])$ acts on $\ell=vz\in\mathbb{C}z$ by $s_j([z])(\ell)=z_j v=\ell_j=w_j(\ell)$, so $s_j$ is the restriction of the linear functional $w_j$ to the tautological lines. Finally, $s_j([z])=0$ for all $j$ iff $z_j=0$ for all $j$, impossible for $z\in S^{2n+1}$; hence $s_0,\dots,s_n$ have no common zero. $\blacksquare$

> [!warning] Illegal but tempting: reading the exponent off the action without the inverse
> It is tempting to declare that a section of $P\times_{\varrho_k}\mathbb{C}$ "is a function transforming by $\lambda^{k}$", by looking at $\varrho_k(\lambda)=\lambda^k$ directly. This is wrong: the equivariance law in the sections theorem is $\hat s(pg)=\rho(g^{-1})\hat s(p)$, with the *inverse*, so the exponent that appears is $-k$, not $+k$. The inverse is forced by the very definition of the associated bundle, whose diagonal action is $(p,v)\cdot g=(pg,\rho(g^{-1})v)$ — chosen precisely so that $[p,v]\mapsto\pi(p)$ is invariant. Dropping the inverse would identify the coordinate functions $z_j$ (which scale by $\lambda^{+1}$) with sections of $P\times_{\varrho_{+1}}\mathbb{C}\cong\mathcal{O}(-1)$, the wrong bundle; the tautological bundle $\mathcal{O}(-1)$ has *no* nonzero global sections (its sections would be homogeneous of degree $-1$, i.e. $\hat s(z\lambda)=\lambda^{-1}\hat s(z)$, and no such nonzero smooth function of $z$ that is also the restriction of an entire function exists on the sphere for degree reasons), whereas $\mathcal{O}(1)$ has the $n+1$ coordinate sections. The sign is the whole content of the bookkeeping.

> [!note]- Independent sanity check: degrees via the first Chern number
> The identification $P\times_{\varrho_k}\mathbb{C}\cong L^{\otimes k}$ is consistent with the additivity of the first Chern class under tensor product, $c_1(A\otimes B)=c_1(A)+c_1(B)$ for line bundles. On the Hopf bundle over $\mathbb{CP}^1$, the series convention fixes $\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=-1$, hence $\deg\mathcal{O}(-1)=-1$ and $\deg\mathcal{O}(1)=+1$. Then $\deg(P\times_{\varrho_k}\mathbb{C})=\deg L^{\otimes k}=k\deg L=k\deg\mathcal{O}(-1)=-k$, so $P\times_{\varrho_{-1}}\mathbb{C}$ has degree $+1$, matching $\mathcal{O}(1)$. A line bundle of positive degree over $\mathbb{CP}^1$ has nonzero holomorphic sections (indeed $\dim H^0(\mathbb{CP}^1,\mathcal{O}(1))=2$, spanned by $z_0,z_1$), while $\mathcal{O}(-1)$ of negative degree has none — exactly the asymmetry the previous callout exploits. The count $n+1$ of coordinate sections of $\mathcal{O}(1)$ over $\mathbb{CP}^n$ matches $\dim H^0(\mathbb{CP}^n,\mathcal{O}(1))=n+1$, the space of linear forms.

---

# Key Takeaways

**Sections of an associated line bundle are homogeneous functions on the total space, with the degree carrying an inescapable minus sign.** The reusable principle is the whole of Part 1: whenever a line bundle is presented as $P\times_{\varrho_k}\mathbb{C}$ for a circle bundle $P$, its sections are exactly the functions $\hat s\colon P\to\mathbb{C}$ with $\hat s(p\lambda)=\lambda^{-k}\hat s(p)$, and this comes for free from [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections theorem]] the instant one substitutes $\varrho_k(\lambda^{-1})=\lambda^{-k}$. The trigger condition is a section problem for a bundle written in associated form; the reaction is to pass to the equivariant-function model, where a geometric object over $M$ becomes an ordinary scalar function on $P$ with a transformation law. The transferable diagnostic is the sign: the inverse in $\rho(g^{-1})$ is not optional decoration but the reason $[p,v]\mapsto\pi(p)$ is well defined, so the degree of homogeneity is always $-k$, never $+k$; getting this backwards silently swaps $\mathcal{O}(1)$ for $\mathcal{O}(-1)$ and every later computation inherits the error. This is the single most common mistake in the associated-bundle formalism and the one worth over-learning.

**The associated-bundle construction is a monoidal functor: it turns tensor products and duals of representations into tensor products and duals of bundles.** The heart of Part 2 is that $k\mapsto P\times_{\varrho_k}\mathbb{C}$ is a homomorphism from the group $(\mathbb{Z},+)$ of $U(1)$-characters to the Picard group of line bundles under $\otimes$, because $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$ and $\varrho_k^*\cong\varrho_{-k}$ from [[Thm - Complex Representations of U(1) and SU(2)|the classification of $U(1)$-representations]] promote directly to bundle isomorphisms. The recurring technique for proving such an isomorphism is the "fix a point in the fibre, then check independence of the choice" argument of Steps 2 and 3: define the candidate map using a chosen $p\in P_m$, then verify that replacing $p$ by $p\lambda$ and using the class relation $[p\lambda,u]_j=[p,\lambda^j u]_j$ leaves the value unchanged — the exponents must balance, and watching them balance ($-k$ and $-l$ summing to $-(k+l)$, or $-k$ meeting $+k$) is both the proof and the sanity check. This pattern recurs for every functor of representations: direct sums give Whitney sums, symmetric and exterior powers give the corresponding bundle operations, and the adjoint representation gives $\operatorname{ad}P$. Once one has the generator $L$ and these two moves, every tensor power is reached by an induction that is pure bookkeeping.

**A line bundle over projective space is best understood through its sections as homogeneous polynomials, and the tautological bundle sets the sign of everything.** Part 3 is the concrete anchor: on the Hopf bundle the generator $L$ is the tautological bundle $\mathcal{O}(-1)$, whose fibre over $[z]$ is the line $\mathbb{C}z$ itself, so $\mathcal{O}(1)=\mathcal{O}(-1)^*$ has sections that are linear functionals on those lines — and the $n+1$ ambient coordinate functionals $w_0,\dots,w_n$, restricted to the tautological lines, are exactly the sections corresponding to the homogeneous-degree-one functions $z_0,\dots,z_n$ on $S^{2n+1}$. The transferable lesson is the dictionary "sections of $\mathcal{O}(d)$ over $\mathbb{CP}^n$ $=$ degree-$d$ homogeneous functions on $\mathbb{C}^{n+1}$ (holomorphically, degree-$d$ homogeneous polynomials)", with $d>0$ giving many sections, $d=0$ giving the constants, and $d<0$ giving none — the base-point-freeness of $\mathcal{O}(1)$ (its coordinate sections have no common zero) is what lets $\mathbb{CP}^n$ embed in projective space by its own coordinates. Whenever a computation over projective space needs a nowhere-vanishing local frame or a global section, this is where to reach: pick the coordinate patch $\{z_j\ne 0\}$, where $s_j$ trivialises $\mathcal{O}(1)$, and grind the rest in an affine chart. Companion exercises: [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]] for the identification $L\cong\mathcal{O}(-1)$ used here, and [[Ex - Line Bundles of Every Degree on a Closed Oriented Surface]] for the way tensor powers realise every degree.
