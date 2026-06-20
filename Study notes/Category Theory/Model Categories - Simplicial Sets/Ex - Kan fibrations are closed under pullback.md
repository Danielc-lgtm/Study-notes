---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Kan Fibration and Anodyne Extension"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $p : E \to B$ be a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] of [[Def - Simplicial Set|simplicial sets]] and let $g : B' \to B$ be any map. Form the [[Def - Pullback and Pushout|pullback]]
$$\begin{array}{ccc} E' & \xrightarrow{\ \bar g\ } & E \\ {\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p} \\ B' & \xrightarrow{\ g\ } & B \end{array} \qquad E' = B' \times_B E.$$
Show that the pulled-back map $p' : E' \to B'$ is again a Kan fibration. Deduce that for every vertex $b \in B_0$ the fibre $F_b = p^{-1}(b)$ is a [[Def - Kan Complex and the Nerve|Kan complex]].

**Recall:**

A map $p : E \to B$ is a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]] if it has the right [[Def - Lifting Property and the Retract Argument|lifting property]] against every horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$: every commuting square with $\Lambda^n_k \to E$ on top, $\Delta^n \to B$ on the bottom, and $p$ on the right admits a diagonal lift $\Delta^n \to E$.

The **pullback** $E' = B' \times_B E$ has, in each dimension, $E'_n = \{(b', e) \in B'_n \times E_n : g(b') = p(e)\}$, with the universal property that maps into $E'$ are pairs of maps into $B'$ and $E$ agreeing in $B$.

A [[Def - Simplicial Set|simplicial set]] $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]] iff $X \to *$ is a Kan fibration.

---

# Convergent Strategy

**Problem class:** This is a *closure-property* problem of the lifting world (topic-page Problem-Solving Strategy): show a class defined by a right [[Def - Lifting Property and the Retract Argument|lifting property]] is closed under an operation. The universal routine is that right lifting classes are *always* closed under pullback, and the proof is a single diagram chase using the universal properties.

**Assumption pattern:** The recognisable feature is "Kan fibration" — i.e. membership of an $\mathrm{RLP}$ class — together with a pullback square. The combination unlocks the standard move: a lifting problem against $p'$ can be *exported* across the pullback to a lifting problem against $p$, which is solvable by hypothesis, and the solution *imported* back by the pullback's universal property.

**Theorem routing:** The route is: lifting square against $p'$ $\to$ compose with $\bar g$ to get a lifting square against $p$ $\to$ solve using the Kan condition on $p$ $\to$ pair the lift with the base map using the pullback universal property $\to$ obtain the lift against $p'$. No deep theorem is needed; the universal property of the pullback does all the work.

**Key decision point:** The only non-obvious step is recognising that one must *not* try to lift in $E'$ directly. The lift in $E'$ is assembled from two pieces — a lift in $E$ (provided by $p$) and the given map to $B'$ — glued by the pullback's universal property. Trying to fill the horn in $E'$ without decomposing it is the natural wrong move; the pullback structure is exactly what lets the problem be split.

---

# Legal Operations Used

1. **Operation 1 from the topic page (fill a horn).** The lift against $p$ is obtained by the Kan condition: the horn in $E$ fills because $p$ is a Kan fibration.

2. **The universal property of pullbacks (from [[Def - Pullback and Pushout]]).** The lift against $p'$ is constructed as the unique map into $E' = B' \times_B E$ induced by the base map $\Delta^n \to B'$ and the lift $\Delta^n \to E$, which agree over $B$.

3. **The closure of $\mathrm{RLP}$ classes under pullback (from [[Def - Kan Fibration and Anodyne Extension]]).** This exercise is the concrete instance of the general fact that any right lifting class is closed under pullback; the fibre case ($g : * \to B$) is the corollary.

---

# Hints

> [!note]- Hint 1
> A Kan fibration is defined by a lifting property. Closure of *any* right lifting class under pullback is a formal fact — try to prove it without using anything special about horns.

