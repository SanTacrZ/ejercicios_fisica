"""Capítulo 7 - Edición visual paso a paso (motor de figuras de fisica_base).

Tema: energía potencial gravitacional y conservación de la energía.
La idea visual central es seguir a dónde va la energía: la altura se vuelve
rapidez, y el trabajo de cada fuerza se lee en el diagrama.

Render de una escena:
    manim -ql cap7_visual.py P7_1
Render del lote:
    manim -ql cap7_visual.py

LOTE 1 (orden de la lista): 7.1, 7.3, 7.5, 7.6, 7.9
LOTE 2 (orden de la lista): 7.11, 7.13, 7.15, 7.16, 7.17
LOTE 3 (orden de la lista): 7.19, 7.23, 7.30, 7.34, 7.36
PENDIENTES cap7:
    37, 41, 42, 43, 45, 46, 49, 53, 55, 56, 57, 59, 63, 64, 66, 67, 68, 70, 73, 77, 87
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


class P7_11(Cap7Scene):
    numero = "7.11"
    titulo = "Trabajo de la fricción en un rizo"
    lista_datos = [
        ("Masa del carrito:", r"m = 120\ \mathrm{kg}"),
        ("Radio del rizo:", r"R = 12.0\ \mathrm{m}"),
        ("Rapidez en A / B:", r"v_A = 25.0,\ v_B = 8.0\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        centro = p(0.0, 0.1)
        radio = 2.1
        aro = Circle(radius=radio, color=self.BLUE, stroke_width=7).move_to(centro)
        fig.registrar("aro", aro, lambda m: Create(m))
        A = centro + DOWN * radio
        B = centro + UP * radio
        self.f_cuerpo(fig, "cartA", A, ancho=0.85, alto=0.6,
                      color=self.BLUE, etiqueta="A")
        self.f_cuerpo(fig, "cartB", B, ancho=0.85, alto=0.6,
                      color=self.GREEN, etiqueta="B")
        self.f_vector(fig, "vA", A, RIGHT, 1.2, color=self.CYAN,
                      etiqueta=r"25", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "vB", B, LEFT, 0.6, color=self.CYAN,
                      etiqueta=r"8", lado=UP, etiqueta_size=20)
        self.f_vector(fig, "fk", A + UP * 0.35, LEFT, 0.9, color=self.YELLOW,
                      etiqueta=r"f", lado=UP, etiqueta_size=22)
        self.f_linea(fig, "h", p(2.0, A[1]), p(2.0, B[1]),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"2R", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El carrito sube del punto A al B",
            "revelar": ["aro", "cartA", "cartB", "vA", "vB", "h"],
            "text": ["Gana altura pero pierde más rapidez de la cuenta: hay fricción."],
        },
        {
            "titulo": "Energía mecánica en A y en B",
            "math": [
                r"K_A = \tfrac12(120)(25.0)^2 = 37500\ \mathrm{J}",
                r"K_B + U_B = \tfrac12(120)(8.0)^2 + (120)(9.80)(24.0)",
                r"= 3840 + 28224 = 32064\ \mathrm{J}",
            ],
        },
        {
            "titulo": "Lo que falta lo hizo la fricción",
            "revelar": ["fk"],
            "math": [r"W_f = 32064 - 37500 = -5436\ \mathrm{J}"],
            "resaltar": ["fk"],
        },
    ]
    resultado_latex = r"W_f = -5.44\times10^3\ \mathrm{J}"


class P7_13(Cap7Scene):
    numero = "7.13"
    titulo = "Horno empujado rampa arriba"
    lista_datos = [
        ("Masa del horno:", r"m = 10.0\ \mathrm{kg}"),
        ("Rampa:", r"8.00\ \mathrm{m},\ 36.9^\circ"),
        ("Empuje paralelo:", r"F = 110\ \mathrm{N}"),
        ("Fricción cinética:", r"\mu_k = 0.250"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(36.9)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.1, -1.6)
        B = A + 4.3 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=6)
        self.f_linea(fig, "base", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"36.9^\circ", etiqueta_size=20)
        C = A + 1.1 * u + 0.42 * n
        g = self.f_cuerpo(fig, "horno", C, ancho=1.2, alto=0.72,
                          color=self.BLUE, etiqueta="horno")
        g[0].rotate(th, about_point=C)
        self.f_vector(fig, "F", C + 0.66 * u, u, 1.15, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", C - 0.66 * u, -u, 0.8, color=self.YELLOW,
                      etiqueta=r"f_k", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "w", C, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "N", C, n, 0.9, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Empuje paralelo rampa arriba",
            "revelar": ["rampa", "base", "theta", "horno"],
            "text": ["Parte del reposo al pie de la rampa."],
        },
        {
            "titulo": "a) Trabajo del empuje",
            "revelar": ["F"],
            "math": [r"W_F = Fd = (110)(8.00) = 880\ \mathrm{J}"],
            "resaltar": ["F"],
        },
        {
            "titulo": "b) Trabajo de la fricción",
            "revelar": ["fk", "N"],
            "math": [
                r"f_k = \mu_k mg\cos 36.9^\circ = 19.6\ \mathrm{N}",
                r"W_f = -f_k d = -157\ \mathrm{J}",
            ],
            "resaltar": ["fk"],
        },
        {
            "titulo": "c) Aumento de energía potencial",
            "revelar": ["w"],
            "math": [
                r"\Delta U = mgd\sin 36.9^\circ",
                r"\Delta U = (10.0)(9.80)(8.00)(0.600) = 471\ \mathrm{J}",
            ],
        },
        {
            "titulo": "d) y e) Rapidez arriba (dos caminos)",
            "math": [
                r"\Delta K = 880 - 157 - 471 = 253\ \mathrm{J}",
                r"a = \dfrac{110-19.6-58.8}{10.0} = 3.16\ \mathrm{m/s^2}",
                r"v = \sqrt{2(3.16)(8.00)} = 7.11\ \mathrm{m/s}",
            ],
            "text": ["Energía y Newton coinciden: ΔK = 253 J en ambos."],
        },
    ]
    resultado_latex = r"W_F = 880\ \mathrm{J},\ W_f = -157\ \mathrm{J},\ \Delta U = 471\ \mathrm{J},\ v = 7.11\ \mathrm{m/s}"


class P7_15(Cap7Scene):
    numero = "7.15"
    titulo = "Energía potencial de un resorte"
    lista_datos = [
        ("Fuerza para estirar 0.200 m:", r"F = 800\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()

        def zig(p0, p1, vueltas=8, amp=0.14):
            a = np.array(p0, dtype=float)
            b = np.array(p1, dtype=float)
            d = b - a
            u = d / (np.linalg.norm(d) + 1e-9)
            nn = np.array([-u[1], u[0], 0.0])
            pts = [a]
            N = 2 * vueltas
            for i in range(1, N):
                pts.append(a + d * (i / N) + nn * (amp if i % 2 else -amp))
            pts.append(b)
            return VMobject().set_points_as_corners(pts).set_color("#F4F7FB").set_stroke(width=4)

        fig.registrar("resorte", zig(p(-3.0, 0.3), p(-0.6, 0.3)), lambda m: Create(m))
        self.f_linea(fig, "pared", p(-3.0, -0.9), p(-3.0, 1.5), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "tope", p(-0.6, 0.3), forma="punto", color=self.YELLOW)
        self.f_linea(fig, "x1", p(-3.0, -0.5), p(-0.6, -0.5),
                     color=self.GREEN, grosor=2, discontinuo=False,
                     etiqueta=r"0.200", lado=DOWN, etiqueta_size=22)
        self.f_linea(fig, "x2", p(-3.0, -1.1), p(-2.5, -1.1),
                     color=self.YELLOW, grosor=3,
                     etiqueta=r"0.05", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Constante del resorte",
            "revelar": ["pared", "resorte", "tope", "x1"],
            "math": [r"k = \dfrac{F}{x} = \dfrac{800}{0.200} = 4000\ \mathrm{N/m}"],
        },
        {
            "titulo": "a) Estirado 0.200 m",
            "math": [
                r"U = \tfrac12 Fx = \tfrac12(800)(0.200)",
                r"U = 80.0\ \mathrm{J}",
            ],
            "resaltar": ["x1"],
        },
        {
            "titulo": "b) Comprimido 5.00 cm",
            "revelar": ["x2"],
            "math": [
                r"U = \tfrac12 kx^2 = \tfrac12(4000)(0.0500)^2",
                r"U = 5.00\ \mathrm{J}",
            ],
            "resaltar": ["x2"],
        },
    ]
    resultado_latex = r"U_a = 80.0\ \mathrm{J}, \qquad U_b = 5.00\ \mathrm{J}"


class P7_16(Cap7Scene):
    numero = "7.16"
    titulo = "Constante elástica de un tendón"
    lista_datos = [
        ("Masa de prueba:", r"m = 250\ \mathrm{g}"),
        ("Estiramiento:", r"x = 1.23\ \mathrm{cm}"),
        ("Tensión máxima:", r"F_{\max} = 138\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "soporte", p(-1.6, 2.1), p(1.6, 2.1), color=self.MUTED, grosor=3)
        self.f_linea(fig, "tendon", p(0.0, 2.1), p(0.0, 0.3),
                     color=self.WHITE, grosor=6)
        self.f_cuerpo(fig, "pesa", p(0.0, -0.05), ancho=0.8, alto=0.6,
                      color=self.ORANGE, etiqueta="250 g")
        self.f_linea(fig, "x", p(0.55, 0.9), p(0.55, 0.3),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"1.23", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w", p(0.0, -0.05), DOWN, 0.8, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El tendón se comporta como resorte",
            "revelar": ["soporte", "tendon", "pesa", "x", "w"],
            "text": ["En equilibrio, la tensión iguala al peso que cuelga."],
        },
        {
            "titulo": "a) Constante de fuerza",
            "math": [
                r"k = \dfrac{mg}{x} = \dfrac{(0.250)(9.80)}{0.0123}",
                r"k = 199\ \mathrm{N/m}",
            ],
            "resaltar": ["tendon"],
        },
        {
            "titulo": "b) Al límite de rotura",
            "math": [
                r"x_{\max} = \dfrac{138}{199} = 0.693\ \mathrm{m}",
                r"U = \tfrac12(138)(0.693) = 47.8\ \mathrm{J}",
            ],
        },
    ]
    resultado_latex = r"k = 199\ \mathrm{N/m}, \quad x_{\max} = 0.693\ \mathrm{m}, \quad U = 47.8\ \mathrm{J}"


class P7_17(Cap7Scene):
    numero = "7.17"
    titulo = "Energía contra estiramiento al cuadrado"
    lista_datos = [
        ("Energía de referencia:", r"U_0"),
        ("Estiramiento de referencia:", r"x_0"),
    ]

    def crear_figura(self):
        fig = Figura()
        axes = self.f_grafica(
            fig, "grafica", [lambda x: x ** 2],
            x_range=[0, 2.2, 0.5], y_range=[0, 4.5, 1.0],
            x_label="x", y_label="U", ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        for x, y, nombre, et in [(1.0, 1.0, "p0", r"(x_0,U_0)"),
                                 (2.0, 4.0, "p1", r"(2x_0,4U_0)"),
                                 (0.5, 0.25, "p2", r"(x_0/2,U_0/4)"),
                                 (np.sqrt(2), 2.0, "p3", r"(x_0\sqrt2,2U_0)"),
                                 (np.sqrt(2) / 2, 0.5, "p4", r"(x_0/\sqrt2,U_0/2)")]:
            pt = axes.c2p(x, y)
            self.f_cuerpo(fig, nombre, pt, forma="punto", color=self.YELLOW)
            self.f_texto(fig, "et" + nombre, et, pt + UP * 0.35 + RIGHT * 0.55,
                         size=20, color=self.YELLOW, math=True)
        return fig

    pasos = [
        {
            "titulo": "U crece con el cuadrado de x",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "math": [r"U = \tfrac12 kx^2 \;\Rightarrow\; U = U_0\left(\dfrac{x}{x_0}\right)^2"],
            "text": ["Duplicar el estiramiento cuadruplica la energía."],
        },
        {
            "titulo": "a) Doble y mitad de distancia",
            "revelar": ["p1", "etp1", "p2", "etp2"],
            "math": [
                r"\text{i. }U(2x_0) = 4U_0",
                r"\text{ii. }U(x_0/2) = U_0/4",
            ],
            "resaltar": ["p1", "p2"],
        },
        {
            "titulo": "b) Doble y mitad de energía",
            "revelar": ["p3", "etp3", "p4", "etp4"],
            "math": [
                r"\text{i. }x = x_0\sqrt{2}",
                r"\text{ii. }x = x_0/\sqrt{2}",
            ],
            "resaltar": ["p3", "p4"],
        },
    ]
    resultado_latex = r"4U_0,\ U_0/4; \qquad x_0\sqrt2,\ x_0/\sqrt2"


class P7_19(Cap7Scene):
    numero = "7.19"
    titulo = "Resorte que se comprime y libro que cae"
    lista_datos = [
        ("Constante del resorte:", r"k = 1600\ \mathrm{N/m}"),
        ("Energía a almacenar:", r"U = 3.20\ \mathrm{J}"),
        ("Libro que cae:", r"m = 1.20\ \mathrm{kg},\ h = 0.80\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-2.8, -1.8), p(2.6, -1.8), color=self.MUTED, grosor=4)

        def zig(p0, p1, vueltas=8, amp=0.14):
            a = np.array(p0, dtype=float)
            b = np.array(p1, dtype=float)
            d = b - a
            u = d / (np.linalg.norm(d) + 1e-9)
            nn = np.array([-u[1], u[0], 0.0])
            pts = [a]
            N = 2 * vueltas
            for i in range(1, N):
                pts.append(a + d * (i / N) + nn * (amp if i % 2 else -amp))
            pts.append(b)
            return VMobject().set_points_as_corners(pts).set_color("#F4F7FB").set_stroke(width=4)

        fig.registrar("resorte", zig(p(0.0, -1.8), p(0.0, -0.9)), lambda m: Create(m))
        self.f_cuerpo(fig, "libro", p(0.0, 0.35), ancho=1.0, alto=0.6,
                      color=self.ORANGE, etiqueta="libro")
        self.f_vector(fig, "v", p(0.0, 0.35), DOWN, 0.9, color=self.CYAN,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=22)
        self.f_linea(fig, "h", p(1.3, -1.8), p(1.3, 0.05),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"0.80", lado=RIGHT, etiqueta_size=22)
        self.f_linea(fig, "xmax", p(-1.1, -1.8), p(-1.1, -1.2),
                     color=self.YELLOW, grosor=3,
                     etiqueta=r"x", lado=LEFT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Resorte vertical y libro que cae",
            "revelar": ["suelo", "resorte", "libro", "v", "h"],
            "text": ["El libro cae 0.80 m y además comprime al resorte."],
        },
        {
            "titulo": "a) Compresión para 3.20 J",
            "math": [
                r"x = \sqrt{\dfrac{2U}{k}} = \sqrt{\dfrac{2(3.20)}{1600}}",
                r"x = 6.32\times10^{-2}\ \mathrm{m} = 6.32\ \mathrm{cm}",
            ],
        },
        {
            "titulo": "b) El libro cae y comprime",
            "revelar": ["xmax"],
            "math": [
                r"mg(h+x) = \tfrac12 kx^2",
                r"800x^2 - 11.76x - 9.41 = 0",
                r"x = 0.116\ \mathrm{m} = 11.6\ \mathrm{cm}",
            ],
            "resaltar": ["xmax"],
        },
    ]
    resultado_latex = r"x_a = 6.32\ \mathrm{cm}, \qquad x_b = 11.6\ \mathrm{cm}"


class P7_23(Cap7Scene):
    numero = "7.23"
    titulo = "Masa disparada por un resorte sin fricción"
    lista_datos = [
        ("Masa:", r"m = 2.50\ \mathrm{kg}"),
        ("Constante:", r"k = 25.0\ \mathrm{N/cm}"),
        ("Energía almacenada:", r"U = 11.5\ \mathrm{J}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.4, -0.4), p(3.0, -0.4), color=self.MUTED, grosor=4)
        self.f_linea(fig, "pared", p(-3.1, -0.4), p(-3.1, 1.6), color=self.MUTED, grosor=4)

        def zig(p0, p1, vueltas=9, amp=0.14):
            a = np.array(p0, dtype=float)
            b = np.array(p1, dtype=float)
            d = b - a
            u = d / (np.linalg.norm(d) + 1e-9)
            nn = np.array([-u[1], u[0], 0.0])
            pts = [a]
            N = 2 * vueltas
            for i in range(1, N):
                pts.append(a + d * (i / N) + nn * (amp if i % 2 else -amp))
            pts.append(b)
            return VMobject().set_points_as_corners(pts).set_color("#F4F7FB").set_stroke(width=4)

        fig.registrar("resorte", zig(p(-3.1, 0.35), p(-1.7, 0.35)), lambda m: Create(m))
        self.f_cuerpo(fig, "masa", p(-0.9, 0.0), ancho=1.1, alto=0.8,
                      color=self.BLUE, etiqueta="masa")
        self.f_vector(fig, "v", p(-0.35, 0.0), RIGHT, 1.2, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "a", p(-2.4, 0.35), RIGHT, 1.0, color=self.RED,
                      etiqueta=r"a", lado=UP, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El resorte comprimido suelta a la masa",
            "revelar": ["mesa", "pared", "resorte", "masa", "v"],
            "text": ["Sin fricción y sin sujeción: la masa se despega al llegar a longitud natural."],
        },
        {
            "titulo": "a) Rapidez máxima",
            "math": [
                r"\tfrac12 mv^2 = 11.5 \;\Rightarrow\; v = \sqrt{\dfrac{2(11.5)}{2.50}}",
                r"v_{\max} = 3.03\ \mathrm{m/s}",
            ],
            "text": ["Ocurre al perder contacto, con el resorte en longitud natural."],
            "resaltar": ["v"],
        },
        {
            "titulo": "b) Aceleración máxima",
            "revelar": ["a"],
            "math": [
                r"x = \sqrt{\dfrac{2(11.5)}{2500}} = 0.0959\ \mathrm{m}",
                r"a = \dfrac{kx}{m} = \dfrac{(2500)(0.0959)}{2.50} = 95.9\ \mathrm{m/s^2}",
            ],
            "text": ["Ocurre al soltarla, con la compresión máxima."],
            "resaltar": ["a"],
        },
    ]
    resultado_latex = r"v_{\max} = 3.03\ \mathrm{m/s}, \qquad a_{\max} = 95.9\ \mathrm{m/s^2}"


class P7_30(Cap7Scene):
    numero = "7.30"
    titulo = "Trabajo sobre tres trayectorias"
    lista_datos = [
        ("Fuerza:", r"\vec F = -\alpha x^2\,\hat\imath,\ \alpha = 12\ \mathrm{N/m^2}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_ejes(fig, "ejes", p(-2.2, -1.6), largo_x=3.4, largo_y=2.6,
                    etiqueta_x="x", etiqueta_y="y")
        O = p(-2.2, -1.6)
        A = O + p(0.8, 0.0)
        B = O + p(0.8, 1.6)
        C = O + p(2.4, 0.0)
        for nombre, pos in [("pA", A), ("pB", B), ("pC", C)]:
            self.f_cuerpo(fig, nombre, pos, forma="punto", color=self.WHITE)
        self.f_texto(fig, "etA", "A", A + DOWN * 0.35 + LEFT * 0.1, size=22, color=self.WHITE)
        self.f_texto(fig, "etB", "B", B + UP * 0.35, size=22, color=self.WHITE)
        self.f_texto(fig, "etC", "C", C + DOWN * 0.35 + RIGHT * 0.1, size=22, color=self.WHITE)
        self.f_vector(fig, "rAB", A, UP, 1.6, color=self.GREEN,
                      etiqueta=None, grosor=5)
        self.f_vector(fig, "rAC", A, RIGHT, 1.6, color=self.CYAN,
                      etiqueta=None, grosor=5)
        self.f_vector(fig, "rCA", C, LEFT, 1.6, color=self.YELLOW,
                      etiqueta=None, grosor=5)
        self.f_vector(fig, "fuerza", O + p(1.6, 0.9), LEFT, 1.2, color=self.RED,
                      etiqueta=r"\vec F", lado=UP, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Tres caminos entre los mismos puntos",
            "revelar": ["ejes", "pA", "etA", "pB", "etB", "pC", "etC", "fuerza"],
            "text": ["La fuerza siempre apunta en −x y crece con x²."],
        },
        {
            "titulo": "a) De A a B (vertical)",
            "revelar": ["rAB"],
            "math": [r"W = 0"],
            "text": ["Fuerza perpendicular al desplazamiento en todo el tramo."],
        },
        {
            "titulo": "b) De A a C (horizontal)",
            "revelar": ["rAC"],
            "math": [
                r"W = \int_{0.10}^{0.30}\!-\alpha x^2\,dx = -\alpha\left[\dfrac{x^3}{3}\right]_{0.10}^{0.30}",
                r"W = -0.104\ \mathrm{J}",
            ],
            "resaltar": ["rAC"],
        },
        {
            "titulo": "c) De regreso y d) conclusión",
            "revelar": ["rCA"],
            "math": [
                r"W_{C\to A} = +0.104\ \mathrm{J}",
                r"W_{\text{ciclo}} = 0 \;\Rightarrow\; \text{conservativa}",
            ],
            "resaltar": ["rCA"],
        },
    ]
    resultado_latex = r"W_{AB} = 0, \quad W_{AC} = -0.104\ \mathrm{J}, \quad \text{conservativa}"


class P7_34(Cap7Scene):
    numero = "7.34"
    titulo = "Fuerza entre dos átomos de hidrógeno"
    lista_datos = [
        ("Energía potencial:", r"U(x) = -C_6/x^6"),
    ]

    def crear_figura(self):
        fig = Figura()
        axes = self.f_grafica(
            fig, "grafica", [lambda x: -1.0 / (x ** 6)],
            x_range=[1.0, 3.0, 0.5], y_range=[-1.1, 0.1, 0.5],
            x_label="x", y_label="U", ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        plot = fig.mob("grafica_c0")
        y0 = -1.0 / (1.4 ** 6)
        m = 6.0 / (1.4 ** 7)
        tang = Line(axes.c2p(1.0, y0 - m * 0.4), axes.c2p(1.8, y0 + m * 0.4),
                    color=self.YELLOW, stroke_width=3)
        fig.registrar("tangente", tang, lambda m: Create(m))
        self.f_vector(fig, "F", p(-1.8, -0.9), LEFT, 1.2, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_cuerpo(fig, "atomo", p(-1.0, -0.9), forma="punto", color=self.CYAN)
        return fig

    pasos = [
        {
            "titulo": "Energía negativa que tiende a cero",
            "revelar": ["grafica_ejes", "grafica_c0", "atomo"],
            "text": ["Lejos, U ≈ 0; cerca, U es muy negativa: conviene acercarse."],
        },
        {
            "titulo": "La fuerza es menos la pendiente",
            "revelar": ["tangente", "F"],
            "math": [
                r"F_x = -\dfrac{dU}{dx} = -\dfrac{d}{dx}\left(-\dfrac{C_6}{x^6}\right)",
                r"F_x = -\dfrac{6C_6}{x^7}",
            ],
            "resaltar": ["tangente", "F"],
        },
        {
            "titulo": "¿Atracción o repulsión?",
            "math": [r"F_x < 0 \;\Rightarrow\; \text{hacia }x\text{ menor}"],
            "text": ["Negativa: tira al átomo hacia su compañero. Es atracción."],
        },
    ]
    resultado_latex = r"F_x = -\dfrac{6C_6}{x^7}\ < 0\ \text{(atractiva)}"


class P7_36(Cap7Scene):
    numero = "7.36"
    titulo = "Fuerza desde U(x, y) en el plano"
    lista_datos = [
        ("Energía potencial:", r"U(x,y) = \alpha(1/x^2 + 1/y^2)"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_ejes(fig, "ejes", p(-1.8, -1.6), largo_x=3.0, largo_y=2.8,
                    etiqueta_x="x", etiqueta_y="y")
        Q = p(0.2, 0.2)
        self.f_cuerpo(fig, "punto", Q, forma="punto", color=self.YELLOW)
        self.f_vector(fig, "Fx", Q, RIGHT, 1.3, color=self.CYAN,
                      etiqueta=r"F_x", lado=DOWN, etiqueta_size=24)
        self.f_vector(fig, "Fy", Q, UP, 1.1, color=self.GREEN,
                      etiqueta=r"F_y", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "F", Q, np.array([1.0, 0.85, 0.0]), 1.7,
                      color=self.RED, etiqueta=r"\vec F", lado=UP, etiqueta_size=26)
        return fig

    pasos = [
        {
            "titulo": "Cada componente sale de una derivada parcial",
            "revelar": ["ejes", "punto"],
            "math": [r"F_x = -\dfrac{\partial U}{\partial x}, \qquad F_y = -\dfrac{\partial U}{\partial y}"],
        },
        {
            "titulo": "Derivando término a término",
            "revelar": ["Fx", "Fy"],
            "math": [
                r"F_x = -\alpha\dfrac{d}{dx}(x^{-2}) = \dfrac{2\alpha}{x^3}",
                r"F_y = -\alpha\dfrac{d}{dy}(y^{-2}) = \dfrac{2\alpha}{y^3}",
            ],
            "resaltar": ["Fx", "Fy"],
        },
        {
            "titulo": "Vector fuerza total",
            "revelar": ["F"],
            "math": [r"\vec F = \dfrac{2\alpha}{x^3}\,\hat\imath + \dfrac{2\alpha}{y^3}\,\hat\jmath"],
            "resaltar": ["F"],
        },
    ]
    resultado_latex = r"\vec F = \dfrac{2\alpha}{x^3}\,\hat\imath + \dfrac{2\alpha}{y^3}\,\hat\jmath"