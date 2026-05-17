---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Rapidity"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Work in $1+1$ dimensions with $\eta = \mathrm{diag}(1,-1)$ and $c = 1$.

1. Show that the set of $2\times 2$ real matrices $L$ satisfying $L^{\mathsf T}\eta L = \eta$ — the **Lorentz group** $O(1,1)$ — is a group under matrix multiplication, verifying all three group axioms directly from the defining condition.
2. Show that $L^{\mathsf T}\eta L = \eta$ implies $\det L = \pm 1$ and $(L^0{}_0)^2 \ge 1$, so $O(1,1)$ has (at least) four disjoint pieces.
3. Show that the **proper orthochronous** piece — $\det L = +1$ and $L^0{}_0 \ge 1$ — consists exactly of the boost matrices $L(\varphi) = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$, $\varphi \in \mathbb{R}$.
4. Identify the other three pieces and describe how each acts on the $(t,x)$-plane.

**Recall:**

The exercise rests on the group-theoretic definition of the Lorentz transformations.

![[Def - The Lorentz Group#The Definition]]

A [[Def - Group|group]] is a set with an associative composition, an identity, and inverses (see [[Group Theory I — §1.1–1.2]]). The Lorentz group is the **pseudo-orthogonal group** of the indefinite form $\eta$ — the analogue, for $\eta$, of the orthogonal group $O(2)$ defined by $R^{\mathsf T}R = I$. The [[Def - The Spacetime Interval|interval]] $t^2 - x^2$ is what these matrices preserve.

---

# Convergent Strategy

**Problem class.** A *structural* problem: verifying group axioms and decomposing a group into its components. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] notes that defining the Lorentz transformations by an invariance makes the group structure fall out for free.

**Assumption pattern.** Only the defining matrix equation $L^{\mathsf T}\eta L = \eta$ is given. The signpost "show it is a group" means: check closure, identity, inverses, each *from the defining equation*, not from any explicit matrix form.

**Theorem routing.** Part 1: manipulate $L^{\mathsf T}\eta L = \eta$ algebraically. Part 2: take determinants, and read off the $(0,0)$ component. Part 3: solve $L^{\mathsf T}\eta L = \eta$ explicitly for a general $2\times 2$ matrix under the two sign constraints; the hyperbolic identity forces the $\cosh/\sinh$ form. Part 4: compose the proper orthochronous piece with parity $P$ and time reversal $T$.

**Key decision point.** The non-obvious efficiency in part 1 is to *never write a matrix*: closure and the inverse property follow by pure manipulation of the defining equation, exactly as for the orthogonal group. The non-obvious step in part 3 is recognising that the constraint equations on the four entries force $L^0{}_0{}^2 - L^1{}_0{}^2 = 1$, the hyperbola, hence the $\cosh/\sinh$ parametrisation.

---

# Legal Operations Used

1. **Classify by the sign of a norm / determinant.** Parts 2 and 4 split the group using $\det L$ and $L^0{}_0$.

2. **Switch to rapidity.** Part 3 identifies the proper orthochronous piece with the rapidity-parametrised boosts.

3. **Use the group axioms** (closure, identity, inverse) as in [[Group Theory I — §1.1–1.2]] — part 1 is exactly this.

4. **Compute an invariant** — the defining condition $L^{\mathsf T}\eta L = \eta$ is the statement that $L$ preserves the interval, and every part exploits it.

---

# Hints

> [!note]- Hint 1
> For closure: if $L_1^{\mathsf T}\eta L_1 = \eta$ and $L_2^{\mathsf T}\eta L_2 = \eta$, compute $(L_1 L_2)^{\mathsf T}\eta(L_1L_2)$ — substitute the inner $L_1^{\mathsf T}\eta L_1$ first. For the inverse: from $\det L = \pm 1$, $L^{-1}$ exists; conjugate the defining equation by $L^{-1}$. Never write an explicit matrix.

> [!note]- Hint 2
> Take $\det$ of both sides of $L^{\mathsf T}\eta L = \eta$: $\det(L^{\mathsf T})\det\eta\det L = \det\eta$, and $\det L^{\mathsf T} = \det L$. For the $(0,0)$ entry: write out the $(0,0)$ component of $L^{\mathsf T}\eta L = \eta$ in terms of the entries of $L$.

> [!note]- Hint 3
> Write $L = \begin{pmatrix}a & b\\c & d\end{pmatrix}$ and impose $L^{\mathsf T}\eta L = \eta$ entry by entry. You get three equations: $a^2 - c^2 = 1$, $b^2 - d^2 = -1$, $ab - cd = 0$. The first says $(a,c)$ lies on a hyperbola — parametrise $a = \cosh\varphi$, $c = \sinh\varphi$ (for $a \ge 1$). Then use the other two to fix $b, d$, and impose $\det L = +1$.

> [!note]- Hint 4
> The four pieces are obtained from the proper orthochronous one by multiplying by $I$, $P = \mathrm{diag}(1,-1)$, $T = \mathrm{diag}(-1,1)$, and $PT = \mathrm{diag}(-1,-1)$. Check the $(\det, \mathrm{sign}\,L^0{}_0)$ of each: $(+,+), (-,+), (-,-), (+,-)$.

---

# Solution

The Lorentz group is the pseudo-orthogonal group of $\eta$ — defined, like the orthogonal group, by an invariance condition, from which the group axioms follow with no computation. Solving the condition explicitly recovers the boosts, and the determinant and time-orientation split the group into four components.

**Step 1: $O(1,1)$ is a group.**

> [!note]- Derivation
> Let $O(1,1) = \{L : L^{\mathsf T}\eta L = \eta\}$.
>
> *Identity.* $I^{\mathsf T}\eta I = \eta$, so $I \in O(1,1)$.
>
> *Closure.* Suppose $L_1, L_2 \in O(1,1)$. Then
> $$(L_1 L_2)^{\mathsf T}\eta(L_1 L_2) = L_2^{\mathsf T}\big(L_1^{\mathsf T}\eta L_1\big)L_2 = L_2^{\mathsf T}\,\eta\,L_2 = \eta,$$
> using $L_1^{\mathsf T}\eta L_1 = \eta$ then $L_2^{\mathsf T}\eta L_2 = \eta$. So $L_1 L_2 \in O(1,1)$.
>
> *Inverses.* From Step 2 below, $\det L = \pm 1 \ne 0$, so $L^{-1}$ exists. Conjugate the defining equation: from $L^{\mathsf T}\eta L = \eta$, left-multiply by $(L^{-1})^{\mathsf T} = (L^{\mathsf T})^{-1}$ and right-multiply by $L^{-1}$:
> $$(L^{-1})^{\mathsf T}\,L^{\mathsf T}\eta L\,L^{-1} = (L^{-1})^{\mathsf T}\eta L^{-1} \;\Longrightarrow\; \eta = (L^{-1})^{\mathsf T}\eta L^{-1}.$$
> So $L^{-1} \in O(1,1)$.
>
> *Associativity* is inherited from matrix multiplication. All three [[Def - Group|group axioms]] hold — and notice that not a single explicit matrix was written. This is the payoff of defining the group by an invariance: closure and the inverse property are pure consequences of the defining equation, exactly as for the orthogonal group $O(2)$ defined by $R^{\mathsf T}R = I$.

**Step 2: $\det L = \pm 1$ and $(L^0{}_0)^2 \ge 1$.**

> [!note]- Derivation
> Take the determinant of $L^{\mathsf T}\eta L = \eta$:
> $$\det(L^{\mathsf T})\,\det\eta\,\det(L) = \det\eta.$$
> Since $\det L^{\mathsf T} = \det L$ and $\det\eta = -1 \ne 0$, this gives $(\det L)^2 = 1$, hence
> $$\det L = \pm 1.$$
> For the time component, write $L = \begin{pmatrix}a & b\\c & d\end{pmatrix}$ with $a = L^0{}_0$. The $(0,0)$ entry of $L^{\mathsf T}\eta L$ is $a^2\cdot 1 + c^2\cdot(-1) = a^2 - c^2$, which must equal $\eta_{00} = 1$. So
> $$a^2 - c^2 = 1 \;\Longrightarrow\; (L^0{}_0)^2 = 1 + c^2 \ge 1.$$
> Thus $L^0{}_0 \ge 1$ or $L^0{}_0 \le -1$ — it can never lie in $(-1,1)$. The two independent binary choices, $\mathrm{sign}(\det L)$ and $\mathrm{sign}(L^0{}_0)$, partition $O(1,1)$ into (at least) four disjoint pieces.

**Step 3: The proper orthochronous piece is exactly the boosts.**

> [!note]- Derivation
> Write $L = \begin{pmatrix}a & b\\c & d\end{pmatrix}$ and impose $L^{\mathsf T}\eta L = \eta$. With $\eta = \mathrm{diag}(1,-1)$,
> $$L^{\mathsf T}\eta L = \begin{pmatrix}a & c\\b & d\end{pmatrix}\begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}\begin{pmatrix}a & b\\c & d\end{pmatrix} = \begin{pmatrix}a^2 - c^2 & ab - cd\\ab - cd & b^2 - d^2\end{pmatrix}.$$
> Setting this equal to $\mathrm{diag}(1,-1)$ gives three equations:
> $$a^2 - c^2 = 1, \qquad b^2 - d^2 = -1, \qquad ab - cd = 0.$$
> Impose the **orthochronous** condition $a = L^0{}_0 \ge 1$. From $a^2 - c^2 = 1$, the point $(a,c)$ lies on the upper branch of a hyperbola, so there is a unique $\varphi \in \mathbb{R}$ with
> $$a = \cosh\varphi, \qquad c = \sinh\varphi.$$
> From $d^2 - b^2 = 1$, similarly $d = \pm\cosh\psi$, $b = \pm\sinh\psi$ for some $\psi$. The cross equation $ab = cd$ gives $\cosh\varphi\,b = \sinh\varphi\,d$, i.e. $b/d = \tanh\varphi$, which forces $\psi = \varphi$ and the sign of $d$ positive: $d = \cosh\varphi$, $b = \sinh\varphi$. (The choice $d = -\cosh\varphi$ would give $\det L = c b - a d = \sinh^2\varphi - \cosh^2\varphi\cdot(-1)$... explicitly, with $d = \cosh\varphi$, $b = \sinh\varphi$: $\det L = ad - bc = \cosh^2\varphi - \sinh^2\varphi = +1$, the **proper** condition.)
>
> Hence the proper orthochronous elements are *exactly*
> $$L(\varphi) = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}, \qquad \varphi \in \mathbb{R},$$
> the [[Def - Rapidity|rapidity]]-parametrised boosts. The abstract definition "preserves the interval, proper, orthochronous" reproduces precisely the boosts of §1.1 — confirming that the group-theoretic and the postulate-based definitions agree.

