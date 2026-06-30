---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Hodge Star"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

The [[Def - The Electromagnetic Field Tensor|field tensor]] $F$ is a 2-form. Relative to an observer $\mathcal{O}$ of four-velocity $U_0$, it decomposes as
$$F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B}),$$
with $\mathbf{E} = F(\cdot,U_0)$, $c\mathbf{B} = \star F(U_0,\cdot)$, both lying in the rest space ($\langle\mathbf{E},U_0\rangle = 0$, $U_0\cdot\mathbf{B} = 0$).

1. Verify that the contraction $F(\cdot,U_0)$ extracts a one-form orthogonal to $U_0$ (so $\mathbf{E}$ genuinely lives in the rest space), and similarly that $\star F(U_0,\cdot)$ is orthogonal to $U_0$.
2. Show that the **metric dual** $F^\sharp$ (both indices raised, $F^{\mu\nu} = g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}$) and the **Hodge dual** $\star F$ are two genuinely different valence-2 tensors associated with $F$, and that $\star F$ is obtained from $F$ by the substitution $\mathbf{E}\to -c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$.
3. Using the decomposition, recover the elementary Lorentz force $\boldsymbol{\mathfrak{F}} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$ for a particle of velocity $\mathbf{V}$ relative to $\mathcal{O}$.
4. Explain why the split of $F$ into $\mathbf{E}$ and $\mathbf{B}$ is observer-dependent while $F$ itself is not.

**Recall:**

![[Def - The Electromagnetic Field Tensor#The Definition]]

An [[Def - Observer and Local Rest Space|observer]] has four-velocity $U_0$ and rest space $\mathcal{E}_{U_0} = U_0^\perp$. The metric dual $\underline{V}$ of a vector $V$ has components $V_\mu = \eta_{\mu\nu}V^\nu$; the [[Def - The Hodge Star|Hodge star]] $\star$ sends a 2-form to a 2-form via $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$.

---

# Convergent Strategy

**Problem class.** A *decomposition-and-interpretation* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.1]]: verify the observer's split of $F$ into rest-space fields and read off the force. The routine is contraction identities plus the geometric meaning of the rest-space projection.

**Assumption pattern.** A single observer with four-velocity $U_0$, defining a rest space $U_0^\perp$ into which the fields are projected. The assumption that $\mathbf{E}$ and $\mathbf{B}$ are *defined by contraction with $U_0$* is what makes them automatically orthogonal to $U_0$, and what makes them observer-dependent. The signpost is that a different $U_0$ gives a different split of the *same* $F$.

**Theorem routing.** Part 1 uses antisymmetry of $F$ to show $F(\cdot,U_0)\cdot U_0 = 0$. Part 2 distinguishes the [[Def - The Hodge Star|Hodge dual]] (a duality on the 2-form) from the metric dual (index-raising). Part 3 contracts the [[Def - The Electromagnetic Field Tensor|decomposition]] with the four-velocity. Part 4 is conceptual, about the observer-dependence of projections.

**Key decision point.** The non-obvious recognition is that $F^\sharp$ and $\star F$ are *different* operations — one raises indices using the metric (changing valence type but not the geometric object), the other applies the Hodge star (a genuinely new 2-form mixing the components). Conflating them is a common error; keeping them distinct is the content of part 2.

---

# Legal Operations Used

1. **Operation 1 (assemble/read the field tensor)** from the topic page: use the observer decomposition $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$. This underlies all four parts.

2. **Operation 9 (project the four-force onto an observer)** from the topic page: contract the decomposition with the particle's four-velocity. This is part 3.

---

# Hints

> [!note]- Hint 1
> $F(\cdot,U_0)$ has components $F_{\alpha\beta}U_0^\beta$. Contract again with $U_0^\alpha$: $F_{\alpha\beta}U_0^\alpha U_0^\beta = 0$ by antisymmetry (symmetric $\times$ antisymmetric). So $\mathbf{E} = F(\cdot,U_0)$ is orthogonal to $U_0$ — it lives in the rest space.

> [!note]- Hint 2
> The metric dual raises indices: $F^{\mu\nu} = g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}$, same geometric object, different index placement. The Hodge dual $\star F$ is a *different* 2-form whose components are $\tfrac12\epsilon F$ — it mixes the entries, sending $\mathbf{E}\to-c\mathbf{B}$ and $c\mathbf{B}\to\mathbf{E}$. They are not the same.

> [!note]- Hint 3
> Contract $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$ with the particle four-velocity $U = \Gamma(U_0 + \mathbf{V})$. The first term gives the electric force $\propto\mathbf{E}$; the Hodge-dual term, when contracted with the rest-space velocity $\mathbf{V}$, produces the cross product $\mathbf{V}\times\mathbf{B}$.

