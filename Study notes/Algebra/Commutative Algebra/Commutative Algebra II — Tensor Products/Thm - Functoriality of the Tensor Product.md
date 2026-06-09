---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Module Homomorphism"
  - "Def - Tensor Product of Modules"
  - "Thm - Universal Property of the Tensor Product of Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Let $R$ be a ring and $M, M', M_1, M_2, M_3, N, N', N_1, N_2, N_3$ be [[Def - Module|R-modules]]. We write $f : M\to M'$, $g : N\to N'$ for $R$-[[Def - Module Homomorphism|linear maps]], $f\otimes g : M\otimes_R N\to M'\otimes_R N'$ for the induced map, $m\otimes n$ for a pure tensor, and $[T]$ for the matrix of a linear map $T$ in chosen bases. For the Kronecker product, $T : k^a\to k^b$ and $S : k^c\to k^d$ are $k$-linear over a field $k$. The full registry is on [[Commutative Algebra II — Tensor Products]].

---

# Statement

> **Theorem (Functoriality of the tensor product).** Let $f : M\to M'$ and $g : N\to N'$ be $R$-linear maps.
>
> 1. **(Existence and uniqueness.)** There is a *unique* $R$-linear map $f\otimes g : M\otimes_R N\to M'\otimes_R N'$ with $(f\otimes g)(m\otimes n) = f(m)\otimes g(n)$ for all $(m,n)$.
> 2. **(Compositionality.)** For $M_1\xrightarrow{h}M_2\xrightarrow{f}M_3$ and $N_1\xrightarrow{i}N_2\xrightarrow{g}N_3$, $(f\otimes g)\circ(h\otimes i) = (f\circ h)\otimes(g\circ i)$, and $\operatorname{id}_M\otimes\operatorname{id}_N = \operatorname{id}_{M\otimes N}$. Hence $M\otimes_R -$ and $-\otimes_R N$ are functors.
> 3. **(Isomorphisms and surjections.)** If $f, g$ are isomorphisms, so is $f\otimes g$ (with inverse $f^{-1}\otimes g^{-1}$); if $f, g$ are surjective, so is $f\otimes g$.

> **Corollary (Kronecker product).** For $T : k^a\to k^b$, $S : k^c\to k^d$ with matrices $[T], [S]$, the matrix of $T\otimes S : k^a\otimes k^c\to k^b\otimes k^d$ in the lexicographically ordered tensor bases is the block matrix
> $$[T\otimes S] = \big([T]_{\ell i}\,[S]\big)_{\ell, i}\ \in\ M_{bd\times ac}(k),$$
> the **Kronecker product** of $[T]$ and $[S]$.

> **Warning (injectivity is NOT preserved).** $f, g$ injective does *not* imply $f\otimes g$ injective: $(\times p)\otimes\operatorname{id} : \mathbb{Z}\otimes\mathbb{Z}/p\to\mathbb{Z}\otimes\mathbb{Z}/p$ is the zero map though $\times p$ and $\operatorname{id}$ are injective.

---

# Motivation

A construction that only acts on objects is half a construction. The tensor product would be far less useful if it sent the pair $(M, N)$ to a module but had nothing to say about *maps* between modules. This theorem supplies the missing half: it makes $\otimes$ act on morphisms, turning $M\otimes_R -$ and $-\otimes_R N$ into genuine functors that transport whole diagrams of $R$-modules. With it, you can tensor an exact sequence, tensor a commuting square, tensor a resolution — the operations that make homological algebra possible.

The concrete payoff is the **Kronecker product**: when the modules are vector spaces and the maps are matrices, $f\otimes g$ is a perfectly explicit block matrix, and the rule "eigenvalues multiply" ($\lambda\mu$ for $T\otimes S$) drops out. This is the matrix incarnation that physicists and engineers use daily for composite systems.

But the deepest content is a *negative* fact, and it is the reason the next chapter exists. Functoriality preserves isomorphisms and surjections — the "good" half of exactness — but it **fails to preserve injections**. Tensoring an injective map can collapse it to zero. This single failure is the entire seed of flatness: a module $M$ is *flat* precisely when $M\otimes -$ does preserve injections, and the obstruction is measured by $\operatorname{Tor}$. So this theorem is simultaneously the tool that makes $\otimes$ functorial and the warning that it is only *right* exact.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "I have linear maps $f, g$ and want a map on the tensor product".

