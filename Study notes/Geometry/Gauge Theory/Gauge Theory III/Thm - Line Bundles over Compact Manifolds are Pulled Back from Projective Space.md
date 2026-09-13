---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Classifying Bundle and Classifying Map"
  - "Def - The Hopf Bundle"
  - "Thm - Vector Bundles are Associated to Their Frame Bundles"
  - "Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Thm - Existence of Smooth Partitions of Unity"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a **compact** smooth manifold (smooth, Hausdorff, second countable, $C^\infty$), and $\mathbb{K}$ is either the field $\mathbb{C}$ of complex numbers or the skew-field $\mathbb{H}$ of quaternions. A **complex line bundle** $L \to M$ is a [[Def - Vector Bundle|vector bundle]] whose fibres $L_m$ are one-dimensional complex vector spaces; a **quaternionic line bundle** is a rank-one right $\mathbb{H}$-module bundle, and we write $\Gamma(L)$ for its space of smooth [[Def - Vector Bundle|sections]]. We write $\underline{V} := M \times V$ for the trivial bundle with fibre a fixed vector space $V$, and $\underline{\mathbb{C}}$ for the trivial complex line bundle $M \times \mathbb{C}$.

Complex projective space $\mathbb{CP}^N$ is the space of complex lines through the origin in $\mathbb{C}^{N+1}$, that is $\mathbb{CP}^N = (\mathbb{C}^{N+1} \setminus \{0\})/\mathbb{C}^\times$ with $[z_0 : \dots : z_N]$ the line spanned by $(z_0, \dots, z_N)$; see [[Def - Complex Projective Space as a Quotient]]. Its **tautological line bundle** is
$$\mathcal{O}(-1) := \{\, (\ell, v) : \ell \in \mathbb{CP}^N,\ v \in \ell \,\} \subset \mathbb{CP}^N \times \mathbb{C}^{N+1}, \qquad \mathcal{O}(-1)_\ell = \ell,$$
the sub-bundle of $\underline{\mathbb{C}^{N+1}}$ whose fibre over a line $\ell$ is that very line, a one-dimensional complex vector space. The quaternionic projective space $\mathbb{HP}^N$ is the space of **right** quaternionic lines $\{v \cdot q : q \in \mathbb{H}\}$ in $\mathbb{H}^{N+1}$, with tautological line bundle $\mathcal{O}_{\mathbb{H}}(-1) \subset \mathbb{HP}^N \times \mathbb{H}^{N+1}$ defined the same way.

For a smooth map $f \colon M \to \mathbb{CP}^N$, the pull-back bundle $f^*\mathcal{O}(-1)$ is the vector bundle over $M$ with fibre $(f^*\mathcal{O}(-1))_m = \mathcal{O}(-1)_{f(m)} = f(m)$ (the pull-back of a bundle is a bundle by [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]] and [[Def - Operations on Vector Bundles and Pull-Back Bundles|the pull-back operation on vector bundles]]). A **principal $U(1)$-bundle** is a [[Def - Principal G-Bundle|principal bundle]] for the circle group $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$; a principal $Sp(1)$-bundle is one for the group $Sp(1) = \{q \in \mathbb{H} : \bar{q}q = 1\}$ of unit quaternions, which [[Ex - SU(2) is the Group of Unit Quaternions|is isomorphic to $SU(2)$]]. We equip every complex vector bundle with a [[Def - Complex Vector Bundle and Hermitian Structure|Hermitian metric]] $\langle \cdot, \cdot \rangle$, taken **linear in the first argument and conjugate-linear in the second**, so that $v \mapsto \langle v, w \rangle$ is $\mathbb{C}$-linear for each fixed $w$.

The Hopf bundle $S^{2N+1} \to \mathbb{CP}^N$ of [[Def - The Hopf Bundle]] is the principal $U(1)$-bundle whose [[Def - Associated Bundle|associated line bundle]] with respect to the standard representation is exactly the tautological bundle, $S^{2N+1} \times_{U(1)} \mathbb{C} \cong \mathcal{O}(-1)$; this identification is proved on [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]]. Isomorphism of bundles is written $\cong$, homotopy of maps $\simeq$; a map that is **fibrewise injective** and $\mathbb{K}$-linear on each fibre is called a **bundle monomorphism**.

The standing set $[M ; \mathbb{CP}^\infty]$ is defined on [[Def - Classifying Bundle and Classifying Map]] as the direct limit $\varinjlim_N [M ; \mathbb{CP}^N]$ over the standard inclusions $\mathbb{CP}^N \hookrightarrow \mathbb{CP}^{N+1}$, $[z_0 : \dots : z_N] \mapsto [z_0 : \dots : z_N : 0]$; concretely, two maps $f \colon M \to \mathbb{CP}^N$ and $f' \colon M \to \mathbb{CP}^{N'}$ represent the same element of $[M ; \mathbb{CP}^\infty]$ if and only if their images under some pair of standard inclusions into a common $\mathbb{CP}^{N''}$ are homotopic there.

