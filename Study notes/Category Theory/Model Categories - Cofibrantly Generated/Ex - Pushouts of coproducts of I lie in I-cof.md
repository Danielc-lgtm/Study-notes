---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Relative Cell Complex"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Pullback and Pushout"
  - "Def - Transfinite Composition and Smallness"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{C}$ be cocomplete and $I$ a set of maps. Prove that the class $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ is **saturated**: it contains all isomorphisms and is closed under

(a) pushout (the pushout of an $I$-cofibration along any map is an $I$-cofibration),

(b) coproduct (a coproduct of $I$-cofibrations is an $I$-cofibration),

(c) transfinite composition (a transfinite composite of $I$-cofibrations is an $I$-cofibration),

(d) retract (a retract of an $I$-cofibration is an $I$-cofibration).

Deduce that every relative $I$-cell complex is an $I$-cofibration, i.e. $I\text{-cell}\subseteq I\text{-cof}$. (No smallness hypothesis is needed for any of this.)

**Recall:**

A map $i$ has the **left lifting property** (LLP) against $p$ if every commuting square with $i$ on the left and $p$ on the right has a diagonal filler. $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$ where $I\text{-inj} = \mathrm{RLP}(I)$.

![[Def - Relative Cell Complex#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a closure-property problem — establishing that a lifting class is stable under the cell operations, which is what lets a set of generators control a whole class. It is the formal backbone behind "$I\text{-cell}\subseteq I\text{-cof}$" used everywhere else.

**Assumption pattern:** The only assumption is that $I\text{-cof}$ is defined as an LLP-class, $\mathrm{LLP}(I\text{-inj})$. Every closure property follows from a single principle: the LLP against a *fixed* map (hence against a fixed class) is preserved by colimit constructions on the source side, because a lifting problem for the colimit can be solved by solving lifting problems for the pieces and assembling.

**Theorem routing:** Each part is a diagram chase: given a lifting square against an arbitrary $p\in I\text{-inj}$, use the universal property of the relevant colimit (pushout, coproduct, transfinite composite) to reduce to lifting the constituent $I$-cofibrations, which lift by hypothesis, then assemble the lifts. Retract closure is the standard paste-and-restrict argument.

**Key decision point:** The non-obvious recognition is that *all four* closures are instances of one fact — "$\mathrm{LLP}(S)$ is saturated for any class $S$" — and that none requires anything about $I$ beyond its being a class to take RLP against. In particular smallness is irrelevant here; it enters only when one wants the *converse* description (retracts of cell complexes), via the small object argument.

---

# Legal Operations Used

1. **Operation 6 from the topic page (close $I\text{-cof}$ under structural operations).** This exercise *proves* that operation: it establishes the four closure properties that make $I\text{-cof}$ saturated.

2. **Operation 1 from the topic page (form the closures of a set).** The class in question is $I\text{-cof} = \mathrm{LLP}(I\text{-inj})$, and the exercise shows it is closed under the cell-building operations, so it contains $I\text{-cell}$.

---

# Hints

> [!note]- Hint 1 (general principle)
> For any class $S$, a map is in $\mathrm{LLP}(S)$ iff it lifts against every $p\in S$. So to prove closure of $\mathrm{LLP}(S)$ under an operation, fix an arbitrary $p\in S$ and show the operation's output lifts against $p$, given that its inputs do.

> [!note]- Hint 2 (pushout)
> Let $g$ be the pushout of $i\in I\text{-cof}$ along $u$. A lifting square for $g$ against $p$ restricts, via the pushout corner, to a lifting square for $i$ against $p$; lift that (since $i\in I\text{-cof}$), and the universal property of the pushout assembles the lift for $g$.

> [!note]- Hint 3 (coproduct)
> A lifting square for $\coprod_k i_k$ against $p$ is, by the universal property of the coproduct, a family of lifting squares for the $i_k$; lift each (since $i_k\in I\text{-cof}$) and take the induced map out of the coproduct.

> [!note]- Hint 4 (transfinite composition)
> Build the lift stage by stage along the tower by transfinite induction: at successors extend the lift across the next $I$-cofibration; at limits use the universal property of the colimit to assemble. The compatibility at each stage is what makes the limit assembly work.

> [!note]- Hint 5 (retract)
> If $f$ is a retract of $g\in I\text{-cof}$, paste the retract diagram onto a lifting square for $f$ to get one for $g$, lift it, then restrict the lift back along the retraction.

---

# Solution

The proof is a sequence of diagram chases, all instances of one principle: lifting against a fixed $p\in I\text{-inj}$ is preserved by source-side colimits and by retracts. Step 1 handles pushout, Step 2 coproduct, Step 3 transfinite composition, Step 4 retract; Step 5 assembles them to get $I\text{-cell}\subseteq I\text{-cof}$.

**Step 1 (a): Closure under pushout.**

> [!note]- Derivation
> Let $i : A\to B$ be in $I\text{-cof}$ and form the pushout of $i$ along $u : A\to X$:
> $$\begin{array}{ccc} A & \xrightarrow{u} & X \\ {\scriptstyle i}\downarrow & & \downarrow{\scriptstyle g} \\ B & \xrightarrow{\bar u} & X\sqcup_A B \end{array}$$
> so $g : X\to X\sqcup_A B$ is the pushout map. Fix $p : E\to F$ in $I\text{-inj}$ and a lifting square for $g$ against $p$: maps $a : X\to E$, $b : X\sqcup_A B\to F$ with $p a = b g$. Precompose with the pushout: $(a u, b\bar u)$ is a lifting square for $i$ against $p$ (check: $p(au) = (pa)u = (bg)u = b(\bar u i) = (b\bar u) i$). Since $i\in I\text{-cof}$ and $p\in I\text{-inj}$, there is $h : B\to E$ with $h i = a u$ and $p h = b\bar u$. Now $a : X\to E$ and $h : B\to E$ agree on $A$ ($au = hi$), so by the universal property of the pushout they induce $\ell : X\sqcup_A B\to E$ with $\ell g = a$ and $\ell\bar u = h$. Then $\ell$ is the diagonal lift for the $g$-square: $\ell g = a$ and $p\ell = b$ (the latter checked on the two pushout legs: $p\ell g = pa = bg$ and $p\ell\bar u = ph = b\bar u$, so $p\ell = b$ by universality). Hence $g\in I\text{-cof}$.

**Step 2 (b): Closure under coproduct.**

> [!note]- Derivation
> Let $\{i_k : A_k\to B_k\}_{k\in T}$ be in $I\text{-cof}$ and form $\coprod i_k : \coprod A_k\to\coprod B_k$. Fix $p\in I\text{-inj}$ and a lifting square: $a : \coprod A_k\to E$, $b : \coprod B_k\to F$ with $p a = b(\coprod i_k)$. By the universal property of the coproduct, $a = \langle a_k\rangle$ and $b = \langle b_k\rangle$ with $(a_k, b_k)$ a lifting square for each $i_k$. Each lifts to $h_k : B_k\to E$ with $h_k i_k = a_k$, $p h_k = b_k$ (since $i_k\in I\text{-cof}$). The induced map $\langle h_k\rangle : \coprod B_k\to E$ satisfies $\langle h_k\rangle(\coprod i_k) = a$ and $p\langle h_k\rangle = b$. So $\coprod i_k\in I\text{-cof}$.

**Step 3 (c): Closure under transfinite composition.**

> [!note]- Derivation
> Let $Z_0\to Z_1\to\cdots$ be a $\lambda$-sequence with each $Z_\beta\to Z_{\beta+1}$ in $I\text{-cof}$, transfinite composite $g : Z_0\to Z_\lambda$. Fix $p\in I\text{-inj}$ and a lifting square $a : Z_0\to E$, $b : Z_\lambda\to F$ with $pa = bg$. Build lifts $\ell_\beta : Z_\beta\to E$ by transfinite induction with $p\ell_\beta = b|_{Z_\beta}$ and $\ell_\beta$ compatible along the tower. Base: $\ell_0 = a$. Successor: given $\ell_\beta$, the square $(\ell_\beta, b|_{Z_{\beta+1}})$ for $Z_\beta\to Z_{\beta+1}$ against $p$ lifts (that map is in $I\text{-cof}$), giving $\ell_{\beta+1}$ extending $\ell_\beta$. Limit $\gamma$: the compatible family $\{\ell_\beta\}_{\beta<\gamma}$ induces $\ell_\gamma : Z_\gamma = \mathrm{colim}_{\beta<\gamma}Z_\beta\to E$ by the universal property, with $p\ell_\gamma = b|_{Z_\gamma}$. At $\beta = \lambda$ this yields $\ell_\lambda : Z_\lambda\to E$ with $\ell_\lambda g = a$ and $p\ell_\lambda = b$. So $g\in I\text{-cof}$.

**Step 4 (d): Closure under retract.**

> [!note]- Derivation
> Let $f$ be a retract of $g\in I\text{-cof}$: there are arrow-category maps $f\to g\to f$ with composite the identity, i.e. squares
> $$\begin{array}{ccccc} X & \xrightarrow{s} & X' & \xrightarrow{r} & X \\ {\scriptstyle f}\downarrow & & {\scriptstyle g}\downarrow & & \downarrow{\scriptstyle f} \\ Y & \xrightarrow{s'} & Y' & \xrightarrow{r'} & Y \end{array}$$
> with $rs = \mathrm{id}_X$, $r's' = \mathrm{id}_Y$. Fix $p\in I\text{-inj}$ and a lifting square $a : X\to E$, $b : Y\to F$ for $f$. Then $(a r, b r')$ is a lifting square for $g$: $p(ar) = (pa)r = (bf)r = b(r'g) = (br')g$. Lift: $h : X'\to E$ with $hg = ar$, $ph = br'$. Set $\ell = h s' : Y\to E$. Then $\ell f = h s' f = h g s = a r s = a$ (using $s' f = g s$ and $rs = \mathrm{id}$) and $p\ell = p h s' = b r' s' = b$ (using $r's' = \mathrm{id}$). So $\ell$ lifts the $f$-square, and $f\in I\text{-cof}$.

