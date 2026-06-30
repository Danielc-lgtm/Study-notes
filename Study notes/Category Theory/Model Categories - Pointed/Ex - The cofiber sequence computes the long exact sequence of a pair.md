---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Singular Homology"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $A \hookrightarrow X$ be a [[Def - Cofibrant and Fibrant Objects|cofibration]] of pointed spaces (a "good pair").

1. Show the [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] $C_f$ of $f : A \hookrightarrow X$ is the quotient $X/A$.
2. Apply a reduced cohomology theory $\widetilde{E}^*$ (a contravariant [[Def - Homotopy|homotopy]] functor $[-, Z_\bullet]$ sending cofiber sequences to long exact sequences) to the Puppe cofiber sequence to recover the **long exact sequence of the pair** $(X, A)$:
$$\cdots \to \widetilde{E}^{\,n}(X/A) \to \widetilde{E}^{\,n}(X) \to \widetilde{E}^{\,n}(A) \xrightarrow{\partial} \widetilde{E}^{\,n+1}(X/A) \to \cdots.$$
3. State the homology version (covariant) and explain where the degree shift comes from.

**Recall:**

![[Def - Cofiber and Fiber Sequence#The Definition]]

The [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] $C_f$ of $f : A \to X$ is the [[Def - Pointed Model Category Suspension and Loop|homotopy pushout]] of $* \leftarrow A \xrightarrow{f} X$; for a [[Def - Cofibrant and Fibrant Objects|cofibration]] $f$, the strict and homotopy cofibers agree, so $C_f = X/A$. The Puppe sequence is $A \to X \to X/A \to \Sigma A \to \cdots$. A reduced cohomology theory $\widetilde{E}^n$ sends cofiber sequences to long exact sequences and has a suspension isomorphism $\widetilde{E}^n(\Sigma Y) \cong \widetilde{E}^{n-1}(Y)$. [[Def - Singular Homology|Singular homology]] $\widetilde{H}_n$ is the covariant analogue.

---

# Convergent Strategy

**Problem class:** This is a "produce a long exact sequence from a cofiber sequence" exercise — the maps-out-of-objects half of the machinery, recovering the most-used exact sequence in cohomology. The route is to identify the cofiber of an inclusion with the quotient, then apply a cohomology theory to the Puppe sequence.

**Assumption pattern:** The assumption that $A \hookrightarrow X$ is a *cofibration* is exactly what makes the strict quotient $X/A$ equal the homotopy cofiber — without it, $X/A$ would be the wrong (non-homotopy-invariant) object. This is the "good pair" hypothesis. Once $C_f = X/A$, the cofiber sequence and the cohomology theory's exactness do the rest, and the suspension isomorphism supplies the degree shift.

**Theorem routing:** Part (1) routes through the agreement of strict and homotopy cofibers for cofibrations. Part (2) routes through exactness of $\widetilde{E}^*$ on the Puppe cofiber sequence and the suspension isomorphism $\widetilde{E}^n(\Sigma A) \cong \widetilde{E}^{n-1}(A)$. Part (3) routes through the same with a covariant functor.

**Key decision point:** The non-obvious step is recognizing that the degree shift in the long exact sequence is the **suspension isomorphism**: the Puppe sequence's $\Sigma A$ term, hit by $\widetilde{E}^n$, becomes $\widetilde{E}^{n-1}(A)$, which is what makes the boundary map raise (or lower) degree. Identifying $\partial$ with "apply $\widetilde{E}$ to $X/A \to \Sigma A$ and use the suspension iso" is the choice that turns abstract exactness into the familiar boundary map.

---

# Legal Operations Used

1. **Operation 2 from the topic page (cofibrant/fibrant-replace before computing) and its corollary that for cofibrations strict = homotopy cofiber.** Part (1) uses that a cofibration's strict quotient is its homotopy cofiber.

2. **Operation 5 from the topic page (apply $[-, Z]$ to a cofiber sequence).** Part (2) applies a cohomology theory $\widetilde{E}^* = [-, Z_\bullet]$ to the Puppe sequence.

3. **Operation 7 from the topic page (rotate a (co)fiber sequence).** The full long exact sequence is read off the infinite (rotated) Puppe sequence and the suspension isomorphism.

---

# Hints

> [!note]- Hint 1
> For a cofibration $A \hookrightarrow X$, the homotopy cofiber is computed without replacement — the inclusion is already "good," so the strict pushout $* \cup_A X = X/A$ already is the homotopy cofiber.

> [!note]- Hint 2
> Apply $\widetilde{E}^n$ to the Puppe sequence $A \to X \to X/A \to \Sigma A \to \Sigma X \to \cdots$. Contravariance reverses the arrows, and exactness gives a long exact sequence.

> [!note]- Hint 3
> The term $\widetilde{E}^n(\Sigma A)$ equals $\widetilde{E}^{n-1}(A)$ by the suspension isomorphism. That is where the boundary map $\partial : \widetilde{E}^n(A) \to \widetilde{E}^{n+1}(X/A)$ comes from — re-indexing the suspension term.

---

# Solution

The solution identifies $C_f = X/A$ for a cofibration, applies a cohomology theory to the Puppe sequence, and reads off the long exact sequence of the pair with the boundary map coming from the suspension isomorphism.

**Step 1: $C_f = X/A$ for a cofibration.**

> [!note]- Derivation
> The [[Def - Cofiber and Fiber Sequence|homotopy cofiber]] of $f : A \to X$ is the homotopy pushout of $* \leftarrow A \xrightarrow{f} X$. To compute a homotopy pushout, one replaces the leg $A \to X$ by a [[Def - Cofibrant and Fibrant Objects|cofibration]]; but $f$ is *already* a cofibration, so no replacement is needed and the homotopy pushout equals the strict pushout
> $$C_f = * \cup_A X = X/A,$$
> the quotient space collapsing $A$ to the basepoint. This is precisely the "good pair" condition: for a cofibration, the strict quotient is homotopy-invariant and equals the homotopy cofiber. (For a non-cofibration the two differ, which is why the long exact sequence of a pair requires a good pair.)

**Step 2: The long exact sequence of the pair in cohomology.**

> [!note]- Derivation
> The Puppe cofiber sequence of $f$ is
> $$A \xrightarrow{f} X \xrightarrow{q} X/A \xrightarrow{\partial} \Sigma A \xrightarrow{-\Sigma f} \Sigma X \to \cdots.$$
> Apply the reduced cohomology theory $\widetilde{E}^n = [-, Z_n]$, contravariant and exact on cofiber sequences. Contravariance reverses arrows, and exactness gives
> $$\cdots \to \widetilde{E}^n(\Sigma A) \to \widetilde{E}^n(X/A) \xrightarrow{q^*} \widetilde{E}^n(X) \xrightarrow{f^*} \widetilde{E}^n(A) \to \cdots.$$
> Now use the **suspension isomorphism** $\widetilde{E}^n(\Sigma A) \cong \widetilde{E}^{n-1}(A)$ and $\widetilde{E}^n(\Sigma X) \cong \widetilde{E}^{n-1}(X)$ to re-index every suspension term. The map $\widetilde{E}^n(X/A) \to \widetilde{E}^n(\Sigma A)$ after $\Sigma A$ is re-indexed becomes the boundary $\partial : \widetilde{E}^{n}(A) \to \widetilde{E}^{n+1}(X/A)$ (shifting the indices to put the boundary in standard position). The result is the long exact sequence of the pair $(X, A)$:
> $$\cdots \to \widetilde{E}^{\,n}(X/A) \xrightarrow{q^*} \widetilde{E}^{\,n}(X) \xrightarrow{f^*} \widetilde{E}^{\,n}(A) \xrightarrow{\partial} \widetilde{E}^{\,n+1}(X/A) \to \cdots,$$
> with $\widetilde{E}^n(X/A) = E^n(X, A)$ the relative cohomology.

**Step 3: The homology version and the degree shift.**

> [!note]- Derivation
> For a *covariant* homotopy functor — reduced [[Def - Singular Homology|singular homology]] $\widetilde{H}_n$ — apply it to the same Puppe sequence *without* reversing arrows. Exactness gives
> $$\cdots \to \widetilde{H}_n(A) \xrightarrow{f_*} \widetilde{H}_n(X) \xrightarrow{q_*} \widetilde{H}_n(X/A) \xrightarrow{\partial} \widetilde{H}_{n-1}(A) \to \cdots,$$
> using the suspension isomorphism $\widetilde{H}_n(\Sigma A) \cong \widetilde{H}_{n-1}(A)$ to re-index. With $\widetilde{H}_n(X/A) = H_n(X, A)$ the relative homology, this is the long exact sequence of the pair in homology. The degree shift in $\partial$ — lowering by one in homology, raising by one in cohomology — is entirely the suspension isomorphism: the boundary map factors through the $\Sigma A$ term of the Puppe sequence, and $\widetilde{E}^*$ or $\widetilde{H}_*$ of a suspension is shifted by one.

> [!note]- Complete formal solution
> **(1)** For a cofibration $A \hookrightarrow X$, the homotopy cofiber needs no replacement, so $C_f = * \cup_A X = X/A$.
>
> **(2)** Apply the contravariant exact $\widetilde{E}^*$ to the Puppe sequence $A \to X \to X/A \to \Sigma A \to \cdots$; the suspension isomorphism $\widetilde{E}^n(\Sigma A) \cong \widetilde{E}^{n-1}(A)$ re-indexes the suspension terms, giving the long exact sequence of the pair $\cdots \to \widetilde{E}^n(X/A) \to \widetilde{E}^n(X) \to \widetilde{E}^n(A) \xrightarrow{\partial} \widetilde{E}^{n+1}(X/A) \to \cdots$.
>
> **(3)** Covariantly with $\widetilde{H}_*$, the same Puppe sequence gives $\cdots \to \widetilde{H}_n(A) \to \widetilde{H}_n(X) \to \widetilde{H}_n(X/A) \xrightarrow{\partial} \widetilde{H}_{n-1}(A) \to \cdots$; the degree shift is the suspension isomorphism. $\blacksquare$

---

# Key Takeaways

**The long exact sequence of a pair is the Puppe cofiber sequence under a cohomology theory.** What is presented in a first course as an axiom (the exactness axiom of Eilenberg–Steenrod) or proved by hand with the snake lemma is, structurally, nothing but applying a homotopy-invariant functor to the cofiber sequence $A \to X \to X/A \to \Sigma A$. The trigger to internalize is that *any* contravariant homotopy functor sending cofiber sequences to exact sequences automatically produces the long exact sequence of every good pair, and the homology version is the same with a covariant functor. This is why "is a cohomology theory" and "sends cofiber sequences to long exact sequences" are the same condition — the exactness axiom is the defining property, not an extra hypothesis.

**The "good pair" hypothesis is exactly the cofibration condition that makes the strict quotient the homotopy cofiber.** The reason elementary treatments fuss over "good pairs," "neighborhood deformation retracts," and CW pairs is that for a general [[Def - Subspace|subspace]] inclusion, the strict quotient $X/A$ is not homotopy-invariant and does not sit in an exact sequence. The clean model-category statement is: the quotient computes the homotopy cofiber precisely when the inclusion is a cofibration. The transferable diagnostic is that whenever a long exact sequence of a pair "works," there is a cofibration in the background making the quotient honest, and whenever it fails, the inclusion was not cofibrant and one must replace it (the mapping cylinder is exactly this replacement).

**Every degree shift in a long exact sequence is a suspension isomorphism in disguise.** The boundary map $\partial$ that raises (cohomology) or lowers (homology) degree by one does so because it factors through the $\Sigma A$ term of the Puppe sequence, and a cohomology theory of a suspension is shifted by one degree. This is the cofiber-sequence counterpart of the previous exercise's observation that the [[Def - Fibration|fibration]] boundary map shifts via $\Omega$. The unifying lesson is that *all* connecting [[Def - Homomorphism|homomorphisms]] in topology — pair, fibration, Mayer–Vietoris — get their degree shift from a suspension or loop hiding in a (co)fiber sequence, and the suspension–loop adjunction is the single mechanism behind every one of them.