> [!warning] Convention: scope of the theorem
> Haydys states the classification (his Theorem 70) for **every** compact Lie group $G$: for a general classifying bundle $E \to B = E/G$, the assignment $f \mapsto f^*E$ is a bijection from isomorphism classes of principal $G$-bundles over $M$ onto $[M ; B]$. That statement rests on the existence of a classifying space for every compact $G$ (Milnor's join construction) and on cellular approximation, neither of which this series proves. **This series proves the theorem only for $G = U(1)$ (with $B = \mathbb{CP}^\infty$, tautological bundle $\mathcal{O}(-1)$) and $G = Sp(1)$ (with $B = \mathbb{HP}^\infty$).** The identical argument, run with $U(n)$ in place of $U(1)$ and the infinite Grassmannian $\operatorname{Gr}_n(\mathbb{C}^\infty)$ in place of $\mathbb{CP}^\infty$, classifies rank-$n$ complex bundles; we record this only as a remark and use nothing beyond the line-bundle case here.

---

# Statement

> **Theorem (line bundles are pulled back from projective space).** Let $M$ be a compact manifold.
>
> **(a) Existence of a classifying map.** For every complex line bundle $L \to M$ there is a natural number $N$ and a smooth map $f \colon M \to \mathbb{CP}^N$ with
> $$f^*\mathcal{O}(-1) \cong L.$$
> Equivalently, every principal $U(1)$-bundle $P \to M$ is isomorphic to the pull-back $f^*\big(S^{2N+1} \to \mathbb{CP}^N\big)$ of the Hopf bundle for some smooth $f \colon M \to \mathbb{CP}^N$.
>
> **(b) Uniqueness up to homotopy, and the bijection.** Two maps $f \colon M \to \mathbb{CP}^N$ and $f' \colon M \to \mathbb{CP}^{N'}$ satisfy $f^*\mathcal{O}(-1) \cong f'^*\mathcal{O}(-1)$ **if and only if** their images under the standard inclusions $\mathbb{CP}^N \hookrightarrow \mathbb{CP}^{N+N'+1}$ and $\mathbb{CP}^{N'} \hookrightarrow \mathbb{CP}^{N+N'+1}$ are homotopic in $\mathbb{CP}^{N+N'+1}$. Consequently the assignment
> $$P \longmapsto [f_P], \qquad f_P \text{ any classifying map of } P,$$
> is a well-defined bijection from the set of isomorphism classes of principal $U(1)$-bundles (equivalently, complex line bundles) over $M$ onto the set $[M ; \mathbb{CP}^\infty]$.
>
> **(c) The quaternionic case.** The same two statements hold for principal $Sp(1)$-bundles over $M$, equivalently for quaternionic line bundles, with $\mathbb{CP}^N$, $\mathbb{CP}^\infty$ and $\mathcal{O}(-1)$ replaced throughout by $\mathbb{HP}^N$, $\mathbb{HP}^\infty$ and the quaternionic tautological bundle $\mathcal{O}_{\mathbb{H}}(-1)$; the associated Hopf bundle is $S^{4N+3} \to \mathbb{HP}^N$, with $Sp(1)$ acting by right multiplication.

---

# Motivation

The classification of line bundles is the question with which gauge theory over a fixed base begins: over a given manifold $M$, *how many* complex line bundles are there, up to isomorphism, and what invariant tells two of them apart? A complex line bundle is the geometric home of a $U(1)$-gauge field — a Maxwell field, in physical language — and the isomorphism class of the bundle is the topological sector in which the field lives. Counting the sectors is therefore the first structural fact one wants.

The naive approach — write down transition functions $g_{\alpha\beta} \colon U_{\alpha\beta} \to U(1)$ and classify them up to the coboundary relation — is correct but unwieldy: it depends on the chosen cover and produces a Čech cohomology set that one still has to compute. The theorem here replaces that local bookkeeping with a single global object. It says that **every** line bundle, no matter how it was built, is the pull-back of **one** universal bundle, the tautological bundle $\mathcal{O}(-1)$ over projective space, along a map $f \colon M \to \mathbb{CP}^N$ that the bundle itself determines up to homotopy. The entire classification problem collapses to a homotopy problem: two bundles are isomorphic precisely when their classifying maps are homotopic. All of the geometry of $M$ that could distinguish line bundles has been concentrated into the homotopy set $[M ; \mathbb{CP}^\infty]$.

The reason projective space is universal is worth stating before the proof, because it is the whole idea. A line bundle is, fibre by fibre, a choice of one-dimensional subspace; and $\mathbb{CP}^N$ is by definition the space of all one-dimensional subspaces of $\mathbb{C}^{N+1}$, carrying over each such subspace the subspace itself as the fibre of $\mathcal{O}(-1)$. So if we can only find enough functions on $M$ to embed each fibre $L_m$ faithfully into a fixed $\mathbb{C}^{N+1}$, the assignment $m \mapsto (\text{the image line } L_m \subset \mathbb{C}^{N+1})$ is a map $M \to \mathbb{CP}^N$ that reproduces $L$ as the pull-back of the tautological bundle. Projective space is the receptacle in which "a varying line" becomes "a map to the space of lines". The compactness of $M$ is what makes the fixed $\mathbb{C}^{N+1}$ finite-dimensional; without it one lands in $\mathbb{C}^\infty$ and $\mathbb{CP}^\infty$ directly.

We assume the reader knows vector bundles and their pull-backs, principal $U(1)$-bundles and their associated line bundles, the existence of Hermitian metrics by partition of unity, and the homotopy invariance of pull-back bundles. Everything else is built here.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis is only "a complex line bundle over a compact manifold". The interesting question is which apparently unrelated data secretly present a line bundle over a compact base to which the theorem then applies.

The first disguised source is **a nowhere-vanishing complex-valued observable on a compact space, twisted by phase ambiguity**. Whenever a physical or geometric problem produces, over each point of a compact $M$, a one-complex-dimensional space of states defined only up to an overall phase — the ground-state ray of a Hamiltonian $H(m)$ with a simple lowest eigenvalue, say — that family of rays is a complex line bundle $L \to M$ (the property $B$ is "a continuously varying simple eigenline"; the bridge $B \Rightarrow A$ is that a simple eigenvalue's eigenspace is a genuine one-dimensional sub-bundle, by the spectral-projection formula $P(m) = \tfrac{1}{2\pi i}\oint (z - H(m))^{-1}\,dz$, which is smooth in $m$). The theorem then says the Berry phase sector of the family is a homotopy class $[f] \in [M ; \mathbb{CP}^\infty]$. *Example problem:* show that the family of ground states of a two-level system parametrised by $S^2$ is a non-trivial line bundle by computing that its classifying map $S^2 \to \mathbb{CP}^1$ has non-zero degree.

The second disguised source is **a divisor or a holomorphic section with prescribed zeros on a compact complex manifold**. A meromorphic function or, more generally, a divisor $D$ on a compact Riemann surface determines a holomorphic line bundle $\mathcal{O}(D)$ (the bridge $B \Rightarrow A$ builds the transition functions from the local defining equations of $D$). The theorem places $\mathcal{O}(D)$ in $[M ; \mathbb{CP}^\infty]$, and over a surface this homotopy set is a single integer — recovering the classical fact that a divisor on a surface is measured up to linear equivalence by its degree. *Example problem:* given a degree-$d$ divisor on the torus $T^2$, exhibit a classifying map $T^2 \to \mathbb{CP}^1$ realising the corresponding integer.

The third disguised source is **any principal $U(1)$-bundle presented by a connection or a curvature two-form**, rather than by its topology. In gauge theory one is usually handed a connection $A$ with curvature $F_A$, not a bundle abstractly; the underlying bundle is still a principal $U(1)$-bundle over the (compact) base, so the theorem applies and provides its classifying map. The bridge $B \Rightarrow A$ is that a connection lives on a bundle, and the [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|Hermitian-structure]] reduction turns the $U(1)$-bundle into its associated line bundle. *Example problem:* given a magnetic monopole field on $S^2$ with total flux $2\pi n$, identify the homotopy class of the classifying map with $n$.

**Targets (Output Amplification).** The bare conclusion is an isomorphism $f^*\mathcal{O}(-1) \cong L$ and a bijection onto a homotopy set. Combined with further ingredients it produces the standard invariants.

Combine the conclusion with **a chosen generator of $H^2_{dR}(\mathbb{CP}^N)$**. Pulling that generator back along the classifying map produces a de Rham class $c_1^{\mathrm{top}}(L) := -f^*[\omega_N] \in H^2_{dR}(M)$ that depends only on the isomorphism class of $L$ (extra ingredient: the homotopy invariance of de Rham cohomology). This is the definition of the topological first Chern class on [[Def - First Chern Class via the Classifying Map]], and the whole apparatus of characteristic classes descends from it; the payoff is a *computable* invariant living in ordinary cohomology rather than in an abstract homotopy set.

Combine the conclusion with **the group structure on line bundles under tensor product**. The bijection of part (b) is then upgraded to a group isomorphism onto a cohomology group, giving the [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|classification of $U(1)$-bundles by the first Chern class]]; over a closed oriented surface the extra ingredient is the clutching construction, and the payoff is that a line bundle over a surface is classified completely by a single integer, its degree.

Combine the quaternionic conclusion with **generic-section transversality over a four-manifold**. Part (c) reduces $Sp(1)$-bundles over a $4$-manifold to homotopy classes of clutching maps $S^3 \to Sp(1)$, and combined with the degree theorem this yields the integer instanton number of the [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|classification of $SU(2)$-bundles]]. The payoff is the topological label $k(P) \in \mathbb{Z}$ that indexes the moduli spaces of Yang–Mills instantons.

