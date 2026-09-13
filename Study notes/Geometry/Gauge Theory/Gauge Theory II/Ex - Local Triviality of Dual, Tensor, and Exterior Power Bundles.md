---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Thm - Vector Bundle Construction Lemma"
  - "Def - Transition Function of a Vector Bundle"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ and $F\to M$ be smooth vector bundles over a common base $M$, of ranks $k$ and $l$ respectively. On page **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]** the derived families
$$E^{*},\qquad \Lambda^{p}E,\qquad E\oplus F,\qquad E\otimes F,\qquad \operatorname{Hom}(E,F)$$
are defined *fibrewise*: their fibre over $m\in M$ is $(E_{m})^{*}$, $\Lambda^{p}(E_{m})$, $E_{m}\oplus F_{m}$, $E_{m}\otimes F_{m}$, and $\operatorname{Hom}(E_{m},F_{m})$ respectively. Haydys (item A-R2.1.2) leaves it to the reader to check that each of these families of vector spaces is itself a smooth vector bundle — that is, satisfies local triviality (clause (iii) of the definition of a vector bundle). Carry out this check in full. Concretely:

1. For each operation, write down the local trivializations induced by trivializations of $E$ and $F$, and compute the resulting transition functions:
   $$\tau^{E^{*}}=(\tau^{E})^{-\mathsf{T}},\quad \Lambda^{p}\tau^{E},\quad \tau^{E}\oplus\tau^{F},\quad \tau^{E}\otimes\tau^{F},\quad \tau^{\operatorname{Hom}}\colon\phi\mapsto\tau^{F}\phi\,(\tau^{E})^{-1}.$$
2. Verify that each derived transition function is a **smooth** map into the appropriate general linear group, and satisfies the **cocycle conditions** $\tau_{\alpha\alpha}=\operatorname{id}$ and $\tau_{\alpha\gamma}=\tau_{\alpha\beta}\tau_{\beta\gamma}$ on triple overlaps. Do the case of $\operatorname{Hom}(E,F)$, whose transition $\phi\mapsto\tau^{F}\phi(\tau^{E})^{-1}$ is the one Haydys singles out, in explicit detail.
3. Conclude, via the **[[Thm - Vector Bundle Construction Lemma|Vector Bundle Construction Lemma]]**, that each derived family is a smooth vector bundle.
4. Show that the total-space topology and smooth structure the construction lemma produces on $E^{*}$ are exactly those making the projection $\pi_{E^{*}}\colon E^{*}\to M$ a smooth submersion with the induced maps as local trivializations, and that this pins them uniquely.

Here $A^{\mathsf{T}}$ is the transpose, $A^{-\mathsf{T}}:=(A^{-1})^{\mathsf{T}}=(A^{\mathsf{T}})^{-1}$, and $\binom{k}{p}$ is the rank of $\Lambda^{p}E$.

> [!warning] Notation: the source's typo-free transition for the dual
> Haydys's manifest records the dual transition as $\tau^{*}=(\tau^{-1})^{\mathsf{t}}$. This is the inverse transpose $(\tau^{E})^{-\mathsf{T}}$ used above; the two orders of "invert" and "transpose" agree, since $(\tau^{-1})^{\mathsf{T}}=(\tau^{\mathsf{T}})^{-1}$. We keep the corrected, unambiguous form $(\tau^{E})^{-\mathsf{T}}$ throughout. As Step 2 shows, using merely $\tau^{\mathsf{T}}$ or merely $\tau^{-1}$ would *not* give a cocycle — it is exactly the double reversal that rescues the homomorphism property.

**Recall.**

The objects in play are a vector bundle and its local-triviality clause, the transition functions of a bundle and their cocycle conditions, the derived (dual, exterior-power, sum, tensor, hom) bundles as fibrewise constructions, the construction lemma that manufactures a bundle from transition data, and the notion of a submersion.

