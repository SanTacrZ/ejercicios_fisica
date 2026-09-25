"""Capítulo 6 - Edición visual paso a paso (motor de figuras de fisica_base).

Tema: trabajo y energía cinética. La idea visual central es que el trabajo
es el ÁREA bajo la curva F(x): cada fórmula se mapea a una región sombreada.

Render de una escena:
    manim -ql cap6_visual.py P6_1
Render del lote:
    manim -ql cap6_visual.py

LOTE 1 (orden de la lista): 6.1, 6.4, 6.5, 6.6, 6.8
LOTE 2 (orden de la lista): 6.12, 6.14, 6.19, 6.20, 6.21
LOTE 3 (orden de la lista): 6.33, 6.34, 6.35, 6.37, 6.43
PENDIENTES cap6:
    45, 46, 52, 56, 60, 61, 65, 66, 69, 71, 72, 75, 76, 80, 81, 84, 85, 87, 94, 97
"""

import numpy as np

from manim import *
from fisica_base import ProblemaScene, Figura


def p(x, y):
    return np.array([x, y, 0.0])


def resorte(p0, p1, vueltas=7, amp=0.13, color="#F4F7FB", grosor=4):
    """Zigzag de resorte entre dos puntos (para registrar en una Figura)."""
    a = np.array(p0, dtype=float)
    b = np.array(p1, dtype=float)
    d = b - a
    u = d / (np.linalg.norm(d) + 1e-9)
    n = np.array([-u[1], u[0], 0.0])
    pts = [a]
    N = 2 * vueltas
    for i in range(1, N):
        t = i / N
        pts.append(a + d * t + n * (amp if i % 2 == 1 else -amp))
    pts.append(b)
    return VMobject().set_points_as_corners(pts).set_color(color).set_stroke(width=grosor)


class Cap6Scene(ProblemaScene):
    encabezado = "CAPÍTULO 6  //  TRABAJO Y ENERGÍA CINÉTICA"
    subtitulo = "Trabajo y energía cinética"


