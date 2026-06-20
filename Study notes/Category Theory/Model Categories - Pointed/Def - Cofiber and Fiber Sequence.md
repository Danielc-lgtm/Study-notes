---
type: definition
subject: model-categories
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Pullback and Pushout"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Thm - The Homotopy Category of a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Pointed Model Category Suspension and Loop|pointed model category]] with zero object $*$, homotopy category $\mathrm{Ho}(\mathcal{C})$, suspension $\Sigma$ and loop $\Omega$. We write $[X, Y]$ for $\mathrm{Ho}(\mathcal{C})(X, Y)$, a pointed set with basepoint the **zero map** $0$. A map $f : X \to Y$ has a **homotopy cofiber** (the [[Def - Pullback and Pushout|homotopy pushout]] of $* \leftarrow X \xrightarrow{f} Y$), written $C_f$ or $Y/X$, and a **homotopy fiber** (the homotopy pullback of $X \xrightarrow{f} Y \leftarrow *$), written $F_f$. Connecting maps are written with a $\partial$. For a fixed test object $Z$, the contravariant functor $[-, Z]$ and the covariant functor $[Z, -]$ turn sequences of objects into sequences of pointed sets. The full symbol registry is on [[Model Categories — Pointed Model Categories and Cofiber Sequences]].

This is a compound page: it defines two dual interlocking notions — the **cofiber sequence** and the **fiber sequence** — together with their **connecting maps** and the **long exact sequences** they induce, because the fiber notion is the formal dual of the cofiber notion and the two are stated, proved, and used in parallel throughout the chapter.

---

# Axiom Motivation

The problem this definition solves is bookkeeping for "what a map forgets and what it adds." Given $f : X \to Y$, two natural questions are: what part of $Y$ is *not* hit by $X$, and what part of $X$ is *collapsed* into the basepoint of $Y$? In algebra these have crisp answers — cokernel and kernel — but in homotopy theory the cokernel and kernel are not homotopy-invariant; quotients and subobjects taken on the nose are the wrong thing, exactly as the strict pushout was the wrong suspension. The cofiber sequence is the homotopy-correct cokernel, and the fiber sequence is the homotopy-correct kernel, packaged so that they extend indefinitely and feed into exact sequences.

Begin with the cofiber. We want "$Y$ modulo the image of $X$," which in $\mathbf{Top}_*$ is the mapping cone: glue a cone on $X$ to $Y$ along $f$, so that all of $X$ is crushed to the cone point. Categorically the mapping cone is the **homotopy pushout** of $* \leftarrow X \xrightarrow{f} Y$, written $C_f = Y \cup_X CX$. This is forced by the same reasoning as the suspension: the strict pushout of $* \leftarrow X \to Y$ is the strict quotient $Y/f(X)$, which is not homotopy-invariant, so one replaces $f$ by a cofibration and takes the honest pushout. The first non-obvious move — and the reason the sequence does not stop at three terms — is to *ask the same question again*. Having built $X \xrightarrow{f} Y \xrightarrow{i} C_f$, form the cofiber of $i$. A short computation (the mapping-cone collapse: $C_i = C_f \cup_Y CY \simeq \Sigma X$) shows the cofiber of $i$ is, up to canonical weak equivalence, the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$. So the cofiber operation, iterated, does not produce an endless string of new objects — it loops back to $\Sigma X$, then $\Sigma Y$, then $\Sigma C_f$, and so on. This is the **Puppe sequence**:
$$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X \xrightarrow{\Sigma f} \Sigma Y \xrightarrow{\Sigma i} \Sigma C_f \to \cdots,$$
and the connecting map $\partial : C_f \to \Sigma X$ is precisely the cofiber-of-the-cofiber identification. Why is this the right structure rather than an arbitrary one? Because applying $[-, Z]$ to it yields a **long exact sequence of pointed sets**, and that exactness is the whole point: it is the machine that computes one mapping set from its neighbors.

Now the exactness, because it dictates the precise shape of the definition. Apply the contravariant $[-, Z]$ to $X \xrightarrow{f} Y \xrightarrow{i} C_f$. A map $Y \to Z$ extends over the cone $C_f$ exactly when its restriction to $X$ is null-homotopic — that is the universal property of the homotopy pushout. In the language of pointed sets this says: the image of $i^* : [C_f, Z] \to [Y, Z]$ is exactly the preimage of the basepoint under $f^* : [Y, Z] \to [X, Z]$, i.e. $\ker(f^*) = \mathrm{im}(i^*)$. That is exactness at $[Y, Z]$. Continuing with the suspension terms gives exactness everywhere, and the sequence
$$\cdots \to [\Sigma X, Z] \to [C_f, Z] \xrightarrow{i^*} [Y, Z] \xrightarrow{f^*} [X, Z]$$
is exact as a sequence of pointed sets (and of groups from the $[\Sigma X, Z]$ term leftward, because suspensions carry a co-group structure). If you had used the strict cofiber, this exactness would fail — extensions over a non-cofibrant quotient are not controlled by null-homotopies — so the **homotopy** pushout is non-negotiable.

