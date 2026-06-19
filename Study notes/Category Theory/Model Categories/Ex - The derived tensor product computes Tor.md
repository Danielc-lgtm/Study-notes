---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Quillen Adjunction and Quillen Equivalence"
  - "Thm - Quillen Adjunctions Descend to Derived Adjunctions"
  - "Def - Tensor Product of Modules"
  - "Def - Chain Map and Chain Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a ring and $N$ a fixed left $R$-module (take $R$ commutative for simplicity). On $\mathbf{Ch}(R)$ with the projective model structure, consider the functor $-\otimes_R N$.

(a) Show that $-\otimes_R N : \mathbf{Ch}(R) \to \mathbf{Ch}(R)$ (suitably, as a left adjoint to $\mathrm{Hom}_R(N, -)$) is a **left Quillen functor**: it preserves cofibrations and trivial cofibrations.

(b) Conclude that its **total left derived functor** $\mathbf{L}(-\otimes_R N)$ exists, computed by $M \mapsto Q M \otimes_R N$ where $QM$ is a cofibrant (= projective) replacement of $M$.

(c) Show that the homology of the derived tensor product computes the classical **Tor** groups:
$$H_n\big(\mathbf{L}(M \otimes_R N)\big) = H_n(P_\bullet \otimes_R N) = \mathrm{Tor}^R_n(M, N),$$
where $P_\bullet \xrightarrow{\sim} M$ is a projective resolution. Explain why the answer is independent of the chosen resolution.

> [!note]- Algebraic background: tensor product, Tor, and why tensoring is not exact
> The **tensor product** $M \otimes_R N$ is the universal target of $R$-bilinear maps out of $M \times N$; for a free module $R^k$, $R^k \otimes_R N = N^k$. Tensoring is **right exact** but not left exact: applying $-\otimes_R N$ to a short exact sequence $0 \to A \to B \to C \to 0$ gives an exact sequence $A \otimes N \to B \otimes N \to C \otimes N \to 0$, but the left map need not be injective. The failure is measured by **Tor**: there is a long exact sequence $\cdots \to \mathrm{Tor}_1(C, N) \to A \otimes N \to B \otimes N \to C \otimes N \to 0$. Classically $\mathrm{Tor}^R_n(M, N)$ is defined by taking a projective resolution $P_\bullet \xrightarrow{\sim} M$, applying $-\otimes_R N$, and taking homology: $\mathrm{Tor}_n(M, N) = H_n(P_\bullet \otimes_R N)$. The key fact making this well-defined is that any two projective resolutions are chain-homotopy equivalent.

**Recall:**

![[Def - Quillen Adjunction and Quillen Equivalence#The Definition]]

The total left derived functor $\mathbf{L}F = F \circ Q$ applies $F$ after cofibrant replacement; see [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]]. In $\mathbf{Ch}(R)$, cofibrant replacement of a module is projective resolution (see [[Ex - The homotopy category of chain complexes is the derived category]]).

---

# Convergent Strategy

**Problem class:** This is a derived-functor computation — the homological-algebra instance of "compute a derived functor" from the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]]. It shows that the classical $\mathrm{Tor}$ is literally the total left derived functor of $\otimes$, an instance of [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]].

**Assumption pattern:** The recognizable feature is that $-\otimes_R N$ is a left adjoint (to $\mathrm{Hom}_R(N, -)$) that *fails* to preserve quasi-isomorphisms but *does* preserve cofibrations and trivial cofibrations. This is the signature of a functor that needs deriving, and the unlock is checking the Quillen condition rather than the impossible "preserves all weak equivalences."

**Theorem routing:** Part (a) routes through "tensoring with $N$ preserves degreewise-projective monomorphisms" and Ken Brown-type reasoning. Part (b) is the existence of $\mathbf{L}F$ from [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] (part 1), with $\mathbf{L}F(M) = QM \otimes N$. Part (c) computes the homology of $QM \otimes N = P_\bullet \otimes N$ and identifies it with $\mathrm{Tor}$ by definition; independence of resolution is the homotopy-invariance built into $\mathbf{L}F$.

**Key decision point:** The non-obvious point is *why* $-\otimes N$ must be derived at all: tensoring is only right exact, so it does not respect quasi-isomorphisms (a quasi-isomorphism $P_\bullet \to M$ tensored with $N$ need not be a quasi-isomorphism). The decision is to recognize that the cofibrant replacement step is precisely what repairs this — you tensor the *resolution*, not the module, and the resolution is the cofibrant model on which $\otimes$ behaves.

---

# Legal Operations Used