class P6_1(Cap6Scene):
    numero = "6.1"
    titulo = "Trabajo sobre un libro empujado"
    lista_datos = [
        ("Empuje horizontal:", r"F = 2.40\ \mathrm{N}"),
        ("Fricción opuesta:", r"f = 0.600\ \mathrm{N}"),
        ("Distancia:", r"d = 1.50\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-2.2, 0.0), p(2.2, 0.0), color=self.MUTED, grosor=4)
        centro = p(0.0, 0.35)
        self.f_cuerpo(fig, "libro", centro, ancho=1.4, alto=0.55,
                      color=self.BLUE)
        self.f_texto(fig, "etLibro", "libro", centro + UP * 0.55 + LEFT * 0.85,
                     size=22, color=self.WHITE)
        self.f_vector(fig, "F", p(-1.6, 0.35), RIGHT, 0.9, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", centro + DOWN * 0.22, LEFT, 1.0, color=self.YELLOW,
                      etiqueta=r"f", lado=DOWN, etiqueta_size=24)
        self.f_vector(fig, "N", p(0.0, 0.62), UP, 0.7, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w", p(0.0, 0.08), DOWN, 0.75, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "d", p(-1.2, -0.55), RIGHT, 1.5, color=self.MUTED,
                      etiqueta=r"d", lado=DOWN, etiqueta_size=22)
        axes = self.f_grafica(
            fig, "grafica", [lambda x: 1.80],
            x_range=[0, 1.6, 0.5], y_range=[0, 2.5, 0.5],
            x_label="x\\,(\\mathrm{m})", y_label="F\\,(\\mathrm{N})",
            ancho=3.6, alto=2.0, centro=(0.6, -2.1),
        )
        area = axes.get_area(fig.mob("grafica_c0"), x_range=[0, 1.5],
                             color=self.CYAN, opacity=0.35)
        fig.registrar("grafica_area", area, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "El libro se empuja sobre la mesa",
            "revelar": ["mesa", "libro", "etLibro", "F", "fk", "d"],
            "text": ["El desplazamiento d apunta a la derecha, igual que el empuje."],
        },
        {
            "titulo": "Trabajo del empuje y de la fricción",
            "math": [
                r"W_F = Fd = (2.40)(1.50) = 3.60\ \mathrm{J}",
                r"W_f = -fd = -(0.600)(1.50) = -0.900\ \mathrm{J}",
            ],
            "text": ["La fricción se opone al desplazamiento: su trabajo es negativo."],
            "resaltar": ["F", "fk"],
        },
        {
            "titulo": "Normal y peso no trabajan",
            "revelar": ["N", "w"],
            "math": [r"W_N = 0, \qquad W_g = 0"],
            "text": ["Son perpendiculares al desplazamiento."],
        },
        {
            "titulo": "Trabajo neto: el área bajo F(x)",
            "revelar": ["grafica_ejes", "grafica_c0", "grafica_area"],
            "math": [
                r"F_{\mathrm{neta}} = 2.40 - 0.600 = 1.80\ \mathrm{N}",
                r"W_{\mathrm{neto}} = (1.80)(1.50) = 2.70\ \mathrm{J}",
            ],
            "resaltar": ["grafica_area"],
        },
    ]
    resultado_latex = r"W_F = 3.60\ \mathrm{J}, \quad W_f = -0.900\ \mathrm{J}, \quad W_{\mathrm{neto}} = 2.70\ \mathrm{J}"


class P6_4(Cap6Scene):
    numero = "6.4"
    titulo = "Obrero que empuja hacia abajo en ángulo"
    lista_datos = [
        ("Masa de la caja:", r"m = 30.0\ \mathrm{kg}"),
        ("Distancia:", r"d = 4.5\ \mathrm{m}"),
        ("Fricción cinética:", r"\mu_k = 0.25"),
        ("Ángulo bajo la horizontal:", r"30^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "piso", p(-2.6, 0.0), p(2.6, 0.0), color=self.MUTED, grosor=4)
        centro = p(0.0, 0.48)
        self.f_cuerpo(fig, "caja", centro, ancho=1.3, alto=0.8,
                      color=self.BLUE)
        self.f_texto(fig, "etCaja", "caja", centro + UP * 0.72 + LEFT * 0.95,
                     size=22, color=self.WHITE)
        fdir = np.array([np.cos(np.deg2rad(30.0)), -np.sin(np.deg2rad(30.0)), 0.0])
        self.f_vector(fig, "F", centro, fdir, 1.45, color=self.RED,
                      etiqueta=r"F", lado=RIGHT, etiqueta_size=26)
        self.f_angulo(fig, "ang30", centro, centro + RIGHT, centro + fdir,
                      radio=0.55, etiqueta=r"30^\circ", etiqueta_size=20)
        self.f_vector(fig, "fk", centro, LEFT, 1.15, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "N", centro, UP, 1.0, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", centro, DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=24)
        axes = self.f_grafica(
            fig, "grafica",
            [lambda x: 85.9, lambda x: -85.9],
            x_range=[0, 4.5, 1.5], y_range=[-110, 110, 55],
            x_label="x\\,(\\mathrm{m})", y_label="F\\,(\\mathrm{N})",
            ancho=3.6, alto=2.0, centro=(0.6, -2.75),
        )
        areaF = axes.get_area(fig.mob("grafica_c0"), x_range=[0, 4.5],
                              color=self.GREEN, opacity=0.3)
        fig.registrar("areaF", areaF, lambda m: FadeIn(m))
        areaFk = axes.get_area(fig.mob("grafica_c1"), x_range=[0, 4.5],
                               color=self.YELLOW, opacity=0.3)
        fig.registrar("areafk", areaFk, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "Empuje inclinado hacia abajo",
            "revelar": ["piso", "caja", "etCaja", "F", "ang30", "fk"],
            "text": ["Al empujar hacia abajo, la normal (y la fricción) crecen."],
        },
        {
            "titulo": "Fuerza necesaria a velocidad constante",
            "revelar": ["N", "w"],
            "math": [
                r"F\cos 30^\circ = \mu_k(mg + F\sin 30^\circ)",
                r"F = \dfrac{73.5}{0.741} = 99.2\ \mathrm{N}",
            ],
            "resaltar": ["F", "N"],
        },
        {
            "titulo": "Trabajos que se cancelan",
            "revelar": ["grafica_ejes", "grafica_c0", "grafica_c1", "areaF", "areafk"],
            "math": [
                r"W_F = F\cos 30^\circ\,d = 387\ \mathrm{J}",
                r"W_f = -f_k d = -387\ \mathrm{J}",
            ],
            "text": ["Las dos áreas son iguales y opuestas: el neto es cero."],
            "resaltar": ["areaF", "areafk"],
        },
        {
            "titulo": "Normal, gravedad y trabajo total",
            "math": [r"W_N = 0, \quad W_g = 0, \quad W_{\mathrm{neto}} = 0"],
        },
    ]
    resultado_latex = r"F = 99.2\ \mathrm{N}, \quad W_F = +387\ \mathrm{J}, \quad W_f = -387\ \mathrm{J}"


class P6_5(Cap6Scene):
    numero = "6.5"
    titulo = "Pintor que sube por una escalera"
    lista_datos = [
        ("Masa del pintor:", r"m = 75.0\ \mathrm{kg}"),
        ("Longitud de la escalera:", r"L = 2.75\ \mathrm{m}"),
        ("Ángulo con la pared:", r"30.0^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        pared_x = 0.65
        B = p(-0.6, -1.8)
        T = p(pared_x, 0.365)
        self.f_linea(fig, "pared", p(pared_x, -1.8), p(pared_x, 1.2),
                     color=self.MUTED, grosor=4)
        self.f_linea(fig, "piso", p(-2.6, -1.8), p(1.2, -1.8), color=self.MUTED, grosor=4)
        self.f_linea(fig, "escalera", B, T, color=self.WHITE, grosor=6)
        self.f_angulo(fig, "ang30", T, T + DOWN, B, radio=0.55,
                      etiqueta=r"30^\circ", etiqueta_size=22)
        P = B + 1.8 * np.array([0.5, np.cos(np.deg2rad(30.0)), 0.0])
        self.f_cuerpo(fig, "pintor", P, forma="punto", color=self.YELLOW)
        self.f_vector(fig, "w", P, DOWN, 1.1, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=24)
        self.f_linea(fig, "h", p(-1.35, -1.8), p(-1.35, 0.365),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"h", lado=LEFT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La escalera forma 30° con la pared",
            "revelar": ["pared", "piso", "escalera", "pintor", "ang30", "h"],
            "text": ["La altura vertical ganada es menor que la longitud recorrida."],
        },
        {
            "titulo": "Trabajo de la gravedad",
            "revelar": ["w"],
            "math": [
                r"h = L\cos 30^\circ = (2.75)(0.866) = 2.38\ \mathrm{m}",
                r"W_g = -mgh = -(75.0)(9.80)(2.38) = -1.75\times10^3\ \mathrm{J}",
            ],
            "text": ["Negativo: la gravedad se opone a la subida."],
            "resaltar": ["w", "h"],
        },
        {
            "titulo": "¿Y si acelera al subir?",
            "math": [r"W_g = -mgh"],
            "text": ["No depende de la rapidez: solo del desnivel vertical superado."],
        },
    ]
    resultado_latex = r"W_g = -1.75\times10^3\ \mathrm{J}"


class P6_6(Cap6Scene):
    numero = "6.6"
    titulo = "Dos remolcadores tiran de un buque"
    lista_datos = [
        ("Fuerza de cada remolcador:", r"F = 1.80\times10^6\ \mathrm{N}"),
        ("Apertura respecto al norte:", r"14^\circ"),
        ("Distancia al norte:", r"d = 0.75\ \mathrm{km}"),
    ]

    def crear_figura(self):
        fig = Figura()
        O = p(0.0, -1.2)
        norte = np.array([0.0, 1.0, 0.0])
        d1 = np.array([-np.sin(np.deg2rad(14.0)), np.cos(np.deg2rad(14.0)), 0.0])
        d2 = np.array([np.sin(np.deg2rad(14.0)), np.cos(np.deg2rad(14.0)), 0.0])
        self.f_vector(fig, "F1", O, d1, 1.6, color=self.CYAN,
                      etiqueta=r"F_1", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "F2", O, d2, 1.6, color=self.GREEN,
                      etiqueta=r"F_2", lado=RIGHT, etiqueta_size=24)
        self.f_angulo(fig, "ang1", O, O + norte, O + d1, radio=0.55,
                      etiqueta=r"14^\circ", etiqueta_size=20)
        self.f_angulo(fig, "ang2", O, O + norte, O + d2, radio=0.55,
                      etiqueta=r"14^\circ", etiqueta_size=20)
        self.f_vector(fig, "d", O, norte, 1.25, color=self.YELLOW)
        self.f_texto(fig, "etD", "d", O + RIGHT * 0.38 + UP * 1.0,
                     size=26, color=self.YELLOW, math=True)
        self.f_cuerpo(fig, "buque", O + 1.7 * norte, ancho=1.1, alto=0.55,
                      color=self.BLUE, etiqueta="buque")
        return fig

    pasos = [
        {
            "titulo": "Dos fuerzas simétricas hacia el norte",
            "revelar": ["F1", "F2", "ang1", "ang2", "d", "etD", "buque"],
            "text": ["Las componentes este-oeste se cancelan entre sí."],
        },
        {
            "titulo": "Solo cuenta la componente norte",
            "math": [r"F_N = F\cos 14^\circ \quad \text{(cada remolcador)}"],
            "resaltar": ["F1", "F2", "d"],
        },
        {
            "titulo": "Trabajo total",
            "math": [
                r"W = 2F\cos 14^\circ\,d = 2(1.80\times10^6)(0.970)(750)",
                r"W = 2.62\times10^9\ \mathrm{J}",
            ],
        },
    ]
    resultado_latex = r"W = 2.62\times10^9\ \mathrm{J}"


class P6_8(Cap6Scene):
    numero = "6.8"
    titulo = "Trabajo de una fuerza en componentes"
    lista_datos = [
        ("Fuerza aplicada:", r"\vec F = (30\ \mathrm{N})\hat\imath - (40\ \mathrm{N})\hat\jmath"),
        ("Desplazamiento:", r"\vec s = (-9.0\ \mathrm{m})\hat\imath - (3.0\ \mathrm{m})\hat\jmath"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_ejes(fig, "ejes", p(-1.6, -1.2), largo_x=2.6, largo_y=2.2,
                    etiqueta_x="x", etiqueta_y="y")
        O = p(-1.6, -1.2)
        fdir = np.array([30.0, -40.0, 0.0])
        sdir = np.array([-9.0, -3.0, 0.0])
        self.f_vector(fig, "F", O, fdir, 1.7, color=self.RED,
                      etiqueta=r"\vec F", lado=RIGHT, etiqueta_size=26)
        self.f_vector(fig, "s", O, sdir, 1.55, color=self.CYAN,
                      etiqueta=r"\vec s", lado=DOWN, etiqueta_size=26)
        return fig

    pasos = [
        {
            "titulo": "Fuerza y desplazamiento en el plano",
            "revelar": ["ejes", "F", "s"],
            "text": ["El trabajo es el producto punto: W = F · s."],
        },
        {
            "titulo": "Producto punto componente a componente",
            "math": [
                r"W = F_x s_x + F_y s_y",
                r"W = (30)(-9.0) + (-40)(-3.0) = -270 + 120",
                r"W = -150\ \mathrm{J}",
            ],
            "resaltar": ["F", "s"],
        },
        {
            "titulo": "Trabajo negativo",
            "math": [r"W < 0"],
            "text": ["La fuerza forma un ángulo obtuso con el desplazamiento: se opone a él."],
        },
    ]
    resultado_latex = r"W = -150\ \mathrm{J}"


class P6_12(Cap6Scene):
    numero = "6.12"
    titulo = "Trabajo de una fuerza en componentes"
    lista_datos = [
        ("Fuerza aplicada:", r"\vec F = (-68.0\ \mathrm{N})\hat\imath + (36.0\ \mathrm{N})\hat\jmath"),
        ("Masa del automóvil:", r"m = 380\ \mathrm{kg}"),
        ("Desplazamiento:", r"48.0\ \mathrm{m}\ \text{a }240^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_ejes(fig, "ejes", p(-1.6, -1.2), largo_x=2.6, largo_y=2.2,
                    etiqueta_x="x", etiqueta_y="y")
        O = p(-1.6, -1.2)
        fdir = np.array([-68.0, 36.0, 0.0])
        sdir = np.array([np.cos(np.deg2rad(240.0)), np.sin(np.deg2rad(240.0)), 0.0])
        self.f_vector(fig, "F", O, fdir, 1.7, color=self.RED,
                      etiqueta=r"\vec F", lado=LEFT, etiqueta_size=26)
        self.f_vector(fig, "s", O, sdir, 1.55, color=self.CYAN,
                      etiqueta=r"\vec s", lado=DOWN, etiqueta_size=26)
        return fig

    pasos = [
        {
            "titulo": "Fuerza y desplazamiento en el plano",
            "revelar": ["ejes", "F", "s"],
            "text": ["El desplazamiento forma 240° con el eje +x."],
        },
        {
            "titulo": "Componentes del desplazamiento",
            "math": [
                r"s_x = 48\cos 240^\circ = -24.0\ \mathrm{m}",
                r"s_y = 48\sin 240^\circ = -41.6\ \mathrm{m}",
            ],
        },
        {
            "titulo": "Trabajo como producto punto",
            "math": [
                r"W = F_x s_x + F_y s_y = (-68)(-24.0) + (36)(-41.6)",
                r"W = 1632 - 1496 = 136\ \mathrm{J}",
            ],
            "resaltar": ["F", "s"],
        },
    ]
    resultado_latex = r"W = 136\ \mathrm{J}"


class P6_14(Cap6Scene):
    numero = "6.14"
    titulo = "Trabajo y rapidez en tres puntos"
    lista_datos = [
        ("Masa del libro:", r"m = 1.50\ \mathrm{kg}"),
        ("Rapidez en A:", r"v_A = 3.21\ \mathrm{m/s}"),
        ("Rapidez en B:", r"v_B = 1.25\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "pista", p(-3.4, 0.6), p(3.4, 0.6), color=self.MUTED, grosor=4)
        for x, nombre, et in [(-2.2, "tA", "A"), (0.0, "tB", "B"), (2.2, "tC", "C")]:
            self.f_linea(fig, nombre, p(x, 0.6), p(x, 0.25), color=self.MUTED, grosor=2)
            self.f_texto(fig, "et" + nombre, et, (x, -0.05, 0), size=22, color=self.WHITE)
        self.f_cuerpo(fig, "libro", p(-2.2, 1.0), ancho=0.9, alto=0.55,
                      color=self.BLUE, etiqueta="libro")
        self.f_vector(fig, "vA", p(-2.2, 1.0), RIGHT, 1.2, color=self.CYAN,
                      etiqueta=r"v_A", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "vB", p(0.0, 1.0), RIGHT, 0.5, color=self.CYAN,
                      etiqueta=r"v_B", lado=DOWN, etiqueta_size=22)
        for x, h, nombre, et, col in [(-1.8, 2.47, "KA", r"K_A", self.CYAN),
                                      (-0.3, 0.37, "KB", r"K_B", self.GREEN),
                                      (1.2, 0.14, "KC", r"K_C", self.YELLOW)]:
            barra = Rectangle(width=0.7, height=max(h, 0.06), color=col,
                              stroke_width=2, fill_color=col, fill_opacity=0.5)
            barra.move_to(np.array([x, -2.6 + max(h, 0.06) / 2, 0.0]))
            fig.registrar(nombre, barra, lambda m: FadeIn(m, shift=0.1 * UP))
            self.f_texto(fig, "et" + nombre, et, (x, -2.25, 0), size=20,
                         color=col, math=True)
        return fig

    pasos = [
        {
            "titulo": "El libro frena de A hacia C",
            "revelar": ["pista", "tA", "ettA", "tB", "ettB", "tC", "ettC",
                        "libro", "vA", "vB"],
            "text": ["La fricción hace trabajo negativo: la energía cinética disminuye."],
        },
        {
            "titulo": "Trabajo entre A y B",
            "revelar": ["KA", "etKA", "KB", "etKB"],
            "math": [
                r"W_{AB} = K_B - K_A = \tfrac12(1.50)(1.25^2 - 3.21^2)",
                r"W_{AB} = -6.56\ \mathrm{J}",
            ],
            "resaltar": ["KA", "KB"],
        },
        {
            "titulo": "De B a C con −0.750 J",
            "revelar": ["KC", "etKC"],
            "math": [
                r"K_C = K_B + W_{BC} = 1.17 - 0.750 = 0.422\ \mathrm{J}",
                r"v_C = \sqrt{2K_C/m} = 0.750\ \mathrm{m/s}",
            ],
            "resaltar": ["KC"],
        },
        {
            "titulo": "Si el trabajo fuera +0.750 J",
            "math": [
                r"K_C = 1.17 + 0.750 = 1.92\ \mathrm{J}",
                r"v_C = 1.60\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"W_{AB} = -6.56\ \mathrm{J}, \quad v_C = 0.750\ \mathrm{m/s}\ (\text{o }1.60)"


class P6_19(Cap6Scene):
    numero = "6.19"
    titulo = "Teorema trabajo-energía en cinco casos"
    lista_datos = [
        ("Secuoya:", r"h = 95.0\ \mathrm{m}"),
        ("Roca del volcán:", r"h = 525\ \mathrm{m}"),
        ("Esquiadora:", r"v_0 = 5.00\ \mathrm{m/s},\ \mu_k = 0.220"),
        ("Trineo en colina 25°:", r"v_0 = 12.0\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-3.5, -1.6), p(3.5, -1.6), color=self.MUTED, grosor=3)
        self.f_linea(fig, "tronco", p(-2.9, -1.6), p(-2.9, 0.2), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "rama", p(-2.9, 0.6), forma="punto", color=self.GREEN)
        self.f_linea(fig, "h95", p(-3.25, -1.6), p(-3.25, 0.6),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"95", lado=LEFT, etiqueta_size=20)
        poly = Polygon(p(-1.75, -1.6), p(-0.65, -1.6), p(-1.2, -0.5),
                       color=self.MUTED, stroke_width=3, fill_opacity=0)
        fig.registrar("volcan", poly, lambda m: Create(m))
        self.f_cuerpo(fig, "roca", p(-1.2, 0.1), forma="punto", color=self.ORANGE)
        self.f_vector(fig, "vRoca", p(-1.2, 0.1), UP, 0.7, color=self.CYAN,
                      etiqueta=r"v_0", lado=RIGHT, etiqueta_size=20)
        self.f_linea(fig, "h525", p(-0.45, -1.6), p(-0.45, 0.1),
                     color=self.ORANGE, grosor=2, discontinuo=True,
                     etiqueta=r"525", lado=RIGHT, etiqueta_size=20)
        self.f_linea(fig, "rugoso", p(0.3, -1.6), p(1.5, -1.6), color=self.YELLOW, grosor=6)
        self.f_texto(fig, "mu", r"\mu_k", (0.9, -2.0, 0), size=22, color=self.YELLOW, math=True)
        self.f_cuerpo(fig, "esquiadora", p(0.6, -1.2), forma="punto", color=self.CYAN)
        self.f_vector(fig, "vE", p(0.6, -1.2), RIGHT, 0.9, color=self.CYAN,
                      etiqueta=r"5.00", lado=UP, etiqueta_size=20)
        u = np.array([np.cos(np.deg2rad(25.0)), np.sin(np.deg2rad(25.0)), 0.0])
        base = p(1.9, -1.6)
        tope = base + 1.2 * u
        self.f_linea(fig, "colina", base, tope, color=self.BLUE, grosor=5)
        self.f_angulo(fig, "ang25", base, base + RIGHT, tope, radio=0.4,
                      etiqueta=r"25^\circ", etiqueta_size=18)
        S = base + 0.45 * u
        self.f_cuerpo(fig, "trineo", S, forma="punto", color=self.RED)
        self.f_vector(fig, "vT", S, u, 0.8, color=self.RED,
                      etiqueta=r"12.0", lado=UP, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Cinco situaciones, un solo teorema",
            "revelar": ["suelo", "tronco", "rama", "h95", "volcan", "roca", "vRoca",
                        "h525", "rugoso", "mu", "esquiadora", "vE", "colina",
                        "ang25", "trineo", "vT"],
            "math": [r"W_{\mathrm{neto}} = \Delta K"],
            "text": ["El trabajo neto siempre es el cambio de energía cinética."],
        },
        {
            "titulo": "a) La rama cae 95.0 m",
            "math": [
                r"v^2 = 2gh = 2(9.80)(95.0)",
                r"v = 43.2\ \mathrm{m/s}",
            ],
            "resaltar": ["rama", "h95"],
        },
        {
            "titulo": "b) La roca sube 525 m",
            "math": [
                r"v_0^2 = 2gh = 2(9.80)(525)",
                r"v_0 = 101\ \mathrm{m/s}",
            ],
            "resaltar": ["roca", "h525"],
        },
        {
            "titulo": "c) La esquiadora frena en lo áspero",
            "math": [
                r"d = \dfrac{v_0^2}{2\mu_k g} = \dfrac{(5.00)^2}{2(0.220)(9.80)}",
                r"d = 5.80\ \mathrm{m}",
            ],
            "resaltar": ["esquiadora", "rugoso"],
        },
        {
            "titulo": "d) Zona áspera de solo 2.90 m",
            "math": [
                r"v^2 = v_0^2 - 2\mu_k g d = 25.0 - 12.5",
                r"v = 3.54\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "e) El trineo sube la colina lisa",
            "math": [
                r"h = \dfrac{v_0^2}{2g} = \dfrac{(12.0)^2}{2(9.80)} = 7.35\ \mathrm{m}",
            ],
            "resaltar": ["trineo", "colina"],
        },
    ]
    resultado_latex = r"43.2\ \mathrm{m/s};\ 101\ \mathrm{m/s};\ 5.80\ \mathrm{m};\ 3.54\ \mathrm{m/s};\ 7.35\ \mathrm{m}"


class P6_20(Cap6Scene):
    numero = "6.20"
    titulo = "Piedra lanzada hacia arriba"
    lista_datos = [
        ("Peso de la piedra:", r"w = 20\ \mathrm{N}"),
        ("Altura de referencia:", r"15.0\ \mathrm{m}"),
        ("Rapidez a 15 m:", r"25.0\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-2.6, -1.8), p(1.6, -1.8), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "piedra", p(0.0, -1.8), forma="punto", color=self.WHITE)
        self.f_vector(fig, "v0", p(0.0, -1.8), UP, 1.2, color=self.CYAN,
                      etiqueta=r"v_0", lado=RIGHT, etiqueta_size=24)
        self.f_linea(fig, "h15", p(0.9, -1.8), p(0.9, -0.2),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"15", lado=RIGHT, etiqueta_size=20)
        self.f_texto(fig, "v15", r"v = 25", (0.9, 0.15, 0), size=22,
                     color=self.CYAN, math=True)
        self.f_linea(fig, "hmax", p(-0.9, -1.8), p(-0.9, 1.3),
                     color=self.YELLOW, grosor=2, discontinuo=True,
                     etiqueta=r"H", lado=LEFT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La piedra sube frenada por su peso",
            "revelar": ["suelo", "piedra", "v0", "h15", "v15", "hmax"],
            "text": ["Sin aire: el peso hace todo el trabajo negativo."],
        },
        {
            "titulo": "Rapidez de lanzamiento",
            "math": [
                r"-w(15.0) = \tfrac12 mv^2 - \tfrac12 mv_0^2",
                r"v_0 = \sqrt{25.0^2 + 2(9.80)(15.0)} = 30.3\ \mathrm{m/s}",
            ],
            "resaltar": ["v0", "v15"],
        },
        {
            "titulo": "Altura máxima",
            "math": [
                r"H = \dfrac{v_0^2}{2g} = \dfrac{(30.3)^2}{2(9.80)} = 46.9\ \mathrm{m}",
            ],
            "resaltar": ["hmax"],
        },
    ]
    resultado_latex = r"v_0 = 30.3\ \mathrm{m/s}, \qquad H = 46.9\ \mathrm{m}"


class P6_21(Cap6Scene):
    numero = "6.21"
    titulo = "Caja de rescate ladera arriba"
    lista_datos = [
        ("Ángulo de la pendiente:", r"\alpha"),
        ("Desnivel hasta el esquiador:", r"h"),
        ("Fricción cinética:", r"\mu_k"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(28.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.1, -1.7)
        B = A + 4.6 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=6)
        self.f_linea(fig, "base", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "alpha", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"\alpha", etiqueta_size=22)
        C = A + 0.9 * u + 0.35 * n
        self.f_cuerpo(fig, "caja", C, ancho=0.95, alto=0.65,
                      color=self.GREEN)
        self.f_texto(fig, "etCaja", "caja", C + UP * 0.62, size=22, color=self.WHITE)
        self.f_vector(fig, "v0", C, u, 1.1, color=self.CYAN,
                      etiqueta=r"v_0", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", C - 0.55 * u, -u, 0.8, color=self.YELLOW,
                      etiqueta=r"f_k", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "N", C, n, 0.9, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w", C, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=22)
        self.f_linea(fig, "h", p(1.4, A[1]), p(1.4, A[1] + 1.7),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"h", lado=RIGHT, etiqueta_size=24)
        self.f_cuerpo(fig, "esquiador", p(1.05, A[1] + 1.7), forma="punto",
                      color=self.RED)
        return fig

    pasos = [
        {
            "titulo": "Geometría: distancia sobre la pendiente",
            "revelar": ["rampa", "base", "alpha", "caja", "etCaja", "esquiador", "h"],
            "math": [r"d = \dfrac{h}{\sin\alpha}"],
        },
        {
            "titulo": "Trabajos del peso y la fricción",
            "revelar": ["v0", "fk", "N", "w"],
            "math": [
                r"W_g = -mgh",
                r"W_f = -\mu_k mg\cos\alpha\cdot d = -\mu_k mgh\cot\alpha",
            ],
            "resaltar": ["fk", "w"],
        },
        {
            "titulo": "Rapidez mínima en la base",
            "math": [
                r"\tfrac12 mv_0^2 + W_g + W_f = 0",
                r"v_0 = \sqrt{2gh\,(1 + \mu_k\cot\alpha)}",
            ],
            "text": ["Justo la necesaria para llegar arriba con rapidez cero."],
        },
    ]
    resultado_latex = r"v_0 = \sqrt{2gh\,(1 + \mu_k\cot\alpha)}"


class P6_33(Cap6Scene):
    numero = "6.33"
    titulo = "Tres masas colgadas de tres resortes en serie"
    lista_datos = [
        ("Masa de cada bloque:", r"m = 6.40\ \mathrm{kg}"),
        ("Constante de cada resorte:", r"k = 7.80\ \mathrm{kN/m}"),
        ("Longitud natural:", r"L_0 = 12.0\ \mathrm{cm}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "soporte", p(-1.2, 2.3), p(1.2, 2.3), color=self.MUTED, grosor=3)
        fig.registrar("res1", resorte(p(0, 2.3), p(0, 1.55)), lambda m: Create(m))
        fig.registrar("res2", resorte(p(0, 0.925), p(0, 0.175)), lambda m: Create(m))
        fig.registrar("res3", resorte(p(0, -0.375), p(0, -1.125)), lambda m: Create(m))
        self.f_cuerpo(fig, "m1", p(0, 1.2), ancho=0.85, alto=0.55,
                      color=self.BLUE, etiqueta=r"m")
        self.f_cuerpo(fig, "m2", p(0, -0.1), ancho=0.85, alto=0.55,
                      color=self.GREEN, etiqueta=r"m")
        self.f_cuerpo(fig, "m3", p(0, -1.4), ancho=0.85, alto=0.55,
                      color=self.ORANGE, etiqueta=r"m")
        self.f_vector(fig, "F1", p(-0.32, 1.2), UP, 1.2, color=self.CYAN,
                      etiqueta=r"F_1", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "F2", p(-0.32, -0.1), UP, 0.85, color=self.CYAN,
                      etiqueta=r"F_2", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "F3", p(-0.32, -1.4), UP, 0.6, color=self.CYAN,
                      etiqueta=r"F_3", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w1", p(0.32, 1.2), DOWN, 0.7, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w2", p(0.32, -0.1), DOWN, 0.7, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w3", p(0.32, -1.4), DOWN, 0.7, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Tres resortes en serie con tres masas",
            "revelar": ["soporte", "res1", "res2", "res3", "m1", "m2", "m3"],
            "text": ["Cada resorte carga las masas que cuelgan debajo de él."],
        },
        {
            "titulo": "Diagrama de cuerpo libre de cada masa",
            "revelar": ["F1", "F2", "F3", "w1", "w2", "w3"],
            "math": [
                r"F_3 = mg, \qquad F_2 = 2mg, \qquad F_1 = 3mg",
            ],
            "text": ["El resorte superior es el más exigido: sostiene a las tres."],
            "resaltar": ["F1", "F2", "F3"],
        },
        {
            "titulo": "Estiramiento y longitud de cada resorte",
            "math": [
                r"x = \dfrac{F}{k} = \dfrac{mg}{k} = 0.804\ \mathrm{cm}\ \text{(por masa)}",
                r"L_3 = 12.8\ \mathrm{cm}, \quad L_2 = 13.6\ \mathrm{cm}, \quad L_1 = 14.4\ \mathrm{cm}",
            ],
        },
    ]
    resultado_latex = r"L_1 = 14.4\ \mathrm{cm}, \quad L_2 = 13.6\ \mathrm{cm}, \quad L_3 = 12.8\ \mathrm{cm}"


class P6_34(Cap6Scene):
    numero = "6.34"
    titulo = "Trabajo de una fuerza variable (gráfica)"
    lista_datos = [
        ("Masa del trineo:", r"m = 10.0\ \mathrm{kg}"),
        ("Fuerza máxima:", r"F_{\max} = 10.0\ \mathrm{N}\ \text{en }x = 8.0\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        f = lambda x: np.where(x <= 8.0, 10.0 * x / 8.0, 10.0 * (12.0 - x) / 4.0)
        axes = self.f_grafica(
            fig, "grafica", [f],
            x_range=[0, 12, 2], y_range=[0, 10, 2],
            x_label="x\\,(\\mathrm{m})", y_label="F_x\\,(\\mathrm{N})",
            ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        plot = fig.mob("grafica_c0")
        a1 = axes.get_area(plot, x_range=[0, 8.0], color=self.GREEN, opacity=0.3)
        fig.registrar("area1", a1, lambda m: FadeIn(m))
        a2 = axes.get_area(plot, x_range=[8.0, 12.0], color=self.YELLOW, opacity=0.3)
        fig.registrar("area2", a2, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "La fuerza varía con la posición",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "text": ["El trabajo es el área bajo la curva, aunque la fuerza cambie."],
        },
        {
            "titulo": "De x = 0 a x = 8.0 m",
            "revelar": ["area1"],
            "math": [r"W = \tfrac12(8.0)(10.0) = 40.0\ \mathrm{J}"],
            "resaltar": ["area1"],
        },
        {
            "titulo": "De x = 8.0 a x = 12.0 m",
            "revelar": ["area2"],
            "math": [r"W = \tfrac12(4.0)(10.0) = 20.0\ \mathrm{J}"],
            "resaltar": ["area2"],
        },
        {
            "titulo": "De x = 0 a x = 12.0 m",
            "math": [r"W = 40.0 + 20.0 = 60.0\ \mathrm{J}"],
        },
    ]
    resultado_latex = r"W_{0\to8} = 40.0\ \mathrm{J}, \quad W_{8\to12} = 20.0\ \mathrm{J}, \quad W_{0\to12} = 60.0\ \mathrm{J}"


class P6_35(Cap6Scene):
    numero = "6.35"
    titulo = "Rapidez con fuerza variable"
    lista_datos = [
        ("Masa del trineo:", r"m = 10.0\ \mathrm{kg}"),
        ("Parte del reposo en:", r"x = 0"),
    ]

    def crear_figura(self):
        fig = Figura()
        f = lambda x: np.where(x <= 8.0, 10.0 * x / 8.0, 10.0 * (12.0 - x) / 4.0)
        axes = self.f_grafica(
            fig, "grafica", [f],
            x_range=[0, 12, 2], y_range=[0, 10, 2],
            x_label="x\\,(\\mathrm{m})", y_label="F_x\\,(\\mathrm{N})",
            ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        plot = fig.mob("grafica_c0")
        a1 = axes.get_area(plot, x_range=[0, 8.0], color=self.GREEN, opacity=0.3)
        fig.registrar("area1", a1, lambda m: FadeIn(m))
        a2 = axes.get_area(plot, x_range=[8.0, 12.0], color=self.YELLOW, opacity=0.3)
        fig.registrar("area2", a2, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "El área da la energía cinética",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "math": [r"\tfrac12 mv^2 = W = \text{área}"],
            "text": ["Sin fricción, todo el trabajo se vuelve rapidez."],
        },
        {
            "titulo": "Rapidez en x = 8.0 m",
            "revelar": ["area1"],
            "math": [
                r"W = 40.0\ \mathrm{J}",
                r"v = \sqrt{\dfrac{2W}{m}} = \sqrt{\dfrac{80.0}{10.0}} = 2.83\ \mathrm{m/s}",
            ],
            "resaltar": ["area1"],
        },
        {
            "titulo": "Rapidez en x = 12.0 m",
            "revelar": ["area2"],
            "math": [
                r"W = 60.0\ \mathrm{J}",
                r"v = \sqrt{\dfrac{120}{10.0}} = 3.46\ \mathrm{m/s}",
            ],
            "resaltar": ["area2"],
        },
    ]
    resultado_latex = r"v(8.0) = 2.83\ \mathrm{m/s}, \qquad v(12.0) = 3.46\ \mathrm{m/s}"


class P6_37(Cap6Scene):
    numero = "6.37"
    titulo = "Caja que comprime un resorte"
    lista_datos = [
        ("Masa de la caja:", r"m = 6.0\ \mathrm{kg}"),
        ("Rapidez inicial:", r"v_0 = 3.0\ \mathrm{m/s}"),
        ("Constante del resorte:", r"k = 75\ \mathrm{N/cm}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "piso", p(-3.2, -0.4), p(2.6, -0.4), color=self.MUTED, grosor=4)
        self.f_linea(fig, "pared", p(-2.9, -0.4), p(-2.9, 1.6), color=self.MUTED, grosor=4)
        fig.registrar("resorte", resorte(p(-2.9, 0.35), p(-0.9, 0.35)),
                       lambda m: Create(m))
        self.f_cuerpo(fig, "caja", p(0.35, 0.0), ancho=1.2, alto=0.8,
                      color=self.BLUE, etiqueta="caja")
        self.f_vector(fig, "v", p(-0.25, 0.0), LEFT, 1.2, color=self.CYAN,
                      etiqueta=r"v_0", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "xmax", p(-0.9, -0.4), p(-0.9, -1.1),
                     color=self.YELLOW, grosor=2, discontinuo=True,
                     etiqueta=r"x_{\max}", lado=DOWN, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La caja se estrella contra el resorte",
            "revelar": ["piso", "pared", "resorte", "caja", "v"],
            "text": ["Sin fricción: la energía cinética se guarda en el resorte."],
        },
        {
            "titulo": "Toda la energía pasa al resorte",
            "revelar": ["xmax"],
            "math": [
                r"\tfrac12 mv_0^2 = \tfrac12 kx_{\max}^2",
                r"x_{\max} = v_0\sqrt{\dfrac{m}{k}} = 3.0\sqrt{\dfrac{6.0}{7500}}",
                r"x_{\max} = 8.49\times10^{-2}\ \mathrm{m} = 8.49\ \mathrm{cm}",
            ],
            "resaltar": ["xmax"],
        },
    ]
    resultado_latex = r"x_{\max} = 8.49\ \mathrm{cm}"


class P6_43(Cap6Scene):
    numero = "6.43"
    titulo = "Trineo impulsado por un resorte gigante"
    lista_datos = [
        ("Constante del resorte:", r"k = 40.0\ \mathrm{N/cm}"),
        ("Masa total:", r"m = 70.0\ \mathrm{kg}"),
        ("Compresión inicial:", r"x_0 = 0.375\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "piso", p(-3.4, -0.5), p(3.2, -0.5), color=self.MUTED, grosor=4)
        self.f_linea(fig, "pared", p(-3.1, -0.5), p(-3.1, 1.7), color=self.MUTED, grosor=4)
        fig.registrar("resorte", resorte(p(-3.1, 0.3), p(-1.5, 0.3), vueltas=9),
                       lambda m: Create(m))
        self.f_cuerpo(fig, "trineo", p(-0.75, -0.05), ancho=1.4, alto=0.8,
                      color=self.BLUE, etiqueta="trineo")
        flecha = DoubleArrow(p(-3.1, -1.0), p(-1.5, -1.0), color=self.YELLOW,
                             stroke_width=3, tip_length=0.15)
        fig.registrar("comp", flecha, lambda m: Create(m))
        self.f_texto(fig, "etComp", r"0.375\ \mathrm{m}", (-2.3, -1.35, 0), size=24,
                     color=self.YELLOW, math=True)
        self.f_vector(fig, "v", p(-0.05, -0.05), RIGHT, 1.2, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=26)
        return fig

    pasos = [
        {
            "titulo": "El resorte comprimido empuja al trineo",
            "revelar": ["piso", "pared", "resorte", "trineo", "comp", "etComp"],
            "text": ["Sin fricción: la energía elástica se vuelve cinética."],
        },
        {
            "titulo": "a) Rapidez al llegar a longitud natural",
            "revelar": ["v"],
            "math": [
                r"\tfrac12 kx_0^2 = \tfrac12 mv^2",
                r"v = x_0\sqrt{\dfrac{k}{m}} = 0.375\sqrt{\dfrac{4000}{70.0}}",
                r"v = 2.83\ \mathrm{m/s}",
            ],
            "resaltar": ["v", "resorte"],
        },
        {
            "titulo": "b) Aún comprimido 0.200 m",
            "math": [
                r"\tfrac12 k(x_0^2 - x^2) = \tfrac12 mv^2",
                r"v = \sqrt{\dfrac{4000(0.375^2 - 0.200^2)}{70.0}} = 2.40\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"v_a = 2.83\ \mathrm{m/s}, \qquad v_b = 2.40\ \mathrm{m/s}"