**Step 4: The other three pieces.**

> [!note]- Derivation
> The remaining three components are obtained from the proper orthochronous piece $SO^+(1,1)$ by composing with the two discrete transformations:
> $$P = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix} \;(\textbf{parity}), \qquad T = \begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix} \;(\textbf{time reversal}).$$
> The four pieces, labelled by $(\det L,\ \mathrm{sign}\,L^0{}_0)$:
>
> - $SO^+(1,1)$, the boosts $L(\varphi)$: $(\det, \mathrm{sign}) = (+1, +)$. Identity component; preserves orientation of space and direction of time.
> - $P\cdot L(\varphi)$: $(-1, +)$. Orthochronous but improper — a boost followed by a spatial reflection $x \mapsto -x$.
> - $T\cdot L(\varphi)$: $(-1, -)$. Non-orthochronous, improper — a boost followed by time reversal $t \mapsto -t$.
> - $PT\cdot L(\varphi)$: $(+1, -)$. Non-orthochronous but proper — a boost followed by total inversion $(t,x)\mapsto(-t,-x)$.
>
> Only $SO^+(1,1)$ is a subgroup (it contains $I$); the other three are *cosets* of it. The full group is $O(1,1) = SO^+(1,1) \sqcup P\cdot SO^+(1,1) \sqcup T\cdot SO^+(1,1) \sqcup PT\cdot SO^+(1,1)$, four connected components. Physically, only $SO^+(1,1)$ relates the inertial frames of ordinary observers; $P$ and $T$ encode the discrete symmetries whose possible violation is a deep question in particle physics.

