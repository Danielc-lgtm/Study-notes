---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Maxwell Equations"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Exterior Derivative"
tags: [physics, special-relativity]
---

# Problem Statement

Show that the single covariant equation $dF = 0$ contains exactly the two homogeneous Maxwell equations:
$$\nabla\cdot\mathbf B = 0 \quad\text{(no magnetic monopoles)}, \qquad \nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t} \quad\text{(Faraday's law)}.$$

1. Write out $dF = 0$ in components as the Bianchi identity $\partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta} = 0$, explaining why the exterior derivative of the $2$-form $F$ has this form.
2. Taking all three indices spatial ($\alpha\beta\gamma = 123$), recover $\nabla\cdot\mathbf B = 0$.
3. Taking one index temporal ($\alpha = 0$, $\beta\gamma$ spatial), recover $\nabla\times\mathbf E = -\partial_t\mathbf B$.
4. Conclude that these two equations are *automatically* satisfied whenever $F = dA$ for a potential $A$, and explain why.

**Recall:**

The electromagnetic field is the antisymmetric $2$-form $F$ whose components, relative to an observer, encode the electric and magnetic fields:

![[Def - The Electromagnetic Field Tensor#The Definition]]

The component dictionary (in an observer's inertial frame) is $F_{0i} = E_i$ and $F_{ij} = -\epsilon_{ijk}B_k$, so that $F_{12} = -B_3$, $F_{23} = -B_1$, $F_{31} = -B_2$, and $F_{0i} = E_i$.

![[Thm - Maxwell Equations#Statement]]

The [[Def - The Exterior Derivative|exterior derivative]] of a $2$-form $F = \tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu$ is the $3$-form $dF$ with components $(dF)_{\alpha\beta\gamma} = \partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta}$, the cyclic (antisymmetrised) sum of gradients.

---

# Convergent Strategy

**Problem class.** A *translate-the-covariant-equation* problem, the first target named in the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: take a four-dimensional Maxwell equation and project it onto an observer to recover the three-dimensional laws. The routine is to unpack the form equation into components, then sort the components by how many indices are temporal.

**Assumption pattern.** The given is $dF = 0$, a statement about a $2$-form. The signpost is "homogeneous" — the equation has no source, which means it concerns the geometry of $F$ alone, and (by the Poincaré lemma) is equivalent to the existence of a potential. What this unlocks is the component dictionary $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B_k$, which converts index statements into vector statements.

**Theorem routing.** The route is: $dF = 0 \to$ Bianchi identity (by the definition of the [[Def - The Exterior Derivative|exterior derivative]] of a $2$-form) $\to$ split by index type (all spatial, one temporal) $\to$ the two three-dimensional equations via the dictionary, exactly as in [[Thm - Maxwell Equations]] Lemmas 1 and 3. The all-spatial case gives no-monopole; the one-temporal case gives Faraday.

**Key decision point.** The non-obvious choice is *which index combinations to take*. There are $\binom{4}{3} = 4$ independent index triples; the one with no temporal index ($123$) gives a scalar equation (no-monopole), and the three with one temporal index ($0ij$) give a vector equation (Faraday). Mistaking which triple gives which equation, or failing to contract the Faraday case with $\epsilon_{ij\ell}$ to extract the curl, is where the bookkeeping fails.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the field as $F = dA$).** Part 4 uses this: once $F = dA$, the Bianchi identity $\partial_{[\alpha}F_{\beta\gamma]} = 0$ holds identically, so the homogeneous equations are automatic.

2. **Operation 7 from the topic page (project a tensor equation onto an observer).** Parts 2 and 3 are this operation: the Bianchi identity is projected by choosing the index types, all-spatial for the scalar no-monopole law, one-temporal for the vector Faraday law.

3. **Operation 2 from the topic page (apply $d$ and use $d^2 = 0$).** Part 4 invokes the nilpotence: $dF = d(dA) = 0$ is why the homogeneous equations need no separate imposition.

---

# Hints

> [!note]- Hint 1
> The exterior derivative of a $2$-form is the antisymmetrised gradient: $(dF)_{\alpha\beta\gamma}$ is the cyclic sum $\partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta}$. Setting this to zero for all triples is $dF = 0$. There are only four independent triples in four dimensions.

> [!note]- Hint 2
> For the no-monopole law, take $\alpha\beta\gamma = 123$ (all spatial). Substitute $F_{ij} = -\epsilon_{ijk}B_k$. The cyclic sum becomes $\partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = -(\partial_1 B_1 + \partial_2 B_2 + \partial_3 B_3)$.

> [!note]- Hint 3
> For Faraday's law, take one index temporal: $\alpha = 0$, $\beta = i$, $\gamma = j$ spatial. The cyclic sum is $\partial_0 F_{ij} + \partial_i F_{j0} + \partial_j F_{0i}$. Use $F_{ij} = -\epsilon_{ijk}B_k$ and $F_{0i} = E_i$ (so $F_{j0} = -E_j$), then contract the resulting equation with $\epsilon_{ij\ell}$ to extract the curl of $\mathbf E$.

> [!note]- Hint 4
> For part 4: if $F = dA$, then $dF = d(dA)$, and the exterior derivative is nilpotent ($d\circ d = 0$). So $dF = 0$ holds with no assumption beyond the existence of $A$ — the homogeneous equations are an identity of the calculus, not a law of physics.

---

# Solution

The proof unpacks $dF = 0$ into the Bianchi identity, then sorts its components by the number of temporal indices. Step 1 writes the Bianchi identity; Step 2 takes all indices spatial to get the no-monopole law; Step 3 takes one index temporal to get Faraday's law; Step 4 observes that $F = dA$ makes both automatic via $d^2 = 0$. The non-obvious move is in Step 3, where contracting with $\epsilon_{ij\ell}$ converts the antisymmetric index pair into the curl.

**Step 1: $dF = 0$ is the Bianchi identity $\partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta} = 0$.**

> [!note]- Derivation
> The field is the $2$-form $F = \tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu$. Its [[Def - The Exterior Derivative|exterior derivative]] is the $3$-form $dF = \tfrac12\partial_\lambda F_{\mu\nu}\,dx^\lambda\wedge dx^\mu\wedge dx^\nu$. Collecting the fully antisymmetric components, $(dF)_{\alpha\beta\gamma}$ is the alternating sum of $\partial_\alpha F_{\beta\gamma}$ over permutations; because $F_{\beta\gamma}$ is already antisymmetric, the six permutations collapse to the three cyclic terms with a common sign:
> $$(dF)_{\alpha\beta\gamma} = \partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta}.$$
> Setting $dF = 0$ requires this to vanish for every index triple — the **Bianchi identity** $\partial_{[\alpha}F_{\beta\gamma]} = 0$.

**Step 2: All-spatial indices give $\nabla\cdot\mathbf B = 0$.**

> [!note]- Derivation
> Take $\alpha\beta\gamma = 123$. The Bianchi identity reads $\partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = 0$. Using the dictionary $F_{ij} = -\epsilon_{ijk}B_k$: $F_{23} = -\epsilon_{23k}B_k = -B_1$, $F_{31} = -B_2$, $F_{12} = -B_3$. So the identity becomes
> $$-\partial_1 B_1 - \partial_2 B_2 - \partial_3 B_3 = 0, \qquad\text{i.e.}\qquad \nabla\cdot\mathbf B = 0.$$
> This is the absence of magnetic monopoles: the magnetic field has no sources. It is the all-spatial component of $dF = 0$.

**Step 3: One temporal index gives $\nabla\times\mathbf E = -\partial_t\mathbf B$.**

> [!note]- Derivation
> Take $\alpha = 0$, $\beta = i$, $\gamma = j$ (spatial). The Bianchi identity is $\partial_0 F_{ij} + \partial_i F_{j0} + \partial_j F_{0i} = 0$. With $F_{ij} = -\epsilon_{ijk}B_k$, $F_{0i} = E_i$, and $F_{j0} = -F_{0j} = -E_j$:
> $$-\partial_t(\epsilon_{ijk}B_k) - \partial_i E_j + \partial_j E_i = 0.$$
> Contract with $\epsilon_{ij\ell}$ (sum over $i, j$). Using $\epsilon_{ij\ell}\epsilon_{ijk} = 2\delta_{\ell k}$ and $\epsilon_{ij\ell}(\partial_j E_i - \partial_i E_j) = -2(\nabla\times\mathbf E)_\ell$:
> $$-2\,\partial_t B_\ell - 2(\nabla\times\mathbf E)_\ell = 0, \qquad\text{i.e.}\qquad \nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t}.$$
> This is Faraday's law of induction: a changing magnetic field induces a circulating electric field. It is the one-temporal-index component of $dF = 0$.

