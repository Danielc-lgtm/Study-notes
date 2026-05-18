---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Lorentz Group"
  - "Def - The Lorentz Transformation"
  - "Def - Four-Vector"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

Working with $c = 1$. An inertial frame $S$ measures an electric field $\mathbf{E} = (E_x, E_y, E_z)$ and a magnetic field $\mathbf{B} = (B_x, B_y, B_z)$ at some event. A second frame $S'$ moves with velocity $v$ along the common $x$-axis of $S$, so $S'$ is related to $S$ by a boost $\Lambda[v]$.

The six numbers $(\mathbf{E}, \mathbf{B})$ are the independent components of a single antisymmetric Lorentz tensor, the **field-strength tensor** $F_{\mu\nu}$. Because $F_{\mu\nu}$ is a tensor, its components in $S'$ are obtained from those in $S$ by applying one factor of the boost matrix to each index:
$$F'_{\mu\nu} = \Lambda_\mu{}^\alpha\,\Lambda_\nu{}^\beta\,F_{\alpha\beta}.$$

1. Write $F_{\mu\nu}$ explicitly as a $4\times4$ matrix in terms of $\mathbf{E}$ and $\mathbf{B}$, and confirm it is antisymmetric with exactly six independent entries.
2. Carry out the tensor transformation $F' = \Lambda F \Lambda^{\mathsf T}$ for the $x$-boost and read off the transformed fields. Show that the components **parallel** to the boost are unchanged, $E'_x = E_x$ and $B'_x = B_x$, while the **perpendicular** components mix:
$$E'_y = \gamma(E_y - vB_z), \quad E'_z = \gamma(E_z + vB_y), \quad B'_y = \gamma(B_y + vE_z), \quad B'_z = \gamma(B_z - vE_y).$$
3. As a concrete instance, take a frame $S$ in which there is a **pure electric field** $\mathbf{E} = (0, E, 0)$ and no magnetic field, $\mathbf{B} = \mathbf{0}$ — the field of a static charge distribution, say. Show that an observer in $S'$ measures a nonzero magnetic field, and identify it. Explain why this is the origin of the magnetic force felt by a moving charge.

**Recall:**

A boost along $x$ relating $S$ and $S'$ moving at relative velocity $v$ is the [[Def - The Lorentz Transformation|Lorentz transformation]]