The first disguised source is **a property to transfer across a tensor**. The property $B$ is "$f$ or $g$ is surjective / an isomorphism / has a known matrix". The bridge: $f\otimes g$ inherits surjectivity and isomorphism (part 3) and has the Kronecker matrix. So to show $M\otimes N\to M'\otimes N'$ is onto, show $f, g$ are onto. The non-obvious caution is that injectivity does *not* transfer. *Example problem:* extension of scalars of a surjection $R^n\twoheadrightarrow M$ stays a surjection $S^n\twoheadrightarrow S\otimes M$.

The second disguised source is **a composite of tensored maps**. The property $B$ is "I have $(f\otimes g)\circ(h\otimes i)$ and want to simplify". The bridge is compositionality (part 2): it equals $(fh)\otimes(gi)$, computed factor-wise. The non-obviousness: tensoring respects composition, so chains of tensored maps collapse to a single tensored map. *Example problem:* verifying a tensored complex is a complex reduces to checking $d\circ d = 0$ factor-wise.

The third disguised source is **a matrix computation over a composite system**. The property $B$ is "operators $T, S$ act on factors $k^a, k^c$". The bridge is the Kronecker corollary: the joint operator is the block matrix $[T\otimes S]$, with eigenvalues $\lambda\mu$ and (for $T\otimes I + I\otimes S$) $\lambda + \mu$. *Example problem:* the energy spectrum of two non-interacting subsystems is the set of sums $E_i + E_j$ — the eigenvalues of $H_1\otimes I + I\otimes H_2$. See [[Ex - The Kronecker product of matrices]].

**Targets (Output Amplification)**

The conclusion $C$ is "$f\otimes g$ exists, is functorial, and preserves isos/surjections".

Combine $C$ with **a presentation $R^n\to R^m\to M\to 0$**. Tensoring with $N$ and using that $\otimes$ preserves surjections and cokernels gives a presentation $N^n\to N^m\to M\otimes N\to 0$. The result $E$ is **right exactness** of $M\otimes -$: it preserves cokernels and surjections. Nonobvious because it shows $M\otimes N$ can be *computed* from a presentation of $M$ — the basis of all concrete tensor computations.

Combine $C$ with **the failure of injectivity**. The map $(\times p)\otimes\operatorname{id}_{\mathbb{Z}/p} = 0$ shows $\mathbb{Z}/p\otimes -$ destroys an injection. The result $E$ is the *definition of flatness*: $M$ is flat iff $M\otimes -$ preserves injections, and the discrepancy is $\operatorname{Tor}^R_1$. Nonobvious because a positive theorem (functoriality) carries inside it the precise negative fact that launches homological algebra.

Combine $C$ with **the eigenvalue/trace structure of the Kronecker product**. From $[T\otimes S]$ one reads $\operatorname{tr}(T\otimes S) = \operatorname{tr}(T)\operatorname{tr}(S)$, $\det(T\otimes S) = (\det T)^c(\det S)^a$, and eigenvalues $\lambda_i\mu_j$. The result $E$ is the full spectral data of composite operators. Nonobvious because the spectrum of a $bd\times ac$ matrix is read off from the two small spectra without diagonalising the big matrix.

---

# Why Is It True

Each part is the universal property applied once. For **existence**, the assignment $(m,n)\mapsto f(m)\otimes g(n)$ is a map $M\times N\to M'\otimes N'$; it is bilinear because $f$ and $g$ are linear and $\otimes$ is bilinear ($f(m_1+m_2)\otimes g(n) = (f m_1 + f m_2)\otimes gn = fm_1\otimes gn + fm_2\otimes gn$, and scalars slide through both $f$ and $\otimes$). The [[Thm - Universal Property of the Tensor Product of Modules|universal property]] then hands you the unique linear $f\otimes g$ with the stated effect on pure tensors. *Functoriality is literally defined by the universal property — that is the one idea.*

For **compositionality**, both $(f\otimes g)(h\otimes i)$ and $(fh)\otimes(gi)$ are linear maps that send the pure tensor $m\otimes n$ to $f(h(m))\otimes g(i(n))$; since pure tensors generate, two linear maps agreeing on them are equal. Same for $\operatorname{id}\otimes\operatorname{id} = \operatorname{id}$. The functor laws hold *because pure tensors generate* and the universal property makes maps unique.

