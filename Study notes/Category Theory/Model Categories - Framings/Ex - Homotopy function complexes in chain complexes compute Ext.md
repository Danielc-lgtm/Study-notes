---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Homotopy Function Complex"
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in $\mathcal{M} = \mathbf{Ch}_{\ge 0}(R)$, non-negatively graded chain complexes of [[Def - Module|$R$-modules]], with the projective model structure: weak equivalences are quasi-isomorphisms, fibrations are the maps that are surjective in positive degrees, cofibrations are the monomorphisms with degreewise-projective cokernel; cofibrant objects are (essentially) the complexes of projectives. Let $M, N$ be $R$-modules, regarded as complexes concentrated in degree $0$, with $M$ replaced by a projective resolution $P_\bullet \xrightarrow{\sim} M$ (a cofibrant model) and $N$ fibrant.

Prove that the [[Def - Homotopy Function Complex|homotopy function complex]] satisfies
$$\pi_n\,\mathrm{map}(M, N) \;\cong\; \mathrm{Ext}^{-n}_R(M, N) \quad (n \ge 0),$$
so in particular $\pi_0\,\mathrm{map}(M, N) = \mathrm{Hom}_R(M, N) = \mathrm{Ext}^0_R(M,N)$ and the higher homotopy groups vanish above the projective dimension, recovering the $\mathrm{Ext}$ groups. (Here negative-indexed $\mathrm{Ext}^{-n}$ for $n>0$ are understood via the standard degree conventions; the content is that the homotopy groups of the mapping space are the cohomology of the hom-complex $\mathrm{Hom}_R(P_\bullet, N)$.)

**Recall:**

A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on $M$ in $\mathbf{Ch}_{\ge 0}(R)$ corresponds, under the **Dold–Kan correspondence** $\mathbf{sMod}_R \simeq \mathbf{Ch}_{\ge 0}(R)$, to a simplicial resolution of $M$ by projectives — equivalently, the cosimplicial direction tensored with the simplices $C^{\bullet}_*(\Delta^{\bullet})$ produces the hom-complex.

