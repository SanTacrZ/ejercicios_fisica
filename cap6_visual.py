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
LOTE 4 (orden de la lista): 6.45, 6.46, 6.52, 6.56, 6.60
LOTE 5 (orden de la lista): 6.61, 6.65, 6.66, 6.69, 6.71
LOTE 6 (orden de la lista): 6.72, 6.75, 6.76, 6.80, 6.81
PENDIENTES cap6:
    84, 85, 87, 94, 97
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


class P6_45(Cap6Scene):
    numero = "6.45"
    titulo = "Deslizador lanzado por un resorte en riel inclinado"
    lista_datos = [
        ("Masa del deslizador:", r"m = 0.0900\ \mathrm{kg}"),
        ("Constante del resorte:", r"k = 640\ \mathrm{N/m}"),
        ("Inclinación del riel:", r"40.0^\circ"),
        ("Alcance máximo:", r"d_{\max} = 1.80\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(40.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.0, -1.5)
        B = A + 3.4 * u
        self.f_linea(fig, "riel", A, B, color=self.BLUE, grosor=6)
        self.f_linea(fig, "base", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "ang40", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"40^\circ", etiqueta_size=20)
        fig.registrar("resorte", resorte(A, A + 0.7 * u), lambda m: Create(m))
        C = A + 1.02 * u + 0.30 * n
        g = self.f_cuerpo(fig, "deslizador", C, ancho=0.9, alto=0.6,
                          color=self.GREEN, etiqueta="m")
        g[0].rotate(th, about_point=C)
        self.f_linea(fig, "marcaMax", A + 1.8 * u - 0.25 * n, A + 1.8 * u + 0.25 * n,
                     color=self.GREEN, grosor=3,
                     etiqueta=r"1.80", lado=UP, etiqueta_size=20)
        self.f_linea(fig, "marca08", A + 0.8 * u - 0.25 * n, A + 0.8 * u + 0.25 * n,
                     color=self.YELLOW, grosor=3,
                     etiqueta=r"0.80", lado=DOWN, etiqueta_size=20)
        flecha = DoubleArrow(A - 0.35 * n, A + 0.7 * u - 0.35 * n,
                             color=self.YELLOW, stroke_width=3, tip_length=0.15)
        fig.registrar("comp", flecha, lambda m: Create(m))
        self.f_texto(fig, "etX", r"x = ?", (A + 0.35 * u - 1.0 * n), size=24,
                     color=self.YELLOW, math=True)
        return fig

    pasos = [
        {
            "titulo": "El resorte dispara al deslizador riel arriba",
            "revelar": ["riel", "base", "ang40", "resorte", "deslizador",
                        "marcaMax", "marca08", "comp", "etX"],
            "text": ["Sin fricción: la energía elástica se reparte entre altura y rapidez."],
        },
        {
            "titulo": "a) Compresión original del resorte",
            "math": [
                r"\tfrac12 kx^2 = mgd\sin 40^\circ",
                r"x = \sqrt{\dfrac{2(0.0900)(9.80)(1.80)(0.643)}{640}}",
                r"x = 5.65\times10^{-2}\ \mathrm{m} = 5.65\ \mathrm{cm}",
            ],
            "resaltar": ["comp", "marcaMax"],
        },
        {
            "titulo": "b) A 0.80 m ya perdió contacto",
            "math": [
                r"K = \tfrac12 kx^2 - mg(0.80)\sin 40^\circ",
                r"K = 1.02 - 0.454 = 0.57\ \mathrm{J}",
            ],
            "text": ["El resorte se estira solo 5.65 cm: a 0.80 m ya va por inercia."],
            "resaltar": ["marca08"],
        },
    ]
    resultado_latex = r"x = 5.65\ \mathrm{cm}, \qquad K(0.80) = 0.57\ \mathrm{J}"


class P6_46(Cap6Scene):
    numero = "6.46"
    titulo = "Ladrillo lanzado por un resorte vertical"
    lista_datos = [
        ("Masa del ladrillo:", r"m = 1.80\ \mathrm{kg}"),
        ("Constante del resorte:", r"k = 450\ \mathrm{N/m}"),
        ("Altura deseada:", r"h = 3.6\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-2.8, -1.8), p(2.4, -1.8), color=self.MUTED, grosor=4)
        fig.registrar("resorte", resorte(p(0.0, -1.8), p(0.0, -0.9), vueltas=8),
                       lambda m: Create(m))
        self.f_cuerpo(fig, "ladrillo", p(0.0, -0.55), ancho=1.0, alto=0.6,
                      color=self.ORANGE, etiqueta="ladrillo")
        self.f_linea(fig, "h", p(1.3, -1.8), p(1.3, 1.6),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"3.6", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "v", p(0.0, -0.55), UP, 1.0, color=self.CYAN,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El resorte vertical impulsa al ladrillo",
            "revelar": ["suelo", "resorte", "ladrillo", "h"],
            "text": ["Toda la energía elástica debe alcanzar para la altura deseada."],
        },
        {
            "titulo": "Compresión necesaria",
            "revelar": ["v"],
            "math": [
                r"\tfrac12 kx^2 = mgh",
                r"x = \sqrt{\dfrac{2(1.80)(9.80)(3.6)}{450}} = 0.531\ \mathrm{m}",
            ],
            "resaltar": ["resorte", "h"],
        },
    ]
    resultado_latex = r"x = 0.531\ \mathrm{m}"


class P6_52(Cap6Scene):
    numero = "6.52"
    titulo = "Potencia media de la fricción"
    lista_datos = [
        ("Masa de la piedra:", r"m = 20.0\ \mathrm{kg}"),
        ("Rapidez inicial:", r"v_0 = 8.00\ \mathrm{m/s}"),
        ("Fricción cinética:", r"\mu_k = 0.200"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "piso", p(-3.3, 0.0), p(3.3, 0.0), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "piedra", p(-1.6, 0.4), ancho=0.85, alto=0.7,
                      color=self.BLUE, etiqueta="piedra")
        self.f_vector(fig, "v0", p(-1.175, 0.4), RIGHT, 1.3, color=self.CYAN,
                      etiqueta=r"v_0", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", p(-2.025, 0.4), LEFT, 1.1, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "d", p(-1.6, -0.6), p(1.7, -0.6),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"d", lado=DOWN, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La piedra frena hasta detenerse",
            "revelar": ["piso", "piedra", "v0", "fk"],
            "text": ["La fricción disipa toda la energía cinética como calor."],
        },
        {
            "titulo": "Distancia y tiempo de frenado",
            "revelar": ["d"],
            "math": [
                r"d = \dfrac{v_0^2}{2\mu_k g} = \dfrac{64.0}{3.92} = 16.3\ \mathrm{m}",
                r"t = \dfrac{v_0}{\mu_k g} = \dfrac{8.00}{1.96} = 4.08\ \mathrm{s}",
            ],
            "resaltar": ["d"],
        },
        {
            "titulo": "Potencia media disipada",
            "math": [
                r"P = \dfrac{W}{t} = \dfrac{-640\ \mathrm{J}}{4.08\ \mathrm{s}}",
                r"P = -157\ \mathrm{W}",
            ],
            "text": ["157 W salen del movimiento y calientan piedra y piso."],
        },
    ]
    resultado_latex = r"P = -157\ \mathrm{W}\ (\text{157 W disipados})"


class P6_56(Cap6Scene):
    numero = "6.56"
    titulo = "Cuántos pasajeros sube el elevador"
    lista_datos = [
        ("Masa del elevador:", r"600\ \mathrm{kg}"),
        ("Altura:", r"20.0\ \mathrm{m}\ \text{en }16.0\ \mathrm{s}"),
        ("Potencia del motor:", r"40\ \mathrm{hp}"),
        ("Masa por pasajero:", r"65.0\ \mathrm{kg}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "muroI", p(-1.9, -2.2), p(-1.9, 2.2), color=self.MUTED, grosor=3)
        self.f_linea(fig, "muroD", p(1.9, -2.2), p(1.9, 2.2), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "cabina", p(0.0, -0.3), ancho=2.0, alto=1.7,
                      color=self.BLUE, etiqueta="elevador")
        for i in range(3):
            self.f_cuerpo(fig, f"pas{i}", p(-0.55 + 0.55 * i, -0.75),
                          forma="punto", color=self.YELLOW)
        self.f_vector(fig, "v", p(1.45, -0.3), UP, 1.1, color=self.CYAN,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=24)
        self.f_linea(fig, "h", p(-2.35, -1.6), p(-2.35, 0.9),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"20", lado=LEFT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Sube a rapidez constante",
            "revelar": ["muroI", "muroD", "cabina", "pas0", "pas1", "pas2", "h"],
            "math": [r"v = \dfrac{20.0}{16.0} = 1.25\ \mathrm{m/s}"],
        },
        {
            "titulo": "La potencia limita el peso total",
            "revelar": ["v"],
            "math": [
                r"P = (600 + 65n)gv \le 40\,\mathrm{hp} = 29840\ \mathrm{W}",
                r"600 + 65n \le \dfrac{29840}{(9.80)(1.25)} = 2436",
                r"n \le 28.2 \;\Rightarrow\; 28\ \text{pasajeros}",
            ],
            "resaltar": ["v"],
        },
    ]
    resultado_latex = r"28\ \text{pasajeros como máximo}"


class P6_60(Cap6Scene):
    numero = "6.60"
    titulo = "Trabajo de una fuerza que crece con x"
    lista_datos = [
        ("Desplazamiento:", r"x = 0 \to 6.9\ \mathrm{m}"),
        ("Fuerza aplicada:", r"F_x = -[20.0 + 3.0x]\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        axes = self.f_grafica(
            fig, "grafica", [lambda x: -(20.0 + 3.0 * x)],
            x_range=[0, 7, 1], y_range=[-45, 5, 10],
            x_label="x\\,(\\mathrm{m})", y_label="F_x\\,(\\mathrm{N})",
            ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        plot = fig.mob("grafica_c0")
        area = axes.get_area(plot, x_range=[0, 6.9], color=self.RED, opacity=0.3)
        fig.registrar("area", area, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "La fuerza se opone y crece con x",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "text": ["El área queda bajo el eje: el trabajo será negativo."],
        },
        {
            "titulo": "Trabajo como integral (área)",
            "revelar": ["area"],
            "math": [
                r"W = \int_0^{6.9}-(20.0+3.0x)\,dx = -\left[20x + 1.5x^2\right]_0^{6.9}",
                r"W = -(138 + 71.4) = -209\ \mathrm{J}",
            ],
            "resaltar": ["area"],
        },
    ]
    resultado_latex = r"W = -209\ \mathrm{J}"


class P6_61(Cap6Scene):
    numero = "6.61"
    titulo = "Energía cinética de una barra giratoria"
    lista_datos = [
        ("Masa de la barra:", r"M = 12.0\ \mathrm{kg}"),
        ("Longitud:", r"L = 2.00\ \mathrm{m}"),
        ("Giro:", r"5.00\ \mathrm{rev\ cada}\ 3.00\ \mathrm{s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        O = p(-1.5, 0.0)
        ang = np.deg2rad(35.0)
        udir = np.array([np.cos(ang), np.sin(ang), 0.0])
        pdir = np.array([-np.sin(ang), np.cos(ang), 0.0])
        E = O + 2.0 * udir
        self.f_linea(fig, "barra", O, E, color=self.WHITE, grosor=7)
        self.f_cuerpo(fig, "pivote", O, forma="punto", color=self.YELLOW)
        giro = CurvedArrow(O + LEFT * 0.7 + DOWN * 0.5, O + LEFT * 0.7 + UP * 0.6,
                           angle=PI / 2, color=self.YELLOW, tip_length=0.16)
        fig.registrar("giro", giro, lambda m: Create(m))
        self.f_texto(fig, "omega", r"\omega", (-2.5, 1.1, 0), size=30,
                     color=self.YELLOW, math=True)
        for i, r in enumerate([0.5, 1.0, 1.5, 2.0]):
            self.f_vector(fig, f"v{i}", O + r * udir, pdir, 0.28 * r + 0.12,
                          color=self.CYAN, etiqueta=None, grosor=6)
        return fig

    pasos = [
        {
            "titulo": "La barra gira alrededor de un extremo",
            "revelar": ["barra", "pivote", "giro", "omega"],
            "math": [r"\omega = \dfrac{5.00(2\pi)}{3.00} = 10.5\ \mathrm{rad/s}"],
        },
        {
            "titulo": "Cada punto va a distinta rapidez",
            "revelar": ["v0", "v1", "v2", "v3"],
            "math": [r"v = \omega r, \qquad I = \tfrac13 ML^2 = \tfrac13(12.0)(2.00)^2 = 16.0\ \mathrm{kg\,m^2}"],
            "text": ["El momento de inercia ya promedia todos esos puntos."],
        },
        {
            "titulo": "Energía cinética rotacional",
            "math": [
                r"K = \tfrac12 I\omega^2 = \tfrac12(16.0)(10.5)^2",
                r"K = 877\ \mathrm{J}",
            ],
        },
    ]
    resultado_latex = r"K = 877\ \mathrm{J}"


class P6_65(Cap6Scene):
    numero = "6.65"
    titulo = "Caja empujada rampa arriba"
    lista_datos = [
        ("Masa de la caja:", r"m = 20.0\ \mathrm{kg}"),
        ("Rampa:", r"15.0\ \mathrm{m},\ 34.0^\circ"),
        ("Empuje horizontal:", r"F = 290\ \mathrm{N}"),
        ("Fricción constante:", r"f_k = 65.0\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(34.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.0, -1.4)
        B = A + 4.5 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=6)
        self.f_linea(fig, "base", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"34^\circ", etiqueta_size=20)
        C = A + 2.0 * u + 0.42 * n
        g = self.f_cuerpo(fig, "caja", C, ancho=1.2, alto=0.72,
                          color=self.BLUE)
        g[0].rotate(th, about_point=C)
        self.f_texto(fig, "etCaja", "caja", C + UP * 0.62 + LEFT * 0.85,
                     size=22, color=self.WHITE)
        self.f_vector(fig, "F", C + LEFT * 0.6, RIGHT, 1.3, color=self.RED,
                      etiqueta=r"290", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "fk", C - 0.66 * u, -u, 0.8, color=self.YELLOW,
                      etiqueta=r"65", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "w", C, DOWN, 1.05, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "N", C, n, 1.0, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_linea(fig, "d15", A + 0.3 * u - 0.3 * n, A + 4.2 * u - 0.3 * n,
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"15", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Empuje horizontal rampa arriba",
            "revelar": ["rampa", "base", "theta", "caja", "etCaja", "d15"],
            "text": ["Parte del reposo al pie de la rampa."],
        },
        {
            "titulo": "a) Trabajo total sobre la caja",
            "revelar": ["F", "fk", "w", "N"],
            "math": [
                r"F_{\parallel} = 290\cos 34^\circ = 240\ \mathrm{N}",
                r"W = (240 - 65.0 - 196\sin 34^\circ)(15.0)",
                r"W = (65.8)(15.0) = 987\ \mathrm{J}",
            ],
            "resaltar": ["F", "fk"],
        },
        {
            "titulo": "b) Tiempo de subida",
            "math": [
                r"a = \dfrac{65.8}{20.0} = 3.29\ \mathrm{m/s^2}",
                r"t = \sqrt{\dfrac{2(15.0)}{3.29}} = 3.02\ \mathrm{s}",
            ],
        },
    ]
    resultado_latex = r"W = 987\ \mathrm{J}, \qquad t = 3.02\ \mathrm{s}"


class P6_66(Cap6Scene):
    numero = "6.66"
    titulo = "Trabajo sobre cada bloque del sistema"
    lista_datos = [
        ("Bloque en la mesa:", r"20.0\ \mathrm{N}"),
        ("Bloque colgante:", r"12.0\ \mathrm{N}"),
        ("Desplazamiento:", r"0.75\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.2, 0.0), p(1.4, 0.0), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "bloque20", p(-1.7, 0.42), ancho=1.15, alto=0.72,
                      color=self.BLUE, etiqueta="20 N")
        self.f_polea(fig, "polea", p(1.4, 0.42), radio=0.32, color=self.BLUE)
        self.f_linea(fig, "cuerdaH", p(-1.1, 0.42), p(1.08, 0.42), color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaV", p(1.4, 0.1), p(1.4, -0.45), color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "bloque12", p(1.4, -0.8), ancho=0.85, alto=0.6,
                      color=self.GREEN, etiqueta="12 N")
        self.f_linea(fig, "d75", p(-1.7, -0.75), p(-0.95, -0.75),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"0.75", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "T20", p(-1.1, 0.42), RIGHT, 0.85, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "T12", p(1.4, -0.5), UP, 0.7, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w12", p(1.4, -1.1), DOWN, 0.8, color=self.ORANGE,
                      etiqueta=r"12", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "fk", p(-1.7, 0.42), LEFT, 0.85, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El sistema de dos bloques se mueve",
            "revelar": ["mesa", "bloque20", "polea", "cuerdaH", "cuerdaV",
                        "bloque12", "d75"],
            "text": ["El de 12 N baja 0.75 m y el de 20 N avanza 0.75 m."],
        },
        {
            "titulo": "a) Sin fricción: la tensión acelera",
            "revelar": ["T20", "T12", "w12"],
            "math": [
                r"T = \dfrac{(20/9.8)(12)}{(32/9.8)} = 7.50\ \mathrm{N}",
                r"12\,\mathrm{N}: W_g = +9.00\ \mathrm{J},\ W_T = -5.62\ \mathrm{J}",
                r"20\,\mathrm{N}: W_T = +5.62\ \mathrm{J}",
            ],
            "resaltar": ["T20", "T12"],
        },
        {
            "titulo": "b) Con fricción: primero ver si se mueve",
            "revelar": ["fk"],
            "math": [
                r"f_{s,\max} = 0.500(20.0) = 10.0\ \mathrm{N} < 12.0\ \mathrm{N}",
                r"T = 9.94\ \mathrm{N}, \quad f_k = 0.325(20.0) = 6.50\ \mathrm{N}",
            ],
            "text": ["Sí se mueve: la estática no alcanza a sostenerlo."],
            "resaltar": ["fk"],
        },
        {
            "titulo": "Trabajos con fricción",
            "math": [
                r"12\,\mathrm{N}: W_g = +9.00\ \mathrm{J},\ W_T = -7.45\ \mathrm{J}",
                r"20\,\mathrm{N}: W_T = +7.45\ \mathrm{J},\ W_f = -4.88\ \mathrm{J}",
            ],
        },
    ]
    resultado_latex = r"a)\ T = 7.50\ \mathrm{N}; \qquad b)\ T = 9.94\ \mathrm{N}"


class P6_69(Cap6Scene):
    numero = "6.69"
    titulo = "Latigazo cervical: rapidez máxima segura"
    lista_datos = [
        ("Masa de la cabeza:", r"m = 5.0\ \mathrm{kg}"),
        ("Energía de fractura:", r"8.0\ \mathrm{J}"),
        ("Duración del choque:", r"10.0\ \mathrm{ms}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "piso", p(-3.4, -1.2), p(3.4, -1.2), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "auto", p(0.0, -0.6), ancho=2.2, alto=0.9,
                      color=self.BLUE, etiqueta="auto")
        self.f_cuerpo(fig, "cabeza", p(0.4, 0.35), ancho=0.6, alto=0.55,
                      color=self.ORANGE, etiqueta="5 kg")
        self.f_vector(fig, "choque", p(-2.9, -0.6), RIGHT, 1.2, color=self.RED,
                      etiqueta=r"choque", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "a", p(0.0, -1.55), RIGHT, 1.2, color=self.RED,
                      etiqueta=r"a", lado=DOWN, etiqueta_size=24)
        self.f_texto(fig, "etT", r"10.0\ \mathrm{ms}", (0.0, -2.0, 0), size=24,
                     color=self.MUTED, math=True)
        return fig

    pasos = [
        {
            "titulo": "Colisión por detrás de 10.0 ms",
            "revelar": ["piso", "auto", "cabeza", "choque", "etT"],
            "text": ["Los huesos del cuello absorben la energía de la cabeza."],
        },
        {
            "titulo": "a) Rapidez máxima sin fractura",
            "revelar": ["a"],
            "math": [
                r"\tfrac12 mv^2 = 8.0\ \mathrm{J}",
                r"v = \sqrt{\dfrac{2(8.0)}{5.0}} = 1.79\ \mathrm{m/s} = 4.0\ \mathrm{mph}",
            ],
            "resaltar": ["cabeza"],
        },
        {
            "titulo": "b) Aceleración de los pasajeros",
            "math": [
                r"a = \dfrac{\Delta v}{\Delta t} = \dfrac{1.79}{0.0100}",
                r"a = 179\ \mathrm{m/s^2} \approx 18g",
            ],
            "resaltar": ["a"],
        },
    ]
    resultado_latex = r"v_{\max} = 1.79\ \mathrm{m/s}\ (4.0\ \mathrm{mph}), \quad a = 179\ \mathrm{m/s^2}"


class P6_71(Cap6Scene):
    numero = "6.71"
    titulo = "Trabajo de una fuerza tipo gravitacional"
    lista_datos = [
        ("Fuerza atractiva:", r"F_x = -k/x^2"),
    ]

    def crear_figura(self):
        fig = Figura()
        axes = self.f_grafica(
            fig, "grafica", [lambda x: -1.0 / (x ** 2)],
            x_range=[0.5, 3.5, 0.5], y_range=[-2.0, 0.2, 0.5],
            x_label="x", y_label="F_x",
            ancho=4.4, alto=3.0, centro=(0.0, -0.2),
        )
        plot = fig.mob("grafica_c0")
        area = axes.get_area(plot, x_range=[1.0, 3.0], color=self.RED, opacity=0.3)
        fig.registrar("area", area, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "Fuerza atractiva hacia el origen",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "text": ["Como la gravedad: tira hacia el origen en todo x."],
        },
        {
            "titulo": "a) Trabajo de x₁ a x₂",
            "revelar": ["area"],
            "math": [
                r"W = \int_{x_1}^{x_2}\!-\dfrac{k}{x^2}\,dx = \left[\dfrac{k}{x}\right]_{x_1}^{x_2}",
                r"W = k\left(\dfrac{1}{x_2} - \dfrac{1}{x_1}\right)",
                r"\text{Si }x_2 > x_1:\ W < 0",
            ],
            "resaltar": ["area"],
        },
        {
            "titulo": "b) El trabajo que usted hace",
            "math": [
                r"W_{\mathrm{usted}} = -W = k\left(\dfrac{1}{x_1} - \dfrac{1}{x_2}\right)",
                r"\text{Si }x_2 > x_1:\ \text{positivo}",
            ],
            "text": ["Usted tira hacia afuera mientras la fuerza tira hacia adentro."],
        },
    ]
    resultado_latex = r"W = k\left(\dfrac{1}{x_2}-\dfrac{1}{x_1}\right)\ (< 0\ \text{si }x_2 > x_1)"


class P6_72(Cap6Scene):
    numero = "6.72"
    titulo = "Asteroide que cae a la Tierra"
    lista_datos = [
        ("Masa del asteroide:", r"m = 20000\ \mathrm{kg}"),
        ("Radio terrestre:", r"R = 6.37\times10^6\ \mathrm{m}"),
        ("Parte del reposo en:", r"x \to \infty"),
    ]

    def crear_figura(self):
        fig = Figura()
        Ct = p(-1.5, 0.9)
        tierra = Circle(radius=1.0, color=self.BLUE, stroke_width=7).move_to(Ct)
        fig.registrar("tierra", tierra, lambda m: Create(m))
        self.f_linea(fig, "radioT", Ct, Ct + p(0.7, -0.7), color=self.GREEN,
                     grosor=2, discontinuo=True, etiqueta=r"R", lado=DOWN,
                     etiqueta_size=22)
        A = p(1.7, 1.5)
        self.f_cuerpo(fig, "asteroide", A, forma="punto", color=self.ORANGE)
        self.f_vector(fig, "v", A, Ct - A, 1.1, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "Fg", A + DOWN * 0.3, Ct - A, 0.9, color=self.RED,
                      etiqueta=r"F_g", lado=RIGHT, etiqueta_size=22)
        axes = self.f_grafica(
            fig, "grafica", [lambda x: 1.0 / (x ** 2)],
            x_range=[1, 6, 1], y_range=[0, 1.2, 0.3],
            x_label="x\\,(R)", y_label="F\\,(mg)",
            ancho=3.4, alto=1.8, centro=(0.4, -2.0),
        )
        plot = fig.mob("grafica_c0")
        area = axes.get_area(plot, x_range=[1, 6], color=self.RED, opacity=0.3)
        fig.registrar("area", area, lambda m: FadeIn(m))
        return fig

    pasos = [
        {
            "titulo": "Caída desde muy lejos",
            "revelar": ["tierra", "radioT", "asteroide", "v"],
            "text": ["La gravedad crece como 1/x² al acercarse."],
        },
        {
            "titulo": "La fuerza en unidades de mg",
            "revelar": ["Fg", "grafica_ejes", "grafica_c0"],
            "math": [r"F = \dfrac{GMm}{x^2} = mg\left(\dfrac{R}{x}\right)^2"],
            "resaltar": ["Fg"],
        },
        {
            "titulo": "Trabajo: el área hasta la superficie",
            "revelar": ["area"],
            "math": [r"W = \int_{\infty}^{R}\!F\,dx = mgR"],
            "resaltar": ["area"],
        },
        {
            "titulo": "Rapidez mínima de impacto",
            "math": [
                r"\tfrac12 mv^2 = mgR \;\Rightarrow\; v = \sqrt{2gR}",
                r"v = \sqrt{2(9.80)(6.37\times10^6)} = 1.12\times10^4\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"v = 11.2\ \mathrm{km/s}"


class P6_75(Cap6Scene):
    numero = "6.75"
    titulo = "Bloque girando atado por un agujero"
    lista_datos = [
        ("Masa del bloque:", r"m = 0.0900\ \mathrm{kg}"),
        ("Radio inicial:", r"r = 0.40\ \mathrm{m},\ v = 0.70\ \mathrm{m/s}"),
        ("Radio final:", r"r = 0.10\ \mathrm{m},\ v = 2.80\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        O = p(-0.6, 0.2)
        self.f_texto(fig, "mesa", "vista superior", (-0.6, 2.3, 0), size=20,
                     color=self.MUTED)
        self.f_cuerpo(fig, "agujero", O, forma="punto", color=self.WHITE)
        orb1 = Circle(radius=1.35, color=self.MUTED, stroke_width=2).move_to(O)
        fig.registrar("orbita1", orb1, lambda m: Create(m))
        orb2 = Circle(radius=0.38, color=self.GREEN, stroke_width=2).move_to(O)
        fig.registrar("orbita2", orb2, lambda m: Create(m))
        B1 = O + p(1.35, 0.0)
        B2 = O + p(0.0, 0.38)
        self.f_linea(fig, "cuerda1", O, B1, color=self.WHITE, grosor=4)
        self.f_linea(fig, "cuerda2", O, B2, color=self.WHITE, grosor=4)
        self.f_cuerpo(fig, "bloque1", B1, forma="punto", color=self.CYAN)
        self.f_cuerpo(fig, "bloque2", B2, forma="punto", color=self.GREEN)
        self.f_linea(fig, "r1", O + DOWN * 0.5, B1 + DOWN * 0.5,
                     color=self.CYAN, grosor=2, discontinuo=True,
                     etiqueta=r"0.40", lado=DOWN, etiqueta_size=20)
        self.f_linea(fig, "r2", O + UP * 0.75, B2 + UP * 0.37,
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"0.10", lado=UP, etiqueta_size=20)
        self.f_vector(fig, "T1", B1, O - B1, 0.85, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "v1", B1, UP, 0.8, color=self.CYAN,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "T2", B2, O - B2, 0.7, color=self.GREEN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El bloque gira atado al centro",
            "revelar": ["mesa", "agujero", "orbita1", "cuerda1", "bloque1", "r1"],
            "text": ["La tensión apunta al centro: es la fuerza centrípeta."],
        },
        {
            "titulo": "a) Tensión con r = 0.40 m",
            "revelar": ["T1", "v1"],
            "math": [r"T = \dfrac{mv^2}{r} = \dfrac{(0.0900)(0.70)^2}{0.40} = 0.110\ \mathrm{N}"],
            "resaltar": ["T1"],
        },
        {
            "titulo": "Se tira de la cuerda hasta r = 0.10 m",
            "revelar": ["orbita2", "cuerda2", "bloque2", "r2", "T2"],
            "math": [r"T = \dfrac{(0.0900)(2.80)^2}{0.10} = 7.06\ \mathrm{N}"],
            "resaltar": ["T2"],
        },
        {
            "titulo": "c) Trabajo de quien tira",
            "math": [
                r"W = \Delta K = \tfrac12(0.0900)(2.80^2 - 0.70^2)",
                r"W = 0.331\ \mathrm{J}",
            ],
            "text": ["Acercar el bloque exige trabajo: gira más rápido."],
        },
    ]
    resultado_latex = r"T = 0.110\ \mathrm{N} \to 7.06\ \mathrm{N}, \quad W = 0.331\ \mathrm{J}"


class P6_76(Cap6Scene):
    numero = "6.76"
    titulo = "Protón contra un núcleo de uranio"
    lista_datos = [
        ("Masa del protón:", r"m = 1.67\times10^{-27}\ \mathrm{kg}"),
        ("Rapidez inicial:", r"v_0 = 3.00\times10^5\ \mathrm{m/s}"),
        ("Repulsión:", r"F = \alpha/x^2,\ \alpha = 2.12\times10^{-26}"),
    ]

    def crear_figura(self):
        fig = Figura()
        N = p(-2.4, 0.2)
        self.f_cuerpo(fig, "nucleo", N, ancho=0.7, alto=0.7,
                      color=self.RED, etiqueta="U")
        self.f_linea(fig, "eje", p(-2.4, 0.2), p(2.6, 0.2), color=self.MUTED, grosor=2)
        P = p(1.6, 0.2)
        self.f_cuerpo(fig, "proton", P, forma="punto", color=self.CYAN)
        self.f_vector(fig, "v0", P, LEFT, 1.2, color=self.CYAN,
                      etiqueta=r"v_0", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "F", P + UP * 0.25, RIGHT, 1.1, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "d1", p(1.6, -0.6), p(1.6, -1.1),
                     color=self.CYAN, grosor=2, discontinuo=True,
                     etiqueta=r"5.00", lado=DOWN, etiqueta_size=20)
        self.f_linea(fig, "d2", p(-0.6, -0.6), p(-0.6, -1.1),
                     color=self.YELLOW, grosor=2, discontinuo=True,
                     etiqueta=r"8{\times}10^{-10}", lado=DOWN, etiqueta_size=18)
        return fig

    pasos = [
        {
            "titulo": "Repulsión eléctrica frena al protón",
            "revelar": ["nucleo", "eje", "proton", "v0", "F", "d1"],
            "text": ["La fuerza crece como 1/x² al acercarse al núcleo."],
        },
        {
            "titulo": "a) Rapidez a 8.00×10⁻¹⁰ m",
            "revelar": ["d2"],
            "math": [
                r"W = -\alpha\left(\dfrac{1}{x_2}-\dfrac{1}{x_1}\right) = -2.65\times10^{-17}\ \mathrm{J}",
                r"v = 2.41\times10^5\ \mathrm{m/s}",
            ],
            "resaltar": ["F"],
        },
        {
            "titulo": "b) Máximo acercamiento",
            "math": [
                r"\tfrac12 mv_0^2 = \alpha\left(\dfrac{1}{x_{\min}}-\dfrac{1}{5.00}\right)",
                r"x_{\min} = 2.82\times10^{-10}\ \mathrm{m}",
            ],
        },
        {
            "titulo": "c) De regreso a 5.00 m",
            "math": [r"v = 3.00\times10^5\ \mathrm{m/s}"],
            "text": ["La fuerza es conservativa: recupera su rapidez inicial."],
        },
    ]
    resultado_latex = r"v = 2.41\times10^5\ \mathrm{m/s}, \quad x_{\min} = 2.82\times10^{-10}\ \mathrm{m}"


class P6_80(Cap6Scene):
    numero = "6.80"
    titulo = "Esfera disparada por un rifle de resorte"
    lista_datos = [
        ("Constante:", r"k = 400\ \mathrm{N/m}"),
        ("Compresión:", r"6.00\ \mathrm{cm}"),
        ("Masa de la esfera:", r"m = 0.0300\ \mathrm{kg}"),
        ("Resistencia en el cañón:", r"6.00\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "tuboS", p(-2.8, 0.35), p(-0.2, 0.35), color=self.MUTED, grosor=3)
        self.f_linea(fig, "tuboI", p(-2.8, -0.35), p(-0.2, -0.35), color=self.MUTED, grosor=3)
        fig.registrar("resorte", resorte(p(-2.8, 0.0), p(-1.6, 0.0), vueltas=8),
                       lambda m: Create(m))
        self.f_cuerpo(fig, "esfera", p(-1.35, 0.0), ancho=0.5, alto=0.5,
                      color=self.ORANGE, etiqueta="m")
        self.f_vector(fig, "v", p(-1.35, 0.0), RIGHT, 1.1, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "mMax", p(-0.7, -0.35), p(-0.7, -0.9),
                     color=self.YELLOW, grosor=2, discontinuo=True,
                     etiqueta=r"v_{\max}", lado=DOWN, etiqueta_size=20)
        self.f_linea(fig, "boca", p(-0.2, -0.35), p(-0.2, -0.9),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"salida", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "El resorte empuja a la esfera por el cañón",
            "revelar": ["tuboS", "tuboI", "resorte", "esfera", "v", "boca"],
            "text": ["La esfera sale justo al agotarse el resorte."],
        },
        {
            "titulo": "a) Sin fricción: rapidez de salida",
            "math": [
                r"\tfrac12 kx^2 = \tfrac12 mv^2",
                r"v = 0.0600\sqrt{\dfrac{400}{0.0300}} = 6.93\ \mathrm{m/s}",
            ],
            "resaltar": ["boca"],
        },
        {
            "titulo": "b) Con resistencia de 6.00 N",
            "math": [
                r"\tfrac12 kx^2 - Fd = \tfrac12 mv^2",
                r"0.720 - 0.360 = \tfrac12(0.0300)v^2",
                r"v = 4.90\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "c) Dónde va más rápido",
            "revelar": ["mMax"],
            "math": [
                r"kx = 6.00 \;\Rightarrow\; x = 0.0150\ \mathrm{m}",
                r"d = 0.0600 - 0.0150 = 0.0450\ \mathrm{m},\quad v = 5.48\ \mathrm{m/s}",
            ],
            "text": ["El máximo es donde el resorte iguala a la resistencia."],
            "resaltar": ["mMax"],
        },
    ]
    resultado_latex = r"v_a = 6.93\ \mathrm{m/s}, \quad v_b = 4.90\ \mathrm{m/s}, \quad v_{\max} = 5.48\ \mathrm{m/s}"


class P6_81(Cap6Scene):
    numero = "6.81"
    titulo = "Libro lanzado por un resorte sobre mesa áspera"
    lista_datos = [
        ("Masa del libro:", r"m = 2.50\ \mathrm{kg}"),
        ("Constante:", r"k = 250\ \mathrm{N/m}"),
        ("Compresión:", r"x = 0.250\ \mathrm{m}"),
        ("Fricción:", r"\mu_k = 0.30"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.4, -0.5), p(3.2, -0.5), color=self.MUTED, grosor=4)
        self.f_linea(fig, "pared", p(-3.1, -0.5), p(-3.1, 1.5), color=self.MUTED, grosor=4)
        fig.registrar("resorte", resorte(p(-3.1, 0.25), p(-2.1, 0.25), vueltas=8),
                       lambda m: Create(m))
        self.f_cuerpo(fig, "libro", p(-1.55, -0.05), ancho=1.0, alto=0.7,
                      color=self.BLUE, etiqueta="libro")
        self.f_vector(fig, "v", p(-1.05, -0.05), RIGHT, 1.1, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", p(-2.05, -0.05), LEFT, 1.0, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=24)
        self.f_linea(fig, "d", p(-2.1, -1.0), p(0.9, -1.0),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"d", lado=DOWN, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El resorte lanza al libro sobre lo áspero",
            "revelar": ["mesa", "pared", "resorte", "libro", "v", "fk"],
            "text": ["La fricción actúa en todo el recorrido, incluso mientras empuja el resorte."],
        },
        {
            "titulo": "Toda la energía la gasta la fricción",
            "revelar": ["d"],
            "math": [
                r"\tfrac12 kx^2 = f_k d = \mu_k mg\,d",
                r"d = \dfrac{0.5(250)(0.250)^2}{0.30(2.50)(9.80)}",
                r"d = \dfrac{7.81}{7.35} = 1.06\ \mathrm{m}",
            ],
            "resaltar": ["d", "fk"],
        },
    ]
    resultado_latex = r"d = 1.06\ \mathrm{m}\ \text{desde que se suelta}"
