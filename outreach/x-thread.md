# Draft: X (Twitter) thread

**Platform:** X (personal account)
**Length:** 7 tweets, each at-or-under 280 chars (counted below; verify in compose window before posting — X counts URLs as 23 chars regardless of length).
**Format:** Plain text. No Markdown. No emoji (per author preference). Each tweet stands alone; people will quote-tweet individual ones.

---

## Tweet 1 — hook

> Fifteen years ago, I had the privilege of advising Rosen Diankov's PhD at CMU. The capstone was IKFast — for a generation of roboticists, the definition of what analytical inverse kinematics could be.
>
> Today, the Personal Robotics Lab is releasing the next chapter: ssik.
>
> 1/

(~280 chars. The Diankov/IKFast hook is the scroll-stopper; only Siddhartha can credibly tell this story. Do not edit.)

## Tweet 2 — what it does

> ssik returns every analytical IK branch for 6R and 7R arms.
>
> Pure Python at runtime. BSD-3-Clause. pip install ssik.
>
> 13 commercial arms ship as prebuilt artifacts. For anything else, `ssik build my_arm.urdf` emits a single-file solver from your robot's description.
>
> 2/

(~270 chars.)

## Tweet 3 — the arm list (great for discoverability / search)

> Prebuilt arms:
>
> UR5, Franka Panda, Kinova JACO 2 & Gen3, KUKA iiwa14, Flexiv Rizon 4 & 10, Kassow KR810, UFactory xArm6 & xArm7, Unitree Z1, AgileX PiPER, Puma 560.
>
> If your arm isn't here, open an issue with the URDF and we'll add it.
>
> 3/

(~250 chars.)

## Tweet 4 — why now

> Why this matters now: the cobot generation — Rizon, JACO, PiPER, Kassow — sits outside the classical kinematic families (Pieper 6R, SRS 7R) that existing analytical IK libraries cover.
>
> ssik handles them via Husty-Pfurner Study-quaternion + subproblem dispatch.
>
> 4/

(~270 chars.)

## Tweet 5 — the demo-collection / VLA angle (the most important tweet for 2026 mindshare)

> What I'm most excited about: teleop rigs for collecting demonstrations to train imitation-learning, behaviour-cloning, and VLA policies.
>
> They need IK that's deterministic, jump-free, fast at controller rate. Analytical IK is that primitive. Numerical IK isn't.
>
> 5/

(~278 chars.)

## Tweet 6 — correctness

> Every prebuilt arm is fuzz-tested at 500 random poses on every PR, with FK closure asserted to a per-class floor.
>
> The promise: correct, every arm, every pose, every time. If you find a pose ssik gets wrong, that's a release-blocking bug — I want to know.
>
> 6/

(~275 chars.)

## Tweet 7 — links + CTA

> Repo: https://github.com/personalrobotics/ssik
> Docs: https://personalrobotics.github.io/ssik/
> DOI: https://doi.org/10.5281/zenodo.20278005
>
> Open-source in the spirit IKFast was. Especially eager to hear from folks building demo-collection rigs.
>
> What arm do you wish had analytical IK?
>
> 7/7

(~280 chars after X's URL shortening.)

---

## Notes for posting

- **Tweet 1 is everything.** On X, ~90% of impressions come from the first tweet of a thread. The Diankov/IKFast lineage hook is uniquely Siddhartha's to make — nobody else can land it the same way. That's the asset; do not rewrite it.
- **Alternative tweet 1** (problem-led; punchier but less differentiated) if the lineage angle feels too inside-baseball for the audience that day:
  > Most analytical IK libraries refuse the arms we actually use today — JACO, Rizon, PiPER, Kassow.
  >
  > We just shipped ssik 1.0, which solves them.
  >
  > pip install ssik. A thread on what it does and who it's for. 1/
- **Posting time:** weekdays 7-9am US Pacific catches Europe lunch + US morning. Avoid Friday afternoons.
- **@-mentions to consider** (only if connected and active on X):
  - @rdiankov — Rosen, if he's still posting. Crediting him publicly is the right thing to do regardless of engagement upside.
  - @AllenSchool, @uwcse — UW signal-boost
  - Vendor accounts (Kinova, Flexiv, Franka, Universal Robots, etc.) — light touch only; reply-mention if they engage, don't tag in the original.
- **Engagement triage in the first hour:**
  - "Does it work for [arm]?" — answer with whether it's prebuilt, buildable, or in the next-release target list. Specific is better.
  - Comparison qs (TracIK, KDL, MoveIt, EAIK, IK-Geo) — complement-not-replace; analytical-branch enumeration is the differentiator. Do not bash competitors.
  - Demo-collection / VLA folks asking for help — pull those into DMs and offer to help concretely. These are the conversations worth having.
- **Quote-RT bait:** Tweet 5 (the VLA / demo-collection one) is the most quotable. If a VLA / robot-learning lab quote-RTs it, reply substantively; that's the highest-leverage interaction.
- **Don't pin the thread to your profile** unless you're willing to live with it as your top-of-page identity for the week. Better to pin only after engagement settles and you can see which tweet (1 or 5) lands hardest, then pin that one with a short add-on.
