---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $O(1,3)$ is the [[Def - The Lorentz Group|Lorentz group]]; $SO^+(1,3)$ its [[Def - Subgroups and Components of the Lorentz Group|restricted (proper orthochronous) subgroup]], $\det\Lambda = +1$ and $\Lambda^0{}_0 \ge 1$. The discrete reflections are $I = -\mathrm{Id}$, $P = \mathrm{diag}(1,-1,-1,-1)$, $T = \mathrm{diag}(-1,1,1,1)$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (Normality of the restricted Lorentz group).** The restricted Lorentz group $SO^+(1,3)$ is a normal subgroup of the full Lorentz group $O(1,3)$: for every $\Lambda \in O(1,3)$ and every $\Lambda_0 \in SO^+(1,3)$,
> $$\Lambda\,\Lambda_0\,\Lambda^{-1} \in SO^+(1,3).$$
> The quotient group is the Klein four-group,
> $$O(1,3)/SO^+(1,3) \;\cong\; \{\mathrm{Id}, I, P, T\} \;\cong\; \mathbb{Z}/2 \times \mathbb{Z}/2,$$
> realised by the coset representatives $\mathrm{Id}, P, T, I = PT$, which are the four connected components of $O(1,3)$.

---

# Motivation

Once $O(1,3)$ is cut into four components, the question is how they fit together as a group. Normality of $SO^+(1,3)$ is the statement that the component structure is *compatible* with the group law — that "which component am I in" is a homomorphism, so that multiplying transformations multiplies their components according to a fixed group law on the four classes. Without normality there would be no quotient group and no clean bookkeeping of components; with it, the four components form a group in their own right, and that group turns out to be the smallest non-cyclic group, the Klein four-group.

The result also identifies $SO^+(1,3)$ as the *canonical* piece of the Lorentz group. A normal subgroup is one that looks the same from every conjugate viewpoint — it is preserved by every inner automorphism — and the identity component of any topological group is always normal for exactly this reason: conjugation is continuous and fixes the identity, so it must map the identity component to itself. The theorem makes this concrete for $O(1,3)$ and computes the resulting quotient, which is the discrete data of parity and time-reversal.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's content is "conjugation preserves the component." The disguised sources are the various ways one encounters the need to track components through a product.

The first disguised source is **"a transformation is conjugated by a reflection."** When one writes $P\Lambda_0 P^{-1}$ or $T\Lambda_0 T^{-1}$ — for instance to ask how a boost looks under parity, or how a process looks time-reversed — the result is again restricted, so the conjugated transformation is still a legitimate proper orthochronous transformation. The bridge is that $P, T \in O(1,3)$ and $\Lambda_0 \in SO^+(1,3)$, so the theorem applies. *Example problem:* show that the parity image $P\,(\text{boost along }x)\,P^{-1}$ of a boost is the boost along $-x$, still a restricted transformation.

The second disguised source is **"a product of transformations from known components."** Whenever you multiply two transformations whose components you know, the component of the product is determined by the group law on $\mathbb{Z}/2\times\mathbb{Z}/2$ — proper times improper is improper, orthochronous times antichronous is antichronous, and so on — precisely because the sign map $\sigma$ is a homomorphism, which is the content of normality. *Example problem:* determine the component of $PT\Lambda_0$ for $\Lambda_0$ restricted, without multiplying matrices, by adding the classes $(1,0) + (0,1) + (0,0) = (1,1)$.

The third disguised source is **"a one-parameter family connects to the identity."** If $\Lambda(t)$ is a continuous path in $O(1,3)$ with $\Lambda(0) = \mathrm{Id}$, then $\Lambda(t) \in SO^+(1,3)$ for all $t$, because the path cannot jump components and starts in the identity component. The bridge is that $SO^+(1,3)$ *is* the identity component, and normality is the abstract reason the identity component is well-behaved under the group structure. *Example problem:* argue that $\exp(t\omega)$ for any $\omega \in \mathfrak{so}(1,3)$ lies in $SO^+(1,3)$ for all $t$.

**Targets (Output Amplification)**

The conclusion is "$SO^+(1,3)$ is normal with Klein-four quotient."

Combine the conclusion with **the splitting $\{\mathrm{Id}, I, P, T\}$**. Since this four-element subgroup maps isomorphically onto the quotient, $O(1,3)$ is the semidirect product $SO^+(1,3) \rtimes (\mathbb{Z}/2\times\mathbb{Z}/2)$. The further result is that every Lorentz transformation factors uniquely as (a restricted transformation) $\times$ (one of the four reflections), reducing all of $O(1,3)$ to its identity component plus a finite choice. The combination is useful because it lets the continuous theory (developed on $SO^+$) be extended to the whole group by hand, reflection by reflection.

