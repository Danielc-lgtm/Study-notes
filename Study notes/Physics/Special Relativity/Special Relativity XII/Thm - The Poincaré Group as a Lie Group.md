---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Poincaré Group"
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - The Poincaré Group|Poincaré group]] is $\mathrm{ISO}(1,3) \simeq \mathbb{R}^4\rtimes\mathrm{O}(1,3)$; its elements are pairs $(\boldsymbol{v}, \Lambda)$ with $\boldsymbol{v}\in E$ a translation vector and $\Lambda\in\mathrm{O}(1,3)$ a [[Def - The Lorentz Group|Lorentz transformation]], composing by $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$. The [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]] is $\mathfrak{so}(1,3)$, with $L\in\mathfrak{so}(1,3)$ an infinitesimal Lorentz transformation (so $\Lambda = \mathrm{Id} + \varepsilon L + O(\varepsilon^2)$); its generators are the boosts $K_i$ and rotations $J_i$ ($i = 1,2,3$). The Poincaré algebra is $\mathfrak{iso}(1,3)$. An orthonormal basis of $E$ is $(e_\alpha)$, $\alpha = 0\ldots3$. $\delta_{ij}$ is the Kronecker delta and $\epsilon_{ijk}$ the three-dimensional Levi-Civita symbol. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---

# Statement

> **The Poincaré group as a Lie group.** The Poincaré group $\mathrm{ISO}(1,3) \simeq \mathbb{R}^4\rtimes\mathrm{O}(1,3)$ is a Lie group of dimension
> $$\dim \mathrm{ISO}(1,3) = 4 + 6 = 10.$$
> Its Lie algebra is the semidirect sum
> $$\mathfrak{iso}(1,3) = E \rtimes \mathfrak{so}(1,3),$$
> the vector space $E\times\mathfrak{so}(1,3)$ (dimension $4 + 6 = 10$) with addition $(\boldsymbol{v}_1, L_1) + (\boldsymbol{v}_2, L_2) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, L_1 + L_2)$ and the Lie bracket
> $$\big[(\boldsymbol{v}_1, L_1),\, (\boldsymbol{v}_2, L_2)\big] = \big(L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1,\; [L_1, L_2]\big),$$
> where $[L_1, L_2] = L_1 L_2 - L_2 L_1$ is the commutator in $\mathfrak{so}(1,3)$. In terms of the ten generators — translations $P_\alpha = (e_\alpha, 0)$, boosts $K_i = (0, K_i)$, rotations $J_i = (0, J_i)$ — the non-vanishing structure relations are
> $$[P_\alpha, P_\beta] = 0, \qquad [K_i, P_0] = P_i, \qquad [K_i, P_j] = \delta_{ij}P_0, \qquad [J_i, P_0] = 0, \qquad [J_i, P_j] = \epsilon_{ijk}P_k,$$
> together with the Lorentz brackets $[J_i, J_j] = \epsilon_{ijk}J_k$, $[J_i, K_j] = \epsilon_{ijk}K_k$, $[K_i, K_j] = -\epsilon_{ijk}J_k$ inherited from $\mathfrak{so}(1,3)$.

---

# Motivation

The Poincaré group has been built as an abstract group with a twisted composition law. The next question is whether it is a *Lie* group — a group that is also a smooth manifold, so that one can speak of infinitesimal Poincaré transformations, generators, and the exponential map — and if so, what its Lie algebra is. The answer is yes, and the dimension is immediate: a semidirect product of a four-dimensional translation group and a six-dimensional Lorentz group is a ten-dimensional manifold. The ten generators are the four translations, three rotations, and three boosts, and they are the ten conserved quantities of relativistic physics (energy, momentum, angular momentum, and centre-of-energy).

