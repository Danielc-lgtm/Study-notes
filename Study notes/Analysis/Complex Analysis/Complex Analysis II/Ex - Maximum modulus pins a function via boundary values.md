---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - (Global) Maximum Modulus Principle"
  - "Thm - Local Maximum Modulus Principle"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $D = \{z \in \mathbb{C} : |z| < 1\}$ be the open unit disc, $\bar D = \{|z| \leq 1\}$ its closure, and $\partial D = \{|z| = 1\}$ its boundary circle. Suppose $f : \bar D \to \mathbb{C}$ satisfies:

1. $f$ is holomorphic on $D$;
2. $f$ is continuous on $\bar D$;
3. $|f(z)| = 1$ for every $z \in \partial D$;
4. $f(0) = 1$.

Show that $f \equiv 1$ on $\bar D$ — that is, $f$ is identically equal to the constant function $1$.

The strategy is a *two-sided squeeze* by the maximum modulus principle: apply it to $f$ to get $|f| \leq 1$ on $\bar D$, then apply it to $1/f$ (which is well-defined because $f$ has no zeros on $\bar D$, by a separate argument) to get $|f| \geq 1$ on $\bar D$. Conclude $|f| \equiv 1$, then deduce constancy and identify the constant.

**Recall:**

![[Thm - (Global) Maximum Modulus Principle#Statement]]

A **holomorphic** function on an open set is a complex differentiable function; on a connected open set, it is determined by its values on any set with an accumulation point (the [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)|identity theorem]]). The maximum modulus principle has *two* forms in the chapter — the *local* form (a holomorphic $f$ on $D(a, r)$ with $|f|$ achieving a local maximum at $a$ is constant on $D(a, r)$) and the *global* form (on a bounded domain $\Omega$ with $f$ holomorphic on $\Omega$ and continuous on $\bar\Omega$, $\max_{\bar\Omega}|f| = \max_{\partial\Omega}|f|$). The global form is what this exercise leans on.

---

# Convergent Strategy

**Problem class.** This is a *pin-the-function* problem, the cleanest example of how the maximum modulus principle constrains an entire holomorphic function from limited boundary information. The class is identified by the prompt "boundary information + interior point information" together with the conclusion "$f$ is determined." The standard reusable shape is: *given $|f| \equiv 1$ on the boundary of a bounded domain and one interior value, the maximum modulus principle on $f$ and on $1/f$ forces $|f| \equiv 1$, from which one further argument extracts the actual value.* The trigger is the *equality* boundary condition $|f| = 1$ — *equality*, not just an upper bound — because equality opens the door to applying max modulus *twice*, once for $f$ and once for $1/f$.

**Assumption pattern.** Three features are essential. First, the boundary condition is an *equality* $|f| = 1$, not just $|f| \leq 1$ — this is what makes the lower bound $|f| \geq 1$ available via $1/f$, in addition to the upper bound $|f| \leq 1$ via $f$. Second, $f(0) = 1$ is *both* a value (not just a modulus) — this is what lets us identify the constant once we know $f$ is constant. Third, the domain is the closed *unit disc* — bounded, with non-empty interior, so both the local and global forms of max modulus apply. The trichotomy "equality on boundary + interior value + bounded domain" is the signature of this exercise class.

**Theorem routing.** The route is a four-step squeeze. (a) Apply the [[Thm - (Global) Maximum Modulus Principle|max modulus principle]] to $f$: $\max_{\bar D}|f| = \max_{\partial D}|f| = 1$, so $|f| \leq 1$ on $\bar D$. (b) Argue $f$ has no zeros on $D$: any zero would, by continuity, force $f(0)$ to be small — but $f(0) = 1$ is far from any zero locally — *however*, this argument requires more care, since zeros could be anywhere; the cleaner argument is to note that $|f| \leq 1$ in $D$ together with $f(0) = 1$ means $|f(0)| = 1$ is the *maximum value* attained, so by the *local* max modulus principle $f$ is constant on a neighbourhood of $0$ — and then by the identity theorem on the connected $D$, $f$ is constant on $D$, with the constant being $1$. The argument actually terminates here without needing $1/f$ at all! (c) The alternative route: apply max modulus to $1/f$ to get $|f| \geq 1$, conclude $|f| \equiv 1$, then conclude $f$ is constant by the *local* max modulus principle. Both routes work. (d) Identify the constant: $f(0) = 1$ pins it.