**Step 4: $F = dA$ makes both equations automatic.**

> [!note]- Derivation
> Suppose the field comes from a [[Def - The Four-Potential|potential]], $F = dA$. Then
> $$dF = d(dA) = 0$$
> identically, because the [[Def - The Exterior Derivative|exterior derivative]] is nilpotent: $d\circ d = 0$ (the [[Thm - Properties of the Exterior Derivative|defining property]] of $d$). So the Bianchi identity, and with it both $\nabla\cdot\mathbf B = 0$ and $\nabla\times\mathbf E = -\partial_t\mathbf B$, hold *automatically* the instant a potential exists — with no physical input beyond "$F$ has a potential". The homogeneous Maxwell equations are not laws of nature in the usual sense; they are identities of the exterior calculus, forced by the structure $F = dA$.

> [!note]- Complete formal solution
> Write $F = \tfrac12 F_{\mu\nu}dx^\mu\wedge dx^\nu$; its exterior derivative has components $(dF)_{\alpha\beta\gamma} = \partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta}$, so $dF = 0$ is the Bianchi identity $\partial_{[\alpha}F_{\beta\gamma]} = 0$. With the dictionary $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B_k$: the triple $123$ gives $-\partial_i B_i = 0$, i.e. $\nabla\cdot\mathbf B = 0$; the triple $0ij$ gives $-\partial_t(\epsilon_{ijk}B_k) - \partial_i E_j + \partial_j E_i = 0$, which contracted with $\epsilon_{ij\ell}$ yields $\nabla\times\mathbf E = -\partial_t\mathbf B$. These are the two homogeneous Maxwell equations. Finally, if $F = dA$ then $dF = d(dA) = 0$ by nilpotence of $d$, so both equations hold automatically — the homogeneous pair is the geometric, source-free half of Maxwell, free once a potential exists. $\blacksquare$