The fiber sequence is the exact dual, and writing both is justified by the dual exactness it produces. The homotopy fiber $F_f$ is the homotopy pullback of $X \xrightarrow{f} Y \leftarrow *$ — "the part of $X$ that maps to the basepoint, fattened to be homotopy-invariant." Iterating the fiber construction loops back to $\Omega Y$ (the fiber of the fiber is the loop), giving the dual Puppe sequence
$$\cdots \to \Omega Y \xrightarrow{\partial} F_f \to X \xrightarrow{f} Y,$$
and applying the *covariant* $[Z, -]$ yields a long exact sequence
$$[Z, \Omega Y] \to [Z, F_f] \to [Z, X] \xrightarrow{f_*} [Z, Y].$$
One must define both because the two sequences answer genuinely different questions: $[-, Z]$ on a cofiber sequence computes maps *out of* the objects (cohomology-like), $[Z, -]$ on a fiber sequence computes maps *into* them (homotopy-like). The deep fact — that the two notions of "(co)fiber sequence" one can write down agree up to sign — is the content of [[Thm - The Puppe Cofiber and Fiber Sequences Agree]], and it is what lets a single category carry both exact sequences coherently.

---

# The Definition

Let $\mathcal{C}$ be a [[Def - Pointed Model Category Suspension and Loop|pointed model category]], $f : X \to Y$ a map of cofibrant objects (replace $X, Y$ by cofibrant models if needed).

**Homotopy cofiber.** The **homotopy cofiber** $C_f$ of $f$ is the [[Def - Pullback and Pushout|homotopy pushout]] of $* \xleftarrow{} X \xrightarrow{f} Y$; concretely, factor $f$ as a cofibration $X \rightarrowtail \widetilde{Y}$ followed by a weak equivalence, then take the strict pushout $C_f = * \cup_X \widetilde{Y}$. There is a canonical **connecting map** $\partial : C_f \to \Sigma X$ in $\mathrm{Ho}(\mathcal{C})$, obtained by identifying the cofiber of $i : Y \to C_f$ with the suspension $\Sigma X$.

**Cofiber sequence.** A **cofiber sequence** is a diagram in $\mathrm{Ho}(\mathcal{C})$ isomorphic to one of the form
$$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X$$
arising as above from some map $f$. Iterating yields the **Puppe sequence**
$$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{\partial} \Sigma X \xrightarrow{-\Sigma f} \Sigma Y \xrightarrow{-\Sigma i} \Sigma C_f \xrightarrow{-\Sigma\partial} \Sigma^2 X \to \cdots,$$
where each consecutive triple is again a cofiber sequence (the signs record that re-suspending introduces a sign, exactly as for triangulated categories).

**Homotopy fiber.** Dually, the **homotopy fiber** $F_f$ of $f$ is the [[Def - Pullback and Pushout|homotopy pullback]] of $X \xrightarrow{f} Y \xleftarrow{} *$; concretely, factor $f$ as a weak equivalence followed by a fibration $\widetilde{X} \twoheadrightarrow Y$, then take the strict pullback $F_f = * \times_Y \widetilde{X}$. There is a canonical connecting map $\partial : \Omega Y \to F_f$.

**Fiber sequence.** A **fiber sequence** is a diagram in $\mathrm{Ho}(\mathcal{C})$ isomorphic to one of the form
$$\Omega Y \xrightarrow{\partial} F_f \xrightarrow{p} X \xrightarrow{f} Y,$$
extending leftward to the dual Puppe sequence $\cdots \to \Omega^2 Y \to \Omega F_f \to \Omega X \to \Omega Y \to F_f \to X \to Y$.

**Long exact sequences.** For any object $Z$:

- Applying $[-, Z]$ to a cofiber sequence gives an **exact sequence of pointed sets**
$$\cdots \to [\Sigma X, Z] \to [C_f, Z] \xrightarrow{i^*} [Y, Z] \xrightarrow{f^*} [X, Z],$$
exact at every term, and a sequence of **groups** (abelian from $[\Sigma^2 X, Z]$ on) to the left of $[\Sigma X, Z]$.
- Applying $[Z, -]$ to a fiber sequence gives an **exact sequence of pointed sets**
$$[Z, \Omega Y] \to [Z, F_f] \xrightarrow{p_*} [Z, X] \xrightarrow{f_*} [Z, Y],$$
exact at every term, and groups to the left of $[Z, \Omega Y]$.