---

# Why Is It True

Set the formal proof aside and watch what a line bundle does. Over each point $m$ the bundle offers a one-dimensional complex vector space $L_m$. If we could name coordinates on $L_m$ — that is, place $L_m$ faithfully inside a *fixed* vector space $\mathbb{C}^{N+1}$, the same space for every $m$ — then the point $m$ would be labelled by the line $L_m \subset \mathbb{C}^{N+1}$, which is a point of $\mathbb{CP}^N$. The labelling $m \mapsto (\text{line } L_m)$ is the classifying map, and by construction the line it names *is* the fibre of $L$; so pulling back the tautological bundle, whose fibre over a line is that line, returns $L$.

The one thing needed is the faithful placement of every fibre into a common $\mathbb{C}^{N+1}$. This is exactly what finitely many spanning sections provide. Sections $s_0, \dots, s_N$ of $L$ that never simultaneously vanish give, at each $m$, the coordinates $v \mapsto (\langle v, s_0(m) \rangle, \dots, \langle v, s_N(m) \rangle)$ of a vector $v \in L_m$; because some $s_i(m) \neq 0$, these coordinates do not all vanish on a non-zero $v$, so the placement is injective. Compactness is what lets finitely many sections suffice: cover $M$ by trivialising patches, on each of which a local non-vanishing section exists, take a finite subcover, and glue with a partition of unity.

> **The mechanism in one sentence:** a line bundle is a rule assigning a line to each point, projective space is the space of all lines, and finitely many nowhere-simultaneously-vanishing sections turn the rule into a map into that space whose pull-back of the universal line is the bundle itself.

Uniqueness up to homotopy runs on the complementary-subspace idea. Two classifying maps $f, f'$ of the same bundle $L$ come from two faithful placements $L \hookrightarrow \mathbb{C}^{N+1}$ and $L \hookrightarrow \mathbb{C}^{N'+1}$. Put the two target spaces side by side as complementary summands of $\mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1}$ and slide linearly from the first placement to the second: at any intermediate time the vector $((1-t)\,\text{first}, t\,\text{second})$ can vanish only if both halves vanish, and each half is a faithful placement, so the slide never kills a non-zero vector. It stays a faithful placement throughout, hence a homotopy of maps into the projective space of the doubled vector space. The reason the receiving space must be enlarged to $\mathbb{CP}^{N+N'+1}$ is precisely to have room for the two images to sit in complementary directions.

---

# What Makes This Hard

The subtle step is not the existence of the classifying map but the linear homotopy in part (b): the naive straight line between two maps into the *same* $\mathbb{CP}^N$ need not stay fibrewise injective — two placements into one $\mathbb{C}^{N+1}$ can cancel at an intermediate time — and the standard error is to omit the enlargement of the target and claim a homotopy that secretly passes through the zero vector. The enlargement to $\mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1}$ (equivalently, the "even/odd coordinate trick") is exactly the device that keeps the two images in complementary subspaces so that the straight line cannot cancel; recognising that this is forced, not decorative, is the crux. The second trap is quaternionic: because $\mathbb{H}$ is non-commutative one must check that every linearity used in the complex proof survives, and it does only because the homotopy parameters $(1-t)$ and $t$ are *real* scalars, which commute with right quaternionic multiplication.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a bundle monomorphism $L \hookrightarrow \underline{\mathbb{C}^{N+1}}$ from finitely many spanning sections and read off a classifying map from it; this proves existence. For uniqueness, turn any two classifying maps of the same bundle back into two monomorphisms, place their targets in complementary summands of a doubled space, and connect them by the straight-line homotopy, which stays fibrewise injective. Finally assemble well-definedness, surjectivity and injectivity of $P \mapsto [f_P]$ over the direct-limit set. The quaternionic case is the same argument with every linearity re-checked against non-commutativity.

**Subgoal decomposition:**

1. **Spanning sections exist.** Produce finitely many sections $s_0, \dots, s_N$ of $L$ with $\{s_i(m)\}$ spanning $L_m$ for every $m$.
   - *Hint:* Local non-vanishing sections on trivialising opens, a finite subcover by compactness, and a partition of unity to glue and extend by zero.
   - *Why needed:* They are the coordinates that place each fibre faithfully into $\mathbb{C}^{N+1}$; without them there is no map to projective space.

2. **A bundle monomorphism yields a classifying map, and conversely.** From a fibrewise-injective linear $\Phi \colon L \to \underline{\mathbb{C}^{N+1}}$ define $f(m) = \Phi(L_m)$ and show $f^*\mathcal{O}(-1) \cong L$; from a map $f$ recover the tautological monomorphism.
   - *Hint:* The fibre of $f^*\mathcal{O}(-1)$ over $m$ is the line $f(m) = \Phi(L_m)$, and $\Phi$ restricts to an isomorphism $L_m \to \Phi(L_m)$.
   - *Why needed:* It is the two-way dictionary between the bundle picture and the map picture, used in both parts.

3. **Existence (part a).** Combine subgoals 1 and 2 to obtain $f$ with $f^*\mathcal{O}(-1) \cong L$; translate to the Hopf-bundle formulation.
   - *Hint:* The Hermitian Gauss map $\Phi(v) = (\langle v, s_i(m) \rangle)_i$ is fibrewise injective because the $s_i$ span.
   - *Why needed:* It is statement (a).

