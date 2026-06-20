---
type: theorem
subject: model-categories
prereqs:
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Homotopy Function Complex"
  - "Def - Simplicial Set"
  - "Thm - Diagrams over a Reedy Category Form a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a [[Def - Model Category|model category]], $X, Y$ objects, $X^{\bullet}$ a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on (a cofibrant model of) $X$, and $Y_{\bullet}$ a [[Def - Cosimplicial and Simplicial Frame|simplicial frame]] on (a fibrant model of) $Y$. We write $\mathrm{map}^{\ell}(X,Y) = \mathcal{M}(X^{\bullet}, Y)$ and $\mathrm{map}^{r}(X,Y) = \mathcal{M}(X, Y_{\bullet})$ for the two one-sided [[Def - Homotopy Function Complex|homotopy function complexes]], both [[Def - Simplicial Set|simplicial sets]]. The bisimplicial set of the framing is $\mathrm{Map}(X^{\bullet}, Y_{\bullet})$ with $([m],[n]) \mapsto \mathcal{M}(X^m, Y_n)$, and $\mathrm{diag}$ takes its diagonal. The homotopy category of simplicial sets is $\mathrm{Ho}(\mathbf{sSet})$; $\simeq$ denotes weak equivalence of simplicial sets and $[X,Y] = \mathrm{Ho}(\mathcal{M})(X,Y)$. The full symbol registry is on [[Model Categories — Framings and Function Complexes]].

---

# Statement

> **Theorem (Framings compute function complexes).** Let $\mathcal{M}$ be a model category and $X, Y$ objects with $X$ cofibrant and $Y$ fibrant.
> 1. **(Kan complex.)** For any cosimplicial frame $X^{\bullet}$ on $X$, the simplicial set $\mathrm{map}^{\ell}(X, Y) = \mathcal{M}(X^{\bullet}, Y)$ is a **Kan complex**; dually $\mathrm{map}^{r}(X, Y) = \mathcal{M}(X, Y_{\bullet})$ is a Kan complex for any simplicial frame $Y_{\bullet}$.
> 2. **(Frame independence.)** Any two cosimplicial frames on $X$ yield weakly equivalent simplicial sets; likewise any two simplicial frames on $Y$. So each construction is well-defined in $\mathrm{Ho}(\mathbf{sSet})$.
> 3. **(Left equals right.)** There is a natural zig-zag of weak equivalences
> $$\mathrm{map}^{\ell}(X, Y) \;\xleftarrow{\ \sim\ }\; \mathrm{diag}\,\mathrm{Map}(X^{\bullet}, Y_{\bullet}) \;\xrightarrow{\ \sim\ }\; \mathrm{map}^{r}(X, Y),$$
> so both define the same object $\mathrm{map}(X, Y) \in \mathrm{Ho}(\mathbf{sSet})$.
> 4. **($\pi_0$ recovers the homotopy category.)** $\pi_0\,\mathrm{map}(X, Y) \cong [X, Y]$, and $\mathrm{map}(-, -)$ is a functor $\mathrm{Ho}(\mathcal{M})^{op} \times \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathbf{sSet})$ agreeing, when $\mathcal{M}$ is a simplicial model category, with the derived simplicial mapping object $\underline{\mathrm{Map}}(QX, RY)$.

The four parts together say: *every model category has a well-defined, frame-independent derived mapping space, computed by either cosimplicial or simplicial resolution, refining the hom-set of the homotopy category into a space.*

---

# Motivation

This theorem is what makes the homotopy function complex a *legitimate invariant* rather than an artifact of a choice. The construction of [[Def - Homotopy Function Complex|$\mathrm{map}(X,Y)$]] required choosing a frame, and frames are far from unique — they are cofibrant replacements, pinned down only up to weak equivalence. If the resulting simplicial set depended on the choice, $\mathrm{map}(X,Y)$ would carry no information beyond the arbitrary frame. The theorem removes the arbitrariness: any two frames give the same homotopy type, and moreover the cosimplicial (source-side) and simplicial (target-side) computations agree. The payoff is that $\mathrm{map}(X,Y)$ is an honest bifunctor into $\mathrm{Ho}(\mathbf{sSet})$ — the **derived hom** of the homotopy theory.

