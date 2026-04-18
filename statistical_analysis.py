import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from scipy import stats
import os

os.makedirs("figures", exist_ok=True)

A_COLOR = "#4f46e5"
B_COLOR = "#94a3b8"
RED_A   = "#e11d48"
RED_B   = "#f87171"
GREEN   = "#10b981"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#e2e8f0",
    "grid.linewidth": 0.6,
    "axes.labelsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 180,
})

# ── Fig 1: Average engagement time ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4))
bars = ax.bar(["Version A\n(with guide)", "Version B\n(without guide)"],
              [119, 29], color=[A_COLOR, B_COLOR], width=0.45,
              edgecolor="none", zorder=3)
for bar, val in zip(bars, [119, 29]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f"{val} s", ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_ylabel("Seconds")
ax.set_ylim(0, 145)
ax.set_title("Fig. 1  Average engagement time per session", fontsize=11, fontweight="bold", pad=10)
ax.annotate("4.1× longer in Version A\np = 0.18 (z-test, n = 60 sessions)",
            xy=(0.97, 0.92), xycoords="axes fraction",
            ha="right", va="top", fontsize=8.5, color="#64748b",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8))
plt.tight_layout()
plt.savefig("figures/fig1_engagement_time.png", bbox_inches="tight")
plt.close()
print("Saved fig1")

# ── Fig 2 + 3: Engagement rate & Bounce rate (side by side) ──────────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 4))

# Fig 2 engagement rate
ax = axes[0]
bars = ax.bar(["A", "B"], [73.3, 62.5], color=[A_COLOR, B_COLOR],
              width=0.4, edgecolor="none", zorder=3)
for bar, val in zip(bars, [73.3, 62.5]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f"{val}%", ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_ylim(50, 90)
ax.set_ylabel("Engagement rate (%)")
ax.set_title("Fig. 2  Engagement rate", fontsize=11, fontweight="bold", pad=10)
ax.annotate("+10.8 pp\nχ² = 0.84, p = 0.36",
            xy=(0.97, 0.95), xycoords="axes fraction",
            ha="right", va="top", fontsize=8.5, color="#64748b",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8))

# Fig 3 bounce rate
ax = axes[1]
bars = ax.bar(["A", "B"], [26.7, 37.5], color=[RED_A, RED_B],
              width=0.4, edgecolor="none", zorder=3)
for bar, val in zip(bars, [26.7, 37.5]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f"{val}%", ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_ylim(15, 50)
ax.set_ylabel("Bounce rate (%)")
ax.set_title("Fig. 3  Bounce rate", fontsize=11, fontweight="bold", pad=10)
ax.annotate("−10.8 pp  (lower is better)\nz = −0.91, p = 0.18",
            xy=(0.97, 0.95), xycoords="axes fraction",
            ha="right", va="top", fontsize=8.5, color="#64748b",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8))

patch_a = mpatches.Patch(color=A_COLOR, label="Version A (with guide)")
patch_b = mpatches.Patch(color=B_COLOR, label="Version B (without guide)")
fig.legend(handles=[patch_a, patch_b], loc="lower center", ncol=2,
           fontsize=9, frameon=False, bbox_to_anchor=(0.5, -0.05))
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig("figures/fig2_3_rates.png", bbox_inches="tight")
plt.close()
print("Saved fig2+3")


# # ── Fig 4: Event composition grouped bar ─────────────────────────────────────
# events     = ["page_view", "scroll", "session_start", "first_visit", "user_engagement"]
# counts_a   = [40, 35, 29, 24, 24]
# counts_b   = [37, 36, 31, 23, 29]

# x   = np.arange(len(events))
# w   = 0.35
# fig, ax = plt.subplots(figsize=(8, 4.5))
# ba  = ax.bar(x - w/2, counts_a, w, color=A_COLOR, edgecolor="none", zorder=3, label="Version A")
# bb  = ax.bar(x + w/2, counts_b, w, color=B_COLOR, edgecolor="none", zorder=3, label="Version B")
# for bar in list(ba) + list(bb):
#     ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
#             str(int(bar.get_height())), ha="center", va="bottom", fontsize=8.5)
# ax.set_xticks(x)
# ax.set_xticklabels(events, fontsize=9.5)
# ax.set_ylabel("Event count")
# ax.set_ylim(0, 50)
# ax.set_title("Fig. 4  Event count by event type — both versions",
#              fontsize=11, fontweight="bold", pad=10)
# ax.legend(fontsize=9, frameon=False)
# ax.annotate("Event volumes are nearly identical across conditions;\nthe key difference lies in session depth, not click count.",
#             xy=(0.99, 0.96), xycoords="axes fraction",
#             ha="right", va="top", fontsize=8, color="#64748b",
#             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8))
# plt.tight_layout()
# plt.savefig("figures/fig4_events.png", bbox_inches="tight")
# plt.close()
# print("Saved fig4")

# ── Fig 4: Event composition grouped bar ─────────────────────────────────────
events   = ["page_view", "scroll", "session_start", "first_visit", "user_engagement"]
counts_a = [40, 35, 29, 24, 24]
counts_b = [37, 36, 31, 23, 29]

