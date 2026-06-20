---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - May's Recognition Principle"
  - "Def - Operad"
  - "Def - Algebra for an Operad"
  - "Def - Higher Homotopy Group"
tags: [category-theory, higher-categories, foundations, homotopy-theory]
---

# Problem Statement

Let $E_1$ be the **little intervals operad** (the $n = 1$ little disks operad): $E_1(k)$ is the space of $k$ disjoint open subintervals of $(0,1)$, ordered by position, with composition by inserting configurations into subintervals. Let $Y$ be a based space and $\Omega Y = \{\gamma : [0,1] \to Y : \gamma(0) = \gamma(1) = *\}$ its based loop space.

(a) Construct the $E_1$-algebra structure on $\Omega Y$: given $c \in E_1(k)$ (an ordered configuration of $k$ subintervals) and loops $\gamma_1, \dots, \gamma_k$, define a loop $\theta_c(\gamma_1, \dots, \gamma_k)$, and check the operad-action axioms hold (up to the homeomorphisms built into reparametrisation).

(b) Show that $E_1$ is homotopy-equivalent, as an operad, to the non-symmetric associative operad $\mathrm{Assoc}^{\mathrm{ns}}$ (each $E_1(k)$ is contractible), so that an $E_1$-algebra is "an $A_\infty$-monoid" — associative up to coherent homotopy.

(c) State what [[Thm - May's Recognition Principle|May's recognition principle]] adds: which $E_1$-algebras are loop spaces, and why the homotopy-coherence captured by $E_1$ (rather than a single homotopy-associative product) is necessary.

**Recall:**