![[Def - Vector Bundle#The Definition]]

A real smooth [[Def - Vector Bundle|vector bundle]] of rank $r$ is a smooth submersion $\pi\colon V\to M$ with each fibre $V_{m}=\pi^{-1}(m)$ a vector space isomorphic to $\mathbb{R}^{r}$, such that each point of $M$ has a neighbourhood $U$ with a diffeomorphism $\psi_{U}\colon\pi^{-1}(U)\to U\times\mathbb{R}^{r}$ (a [[Def - Local Trivialization|local trivialization]]) commuting with the projections and restricting to a linear isomorphism on each fibre. Local triviality is clause (iii); the submersion requirement is clause (i).

![[Def - Transition Function of a Vector Bundle#The Definition]]

Given two overlapping local trivializations $\psi_{\alpha},\psi_{\beta}$ of $E$ over $U_{\alpha},U_{\beta}$, the [[Def - Transition Function of a Vector Bundle|transition function]] $\tau^{E}_{\alpha\beta}\colon U_{\alpha\beta}\to\operatorname{GL}(k,\mathbb{R})$ (where $U_{\alpha\beta}:=U_{\alpha}\cap U_{\beta}$) is the unique smooth $\operatorname{GL}(k,\mathbb{R})$-valued map with
$$\bigl(\psi_{\alpha}\circ\psi_{\beta}^{-1}\bigr)(m,v)=\bigl(m,\ \tau^{E}_{\alpha\beta}(m)\,v\bigr),\qquad (m,v)\in U_{\alpha\beta}\times\mathbb{R}^{k}.$$
These satisfy the cocycle conditions $\tau^{E}_{\alpha\alpha}=\operatorname{id}$ and, on triple overlaps $U_{\alpha\beta\gamma}$, $\tau^{E}_{\alpha\gamma}=\tau^{E}_{\alpha\beta}\,\tau^{E}_{\beta\gamma}$. Equivalently, the frame $e^{\alpha}_{j}(m):=\psi_{\alpha}^{-1}(m,\varepsilon_{j})$ (with $\varepsilon_{j}$ the standard basis of $\mathbb{R}^{k}$) transforms by $e^{\beta}_{j}=\sum_{i}(\tau^{E}_{\alpha\beta})_{ij}\,e^{\alpha}_{i}$; we write $\tau^{F}_{\alpha\beta}\colon U_{\alpha\beta}\to\operatorname{GL}(l,\mathbb{R})$ for the transition functions of $F$.

![[Thm - Vector Bundle Construction Lemma#Statement]]

The [[Thm - Vector Bundle Construction Lemma|construction lemma]] is the converse machine: given a base $M$, a family of fibres $\{V_{m}\}$ of fixed dimension $r$, an open cover $\{U_{\alpha}\}$, fibrewise-linear bijections $\Phi_{\alpha}\colon\pi^{-1}(U_{\alpha})\to U_{\alpha}\times\mathbb{R}^{r}$, and smooth maps $\tau_{\alpha\beta}\colon U_{\alpha\beta}\to\operatorname{GL}(r,\mathbb{R})$ with $\Phi_{\alpha}\Phi_{\beta}^{-1}(m,v)=(m,\tau_{\alpha\beta}(m)v)$ satisfying the cocycle conditions, there is a **unique** topology and smooth structure on $V=\bigsqcup_{m}V_{m}$ making it a smooth rank-$r$ vector bundle with the $\Phi_{\alpha}$ as smooth local trivializations. Our task is to produce exactly this data for each derived family.

![[Def - Operations on Vector Bundles and Pull-Back Bundles#The Definition]]

We use the fibrewise definitions of $E^{*}$, $\Lambda^{p}E$, $E\oplus F$, $E\otimes F$, $\operatorname{Hom}(E,F)$ from **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]**, together with the standard multilinear algebra of the [[Def - Dual Space|dual space]], the [[Def - Alternating Tensor and Lambda k V Dual|exterior power]], and the [[Def - Tensor Product of Vector Spaces|tensor product]].

---

# Convergent Strategy

**Problem class.** This is a *manufacture-a-bundle-from-fibrewise-data* problem, the exact situation the construction lemma exists for. The five operations look like five separate verifications, but they are five instances of one phenomenon: each operation is a *smooth functor* of vector spaces, and a smooth functor sends a local trivialization to a local trivialization and a transition cocycle to a transition cocycle. The strategy is therefore to isolate the one structural lemma — that a smooth group homomorphism transports cocycles to cocycles — and then feed it five explicitly different homomorphisms.

**Assumption pattern.** The only inputs are the trivializations and transition cocycles $\{\tau^{E}_{\alpha\beta}\}$, $\{\tau^{F}_{\alpha\beta}\}$ of the given bundles, plus the fact that the fibre operations are functorial (natural in linear isomorphisms). The recognisable trigger is that we already have transition data and merely need to *transport* it through a fixed algebraic construction; whenever that is the shape, one looks for the group homomorphism $\rho$ implementing the construction and checks that it is smooth and multiplicative — cocycle transport is then automatic and simultaneous for the identity and triple-overlap conditions.

**Theorem routing.** The route is: (i) prove the **cocycle-transport lemma** — if $\rho\colon\operatorname{GL}(k)\to\operatorname{GL}(N)$ is a smooth group homomorphism and $\{\tau_{\alpha\beta}\}$ a smooth $\operatorname{GL}(k)$-cocycle, then $\{\rho\circ\tau_{\alpha\beta}\}$ is a smooth $\operatorname{GL}(N)$-cocycle (and its product-group version); (ii) for each operation exhibit the induced trivialization and identify its transition as $\rho\circ\tau$ (or $\rho\circ(\tau^{E},\tau^{F})$) for a *specific* $\rho$; (iii) check that $\rho$ is a smooth homomorphism into $\operatorname{GL}$ — five short but genuinely distinct computations, including the determinant of $\Lambda^{p}\tau$, of $\tau^{E}\otimes\tau^{F}$, and the explicit inverse of $\phi\mapsto\tau^{F}\phi(\tau^{E})^{-1}$; (iv) invoke the **[[Thm - Vector Bundle Construction Lemma]]** to conclude each is a bundle; (v) read off the submersion property of $\pi_{E^{*}}$ from the trivializations and the lemma's uniqueness.

**Key decision point.** The decisive move is to *route everything through group homomorphisms rather than verify cocycles by hand five times*. Doing so exposes the single subtle point — why the dual and hom transitions must use the inverse transpose $g\mapsto g^{-\mathsf{T}}$, not the transpose $g\mapsto g^{\mathsf{T}}$ or the inverse $g\mapsto g^{-1}$: only the double reversal is a group *homomorphism* ($g\mapsto g^{-1}$ and $g\mapsto g^{\mathsf{T}}$ are each anti-homomorphisms, so each alone would turn the cocycle $\tau_{\alpha\gamma}=\tau_{\alpha\beta}\tau_{\beta\gamma}$ into the *reversed* product and break it). Recognising that the cocycle condition *forces* the inverse transpose is the insight the exercise is really about.

---

# Legal Operations Used

The topic page for this chapter is not yet assembled; the operations are named descriptively and will be reconciled with its numbered Legal Operations list.

1. **Apply a fibre functor to a trivialization to induce a trivialization.** For each operation, apply the algebraic construction fibrewise to the linear isomorphism $\psi_{\alpha}|_{E_{m}}\colon E_{m}\to\mathbb{R}^{k}$ (and $\psi_{\alpha}|_{F_{m}}$), obtaining a fibrewise linear isomorphism from the derived fibre to the model space; this is the candidate local trivialization $\Phi_{\alpha}$.

2. **Identify the induced transition as a group homomorphism applied to the given cocycle.** Compute $\Phi_{\alpha}\Phi_{\beta}^{-1}$ and read off the transition as $\rho\circ\tau^{E}_{\alpha\beta}$ (or $\rho\circ(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})$) for the operation's structure homomorphism $\rho$.

3. **Transport a cocycle through a smooth homomorphism (the cocycle-transport lemma).** Use that a smooth group homomorphism preserves smoothness, the identity, and products, so it carries a transition cocycle to a transition cocycle — proved once, applied to all five operations.

4. **Verify a matrix map lands in $\operatorname{GL}$ by exhibiting a nonzero determinant or an explicit inverse.** For each $\rho$, confirm invertibility of the image, either by a determinant formula ($\det\Lambda^{p}g=(\det g)^{\binom{k-1}{p-1}}$, $\det(g\oplus h)=\det g\det h$, $\det(g\otimes h)=(\det g)^{l}(\det h)^{k}$) or by writing the two-sided inverse ($\phi\mapsto\tau^{F}\phi(\tau^{E})^{-1}$ inverts via $\phi\mapsto(\tau^{F})^{-1}\phi\,\tau^{E}$).

5. **Invoke the construction lemma to promote transition data to a bundle, and read the submersion off the trivialization.** Feed the verified data to the **[[Thm - Vector Bundle Construction Lemma]]**; then use $\pi=\operatorname{pr}_{1}\circ\Phi_{\alpha}$ and the lemma's uniqueness to identify and pin the total-space topology.

---

# Hints

> [!note]- Hint 1
> Do not attack the five operations separately. Each of $E^{*},\Lambda^{p}E,E\oplus F,E\otimes F,\operatorname{Hom}(E,F)$ is a functor $\mathcal{T}$ of vector spaces that is natural in linear isomorphisms. Apply $\mathcal{T}$ fibrewise to $\psi_{\alpha}|_{E_{m}}$ to get a trivialization of the derived family. What is the transition function of the result, in terms of $\mathcal T$ and $\tau^{E}_{\alpha\beta}$?

> [!note]- Hint 2
> You should find that the induced transition is $\mathcal{T}(\tau^{E}_{\alpha\beta})$, i.e. the functor applied to the transition matrix; for the two-bundle operations it is $\mathcal{T}(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})$. On matrices, $\mathcal T$ becomes a map $\rho\colon\operatorname{GL}(k)\to\operatorname{GL}(N)$. Prove one lemma: if $\rho$ is a smooth *group homomorphism*, then $\{\rho\circ\tau_{\alpha\beta}\}$ inherits the cocycle conditions from $\{\tau_{\alpha\beta}\}$. Then the whole problem reduces to checking, for each operation, that its $\rho$ is a smooth homomorphism into $\operatorname{GL}$.

> [!note]- Hint 3
> For the dual, the functor sends a linear iso $g$ to the map on covectors that keeps the pairing $\langle\xi,v\rangle$ invariant. Work out that this is $g\mapsto g^{-\mathsf{T}}$. Check it is a *homomorphism*: $(gh)^{-\mathsf{T}}=g^{-\mathsf{T}}h^{-\mathsf{T}}$. Notice that $g\mapsto g^{\mathsf{T}}$ alone reverses order ($(gh)^{\mathsf T}=h^{\mathsf T}g^{\mathsf T}$) and $g\mapsto g^{-1}$ alone reverses order too; only doing both restores order. This is *why* the transition is the inverse transpose.

> [!note]- Hint 4
> For $\operatorname{Hom}(E,F)$, the transition is $\phi\mapsto\tau^{F}\phi(\tau^{E})^{-1}$ on the matrix space $\operatorname{Hom}(\mathbb{R}^{k},\mathbb{R}^{l})$. To see it is smooth into $\operatorname{GL}$, note it is linear in $\phi$ (so smooth in $\phi$), its matrix entries are smooth functions of the entries of $\tau^{F}$ and of $(\tau^{E})^{-1}$ (which are smooth by Cramer's rule since $\det\tau^{E}\ne0$), and it is invertible with inverse $\phi\mapsto(\tau^{F})^{-1}\phi\,\tau^{E}$. For part 4, remember $\pi_{E^{*}}=\operatorname{pr}_{1}\circ\Phi^{*}_{\alpha}$ locally, and $\operatorname{pr}_{1}$ is a submersion while $\Phi^{*}_{\alpha}$ is a diffeomorphism.

---

# Solution

The plan is to prove one transport lemma, then run it five times. First we show that a smooth group homomorphism carries a transition cocycle to a transition cocycle; then, for each operation, we build the induced trivialization, identify its transition as such a homomorphism applied to the given cocycle, and verify the homomorphism is smooth and $\operatorname{GL}$-valued; finally the construction lemma delivers the bundle and, for $E^{*}$, its submersion topology. Throughout, $k=\operatorname{rk}E$, $l=\operatorname{rk}F$, $\{U_{\alpha}\}$ is a common trivializing cover (refine the two covers to a common one), and $\varepsilon_{1},\dots,\varepsilon_{k}$ is the standard basis of $\mathbb{R}^{k}$.

**Step 0: The cocycle-transport lemma.**

Let $\rho\colon\operatorname{GL}(k,\mathbb{R})\to\operatorname{GL}(N,\mathbb{R})$ be a smooth group homomorphism, and let $\{\tau_{\alpha\beta}\colon U_{\alpha\beta}\to\operatorname{GL}(k,\mathbb{R})\}$ be a smooth cocycle. Then $\{\rho\circ\tau_{\alpha\beta}\}$ is a smooth $\operatorname{GL}(N,\mathbb{R})$-valued cocycle. The same holds with $\operatorname{GL}(k)$ replaced by a product $\operatorname{GL}(l)\times\operatorname{GL}(k)$ and $\{\tau_{\alpha\beta}\}$ by the componentwise product cocycle $\{(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})\}$.

> [!note]- Derivation
> **Smoothness.** $\rho\circ\tau_{\alpha\beta}\colon U_{\alpha\beta}\to\operatorname{GL}(N,\mathbb{R})$ is smooth as a composition of the smooth map $\tau_{\alpha\beta}$ with the smooth map $\rho$.
>
> **Identity condition.** Since $\rho$ is a group homomorphism, $\rho(\operatorname{id}_{k})=\operatorname{id}_{N}$ (a homomorphism carries the identity to the identity). Hence
> $$(\rho\circ\tau_{\alpha\alpha})=\rho(\operatorname{id}_{k})=\operatorname{id}_{N}\qquad\text{(using }\tau_{\alpha\alpha}=\operatorname{id}_{k}\text{, the identity cocycle condition for }\tau).$$
>
> **Triple-overlap condition.** On $U_{\alpha\beta\gamma}$, using the cocycle condition $\tau_{\alpha\gamma}=\tau_{\alpha\beta}\tau_{\beta\gamma}$ for $\tau$ and multiplicativity of $\rho$,
> $$\rho\circ\tau_{\alpha\gamma}=\rho(\tau_{\alpha\beta}\,\tau_{\beta\gamma})=\rho(\tau_{\alpha\beta})\,\rho(\tau_{\beta\gamma})=(\rho\circ\tau_{\alpha\beta})(\rho\circ\tau_{\beta\gamma})\qquad(\rho\text{ multiplicative}).$$
> Thus $\{\rho\circ\tau_{\alpha\beta}\}$ is a smooth cocycle.
>
> **Product version.** The set $\operatorname{GL}(l)\times\operatorname{GL}(k)$ is a Lie group under componentwise multiplication, and $\{(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})\}$ is a cocycle in it because each component is: $(\tau^{F}_{\alpha\alpha},\tau^{E}_{\alpha\alpha})=(\operatorname{id},\operatorname{id})$ and $(\tau^{F}_{\alpha\gamma},\tau^{E}_{\alpha\gamma})=(\tau^{F}_{\alpha\beta}\tau^{F}_{\beta\gamma},\ \tau^{E}_{\alpha\beta}\tau^{E}_{\beta\gamma})=(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})(\tau^{F}_{\beta\gamma},\tau^{E}_{\beta\gamma})$. Repeating the three checks above with $\operatorname{GL}(k)$ replaced by the product group and $\rho$ a smooth homomorphism out of it proves the claim.

**Step 1: Each operation induces a trivialization whose transition is a homomorphism applied to the cocycle.**

For each operation we apply the fibre construction to the trivializing isomorphisms; the transition of the result is $\rho\circ\tau$ with $\rho$ the corresponding *structure homomorphism*. We record the isomorphism explicitly for the dual (the subtle case) and state the rest as instances of the same functorial computation.

> [!note]- Derivation
> Fix $U_{\alpha}$ and let $g_{\alpha}(m):=\psi^{E}_{\alpha}|_{E_{m}}\colon E_{m}\xrightarrow{\ \sim\ }\mathbb{R}^{k}$ and $h_{\alpha}(m):=\psi^{F}_{\alpha}|_{F_{m}}\colon F_{m}\xrightarrow{\ \sim\ }\mathbb{R}^{l}$ be the fibrewise linear isomorphisms of the given trivializations. By the transition definition, on $U_{\alpha\beta}$,
> $$g_{\alpha}(m)\,g_{\beta}(m)^{-1}=\tau^{E}_{\alpha\beta}(m),\qquad h_{\alpha}(m)\,h_{\beta}(m)^{-1}=\tau^{F}_{\alpha\beta}(m)\qquad\text{(both as elements of }\operatorname{GL}\text{).}$$
>
> **Dual $E^{*}$ (model space $(\mathbb{R}^{k})^{*}\cong\mathbb{R}^{k}$, rank $k$).** For a linear iso $g\colon E_{m}\to\mathbb{R}^{k}$ the natural induced isomorphism on duals preserving the pairing is $(g^{-1})^{*}=(g^{*})^{-1}\colon (E_{m})^{*}\to(\mathbb{R}^{k})^{*}$, characterised by $\bigl[(g^{-1})^{*}\xi\bigr](w)=\xi(g^{-1}w)$ for $\xi\in(E_{m})^{*}$, $w\in\mathbb{R}^{k}$; on coordinates (identifying $(\mathbb{R}^{k})^{*}\cong\mathbb{R}^{k}$ by the standard basis) this is left multiplication by the inverse transpose $g^{-\mathsf{T}}$ of the matrix of $g$. Define $\Phi^{*}_{\alpha}(\xi):=(m,(g_{\alpha}(m)^{-1})^{*}\xi)$ for $\xi\in(E_{m})^{*}$; it is a fibrewise linear isomorphism onto $U_{\alpha}\times\mathbb{R}^{k}$. Its transition is
> $$\Phi^{*}_{\alpha}(\Phi^{*}_{\beta})^{-1}(m,c)=\bigl(m,\ (g_{\alpha}g_{\beta}^{-1})^{-\mathsf{T}}c\bigr)=\bigl(m,\ (\tau^{E}_{\alpha\beta})^{-\mathsf{T}}c\bigr),$$
> so the dual transition is $\rho_{*}\circ\tau^{E}_{\alpha\beta}$ with $\rho_{*}(g):=g^{-\mathsf{T}}$. (This is the corrected form of Haydys's $\tau^{*}=(\tau^{-1})^{\mathsf t}$; see the Notation callout.)
>
> **Exterior power $\Lambda^{p}E$ (model $\Lambda^{p}\mathbb{R}^{k}$, rank $\binom{k}{p}$).** The functor $\Lambda^{p}$ sends $g$ to $\Lambda^{p}g$, the linear map with $(\Lambda^{p}g)(v_{1}\wedge\cdots\wedge v_{p})=gv_{1}\wedge\cdots\wedge gv_{p}$; its matrix in the standard basis of $\Lambda^{p}\mathbb{R}^{k}$ has as entries the $p\times p$ minors of $g$. Set $\Phi^{\Lambda}_{\alpha}(\eta):=(m,\Lambda^{p}g_{\alpha}(m)\,\eta)$; its transition is $\rho_{\Lambda}\circ\tau^{E}_{\alpha\beta}$ with $\rho_{\Lambda}(g):=\Lambda^{p}g$, because $\Lambda^{p}$ is a functor: $\Lambda^{p}(g_{\alpha}g_{\beta}^{-1})=\Lambda^{p}g_{\alpha}\,\Lambda^{p}(g_{\beta}^{-1})=\Lambda^{p}g_{\alpha}\,(\Lambda^{p}g_{\beta})^{-1}$.
>
> **Direct sum $E\oplus F$ (model $\mathbb{R}^{k}\oplus\mathbb{R}^{l}=\mathbb{R}^{k+l}$, rank $k+l$).** Set $\Phi^{\oplus}_{\alpha}(v,w):=(m,(g_{\alpha}(m)v,\ h_{\alpha}(m)w))$; its transition is $(g_{\alpha}g_{\beta}^{-1})\oplus(h_{\alpha}h_{\beta}^{-1})=\tau^{E}_{\alpha\beta}\oplus\tau^{F}_{\alpha\beta}$, the block-diagonal matrix, i.e. $\rho_{\oplus}\circ(\tau^{E}_{\alpha\beta},\tau^{F}_{\alpha\beta})$ with $\rho_{\oplus}(g,h):=\operatorname{diag}(g,h)$.
>
> **Tensor product $E\otimes F$ (model $\mathbb{R}^{k}\otimes\mathbb{R}^{l}\cong\mathbb{R}^{kl}$, rank $kl$).** Set $\Phi^{\otimes}_{\alpha}(u):=(m,(g_{\alpha}(m)\otimes h_{\alpha}(m))u)$; its transition is $(g_{\alpha}g_{\beta}^{-1})\otimes(h_{\alpha}h_{\beta}^{-1})=\tau^{E}_{\alpha\beta}\otimes\tau^{F}_{\alpha\beta}$, the [[Ex - The Kronecker product of matrices|Kronecker product]], i.e. $\rho_{\otimes}\circ(\tau^{E}_{\alpha\beta},\tau^{F}_{\alpha\beta})$ with $\rho_{\otimes}(g,h):=g\otimes h$, using the multiplicativity of the Kronecker product $(g_{1}\otimes h_{1})(g_{2}\otimes h_{2})=(g_{1}g_{2})\otimes(h_{1}h_{2})$.
>
> **Hom bundle $\operatorname{Hom}(E,F)$ (model $\operatorname{Hom}(\mathbb{R}^{k},\mathbb{R}^{l})\cong\mathbb{R}^{kl}$, rank $kl$).** For a homomorphism $\phi\colon E_{m}\to F_{m}$ set $\Phi^{H}_{\alpha}(\phi):=(m,\ h_{\alpha}(m)\,\phi\,g_{\alpha}(m)^{-1})$, i.e. read $\phi$ as an $l\times k$ matrix by conjugating with the trivializations. Its transition is
> $$\Phi^{H}_{\alpha}(\Phi^{H}_{\beta})^{-1}(m,M)=\bigl(m,\ (h_{\alpha}h_{\beta}^{-1})\,M\,(g_{\alpha}g_{\beta}^{-1})^{-1}\bigr)=\bigl(m,\ \tau^{F}_{\alpha\beta}\,M\,(\tau^{E}_{\alpha\beta})^{-1}\bigr),$$
> so the hom transition is $\rho_{H}\circ(\tau^{F}_{\alpha\beta},\tau^{E}_{\alpha\beta})$ with $\rho_{H}(a,b)(M):=a\,M\,b^{-1}$ acting on $M\in\operatorname{Hom}(\mathbb{R}^{k},\mathbb{R}^{l})$. This is the transition Haydys singles out.

**Step 2: Each structure homomorphism is a smooth homomorphism into $\operatorname{GL}$.**

We verify, for each $\rho$ above, that it is (a) a group homomorphism, (b) smooth, and (c) $\operatorname{GL}$-valued. Then Step 0 makes every derived transition a smooth cocycle. These are five distinct computations; we write each out.

> [!note]- Derivation
> Recall two facts used repeatedly: on $\operatorname{GL}(k,\mathbb{R})$, matrix multiplication is polynomial (hence smooth), and inversion $g\mapsto g^{-1}$ is smooth, with entries $(g^{-1})_{ij}=(-1)^{i+j}\det(\widehat{g}_{ji})/\det g$ by Cramer's rule — rational functions with nonvanishing denominator $\det g$ (a proof that $\operatorname{GL}$ is a Lie group is on **[[Ex - The General Linear Group is a Smooth Manifold]]**).
>
> **Dual, $\rho_{*}(g)=g^{-\mathsf{T}}$.**
> *Homomorphism:* $\rho_{*}(gh)=(gh)^{-\mathsf{T}}=\bigl((gh)^{-1}\bigr)^{\mathsf{T}}=(h^{-1}g^{-1})^{\mathsf{T}}=(g^{-1})^{\mathsf{T}}(h^{-1})^{\mathsf{T}}=g^{-\mathsf{T}}h^{-\mathsf{T}}=\rho_{*}(g)\rho_{*}(h)$, where the middle equality uses $(AB)^{\mathsf{T}}=B^{\mathsf{T}}A^{\mathsf{T}}$ and the reversal from inversion; the two order-reversals cancel. *Smooth:* composition of the smooth inversion and the linear (hence smooth) transpose. *$\operatorname{GL}$-valued:* $\det(g^{-\mathsf{T}})=\det(g^{-1})=(\det g)^{-1}\ne 0$, so $g^{-\mathsf{T}}\in\operatorname{GL}(k)$.
>
> **Exterior power, $\rho_{\Lambda}(g)=\Lambda^{p}g$.** *Homomorphism:* functoriality $\Lambda^{p}(gh)=\Lambda^{p}g\,\Lambda^{p}h$ and $\Lambda^{p}(\operatorname{id})=\operatorname{id}$, from $(\Lambda^{p}(gh))(v_{1}\wedge\cdots\wedge v_{p})=ghv_{1}\wedge\cdots\wedge ghv_{p}=(\Lambda^{p}g)(hv_{1}\wedge\cdots\wedge hv_{p})=(\Lambda^{p}g\,\Lambda^{p}h)(v_{1}\wedge\cdots\wedge v_{p})$. *Smooth:* the entries of $\Lambda^{p}g$ are $p\times p$ minors of $g$, polynomials in the entries of $g$. *$\operatorname{GL}$-valued:* invertibility is immediate from functoriality — $\Lambda^{p}g$ has the two-sided inverse $\Lambda^{p}(g^{-1})$, because $\Lambda^{p}g\,\Lambda^{p}(g^{-1})=\Lambda^{p}(gg^{-1})=\Lambda^{p}(\operatorname{id})=\operatorname{id}$ and likewise $\Lambda^{p}(g^{-1})\,\Lambda^{p}g=\operatorname{id}$, so $\Lambda^{p}g\in\operatorname{GL}(\binom{k}{p},\mathbb{R})$ with no appeal to diagonalisability. Its determinant is moreover $\det\Lambda^{p}g=(\det g)^{\binom{k-1}{p-1}}$: upper-triangularise $g$ over $\mathbb{C}$ (Schur decomposition), so that in a suitable ordered basis $g$ is upper triangular with diagonal entries its eigenvalues $\mu_{1},\dots,\mu_{k}$ (repeated with algebraic multiplicity); in the lexicographically ordered induced basis $\{\varepsilon_{i_{1}}\wedge\cdots\wedge\varepsilon_{i_{p}}\}$ of $\Lambda^{p}\mathbb{C}^{k}$ the map $\Lambda^{p}g$ is again upper triangular, with diagonal entry $\mu_{i_{1}}\cdots\mu_{i_{p}}$ on $\varepsilon_{i_{1}}\wedge\cdots\wedge\varepsilon_{i_{p}}$, whence $\det\Lambda^{p}g=\prod_{i_{1}<\cdots<i_{p}}\mu_{i_{1}}\cdots\mu_{i_{p}}=(\mu_{1}\cdots\mu_{k})^{\binom{k-1}{p-1}}=(\det g)^{\binom{k-1}{p-1}}\ne0$, since each of the $k$ indices lies in exactly $\binom{k-1}{p-1}$ of the $p$-subsets and $\mu_{1}\cdots\mu_{k}=\det g$.
>
> **Direct sum, $\rho_{\oplus}(g,h)=\operatorname{diag}(g,h)$.** *Homomorphism:* $\operatorname{diag}(g_{1},h_{1})\operatorname{diag}(g_{2},h_{2})=\operatorname{diag}(g_{1}g_{2},h_{1}h_{2})=\rho_{\oplus}((g_{1},h_{1})(g_{2},h_{2}))$ by block multiplication, and $\rho_{\oplus}(\operatorname{id},\operatorname{id})=\operatorname{id}_{k+l}$. *Smooth:* the entries of $\operatorname{diag}(g,h)$ are the entries of $g$, of $h$, and constants $0$. *$\operatorname{GL}$-valued:* $\det\operatorname{diag}(g,h)=\det g\,\det h\ne0$.
>
> **Tensor product, $\rho_{\otimes}(g,h)=g\otimes h$.** *Homomorphism:* $(g_{1}\otimes h_{1})(g_{2}\otimes h_{2})=(g_{1}g_{2})\otimes(h_{1}h_{2})$ (the mixed-product property of the [[Ex - The Kronecker product of matrices|Kronecker product]], proved there) and $\operatorname{id}_{k}\otimes\operatorname{id}_{l}=\operatorname{id}_{kl}$. *Smooth:* the entries of $g\otimes h$ are the products $g_{ij}h_{pq}$, polynomial in the entries. *$\operatorname{GL}$-valued:* invertibility is immediate from the same mixed-product property, which gives the two-sided inverse $g^{-1}\otimes h^{-1}$, since $(g\otimes h)(g^{-1}\otimes h^{-1})=(gg^{-1})\otimes(hh^{-1})=\operatorname{id}_{k}\otimes\operatorname{id}_{l}=\operatorname{id}_{kl}$ and likewise on the other side; explicitly $\det(g\otimes h)=(\det g)^{l}(\det h)^{k}\ne0$.
>
> **Hom, $\rho_{H}(a,b)(M)=aMb^{-1}$.** *Homomorphism:* for $(a_{1},b_{1}),(a_{2},b_{2})\in\operatorname{GL}(l)\times\operatorname{GL}(k)$ and any $M$,
> $$\rho_{H}\bigl((a_{1},b_{1})(a_{2},b_{2})\bigr)(M)=\rho_{H}(a_{1}a_{2},b_{1}b_{2})(M)=a_{1}a_{2}M(b_{1}b_{2})^{-1}=a_{1}a_{2}Mb_{2}^{-1}b_{1}^{-1},$$
> $$\bigl(\rho_{H}(a_{1},b_{1})\circ\rho_{H}(a_{2},b_{2})\bigr)(M)=\rho_{H}(a_{1},b_{1})\bigl(a_{2}Mb_{2}^{-1}\bigr)=a_{1}\bigl(a_{2}Mb_{2}^{-1}\bigr)b_{1}^{-1}=a_{1}a_{2}Mb_{2}^{-1}b_{1}^{-1},$$
> equal for all $M$; and $\rho_{H}(\operatorname{id},\operatorname{id})=\operatorname{id}$. So $\rho_{H}$ is a homomorphism (again the double reversal $b\mapsto b^{-1}$ inside conjugation is what restores order). *Smooth:* $\rho_{H}(a,b)$ is linear in $M$, so as an element of $\operatorname{GL}(\operatorname{Hom}(\mathbb{R}^{k},\mathbb{R}^{l}))$ its matrix entries are bilinear in the entries of $a$ and of $b^{-1}$; the entries of $b^{-1}$ are smooth in $b$ (Cramer), so $(a,b)\mapsto\rho_{H}(a,b)$ is smooth. *$\operatorname{GL}$-valued:* $\rho_{H}(a,b)$ has the two-sided inverse $\rho_{H}(a^{-1},b^{-1})\colon M\mapsto a^{-1}Mb$, since $a^{-1}(aMb^{-1})b=M$ and $a(a^{-1}Mb)b^{-1}=M$; a linear map with a two-sided inverse is invertible, so $\rho_{H}(a,b)\in\operatorname{GL}(\operatorname{Hom}(\mathbb{R}^{k},\mathbb{R}^{l}))$.
>
> By Step 0 applied to each of $\rho_{*},\rho_{\Lambda}$ (single-bundle) and $\rho_{\oplus},\rho_{\otimes},\rho_{H}$ (product-group), the five derived transition families
> $$\{(\tau^{E}_{\alpha\beta})^{-\mathsf{T}}\},\quad\{\Lambda^{p}\tau^{E}_{\alpha\beta}\},\quad\{\tau^{E}_{\alpha\beta}\oplus\tau^{F}_{\alpha\beta}\},\quad\{\tau^{E}_{\alpha\beta}\otimes\tau^{F}_{\alpha\beta}\},\quad\{\tau^{F}_{\alpha\beta}\,\cdot\,(\tau^{E}_{\alpha\beta})^{-1}\}$$
> are smooth $\operatorname{GL}$-valued cocycles.

**Step 3: The construction lemma promotes each to a smooth vector bundle.**

Each derived family, with the trivializations of Step 1 and the cocycles of Step 2, satisfies the hypotheses of the construction lemma, hence is a smooth vector bundle.

> [!note]- Derivation
> Take any one operation with induced fibrewise-linear bijections $\Phi_{\alpha}\colon\pi^{-1}(U_{\alpha})\to U_{\alpha}\times\mathbb{R}^{N}$ (here $N$ is $k$, $\binom{k}{p}$, $k+l$, $kl$, or $kl$) and transition $\tau^{\mathcal{T}}_{\alpha\beta}=\rho\circ\tau$ from Steps 1–2, which by Step 2 is smooth, $\operatorname{GL}(N)$-valued, and satisfies $\tau^{\mathcal{T}}_{\alpha\alpha}=\operatorname{id}$, $\tau^{\mathcal{T}}_{\alpha\gamma}=\tau^{\mathcal{T}}_{\alpha\beta}\tau^{\mathcal{T}}_{\beta\gamma}$. These are exactly hypotheses (i)–(iii) of the **[[Thm - Vector Bundle Construction Lemma|Vector Bundle Construction Lemma]]**: an open cover $\{U_{\alpha}\}$, fibrewise-linear bijections $\Phi_{\alpha}$ (with common fibre dimension $N$ — the fibres do have this fixed dimension: $\dim(E_{m})^{*}=k$, $\dim\Lambda^{p}(E_{m})=\binom{k}{p}$, $\dim(E_{m}\oplus F_{m})=k+l$, $\dim(E_{m}\otimes F_{m})=kl=\dim\operatorname{Hom}(E_{m},F_{m})$), and a smooth cocycle $\{\tau^{\mathcal{T}}_{\alpha\beta}\}$ realising $\Phi_{\alpha}\Phi_{\beta}^{-1}(m,v)=(m,\tau^{\mathcal{T}}_{\alpha\beta}(m)v)$. The lemma therefore endows the total space with a unique topology and smooth structure making it a smooth rank-$N$ vector bundle over $M$ with the $\Phi_{\alpha}$ as smooth trivializations. Applying this to each of the five operations proves that $E^{*}$, $\Lambda^{p}E$, $E\oplus F$, $E\otimes F$, and $\operatorname{Hom}(E,F)$ are smooth vector bundles, of ranks $k$, $\binom{k}{p}$, $k+l$, $kl$, $kl$ respectively.

**Step 4: The total-space topology of $E^{*}$ is the unique one making $\pi_{E^{*}}$ a submersion compatible with the trivializations.**

The topology and smooth structure the construction lemma places on $E^{*}$ make $\pi_{E^{*}}\colon E^{*}\to M$ a smooth submersion; and this data is pinned uniquely by the requirement that the induced maps $\Phi^{*}_{\alpha}$ be diffeomorphisms.

> [!note]- Derivation
> **The projection is a submersion.** By the construction lemma each $\Phi^{*}_{\alpha}\colon\pi_{E^{*}}^{-1}(U_{\alpha})\to U_{\alpha}\times\mathbb{R}^{k}$ is a diffeomorphism, and it intertwines the projections: $\operatorname{pr}_{1}\circ\Phi^{*}_{\alpha}=\pi_{E^{*}}$ on $\pi_{E^{*}}^{-1}(U_{\alpha})$ (this is the commuting-triangle clause of a trivialization). Hence locally
> $$\pi_{E^{*}}=\operatorname{pr}_{1}\circ\Phi^{*}_{\alpha}.$$
> The projection $\operatorname{pr}_{1}\colon U_{\alpha}\times\mathbb{R}^{k}\to U_{\alpha}$ is a [[Def - Immersion, Submersion, and Embedding|submersion]] (its differential $(v,w)\mapsto v$ is surjective at every point), and $\Phi^{*}_{\alpha}$ is a diffeomorphism (its differential is an isomorphism everywhere). A composition of a diffeomorphism followed by a submersion is a submersion — the differential $d\pi_{E^{*}}=d\operatorname{pr}_{1}\circ d\Phi^{*}_{\alpha}$ is surjective, being the composite of a surjection after an isomorphism. As $\{U_{\alpha}\}$ covers $M$, $\pi_{E^{*}}$ is a submersion on all of $E^{*}$; this verifies clause (i) of the definition of a vector bundle for $E^{*}$.
>
> **Uniqueness pins the topology.** The construction lemma asserts *unique*ness: there is exactly one topology and smooth structure on $E^{*}=\bigsqcup_{m}(E_{m})^{*}$ for which the $\Phi^{*}_{\alpha}$ are diffeomorphisms onto $U_{\alpha}\times\mathbb{R}^{k}$. Concretely this topology is the one for which a set $W\subseteq E^{*}$ is open if and only if $\Phi^{*}_{\alpha}(W\cap\pi_{E^{*}}^{-1}(U_{\alpha}))$ is open in $U_{\alpha}\times\mathbb{R}^{k}$ for every $\alpha$ (the topology transported from the model spaces and glued; it is well defined because the transition maps $\Phi^{*}_{\alpha}(\Phi^{*}_{\beta})^{-1}$ are diffeomorphisms of open sets by Step 2). With it the $\Phi^{*}_{\alpha}$ are trivializations and $\pi_{E^{*}}$ is a submersion by the previous paragraph.
>
> **Submersion alone does not pin it — compatibility does.** It is worth being precise about the phrasing: many inequivalent topologies on a set can make a given surjection a submersion, so "the topology making $\pi_{E^{*}}$ a submersion" is not by itself a definite description. What makes it definite is the *joint* requirement — a smooth manifold topology for which $\pi_{E^{*}}$ is a submersion *and* the fibrewise-linear maps $\Phi^{*}_{\alpha}$ are the local trivializations; that is exactly the vector-bundle structure, and the construction lemma says it is unique. So the total-space topology of $E^{*}$ is precisely the unique vector-bundle topology, and under it $E^{*}\to M$ is a submersion as required by clause (i). $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For smooth vector bundles $E,F\to M$ of ranks $k,l$, the fibrewise families $E^{*},\Lambda^{p}E,E\oplus F,E\otimes F,\operatorname{Hom}(E,F)$ are smooth vector bundles, of ranks $k,\binom{k}{p},k+l,kl,kl$; and the construction-lemma topology on $E^{*}$ is the unique vector-bundle topology, under which $\pi_{E^{*}}$ is a submersion.
>
> *Transport lemma.* If $\rho\colon\operatorname{GL}(k)\to\operatorname{GL}(N)$ (or $\rho\colon\operatorname{GL}(l)\times\operatorname{GL}(k)\to\operatorname{GL}(N)$) is a smooth group homomorphism and $\{\tau_{\alpha\beta}\}$ a smooth cocycle, then $\{\rho\circ\tau_{\alpha\beta}\}$ is a smooth cocycle: it is smooth as a composition, $\rho(\tau_{\alpha\alpha})=\rho(\operatorname{id})=\operatorname{id}$, and $\rho(\tau_{\alpha\gamma})=\rho(\tau_{\alpha\beta}\tau_{\beta\gamma})=\rho(\tau_{\alpha\beta})\rho(\tau_{\beta\gamma})$.
>
> *Induced transitions.* Writing $g_{\alpha}=\psi^{E}_{\alpha}|_{E_{m}}$, $h_{\alpha}=\psi^{F}_{\alpha}|_{F_{m}}$ with $g_{\alpha}g_{\beta}^{-1}=\tau^{E}_{\alpha\beta}$, $h_{\alpha}h_{\beta}^{-1}=\tau^{F}_{\alpha\beta}$, the fibrewise application of each operation to $g_{\alpha}$ (and $h_{\alpha}$) gives trivializations whose transitions are $(\tau^{E}_{\alpha\beta})^{-\mathsf{T}}$ (dual), $\Lambda^{p}\tau^{E}_{\alpha\beta}$ (exterior power), $\tau^{E}_{\alpha\beta}\oplus\tau^{F}_{\alpha\beta}$ (sum), $\tau^{E}_{\alpha\beta}\otimes\tau^{F}_{\alpha\beta}$ (tensor), and $M\mapsto\tau^{F}_{\alpha\beta}M(\tau^{E}_{\alpha\beta})^{-1}$ (hom); each is $\rho\circ\tau$ for the structure homomorphism $\rho_{*}(g)=g^{-\mathsf{T}}$, $\rho_{\Lambda}(g)=\Lambda^{p}g$, $\rho_{\oplus}(g,h)=\operatorname{diag}(g,h)$, $\rho_{\otimes}(g,h)=g\otimes h$, $\rho_{H}(a,b)M=aMb^{-1}$.
>
> *Each $\rho$ is a smooth homomorphism into $\operatorname{GL}$.* $\rho_{*}$: $(gh)^{-\mathsf{T}}=g^{-\mathsf{T}}h^{-\mathsf{T}}$ (double reversal), smooth by Cramer, $\det g^{-\mathsf{T}}=(\det g)^{-1}\ne0$. $\rho_{\Lambda}$: functorial, entries are minors, $\det\Lambda^{p}g=(\det g)^{\binom{k-1}{p-1}}\ne0$. $\rho_{\oplus}$: block-multiplicative, $\det=\det g\det h\ne0$. $\rho_{\otimes}$: $(g_{1}\otimes h_{1})(g_{2}\otimes h_{2})=(g_{1}g_{2})\otimes(h_{1}h_{2})$, $\det=(\det g)^{l}(\det h)^{k}\ne0$. $\rho_{H}$: $\rho_{H}((a_{1},b_{1})(a_{2},b_{2}))=\rho_{H}(a_{1},b_{1})\rho_{H}(a_{2},b_{2})$ by direct expansion, smooth (linear in $M$, entries smooth in $a,b^{-1}$), invertible with inverse $M\mapsto a^{-1}Mb$. By the transport lemma every derived transition is a smooth $\operatorname{GL}$-cocycle.
>
> *Conclusion via the construction lemma.* Each family has fixed fibre dimension, an open cover, fibrewise-linear bijections, and a smooth transition cocycle, so the **[[Thm - Vector Bundle Construction Lemma]]** makes it a smooth vector bundle of the stated rank. For $E^{*}$, the lemma's structure gives $\pi_{E^{*}}=\operatorname{pr}_{1}\circ\Phi^{*}_{\alpha}$ locally, a submersion after a diffeomorphism, hence a submersion; and the lemma's uniqueness makes the vector-bundle topology (the unique one for which the $\Phi^{*}_{\alpha}$ are diffeomorphisms) the total-space topology. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to "define" the dual transition as $\tau^{\mathsf{T}}$ (matching covariant/contravariant indices sloppily) or as $\tau^{-1}$, and then wave at the cocycle condition. Both fail. The map $g\mapsto g^{\mathsf{T}}$ satisfies $(gh)^{\mathsf{T}}=h^{\mathsf{T}}g^{\mathsf{T}}$ and $g\mapsto g^{-1}$ satisfies $(gh)^{-1}=h^{-1}g^{-1}$ — each is an *anti*-homomorphism, so each would turn $\tau_{\alpha\gamma}=\tau_{\alpha\beta}\tau_{\beta\gamma}$ into $\tau_{\beta\gamma}^{\sharp}\tau_{\alpha\beta}^{\sharp}$, the reversed product, which is not the cocycle condition unless the group is abelian (e.g. rank one). Only the inverse transpose $g\mapsto g^{-\mathsf{T}}$ — two reversals — is a genuine homomorphism, and that is exactly why the dual bundle's transition *must* be the inverse transpose. The same remark explains the two-sided form $aMb^{-1}$ for $\operatorname{Hom}$: the target index gets $a$ (covariant, unreversed) and the source index gets $b^{-1}$ (contravariant, reversed), and together they compose in the correct order.

---

# Key Takeaways

**A functorial fibre operation transports a bundle to a bundle, and the whole verification reduces to "the operation is a smooth group homomorphism on transition matrices".** The lesson generalises far past these five examples: any construction of vector spaces that is *natural in linear isomorphisms* — symmetric powers $\operatorname{Sym}^{p}E$, mixed tensors $E^{\otimes r}\otimes(E^{*})^{\otimes s}$, the determinant line $\Lambda^{k}E$, the trace-free or self-dual pieces of $\operatorname{End}E$ — automatically produces a bundle, because it induces a homomorphism $\rho$ from $\operatorname{GL}(k)$ (or a product) to $\operatorname{GL}$ of the model space, and the cocycle-transport lemma does the rest. The trigger to reach for this machine is precisely the phrase "the reader should check local triviality" of a fibrewise construction: instead of chasing charts, name the structure homomorphism $\rho$, check it is smooth and multiplicative and lands in $\operatorname{GL}$, and cite the construction lemma. The transferable diagnostic is that the *only* real content is the homomorphism property of $\rho$; smoothness is always Cramer's rule plus polynomiality, and $\operatorname{GL}$-valuedness is always a determinant or an explicit inverse.

**The cocycle condition is what forces the "right" transition law, and it is the group-homomorphism property that enforces it.** The recurring beginner error — writing the dual transition as $\tau^{\mathsf{T}}$ or $\tau^{-1}$, or the hom transition with the factors on the wrong side — is diagnosed instantly by the transport lemma: those maps are anti-homomorphisms and would reverse the triple-overlap product. The correct laws $g\mapsto g^{-\mathsf{T}}$ and $(a,b)\mapsto aMb^{-1}$ are singled out among all "index-balanced" candidates by being the ones that *compose in the correct order*. This is the abstract reason behind the classical bookkeeping that covariant indices transform by $\tau$ and contravariant indices by $\tau^{-\mathsf{T}}$: contravariance is exactly the passage to the inverse transpose, the unique way to keep the dual pairing invariant while remaining a homomorphism. When you next meet an unfamiliar tensor bundle and are unsure of its transition law, write the candidate as a map on matrices and test whether it is a homomorphism; only the homomorphism survives to define a bundle.

**A total space is determined not by "the projection is a submersion" alone but by compatibility with a chosen atlas of trivializations, and the construction lemma is the theorem that packages this uniqueness.** The subtlety flagged in Step 4 recurs whenever one builds a manifold by gluing charts: a bare surjection admits many topologies making it a submersion, and what selects the geometric one is the demand that a prescribed family of local models be diffeomorphisms. The construction lemma is precisely the statement that such a demand has a unique solution, and it is the workhorse behind every "the total space is a smooth manifold" claim in bundle theory — for the tangent bundle, for associated bundles, for the frame bundle. The pattern to carry forward: to endow a fibrewise-defined set with a canonical smooth structure, do not try to topologise the total space directly; instead supply trivializations and a smooth transition cocycle and let the construction lemma manufacture the unique compatible structure, then read off submersivity and any other local property from the model $\operatorname{pr}_{1}\colon U\times\mathbb{R}^{N}\to U$.
