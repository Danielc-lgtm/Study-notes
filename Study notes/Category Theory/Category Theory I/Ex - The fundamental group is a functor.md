---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Functor"
  - "Def - Path-Product and the Fundamental Group"
  - "Thm - The Fundamental Group is a Group"
tags: [category-theory, foundations, homotopy-theory]
---

# Problem Statement

Show that the fundamental group is a [[Def - Functor|functor]] $\pi_1 : \mathbf{Top}_* \to \mathbf{Grp}$ from based [[Def - Topological Space|topological spaces]] to [[Def - Group|groups]]. Precisely: a based continuous map $f : (X, x_0) \to (Y, y_0)$ (so $f(x_0) = y_0$) induces a [[Def - Homomorphism|group homomorphism]]
$$f_* : \pi_1(X, x_0) \longrightarrow \pi_1(Y, y_0), \qquad f_*[\gamma] = [f \circ \gamma],$$
and this assignment satisfies $(g \circ f)_* = g_* \circ f_*$ and $(1_X)_* = 1_{\pi_1(X, x_0)}$. Then deduce that a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]] (in particular a homeomorphism) induces an isomorphism on $\pi_1$, and use this to argue $\mathbb{R}^2 \not\cong \mathbb{R}^2 \setminus \{0\}$.

**Recall:**