![[Def - The Lorentz Group#Examples / Corollaries]]

with $\gamma = (1-v^2)^{-1/2}$. The matrix that boosts components *from* $S'$ *to* $S$ is $\Lambda[v]$; its inverse, boosting from $S$ to $S'$, is $\Lambda[-v]$ (flip the sign of $v$).

A [[Def - Four-Vector|four-vector]] is an object whose components transform by one factor of $\Lambda$, $X^\mu = \Lambda^\mu{}_\nu X'^\nu$. A **tensor** of rank two is the immediate generalisation: an object $F_{\mu\nu}$ carrying *two* indices, transforming with one factor of the transformation matrix per index. With both indices down, the transformation law is $F'_{\mu\nu} = \Lambda_\mu{}^\alpha \Lambda_\nu{}^\beta F_{\alpha\beta}$, where $\Lambda_\mu{}^\alpha$ is the matrix taking $S \to S'$. In plain matrix notation, treating $F$ as a $4\times4$ matrix, this is $F' = \Lambda F \Lambda^{\mathsf T}$ with $\Lambda$ the $S \to S'$ boost. The [[Def - Minkowski Space and the Metric|Minkowski metric]] $\eta = \mathrm{diag}(1,-1,-1,-1)$ is used to raise and lower indices.

The **field-strength tensor** packages the electric and magnetic fields. With indices down it is
$$F_{\mu\nu} = \begin{pmatrix} 0 & E_x & E_y & E_z \\ -E_x & 0 & B_z & -B_y \\ -E_y & -B_z & 0 & B_x \\ -E_z & B_y & -B_x & 0 \end{pmatrix},$$
antisymmetric, $F_{\mu\nu} = -F_{\nu\mu}$, so its diagonal vanishes and its $\binom{4}{2}=6$ above-diagonal entries — three holding $\mathbf{E}$, three holding $\mathbf{B}$ — are the independent data. This single object is what Maxwell's equations are really about; $\mathbf{E}$ and $\mathbf{B}$ are its frame-dependent slices.

---

# Convergent Strategy

**Problem class.** This is a *structural / transform-an-object* problem in the sense of the [[Special Relativity I — Lorentz Transformations and Minkowski Space#Sources and Targets|topic's Sources and Targets]]: a quantity is given in one frame and wanted in another, and the work is to apply the correct transformation law and bookkeep which frame measures what. The new feature relative to earlier exercises is that the object being transformed is not a four-vector but a rank-two tensor, so the boost is applied *twice*.

**Assumption pattern.** The signpost is the phrase "find the fields in a boosted frame". The fields $\mathbf{E}, \mathbf{B}$ do not transform among themselves as three-vectors, and there is no shortcut in three-vector language. The only clean route is to recognise that the six field components are the entries of one Lorentz tensor $F_{\mu\nu}$, and that tensors have a *known* transformation law. The instant a problem asks how a non-scalar electromagnetic quantity changes between frames, the move is: assemble it into a tensor, transform the tensor, read the components back off.

**Theorem routing.** The route is fixed and mechanical once the tensor is assembled. The transformation law $F'_{\mu\nu} = \Lambda_\mu{}^\alpha \Lambda_\nu{}^\beta F_{\alpha\beta}$ — one [[Def - The Lorentz Group|Lorentz matrix]] per index — is the matrix product $F' = \Lambda F \Lambda^{\mathsf T}$. Multiply three $4\times4$ matrices, and the entries of $F'$ are the transformed fields. The defining property $\Lambda^{\mathsf T}\eta\Lambda = \eta$ of the Lorentz group is what guarantees $F'$ is again antisymmetric, so the output is again a legitimate field tensor.

**Key decision point.** Two non-obvious choices make the problem go smoothly. First, *do not* try to transform $\mathbf{E}$ and $\mathbf{B}$ directly — there is no three-vector law, and attempting one is the standard way to get stuck. Recognising that the object with a transformation law is the *tensor*, not the fields, is the whole insight. Second, get the *direction* of the boost right: $F' = \Lambda F \Lambda^{\mathsf T}$ uses the $S \to S'$ matrix, which is $\Lambda[-v]$ if $\Lambda[v]$ is the matrix conventionally written for the boost. A sign error here flips the sign of every mixing term, which is exactly the kind of bookkeeping slip the [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] warns is where relativity errors live.

---

# Legal Operations Used

1. **Apply the Lorentz transformation in matrix form** ([[Def - The Lorentz Transformation]]). The $x$-boost matrix is the engine of the whole computation; here it acts not on a coordinate column but on each of the two indices of a tensor.

2. **Recognise a quantity as a tensor and transform it by its transformation law.** The six field components are not three-vectors; they are the entries of the rank-two tensor $F_{\mu\nu}$ ([[Def - Four-Vector|four-vectors and tensors]]). A tensor with two lower indices transforms as $F' = \Lambda F \Lambda^{\mathsf T}$ — one factor of $\Lambda$ per index.

3. **Use the defining property of the Lorentz group** $\Lambda^{\mathsf T}\eta\Lambda = \eta$ ([[Def - The Lorentz Group]]) to confirm that the transformed $F'$ is again antisymmetric, hence a genuine field tensor — the structural check that the operation is legal.

4. **Compute an invariant in a convenient frame.** As a consistency check, the two scalars $\mathbf{E}\cdot\mathbf{B}$ and $E^2 - B^2$ are Lorentz invariant — built from $F_{\mu\nu}$ by full index contraction — and must come out equal in $S$ and $S'$.

---

# Hints

> [!note]- Hint 1
> Do not look for a three-vector transformation law for $\mathbf{E}$ and $\mathbf{B}$ — there isn't one. The six numbers $(\mathbf{E}, \mathbf{B})$ are the independent entries of a single rank-two antisymmetric tensor $F_{\mu\nu}$. A tensor *does* have a transformation law: one factor of the boost matrix per index.

> [!note]- Hint 2
> With both indices down, the law is $F'_{\mu\nu} = \Lambda_\mu{}^\alpha \Lambda_\nu{}^\beta F_{\alpha\beta}$. Read as ordinary matrix multiplication with $F$ a $4\times4$ matrix, this is $F' = \Lambda F \Lambda^{\mathsf T}$, where $\Lambda$ is the matrix that boosts $S \to S'$. Write down the $4\times4$ boost matrix and the $4\times4$ matrix $F$, and multiply.

> [!note]- Hint 3
> The boost only touches the $0$ and $1$ rows and columns; the $2,3$ block of $\Lambda$ is the identity. So only entries of $F$ with a $0$ or $1$ index are altered. $F_{23} = B_x$ involves neither, so $B'_x = B_x$; $F_{01} = E_x$ involves both in a way that the boost leaves fixed (the boost preserves the $(0,1)$-plane's antisymmetric form), so $E'_x = E_x$. The genuine mixing is in the entries $F_{02}, F_{03}, F_{12}, F_{13}$ — one boosted index, one untouched.

> [!note]- Hint 4
> For part 3, set $\mathbf{B} = \mathbf{0}$ and $\mathbf{E} = (0,E,0)$ in the part-2 formulas. The only field component is $E_y = E$. Then $E'_y = \gamma E$ and $B'_z = \gamma(B_z - vE_y) = -\gamma v E$. A pure electric field in $S$ carries a magnetic field $B'_z = -\gamma v E$ in $S'$ — the field of a charge is partly magnetic to anyone who sees the charge move.

---

# Solution

The six components $(\mathbf{E}, \mathbf{B})$ are not three-vectors that transform among themselves; they are the independent entries of one antisymmetric Lorentz tensor $F_{\mu\nu}$. Transforming the *tensor* — one factor of the boost matrix per index — produces a transformation law for the fields in which the components along the boost are inert and the perpendicular components rotate $\mathbf{E}$ into $\mathbf{B}$ and back.

**Step 1: The field tensor and its antisymmetry.**

The electromagnetic field is the rank-two antisymmetric tensor
$$F_{\mu\nu} = \begin{pmatrix} 0 & E_x & E_y & E_z \\ -E_x & 0 & B_z & -B_y \\ -E_y & -B_z & 0 & B_x \\ -E_z & B_y & -B_x & 0 \end{pmatrix}.$$
Antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ kills the four diagonal entries and pairs the off-diagonal ones, leaving $\binom{4}{2} = 6$ independent numbers: the three $F_{0i} = E_i$ and the three spatial $F_{ij} = \varepsilon_{ijk}B_k$.

> [!note]- Derivation
> A general $4\times4$ matrix has $16$ entries. Imposing antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ forces the diagonal to vanish ($F_{\mu\mu} = -F_{\mu\mu} \Rightarrow F_{\mu\mu} = 0$) and ties each below-diagonal entry to minus its above-diagonal partner, leaving $16 - 4 = 12$ entries determined by $6$ free ones. Those six are organised so that the time–space block holds the electric field — $F_{0i} = E_i$ for $i = 1,2,3$ — and the space–space block holds the magnetic field through $F_{ij} = \varepsilon_{ijk}B_k$, giving $F_{12} = B_z$, $F_{23} = B_x$, $F_{31} = B_y$. That a single tensor has exactly six slots, and the electromagnetic field has exactly six components ($\mathbf{E}$ and $\mathbf{B}$), is the first sign that $\mathbf{E}$ and $\mathbf{B}$ are two faces of one object. The placement — $\mathbf{E}$ in the time rows, $\mathbf{B}$ in the space block — is itself meaningful: it forecasts that a boost, which rotates time into space, will rotate $\mathbf{E}$ into $\mathbf{B}$.

**Step 2: Transform the tensor; parallel components inert, perpendicular components mix.**

Applying $F' = \Lambda F \Lambda^{\mathsf T}$ with the $x$-boost gives
$$E'_x = E_x, \quad B'_x = B_x,$$
$$E'_y = \gamma(E_y - vB_z), \quad E'_z = \gamma(E_z + vB_y), \quad B'_y = \gamma(B_y + vE_z), \quad B'_z = \gamma(B_z - vE_y).$$
The components along the boost direction are unchanged; the perpendicular components of $\mathbf{E}$ and $\mathbf{B}$ rotate into one another with a factor of $\gamma$.

> [!note]- Derivation
> Take $\Lambda$ to be the matrix boosting $S \to S'$ — that is, $\Lambda[-v]$ in the convention where $\Lambda[v]$ boosts $S' \to S$:
> $$\Lambda = \begin{pmatrix} \gamma & -\gamma v & 0 & 0 \\ -\gamma v & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
> The transformation law for a twice-covariant tensor, $F'_{\mu\nu} = \Lambda_\mu{}^\alpha \Lambda_\nu{}^\beta F_{\alpha\beta}$, is the matrix product $F' = \Lambda F \Lambda^{\mathsf T}$. Compute it in two stages. First $M = \Lambda F$:
> $$M = \Lambda F = \begin{pmatrix} \gamma & -\gamma v & 0 & 0 \\ -\gamma v & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 0 & E_x & E_y & E_z \\ -E_x & 0 & B_z & -B_y \\ -E_y & -B_z & 0 & B_x \\ -E_z & B_y & -B_x & 0 \end{pmatrix}.$$
> Row $0$ of $M$ is $\gamma(\text{row }0\text{ of }F) - \gamma v(\text{row }1\text{ of }F) = \gamma(0, E_x, E_y, E_z) - \gamma v(-E_x, 0, B_z, -B_y) = (\gamma vE_x,\ \gamma E_x,\ \gamma E_y - \gamma vB_z,\ \gamma E_z + \gamma vB_y)$. Row $1$ of $M$ is $-\gamma v(\text{row }0\text{ of }F) + \gamma(\text{row }1\text{ of }F) = -\gamma v(0,E_x,E_y,E_z) + \gamma(-E_x,0,B_z,-B_y) = (-\gamma E_x,\ -\gamma vE_x,\ -\gamma vE_y + \gamma B_z,\ -\gamma vE_z - \gamma B_y)$. Rows $2$ and $3$ of $M$ are just rows $2$ and $3$ of $F$ unchanged, since the lower block of $\Lambda$ is the identity.
> 
> Now $F' = M\Lambda^{\mathsf T}$, and $\Lambda^{\mathsf T} = \Lambda$ here since the boost matrix is symmetric. Right-multiplication by $\Lambda$ mixes columns $0$ and $1$ the same way left-multiplication mixed rows. Reading off the entries of the result:
> - $F'_{01} = E'_x$: the $(0,1)$ entry comes out $\gamma^2 E_x - \gamma^2 v^2 E_x = \gamma^2(1-v^2)E_x = E_x$, using $\gamma^2(1-v^2) = 1$. So $E'_x = E_x$.
> - $F'_{23} = B'_x$: rows and columns $2,3$ are untouched by the boost, so $F'_{23} = F_{23} = B_x$. So $B'_x = B_x$.
> - $F'_{02} = E'_y$: this entry is $\gamma F_{02} - \gamma v F_{12} = \gamma E_y - \gamma v B_z$. So $E'_y = \gamma(E_y - vB_z)$.
> - $F'_{03} = E'_z$: $\gamma F_{03} - \gamma v F_{13} = \gamma E_z - \gamma v(-B_y) = \gamma(E_z + vB_y)$.
> - $F'_{12} = B'_z$: $-\gamma v F_{02} + \gamma F_{12} = -\gamma v E_y + \gamma B_z = \gamma(B_z - vE_y)$.
> - $F'_{31} = B'_y$: $-\gamma v F_{30} + \gamma F_{31}$, and with $F_{30} = -E_z$, $F_{31} = B_y$ this is $\gamma v E_z + \gamma B_y = \gamma(B_y + vE_z)$.
> 
> Collecting the results, the components *along* the boost ($x$) are unchanged, $E'_x = E_x$ and $B'_x = B_x$, while the four *transverse* components mix:
> $$E'_y = \gamma(E_y - vB_z), \quad E'_z = \gamma(E_z + vB_y), \quad B'_y = \gamma(B_y + vE_z), \quad B'_z = \gamma(B_z - vE_y).$$
> Two structural remarks. The transformed $F'$ is again antisymmetric — guaranteed in advance, since $\Lambda^{\mathsf T}\eta\Lambda = \eta$ means a Lorentz transformation maps antisymmetric tensors to antisymmetric tensors — so $F'$ is again a legitimate field tensor, with fields $\mathbf{E}', \mathbf{B}'$ read off its slots. And the pattern is exactly a hyperbolic rotation of the pair $(\mathbf{E}_\perp, \mathbf{B}_\perp)$: writing it in vector form, $\mathbf{E}'_\perp = \gamma(\mathbf{E}_\perp + \mathbf{v}\times\mathbf{B})_\perp$ and $\mathbf{B}'_\perp = \gamma(\mathbf{B}_\perp - \mathbf{v}\times\mathbf{E})_\perp$, the boost rotates $\mathbf{E}$ into $\mathbf{B}$ just as it rotates $t$ into $x$.

**Step 3: A pure electric field carries a magnetic field for a moving observer.**

Set $\mathbf{B} = \mathbf{0}$ and $\mathbf{E} = (0, E, 0)$ in $S$. The transformation gives
$$\mathbf{E}' = (0,\ \gamma E,\ 0), \qquad \mathbf{B}' = (0,\ 0,\ -\gamma vE).$$
There *is* a magnetic field in $S'$, even though $S$ saw none. A field that is purely electric to one observer is electric *and* magnetic to another in relative motion — and this is the origin of the magnetic force on a moving charge.

> [!note]- Derivation
> With $\mathbf{B} = \mathbf{0}$ the part-2 formulas collapse. The parallel components vanish trivially: $E'_x = E_x = 0$, $B'_x = B_x = 0$. The transverse electric components: $E'_y = \gamma(E_y - vB_z) = \gamma E$ and $E'_z = \gamma(E_z + vB_y) = 0$. The transverse magnetic components: $B'_y = \gamma(B_y + vE_z) = 0$ and $B'_z = \gamma(B_z - vE_y) = -\gamma vE$. So $\mathbf{E}' = (0, \gamma E, 0)$ and $\mathbf{B}' = (0, 0, -\gamma vE)$.
> 
> The physics this unlocks is the unification of the electric and magnetic forces. Consider a long straight wire carrying a steady current — a line of positive ions at rest and a line of conduction electrons drifting along it. In the wire's rest frame the ion and electron charge densities cancel, the wire is electrically neutral, and a test charge sitting *beside* the wire feels no electric force; what it does feel, if it is moving parallel to the wire, is the magnetic force from the field $\mathbf{B}$ that the current produces. Now boost into the rest frame of that test charge. In this frame the test charge is at rest, so by definition it feels no *magnetic* force — magnetic forces act only on moving charges. Yet the force on it cannot simply disappear; a force is a physical fact, and frames must agree on whether the charge accelerates. The resolution is exactly the transformation computed above. In the boosted frame the two charge lines of the wire are length-contracted by *different* amounts — the electrons and ions have different velocities, hence different $\gamma$ factors — so their densities no longer cancel and the wire carries a net charge. The wire is now electrically charged, and the test charge feels an *electric* force. The magnetic force in one frame and the electric force in the other are the same physical interaction, related by the boost; what one observer attributes to $\mathbf{B}$, another attributes to $\mathbf{E}$, because $\mathbf{E}$ and $\mathbf{B}$ are slices of the one tensor $F_{\mu\nu}$. Magnetism is not a separate force of nature; it is what electrostatics looks like once you take seriously that the source is moving and that simultaneity and length are frame-dependent. The factor $\gamma v$ in $B'_z = -\gamma vE$ is, to leading order in $v$, just $v$ — and $vE$ is precisely the magnetic field strength a slow charge density expects, the relativistic correction to Coulomb's law at first order in $v/c$.

> [!note]- Complete formal solution
> **The tensor.** The electromagnetic field is the antisymmetric rank-two tensor $F_{\mu\nu}$ with $F_{0i} = E_i$ and $F_{ij} = \varepsilon_{ijk}B_k$, i.e.
> $$F_{\mu\nu} = \begin{pmatrix} 0 & E_x & E_y & E_z \\ -E_x & 0 & B_z & -B_y \\ -E_y & -B_z & 0 & B_x \\ -E_z & B_y & -B_x & 0 \end{pmatrix}.$$
> Antisymmetry leaves $\binom42 = 6$ independent entries — the three $E_i$ and three $B_i$.
> 
> **The transformation.** Under a boost $S \to S'$ along $x$ with matrix $\Lambda = \mathrm{diag\text{-}block}\big(\begin{smallmatrix}\gamma & -\gamma v\\ -\gamma v & \gamma\end{smallmatrix},\ I_2\big)$, a twice-covariant tensor transforms as $F'_{\mu\nu} = \Lambda_\mu{}^\alpha\Lambda_\nu{}^\beta F_{\alpha\beta}$, i.e. $F' = \Lambda F\Lambda^{\mathsf T}$. Multiplying out the three $4\times4$ matrices and using $\gamma^2(1-v^2) = 1$ gives, for the components along the boost,
> $$E'_x = E_x, \qquad B'_x = B_x,$$
> and for the perpendicular components,
> $$E'_y = \gamma(E_y - vB_z), \quad E'_z = \gamma(E_z + vB_y), \quad B'_y = \gamma(B_y + vE_z), \quad B'_z = \gamma(B_z - vE_y).$$
> The result $F'$ is again antisymmetric (because $\Lambda^{\mathsf T}\eta\Lambda = \eta$), hence a legitimate field tensor. In vector form: $\mathbf{E}'_\parallel = \mathbf{E}_\parallel$, $\mathbf{B}'_\parallel = \mathbf{B}_\parallel$, and $\mathbf{E}'_\perp = \gamma(\mathbf{E} + \mathbf{v}\times\mathbf{B})_\perp$, $\mathbf{B}'_\perp = \gamma(\mathbf{B} - \mathbf{v}\times\mathbf{E})_\perp$.
> 
> **The pure electric field.** Substituting $\mathbf{B} = \mathbf{0}$, $\mathbf{E} = (0,E,0)$ gives $\mathbf{E}' = (0,\gamma E,0)$ and $\mathbf{B}' = (0,0,-\gamma vE)$. A field purely electric in $S$ is electric and magnetic in $S'$. As a check, the invariants are preserved: $\mathbf{E}\cdot\mathbf{B} = 0 = \mathbf{E}'\cdot\mathbf{B}'$, and $E^2 - B^2 = E^2$ in $S$ while $E'^2 - B'^2 = \gamma^2 E^2 - \gamma^2 v^2 E^2 = \gamma^2(1-v^2)E^2 = E^2$ in $S'$. The transformed field is the origin of the magnetic force on a moving charge: the magnetic interaction is electrostatics seen from a frame in which the source charges move. $\blacksquare$

---

# Key Takeaways

**When a non-scalar electromagnetic quantity must be transformed between frames, assemble it into a tensor and transform the tensor — never the fields directly.** The fields $\mathbf{E}$ and $\mathbf{B}$ are three-vectors in the language of a single frame, but they are *not* three-vectors with respect to boosts: there is no $3\times3$ matrix that sends $(\mathbf{E},\mathbf{B})$ to $(\mathbf{E}',\mathbf{B}')$ frame-vector-style, and every attempt to find one stalls. The object that *does* carry a transformation law is the rank-two tensor $F_{\mu\nu}$, and the law is the universal one: one factor of the Lorentz matrix per index, $F' = \Lambda F\Lambda^{\mathsf T}$. This is the general lesson of which four-vector transformation is the rank-one case — a [[Def - Four-Vector|four-vector]] gets one $\Lambda$, a rank-two tensor gets two, a rank-$k$ tensor gets $k$. The trigger to recognise: any time a problem gives you a multi-component physical quantity in one frame and asks for it in another, the first question is "what is its tensor rank?", and the answer dictates how many copies of $\Lambda$ to apply. The same move handles the transformation of the stress tensor, the current density, the gradient of a field — anything with indices.

**Parallel components are inert, perpendicular components mix — because a boost only touches the plane it acts in.** The split $E'_\parallel = E_\parallel$, $B'_\parallel = B_\parallel$ with the transverse components rotating is not special to electromagnetism; it is a feature of every $x$-boost. The boost matrix is the identity on the $y,z$ block and a hyperbolic rotation on the $t,x$ block, so any tensor index pointing along $y$ or $z$ is left alone and any index in the $t,x$ plane is rotated. For the field tensor, the $x$-components of $\mathbf{E}$ and $\mathbf{B}$ sit in tensor slots that the boost happens to preserve, while the transverse components sit in slots with exactly one boosted index — and one boosted index is what produces the cross-term mixing of $\mathbf{E}$ into $\mathbf{B}$. The reusable principle: to see how *anything* transforms under a boost, decompose it into pieces parallel and perpendicular to the boost; the parallel pieces are typically simplest (often invariant), and the action is in the perpendicular pieces. This is the same decomposition that makes [[Ex - Length contraction|length contraction]] act only along the direction of motion.

**Electricity and magnetism are one field; magnetism is electrostatics seen from a moving frame.** The pure-electric-field instance is the conceptual heart of the exercise. That a static charge — pure $\mathbf{E}$, no $\mathbf{B}$ — acquires a magnetic field $\mathbf{B}' = \gamma\,\mathbf{v}\times\mathbf{E}$ for an observer who sees it move is not a curiosity; it is the explanation of magnetism itself. The magnetic force on a charge moving past a current-carrying wire, computed in the wire's frame, becomes a purely *electric* force in the charge's own rest frame, where the wire — its electron and ion lines length-contracted by different factors — is no longer neutral. The same physical push, two names. This is why one cannot have a consistent relativistic theory of the electric field *alone*: the moment you boost, an electric field generates a magnetic one, so the magnetic field is forced into existence by relativity plus electrostatics. The general trigger this installs: whenever a force "vanishes" in one frame (here, the magnetic force on a charge brought to rest), do not conclude the interaction is gone — look for the same interaction reappearing under a different name, because frames must agree on whether a particle accelerates even when they disagree on *why*. The invariants $\mathbf{E}\cdot\mathbf{B}$ and $E^2 - B^2$ are the bookkeeping that enforces this agreement: they are the same in every frame, so "purely electric" ($\mathbf{E}\cdot\mathbf{B} = 0$, $E^2 - B^2 > 0$) is a frame-independent *class* of field even though the split into $\mathbf{E}$ and $\mathbf{B}$ is not — and a field can be boosted to purely magnetic only if it was in the opposite class, $E^2 - B^2 < 0$, to begin with.
