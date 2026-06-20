---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Reedy Category and the Reedy Model Structure"
  - "Def - Pullback and Pushout"
  - "Def - Homotopy Limit and Colimit"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

(a) Show that the tower poset $\omega = (0 \to 1 \to 2 \to \cdots)$ is a [[Def - Reedy Category and the Reedy Model Structure|Reedy category]] with $\deg n = n$, all non-identity maps direct. Compute $L_n X$ and $M_n X$ for a diagram $X : \omega \to \mathcal{M}$, and identify the Reedy cofibrations. State what $\omega^{op}$ gives.

(b) Show that the cube poset $\underline{2}^{\,k} = (\{0,1\}^k, \le)$ — the indexing category of a $k$-cube — is Reedy with $\deg(\varepsilon) = \sum_i \varepsilon_i$ (the number of $1$'s) and all non-identity maps direct. For $k = 2$ (a commutative square $X : \underline{2}^2 \to \mathcal{M}$ with terminal vertex $X_{11}$) compute the matching object $M_{11} X$ and identify what Reedy fibrancy of the square means.

(c) In each case, state the consequence for [[Def - Homotopy Limit and Colimit|homotopy limits and colimits]]: when does the ordinary $\lim$ (resp. $\operatorname{colim}$) already compute the homotopy limit (resp. colimit)?

**Recall:**

A [[Def - Reedy Category and the Reedy Model Structure|Reedy category]] requires a degree function and direct/inverse subcategories with unique factorization. The latching object $L_r X$ is the colimit over non-identity direct maps into $r$ from lower degree; the matching object $M_r X$ is the limit over non-identity inverse maps out of $r$. A diagram is Reedy cofibrant when each latching map is a cofibration, Reedy fibrant when each matching map is a fibration.

For a Reedy shape $\mathcal{R}$, the homotopy colimit (resp. limit) of a diagram is the strict colimit (resp. limit) of its Reedy-cofibrant (resp. fibrant) replacement.

A [[Def - Pullback and Pushout|pullback]] of $B \to D \leftarrow C$ is the limit $B \times_D C$; a square is **homotopy cartesian** when the comparison map from the corner to the homotopy pullback is a weak equivalence.

---

# Convergent Strategy

**Problem class:** This is a "recognize a Reedy structure and read off the homotopy (co)limit consequence" problem, combining Legal Operations 1, 2, and the homotopy-(co)limit unlock from the topic page. The routine is to verify the Reedy axioms for a poset (where they are easy — posets have no non-trivial automorphisms and unique factorization is trivial when all maps are direct), compute the relevant latching/matching object, and then quote the principle that Reedy (co)fibrant replacement computes the homotopy (co)limit.

**Assumption pattern:** The asset is that $\omega$ and the cube are *posets*, so every hom-set has at most one element and the only factorization of any map is the trivial one. Declaring *all* non-identity maps direct (so $\mathcal{R}^{-} =$ identities) makes unique factorization automatic and the matching objects trivial, which is exactly the configuration suited to homotopy *colimits*; declaring all maps inverse suits homotopy *limits*.

**Theorem routing:** The Reedy verification feeds [[Thm - Diagrams over a Reedy Category Form a Model Category]], producing the Reedy model structure on $\mathcal{M}^{\omega}$ and $\mathcal{M}^{\underline{2}^k}$; the homotopy-(co)limit consequence is the standard application of that theorem to compute [[Def - Homotopy Limit and Colimit|holim and hocolim]].

**Key decision point:** The non-obvious choice is *which subcategory to make direct*. Making all maps direct ($\mathcal{R}^{-} =$ identities) kills the matching objects ($M_r X = *$), so every map is a Reedy fibration and the structure is tuned for cofibrant replacement and homotopy *colimits*. Making all maps inverse kills the latching objects and tunes for homotopy *limits*. For the cube, the same poset can be read either way; the correct reading depends on whether you want $\operatorname{hocolim}$ (a homotopy pushout, total cofibre) or $\operatorname{holim}$ (a homotopy pullback, total fibre).

---

# Legal Operations Used

1. **Operation 1 from the topic page (find the degree function and direct/inverse split).** We assign degree by position (for $\omega$) or by number of $1$'s (for the cube), and choose all non-identity maps direct or inverse depending on whether colimits or limits are wanted.

2. **Operation 2 from the topic page (compute a latching/matching object).** We evaluate $L_n X = X_{n-1}$ for the tower and $M_{11}X = X_{01}\times_{X_{00}} X_{10}$ for the square.

3. **Operation 5 from the topic page ((co)fibrantly replace before a homotopy invariant).** The homotopy (co)limit is the strict (co)limit *after* Reedy (co)fibrant replacement.

---

# Hints

> [!note]- Hint 1
> In $\omega$ with all maps direct, the matching category $\partial(n\downarrow\omega^{-})$ is empty (no non-identity inverse maps), so $M_n X = *$. The latching category $\partial(\omega^{+}\downarrow n)$ has a terminal object: the unique map $n-1 \to n$. A colimit over a category with a terminal object is the value at that terminal object, so $L_n X = X_{n-1}$.

> [!note]- Hint 2
> For the cube's terminal vertex $11$, the matching category $\partial(11 \downarrow (\underline{2}^2)^{-})$ (reading all maps inverse, for limits) consists of the two maps $11 \to 01$ and $11 \to 10$ and their common composite $11 \to 00$. The limit of this diagram is the pullback $X_{01} \times_{X_{00}} X_{10}$.

> [!note]- Hint 3
> Reedy fibrancy of the square at the top vertex says the matching map $X_{11} \to X_{01}\times_{X_{00}} X_{10}$ is a fibration; combined with fibrancy at the other vertices this is exactly the condition that the square is a homotopy pullback (homotopy cartesian) once the objects are fibrant.

---

# Solution

The plan: Step 1 handles the tower, computing $L_n X = X_{n-1}$ and $M_n X = *$ and identifying Reedy cofibrations as the levelwise-relative cofibrations; Step 2 handles the cube, computing the matching object at the top vertex as a pullback; Step 3 states the homotopy-(co)limit consequence in both cases.

**Step 1: The tower $\omega$ — latching $=$ previous stage, matching trivial.**

> [!note]- Derivation
> $\omega$ is a poset, so every hom-set has at most one element; unique factorization holds trivially with all non-identity maps in $\omega^{+}$ and $\omega^{-} = \{\text{identities}\}$. Degree-raising is clear ($m \to n$ exists iff $m \le n$). So $\omega$ is Reedy.
>
> *Matching.* The matching category at $n$ uses non-identity *inverse* maps out of $n$; there are none, so $M_n X = \lim_{\varnothing} = *$ (terminal object). Hence every relative matching map is $X_n \to Y_n \times_{*} M_n = X_n \to Y_n$ — wait, more precisely the relative matching map is $X_n \to Y_n \times_{M_n Y} M_n X = X_n \to Y_n$, so *Reedy fibrations of towers are exactly the levelwise fibrations*.
>
> *Latching.* The latching category at $n \ge 1$ has objects the non-identity direct maps into $n$, all of which factor through the unique map $n-1 \to n$; this category has $n-1 \to n$ as a terminal object, so the colimit is $L_n X = X_{n-1}$, and the latching map is the structure map $X_{n-1} \to X_n$. At $n = 0$ the latching category is empty: $L_0 X = \varnothing$.
>
> Therefore a map $f : X \to Y$ of towers is a **Reedy cofibration** iff the relative latching map $X_n \cup_{X_{n-1}} Y_{n-1} \to Y_n$ is a cofibration for all $n$ (with $X_0 \to Y_0$ a cofibration at the bottom) — i.e. each new stage is attached by a cofibration relative to the previous one. This is the correct notion for building a sequential **homotopy colimit**.
>
> Dually $\omega^{op}$ (all maps inverse) has $L_n X = *$ and $M_n X = X_{n+1}$; Reedy fibrations are the levelwise fibrations relative to the next stage, the correct notion for sequential **homotopy limits** (e.g. $\lim$ of a tower of fibrations).

**Step 2: The cube $\underline{2}^k$ — matching at the top vertex is a pullback.**

> [!note]- Derivation
> $\underline{2}^k$ is a poset with $\varepsilon \le \varepsilon'$ iff $\varepsilon_i \le \varepsilon'_i$ coordinatewise; degree $\deg(\varepsilon) = \sum_i \varepsilon_i$. A non-identity map $\varepsilon \to \varepsilon'$ has $\varepsilon < \varepsilon'$, raising degree, so taking all non-identity maps direct gives a Reedy structure (unique factorization trivial in a poset). It is also Reedy with all maps inverse, the reading suited to limits.
>
> For $k = 2$, read all maps inverse (limit reading). The terminal vertex is $11$ with $\deg 2$. The matching category $\partial(11 \downarrow (\underline{2}^2)^{-})$ has the two codimension-$1$ vertices $01, 10$ (via $11 \to 01$, $11 \to 10$) and the bottom vertex $00$ (via the composite), forming the cospan $01 \to 00 \leftarrow 10$. Hence
> $$M_{11} X = \lim\big(X_{01} \to X_{00} \leftarrow X_{10}\big) = X_{01} \times_{X_{00}} X_{10},$$
> the [[Def - Pullback and Pushout|pullback]] of the bottom three vertices. The matching map is the canonical map $X_{11} \to X_{01}\times_{X_{00}} X_{10}$ comparing the corner to the pullback.

**Step 3: Homotopy-(co)limit consequences.**

> [!note]- Derivation
> *Tower (colimit reading).* If $X : \omega \to \mathcal{M}$ is Reedy cofibrant — each map $X_{n-1} \to X_n$ a cofibration between cofibrant objects (a *cofibrant tower*) — then $\operatorname*{hocolim}_{\omega} X \simeq \operatorname*{colim}_{\omega} X$: the ordinary sequential colimit already computes the homotopy colimit. For a general tower one first Reedy-cofibrantly replaces (e.g. by a mapping-telescope construction) and then takes the colimit.
>
> *Tower (limit reading, $\omega^{op}$).* If $X : \omega^{op} \to \mathcal{M}$ is Reedy fibrant — a tower of fibrations between fibrant objects — then $\operatorname*{holim} X \simeq \lim X$: the ordinary inverse limit of a tower of fibrations is the homotopy limit. (This is the familiar fact that $\lim$ of a tower of fibrations is well-behaved while $\lim$ of a general tower needs $\lim^1$ corrections.)
>
> *Square (limit reading).* If $X : \underline{2}^2 \to \mathcal{M}$ is Reedy fibrant — all objects fibrant and the matching map $X_{11} \to X_{01}\times_{X_{00}} X_{10}$ a fibration, together with $X_{01}, X_{10} \to X_{00}$ fibrations — then the strict pullback computes the homotopy pullback, i.e. the square is **homotopy cartesian**. Dually, a Reedy-cofibrant square (with $X_{00} \to X_{01}, X_{10}$ cofibrations and the relative latching map a cofibration) has strict pushout equal to the homotopy pushout, i.e. it is **homotopy cocartesian**. This is the precise hypothesis under which Mayer–Vietoris squares behave.

> [!note]- Complete formal solution
> **(a)** $\omega$ is a poset, hence Reedy with all non-identity maps direct and trivial factorization. $M_n X = *$ (no inverse maps), so Reedy fibrations are levelwise fibrations; $L_n X = X_{n-1}$ (the latching category has terminal object $n-1 \to n$), $L_0 X = \varnothing$, so Reedy cofibrations are maps whose relative latching maps $X_n \cup_{X_{n-1}} Y_{n-1} \to Y_n$ are cofibrations. $\omega^{op}$ gives $L_n X = *$, $M_n X = X_{n+1}$, suited to homotopy limits.
>
> **(b)** $\underline{2}^k$ is a poset with degree $=$ number of $1$'s, Reedy with all non-identity maps direct (or all inverse). For $k=2$, reading all maps inverse, $M_{11} X = X_{01}\times_{X_{00}} X_{10}$, with matching map the comparison $X_{11}\to X_{01}\times_{X_{00}} X_{10}$.
>
> **(c)** A Reedy-cofibrant tower has $\operatorname{hocolim} = \operatorname{colim}$; a Reedy-fibrant tower (over $\omega^{op}$) has $\operatorname{holim} = \lim$; a Reedy-fibrant square is homotopy cartesian (strict pullback = homotopy pullback) and a Reedy-cofibrant square is homotopy cocartesian. In each case the ordinary (co)limit computes the homotopy (co)limit exactly when the diagram is Reedy (co)fibrant. $\blacksquare$

---

# Key Takeaways

**Choosing which maps are direct versus inverse is choosing whether you are computing a colimit or a limit.** A poset is Reedy in (at least) two ways: all non-identity maps direct, or all inverse. The first kills matching objects and is tuned for cofibrant replacement and homotopy *colimits*; the second kills latching objects and is tuned for fibrant replacement and homotopy *limits*. This is the operational heart of using Reedy categories to compute $\operatorname{hocolim}$ and $\operatorname{holim}$: the *same* indexing poset gives both, and you pick the reading matching your target. The trigger to internalize: "I want a homotopy colimit → make everything direct, replace cofibrantly, take colimit; I want a homotopy limit → make everything inverse, replace fibrantly, take limit."

**Reedy (co)fibrancy is exactly the condition under which the strict (co)limit is already correct.** The recurring theme of the whole chapter — resolve, then compute — specializes here to a sharp criterion: the ordinary $\lim$ or $\operatorname{colim}$ computes the homotopy version precisely when the diagram is Reedy fibrant or cofibrant. A tower of fibrations has the right $\lim$; a cofibrant tower has the right $\operatorname{colim}$; a homotopy-cartesian square has the right pullback. For a *general* diagram you must first Reedy-(co)fibrantly replace — the mapping telescope for towers, fibrant replacement of the corner for squares. This is why "homotopy pullback" and "homotopy pushout" are not the naive pullback and pushout: the naive ones are correct only after replacement, and the replacement is exactly making the relevant latching/matching map a (co)fibration.

**The matching object of a cube is a pullback, the latching object a pushout, which is why cubes encode (co)cartesianness and total (co)fibres.** Computing $M_{11}X = X_{01}\times_{X_{00}}X_{10}$ shows the matching map at the top vertex *is* the comparison map to the pullback, so Reedy fibrancy of a square *is* homotopy-cartesianness. This generalizes: for a $k$-cube the top-vertex matching object is the limit of the rest of the cube (the "total homotopy fibre" setup) and the bottom-vertex latching object is the colimit of the rest (the "total homotopy cofibre"), which is the foundation of Goodwillie's calculus of functors and of Mayer–Vietoris/Blakers–Massey arguments. The transferable recognition: whenever a homotopy pullback, homotopy pushout, total fibre, or total cofibre appears, you are looking at a matching or latching map of a cube, and the Reedy structure is the right tool. See [[Ex - Latching and matching objects for cosimplicial and simplicial objects]] for the analogous computation over $\Delta$ and $\Delta^{op}$.
