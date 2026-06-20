---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Projective Model Structure on Chain Complexes"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

In $\mathbf{Ch}(R)$, let $S^n$ be the sphere complex ($R$ in degree $n$, zero differential) and $D^n$ the disk complex ($R \xrightarrow{1} R$ in degrees $n, n-1$). 

**(a)** Establish the natural isomorphisms
$$\mathbf{Ch}(R)(S^n, C) \cong Z_n(C) \quad (\text{the } n\text{-cycles}), \qquad \mathbf{Ch}(R)(D^n, C) \cong C_n \quad (\text{the degree-}n\text{ chains}).$$

**(b)** Using (a), show that a chain map $p : E \to B$ has the right lifting property against the set $\{0 \hookrightarrow D^n : n \in \mathbb{Z}\}$ if and only if $p$ is **surjective in every degree** (a fibration), and against $\{S^{n-1} \hookrightarrow D^n : n \in \mathbb{Z}\}$ if and only if $p$ is a **degreewise-surjective quasi-isomorphism** (a trivial fibration).

**Recall:**

A [[Def - Chain Map and Chain Homotopy|chain map]] $f : C \to D$ is a family $f_n : C_n \to D_n$ with $d^D f_n = f_{n-1} d^C$. The $n$-cycles are $Z_n(C) = \ker d_n$.

In a [[Def - Model Category|model category]], $i$ has the **left lifting property** against $p$ (and $p$ the **right lifting property** against $i$) if every commuting square with $i$ on the left, $p$ on the right has a diagonal filler. In the [[Def - Projective Model Structure on Chain Complexes|projective model structure]] the fibrations are the degreewise surjections and the trivial fibrations the degreewise-surjective quasi-isomorphisms.

---

# Convergent Strategy

**Problem class:** This is a "lifting against generators" problem — the central computational move of cofibrantly generated model categories, and the technique behind verifying [[Thm - Chain Complexes of Modules Form a Model Category|the model-category axioms on Ch(R)]]. The routine is to translate an abstract lifting square into a concrete algebraic statement using a representability isomorphism, then read off the condition on $p$.

**Assumption pattern:** The recognisable structure is "right lifting property against a *set* of generators". The assumptions present are the specific shapes of the generators $0 \hookrightarrow D^n$ and $S^{n-1}\hookrightarrow D^n$; what they unlock is, via part (a), a description of maps *out of* the generators as cycles and chains, converting the lifting square into a surjectivity question.

**Theorem routing:** Part (a) is proved directly from the definition of chain map (a map is determined by where it sends generators, constrained by commuting with $d$). Part (b) routes the lifting square through (a): a lift against $0 \hookrightarrow D^n$ is the data of a preimage of an arbitrary chain, and a lift against $S^{n-1}\hookrightarrow D^n$ adds the cycle-filling condition that forces the quasi-isomorphism. These are exactly Lemmas 1–3 of [[Thm - Chain Complexes of Modules Form a Model Category]].

**Key decision point:** The non-obvious choice is recognising that $D^n$ *represents the degree-$n$ chains functor* and $S^n$ *represents the cycles functor* — this representability is what makes the generators tractable. A reader who tries to attack the lifting square without first computing maps out of the generators will drown in diagram chasing; the decision to compute $\mathbf{Ch}(R)(D^n, -)$ and $\mathbf{Ch}(R)(S^n, -)$ first is what makes the rest mechanical.

---

# Legal Operations Used

1. **Operation 2 from the topic page (probe a complex with the sphere and disk complexes).** Part (a) is precisely this operation: computing $\mathbf{Ch}(R)(S^n, C)$ and $\mathbf{Ch}(R)(D^n, C)$ to extract cycles and chains.

2. **Operation 1 from the topic page (check a chain-complex condition one degree at a time).** Part (b) reduces the lifting condition to degreewise surjectivity, a module-level statement checked one degree at a time.

---

# Hints

> [!note]- Hint 1
> A chain map out of $D^n$ is determined by the image of the degree-$n$ generator $1 \in R = (D^n)_n$. What constraint does commuting with the differential put on the degree-$(n-1)$ component?

> [!note]- Hint 2
> A chain map out of $S^n$ is determined by the image of $1 \in R = (S^n)_n$, but now the differential of $S^n$ is zero, so the image must be a *cycle*. Why?