Combine the conclusion with **a homomorphism out of $\mathbb{Z}/2\times\mathbb{Z}/2$**. Any assignment of signs to parity and time-reversal — for instance the action of $P$ and $T$ on a field, or their eigenvalues in a representation — factors through the quotient, so it is determined by its values on $P$ and $T$ alone. The further result is the classification of how discrete symmetries act: a representation of $O(1,3)$ restricts to a representation of $SO^+(1,3)$ together with two commuting involutions implementing $P$ and $T$. The combination is nonobvious because it reduces the discrete-symmetry data of a relativistic theory to just two operators.

Combine the conclusion with **the connectedness of $SO^+(1,3)$**. Since the quotient is discrete and the subgroup is connected, the four cosets are exactly the four connected components, so $\pi_0(O(1,3)) \cong \mathbb{Z}/2\times\mathbb{Z}/2$ as a group, not merely as a set. The further result is that the *group* of components equals the Klein four-group, which is what makes "component" a multiplicative invariant. The combination closes the loop between topology ($\pi_0$) and algebra (the quotient group).

---

# Why Is It True

The deep reason is a general fact about topological groups, and it is worth stating in full generality first.

**The identity component of any topological group is a normal subgroup.** Here is the whole argument in one breath: conjugation by a fixed element $g$, the map $x \mapsto gxg^{-1}$, is continuous and sends the identity to the identity, so it maps the connected component of the identity into a connected set containing the identity — which must be the identity component itself. Hence the identity component is preserved by every conjugation, i.e. it is normal. For $O(1,3)$, the identity component is $SO^+(1,3)$ (a fact from the [[Def - Subgroups and Components of the Lorentz Group|component analysis]]), so it is normal. **The mechanism is that conjugation is a continuous automorphism, and a continuous automorphism cannot tear apart a connected piece glued to the identity.**

One can also see it concretely, without topology, through the two sign invariants. The determinant is multiplicative, $\det(\Lambda\Lambda_0\Lambda^{-1}) = \det\Lambda_0 = +1$, so conjugation preserves properness for free. The harder half is the time-component sign. The orthochronous condition is "$\Lambda$ maps future-timelike vectors to future-timelike vectors," and one checks that if $\Lambda_0$ does this then so does $\Lambda\Lambda_0\Lambda^{-1}$ — but with a twist depending on whether $\Lambda$ itself is orthochronous. If $\Lambda$ is orthochronous, take a future vector $u$; then $\Lambda^{-1}u$ is future (since $\Lambda^{-1}$ is orthochronous), $\Lambda_0\Lambda^{-1}u$ is future (since $\Lambda_0$ is), and $\Lambda\Lambda_0\Lambda^{-1}u$ is future — so the conjugate is orthochronous. If $\Lambda$ is antichronous, then $\Lambda^{-1}u$ is *past*, $\Lambda_0\Lambda^{-1}u$ is past (since $\Lambda_0$ maps past to past, being orthochronous), and $\Lambda\Lambda_0\Lambda^{-1}u$ is future (since $\Lambda$ maps past to future) — so the conjugate is *again* orthochronous. Either way the double time-flip cancels, and the conjugate stays in $SO^+(1,3)$.

The quotient being the Klein four-group is then forced. The four components are the four sign pairs, the sign map $\sigma$ is a surjective homomorphism onto $\mathbb{Z}/2\times\mathbb{Z}/2$ with kernel $SO^+(1,3)$, and the first isomorphism theorem hands back the quotient. That the quotient is $\mathbb{Z}/2\times\mathbb{Z}/2$ rather than $\mathbb{Z}/4$ is visible from the reflections: $P^2 = T^2 = \mathrm{Id}$, every nonidentity element has order two, which is the signature of the Klein four-group (the cyclic group $\mathbb{Z}/4$ has an element of order four).

---

# What Makes This Hard

The proper-and-determinant half is trivial; the difficulty is entirely in the time-component sign under conjugation, where most people stop after the case $\Lambda$ orthochronous and forget to check $\Lambda$ antichronous — missing that the two time-flips of an antichronous $\Lambda$ and its inverse cancel, so the conjugate is *still* orthochronous. The second non-obvious point is recognising that the quotient is the Klein four-group and not $\mathbb{Z}/4$: the common error is to assume four components form a cyclic group, when in fact every reflection is an involution, forcing $\mathbb{Z}/2\times\mathbb{Z}/2$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show conjugation preserves both sign invariants. The determinant is immediate by multiplicativity. For the time-component, track a future-timelike vector through $\Lambda^{-1}, \Lambda_0, \Lambda$ in the two cases $\Lambda$ orthochronous and $\Lambda$ antichronous, observing that the time-orientation flips cancel. Then read off the quotient from the sign homomorphism.