**Key decision point.** The crux is recognising that $f(0) = 1$ with $|f| \leq 1$ on $\bar D$ means $|f|$ attains its *maximum* (which is $1$) *at an interior point* (the centre $0$). The [[Thm - (Global) Maximum Modulus Principle|global max modulus principle]] is then applicable in its *strong* form: if the maximum of $|f|$ on $\bar\Omega$ is attained at an interior point, $f$ is constant. This is the decisive collapse: the two pieces of information "boundary modulus $= 1$" and "interior value $f(0) = 1$" together force $f$ to be the constant $1$ in a single application of max modulus — no need for the $1/f$ argument at all. The alternative $1/f$ argument is a *check* (it gives $|f| \equiv 1$, from which constancy follows by a separate route) but is not the most direct path. Recognising "interior maximum $\Rightarrow$ constant" as a single move is the lesson.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Complex Analysis II — Cauchy's Theorem and its Consequences#Legal Operations|the topic page's Legal Operations]]:

1. **Apply max modulus to pin a function via boundary values** (operation 8 from the topic page). The global max modulus principle says $\max_{\bar D}|f| = \max_{\partial D}|f| = 1$, hence $|f| \leq 1$ on $\bar D$. Combined with $f(0) = 1$, the maximum of $|f|$ is attained at the interior point $0$, so by the strong form of max modulus $f$ is constant. This is the *signature* application of max modulus and the canonical trigger for the entire technique.

2. **Apply max modulus to $1/f$** (operation 8, again, after a domain-of-definition check). When $f$ has no zeros, $1/f$ is holomorphic, and applying max modulus to $1/f$ gives a *lower* bound on $|f|$ — symmetrically to the upper bound from $f$. The combined upper-and-lower-bound argument gives $|f| \equiv 1$ on $\bar D$. This is the *alternative* route alluded to in the problem statement; it gives a different proof of the same conclusion.

3. **Use Liouville-type constancy from a single value** (operation 5 from the topic page, in spirit). Once $f$ is known to be constant on the connected $\bar D$, evaluating at any point identifies the constant. $f(0) = 1$ gives the constant value $1$, so $f \equiv 1$ on $\bar D$.

---

# Hints

> [!note]- Hint 1
> Apply the [[Thm - (Global) Maximum Modulus Principle|max modulus principle]] to $f$ on the closed disc $\bar D$: $\max_{\bar D}|f| = \max_{\partial D}|f|$. The hypothesis $|f| = 1$ on $\partial D$ gives $\max_{\partial D}|f| = 1$, so $|f(z)| \leq 1$ for every $z \in \bar D$.

> [!note]- Hint 2
> Now use $f(0) = 1$ together with $|f| \leq 1$. The value $|f(0)| = 1$ equals the maximum of $|f|$ on $\bar D$. So $|f|$ attains its maximum at the *interior* point $0$.

> [!note]- Hint 3
> By the *strong* form of the max modulus principle: if a non-constant holomorphic function on a domain attains a local maximum of $|f|$ in the interior, that is a contradiction. Equivalently: a holomorphic function attaining its maximum modulus on the interior is constant.

> [!note]- Hint 4
> Apply the strong form: $f$ is constant on $D$, hence (by continuity) on $\bar D$. Evaluate at $0$ to identify the constant: $f(0) = 1$, so $f \equiv 1$.

