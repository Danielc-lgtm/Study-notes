---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Orthogonal Decomposition of 2-Forms"
  - "Def - The Hodge Star"
  - "Thm - The Complexification of so(1,3) and the (A,B) Decomposition"
tags: [physics, special-relativity]
---

# Problem Statement

Work in four-dimensional Lorentzian spacetime, mostly-minus signature, $c = 1$.

1. Since $\star^2 = -1$ on $2$-forms, the [[Def - The Hodge Star|Hodge star]] has no real eigenvalues. Complexify $\mathscr{A}_2(E)$ and build the projectors $P^\pm = \tfrac12(1 \mp i\star)$ onto the $\pm i$ eigenspaces; verify they are complementary projectors with $\star P^\pm = \pm iP^\pm$.
2. Define the **self-dual** ($\mathscr{A}_2^+$, eigenvalue $+i$) and **anti-self-dual** ($\mathscr{A}_2^-$, eigenvalue $-i$) $2$-forms, and show each has complex dimension $3$, with $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2^+ \oplus \mathscr{A}_2^-$.
3. For the field strength $F$ with parts $(\mathbf E, \mathbf B)$, show that the self-dual part $F^+ = P^+F$ is built from the Riemann-Silberstein combination $\mathbf E + i\mathbf B$, and the anti-self-dual part from $\mathbf E - i\mathbf B$.
4. Match the decomposition to the $(1,0)\oplus(0,1)$ representation of the [[Def - Lie Algebra of the Lorentz Group|Lorentz algebra]]: the self-dual $2$-forms carry $(1,0)$ and the anti-self-dual carry $(0,1)$, and the projectors $P^\pm$ correspond to the algebra generators $\mathbf J \pm i\mathbf K$.

**Recall:**