The conceptual importance is that it certifies the slogan "every model category is, up to homotopy, enriched over spaces." Quillen's homotopy category $\mathrm{Ho}(\mathcal{M})$ is enriched over *sets*; this theorem upgrades that to an enrichment over *homotopy types*, with $\mathrm{map}(X,Y)$ the hom-space and $\pi_0$ recovering the old hom-set. It is the bridge from $1$-categorical homotopy theory (Quillen's $\mathrm{Ho}$) to the $\infty$-categorical homotopy theory (mapping spaces of $\mathcal{M}[\mathcal{W}^{-1}]$): the function complex *is* the $\infty$-categorical hom, and this theorem is the proof that the strict point-set construction computes it correctly.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses are "$X$ cofibrant, $Y$ fibrant, and a frame chosen." Recognizing when a problem secretly supplies these is the skill.

The first disguised source is **a strict simplicial enrichment**. If $\mathcal{M}$ happens to be a simplicial model category, then $X \otimes \Delta^{\bullet}$ is *already* a cosimplicial frame, so part 4's compatibility statement applies and the homotopy function complex is the strict $\underline{\mathrm{Map}}(QX, RY)$. The non-obvious step is that the strict enrichment is *one particular frame*, so all the abstract framing theory specializes correctly. *Example problem:* in $\mathbf{sSet}$, deduce $\mathrm{map}(X,Y) \simeq Y^X$ for Kan $X, Y$ by recognizing $X \times \Delta^{\bullet}$ as the frame.

The second disguised source is **a chosen resolution from another theory**. A projective resolution in $\mathbf{Ch}(R)$, a cofibrant simplicial resolution of an algebra, a CW approximation in $\mathbf{Top}$ — each is (or yields) a frame. The non-obviousness is that "I already resolved $X$ for another purpose" means "I already have the frame I need to compute mapping spaces." *Example problem:* compute $\mathrm{map}(M, N)$ in $\mathbf{Ch}(R)$ from a projective resolution of $M$ and recover $\mathrm{Ext}$ groups as $\pi_*$.

The third disguised source is **the need to compare two model categories**. A Quillen equivalence induces weak equivalences of homotopy function complexes (because it preserves frames up to weak equivalence); so whenever you have a Quillen equivalence, you have an identification of all derived mapping spaces. The non-obvious recognition is that frame-independence (part 2) is exactly what lets a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] transport mapping spaces. *Example problem:* deduce that $|{-}| \dashv \mathrm{Sing}$ induces $\mathrm{map}_{\mathbf{Top}}(|X|, |Y|) \simeq \mathrm{map}_{\mathbf{sSet}}(X, Y)$.

**Targets (Output Amplification)**

The conclusion is a well-defined space $\mathrm{map}(X,Y)$. Combined with other facts it does much more.

Combine the conclusion with **a fibration $Y \twoheadrightarrow Z$**. Then $\mathrm{map}(X, -)$ sends it to a Kan fibration $\mathrm{map}(X, Y) \to \mathrm{map}(X, Z)$ (the function complex is a right Quillen functor in the second variable). The further result is the **long exact sequence of a fibration of mapping spaces**, the source of obstruction theory: lifting a map $X \to Z$ to $X \to Y$ is controlled by the fibre of this Kan fibration and its homotopy groups.

Combine the conclusion with **the simplicial model structure on $\mathbf{sSet}$**. Because $\mathrm{map}(X,Y)$ is a Kan complex, $\pi_n(\mathrm{map}(X,Y), f)$ are genuine homotopy groups; combined with composition $\mathrm{map}(Y,Z) \times \mathrm{map}(X,Y) \to \mathrm{map}(X,Z)$ they make $\mathrm{Ho}(\mathcal{M})$ into a category **enriched in $\mathrm{Ho}(\mathbf{sSet})$**, and refine to the underlying $\infty$-category. The further result is that derived mapping spaces compose homotopy-coherently — the substance of the $\infty$-categorical structure.