> [!note]- Complete formal solution
> $O(1,1) = \{L : L^{\mathsf T}\eta L = \eta\}$ is a group: $I$ satisfies the condition; if $L_1, L_2$ do then $(L_1L_2)^{\mathsf T}\eta(L_1L_2) = L_2^{\mathsf T}(L_1^{\mathsf T}\eta L_1)L_2 = L_2^{\mathsf T}\eta L_2 = \eta$; and conjugating the defining equation by $L^{-1}$ (which exists since $\det L \ne 0$) shows $L^{-1}$ satisfies it. Taking $\det$ gives $(\det L)^2 = 1$; the $(0,0)$ entry gives $a^2 - c^2 = 1$ so $(L^0{}_0)^2 \ge 1$ — four components. Solving $L^{\mathsf T}\eta L = \eta$ for $L = \begin{pmatrix}a&b\\c&d\end{pmatrix}$ yields $a^2-c^2=1$, $b^2-d^2=-1$, $ab=cd$; with $a\ge 1$ and $\det L = +1$ this forces $L = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$. The other three components are $P\cdot SO^+(1,1)$, $T\cdot SO^+(1,1)$, $PT\cdot SO^+(1,1)$, with $P = \mathrm{diag}(1,-1)$, $T = \mathrm{diag}(-1,1)$. $\blacksquare$

