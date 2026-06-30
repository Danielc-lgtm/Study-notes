---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Poincaré Group"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

A Poincaré transformation can be read in two ways. The **passive** reading relates the coordinates of *one event* in two inertial frames; the **active** reading sends *one event to a different event* within a single frame. Working with $c = 1$:

1. State the passive transformation: if an event $M$ has coordinates $(x^\alpha)$ in frame $\mathcal{O}$ and $(x'^\alpha)$ in frame $\mathcal{O}'$, write $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$, and explain that *nothing physically moves* — only the labels change.
2. State the active transformation: the [[Def - The Poincaré Group|Poincaré map]] $f$ sends an event $M$ to a *new* event $f(M)$, with $\overrightarrow{O\,f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}$ in one fixed frame, so that *something physically moves*.
3. Show the two have *identical algebraic form* but opposite meaning, and exhibit the relationship between the basis transformation $e_\alpha = \Lambda^\beta{}_\alpha e'_\beta$ and the coordinate transformation $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$ — i.e. that components transform by the inverse-transpose of the basis.
4. Give a concrete $1+1$ boost both ways and show that the *same* matrix $\Lambda$ serves both, with the active interpretation moving a particle and the passive interpretation relabelling a fixed event.

**Recall:**

![[Def - The Poincaré Group#The Definition]]

A [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ has matrix $\Lambda^\alpha{}_\beta$ in a basis. Under a change of basis $e_\alpha = \Lambda^\beta{}_\alpha e'_\beta$ (new basis $e'$ in terms of old $e$), the *components* of a fixed vector transform contravariantly, by the inverse matrix. The distinction between active (move the object) and passive (relabel the coordinates) is universal in physics; conflating them is the commonest source of sign and transpose errors.

---

# Convergent Strategy

**Problem class.** A *conceptual-disambiguation* problem: two transformations with the same formula but opposite meaning. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] warns that the same matrix serves both viewpoints and that one must declare which before writing it down.

**Assumption pattern.** Both readings use the same Lorentz matrix $\Lambda$ and translation. The signpost distinguishing them is *what is held fixed*: passive holds the event fixed and changes the frame; active holds the frame fixed and moves the event. The relationship between them is the inverse-transpose rule connecting basis change to component change.

**Theorem routing.** No theorem — the content is the careful identification of the two interpretations and the inverse relationship $e_\alpha = \Lambda^\beta{}_\alpha e'_\beta$ versus $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$. The route is to write both, note their identical form, and trace why a sign or transpose error comes from confusing them.

**Key decision point.** The crux is that the matrix relating the *bases* is the inverse of the matrix relating the *coordinates*: if the new basis is $e'_\alpha = (\Lambda^{-1})^\beta{}_\alpha e_\beta$, then the components transform by $\Lambda$, $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$ (contravariant = "against" the basis). Deciding, before writing any matrix, whether the event moves (active) or the frame does (passive), and which way $\Lambda$ versus $\Lambda^{-1}$ goes, is the entire discipline of the exercise.

---

# Legal Operations Used

1. **Distinguish active from passive before writing a matrix** (operation underlying illegal operation 3 of the topic page). The exercise is the explicit working-through of the active/passive distinction that prevents the inverse-versus-transpose error.

2. **Decompose a Poincaré transformation as $(\boldsymbol{v}, \Lambda)$** (operation 4 from the topic page), applied in both the active reading (the map $f$) and the passive reading (the coordinate change).

---

# Hints

> [!note]- Hint 1
> Passive: the event $M$ does not move. You are reading its *one* spacetime location off two different coordinate grids. The formula $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$ converts the $\mathcal{O}$-labels to the $\mathcal{O}'$-labels of the same point.

> [!note]- Hint 2
> Active: the event *does* move. You apply the map $f$ to $M$ and get a genuinely different event $f(M)$, both described in the *same* frame $\mathcal{O}$. The formula $\overrightarrow{O\,f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}$ gives the coordinates of the new event.

> [!note]- Hint 3
> If the new basis is written in terms of the old by $e'_\alpha = (\Lambda^{-1})^\beta{}_\alpha e_\beta$, then a fixed vector $X = x^\beta e_\beta = x'^\alpha e'_\alpha$ has new components $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$ — components transform by $\Lambda$ while the basis transforms by $\Lambda^{-1}$. This inverse relationship is the source of the active/passive sign flip.

> [!note]- Hint 4
> In $1+1$, the boost matrix is $\Lambda = \begin{pmatrix}\gamma & \gamma v\\ \gamma v & \gamma\end{pmatrix}$ acting on $(t, x)$. Actively, it moves a particle at rest, $(t, 0)\mapsto(\gamma t, \gamma v t)$ — a particle now moving at velocity $v$. Passively, the *same* matrix relabels a fixed event into the coordinates of a frame moving at $-v$ (so that the fixed event appears to move at $+v$). The active boost by $+v$ and the passive boost to a frame moving at $-v$ use the same $\Lambda$.

---

# Solution

The two readings share a formula and oppose in meaning. Step 1 states the passive reading (relabel a fixed event). Step 2 states the active reading (move an event in a fixed frame). Step 3 exhibits the inverse relationship between basis change and component change. Step 4 gives a concrete boost both ways.

**Step 1: Passive — relabel a fixed event.**

> [!note]- Derivation
> Two inertial observers $\mathcal{O}$ and $\mathcal{O}'$ lay down two coordinate grids on the *same* spacetime. A single event $M$ — a flashbulb going off, say — has coordinates $(x^\alpha)$ as read by $\mathcal{O}$ and coordinates $(x'^\alpha)$ as read by $\mathcal{O}'$. These are two labellings of *one* point; the flashbulb does not move. The relation is the **passive Poincaré transformation** (Gourgoulhon's eq. 8.12):
> $$x'^\alpha = \Lambda^\alpha{}_\beta\,x^\beta + x_0'^\alpha,$$
> where $\Lambda$ is the Lorentz matrix relating the two frames' axes and $x_0'^\alpha$ is the offset of their origins (the coordinates, in $\mathcal{O}'$, of $\mathcal{O}$'s origin event). Nothing physical changes — only the description. This is the transformation one uses to answer "given the event's coordinates in $S$, what are its coordinates in $S'$?"