Here a sequence of pointed sets $A \xrightarrow{u} B \xrightarrow{v} C$ is **exact at $B$** if $u(A) = v^{-1}(*)$, the image of $u$ equals the preimage of the basepoint under $v$.

---

# Categorical / Structural Definition

A cofiber sequence is most cleanly described as a **homotopy-pushout square with a corner at the zero object**. The square
$$
\begin{array}{ccc}
X & \xrightarrow{\,f\,} & Y \\
\downarrow & & \downarrow i \\
* & \xrightarrow{} & C_f
\end{array}
$$
is a homotopy pushout, which is exactly the statement that $C_f$ is the universal homotopy-receiver of $Y$ that kills $X$. The connecting map and the suspension arise by **pasting** such squares: glue the cofiber square of $f$ to the cofiber square of $i$, and the outer rectangle is a homotopy pushout exhibiting $\Sigma X$ as the cofiber of $i$. This pasting lemma for homotopy pushouts is the structural engine of the Puppe sequence — the whole infinite sequence is a horizontal strip of homotopy-pushout squares, each sharing an edge with the next, with the bottom row constantly $*$. Dually a fiber sequence is a horizontal strip of homotopy-*pullback* squares with top row constantly $*$.

This packaging makes the exactness conceptual rather than computational. Exactness of $[-, Z]$ on a cofiber sequence is precisely the **universal property of the homotopy pushout** read in $\mathrm{Ho}(\mathcal{C})(-, Z)$: a map $Y \to Z$ extends to $C_f$ iff its composite with $f$ is the zero map (up to homotopy), which is the equality "image of $i^*$ = kernel of $f^*$." So the long exact sequence is not an extra theorem layered on top — it is the corepresentable image of the pushout's universal property, applied to each square in the strip. The forward link is that a [[Def - Pre-Triangulated Category|pre-triangulated category]] is precisely an axiomatization of "$\mathrm{Ho}(\mathcal{C})$ with these strips of squares," and a **triangulated category** is the further axiomatization once $\Sigma$ becomes invertible.

---

# Relate to Other Fields / Compression

In algebraic topology these are the most-used exact sequences in the subject. The cofiber sequence of an inclusion $A \hookrightarrow X$ of a [[Def - Cofibrant and Fibrant Objects|cofibration]], with $[-, Z]$ taken to be a cohomology theory $E^*$, *is* the long exact sequence of the pair $(X, A)$ in $E$-cohomology: $\cdots \to E^n(X/A) \to E^n(X) \to E^n(A) \to E^{n+1}(X/A) \to \cdots$, where the degree shift is the suspension. The fiber sequence of a [[Def - Cofibrant and Fibrant Objects|fibration]] $F \to E \to B$, with $[Z, -]$ taken to be [[Def - Higher Homotopy Group|homotopy groups]] $\pi_*$ (so $Z = S^n$), is the **long exact sequence of a fibration**: $\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(F) \to \cdots$, with the connecting map $\partial$ exactly the $\Omega B \to F$ above evaluated on spheres. Both classical sequences are single instances of the abstract construction.

**True name:** a cofiber sequence is the **homotopy cokernel done thrice** — map, its cofiber, and the connecting map to the suspension — and a fiber sequence is the **homotopy kernel done thrice**. The operative slogan is: *the cofiber of the cofiber is the suspension of the source* ($C_i \simeq \Sigma X$), and dually *the fiber of the fiber is the loop of the target* ($F_p \simeq \Omega Y$). Knowing this single identity lets you continue either sequence indefinitely without recomputing anything; it is why "three-term sequence" and "infinite sequence" are the same data.

The homological-algebra compression is the cleanest. In $\mathrm{Ch}(R)$ a map of complexes $f$ has a strict cokernel and kernel, but the homotopy-correct versions are the **mapping cone** $C_f$ and the **mapping cocone**, and the cofiber sequence $X \to Y \to C_f \to X[1]$ is exactly the **distinguished triangle** of the derived category $D(R)$. The connecting map $C_f \to X[1] = \Sigma X$ is the degree-shift connecting homomorphism, and applying $\mathrm{Hom}(-, Z)$ or homology recovers the **long exact sequence of Ext or of homology**. So a cofiber sequence is the general-model-category name for "the triangle a short exact sequence of complexes determines," and the agreement theorem below is the model-category source of the triangulated structure.

---

# Examples / Corollaries

