---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Thm - The Suspension-Loop Adjunction"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a ring and $\mathrm{Ch}(R)$ the category of (unbounded) chain complexes of $R$-modules, with the projective model structure, pointed by the zero complex $0$. Its homotopy category is the derived category $D(R)$.

1. Recall the **shift** $X[1]$ of a complex $X_\bullet$: $X[1]_n = X_{n-1}$ with differential $d_{X[1]} = -d_X$. Show that the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ in this pointed model category is naturally isomorphic to $X[1]$ in $D(R)$, by computing the homotopy pushout of $0 \leftarrow X \rightarrow 0$ as a mapping cone.
2. Show dually that the [[Def - Pointed Model Category Suspension and Loop|loop]] $\Omega X$ is $X[-1]$.
3. Verify that the [[Thm - The Suspension-Loop Adjunction|suspension–loop adjunction]] $[\Sigma X, Y] \cong [X, \Omega Y]$ is the shift adjunction $[X[1], Y] \cong [X, Y[-1]]$ in $D(R)$, and observe that here $\Sigma$ is an *equivalence* (so $D(R)$ is triangulated).

**Recall:**

The [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ is the homotopy pushout of $0 \leftarrow X \rightarrow 0$. In $\mathrm{Ch}(R)$ the [[Def - Cylinder Object, Path Object, and Homotopy|cylinder]] on $X$ is the complex $X \oplus X \oplus X[1]$ realizing $X \times [0,1]$; the homotopy pushout collapsing both ends is the **mapping cone** of $X \to 0$. The mapping cone of $f : X \to Y$ is $\mathrm{Cone}(f) = Y \oplus X[1]$ with differential $\begin{pmatrix} d_Y & f \\ 0 & -d_X \end{pmatrix}$. A [[Def - Chain Map and Chain Homotopy|chain map]] is a degreewise map commuting with differentials; chain homotopy is the homotopy relation. The shift $X[1]_n = X_{n-1}$, $d_{X[1]} = -d_X$.

---

# Convergent Strategy

**Problem class:** This is a "compute the derived (co)limit in a concrete model category and identify it with a familiar algebraic operation" exercise. The route is to evaluate the homotopy pushout defining $\Sigma$ via the explicit mapping-cone formula and recognize the degree shift.

**Assumption pattern:** The assumption is that $\mathrm{Ch}(R)$ has an explicit cylinder/cone, so the homotopy pushout is computable by a formula rather than abstractly. Crucially, in $\mathrm{Ch}(R)$ the shift is *invertible* (shift down undoes shift up), which signals — and the exercise confirms — that $D(R)$ is the stable, triangulated, boundary case where $\Sigma$ is an equivalence.

**Theorem routing:** Part (1) routes through the mapping-cone formula: $\Sigma X = C_{(X \to 0)} = \mathrm{Cone}(X \to 0) = 0 \oplus X[1] = X[1]$. Part (2) routes through the dual (mapping cocone / homotopy pullback) giving $X[-1]$. Part (3) routes through the [[Thm - The Suspension-Loop Adjunction|adjunction]] and the elementary fact that shifting up by one and shifting down by one are inverse functors.

**Key decision point:** The interesting decision is to compute $\Sigma X$ as the cofiber of $X \to 0$ rather than as an abstract homotopy pushout. Recognizing "$\Sigma X =$ homotopy cofiber of $X \to *$" (the true name of suspension) turns the computation into evaluating a mapping cone with $Y = 0$, which collapses to $X[1]$ in one line. The alternative — building the full cylinder $X \oplus X \oplus X[1]$ and collapsing both ends — gives the same answer with more work.

---

# Legal Operations Used

1. **Operation 1 from the topic page (replace a strict (co)limit by its homotopy version).** The suspension is the homotopy pushout, computed via the mapping cone, not the strict pushout (which would be $0$).

2. **Operation 3 from the topic page (recognize a homotopy pushout square with a corner at $*$).** The square defining $\Sigma X$ has two corners at the zero complex, so $\Sigma X$ is the cofiber of $X \to 0$.

3. **Operation 6 from the topic page (use the suspension–loop adjunction).** Part (3) checks the adjunction is the shift adjunction.

---

# Hints

> [!note]- Hint 1
> Use the true name: $\Sigma X$ is the homotopy cofiber of $X \to 0$, i.e. the mapping cone of $X \to 0$. Plug $Y = 0$ into the mapping-cone formula $\mathrm{Cone}(f) = Y \oplus X[1]$.

> [!note]- Hint 2
> The mapping cone of $X \xrightarrow{0} 0$ is $0 \oplus X[1]$ with differential $\begin{pmatrix} d_0 & 0 \\ 0 & -d_X\end{pmatrix} = (-d_X)$ on $X[1]$. That is exactly the shift $X[1]$.

> [!note]- Hint 3
> For part (3), shifting up by one is invertible: $(X[1])[-1] = X$. So $\Sigma = [1]$ and $\Omega = [-1]$ are mutually inverse, the unit and counit of the adjunction are isomorphisms, and the adjunction bijection is just the tautology that an invertible functor and its inverse are adjoint.

---

# Solution

The solution computes $\Sigma X = X[1]$ as the mapping cone of $X \to 0$, dualizes for $\Omega X = X[-1]$, and observes the adjunction is the (invertible) shift adjunction, so $D(R)$ is triangulated.

**Step 1: $\Sigma X \simeq X[1]$ via the mapping cone of $X \to 0$.**

> [!note]- Derivation
> By the true name of suspension, $\Sigma X$ is the homotopy cofiber of $X \to 0$, i.e. the [[Def - Pullback and Pushout|homotopy pushout]] of $0 \leftarrow X \rightarrow 0$. In $\mathrm{Ch}(R)$ this homotopy pushout is the **mapping cone** of $X \to 0$. The mapping cone of a [[Def - Chain Map and Chain Homotopy|chain map]] $f : X \to Y$ is
> $$\mathrm{Cone}(f)_n = Y_n \oplus X_{n-1}, \qquad d = \begin{pmatrix} d_Y & f \\ 0 & -d_X \end{pmatrix}.$$
> Take $Y = 0$ and $f = 0$. Then $\mathrm{Cone}(0 : X \to 0)_n = 0 \oplus X_{n-1} = X_{n-1} = X[1]_n$, with differential $\begin{pmatrix} 0 & 0 \\ 0 & -d_X \end{pmatrix}$, which on the surviving summand $X[1]$ is $-d_X = d_{X[1]}$. Hence $\Sigma X = \mathrm{Cone}(X \to 0) = X[1]$. (Computing the full homotopy pushout via the cylinder $X \oplus X \oplus X[1]$ and collapsing both ends gives the same $X[1]$ after the contractible summands cancel.)

**Step 2: $\Omega X \simeq X[-1]$ dually.**

> [!note]- Derivation
> The [[Def - Pointed Model Category Suspension and Loop|loop]] $\Omega X$ is the homotopy fiber of $0 \to X$, i.e. the homotopy pullback of $0 \to X \leftarrow 0$. In $\mathrm{Ch}(R)$ this is the **mapping cocone** (shifted-down mapping cone) of $0 \to X$, which is $X[-1]$: $X[-1]_n = X_{n+1}$ with differential $-d_X$. Concretely, $\Omega = [-1]$ is forced as the right adjoint of $\Sigma = [1]$, and a direct computation of the homotopy pullback of $0 \to X \leftarrow 0$ via a path object yields $X[-1]$. Note $\Omega \Sigma X = (X[1])[-1] = X$ on the nose, so the unit $\eta$ is an isomorphism.

**Step 3: The adjunction is the shift adjunction, and $\Sigma$ is an equivalence.**

> [!note]- Derivation
> The [[Thm - The Suspension-Loop Adjunction|suspension–loop adjunction]] reads
> $$[\Sigma X, Y] = [X[1], Y] \cong [X, Y[-1]] = [X, \Omega Y].$$
> Since shifting up and shifting down are inverse functors — $[1] \circ [-1] = \mathrm{id} = [-1] \circ [1]$ — the functor $\Sigma = [1]$ is an **equivalence** of $D(R)$, with quasi-inverse $\Omega = [-1]$. The adjunction bijection is then the trivial one for an equivalence and its inverse: $[X[1], Y] \cong [X, Y[-1]]$ holds because applying $[-1]$ to a map $X[1] \to Y$ gives $X \to Y[-1]$ and vice versa, bijectively.
>
> Because $\Sigma$ is an equivalence, the pointed model category $\mathrm{Ch}(R)$ is **stable**, the unit $\eta : X \to \Omega\Sigma X$ and counit $\varepsilon : \Sigma\Omega Y \to Y$ are isomorphisms, and $D(R)$ is a **triangulated category**: the cofiber sequences $X \to Y \to \mathrm{Cone}(f) \to X[1]$ are exactly the distinguished triangles. This is the boundary case foreshadowed throughout the chapter, where pre-triangulated upgrades to triangulated precisely because suspension is invertible.

> [!note]- Complete formal solution
> **(1)** $\Sigma X$ is the homotopy cofiber of $X \to 0$, the mapping cone $\mathrm{Cone}(X \to 0)$. With $\mathrm{Cone}(f)_n = Y_n \oplus X_{n-1}$, $d = \begin{pmatrix} d_Y & f \\ 0 & -d_X\end{pmatrix}$ and $Y = 0$, $f = 0$, this is $X_{n-1} = X[1]_n$ with differential $-d_X = d_{X[1]}$. So $\Sigma X = X[1]$.
>
> **(2)** Dually $\Omega X$ is the homotopy fiber of $0 \to X$, the mapping cocone $X[-1]$, with $X[-1]_n = X_{n+1}$, $d = -d_X$. Then $\Omega\Sigma X = X$ on the nose.
>
> **(3)** The adjunction is $[X[1], Y] \cong [X, Y[-1]]$. Since $[1]$ and $[-1]$ are mutually inverse, $\Sigma$ is an equivalence with quasi-inverse $\Omega$, the unit/counit are isomorphisms, $\mathrm{Ch}(R)$ is stable, and $D(R)$ is triangulated with distinguished triangles the cofiber sequences $X \to Y \to \mathrm{Cone}(f) \to X[1]$. $\blacksquare$

---

# Key Takeaways

**Suspension is "add a dimension" in topology and "shift the grading" in homological algebra — one construction, two faces.** The computation $\Sigma X = X[1]$ is the cleanest demonstration that the abstract suspension is not a topological accident: in chain complexes it is the degree shift, an utterly algebraic operation, arising from the *same* homotopy pushout that produces the topological reduced suspension. The transferable insight is that any time you see a "shift" or "degree-raising" operation in a homotopical setting, suspect it is the suspension of the relevant pointed model category, and expect it to obey the cofiber-sequence and adjunction machinery. Recognizing the mapping cone as the homotopy cofiber is the bridge that makes this identification a one-line computation rather than a coincidence.

**Invertibility of the shift is exactly stability, and stability is exactly what makes the derived category triangulated.** The fact that $[1]$ and $[-1]$ are inverse is what separates $\mathrm{Ch}(R)$ from $\mathbf{Top}_*$: in spaces $\Sigma$ is wildly non-invertible, so $\mathrm{Ho}(\mathbf{Top}_*)$ is only pre-triangulated, whereas in chain complexes $\Sigma$ is an equivalence, so $D(R)$ is fully triangulated. The diagnostic to carry is "is $\Omega\Sigma X \simeq X$?" — if yes, the category is stable and the cofiber sequences are distinguished triangles; if no, you are in the unstable, merely pre-triangulated world. This single question is the dividing line between the two halves of the subject, and the derived category is the prototypical example of the stable side.

**The mapping cone is the homotopy cofiber, and this identification powers all of homological algebra's long exact sequences.** Once $\Sigma X = X[1]$ and $\mathrm{Cone}(f)$ is recognized as the homotopy cofiber, the cofiber sequence $X \to Y \to \mathrm{Cone}(f) \to X[1]$ becomes the distinguished triangle of $D(R)$, and applying $\mathrm{Hom}(-, Z)$ or homology to it yields the long exact sequences of Ext and of homology with their snake-lemma connecting maps. The reusable principle is that the entire long-exact-sequence calculus of homological algebra is the cofiber-sequence calculus of this chapter, specialized to chain complexes — so a technique learned for general pointed model categories transfers verbatim to computing derived functors, and vice versa.