4. **The easy direction of (b).** Homotopic (in $\mathbb{CP}^{N+N'+1}$) classifying maps give isomorphic bundles.
   - *Hint:* Standard inclusions pull the tautological bundle back to the tautological bundle; then invoke homotopy invariance of pull-back bundles.
   - *Why needed:* It is the "if" of the equivalence in (b).

5. **The hard direction of (b).** Isomorphic bundles give homotopic classifying maps in $\mathbb{CP}^{N+N'+1}$.
   - *Hint:* Two monomorphisms of the same $L$ into $\mathbb{C}^{N+1}$ and $\mathbb{C}^{N'+1}$; put them in complementary summands of $\mathbb{C}^{N+N'+2}$ and take the straight line.
   - *Why needed:* It is the "only if" of the equivalence in (b).

6. **The bijection.** From subgoals 3–5, show $P \mapsto [f_P]$ is well-defined, surjective, and injective onto $[M ; \mathbb{CP}^\infty]$.
   - *Hint:* Well-definedness and injectivity are subgoal 5; surjectivity is subgoal 3 applied to the pull-back of the Hopf bundle by any representative.
   - *Why needed:* It is the concluding sentence of (b).

7. **Quaternionic case (c).** Re-run subgoals 1–6 over $\mathbb{H}$, checking that every linearity used holds for right $\mathbb{H}$-modules.
   - *Hint:* Real homotopy parameters commute with right multiplication; a quaternionic Hermitian metric exists by partition of unity.
   - *Why needed:* It is statement (c).

---

# Lemma Decomposition

> [!note]- Lemma 1: A line bundle over a compact manifold has finitely many nowhere-simultaneously-vanishing sections
> **Statement:** Let $L \to M$ be a complex line bundle over a compact manifold. Then there are finitely many sections $s_0, \dots, s_N \in \Gamma(L)$ such that for every $m \in M$ the set $\{s_0(m), \dots, s_N(m)\}$ contains a non-zero vector; since $L_m$ is one-dimensional, that vector spans $L_m$.
>
> **Hint:** On each trivialising open set there is a nowhere-vanishing local section (the image of the constant section $1$); pass to a finite subcover by compactness and multiply by a subordinate partition of unity.
>
> **Why needed:** These sections are the coordinate functions that embed every fibre faithfully into a fixed $\mathbb{C}^{N+1}$; they are the raw material of the classifying map.
>
> > [!note]- Full proof
> > **Set-up.** Since $L$ is a vector bundle, every point of $M$ has an open neighbourhood $U$ over which $L$ is trivial, with a trivialisation $\psi_U \colon L|_U \to U \times \mathbb{C}$. Define the local section $e_U \in \Gamma(L|_U)$ by $e_U(m) := \psi_U^{-1}(m, 1)$; it is smooth and nowhere zero on $U$, because $\psi_U$ is a fibrewise isomorphism and $1 \neq 0$.
> >
> > **Finite subcover.** The collection of all such trivialising open sets covers $M$. Because $M$ is compact, finitely many of them, $U_0, \dots, U_N$, already cover $M$, with local non-vanishing sections $e_0, \dots, e_N$ on them.
> >
> > **Partition of unity.** By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]] — for any open cover of a smooth manifold there are smooth functions $\varphi_i \geq 0$ with $\operatorname{supp}\varphi_i \subset U_i$, locally finite supports, and $\sum_i \varphi_i \equiv 1$ — choose $\{\varphi_i\}_{i=0}^N$ subordinate to $\{U_i\}$. Define
> > $$s_i(m) := \begin{cases} \varphi_i(m)\, e_i(m), & m \in U_i, \\ 0, & m \notin \operatorname{supp}\varphi_i, \end{cases}$$
> > which is a well-defined smooth global section of $L$: the two clauses agree on the overlap $U_i \setminus \operatorname{supp}\varphi_i$, where both are zero (since $\varphi_i = 0$ there), and $\operatorname{supp}\varphi_i$ is closed in $U_i$ so the extension by zero is smooth.
> >
> > **Spanning.** Fix $m \in M$. Since $\sum_i \varphi_i(m) = 1 > 0$, some index $j$ has $\varphi_j(m) > 0$; then $s_j(m) = \varphi_j(m)\, e_j(m) \neq 0$ because $e_j(m) \neq 0$ and $\varphi_j(m) \neq 0$. As $L_m$ is one-dimensional, the single non-zero vector $s_j(m)$ spans $L_m$. Therefore $\{s_0(m), \dots, s_N(m)\}$ spans $L_m$ for every $m$. $\blacksquare$

> [!note]- Lemma 2: Bundle monomorphisms into a trivial bundle are the same data as maps to projective space
> **Statement:** Let $L \to M$ be a complex line bundle.
> (i) If $\Phi \colon L \to \underline{\mathbb{C}^{N+1}}$ is a bundle monomorphism (fibrewise $\mathbb{C}$-linear and injective on each fibre), then $f_\Phi(m) := \Phi(L_m) \subset \mathbb{C}^{N+1}$ is a well-defined complex line, the map $f_\Phi \colon M \to \mathbb{CP}^N$ is smooth, and $\Phi$ restricts to an isomorphism of vector bundles $L \xrightarrow{\ \cong\ } f_\Phi^*\mathcal{O}(-1)$.
> (ii) Conversely, if $f \colon M \to \mathbb{CP}^N$ is smooth, then the tautological inclusion $\jmath \colon f^*\mathcal{O}(-1) \hookrightarrow \underline{\mathbb{C}^{N+1}}$, $(m, v) \mapsto (m, v)$ where $v \in f(m) \subset \mathbb{C}^{N+1}$, is a bundle monomorphism with $f_{\jmath} = f$.
>
> **Hint:** The fibre of $f^*\mathcal{O}(-1)$ over $m$ is by definition the line $f(m)$; matching it with $\Phi(L_m)$ is what makes $\Phi$ an isomorphism onto the pull-back. Read smoothness off a local non-vanishing section.
>
> **Why needed:** It converts "find a classifying map" into "find a bundle monomorphism", which Lemma 1 supplies, and lets part (b) turn abstract isomorphisms of bundles back into monomorphisms to be homotoped.
>
> > [!note]- Full proof
> > **(i) $f_\Phi$ is well-defined and smooth.** Fix $m$. Because $\Phi$ is injective and $\mathbb{C}$-linear on the one-dimensional fibre $L_m$, the image $\Phi(L_m)$ is a one-dimensional linear subspace of $\mathbb{C}^{N+1}$, that is, a point of $\mathbb{CP}^N$; so $f_\Phi(m) := \Phi(L_m)$ is well-defined. For smoothness, work near a fixed $m_0$. By Lemma 1 or directly by local triviality, choose a smooth nowhere-vanishing local section $e$ of $L$ on a neighbourhood $U$ of $m_0$. Then $\Phi(e(m)) \in \mathbb{C}^{N+1} \setminus \{0\}$ for $m \in U$ (injectivity applied to $e(m) \neq 0$), and $f_\Phi(m) = [\Phi(e(m))]$, the projective class. The map $m \mapsto \Phi(e(m))$ is smooth into $\mathbb{C}^{N+1} \setminus \{0\}$ (composition of the smooth section $e$ with the smooth bundle map $\Phi$), and the quotient projection $\mathbb{C}^{N+1} \setminus \{0\} \to \mathbb{CP}^N$ is smooth (by [[Def - Complex Projective Space as a Quotient|the construction of $\mathbb{CP}^N$ as a smooth quotient]]); hence $f_\Phi$ is smooth on $U$, and $m_0$ was arbitrary.
> >
> > **(i) $\Phi$ is an isomorphism onto $f_\Phi^*\mathcal{O}(-1)$.** By definition $(f_\Phi^*\mathcal{O}(-1))_m = \mathcal{O}(-1)_{f_\Phi(m)} = f_\Phi(m) = \Phi(L_m)$, a subspace of $\mathbb{C}^{N+1}$. Define $\bar\Phi \colon L \to f_\Phi^*\mathcal{O}(-1)$ over $M$ by $\bar\Phi(v) := \Phi(v)$ for $v \in L_m$; this lands in $\Phi(L_m) = (f_\Phi^*\mathcal{O}(-1))_m$ and is $\mathbb{C}$-linear. On the fibre $L_m$ it is injective (as $\Phi$ is) between two one-dimensional spaces, hence a linear isomorphism onto $(f_\Phi^*\mathcal{O}(-1))_m$. Both $\bar\Phi$ and its fibrewise inverse are smooth: in the local frame $e$ above, $\bar\Phi(e(m)) = \Phi(e(m))$ is a smooth nowhere-vanishing section of $f_\Phi^*\mathcal{O}(-1)$, so $\bar\Phi$ carries the frame $e$ of $L$ to a frame of $f_\Phi^*\mathcal{O}(-1)$, and a fibrewise-linear bundle map carrying a frame to a frame is a bundle isomorphism. Hence $\bar\Phi \colon L \cong f_\Phi^*\mathcal{O}(-1)$.
> >
> > **(ii) Converse.** Given smooth $f \colon M \to \mathbb{CP}^N$, the pull-back bundle $f^*\mathcal{O}(-1)$ has total space $\{(m, v) : v \in f(m)\}$ and is a smooth vector bundle by [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|the pull-back theorem]] applied to the tautological bundle. The map $\jmath(m, v) = (m, v \in \mathbb{C}^{N+1})$ is $\mathbb{C}$-linear on each fibre and injective there (it is the inclusion of the subspace $f(m)$ into $\mathbb{C}^{N+1}$), hence a bundle monomorphism; and $f_{\jmath}(m) = \jmath(\{m\} \times f(m)) = f(m)$, so $f_{\jmath} = f$. $\blacksquare$

