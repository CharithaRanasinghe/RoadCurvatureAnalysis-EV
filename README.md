# RoadCurvatureAnalysis-EV

**Formal project for analysing road curvature from GPS/GPX data and simulating rear-wheel speed/power behaviour for electric vehicles (EVs).**

---

## Overview

`RoadCurvatureAnalysis-EV` extracts route geometry from GPX/CSV tracks, computes curvature and turning radius along the path, and simulates inner/outer rear-wheel linear and angular speeds for a given vehicle speed and track width. The project is intended as a foundation for comparing torque-split strategies, energy consumption modeling, and road-design sensitivity studies for EVs.

Target users: researchers, EEE/transportation students, EV control engineers, and hobbyists.

---

## Example

Kadawatha-Expressway - Kadawatha Interchange - Outer Circular Highway
https://github.com/CharithaRanasinghe/RoadCurvatureAnalysis-EV/tree/ExampleWheelPowerDistribution-KadawathaExpressway

<img width="1350" height="492" alt="SelectedTrackforAnalysis" src="https://github.com/user-attachments/assets/f7d35e1e-6b7b-45f7-bc99-1a56ba15a658" />

<img width="1506" height="839" alt="WheelPowerDistribution-withCurvature" src="https://github.com/user-attachments/assets/88c876cf-3cf0-41da-84b8-98337037068b" />

---

## Features

* Parse GPX and CSV tracks (handles timestamps if present)
* Project lat/lon to local metric coordinates (UTM)
* Compute curvature and radius using robust numerical derivatives
* Smooth noisy GPS data (Savitzky–Golay filter)
* Compute inner & outer wheel linear and angular speeds
* Flag sharp turns and export per-point results to CSV
* Plot curvature and wheel-speed profiles (combined plot)
* Configurable vehicle parameters (track width, wheel radius, default speed)

---

## Quickstart

### Prerequisites

* Python 3.9+
* Recommended packages:

  ```bash
  pip install numpy pandas pyproj matplotlib gpxpy scipy
  ```

### Run the example script

1. Place your GPX or CSV track in the repository folder.
2. Edit the script parameters (`DEFAULT_SPEED`, `TRACK_WIDTH`, etc.) or pass the file path on the command line.

Example (if script is `gpx_curvature_sim.py`):

```bash
python gpx_curvature_sim.py path/to/your_track.gpx
```

Outputs:

* `gpx_curvature_results.csv` (per point: s, x, y, curvature, radius, wheel speeds)
* `gpx_curvature_radius.png` and `gpx_curvature_wheel_speeds.png` (plots)

---

## Files & Structure (recommended)

```
RoadCurvatureAnalysis-EV/
├─ data/                 # raw GPX/CSV files (not committed large files)
├─ notebooks/            # Jupyter notebooks for experiments/visualization
├─ src/                  # main scripts and modules
│  ├─ gpx_curvature_sim.py
│  ├─ utils.py            # projection, smoothing, plotting helpers
├─ examples/             # example GPX/CSV and outputs
├─ README.md
├─ requirements.txt
├─ LICENSE
└─ .gitignore
```

---

## CSV input format (if using CSV)

Minimal required columns:

```
latitude,longitude[,time]
```

If `time` exists, the script will attempt to use timestamps to compute instantaneous speed; otherwise a default speed is used.

---

## API / Usage (script interface)

**`process_gpx(path, speed=DEFAULT_SPEED)`** — processes a GPX/CSV file and returns a pandas DataFrame with these columns:

* `s_m`, `x`, `y`, `curvature_1pm`, `radius_m`, `center_speed_mps`, `u_inner_mps`, `u_outer_mps`, `omega_inner_rps`, `omega_outer_rps`, `is_sharp`

You can import `src.gpx_curvature_sim` from notebooks and call `process_gpx()` directly for programmatic use.

---

## License

Suggested: **MIT License** (permissive, easy for collaboration)

---

## Contribution

1. Fork the repo
2. Create a feature branch
3. Add tests and documentation
4. Open a pull request

---