1. **Operation 4 from the topic page (replace by a cofibrant model).** The derived tensor product tensors the projective resolution $QM = P_\bullet$, not $M$ itself; cofibrant replacement is the whole content.

2. **Operation 8 from the topic page (recognize a class by its lifting property), via Ken Brown.** Cofibration preservation is checked against the generating cofibrations of $\mathbf{Ch}(R)$, and Ken Brown's lemma upgrades trivial-cofibration preservation to preservation of weak equivalences between cofibrant objects.

3. **Operation 1 from the topic page (factor a map).** Cofibrant replacement of $M$ is the factorization $0 \to QM \xrightarrow{\sim} M$, i.e. the projective resolution.

---

# Hints

> [!note]- Hint 1
> Why does $-\otimes N$ need deriving? Tensoring is only right exact. Tensoring a quasi-isomorphism $P_\bullet \xrightarrow{\sim} M$ with $N$ need not be a quasi-isomorphism — that discrepancy is exactly $\mathrm{Tor}$. So $-\otimes N$ does not descend to homotopy categories directly.

> [!note]- Hint 2
> For (a): cofibrations of $\mathbf{Ch}(R)$ are degreewise-split monos with projective cokernel. Tensoring with $N$ preserves degreewise splittings (split monos stay split monos under any additive functor) and sends projective cokernels to... well, $P \otimes N$ — preservation of cofibrations follows. For trivial cofibrations, use that tensoring a contractible complex stays contractible.

> [!note]- Hint 3
> For (b): by [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]], a left Quillen functor has a total left derived functor $\mathbf{L}F = F \circ Q$. Here $QM = P_\bullet$ is a projective resolution, so $\mathbf{L}(-\otimes N)(M) = P_\bullet \otimes N$.

> [!note]- Hint 4
> For (c): $\mathrm{Tor}_n(M, N)$ is *defined* as $H_n(P_\bullet \otimes N)$. So the homology of the derived tensor product is Tor by definition. Independence of resolution is automatic: $\mathbf{L}F$ is well-defined on the homotopy category, and any two projective resolutions are isomorphic there (chain-homotopy equivalent).

---

# Solution

The solution verifies $-\otimes N$ is left Quillen (a), invokes the existence of the derived functor (b), and identifies its homology with Tor (c), with independence of resolution coming free from homotopy-invariance.

**Step 1: $-\otimes_R N$ is a left Quillen functor.**

> [!note]- Derivation
> $-\otimes_R N$ is left adjoint to $\mathrm{Hom}_R(N, -)$ (the tensor-hom adjunction), so it is a left adjoint. *Cofibration preservation:* a cofibration in $\mathbf{Ch}(R)$ is a degreewise-split monomorphism with degreewise-projective cokernel. Applying the additive functor $-\otimes N$ preserves degreewise splittings (a split mono $i$ with retraction $r$, $ri = \mathrm{id}$, gives $(r\otimes N)(i \otimes N) = \mathrm{id}$), so $i \otimes N$ is a degreewise-split mono; its cokernel is (cokernel of $i$) $\otimes N = (\text{projective}) \otimes N$, which is a direct summand of a free-module tensor, hence projective when $N$ is. So $-\otimes N$ sends cofibrations to cofibrations. *Trivial-cofibration preservation:* a trivial cofibration is a cofibration that is a quasi-isomorphism; its cofiber is a contractible complex of projectives, and tensoring a contractible complex with $N$ stays contractible (a contracting homotopy $s$ gives $s \otimes N$), so $-\otimes N$ preserves trivial cofibrations. Hence $-\otimes N$ is a left Quillen functor.

**Step 2: The total left derived functor exists.**

> [!note]- Derivation
> By [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] (part 1), since $-\otimes N$ is left Quillen it preserves weak equivalences between cofibrant objects (Ken Brown), so its total left derived functor exists:
> $$\mathbf{L}(-\otimes_R N) : \mathrm{Ho}(\mathbf{Ch}(R)) \to \mathrm{Ho}(\mathbf{Ch}(R)), \qquad \mathbf{L}(-\otimes N)(M) = QM \otimes_R N,$$
> where $QM$ is a cofibrant replacement of $M$. For a module $M$ in degree $0$, $QM = P_\bullet$ is a projective resolution (see [[Ex - The homotopy category of chain complexes is the derived category]]), so $\mathbf{L}(-\otimes N)(M) = P_\bullet \otimes_R N$.

**Step 3: The homology is Tor.**

