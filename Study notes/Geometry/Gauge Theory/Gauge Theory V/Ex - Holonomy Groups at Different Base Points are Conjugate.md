---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Holonomy Group of a Connection"
  - "Thm - Properties of Parallel Transport"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a smooth real vector bundle of rank $k$ over a connected manifold $M$, and let $\nabla$ be a connection on $E$. For a base point $m\in M$ write
$$\operatorname{Hol}_m(\nabla)=\{PT_\gamma\in GL(E_m):\gamma\text{ a piecewise smooth loop based at }m\}$$
for the holonomy group at $m$. Prove Haydys's "standard argument":

1. **(Conjugacy of the groups.)** If $m$ and $m'$ lie in the same connected component of $M$, then $\operatorname{Hol}_m(\nabla)$ and $\operatorname{Hol}_{m'}(\nabla)$ are conjugate. Precisely, for any piecewise smooth path $\gamma$ from $m$ to $m'$ the parallel transport $PT_\gamma\colon E_m\to E_{m'}$ satisfies
$$\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1},$$
and after choosing bases of $E_m$ and $E_{m'}$ this reads $\operatorname{Hol}_{m'}(\nabla)=A\,\operatorname{Hol}_m(\nabla)\,A^{-1}$ for the matrix $A\in GL_k(\mathbb R)$ of $PT_\gamma$.
2. **(Independence of the base point up to conjugacy.)** Consequently the conjugacy class of $\operatorname{Hol}_m(\nabla)$ in $GL_k(\mathbb R)$ does not depend on the choice of base point in the connected manifold $M$.
3. **(Independence of the basis up to conjugacy.)** At a fixed base point, changing the basis of $E_m$ replaces $\operatorname{Hol}_m(\nabla)$ by a conjugate subgroup of $GL_k(\mathbb R)$; so $\operatorname{Hol}(\nabla)$ is well defined as a subgroup of $GL_k(\mathbb R)$ up to conjugacy, with the base point dropped from the notation.

The intended route is to move a loop from $m'$ to $m$ and back by pre- and post-composing with a fixed path $\gamma$, and to read the resulting identity through the multiplicativity and reversal properties of parallel transport.

**Recall:**

The objects in play are the holonomy group of a connection and the structural identities satisfied by parallel transport under concatenation and reversal of curves.

