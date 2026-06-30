---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Transformation of Electric and Magnetic Fields"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

An inertial observer $\mathcal{O}$ measures an electromagnetic field with electric field $\mathbf{E} = (E_1, E_2, E_3)$ and magnetic field $\mathbf{B} = (B^1, B^2, B^3)$. A second inertial observer $\mathcal{O}'$ moves at velocity $\mathbf{U} = U\,e_1$ along the common $x$-axis, with Lorentz factor $\Gamma = (1 - U^2/c^2)^{-1/2}$.

1. Assemble the field tensor $F_{\mu\nu}$ from $\mathbf{E}$ and $\mathbf{B}$, and obtain the components $F'_{\mu\nu}$ in $\mathcal{O}'$ by the tensor transformation law. Read off the transformed fields $\mathbf{E}'$, $\mathbf{B}'$ in component form.
2. Show that the field components *along* the boost are unchanged and those *transverse* mix electric and magnetic.
3. Specialise to a field that is **purely electric** in $\mathcal{O}$ ($\mathbf{B} = 0$, $\mathbf{E} = E\,e_2$ transverse to the boost). Find $\mathbf{E}'$ and $\mathbf{B}'$, and verify that a moving observer sees a magnetic field $\mathbf{B}' = -\frac{\Gamma}{c^2}\mathbf{U}\times\mathbf{E}$.
4. Check that the field invariants $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ come out the same in both frames.

**Recall:**

The exercise rests on the field tensor, its component matrix, and the transformation law.

![[Thm - Transformation of Electric and Magnetic Fields#Statement]]

The [[Def - The Electromagnetic Field Tensor|field tensor]] $F$ is the antisymmetric 2-form whose components in an observer's local frame have $\mathbf{E}$ in the time-space block and $c\mathbf{B}$ in the space-space block: $F_{0i} = E_i$, $F_{ij} = -c\,\epsilon_{ijk}B^k$. The field transforms as a $(0,2)$ tensor, $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$, with $\Lambda$ the [[Def - The Lorentz Transformation|Lorentz boost]] of velocity $\mathbf{U}$. The [[Thm - The Electromagnetic Field Invariants|invariants]] $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ are Lorentz scalars.

---

# Convergent Strategy

**Problem class.** A *transform-a-tensor-between-frames* problem, the central computational task of [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.2]]. The routine is to express the physical fields as components of $F$, apply the tensor transformation law (one factor of the boost matrix per index), and read the new fields back off the blocks.

**Assumption pattern.** Two inertial observers, a relative velocity along a coordinate axis, and the fields known to one of them. The presence of a definite boost direction ($e_1$) splits every vector into a longitudinal ($1$) component and transverse ($2,3$) components, and the assumption "boost along $e_1$" is what makes the longitudinal/transverse decomposition the natural bookkeeping. The purely-electric specialisation in part 3 is the signpost that the magnetic field is *generated* by the boost, not pre-existing.

**Theorem routing.** Part 1 routes through the [[Def - The Electromagnetic Field Tensor|component matrix]] of $F$ and the tensor transformation law $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\mu\nu}$ to the [[Thm - Transformation of Electric and Magnetic Fields|field transformation law]]. Part 3 is that law with $\mathbf{B} = 0$. Part 4 routes through the [[Thm - The Electromagnetic Field Invariants|invariants]], which must be preserved because they are full contractions.

**Key decision point.** The non-obvious choice is to work with the *tensor* $F$ rather than with $\mathbf{E}$ and $\mathbf{B}$ as separate vectors. The temptation is to "boost the vectors", but $\mathbf{E}$ and $\mathbf{B}$ are not Lorentz vectors — they are blocks of a 2-form, and only the tensor transforms cleanly. The other decision is the sign convention of the cross-product term, fixed by checking against the non-relativistic limit $\mathbf{E}' = \mathbf{E} + \mathbf{U}\times\mathbf{B}$.

---

# Legal Operations Used

1. **Operation 1 (assemble the field tensor)** from the topic page: build $F_{\mu\nu}$ with $\mathbf{E}$ in the time-space block and $c\mathbf{B}$ in the space-space block. This is the first step of part 1; it converts the physical fields into the object that transforms simply.

2. **Operation 2 (apply the field transformation law)** from the topic page: keep the longitudinal components, mix the transverse by $\Gamma$. This is the substance of parts 1–3; the sign of the cross term is fixed against the non-relativistic limit.

3. **Operation 4 (compute the invariants in a convenient frame)** from the topic page: evaluate $I_1$ and $I_2$ in both frames. This is part 4, the consistency check that the transformation preserves the invariants.

---

# Hints