**Subgoal decomposition:**

1. **Conjugation preserves $\det = +1$.** Show $\det(\Lambda\Lambda_0\Lambda^{-1}) = \det\Lambda_0$.
   - *Hint:* The determinant is multiplicative and $\det\Lambda\,\det\Lambda^{-1} = 1$.
   - *Why needed:* It disposes of the proper half, leaving only the time-orientation.

2. **Characterise orthochronous by future-vector preservation.** Recall $\Lambda$ is orthochronous iff it maps every future-timelike vector to a future-timelike vector, and antichronous iff it maps them to past-timelike vectors.
   - *Hint:* This is the geometric meaning of $\Lambda^0{}_0 \ge 1$ versus $\le -1$.
   - *Why needed:* It converts the sign condition into a trackable action on vectors.

3. **Track a future vector through the conjugate, both cases.** For a future-timelike $u$, follow $\Lambda^{-1}u \to \Lambda_0\Lambda^{-1}u \to \Lambda\Lambda_0\Lambda^{-1}u$, in the case $\Lambda$ orthochronous (no flips) and $\Lambda$ antichronous (two flips that cancel).
   - *Hint:* $\Lambda^{-1}$ has the same orthochronous/antichronous type as $\Lambda$; $\Lambda_0$ preserves time-orientation.
   - *Why needed:* It shows the conjugate is orthochronous regardless of $\Lambda$'s type — the heart of normality.

4. **Read off the quotient.** Identify the sign map $\sigma$ as a surjective homomorphism onto $\mathbb{Z}/2\times\mathbb{Z}/2$ with kernel $SO^+(1,3)$, and apply the first isomorphism theorem.
   - *Hint:* $P^2 = T^2 = \mathrm{Id}$ and $I = PT$ give the Klein four-group structure.
   - *Why needed:* It delivers the quotient group and the coset representatives.

---

# Lemma Decomposition

> [!note]- Lemma 1: Conjugation preserves the determinant
> **Statement:** For $\Lambda \in O(1,3)$ and $\Lambda_0 \in SO^+(1,3)$, $\det(\Lambda\Lambda_0\Lambda^{-1}) = +1$.
>
> **Hint:** Multiplicativity of the determinant.
>
> **Why needed:** It establishes the proper half of normality, reducing the problem to the time-orientation.
>
> > [!note]- Full proof
> > $\det(\Lambda\Lambda_0\Lambda^{-1}) = \det\Lambda\cdot\det\Lambda_0\cdot\det\Lambda^{-1} = \det\Lambda_0\cdot(\det\Lambda\cdot(\det\Lambda)^{-1}) = \det\Lambda_0 = +1$, since $\Lambda_0$ is proper. $\blacksquare$

> [!note]- Lemma 2: Inverse and original have the same time-orientation type
> **Statement:** If $\Lambda \in O(1,3)$ is orthochronous, so is $\Lambda^{-1}$; if $\Lambda$ is antichronous, so is $\Lambda^{-1}$.
>
> **Hint:** Orthochronous transformations form a subgroup, hence are closed under inverses; the antichronous set is the nonidentity coset.
>
> **Why needed:** It controls the time-orientation of the outer factors $\Lambda$ and $\Lambda^{-1}$ in the conjugate.
>
> > [!note]- Full proof
> > The orthochronous transformations $O^+(1,3)$ form a subgroup of $O(1,3)$ (the condition $\Lambda^0{}_0 \ge 1$ is preserved under products and inverses, as the time-component inequality shows), so $\Lambda$ orthochronous $\Rightarrow$ $\Lambda^{-1}$ orthochronous. If $\Lambda$ is antichronous, then $\Lambda = T'\,\Lambda'$ for some orthochronous $\Lambda'$ and a fixed antichronous representative $T'$ (e.g. $T$); then $\Lambda^{-1} = \Lambda'^{-1}T'^{-1}$, a product of an orthochronous and an antichronous transformation, hence antichronous. Geometrically: orthochronous maps future-timelike vectors to future-timelike, antichronous maps them to past-timelike, and inverting reverses the roles but not the type. $\blacksquare$

