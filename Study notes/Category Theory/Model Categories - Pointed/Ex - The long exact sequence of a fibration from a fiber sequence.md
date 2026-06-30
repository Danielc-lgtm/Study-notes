---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cofiber and Fiber Sequence"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Higher Homotopy Group"
  - "Thm - The Suspension-Loop Adjunction"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $p : E \to B$ be a [[Def - Cofibrant and Fibrant Objects|fibration]] of pointed spaces with [[Def - Cofiber and Fiber Sequence|homotopy fiber]] $F = F_p$.

1. Write down the dual Puppe **fiber sequence** of $p$ and apply $[S^n, -]$ to obtain the long exact sequence of the [[Def - Fibration|fibration]]
$$\cdots \to \pi_n(F) \to \pi_n(E) \xrightarrow{p_*} \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(F) \to \cdots \to \pi_0(E) \to \pi_0(B).$$
2. Identify the connecting map $\partial : \pi_n(B) \to \pi_{n-1}(F)$ as the map induced by $\Omega B \to F$ (the fiber connecting map) together with $\pi_n(B) = \pi_{n-1}(\Omega B)$.
3. Specialize to the path–loop fibration $\Omega B \to PB \to B$ (with $PB \simeq *$) to recover $\pi_n(\Omega B) \cong \pi_{n+1}(B)$.

**Recall:**