For **isomorphisms**, $f^{-1}\otimes g^{-1}$ is a two-sided inverse by compositionality: $(f^{-1}\otimes g^{-1})(f\otimes g) = (f^{-1}f)\otimes(g^{-1}g) = \operatorname{id}\otimes\operatorname{id} = \operatorname{id}$. For **surjections**, the image of $f\otimes g$ is a submodule containing every pure tensor $m'\otimes n'$ of $M'\otimes N'$ (write $m' = f(m)$, $n' = g(n)$ by surjectivity, so $m'\otimes n' = (f\otimes g)(m\otimes n)$); since pure tensors generate, the image is everything.

For the **failure of injectivity**, watch the scalars slide. $(\times p)\otimes\operatorname{id}$ sends $a\otimes\bar b\mapsto pa\otimes\bar b = a\otimes\overline{pb} = a\otimes\bar 0 = 0$ — the injectivity of $\times p$ is *defeated by sliding the $p$ onto the second factor*, where it annihilates because $pb\equiv 0\pmod p$. **The mechanism: $\otimes$ lets a scalar that is injective on one side migrate to the other side, where it can be a zero-divisor — so an injection can become the zero map.** This is exactly what flatness forbids.

For the **Kronecker product**, expand $(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j = (\sum_\ell [T]_{\ell i}f_\ell)\otimes(\sum_t [S]_{tj}f_t) = \sum_{\ell,t}[T]_{\ell i}[S]_{tj}\,f_\ell\otimes f_t$; ordering the bases $\{e_i\otimes e_j\}$ and $\{f_\ell\otimes f_t\}$ lexicographically arranges these coefficients into the block matrix $([T]_{\ell i}[S])$.

---

# What Makes This Hard

The conceptual trap is *symmetry expectation*: since $f\otimes g$ preserves isomorphisms and surjections, one reflexively expects injections too — and they are not preserved, which is the single most important fact to internalise. The non-obvious step is seeing *why* injectivity fails: the scalar $p$ in $\times p$ migrates across the $\otimes$ to the other factor and dies there. The common error is, in the Kronecker corollary, to mis-order the tensor basis (or to write $[S]\otimes[T]$ instead of $[T]\otimes[S]$), producing a matrix that is a permutation-conjugate of the correct one.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $f\otimes g$ by the universal property applied to the bilinear map $(m,n)\mapsto f(m)\otimes g(n)$. Prove every functor law and preservation property by checking on pure tensors (which generate). Get the inverse for isomorphisms from compositionality. Compute the Kronecker matrix by expanding on basis tensors. For the injectivity counterexample, slide the scalar across.

**Subgoal decomposition:**

1. **Define $f\otimes g$.** Show $(m,n)\mapsto f(m)\otimes g(n)$ is bilinear, hence induces a unique linear map.
   - *Hint:* Bilinearity follows from linearity of $f, g$ and bilinearity of $\otimes$; cite the [[Thm - Universal Property of the Tensor Product of Modules|universal property]].
   - *Why needed:* It is part 1, and everything else uses the map.

2. **Functor laws.** Show $(f\otimes g)(h\otimes i) = (fh)\otimes(gi)$ and $\operatorname{id}\otimes\operatorname{id} = \operatorname{id}$.
   - *Hint:* Both sides agree on pure tensors; pure tensors generate, so the maps are equal.
   - *Why needed:* It is part 2 and gives the inverse in part 3.

3. **Preservation.** Show isomorphisms and surjections are preserved.
   - *Hint:* Inverse is $f^{-1}\otimes g^{-1}$ by step 2; for surjections, every pure tensor of the target is hit, and pure tensors generate.
   - *Why needed:* It is part 3, the "good half" of exactness.

4. **Kronecker matrix.** Expand $(T\otimes S)(e_i\otimes e_j)$ and order the basis.
   - *Hint:* $Te_i\otimes Se_j = \sum_{\ell,t}[T]_{\ell i}[S]_{tj}\,f_\ell\otimes f_t$; lexicographic order gives the block form.
   - *Why needed:* It is the concrete corollary and the eigenvalue rule.

5. **Injectivity fails.** Exhibit $(\times p)\otimes\operatorname{id}_{\mathbb{Z}/p} = 0$.
   - *Hint:* $a\otimes\bar b\mapsto pa\otimes\bar b = a\otimes\overline{pb} = 0$; slide $p$ to the second factor.
   - *Why needed:* It is the warning and the seed of flatness.

---

# Lemma Decomposition

> [!note]- Lemma 1: $f\otimes g$ exists and is unique
> **Statement:** For $R$-linear $f : M\to M'$, $g : N\to N'$, there is a unique $R$-linear $f\otimes g : M\otimes N\to M'\otimes N'$ with $(f\otimes g)(m\otimes n) = f(m)\otimes g(n)$.
>
> **Hint:** The map $b(m,n) = f(m)\otimes g(n)$ is bilinear; apply the [[Thm - Universal Property of the Tensor Product of Modules|universal property]].
>
> **Why needed:** It constructs the object of the theorem; uniqueness makes the functor laws checkable on pure tensors.
>
> > [!note]- Full proof
> > Define $b : M\times N\to M'\otimes N'$ by $b(m,n) = f(m)\otimes g(n)$. It is $R$-bilinear: $b(m_1+m_2, n) = f(m_1+m_2)\otimes g(n) = (f m_1 + f m_2)\otimes g(n) = f m_1\otimes g n + f m_2\otimes g n = b(m_1,n)+b(m_2,n)$ using linearity of $f$ and bilinearity of $\otimes$; similarly in the second slot; and $b(rm, n) = f(rm)\otimes gn = (r\,fm)\otimes gn = r(fm\otimes gn) = r\,b(m,n) = b(m, rn)$. By the universal property there is a unique $R$-linear $f\otimes g : M\otimes N\to M'\otimes N'$ with $(f\otimes g)(m\otimes n) = b(m,n) = f(m)\otimes g(n)$.

> [!note]- Lemma 2: Compositionality
> **Statement:** $(f\otimes g)\circ(h\otimes i) = (f\circ h)\otimes(g\circ i)$ and $\operatorname{id}_M\otimes\operatorname{id}_N = \operatorname{id}_{M\otimes N}$.
>
> **Hint:** Both sides are linear and agree on pure tensors; pure tensors generate.
>
> **Why needed:** It is the functoriality and yields the inverse $f^{-1}\otimes g^{-1}$ for isomorphisms.
>
> > [!note]- Full proof
> > On a pure tensor $m\otimes n$: $\big((f\otimes g)(h\otimes i)\big)(m\otimes n) = (f\otimes g)(h(m)\otimes i(n)) = f(h(m))\otimes g(i(n)) = (fh)(m)\otimes(gi)(n) = \big((fh)\otimes(gi)\big)(m\otimes n)$. Two $R$-linear maps agreeing on the generating set of pure tensors are equal, so the maps coincide. Likewise $(\operatorname{id}_M\otimes\operatorname{id}_N)(m\otimes n) = m\otimes n$, so $\operatorname{id}_M\otimes\operatorname{id}_N = \operatorname{id}_{M\otimes N}$.

> [!note]- Lemma 3: Preservation of isomorphisms and surjections
> **Statement:** If $f, g$ are isomorphisms then $f\otimes g$ is an isomorphism with inverse $f^{-1}\otimes g^{-1}$; if $f, g$ are surjective then $f\otimes g$ is surjective.
>
> **Hint:** Use Lemma 2 for the inverse; for surjectivity, hit every pure tensor of the target.
>
> **Why needed:** It is the "good half" of exactness that does transfer, in contrast to injectivity.
>
> > [!note]- Full proof
> > **Isomorphisms.** By Lemma 2, $(f^{-1}\otimes g^{-1})(f\otimes g) = (f^{-1}f)\otimes(g^{-1}g) = \operatorname{id}_M\otimes\operatorname{id}_N = \operatorname{id}_{M\otimes N}$, and symmetrically $(f\otimes g)(f^{-1}\otimes g^{-1}) = \operatorname{id}_{M'\otimes N'}$. So $f\otimes g$ is invertible.
> >
> > **Surjections.** The image $\operatorname{im}(f\otimes g)$ is a submodule of $M'\otimes N'$. Any pure tensor $m'\otimes n'$ has $m' = f(m)$, $n' = g(n)$ for some $m, n$ (surjectivity), so $m'\otimes n' = f(m)\otimes g(n) = (f\otimes g)(m\otimes n)\in\operatorname{im}(f\otimes g)$. Pure tensors generate $M'\otimes N'$, so $\operatorname{im}(f\otimes g) = M'\otimes N'$.

> [!note]- Lemma 4: Injectivity is not preserved
> **Statement:** There are injective $R$-linear $f, g$ with $f\otimes g$ not injective; explicitly $(\times p)\otimes\operatorname{id}_{\mathbb{Z}/p}$ on $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/p$ is the zero map.
>
> **Hint:** Slide the scalar $p$ from the first factor to the second, where it annihilates.
>
> **Why needed:** It is the warning of the theorem and the defining obstruction that flatness removes.
>
> > [!note]- Full proof
> > Let $f = (\times p) : \mathbb{Z}\to\mathbb{Z}$ (injective, as $\mathbb{Z}$ is a domain) and $g = \operatorname{id} : \mathbb{Z}/p\to\mathbb{Z}/p$ (injective). For any $a\otimes\bar b\in\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/p$,
> > $$(f\otimes g)(a\otimes\bar b) = (pa)\otimes\bar b = a\otimes(p\bar b) = a\otimes\overline{pb} = a\otimes\bar 0 = 0,$$
> > using $r(m\otimes n) = (rm)\otimes n = m\otimes(rn)$ and $pb\equiv 0\pmod p$. Since pure tensors generate, $f\otimes g = 0$. But $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/p\cong\mathbb{Z}/p\neq 0$, so the zero map is not injective. Hence injectivity is not preserved.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : M\to M'$, $g : N\to N'$ be $R$-linear.
>
> **Part 1 (existence, uniqueness)** is **Lemma 1**: the bilinear map $(m,n)\mapsto f(m)\otimes g(n)$ induces, by the [[Thm - Universal Property of the Tensor Product of Modules|universal property]], the unique $R$-linear $f\otimes g$ with $(f\otimes g)(m\otimes n) = f(m)\otimes g(n)$.
>
> **Part 2 (compositionality)** is **Lemma 2**: on pure tensors both $(f\otimes g)(h\otimes i)$ and $(fh)\otimes(gi)$ send $m\otimes n\mapsto fh(m)\otimes gi(n)$; agreement on generators forces equality, and $\operatorname{id}\otimes\operatorname{id} = \operatorname{id}$. Thus $M\otimes_R -$ (and $-\otimes_R N$) preserve identities and composition, so are functors.
>
> **Part 3 (preservation)** is **Lemma 3**: $f^{-1}\otimes g^{-1}$ inverts $f\otimes g$ when $f, g$ are isomorphisms; and surjectivity of $f, g$ makes every pure tensor of $M'\otimes N'$ lie in the image, which therefore (pure tensors generating) is all of $M'\otimes N'$.
>
> ---
> **Kronecker corollary.** For $T : k^a\to k^b$, $S : k^c\to k^d$ with standard bases $e_i, f_\ell$ etc.,
> $$(T\otimes S)(e_i\otimes e_j) = Te_i\otimes Se_j = \Big(\sum_{\ell=1}^b [T]_{\ell i}f_\ell\Big)\otimes\Big(\sum_{t=1}^d [S]_{tj}f_t\Big) = \sum_{\ell, t}[T]_{\ell i}[S]_{tj}\,(f_\ell\otimes f_t).$$
> Ordering $\{e_i\otimes e_j\}$ and $\{f_\ell\otimes f_t\}$ lexicographically ($e_1\otimes e_1, \dots, e_1\otimes e_c, e_2\otimes e_1, \dots$) collects these coefficients into the $bd\times ac$ block matrix $[T\otimes S] = ([T]_{\ell i}[S])_{\ell, i}$, the Kronecker product. In particular each eigenpair $(\lambda, v)$ of $T$ and $(\mu, w)$ of $S$ gives an eigenpair $(\lambda\mu, v\otimes w)$ of $T\otimes S$, and $(\lambda+\mu, v\otimes w)$ of $T\otimes I + I\otimes S$.
>
> ---
> **Warning (injectivity)** is **Lemma 4**: $(\times p)\otimes\operatorname{id}_{\mathbb{Z}/p} = 0$ on $\mathbb{Z}\otimes\mathbb{Z}/p\cong\mathbb{Z}/p\neq 0$, so injectivity of the factors does not survive. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Spectrum of non-interacting quantum systems (physics).** For Hamiltonians $H_1, H_2$ on $\mathcal{H}_1, \mathcal{H}_2$, the joint Hamiltonian of the non-interacting composite is $H_1\otimes I + I\otimes H_2$, whose eigenvalues are the sums $E_i + E_j$ by the Kronecker eigenvalue rule. Nonobvious because the spectrum of the large $\dim_1\cdot\dim_2$ operator is read off from the two small spectra without diagonalising. See [[Ex - The Kronecker product of matrices]].

**Sylvester equation and Lyapunov stability (control theory).** The linear operator $X\mapsto AX + XB$ on matrices is $(A\otimes I + I\otimes B^{\!\top})$ under vectorisation; it is invertible iff no eigenvalue of $A$ is the negative of an eigenvalue of $B$, by the eigenvalue-sum rule. Nonobvious because solvability of a matrix equation becomes a spectral disjointness condition via the Kronecker product.

**Künneth formula (algebraic topology).** The homology of a product space $X\times Y$ is built from $H_*(X)\otimes H_*(Y)$, with a correction term — the $\operatorname{Tor}$ — that exists *because* $\otimes$ is not exact, exactly the failure of injectivity here. Nonobvious because the homology of a product is the tensor product of homologies *up to* the obstruction this theorem's warning predicts.

---

# Bridges

- **[[Thm - Universal Property of the Tensor Product of Modules|Universal Property]]** — functoriality is not an independent fact: $f\otimes g$ is *defined* by feeding the bilinear map $(m,n)\mapsto f(m)\otimes g(n)$ into the universal property, and every functor law (compositionality, preservation) is proved by "agree on pure tensors, which generate". This theorem is the universal property used systematically on morphisms.

- **[[Thm - Standard Isomorphisms of Tensor Products|Standard Isomorphisms]]** — functoriality is what lets the standard isomorphisms be *natural*: the commutativity isomorphism $M\otimes N\to N\otimes M$ is natural in $M$ and $N$ precisely because $f\otimes g$ behaves well under the swap, and distributivity over direct sums uses $f\otimes g$ to assemble the component maps.

- **Right exactness and flatness** — applying functoriality to a presentation $R^n\to R^m\to M\to 0$ and using preservation of surjections gives $N^n\to N^m\to M\otimes N\to 0$, the **right exactness** of $\otimes$; the failure of injectivity (Lemma 4) is exactly what *fails* on the left, and the modules that restore it are the **flat** ones. Both are developed in [[Commutative Algebra III — Flatness and Exactness]], with $\mathbb{Z}/p$ the canonical non-flat module witnessed here.

- **[[Ex - The Kronecker product of matrices|The Kronecker product]]** — the corollary is the computational face of functoriality; the exercise derives the block form, the eigenvalue rules $\lambda\mu$ and $\lambda+\mu$, and the identities $V^*\otimes W\cong\operatorname{Hom}(V,W)$ and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ from it.

---

# Unlocked by This

> [!tip] Right exactness, Tor, and flat modules *(from Homological Algebra)*
> The functor $M\otimes_R -$ is **right exact** (it preserves cokernels and surjections, by this theorem) but not left exact (Lemma 4). The left-hand failure is measured by the derived functors $\operatorname{Tor}^R_i(M, -)$, and $M$ is **flat** exactly when $M\otimes_R -$ is exact. The map $(\times p)\otimes\operatorname{id}_{\mathbb{Z}/p} = 0$ computes $\operatorname{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/p, \mathbb{Z}/p) = \mathbb{Z}/p\neq 0$. This is the whole of [[Commutative Algebra III — Flatness and Exactness]].

> [!tip] The Künneth theorem and external products *(from Algebraic Topology)*
> Functoriality of $\otimes$ on chain maps makes $C_*(X)\otimes C_*(Y)$ a complex computing $H_*(X\times Y)$; the **Künneth formula** $H_n(X\times Y)\cong\bigoplus_{p+q=n}H_p(X)\otimes H_q(Y)\ \oplus\ \bigoplus_{p+q=n-1}\operatorname{Tor}(H_p(X), H_q(Y))$ has a correction term precisely because $\otimes$ is only right exact — the Tor term is the homological shadow of the injectivity failure proved here.