**Is an instance — the cofiber sequence of $S^{n-1} \hookrightarrow D^n$.** In $\mathbf{Top}_*$, the inclusion of the boundary sphere into the disk has homotopy cofiber $D^n / S^{n-1} = S^n$. The cofiber sequence is $S^{n-1} \to D^n \to S^n \to \Sigma S^{n-1} = S^n$, and since $D^n \simeq *$, applying $[-, Z]$ recovers the suspension isomorphism $[S^n, Z] \cong [\Sigma S^{n-1}, Z]$. This is the bare-bones example that makes "cofiber of inclusion = quotient" concrete.

**Is an instance — the path-loop fibration.** In $\mathbf{Top}_*$, the path space $PY$ (paths starting at the basepoint) fibers over $Y$ by endpoint evaluation $PY \to Y$, with fiber the based loop space $\Omega Y$. Since $PY \simeq *$, the fiber sequence $\Omega Y \to PY \to Y$ and the covariant $[S^n, -]$ give the homotopy-group shift $\pi_n(\Omega Y) \cong \pi_{n+1}(Y)$ — the same adjunction shift, now seen as exactness of a fiber sequence with contractible total space.

**Is an instance — a short exact sequence of chain complexes.** A short exact sequence $0 \to X \xrightarrow{f} Y \to Q \to 0$ in $\mathrm{Ch}(R)$ with $f$ a cofibration (degreewise split mono with cofibrant cokernel) has homotopy cofiber $C_f \simeq Q$, and the cofiber sequence $X \to Y \to Q \xrightarrow{\partial} X[1]$ in $D(R)$ produces, via homology, the **long exact sequence in homology** with $\partial$ the snake-lemma connecting homomorphism. This is the example that ties the abstract connecting map to the one from a first homological-algebra course.

**Is NOT an instance — the strict quotient as cofiber.** For a non-cofibration $f : X \to Y$, the *strict* quotient $Y/f(X)$ is generally **not** the homotopy cofiber and does **not** sit in an exact sequence. Take $f : S^1 \to D^2$ the boundary inclusion but regarded as a map of spaces where $S^1$ is collapsed naively: the strict cokernel and the homotopy cofiber $S^2$ differ, and only the latter makes $[-, Z]$ exact. The repair is to replace $f$ by a cofibration first — exactly the cofibrant-replacement step the definition builds in.

**Is NOT an instance — a sequence that is exact only at the ends.** A diagram $X \to Y \to C$ where $C$ merely *contains* the strict cokernel but the square is not a homotopy pushout fails exactness at $[Y, Z]$: there can be maps $Y \to Z$ killing $X$ that do **not** extend over $C$, so $\mathrm{im}(i^*) \subsetneq \ker(f^*)$. Exactness is equivalent to the homotopy-pushout condition; a "long sequence" without the pushout squares is not a cofiber sequence.

**Calibration check.** Verify three things. First, that $[-, Z]$ applied to $X \xrightarrow{f} Y \xrightarrow{i} C_f$ is exact at $[Y, Z]$ by translating the homotopy-pushout universal property into "extends over $C_f$ iff null on $X$." Second, that the cofiber of $i : Y \to C_f$ is weakly equivalent to $\Sigma X$ (collapse $Y$ inside the mapping cone and watch the cone on $X$ become the suspension). Third, that for a fiber sequence $F \to E \to B$ with $E \simeq *$, the connecting map exhibits $F \simeq \Omega B$.

---

# Unlocked by This

> [!tip] Pre-Triangulated and Triangulated Categories *(from this chapter and the next)*
> A [[Def - Pre-Triangulated Category|pre-triangulated category]] is exactly the homotopy category $\mathrm{Ho}(\mathcal{C})$ equipped with $\Sigma \dashv \Omega$ and its classes of cofiber and fiber sequences, satisfying compatibility axioms abstracted from this page. When $\Sigma$ is moreover an equivalence, the cofiber sequences become the **distinguished triangles** of a **triangulated category** — the framework governing derived categories and the stable homotopy category. The connecting map $\partial : C_f \to \Sigma X$ is the rotation $X \to Y \to Z \to \Sigma X$ of a triangle.

> [!tip] Cohomology Theories and the Long Exact Sequence of a Pair *(from algebraic topology)*
> Any homotopy-invariant functor $[-, Z]$ (a **cohomology theory** when $Z$ ranges over a spectrum) turns every cofiber sequence into a long exact sequence; applied to inclusions of subcomplexes this is the long exact sequence of a pair, and applied to fibrations the long exact sequence of a fibration. The Eilenberg–Steenrod exactness axiom is precisely "send cofiber sequences to exact sequences."

> [!tip] The Snake Lemma and Derived Functors *(from homological algebra)*
> In $D(R)$ a cofiber sequence is a distinguished triangle, and applying a derived functor produces a long exact sequence whose connecting maps are the snake-lemma boundary maps. This is the structural reason **derived functors** come with long exact sequences at all — they are the images of cofiber sequences under an exact (triangulated) functor.
