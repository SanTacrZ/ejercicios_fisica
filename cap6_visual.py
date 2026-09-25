"""Capítulo 6 - Edición visual paso a paso (motor de figuras de fisica_base).

Tema: trabajo y energía cinética. La idea visual central es que el trabajo
es el ÁREA bajo la curva F(x): cada fórmula se mapea a una región sombreada.

Render de una escena:
    manim -ql cap6_visual.py P6_1
Render del lote:
    manim -ql cap6_visual.py

LOTE 1 (orden de la lista): 6.1, 6.4, 6.5, 6.6, 6.8
PENDIENTES cap6:
    12, 14, 19, 20, 21, 33, 34, 35, 37, 43, 45, 46, 52, 56,
    60, 61, 65, 66, 69, 71, 72, 75, 76, 80, 81, 84, 85, 87, 94, 97
"""

import numpy as np

from manim import *
from fisica_base import ProblemaScene, Figura


def p(x, y):
    return np.array([x, y, 0.0])


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