> [!note]- Lemma 3: The conjugate of an orthochronous transformation is orthochronous
> **Statement:** For $\Lambda \in O(1,3)$ and $\Lambda_0 \in O^+(1,3)$, the conjugate $\Lambda\Lambda_0\Lambda^{-1}$ is orthochronous.
>
> **Hint:** Track a future-timelike vector; count time-orientation flips in the two cases for $\Lambda$.
>
> **Why needed:** Combined with Lemma 1 it gives normality.
>
> > [!note]- Full proof
> > Let $u$ be future-timelike. Apply the three factors in turn.
> >
> > *Case $\Lambda$ orthochronous.* By Lemma 2, $\Lambda^{-1}$ is orthochronous, so $\Lambda^{-1}u$ is future-timelike. $\Lambda_0$ is orthochronous, so $\Lambda_0\Lambda^{-1}u$ is future-timelike. $\Lambda$ is orthochronous, so $\Lambda\Lambda_0\Lambda^{-1}u$ is future-timelike. Hence the conjugate maps future to future: orthochronous.
> >
> > *Case $\Lambda$ antichronous.* By Lemma 2, $\Lambda^{-1}$ is antichronous, so $\Lambda^{-1}u$ is *past*-timelike. $\Lambda_0$ is orthochronous, hence maps past-timelike to past-timelike, so $\Lambda_0\Lambda^{-1}u$ is past-timelike. $\Lambda$ is antichronous, hence maps past-timelike to future-timelike, so $\Lambda\Lambda_0\Lambda^{-1}u$ is future-timelike. The two flips cancel; the conjugate is orthochronous.
> >
> > In both cases $\Lambda\Lambda_0\Lambda^{-1}$ maps every future-timelike vector to a future-timelike vector, so it is orthochronous. $\blacksquare$

> [!note]- Lemma 4: The quotient is the Klein four-group
> **Statement:** The map $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$, $\Lambda \mapsto (\tfrac{1-\det\Lambda}{2}, \tfrac{1-\mathrm{sgn}\Lambda^0{}_0}{2})$, is a surjective homomorphism with kernel $SO^+(1,3)$.
>
> **Hint:** Both components are homomorphisms; $I, P, T$ hit the three nonzero classes.
>
> **Why needed:** It identifies the quotient via the first isomorphism theorem.
>
> > [!note]- Full proof
> > The determinant component $\Lambda \mapsto \tfrac{1-\det\Lambda}{2}$ is a homomorphism to $\mathbb{Z}/2$ because $\det$ is multiplicative and valued in $\{\pm 1\}$. The time-component $\Lambda \mapsto \tfrac{1-\mathrm{sgn}\Lambda^0{}_0}{2}$ is a homomorphism to $\mathbb{Z}/2$ because the orthochronous transformations form an index-two subgroup (the product of two antichronous transformations is orthochronous, as in Lemma 2). The pair $\sigma$ is therefore a homomorphism to $\mathbb{Z}/2\times\mathbb{Z}/2$. Its kernel is $\{\det = +1, \Lambda^0{}_0 \ge 1\} = SO^+(1,3)$. It is surjective: $\sigma(\mathrm{Id}) = (0,0)$, $\sigma(P) = (1,0)$, $\sigma(T) = (0,1)$, $\sigma(I) = \sigma(PT) = (1,1)$. By the first isomorphism theorem, $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$, with $P^2 = T^2 = \mathrm{Id}$ confirming every nonidentity class has order two. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Lambda \in O(1,3)$ and $\Lambda_0 \in SO^+(1,3)$. We show $\Lambda\Lambda_0\Lambda^{-1} \in SO^+(1,3)$.
>
> By Lemma 1, $\det(\Lambda\Lambda_0\Lambda^{-1}) = \det\Lambda_0 = +1$, so the conjugate is proper.
>
> By Lemma 3, the conjugate is orthochronous: tracking a future-timelike vector $u$ through $\Lambda^{-1}, \Lambda_0, \Lambda$ gives a future-timelike result whether $\Lambda$ is orthochronous (no time-flips) or antichronous (two cancelling flips), using Lemma 2 to fix the type of $\Lambda^{-1}$.
>
> Therefore $\Lambda\Lambda_0\Lambda^{-1}$ has $\det = +1$ and $\Lambda^0{}_0 \ge 1$, i.e. $\Lambda\Lambda_0\Lambda^{-1} \in SO^+(1,3)$. Since this holds for all $\Lambda \in O(1,3)$ and $\Lambda_0 \in SO^+(1,3)$, the restricted group is normal.
>
> For the quotient, Lemma 4 exhibits the surjective homomorphism $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$ with kernel $SO^+(1,3)$, so by the first isomorphism theorem $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$, with coset representatives $\mathrm{Id}, P, T, I = PT$, the four connected components. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The orthogonal group $O(n)$ and orientation.** The same argument shows $SO(n)$ is normal in $O(n)$ with quotient $\mathbb{Z}/2$ (the determinant alone), and more generally that the identity component of any matrix group is normal. The application is to see the Lorentz case as one instance of a universal phenomenon: the connected component of the identity is always a normal subgroup, and the component group $\pi_0$ is always the quotient. It is nonobvious that the *topological* notion (identity component) and the *algebraic* notion (normal subgroup) coincide so cleanly.

