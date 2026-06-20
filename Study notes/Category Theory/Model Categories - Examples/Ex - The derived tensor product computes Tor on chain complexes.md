---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Projective Model Structure on Chain Complexes"
  - "Thm - Chain Complexes of Modules Form a Model Category"
  - "Def - Tensor Product of Modules"
  - "Def - Projective Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

In the [[Def - Projective Model Structure on Chain Complexes|projective model structure]] on $\mathbf{Ch}(R)$, show that the total left derived functor of $-\otimes_R N$ computes Tor: for a [[Def - Module|module]] $M$ (as a complex in degree $0$),
$$H_n\big(\mathbf{L}(-\otimes_R N)(M)\big) \;\cong\; \mathrm{Tor}^R_n(M, N).$$
That is, $\mathbf{L}(-\otimes_R N)(M) = QM \otimes_R N$ where $QM$ is a cofibrant replacement (projective resolution), and its homology is Tor. Then verify the answer in the case $R = \mathbb{Z}$, $M = \mathbb{Z}/m$, $N = \mathbb{Z}/n$, recovering $\mathrm{Tor}^{\mathbb{Z}}_0 = \mathbb{Z}/\gcd(m,n)$ and $\mathrm{Tor}^{\mathbb{Z}}_1 = \mathbb{Z}/\gcd(m,n)$.

**Recall:**