Combine the conclusion with **a homotopy (co)limit**. Since $\mathrm{map}(X, -)$ preserves homotopy limits and $\mathrm{map}(-, Y)$ takes homotopy colimits to homotopy limits, one gets formulas like $\mathrm{map}(\operatorname{hocolim}_i X_i, Y) \simeq \operatorname{holim}_i \mathrm{map}(X_i, Y)$. The further result is the standard descent / Mayer–Vietoris computations of mapping spaces, non-obvious because they convert a colimit in the source into a limit of spaces.

---

# Why Is It True

The whole theorem rests on a single observation: *a frame is a (co)fibrant object in a Reedy model structure, and applying a corepresentable to a (co)fibrant–fibrant pair lands in Kan complexes and respects weak equivalences.* Once you see that frames are Reedy (co)fibrant replacements ([[Thm - Diagrams over a Reedy Category Form a Model Category]]), every part follows from formal model-category reasoning.

For part 1 (Kan complex): a horn-filling problem $\Lambda^n_i \to \mathrm{map}^{\ell}(X,Y) = \mathcal{M}(X^{\bullet}, Y)$ transposes, by the corepresentable, into a lifting problem in $\mathcal{M}$ — extend a map defined on the "horn part" of $X^n$ to all of $X^n$, against $Y \to *$. Because $X^{\bullet}$ is Reedy cofibrant, the inclusion of the horn part of $X^n$ is a (trivial) cofibration; because $Y$ is fibrant, $Y \to *$ is a fibration; so the lift exists by MC4. Horn-filling against a fibrant target is exactly what makes a simplicial set a Kan complex.

> **The single mechanism: $\mathrm{map}^{\ell}(X,Y)_n = \mathcal{M}(X^n, Y)$ turns simplicial structure of the mapping space into the latching/cofibration structure of the frame, so "the mapping space is a Kan complex / frame-independent" becomes "the frame is Reedy cofibrant and $Y$ is fibrant" — the same cofibrant-source / fibrant-target pairing that governs homotopy.**

For part 2 (frame independence): any two cosimplicial frames on $X$ are two Reedy-cofibrant replacements of the same constant diagram $cX$, hence weakly equivalent in the Reedy structure by uniqueness of cofibrant replacement up to weak equivalence; applying $\mathcal{M}(-, Y)$ with $Y$ fibrant — a right Quillen functor — sends this weak equivalence of frames to a weak equivalence of Kan complexes. The same uniqueness-of-replacement argument that makes derived functors well-defined makes the function complex well-defined.

For part 3 (left = right): introduce the bisimplicial set $\mathrm{Map}(X^{\bullet}, Y_{\bullet})$, $\;([m],[n]) \mapsto \mathcal{M}(X^m, Y_n)$. Fixing the simplicial direction, each row $\mathcal{M}(X^{\bullet}, Y_n)$ is weakly equivalent to $\mathcal{M}(X^{\bullet}, Y) = \mathrm{map}^{\ell}$ because $Y_n \simeq Y$ (the frame is homotopically constant) and $X^{\bullet}$ is Reedy cofibrant; so the inclusion of the $0$th column $\mathrm{map}^{\ell} \to \mathrm{diag}$ is a weak equivalence by the realization (bisimplicial-diagonal) lemma. Symmetrically the other inclusion to $\mathrm{map}^{r}$ is a weak equivalence. The diagonal is the bridge.

For part 4 ($\pi_0$): a $0$-simplex of $\mathcal{M}(X^{\bullet}, Y)$ is a map $X^0 \to Y$, i.e. a map $X \to Y$ (up to the chosen models); a $1$-simplex is a map $X^1 \to Y$ out of the cylinder $X^1$, i.e. a **homotopy**. So path components are maps modulo homotopy, which is $[X,Y]$. The compatibility with simplicial enrichment is the source-side specialization noted above.

