---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Integral Closure and Normal Domain"
  - "Def - The Induced Map on Spectra"
  - "Def - Lying Over, Going Up, Going Down"
  - "Def - Prime and Maximal Ideal"
  - "Def - Field of Fractions"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]] of *integral domains*, with $A$ **[[Def - Integral Closure and Normal Domain|integrally closed]]** in $K = \operatorname{Frac} A$. Primes of $A$: $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$; primes of $B$: $\mathfrak{q}_1, \mathfrak{q}_2$. For $\mathfrak{q}_1 \in \operatorname{Spec} B$, $B_{\mathfrak{q}_1} = (B \setminus \mathfrak{q}_1)^{-1}B$ is the localization of $B$ at the prime $\mathfrak{q}_1$ (a genuine local ring of $B$). For an ideal $\mathfrak{a} \trianglelefteq A$, $\sqrt{\mathfrak{a}B}$ is the radical of the extended ideal; the **integral closure of $\mathfrak{a}$ in $B$** (the set of $b \in B$ integral over $\mathfrak{a}$, meaning $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ with $a_i \in \mathfrak{a}$) equals $\sqrt{\mathfrak{a}B}$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

---

# Statement

> **Theorem (Going Down).** Let $A \subseteq B$ be an integral extension of integral domains with $A$ integrally closed in its field of fractions. Let $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ be primes of $A$ and $\mathfrak{q}_1 \in \operatorname{Spec} B$ a prime lying over $\mathfrak{p}_1$ (that is, $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$). Then there exists $\mathfrak{q}_2 \in \operatorname{Spec} B$ with
> $$\mathfrak{q}_2 \subseteq \mathfrak{q}_1 \qquad \text{and} \qquad \mathfrak{q}_2 \cap A = \mathfrak{p}_2.$$

> **Sharpness.** The hypothesis that $A$ is integrally closed is essential: without it, going down can fail (see [[Ex - Going down can fail without normality]]).

---

# Motivation

Going down is the mirror image of [[Thm - Going Up|going up]] — it lifts an inclusion of base primes *downward* rather than upward — but it is a fundamentally different theorem, because it can *fail*. [[Thm - Lying Over|Lying over]], going up, and [[Thm - Incomparability|incomparability]] hold for every integral extension with no hypothesis on the rings. Going down demands that the base $A$ be an [[Def - Integral Closure and Normal Domain|integrally closed domain]] — normal — and the demand is not a convenience of the proof: a non-normal $A$ genuinely permits going down to fail, as the "two lines glued at a point" example shows. So this theorem is where normality earns its keep in the dimension theory of varieties.

Geometrically, going down is the statement that a finite map onto a normal base does not let fibre dimension *jump* as you specialise. Going up follows a base point as it specialises (moves to a more special point); going down follows it as it *generises* (moves to a more generic point), starting from a chosen preimage of the special point and finding a preimage of the generic point below it. For a normal base this is always possible — the geometry over a normal variety is "equidimensional", no component of a fibre suddenly appears or grows. For a non-normal base the gluing of branches can trap a chosen preimage so that no preimage of the generic point lies below it, and going down breaks.

The importance is the *catenary* dimension formula. To prove that all maximal chains of primes in a finitely generated $k$-domain have the same length — equivalently $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$, codimension plus dimension equals ambient dimension — one Noether-normalizes to a polynomial ring (which is normal) and transports chains across the integral extension, splicing a chain *below* $\mathfrak{p}$ to a chain *above* it using going down. Without going down one gets $\dim A = \dim B$ (which needs only the other three theorems) but not the finer statement about the *position* of an intermediate prime. Going down is the theorem of fine dimension, not gross dimension.