---

# Key Takeaways

**Defining a group by an invariance makes the group axioms free — never verify closure by computing matrices.** The whole of Step 1 used only the defining equation $L^{\mathsf T}\eta L = \eta$, manipulated algebraically: closure was one substitution, the inverse one conjugation. No explicit boost matrix appeared. This is the universal advantage of an invariance definition over a parametric one. The orthogonal group $O(n)$, the unitary group, the symplectic group, the Lorentz group — all are defined as "the maps preserving such-and-such a form", and for every one of them closure and inverses follow by the identical two-line argument. The lesson generalises beyond physics: whenever you meet a group defined as a stabiliser or an isometry group, prove it is a group from the defining property, not from coordinates. The coordinates are for *solving* the condition (Step 3), not for checking the axioms.

**The Lorentz group is the pseudo-orthogonal group, and "pseudo" is exactly one minus sign.** The condition $L^{\mathsf T}\eta L = \eta$ is the orthogonal-group condition $R^{\mathsf T}R = I$ with the identity replaced by $\eta = \mathrm{diag}(1,-1)$. That single sign change converts the *compact* group $O(2)$ — whose proper part is the circle of rotations — into the *non-compact* group $O(1,1)$ — whose proper part is the line of boosts. The hyperbola $a^2 - c^2 = 1$ replaces the circle $a^2 + c^2 = 1$, the hyperbolic functions replace the trigonometric ones, and an unbounded rapidity replaces a periodic angle. Recognising the Lorentz group as $O(1,1)$, a member of the pseudo-orthogonal family $O(p,q)$, places it in a known mathematical landscape: everything one knows about isometry groups of bilinear forms applies, with the proviso that the form is indefinite. The indefiniteness is the whole of relativity, and it is localised in that one sign.

**A group with several components has one subgroup — the identity component — and the rest are its cosets.** The four pieces of $O(1,1)$ are not four subgroups. Only $SO^+(1,1)$, containing the identity, is a subgroup; $P\cdot SO^+(1,1)$, $T\cdot SO^+(1,1)$, $PT\cdot SO^+(1,1)$ are cosets — they are closed under nothing, since the product of two improper transformations is proper. This is a general feature of groups built from a connected piece plus discrete symmetries: the identity component is a normal subgroup, the discrete symmetries (here $P$ and $T$, generating a copy of the Klein four-group) index the components, and the full group is the identity component extended by that finite group. The physically continuous transformations — those reachable from "do nothing" by a smooth motion — are exactly the identity component, which is why physics restricts attention to $SO^+(1,3)$; the discrete pieces $P$, $T$, $PT$ are separate symmetries whose status (are they symmetries of nature at all?) is a question rather than an assumption. The same component structure appears in $O(3)$ (two components, rotations and rotation-reflections) and in the general $O(p,q)$.