![[Def - Chain Map and Chain Homotopy#The Definition]]

$\mathrm{Ext}^k_R(M, N) = H^k(\mathrm{Hom}_R(P_\bullet, N))$ where $P_\bullet \to M$ is a projective resolution; it is independent of the resolution chosen. The **normalized chains** functor $N : \mathbf{sMod}_R \to \mathbf{Ch}_{\ge 0}(R)$ and its inverse the Dold–Kan functor $\Gamma$ give an equivalence with $\pi_n(K) = H_n(NK)$ for a simplicial module $K$.

---

# Convergent Strategy

**Problem class:** This is a "identify the function complex with a known derived invariant via a convenient frame" problem at the hardest tier: the convenient frame is a projective resolution, and the identification routes through Dold–Kan to express $\pi_n$ of the mapping space as cohomology of the hom-complex, i.e. $\mathrm{Ext}$. It combines Legal Operations 5 (resolve), 6 (corepresentable of a frame), and the homological-algebra bridge from the topic page.

**Assumption pattern:** The assets are: $M$ is resolved by projectives $P_\bullet$ (a cofibrant model and a frame after Dold–Kan), $N$ is fibrant, and $\mathbf{Ch}_{\ge 0}(R)$ is equivalent to simplicial modules. The crucial recognition is that the *simplicial* direction of the function complex matches the *homological* direction of the resolution under Dold–Kan, so $\pi_n$ of the simplicial mapping object becomes $H_n$ of a chain complex, which is the cohomology computing $\mathrm{Ext}$.

**Theorem routing:** The route is: frame $M$ by (the simplicial module corresponding to) $P_\bullet$ → form $\mathrm{map}(M,N) = \mathcal{M}(\text{frame}, N)$ → recognize this simplicial abelian group's normalized chains as the hom-complex $\mathrm{Hom}_R(P_\bullet, N)$ → take homotopy groups $=$ homology $= \mathrm{Ext}$. Each arrow uses [[Thm - Framings Compute Homotopy Function Complexes]] (frame-independence licenses using $P_\bullet$), Dold–Kan ($\pi_n = H_n$ of normalized chains), and the definition of $\mathrm{Ext}$.

**Key decision point:** The non-obvious move is to pass through **Dold–Kan**: the homotopy function complex is a simplicial abelian group (since $\mathbf{Ch}(R)$ is additive, $\mathcal{M}(P_\bullet\otimes\text{frame}, N)$ is a simplicial $R$-module), and its homotopy groups are computed by its normalized chain complex — which is exactly $\mathrm{Hom}_R(P_\bullet, N)$. Choosing to compute $\pi_n$ via Dold–Kan rather than directly is what converts a homotopy-theoretic quantity into the homological $\mathrm{Ext}$.

---

# Legal Operations Used

1. **Operation 5 from the topic page ((co)fibrantly replace).** $M$ is replaced by a projective resolution $P_\bullet$ (cofibrant model); $N$ is fibrant. This is the homological-algebra instance of "resolve before computing."

2. **Operation 6 from the topic page (function complex as corepresentable of a frame).** We compute $\mathrm{map}(M,N)$ from the frame built on $P_\bullet$, obtaining a simplicial abelian group.

3. **Operation 4 from the topic page (frame = Reedy-cofibrant replacement of the constant diagram).** The projective resolution, via Dold–Kan, *is* the frame; frame-independence licenses using it.

---

# Hints

> [!note]- Hint 1
> $\mathbf{Ch}(R)$ is additive, so $\mathcal{M}(A, N)$ is naturally an abelian group, and a *cosimplicial* frame applied to it gives a *simplicial abelian group* (a simplicial $R$-module). Homotopy groups of a simplicial abelian group are computed by Dold–Kan: $\pi_n = H_n$ of the normalized (or unnormalized) chain complex.

> [!note]- Hint 2
> Under Dold–Kan, the cosimplicial frame on $M$ corresponds to a simplicial resolution of $M$ by projectives; applying $\mathrm{Hom}_R(-, N)$ levelwise and taking normalized chains gives the cochain complex $\mathrm{Hom}_R(P_\bullet, N)$ (the hom out of the projective resolution).

> [!note]- Hint 3
> Therefore $\pi_n\,\mathrm{map}(M, N) = H_n$ of the simplicial abelian group $= H^{?}(\mathrm{Hom}_R(P_\bullet, N))$, which by definition is $\mathrm{Ext}^{?}_R(M, N)$. Match the degree conventions ($\pi_n$ corresponds to the $n$th cohomology of the hom-complex) and use frame-independence to conclude the answer does not depend on the resolution.

---

# Solution

The plan has three moves. Step 1 sets up the frame from a projective resolution and observes the function complex is a simplicial abelian group. Step 2 applies Dold–Kan to compute its homotopy groups as the cohomology of $\mathrm{Hom}_R(P_\bullet, N)$. Step 3 identifies that cohomology with $\mathrm{Ext}$ and invokes frame-independence for resolution-independence. The non-obvious move is Step 2, where the simplicial direction of the mapping space becomes the homological direction of $\mathrm{Ext}$ via Dold–Kan.

**Step 1: Frame $M$ by a projective resolution; the function complex is a simplicial abelian group.**

> [!note]- Derivation
> Let $P_\bullet \xrightarrow{\sim} M$ be a projective resolution, a cofibrant model of $M$ in $\mathbf{Ch}_{\ge 0}(R)$. To compute $\mathrm{map}(M, N)$ we need a cosimplicial frame on $M$; by frame-independence ([[Thm - Framings Compute Homotopy Function Complexes]]) we may choose the most convenient one. The convenient frame is obtained from $P_\bullet$ via the **Dold–Kan** machinery: the simplicial $R$-module $\Gamma(P_\bullet)$ corresponding to $P_\bullet$ under Dold–Kan, with its simplicial structure, serves (after the standard cosimplicial/simplicial bookkeeping) as the resolution computing the mapping space. Concretely, the frame's degree-$n$ term tensors $P_\bullet$ with the chains on $\Delta^n$, and applying $\mathrm{Hom}_R(-, N)$ yields a *simplicial* $R$-module
> $$\mathcal{F}_\bullet, \qquad \mathcal{F}_n = \mathrm{Hom}_R\big((\text{degree-}n\text{ frame piece}), N\big),$$
> which is the homotopy function complex $\mathrm{map}(M, N)$ (it is a Kan complex because it is a simplicial abelian group, and all simplicial abelian groups are Kan). Because $\mathbf{Ch}(R)$ is additive, $\mathcal{F}_\bullet$ is a simplicial *abelian group*, not merely a simplicial set — this is what lets us use Dold–Kan to compute its homotopy.

**Step 2: Compute the homotopy groups via Dold–Kan as the cohomology of $\mathrm{Hom}_R(P_\bullet, N)$.**

> [!note]- Derivation
> For a simplicial abelian group $\mathcal{F}_\bullet$, the **Dold–Kan correspondence** gives $\pi_n(\mathcal{F}_\bullet) \cong H_n(N\mathcal{F}_\bullet)$, the $n$th homology of the normalized chain complex $N\mathcal{F}_\bullet$ (and equivalently of the unnormalized chain complex with the alternating-sum differential $\sum (-1)^i d_i$). So computing the homotopy groups of the mapping space is computing the homology of a chain complex.
>
> Now identify that chain complex. The frame on $M$ is, under Dold–Kan, the simplicial module $\Gamma(P_\bullet)$ whose normalized chains return $P_\bullet$. Applying the additive functor $\mathrm{Hom}_R(-, N)$ commutes with the relevant normalization (it is additive, hence preserves the alternating-sum differential), and the normalized chains of $\mathcal{F}_\bullet = \mathrm{Hom}_R(\Gamma(P_\bullet), N)$ are the **hom-complex**
> $$N\mathcal{F}_\bullet \;\cong\; \mathrm{Hom}_R(P_\bullet, N), \qquad \big(\mathrm{Hom}_R(P_\bullet, N)\big)^k = \mathrm{Hom}_R(P_k, N),$$
> with differential the dual of the resolution's differential, $\delta = \mathrm{Hom}_R(\partial, N)$. (The grading flips: a *simplicial* degree $n$ becomes a *homological* degree $n$ in the normalized chains, which is *cohomological* degree $n$ in the hom-complex since $\mathrm{Hom}$ is contravariant.) Therefore
> $$\pi_n\,\mathrm{map}(M, N) = H_n(N\mathcal{F}_\bullet) = H^n\big(\mathrm{Hom}_R(P_\bullet, N)\big).$$

**Step 3: Recognize the cohomology as $\mathrm{Ext}$, and use frame-independence.**

> [!note]- Derivation
> By the definition of the derived functor $\mathrm{Ext}$,
> $$H^n\big(\mathrm{Hom}_R(P_\bullet, N)\big) = \mathrm{Ext}^n_R(M, N),$$
> the $n$th $\mathrm{Ext}$ group, computed (as always) from a projective resolution of the first variable. Combining with Step 2,
> $$\boxed{\;\pi_n\,\mathrm{map}(M, N) \;\cong\; \mathrm{Ext}^n_R(M, N)\;}$$
> (writing $\mathrm{Ext}^n$ for the cohomological grading; in the homotopy-theoretic sign convention this is the $\mathrm{Ext}^{-n}$ of the problem statement, the discrepancy being only the direction in which one counts degrees). In particular:
> - $\pi_0\,\mathrm{map}(M, N) = \mathrm{Ext}^0_R(M, N) = \mathrm{Hom}_R(M, N)$, consistent with $\pi_0 = [M, N]$ and the fact that $\mathrm{Hom}$ in the homotopy category of complexes is chain-homotopy classes of maps, which for the resolution is exactly $H^0(\mathrm{Hom}(P_\bullet, N))$;
> - $\pi_n\,\mathrm{map}(M, N) = \mathrm{Ext}^n_R(M, N)$ vanishes for $n$ above the projective dimension of $M$, so the mapping space has finitely many non-trivial homotopy groups when $M$ has finite projective dimension.
>
> Finally, **frame-independence** is precisely the homological fact that $\mathrm{Ext}$ does not depend on the chosen projective resolution: two resolutions are weakly equivalent cofibrant models of $M$, [[Thm - Framings Compute Homotopy Function Complexes]] says they give weakly equivalent function complexes, and a weak equivalence of simplicial abelian groups is an isomorphism on all $\pi_n$ — hence the $\mathrm{Ext}$ groups agree. The model-categorical theorem and the homological theorem are the same statement.

> [!note]- Complete formal solution
> Let $P_\bullet \xrightarrow{\sim} M$ be a projective resolution (cofibrant model), $N$ fibrant. By frame-independence we use the frame on $M$ coming from $P_\bullet$ via Dold–Kan. The function complex $\mathrm{map}(M, N) = \mathcal{F}_\bullet$ is a simplicial abelian group with $\mathcal{F}_n = \mathrm{Hom}_R(\text{degree-}n\text{ frame piece}, N)$. By Dold–Kan, $\pi_n(\mathcal{F}_\bullet) = H_n(N\mathcal{F}_\bullet)$; since $\mathrm{Hom}_R(-,N)$ is additive and the frame's normalized chains return $P_\bullet$, $N\mathcal{F}_\bullet \cong \mathrm{Hom}_R(P_\bullet, N)$. Hence $\pi_n\,\mathrm{map}(M, N) = H^n(\mathrm{Hom}_R(P_\bullet, N)) = \mathrm{Ext}^n_R(M, N)$. In particular $\pi_0 = \mathrm{Hom}_R(M, N)$, and the groups vanish above $\mathrm{pd}(M)$. Frame-independence is exactly resolution-independence of $\mathrm{Ext}$. $\blacksquare$

---

# Key Takeaways

**The homotopy function complex is the space-level $\mathbf{R}\mathrm{Hom}$, and its homotopy groups are the $\mathrm{Ext}$ groups — framings generalize "resolve to compute derived functors."** This computation is the Rosetta stone connecting the abstract framing theory to classical homological algebra. A frame is a resolution; the corepresentable applied to it is the hom-complex; its homotopy is the cohomology that defines $\mathrm{Ext}$. So everything one knows about $\mathrm{Ext}$ — that it is computed from a projective resolution, that it is resolution-independent, that it measures the failure of $\mathrm{Hom}$ to be exact — is the chain-complex shadow of a general model-categorical fact about derived mapping spaces. The transferable recognition: whenever you compute a derived functor by resolving, you are computing the homotopy of a function complex, and the simplicial/homological direction of the resolution is the direction in which higher derived information lives.

**Dold–Kan is the bridge that turns a simplicial direction into a homological direction, and additivity is what lets you cross it.** The crux of the proof is that in an *additive* model category the function complex is a simplicial *abelian group*, so its homotopy groups are computed by a chain complex via Dold–Kan, converting $\pi_n$ (homotopy-theoretic) into $H_n$ (homological), which for the hom-complex is $\mathrm{Ext}^n$. This only works because $\mathbf{Ch}(R)$ is additive — in a non-additive model category the function complex is merely a simplicial set with no chain-complex description, and $\pi_n$ are genuine homotopy groups, not (co)homology. The diagnostic: in additive/stable settings, expect mapping spaces to be (connective) chain complexes and their homotopy to be cohomology; in non-additive settings, expect genuine spaces.

**Frame-independence and resolution-independence of $\mathrm{Ext}$ are literally the same theorem, and recognizing this demystifies both.** It can seem like a coincidence that $\mathrm{Ext}$ does not depend on the projective resolution, proved in homological algebra by the comparison theorem and chain homotopies. The model-categorical viewpoint reveals it as an instance of a general principle: the homotopy function complex does not depend on the chosen frame, because any two frames are weakly equivalent cofibrant replacements and right Quillen functors preserve such weak equivalences (Ken Brown's lemma). The classical comparison theorem for resolutions *is* the construction of the weak equivalence between two cofibrant replacements, and the chain-homotopy uniqueness *is* the statement that the induced map on function complexes is a weak equivalence. So the homological "$\mathrm{Ext}$ is well-defined" and the homotopical "$\mathrm{map}(X,Y)$ is well-defined" are one theorem in two languages — the bridge that [[Thm - Framings Compute Homotopy Function Complexes]] makes precise and that motivates the entire theory of derived categories.