> [!note]- Hint 4
> $\mathbf{E} = F(\cdot,U_0)$ depends on $U_0$ explicitly. A different observer $U_0'$ gives $\mathbf{E}' = F(\cdot,U_0')$, a different rest-space vector. But $F$ — the object being contracted — is the same tensor. So the split is observer-dependent, the tensor is not.

---

# Solution

The plan: verify the rest-space character of $\mathbf{E}$ and $\mathbf{B}$ (Step 1), distinguish the two duals (Step 2), project the decomposition to the elementary force (Step 3), and articulate the observer-dependence (Step 4). The conceptual core is that the split into $\mathbf{E}$, $\mathbf{B}$ is a projection adapted to one observer.

**Step 1: $\mathbf{E}$ and $\mathbf{B}$ live in the rest space.**

> [!note]- Derivation
> The one-form $\mathbf{E} = F(\cdot,U_0)$ has components $E_\alpha = F_{\alpha\beta}U_0^\beta$. Its contraction with $U_0$ is
> $$\langle\mathbf{E}, U_0\rangle = E_\alpha U_0^\alpha = F_{\alpha\beta}U_0^\alpha U_0^\beta = 0,$$
> vanishing because $F_{\alpha\beta}$ is antisymmetric and $U_0^\alpha U_0^\beta$ is symmetric. So $\mathbf{E}\perp U_0$: the electric field lies in the [[Def - Observer and Local Rest Space|rest space]] $\mathcal{E}_{U_0}$. The same argument applied to $\star F$ (also a 2-form, also antisymmetric) gives $\langle\star F(U_0,\cdot), U_0\rangle = (\star F)_{\alpha\beta}U_0^\alpha U_0^\beta = 0$, so $c\mathbf{B} = \star F(U_0,\cdot)$ is likewise in the rest space. Both fields are genuinely *spatial* relative to $\mathcal{O}$ — they have no time component in $\mathcal{O}$'s frame.

**Step 2: Metric dual versus Hodge dual.**

> [!note]- Derivation
> The **metric dual** $F^\sharp$ raises both indices using the metric: $F^{\mu\nu} = g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}$. This does not produce a new geometric object — it is the *same* tensor $F$ expressed with contravariant indices, the type-$(2,0)$ avatar of the type-$(0,2)$ form. Its component matrix differs from $F_{\alpha\beta}$ only by the sign flips of index-raising (time-space block flips, space-space does not).
>
> The **Hodge dual** $\star F$ is a *genuinely different* 2-form: $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$, built by contracting with the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]. Its components are *not* a re-indexing of $F$'s — they mix the electric and magnetic parts. Explicitly (from the [[Def - The Hodge Star|Hodge-star]] computation), $\star F$ is $F$ with the substitution
> $$\mathbf{E}\to -c\mathbf{B}, \qquad c\mathbf{B}\to\mathbf{E}.$$
> So $F^\sharp$ and $\star F$ are two *different* valence-2 tensors associated with $F$: the first by raising indices (no new content), the second by Hodge duality (electric–magnetic exchange). Conflating them is a mistake; $\star F$ is what appears in the second invariant and in Maxwell's equations.

**Step 3: Recover the elementary Lorentz force.**

> [!note]- Derivation
> The Lorentz four-force is $f = qF(\cdot,U)$ with $U = \Gamma(U_0 + \mathbf{V})$. Insert the decomposition $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$ and contract the second slot with $U$:
> $$f = q\Gamma\,F(\cdot, U_0) + q\Gamma\,F(\cdot,\mathbf{V}).$$
> The first term: $F(\cdot,U_0) = \mathbf{E}$ (the electric part; the Hodge-dual magnetic term contracted with $U_0$ vanishes in the rest-space directions). The second term: contracting $\star(\underline{U_0}\wedge c\mathbf{B})$ with the rest-space velocity $\mathbf{V}$ produces, by the [[Def - The Hodge Star|Hodge-star]] and wedge identities, the cross product $c\mathbf{B}$ "rotated" by $\mathbf{V}$ — concretely $\mathbf{V}\times\mathbf{B}$. Collecting the rest-space (spatial) part and converting from proper-time to coordinate-time rate (divide by $\Gamma$):
> $$\boldsymbol{\mathfrak{F}} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B}).$$
> The electric field contributes a force along itself; the magnetic field, through the Hodge-dual term, contributes the velocity-dependent $\mathbf{V}\times\mathbf{B}$. This is the elementary Lorentz force, recovered from the covariant decomposition.

**Step 4: Why the split is observer-dependent.**