> [!note]- Hint 5 (alternative route)
> Without using the strong form of max modulus, do the following. Since $|f| = 1$ on $\partial D$, $f$ has no zeros on $\partial D$. If $f$ had a zero in $D$, the open-mapping theorem (or a direct argument) would give a contradiction — but more cleanly: $|f(0)| = 1 \neq 0$, so $0$ is not a zero, and once we know $|f|$ attains its max at $0$, the local max modulus principle on a small disc around $0$ gives $f$ constant on a neighbourhood; the identity theorem extends to all of $D$. Either way, $1/f$ is also holomorphic on $D$ (no zeros), with $|1/f| = 1$ on $\partial D$, so $\max_{\bar D}|1/f| = 1$, i.e., $|f| \geq 1$ on $\bar D$. Combined with $|f| \leq 1$, $|f| \equiv 1$ on $\bar D$.

---

# Solution

The plan is to apply the maximum modulus principle as a *two-sided* tool: first the global form on $f$ gives $|f| \leq 1$ on $\bar D$; the additional input $f(0) = 1$ then makes the maximum of $|f|$ attained at the interior point $0$, whence the strong form of max modulus pins $f$ as a constant. The final identification of the constant uses $f(0) = 1$.

**Step 1: $|f| \leq 1$ on $\bar D$.**

By the [[Thm - (Global) Maximum Modulus Principle|global max modulus principle]],
$$\max_{\bar D}|f| \;=\; \max_{\partial D}|f| \;=\; 1.$$
Hence $|f(z)| \leq 1$ for every $z \in \bar D$.

> [!note]- Derivation
> The hypothesis is that $f$ is holomorphic on the bounded domain $D$ and continuous on its closure $\bar D$, with $|f| = 1$ on $\partial D$. The [[Thm - (Global) Maximum Modulus Principle|global max modulus principle]] states: for such $f$ on a bounded domain $\Omega$, $\max_{\bar\Omega}|f| = \max_{\partial\Omega}|f|$. Applied here with $\Omega = D$: $\max_{\bar D}|f| = \max_{\partial D}|f|$.
>
> The boundary maximum is computed from the hypothesis: $|f(z)| = 1$ for every $z \in \partial D$, so the supremum is $1$ (in fact every value on $\partial D$ is exactly $1$). Hence $\max_{\bar D}|f| = 1$, i.e., $|f(z)| \leq 1$ for every $z \in \bar D$, with equality possible (and indeed achieved at every boundary point).

**Step 2: $|f(0)| = 1$ is the maximum of $|f|$ on $\bar D$, attained at the interior point $0$.**

The hypothesis $f(0) = 1$ gives $|f(0)| = 1$, which together with Step 1 means $|f|$ attains its maximum at the interior point $0 \in D$.

> [!note]- Derivation
> From the hypothesis, $|f(0)| = |1| = 1$. From Step 1, $|f(z)| \leq 1$ everywhere on $\bar D$, and equality holds at $0$. So $|f|$ attains its supremum on $\bar D$ at the point $0$, which is in the *open* disc $D$ (not on the boundary).
>
> This is the crucial observation: the maximum is attained *in the interior*. The local-form max modulus principle ([[Thm - Local Maximum Modulus Principle]]) now applies.

**Step 3: $f$ is constant on $D$ (hence on $\bar D$).**

By the [[Thm - Local Maximum Modulus Principle|local maximum modulus principle]] applied at $0$: since $|f|$ has a local (in fact global) maximum at $0$ and $f$ is holomorphic on $D(0, 1) = D$, $f$ is constant on $D$. By continuity on $\bar D$, $f$ is constant on $\bar D$.

> [!note]- Derivation
> The [[Thm - Local Maximum Modulus Principle|local max modulus principle]] reads: if $f$ is holomorphic on $D(a, r)$ and $|f|$ attains a local maximum at $a$, then $f$ is constant on $D(a, r)$. Apply this with $a = 0$ and $r = 1$: $f$ is holomorphic on $D = D(0, 1)$, and $|f|$ attains a local maximum at $0$ (it attains the *global* maximum there, which is a fortiori a local maximum). So $f$ is constant on $D$.
>
> By continuity, $f$ is then constant on $\bar D$ — the boundary values of $f$ are limits of the constant value on $D$, hence also that constant.
>
> *Alternative via the identity theorem.* If one is queasy about the local max modulus principle: argue instead that $f$ is constant on a *small* disc $D(0, \varepsilon) \subseteq D$ around $0$ (which the local principle establishes from a *local* max), and then invoke the [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)|identity theorem]] on the connected $D$ to extend the constancy from the small disc to all of $D$. Either route reaches the same conclusion.

