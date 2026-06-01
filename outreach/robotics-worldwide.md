# Draft: robotics-worldwide mailing list post

**List:** robotics-worldwide@usc.edu (subscribe / archives at https://duerer.usc.edu/mailman/listinfo.cgi/robotics-worldwide)
**Suggested subject:** `[Software] ssik: open-source analytical inverse kinematics for 6R and 7R revolute manipulators`

---

## Subject

`[Software] ssik: open-source analytical inverse kinematics for 6R and 7R revolute manipulators`

## Body

Dear robotics-worldwide,

I'd like to share **ssik**, an open-source Python library for analytical inverse kinematics on 6R and 7R revolute manipulators. It's the successor to the Personal Robotics Lab's earlier IKFast work led by Rosen Diankov — modernised for the cobot generation and built especially for the learning pipelines now running on top of these arms.

  pip install ssik
  Repo:    https://github.com/personalrobotics/ssik
  Docs:    https://personalrobotics.github.io/ssik/
  DOI:     https://doi.org/10.5281/zenodo.20278005
  License: BSD-3-Clause

### Fast

Median per-pose timings on the prebuilt arms:

  - Puma 560, UR5:                                  0.2 – 0.5 ms
  - Kinova JACO 2, UFactory xArm6, AgileX PiPER:    ~1 ms (non-Pieper 6R)
  - KUKA iiwa14:                                    4.5 ms (SRS 7R, 128 redundancy branches)
  - Franka Panda, Flexiv Rizon 4, Kassow KR810:     27 – 30 ms (non-SRS 7R)

At a 30 Hz teleop loop every prebuilt fits inside the controller period; on the closed-form classes ssik runs three orders of magnitude faster than that. The goal is for IK to never be the bottleneck in your data pipeline.

### Built for learning

The application I most want to enable is **teleoperation for collecting demonstrations to train imitation-learning, behaviour-cloning, and VLA policies**. These pipelines need IK that is deterministic, jump-free, and fast — properties analytical IK has and numerical IK doesn't. The pattern

  sols = arm.solve(T_target, max_solutions=1, q_seed=q_current)

returns the analytical branch nearest the current joint state in a single closed-form call: no seed-dependent jumps, no convergence stalls mid-demonstration, no surprises when the operator crosses a singularity. If you are building demonstration-collection infrastructure I would genuinely love to hear what you need.

### Arms and correctness

Thirteen commercial arms ship as prebuilt artifacts (UR5, Puma 560, Kinova JACO 2 & Gen3, KUKA iiwa14, Franka Panda, Flexiv Rizon 4 & 10, Kassow KR810, UFactory xArm6 & xArm7, Unitree Z1, AgileX PiPER). Any other arm is supported via `ssik build my_arm.urdf`, which emits a single-file Python artifact specialised to the URDF — adding a new prebuilt to the repository is a one-line `MANIFEST.toml` entry, and contributions are warmly welcomed.

Correctness is enforced empirically: every prebuilt is exercised by a 500-pose Hypothesis fuzz sweep on every pull request, with forward-kinematics closure asserted to a per-class floor. If you find a pose ssik gets wrong, that's a release-blocking bug I'd want to hear about.

The implementation is a clean-room reimplementation from the open literature (Elias & Wen 2022/2025; Husty, Pfurner & Schröcker 2007; Raghavan & Roth 1993; Singh & Kreutz-Delgado 1989); per-module docstrings cite the relevant references. No LGPL code from OpenRAVE / IKFast is vendored.

Issues, pull requests, and arm requests are warmly welcomed. Thank you to the many people across this community whose work on IK over the decades has made this possible.

Best,
Siddhartha Srinivasa
Professor, Paul G. Allen School of Computer Science and Engineering
Personal Robotics Laboratory, University of Washington
https://goodrobot.ai

---

## Notes for posting

- robotics-worldwide is a moderated, low-volume academic list. The subject-line prefix "[Software]" is the convention for tool announcements.
- One post per major release is well within community norms; do not post for every PATCH.
- Expected replies: comparison questions (IKFast, IK-Geo, EAIK, OPW); requests for specific arms; bug reports. Be ready to handle each with a specific reference back to the docs.