![[Thm - Orthogonal Decomposition of 2-Forms#Statement]]

The [[Def - The Hodge Star|Hodge star]] satisfies $\star^2 = -1$ on $2$-forms. The complexified Lorentz algebra splits as $\mathfrak{so}(1,3)_\mathbb{C} \cong \mathfrak{su}(2)_+ \oplus \mathfrak{su}(2)_-$ via the combinations $\mathbf N_\pm = \tfrac12(\mathbf J \pm i\mathbf K)$ of the rotation generators $\mathbf J$ and boost generators $\mathbf K$; see [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]]. A representation is labelled $(A, B)$ by the spins of the two $\mathfrak{su}(2)$ factors.

---

# Convergent Strategy

**Problem class.** A *structural* and *decompose-an-object* problem — the capstone of the chapter — connecting the [[Def - The Hodge Star|Hodge star]] on $2$-forms to the [[Def - Lie Algebra of the Lorentz Group|representation theory]] of the Lorentz group. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: $\star^2 = -1$ means $\star$ is a complex structure, so complexify and diagonalise.

**Assumption pattern.** The single input is $\star^2 = -1$ on $2$-forms. This is exactly the condition for an operator to have eigenvalues $\pm i$ over $\mathbb{C}$ and to define a complex structure. The Riemann-Silberstein identification uses the field-strength duality $\star : (\mathbf E, \mathbf B) \to (-\mathbf B, \mathbf E)$. The representation-theoretic match uses the parallel structure $\mathbf N_\pm = \tfrac12(\mathbf J \pm i\mathbf K)$.

**Theorem routing.** Part 1: verify the projector identities from $\star^2 = -1$. Part 2: dimension count via complex conjugation swapping eigenspaces. Part 3: apply $\star$ to the $(\mathbf E, \mathbf B)$ parts and read off $\mathbf E \pm i\mathbf B$. Part 4: identify $\star$ on $2$-forms with the action of the algebra's complex structure, matching $P^\pm \leftrightarrow \mathbf N_\pm$.

**Key decision point.** The crux is recognising that *three* a priori different $\pm i$ decompositions are the *same* decomposition: (a) the eigenspaces of $\star$ on $2$-forms; (b) the Riemann-Silberstein split $\mathbf E \pm i\mathbf B$ of the electromagnetic field; (c) the $(1,0)\oplus(0,1)$ split of the adjoint representation of the Lorentz group via $\mathbf J \pm i\mathbf K$. Seeing that the Hodge star *is* the complex structure that realises the chiral decomposition of the Lorentz algebra on the space of fields — that these are one phenomenon — is the deep payoff of the entire chapter.

---

# Legal Operations Used

1. **Operation 10 from the topic page (complexify and project onto self-dual / anti-self-dual parts).** The entire exercise: forming $P^\pm = \tfrac12(1 \mp i\star)$ and the eigenspaces.

2. **Operation 7 from the topic page (invert the Hodge star with the sign rule).** Uses $\star^2 = -1$ throughout to verify the projector algebra.

3. **Operation 9 from the topic page (decompose a $2$-form relative to an observer).** Part 3 uses the observer's $(\mathbf E, \mathbf B)$ split to express the self-dual part.

---

# Hints

> [!note]- Hint 1
> Check $P^+ + P^- = 1$, $(P^\pm)^2 = P^\pm$, $P^+P^- = 0$, and $\star P^\pm = \pm iP^\pm$, using only $\star^2 = -1$. E.g. $(P^+)^2 = \tfrac14(1 - i\star)^2 = \tfrac14(1 - 2i\star - \star^2) = \tfrac14(2 - 2i\star) = P^+$.

> [!note]- Hint 2
> The two eigenspaces are complex conjugates: complex conjugation fixes the real operator $\star$ but sends $i \to -i$, so it maps the $+i$ eigenspace to the $-i$ eigenspace. Hence they have equal dimension, summing to $\dim_\mathbb{C}\mathscr{A}_2(E)_\mathbb{C} = 6$, so each is $3$.

> [!note]- Hint 3
> $\star$ acts on the field as $(\mathbf E, \mathbf B) \mapsto (-\mathbf B, \mathbf E)$. So $-i\star F$ has parts $(-i)(-\mathbf B, \mathbf E) = (i\mathbf B, -i\mathbf E)$, and $F^+ = \tfrac12(F - i\star F)$ has electric part $\tfrac12(\mathbf E + i\mathbf B)$ — proportional to $\mathbf E + i\mathbf B$. Self-duality $\star F^+ = iF^+$ means the magnetic part is $-i$ times the electric part.

> [!note]- Hint 4
> Both $\star$ (on $2$-forms) and the algebra's complex structure (via $\mathbf J \pm i\mathbf K$) split a six-real-dimensional space into two three-complex-dimensional pieces by the *same* eigenvalue $\pm i$. A $2$-form transforms in the adjoint $= (1,0)\oplus(0,1)$; the self-dual part is the $(1,0)$ summand, on which $\mathbf N_- = \tfrac12(\mathbf J - i\mathbf K)$ acts trivially.

---

# Solution

This is the chapter's summit: $\star^2 = -1$ forces a complex decomposition of the $2$-forms that is simultaneously the Riemann-Silberstein split of electromagnetism and the chiral $(1,0)\oplus(0,1)$ split of the Lorentz group. The plan: build the eigenprojectors of $\star$ (Step 1), establish the self-dual/anti-self-dual decomposition with its $3+3$ dimensions (Step 2), identify the parts with $\mathbf E \pm i\mathbf B$ (Step 3), and match to the Lorentz representations (Step 4).

**Step 1: the projectors $P^\pm = \tfrac12(1 \mp i\star)$.**

> [!note]- Derivation
> Since $\star^2 = -1$ on $\mathscr{A}_2(E)$, the Hodge star is a real linear operator with no real eigenvalues; complexify to $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2(E)\otimes\mathbb{C}$. Define $P^\pm = \tfrac12(1 \mp i\star)$ and verify the projector algebra using only $\star^2 = -1$:
> - *Complementary:* $P^+ + P^- = \tfrac12(1 - i\star) + \tfrac12(1 + i\star) = 1$.
> - *Idempotent:* $(P^\pm)^2 = \tfrac14(1 \mp i\star)^2 = \tfrac14(1 \mp 2i\star + i^2\star^2) = \tfrac14(1 \mp 2i\star - (-1)) = \tfrac14(2 \mp 2i\star) = \tfrac12(1 \mp i\star) = P^\pm$.
> - *Orthogonal:* $P^+P^- = \tfrac14(1 - i\star)(1 + i\star) = \tfrac14(1 + i\star - i\star - i^2\star^2) = \tfrac14(1 + \star^2)\cdot... = \tfrac14(1 - 1) = 0$.
> - *Eigenprojection:* $\star P^\pm = \tfrac12(\star \mp i\star^2) = \tfrac12(\star \pm i) = \pm i\cdot\tfrac12(1 \mp i\star) = \pm iP^\pm$.
>
> So $P^\pm$ are complementary, idempotent, orthogonal projectors, and $P^\pm$ projects onto the $\pm i$ eigenspace of $\star$. Every $2$-form decomposes as $A = P^+A + P^-A = A^+ + A^-$.

**Step 2: the self-dual / anti-self-dual decomposition, $3 + 3$.**

> [!note]- Derivation
> Define the **self-dual** and **anti-self-dual** subspaces as the eigenspaces:
> $$\mathscr{A}_2^+ = \{F \in \mathscr{A}_2(E)_\mathbb{C} : \star F = +iF\} = P^+(\mathscr{A}_2(E)_\mathbb{C}), \qquad \mathscr{A}_2^- = \{F : \star F = -iF\} = P^-(\mathscr{A}_2(E)_\mathbb{C}).$$
> Since $P^\pm$ are complementary, $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2^+ \oplus \mathscr{A}_2^-$. For the dimensions: complex conjugation is a real operation that fixes the real Hodge star $\star$ but conjugates the eigenvalue, $\overline{iF} = -i\bar F$. So if $\star F = iF$ then $\star\bar F = \overline{\star F} = \overline{iF} = -i\bar F$, meaning conjugation sends $\mathscr{A}_2^+$ to $\mathscr{A}_2^-$ bijectively. Hence $\dim_\mathbb{C}\mathscr{A}_2^+ = \dim_\mathbb{C}\mathscr{A}_2^-$, and since they sum to $\dim_\mathbb{C}\mathscr{A}_2(E)_\mathbb{C} = 6$,
> $$\dim_\mathbb{C}\mathscr{A}_2^+ = \dim_\mathbb{C}\mathscr{A}_2^- = 3.$$
> A self-dual $2$-form is determined by three complex numbers — exactly the components of a single complex three-vector, which will be $\mathbf E + i\mathbf B$.

**Step 3: $F^+$ from $\mathbf E + i\mathbf B$.**

> [!note]- Derivation
> Decompose $F$ relative to an observer into electric and magnetic parts $(\mathbf E, \mathbf B)$. The Hodge star acts (from [[Ex - Computing the Hodge dual of a 2-form]]) as the quarter-turn $\star : (\mathbf E, \mathbf B) \mapsto (-\mathbf B, \mathbf E)$. Compute the self-dual projection $F^+ = P^+F = \tfrac12(F - i\star F)$ in terms of parts:
> $$F = (\mathbf E, \mathbf B), \qquad -i\star F = -i(-\mathbf B, \mathbf E) = (i\mathbf B, -i\mathbf E),$$
> so
> $$F^+ = \tfrac12\big[(\mathbf E, \mathbf B) + (i\mathbf B, -i\mathbf E)\big] = \tfrac12\big(\mathbf E + i\mathbf B,\ \mathbf B - i\mathbf E\big) = \tfrac12\big(\mathbf E + i\mathbf B,\ -i(\mathbf E + i\mathbf B)\big).$$
> Both the electric and the magnetic part of $F^+$ are proportional to the single complex vector
> $$\boxed{\ \mathbf F^+ = \mathbf E + i\mathbf B\ }$$
> (the **Riemann-Silberstein vector**), with the magnetic part equal to $-i$ times the electric part — which is exactly the self-duality condition $\star F^+ = iF^+$ written in rest-space components. Likewise $F^- = P^-F = \tfrac12(F + i\star F)$ is built from $\mathbf F^- = \mathbf E - i\mathbf B$. So the self-dual and anti-self-dual parts of the field strength are precisely the two complex combinations $\mathbf E \pm i\mathbf B$ — the two helicities of the electromagnetic field. (Maxwell's source-free equations for $\mathbf F^\pm$ become the single first-order equation $i\partial_t\mathbf F^\pm = \pm\nabla\times\mathbf F^\pm$.)

**Step 4: matching to $(1,0)\oplus(0,1)$ of the Lorentz algebra.**

> [!note]- Derivation
> A $2$-form transforms in the **adjoint representation** of the [[Def - The Lorentz Group|Lorentz group]] (six-dimensional, the same dimension as the algebra), because the space of antisymmetric $2$-tensors is isomorphic to $\mathfrak{so}(1,3)$ via $A_{\mu\nu} \leftrightarrow$ generator. By [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]], the complexified algebra splits as
> $$\mathfrak{so}(1,3)_\mathbb{C} \cong \mathfrak{su}(2)_+ \oplus \mathfrak{su}(2)_-, \qquad \mathbf N_\pm = \tfrac12(\mathbf J \pm i\mathbf K),$$
> where $\mathbf J$ are the rotation and $\mathbf K$ the boost generators, and the adjoint representation decomposes as $(1,0)\oplus(0,1)$ — a spin-$1$ of $\mathfrak{su}(2)_+$ (three-dimensional) plus a spin-$1$ of $\mathfrak{su}(2)_-$ (three-dimensional).
>
> The match is exact: the Hodge star $\star$ on $2$-forms acts as the *same* complex structure that the combination $\mathbf J \pm i\mathbf K$ implements on the algebra. Concretely, under the identification of $2$-forms with generators, $\star$ corresponds to "multiply the boost part by $i$ and rotate" — and the $+i$ eigenspace of $\star$ (the self-dual $2$-forms $\mathscr{A}_2^+$) is exactly the $(1,0)$ summand, on which $\mathbf N_- = \tfrac12(\mathbf J - i\mathbf K)$ acts trivially and $\mathbf N_+$ acts as spin $1$. The projectors $P^\pm = \tfrac12(1 \mp i\star)$ on forms are the image of the algebra projectors onto $\mathfrak{su}(2)_\pm$. So:
> $$\mathscr{A}_2^+ \leftrightarrow (1,0), \qquad \mathscr{A}_2^- \leftrightarrow (0,1),$$
> and the self-dual / anti-self-dual decomposition of the electromagnetic field *is* the chiral $(1,0)\oplus(0,1)$ decomposition of the field strength under the Lorentz group. The two helicities $\mathbf E \pm i\mathbf B$ are the left-handed and right-handed pieces, and a parity transformation (which swaps $\mathbf J$-even, $\mathbf K$-odd, hence $\mathbf N_+ \leftrightarrow \mathbf N_-$) exchanges them.

> [!note]- Complete formal solution
> **(1)** With $\star^2 = -1$: $P^\pm = \tfrac12(1 \mp i\star)$ satisfy $P^+ + P^- = 1$, $(P^\pm)^2 = P^\pm$, $P^+P^- = 0$, $\star P^\pm = \pm iP^\pm$.
> **(2)** $\mathscr{A}_2^\pm = P^\pm(\mathscr{A}_2(E)_\mathbb{C})$ are the $\pm i$ eigenspaces; complex conjugation swaps them, so each has dimension $3$, and $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2^+ \oplus \mathscr{A}_2^-$.
> **(3)** With $\star : (\mathbf E, \mathbf B) \mapsto (-\mathbf B, \mathbf E)$, $F^+ = \tfrac12(F - i\star F)$ has both parts proportional to $\mathbf E + i\mathbf B$; $F^-$ to $\mathbf E - i\mathbf B$. These are the Riemann-Silberstein combinations / two helicities.
> **(4)** A $2$-form is in the adjoint $= (1,0)\oplus(0,1)$; $\star$ realises the complex structure $\mathbf J \pm i\mathbf K$, so $\mathscr{A}_2^+ \leftrightarrow (1,0)$, $\mathscr{A}_2^- \leftrightarrow (0,1)$, and $P^\pm \leftrightarrow \mathbf N_\pm$. $\blacksquare$

---

# Key Takeaways

**An operator with $\star^2 = -1$ is a complex structure, and complexifying is the *only* way to diagonalise it.** The mechanical heart of the exercise is that $\star^2 = -1$ has no real solution, so $\star$ cannot be diagonalised over $\mathbb{R}$ — but over $\mathbb{C}$ it has eigenvalues $\pm i$, and the projectors $\tfrac12(1 \mp i\star)$ split the complexified space into eigenspaces. This is a completely general technique: any real operator $J$ with $J^2 = -1$ (a *complex structure*) is "multiplication by $i$," and the right move is always to complexify and project with $\tfrac12(1 \mp iJ)$. The same construction diagonalises the complex structure of a Kähler manifold (splitting forms into holomorphic and anti-holomorphic types), the operator $i$ on a real vector space underlying a complex one, and the Hodge star on middle-degree forms in Lorentzian signature. The reusable trigger: $J^2 = -1$ means "complexify and use $\tfrac12(1 \mp iJ)$," and the appearance of $i$ is forced, not chosen. Recognising the Hodge star on $2$-forms as a complex structure is what unlocks the entire decomposition.

**The Riemann-Silberstein vector $\mathbf E + i\mathbf B$ is the self-dual part of the field, and it is the photon's helicity.** The combination $\mathbf F^\pm = \mathbf E \pm i\mathbf B$ is not an algebraic trick but the eigenform of the Hodge star, and it packages the electromagnetic field into a single complex three-vector on which Maxwell's source-free equations become one first-order equation $i\partial_t\mathbf F^\pm = \pm\nabla\times\mathbf F^\pm$ — the closest classical analogue of a Schrödinger equation for the photon. The self-dual part $\mathbf F^+$ is positive helicity, the anti-self-dual $\mathbf F^-$ negative helicity, and a circularly polarised wave is purely one or the other. The reusable insight is that the two helicities of any massless field of definite spin are its self-dual and anti-self-dual parts, and the Hodge star is the operator that separates them. This is why the field invariants $\mathbf B^2 - \mathbf E^2$ and $\mathbf E\cdot\mathbf B$ combine into the single complex invariant $(\mathbf E + i\mathbf B)^2$ — they are the real and imaginary parts of the squared length of the self-dual part — and why a null (radiation) field is exactly one whose self-dual part is a null complex vector.

**Three decompositions are one: the Hodge star realises the chiral $(1,0)\oplus(0,1)$ split of the Lorentz group on the space of fields.** The deepest payoff of the chapter is that the $\pm i$ eigenspaces of $\star$ on $2$-forms, the Riemann-Silberstein split $\mathbf E \pm i\mathbf B$, and the $(1,0)\oplus(0,1)$ decomposition of the adjoint representation of the Lorentz group via $\mathbf J \pm i\mathbf K$ are the *same* decomposition seen three ways. A $2$-form lives in the adjoint representation, which is reducible into a left-handed $(1,0)$ and a right-handed $(0,1)$ piece; the Hodge star is the complex structure that effects this split, and its eigenprojectors $\tfrac12(1 \mp i\star)$ are the image of the algebra projectors $\mathbf N_\pm = \tfrac12(\mathbf J \pm i\mathbf K)$ onto the two $\mathfrak{su}(2)$ factors. The transferable lesson is that the Hodge star is not merely a computational device — it is the geometric realisation, on the space of fields, of the chiral decomposition of the Lorentz group, and the chirality of the electromagnetic field, the helicity of the photon, and the left/right asymmetry that the Standard Model exploits all trace to this single $\star^2 = -1$. This connects [[Special Relativity X — The Lorentz Group as a Lie Group|the Lie-algebraic representation theory]] to the [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map|spinor formalism]] (where self-dual and anti-self-dual field strengths are written with two undotted or two dotted indices, $F^+_{AB}$ and $F^-_{\dot A\dot B}$), and it is the conceptual bridge from the algebra of forms to the representation theory of relativistic fields — the reason this chapter is the machinery that makes the electromagnetic chapters, and ultimately quantum field theory, clean.
