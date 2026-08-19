---
type: definition
subject: probability-geometry
prereqs:
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Section 6.1 (opening)"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\Gamma \subset \mathrm{PSL}(2,\mathbb{R})$ a discrete torsion-free subgroup.
- $\mathcal{P}_X$ — the set of oriented primitive closed geodesics on $X$; $\gamma \in \mathcal{P}_X$ has length $\ell_\gamma > 0$.
- $C_X(\gamma^m)$ — the free homotopy class of loops winding $m \ge 1$ times around $\gamma$.
- $\kappa > 0$ the killing rate, $s := \tfrac12 + \sqrt{\tfrac14 + \kappa} \in (1, \infty)$ the spectral parameter (so $\kappa = s(s-1)$). Section 6.1 assumes $\kappa > 0$, equivalently $s > 1$; the $\kappa = 0$ case uses §5's renormalisation.
- $\mu^\kappa_X(C_X(\gamma^m))$ — the killed loop-measure mass of the class, given in closed form by $\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ (§3.1.2).
- $Z_X(s) = \prod_{\gamma\in\mathcal P_X}\prod_{k\ge 0}(1 - e^{-(s+k)\ell_\gamma})$ — the Selberg zeta function; $F(s) := -\log Z_X(s)$ the total killed mass.
- $L := m\ell_\gamma$ — the geodesic length attached to the class $C_X(\gamma^m)$, viewed as a random variable on the probability space of classes.
- $\ell_{\mathrm{sys}} := \min_{\gamma \in \mathcal{P}_X}\ell_\gamma$ the *systole* (shortest primitive geodesic length); $N_{\mathrm{sys}} := \#\{\gamma \in \mathcal P_X : \ell_\gamma = \ell_{\mathrm{sys}}\} \ge 2$ its multiplicity.
- $\mathbb{P}_s, \mathbb{E}_s, \operatorname{Var}_s$ — probability, expectation, variance under the measure defined below.

> [!recall]- Free homotopy class $C_X(\gamma^m)$ on $X$
> **Formally:** two oriented closed curves on $X$ are *freely homotopic* if one continuously deforms into the other on $X$ with the basepoint allowed to move. The set of free homotopy classes is in bijection with the set of conjugacy classes of $\Gamma$; the class $C_X(\gamma^m)$ corresponds to the conjugacy class of $\tau^m \in \Gamma$, where $\tau$ is a primitive hyperbolic element with translation length $\ell_\gamma$. Winding around $\gamma$ once gives $C_X(\gamma)$; winding $m$ times gives $C_X(\gamma^m)$.
> **In words:** every loop on the surface goes around some collection of holes in some pattern; two loops going around the same holes in the same pattern belong to one class. The class $C_X(\gamma^m)$ is "the taut loop $\gamma$, traversed $m$ times". The countable index set of the probability measure below is exactly these classes: pairs $(\gamma, m)$ with $\gamma$ a primitive geodesic and $m \ge 1$.
> **Concretely:** on the torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ (a flat surrogate), $\Gamma = \mathbb{Z}^2$ is abelian, so free homotopy classes are in bijection with $\mathbb{Z}^2$: the class of $(a, b)$ is "$a$ times horizontally, $b$ times vertically". On a hyperbolic surface — say a closed genus-$2$ pretzel — $\Gamma$ is non-abelian and classes are indexed by pairs $(\gamma, m)$ where $\gamma$ picks one of the infinitely many primitive closed geodesics and $m \ge 1$ counts iterations. Full detail: [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

> [!recall]- Killed loop-measure mass $\mu^\kappa_X(C_X(\gamma^m))$
> **Formally:** for the Brownian loop measure on $X$ with killing at rate $\kappa \ge 0$, the mass of the free homotopy class $C_X(\gamma^m)$ is
> $$\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},\qquad s = \tfrac12 + \sqrt{\tfrac14 + \kappa},$$
> a positive real number depending only on the geodesic length $\ell_\gamma$, the winding $m$, and the spectral parameter $s$. (Derivation: apply Theorem 3.5 with Bernstein function $\phi(\lambda) = \lambda + \kappa$.)
> **In words:** a single number attached to each topological class, telling you how much "loop-measure weight" the class carries. Longer classes ($L = m\ell_\gamma$ large) get exponentially suppressed weight $\propto e^{-sL}$; the parameter $s$ controls how heavily the suppression penalises length. Summed over all classes the total is finite (Corollary 4.3) and equals $-\log Z_X(s)$, which is what makes normalisation to a probability measure possible.
> **Concretely:** on an infinite-area surface with a single closed geodesic of length $\ell = \log 2$ and $\kappa = 0$ (so $s = 1$), the mass of the once-wound class $C_X(\gamma)$ is $\frac11\cdot\frac{e^0}{e^{\log 2}-1} = \frac{1}{2-1} = 1$; the twice-wound class $C_X(\gamma^2)$ has mass $\frac12\cdot\frac{1}{e^{2\log 2}-1} = \frac12\cdot\frac13 = \frac16$; the iterates decay geometrically. Full derivation: [[Thm - Mass of a Subordinate Brownian Loop Class]].