**Step 4: Identify the constant: $f \equiv 1$.**

The constant value of $f$ on $\bar D$ is $f(0) = 1$.

> [!note]- Derivation
> $f$ is constant on $\bar D$ (Step 3), so $f(z) = f(0)$ for every $z \in \bar D$. By hypothesis $f(0) = 1$, hence $f(z) = 1$ for every $z \in \bar D$. $\blacksquare$

> [!note]- Complete formal solution
> *Step 1.* By the [[Thm - (Global) Maximum Modulus Principle|global max modulus principle]] applied to the bounded domain $D$ with $f$ holomorphic on $D$ and continuous on $\bar D$:
> $$\max_{\bar D}|f| \;=\; \max_{\partial D}|f| \;=\; 1.$$
> Hence $|f(z)| \leq 1$ for every $z \in \bar D$.
>
> *Step 2.* From the hypothesis, $|f(0)| = |1| = 1$, the maximum value. So $|f|$ attains its maximum at the interior point $0 \in D$.
>
> *Step 3.* By the [[Thm - Local Maximum Modulus Principle|local max modulus principle]] at $0$, $f$ is constant on $D$; by continuity, also on $\bar D$.
>
> *Step 4.* The constant equals $f(0) = 1$, hence $f \equiv 1$ on $\bar D$. $\blacksquare$

> [!note]- Sanity check via $1/f$
> Here is the alternative two-sided-squeeze argument promised in the problem statement. Step 1 gives $|f| \leq 1$ on $\bar D$. To get the lower bound, note that the hypothesis $|f| = 1$ on $\partial D$ forces $f \neq 0$ on $\partial D$; together with $f(0) = 1 \neq 0$ and continuity, one shows (with a little work, e.g., using the [[Thm - Principle of Isolated Zeros|isolated zeros theorem]] applied to $f$ on $D$) that $f$ has no zeros in $D$ at all. Hence $1/f$ is holomorphic on $D$ and continuous on $\bar D$. Apply the global max modulus principle to $1/f$:
> $$\max_{\bar D}|1/f| \;=\; \max_{\partial D}|1/f| \;=\; 1,$$
> hence $|1/f| \leq 1$ on $\bar D$, i.e., $|f| \geq 1$ on $\bar D$.
>
> Combined: $|f| \equiv 1$ on $\bar D$. A holomorphic function with constant modulus on a domain is constant (by the open-mapping theorem, or by a direct application of the local max modulus principle). The constant is $f(0) = 1$.
>
> This alternative route is a useful *check* and reveals the symmetric role of $f$ and $1/f$ under max modulus, but the direct argument above (using $f(0) = 1$ as the interior maximum) is one step shorter.

> [!warning] Illegal but tempting alternative route
> A tempting move is to try Liouville: "$f$ is bounded on $\bar D$, hence on $D$, so by Liouville $f$ is constant." This is *wrong* — Liouville requires $f$ to be entire (holomorphic on *all* of $\mathbb{C}$), not just on the unit disc. A function holomorphic on the disc and bounded on the disc need *not* be constant: $f(z) = z$ is holomorphic on $D$, bounded by $1$ on $D$, and not constant. The correct tool for "bounded holomorphic on a *disc*" is the max modulus principle (which gives interior-vs-boundary information), not Liouville (which gives constancy from boundedness on the *whole plane*). This distinction is precise: Liouville lives on $\mathbb{C}$; max modulus lives on bounded domains. Confusing the two is one of the most common errors in §2.4.

---

# Key Takeaways

**Interior maximum is the universal trigger for constancy via max modulus.**