Why should normality make downward lifting possible? The proof shows that $\mathfrak{p}_2$ is *contracted* from the localization $B_{\mathfrak{q}_1}$ — i.e. $\mathfrak{p}_2 = (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A$ — and then $\mathfrak{q}_2 := (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap B$ does the job. The only hard inclusion is $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$, and it is here that normality enters: an element of $\sqrt{\mathfrak{p}_2 B}$ is integral over $\mathfrak{p}_2$, so by normality its minimal polynomial over $K = \operatorname{Frac} A$ has all *non-leading* coefficients in $\mathfrak{p}_2$. This control over minimal polynomials — available *only* when $A$ is integrally closed — is the entire mechanism.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A \subseteq B$ integral, *both domains*, $A$ integrally closed, plus a descending base inclusion $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ and a prime $\mathfrak{q}_1$ over $\mathfrak{p}_1$".

The first disguised source is **a polynomial ring or any UFD as base**: a [[Thm - Principal Ideal Domains are Unique Factorization Domains|UFD is integrally closed]], so whenever $A = k[X_1,\dots,X_n]$ (or any UFD) sits integrally inside $B$, going down is available. *Example problem:* transporting a chain across the integral extension $k[X_1,\dots,X_d] \subseteq A$ from Noether normalization, where the polynomial ring is the normal base.

The second disguised source is **the ring of integers of a number field as base**: $\mathcal{O}_K$ is integrally closed (it is the integral closure of $\mathbb{Z}$ in $K$). So for a further integral extension $\mathcal{O}_K \subseteq B$, going down applies. *Example problem:* lifting prime divisibility relations downward in a tower of number rings, where each base is normal.

The third disguised source is **a flat extension**, where going down holds *without* normality. Although this theorem is stated for normal $A$, the *conclusion* (going down) also follows from flatness of $A \to B$; recognising flatness as an alternative route broadens when going down is usable. *Example problem:* a localization or a free extension automatically goes down, no normality check needed.

**Targets (Output Amplification)**

The conclusion is "$\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$".

Combine going down with **[[Thm - Going Up|going up]]** to splice a chain *through* a prescribed prime $\mathfrak{p}$. Going down builds the part of the chain below $\mathfrak{p}$, going up the part above; together they realise a full chain in $B$ over a full chain in $A$ passing through $\mathfrak{p}$. The result $E$ is the catenary formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$.

Combine going down with **[[Thm - Incomparability|incomparability]]** to get *strictness* of the descending lift. Going down gives $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$; incomparability (distinct contractions $\mathfrak{p}_2 \neq \mathfrak{p}_1$) forces $\mathfrak{q}_2 \subsetneq \mathfrak{q}_1$. The result $E$ is that descending chains lift to descending chains of the same length.

Combine going down with **the height interpretation $\operatorname{ht}\mathfrak{q} = \dim B_{\mathfrak{q}}$**. Going down lets a chain below $\mathfrak{p}_1$ lift below $\mathfrak{q}_1$, so $\operatorname{ht}\mathfrak{q}_1 \geq \operatorname{ht}\mathfrak{p}_1$; with incomparability giving the reverse, $\operatorname{ht}\mathfrak{q}_1 = \operatorname{ht}(\mathfrak{q}_1 \cap A)$. The result $E$: height is preserved by contraction along an integral extension of a normal domain.

---

# Why Is It True

The strategy is to find $\mathfrak{q}_2$ as a *contraction from a localization*. Localize $B$ at $\mathfrak{q}_1$: the localization map $B \to B_{\mathfrak{q}_1}$ is injective ($B$ is a domain). Consider the extended ideal $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ and its contraction $\mathfrak{q}_2 := (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap B$. By construction $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ (the contraction of any prime of $B_{\mathfrak{q}_1}$ along $B \to B_{\mathfrak{q}_1}$ lands inside $\mathfrak{q}_1$, since $B_{\mathfrak{q}_1}$ inverts exactly $B \setminus \mathfrak{q}_1$), and $\mathfrak{q}_2$ contracts to $\mathfrak{p}_2$ in $A$ *provided* $\mathfrak{p}_2$ is itself contracted from $B_{\mathfrak{q}_1}$ — that is, provided $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A = \mathfrak{p}_2$. The inclusion $\supseteq$ is automatic; the content is $\subseteq$:
$$(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2.$$

To prove it, take $y/s \in (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A$ with $y \in \mathfrak{p}_2 B$ and $s \in B \setminus \mathfrak{q}_1$ (every element of $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ has this form). The integral closure of $\mathfrak{p}_2$ in $B$ is $\sqrt{\mathfrak{p}_2 B}$, so $y \in \mathfrak{p}_2 B$ means $y$ is *integral over the ideal $\mathfrak{p}_2$*: it satisfies a monic equation with non-leading coefficients in $\mathfrak{p}_2$. **Here is where normality fires.** Since $A$ is integrally closed, the *minimal* polynomial of $y$ over $K = \operatorname{Frac} A$ already has all its non-leading coefficients in $\mathfrak{p}_2$:
$$y^r + u_1 y^{r-1} + \cdots + u_r = 0, \qquad u_1, \dots, u_r \in \mathfrak{p}_2.$$
Now write $y = (y/s) \cdot s$ with $y/s \in A$ (it lies in $A$ by assumption) and $s \in B$. The minimal polynomial of $s = y/(y/s)$ over $K$ is obtained from that of $y$ by scaling: dividing the equation for $y$ by $(y/s)^r$ gives the minimal equation for $s$,
$$s^r + \underbrace{(s/y)\,u_1}_{}\, s^{r-1} + \cdots + (s/y)^r u_r = 0, \qquad \text{coefficients } (s/y)^i u_i \in K.$$
But $s \in B$ is integral over $A$, and $A$ is integrally closed, so the coefficients $(s/y)^i u_i$ of $s$'s minimal polynomial lie in $A$. **Suppose, for contradiction, $y/s \notin \mathfrak{p}_2$.** Then from $u_i = (y/s)^i \big((s/y)^i u_i\big)$ with $u_i \in \mathfrak{p}_2$, $(y/s)^i \notin \mathfrak{p}_2$, and $(s/y)^i u_i \in A$, primeness of $\mathfrak{p}_2$ forces $(s/y)^i u_i \in \mathfrak{p}_2$ for each $i$. Plugging into the scaled equation, $s^r = -\sum_i (s/y)^i u_i\, s^{r-i} \in \mathfrak{p}_2 B \subseteq \mathfrak{p}_1 B = (\mathfrak{q}_1 \cap A)B \subseteq \mathfrak{q}_1$, so $s^r \in \mathfrak{q}_1$, hence $s \in \mathfrak{q}_1$ — contradicting $s \in B \setminus \mathfrak{q}_1$. Therefore $y/s \in \mathfrak{p}_2$, proving the inclusion.

**The mechanism in one line: normality forces the minimal polynomial of an element of $\sqrt{\mathfrak{p}_2 B}$ to have coefficients in $\mathfrak{p}_2$, and scaling that polynomial across to $s$ shows that if the contracted element escaped $\mathfrak{p}_2$, then $s$ would fall into $\mathfrak{q}_1$ — impossible.** Strip normality away and the minimal polynomial's coefficients need not lie in $\mathfrak{p}_2$, the scaling argument collapses, and $\mathfrak{p}_2$ may fail to be contracted from $B_{\mathfrak{q}_1}$ — which is exactly how the counterexample evades the conclusion.

---

# What Makes This Hard

This is the hardest proof in the chapter, and the difficulty is concentrated in one move: recognising that $\mathfrak{p}_2$ being *contracted from* $B_{\mathfrak{q}_1}$ is the right reformulation, and that the only nontrivial inclusion $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$ is controlled by the *minimal polynomials* of elements of $\sqrt{\mathfrak{p}_2 B}$. The crux step — that for integrally closed $A$, an element integral over the ideal $\mathfrak{p}_2$ has minimal polynomial with non-leading coefficients in $\mathfrak{p}_2$ — is where normality is used and is easy to overlook. The most common error is to assume going down is as free as going up and skip the normality hypothesis entirely; the second is to mishandle the scaling that produces $s$'s minimal polynomial from $y$'s, forgetting that integrality of $s$ plus normality of $A$ is what puts those scaled coefficients back in $A$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build $\mathfrak{q}_2 = (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap B$ inside $\mathfrak{q}_1$; show it contracts to $\mathfrak{p}_2$ by proving $\mathfrak{p}_2$ is contracted from $B_{\mathfrak{q}_1}$, i.e. $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$; the proof of this inclusion runs on normality, which forces the minimal polynomial of $y \in \sqrt{\mathfrak{p}_2 B}$ to have coefficients in $\mathfrak{p}_2$, scaled across to $s$ to derive a contradiction with $s \notin \mathfrak{q}_1$.

**Subgoal decomposition:**

1. **Reduce to: $\mathfrak{p}_2$ is contracted from $B_{\mathfrak{q}_1}$.**
   - *Hint:* If $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A = \mathfrak{p}_2$, set $\mathfrak{q}_2 = (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap B$; then $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.
   - *Why needed:* It turns the existence problem into one ideal-contraction equality.

2. **Prove the only nontrivial inclusion $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$.**
   - *Hint:* Take $y/s$ with $y \in \mathfrak{p}_2 B = \sqrt{\mathfrak{p}_2 B}$'s integral closure, $s \notin \mathfrak{q}_1$; $y$ is integral over $\mathfrak{p}_2$.
   - *Why needed:* This is the whole content of the theorem.

3. **Use normality: minimal polynomial of $y$ has coefficients in $\mathfrak{p}_2$; scale to $s$; contradict $s \notin \mathfrak{q}_1$ if $y/s \notin \mathfrak{p}_2$.**
   - *Hint:* From $y^r + u_1 y^{r-1} + \cdots + u_r = 0$ ($u_i \in \mathfrak{p}_2$), divide by $(y/s)^r$ to get $s$'s minimal equation; integrality of $s$ + normality puts its coefficients in $A$; assume $y/s \notin \mathfrak{p}_2$ to force $s^r \in \mathfrak{q}_1$.
   - *Why needed:* It is the step that fails without normality, and it closes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: The integral closure of an ideal is its radical extension
> **Statement:** For an integral extension $A \subseteq B$ and an ideal $\mathfrak{a} \trianglelefteq A$, the set of $b \in B$ integral over $\mathfrak{a}$ (satisfying a monic equation with non-leading coefficients in $\mathfrak{a}$) equals $\sqrt{\mathfrak{a}B}$.
>
> **Hint:** "$\supseteq$": an element of $\sqrt{\mathfrak{a}B}$ has a power in $\mathfrak{a}B$, giving an integral relation over $\mathfrak{a}$. "$\subseteq$": an integral relation over $\mathfrak{a}$ shows a power lies in $\mathfrak{a}B$.
>
> **Why needed:** It identifies "$y \in \mathfrak{p}_2 B$" with "$y$ integral over $\mathfrak{p}_2$", the starting point of the key step.
>
> > [!note]- Full proof
> > ($\subseteq$) If $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ with $a_i \in \mathfrak{a}$, then $b^n = -(a_1 b^{n-1} + \cdots + a_n) \in \mathfrak{a}B$, so $b \in \sqrt{\mathfrak{a}B}$. ($\supseteq$) Let $b \in \sqrt{\mathfrak{a}B}$, so $b^m \in \mathfrak{a}B$ for some $m$; write $b^m = \sum_j a_j' c_j$ with $a_j' \in \mathfrak{a}$, $c_j \in B$. The $A$-module $M = A[c_1,\dots,c_k]$ (with the $c_j$ from the expression and finitely many integral generators) is finitely generated since $B$ is integral, and $b^m M \subseteq \mathfrak{a}M$; the determinant trick (Cayley–Hamilton with entries in $\mathfrak{a}$) yields a monic equation for $b^m$, hence for $b$, with non-leading coefficients in $\mathfrak{a}$.

> [!note]- Lemma 2: Normality controls the minimal polynomial
> **Statement:** Let $A$ be integrally closed in $K = \operatorname{Frac} A$, $\mathfrak{a} \trianglelefteq A$, and $b$ integral over $\mathfrak{a}$ (lying in a field extension $L \supseteq K$). Then the minimal polynomial of $b$ over $K$ is $T^r + u_1 T^{r-1} + \cdots + u_r$ with all $u_i \in \mathfrak{a}$ (in particular $u_i \in A$).
>
> **Hint:** Over an algebraic closure factor the minimal polynomial; each root is integral over $\mathfrak{a}$, so each coefficient (an elementary symmetric function of the roots) is integral over $\mathfrak{a}$ and lies in $K$, hence in $A$ by normality — and being integral over the ideal $\mathfrak{a}$ means each coefficient lies in $\sqrt{\mathfrak{a}}$, which equals $\mathfrak{a}$ when $\mathfrak{a}$ is prime.
>
> **Why needed:** This is the exact place normality is used; it provides the coefficients $u_i \in \mathfrak{p}_2$ in the main proof.
>
> > [!note]- Full proof
> > Since $b$ is integral over $\mathfrak{a}$, it satisfies $f(b) = 0$ for some monic $f = T^N + a_1 T^{N-1} + \cdots + a_N$ with $a_i \in \mathfrak{a}$. The minimal polynomial $g = T^r + u_1 T^{r-1} + \cdots + u_r$ of $b$ over $K$ divides $f$ in $K[T]$. Fix an algebraic closure $\Omega \supseteq K$ and factor $g = \prod_{i=1}^r (T - \alpha_i)$ with $\alpha_i \in \Omega$. Since $g \mid f$, each root $\alpha_i$ is also a root of $f$, hence satisfies the same monic $\mathfrak{a}$-integral relation $f$, so each $\alpha_i$ is integral over $\mathfrak{a}$. Each coefficient $u_j = \pm e_j(\alpha_1,\dots,\alpha_r)$ is an elementary symmetric polynomial in the $\alpha_i$, hence a sum of products of elements integral over $\mathfrak{a}$, hence itself integral over $\mathfrak{a}$. As $u_j \in K$ and $A$ is integrally closed, $u_j \in A$. Finally, integrality over the ideal $\mathfrak{a}$ gives a relation $u_j^m + c_1 u_j^{m-1} + \cdots + c_m = 0$ with $c_i \in \mathfrak{a}$, so $u_j^m \in \mathfrak{a}$, i.e. $u_j \in \sqrt{\mathfrak{a}}$. When $\mathfrak{a}$ is prime (the case used in the theorem, $\mathfrak{a} = \mathfrak{p}_2$), $\sqrt{\mathfrak{a}} = \mathfrak{a}$, so $u_j \in \mathfrak{a}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be an integral extension of domains, $A$ integrally closed in $K = \operatorname{Frac} A$, $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ in $\operatorname{Spec} A$, and $\mathfrak{q}_1 \in \operatorname{Spec} B$ with $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$.
>
> **Step 0 — the localization $B \to B_{\mathfrak{q}_1}$ is injective.** As $B$ is a domain and $B \setminus \mathfrak{q}_1$ contains no zero-divisors, the localization map is injective; identify $B \subseteq B_{\mathfrak{q}_1}$.
>
> **Step 1 — reduce to a contraction equality.** It suffices to show $\mathfrak{p}_2$ is contracted from $B_{\mathfrak{q}_1}$ along $A \to B \to B_{\mathfrak{q}_1}$, i.e.
> $$(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A = \mathfrak{p}_2.$$
> Granting this equality, a prime $\mathfrak{n}$ of $B_{\mathfrak{q}_1}$ minimal over $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ contracts to $\mathfrak{p}_2$ in $A$ (Step 3), and $\mathfrak{q}_2 := \mathfrak{n} \cap B$ is then a prime of $B$ contained in $\mathfrak{q}_1$ with $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$ — the required prime. (The extended ideal $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ itself need not be prime, which is why we pass to a minimal prime over it.)
>
> The inclusion $\mathfrak{p}_2 \subseteq (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A$ is automatic (extend then contract). We prove the reverse.
>
> **Step 2 — the key inclusion $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$.** Take $x \in (\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A$. Every element of $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ has the form $y/s$ with $y \in \mathfrak{p}_2 B$ and $s \in B \setminus \mathfrak{q}_1$; so $x = y/s$, with $x \in A$.
>
> By Lemma 1, $y \in \mathfrak{p}_2 B = \sqrt{\mathfrak{p}_2 B}$ is integral over the ideal $\mathfrak{p}_2$. By Lemma 2 (using $A$ integrally closed and $\mathfrak{p}_2$ prime), the minimal polynomial of $y$ over $K$ is
> $$y^r + u_1 y^{r-1} + \cdots + u_r = 0, \qquad u_1, \dots, u_r \in \mathfrak{p}_2.$$
> Now $y = x \cdot s$ with $x = y/s \in A \subseteq K$ and $s \in B \subseteq \operatorname{Frac} B$. The minimal polynomial of $s$ over $K$ is obtained by dividing the equation for $y = xs$ by $x^r$:
> $$s^r + \tfrac{u_1}{x}\, s^{r-1} + \cdots + \tfrac{u_r}{x^r} = 0. \qquad (\ast)$$
> Since $s \in B$ is integral over $A$ and $A$ is integrally closed, all coefficients of $s$'s minimal polynomial lie in $A$: $\tfrac{u_i}{x^i} \in A$ for each $i$.
>
> **Suppose $x = y/s \notin \mathfrak{p}_2$.** Then $x^i \notin \mathfrak{p}_2$ for each $i$ (primeness). From $u_i = x^i \cdot \tfrac{u_i}{x^i}$ with $u_i \in \mathfrak{p}_2$, $x^i \notin \mathfrak{p}_2$, and $\tfrac{u_i}{x^i} \in A$, primeness of $\mathfrak{p}_2$ gives $\tfrac{u_i}{x^i} \in \mathfrak{p}_2$ for all $i$. Rearranging $(\ast)$,
> $$s^r = -\sum_{i=1}^r \tfrac{u_i}{x^i}\, s^{r-i} \in \mathfrak{p}_2 B.$$
> Hence
> $$s^r \in \mathfrak{p}_2 B \subseteq \mathfrak{p}_1 B = (\mathfrak{q}_1 \cap A)B \subseteq \mathfrak{q}_1 B \subseteq \mathfrak{q}_1,$$
> so $s^r \in \mathfrak{q}_1$, and as $\mathfrak{q}_1$ is prime, $s \in \mathfrak{q}_1$ — contradicting $s \in B \setminus \mathfrak{q}_1$.
>
> Therefore $x = y/s \in \mathfrak{p}_2$, proving $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A \subseteq \mathfrak{p}_2$, hence equality.
>
> **Step 3 — extract $\mathfrak{q}_2$.** Since $(\mathfrak{p}_2 B_{\mathfrak{q}_1}) \cap A = \mathfrak{p}_2$ is prime, there is a prime $\mathfrak{n}$ of $B_{\mathfrak{q}_1}$ lying over $\mathfrak{p}_2$ with $\mathfrak{n} \subseteq \mathfrak{q}_1 B_{\mathfrak{q}_1}$ (take $\mathfrak{n}$ minimal over $\mathfrak{p}_2 B_{\mathfrak{q}_1}$; its contraction to $A$ is $\supseteq \mathfrak{p}_2$ and $\subseteq (\mathfrak{p}_2 B_{\mathfrak{q}_1})\cap A = \mathfrak{p}_2$, hence $= \mathfrak{p}_2$). Then $\mathfrak{q}_2 := \mathfrak{n} \cap B$ is a prime of $B$ with $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ (as $\mathfrak{n} \subseteq \mathfrak{q}_1 B_{\mathfrak{q}_1}$ contracts into $\mathfrak{q}_1$) and $\mathfrak{q}_2 \cap A = \mathfrak{n} \cap A = \mathfrak{p}_2$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The catenary property of affine varieties.** For a finitely generated $k$-domain $A$, going down (applied across a Noether normalization $k[X_1,\dots,X_d] \subseteq A$, where the polynomial ring is normal) is the key to showing all maximal chains of primes have length $d = \dim A$, equivalently $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$. The application is non-obvious because it is the *position* of $\mathfrak{p}$ in a chain, not just total dimension, that going down controls — and dimension equality alone (the other three theorems) does not give it.

**Why normalization is needed in resolution and intersection theory.** A non-normal variety can have a finite map to it that fails going down — the "two lines glued at a point" — and this is precisely the local obstruction that *normalization* removes. The application is non-obvious because it reframes the geometric operation "normalize a variety" as "make going down hold", linking a singularity-resolution step to a prime-lifting property.

**Height is preserved under integral extension of a normal domain.** Combining going down (chains below $\mathfrak{p}_1$ lift below $\mathfrak{q}_1$) with incomparability (the reverse), one gets $\operatorname{ht}\mathfrak{q}_1 = \operatorname{ht}(\mathfrak{q}_1 \cap A)$ for $A$ normal. The application is non-obvious because height is a *local* codimension, and its preservation across a finite map is exactly what makes the codimension of a subvariety well-behaved under finite covers — used throughout the dimension theory of [[Commutative Algebra XII — Dimension Theory|schemes]].

---

# Bridges

- **[[Thm - Going Up|Going Up]]** — going down is the mirror of going up (descending vs ascending chain lifting), but with a crucial asymmetry: going up is free, going down needs normality. The two are *spliced* in the proof of the catenary formula — going up builds the chain above a prime $\mathfrak{p}$, going down the chain below it — so together they realise a full chain through $\mathfrak{p}$.

- **[[Def - Integral Closure and Normal Domain|Integral Closure and Normal Domain]]** — normality is the precise hypothesis going down needs, and Lemma 2 is exactly where it is used: an [[Def - Integral Closure and Normal Domain|integrally closed domain]] is one where elements of $K$ integral over $A$ already lie in $A$, which forces the minimal-polynomial coefficients into $A$ (and into $\mathfrak{p}_2$). The failure of going down is the failure of this control, visible in the non-normal counterexample.

- **[[Thm - A UFD is Integrally Closed|A UFD is Integrally Closed]]** — this is the standard supply of normal bases: every UFD (in particular every polynomial ring $k[X_1,\dots,X_n]$ and every PID) is integrally closed, so going down applies with such a base. It is why Noether normalization, which lands in a polynomial ring, pairs so well with going down.

- **[[Def - Lying Over, Going Up, Going Down|Flat maps go down]]** — there is a second, orthogonal sufficient condition: a *flat* ring map satisfies going down with no normality hypothesis. Localizations and free extensions are flat, so they go down automatically. Normality and flatness are the two classical routes to going down, and recognising which is present is the first decision when downward lifting is wanted.

---

# Unlocked by This

> [!tip] Equidimensionality and the dimension formula *(from Algebraic Geometry)*
> Going down is the algebra of *no fibre-dimension jumping* over a normal base — the **equidimensionality** of finite (and flat) families. Its downstream payoff is the **dimension formula** $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ for a finitely generated $k$-domain: the dimension of a subvariety plus its codimension equals the dimension of the ambient variety. This catenary property, developed fully in [[Commutative Algebra XII — Dimension Theory|the dimension chapter]], is what makes codimension a well-behaved invariant on normal varieties and **schemes**, and going down is its engine.

> [!tip] Normalization as the cure for going-down failure *(from Algebraic Geometry)*
> The failure of going down on a non-normal base is *exactly* the local pathology that **normalization** removes: passing from a variety to its normalization replaces the base by an integrally closed ring, restoring going down. This is why normal varieties are the natural setting for the dimension theory of finite maps, and why the "two lines glued at a point" — a non-normal curve — is the canonical picture of going-down failure.