**Crystallographic point groups.** In crystallography, the point group of a crystal is a finite subgroup of $O(3)$, and the question of which point groups contain the inversion $-\mathrm{Id}$ (the centrosymmetric ones) is exactly a question about cosets of $SO(3)$. The Klein-four structure of $\{\mathrm{Id}, I, P, T\}$ reappears, restricted to space, as the structure governing how a centrosymmetric crystal's symmetries split into proper rotations and improper rotoinversions. The application is surprising because it imports the discrete-symmetry bookkeeping of relativity into solid-state physics.

**Galois theory and field extensions.** The quotient $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$ is structurally identical to the Galois group of a biquadratic extension $\mathbb{Q}(\sqrt{a},\sqrt{b})/\mathbb{Q}$, where the two $\mathbb{Z}/2$ factors swap $\sqrt{a} \leftrightarrow -\sqrt{a}$ and $\sqrt{b} \leftrightarrow -\sqrt{b}$ independently. The two reflections $P, T$ play the role of the two square-root sign-changes. The application battle-tests the Klein-four structure by recognising it in pure algebra, far from any geometry of spacetime.

---

# Bridges

- **[[Def - Subgroups and Components of the Lorentz Group]]** — this theorem is the group-theoretic completion of the component definition: the four components defined there are shown here to form a group under the induced multiplication, with $SO^+(1,3)$ the identity element (the kernel) and $\{P, T, I\}$ the three involutions. The definition supplies the components as sets; the theorem supplies the group structure on them.

- **The identity component of a Lie group** — the result is the special case, for $O(1,3)$, of the general theorem that the connected component of the identity in any [[Def - Lie Group|Lie group]] $G$ is a normal subgroup $G_0$, with $G/G_0 = \pi_0(G)$ the group of components. The proof here (track a future vector) is the concrete shadow of the abstract proof (conjugation is a continuous automorphism fixing the identity, hence preserves the identity component). For $O(1,3)$, $\pi_0 = \mathbb{Z}/2\times\mathbb{Z}/2$; for $O(n)$, $\pi_0 = \mathbb{Z}/2$.

- **The semidirect product structure** — combined with the splitting $\{\mathrm{Id}, I, P, T\}$, normality gives $O(1,3) = SO^+(1,3) \rtimes (\mathbb{Z}/2\times\mathbb{Z}/2)$, the same structure by which the full [[Def - The Poincaré Group|Poincaré group]] is built as Lorentz transformations semidirect-producted with translations. The pattern "normal subgroup $\rtimes$ quotient" recurs throughout: it is how a group is reconstructed from a normal piece and a complementary piece, and it is the algebraic skeleton of both the component structure here and the inhomogeneous extension of the Lorentz group to the Poincaré group.

---

# Unlocked by This

> [!tip] The CPT Theorem *(from quantum field theory)*
> Normality of $SO^+(1,3)$ and the identification of the quotient with $\{\mathrm{Id}, P, T, PT\}$ is the classical setting for the deepest discrete symmetry of relativistic physics: the **CPT theorem**, which states that any local, Lorentz-invariant quantum field theory with a Hermitian Hamiltonian is invariant under the combined operation of charge conjugation $C$, parity $P$, and time reversal $T$, even when the individual operations are violated. The theorem rests on the fact that $PT$ (the total inversion $I$, up to the proper-orthochronous part) is connected to the identity in the *complexified* Lorentz group $SO(4,\mathbb{C})$, so the analytic continuation of a Lorentz-invariant theory forces $CPT$ invariance. The four-component structure of $O(1,3)$ established here is the classical skeleton, and the CPT theorem is the statement that the diagonal $\mathbb{Z}/2$ generated by $CPT$ is always unbroken.
