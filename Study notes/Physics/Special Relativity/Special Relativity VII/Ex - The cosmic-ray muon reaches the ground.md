---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Time Dilation (General Observer)"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Problem Statement

Muons are unstable particles, with a proper mean lifetime $\tau_0 = 2.2 \times 10^{-6}\,\mathrm{s}$. They are produced high in the atmosphere by cosmic rays, at altitudes of order $10\,\mathrm{km}$, moving at speeds close to $c$. Working with $c = 1$ where convenient and restoring it where the answer is more recognisable:

1. In a world *without* time dilation, how far would a muon travel, on average, before decaying? Compare this to the $\sim 10\,\mathrm{km}$ it must cover to reach the ground, and state the naive (wrong) conclusion.
2. Now account for time dilation. The terrestrial observer measures a dilated mean lifetime $\Gamma\tau_0$. Show that the mean distance travelled in the lab frame is $d = \Gamma V \tau_0$, and find the Lorentz factor needed for a muon to have a good chance of reaching the ground from $10\,\mathrm{km}$.
3. Resolve the same physics from the *muon's* rest frame, where its lifetime is just $\tau_0$. What is contracted, and by how much, so that the two frames agree the muon arrives?
4. The Frisch–Smith experiment (1963) selected muons with $0.9950 \le V \le 0.9954$ (in units of $c$) at the top of Mount Washington (altitude $1910\,\mathrm{m}$) and measured their flux again at Cambridge, Massachusetts (altitude $3\,\mathrm{m}$). They found the muons survived as if their lifetime were $(8.8 \pm 0.8)\tau_0$. What Lorentz factor does this imply, and is it consistent with the selected speed?

**Recall:**

The exercise rests on time dilation and the relation between proper time and lab time.

![[Thm - Time Dilation (General Observer)#Statement]]

The [[Def - Proper Time|proper time]] $\tau_0$ of the muon is the time measured by a clock carried with the muon — and a decay is exactly such a clock, governed by the muon's own proper time. The [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] relates the observer's elapsed time to the muon's by $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$, so the terrestrial observer assigns the muon a lifetime $\Gamma$ times longer than $\tau_0$.

---

# Convergent Strategy

**Problem class.** A *predict-the-outcome-of-an-experiment* problem, the physical pay-off of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|kinematics]]: the geometric fact $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$ is turned into a falsifiable prediction (the surviving muon flux) and confronted with measurement. It is also a *frame-invariance check*, since the same arrival must follow from time dilation in the lab frame and length contraction in the muon frame.