> [!note]- Hint 2
> Start with a lifting square against $p'$: a horn $a : \Lambda^n_k \to E'$ and a simplex $b' : \Delta^n \to B'$ with $p' a = b'|_{\Lambda^n_k}$. Push $a$ forward to $E$ via $\bar g$, and push $b'$ down to $B$ via $g$. Check you now have a lifting square against $p$.

> [!note]- Hint 3
> Solve the lifting square against $p$ using the Kan condition: get $\ell : \Delta^n \to E$. Now you have two compatible maps out of $\Delta^n$ — namely $\ell$ into $E$ and $b'$ into $B'$ — agreeing over $B$. The pullback's universal property turns them into a single map $\Delta^n \to E'$.

> [!note]- Hint 4
> For the fibre, take $g$ to be $b : \Delta^0 \to B$ (a vertex) and $B' = \Delta^0 = *$. The pullback $E' = * \times_B E$ is the fibre $F_b$, and $p' : F_b \to *$ is a Kan fibration, i.e. $F_b$ is a Kan complex.

---

# Solution

The pullback of a Kan fibration is a Kan fibration by a one-step diagram chase: a horn-lifting problem against $p'$ transports to one against $p$, the Kan condition solves it in $E$, and the [[Def - Pullback and Pushout|pullback]] universal property reassembles the solution in $E'$. The fibre is the special case where the base of the pullback is a point.

**Step 1: Set up a lifting square against $p'$.**

