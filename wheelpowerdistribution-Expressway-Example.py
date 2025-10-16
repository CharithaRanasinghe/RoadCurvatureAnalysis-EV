import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

WHEEL_BASE = 0.3     # m
VEHICLE_SPEED = 3.0  # m/s

df = pd.read_csv("track_points.csv")  # csv
lat = df["X"].to_numpy()
lon = df["Y"].to_numpy()

R = 6371000
lat_rad = np.radians(lat)
lon_rad = np.radians(lon)
x = R * np.cos(lat_rad.mean()) * (lon_rad - lon_rad[0])
y = R * (lat_rad - lat_rad[0])

ds = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
s = np.concatenate(([0], np.cumsum(ds)))

def derivative(arr, s):
    arr = np.array(arr)
    s = np.array(s)
    d = np.zeros_like(arr)
    d[1:-1] = (arr[2:] - arr[:-2]) / (s[2:] - s[:-2])
    d[0] = d[1]
    d[-1] = d[-2]
    return d

x1 = derivative(x, s)
y1 = derivative(y, s)
x2 = derivative(x1, s)
y2 = derivative(y1, s)


curvature = np.abs(x1*y2 - y1*x2) / (x1**2 + y1**2)**1.5
curvature[curvature == 0] = 1e-6
radius = 1 / curvature


v_inner = VEHICLE_SPEED * (radius - WHEEL_BASE/2) / radius
v_outer = VEHICLE_SPEED * (radius + WHEEL_BASE/2) / radius


results = pd.DataFrame({
    "s_m": s,
    "x_m": x,
    "y_m": y,
    "curvature_1pm": curvature,
    "radius_m": radius,
    "v_inner_mps": v_inner,
    "v_outer_mps": v_outer
})
results.to_csv("wheel_speed_with_curvature.csv", index=False)
print("Saved results to wheel_speed_with_curvature.csv")


fig, ax1 = plt.subplots(figsize=(12,6))

color_inner = 'tab:blue'
color_outer = 'tab:red'
color_curv = 'tab:purple'

ax1.set_xlabel("Distance along path (m)")
ax1.set_ylabel("Wheel speeds (m/s)")
ax1.plot(s, v_inner, color=color_inner, label="Inner Wheel")
ax1.plot(s, v_outer, color=color_outer, label="Outer Wheel")
ax1.tick_params(axis='y')
ax1.grid(True)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.set_ylabel("Curvature (1/m)")
ax2.plot(s, curvature, color=color_curv, linestyle='--', label="Curvature")
ax2.tick_params(axis='y', labelcolor=color_curv)
ax2.legend(loc='upper right')

plt.title("Wheel Speeds and Curvature along GPS Path")
plt.show()