The [[Def - Path-Product and the Fundamental Group|fundamental group]] $\pi_1(X, x_0)$ consists of homotopy classes (rel endpoints) of loops at $x_0$, with product $[\gamma][\delta] = [\gamma \cdot \delta]$ (concatenate). ![[Thm - The Fundamental Group is a Group#Statement]]

---

# Convergent Strategy

**Problem class:** This is a "verify a named assignment is a functor and harvest the consequence" exercise. The route is: check $f_*$ is well-defined (respects homotopy), is a homomorphism, then verify the two functor axioms, then apply [[Thm - Functors Preserve Isomorphisms|functors preserve isomorphisms]].

**Assumption pattern:** The decisive facts are that composing a loop with a continuous map yields a loop, and composing a *homotopy* with a continuous map yields a homotopy — so $f_*$ is well-defined on homotopy classes. Functoriality then reduces to associativity of map composition: $(g \circ f) \circ \gamma = g \circ (f \circ \gamma)$.

**Theorem routing:** Well-definedness and homomorphism property are direct. Functoriality is the identity $(g \circ f) \circ \gamma = g \circ (f \circ \gamma)$. The geometric payoff routes through [[Thm - Functors Preserve Isomorphisms|"functors preserve isomorphisms"]]: a homotopy equivalence is an iso in the homotopy category, so $\pi_1$ sends it to an iso, distinguishing spaces with non-isomorphic fundamental groups.

**Key decision point:** The non-obvious step is recognizing that *both* a loop and a homotopy between loops push forward under $f$ — well-definedness on homotopy classes is what makes $f_*$ a function at all, and it is the step most often skipped.

---

# Legal Operations Used

1. **Operation: check well-definedness on equivalence classes before checking algebra** (topic page, Legal Operation 7). $f_*$ acts on homotopy classes; we verify $[\gamma] = [\gamma'] \Rightarrow [f\gamma] = [f\gamma']$.

2. **Operation: reduce functoriality to associativity of composition** (topic page, Legal Operation 7). $(gf)_* = g_* f_*$ is $(gf)\gamma = g(f\gamma)$.

3. **Operation: transport non-isomorphism through a functor** (topic page, Legal Operation 3; [[Thm - Functors Preserve Isomorphisms]]). Different $\pi_1$ values force non-homotopy-equivalence.

---

# Hints

> [!note]- Hint 1
> First check $f_*$ is well-defined: if $\gamma \simeq \gamma'$ via a homotopy $H$, is $f \circ \gamma \simeq f \circ \gamma'$? Compose $H$ with $f$.

> [!note]- Hint 2
> Homomorphism: $f_*([\gamma][\delta]) = [f \circ (\gamma \cdot \delta)]$. Show $f \circ (\gamma \cdot \delta) = (f \circ \gamma) \cdot (f \circ \delta)$ — pushing a concatenation forward is the concatenation of the pushforwards.

> [!note]- Hint 3
> Functoriality: $(g \circ f)_*[\gamma] = [(g \circ f)\gamma] = [g(f\gamma)] = g_*[f\gamma] = g_*(f_*[\gamma])$. The middle step is associativity of map composition.

> [!note]- Hint 4
> Application: $\pi_1(\mathbb{R}^2) = 0$ (contractible) but $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$ (it deformation-retracts to $S^1$). A homeomorphism would induce an isomorphism of these by functoriality — but $0 \not\cong \mathbb{Z}$.

---

# Solution

The plan: establish $f_*$ is well-defined on homotopy classes (push homotopies forward), then a homomorphism (pushforward of a concatenation is the concatenation of pushforwards), then verify the two functor axioms (composition reduces to associativity of map composition). Finally, apply that functors preserve isomorphisms to distinguish $\mathbb{R}^2$ from the punctured plane.

**Step 1: $f_*$ is well-defined.**

> [!note]- Derivation
> Let $f : (X, x_0) \to (Y, y_0)$ be continuous with $f(x_0) = y_0$. If $\gamma$ is a loop at $x_0$, then $f \circ \gamma$ is a loop at $y_0$ (continuous, and starts/ends at $f(x_0) = y_0$). If $\gamma \simeq \gamma'$ rel endpoints via a homotopy $H : [0,1] \times [0,1] \to X$ (with $H(\cdot, 0) = \gamma$, $H(\cdot, 1) = \gamma'$, fixing endpoints), then $f \circ H : [0,1] \times [0,1] \to Y$ is a homotopy rel endpoints from $f \circ \gamma$ to $f \circ \gamma'$. So $[\gamma] = [\gamma']$ implies $[f\gamma] = [f\gamma']$, and $f_*[\gamma] := [f \circ \gamma]$ is a well-defined function $\pi_1(X, x_0) \to \pi_1(Y, y_0)$.

**Step 2: $f_*$ is a group homomorphism.**

> [!note]- Derivation
> For loops $\gamma, \delta$ at $x_0$, the [[Def - Path-Product and the Fundamental Group|product]] is $[\gamma][\delta] = [\gamma \cdot \delta]$ where $\gamma \cdot \delta$ runs $\gamma$ on $[0, \tfrac12]$ then $\delta$ on $[\tfrac12, 1]$. Composing with $f$,
> $$f \circ (\gamma \cdot \delta) = (f \circ \gamma) \cdot (f \circ \delta),$$
> because on $[0,\tfrac12]$ both equal $f(\gamma(2t))$ and on $[\tfrac12,1]$ both equal $f(\delta(2t-1))$. Hence
> $$f_*([\gamma][\delta]) = [f(\gamma \cdot \delta)] = [(f\gamma)\cdot(f\delta)] = [f\gamma][f\delta] = f_*[\gamma]\,f_*[\delta].$$
> So $f_*$ is a [[Def - Homomorphism|homomorphism]].

**Step 3: The functor axioms.**

> [!note]- Derivation
> *Identities.* $(1_X)_*[\gamma] = [1_X \circ \gamma] = [\gamma]$, so $(1_X)_* = 1_{\pi_1(X,x_0)}$.
>
> *Composition.* For based maps $f : (X,x_0) \to (Y,y_0)$ and $g : (Y, y_0) \to (Z, z_0)$, and any loop $\gamma$ at $x_0$,
> $$(g \circ f)_*[\gamma] = [(g \circ f) \circ \gamma] = [g \circ (f \circ \gamma)] = g_*[f \circ \gamma] = g_*\big(f_*[\gamma]\big),$$
> where the middle equality is associativity of composition of maps. So $(g \circ f)_* = g_* \circ f_*$, and $\pi_1 : \mathbf{Top}_* \to \mathbf{Grp}$ is a [[Def - Functor|functor]].

**Step 4: Application — distinguishing spaces.**

> [!note]- Derivation
> By [[Thm - Functors Preserve Isomorphisms|"functors preserve isomorphisms"]], a homeomorphism $f : X \to Y$ (an isomorphism in $\mathbf{Top}$, hence after basing in $\mathbf{Top}_*$) induces an isomorphism $f_* : \pi_1(X, x_0) \xrightarrow{\sim} \pi_1(Y, f(x_0))$. (The same holds for [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalences]], since $\pi_1$ factors through the homotopy category.) Now $\mathbb{R}^2$ is contractible, so $\pi_1(\mathbb{R}^2) = 0$, while $\mathbb{R}^2 \setminus \{0\}$ deformation-retracts onto the circle $S^1$, so $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z}$. If $\mathbb{R}^2 \cong \mathbb{R}^2 \setminus \{0\}$ were a homeomorphism, functoriality would force $0 \cong \mathbb{Z}$ as groups — false. Hence $\mathbb{R}^2 \not\cong \mathbb{R}^2 \setminus \{0\}$.