![[Def - Cofiber and Fiber Sequence#The Definition]]

The [[Def - Cofiber and Fiber Sequence|fiber sequence]] of $p : E \to B$ is $\cdots \to \Omega B \xrightarrow{\partial} F \xrightarrow{j} E \xrightarrow{p} B$, where $F = F_p$ is the [[Def - Homotopy|homotopy]] fiber. Applying $[Z, -]$ to a fiber sequence gives a long exact sequence of pointed sets. The [[Def - Higher Homotopy Group|homotopy group]] $\pi_n(Y) = [S^n, Y]$, and $\pi_n(\Omega Y) \cong \pi_{n+1}(Y)$ by the [[Thm - The Suspension-Loop Adjunction|suspension–loop adjunction]] $[S^n, \Omega Y] \cong [\Sigma S^n, Y] = [S^{n+1}, Y]$.

---

# Convergent Strategy

**Problem class:** This is a "produce a long exact sequence from a fiber sequence" exercise — the maps-into-objects half of the chapter's computational machinery. The route is to take the dual Puppe fiber sequence and apply $[S^n, -]$, then translate the abstract terms into homotopy [[Def - Group|groups]].

**Assumption pattern:** The assumption is that $p$ is a fibration, so its homotopy fiber is the actual fiber and the fiber sequence is the classical $F \to E \to B$. Applying $[S^n, -]$ converts the fiber sequence into the long exact sequence; the key is recognizing that the $\Omega B$ term in the fiber sequence, hit by $[S^n, -]$, becomes $\pi_n(\Omega B) = \pi_{n+1}(B)$, which is what shifts the degree in the connecting map.

**Theorem routing:** Part (1) routes through the exactness of $[Z, -]$ on a fiber sequence ([[Def - Cofiber and Fiber Sequence|definition]]) with $Z = S^n$. Part (2) routes through the [[Thm - The Suspension-Loop Adjunction|adjunction]] $[S^n, \Omega B] \cong [S^{n+1}, B]$ to identify the degree shift. Part (3) routes through the contractibility of $PB$ and exactness.

**Key decision point:** The interesting choice is to apply $[S^n, -]$ (maps *into*) rather than $[-, S^n]$, because homotopy groups are maps out of spheres into the space, i.e. maps into the objects of the fiber sequence. Getting the variance right — fiber sequence with $[Z, -]$, cofiber sequence with $[-, Z]$ — is the decision that makes the long exact sequence come out as homotopy groups rather than cohomology.

---

# Legal Operations Used

1. **Operation 5 from the topic page (apply $[Z, -]$ to a fiber sequence).** With $Z = S^n$ this produces the long exact sequence of homotopy groups.

2. **Operation 6 from the topic page (use the suspension–loop adjunction).** Part (2) uses $[S^n, \Omega B] \cong [S^{n+1}, B]$ to identify the connecting map's degree shift.

3. **Operation 7 from the topic page (rotate a (co)fiber sequence).** The infinite fiber sequence is the rotation of the three-term one, supplying all degrees at once.

---

# Hints

> [!note]- Hint 1
> The fiber sequence of $p$ is $\cdots \to \Omega E \to \Omega B \to F \to E \to B$. Apply $[S^n, -]$ to the whole thing. Exactness of $[Z, -]$ on a fiber sequence gives an exact sequence of pointed sets.

> [!note]- Hint 2
> $[S^n, F] = \pi_n(F)$, $[S^n, E] = \pi_n(E)$, $[S^n, B] = \pi_n(B)$. What is $[S^n, \Omega B]$?

> [!note]- Hint 3
> $[S^n, \Omega B] \cong [\Sigma S^n, B] = [S^{n+1}, B] = \pi_{n+1}(B)$. So the $\Omega B$ term contributes $\pi_{n+1}(B)$, and the map out of it into $\pi_n(F)$ is the connecting map $\partial : \pi_{n+1}(B) \to \pi_n(F)$ (re-index to $\partial : \pi_n(B) \to \pi_{n-1}(F)$).

---

# Solution

The solution applies $[S^n, -]$ to the fiber sequence of $p$, translates the terms into homotopy groups using the adjunction, and specializes to the path–loop fibration.

**Step 1: Apply $[S^n, -]$ to the fiber sequence.**

> [!note]- Derivation
> The dual Puppe [[Def - Cofiber and Fiber Sequence|fiber sequence]] of $p : E \to B$ is
> $$\cdots \to \Omega E \xrightarrow{\Omega p} \Omega B \xrightarrow{\partial} F \xrightarrow{j} E \xrightarrow{p} B.$$
> Applying $[S^n, -]$ — exact on fiber sequences — gives the exact sequence of pointed sets
> $$\cdots \to [S^n, \Omega B] \xrightarrow{\partial_*} [S^n, F] \xrightarrow{j_*} [S^n, E] \xrightarrow{p_*} [S^n, B].$$
> Now $[S^n, F] = \pi_n(F)$, $[S^n, E] = \pi_n(E)$, $[S^n, B] = \pi_n(B)$, exact at each (and the segments are groups for $n \ge 1$, abelian for $n \ge 2$, since the spheres $S^n$ with $n \ge 1$ are suspensions). Splicing across all $n$ assembles the full long exact sequence of the fibration.

**Step 2: The connecting map and the degree shift.**

> [!note]- Derivation
> The term $[S^n, \Omega B]$ is not a homotopy group of $B$ in degree $n$; the [[Thm - The Suspension-Loop Adjunction|adjunction]] gives
> $$[S^n, \Omega B] \cong [\Sigma S^n, B] = [S^{n+1}, B] = \pi_{n+1}(B).$$
> So the map $\partial_* : [S^n, \Omega B] \to [S^n, F]$ is, after this identification, a map $\pi_{n+1}(B) \to \pi_n(F)$ — the **connecting homomorphism** of the fibration, raising on $B$ and dropping on $F$ by one degree. Re-indexing ($n+1 \rightsquigarrow n$) writes it as $\partial : \pi_n(B) \to \pi_{n-1}(F)$. It is induced by the fiber connecting map $\Omega B \to F$, composed with the adjunction identification $\pi_n(B) = \pi_{n-1}(\Omega B)$. Threading the identifications through the exact sequence of Step 1 yields
> $$\cdots \to \pi_n(F) \to \pi_n(E) \xrightarrow{p_*} \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(F) \to \cdots \to \pi_0(E) \to \pi_0(B).$$

**Step 3: The path–loop fibration.**

> [!note]- Derivation
> Take the path–loop fibration $\Omega B \xrightarrow{} PB \xrightarrow{} B$, where $PB$ is the based path space (paths starting at the basepoint), the homotopy fiber is $\Omega B$, and $PB$ is **contractible** ($PB \simeq *$) because every path retracts to its starting point. Plug into the long exact sequence with $E = PB$, $F = \Omega B$: since $\pi_n(PB) = 0$ for all $n$, the long exact sequence
> $$\pi_n(PB) \to \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(\Omega B) \to \pi_{n-1}(PB)$$
> has zeros at both ends, forcing $\partial$ to be an isomorphism: $\pi_n(B) \cong \pi_{n-1}(\Omega B)$, i.e. $\pi_{n-1}(\Omega B) \cong \pi_n(B)$. This is the loop-space degree shift, recovered as a degenerate case of the fibration long exact sequence — and it is exactly the [[Thm - The Suspension-Loop Adjunction|suspension–loop adjunction]] $\pi_n(\Omega B) \cong \pi_{n+1}(B)$ seen through the fiber sequence.

> [!note]- Complete formal solution
> **(1)** Apply $[S^n, -]$ to the fiber sequence $\cdots \to \Omega B \to F \to E \to B$ of $p$; exactness on fiber sequences gives exact $\cdots \to [S^n, \Omega B] \to \pi_n(F) \to \pi_n(E) \to \pi_n(B)$.
>
> **(2)** By the adjunction $[S^n, \Omega B] \cong [S^{n+1}, B] = \pi_{n+1}(B)$, so the map out of the $\Omega B$ term is the connecting homomorphism $\partial : \pi_{n+1}(B) \to \pi_n(F)$ (equivalently $\pi_n(B) \to \pi_{n-1}(F)$), induced by $\Omega B \to F$. Splicing gives $\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(F) \to \cdots \to \pi_0(E) \to \pi_0(B)$.
>
> **(3)** For $\Omega B \to PB \to B$ with $PB \simeq *$, all $\pi_n(PB) = 0$, so $\partial : \pi_n(B) \to \pi_{n-1}(\Omega B)$ is an isomorphism: $\pi_n(\Omega B) \cong \pi_{n+1}(B)$. $\blacksquare$

---

# Key Takeaways

**Fiber sequences with $[Z, -]$ give homotopy; cofiber sequences with $[-, Z]$ give cohomology — choose by variance.** The single most important decision in producing a long exact sequence is whether you are computing maps *into* the objects (homotopy groups, $[S^n, -]$, fiber sequence) or maps *out of* them (cohomology, $[-, Z]$, cofiber sequence). Get the pairing wrong and the sequence comes out in the wrong variance or fails to be exact. The trigger is the object you fix: a test sphere $S^n$ that you map *out of* pairs with $[S^n, -]$ and fiber sequences; a coefficient object you map *into* pairs with $[-, Z]$ and cofiber sequences. This pairing is the practical content of the agreement theorem — the two are dual, and which one you use is dictated by whether your invariant is covariant or contravariant.

**The connecting map's degree shift comes entirely from $[S^n, \Omega B] = \pi_{n+1}(B)$.** What makes the fibration long exact sequence "shift degree" — sending $\pi_n(B)$ to $\pi_{n-1}(F)$ — is not an extra structure but the adjunction identity that maps into a loop space raise the homotopy degree by one. The reusable insight is that any time a long exact sequence has a connecting map that changes degree, the shift is a suspension or loop hiding in one of the terms, and the suspension–loop adjunction is what exposes it. Recognizing the $\Omega B$ term as "$\pi_{n+1}(B)$ in disguise" is the move that turns an abstract fiber-sequence exactness into the familiar degree-shifting boundary map of a first algebraic topology course.

**A contractible total space collapses the long exact sequence into an isomorphism — the universal trick for extracting shifts.** The path–loop fibration recovers $\pi_n(\Omega B) \cong \pi_{n+1}(B)$ purely because $PB \simeq *$ kills the flanking terms, forcing the connecting map to be an isomorphism. This is the dual of the contractible-cone trick from the suspension exercise, and it is the universal way to extract a clean isomorphism from a (co)fiber sequence: arrange for a contractible term and read off the isomorphism between its neighbors. The diagnostic to carry is that whenever a fiber sequence has a contractible total space (or a cofiber sequence a contractible middle), the connecting map is an isomorphism and you have computed a shift for free.