> [!note]- Hint 3
> For (b), a lifting square for $0 \hookrightarrow D^n$ against $p$ has trivial top map; the bottom is (by (a)) an element of $B_n$, and a lift is an element of $E_n$ mapping to it. That is exactly a preimage. Now do $S^{n-1}\hookrightarrow D^n$, where the top map is (by (a)) a cycle in $E_{n-1}$.

---

# Solution

The whole solution is the representability of (a) feeding into (b). Once maps out of $D^n$ and $S^n$ are identified with chains and cycles, a lifting square becomes a system of module equations whose solvability is degreewise surjectivity (for $J$) or surjectivity plus acyclicity of the kernel (for $I$).

**Step 1: $\mathbf{Ch}(R)(D^n, C) \cong C_n$ and $\mathbf{Ch}(R)(S^n, C) \cong Z_n(C)$.**

> [!note]- Derivation
> $D^n$ is $\cdots \to 0 \to R \xrightarrow{1} R \to 0 \to \cdots$ with the two $R$'s in degrees $n$ and $n-1$. A chain map $\varphi : D^n \to C$ consists of $\varphi_n : R \to C_n$ and $\varphi_{n-1} : R \to C_{n-1}$ (all other components zero) with the commuting condition $d^C_n \circ \varphi_n = \varphi_{n-1} \circ d^{D^n}_n = \varphi_{n-1} \circ 1 = \varphi_{n-1}$. So $\varphi_{n-1}$ is *forced* to equal $d^C_n \varphi_n$, and $\varphi$ is determined by $\varphi_n$, which is determined by $\varphi_n(1) \in C_n$, an arbitrary element. Therefore $\varphi \mapsto \varphi_n(1)$ is a bijection $\mathbf{Ch}(R)(D^n, C) \cong C_n$, natural in $C$.
>
> $S^n$ is $R$ in degree $n$ with zero differential. A chain map $\psi : S^n \to C$ is $\psi_n : R \to C_n$ with the commuting condition $d^C_n \circ \psi_n = \psi_{n-1} \circ d^{S^n}_n = \psi_{n-1} \circ 0 = 0$, so $d^C_n(\psi_n(1)) = 0$, i.e. $\psi_n(1) \in \ker d^C_n = Z_n(C)$, otherwise arbitrary. Therefore $\psi \mapsto \psi_n(1)$ is a bijection $\mathbf{Ch}(R)(S^n, C) \cong Z_n(C)$, natural in $C$.

**Step 2: RLP against $\{0 \hookrightarrow D^n\}$ $\iff$ degreewise surjective.**

> [!note]- Derivation
> A commuting square with $0 \hookrightarrow D^n$ on the left and $p : E \to B$ on the right consists of: a chain map $0 \to E$ (necessarily trivial) and a chain map $D^n \to B$, which by Step 1 is an element $b \in B_n$. A diagonal filler is a chain map $D^n \to E$, i.e. (by Step 1) an element $e \in E_n$, such that $p \circ e = b$ in degree $n$, that is $p_n(e) = b$. Such $e$ exists for *every* $b \in B_n$ precisely when $p_n$ is surjective. Ranging over all $n$, the RLP against $\{0 \hookrightarrow D^n\}$ holds if and only if $p_n$ is surjective for all $n$ — i.e. $p$ is a fibration.

**Step 3: RLP against $\{S^{n-1}\hookrightarrow D^n\}$ $\iff$ degreewise-surjective quasi-isomorphism.**

> [!note]- Derivation
> A commuting square with $S^{n-1}\hookrightarrow D^n$ on the left and $p$ on the right consists of: a chain map $S^{n-1} \to E$, which by Step 1 is a cycle $z \in Z_{n-1}(E)$, and a chain map $D^n \to B$, which by Step 1 is an element $b \in B_n$; commutativity forces $p_{n-1}(z) = d^B_n(b)$ (the image of $z$ in $B$ must be the boundary of $b$). A diagonal filler $D^n \to E$ is an element $e \in E_n$ with $d^E_n(e) = z$ and $p_n(e) = b$.
>
> So the RLP says: for every $z \in Z_{n-1}(E)$ and $b \in B_n$ with $p(z) = d(b)$, there is $e \in E_n$ with $de = z$ and $p(e) = b$. Taking $z = 0$, $b$ arbitrary in $B_n$ recovers surjectivity of $p_n$ (the filler $e$ is a cycle, but ranging $n$ this gives surjectivity in every degree). The full condition additionally forces: whenever a cycle of $E$ becomes a boundary downstairs, it is already a boundary upstairs compatibly — which is exactly the statement that the kernel $K = \ker p$ is acyclic. By the long exact homology sequence of $0 \to K \to E \xrightarrow{p} B \to 0$ (valid since $p$ is surjective), $K$ acyclic $\iff$ $H_*(p)$ an isomorphism $\iff$ $p$ a quasi-isomorphism. Hence the RLP against $\{S^{n-1}\hookrightarrow D^n\}$ holds if and only if $p$ is a degreewise-surjective quasi-isomorphism — a trivial fibration.