The **total left derived functor** of a left [[Def - Quillen Adjunction and Quillen Equivalence|Quillen functor]] $F$ is $\mathbf{L}F = F \circ Q$, where $Q$ is cofibrant replacement; it exists because $F$ preserves weak equivalences between cofibrant objects (Ken Brown's lemma). In $\mathbf{Ch}(R)$ the cofibrant replacement of a module $M$ is a projective resolution $P_\bullet \xrightarrow{\sim} M$ (see [[Ex - Identifying the cofibrant objects in chain complexes]]).

![[Def - Tensor Product of Modules#The Definition]]

$\mathrm{Tor}^R_n(M, N) = H_n(P_\bullet \otimes_R N)$ for any projective resolution $P_\bullet \to M$ — the classical definition of the Tor groups.

---

# Convergent Strategy

**Problem class:** This is a "compute a derived functor" problem, the fourth recurring target. The route is the universal recipe: replace the input by a cofibrant object, apply the underlying functor, take homology — and recognise the output as a classical invariant.

**Assumption pattern:** The assumption is that $-\otimes_R N$ is a left Quillen functor on $\mathbf{Ch}(R)$ (it preserves cofibrations and trivial cofibrations because it preserves degreewise-projective monos with acyclic cokernel). This unlocks the existence of the total left derived functor $\mathbf{L}(-\otimes_R N) = (-\otimes_R N)\circ Q$. The further assumption that cofibrant replacement is projective resolution converts the abstract $\mathbf{L}$ into the concrete "resolve and tensor".

**Theorem routing:** The route is $\mathbf{L}(-\otimes_R N)(M) = QM \otimes_R N$ (definition of total derived functor) $= P_\bullet \otimes_R N$ (cofibrant replacement = projective resolution, from [[Ex - Identifying the cofibrant objects in chain complexes]]), whose homology is $\mathrm{Tor}^R_*(M,N)$ (classical definition). Independence of the resolution is guaranteed by [[Thm - Chain Complexes of Modules Form a Model Category|the model structure]] via Ken Brown's lemma.

**Key decision point:** The non-obvious choice is which factor to resolve. Tensor is symmetric up to the obvious flip, so one could resolve $M$ *or* $N$; both compute the same Tor (balancing of Tor). The decision to resolve $M$ rather than tensor it directly is the entire content — tensoring $M$ directly gives $M \otimes_R N$, which is only $\mathrm{Tor}_0$ and loses the higher information. The check at the end ($\mathbb{Z}/m \otimes \mathbb{Z}/n = \mathbb{Z}/\gcd$ but $\mathrm{Tor}_1 \neq 0$) is what makes the necessity of resolution vivid.

---

# Legal Operations Used

1. **Operation 3 from the topic page (replace a module by its projective resolution).** The core operation: $M$ is resolved before tensoring, which is what $\mathbf{L}$ does.

2. **Operation 1 from the topic page (check a chain-complex condition one degree at a time).** Computing $P_\bullet \otimes_R N$ and its homology is done degree by degree.

3. **Operation 9 from the topic page (dualize between projective and injective / balance).** The remark that one may resolve either factor — the balancing of Tor — is a use of the symmetry between the two resolutions.

---

# Hints

> [!note]- Hint 1
> By definition $\mathbf{L}(-\otimes_R N)(M) = QM \otimes_R N$. What is $QM$ for a module $M$?

> [!note]- Hint 2
> Once $QM = P_\bullet$ is a projective resolution, $\mathbf{L}(-\otimes_R N)(M) = P_\bullet \otimes_R N$. Compare its homology with the classical definition of Tor.

> [!note]- Hint 3
> For the example, resolve $\mathbb{Z}/m$ over $\mathbb{Z}$ by $\mathbb{Z} \xrightarrow{m} \mathbb{Z}$, tensor with $\mathbb{Z}/n$ (so the map becomes multiplication by $m$ on $\mathbb{Z}/n$), and compute the kernel and cokernel of $\cdot m : \mathbb{Z}/n \to \mathbb{Z}/n$.

---

# Solution

The computation is a direct unwinding: the total derived functor is "resolve and tensor", and the homology of a resolved-and-tensored complex is by definition Tor. The numerical check shows the higher Tor is genuinely nonzero, justifying the whole apparatus.

**Step 1: $\mathbf{L}(-\otimes_R N)(M) = P_\bullet \otimes_R N$ for a projective resolution $P_\bullet$.**

> [!note]- Derivation
> The functor $-\otimes_R N : \mathbf{Ch}(R) \to \mathbf{Ch}(\mathbb{Z})$ (or $\mathbf{Ch}(R')$ if $N$ is a bimodule) is a left [[Def - Quillen Adjunction and Quillen Equivalence|Quillen functor]]: it preserves cofibrations, because tensoring a degreewise-split mono with projective cokernel by $N$ yields again a degreewise-split mono (projectives stay flat, the splitting is preserved), and it preserves trivial cofibrations by the same reasoning plus acyclicity. By Ken Brown's lemma it preserves quasi-isomorphisms between cofibrant (degreewise-projective) complexes, so the total left derived functor exists and is computed by cofibrant replacement:
> $$\mathbf{L}(-\otimes_R N)(M) = QM \otimes_R N.$$
> By [[Ex - Identifying the cofibrant objects in chain complexes|the cofibrant-replacement identification]], $QM = P_\bullet$, a projective resolution of $M$. Hence $\mathbf{L}(-\otimes_R N)(M) = P_\bullet \otimes_R N$.

**Step 2: its homology is Tor.**

> [!note]- Derivation
> The homology of $P_\bullet \otimes_R N$ is, by the classical definition,
> $$H_n(P_\bullet \otimes_R N) = \mathrm{Tor}^R_n(M, N).$$
> [[Thm - Chain Complexes of Modules Form a Model Category|The model structure]] guarantees this is independent of the resolution chosen (Ken Brown's lemma: two projective resolutions are quasi-isomorphic cofibrant objects, and $-\otimes_R N$ sends quasi-isomorphisms between them to quasi-isomorphisms), so $\mathrm{Tor}^R_n(M,N)$ is well-defined — exactly the independence-of-resolution lemma of homological algebra, now a special case of the fundamental theorem. In particular $\mathrm{Tor}^R_0(M,N) = H_0(P_\bullet \otimes_R N) = M \otimes_R N$ (right-exactness of $\otimes$), and the higher Tor measure the failure of $\otimes$ to be exact.

**Step 3: the example $R = \mathbb{Z}$, $M = \mathbb{Z}/m$, $N = \mathbb{Z}/n$.**

> [!note]- Derivation
> A projective (free) resolution of $\mathbb{Z}/m$ over $\mathbb{Z}$ is the two-term complex
> $$P_\bullet : \quad 0 \to \mathbb{Z} \xrightarrow{\;\cdot m\;} \mathbb{Z} \to 0 \qquad (\text{degrees } 1, 0).$$
> Tensoring with $\mathbb{Z}/n$ (using $\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z}/n = \mathbb{Z}/n$) gives
> $$P_\bullet \otimes_{\mathbb{Z}} \mathbb{Z}/n : \quad 0 \to \mathbb{Z}/n \xrightarrow{\;\cdot m\;} \mathbb{Z}/n \to 0.$$
> Now compute the homology of $\cdot m : \mathbb{Z}/n \to \mathbb{Z}/n$. Let $d = \gcd(m, n)$.
> - $H_0 = \operatorname{coker}(\cdot m) = (\mathbb{Z}/n)/m(\mathbb{Z}/n)$. The image $m(\mathbb{Z}/n)$ is the subgroup generated by $m \bmod n$, which is $d\,\mathbb{Z}/n$ (since $\gcd(m,n) = d$). So $H_0 = (\mathbb{Z}/n)/(d\mathbb{Z}/n) \cong \mathbb{Z}/d = \mathbb{Z}/\gcd(m,n)$. This matches $\mathbb{Z}/m \otimes \mathbb{Z}/n = \mathbb{Z}/\gcd(m,n)$.
> - $H_1 = \ker(\cdot m \text{ on } \mathbb{Z}/n) = \{x \in \mathbb{Z}/n : mx \equiv 0 \bmod n\}$. This is the $m$-torsion of $\mathbb{Z}/n$, which is the subgroup of order $d = \gcd(m,n)$, namely $(n/d)\mathbb{Z}/n \cong \mathbb{Z}/d$. So $H_1 = \mathbb{Z}/\gcd(m,n)$.
>
> Therefore $\mathrm{Tor}^{\mathbb{Z}}_0(\mathbb{Z}/m, \mathbb{Z}/n) = \mathbb{Z}/\gcd(m,n)$ and $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/m, \mathbb{Z}/n) = \mathbb{Z}/\gcd(m,n)$, with all higher Tor zero (the resolution has length $1$).

> [!note]- Complete formal solution
> The functor $-\otimes_R N$ is left Quillen (preserves cofibrations and trivial cofibrations, since tensoring a degreewise-projective mono-with-projective-cokernel by $N$ preserves the splitting and acyclicity). Its total left derived functor is $\mathbf{L}(-\otimes_R N)(M) = QM \otimes_R N$, and $QM = P_\bullet$ is a projective resolution of $M$. Hence $H_n(\mathbf{L}(-\otimes_R N)(M)) = H_n(P_\bullet \otimes_R N) = \mathrm{Tor}^R_n(M,N)$ by the classical definition; independence of the resolution is Ken Brown's lemma applied in the [[Thm - Chain Complexes of Modules Form a Model Category|model structure]].
>
> For $R = \mathbb{Z}$, resolving $\mathbb{Z}/m$ by $0 \to \mathbb{Z}\xrightarrow{m}\mathbb{Z}\to 0$ and tensoring with $\mathbb{Z}/n$ gives $0 \to \mathbb{Z}/n \xrightarrow{m} \mathbb{Z}/n \to 0$. With $d = \gcd(m,n)$: the cokernel of $\cdot m$ is $\mathbb{Z}/d$ ($= H_0 = \mathrm{Tor}_0$) and the kernel is the $m$-torsion subgroup $\cong \mathbb{Z}/d$ ($= H_1 = \mathrm{Tor}_1$); higher Tor vanish. $\blacksquare$

---

# Key Takeaways

**Every "derived" functor is "resolve, apply, take homology" — and this exercise is the cleanest instance.** The single most reusable lesson is the three-step recipe $\mathbf{L}F = (\text{resolve}) \to (\text{apply } F) \to (\text{take homology})$, justified once and for all by the model structure. The trigger is any classical derived functor — Tor, Ext, derived global sections, group cohomology, sheaf cohomology; the reaction is to identify the underlying functor, cofibrant-replace (resolve) its input, and read off the answer. The model structure is what guarantees the result does not depend on the resolution, which is the lemma every homological algebra course proves by hand for each functor separately — here it is a single consequence of Ken Brown's lemma.

**The failure of a functor to be exact is exactly the higher derived functor, and resolution is the only way to see it.** The numerical check makes this concrete: $\mathbb{Z}/m \otimes \mathbb{Z}/n = \mathbb{Z}/\gcd$ captures $\mathrm{Tor}_0$, but the *naive* tensor product is blind to $\mathrm{Tor}_1 = \mathbb{Z}/\gcd$, which is the $m$-torsion that only appears after resolving. This is why tensoring directly (using the non-cofibrant module $M$ itself) is the illegal-but-tempting operation warned about on the topic page: it gives the right $\mathrm{Tor}_0$ but silently discards all higher information. The diagnostic to carry: whenever a functor is only right-exact (or only left-exact), its derived functors are nonzero in general and *must* be computed by resolution; the discrepancy between $F$ and $\mathbf{L}F$ is precisely the obstruction to exactness.

**Tor is balanced — you may resolve either factor — and this is a shadow of the symmetry of the model structure.** Although we resolved $M$, resolving $N$ instead gives the same Tor groups; this "balancing" is the statement that $\otimes^{\mathbf{L}}_R$ is a derived *bifunctor*, symmetric up to coherent isomorphism. The practical payoff is freedom: resolve whichever factor has the simpler projective resolution. More structurally, this is the chain-complex face of the general principle that a derived bifunctor can be computed by replacing either argument, which underlies the balancing of Ext (resolve the source projectively or the target injectively) and the symmetry of the derived tensor product on the derived category. Recognising when a derived functor is balanced tells you when you have a choice of resolution to exploit.
