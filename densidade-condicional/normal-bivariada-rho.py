"""Build a compact, vector wireframe comparison for the bivariate normal."""

import argparse
import os
from pathlib import Path
import tempfile


# Keep Matplotlib's caches writable when this script runs in a restricted sandbox.
_CACHE_ROOT = Path(tempfile.gettempdir()) / "mprob-matplotlib-cache"
_CACHE_ROOT.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_CACHE_ROOT / "config"))
os.environ.setdefault("XDG_CACHE_HOME", str(_CACHE_ROOT / "xdg"))

import matplotlib as mpl
mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from matplotlib.path import Path as MplPath
from mpl_toolkits.mplot3d import proj3d


TEAL = "#abcfcb"
RED = "#c4473a"
MUTED = "#57534e"
TEXT = "#1c1917"
RHO_VALUES = (0.0, 0.8)
LIM = 3.2
ZLIM = 0.29
RHO08_Y_LABEL_ALONG_AXIS = 0.68
RHO08_Y_LABEL_NORMAL_OFFSET = 0.03

mpl.rcParams.update(
    {
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage[T1]{fontenc}\usepackage{lmodern}",
        "font.family": "serif",
        "font.size": 11,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.compression": 9,
    }
)


def density(rho: float, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Standard bivariate-normal density with correlation rho."""
    denominator = 1.0 - rho**2
    quadratic = x**2 - 2.0 * rho * x * y + y**2
    return np.exp(-quadratic / (2.0 * denominator)) / (
        2.0 * np.pi * np.sqrt(denominator)
    )


def axes_fraction(ax, point: tuple[float, float, float]) -> np.ndarray:
    """Project a 3D point to the 2D axes coordinate system."""
    x2d, y2d, _ = proj3d.proj_transform(*point, ax.get_proj())
    return ax.transAxes.inverted().transform(ax.transData.transform((x2d, y2d)))


class TikzStealthArrow(mpl.patches.ArrowStyle._Base):
    """A filled arrowhead with TikZ's concave Stealth silhouette."""

    def transmute(self, path, mutation_size, linewidth):
        start, end = path.vertices[-2:]
        direction = end - start
        direction /= np.linalg.norm(direction)
        normal = np.array([-direction[1], direction[0]])

        length = 0.55 * mutation_size
        width = 0.75 * length
        inset = 0.325 * length
        base = end - length * direction
        notch = base + inset * direction
        vertices = np.array(
            [
                end,
                base + 0.5 * width * normal,
                notch,
                base - 0.5 * width * normal,
                end,
            ]
        )
        codes = [
            MplPath.MOVETO,
            MplPath.LINETO,
            MplPath.LINETO,
            MplPath.LINETO,
            MplPath.CLOSEPOLY,
        ]
        return MplPath(vertices, codes), True


def add_stealth_arrow(ax, start: tuple[float, float, float],
                      end: tuple[float, float, float]) -> None:
    """Draw a screen-sized TikZ-Stealth arrowhead at a projected 3D axis tip."""
    start_2d = axes_fraction(ax, start)
    end_2d = axes_fraction(ax, end)
    direction = end_2d - start_2d
    direction /= np.linalg.norm(direction)
    arrow = FancyArrowPatch(
        end_2d - 0.05 * direction,
        end_2d,
        transform=ax.transAxes,
        arrowstyle=TikzStealthArrow(),
        mutation_scale=11,
        linewidth=0.65,
        color=MUTED,
        shrinkA=0,
        shrinkB=0,
        clip_on=False,
        zorder=10,
    )
    ax.figure.add_artist(arrow)


def add_panel(
    ax, rho: float, X: np.ndarray, Y: np.ndarray, stride: int, elev: float, azim: float
) -> None:
    Z = density(rho, X, Y)
    ax.set_axis_off()
    ax.set_proj_type("ortho")
    ax.view_init(elev=elev, azim=azim)
    ax.set_box_aspect((1.0, 1.0, 0.65))
    ax.set_xlim(-3.45, 3.45)
    ax.set_ylim(-3.45, 3.45)
    ax.set_zlim(0.0, ZLIM)

    # Smooth curves in both coordinate directions, evaluated on a fine grid.
    ax.plot_wireframe(
        X,
        Y,
        Z,
        rstride=stride,
        cstride=stride,
        color=TEAL,
        linewidth=0.62,
        antialiased=True,
    )

    if rho == RHO_VALUES[1]:
        # Highlight the x=0.5 section on the right panel only.
        section_y = np.linspace(-LIM, LIM, 401)
        for section_x_value in (0.5,):
            section_x = np.full_like(section_y, section_x_value)
            ax.plot(
                section_x,
                section_y,
                density(rho, section_x, section_y),
                color=RED,
                linewidth=1.5,
                antialiased=True,
                zorder=10,
            )

        # Add the y=-1 section, offset from the x=0.5 section.
        section_x = np.linspace(-LIM, LIM, 401)
        section_y = np.full_like(section_x, -1.0)
        ax.plot(
            section_x,
            section_y,
            density(rho, section_x, section_y),
            color=RED,
            linewidth=1.5,
            antialiased=True,
            zorder=10,
        )

    # Plain axis lines without arrowheads or enclosing planes.
    edge = 3.32
    axis_style = {"color": MUTED, "linewidth": 0.65, "solid_capstyle": "round"}
    ax.plot([-edge, edge], [-edge, -edge], [0.0, 0.0], **axis_style)
    ax.plot([-edge, -edge], [-edge, edge], [0.0, 0.0], **axis_style)
    ax.plot([-edge, -edge], [-edge, -edge], [0.0, ZLIM], **axis_style)
    for start, end in (
        ((-edge, -edge, 0.0), (edge, -edge, 0.0)),
        ((-edge, -edge, 0.0), (-edge, edge, 0.0)),
        ((-edge, -edge, 0.0), (-edge, -edge, ZLIM)),
    ):
        add_stealth_arrow(ax, start, end)

    # Keep all labels horizontal and close to their projected axis endpoints.
    ax.text2D(0.5, -0.035, rf"$\rho={rho:g}$", transform=ax.transAxes,
              ha="center", va="top", color=TEXT, fontsize=14, clip_on=False)

    origin = axes_fraction(ax, (-edge, -edge, 0.0))
    for point, label in (((edge, -edge, 0.0), r"$x$"),
                         ((-edge, edge, 0.0), r"$y$")):
        tip = axes_fraction(ax, point)
        direction = tip - origin
        direction /= np.linalg.norm(direction)
        label_position = tip + 0.045 * direction
        if rho == RHO_VALUES[1] and label == r"$y$":
            normal = np.array([-direction[1], direction[0]])
            label_position = origin + RHO08_Y_LABEL_ALONG_AXIS * (tip - origin)
            label_position += RHO08_Y_LABEL_NORMAL_OFFSET * normal
        ax.text2D(label_position[0], label_position[1], label,
                  transform=ax.transAxes, ha="center", va="center",
                  color=TEXT, fontsize=11)

    if rho == RHO_VALUES[0]:
        z_tip = axes_fraction(ax, (-edge, -edge, ZLIM))
        z_base = axes_fraction(ax, (-edge, -edge, 0.0))
        z_direction = z_tip - z_base
        z_direction /= np.linalg.norm(z_direction)
        z_left = np.array([-z_direction[1], z_direction[0]])
        label_position = z_tip + 0.045 * z_left
        ax.text2D(label_position[0], label_position[1], r"$f(x,y)$",
                  transform=ax.transAxes, ha="right", va="center",
                  color=TEXT, fontsize=11)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stride",
        type=int,
        default=4,
        help="distance between wireframe curves in the 121-point grid (default: 4)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_suffix(".pdf"),
        help="output PDF path",
    )
    parser.add_argument("--elev", type=float, default=28, help="camera elevation angle")
    parser.add_argument("--azim", type=float, default=330, help="camera azimuth angle")
    parser.add_argument(
        "--rho08-azim-offset",
        type=float,
        default=-20,
        help="additional camera azimuth for the rho=0.8 panel",
    )
    args = parser.parse_args()
    if args.stride < 1:
        parser.error("--stride must be a positive integer")

    grid = np.linspace(-LIM, LIM, 121)
    X, Y = np.meshgrid(grid, grid)

    fig = plt.figure(figsize=(8.2, 3.7), facecolor="white")
    axes = (fig.add_subplot(1, 2, 1, projection="3d"),
            fig.add_subplot(1, 2, 2, projection="3d"))
    fig.subplots_adjust(left=0.035, right=0.995, bottom=0.035,
                        top=0.94, wspace=0.005)

    for ax, rho in zip(axes, RHO_VALUES):
        panel_azim = args.azim
        if rho == 0.8:
            panel_azim += args.rho08_azim_offset
        add_panel(ax, rho, X, Y, args.stride, args.elev, panel_azim)

    fig.savefig(args.output, format="pdf", bbox_inches="tight", pad_inches=0.025)
    plt.close(fig)
    print(args.output)


if __name__ == "__main__":
    main()