> [!note]- Lemma 3: Two monomorphisms of one bundle are joined by a fibrewise-injective straight-line homotopy in the doubled space
> **Statement:** Let $L \to M$ be a complex line bundle and let $\Phi \colon L \to \underline{\mathbb{C}^{N+1}}$ and $\Phi' \colon L \to \underline{\mathbb{C}^{N'+1}}$ be bundle monomorphisms. Write $W := \mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1} = \mathbb{C}^{N+N'+2}$ and let $\iota_A \colon \mathbb{CP}^N \hookrightarrow \mathbb{P}(W) = \mathbb{CP}^{N+N'+1}$, $\iota_B \colon \mathbb{CP}^{N'} \hookrightarrow \mathbb{P}(W)$ be the standard inclusions coming from the two summands. Then the family
> $$g_t \colon L \to \underline{W}, \qquad g_t(v) := \big((1-t)\,\Phi(v),\ t\,\Phi'(v)\big) \in \mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1}, \qquad t \in [0,1],$$
> is a bundle monomorphism for **every** $t$, and the induced maps $F_t := f_{g_t} \colon M \to \mathbb{CP}^{N+N'+1}$ form a smooth homotopy from $F_0 = \iota_A \circ f_\Phi$ to $F_1 = \iota_B \circ f_{\Phi'}$.
>
> **Hint:** The two images live in complementary summands, so $g_t(v) = 0$ forces both components to vanish; use injectivity of $\Phi$ (or $\Phi'$) at each end and of either one in the interior.
>
> **Why needed:** It is the entire content of the hard direction of part (b): isomorphic bundles produce two monomorphisms of the same $L$, and this homotopy connects their classifying maps inside the enlarged projective space.
>
> > [!note]- Full proof
> > **$g_t$ is a bundle map, linear on fibres.** For fixed $t$, each component $(1-t)\Phi$ and $t\Phi'$ is $\mathbb{C}$-linear on fibres (a real scalar multiple of a $\mathbb{C}$-linear map), so their direct sum $g_t$ is $\mathbb{C}$-linear on each fibre, and $g_t$ depends smoothly on $(m, t)$ because $\Phi, \Phi'$ do and $t \mapsto (1-t, t)$ is smooth.
> >
> > **$g_t$ is injective on every fibre, for every $t$.** Fix $m$ and $t \in [0,1]$, and suppose $v \in L_m$ with $g_t(v) = 0$. Then, reading the two summands of $W = \mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1}$ separately,
> > $$(1-t)\,\Phi(v) = 0 \quad \text{and} \quad t\,\Phi'(v) = 0 \qquad \text{(a vector of } \mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1} \text{ is zero iff both components are).}$$
> > We split on $t$. **If $t < 1$**, then $1 - t \neq 0$, so the first equation gives $\Phi(v) = 0$, whence $v = 0$ (since $\Phi$ is fibrewise injective). **If $t = 1$**, then the second equation reads $\Phi'(v) = 0$, whence $v = 0$ (since $\Phi'$ is fibrewise injective). The two cases $t < 1$ and $t = 1$ are exhaustive, so in all cases $v = 0$; hence $g_t$ is injective on $L_m$. Combined with the previous paragraph, $g_t$ is a bundle monomorphism for every $t$.
> >
> > **The induced homotopy.** By Lemma 2(i) applied to $g_t$ (each is a bundle monomorphism into $\underline{W}$), the map $F_t := f_{g_t} \colon M \to \mathbb{P}(W) = \mathbb{CP}^{N+N'+1}$, $F_t(m) = g_t(L_m)$, is smooth; and jointly in $(m, t)$ it is smooth because $g_t$ is smooth in $(m, t)$ and fibrewise non-zero, so $(m, t) \mapsto [g_t(e(m))]$ is smooth for a local non-vanishing frame $e$ (as in Lemma 2). Thus $(m, t) \mapsto F_t(m)$ is a smooth homotopy. At the endpoints,
> > $$F_0(m) = g_0(L_m) = \Phi(L_m) \oplus 0 = \iota_A\big(\Phi(L_m)\big) = \iota_A\big(f_\Phi(m)\big) \qquad \text{(since } g_0 = \Phi \oplus 0\text{),}$$
> > $$F_1(m) = g_1(L_m) = 0 \oplus \Phi'(L_m) = \iota_B\big(\Phi'(L_m)\big) = \iota_B\big(f_{\Phi'}(m)\big) \qquad \text{(since } g_1 = 0 \oplus \Phi'\text{).}$$
> > Therefore $F_t$ is a homotopy from $\iota_A \circ f_\Phi$ to $\iota_B \circ f_{\Phi'}$ inside $\mathbb{CP}^{N+N'+1}$. $\blacksquare$

> [!note]- Lemma 4: Complex line bundles and principal $U(1)$-bundles are the same classification problem
> **Statement:** Over any manifold $M$ there is a bijection between isomorphism classes of complex line bundles and isomorphism classes of principal $U(1)$-bundles, natural in $M$: to a line bundle $L$ with any Hermitian metric one assigns the unitary frame bundle $U(L)$, a principal $U(1)$-bundle; to a principal $U(1)$-bundle $P$ one assigns the associated line bundle $P \times_{\varrho_1} \mathbb{C}$ for the standard representation $\varrho_1(\lambda) w = \lambda w$. These assignments are mutually inverse on isomorphism classes and independent of the chosen Hermitian metric.
>
> **Hint:** Existence of a Hermitian metric and its reduction of the frame bundle come from [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group]]; the associated-bundle identity from [[Thm - Vector Bundles are Associated to Their Frame Bundles]]; metric-independence from convexity plus homotopy invariance.
>
> **Why needed:** It licenses passing freely between the "$f^*\mathcal{O}(-1) \cong L$" and "$P \cong f^*(\text{Hopf})$" phrasings in (a) and makes the bijection of (b) a statement about $U(1)$-bundles.
>
> > [!note]- Full proof
> > **From $L$ to a $U(1)$-bundle.** A complex line bundle $L$ admits a Hermitian metric $h$: patch the flat metrics of local trivialisations with a partition of unity (a convex combination of Hermitian inner products is a Hermitian inner product), using [[Thm - Existence of Smooth Partitions of Unity|partitions of unity]]. By [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|the reduction theorem]] — a Hermitian structure on a rank-one complex bundle is the same as a $U(1)$-reduction $U(L) \subset \operatorname{Fr}(L)$ of its frame bundle — the unitary frame bundle $U(L) = \{\, \text{unit-length frames } u \colon \mathbb{C} \to L_m \,\}$ is a principal $U(1)$-bundle.
> >
> > **From a $U(1)$-bundle to $L$.** By [[Thm - Vector Bundles are Associated to Their Frame Bundles|the associated-bundle identity]], the standard representation $\varrho_1$ recovers the bundle: $U(L) \times_{\varrho_1} \mathbb{C} \cong L$, and conversely, starting from a principal $U(1)$-bundle $P$, the associated bundle $P \times_{\varrho_1} \mathbb{C}$ is a complex line bundle whose unitary frame bundle is again $P$. Thus the two assignments are mutually inverse on isomorphism classes.
> >
> > **Independence of the metric.** Let $h_0, h_1$ be two Hermitian metrics on $L$, with unitary frame bundles $U_0(L), U_1(L)$. The straight-line family $h_t := (1-t)h_0 + t h_1$ is a Hermitian metric for each $t \in [0,1]$ (a convex combination of Hermitian inner products is positive-definite Hermitian), so it is a Hermitian metric on the pull-back bundle $\operatorname{pr}^*L \to M \times [0,1]$ under the projection $\operatorname{pr} \colon M \times [0,1] \to M$; its unitary frame bundle $Q \to M \times [0,1]$ is a principal $U(1)$-bundle restricting to $U_0(L)$ over $M \times \{0\}$ and to $U_1(L)$ over $M \times \{1\}$. By [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|homotopy invariance of principal bundles]] — a principal bundle over $M \times [0,1]$ has isomorphic restrictions to $M \times \{0\}$ and $M \times \{1\}$ — we conclude $U_0(L) \cong U_1(L)$. Hence the isomorphism class of the $U(1)$-bundle does not depend on the metric. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a compact manifold and $L \to M$ a complex line bundle. Fix once and for all a Hermitian metric $\langle \cdot, \cdot \rangle$ on $L$, linear in the first and conjugate-linear in the second argument; it exists by the partition-of-unity argument recorded in Lemma 4. We freely use the dictionary of Lemma 4 between complex line bundles and principal $U(1)$-bundles, and the identification $S^{2N+1} \times_{U(1)} \mathbb{C} \cong \mathcal{O}(-1)$ of the [[Def - The Hopf Bundle|Hopf bundle]]'s associated line bundle with the tautological bundle, proved on [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]].
>
> **Step 0 — well-posedness of the pull-back.** For any smooth $f \colon M \to \mathbb{CP}^N$ the pull-back $f^*\mathcal{O}(-1)$ is a genuine complex line bundle over $M$, by [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|the pull-back theorem]] applied to the vector bundle $\mathcal{O}(-1) \to \mathbb{CP}^N$; so both sides of "$f^*\mathcal{O}(-1) \cong L$" are objects of the same category, and the statement is meaningful.
>
> ---
> **Part (a) — existence of a classifying map.**
>
> **Construct spanning sections.** By **Lemma 1**, compactness gives finitely many sections $s_0, \dots, s_N \in \Gamma(L)$ whose values span $L_m$ at every $m$ (equivalently, at each $m$ some $s_i(m) \neq 0$).
>
> **Construct the Gauss map.** Define the bundle map
> $$\Phi \colon L \to \underline{\mathbb{C}^{N+1}}, \qquad \Phi(v) := \big(\langle v, s_0(m) \rangle,\ \dots,\ \langle v, s_N(m) \rangle\big) \quad \text{for } v \in L_m.$$
> It is $\mathbb{C}$-linear on each fibre, because $v \mapsto \langle v, s_i(m) \rangle$ is $\mathbb{C}$-linear (the metric is linear in the first argument). It is injective on each fibre: suppose $v \in L_m$ has $\Phi(v) = 0$, so $\langle v, s_i(m) \rangle = 0$ for all $i$; choose $j$ with $s_j(m) \neq 0$ (possible since the $s_i$ span), and write $v = \lambda\, s_j(m)$ with $\lambda \in \mathbb{C}$ (as $s_j(m)$ spans the line $L_m$); then
> $$0 = \langle v, s_j(m) \rangle = \lambda\,\langle s_j(m), s_j(m) \rangle = \lambda\, \| s_j(m) \|^2 \qquad \text{(linearity in the first slot),}$$
> and $\| s_j(m) \|^2 > 0$ forces $\lambda = 0$, hence $v = 0$. So $\Phi$ is a bundle monomorphism.
>
> **Read off the classifying map.** By **Lemma 2(i)**, the map $f := f_\Phi \colon M \to \mathbb{CP}^N$, $f(m) = \Phi(L_m)$, is smooth and $\Phi$ furnishes an isomorphism $L \cong f^*\mathcal{O}(-1)$. This proves the first sentence of (a).
>
> **Translate to the Hopf bundle.** Let $P := U(L)$ be the unitary frame bundle of $L$, a principal $U(1)$-bundle (Lemma 4). The unitary frame bundle of the tautological bundle is the Hopf bundle, $U(\mathcal{O}(-1)) = S^{2N+1}$ (a unit vector of the fibre line $\mathcal{O}(-1)_\ell = \ell$ is exactly a point of the sphere $S^{2N+1}$ lying over $\ell$, by [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the tautological identification]]). Because the isomorphism $L \cong f^*\mathcal{O}(-1)$ is unitary (it carries the Hermitian metric of $L$ to the pulled-back Hermitian metric of $\mathcal{O}(-1)$; if not literally, replace it by its unitary part, unique by Lemma 4), it induces an isomorphism of unitary frame bundles $P = U(L) \cong U(f^*\mathcal{O}(-1))$. Finally, taking unitary frames commutes with pull-back fibrewise:
> $$\big(U(f^*\mathcal{O}(-1))\big)_m = U\big((f^*\mathcal{O}(-1))_m\big) = U\big(\mathcal{O}(-1)_{f(m)}\big) = (S^{2N+1})_{f(m)} = (f^*S^{2N+1})_m \qquad \text{(a unitary frame of the fibre over } m \text{ is a unitary frame of the fibre over } f(m) \text{),}$$
> and this fibrewise identification is a smooth bundle isomorphism $U(f^*\mathcal{O}(-1)) \cong f^*S^{2N+1}$ because it carries local unitary frames to local unitary frames. Combining, $P \cong f^*\big(S^{2N+1} \to \mathbb{CP}^N\big)$. This proves the second sentence of (a).
>
> ---
> **Part (b), direction ($\Leftarrow$) — homotopic maps classify isomorphic bundles.**
>
> **The inclusions pull the tautological bundle back to itself.** Let $\iota \colon \mathbb{CP}^N \hookrightarrow \mathbb{CP}^{N+N'+1} = \mathbb{P}(\mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1})$ be the standard inclusion arising from the first summand. For a line $\ell \subset \mathbb{C}^{N+1}$, the fibre $\mathcal{O}(-1)_{\iota(\ell)}$ over $\iota(\ell)$ is the same line $\ell$, now regarded inside $\mathbb{C}^{N+1} \oplus \mathbb{C}^{N'+1}$; hence the tautological identification gives $\iota^*\mathcal{O}(-1) = \mathcal{O}(-1)$ as bundles over $\mathbb{CP}^N$, and likewise for the inclusion of the second summand.
>
> **Apply homotopy invariance.** Suppose $\iota_A \circ f \simeq \iota_B \circ f'$ in $\mathbb{CP}^{N+N'+1}$, where $\iota_A, \iota_B$ are the two standard inclusions. By [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|homotopy invariance of pull-back bundles]] — smoothly homotopic maps pull back isomorphic bundles — we have $(\iota_A \circ f)^*\mathcal{O}(-1) \cong (\iota_B \circ f')^*\mathcal{O}(-1)$. By functoriality of pull-back and the previous paragraph,
> $$(\iota_A \circ f)^*\mathcal{O}(-1) = f^*\big(\iota_A^*\mathcal{O}(-1)\big) = f^*\mathcal{O}(-1), \qquad (\iota_B \circ f')^*\mathcal{O}(-1) = f'^*\mathcal{O}(-1).$$
> Combining the two displays, $f^*\mathcal{O}(-1) \cong f'^*\mathcal{O}(-1)$, as required.
>
> ---
> **Part (b), direction ($\Rightarrow$) — isomorphic bundles have homotopic maps.**
>
> **Recover two monomorphisms of one bundle.** Suppose $f^*\mathcal{O}(-1) \cong f'^*\mathcal{O}(-1)$; call this common line bundle $L$ (this is the setting of the theorem, where $L$ is given and $f, f'$ both classify it). By **Lemma 2(ii)** the tautological inclusions give bundle monomorphisms $\jmath \colon f^*\mathcal{O}(-1) \hookrightarrow \underline{\mathbb{C}^{N+1}}$ and $\jmath' \colon f'^*\mathcal{O}(-1) \hookrightarrow \underline{\mathbb{C}^{N'+1}}$ with $f_\jmath = f$ and $f_{\jmath'} = f'$. Fix isomorphisms $\alpha \colon L \xrightarrow{\cong} f^*\mathcal{O}(-1)$ and $\alpha' \colon L \xrightarrow{\cong} f'^*\mathcal{O}(-1)$ and set
> $$\Phi := \jmath \circ \alpha \colon L \hookrightarrow \underline{\mathbb{C}^{N+1}}, \qquad \Phi' := \jmath' \circ \alpha' \colon L \hookrightarrow \underline{\mathbb{C}^{N'+1}}.$$
> Each is a composite of a bundle isomorphism with a bundle monomorphism, hence a bundle monomorphism, and $f_\Phi = f_{\jmath} = f$, $f_{\Phi'} = f_{\jmath'} = f'$ (the classifying map of Lemma 2 depends only on the image sub-bundle, which is unchanged by pre-composing with the isomorphism $\alpha$ of $L$ onto the source).
>
> **Homotope in the doubled space.** Apply **Lemma 3** to $\Phi, \Phi'$: the straight-line family $g_t = (1-t)\Phi \oplus t\Phi'$ into $\underline{\mathbb{C}^{N+N'+2}}$ is fibrewise injective for every $t$, and its induced maps give a smooth homotopy from $\iota_A \circ f_\Phi = \iota_A \circ f$ to $\iota_B \circ f_{\Phi'} = \iota_B \circ f'$ in $\mathbb{CP}^{N+N'+1}$. Thus $\iota_A \circ f \simeq \iota_B \circ f'$, which is the claim.
>
> ---
> **Part (b), the bijection.** Consider the assignment $\Theta \colon P \mapsto [f_P]$ sending a principal $U(1)$-bundle (equivalently, by Lemma 4, a complex line bundle $L$) to the class in $[M ; \mathbb{CP}^\infty] = \varinjlim_N [M ; \mathbb{CP}^N]$ of any classifying map $f_P$ produced by part (a).
>
> **Well-defined.** If $f$ and $f'$ are two classifying maps of the same $L$ — that is, $f^*\mathcal{O}(-1) \cong L \cong f'^*\mathcal{O}(-1)$ — then by direction ($\Rightarrow$) of (b), $\iota_A \circ f \simeq \iota_B \circ f'$ in $\mathbb{CP}^{N+N'+1}$, so $f$ and $f'$ represent the same element of the direct limit $[M ; \mathbb{CP}^\infty]$. Hence $[f_P]$ is independent of the choice of classifying map, and (using Lemma 4) $\Theta$ depends only on the isomorphism class of $P$.
>
> **Surjective.** Let $c \in [M ; \mathbb{CP}^\infty]$; since the whole series works in the smooth category, $c$ is a smooth-homotopy class of smooth maps, represented by a smooth $f \colon M \to \mathbb{CP}^N$ at some finite stage $N$ (that is how the direct limit $\varinjlim_N [M ; \mathbb{CP}^N]$ is defined on [[Def - Classifying Bundle and Classifying Map|the classifying-bundle page]]). Set $L := f^*\mathcal{O}(-1)$ and $P := U(L)$. Then $f$ is a classifying map of $P$ by construction, so $\Theta(P) = [f] = c$.
>
> **Injective.** Suppose $\Theta(P) = \Theta(Q)$ with classifying maps $f$ of $P$ and $f'$ of $Q$. Equality in the direct limit means that after the standard inclusions into some common $\mathbb{CP}^{N''}$ the maps $f$ and $f'$ are homotopic there. By direction ($\Leftarrow$) of (b) applied at that stage (the standard inclusions pull $\mathcal{O}(-1)$ back to $\mathcal{O}(-1)$, and homotopy invariance then transfers the isomorphism), $f^*\mathcal{O}(-1) \cong f'^*\mathcal{O}(-1)$; that is, the line bundles classified by $P$ and $Q$ are isomorphic, so $P \cong Q$ by Lemma 4. Hence $\Theta$ is injective, and therefore a bijection.
>
> ---
> **Part (c) — the quaternionic case.** We repeat parts (a) and (b) with $\mathbb{C}$ replaced by $\mathbb{H}$, $\mathbb{CP}^N$ by $\mathbb{HP}^N$, and $\mathcal{O}(-1)$ by $\mathcal{O}_{\mathbb{H}}(-1)$; the group is $Sp(1)$, acting on $\mathbb{H}^{N+1}$ and on quaternionic lines by **right** multiplication, and a quaternionic line bundle is a rank-one **right** $\mathbb{H}$-module bundle. Non-commutativity of $\mathbb{H}$ forces us to verify each linearity claim, and we list the three places where it matters.
>
> **First, a quaternionic Hermitian metric exists.** A quaternionic Hermitian form $\langle \cdot, \cdot \rangle \colon L \times L \to \mathbb{H}$, conjugate-linear in the first and right-$\mathbb{H}$-linear in the second argument (so $\langle v, w\, q \rangle = \langle v, w \rangle\, q$), exists on any quaternionic bundle by patching local flat forms with a partition of unity; a convex combination with **real** coefficients $\varphi_i \geq 0$ of positive quaternionic Hermitian forms is again positive quaternionic Hermitian, because the real coefficients commute with quaternions and preserve positivity. This uses [[Thm - Existence of Smooth Partitions of Unity|partitions of unity]] exactly as in Lemma 4.
>
> **Second, the Gauss map is right-$\mathbb{H}$-linear and fibrewise injective.** With right-$\mathbb{H}$-linear metric in the second slot, define $\Phi(v) := (\langle s_0(m), v \rangle, \dots, \langle s_N(m), v \rangle) \in \mathbb{H}^{N+1}$ for $v \in L_m$, using spanning sections $s_i$ from the quaternionic form of Lemma 1 (whose proof used only compactness, partitions of unity, and local non-vanishing sections, all available for right $\mathbb{H}$-module bundles). Then $\Phi(v\,q) = \Phi(v)\,q$ (right-linearity in the second slot), so $\Phi$ is a monomorphism of right $\mathbb{H}$-modules; injectivity on fibres follows as before, since $\langle s_j(m), v \rangle = 0$ for a spanning $s_j(m)$ forces $v = 0$ by positivity. Its image $\Phi(L_m)$ is a right quaternionic line, a point of $\mathbb{HP}^N$, and $f_\Phi^*\mathcal{O}_{\mathbb{H}}(-1) \cong L$ by the quaternionic form of Lemma 2, giving (a). The Hopf bundle $S^{4N+3} \to \mathbb{HP}^N$ plays the role of $S^{2N+1} \to \mathbb{CP}^N$, its associated line bundle being $\mathcal{O}_{\mathbb{H}}(-1)$ [[Def - The Hopf Bundle|(quaternionic Hopf bundle)]].
>
> **Third, the straight-line homotopy stays right-$\mathbb{H}$-linear.** In $W = \mathbb{H}^{N+1} \oplus \mathbb{H}^{N'+1}$ set $g_t(v) := ((1-t)\Phi(v), t\Phi'(v))$. The scalars $(1-t)$ and $t$ are **real**, so they lie in the centre of $\mathbb{H}$ and commute with right multiplication: $g_t(v\,q) = ((1-t)\Phi(v)q, t\Phi'(v)q) = g_t(v)\,q$, so $g_t$ is right-$\mathbb{H}$-linear. Fibrewise injectivity for every $t$ holds by the identical case split on $t < 1$ and $t = 1$ as in Lemma 3, since $\Phi, \Phi'$ are fibrewise injective. Thus the quaternionic forms of Lemma 3 and of the bijection argument go through verbatim, with $\mathbb{HP}^{N+N'+1}$ the enlarged target and $[M ; \mathbb{HP}^\infty] = \varinjlim_N [M ; \mathbb{HP}^N]$ the direct limit. Because $Sp(1) \cong SU(2)$ [[Ex - SU(2) is the Group of Unit Quaternions|(unit quaternions)]], the same statements classify principal $SU(2)$-bundles that arise as quaternionic frame bundles. This proves (c).
>
> **Conclusion.** Every complex line bundle over a compact manifold is the pull-back of the tautological bundle along a smooth map to a finite projective space; two such maps classify isomorphic bundles precisely when they become homotopic in a common projective space; and the induced map from isomorphism classes of principal $U(1)$-bundles to $[M ; \mathbb{CP}^\infty]$ is a bijection. The same holds for principal $Sp(1)$-bundles with quaternionic projective space. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Adiabatic quantum mechanics and the Berry phase.** Let $H \colon M \to \operatorname{Herm}(n)$ be a smooth family of Hermitian Hamiltonians over a compact parameter manifold $M$, each with a non-degenerate lowest eigenvalue. The ground-state rays form a complex line bundle $L \to M$, the *Berry bundle*. The theorem applies because $M$ is compact, and its classifying map $f \colon M \to \mathbb{CP}^N$ measures the topological obstruction to a global smooth choice of ground-state wavefunction. This is non-obvious because the physical input is a spectral-theory family, with no bundle in sight until one recognises the eigenline as a smooth sub-bundle via the spectral projection $P(m) = \tfrac{1}{2\pi i}\oint (z - H(m))^{-1}\,dz$.

**Divisors on a compact Riemann surface.** For a compact Riemann surface $\Sigma$, a divisor $D = \sum n_i p_i$ produces a holomorphic line bundle $\mathcal{O}(D)$, and the theorem realises $\mathcal{O}(D)$ as $f^*\mathcal{O}(-1)$ for a smooth $f \colon \Sigma \to \mathbb{CP}^N$. The application is non-obvious because the natural home of a divisor is complex-analytic (linear equivalence, the Picard group) whereas the theorem is smooth-topological; the bridge is that the smooth isomorphism class forgets the holomorphic structure and lands in $[\Sigma ; \mathbb{CP}^\infty]$, which over a surface is a single integer, the degree $\sum n_i$.

**Magnetic monopoles and Dirac quantisation.** A magnetic monopole on $S^2$ is a connection on a principal $U(1)$-bundle over $S^2$; the theorem classifies the possible bundles by $[S^2 ; \mathbb{CP}^\infty]$, which is $\mathbb{Z}$, recovering Dirac's quantisation of magnetic charge as the discreteness of the classifying homotopy class. The application is non-obvious because the physics is stated in terms of a continuously varying field strength, and the integrality is not visible until the bundle is placed in the homotopy set; the enlargement device of part (b) is exactly what forbids interpolating continuously between charges.

---

# Bridges

- **[[Def - First Chern Class via the Classifying Map|First Chern class via the classifying map]]** — the direct downstream construction. Once every line bundle is $f^*\mathcal{O}(-1)$ for a classifying $f$, one defines $c_1^{\mathrm{top}}(L) := -f^*[\omega_N]$ by pulling back the generator of $H^2_{dR}(\mathbb{CP}^N)$; part (b) and the homotopy invariance of de Rham cohomology make this independent of the choice of $f$, and the sign is a convention that reconciles it with the curvature formula.

- **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|Classification of $U(1)$-bundles by the first Chern class]]** — the completion of the count. Where the present theorem identifies the classifying set as $[M ; \mathbb{CP}^\infty]$, that theorem computes the set over a closed oriented surface as $\mathbb{Z}$ via the clutching construction, upgrading the bijection here into a group isomorphism $\operatorname{Pic}(\Sigma) \cong \mathbb{Z}$ under tensor product of bundles.