> [!recall]- Selberg zeta function $Z_X(s)$ and $F(s) = -\log Z_X(s)$
> **Formally:** $Z_X(s) := \prod_{\gamma \in \mathcal P_X}\prod_{k \ge 0}(1 - e^{-(s+k)\ell_\gamma})$, absolutely convergent for $\operatorname{Re}s > \delta$ (the critical exponent of $\Gamma$) and meromorphically continued to $\mathbb{C}$. Its logarithm expands as $-\log Z_X(s) = \sum_{\gamma, m \ge 1}\frac{1}{m}\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$, term-by-term equal to the sum of killed loop masses over all $(\gamma, m)$. Write $F(s) := -\log Z_X(s) > 0$ (positive because it is a sum of positive masses).
> **In words:** an analytic generating function assembled from the whole length spectrum, playing for closed geodesics the role Riemann zeta plays for primes. Its numerical *value* at $s = \tfrac12 + \sqrt{\tfrac14 + \kappa}$ is the total mass of killed loops; its *derivatives* generate the moments of the length random variable $L$ under the probability measure below. For $s > \delta$ the value is finite and positive.
> **Concretely:** for a toy surface $X$ with just one primitive geodesic of length $\ell = 1$, $Z_X(s) = \prod_{k \ge 0}(1 - e^{-(s+k)})$; at $s = 2$, $Z_X(2) = (1-e^{-2})(1-e^{-3})(1-e^{-4})\cdots \approx 0.865\cdot 0.950\cdot 0.982\cdots \approx 0.774$, so $F(2) = -\log 0.774 \approx 0.257$; each factor is closer to $1$ as $k$ grows, so the product converges. Full detail: [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

---

# Statement

> **Definition (probability measure on free homotopy classes; Belyaev–Huseynli §6.1).** Let $X = \Gamma\backslash\mathbb{H}^2$ be a geometrically finite hyperbolic surface, $\kappa > 0$, and $s = \tfrac12 + \sqrt{\tfrac14 + \kappa}$ (so $s > 1$). The *probability measure on free homotopy classes* is
> $$\mathbb{P}_s\big(C_X(\gamma^m)\big) := \frac{\mu^\kappa_X(C_X(\gamma^m))}{-\log Z_X(s)} = \frac{\mu^\kappa_X(C_X(\gamma^m))}{\displaystyle\sum_{\gamma' \in \mathcal P_X}\sum_{m' \ge 1}\mu^\kappa_X(C_X((\gamma')^{m'}))},\qquad \gamma \in \mathcal P_X,\ m \ge 1.$$
> Each class $C_X(\gamma^m)$ carries a weight proportional to its killed-loop mass. The normalising constant $-\log Z_X(s)$ is finite and positive for $s > \delta$ ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]); since $\kappa > 0$ implies $s > 1 \ge \delta$, the measure is well-defined on every such $X$.

---

# In One Line

Normalise the killed loop mass by its finite total to get an honest probability distribution on topological types, whose moment generating function of the geodesic length $L = m\ell_\gamma$ is a ratio of Selberg zeta values, $\mathbb{E}_s[e^{-rL}] = \log Z_X(s+r)/\log Z_X(s)$ — so every moment falls out of the Selberg zeta and its derivatives.

---

# Motivation and Unpacking