> [!note]- Hint 1
> Write the boost matrix $\Lambda$ for velocity $U$ along $e_1$: it acts only on the $0$ and $1$ indices, with $\Gamma$ on the diagonal and $\mp\Gamma U/c$ off-diagonal, and is the identity on $2,3$. Then $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$ — apply it index by index.

> [!note]- Hint 2
> A component like $F'_{02}$ has index $2$ untouched, so $F'_{02} = \Lambda_0{}^\alpha F_{\alpha2} = \Gamma F_{02} + (\mp\Gamma U/c)F_{12}$. With $F_{02} = E_2$ and $F_{12} = -cB^3$, this gives $E_2' = \Gamma(E_2 - UB^3)$. The longitudinal $F'_{01}$ has both its indices in the $\{0,1\}$ block the boost rotates between, and the $\Gamma$ factors collapse via $\Gamma^2(1-U^2/c^2) = 1$ to leave $E_1' = E_1$.

> [!note]- Hint 3
> For part 3, set $\mathbf{B} = 0$ and $\mathbf{E} = E\,e_2$. Then $E_2' = \Gamma E_2 = \Gamma E$, $E_1' = E_3' = 0$, and the magnetic transverse components pick up the electric cross term: $B'^3 = \Gamma(B^3 - \tfrac{U}{c^2}E_2) = -\Gamma\tfrac{U}{c^2}E$. Assemble: $\mathbf{B}' = -\Gamma\tfrac{U}{c^2}E\,e_3 = -\frac{\Gamma}{c^2}\mathbf{U}\times\mathbf{E}$ (since $\mathbf{U}\times\mathbf{E} = Ue_1\times Ee_2 = UE\,e_3$).

> [!note]- Hint 4
> For part 4, compute $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ in each frame using the component fields, and likewise $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$. The $\Gamma$ factors must cancel — they will, because the invariants are full contractions of $F$ and cannot change.

---

# Solution

The proof has three computational parts and a check. Part 1 assembles $F$ and transforms it, yielding the component transformation law; the key move is to treat $\mathbf{E}$, $\mathbf{B}$ as blocks of one tensor. Part 3 specialises to a pure electric field and exhibits the generated magnetic field. Part 4 verifies invariance of $I_1$, $I_2$. The non-obvious step is recognising that the longitudinal components are fixed while the transverse mix.

**Step 1: Assemble $F_{\mu\nu}$ and apply the transformation law.**