> [!note]- Derivation
> The fields are *defined by contraction with the observer's four-velocity*: $\mathbf{E} = F(\cdot,U_0)$ and $c\mathbf{B} = \star F(U_0,\cdot)$. The object being contracted, $F$, is a fixed tensor on spacetime — it does not refer to any observer. But the contraction *does*: it picks out the slice of $F$ along $U_0$'s time axis. A different observer $\mathcal{O}'$ with four-velocity $U_0'$ contracts the *same* $F$ with a *different* $U_0'$, getting $\mathbf{E}' = F(\cdot,U_0')$ and $c\mathbf{B}' = \star F(U_0',\cdot)$ — different rest-space vectors. So:
> - $F$ is **absolute** (observer-independent): it is the geometric object.
> - $\mathbf{E}$, $\mathbf{B}$ are **relative** (observer-dependent): they are $F$'s projections adapted to one observer's rest space.
>
> This is why the [[Thm - Transformation of Electric and Magnetic Fields|transformation law]] mixes $\mathbf{E}$ and $\mathbf{B}$ — changing $U_0$ re-slices $F$ — and why only $F$ and its [[Thm - The Electromagnetic Field Invariants|invariants]] (which do not refer to any $U_0$) are objective. The fields are shadows; the tensor casts them.

> [!note]- Complete formal solution
> $\mathbf{E} = F(\cdot,U_0)$ satisfies $\langle\mathbf{E},U_0\rangle = F_{\alpha\beta}U_0^\alpha U_0^\beta = 0$ (antisymmetric $\times$ symmetric), so it lies in the rest space; likewise $c\mathbf{B} = \star F(U_0,\cdot)$. The metric dual $F^\sharp$ (indices raised) and the Hodge dual $\star F$ (the 2-form $\tfrac12\epsilon F$, equal to $F$ under $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$) are distinct valence-2 tensors. Contracting $f = qF(\cdot,U)$ with $U = \Gamma(U_0+\mathbf{V})$ and the decomposition recovers $\boldsymbol{\mathfrak{F}} = q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$. The split is observer-dependent because $\mathbf{E}$, $\mathbf{B}$ are defined by contracting the fixed tensor $F$ with the observer-specific $U_0$; a different observer re-slices the same $F$. $\blacksquare$

---

# Key Takeaways

**$\mathbf{E}$ and $\mathbf{B}$ are projections of $F$ onto an observer's rest space.** The decomposition $F = \underline{U_0}\wedge\mathbf{E} + \star(\underline{U_0}\wedge c\mathbf{B})$ makes precise the sense in which the electric and magnetic fields are *slices* of the field tensor: $\mathbf{E} = F(\cdot,U_0)$ and $c\mathbf{B} = \star F(U_0,\cdot)$ are obtained by contracting $F$ (and its Hodge dual) with the observer's four-velocity, and they automatically lie in the rest space because $F$ is antisymmetric. This is the structural reason the fields are observer-dependent: the contraction refers to $U_0$, so changing the observer changes the slice. The reusable insight is that *any* observer-relative three-vector in relativity (the electric field, the velocity, the spatial momentum) is a projection of an absolute four-dimensional object onto a rest space, and the projection carries the observer-dependence. Recognising this dissolves the puzzlement about why $\mathbf{E}$ and $\mathbf{B}$ "change between frames" — they are not changing, the slice is.

**The metric dual and the Hodge dual are different operations.** A frequent confusion is to treat "raising the indices of $F$" and "taking the Hodge dual of $F$" as the same. They are not: the metric dual $F^\sharp$ is the same geometric object with contravariant indices (no new content, just a sign-flipping re-indexing), while the Hodge dual $\star F$ is a *genuinely new* 2-form that exchanges $\mathbf{E}\leftrightarrow c\mathbf{B}$. The distinction matters because $\star F$ — not $F^\sharp$ — is what enters the second invariant $I_2 = \tfrac14(\star F)_{\mu\nu}F^{\mu\nu}$, the dual Maxwell equation $d\star F = \mu_0\star J$, and the self-dual decomposition. The diagnostic: if an operation mixes electric and magnetic, it is the Hodge star; if it only changes index height, it is the metric dual. Keeping the two straight prevents a whole class of errors in covariant electromagnetism.

**The tensor is absolute; the fields are relative — and that is the whole philosophy of the chapter.** The deepest content of part 4 is the clean separation between what is observer-independent ($F$, and its invariants $I_1$, $I_2$) and what is observer-dependent (the split into $\mathbf{E}$ and $\mathbf{B}$, the three-force, the energy). The fields are defined *by* contraction with an observer's four-velocity, so they inherit that observer's perspective; the tensor, being defined without reference to any observer, is objective. This is the relativistic resolution of the old puzzle "is the field electric or magnetic?" — the question is malformed, because the answer depends on the observer, and only the [[Thm - The Electromagnetic Field Invariants|invariant classification]] (mostly electric, mostly magnetic, null) is frame-independent. The reusable principle, applicable throughout relativistic physics, is to always ask of any quantity: is it the absolute object, or a projection of it onto some observer's rest space? The projections vary; the objects do not.