> [!note]- Complete formal solution
> *Well-defined:* $f \circ \gamma$ is a loop at $y_0$; $f \circ H$ is a rel-endpoint homotopy whenever $H$ is, so $f_*[\gamma] = [f\gamma]$ respects classes.
>
> *Homomorphism:* $f \circ (\gamma\cdot\delta) = (f\gamma)\cdot(f\delta)$, so $f_*([\gamma][\delta]) = f_*[\gamma]f_*[\delta]$.
>
> *Functor:* $(1_X)_* = 1$ since $1_X \circ \gamma = \gamma$; $(gf)_*[\gamma] = [(gf)\gamma] = [g(f\gamma)] = g_*f_*[\gamma]$.
>
> *Application:* a homeomorphism induces a $\pi_1$-isomorphism (functors preserve isos); $\pi_1(\mathbb{R}^2) = 0 \neq \mathbb{Z} = \pi_1(\mathbb{R}^2\setminus\{0\})$, so the spaces are not homeomorphic. $\blacksquare$

---

# Key Takeaways

**Functoriality is what makes algebraic topology a transfer principle.** The reusable insight is that the *only* reason invariants like $\pi_1$, [[Def - Singular Homology|homology]], and cohomology can prove two spaces different is that they are functors: a continuous map induces an algebraic map, compatibly with composition, so a topological relationship becomes an algebraic one. Whenever you want to prove two spaces are not homeomorphic (or not homotopy equivalent), the method is always the same — apply a functor, compute it on both spaces, and exhibit non-isomorphic values. This single move, "functor turns geometry into algebra", is the entire engine of the subject, and this exercise is its prototype.

**Always verify well-definedness on equivalence classes first.** The step beginners most often skip — and the one doing real work here — is checking that $f_*$ respects homotopy, i.e. that pushing a homotopy forward by $f$ is again a homotopy. The general pattern: whenever a map is defined on equivalence classes by acting on representatives, the first obligation is to confirm the action respects the equivalence. Here a homotopy $H$ becomes a homotopy $f \circ H$; in quotient groups a coset operation must be representative-independent; in measure theory an a.e.-defined operation must respect null sets. The trigger "this map is defined on classes by a formula on representatives" should fire the reflex "check well-definedness", and it is usually a one-line composition argument.

**Functoriality almost always reduces to associativity of composition.** Notice that the substantive functor axiom $(g \circ f)_* = g_* \circ f_*$ collapsed to the identity $(g \circ f) \circ \gamma = g \circ (f \circ \gamma)$ — pure associativity of composing maps. This is typical: for invariants defined by "post-compose the test object with the map", functoriality is associativity, and for invariants defined by "pre-compose" (contravariant ones), it is again associativity with the order reversed. Recognizing that the functor axioms are nearly free once well-definedness is settled lets you verify new functorial invariants quickly: the real content is the well-definedness, the functoriality is bookkeeping.