---

# Key Takeaways

**One covariant equation packages two three-dimensional laws, sorted by temporal index count.** The lesson that generalises far beyond this problem is that a single tensor equation in four dimensions contains several three-dimensional equations, and the way to extract them is to project onto an observer by choosing how many indices point along the time direction. Here $dF = 0$ (a $3$-form equation with four independent components) splits into one scalar equation (all spatial indices: no-monopole) and one vector equation (one temporal index: Faraday). The same sorting recovers Gauss and Ampère from the inhomogeneous equation. Whenever you face a covariant equation and want its laboratory content, the move is to fix an observer and enumerate the index types — the trigger is "translate four-dimensional to three-dimensional", and the technique is index-type bookkeeping.

**The homogeneous Maxwell equations are free, and that fact is the seed of the gauge principle.** The deepest content of this exercise is part 4: $\nabla\cdot\mathbf B = 0$ and Faraday's law are not independent physical laws but identities forced by $F = dA$ and $d^2 = 0$. This reframes how to think about half of electromagnetism: it is geometry, not dynamics. The reusable principle is that whenever a field is the exterior derivative of a potential, the closedness $d(\text{field}) = 0$ is automatic, and any "law" expressing that closedness costs nothing. This is why introducing the potential is always the first move when solving Maxwell, and it is the abelian shadow of the Bianchi identity $DF = 0$ that every gauge-theory curvature satisfies. Recognising "this equation is just $d^2 = 0$" saves the work of imposing it.

**The $\epsilon$-contraction is the standard device for converting an antisymmetric index pair to a curl.** A recurring technical move, useful across all of electromagnetism and vector calculus, is that an equation antisymmetric in two spatial indices $i, j$ is equivalent to a vector equation obtained by contracting with $\epsilon_{ij\ell}$. Here $\partial_i E_j - \partial_j E_i$, an antisymmetric tensor, becomes $(\nabla\times\mathbf E)_\ell$ after contraction; the same trick converts $F_{ij} = -\epsilon_{ijk}B_k$ between the tensor and vector descriptions of the magnetic field. The trigger is "an equation antisymmetric in two spatial indices"; the reaction is "contract with $\epsilon$ to get a curl or a cross product". This is the bridge between the index-heavy covariant formalism and the vector-calculus form physicists compute with.
