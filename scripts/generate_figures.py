"""Generate every diagram in this repo from first principles / cited values.

Run:  python scripts/generate_figures.py
Needs: numpy, matplotlib, pillow
All outputs land in <track>/png/ and gifs/. Values and their sources are
listed in each track's notes file and in IMAGE-SOURCES.md.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BG, FG, MUTED, GRID = "#0b1020", "#e8ecf8", "#9aa4c2", "#24304f"
C = ["#6ea8fe", "#f6b94c", "#ff7a90", "#5ad1a4", "#b892ff", "#59c3e8", "#f28c38"]

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "axes.edgecolor": GRID, "axes.labelcolor": FG, "text.color": FG,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.grid": True,
    "grid.color": GRID, "grid.linewidth": 0.6, "font.size": 11,
    "axes.titleweight": "bold", "axes.titlesize": 14, "legend.frameon": False,
})


def out(track, name):
    d = os.path.join(ROOT, track, "png") if track != "gifs" else os.path.join(ROOT, "gifs")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, name)


def save(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print("wrote", os.path.relpath(path, ROOT))


# ---------------------------------------------------------------- stellar
def hr_diagram():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    # main-sequence band from L ~ M^3.5 and R ~ M^0.8 -> T via Stefan-Boltzmann
    M = np.logspace(-1, 1.6, 200)
    L = M ** 3.5
    R = M ** 0.8
    T = 5772 * (L / R**2) ** 0.25
    ax.plot(T, L, color=C[0], lw=10, alpha=0.25, solid_capstyle="round")
    ax.plot(T, L, color=C[0], lw=1.5, label="Main sequence (L ∝ M^3.5 model)")
    stars = {  # name: (T_eff K, L/Lsun, colour)
        "Sun": (5772, 1, C[1]), "Proxima Cen": (3042, 0.0017, C[2]),
        "Sirius A": (9940, 25.4, C[5]), "Vega": (9602, 40, C[5]),
        "Betelgeuse": (3600, 1.0e5, C[2]), "Rigel": (12100, 1.2e5, C[5]),
        "Sirius B (white dwarf)": (25000, 0.056, FG),
    }
    for n, (t, l, c) in stars.items():
        ax.scatter(t, l, s=90, color=c, edgecolor="white", lw=0.6, zorder=5)
        ax.annotate(n, (t, l), xytext=(8, 6), textcoords="offset points", fontsize=10)
    ax.set_xscale("log"); ax.set_yscale("log"); ax.invert_xaxis()
    ax.set_xlim(40000, 2500); ax.set_ylim(1e-4, 1e6)
    ax.set_xlabel("Surface temperature (K)  →  cooler")
    ax.set_ylabel("Luminosity (L☉)")
    ax.text(30000, 3e-3, "White dwarfs", color=MUTED, style="italic")
    ax.text(4500, 3e4, "Giants &\nsupergiants", color=MUTED, style="italic")
    ax.set_title("Hertzsprung–Russell diagram: where stars live")
    ax.legend(loc="lower left")
    save(fig, out("stellar", "hr_diagram_generated.png"))


def stellar_lifetimes():
    fig, ax = plt.subplots(figsize=(9, 5))
    M = np.logspace(-0.7, 1.7, 200)
    t = 10 * M ** -2.5  # Gyr, t ~ 10 Gyr (M/Msun)^-2.5
    ax.plot(M, t, color=C[3], lw=2.5)
    ax.axhline(13.8, color=C[2], ls="--", lw=1.2)
    ax.text(0.25, 15.5, "Age of the universe ≈ 13.8 Gyr", color=C[2])
    for m, lab in [(1, "Sun ≈ 10 Gyr"), (10, "10 M☉ ≈ 30 Myr"), (0.5, "0.5 M☉ ≈ 57 Gyr")]:
        ax.scatter(m, 10 * m ** -2.5, color=C[1], zorder=5, s=60)
        ax.annotate(lab, (m, 10 * m ** -2.5), xytext=(10, 6), textcoords="offset points")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("Stellar mass (M☉)"); ax.set_ylabel("Main-sequence lifetime (Gyr)")
    ax.set_title("Heavier stars burn out faster  (t ≈ 10 Gyr · M^-2.5)")
    save(fig, out("stellar", "stellar_lifetime_generated.png"))


def exoplanet_milestones():
    fig, ax = plt.subplots(figsize=(9, 5))
    yrs = [1992, 1995, 2014, 2016, 2019, 2022, 2025]
    cnt = [3, 4, 1800, 3400, 4000, 5000, 6000]
    ax.plot(yrs, cnt, color=C[4], lw=2.5, marker="o", ms=8)
    notes = {1992: "Pulsar planets", 1995: "51 Peg b", 2016: "Kepler bulk\nvalidation",
             2019: "4,000", 2022: "5,000 (Mar)", 2025: "6,000 (Sep)"}
    for y, c in zip(yrs, cnt):
        if y in notes:
            ax.annotate(notes[y], (y, c), xytext=(-10, 12), textcoords="offset points", fontsize=10)
    ax.set_xlabel("Year"); ax.set_ylabel("Confirmed exoplanets")
    ax.set_title("Confirmed exoplanets (NASA Exoplanet Archive milestones)")
    ax.set_xlim(1990, 2027); ax.set_ylim(0, 6800)
    save(fig, out("stellar", "exoplanet_milestones_generated.png"))


# ---------------------------------------------------------------- planetary
def planet_sizes():
    fig, ax = plt.subplots(figsize=(10, 4.2))
    p = [("Mercury", .383, "#b7a99a"), ("Venus", .949, "#e8c27a"), ("Earth", 1, "#4f9cf0"),
         ("Mars", .532, "#d9643a"), ("Jupiter", 11.21, "#d8b08c"), ("Saturn", 9.45, "#e6cf8f"),
         ("Uranus", 4.01, "#8fd6e0"), ("Neptune", 3.88, "#4f6fe0")]
    x = 0
    for k, (n, r, c) in enumerate(p):
        x += r + 0.9
        ax.add_patch(plt.Circle((x, 0), r, color=c))
        y = -max(r, 1) - 1.3 - (3.2 if (k < 4 and k % 2) else 0)
        ax.text(x, y, f"{n}\n{r:g} R⊕", ha="center", va="top", fontsize=9)
        x += r
    ax.set_xlim(0, x + 1); ax.set_ylim(-15, 12.5); ax.set_aspect("equal")
    ax.axis("off"); ax.set_title("Planet radii to scale (Earth = 1)")
    save(fig, out("planetary", "planet_sizes_generated.png"))


def habitable_zones():
    fig, ax = plt.subplots(figsize=(9, 6))
    L = np.logspace(-4, 1.2, 200)
    inner, outer = 0.95 * np.sqrt(L), 1.67 * np.sqrt(L)
    ax.fill_betweenx(L, inner, outer, color=C[3], alpha=0.25, label="Conservative habitable zone (scaled)")
    pts = {"Venus": (0.723, 1), "Earth": (1, 1), "Mars": (1.524, 1),
           "Proxima b": (0.0485, 0.00155), "TRAPPIST-1e": (0.0293, 0.000553),
           "K2-18 b": (0.143, 0.0234)}
    for n, (a, l) in pts.items():
        ax.scatter(a, l, s=70, color=C[1] if n in ("Venus", "Earth", "Mars") else C[2],
                   edgecolor="white", lw=0.6, zorder=5)
        ax.annotate(n, (a, l), xytext=(7, 5), textcoords="offset points")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("Orbital distance (AU)"); ax.set_ylabel("Host-star luminosity (L☉)")
    ax.set_title("Habitable zones scale with √L")
    ax.legend(loc="upper left")
    save(fig, out("planetary", "habitable_zones_generated.png"))


# ---------------------------------------------------------------- cosmology
def energy_budget():
    fig, ax = plt.subplots(figsize=(7, 7))
    vals, labs = [68.5, 26.5, 4.9], ["Dark energy 68.5%", "Dark matter 26.5%", "Ordinary matter 4.9%"]
    w, _ = ax.pie(vals, colors=[C[4], C[0], C[1]], startangle=90,
                  wedgeprops=dict(width=0.38, edgecolor=BG, linewidth=3))
    ax.legend(w, labs, loc="lower center", bbox_to_anchor=(0.5, -0.08), ncol=1)
    ax.text(0, 0, "Today's\nuniverse", ha="center", va="center", fontsize=15, weight="bold")
    ax.set_title("Cosmic energy budget (Planck 2018, ΛCDM)")
    save(fig, out("cosmology", "energy_budget_generated.png"))


def dark_energy_evolution():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    z = np.linspace(0, 3, 300); a = 1 / (1 + z)
    def rho(w0, wa):  # CPL: rho/rho0 = a^{-3(1+w0+wa)} exp(-3 wa (1-a))
        return a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    ax.plot(z, np.ones_like(z), color=C[0], lw=2.5, label="Cosmological constant Λ (w = −1)")
    ax.plot(z, rho(-0.75, -0.86), color=C[2], lw=2.5,
            label="Evolving (w0 ≈ −0.75, wa ≈ −0.86, DESI-DR2-like)")
    ax.set_ylim(0.5, 1.25)
    ax.set_xlabel("Redshift z  (looking back in time →)")
    ax.set_ylabel("Dark-energy density / today's value")
    ax.set_title("Is dark energy weakening? Λ vs an evolving fit")
    ax.legend(loc="upper right")
    ax.text(1.6, 0.55, "Illustrative only — DESI 2025\npreference is 2.8–4.2σ,\nnot a 5σ discovery",
            color=MUTED, fontsize=10)
    save(fig, out("cosmology", "dark_energy_evolution_generated.png"))


def cosmic_timeline():
    fig, ax = plt.subplots(figsize=(11, 3.8))
    ev = [("~10⁻³² s", "Inflation"), ("3 min", "First nuclei\n(H, He)"),
          ("380,000 yr", "CMB released"), ("~100–200 Myr", "First stars"),
          ("~280 Myr", "JWST MoM-z14\n(z ≈ 14.4)"), ("9.2 Gyr", "Sun & Earth\nform"),
          ("13.8 Gyr", "Today")]
    xs = np.arange(len(ev))
    ax.plot(xs, np.zeros_like(xs), color=C[0], lw=3)
    for i, (t, l) in enumerate(ev):
        ax.scatter(i, 0, color=C[1], s=80, zorder=5)
        ax.text(i, 0.35, l, ha="center", va="bottom", fontsize=10, weight="bold")
        ax.text(i, -0.3, t, ha="center", va="top", fontsize=10, color=MUTED)
    ax.set_xlim(-0.6, len(ev) - 0.4); ax.set_ylim(-1, 1.3)
    ax.axis("off"); ax.set_title("Milestones after the Big Bang (not to scale)")
    save(fig, out("cosmology", "cosmic_timeline_generated.png"))


# ---------------------------------------------------------------- exploration
def mission_timeline():
    fig, ax = plt.subplots(figsize=(11, 6))
    D = lambda y, m, d=1: date(y, m, d).toordinal()
    rows = [  # (label, start, end, done?)
        ("Europa Clipper cruise", D(2024, 10, 14), D(2030, 4, 11), "active"),
        ("Tianwen-2 (Kamoʻoalewa)", D(2025, 5, 29), D(2027, 11, 29), "active"),
        ("Artemis II (crewed flyby)", D(2026, 4, 1), D(2026, 4, 10), "done"),
        ("Rubin LSST (10-yr survey)", D(2026, 6, 30), D(2030, 12, 31), "active"),
        ("Gaganyaan G1 (uncrewed)", D(2026, 11, 1), D(2026, 12, 31), "planned"),
        ("Artemis III (LEO docking test)", D(2027, 6, 1), D(2027, 9, 1), "planned"),
        ("Gaganyaan H1 (crewed)", D(2027, 4, 1), D(2027, 12, 31), "planned"),
        ("Chandrayaan-4 (sample return)", D(2027, 6, 1), D(2028, 6, 30), "planned"),
        ("Artemis IV (crewed landing)", D(2028, 1, 1), D(2028, 12, 31), "planned"),
        ("Chandrayaan-5 / LUPEX", D(2028, 1, 1), D(2029, 6, 30), "planned"),
    ]
    col = {"done": C[3], "active": C[0], "planned": C[1]}
    for i, (l, s, e, st) in enumerate(rows[::-1]):
        ax.barh(i, max(e - s, 25), left=s, color=col[st], alpha=0.95 if st != "planned" else 0.55,
                hatch=None if st != "planned" else "//", edgecolor=col[st])
    today = date(2026, 11, 15).toordinal()
    ax.axvline(today, color=C[2], lw=1.5, ls="--"); ax.text(today + 15, len(rows) - 0.6, "15 Nov 2026", color=C[2])
    ticks = [D(y, 1) for y in range(2024, 2031)]
    ax.set_xticks(ticks); ax.set_xticklabels(range(2024, 2031))
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows[::-1]], fontsize=10, color=FG)
    ax.set_xlim(D(2024, 6), D(2030, 12, 31))
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=col["done"], label="Completed"), Patch(color=col["active"], label="Active"),
                       Patch(facecolor=col["planned"], alpha=0.55, hatch="//", label="Planned / target")],
              loc="lower right")
    ax.set_title("Mission tracker timeline (status as of 15 Nov 2026)")
    save(fig, out("exploration", "mission_timeline_generated.png"))


MU_SUN = 1.32712440018e20  # m^3/s^2
AU = 1.495978707e11


def hohmann(r1, r2):
    a = (r1 + r2) / 2
    v1, v2 = np.sqrt(MU_SUN / r1), np.sqrt(MU_SUN / r2)
    dv1 = np.sqrt(MU_SUN / r1) * (np.sqrt(2 * r2 / (r1 + r2)) - 1)
    dv2 = np.sqrt(MU_SUN / r2) * (1 - np.sqrt(2 * r1 / (r1 + r2)))
    tof = np.pi * np.sqrt(a ** 3 / MU_SUN)
    return dv1, dv2, tof


def hohmann_figure():
    r1, r2 = 1.0, 1.524
    dv1, dv2, tof = hohmann(r1 * AU, r2 * AU)
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r1 * np.cos(th), r1 * np.sin(th), color=C[0], label="Earth orbit (1 AU)")
    ax.plot(r2 * np.cos(th), r2 * np.sin(th), color=C[2], label="Mars orbit (1.524 AU)")
    a, e = (r1 + r2) / 2, (r2 - r1) / (r2 + r1)
    t = np.linspace(0, np.pi, 200); r = a * (1 - e**2) / (1 + e * np.cos(t))
    ax.plot(r * np.cos(t), r * np.sin(t), color=C[1], lw=2.5, label="Hohmann transfer")
    ax.scatter(0, 0, s=300, color="#ffd34d", zorder=5)
    ax.scatter(r1, 0, color=C[0], s=80, zorder=6); ax.scatter(-r2, 0, color=C[2], s=80, zorder=6)
    ax.annotate(f"Δv₁ = {dv1/1000:.2f} km/s", (r1, 0), xytext=(10, -25), textcoords="offset points")
    ax.annotate(f"Δv₂ = {dv2/1000:.2f} km/s", (-r2, 0), xytext=(-40, 18), textcoords="offset points")
    ax.text(0, -0.35, f"Transfer time ≈ {tof/86400:.0f} days", ha="center", color=MUTED)
    ax.set_aspect("equal"); ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.9, 1.9)
    ax.set_xlabel("AU"); ax.set_ylabel("AU"); ax.legend(loc="lower left", fontsize=9)
    ax.set_title("Earth → Mars Hohmann transfer (heliocentric)")
    save(fig, out("exploration", "hohmann_earth_mars_generated.png"))
    return dv1, dv2, tof


def hohmann_gif():
    r1, r2 = 1.0, 1.524
    a, e = (r1 + r2) / 2, (r2 - r1) / (r2 + r1)
    T1, T2, Tt = 1.0, r2 ** 1.5, a ** 1.5  # years (Kepler III)
    tof = Tt / 2
    phase = np.pi - 2 * np.pi * tof / T2  # Mars lead angle at launch
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    th = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r1 * np.cos(th), r1 * np.sin(th), color=C[0], lw=0.8)
    ax.plot(r2 * np.cos(th), r2 * np.sin(th), color=C[2], lw=0.8)
    ax.scatter(0, 0, s=220, color="#ffd34d")
    ax.set_aspect("equal"); ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8); ax.axis("off")
    title = ax.set_title("")
    earth, = ax.plot([], [], "o", color=C[0], ms=9)
    mars, = ax.plot([], [], "o", color=C[2], ms=8)
    ship, = ax.plot([], [], "o", color=C[1], ms=5)
    trail, = ax.plot([], [], color=C[1], lw=1.8)
    n = 90; ts = np.linspace(0, tof, n); xs, ys = [], []

    def kepler_E(M):
        E = M.copy() if hasattr(M, "copy") else M
        for _ in range(30):
            E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
        return E

    def step(i):
        t = ts[i]
        ea = 2 * np.pi * t / T1; ma = phase + 2 * np.pi * t / T2
        E = kepler_E(2 * np.pi * t / Tt)
        nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
        r = a * (1 - e * np.cos(E))
        x, y = r * np.cos(nu), r * np.sin(nu); xs.append(x); ys.append(y)
        earth.set_data([r1 * np.cos(ea)], [r1 * np.sin(ea)])
        mars.set_data([r2 * np.cos(ma)], [r2 * np.sin(ma)])
        ship.set_data([x], [y]); trail.set_data(xs, ys)
        title.set_text(f"Earth → Mars Hohmann transfer   day {t*365.25:4.0f}")
        return earth, mars, ship, trail

    anim = animation.FuncAnimation(fig, step, frames=n, blit=False)
    p = out("gifs", "hohmann_transfer.gif")
    anim.save(p, writer=animation.PillowWriter(fps=15), dpi=90)
    plt.close(fig); print("wrote", os.path.relpath(p, ROOT))


# ---------------------------------------------------------------- astrobiology
def cold_scale():
    fig, ax = plt.subplots(figsize=(10, 6))
    levels = ["1  Detect a possible signal of life", "2  Rule out contamination",
              "3  Show biology could produce it here", "4  Rule out non-biological sources",
              "5  Independent, additional signal", "6  Rule out alternative hypotheses",
              "7  Follow-up predictions confirmed"]
    for i, l in enumerate(levels):
        ax.barh(i, 1, color=C[0], alpha=0.12 + 0.11 * i, edgecolor=BG)
        ax.text(0.02, i, l, va="center", fontsize=10.5)
    cases = [("K2-18 b DMS/DMDS", 0.0, C[2]), ("Venus phosphine", 0.0, C[1]),
             ("Mars 'Sapphire Canyon'\nleopard spots", 0.0, C[3]), ("Enceladus plume\norganics & phosphates", 0.0, C[4])]
    ys = [0.15, -0.15, 0.25, -0.25]
    xs = [0.62, 0.62, 0.84, 0.84]
    for (n, _, c), y, x in zip(cases, ys, xs):
        ax.scatter(x, y, s=120, color=c, edgecolor="white", zorder=5)
        ax.annotate(n, (x, y), xytext=(0, -28 if y < 0 else 16), textcoords="offset points",
                    ha="center", fontsize=8.5, color=c)
    ax.set_xlim(0, 1); ax.set_ylim(-1.2, 6.6); ax.set_xticks([]); ax.set_yticks([])
    ax.grid(False)
    ax.set_title("Confidence of Life Detection (CoLD) ladder — every current claim sits at level 1")
    save(fig, out("astrobiology", "cold_scale_generated.png"))


# ---------------------------------------------------------------- small bodies
def interstellar_objects():
    objs = [("1I/ʻOumuamua (2017)", 1.20, 26.3), ("2I/Borisov (2019)", 3.36, 32.2), ("3I/ATLAS (2025)", 6.1, 58.0)]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
    names = [o[0] for o in objs]
    a1.bar(names, [o[1] for o in objs], color=[C[5], C[0], C[2]])
    a1.axhline(1, color=C[1], ls="--"); a1.text(-0.4, 1.15, "e = 1: escape threshold", color=C[1], fontsize=9)
    a1.set_ylabel("Orbital eccentricity e"); a1.set_title("How unbound?")
    a2.bar(names, [o[2] for o in objs], color=[C[5], C[0], C[2]])
    a2.set_ylabel("Speed far from the Sun, v∞ (km/s)"); a2.set_title("How fast?")
    for a in (a1, a2):
        a.tick_params(axis="x", labelsize=9)
    fig.suptitle("The three known interstellar objects", fontweight="bold")
    save(fig, out("small-bodies", "interstellar_objects_generated.png"))


def hyperbolic_orbit():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    th = np.linspace(0, 2 * np.pi, 300)
    for r, c, n in [(1.0, C[0], "Earth"), (1.524, C[2], "Mars"), (5.2, C[1], "Jupiter")]:
        ax.plot(r * np.cos(th), r * np.sin(th), color=c, lw=1, alpha=0.7)
        ax.text(r * 0.72, r * 0.72, n, color=c, fontsize=9)
    q, e = 1.36, 6.1
    p_ = q * (1 + e); nu_max = np.arccos(-1 / e) - 0.02
    nu = np.linspace(-nu_max * 0.97, nu_max * 0.97, 400); r = p_ / (1 + e * np.cos(nu))
    m = r < 7
    ax.plot((r * np.cos(nu))[m], (r * np.sin(nu))[m], color=C[2], lw=2.5, label="3I/ATLAS (e ≈ 6.1, q ≈ 1.36 AU)")
    ax.scatter(0, 0, color="#ffd34d", s=200, zorder=5); ax.scatter(q, 0, color=C[2], s=50, zorder=6)
    ax.annotate("Perihelion 29 Oct 2025", (q, 0), xytext=(10, -18), textcoords="offset points", fontsize=9)
    ax.set_aspect("equal"); ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_xlabel("AU"); ax.set_ylabel("AU")
    ax.legend(loc="lower left", fontsize=9); ax.set_title("A one-way pass: 3I/ATLAS's hyperbolic path")
    save(fig, out("small-bodies", "hyperbolic_orbit_3i_generated.png"))


# ---------------------------------------------------------------- black holes / GW
def gw250114():
    G, c, Ms = 6.674e-11, 2.998e8, 1.989e30
    def area_km2(M, chi=0.0):  # Kerr horizon area A = 8 pi (GM/c^2)^2 (1 + sqrt(1 - chi^2))
        rg = G * M * Ms / c ** 2
        return 8 * np.pi * rg ** 2 * (1 + np.sqrt(1 - chi ** 2)) / 1e6
    a1, a2 = area_km2(33.6), area_km2(32.2)
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.bar(["BH 1\n33.6 M☉", "BH 2\n32.2 M☉"], [a1, a2], color=[C[0], C[4]])
    ax.bar(["Before\n(sum)"], [a1 + a2], color=C[5])
    ax.bar(["After\n(remnant)"], [400000], color=C[2])
    for i, v in enumerate([a1, a2, a1 + a2, 400000]):
        ax.text(i, v + 6000, f"{v/1000:,.0f}k km²", ha="center", weight="bold")
    ax.set_ylabel("Event-horizon area (km²)")
    ax.set_title("GW250114: total horizon area grew (Hawking's area law)")
    ax.text(0.02, 0.92, "Pre-merger areas: non-spinning Kerr estimate from published masses\nRemnant ≈ 400,000 km² as reported by LVK coverage",
            transform=ax.transAxes, fontsize=8.5, color=MUTED)
    save(fig, out("black-holes-gw", "gw250114_area_law_generated.png"))


def chirp():
    t = np.linspace(-0.25, 0.02, 4000)
    tc = 0.0
    tau = np.clip(tc - t, 1e-4, None)
    f = 30 * (tau / 0.25) ** (-3 / 8)
    phase = 2 * np.pi * np.cumsum(f) * (t[1] - t[0])
    amp = np.where(t < tc, (tau / 0.25) ** (-1 / 4), np.exp(-(t - tc) / 0.004) * (1e-4 / 0.25) ** (-1 / 4) * 0)
    ring = np.where(t >= tc, np.exp(-(t - tc) / 0.004) * np.cos(2 * np.pi * 250 * (t - tc)), 0)
    h = np.where(t < tc, amp * np.cos(phase), 0) / 12 + ring * 0.9
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t * 1000, h, color=C[0], lw=1)
    ax.set_xlabel("Time relative to merger (ms)"); ax.set_ylabel("Strain (arbitrary units)")
    ax.text(-240, 0.8, "Inspiral: frequency and amplitude rise (chirp)", color=MUTED, fontsize=9)
    ax.text(2, 0.8, "Ringdown", color=C[2], fontsize=9)
    ax.set_title("Schematic binary black-hole chirp (Newtonian inspiral + damped ringdown)")
    save(fig, out("black-holes-gw", "chirp_schematic_generated.png"))


# ---------------------------------------------------------------- heliophysics
def sun_distances():
    # all measured from the Sun's CENTRE (Parker's surface distances + 0.7 million km solar radius)
    rows = [("Mercury (perihelion)", 46.0), ("Helios 2 (1976 record)", 43.4), ("Parker Solar Probe, 2023", 7.96),
            ("Parker Solar Probe, Dec 2024", 6.8)]
    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.barh([r[0] for r in rows], [r[1] for r in rows], color=[MUTED, C[5], C[0], C[2]])
    for i, (_, d) in enumerate(rows):
        ax.text(d + 0.6, i, f"{d} million km", va="center")
    ax.set_xlim(0, 56); ax.invert_yaxis()
    ax.set_xlabel("Closest distance from the Sun's centre (million km)")
    ax.text(30, 3.3, "Parker: 6.1 million km from the surface", color=MUTED, fontsize=9)
    ax.set_title("Getting close to a star")
    save(fig, out("heliophysics", "sun_approach_records_generated.png"))


def h0_tension():
    rows = [("Planck CMB + ΛCDM", 67.4, 0.5, C[4]), ("CCHP TRGB+JWST (Freedman 2025)", 70.39, 1.9, C[1]),
            ("CCHP Cepheids subset", 72.04, 2.0, C[5]), ("SH0ES Cepheids+JWST (Riess)", 73.2, 1.0, C[2])]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    for i, (n, v, e, c) in enumerate(rows):
        ax.errorbar(v, i, xerr=e, fmt="o", color=c, ms=9, capsize=5, lw=2)
        ax.text(v, i + 0.25, f"{v}", ha="center", fontsize=10)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows])
    ax.axvspan(66.9, 67.9, color=C[4], alpha=0.12); ax.axvspan(72.2, 74.2, color=C[2], alpha=0.12)
    ax.set_xlabel("H₀ (km/s/Mpc)"); ax.set_xlim(64, 77); ax.invert_yaxis()
    ax.set_title("The Hubble tension: early-universe vs local measurements")
    ax.text(74.4, -0.35, "1σ error bars, rounded", fontsize=8.5, color=MUTED)
    save(fig, out("cosmology", "hubble_tension_generated.png"))


if __name__ == "__main__":
    hr_diagram(); stellar_lifetimes(); exoplanet_milestones()
    planet_sizes(); habitable_zones()
    energy_budget(); dark_energy_evolution(); cosmic_timeline()
    mission_timeline(); dv = hohmann_figure(); hohmann_gif()
    cold_scale()
    interstellar_objects(); hyperbolic_orbit(); gw250114(); chirp(); sun_distances(); h0_tension()
    print("Hohmann Earth->Mars: dv1=%.3f km/s dv2=%.3f km/s tof=%.1f d" % (dv[0]/1e3, dv[1]/1e3, dv[2]/86400))