- **[[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|Classification of $SU(2)$-bundles over four-manifolds]]** — the quaternionic sequel. Part (c) reduces $Sp(1) \cong SU(2)$ bundles to homotopy classes of maps into $\mathbb{HP}^\infty$; over a four-manifold that theorem then extracts the integer instanton number by the clutching and degree machinery, the topological label of Yang–Mills moduli spaces.

- **[[Thm - First Chern Class of a Line Bundle from Curvature|First Chern class of a line bundle from curvature]]** — the analytic counterpart. The classifying-map first Chern class defined downstream of this theorem is proved in chapter VI to equal $[\tfrac{i}{2\pi}F_A]$ for any Hermitian connection, tying the homotopy-theoretic classification here to the differential-geometric Chern–Weil representative.

- **The Grassmannian classification of higher-rank bundles** — the natural generalisation. Replacing the single line by an $n$-plane, one replaces $\mathbb{CP}^\infty$ with the infinite Grassmannian $\operatorname{Gr}_n(\mathbb{C}^\infty)$ and the tautological line with the tautological $n$-plane bundle; the proof here transcribes with "spanning sections" becoming "sections spanning each fibre" and "line" becoming "$n$-plane", giving the classification of rank-$n$ complex bundles over compact manifolds.

---

# Unlocked by This

> [!tip] Topological First Chern Class *(from Gauge Theory)*
> With every line bundle exhibited as a pull-back $f^*\mathcal{O}(-1)$, one may pull back cohomology classes of projective space to obtain characteristic classes of the bundle that depend only on its isomorphism class. This is the definition of the topological first Chern class; see [[Def - First Chern Class via the Classifying Map]].

> [!tip] Homotopy Classification of Bundles *(from Algebraic Topology)*
> The bijection onto $[M ; \mathbb{CP}^\infty]$ is the line-bundle instance of the general principle that principal $G$-bundles over a space are classified by homotopy classes of maps into a classifying space $BG$; here $BU(1) = \mathbb{CP}^\infty$ and $BSp(1) = \mathbb{HP}^\infty$. See [[Def - Classifying Bundle and Classifying Map]].