**Step 5: $I\text{-cell}\subseteq I\text{-cof}$.**

> [!note]- Derivation
> Each generator $i\in I$ lies in $I\text{-cof}$: by definition of $I\text{-inj} = \mathrm{RLP}(I)$, every $p\in I\text{-inj}$ lifts against $i$, so $i\in\mathrm{LLP}(I\text{-inj}) = I\text{-cof}$. A relative $I$-cell complex is a transfinite composite (Step 3) of pushouts (Step 1) of coproducts (Step 2) of maps of $I$. Each operation preserves membership in $I\text{-cof}$, so every relative cell complex is an $I$-cofibration: $I\text{-cell}\subseteq I\text{-cof}$. Isomorphism-containment is the empty (length-$0$) cell complex case. No smallness was used.

> [!note]- Complete formal solution
> For any class $S$, $\mathrm{LLP}(S)$ is saturated. Fix $p\in S$ throughout. **Pushout:** a lifting square for the pushout map restricts to one for the original via the pushout corner; lift and reassemble by the pushout's universal property. **Coproduct:** a lifting square for $\coprod i_k$ decomposes into squares for each $i_k$; lift componentwise and use the coproduct's universal property. **Transfinite composition:** build the lift by induction — extend across each successor $I$-cofibration, assemble at limits by the colimit's universal property. **Retract:** paste the retract maps onto an $f$-square to get a $g$-square, lift it, restrict back via the section. Each generator lies in $\mathrm{LLP}(\mathrm{RLP}(I)) = I\text{-cof}$, and a relative cell complex is a transfinite composite of pushouts of coproducts of generators, so by the four closures $I\text{-cell}\subseteq I\text{-cof}$. No smallness is required. $\blacksquare$