**Step 2: Active — move an event in a fixed frame.**

> [!note]- Derivation
> Now fix a single frame $\mathcal{O}$ and apply the [[Def - The Poincaré Group|Poincaré map]] $f$ to an event $M$. The map produces a *genuinely different* event $f(M)$ — the result of physically sliding and rotating the event through spacetime. Both $M$ and $f(M)$ are described in the *same* frame $\mathcal{O}$. The relation is the **active Poincaré transformation** (Gourgoulhon's eq. 8.18–8.19):
> $$\overrightarrow{O\,f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}, \qquad\text{i.e.}\qquad x'^\alpha = \Lambda^\alpha{}_\beta\,x^\beta + x_0'^\alpha,$$
> where now $(x'^\alpha)$ are the coordinates of the *new* event $f(M)$ in the *same* frame, $(x^\alpha)$ those of $M$, and $x_0'^\alpha = \boldsymbol{v}$ is the translation. Here something physical moves — a particle initially at $M$ is carried to $f(M)$. This is the transformation one uses to model a physical boost of an apparatus or a rigid displacement of a system.

**Step 3: Identical form, opposite meaning, inverse relationship.**

> [!note]- Derivation
> Comparing Steps 1 and 2: the two transformations have **identical algebraic form**, $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$, but the symbols mean different things. Passively, $(x^\alpha)$ and $(x'^\alpha)$ are *two coordinate systems* for one event; actively, they are *two events* in one coordinate system. Gourgoulhon flags exactly this (his remark after eq. 8.19): "this relation has the same structure as [the passive one], the difference being that here $x'^\alpha$ stands for the coordinates of the image of a point by $f$, whereas [passively] $(x'^\alpha)$ and $(x^\alpha)$ are two different coordinate systems."
>
> The inverse relationship that makes this consistent: under a passive change of frame, the *basis* vectors transform one way and the *components* the opposite way. If the two frames' bases are related by
> $$e_\alpha = \Lambda^\beta{}_\alpha\,e'_\beta \qquad\text{(Gourgoulhon eq. 8.11: old basis in terms of new)},$$
> then a *fixed* vector $X = x^\alpha e_\alpha = x'^\beta e'_\beta$ has components related by the *inverse-transpose*: substituting $e_\alpha = \Lambda^\beta{}_\alpha e'_\beta$ gives $X = x^\alpha\Lambda^\beta{}_\alpha e'_\beta$, so matching coefficients of $e'_\beta$, $x'^\beta = \Lambda^\beta{}_\alpha x^\alpha$. The basis transforms by $\Lambda$ (with indices $\Lambda^\beta{}_\alpha$, summing the *upper* on the new basis), the components by the *same* $\Lambda$ but contracted on the *other* index — and the matrix relating coordinate grids $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta$ is the inverse of the matrix that would actively move a vector to have those new components. The upshot: **a passive change to a frame moving at velocity $v$ is the same matrix as an active boost by velocity $-v$** (and vice versa). This inverse is exactly the sign that flips when active and passive are confused.

**Step 4: A concrete boost both ways.**

> [!note]- Derivation
> Work in $1+1$ with the boost matrix (acting on column $(t, x)^{\mathsf T}$)
> $$\Lambda = \begin{pmatrix}\gamma & \gamma v\\ \gamma v & \gamma\end{pmatrix}, \qquad \gamma = (1 - v^2)^{-1/2}.$$
> *Active.* Apply $\Lambda$ to a particle at rest at the spatial origin, worldline event $(t, 0)$:
> $$\begin{pmatrix}\gamma & \gamma v\\ \gamma v & \gamma\end{pmatrix}\begin{pmatrix}t\\ 0\end{pmatrix} = \begin{pmatrix}\gamma t\\ \gamma v t\end{pmatrix}.$$
> The event $(t, 0)$ is moved to $(\gamma t, \gamma v t)$ — a particle now at position $x = \gamma v t = v(\gamma t)$, i.e. *moving at velocity $v$* in the *same* frame. The active boost has physically set the particle into motion at $+v$.
>
> *Passive.* Use the *same* matrix $\Lambda$ to relabel a *fixed* event. The standard passive boost to a frame $\mathcal{O}'$ moving at velocity $V$ relative to $\mathcal{O}$ is $x'^\alpha = \Lambda[-V]^\alpha{}_\beta x^\beta$ with $\Lambda[-V] = \begin{pmatrix}\gamma & \gamma V\\ \gamma V & \gamma\end{pmatrix}$ (Gourgoulhon's eq. 8.14 has $V\to V' = -V$). So the matrix $\Lambda$ above, read passively, transforms coordinates to a frame $\mathcal{O}'$ moving at $V = -v$ relative to $\mathcal{O}$. A fixed event at rest in $\mathcal{O}$ then appears, in $\mathcal{O}'$, to move at $+v$ — consistent, because if $\mathcal{O}'$ recedes at $-v$ then objects at rest in $\mathcal{O}$ advance at $+v$ as seen by $\mathcal{O}'$.
>
> The *same* matrix $\Lambda$ thus serves both: actively it boosts a particle by $+v$; passively it transforms to a frame moving at $-v$. The active boost by $+v$ and the passive boost to a frame at $-v$ are the same matrix — which is exactly the inverse relationship of Step 3 made concrete.

> [!note]- Complete formal solution
> *Passive:* one event $M$, two frames; coordinates related by $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$ — labels change, nothing moves. *Active:* one frame, two events; the map $f$ sends $M$ to $f(M)$ with $\overrightarrow{O f(M)} = \Lambda(\overrightarrow{OM}) + \boldsymbol{v}$, same formula $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$ but now $(x'^\alpha)$ is the new event — something moves. The two are algebraically identical, semantically opposite. The reconciliation is the inverse relationship between basis and components: if $e_\alpha = \Lambda^\beta{}_\alpha e'_\beta$ then a fixed vector's components obey $x'^\beta = \Lambda^\beta{}_\alpha x^\alpha$, so the matrix relating coordinate grids is the inverse of the matrix that actively moves a vector to those components — concretely, a passive change to a frame moving at $v$ equals an active boost by $-v$. In $1+1$ the boost $\Lambda = \big(\begin{smallmatrix}\gamma & \gamma v\\ \gamma v & \gamma\end{smallmatrix}\big)$ actively sends $(t, 0)\mapsto(\gamma t, \gamma v t)$ (particle now at velocity $+v$) and passively transforms to a frame moving at $-v$; the same matrix, opposite reading. $\blacksquare$

---

# Key Takeaways

**Declare active or passive before writing a single matrix — that decision fixes whether you use $\Lambda$ or $\Lambda^{-1}$.** The active and passive transformations share the formula $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$, so the symbols alone do not tell you which you are doing; the meaning is in what is held fixed (the event, passively; the frame, actively). The discipline that prevents the characteristic sign-and-transpose error is to state, before writing the matrix, whether the object moves or the frame does. The trigger to invoke this care: any time a problem mixes "boost the particle" with "transform to the moving frame", stop and label each as active or passive. Almost every relativistic sign error — a boost going the wrong way, a $\gamma v$ with the wrong sign — traces to silently switching viewpoints mid-calculation.

**Basis and components transform inversely: a passive change to a frame moving at $v$ is an active boost by $-v$.** The structural fact behind the active/passive duality is that the matrix relating two *bases* is the inverse of the matrix relating the *components* of a fixed vector — the contravariant transformation law. So moving to a frame that recedes at velocity $v$ (passive) produces the same coordinate change as physically boosting the object by $-v$ (active). This is why the same Lorentz matrix appears in both, with the velocity flipped. The transferable diagnostic: whenever you see two transformations that look identical but are described oppositely (one "change of frame", one "motion of object"), suspect they are active/passive duals related by inversion, and the velocity (or angle, or translation) carries the opposite sign. This duality pervades physics — it is the same as the distinction between transforming a field and transforming the coordinates it is evaluated at.

**The active reading is the group acting on spacetime; the passive reading is the group relating descriptions — and both are the same Poincaré group.** Stepping back, the active transformations are the Poincaré group acting on $\mathscr{E}$ (the genuine isometries that move events), while the passive transformations are the same group recording how two inertial observers' coordinate systems relate. They are two *faces* of the one group $\mathrm{ISO}(1,3)$ — the active action on points and the passive action on charts — and recognising that they are the same group seen from two sides is the conceptual unification of the whole chapter (the "one group, four faces" frame of the topic page's Insights). A symmetry of nature is an active transformation that leaves the physics invariant; the corresponding passive transformation is the statement that two observers related by it describe the same physics. Holding both readings of the Poincaré group in view — and knowing which one a given problem needs — is what makes the group a usable tool rather than a source of confusion.