The genuinely interesting content is the Lie *bracket*, and here the Poincaré group poses a problem the Lorentz group did not. When we built $\mathfrak{so}(1,3)$ in [[Special Relativity X — The Lorentz Group as a Lie Group]], the bracket came for free: the Lorentz group is a group of matrices, its Lie algebra is a space of matrices, and the bracket is the matrix commutator $[A, B] = AB - BA$. The Poincaré group is *not* naturally a group of matrices — its elements are affine maps of spacetime, and an affine map is not a linear endomorphism whose commutator one can take. So the bracket cannot be borrowed; it must be *constructed*. This theorem does so the way the bracket is defined for *any* Lie group: as the leading-order measure of how much two infinitesimal group elements fail to commute, read directly off the group composition law. The result is the formula $[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$, and seeing it emerge from the composition law — rather than be handed down as a commutator — is the clearest illustration in all of physics of what a Lie bracket actually *is*.

The structure constants that come out are the commutation relations of relativistic quantum mechanics. The bracket $[J_i, P_j] = \epsilon_{ijk}P_k$ says momentum is a vector under rotations; $[K_i, P_0] = P_i$ says energy turns into momentum under a boost; $[K_i, P_j] = \delta_{ij}P_0$ says momentum turns into energy. Every relativistic field theory is built so that its fields carry a representation of exactly this algebra, which is why the present theorem, abstract though it looks, is the kinematic skeleton onto which all of quantum field theory is hung.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "we have the Poincaré group with its semidirect composition law". Recognising the disguises:

The first disguised source is **"a group is a semidirect product $N\rtimes H$ of Lie groups"**. Any such product is automatically a Lie group of dimension $\dim N + \dim H$, with Lie algebra the semidirect sum, by exactly the construction here. So whenever a symmetry group is presented as a semidirect product — the Euclidean group $\mathbb{R}^3\rtimes\mathrm{O}(3)$, the Galilean group, the affine group $\mathbb{R}^n\rtimes\mathrm{GL}(n)$ — the same dimension count and bracket formula apply. The bridge is that the semidirect structure determines the manifold and the algebra mechanically. *Example problem:* find the dimension and Lie algebra of the Euclidean group of rigid motions of $\mathbb{R}^3$.

The second disguised source is **"a group composition law is given, smooth in its parameters"**. To extract a Lie algebra one needs only a smooth composition law; the bracket is then the second-order term in the expansion of $g(\varepsilon)h(\varepsilon)g(\varepsilon)^{-1}h(\varepsilon)^{-1}$. So any concretely-presented Lie group, even one with no matrix realisation, yields its algebra this way. The bridge is the general construction of the Lie algebra of a Lie group from the group multiplication ([[Def - The Lie Algebra of a Lie Group]]). *Example problem:* compute the bracket of a Lie group given only its multiplication rule in coordinates.

The third disguised source is **"the Lorentz algebra brackets and the action of generators on vectors are known"**. The Poincaré structure constants are assembled from the $\mathfrak{so}(1,3)$ brackets plus the action of $K_i, J_i$ on the basis vectors $e_\alpha$. So any problem that supplies these two ingredients — the Lorentz commutators and the matrices $K_i, J_i$ — supplies everything needed to compute a Poincaré bracket. The bridge is the intrinsic bracket formula, whose first slot is $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$, evaluated using the known action. *Example problem:* compute $[K_i, P_j]$ given the boost matrix's action $K_i(e_0) = e_i$, $K_i(e_j) = \delta_{ij}e_0$.

**Targets (Output Amplification)**

The conclusion is "$\mathrm{ISO}(1,3)$ is a ten-dimensional Lie group with this bracket and these structure constants".

Combine the conclusion with **the exponential map**. The exponential map carries the Lie algebra back to the identity component of the group, so any element of $\mathfrak{iso}(1,3)$ exponentiates to a finite Poincaré transformation. The further result is that a generic restricted Poincaré transformation is $\exp(\boldsymbol{a}\cdot P + \tfrac12\omega_{\mu\nu}J^{\mu\nu})$ for a translation $\boldsymbol{a}$ and an antisymmetric $\omega$. The combination is what lets one parametrise and compute with finite transformations via their generators. *Example:* writing a boost as $\exp(\zeta K_1)$ with rapidity $\zeta$.

Combine the conclusion with **the Casimir construction**. Once the algebra and its brackets are in hand, one can look for operators commuting with all generators — the Casimirs. The further result is the pair $P^2$ and $W^2$ that label the irreducible representations ([[Def - Casimir Invariants of the Poincaré Group]]). The combination is nonobvious because the spin Casimir $W^2$ requires the Pauli–Lubanski vector, a specific quadratic combination built from the structure the theorem provides. *Example:* verifying $[P^2, J_{\mu\nu}] = 0$ from the brackets.

Combine the conclusion with **the unitary representation theory**. The algebra's generators, promoted to Hermitian operators, become the energy–momentum and angular-momentum observables, and the structure constants become their commutation relations. The further result is the whole apparatus of relativistic quantum mechanics — the algebra of observables that any relativistic quantum system must represent. The combination is the bridge from the geometry of this chapter to quantum field theory. *Example:* the Heisenberg-like relation $[K_i, P_0] = iP_i$ governing how energy and momentum transform under boosts in a quantum theory.

---

# Why Is It True

The dimension is the easy half: a manifold that is a product (as a manifold, before worrying about the group law) of a four-dimensional $\mathbb{R}^4$ and a six-dimensional $\mathrm{O}(1,3)$ is ten-dimensional. The semidirect twist affects the *group* structure but not the underlying manifold, so the dimension is simply $4 + 6 = 10$.

The bracket is the half worth dwelling on, and the key idea is that **the Lie bracket measures the failure of two infinitesimal group elements to commute, and you read it off whatever composition law you have.** Take two infinitesimal Poincaré transformations $f_1 = (\varepsilon\boldsymbol{v}_1, \mathrm{Id} + \varepsilon L_1)$ and $f_2 = (\varepsilon\boldsymbol{v}_2, \mathrm{Id} + \varepsilon L_2)$, each a small displacement from the identity controlled by a parameter $\varepsilon$. Compose them in both orders and subtract. Using the semidirect law, the product $f_1 f_2$ has translation part $\varepsilon\boldsymbol{v}_1 + (\mathrm{Id} + \varepsilon L_1)(\varepsilon\boldsymbol{v}_2) = \varepsilon(\boldsymbol{v}_1 + \boldsymbol{v}_2) + \varepsilon^2 L_1\boldsymbol{v}_2$ and Lorentz part $(\mathrm{Id}+\varepsilon L_1)(\mathrm{Id}+\varepsilon L_2) = \mathrm{Id} + \varepsilon(L_1 + L_2) + \varepsilon^2 L_1 L_2$. Swapping $1\leftrightarrow2$ and subtracting, the linear-in-$\varepsilon$ terms cancel (the algebra is commutative to first order, as it must be), and the surviving $\varepsilon^2$ terms are exactly the bracket: translation part $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$, Lorentz part $L_1 L_2 - L_2 L_1 = [L_1, L_2]$. **The bracket is the $\varepsilon^2$ remainder of $f_1 f_2 - f_2 f_1$, and the lone factor $L_1$ in the semidirect law is what puts $L_1\boldsymbol{v}_2$, not $\boldsymbol{v}_2$, into the first slot.**

Why this *must* be the bracket, and not a matter of choice: a Lie bracket is required to be bilinear, antisymmetric, and to satisfy the Jacobi identity, and it must reproduce the group's non-commutativity to leading order. The formula above is manifestly bilinear and antisymmetric (swapping $1\leftrightarrow2$ flips the sign), it lands inside $\mathfrak{iso}(1,3)$ (the first slot $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1\in E$ since $L_i$ act on $E$, the second slot $[L_1,L_2]\in\mathfrak{so}(1,3)$), and one checks Jacobi holds (inherited from Jacobi in $\mathfrak{so}(1,3)$ and the linearity of the action). So it satisfies every axiom of a Lie bracket and reproduces the group law to second order — by the general theory it *is* the bracket of the Lie algebra, the same one the abstract functorial construction produces.

The structure constants then follow by feeding the generators into this formula. The translations all sit in the first slot with zero Lorentz part, so $[P_\alpha, P_\beta] = (0\cdot e_\beta - 0\cdot e_\alpha, [0,0]) = 0$ — translations commute, the abelian normal subgroup. The boost $K_i$ and rotation $J_i$ sit in the second slot with zero translation part, so their bracket with $P_\alpha = (e_\alpha, 0)$ is $[(e_\alpha, 0), (0, K_i)] = (0 - K_i e_\alpha, 0) = (-K_i e_\alpha, 0)$, i.e. $[K_i, P_\alpha] = (K_i e_\alpha, 0)$ up to the antisymmetry sign — and one reads off the action $K_i e_0 = e_i$, $K_i e_j = \delta_{ij}e_0$ to get $[K_i, P_0] = P_i$, $[K_i, P_j] = \delta_{ij}P_0$. Similarly $J_i e_0 = 0$ and $J_i e_j = \epsilon_{ijk}e_k$ give $[J_i, P_0] = 0$, $[J_i, P_j] = \epsilon_{ijk}P_k$. Every structure constant is just the action of a Lorentz generator on a basis vector, packaged by the bracket formula.

---

# What Makes This Hard

The conceptual obstacle is letting go of the matrix commutator. Having built $\mathfrak{so}(1,3)$ as matrices, one instinctively wants the Poincaré bracket to be a commutator too — but the Poincaré group is not a matrix group, and the affine maps $(\boldsymbol{v}, \Lambda)$ have no commutator to take. The non-obvious step is realising that the bracket must instead be *defined* from the composition law, as the second-order term in $f_1 f_2 - f_2 f_1$, and that this is in fact the general definition the matrix case merely specialises. The common error is to write $[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (\boldsymbol{v}_1\times\boldsymbol{v}_2 \text{ or } 0, [L_1, L_2])$ — forgetting the cross-term $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$ that couples the translations to the Lorentz part — which loses exactly the brackets $[K_i, P_\alpha]$ and $[J_i, P_\alpha]$ that make the algebra non-trivial. (One *can* embed the Poincaré group in $5\times5$ matrices via homogeneous coordinates, $(\boldsymbol{v},\Lambda)\mapsto\left(\begin{smallmatrix}\Lambda & \boldsymbol{v}\\ 0 & 1\end{smallmatrix}\right)$, recovering the commutator — but the intrinsic construction is the point, and the embedding is a convenience.)

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The dimension is $4 + 6 = 10$ from the semidirect product. For the bracket, expand the composition of two infinitesimal Poincaré transformations to second order in $\varepsilon$, antisymmetrise, and read off the bracket; verify it is bilinear, antisymmetric, lands in the algebra, and satisfies Jacobi. Then feed the generators $P_\alpha = (e_\alpha, 0)$, $K_i = (0, K_i)$, $J_i = (0, J_i)$ into the bracket, using the known action of $K_i, J_i$ on the basis vectors, to get the structure constants.

**Subgoal decomposition:**

1. **Dimension.** Show $\dim\mathrm{ISO}(1,3) = 10$.
   - *Hint:* As a manifold it is $\mathbb{R}^4\times\mathrm{O}(1,3)$, dimensions $4$ and $6$.
   - *Why needed:* Fixes the size of the algebra, $\dim\mathfrak{iso}(1,3) = 10$.

2. **Extract the bracket from the composition law.** Compose $f_1 = (\varepsilon\boldsymbol{v}_1, \mathrm{Id}+\varepsilon L_1)$ and $f_2$ both ways, subtract, keep $O(\varepsilon^2)$.
   - *Hint:* The semidirect law gives translation part $\varepsilon(\boldsymbol{v}_1+\boldsymbol{v}_2) + \varepsilon^2 L_1\boldsymbol{v}_2$; antisymmetrising kills the linear term and leaves $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$.
   - *Why needed:* This *is* the bracket; the cross-term is the whole content.

3. **Verify the Lie-algebra axioms.** Check bilinearity, antisymmetry, closure, Jacobi.
   - *Hint:* Bilinearity and antisymmetry are visible; closure because $L_i\boldsymbol{v}_j\in E$ and $[L_1,L_2]\in\mathfrak{so}(1,3)$; Jacobi inherited from $\mathfrak{so}(1,3)$ plus linearity of the action.
   - *Why needed:* Confirms the formula is a genuine Lie bracket.

4. **Compute the structure constants.** Plug in the generators and the action $K_i e_0 = e_i$, $K_i e_j = \delta_{ij}e_0$, $J_i e_0 = 0$, $J_i e_j = \epsilon_{ijk}e_k$.
   - *Hint:* $[P_\alpha, P_\beta] = 0$; $[K_i, P_\alpha] = (K_i e_\alpha, 0)$; $[J_i, P_\alpha] = (J_i e_\alpha, 0)$.
   - *Why needed:* Produces the explicit relations $[K_i, P_0] = P_i$, $[K_i, P_j] = \delta_{ij}P_0$, $[J_i, P_0] = 0$, $[J_i, P_j] = \epsilon_{ijk}P_k$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Poincaré group is a ten-dimensional smooth manifold
> **Statement:** $\mathrm{ISO}(1,3)$ is a Lie group of dimension $10$.
>
> **Hint:** A semidirect product of Lie groups is a Lie group whose underlying manifold is the product manifold.
>
> **Why needed:** Establishes that there is a Lie algebra at all, of the right dimension.
>
> > [!note]- Full proof
> > As a set, $\mathrm{ISO}(1,3) = E\times\mathrm{O}(1,3) \cong \mathbb{R}^4\times\mathrm{O}(1,3)$. Give it the product smooth structure: $\mathbb{R}^4$ is a four-dimensional manifold and $\mathrm{O}(1,3)$ is a six-dimensional Lie group ([[Special Relativity X — The Lorentz Group as a Lie Group]]). The group multiplication $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ is smooth in all arguments (it is built from addition, the smooth action $(\Lambda, \boldsymbol{v})\mapsto\Lambda\boldsymbol{v}$, and the smooth multiplication of $\mathrm{O}(1,3)$), and inversion $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$ is smooth. Hence $\mathrm{ISO}(1,3)$ is a Lie group, of dimension $\dim\mathbb{R}^4 + \dim\mathrm{O}(1,3) = 4 + 6 = 10$. $\blacksquare$

> [!note]- Lemma 2: The bracket from the composition law
> **Statement:** Expanding the composition of two infinitesimal Poincaré transformations to second order and antisymmetrising yields $[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$.
>
> **Hint:** Write $f_k = (\varepsilon\boldsymbol{v}_k, \mathrm{Id}+\varepsilon L_k)$, compute $f_1 f_2$ and $f_2 f_1$ via the semidirect law, subtract, and read the $\varepsilon^2$ coefficient.
>
> **Why needed:** It is the construction of the Poincaré bracket, the heart of the theorem.
>
> > [!note]- Full proof
> > Let $f_1 = (\varepsilon\boldsymbol{v}_1, \mathrm{Id}+\varepsilon L_1)$ and $f_2 = (\varepsilon\boldsymbol{v}_2, \mathrm{Id}+\varepsilon L_2)$. By the semidirect law,
> > $$f_1 f_2 = \big(\varepsilon\boldsymbol{v}_1 + (\mathrm{Id}+\varepsilon L_1)(\varepsilon\boldsymbol{v}_2),\; (\mathrm{Id}+\varepsilon L_1)(\mathrm{Id}+\varepsilon L_2)\big).$$
> > The translation part is $\varepsilon\boldsymbol{v}_1 + \varepsilon\boldsymbol{v}_2 + \varepsilon^2 L_1\boldsymbol{v}_2 = \varepsilon(\boldsymbol{v}_1+\boldsymbol{v}_2) + \varepsilon^2 L_1\boldsymbol{v}_2$, and the Lorentz part is $\mathrm{Id} + \varepsilon(L_1+L_2) + \varepsilon^2 L_1 L_2$. Interchanging $1\leftrightarrow2$,
> > $$f_2 f_1 = \big(\varepsilon(\boldsymbol{v}_1+\boldsymbol{v}_2) + \varepsilon^2 L_2\boldsymbol{v}_1,\; \mathrm{Id} + \varepsilon(L_1+L_2) + \varepsilon^2 L_2 L_1\big).$$
> > The first-order terms agree (the algebra is commutative to first order), so subtracting isolates the second order:
> > $$f_1 f_2 - f_2 f_1 \;\big|_{O(\varepsilon^2)} = \big(\varepsilon^2(L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1),\; \varepsilon^2(L_1 L_2 - L_2 L_1)\big).$$
> > Stripping the $\varepsilon^2$, the bracket is $[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$. (This matches Gourgoulhon's eq. 8.30, obtained there by comparing $f_1\circ f_2 - f_2\circ f_1$ directly.) $\blacksquare$

> [!note]- Lemma 3: The formula is a Lie bracket
> **Statement:** The map $[\,\cdot\,,\,\cdot\,]$ of Lemma 2 is bilinear, antisymmetric, valued in $\mathfrak{iso}(1,3)$, and satisfies the Jacobi identity.
>
> **Hint:** Bilinearity and antisymmetry are immediate; closure because $L_i\boldsymbol{v}_j\in E$ and $[L_1,L_2]\in\mathfrak{so}(1,3)$; Jacobi from Jacobi in $\mathfrak{so}(1,3)$ and linearity of the action of $\mathfrak{so}(1,3)$ on $E$.
>
> **Why needed:** Confirms $\mathfrak{iso}(1,3)$ with this bracket is genuinely a Lie algebra, so it is the Lie algebra of the group.
>
> > [!note]- Full proof
> > *Bilinearity:* each slot is linear in $(\boldsymbol{v}_1, L_1)$ and in $(\boldsymbol{v}_2, L_2)$, since $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$ and $[L_1, L_2]$ are bilinear. *Antisymmetry:* swapping $1\leftrightarrow2$ sends $(L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$ to $(L_2\boldsymbol{v}_1 - L_1\boldsymbol{v}_2, [L_2, L_1]) = -(L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$. *Closure:* $L_i\in\mathfrak{so}(1,3)$ acts on $E$, so $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1\in E$; and $[L_1, L_2]\in\mathfrak{so}(1,3)$; hence the bracket lands in $E\times\mathfrak{so}(1,3) = \mathfrak{iso}(1,3)$. *Jacobi:* write $X_k = (\boldsymbol{v}_k, L_k)$. The Lorentz slot of the double bracket reproduces the Jacobi identity of $\mathfrak{so}(1,3)$, which holds. The translation slot of $[X_1, [X_2, X_3]] + \text{cyclic}$ is $L_1(L_2\boldsymbol{v}_3 - L_3\boldsymbol{v}_2) - [L_2, L_3]\boldsymbol{v}_1 + \text{cyclic}$; expanding and using that the action is a Lie-algebra action (i.e. $[L_2, L_3]\boldsymbol{v}_1 = L_2 L_3\boldsymbol{v}_1 - L_3 L_2\boldsymbol{v}_1$), all terms cancel in cyclic sum. Hence Jacobi holds, and $\mathfrak{iso}(1,3)$ is a Lie algebra. $\blacksquare$

> [!note]- Lemma 4: The structure constants
> **Statement:** With $P_\alpha = (e_\alpha, 0)$, $K_i = (0, K_i)$, $J_i = (0, J_i)$, the brackets are $[P_\alpha, P_\beta] = 0$, $[K_i, P_0] = P_i$, $[K_i, P_j] = \delta_{ij}P_0$, $[J_i, P_0] = 0$, $[J_i, P_j] = \epsilon_{ijk}P_k$.
>
> **Hint:** Apply the bracket formula and the action $K_i e_0 = e_i$, $K_i e_j = \delta_{ij}e_0$, $J_i e_0 = 0$, $J_i e_j = \epsilon_{ijk}e_k$.
>
> **Why needed:** These are the explicit structure constants — the commutation relations of relativistic kinematics.
>
> > [!note]- Full proof
> > *Translations.* $[P_\alpha, P_\beta] = [(e_\alpha, 0), (e_\beta, 0)] = (0\cdot e_\beta - 0\cdot e_\alpha,\, [0, 0]) = (0, 0) = 0$.
> >
> > *Boosts with translations.* $[K_i, P_\alpha] = [(0, K_i), (e_\alpha, 0)] = (K_i e_\alpha - 0\cdot 0,\, [K_i, 0]) = (K_i e_\alpha, 0)$. Reading the action of the boost generator off its matrix ([[Special Relativity X — The Lorentz Group as a Lie Group]]): $K_i e_0 = e_i$ and $K_i e_j = \delta_{ij}e_0$. Hence $[K_i, P_0] = (e_i, 0) = P_i$ and $[K_i, P_j] = (\delta_{ij}e_0, 0) = \delta_{ij}P_0$.
> >
> > *Rotations with translations.* $[J_i, P_\alpha] = [(0, J_i), (e_\alpha, 0)] = (J_i e_\alpha, 0)$. The rotation generator acts by $J_i e_0 = 0$ (rotations fix the time axis) and $J_i e_j = \epsilon_{ijk}e_k$. Hence $[J_i, P_0] = (0, 0) = 0$ and $[J_i, P_j] = (\epsilon_{ijk}e_k, 0) = \epsilon_{ijk}P_k$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Dimension (Lemma 1).* As a manifold $\mathrm{ISO}(1,3) = \mathbb{R}^4\times\mathrm{O}(1,3)$, with smooth multiplication and inversion, so it is a Lie group of dimension $4 + 6 = 10$. Its Lie algebra $\mathfrak{iso}(1,3)$ is the tangent space at the identity, $E\times\mathfrak{so}(1,3)$, of dimension $10$, with the additive vector-space structure $(\boldsymbol{v}_1, L_1) + (\boldsymbol{v}_2, L_2) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, L_1 + L_2)$.
>
> *Bracket (Lemmas 2–3).* Expanding the composition of two infinitesimal Poincaré transformations $f_k = (\varepsilon\boldsymbol{v}_k, \mathrm{Id} + \varepsilon L_k)$ to second order and antisymmetrising gives
> $$[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1,\; [L_1, L_2]),$$
> which is bilinear, antisymmetric, valued in $\mathfrak{iso}(1,3)$, and satisfies the Jacobi identity (inherited from $\mathfrak{so}(1,3)$ together with the fact that $\mathfrak{so}(1,3)$ acts on $E$ as a Lie algebra). Hence $(\mathfrak{iso}(1,3), [\,\cdot\,,\,\cdot\,])$ is a Lie algebra, and it is the Lie algebra of $\mathrm{ISO}(1,3)$.
>
> *Structure constants (Lemma 4).* Writing $P_\alpha = (e_\alpha, 0)$, $K_i = (0, K_i)$, $J_i = (0, J_i)$ and using the bracket formula with the actions $K_i e_0 = e_i$, $K_i e_j = \delta_{ij}e_0$, $J_i e_0 = 0$, $J_i e_j = \epsilon_{ijk}e_k$:
> $$[P_\alpha, P_\beta] = 0, \quad [K_i, P_0] = P_i, \quad [K_i, P_j] = \delta_{ij}P_0, \quad [J_i, P_0] = 0, \quad [J_i, P_j] = \epsilon_{ijk}P_k,$$
> together with the purely-Lorentz brackets $[J_i, J_j] = \epsilon_{ijk}J_k$, $[J_i, K_j] = \epsilon_{ijk}K_k$, $[K_i, K_j] = -\epsilon_{ijk}J_k$ inherited from $\mathfrak{so}(1,3)$. These ten generators and their brackets constitute the Poincaré algebra. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Euclidean group of rigid motions (geometry).** The group $\mathrm{ISO}(3) = \mathbb{R}^3\rtimes\mathrm{O}(3)$ of rigid motions of three-dimensional space is the exact Euclidean analogue, of dimension $3 + 3 = 6$, with Lie algebra $\mathfrak{iso}(3) = \mathbb{R}^3\rtimes\mathfrak{so}(3)$ and the identical bracket formula $[(\boldsymbol{v}_1, L_1), (\boldsymbol{v}_2, L_2)] = (L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1, [L_1, L_2])$. Its structure constants $[J_i, P_j] = \epsilon_{ijk}P_k$ (angular momentum and linear momentum) are the non-relativistic shadow of the Poincaré ones. The application is nonobvious because it shows the semidirect construction and its bracket are signature-independent: only $\mathrm{O}(n)$ versus $\mathrm{O}(1,3)$ changes.

**The Heisenberg algebra and central extensions (quantum mechanics).** The Galilean group, the $c\to\infty$ contraction of the Poincaré group, admits a non-trivial central extension in which $[K_i, P_j] = im\delta_{ij}$ — the mass appears as a central charge rather than as the structure constant $\delta_{ij}P_0$. This is structurally a Heisenberg-type relation, and tracing how the Poincaré bracket $[K_i, P_j] = \delta_{ij}P_0$ contracts and then centrally extends is a clean exercise in Lie-algebra contraction and cohomology. The application is surprising because the *relativistic* algebra has no such central extension (the Poincaré group is its own universal central extension up to the trivial one), so the Bargmann mass-superselection rule is a purely non-relativistic phenomenon.

**Gauging the Poincaré algebra (gravitation).** Promoting the global Poincaré symmetry to a local one — letting the group element depend on spacetime position and introducing gauge fields for the generators — yields the Poincaré gauge theory of gravity, in which the translations $P_\alpha$ gauge to the vierbein (tetrad) field and the Lorentz generators $J_i, K_i$ to the spin connection. The structure constants computed here become the structure of the gravitational gauge algebra. The application is out-of-distribution because the same ten-generator algebra that classifies particles also, when gauged, produces the geometry of curved spacetime.

---

# Bridges

- **[[Def - The Poincaré Group]]** — this theorem promotes the abstract group of that page to a Lie group and extracts its infinitesimal structure. The semidirect composition law $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ defined there is exactly what is differentiated here to produce the bracket; the lone factor $\Lambda_1$ becomes the lone factor $L_1$ in the cross-term $L_1\boldsymbol{v}_2 - L_2\boldsymbol{v}_1$.

- **[[Def - Lie Algebra of the Lorentz Group]]** — the Poincaré algebra contains the Lorentz algebra $\mathfrak{so}(1,3)$ as the subalgebra of elements with zero translation part, and the purely-Lorentz brackets $[J, J] = J$, $[J, K] = K$, $[K, K] = -J$ are imported wholesale. The new brackets are precisely those coupling the boosts and rotations to the translations, $[K_i, P_\alpha]$ and $[J_i, P_\alpha]$, which the present theorem computes.

- **[[Def - The Lie Algebra of a Lie Group]]** — the construction here is the general functorial passage from a Lie group to its Lie algebra, specialised to $\mathrm{ISO}(1,3)$. For a *matrix* group that construction reduces to the commutator ([[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]); the Poincaré group, being a group of affine maps rather than matrices, requires the construction in its intrinsic form, which is why the bracket is read off the composition law rather than computed as $AB - BA$. The general theory lives in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

- **[[Def - Casimir Invariants of the Poincaré Group]]** — the structure constants computed here are exactly what is needed to identify the Casimirs: $P^2 = P_\mu P^\mu$ commutes with all generators because $[P_\alpha, P_\beta] = 0$ and $P^2$ is a Lorentz scalar, and the spin Casimir $W^2$ is built from the Pauli–Lubanski vector using these brackets. The algebra is the input; the representation theory is the output.

---

# Unlocked by This

> [!tip] The Casimir Invariants and the Wigner Classification *(from §12.3)*
> With the algebra and its brackets in hand, one searches for operators commuting with all ten generators — the [[Def - Casimir Invariants of the Poincaré Group|Casimirs]] $P^2$ and $W^2$ — whose eigenvalues are the mass and spin. Wigner's classification of the irreducible unitary representations by these two labels is the definition of an elementary particle.

> [!tip] The Poincaré Algebra of Observables *(from QFT)*
> Promoted to Hermitian operators, the ten generators become the conserved observables of any relativistic quantum theory: the four-momentum $P^\mu = (H, \boldsymbol{P})$, the angular momentum $J_i$, and the boosts $K_i$. The structure constants become their commutation relations — $[J_i, P_j] = i\epsilon_{ijk}P_k$ (momentum is a vector), $[K_i, P_0] = iP_i$ (energy and momentum mix under boosts) — which every relativistic quantum field must represent. This is the kinematic algebra underlying all of quantum field theory.

> [!tip] Spacetime Symmetries via Noether *(from the Principle of Least Action)*
> By Noether's theorem each of the ten one-parameter subgroups generated by $P_\alpha, J_i, K_i$ yields a conserved current and charge: the four translations give energy and momentum, the three rotations give angular momentum, and the three boosts give the centre-of-energy theorem. The ten-dimensional Poincaré algebra is thus the source of the ten conservation laws of relativistic mechanics. See [[Def - Angular Momentum Four-Tensor]].
