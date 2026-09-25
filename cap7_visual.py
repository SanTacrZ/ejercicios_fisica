"""Capítulo 7 - Edición visual paso a paso (motor de figuras de fisica_base).

Tema: energía potencial gravitacional y conservación de la energía.
La idea visual central es seguir a dónde va la energía: la altura se vuelve
rapidez, y el trabajo de cada fuerza se lee en el diagrama.

Render de una escena:
    manim -ql cap7_visual.py P7_1
Render del lote:
    manim -ql cap7_visual.py

LOTE 1 (orden de la lista): 7.1, 7.3, 7.5, 7.6, 7.9
PENDIENTES cap7:
    11, 13, 15, 16, 17, 19, 23, 30, 34, 36, 37, 41, 42, 43,
    45, 46, 49, 53, 55, 56, 57, 59, 63, 64, 66, 67, 68, 70, 73, 77, 87
"""

import numpy as np

from manim import *
from fisica_base import ProblemaScene, Figura


def p(x, y):
    return np.array([x, y, 0.0])


class Cap7Scene(ProblemaScene):
    encabezado = "CAPÍTULO 7  //  ENERGÍA POTENCIAL Y CONSERVACIÓN"
    subtitulo = "Energía potencial y conservación"


class P7_1(Cap7Scene):
    numero = "7.1"
    titulo = "Cambio de energía potencial del alpinista"
    lista_datos = [
        ("Masa del alpinista:", r"m = 75\ \mathrm{kg}"),
        ("Día 1:", r"1500\ \mathrm{m} \to 2400\ \mathrm{m}"),
        ("Día 2:", r"2400\ \mathrm{m} \to 1350\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()

        def y(h):
            return -2.2 + (h - 1300) * 0.0035

        self.f_linea(fig, "eje", p(-2.5, -2.3), p(-2.5, 1.9), color=self.MUTED, grosor=3)
        for h, nombre in [(1350, "t1350"), (1500, "t1500"), (2400, "t2400")]:
            self.f_linea(fig, nombre, p(-2.5, y(h)), p(-2.0, y(h)),
                         color=self.WHITE, grosor=3)
            self.f_texto(fig, "et" + nombre, f"{h}", (-1.55, y(h), 0), size=22,
                         color=self.WHITE)
        self.f_cuerpo(fig, "a1500", p(-0.6, y(1500)), forma="punto", color=self.CYAN)
        self.f_cuerpo(fig, "a2400", p(-0.6, y(2400)), forma="punto", color=self.GREEN)
        self.f_cuerpo(fig, "a1350", p(-0.6, y(1350)), forma="punto", color=self.YELLOW)
        self.f_vector(fig, "sube", p(-0.6, y(1500)), UP, y(2400) - y(1500),
                      color=self.GREEN, etiqueta=r"\Delta U > 0", lado=RIGHT,
                      etiqueta_size=22)
        self.f_vector(fig, "baja", p(0.35, y(2400)), DOWN, y(2400) - y(1350),
                      color=self.YELLOW, etiqueta=r"\Delta U < 0", lado=RIGHT,
                      etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Dos días en el risco",
            "revelar": ["eje", "t1350", "ett1350", "t1500", "ett1500", "t2400",
                        "ett2400", "a1500", "a2400", "a1350"],
            "text": ["La energía potencial solo depende de la altura, no del camino."],
        },
        {
            "titulo": "a) Primer día: subida",
            "revelar": ["sube"],
            "math": [
                r"\Delta U = mg(2400-1500) = (75)(9.80)(900)",
                r"\Delta U = +6.62\times10^5\ \mathrm{J}",
            ],
            "resaltar": ["sube"],
        },
        {
            "titulo": "b) Segundo día: bajada",
            "revelar": ["baja"],
            "math": [
                r"\Delta U = mg(1350-2400) = (75)(9.80)(-1050)",
                r"\Delta U = -7.72\times10^5\ \mathrm{J}",
            ],
            "resaltar": ["baja"],
        },
    ]
    resultado_latex = r"\Delta U_a = +6.62\times10^5\ \mathrm{J}, \quad \Delta U_b = -7.72\times10^5\ \mathrm{J}"


class P7_3(Cap7Scene):
    numero = "7.3"
    titulo = "Saco de correo desplazado lateralmente"
    lista_datos = [
        ("Masa del saco:", r"m = 120\ \mathrm{kg}"),
        ("Longitud de la cuerda:", r"L = 3.5\ \mathrm{m}"),
        ("Desplazamiento lateral:", r"x = 2.0\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        O = p(0.0, 1.8)
        L = 2.2
        sinT = 2.0 / 3.5
        cosT = np.sqrt(1.0 - sinT ** 2)
        B = O + L * np.array([sinT, -cosT, 0.0])
        A0 = O + L * DOWN
        self.f_linea(fig, "techo", p(-2.2, 1.8), p(2.2, 1.8), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "pivote", O, forma="punto", color=self.WHITE)
        self.f_linea(fig, "cuerdaV", O, A0, color=self.MUTED, grosor=3,
                     discontinuo=True)
        self.f_linea(fig, "cuerda", O, B, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "saco", B, ancho=0.9, alto=0.7,
                      color=self.BLUE, etiqueta="saco")
        self.f_angulo(fig, "theta", O, O + DOWN, B, radio=0.55,
                      etiqueta=r"\theta", etiqueta_size=22)
        self.f_vector(fig, "F", B, RIGHT, 1.0, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "T", B, O - B, 0.95, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "h", p(-0.9, A0[1]), p(-0.9, B[1]),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"h", lado=LEFT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El saco cuelga desplazado un ángulo θ",
            "revelar": ["techo", "pivote", "cuerdaV", "cuerda", "saco", "theta"],
            "math": [r"\sin\theta = \dfrac{2.0}{3.5} = 0.571 \;\Rightarrow\; \theta = 34.8^\circ"],
        },
        {
            "titulo": "a) Fuerza horizontal para sostenerlo",
            "revelar": ["F", "T"],
            "math": [
                r"F = mg\tan\theta = (120)(9.80)(0.696)",
                r"F = 819\ \mathrm{N}",
            ],
            "resaltar": ["F"],
        },
        {
            "titulo": "b) Trabajo de la cuerda y del trabajador",
            "revelar": ["h"],
            "math": [
                r"W_{\mathrm{cuerda}} = 0",
                r"W = mgh = mgL(1-\cos\theta) = 738\ \mathrm{J}",
            ],
            "text": ["La tensión es perpendicular al arco: no trabaja."],
            "resaltar": ["h"],
        },
    ]
    resultado_latex = r"F = 819\ \mathrm{N}, \quad W_{\mathrm{cuerda}} = 0, \quad W = 738\ \mathrm{J}"


class P7_5(Cap7Scene):
    numero = "7.5"
    titulo = "Pelota lanzada desde una azotea"
    lista_datos = [
        ("Altura del edificio:", r"h = 22.0\ \mathrm{m}"),
        ("Rapidez inicial:", r"v_0 = 12.0\ \mathrm{m/s},\ 53.1^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-3.4, -1.8), p(3.2, -1.8), color=self.MUTED, grosor=4)
        edif = Rectangle(width=1.6, height=3.0, color=self.MUTED, stroke_width=3,
                         fill_color=self.PANEL, fill_opacity=0.9).move_to(p(-2.4, -0.3))
        fig.registrar("edificio", edif, lambda m: Create(m))
        R0 = p(-1.6, 1.2)
        self.f_cuerpo(fig, "pelota", R0, forma="punto", color=self.WHITE)
        up = np.array([np.cos(np.deg2rad(53.1)), np.sin(np.deg2rad(53.1)), 0.0])
        dn = np.array([np.cos(np.deg2rad(53.1)), -np.sin(np.deg2rad(53.1)), 0.0])
        self.f_vector(fig, "vUp", R0, up, 1.1, color=self.CYAN,
                      etiqueta=r"v_0", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "vDn", R0, dn, 1.1, color=self.GREEN,
                      etiqueta=r"v_0", lado=DOWN, etiqueta_size=22)
        t1 = Arc(radius=2.2, start_angle=75 * DEGREES, angle=70 * DEGREES,
                 color=self.CYAN, stroke_width=3).move_to(p(-0.4, -1.0))
        fig.registrar("trayA", t1, lambda m: Create(m))
        t2 = Arc(radius=1.6, start_angle=20 * DEGREES, angle=60 * DEGREES,
                 color=self.GREEN, stroke_width=3).move_to(p(-0.5, -1.3))
        fig.registrar("trayB", t2, lambda m: Create(m))
        self.f_linea(fig, "h", p(1.5, -1.8), p(1.5, 1.2),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"22", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Lanzamiento a 53.1° sobre la horizontal",
            "revelar": ["suelo", "edificio", "pelota", "vUp", "h"],
            "text": ["Con energía basta la rapidez inicial y el desnivel."],
        },
        {
            "titulo": "a) Rapidez justo antes de tocar el suelo",
            "revelar": ["trayA"],
            "math": [
                r"\tfrac12 mv_0^2 + mgh = \tfrac12 mv^2",
                r"v = \sqrt{12.0^2 + 2(9.80)(22.0)} = 24.0\ \mathrm{m/s}",
            ],
            "resaltar": ["trayA"],
        },
        {
            "titulo": "b) Y si se lanza hacia abajo",
            "revelar": ["vDn", "trayB"],
            "math": [r"v = 24.0\ \mathrm{m/s}"],
            "text": ["La misma rapidez: la energía no ve la dirección."],
            "resaltar": ["trayB"],
        },
        {
            "titulo": "c) Con resistencia del aire",
            "math": [r"v_b > v_a"],
            "text": ["La del inciso (b) vuela menos tiempo y pierde menos energía."],
        },
    ]
    resultado_latex = r"v_a = v_b = 24.0\ \mathrm{m/s}\ (\text{sin aire})"


class P7_6(Cap7Scene):
    numero = "7.6"
    titulo = "Rapidez al pie de una rampa (dos niveles cero)"
    lista_datos = [
        ("Masa de la caja:", r"M"),
        ("Ángulo de la rampa:", r"\alpha"),
        ("Distancia recorrida:", r"d"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(30.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.0, -1.5)
        B = A + 4.2 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=6)
        self.f_angulo(fig, "alpha", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"\alpha", etiqueta_size=22)
        C = A + 3.3 * u + 0.38 * n
        g = self.f_cuerpo(fig, "caja", C, ancho=1.1, alto=0.7,
                          color=self.BLUE, etiqueta="caja")
        g[0].rotate(th, about_point=C)
        self.f_linea(fig, "nivelBase", p(A[0] - 0.4, A[1]), p(B[0] + 0.4, A[1]),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"U = 0\ (a)", lado=RIGHT, etiqueta_size=20)
        self.f_linea(fig, "nivelCima", p(B[0] - 1.6, B[1]), p(B[0] + 0.4, B[1]),
                     color=self.YELLOW, grosor=2, discontinuo=True,
                     etiqueta=r"U = 0\ (b)", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "v", C, u, 1.0, color=self.CYAN,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La caja baja por la rampa lisa",
            "revelar": ["rampa", "alpha", "caja"],
            "text": ["Sin fricción: la energía mecánica se conserva."],
        },
        {
            "titulo": "a) Cero de energía en la base",
            "revelar": ["nivelBase", "v"],
            "math": [
                r"mgd\sin\alpha + 0 = \tfrac12 mv^2 + 0",
                r"v = \sqrt{2gd\sin\alpha}",
            ],
            "resaltar": ["nivelBase"],
        },
        {
            "titulo": "b) Cero de energía en la cima",
            "revelar": ["nivelCima"],
            "math": [
                r"0 + 0 = \tfrac12 mv^2 - mgd\sin\alpha",
                r"v = \sqrt{2gd\sin\alpha}",
            ],
            "text": ["El mismo resultado: el cero de U es arbitrario."],
            "resaltar": ["nivelCima"],
        },
        {
            "titulo": "c) ¿Y la fuerza normal?",
            "math": [r"W_N = 0"],
            "text": ["Es perpendicular al desplazamiento en todo punto."],
        },
    ]
    resultado_latex = r"v = \sqrt{2gd\sin\alpha}\ \text{(igual en a) y b)}"


class P7_9(Cap7Scene):
    numero = "7.9"
    titulo = "Piedra que se desliza en un tazón"
    lista_datos = [
        ("Masa de la piedra:", r"m = 0.20\ \mathrm{kg}"),
        ("Radio del tazón:", r"R = 0.50\ \mathrm{m}"),
        ("Trabajo de la fricción:", r"W_f = -0.22\ \mathrm{J}"),
    ]

    def crear_figura(self):
        fig = Figura()
        C = p(0.0, 0.6)
        radio = 1.6
        tazon = Arc(radius=radio, start_angle=180 * DEGREES, angle=180 * DEGREES,
                    color=self.BLUE, stroke_width=7).move_to(C)
        fig.registrar("tazon", tazon, lambda m: Create(m))
        A = C + p(-radio, 0.0)
        B = C + p(0.0, -radio)
        self.f_cuerpo(fig, "piedraA", A, forma="punto", color=self.WHITE)
        self.f_cuerpo(fig, "piedraB", B, forma="punto", color=self.YELLOW)
        self.f_linea(fig, "radioR", C, A, color=self.GREEN,
                     grosor=2, discontinuo=True, etiqueta=r"R", lado=UP,
                     etiqueta_size=22)
        self.f_vector(fig, "N", B, UP, 1.0, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", B, DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "fk", A + DOWN * 0.35, UP, 0.65, color=self.YELLOW,
                      etiqueta=r"f", lado=LEFT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "La piedra se desliza del borde al fondo",
            "revelar": ["tazon", "piedraA", "radioR"],
            "text": ["Cae una altura R y la fricción le roba 0.22 J."],
        },
        {
            "titulo": "a) Trabajo de la normal y del peso",
            "math": [
                r"W_N = 0",
                r"W_g = mgR = (0.20)(9.80)(0.50) = 0.98\ \mathrm{J}",
            ],
            "text": ["La normal es perpendicular al movimiento en todo punto."],
        },
        {
            "titulo": "b) Rapidez en el fondo B",
            "revelar": ["piedraB", "fk"],
            "math": [
                r"K_B = 0.98 - 0.22 = 0.76\ \mathrm{J}",
                r"v_B = \sqrt{2(0.76)/0.20} = 2.76\ \mathrm{m/s}",
            ],
            "resaltar": ["piedraB"],
        },
        {
            "titulo": "c) Normal en el fondo",
            "revelar": ["N", "w"],
            "math": [
                r"N - mg = \dfrac{mv_B^2}{R}",
                r"N = 1.96 + 3.04 = 5.00\ \mathrm{N}",
            ],
            "resaltar": ["N"],
        },
    ]
    resultado_latex = r"W_N = 0,\ W_g = 0.98\ \mathrm{J},\ v_B = 2.76\ \mathrm{m/s},\ N = 5.00\ \mathrm{N}"