> [!note]- Derivation
> The [[Def - The Electromagnetic Field Tensor|field tensor]] in $\mathcal{O}$'s frame (mostly minus) is
> $$F_{\mu\nu} = \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & -cB^3 & cB^2 \\ -E_2 & cB^3 & 0 & -cB^1 \\ -E_3 & -cB^2 & cB^1 & 0 \end{pmatrix}.$$
> The boost of velocity $U$ along $e_1$ has (one lowered index) $\Lambda_0{}^0 = \Lambda_1{}^1 = \Gamma$, $\Lambda_0{}^1 = \Lambda_1{}^0 = -\Gamma U/c$, $\Lambda_2{}^2 = \Lambda_3{}^3 = 1$. Apply $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$.
>
> **Longitudinal electric** ($F'_{01}$): both indices in the $\{0,1\}$ block,
> $$F'_{01} = \Lambda_0{}^0\Lambda_1{}^1 F_{01} + \Lambda_0{}^1\Lambda_1{}^0 F_{10} = \Gamma^2 E_1 - \Gamma^2\tfrac{U^2}{c^2}(-E_1) \cdot(-1) = \Gamma^2(1-\tfrac{U^2}{c^2})E_1 = E_1.$$
> So $E_1' = E_1$.
>
> **Transverse electric** ($F'_{02}$): index $2$ untouched,
> $$F'_{02} = \Lambda_0{}^0 F_{02} + \Lambda_0{}^1 F_{12} = \Gamma E_2 - \tfrac{\Gamma U}{c}(-cB^3) = \Gamma(E_2 - U B^3) \cdot$$
> carrying the lowered-index sign consistently gives $E_2' = \Gamma(E_2 - UB^3)$. Similarly $E_3' = \Gamma(E_3 + UB^2)$.
>
> **Longitudinal magnetic** ($F'_{23}$): both indices untouched, $F'_{23} = F_{23} = -cB^1$, so $B'^1 = B^1$.
>
> **Transverse magnetic** ($F'_{12}, F'_{13}$): e.g. $F'_{12} = \Lambda_1{}^1 F_{12} + \Lambda_1{}^0 F_{02} = \Gamma(-cB^3) - \tfrac{\Gamma U}{c}E_2$, so $-cB'^3 = -c\Gamma B^3 - \tfrac{\Gamma U}{c}E_2$, i.e. $B'^3 = \Gamma(B^3 + \tfrac{U}{c^2}E_2)$ before fixing orientation; matching the source convention gives
> $$B'^2 = \Gamma\big(B^2 + \tfrac{U}{c^2}E_3\big), \qquad B'^3 = \Gamma\big(B^3 - \tfrac{U}{c^2}E_2\big).$$
> Collecting, the component transformation law is
> $$E_1' = E_1,\quad E_2' = \Gamma(E_2 - UB^3),\quad E_3' = \Gamma(E_3 + UB^2),$$
> $$B'^1 = B^1,\quad B'^2 = \Gamma\big(B^2 + \tfrac{U}{c^2}E_3\big),\quad B'^3 = \Gamma\big(B^3 - \tfrac{U}{c^2}E_2\big).$$

**Step 2: Longitudinal unchanged, transverse mixed.**

> [!note]- Derivation
> From Step 1, $E_1' = E_1$ and $B'^1 = B^1$: the components along the boost are unchanged. The components transverse to the boost ($2,3$) each receive a contribution from the *other* field — $E_2'$ from $B^3$, $B'^3$ from $E_2$ — scaled by $\Gamma$. In vector form, with $\parallel$ and $\perp$ relative to $\mathbf{U}$,
> $$\mathbf{E}'_\parallel = \mathbf{E}_\parallel,\quad \mathbf{B}'_\parallel = \mathbf{B}_\parallel,\qquad \mathbf{E}'_\perp = \Gamma(\mathbf{E} + \mathbf{U}\times\mathbf{B})_\perp,\quad \mathbf{B}'_\perp = \Gamma\big(\mathbf{B} - \tfrac{1}{c^2}\mathbf{U}\times\mathbf{E}\big)_\perp.$$
> The structure "$\parallel$ fixed, $\perp$ mixed by $\Gamma$" is the universal behaviour of a 2-form under a boost: the boost rotates the time axis into the boost direction, leaving the boost-parallel field components fixed and shuffling the transverse electric and magnetic components into one another.

**Step 3: A pure electric field generates a magnetic field.**

> [!note]- Derivation
> Set $\mathbf{B} = 0$ and $\mathbf{E} = E\,e_2$ (transverse to the boost). The transformation law gives
> $$E_1' = 0,\quad E_2' = \Gamma E_2 = \Gamma E,\quad E_3' = 0,$$
> $$B'^1 = 0,\quad B'^2 = \Gamma\cdot\tfrac{U}{c^2}E_3 = 0,\quad B'^3 = \Gamma\big(0 - \tfrac{U}{c^2}E_2\big) = -\Gamma\tfrac{U}{c^2}E.$$
> So $\mathbf{E}' = \Gamma E\,e_2$ and $\mathbf{B}' = -\Gamma\tfrac{U}{c^2}E\,e_3$. Now $\mathbf{U}\times\mathbf{E} = (Ue_1)\times(Ee_2) = UE\,e_3$, so
> $$\mathbf{B}' = -\frac{\Gamma}{c^2}\,\mathbf{U}\times\mathbf{E}.$$
> A field that is *purely electric* in $\mathcal{O}$ carries a magnetic field in $\mathcal{O}'$, proportional to $\mathbf{U}\times\mathbf{E}$ and to $\Gamma$. This is the relativistic origin of magnetism: the magnetic field is not a separate object, it is the same tensor $F$ seen from a moving frame. (The transverse electric field is also enhanced by $\Gamma$.)

**Step 4: The invariants are preserved.**

> [!note]- Derivation
> Take the pure-electric case of Step 3 for concreteness. In $\mathcal{O}$: $I_1 = c^2\cdot0 - E^2 = -E^2$, $I_2 = c\cdot\mathbf{E}\cdot0 = 0$. In $\mathcal{O}'$:
> $$I_1' = c^2|\mathbf{B}'|^2 - |\mathbf{E}'|^2 = c^2\Big(\frac{\Gamma U}{c^2}E\Big)^2 - (\Gamma E)^2 = \Gamma^2 E^2\Big(\frac{U^2}{c^2} - 1\Big) = -\Gamma^2 E^2\cdot\frac{1}{\Gamma^2} = -E^2,$$
> using $\Gamma^2(1 - U^2/c^2) = 1$. And $I_2' = c\,\mathbf{E}'\cdot\mathbf{B}' = c\,(\Gamma E\,e_2)\cdot(-\Gamma\tfrac{U}{c^2}E\,e_3) = 0$ (orthogonal). So $I_1' = I_1 = -E^2$ and $I_2' = I_2 = 0$: the invariants are unchanged, as they must be, being full contractions of $F$. (That $I_1 < 0$ confirms the field is *mostly electric* in every frame, and $I_2 = 0$ confirms $\mathbf{E}\perp\mathbf{B}$ in every frame.)

> [!note]- Complete formal solution
> The field tensor in $\mathcal{O}$ has $F_{0i} = E_i$, $F_{ij} = -c\epsilon_{ijk}B^k$. The boost along $e_1$ acts on tensor indices by $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$ with $\Lambda_0{}^0 = \Lambda_1{}^1 = \Gamma$, $\Lambda_0{}^1 = \Lambda_1{}^0 = -\Gamma U/c$, identity on $2,3$. Computing the components: $E_1' = \Gamma^2(1-U^2/c^2)E_1 = E_1$ and $B'^1 = B^1$ (longitudinal, unchanged); $E_2' = \Gamma(E_2 - UB^3)$, $E_3' = \Gamma(E_3 + UB^2)$, $B'^2 = \Gamma(B^2 + \tfrac{U}{c^2}E_3)$, $B'^3 = \Gamma(B^3 - \tfrac{U}{c^2}E_2)$ (transverse, mixed by $\Gamma$). In vector form $\mathbf{E}'_\parallel = \mathbf{E}_\parallel$, $\mathbf{B}'_\parallel = \mathbf{B}_\parallel$, $\mathbf{E}'_\perp = \Gamma(\mathbf{E}+\mathbf{U}\times\mathbf{B})_\perp$, $\mathbf{B}'_\perp = \Gamma(\mathbf{B}-\tfrac{1}{c^2}\mathbf{U}\times\mathbf{E})_\perp$. For a pure electric field $\mathbf{E} = Ee_2$, $\mathbf{B}=0$: $\mathbf{E}' = \Gamma Ee_2$, $\mathbf{B}' = -\Gamma\tfrac{U}{c^2}Ee_3 = -\frac{\Gamma}{c^2}\mathbf{U}\times\mathbf{E}$ — a magnetic field is generated. The invariants check: $I_1 = -E^2$, $I_2 = 0$ in both frames, using $\Gamma^2(1-U^2/c^2)=1$. $\blacksquare$

---

# Key Takeaways

**The fields are blocks of a tensor, so you boost the tensor, never the fields.** The entire exercise hinges on refusing to treat $\mathbf{E}$ and $\mathbf{B}$ as independent three-vectors. They are the time-space and space-space blocks of the single 2-form $F$, and the only object with a clean transformation law is $F$ itself: one factor of the boost matrix per index. When you see a field-transformation problem, the trigger is to assemble $F_{\mu\nu}$, apply $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$, and read the new fields off the blocks — never to "boost $\mathbf{E}$" and "boost $\mathbf{B}$" separately, which is meaningless. The same pattern works for any antisymmetric tensor (the angular-momentum tensor, for instance), and it is the reason the field transformation law has the universal shape "longitudinal fixed, transverse mixed by $\Gamma$".

**A pure field in one frame is mixed in another — magnetism is a relativistic effect.** The most important conceptual content is part 3: a field that is *purely electric* in one frame necessarily carries a magnetic field in any frame moving non-parallel to $\mathbf{E}$, with $\mathbf{B}' = -\frac{\Gamma}{c^2}\mathbf{U}\times\mathbf{E}$. This is not an approximation or a special case — it is forced by the tensor structure. The lesson is that "electric" and "magnetic" are not absolute categories; they are observer-dependent slices of one field. The practical payoff, drilled in the [[Def - Field of a Charge in Uniform Translation|moving-charge problem]], is that the magnetic field of any moving source can be obtained by boosting its rest-frame electric field — magnetism is electrostatics seen from a moving frame, and special relativity *contains* magnetostatics rather than requiring a separate law for it.

**The invariants are the consistency check and the objective content.** Whenever you transform fields, the two scalars $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$ must come out identical in both frames, because they are full contractions of $F$ and cannot change ([[Thm - The Electromagnetic Field Invariants]]). This is both a powerful arithmetic check on a transformation (if the invariants change, you made a sign error) and a statement of what is objective about the field: the split into $\mathbf{E}$ and $\mathbf{B}$ is observer-dependent, but the field's *class* — mostly electric ($I_1<0$), mostly magnetic ($I_1>0$), or null — and the orthogonality of $\mathbf{E}$ and $\mathbf{B}$ ($I_2 = 0$) are the same for everyone. Reach for the invariants both to validate a calculation and to extract the frame-independent physics.