---

# What Makes This Hard

The conceptually subtle step is part 3, the comparison of the cosimplicial and simplicial computations via the bisimplicial diagonal: it requires the **realization lemma** (a levelwise weak equivalence of bisimplicial sets induces a weak equivalence on diagonals) together with the fact that *both* a frame's structure maps are weak equivalences *and* the frame is Reedy (co)fibrant — using only one of the two conditions is the standard error. The other trap is forgetting that $\mathrm{map}^{\ell}$ needs $X$ resolved *and* $Y$ fibrant: people compute $\mathcal{M}(X^{\bullet}, Y)$ for a non-fibrant $Y$ and get a simplicial set that is not a Kan complex and not frame-independent, exactly as $\mathbf{R}\mathrm{Hom}$ computed without a fibrant/injective target gives the wrong answer.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce everything to two facts about the Reedy structure on $\mathcal{M}^{\Delta}$: frames are Reedy-cofibrant replacements of $cX$, and the horn inclusions of $X^{\bullet}$ are (trivial) cofibrations. Then part 1 is horn-filling = MC4, part 2 is uniqueness of cofibrant replacement transported by a right Quillen functor, part 3 is the bisimplicial diagonal/realization lemma, part 4 is unwinding $0$- and $1$-simplices.

**Subgoal decomposition:**

1. **Horn parts of a frame are (trivial) cofibrations.** Show that for a cosimplicial frame $X^{\bullet}$, the inclusion of the latching-plus-horn data $\to X^n$ is a cofibration in $\mathcal{M}$, trivial for inner horns.
   - *Hint:* Reedy cofibrancy says each latching map $L_n X^{\bullet} \to X^n$ is a cofibration; the horn inclusions are built from these and from the weak-equivalence structure maps.
   - *Why needed:* It is the input to horn-filling in part 1.

2. **$\mathrm{map}^{\ell}(X,Y)$ is a Kan complex.** Transpose horn-filling to a lifting problem in $\mathcal{M}$ and solve by MC4.
   - *Hint:* A horn $\Lambda^n_i \to \mathcal{M}(X^{\bullet}, Y)$ transposes to extending a map off the horn-part of $X^n$ to $X^n$, against $Y \to *$.
   - *Why needed:* It makes the function complex a legitimate homotopy type.