> [!note]- Complete formal solution
> **(a)** A chain map out of $D^n = (R \xrightarrow{1} R)$ in degrees $n, n-1$ is determined by $\varphi_n(1) \in C_n$, since commuting with $d$ forces $\varphi_{n-1} = d^C_n \varphi_n$; the assignment $\varphi \mapsto \varphi_n(1)$ is a natural bijection $\mathbf{Ch}(R)(D^n, C) \cong C_n$. A chain map out of $S^n = (R \text{ in degree } n)$ is determined by $\psi_n(1)$, which must satisfy $d^C_n \psi_n(1) = 0$ since $S^n$ has zero differential; so $\psi \mapsto \psi_n(1)$ is a natural bijection $\mathbf{Ch}(R)(S^n, C) \cong Z_n(C)$.
>
> **(b)** By (a), a lift against $0 \hookrightarrow D^n$ is a preimage in $E_n$ of a given $b \in B_n$; lifts exist for all $b$ and all $n$ iff $p$ is degreewise surjective, i.e. a fibration. By (a), a lift against $S^{n-1}\hookrightarrow D^n$ is, for a cycle $z \in Z_{n-1}(E)$ and $b \in B_n$ with $p(z) = db$, an $e \in E_n$ with $de = z$, $p(e) = b$. Existence of all such lifts is equivalent to $p$ being surjective with acyclic kernel; by the long exact homology sequence this is equivalent to $p$ being a degreewise-surjective quasi-isomorphism, i.e. a trivial fibration. $\blacksquare$

---

# Key Takeaways

**The sphere and disk complexes are corepresenting objects, and this is the whole reason they work as generators.** The deepest content of this exercise is that $D^n$ corepresents "degree-$n$ chains" and $S^n$ corepresents "$n$-cycles": maps *out of* them sample exactly those pieces of a complex. Whenever a model structure is cofibrantly generated, the generators are chosen so that mapping out of them probes the structure you care about — disks probe "underlying elements", spheres probe "cycles" or "boundary data". The reusable diagnostic: when you meet a new set of generating cofibrations, immediately ask "what functor does each generator corepresent?", because that functor is the translation key that turns every lifting problem into a concrete computation. This is the same move as computing $\mathbf{Ch}(R)(D^n, -) = (-)_n$, and it generalises to spaces ($D^n$ corepresents points-with-disk-structure) and to simplicial sets ($\Delta^n$ corepresents $n$-simplices via Yoneda).

**A lifting square is solved by reading off equations from the corners.** The procedure in (b) — replace each corner map by the element it represents, write the commutativity as an equation, write the lift as a solution — is the universal method for checking lifting properties against generators. It converts a category-theoretic diagram into linear algebra: "find $e$ with $de = z$ and $p(e) = b$". The trigger is any RLP-against-generators question; the reaction is "represent the corners, extract the equations, characterise solvability". Mastering this turns the otherwise daunting verification of model-category axioms into a sequence of routine module computations, which is exactly why cofibrantly generated model structures are tractable.

**Surjectivity plus acyclic kernel is the algebraic face of "trivial fibration".** The result that trivial fibrations are surjections with acyclic kernel is worth memorising as a trigger-reaction pattern: whenever you need a trivial fibration in $\mathbf{Ch}(R)$, build a surjection whose kernel is acyclic, and conversely whenever you have such a surjection you have a tool that lifts against every cofibration. This is the chain-complex analogue of "trivial Serre fibration = surjection with weakly contractible fibres" in topology, and the parallel is exact: acyclic kernel $\leftrightarrow$ weakly contractible fibre. Recognising the parallel lets you transport intuition between the algebraic and topological model structures, which is one of the chapter's central payoffs.