The [[Thm - (Global) Maximum Modulus Principle|max modulus principle]] in its strong form says: *a holomorphic function on a domain attaining a local maximum of $|f|$ at an interior point is constant.* This is *the* trigger-reaction pattern of §2.4. The signature in a problem is: a holomorphic $f$ on a bounded domain, a known interior value, and the deduction that this interior value happens to equal the maximum of $|f|$ on the closure. From these three pieces, max modulus immediately collapses $f$ to a constant. In the present exercise, the signature is "(i) $|f| = 1$ on the boundary (forcing $|f| \leq 1$ inside), (ii) $f(0) = 1$ (an interior value of modulus $1$)" — together identifying $|f(0)|$ as the maximum modulus attained on the closed disc, hence interior max, hence constant. The reusable diagnostic is: whenever you encounter a holomorphic function with an explicit boundary modulus bound and an interior value attaining that bound, max modulus pins the function to a constant in one move.

**The two-sided squeeze with $f$ and $1/f$ is the deeper way max modulus controls a function.**

The "alternative route" via $1/f$ illustrates a more general technique: when $f$ has no zeros on a domain, *both* $f$ and $1/f$ are holomorphic, and applying max modulus to both gives a *two-sided* bound on $|f|$. If the boundary values satisfy $|f| \equiv c$ for a constant $c$, then $\max_{\bar D}|f| = c$ and $\max_{\bar D}|1/f| = 1/c$ together force $|f| \leq c$ and $|f| \geq c$, i.e., $|f| \equiv c$ identically. A holomorphic function with constant modulus is then constant (by the Cauchy–Riemann equations: $|f|^2 = f\bar f$ constant forces $\bar f$ to be a function of $f$, which is only possible if $f$ is constant). This two-sided technique is the engine of the **Schwarz lemma** in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]] (where the disc is mapped to itself with $f(0) = 0$, and max modulus on $f(z)/z$ gives $|f(z)| \leq |z|$), and of automorphism characterisations of the disc and the upper half-plane. The reusable trigger is: *if the boundary modulus is a constant $c$ and $f$ has no zeros, expect $|f| \equiv c$ in the interior, and try max modulus on $f$ and $1/f$ together.*

**Distinguish max modulus from Liouville: domain matters.**

Both [[Thm - Liouville's Theorem|Liouville]] and [[Thm - (Global) Maximum Modulus Principle|max modulus]] conclude "$f$ is constant" from a size constraint on $f$, but they apply on different domains. Liouville requires $f$ entire (holomorphic on $\mathbb{C}$) and bounded; max modulus requires $f$ holomorphic on a *bounded* domain with the modulus controlled on the *boundary*. The trigger structure is different: Liouville is "uniform boundedness on the whole plane," max modulus is "boundary modulus controlled, plus interior value attaining it." Mixing them up (e.g., trying Liouville on a function only known holomorphic on a disc) is one of the most common conceptual errors, and the present exercise is the canonical setting where the *correct* tool is max modulus, not Liouville. A clean mental separation: *Liouville for entire-and-bounded; max modulus for bounded-domain-and-boundary-controlled.*

**Cross-link to companion exercises and downstream uses.**

The Schwarz lemma (a downstream §2.4-adjacent result, used in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]]) is the direct generalisation of this exercise: instead of $|f| = 1$ on $\partial D$ and $f(0) = 1$, one assumes $|f| \leq 1$ on $D$ (i.e., $f$ maps $D$ into itself) and $f(0) = 0$, and concludes $|f(z)| \leq |z|$ and $|f'(0)| \leq 1$. The proof applies max modulus to $f(z)/z$ on $\bar D$. The pattern of the present exercise — "interior-attained-maximum forces constancy" — is the engine, and the Schwarz lemma is the next refinement. See also [[Ex - Liouville for harmonic functions]] for the harmonic-function analogue of max-modulus-as-rigidity, and [[Ex - Cauchy estimates bound the growth of an entire function]] for a different growth-controls-structure argument in the same chapter.