![[Thm - May's Recognition Principle#Statement]]

A space is **contractible** if it is homotopy-equivalent to a point. A based loop space $\Omega Y$ has concatenation of loops as a multiplication, associative and unital only up to reparametrising homotopy. See [[Def - Higher Homotopy Group|higher homotopy groups]] for $\pi_0(\Omega Y) = \pi_1(Y)$.

---

# Convergent Strategy

**Problem class:** This is a *recognise-and-construct-an-operad-action* problem in topology, and the capstone application of the chapter: it exhibits a topological operad acting on a loop space and connects to the recognition principle. The method is to build the structure maps geometrically and then identify the operad up to homotopy.

**Assumption pattern:** The signal is "a multiplication that is associative only up to homotopy, parametrised by a space of configurations". Loop concatenation is not strictly associative — $(\alpha\cdot\beta)\cdot\gamma$ and $\alpha\cdot(\beta\cdot\gamma)$ differ by reparametrisation — and the *space* $E_1(k)$ of ways to subdivide $[0,1]$ is exactly what records these reparametrisations. Recognising "homotopy-associative, with a contractible space of composition choices" is the trigger for "$E_1$-algebra".

**Theorem routing:** Part (a) routes through the geometric definition: place $\gamma_i$ on the $i$th subinterval (reparametrised to fill it) and the basepoint elsewhere. Part (b) routes through the contractibility of configuration spaces of intervals (each $E_1(k) \simeq *$, with $\pi_0(E_1(k))$ a single point but the ordering giving $\mathrm{Assoc}^{\mathrm{ns}}$ structure on components). Part (c) routes through [[Thm - May's Recognition Principle|May's principle]]: group-like $E_1$-algebras are exactly loop spaces.

**Key decision point:** The crux is appreciating *why a single homotopy-associative product is not enough* and the contractible space $E_1(k)$ is. A homotopy-associative $H$-space records associativity by one homotopy; but to deloop, one needs that homotopy to be coherent with all higher ones — the pentagon homotopy, and beyond. The contractibility of $E_1(k)$ encodes *all* these higher coherences at once. The temptation is to think "homotopy-associative + inverses = loop space"; the decision is to recognise this is false (Stasheff's $A_\infty$ obstruction) and that the operad supplies the missing tower.

---

# Legal Operations Used

1. **Construct an operad action geometrically (operation 1 from the topic page).** We define the structure maps $E_1(k) \times (\Omega Y)^k \to \Omega Y$ by placing loops on subintervals.

2. **Identify an operad up to homotopy via contractibility (operation 6 from the topic page).** We show $E_1 \simeq \mathrm{Assoc}^{\mathrm{ns}}$ because each $E_1(k)$ is contractible.

3. **Invoke the recognition principle to characterise algebras (operation 7 from the topic page).** We cite May's theorem to identify group-like $E_1$-algebras as loop spaces.

---

# Hints

> [!note]- Hint 1
> A point of $E_1(k)$ is an ordered tuple of disjoint subintervals $(a_1, b_1), \dots, (a_k, b_k)$ of $(0,1)$. Define $\theta_c(\gamma_\bullet)(t) = \gamma_i\big(\frac{t - a_i}{b_i - a_i}\big)$ if $t \in (a_i, b_i)$, and $*$ otherwise. This is a loop because it is $*$ at $0$, $1$, and on the gaps.

> [!note]- Hint 2
> The standard configuration "two intervals $(0, \tfrac12), (\tfrac12, 1)$" gives ordinary loop concatenation $\gamma_1 \cdot \gamma_2$. Different configurations give reparametrised versions, connected by paths in $E_1(2)$.

> [!note]- Hint 3
> $E_1(k)$ deformation-retracts onto any single configuration by sliding and shrinking the intervals continuously — so $E_1(k)$ is contractible. Its set of path components is a single point, but the *ordering* of the intervals is the data making $\pi_0$-level structure the non-symmetric associative operad.

> [!note]- Hint 4
> For (c): May's principle says a *group-like* $E_1$-algebra (one whose $\pi_0$-monoid is a group) is weakly equivalent to a loop space $\Omega Y$. Group-likeness is essential: a non-group-like $E_1$-algebra (like the free one) is only a loop space after group completion.

---

# Solution

The plan: build the geometric action and check the axioms up to reparametrisation (Step 1); prove contractibility and identify $E_1 \simeq \mathrm{Assoc}^{\mathrm{ns}}$ (Step 2); state the recognition principle and explain the necessity of coherence (Step 3).

**Step 1: The $E_1$-action on $\Omega Y$.**

> [!note]- Derivation
> For $c = ((a_1,b_1), \dots, (a_k, b_k)) \in E_1(k)$ (disjoint, ordered subintervals) and loops $\gamma_1, \dots, \gamma_k \in \Omega Y$, define
> $$\theta_c(\gamma_1, \dots, \gamma_k)(t) = \begin{cases} \gamma_i\!\left(\dfrac{t - a_i}{b_i - a_i}\right) & t \in [a_i, b_i], \\[4pt] * & \text{otherwise.}\end{cases}$$
> This is continuous (each $\gamma_i$ is a loop, so it equals $*$ at the endpoints $a_i, b_i$, matching the constant value on the gaps) and is a based loop. The assignment is continuous in $c$ and the $\gamma_i$, giving a map $E_1(k) \times (\Omega Y)^k \to \Omega Y$. *Unit:* $E_1(1)$ contains the full interval $(0,1)$, acting as the identity (up to reparametrisation). *Associativity:* inserting a configuration into a subinterval and then placing loops is the same as placing the composite loops directly — both reparametrise the loops onto nested subintervals, and the operad composition of $E_1$ (insert configs into subintervals) matches this exactly. So $\Omega Y$ is an $E_1$-algebra.

**Step 2: $E_1 \simeq \mathrm{Assoc}^{\mathrm{ns}}$.**

> [!note]- Derivation
> Each $E_1(k)$ is contractible: the space of $k$ disjoint ordered open subintervals of $(0,1)$ deformation-retracts onto the single "standard" configuration $(\frac{0}{k}, \frac{1}{k}), (\frac{1}{k}, \frac{2}{k}), \dots$ by continuously sliding and rescaling each interval to its standard slot (the configuration space of ordered disjoint intervals is convex up to the ordering constraint, hence contractible). Thus $E_1(k) \simeq *$ for all $k$, and the operad map $E_1 \to \mathrm{Assoc}^{\mathrm{ns}}$ collapsing each $E_1(k)$ to its single point $* = \mathrm{Assoc}^{\mathrm{ns}}(k)$ is an operad equivalence (a levelwise homotopy equivalence respecting composition). So $E_1$ is a topological *resolution* of the associative operad: an $E_1$-algebra is associative-up-to-coherent-homotopy, an **$A_\infty$-monoid**. The chains $C_*(E_1)$ give the $A_\infty$-operad, whose algebras are $A_\infty$-algebras. The ordering of the intervals (not their positions, which contract away) is what makes the homotopy-level structure *associative* rather than commutative — there is no room in dimension $1$ to slide intervals past each other, so no commutativity, exactly mirroring $E_1 \simeq \mathrm{Assoc}$, not $\mathrm{Comm}$.

**Step 3: The recognition principle.**

> [!note]- Derivation
> Part (a) shows loop spaces *are* $E_1$-algebras (and group-like, since $\pi_0(\Omega Y) = \pi_1(Y)$ is a group). [[Thm - May's Recognition Principle|May's recognition principle]] supplies the converse: a *group-like* $E_1$-algebra $X$ is weakly equivalent to a loop space, $X \simeq \Omega(BX)$ for a delooping $BX$ (the classifying space / bar construction). The group-like hypothesis is essential — looping always produces a group-like space, so a non-group-like $E_1$-algebra (such as the free $E_1$-algebra $\coprod_k E_1(k)\times_{} X^k$, whose $\pi_0$ is a free monoid, not a group) is a loop space only after group completion.
>
> *Why coherence (the contractible $E_1(k)$, not a single homotopy) is necessary:* a delooping $BX$ exists only if the multiplication on $X$ is coherently associative to all orders. A bare homotopy-associative $H$-space records associativity by one homotopy but says nothing about the *pentagon* coherence relating the two ways of re-associating four factors, nor the higher ones; without these, the bar construction fails to be well-defined and there is no $BX$. Stasheff's associahedra $K_n$ are exactly the spaces parametrising these higher coherences, and $E_1(n)$ (contractible, hence carrying all of them) supplies them all at once. This is why "homotopy-associative $H$-space with inverses" is *not* enough to be a loop space: the canonical counterexamples are homotopy-associative $H$-spaces that are not loop spaces, failing the higher (pentagon-and-beyond) coherence that $E_1$ enforces.

> [!note]- Complete formal solution
> *(a)* Define $\theta_c(\gamma_\bullet)(t) = \gamma_i((t-a_i)/(b_i-a_i))$ on $[a_i,b_i]$ and $*$ elsewhere; this is a based loop, continuous in all data, with $E_1(1)$ acting as identity and $E_1$-composition matching nesting of subintervals. So $\Omega Y$ is an $E_1$-algebra, group-like since $\pi_0(\Omega Y) = \pi_1(Y)$.
>
> *(b)* Each $E_1(k)$ deformation-retracts to its standard configuration, hence is contractible; the collapse $E_1 \to \mathrm{Assoc}^{\mathrm{ns}}$ is an operad equivalence, so $E_1$-algebras are $A_\infty$-monoids (associative up to coherent homotopy). The ordering survives, the positions contract, giving $\mathrm{Assoc}$ not $\mathrm{Comm}$.
>
> *(c)* By [[Thm - May's Recognition Principle|May's principle]], group-like $E_1$-algebras are exactly loop spaces up to weak equivalence; group-likeness is needed because looping yields group-like spaces, and the full $E_1$-coherence (contractible $E_1(k)$, the associahedra) rather than a single associativity homotopy is needed for the delooping bar construction to exist. $\blacksquare$

---

# Key Takeaways

**The configuration space is the space of composition choices, and its homotopy type is the algebra's coherence.** The deepest lesson is that the *topology* of $E_1(k)$ — its contractibility — is what encodes "associative up to coherent homotopy". Each point of $E_1(k)$ is a way to combine $k$ loops; paths between points are homotopies between combinations; the contractibility says all these ways are coherently equivalent, to all higher orders. This is the defining move of topological operads: replace an algebraic axiom (associativity) by a *space* of operations whose homotopy type measures how strictly the axiom holds. When you meet a structure that is "associative/commutative up to homotopy", the right invariant is not "does a homotopy exist?" but "what is the homotopy type of the space of operations?" — and an operad is exactly the device that records it.

**Dimension controls commutativity: one dimension gives associative, infinite dimension gives commutative.** That $E_1 \simeq \mathrm{Assoc}$ (not $\mathrm{Comm}$) because intervals on a line cannot slide past each other is the geometric heart of the Eckmann–Hilton phenomenon from the [[Def - Higher Homotopy Group|higher homotopy group]] page. In $E_n$ for $n \geq 2$ the little disks *can* be moved around each other, so $E_n(2) \simeq S^{n-1}$ is connected and the product becomes homotopy-commutative; as $n \to \infty$, $E_\infty(k) \simeq E\Sigma_k$ is contractible-with-free-action and the algebras are fully (homotopy-)commutative. The single dial — how much room the configurations have to permute — runs the entire spectrum from associative to commutative, and it is *literally* the dimension $n$. This is the cleanest possible statement of "more dimensions force more commutativity", and it is why loop spaces (one loop coordinate) are merely associative while $n$-fold loop spaces acquire increasing commutativity.

**Recognition means structure is sufficient, not just necessary — and group-likeness plus full coherence is the exact price.** The capstone insight is that [[Thm - May's Recognition Principle|May's principle]] turns an operad action from a *property a loop space happens to have* into a *complete characterisation*: having a group-like $E_1$-action is enough to *be* a loop space. The two non-negotiable ingredients are group-likeness (because looping always lands in group-like spaces) and the full homotopy-coherence of $E_1$ (because the bar-construction delooping needs every higher associativity coherence, the associahedra, which a single homotopy cannot supply). This is the template for the entire operadic philosophy in homotopy theory: encode a homotopy-coherent structure by an operad, check group-likeness, and read off a deep topological conclusion — the same pattern that, for $E_n$, recognises $n$-fold loop spaces, and for $E_\infty$, recognises infinite loop spaces and connective spectra.