> [!note]- Derivation
> By definition (algebraic background), $\mathrm{Tor}^R_n(M, N) = H_n(P_\bullet \otimes_R N)$ for a projective resolution $P_\bullet \xrightarrow{\sim} M$. By Step 2, $\mathbf{L}(-\otimes N)(M) = P_\bullet \otimes N$, so
> $$H_n\big(\mathbf{L}(M \otimes_R N)\big) = H_n(P_\bullet \otimes_R N) = \mathrm{Tor}^R_n(M, N).$$
> *Independence of resolution:* $\mathbf{L}(-\otimes N)$ is a well-defined functor on $\mathrm{Ho}(\mathbf{Ch}(R))$ by Step 2, and any two projective resolutions $P_\bullet, P'_\bullet$ of $M$ are isomorphic in $\mathrm{Ho}(\mathbf{Ch}(R))$ (they are quasi-isomorphic complexes of projectives, hence chain-homotopy equivalent — Whitehead in $\mathbf{Ch}(R)$). Applying the functor $\mathbf{L}(-\otimes N)$ to isomorphic objects gives isomorphic objects, so $P_\bullet \otimes N$ and $P'_\bullet \otimes N$ are chain-homotopy equivalent and have the same homology. Hence $\mathrm{Tor}_n(M, N)$ is independent of the resolution — a fact that classically requires the comparison theorem for resolutions but here is automatic from homotopy-invariance of the derived functor.

> [!note]- Complete formal solution
> **(a)** $-\otimes_R N$ is left adjoint to $\mathrm{Hom}_R(N, -)$. It preserves cofibrations (degreewise-split monos with projective cokernel: splittings and projectivity survive tensoring with $N$) and trivial cofibrations (contractible cofibers stay contractible under tensoring). So it is a left Quillen functor.
>
> **(b)** By [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]], the total left derived functor $\mathbf{L}(-\otimes N) = (-\otimes N) \circ Q$ exists; for a module $M$, $QM = P_\bullet$ is a projective resolution and $\mathbf{L}(M \otimes N) = P_\bullet \otimes N$.
>
> **(c)** $H_n(P_\bullet \otimes N) = \mathrm{Tor}^R_n(M, N)$ by definition of Tor. Independence of resolution follows because $\mathbf{L}(-\otimes N)$ is well-defined on $\mathrm{Ho}(\mathbf{Ch}(R))$ and any two projective resolutions of $M$ are isomorphic there, so their tensor products are chain-homotopy equivalent with equal homology. $\blacksquare$

---

# Key Takeaways

**Tor is the total left derived functor of the tensor product, which is the cleanest possible explanation of where derived functors come from.** The classical recipe — resolve, tensor, take homology — is not an ad hoc definition but the unwinding of $\mathbf{L}(-\otimes N) = (-\otimes N) \circ Q$, where $Q$ is cofibrant (projective) replacement. The model-categorical viewpoint explains every feature of Tor at once: why you resolve (cofibrant replacement is needed because $\otimes$ is left Quillen, not exact), why you can use *any* projective resolution (homotopy-invariance of the derived functor), and why Tor fits into a long exact sequence (it is the derived functor of a right-exact functor). The same template gives Ext as $\mathbf{R}\,\mathrm{Hom}$, group cohomology, sheaf cohomology, and every other derived functor — recognizing "classical derived functor = total derived functor of a Quillen functor" unifies the entire subject.

**A functor needs deriving precisely when it is left/right Quillen but not exact, and the fix is always to insert a (co)fibrant replacement.** Tensoring fails to respect quasi-isomorphisms because it is only right exact; the failure is the obstruction to $-\otimes N$ descending to the homotopy category. The repair is universal: replace the input by a cofibrant (projective) object on which the functor *does* respect weak equivalences (Ken Brown's lemma), and apply the functor there. This is the diagnostic to carry everywhere — when a construction is not homotopy-invariant, check whether it is a Quillen functor, and if so derive it by replacement. The trigger is "this functor doesn't respect the equivalences I care about"; the reaction is "is it Quillen? then resolve first."

**Independence of the resolution is homotopy-invariance, not a separate theorem.** Classically, that $\mathrm{Tor}$ does not depend on the chosen projective resolution requires the comparison theorem (any two resolutions are chain-homotopy equivalent), proved by a careful lifting argument. From the model-categorical view this is free: the derived functor is defined on the *homotopy category*, where all projective resolutions of $M$ are literally isomorphic, so applying the functor gives isomorphic outputs automatically. This is a recurring payoff of the abstract framework — well-definedness statements that take real work classically become trivial consequences of working in the homotopy category, because the framework was built precisely so that homotopy-invariant constructions are the only ones it can express. Recognizing "independence of choices = homotopy-invariance" saves enormous effort and is one of the main reasons to adopt the model-categorical language.