**The natural probability measure attached to random loops.** The mass $\mu^\kappa_X(C_X(\gamma^m))$ is a *number*, telling you how much loop weight the class carries, but a number alone does not answer distributional questions ("what is the probability that a random loop winds around the systole?", "what is the expected geodesic length of a typical class?"). Once the total mass is finite — a fact §4 established as an identity with the Selberg zeta — the loop measure divided by its total *is* a probability distribution on classes, and every function of the class becomes an ordinary random variable. The paper's §6.1 works out this construction and its immediate consequences.

**The intersection-geometry motivation.** The classes carry information the surface's *intersection theory* cares about: for instance, the probability that two independent random classes' geodesic representatives intersect. By weighting each class by an *explicit* function of its length, the measure lets one compute intersection statistics — the same probability-measure trick number theorists use when they weight primes by $\log p$ and normalise.

**The natural random variable is the geodesic length.** Every class $C_X(\gamma^m)$ has a distinguished number attached — the length $L := m\ell_\gamma$ of its taut geodesic representative traced $m$ times. Under $\mathbb{P}_s$ this becomes a random variable, and its distribution has an especially clean structure: shifting the spectral parameter $s \mapsto s + r$ *tilts* the measure by $e^{-rL}$, because the mass formula depends on $s$ only through the factor $e^{(1-s)m\ell_\gamma} = e^{(1-s)L}$. That tilt-by-length identity is the whole reason moments are so accessible.

**Concretely.** On an infinite-area surface with one primitive geodesic of length $\ell = \log 2$ and $\kappa$ chosen so $s = 2$ (i.e. $\kappa = s(s-1) = 2$), the class masses are $\mu^\kappa(C_X(\gamma^m)) = \frac1m\cdot\frac{e^{-m\log 2}}{e^{m\log 2}-1} = \frac{2^{-m}}{m(2^m - 1)}$: $1/2$ for $m=1$, $1/24$ for $m=2$, $1/168$ for $m=3$, …; the normalising total is $F(2) = \sum \frac{2^{-m}}{m(2^m-1)} \approx 0.545$; and $\mathbb{P}_s(C_X(\gamma)) = (1/2)/0.545 \approx 0.917$, $\mathbb{P}_s(C_X(\gamma^2)) \approx 0.076$, etc. Under $\mathbb{P}_s$ the mass concentrates overwhelmingly on the once-wound class — the shortest, which for a single-geodesic surface is the systole.

## Moments and asymptotics

