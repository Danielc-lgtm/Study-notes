---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Reedy Category and the Reedy Model Structure"
  - "Def - Cylinder Object, Path Object, and Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{M}$ be a [[Def - Model Category|model category]] and $X$ an object. Consider the **constant cosimplicial object** $cX : \Delta \to \mathcal{M}$, with $(cX)^n = X$ for all $n$ and every coface and codegeneracy the identity.

(a) Show that $cX$ satisfies the *homotopical-constancy* condition for a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] (every structure map is a weak equivalence).

(b) Compute the degree-$1$ latching map of $cX$ and show that $cX$ is [[Def - Reedy Category and the Reedy Model Structure|Reedy cofibrant]] **if and only if** the fold map $\nabla : X \sqcup X \to X$ is a cofibration — equivalently, if and only if $X$ admits $X$ itself as a strict cylinder object. Conclude that $cX$ is generically *not* a frame.

(c) Give a concrete example in $\mathbf{Top}$ where $cX$ fails to be a frame, and explain why "just take the constant object" computes the wrong mapping space.

**Recall:**

A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on $X$ is a cosimplicial object $X^{\bullet}$ that is (1) Reedy cofibrant — each latching map $L_n X^{\bullet} \to X^n$ is a cofibration — and (2) homotopically constant — $X^0 \simeq X$ and every structure map is a weak equivalence.