> [!note]- Derivation
> Suppose given a commuting square
> $$\begin{array}{ccc} \Lambda^n_k & \xrightarrow{\ a\ } & E' \\ \cap & & \downarrow{\scriptstyle p'} \\ \Delta^n & \xrightarrow{\ b'\ } & B' \end{array}$$
> with $p' \circ a = b'|_{\Lambda^n_k}$. By the [[Def - Pullback and Pushout|pullback]] description, $a = (a_{B'}, a_E)$ where $a_{B'} = p' a : \Lambda^n_k \to B'$ and $a_E = \bar g a : \Lambda^n_k \to E$, with $g \circ a_{B'} = p \circ a_E$. Note $a_{B'} = b'|_{\Lambda^n_k}$.

**Step 2: Transport to a lifting square against $p$ and solve.**

> [!note]- Derivation
> Compose downward: $g \circ b' : \Delta^n \to B$ and $a_E = \bar g a : \Lambda^n_k \to E$ form a square
> $$\begin{array}{ccc} \Lambda^n_k & \xrightarrow{\ a_E\ } & E \\ \cap & & \downarrow{\scriptstyle p} \\ \Delta^n & \xrightarrow{\ g b'\ } & B \end{array}$$
> which commutes: $p \circ a_E = g \circ a_{B'} = g \circ (b'|_{\Lambda^n_k}) = (g b')|_{\Lambda^n_k}$. Since $p$ is a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]], the Kan condition (operation 1) supplies a lift $\ell : \Delta^n \to E$ with $\ell|_{\Lambda^n_k} = a_E$ and $p \circ \ell = g \circ b'$.

**Step 3: Reassemble the lift in $E'$.**

> [!note]- Derivation
> The two maps $b' : \Delta^n \to B'$ and $\ell : \Delta^n \to E$ satisfy $g \circ b' = p \circ \ell$ (the second condition of Step 2), so by the universal property of the pullback $E' = B' \times_B E$ they induce a unique map $\tilde\ell = (b', \ell) : \Delta^n \to E'$ with $p' \tilde\ell = b'$ and $\bar g \tilde\ell = \ell$. Restricting to $\Lambda^n_k$: $p' (\tilde\ell|_{\Lambda^n_k}) = b'|_{\Lambda^n_k} = a_{B'}$ and $\bar g(\tilde\ell|_{\Lambda^n_k}) = \ell|_{\Lambda^n_k} = a_E$, so $\tilde\ell|_{\Lambda^n_k} = (a_{B'}, a_E) = a$ by uniqueness. Thus $\tilde\ell$ is a lift of the original square: $p'$ is a Kan fibration.

**Step 4: The fibre is a Kan complex.**

> [!note]- Derivation
> Take $B' = \Delta^0 = *$ and $g = b : * \to B$ the vertex $b \in B_0$. The pullback $E' = * \times_B E$ is precisely the fibre $F_b = p^{-1}(b)$ (the simplices of $E$ mapping to the degeneracies of $b$). By Steps 1–3, $p' : F_b \to *$ is a Kan fibration, which is exactly the statement that $F_b$ is a [[Def - Kan Complex and the Nerve|Kan complex]].

> [!note]- Complete formal solution
> Let $E' = B' \times_B E$ with projections $p' : E' \to B'$ and $\bar g : E' \to E$. Given a horn-lifting square $(a : \Lambda^n_k \to E',\ b' : \Delta^n \to B')$ with $p'a = b'|_{\Lambda^n_k}$, set $a_E = \bar g a$. Then $(a_E,\ g b')$ is a horn-lifting square against $p$, since $p a_E = g p' a = g(b'|_{\Lambda^n_k}) = (gb')|_{\Lambda^n_k}$. As $p$ is a [[Def - Kan Fibration and Anodyne Extension|Kan fibration]], there is a lift $\ell : \Delta^n \to E$ with $\ell|_{\Lambda^n_k} = a_E$, $p\ell = gb'$. Since $g b' = p\ell$, the pair $(b', \ell)$ induces $\tilde\ell : \Delta^n \to E'$ with $p'\tilde\ell = b'$, $\bar g\tilde\ell = \ell$; uniqueness gives $\tilde\ell|_{\Lambda^n_k} = a$. So $\tilde\ell$ lifts the square and $p'$ is a Kan fibration. Taking $B' = *$, $g = b$, the fibre $F_b = *\times_B E$ has $F_b \to *$ a Kan fibration, so $F_b$ is a Kan complex. $\quad\blacksquare$

---

# Key Takeaways

**Right lifting classes are closed under pullback — always, and by the same chase.** This exercise is one instance of a structural fact worth internalising completely: for any class $\mathcal{S}$ of maps, $\mathrm{RLP}(\mathcal{S})$ is closed under pullback, composition, retract, and (cofiltered) limit. The proof never depends on what $\mathcal{S}$ is — it is pure universal-property bookkeeping. So whenever you meet "fibration" (a right lifting class) and an operation that builds new maps from old, the reflex should be to ask whether that operation is one of these four; if so, fibrations are closed under it for free. Dually, left lifting classes (cofibrations, anodyne maps) are closed under pushout, transfinite composition, retract, and coproduct. Memorising which closures go with which side removes a large fraction of the routine verifications in homotopy theory.

**The fibre is a pullback, so fibre-properties are pullback-properties.** The deduction that fibres of Kan fibrations are Kan complexes is not a separate theorem — it is the pullback-closure specialised to $g : * \to B$. This is the general principle that "the fibre over a point is the pullback along the point", and it means every closure property of fibrations descends to a property of fibres: fibres of Kan fibrations are Kan, fibres of minimal fibrations are minimal Kan complexes, fibres of trivial fibrations are contractible. Whenever you want to know something about the fibre of a map, the trigger-reaction is to write the fibre as a pullback and transport the property of the map.

**Lifts in a pullback are assembled, not found.** The one genuinely instructive move is that you do not fill the horn in $E'$ directly; you split the problem, solve the half that lives in $E$ using the actual homotopical input (the Kan condition), and glue using the universal property. This "decompose along the pullback, solve the hard half, reassemble" pattern is ubiquitous: it is how one lifts against any map built as a pullback, how base change works in fibrewise homotopy theory, and how the long exact sequence of a fibration is constructed. The transferable diagnostic is: when a lifting or extension problem lives in a limit (pullback, product, equaliser), push it to the factors, solve there, and pull back the solution.