3. **Frame independence.** Show two frames are weakly equivalent Reedy-cofibrant replacements and that $\mathcal{M}(-, Y)$ preserves the weak equivalence.
   - *Hint:* Cofibrant replacements of $cX$ are unique up to weak equivalence between cofibrant objects; $\mathcal{M}(-, Y)$ for fibrant $Y$ is a right Quillen functor, so it preserves such weak equivalences (Ken Brown's lemma).
   - *Why needed:* It makes $\mathrm{map}(X,Y)$ well-defined in $\mathrm{Ho}(\mathbf{sSet})$.

4. **Left equals right.** Form the bisimplicial set and apply the realization lemma to both column/row inclusions.
   - *Hint:* Each row $\mathcal{M}(X^{\bullet}, Y_n) \simeq \mathrm{map}^{\ell}$ since $Y_n \simeq Y$; each column $\mathcal{M}(X^m, Y_{\bullet}) \simeq \mathrm{map}^{r}$ since $X^m \simeq X$; diagonals of levelwise-equivalent bisimplicial sets are equivalent.
   - *Why needed:* It identifies the two constructions, giving a single $\mathrm{map}(X,Y)$.

5. **$\pi_0$ and functoriality.** Identify $0$-simplices with maps and $1$-simplices with homotopies; check bifunctoriality.
   - *Hint:* $X^0 \simeq X$, $X^1$ is a cylinder; path-connectedness in the function complex is the homotopy relation.
   - *Why needed:* It anchors the function complex to the known homotopy category.

---

# Lemma Decomposition

> [!note]- Lemma 1: Corepresentable of a Reedy-cofibrant frame against a fibrant object is a Kan complex
> **Statement:** If $X^{\bullet}$ is a cosimplicial frame and $Y$ is fibrant, then $\mathcal{M}(X^{\bullet}, Y)$ is a Kan complex.
>
> **Hint:** Transpose a horn-filling problem into a lifting problem in $\mathcal{M}$; the horn inclusion of the frame is a trivial cofibration and $Y \to *$ is a fibration.
>
> **Why needed:** It is part 1; without it the function complex is not a homotopy type.
>
> > [!note]- Full proof
> > A simplicial set $K$ is a Kan complex iff every horn $\Lambda^n_i \to K$ ($0 \le i \le n$, $n \ge 1$) extends to $\Delta^n \to K$. For $K = \mathcal{M}(X^{\bullet}, Y)$, by the [[Def - Simplicial Set|Yoneda]]/adjunction identification $\mathbf{sSet}(\Delta^n, K) = K_n = \mathcal{M}(X^n, Y)$ and $\mathbf{sSet}(\Lambda^n_i, K) = \mathcal{M}(\mathrm{colim}\, X^{\bullet}|_{\Lambda^n_i}, Y) = \mathcal{M}(X^n_{\Lambda^n_i}, Y)$, where $X^n_{\Lambda^n_i}$ is the "horn part" of $X^n$ (the colimit of the frame over the simplices of $\Lambda^n_i$). The horn-filling problem becomes the lifting problem in $\mathcal{M}$
> > $$\begin{array}{ccc} X^n_{\Lambda^n_i} & \longrightarrow & Y \\ \downarrow & & \downarrow \\ X^n & \longrightarrow & * \end{array}$$
> > The left map is the inclusion of the horn part. By Reedy cofibrancy of $X^{\bullet}$ this inclusion is a cofibration, and because every structure map of a frame is a weak equivalence it is in fact a *trivial* cofibration (the horn part is weakly equivalent to $X^n$). The right map $Y \to *$ is a fibration since $Y$ is fibrant. By MC4 the lift exists, filling the horn. Hence $K$ is a Kan complex.

> [!note]- Lemma 2: Frames are cofibrant replacements of the constant diagram, unique up to weak equivalence
> **Statement:** A cosimplicial frame on $X$ is a Reedy-cofibrant object $X^{\bullet}$ with a Reedy weak equivalence $X^{\bullet} \xrightarrow{\sim} cX$; any two are connected by a weak equivalence of Reedy-cofibrant objects.
>
> **Hint:** This is uniqueness of cofibrant replacement in the Reedy model structure of [[Thm - Diagrams over a Reedy Category Form a Model Category]].
>
> **Why needed:** It is the engine of frame independence (part 2).
>
> > [!note]- Full proof
> > By [[Thm - Diagrams over a Reedy Category Form a Model Category]], $\mathcal{M}^{\Delta}$ has the Reedy model structure, in which $cX$ is an object. A cosimplicial frame is exactly a cofibrant object $X^{\bullet}$ with a weak equivalence (here a Reedy weak equivalence, i.e. objectwise) to $cX$ — a cofibrant replacement of $cX$. Given two cofibrant replacements $X^{\bullet} \xrightarrow{\sim} cX \xleftarrow{\sim} X'^{\bullet}$, lift $\mathrm{id}_{cX}$ along the trivial fibration part of a factorization to obtain a weak equivalence $X^{\bullet} \to X'^{\bullet}$ between cofibrant objects (standard: cofibrant replacements of an object are unique up to weak equivalence, by lifting against the trivial fibration $X'^{\bullet} \xrightarrow{\sim} cX$). This is the required comparison.

> [!note]- Lemma 3: A right Quillen functor preserves weak equivalences between cofibrant objects (Ken Brown)
> **Statement:** Applying $\mathcal{M}(-, Y)$ (for $Y$ fibrant) to a weak equivalence between Reedy-cofibrant cosimplicial objects yields a weak equivalence of Kan complexes.
>
> **Hint:** $\mathcal{M}(-, Y) : (\mathcal{M}^{\Delta})^{op} \to \mathbf{sSet}$ is (right) Quillen; invoke Ken Brown's lemma.
>
> **Why needed:** It transports the frame comparison of Lemma 2 into a comparison of function complexes, completing part 2.
>
> > [!note]- Full proof
> > The functor $X^{\bullet} \mapsto \mathcal{M}(X^{\bullet}, Y)$ sends colimits to limits and, for fibrant $Y$, sends Reedy (trivial) cofibrations to (trivial) Kan fibrations of simplicial sets — this is the adjunction transpose of the SM7-type condition, and is exactly the statement that $(-) \mapsto \mathcal{M}(-, Y)$ is right Quillen from the opposite Reedy structure. By Ken Brown's lemma a right Quillen functor preserves all weak equivalences between fibrant objects of its source — here the source is $(\mathcal{M}^{\Delta})^{op}$, whose fibrant objects are the Reedy-cofibrant cosimplicial objects. Hence a weak equivalence between Reedy-cofibrant frames is sent to a weak equivalence of (Kan, by Lemma 1) simplicial sets.

> [!note]- Lemma 4: Bisimplicial diagonal comparison (realization lemma)
> **Statement:** The inclusions $\mathrm{map}^{\ell}(X,Y) \to \mathrm{diag}\,\mathrm{Map}(X^{\bullet}, Y_{\bullet}) \leftarrow \mathrm{map}^{r}(X,Y)$ are weak equivalences.
>
> **Hint:** Each row and each column of the bisimplicial set $\mathcal{M}(X^m, Y_n)$ is a weak equivalence onto the corresponding one-sided complex because frame structure maps are weak equivalences; apply the realization lemma.
>
> **Why needed:** It is part 3, identifying the cosimplicial and simplicial computations.
>
> > [!note]- Full proof
> > Consider $B_{m,n} = \mathcal{M}(X^m, Y_n)$. Fix $n$: the simplicial set $m \mapsto \mathcal{M}(X^m, Y_n)$ is $\mathrm{map}^{\ell}(X, Y_n)$, and since the coaugmentation $Y \xrightarrow{\sim} Y_n$ is a weak equivalence between fibrant objects, $\mathrm{map}^{\ell}(X, Y_n) \simeq \mathrm{map}^{\ell}(X, Y)$ by Lemma 3 (applied in the second variable). So the bisimplicial set $B$ has each row weakly equivalent to the constant value $\mathrm{map}^{\ell}(X,Y)$. The **realization lemma** states that if a map of bisimplicial sets is a levelwise weak equivalence in one direction, the induced map on diagonals is a weak equivalence; applying it to the inclusion of the constant row $\mathrm{map}^{\ell}(X,Y) \hookrightarrow B$ (more precisely, the projection $\mathrm{diag}\,B \to \mathrm{map}^{\ell}(X,Y)$ induced by $Y_{\bullet} \to Y_0 \simeq Y$) gives $\mathrm{diag}\,B \simeq \mathrm{map}^{\ell}(X,Y)$. The same argument in the other variable (columns, using $X^m \simeq X$) gives $\mathrm{diag}\,B \simeq \mathrm{map}^{r}(X,Y)$. Composing the two equivalences with the diagonal as the common object gives the zig-zag.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be cofibrant, $Y$ fibrant, $X^{\bullet}$ a cosimplicial frame on $X$, $Y_{\bullet}$ a simplicial frame on $Y$.
>
> **Step 0 — frames exist.** By [[Thm - Diagrams over a Reedy Category Form a Model Category]] the Reedy model structures on $\mathcal{M}^{\Delta}$ and $\mathcal{M}^{\Delta^{op}}$ exist, so $cX$ has a Reedy-cofibrant replacement (a cosimplicial frame) and $cY$ a Reedy-fibrant replacement (a simplicial frame). All four simplicial sets below are therefore defined.
>
> **Step 1 — Kan complex (part 1).** By Lemma 1, $\mathrm{map}^{\ell}(X,Y) = \mathcal{M}(X^{\bullet}, Y)$ is a Kan complex. Dualizing (work in $\mathcal{M}^{op}$, where a simplicial frame on $Y$ is a cosimplicial frame and $X$ cofibrant becomes fibrant), $\mathrm{map}^{r}(X,Y) = \mathcal{M}(X, Y_{\bullet})$ is a Kan complex.
>
> **Step 2 — frame independence (part 2).** By Lemma 2 any two cosimplicial frames on $X$ are connected by a weak equivalence of Reedy-cofibrant objects; by Lemma 3, $\mathcal{M}(-, Y)$ sends it to a weak equivalence of Kan complexes. So $\mathrm{map}^{\ell}(X,Y)$ is independent of the frame in $\mathrm{Ho}(\mathbf{sSet})$. Dually for $\mathrm{map}^{r}$.
>
> **Step 3 — left equals right (part 3).** By Lemma 4 the bisimplicial set $B_{m,n} = \mathcal{M}(X^m, Y_n)$ has diagonal weakly equivalent to both $\mathrm{map}^{\ell}(X,Y)$ and $\mathrm{map}^{r}(X,Y)$, giving the natural zig-zag
> $$\mathrm{map}^{\ell}(X, Y) \xleftarrow{\sim} \mathrm{diag}\,B \xrightarrow{\sim} \mathrm{map}^{r}(X, Y).$$
> Define $\mathrm{map}(X,Y) \in \mathrm{Ho}(\mathbf{sSet})$ to be this common object.
>
> **Step 4 — $\pi_0$ and functoriality (part 4).** A $0$-simplex of $\mathcal{M}(X^{\bullet}, Y)$ is a map $X^0 \to Y$; since $X^0 \simeq X$ and $X$ is cofibrant, $Y$ fibrant, these represent elements of $[X,Y]$. A $1$-simplex is a map $X^1 \to Y$ from the cylinder object $X^1$, i.e. a left homotopy; two $0$-simplices are in the same path component iff connected by such a homotopy. Hence $\pi_0\,\mathrm{map}(X,Y) = \mathcal{M}(X,Y)/\!\simeq\, = [X,Y]$. Functoriality in both variables follows from functoriality of frames (or from frame-independence, allowing any functorial choice); when $\mathcal{M}$ is simplicial, $X \otimes \Delta^{\bullet}$ is a frame and $\mathcal{M}(X \otimes \Delta^{\bullet}, Y) = \underline{\mathrm{Map}}(X, Y)$ by the tensor-cotensor adjunction, giving the compatibility.
>
> **Conclusion.** All four parts hold, so framings compute a well-defined homotopy function complex $\mathrm{map}(X,Y)$ refining $[X,Y]$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Ext groups as homotopy groups of a function complex.** In $\mathbf{Ch}(R)$, take $M$ with a projective resolution as the frame and $N$ fibrant; the theorem yields $\pi_n \mathrm{map}(M, N) \cong \mathrm{Ext}^{-n}_R(M, N)$. The application is non-obvious because it identifies the *homotopy groups of a space* with the classical derived functors $\mathrm{Ext}$ — the function complex is the space-level $\mathbf{R}\mathrm{Hom}$.

**Obstruction theory via the fibration $\mathrm{map}(X, Y) \to \mathrm{map}(X, Z)$.** Given a fibration $Y \twoheadrightarrow Z$ in $\mathbf{Top}$, the induced Kan fibration of function complexes has a long exact sequence in homotopy whose connecting maps are the obstruction classes to lifting $X \to Z$ through $Y$. Recognizing the lifting problem as a $\pi_0$-surjectivity question for this Kan fibration is the bridge to classical obstruction theory.

**Comparing homotopy theories via Quillen equivalence.** A [[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]] $F \dashv U$ induces weak equivalences $\mathrm{map}_{\mathcal{N}}(FX, Y) \simeq \mathrm{map}_{\mathcal{M}}(X, UY)$ on all derived mapping spaces, because $F$ carries a frame on $X$ to a frame on $FX$. Applying this to $|{-}| \dashv \mathrm{Sing}$ shows topological and simplicial mapping spaces agree up to weak equivalence — a non-obvious transport of the *entire* mapping space, not just its $\pi_0$.

---

# Bridges

- **[[Thm - Diagrams over a Reedy Category Form a Model Category]]** — the foundation. That theorem supplies the Reedy model structures on $\mathcal{M}^{\Delta}$ and $\mathcal{M}^{\Delta^{op}}$ in which frames are (co)fibrant replacements of constant diagrams; this theorem consumes those frames to build and compare homotopy function complexes. The relationship is exactly that of "model structure on diagrams" to "the derived mapping space it computes."

- **[[Thm - The Homotopy Category of a Model Category]]** — the $\pi_0$ shadow. Where that theorem computes the hom-*set* $[X,Y] = \pi(QX, RY)$ via bifibrant replacement and a single cylinder, this theorem computes the hom-*space* $\mathrm{map}(X,Y)$ via a whole frame, and part 4 shows the former is the $\pi_0$ of the latter. The function complex is the homotopy-category hom with its higher structure restored.

- **[[Def - Quillen Adjunction and Quillen Equivalence|Quillen equivalence]]** — the comparison tool. A Quillen equivalence preserves frames up to weak equivalence and hence induces weak equivalences on all homotopy function complexes; this is the precise sense in which Quillen-equivalent model categories "have the same mapping spaces," refining "the same homotopy category."

- **The Dwyer–Kan simplicial localization** — the alternative construction. The hammock localization $L^H\mathcal{M}$ assigns to $X, Y$ a simplicial mapping set $L^H\mathcal{M}(X,Y)$ weakly equivalent to $\mathrm{map}(X,Y)$; the agreement of framings with the simplicial localization is the statement that the homotopy function complex is intrinsic to the homotopy theory, computable by resolving objects (framings) or by resolving morphisms (hammocks).

---

# Unlocked by This

> [!tip] Model Categories Present ∞-Categories *(from Higher Category Theory)*
> Part 4 — that $\mathrm{map}(X,Y)$ is a well-defined Kan complex with $\pi_0 = [X,Y]$, composing homotopy-coherently — is exactly the data of the **∞-category** $\mathcal{M}[\mathcal{W}^{-1}]$ underlying $\mathcal{M}$: its objects are those of $\mathcal{M}$ and its mapping spaces are the homotopy function complexes. This theorem is the proof that a model category presents an ∞-category, the foundational fact of **higher algebra**.

> [!tip] Mapping Space Spectral Sequences *(from Stable Homotopy Theory)*
> The Kan-fibration behavior of $\mathrm{map}(X, -)$ along a tower gives the **Bousfield–Kan / Federer spectral sequence** computing $\pi_* \mathrm{map}(X, Y)$ from cohomology, and along a cosimplicial resolution the **Tot spectral sequence**. The derived mapping space is the home of all "homotopy groups of a space of maps" computations.

> [!tip] Derived Hom, Ext, and the Derived Category *(from Homological Algebra)*
> For chain complexes the homotopy function complex is the space-level **$\mathbf{R}\mathrm{Hom}$**, with $\pi_*$ the $\mathrm{Ext}$ groups; passing to $\mathrm{Ho}$ recovers morphisms in the **derived category**. This theorem is the model-categorical proof that derived hom is well-defined and resolution-independent, the homotopical generalization of "$\mathrm{Ext}$ does not depend on the resolution."