![[Def - Cylinder Object, Path Object, and Homotopy#The Definition]]

The degree-$1$ latching object of a cosimplicial object is $L_1 X^{\bullet} = X^0 \sqcup X^0$ (the colimit over the two cofaces $d^0, d^1 : [0]\to[1]$), and the latching map $L_1 X^{\bullet} \to X^1$ is $(d^0, d^1)$.

---

# Convergent Strategy

**Problem class:** This is a "certify (or refute) a frame" problem — the §2 verification class from the topic page, where one checks the two frame conditions and finds that the naive candidate fails one of them. The routine is to compute the relevant latching map (Legal Operation 2/3) and test whether it is a cofibration.

**Assumption pattern:** The asset is the explicit structure of $cX$: all terms equal $X$, all structure maps identities. This makes condition (2) trivial and isolates the entire question in condition (1) — Reedy cofibrancy — which reduces to the degree-$1$ latching map because that is the first place the latching object is non-initial.

**Theorem routing:** No theorem is invoked beyond the [[Def - Cosimplicial and Simplicial Frame|frame definition]] and the latching-object computation; the result is a *warning* feeding [[Thm - Framings Compute Homotopy Function Complexes]] — using $cX$ as a frame computes the unresolved hom $\mathcal{M}(X, Y)$, which is not the [[Def - Homotopy Function Complex|homotopy function complex]].

**Key decision point:** The non-obvious recognition is that "$X$ is a strict cylinder for itself" — the fold map being a cofibration — is an extremely restrictive condition, essentially never true for non-discrete objects. The decision is to test condition (1) at degree $1$ first, because the degree-$1$ latching map is the fold map and immediately exposes the failure; testing higher degrees or condition (2) wastes effort on the parts that hold.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute a latching object).** We compute $L_1(cX) = X \sqcup X$ from the two cofaces $d^0, d^1 : [0] \to [1]$.

2. **Operation 3 from the topic page (check Reedy cofibrancy via latching maps).** The degree-$1$ latching map is the fold map $\nabla$, and Reedy cofibrancy demands it be a cofibration.

3. **Operation 5 from the topic page ((co)fibrantly replace before a homotopy invariant).** The repair is to Reedy-cofibrantly replace $cX$ rather than using it raw, which is exactly "resolve before computing the mapping space."

---

# Hints

> [!note]- Hint 1
> Condition (2) is immediate: every structure map of $cX$ is the identity, and identities are weak equivalences. So whether $cX$ is a frame depends entirely on condition (1), Reedy cofibrancy.

> [!note]- Hint 2
> The degree-$1$ latching object is the colimit over the two cofaces $d^0, d^1 : [0] \to [1]$, namely $L_1(cX) = (cX)^0 \sqcup (cX)^0 = X \sqcup X$. The latching map sends each copy of $X$ to $(cX)^1 = X$ by the (identity) cofaces, so it is the fold map $\nabla : X \sqcup X \to X$.

> [!note]- Hint 3
> A cylinder object on $X$ is a *factorization* of $\nabla$ as a cofibration followed by a weak equivalence. If $\nabla$ itself is a cofibration, then $X$ serves as its own cylinder (with $\sigma = \mathrm{id}$). For most objects $\nabla$ is *not* a cofibration — e.g. for $X$ a positive-dimensional CW complex, $X \sqcup X \to X$ is not a cofibration.

---

# Solution

The plan: Step 1 dispatches condition (2) trivially; Step 2 computes the degree-$1$ latching map as the fold map and identifies Reedy cofibrancy of $cX$ with "$\nabla$ is a cofibration"; Step 3 exhibits the failure in $\mathbf{Top}$ and explains the wrong-mapping-space consequence.

**Step 1: $cX$ is homotopically constant.**

> [!note]- Derivation
> Every coface and codegeneracy of $cX$ is, by definition, the identity map $X \to X$, and the augmentation $cX \to cX$ is the identity. Identities are weak equivalences (every model category has them, since $\mathcal{W}$ contains all identities and satisfies 2-out-of-3). In particular $(cX)^0 = X \simeq X$. So condition (2) of being a frame holds for $cX$. The entire question reduces to condition (1).

**Step 2: The degree-$1$ latching map is the fold map; Reedy cofibrancy ⟺ $\nabla$ a cofibration.**

> [!note]- Derivation
> At degree $0$: the latching category is empty, so $L_0(cX) = \varnothing$ and Reedy cofibrancy at degree $0$ says $\varnothing \to (cX)^0 = X$ is a cofibration, i.e. $X$ is cofibrant. (For a fair comparison assume $X$ cofibrant; this is condition we can satisfy.)
>
> At degree $1$: the latching category $\partial(\Delta^{+}\downarrow[1])$ has two objects, the cofaces $d^0, d^1 : [0] \to [1]$, and no further identifications (the only lower object is $[0]$). So
> $$L_1(cX) = (cX)^0 \sqcup (cX)^0 = X \sqcup X,$$
> and the latching map $L_1(cX) \to (cX)^1 = X$ is the map induced by $cX(d^0) = \mathrm{id}_X$ and $cX(d^1) = \mathrm{id}_X$, namely the **fold map** $\nabla : X \sqcup X \to X$ (the identity on each summand).
>
> Reedy cofibrancy at degree $1$ therefore requires the fold map $\nabla : X \sqcup X \to X$ to be a cofibration. Now recall a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] on $X$ is a factorization $X \sqcup X \xrightarrow{\text{cof}} \mathrm{Cyl}(X) \xrightarrow{\sim} X$ of $\nabla$. The constant object uses $\mathrm{Cyl}(X) = X$ with the second map the identity (a weak equivalence), so $cX$ being Reedy cofibrant at degree $1$ is *exactly* the statement that $X$ itself, with the fold map, is a strict cylinder object — i.e. $\nabla$ is a cofibration. Higher degrees impose further (generically also-failing) conditions, but degree $1$ already settles it: **$cX$ is Reedy cofibrant only if $\nabla$ is a cofibration.**
>
> For a non-discrete object this fails: in $\mathbf{Top}$, $X \sqcup X \to X$ glues the two copies to one, and a cofibration in $\mathbf{Top}$ (a retract of a relative cell complex) cannot be a surjection collapsing distinct points unless $X$ is discrete. So $cX$ is **not** Reedy cofibrant, hence **not** a frame, for any non-discrete space $X$.

**Step 3: Concrete failure in $\mathbf{Top}$ and the wrong mapping space.**

> [!note]- Derivation
> Take $X = S^1$ (or any positive-dimensional CW complex) in $\mathbf{Top}$ with the Quillen model structure (cofibrations = retracts of relative cell complexes). The fold map $\nabla : S^1 \sqcup S^1 \to S^1$ identifies the two circles; it is not a cofibration (it is not even injective). So $c(S^1)$ fails Reedy cofibrancy and is not a frame.
>
> If one nonetheless used $cX$ as a "frame" to compute a mapping complex, one would get
> $$\big(\mathcal{M}(cX, Y)\big)_n = \mathcal{M}((cX)^n, Y) = \mathcal{M}(X, Y),$$
> the *constant* simplicial set on the hom-set $\mathcal{M}(X, Y)$ — a discrete simplicial set with no higher simplices. Its $\pi_0$ is the raw hom-set $\mathcal{M}(X, Y)$, **not** the homotopy classes $[X, Y]$, and it has trivial higher homotopy, discarding all the higher-homotopy information the [[Def - Homotopy Function Complex|homotopy function complex]] is supposed to record. This is wrong on both counts: it is not homotopy-invariant (it depends on the strict $X$, not its homotopy type) and it is discrete (it forgets the space structure of $\mathrm{Map}(X,Y)$).
>
> **The repair** is Legal Operation 5: take a genuine Reedy-cofibrant replacement of $cX$ — a real cosimplicial frame $X^{\bullet}$, whose degree-$1$ term $X^1$ is an actual cylinder object (e.g. $X \times [0,1]$) rather than $X$ — and compute $\mathcal{M}(X^{\bullet}, RY)$. Then degree-$1$ maps $X^1 \to Y$ are genuine homotopies, $\pi_0 = [X,Y]$, and the higher simplices recover the mapping space.