![[Def - Holonomy Group of a Connection#The Definition]]

That $\operatorname{Hol}_m(\nabla)$ is genuinely a subgroup of $GL(E_m)$ — closed under composition and inverses and containing the identity — is proved on [[Def - Holonomy Group of a Connection|its page]] (Corollary 1) from the two properties recalled next; the present exercise proves the base-point statement, which that page records as its Corollary 3.

![[Thm - Properties of Parallel Transport#Statement]]

The two structural properties this exercise consumes are, in the numbering of [[Thm - Properties of Parallel Transport|that theorem]]:

- **Property (3) — reversal.** If $\bar c$ denotes the curve $c$ traversed backwards, then $PT_{\bar c}=PT_c^{-1}$.
- **Property (4) — concatenation.** If $c_1$ ends where $c_2$ begins, and $c_2*c_1$ denotes "first $c_1$, then $c_2$", then $PT_{c_2*c_1}=PT_{c_2}\circ PT_{c_1}$.

We also use that a **connected manifold is path-connected** (indeed piecewise-smooth-path-connected): a manifold is locally path connected, so each connected component is open and path connected, and any two points of $M$ can be joined by a piecewise smooth path.

---

# Convergent Strategy

**Problem class.** This is a *change-of-basepoint* problem: an invariant defined at a point of a connected space is shown to be independent of the point up to the natural identification that connectedness provides. The pattern recurs throughout the subject — the fundamental group at different base points, the fibre of a covering, the isotropy representation of a bundle — and the mechanism is always the same: a path between the two points induces an isomorphism, and the two point-based objects correspond under it.

**Assumption pattern.** The hypothesis "same connected component" is used exactly once, to *produce a path* $\gamma$ from $m$ to $m'$; everything after that is formal manipulation of parallel transports. The recognisable trigger is that the object $\operatorname{Hol}_m(\nabla)$ lives in $GL(E_m)$, a group attached to the single fibre $E_m$, while $\operatorname{Hol}_{m'}(\nabla)$ lives in $GL(E_{m'})$; to compare two groups attached to different fibres one needs an isomorphism $E_m\to E_{m'}$, and the only canonical-up-to-path such isomorphism a connection offers is parallel transport.

**Theorem routing.** The route is: pick a path $\gamma$ from $m$ to $m'$ (connectedness); given a loop $c$ at $m$, build the loop $\gamma*c*\bar\gamma$ at $m'$ (a legal concatenation because the endpoints match); compute its transport by [[Thm - Properties of Parallel Transport|property (4)]] as $PT_\gamma\circ PT_c\circ PT_{\bar\gamma}$, then by [[Thm - Properties of Parallel Transport|property (3)]] as $PT_\gamma\circ PT_c\circ PT_\gamma^{-1}$. This gives one inclusion; the symmetric construction (starting from a loop at $m'$ and conjugating by $\bar\gamma$) gives the reverse inclusion, and the two together give equality. Independence of base point is then the observation that conjugacy is an equivalence relation, and independence of basis is the elementary fact that a change of basis conjugates every matrix representation.

**Key decision point.** The single non-obvious move is *how to turn a loop at $m$ into a loop at $m'$.* One cannot simply "translate" a loop across the manifold; one must physically prepend a trip $\bar\gamma$ from $m'$ to $m$ and append the return trip $\gamma$ from $m$ to $m'$, so that the excursion begins and ends at $m'$ while doing its actual work — the loop $c$ — at $m$. Recognising that this sandwich $\gamma*c*\bar\gamma$ is the correct object, and that its transport factors as a conjugate of $PT_c$, is the whole content; the properties of parallel transport then do the arithmetic automatically. A secondary decision is to prove *both* inclusions rather than one: the map $c\mapsto\gamma*c*\bar\gamma$ shows $PT_\gamma\operatorname{Hol}_m PT_\gamma^{-1}\subseteq\operatorname{Hol}_{m'}$, and only the reverse construction gives equality, which is what "conjugate" requires.

---

# Legal Operations Used

This solution deploys the following legal operations, named descriptively (the topic page's numbered Legal Operations list will absorb them once written):

1. **Extract a path from connectedness.** Use that $M$ is connected, hence piecewise-smooth-path-connected, to choose a fixed path $\gamma$ from $m$ to $m'$; this is the only use of the hypothesis.

2. **Conjugate a loop by a path (the sandwich construction).** Turn a loop $c$ based at $m$ into the loop $\gamma*c*\bar\gamma$ based at $m'$ by prepending $\bar\gamma$ and appending $\gamma$; check that the endpoints match at every junction.

3. **Multiply parallel transports along a concatenation.** Apply property (4) of [[Thm - Properties of Parallel Transport|the properties theorem]] to factor $PT_{\gamma*c*\bar\gamma}=PT_\gamma\circ PT_c\circ PT_{\bar\gamma}$.

4. **Invert a parallel transport by reversing the curve.** Apply property (3) to replace $PT_{\bar\gamma}$ by $PT_\gamma^{-1}$, exhibiting the transport as a conjugate.

5. **Prove set equality by two inclusions.** Establish $PT_\gamma\operatorname{Hol}_m PT_\gamma^{-1}\subseteq\operatorname{Hol}_{m'}$ and the reverse, using the symmetric sandwich, to conclude equality.

6. **Pass to matrices and use that conjugacy is an equivalence relation.** Represent $PT_\gamma$ by a matrix $A\in GL_k(\mathbb R)$ after choosing bases, and use reflexivity, symmetry, and transitivity of conjugacy to conclude base-point and basis independence.

---

# Hints

> [!note]- Hint 1
> The two groups $\operatorname{Hol}_m(\nabla)$ and $\operatorname{Hol}_{m'}(\nabla)$ live in $GL(E_m)$ and $GL(E_{m'})$ — automorphism groups of *different* vector spaces. To compare them you first need one isomorphism $E_m\to E_{m'}$. What does a connection give you, once you have a path from $m$ to $m'$?

> [!note]- Hint 2
> You cannot move a loop at $m$ to a loop at $m'$ by itself. But you can travel from $m'$ to $m$ along $\bar\gamma$, run your loop $c$ at $m$, and travel back along $\gamma$. Write down this concatenation and check that it is a genuine loop based at $m'$.

> [!note]- Hint 3
> Apply the concatenation property (4) of [[Thm - Properties of Parallel Transport|parallel transport]] to $\gamma*c*\bar\gamma$. You will get a product of three transports. Now use the reversal property (3) to rewrite $PT_{\bar\gamma}$. What familiar algebraic shape — $XYX^{-1}$ — appears?

> [!note]- Hint 4
> One sandwich gives $PT_\gamma\operatorname{Hol}_m PT_\gamma^{-1}\subseteq\operatorname{Hol}_{m'}$. To get equality, do the same with the roles of $m$ and $m'$ exchanged, conjugating a loop $c'$ at $m'$ by $\bar\gamma$ to a loop at $m$. For parts 2 and 3, remember that "$G_1$ is conjugate to $G_2$" is an equivalence relation, and that changing a basis conjugates every matrix by the change-of-basis matrix.

---

# Solution

The proof rests on one construction — sandwiching a loop $c$ at $m$ between a path $\gamma$ and its reverse $\bar\gamma$ to make a loop at $m'$ — and two properties of parallel transport, concatenation and reversal, which turn the transport of the sandwich into a conjugate of the transport of $c$. Two symmetric applications give the conjugacy of the two holonomy groups; the base-point and basis statements are then formal consequences of conjugacy being an equivalence relation.

**Step 0: A path exists and parallel transport along it is an isomorphism.**

Because $M$ is connected it is piecewise-smooth-path-connected, so there is a piecewise smooth path $\gamma$ from $m$ to $m'$, and $PT_\gamma\colon E_m\to E_{m'}$ is a linear isomorphism.

> [!note]- Derivation
> A smooth manifold is locally path connected: every point has a chart homeomorphic to an open ball, and an open ball is path connected by straight-line segments, which are smooth. It follows that each path component of $M$ is open, because every point of a path component has a chart-ball neighbourhood contained in the same path component. The complement of a path component is the union of the remaining path components, hence also open; so each path component is both open and closed. As $M$ is connected and nonempty, it has exactly one path component, and therefore $M$ is path connected; the joining paths, built by concatenating straight segments inside successive charts, are piecewise smooth. Fix such a path
> $$\gamma\colon[0,1]\to M,\qquad \gamma(0)=m,\quad\gamma(1)=m'.$$
> Parallel transport $PT_\gamma\colon E_m\to E_{m'}$ is a well-defined **linear isomorphism**: a parallel section along $\gamma$ solves the linear ordinary differential equation $\nabla_t s=0$, which in a trivialisation of $\gamma^{*}E$ over the contractible interval $[0,1]$ reads $\dot s+B(t)s=0$ with $B$ continuous, and by [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness theorem for horizontal lifts]] this has a unique solution on all of $[0,1]$ for each initial value in $E_m$; the map $u\mapsto PT_\gamma u:=s_u(1)$ is linear because the equation is linear in $s$, and invertible by property (3) below. Its inverse is $PT_{\bar\gamma}=PT_\gamma^{-1}$ by property (3) of [[Thm - Properties of Parallel Transport|the properties of parallel transport]], where $\bar\gamma(t)=\gamma(1-t)$ is the reversed path.

**Step 1: Each loop at $m$ conjugates to a loop at $m'$, and its transport is a conjugate of $PT_c$.**

For a loop $c$ based at $m$, the sandwich $\gamma*c*\bar\gamma$ is a loop based at $m'$, and its parallel transport is $PT_\gamma\circ PT_c\circ PT_\gamma^{-1}$.

> [!note]- Derivation
> Let $c$ be a piecewise smooth loop based at $m$, so $c(0)=c(1)=m$. Form the concatenation
> $$\gamma*c*\bar\gamma\colon\quad m'\xrightarrow{\ \bar\gamma\ }m\xrightarrow{\ c\ }m\xrightarrow{\ \gamma\ }m',$$
> read left to right as "first traverse $\bar\gamma$, then $c$, then $\gamma$". Every junction matches: $\bar\gamma$ ends at $m$ where $c$ begins, and $c$ ends at $m$ where $\gamma$ begins; the whole curve starts and ends at $m'$, so it is a **loop based at $m'$**, and it is piecewise smooth as a concatenation of piecewise smooth pieces.
>
> **Factor the transport by concatenation.** By property (4) of [[Thm - Properties of Parallel Transport|the properties of parallel transport]], the transport of a concatenation is the composite of the transports in the order traversed:
> $$PT_{\gamma*c*\bar\gamma}=PT_\gamma\circ PT_c\circ PT_{\bar\gamma}\qquad\text{(property (4), applied twice to the three pieces).}$$
> **Rewrite the reversed piece.** By property (3), $PT_{\bar\gamma}=PT_\gamma^{-1}$, so
> $$PT_{\gamma*c*\bar\gamma}=PT_\gamma\circ PT_c\circ PT_\gamma^{-1}\qquad\text{(property (3): reversal inverts the transport).}$$
> The left-hand side is the transport of a loop at $m'$, hence lies in $\operatorname{Hol}_{m'}(\nabla)$. Therefore, for every $c$ with $PT_c\in\operatorname{Hol}_m(\nabla)$,
> $$PT_\gamma\circ PT_c\circ PT_\gamma^{-1}\in\operatorname{Hol}_{m'}(\nabla),$$
> which is the inclusion
> $$PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}\ \subseteq\ \operatorname{Hol}_{m'}(\nabla).$$

**Step 2: The reverse inclusion, hence equality.**

The symmetric sandwich sends loops at $m'$ to loops at $m$ and gives the reverse inclusion; combined with Step 1 this yields $\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}$.

> [!note]- Derivation
> Let $c'$ be a loop based at $m'$. Form the sandwich by the reversed path,
> $$\bar\gamma*c'*\gamma\colon\quad m\xrightarrow{\ \gamma\ }m'\xrightarrow{\ c'\ }m'\xrightarrow{\ \bar\gamma\ }m,$$
> a piecewise smooth loop based at $m$. By properties (4) and (3),
> $$PT_{\bar\gamma*c'*\gamma}=PT_{\bar\gamma}\circ PT_{c'}\circ PT_\gamma=PT_\gamma^{-1}\circ PT_{c'}\circ PT_\gamma\qquad\text{(property (4), then property (3)).}$$
> This lies in $\operatorname{Hol}_m(\nabla)$, so $PT_\gamma^{-1}\circ\operatorname{Hol}_{m'}(\nabla)\circ PT_\gamma\subseteq\operatorname{Hol}_m(\nabla)$. Composing on the left with $PT_\gamma$ and on the right with $PT_\gamma^{-1}$ (both isomorphisms) preserves the inclusion and gives
> $$\operatorname{Hol}_{m'}(\nabla)\ \subseteq\ PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}.$$
> Combining with the inclusion of Step 1,
> $$\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}.$$
> The conjugating map $PT_\gamma\colon E_m\to E_{m'}$ is the abstract statement; choosing bases of $E_m$ and $E_{m'}$ and letting $A\in GL_k(\mathbb R)$ be the matrix of $PT_\gamma$ turns this into $\operatorname{Hol}_{m'}(\nabla)=A\,\operatorname{Hol}_m(\nabla)\,A^{-1}$ inside $GL_k(\mathbb R)$. This is part 1.

**Step 3: Independence of the base point up to conjugacy.**

Since any two points of the connected manifold are joined by a path, all the groups $\operatorname{Hol}_m(\nabla)$ form a single conjugacy class in $GL_k(\mathbb R)$.

> [!note]- Derivation
> Conjugacy of subgroups is an equivalence relation: it is reflexive (conjugate by the identity), symmetric (if $H'=AHA^{-1}$ then $H=A^{-1}H'A$), and transitive (if $H'=AHA^{-1}$ and $H''=BH'B^{-1}$ then $H''=(BA)H(BA)^{-1}$). By Step 2, for any two points $m,m'$ in the connected manifold $M$ the groups $\operatorname{Hol}_m(\nabla)$ and $\operatorname{Hol}_{m'}(\nabla)$ are conjugate. Hence they all lie in **one conjugacy class**, and the class is a base-point-independent invariant of $(\nabla)$. Different choices of connecting path $\gamma$ give different conjugating elements $A$, but all produce the same conjugacy class, so the possible non-uniqueness of $\gamma$ does not affect the conclusion. This is part 2.

**Step 4: Independence of the basis up to conjugacy.**

At a fixed base point, changing the basis of $E_m$ replaces the matrix group by a conjugate; so $\operatorname{Hol}(\nabla)$ is well defined up to conjugacy in $GL_k(\mathbb R)$, and the base point is dropped from the notation.

> [!note]- Derivation
> Fix $m$ and two bases of $E_m$, related by a change-of-basis matrix $B\in GL_k(\mathbb R)$. If a linear map $\phi\in GL(E_m)$ has matrix $P$ in the first basis, its matrix in the second is $B^{-1}PB$. Applying this to every $\phi=PT_c$ in $\operatorname{Hol}_m(\nabla)$, the matrix group computed in the second basis is $B^{-1}\bigl(\operatorname{Hol}_m(\nabla)\bigr)B$ — a **conjugate** of the one computed in the first. Together with Step 3, both remaining ambiguities in "$\operatorname{Hol}(\nabla)\subseteq GL_k(\mathbb R)$" — the base point and the basis — change the subgroup only by conjugation. Therefore $\operatorname{Hol}(\nabla)$ is a well-defined subgroup of $GL_k(\mathbb R)$ **up to conjugacy**, and one may drop the base point from the notation, as Haydys does after Definition 101. This is part 3.

> [!note]- Complete formal solution
> **Claim.** For $m,m'$ in the connected manifold $M$ and any piecewise smooth path $\gamma$ from $m$ to $m'$, $\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}$; consequently the conjugacy class of $\operatorname{Hol}_m(\nabla)$ in $GL_k(\mathbb R)$ is independent of the base point and of the basis of the fibre.
>
> Since $M$ is a connected manifold it is piecewise-smooth-path-connected (its path components are open and closed, so the connected $M$ has a single one); fix a piecewise smooth path $\gamma$ with $\gamma(0)=m$, $\gamma(1)=m'$. Then $PT_\gamma\colon E_m\to E_{m'}$ is a linear isomorphism — the parallel-transport equation $\nabla_t s=0$ is linear with a unique solution for each initial value by [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness theorem]] — with inverse $PT_{\bar\gamma}=PT_\gamma^{-1}$ (property (3)).
>
> For a loop $c$ at $m$, the curve $\gamma*c*\bar\gamma$ is a loop at $m'$, and by properties (4) and (3),
> $$PT_{\gamma*c*\bar\gamma}=PT_\gamma\circ PT_c\circ PT_{\bar\gamma}=PT_\gamma\circ PT_c\circ PT_\gamma^{-1}\in\operatorname{Hol}_{m'}(\nabla),$$
> so $PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}\subseteq\operatorname{Hol}_{m'}(\nabla)$. For a loop $c'$ at $m'$, the curve $\bar\gamma*c'*\gamma$ is a loop at $m$, and by the same properties $PT_\gamma^{-1}\circ PT_{c'}\circ PT_\gamma\in\operatorname{Hol}_m(\nabla)$, whence $\operatorname{Hol}_{m'}(\nabla)\subseteq PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}$. The two inclusions give
> $$\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1},$$
> i.e. $\operatorname{Hol}_{m'}(\nabla)=A\,\operatorname{Hol}_m(\nabla)\,A^{-1}$ with $A\in GL_k(\mathbb R)$ the matrix of $PT_\gamma$ in chosen bases.
>
> Conjugacy of subgroups is reflexive, symmetric, and transitive, so all the $\operatorname{Hol}_m(\nabla)$ (over the connected $M$) form one conjugacy class, independent of the base point. At a fixed point a change of basis $B\in GL_k(\mathbb R)$ replaces $\operatorname{Hol}_m(\nabla)$ by $B^{-1}\operatorname{Hol}_m(\nabla)B$, again a conjugate. Hence $\operatorname{Hol}(\nabla)$ is a well-defined subgroup of $GL_k(\mathbb R)$ up to conjugacy, and the base point may be dropped. $\blacksquare$

> [!warning] Illegal but tempting: claiming the groups are *equal*, not merely conjugate
> It is tempting to say the holonomy group "is the same" at every point. But $\operatorname{Hol}_m(\nabla)\subseteq GL(E_m)$ and $\operatorname{Hol}_{m'}(\nabla)\subseteq GL(E_{m'})$ are subgroups of automorphism groups of *different* vector spaces; there is no canonical way to identify $E_m$ with $E_{m'}$, only the path-dependent isomorphism $PT_\gamma$. Different paths $\gamma$ generally give genuinely different identifications, and correspondingly different — though conjugate — matrix subgroups. Equality holds only in the degenerate special cases where transport is canonical: on the principal bundle one does get $\operatorname{Hol}_{\Gamma_\gamma(p)}(\omega)=\operatorname{Hol}_p(\omega)$ *equal* (not merely conjugate) when the endpoint is the transport of the start point, precisely because the reference frame moves with the point. The extra structure that would upgrade "conjugate" to "equal" is exactly such a coherent choice of reference frame along the path; without it, conjugacy is the sharpest true statement.

# Key Takeaways

**To compare a point-based invariant at two points of a connected space, transport one to the other along a path and read the invariant through the induced isomorphism.** The holonomy group is attached to a fibre, and fibres over different points are different vector spaces with no canonical identification. Connectedness supplies a path, the connection turns the path into an isomorphism $PT_\gamma\colon E_m\to E_{m'}$, and the invariant at $m'$ is the invariant at $m$ *seen through* that isomorphism — which for a subgroup of a general linear group means "conjugated by $PT_\gamma$". This is the universal template for base-point independence: it is how the fundamental group at different base points is shown isomorphic (change-of-base-point by a path), how the fibres of a covering are identified, and how any bundle-of-groups over a connected base has a well-defined isomorphism type of fibre. The trigger is "an invariant defined at a point of a connected space"; the reaction is "choose a path and transport".

**The sandwich $\gamma*c*\bar\gamma$ is the concrete realisation of conjugation by a path, and it is worth memorising as a move.** A loop at $m$ cannot be relocated to $m'$; instead one *escorts* it — travel out to $m$ along $\bar\gamma$, perform the loop $c$ there, travel back along $\gamma$ — producing a loop at $m'$ whose transport is literally $PT_\gamma\,PT_c\,PT_\gamma^{-1}$. The algebraic shape $XYX^{-1}$ falls out of the two properties of parallel transport, concatenation (property 4) and reversal (property 3), with no computation. The same escorting construction appears whenever one conjugates a based loop by a path — in the change-of-base-point isomorphism of $\pi_1$, in the definition of the monodromy action, and in the proof that the normal closure generated by null-homotopic loops (the restricted holonomy) is normal in the full holonomy. When you see "conjugate by a path", picture the sandwich.

**Conjugate, not equal — and the honest object is the conjugacy class.** The result is not that the holonomy group is a fixed subgroup of $GL_k(\mathbb R)$, but that its *conjugacy class* is a well-defined invariant of the connection on a connected manifold, once one accepts that base point and basis are both arbitrary. This is why every genuinely useful statement about holonomy is phrased in conjugation-invariant terms: whether $\operatorname{Hol}(\nabla)$ is compact, whether it is all of $G$ or a proper subgroup, what its Lie algebra is (the Ambrose–Singer theorem, which identifies it with the span of the curvature), and which abstract group it is isomorphic to. The diagnostic to carry away: before asserting a property of a holonomy group, check that the property is invariant under conjugation; if it is not — such as "contains this *particular* matrix" — it is an artefact of the base point and the basis, not a fact about the connection. The companion exercise [[Ex - Holonomy of Euclidean and Hermitian Connections Lies in the Orthogonal and Unitary Groups|showing that metric and Hermitian connections have holonomy in O(k) and U(m')]] is a case in point: "contained in $O(k)$" *is* conjugation-invariant (a conjugate of an orthogonal group by an orthogonal change of orthonormal basis is again $O(k)$), which is exactly why that containment is a legitimate statement about the connection.