---

# Key Takeaways

**Every lifting class is saturated, and this single fact powers all of cofibrant generation.** The four closure properties are not four separate theorems but one: $\mathrm{LLP}(S)$ is preserved by source-side colimits (pushout, coproduct, transfinite composite) and by retract, for *any* class $S$, by solving the colimit's lifting problem piece by piece. This is what lets a *set* $I$ control the *class* $I\text{-cof}$ — you build cofibrations by gluing generators and the result stays a cofibration automatically. The trigger to invoke saturation: any time you have constructed a map by a colimit of cofibrations and need to know the result is a cofibration. The dual statement — $\mathrm{RLP}(S)$ is closed under pullback, product, and retract — powers the corresponding facts for fibrations.

**Smallness is conspicuously absent here, and knowing that sharpens its role.** Not one of the closure properties, nor $I\text{-cell}\subseteq I\text{-cof}$, uses smallness — they are pure diagram chases valid for any set $I$ in any cocomplete category. Smallness is needed only for the *converse*, $I\text{-cof}\subseteq$ retracts of $I\text{-cell}$, which requires the small object argument. Keeping straight which direction is free (cell complexes are cofibrations) and which needs smallness (cofibrations are retracts of cell complexes) is one of the cleanest ways to organize the chapter: the "easy" containment is saturation, the "hard" one is the small object argument.

**Lifting problems for colimits are solved on the pieces and assembled — this is the master diagram-chase template.** The recurring move across all four parts is to take a lifting square for a complicated map, restrict it (via a universal property) to lifting squares for simpler maps, solve those, and reassemble the solution (via the same universal property). This template — "decompose the lifting problem along the colimit, solve pieces, glue" — is the single most reused diagram chase in homotopy theory, appearing in the closure theorem, the small object argument, and the recognition theorem. Internalizing it means most closure statements become routine: identify the colimit, restrict, lift, reassemble.