> [!note]- Complete formal solution
> **(a)** Every structure map of $cX$ is an identity, hence a weak equivalence, so $cX$ is homotopically constant.
>
> **(b)** $L_0(cX) = \varnothing$ and $L_1(cX) = X \sqcup X$ (colimit over the two cofaces), with latching map the fold $\nabla : X \sqcup X \to X$. Reedy cofibrancy at degree $1$ demands $\nabla$ be a cofibration; this holds iff $X$ with the fold map is a strict cylinder object for itself. For non-discrete $X$ (e.g. in $\mathbf{Top}$) $\nabla$ is not a cofibration, so $cX$ is not Reedy cofibrant, hence not a frame.
>
> **(c)** For $X = S^1 \in \mathbf{Top}$, $\nabla : S^1\sqcup S^1 \to S^1$ is not a cofibration, so $c(S^1)$ is not a frame. Using it computes the constant simplicial set on $\mathcal{M}(S^1, Y)$, with $\pi_0 = \mathcal{M}(S^1,Y) \ne [S^1, Y]$ and no higher homotopy — the wrong mapping space. The correct computation uses a Reedy-cofibrant replacement of $c(S^1)$, e.g. with $X^1 = S^1\times[0,1]$. $\blacksquare$

---

# Key Takeaways

**Reedy cofibrancy is the load-bearing condition in the definition of a frame, and the constant object is the canonical illustration of why.** It is tempting to think a frame is just "a cosimplicial object resolving $X$," and the homotopical-constancy condition (every structure map a weak equivalence) seems to be the content. But the constant object satisfies homotopical constancy perfectly and still fails to be a frame — because it is not Reedy cofibrant. The lesson is that the *cofibrancy* condition, not the constancy condition, is where the work happens: it is what forces each level to be a genuine cylinder rather than a degenerate copy of $X$. Whenever you propose a candidate frame, check Reedy cofibrancy first and at the lowest non-trivial degree, because that is where naive candidates break.

**The degree-$1$ latching map is the fold map, so "frame" begins with "cylinder," and this anchors the whole construction to homotopy.** The computation $L_1 X^{\bullet} = X \sqcup X$ with latching map the fold $\nabla$ is the precise reason a frame's degree-$1$ term must be a cylinder object: Reedy cofibrancy at degree $1$ *is* the cofibration half of the cylinder axiom. This is the structural link between framings and the elementary theory of [[Def - Cylinder Object, Path Object, and Homotopy|homotopy via cylinders]]: a frame is "a coherent system of iterated cylinders," and the first cylinder appears in degree $1$ as the resolution of the fold map. The diagnostic to carry: if you ever see a fold map $A \sqcup A \to A$ that needs to be factored into a cofibration, you are building (the bottom of) a cylinder or a frame.

**Using an unresolved object computes a hom-set, not a hom-space — the same error as computing a derived functor without a resolution.** The constant object computes the discrete simplicial set on $\mathcal{M}(X,Y)$, which gets even $\pi_0$ wrong (it gives the raw hom-set, not homotopy classes) and discards all higher structure. This is exactly parallel to computing $\mathrm{Ext}(M,N)$ as $\mathrm{Hom}(M,N)$ without resolving $M$: you get the degree-zero part and nothing else, and even that may be wrong if $M$ is not projective. The universal moral of the chapter, made vivid here: *resolve before you compute*, and the resolution is a frame (= cofibrant replacement of the constant diagram). The contrasting positive case — where a strict tensoring *does* supply a frame for free — is [[Ex - In a simplicial model category the tensor with simplices is a frame]].