x = np.arange(len(events))
w = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))

# bars
ba = ax.bar(
    x - w/2, counts_a, w,
    color=A_COLOR, edgecolor="none", zorder=3,
    label="Version A (with guide)"
)
bb = ax.bar(
    x + w/2, counts_b, w,
    color=B_COLOR, edgecolor="none", zorder=3,
    label="Version B (without guide)"
)

# value labels
for bar in list(ba) + list(bb):
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.4,
        str(int(bar.get_height())),
        ha="center", va="bottom", fontsize=8.5
    )

# axes
ax.set_xticks(x)
ax.set_xticklabels(events, fontsize=9.5)
ax.set_ylabel("Event count")
ax.set_ylim(0, 50)

# title
ax.set_title(
    "Fig. 4  Event count by event type — both versions",
    fontsize=11, fontweight="bold", pad=12
)

# legend：放到图内顶部，标题下方，不和 annotation 打架
ax.legend(
    fontsize=9,
    frameon=False,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.995),
    ncol=2,
    borderaxespad=0.2
)

# annotation：右上角稍微往下挪
ax.annotate(
    "Event volumes are nearly identical across conditions;\n"
    "the key difference lies in session depth, not click count.",
    xy=(0.99, 0.90), xycoords="axes fraction",
    ha="right", va="top",
    fontsize=8, color="#64748b",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8)
)

# grid
ax.grid(axis="y", color="#cbd5e1", linewidth=0.8, alpha=0.8, zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 注意：这里不要再用 fig.subplots_adjust(top=...)
plt.tight_layout()
plt.savefig("figures/fig4_events.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved fig4")

# Fig 5: Power analysis curve (CORRECTED: n=250 for 80% power)
def compute_power(n, p0=0.375, p1=0.267, alpha=0.05):
    pbar   = (p0 + p1) / 2
    se     = np.sqrt(2 * pbar * (1 - pbar) / n)
    z_stat = abs(p0 - p1) / se - stats.norm.ppf(1 - alpha)
    return stats.norm.cdf(z_stat)
 
ns     = np.arange(10, 300, 1)
powers = [compute_power(n) for n in ns]
 
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(ns, powers, color=A_COLOR, lw=2, zorder=3)
ax.fill_between(ns, powers, alpha=0.1, color=A_COLOR)
ax.axhline(0.80, color=GREEN, lw=1.5, linestyle="--", label="80% power threshold")
ax.axvline(250, color=GREEN, lw=1, linestyle=":", alpha=0.7)
ax.axvline(30,  color="#e11d48", lw=1, linestyle=":", alpha=0.7)
 
current_power = compute_power(30)
ax.scatter([30],  [current_power],       color="#e11d48", zorder=5, s=60)
ax.scatter([250], [compute_power(250)],  color=GREEN,     zorder=5, s=60)
 
ax.annotate(f"Current study\nn = 30/group\npower approx {current_power*100:.0f}%",
            xy=(30, current_power), xytext=(60, 0.18),
            fontsize=8.5, color="#e11d48",
            arrowprops=dict(arrowstyle="->", color="#e11d48", lw=1))
ax.annotate("n = 250/group\n-> 80% power",
            xy=(250, compute_power(250)), xytext=(180, 0.70),
            fontsize=8.5, color="#0f6e56",
            arrowprops=dict(arrowstyle="->", color="#0f6e56", lw=1))
 
ax.set_xlabel("Sessions per group (n)")
ax.set_ylabel("Statistical power")
ax.set_ylim(0, 1.05)
ax.set_xlim(10, 290)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v*100:.0f}%"))
ax.set_title("Fig. 5  Statistical power vs. sample size\n"
             "(detecting 10.8 pp bounce rate difference, alpha = 0.05, one-tailed)",
             fontsize=11, fontweight="bold", pad=10)
ax.legend(fontsize=9, frameon=False)
plt.tight_layout()
plt.savefig("figures/fig5_power.png", bbox_inches="tight")
plt.close()
print("Saved fig5")

# ── Fig 6: Total engagement time horizontal bar ───────────────────────────────
fig, ax = plt.subplots(figsize=(6.5, 3))
vals    = [59.57, 15.55]
labels  = ["Version A\n(with guide)", "Version B\n(without guide)"]
colors  = [A_COLOR, B_COLOR]
bars    = ax.barh(labels, vals, color=colors, edgecolor="none", height=0.45, zorder=3)
for bar, val in zip(bars, vals):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            f"{val:.1f} min", va="center", fontsize=11, fontweight="bold")
ax.set_xlim(0, 72)
ax.set_xlabel("Total engagement time (minutes)")
ax.set_title("Fig. 6  Total accumulated user engagement (25 users each)",
             fontsize=11, fontweight="bold", pad=10)
ax.annotate("3.8× more total engagement in Version A",
            xy=(0.98, 0.08), xycoords="axes fraction",
            ha="right", va="bottom", fontsize=8.5, color="#64748b",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e2e8f0", lw=0.8))
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("figures/fig6_total_engagement.png", bbox_inches="tight")
plt.close()
print("Saved fig6")

print("\nDone! All figures saved to ./figures/")
