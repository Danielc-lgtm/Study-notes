---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Liouville's Theorem"
  - "Thm - Real and Imaginary Parts of a Holomorphic Function are Harmonic"
  - "Thm - Existence of a Logarithm on Simply Connected Domains"
tags: [analysis, complex-analysis]
---

# Problem Statement

Show that a bounded harmonic function $u : \mathbb{R}^2 \to \mathbb{R}$ (i.e., $\Delta u = 0$ on all of $\mathbb{R}^2$, and $|u(x, y)| \leq M$ for some $M$) is constant.

**Recall:**

A function $u : \mathbb{R}^2 \to \mathbb{R}$ is **harmonic** if $u \in C^2$ and $\Delta u = u_{xx} + u_{yy} = 0$. On a simply connected domain in $\mathbb{R}^2 \cong \mathbb{C}$, every harmonic $u$ has a **harmonic conjugate** $v$ (also harmonic) such that $f = u + iv$ is holomorphic — by integrating the candidate $dv = -u_y\,dx + u_x\,dy$ (closed by CR-consistency), which is exact on simply connected domains.

[[Thm - Liouville's Theorem]]: a bounded entire function is constant.

---

# Convergent Strategy

**Problem class:** Use complex methods to prove a real-analytic statement (Liouville for harmonic functions).

**Assumption pattern:** $u$ harmonic on $\mathbb{R}^2$ (simply connected!), $u$ bounded.

**Theorem routing:** Build a holomorphic $f = u + iv$ via harmonic conjugate. Show $e^f$ is bounded entire (since $|e^f| = e^u$ is bounded). Apply Liouville to $e^f$. Conclude $f$ constant, hence $u$ constant.

**Key decision point:** Recognizing that $|e^f| = e^u$ — so a bounded $u$ gives bounded $|e^f|$, even though $f$ itself need not be bounded ($v$ could be unbounded).

---

# Legal Operations Used

1. **Construct harmonic conjugate** $v$ on $\mathbb{R}^2$ (simply connected). Get holomorphic $f = u + iv$.
2. **Form $g = e^f$.** Entire, since $f$ entire.
3. **Bound $|g| = e^u \leq e^M$.** Bounded entire.
4. **Apply Liouville** to $g$. $g$ constant.
5. **From $g$ constant** conclude $f$ constant (up to additive $2\pi i k$), hence $u = \operatorname{Re} f$ constant.

---

# Hints

> [!note]- Hint 1
> Build a harmonic conjugate $v$ for $u$ on $\mathbb{R}^2$ — this works because $\mathbb{R}^2$ is simply connected.

> [!note]- Hint 2
> $f = u + iv$ is entire. Consider $g = e^f$: still entire, and $|g| = e^{\operatorname{Re} f} = e^u \leq e^M$. So $g$ is bounded entire — apply Liouville.

> [!note]- Hint 3
> $g$ constant means $f$ takes values in a discrete set $\{f_0 + 2\pi i k\}$. By continuity (since $f$ entire), $f$ is constant. So $u$ is constant.

---

# Solution

The proof breaks into six steps that together lift the harmonic statement to a holomorphic one and apply complex Liouville. Steps 1–2 build a holomorphic $f = u + iv$ on $\mathbb{R}^2$ via harmonic conjugate and form $g = e^f$; Steps 3–4 use $|g| = e^u \leq e^M$ to apply Liouville and conclude $g$ is constant; Steps 5–6 propagate "g constant" back to $f$ via discreteness of $\exp^{-1}(c)$ and connectedness of $\mathbb{R}^2$, then read off $u = \operatorname{Re} f$ constant. The non-obvious move is in Step 2 — using the exponential to convert a bound on $\operatorname{Re} f$ into a bound on $|e^f|$, since $f$ itself need not be bounded.

**Step 1: Harmonic conjugate.**

$\mathbb{R}^2$ is simply connected, so by the standard construction of harmonic conjugates, there exists a harmonic $v : \mathbb{R}^2 \to \mathbb{R}$ such that $f := u + iv$ is holomorphic on $\mathbb{R}^2 \cong \mathbb{C}$.

> [!note]- Construction of $v$
> The candidate differential is $dv = -u_y\,dx + u_x\,dy$. This 1-form is *closed* on $\mathbb{R}^2$: $\partial(-u_y)/\partial y = -u_{yy}$ and $\partial u_x/\partial x = u_{xx}$, and $u_{xx} + u_{yy} = \Delta u = 0$ (so the closedness condition $\partial(-u_y)/\partial y = \partial u_x/\partial x$ becomes $-u_{yy} = u_{xx}$, i.e., $u_{xx} + u_{yy} = 0$, which holds). Since $\mathbb{R}^2$ is simply connected, the closed form $dv$ is *exact*: $dv = dv$ for some $v$, defined up to a constant by integration along any path. The resulting $f = u + iv$ has $u_x = v_y$ and $u_y = -v_x$ (CR), and continuous partials, so $f$ is holomorphic.

**Step 2: Form $g = e^f$.**

$f$ is entire; the composition $g = e^f$ is also entire (composition of entire functions).

**Step 3: $|g|$ is bounded.**

$|g(z)| = |e^{f(z)}| = e^{\operatorname{Re} f(z)} = e^{u(z)} \leq e^M$ (since $u \leq M$). So $g$ is bounded entire with $|g| \leq e^M$.

**Step 4: Apply Liouville.**

By [[Thm - Liouville's Theorem]], $g$ is constant. So $e^{f(z)} = c$ for some constant $c \in \mathbb{C}^\times$ (note $c \neq 0$ since $e^f$ is never zero, by [[Thm - Properties of the Complex Exponential|properties of exp]]).

**Step 5: $f$ is constant.**

Since $e^f = c$, $f$ takes values in the set $\exp^{-1}(c) = \{w_0 + 2\pi i k : k \in \mathbb{Z}\}$ where $w_0$ is one specific logarithm of $c$. This is a discrete subset of $\mathbb{C}$.

But $f$ is *continuous* (entire) on the *connected* $\mathbb{R}^2$. The image of a connected set under a continuous map is connected. The only connected subsets of a discrete set are singletons. So $f$ is constant.

**Step 6: $u$ is constant.**

$u = \operatorname{Re} f$ is the real part of a constant complex number, hence constant. $\blacksquare$

> [!note]- Complete formal solution
> $\mathbb{R}^2$ is simply connected. By harmonic conjugate construction, $v$ exists with $f = u + iv$ entire. Form $g = e^f$, entire. $|g| = e^u \leq e^M$ bounded. By [[Thm - Liouville's Theorem]], $g \equiv c$ constant ($c \in \mathbb{C}^\times$). So $f$ takes values in the discrete set $\{w_0 + 2\pi i k\}$; continuity on connected $\mathbb{R}^2$ forces $f$ constant. Hence $u = \operatorname{Re} f$ constant. $\blacksquare$

---

# Key Takeaways

**Lifting Liouville to harmonic.**

A "real" theorem (Liouville for harmonic functions) is most cleanly proved by *lifting* to a complex function and applying complex Liouville. The lift uses two ingredients:
1. **Harmonic conjugate construction** — converts the harmonic $u$ into a holomorphic $f = u + iv$. Requires simple-connectedness of the domain. For $\mathbb{R}^2$, this is automatic.
2. **Exponentiation** — converts the unbounded $f$ (only $u$ is bounded; $v$ could be unbounded) into a bounded $e^f$. The trick is $|e^f| = e^{\operatorname{Re} f} = e^u$, which is bounded by $e^M$.

**The general pattern.**

Many statements about harmonic functions in 2D lift to statements about holomorphic functions on simply connected planar domains. Key examples: harmonic mean value property (CIF + take real parts), maximum modulus for harmonic ($|f| \to e^f$ trick), regularity ($u$ harmonic $\Rightarrow$ $u \in C^\infty$ via $u = \operatorname{Re} f$). The complex theory is "two-dimensional potential theory in disguise".

**Why doesn't this work in higher dimensions?**

There is no complex structure on $\mathbb{R}^n$ for $n > 2$. Harmonic functions in higher dimensions are studied directly, without the holomorphic lift. Liouville for harmonic in $\mathbb{R}^n$ still holds, but the proof is different (via Harnack's inequality or the mean value property directly).

**Exponentiation as the modulus-control trick.**

The move "consider $e^f$ when $\operatorname{Re} f$ is bounded but $f$ is not" is a recurring trick. It appears in the **Phragmén–Lindelöf principle** (a refinement of the maximum modulus principle), in the analysis of growth of entire functions, and in many one-variable complex analysis arguments. The trigger: a bound on $\operatorname{Re} f$, not on $|f|$ itself.