**Assumption pattern.** A decay process with a definite proper lifetime $\tau_0$ is specified — the signpost (per the chapter's third disguised source for time dilation) that "any finite-duration physical process is a clock", so the theorem governs its observed rate. The speed is close to but below $c$, so $\Gamma \gg 1$, and the altitude is fixed. The phrase "resolve from the muon's frame" signals that part 3 must give the *complementary* explanation (length contraction) that agrees with part 2.

**Theorem routing.** Parts 1–2 apply [[Thm - Time Dilation (General Observer)]]: the lab-measured lifetime is $\Gamma\tau_0$, so the mean lab-frame travel distance is $d = \Gamma V\tau_0$, and requiring $d \gtrsim 10\,\mathrm{km}$ fixes the needed $\Gamma$. Part 3 routes through the *reciprocal* effect — in the muon frame the lifetime is $\tau_0$ but the atmospheric thickness is [[Thm - Length Contraction|length-contracted]] to $L/\Gamma$ — and the consistency of the two descriptions is the content of [[Def - Lorentz Factor and Relative Velocity]]. Part 4 inverts the measured lifetime ratio to extract $\Gamma$ and checks it against the velocity formula $\Gamma = (1-V^2)^{-1/2}$.

**Key decision point.** The crux is recognising that time dilation (lab frame) and length contraction (muon frame) are *the same physics seen two ways*, and that a single number — the survival ratio — must come out the same in both. The natural error is to apply *both* dilation and contraction in the *same* frame, double-counting the factor of $\Gamma$; the correct accounting uses dilation in the lab frame OR contraction in the muon frame, never both at once.

---

# Legal Operations Used

1. **Read the Lorentz factor as a scalar product / use time dilation** (operations 1 and from [[Thm - Time Dilation (General Observer)|the time-dilation theorem]]). The lab-frame lifetime is $\Gamma\tau_0$; the muon's clock (its decay) runs slow by $\Gamma$ as seen from the ground.

2. **Work in the rest frame, then reconcile** (operation 7, specialised). Part 3 computes in the muon's rest frame, where the lifetime is the proper $\tau_0$ and the atmosphere is contracted, then checks consistency with the lab-frame description.

3. **Use the speed–Lorentz-factor relation** (operation 4). The unit-norm constraint gives $\Gamma = (1-V^2)^{-1/2}$, used to check that the measured survival ratio matches the selected speed in part 4.

---

# Hints

> [!note]- Hint 1
> Without time dilation, the mean distance a muon travels before decaying is just speed times proper lifetime: $d_{\text{naive}} = V\tau_0 \approx c\tau_0$. Plug in $c\tau_0 = (3\times10^8\,\mathrm{m\,s^{-1}})(2.2\times10^{-6}\,\mathrm{s})$ and compare to $10\,\mathrm{km}$.

> [!note]- Hint 2
> With time dilation, the terrestrial observer sees the muon live for $\Gamma\tau_0$, so it travels $d = V\cdot\Gamma\tau_0 = \Gamma V\tau_0$. Set $d \gtrsim 10\,\mathrm{km}$ and solve for $\Gamma$ using $c\tau_0 \approx 660\,\mathrm{m}$.

> [!note]- Hint 3
> In the muon's frame, the muon's clock reads its proper lifetime $\tau_0$ (no dilation — it is at rest in its own frame). But the $10\,\mathrm{km}$ of atmosphere rushes past at speed $V$, [[Thm - Length Contraction|contracted]] to $L/\Gamma$. The muon survives if $L/\Gamma \lesssim V\tau_0$, i.e. $L \lesssim \Gamma V\tau_0$ — the *same* condition as part 2. The factor $\Gamma$ appears once, as contraction of distance, instead of once, as dilation of time.

> [!note]- Hint 4
> The survival ratio $(8.8 \pm 0.8)$ is the factor by which the muons' *effective* lifetime exceeded $\tau_0$, which is $\Gamma$. So $\Gamma = 8.8 \pm 0.8$. Check against the speed: $\Gamma = (1 - V^2)^{-1/2}$ for $V = 0.9952$ gives $\Gamma = 1/\sqrt{1 - 0.9952^2}$. Compute and compare.

---

# Solution

The route is to confront the naive non-relativistic estimate with the dilated one, then show the muon-frame (length-contraction) account gives the identical condition, and finally check the numbers against the Frisch–Smith data. Step 1 establishes the puzzle (muons should not reach the ground); Step 2 resolves it in the lab frame by time dilation; Step 3 resolves it in the muon frame by length contraction and confirms agreement; Step 4 extracts the experimental Lorentz factor and verifies consistency. The non-obvious thread is that one factor of $\Gamma$ — dilation in one frame, contraction in the other — accounts for the survival, and double-counting it is the error to avoid.

**Step 1: Without time dilation a muon travels only $\sim 660\,\mathrm{m}$, far short of $10\,\mathrm{km}$.**

> [!note]- Derivation
> The mean distance before decay, with no relativistic correction, is speed times proper lifetime:
> $$d_{\text{naive}} = V\tau_0 \approx c\tau_0 = (2.998\times10^8\,\mathrm{m\,s^{-1}})(2.2\times10^{-6}\,\mathrm{s}) \approx 660\,\mathrm{m}.$$
> A muon created at $10\,\mathrm{km}$ would, on this reckoning, decay after only $660\,\mathrm{m}$ — about $1/15$ of the way down. The number of muons surviving the full descent would be suppressed by $e^{-10000/660} \approx e^{-15} \approx 3\times10^{-7}$, essentially none. The naive (and wrong) conclusion is that no appreciable muon flux should reach the ground. Yet a copious flux is observed — roughly one muon per square centimetre per minute at sea level. The resolution is time dilation.

**Step 2: With time dilation, $d = \Gamma V\tau_0$; reaching $10\,\mathrm{km}$ needs $\Gamma \gtrsim 15$.**

> [!note]- Derivation
> The decay is a clock carried by the muon, ticking in the muon's [[Def - Proper Time|proper time]]. By [[Thm - Time Dilation (General Observer)|time dilation]], the terrestrial observer measures the muon's mean lifetime to be dilated:
> $$\tau_{\text{lab}} = \Gamma\tau_0.$$
> In that time the muon travels, in the lab frame, a mean distance
> $$d = V\,\tau_{\text{lab}} = \Gamma V\tau_0 \approx \Gamma\,c\tau_0 = \Gamma\cdot 660\,\mathrm{m}.$$
> For the muon to have a reasonable chance of covering $L = 10\,\mathrm{km} = 10000\,\mathrm{m}$, we need $d \gtrsim L$, i.e.
> $$\Gamma \gtrsim \frac{L}{c\tau_0} = \frac{10000}{660} \approx 15.$$
> A Lorentz factor of order $15$ — corresponding to $V = \sqrt{1 - \Gamma^{-2}} \approx 0.998c$ — multiplies the effective lifetime fifteenfold, turning the $660\,\mathrm{m}$ into $\sim 10\,\mathrm{km}$ and letting an appreciable fraction survive. This is entirely achievable for cosmic-ray muons, which are ultra-relativistic; the time dilation of this chapter is exactly what lets them reach the ground.

**Step 3: In the muon frame the lifetime is $\tau_0$, but the atmosphere is contracted to $L/\Gamma$ — the same condition.**

> [!note]- Derivation
> Switch to the muon's rest frame. Here the muon is at rest, so its clock runs at its proper rate and its mean lifetime is just $\tau_0$ — *no dilation*, because in its own frame the muon is not moving. What is different is the atmosphere: the $10\,\mathrm{km}$ thickness, at rest in the lab frame, rushes past the muon at speed $V$ and is therefore [[Thm - Length Contraction|length-contracted]] to
> $$L' = \frac{L}{\Gamma}.$$
> The muon survives the crossing if the contracted thickness is covered within its proper lifetime:
> $$\frac{L}{\Gamma} \lesssim V\tau_0 \approx c\tau_0,\qquad\text{i.e.}\qquad L \lesssim \Gamma\,c\tau_0,\qquad\text{i.e.}\qquad \Gamma \gtrsim \frac{L}{c\tau_0} \approx 15.$$
> This is *identical* to the condition from Step 2. The two frames agree the muon arrives, but they explain it differently: the lab frame says the muon's clock runs slow (dilated lifetime $\Gamma\tau_0$), the muon frame says the journey is short (contracted distance $L/\Gamma$). The factor $\Gamma$ appears exactly once in each account — as dilation of time in the lab, as contraction of length in the muon frame — and the physics is the same. Applying *both* in one frame would double-count, predicting survival from $\Gamma^2\,c\tau_0$, which is wrong.

**Step 4: Frisch–Smith measured an effective lifetime ratio of $8.8 \pm 0.8$, giving $\Gamma = 8.4 \pm 2.0$, consistent with $V \approx 0.995c$.**

> [!note]- Derivation
> Frisch and Smith compared the muon flux at the top of Mount Washington ($z_1 = 1910\,\mathrm{m}$) with that at Cambridge ($z_2 = 3\,\mathrm{m}$), a descent of $\Delta z \approx 1907\,\mathrm{m}$. They selected muons with $0.9950 \le V \le 0.9954$, mean $V \approx 0.9952c$. The measured survival corresponded to muons decaying as if their lifetime were $(8.8\pm0.8)\tau_0$ — that is, the *effective* lifetime exceeded the proper lifetime by the factor
> $$\frac{\tau_{\text{lab}}}{\tau_0} = \Gamma = 8.8 \pm 0.8\quad(\text{flux-based}),$$
> and converting the flux ratio to an inferred Lorentz factor gives $\Gamma = 8.4 \pm 2.0$.
>
> Now the consistency check. From the selected speed,
> $$\Gamma_{\text{velocity}} = \frac{1}{\sqrt{1 - V^2}} = \frac{1}{\sqrt{1 - (0.9952)^2}} = \frac{1}{\sqrt{1 - 0.99042}} = \frac{1}{\sqrt{0.00958}} \approx \frac{1}{0.0979} \approx 10.2.$$
> The flux-inferred $\Gamma = 8.4 \pm 2.0$ overlaps the velocity-predicted $\Gamma \approx 10$ within the experimental uncertainty (the range $8.4 \pm 2.0$ reaches $10.4$). The agreement is the quantitative confirmation: muons selected at a known speed survive by exactly the factor $\Gamma$ that time dilation predicts. (The later CERN storage-ring experiment, Bailey *et al.* 1979, reached $\Gamma = 29.3$ at $V = 0.9994c$ and confirmed the dilation to one part in $10^3$.)

> [!note]- Complete formal solution
> Without time dilation, a muon travels a mean $d_{\text{naive}} = c\tau_0 \approx 660\,\mathrm{m}$ before decaying, so from $10\,\mathrm{km}$ the survival probability is $\sim e^{-15} \approx 3\times10^{-7}$ — essentially none, contradicting the observed sea-level flux. With [[Thm - Time Dilation (General Observer)|time dilation]], the lab-frame lifetime is $\Gamma\tau_0$ and the mean distance is $d = \Gamma c\tau_0$, so reaching $L = 10\,\mathrm{km}$ requires $\Gamma \gtrsim L/(c\tau_0) \approx 15$, easily met by ultra-relativistic muons. In the muon's rest frame the lifetime is the proper $\tau_0$, but the atmosphere is [[Thm - Length Contraction|contracted]] to $L/\Gamma$, giving the identical survival condition $\Gamma \gtrsim L/(c\tau_0)$ — dilation and contraction are one factor of $\Gamma$ seen in two frames, and applying both at once double-counts. The Frisch–Smith experiment, selecting $V \approx 0.9952c$ between Mount Washington and Cambridge, measured an effective lifetime ratio of $8.8 \pm 0.8$, giving $\Gamma = 8.4 \pm 2.0$, consistent within errors with the velocity prediction $\Gamma = (1-V^2)^{-1/2} \approx 10$. The muons reach the ground because their clocks run slow by exactly the Lorentz factor. $\blacksquare$

---

# Key Takeaways

**A decay is a clock, and time dilation governs it exactly as it governs a mechanical clock — because it is the proper time that dilates, not any internal machinery.** The deep point of the muon experiment, made vivid by Tong's remark that an elementary particle is "structureless, certainly not some clock with internal machinery", is that the muon has no gears to slow down: what runs slow is the proper time along its worldline, and the decay probability depends only on the elapsed proper time. So the survival of muons to ground level is a *direct* measurement of $\mathrm{d}\tau = \Gamma\,\mathrm{d}\tau'$, with no model of muon structure needed. The reusable trigger: whenever a problem gives a lifetime, period, or decay constant "in the rest frame" or "proper", that is a proper-time interval $\tau_0$, and any other observer measures $\Gamma\tau_0$. This is the working tool of all of particle physics — every secondary beamline's length is set by the decay length $\Gamma V\tau_0$ of the particles it transports.

**Time dilation and length contraction are the same physics seen from two frames, and you apply exactly one of them — never both at once.** The muon reaches the ground either because its clock runs slow (lab frame: lifetime $\Gamma\tau_0$, full distance $L$) or because the distance is short (muon frame: lifetime $\tau_0$, contracted distance $L/\Gamma$), and the two accounts give the identical condition $\Gamma \gtrsim L/(c\tau_0)$ with one factor of $\Gamma$ in each. The classic and costly error is to mix frames — to dilate the lifetime *and* contract the distance in the same calculation — which inserts $\Gamma^2$ and predicts twice the survival. The diagnostic is to fix a single frame at the outset and ask which effect operates there: in the frame where the clock moves, time dilates; in the frame where the distance moves, length contracts; you are in one frame, so you get one effect. This frame-invariance check — that two correct frames give one physical answer — is the master sanity test of every relativistic kinematics problem.

**The Lorentz factor is the bridge between a kinematic input (speed) and an experimental observable (survival fraction), and consistency between the two is the test.** The Frisch–Smith experiment is a closed loop: it *selects* muons of known speed $V$, predicts $\Gamma = (1-V^2)^{-1/2}$ from that speed, independently *measures* the effective lifetime ratio (hence $\Gamma$) from the flux survival, and checks the two agree. This is the anatomy of a precision test of relativity — not "does time dilation happen?" but "does the *amount* of dilation match the *amount* of speed, by the specific function $\Gamma(V)$?". The reusable principle is that a quantitative confirmation pins down the functional form $\Gamma = (1-V^2)^{-1/2}$, not merely the qualitative existence of the effect; the same loop structure underlies the CERN storage-ring measurement ($\Gamma = 29.3$, accuracy $10^{-3}$) and, in the Doppler guise, the Ives–Stilwell experiment of [[Special Relativity VIII — Kinematics II, Change of Observer]]. A companion exercise drilling the cleaner inertial-frame version of the muon problem is [[Ex - Time dilation and the cosmic-ray muon]] in Special Relativity II.