> [!note]- All moments of $L$ from derivatives of $-\log Z_X$
> Write $F(s) := -\log Z_X(s) = \sum_{\gamma, m \ge 1}\mu^\kappa_X(C_X(\gamma^m))$ for the total killed mass. Every $\mu^\kappa_X(C_X(\gamma^m))$ depends on $s$ only through $e^{(1-s)m\ell_\gamma} = e^{(1-s)L}$, so
> $$\frac{d}{ds}\mu^\kappa_X(C_X(\gamma^m)) = -(m\ell_\gamma)\,\mu^\kappa_X(C_X(\gamma^m)) = -L\,\mu^\kappa_X(C_X(\gamma^m)).$$
>
> **Tilt identity (moment generating function).** For $r > 1 - s$,
> $$\mathbb{E}_s\big[e^{-rL}\big] = \frac{\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))\,e^{-r m\ell_\gamma}}{-\log Z_X(s)} = \frac{-\log Z_X(s + r)}{-\log Z_X(s)} = \frac{\log Z_X(s + r)}{\log Z_X(s)},$$
> because $e^{(1-s)m\ell_\gamma}\cdot e^{-r m\ell_\gamma} = e^{(1-(s+r))m\ell_\gamma}$ is exactly the summand at parameter $s + r$. The tilt identity says: *shifting the spectral parameter is the same as tilting the length distribution.*
>
> **All moments.** Differentiating $F(s)$ once in $s$ pulls a factor $-L$ out of every summand; differentiating $n$ times pulls $(-L)^n$. Hence $\sum_{\gamma, m}\mu^\kappa_X(C_X(\gamma^m))L^n = (-1)^n F^{(n)}(s)$, and dividing by $F(s)$ gives
> $$\mathbb{E}_s[L^n] = \frac{(-1)^n F^{(n)}(s)}{F(s)},\qquad n \ge 1.$$
>
> **First two cumulants (derivatives of $\log F$).** By the chain rule,
> $$\mathbb{E}_s[L] = -\frac{d}{ds}\log F(s) = -\frac{F'(s)}{F(s)} = -\frac{Z_X'(s)}{Z_X(s)\log Z_X(s)},$$
> $$\operatorname{Var}_s(L) = \frac{d^2}{ds^2}\log F(s) = \frac{F''(s)F(s) - F'(s)^2}{F(s)^2}.$$
> Since $\operatorname{Var}_s(L) > 0$, $\log F$ is strictly convex on $(1, \infty)$; hence $s \mapsto \mathbb{E}_s[L]$ is strictly decreasing. **More killing shortens the typical class**, as expected.

> [!note]- The systole limit $s \to \infty$
> As $s \to \infty$ the killed-mass weights $\mu^\kappa_X(C_X(\gamma^m)) \sim e^{-s m\ell_\gamma}/m$ are dominated exponentially by the *shortest* term. Two observations pick out the systole.
>
> **Only primitive systolic classes survive.** For any $(\gamma, m)$ with $m \ge 2$ or $\ell_\gamma > \ell_{\mathrm{sys}}$, the exponent $-s m\ell_\gamma$ is more negative than $-s\ell_{\mathrm{sys}}$ by at least $s(\ell_{\mathrm{sys}}(m-1)) \ge s\ell_{\mathrm{sys}}$ (if $m \ge 2$) or $s(\ell_\gamma - \ell_{\mathrm{sys}}) > 0$ (if $\gamma$ is not systolic). All such contributions are exponentially smaller than the leading systolic $m=1$ terms.
>
> **The systole is realised by at least two oriented classes.** In a torsion-free Fuchsian group $\Gamma$, no hyperbolic element is conjugate to its inverse (a standard fact: conjugating $\tau : z \mapsto e^{\ell}z$ to $\tau^{-1} : z \mapsto e^{-\ell}z$ would require an isometry reversing the axis's orientation, which no orientation-preserving Möbius map does; combined with discreteness this excludes it inside $\Gamma$). So the oriented systole and its reverse are two distinct primitive classes, giving $N_{\mathrm{sys}} \ge 2$.
>
> **Consequences.** The measure concentrates uniformly on systolic classes,
> $$\mathbb{P}_s(C_X(\gamma)) \xrightarrow{s \to \infty} \frac{1}{N_{\mathrm{sys}}}\quad (\ell_\gamma = \ell_{\mathrm{sys}}),\qquad \mathbb{P}_s(C_X(\gamma^m)) \xrightarrow{s \to \infty} 0\quad (\text{else}),$$
> and the mean length converges to the systolic length, $\mathbb{E}_s[L] \to \ell_{\mathrm{sys}}$.
>
> **Analytic side.** The dominance of the primitive systolic terms gives the sharp asymptotic
> $$-\log Z_X(s) \sim \frac{N_{\mathrm{sys}}}{1 - e^{-\ell_{\mathrm{sys}}}}\,e^{-s\ell_{\mathrm{sys}}}\qquad (s \to \infty),$$
> because each of the $N_{\mathrm{sys}}$ leading terms contributes $\frac{e^{(1-s)\ell_{\mathrm{sys}}}}{e^{\ell_{\mathrm{sys}}} - 1} = \frac{e^{-s\ell_{\mathrm{sys}}}}{1 - e^{-\ell_{\mathrm{sys}}}}$. Inverting reveals two recovery formulas:
> $$\ell_{\mathrm{sys}} = -\lim_{s \to \infty}\frac{1}{s}\log\big(-\log Z_X(s)\big),\qquad N_{\mathrm{sys}} = (1 - e^{-\ell_{\mathrm{sys}}})\lim_{s \to \infty}e^{s\ell_{\mathrm{sys}}}(-\log Z_X(s)).$$
> The systole *and* its multiplicity are read off from the large-$s$ asymptotics of the Selberg zeta.

---

# Where the paper uses this

Introduced at the top of [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.1]]. The tilt identity and moment formulas feed the coarser homology-class construction in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]], where the same normalising Selberg zeta value ($-\log Z_X(s)$) appears as the character-torus integral of $-\log L_X(s, \chi)$ at the trivial character. The systole limit connects to the length-spectrum rigidity results of §3.4 ([[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]], [[Cor - Loop Masses Determine the Hyperbolic Surface|Cor 3.12]]).
