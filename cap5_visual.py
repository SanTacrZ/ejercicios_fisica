"""Capítulo 5 - Edición visual paso a paso (motor de figuras de fisica_base).

Los diagramas reproducen las figuras del libro (Sears-Zemansky, 13a ed.):
    E5.2, E5.7, E5.9, E5.10, E5.13
Cada problema define `crear_figura()` (diagrama persistente que se revela por
partes) y `pasos` con las ecuaciones que se escriben al lado.

Render de una escena:
    manim -ql cap5_visual.py P5_2
Render del lote:
    manim -ql cap5_visual.py

LOTE 1 (orden de la lista): 5.2, 5.7, 5.9, 5.10, 5.13
LOTE 2 (orden de la lista): 5.14, 5.15, 5.17, 5.19, 5.21
LOTE 3 (orden de la lista): 5.27, 5.31, 5.33, 5.34, 5.42
LOTE 4 (orden de la lista): 5.44, 5.45, 5.46, 5.47, 5.51
LOTE 5 (orden de la lista): 5.56, 5.57, 5.58, 5.59, 5.60
LOTE 6 (orden de la lista): 5.65, 5.66, 5.68, 5.72, 5.74
LOTE 7 (orden de la lista): 5.77, 5.80, 5.84, 5.85, 5.87
PENDIENTES cap5:
    92, 100, 101, 103, 110, 112, 119, 127
"""

import numpy as np

from manim import *
from fisica_base import ProblemaScene, Figura


def p(x, y):
    return np.array([x, y, 0.0])


class P5_2(ProblemaScene):
    numero = "5.2"
    titulo = "Tres arreglos de poleas en equilibrio"
    subtitulo = "Primera ley de Newton · poleas y cuerdas ideales"
    lista_datos = [("Peso de cada bloque:", r"w")]

    def crear_figura(self):
        fig = Figura()
        # ---------------- caso a) cuerda anclada a la pared ----------------
        self.f_linea(fig, "a_pared", p(-3.45, -1.0), p(-3.45, 1.8), color=self.MUTED, grosor=3)
        self.f_polea(fig, "a_polea", p(-2.6, 1.3), radio=0.3, color=self.BLUE)
        self.f_linea(fig, "a_ramo", p(-3.45, 1.3), p(-2.9, 1.3), color=self.WHITE, grosor=3)
        self.f_linea(fig, "a_cuerda", p(-2.6, 1.0), p(-2.6, 0.28), color=self.WHITE, grosor=3)
        self.f_cuerpo(fig, "a_bloque", p(-2.6, -0.05), ancho=0.6, alto=0.5,
                      color=self.ORANGE, etiqueta="w")
        self.f_vector(fig, "a_T", p(-2.6, 0.2), UP, 0.72, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=20)
        # ---------------- caso b) polea fija, dos pesos ----------------
        self.f_linea(fig, "b_techo", p(-1.0, 1.8), p(1.0, 1.8), color=self.MUTED, grosor=3)
        self.f_polea(fig, "b_polea", p(0.0, 1.3), radio=0.3, color=self.BLUE)
        self.f_linea(fig, "b_cuerdaI", p(-0.3, 1.3), p(-0.3, 0.28), color=self.WHITE, grosor=3)
        self.f_linea(fig, "b_cuerdaD", p(0.3, 1.3), p(0.3, 0.28), color=self.WHITE, grosor=3)
        self.f_cuerpo(fig, "b_bloque1", p(-0.3, -0.05), ancho=0.6, alto=0.5,
                      color=self.ORANGE, etiqueta="w")
        self.f_cuerpo(fig, "b_bloque2", p(0.3, -0.05), ancho=0.6, alto=0.5,
                      color=self.ORANGE, etiqueta="w")
        self.f_vector(fig, "b_T1", p(-0.3, 0.2), UP, 0.68, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "b_T2", p(0.3, 0.2), UP, 0.68, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=20)
        # ---------------- caso c) dos poleas fijas ----------------
        self.f_linea(fig, "c_viga", p(1.35, 1.8), p(3.65, 1.8), color=self.MUTED, grosor=3)
        self.f_polea(fig, "c_polea1", p(2.0, 1.3), radio=0.3, color=self.BLUE)
        self.f_polea(fig, "c_polea2", p(3.0, 1.3), radio=0.3, color=self.BLUE)
        self.f_linea(fig, "c_cuerdaI", p(1.7, 1.3), p(1.7, 0.28), color=self.WHITE, grosor=3)
        self.f_linea(fig, "c_cuerdaD", p(3.3, 1.3), p(3.3, 0.28), color=self.WHITE, grosor=3)
        self.f_linea(fig, "c_cuerdaM", p(2.0, 1.6), p(3.0, 1.6), color=self.WHITE, grosor=3)
        self.f_cuerpo(fig, "c_bloque1", p(1.7, -0.05), ancho=0.6, alto=0.5,
                      color=self.ORANGE, etiqueta="w")
        self.f_cuerpo(fig, "c_bloque2", p(3.3, -0.05), ancho=0.6, alto=0.5,
                      color=self.ORANGE, etiqueta="w")
        self.f_vector(fig, "c_T1", p(1.7, 0.2), UP, 0.68, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "c_T2", p(3.3, 0.2), UP, 0.68, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Tres arreglos con poleas ideales",
            "revelar": ["a_pared", "a_polea", "a_ramo", "a_cuerda", "a_bloque",
                        "b_techo", "b_polea", "b_cuerdaI", "b_cuerdaD",
                        "b_bloque1", "b_bloque2",
                        "c_viga", "c_polea1", "c_polea2", "c_cuerdaI",
                        "c_cuerdaD", "c_cuerdaM", "c_bloque1", "c_bloque2"],
            "text": ["Cada bloque pesa w y todo está en reposo (a = 0)."],
        },
        {
            "titulo": "Caso a) la cuerda se ancla a la pared",
            "revelar": ["a_T"],
            "math": [r"\sum F_y = 0 \;\Rightarrow\; T - w = 0", r"T = w"],
            "text": ["La polea solo cambia la dirección de la cuerda."],
            "resaltar": ["a_T"],
        },
        {
            "titulo": "Caso b) una polea fija con dos pesos",
            "revelar": ["b_T1", "b_T2"],
            "math": [r"T = w \quad \text{(en cada rama)}"],
            "resaltar": ["b_T1", "b_T2"],
        },
        {
            "titulo": "Caso c) dos poleas fijas",
            "revelar": ["c_T1", "c_T2"],
            "math": [r"T = w"],
            "resaltar": ["c_T1", "c_T2"],
        },
        {
            "titulo": "La idea que unifica los tres casos",
            "math": [r"\boxed{T = w} \quad \text{en los tres arreglos}"],
            "text": ["Una cuerda ideal transmite la misma tensión; la polea solo redirige."],
        },
    ]
    resultado_latex = r"a)\ T = w, \qquad b)\ T = w, \qquad c)\ T = w"


class P5_7(ProblemaScene):
    numero = "5.7"
    titulo = "Tensión en cada cuerda de un objeto suspendido"
    subtitulo = "Primera ley de Newton · partícula en equilibrio"
    lista_datos = [("Peso suspendido:", r"w")]

    TECHO_Y = 1.5
    NUDO = p(0.0, -0.3)

    def crear_figura(self):
        fig = Figura()
        nudo = self.NUDO
        ty = self.TECHO_Y

        def tope(ang_deg, lado):
            ang = np.deg2rad(ang_deg)
            largo = (ty - nudo[1]) / np.sin(ang)
            x = nudo[0] + (-1 if lado == "izq" else 1) * largo * np.cos(ang)
            return p(x, ty)

        a_izq = tope(30, "izq")
        a_der = tope(45, "der")
        b_izq = tope(60, "izq")

        self.f_linea(fig, "techo", p(-3.5, ty), p(2.1, ty), color=self.MUTED, grosor=3)
        self.f_linea(fig, "cuerdaA", nudo, a_izq, color=self.CYAN, grosor=3)
        self.f_linea(fig, "cuerdaB", nudo, a_der, color=self.GREEN, grosor=3)
        self.f_linea(fig, "cuerdaA2", nudo, b_izq, color=self.CYAN, grosor=3)
        self.f_cuerpo(fig, "nudo", nudo, forma="punto", color=self.WHITE)
        self.f_linea(fig, "cuerdaV", nudo, p(0.0, -1.35), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "bloque", p(0.0, -1.65), ancho=1.0, alto=0.6,
                      color=self.BLUE, etiqueta="w")

        self.f_angulo(fig, "angA", a_izq, p(a_izq[0] + 1.0, ty), nudo,
                      radio=0.45, etiqueta=r"30^\circ", etiqueta_size=20)
        self.f_angulo(fig, "angB", a_der, p(a_der[0] - 1.0, ty), nudo,
                      radio=0.45, etiqueta=r"45^\circ", etiqueta_size=20)
        self.f_angulo(fig, "angA2", b_izq, p(b_izq[0] + 1.0, ty), nudo,
                      radio=0.45, etiqueta=r"60^\circ", etiqueta_size=20)

        self.f_vector(fig, "TA", nudo, a_izq - nudo, 1.15, color=self.CYAN,
                      etiqueta=r"T_A", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "TB", nudo, a_der - nudo, 1.15, color=self.GREEN,
                      etiqueta=r"T_B", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "TA2", nudo, b_izq - nudo, 1.15, color=self.CYAN,
                      etiqueta=r"T_A", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "w", nudo, DOWN, 1.05, color=self.ORANGE,
                      etiqueta=r"w", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El objeto cuelga de dos cuerdas",
            "revelar": ["techo", "cuerdaA", "cuerdaB", "nudo", "cuerdaV",
                        "bloque", "angA", "angB"],
            "text": ["El nudo C está en reposo: es una partícula en equilibrio."],
        },
        {
            "titulo": "Diagrama de cuerpo libre del nudo C",
            "revelar": ["TA", "TB", "w"],
            "math": [r"\sum F_x = 0, \qquad \sum F_y = 0"],
            "text": ["Solo actúan las dos tensiones y el peso del objeto."],
            "resaltar": ["TA", "TB", "w"],
        },
        {
            "titulo": "Caso a) cuerdas a 30° y 45°",
            "math": [
                r"T_A\cos 30^\circ = T_B\cos 45^\circ",
                r"T_A\sin 30^\circ + T_B\sin 45^\circ = w",
                r"T_A = 0.732\,w, \qquad T_B = 0.897\,w",
            ],
            "resaltar": ["TA", "TB"],
        },
        {
            "titulo": "Caso b) la cuerda A pasa a 60°",
            "ocultar": ["cuerdaA", "angA", "TA"],
            "revelar": ["cuerdaA2", "angA2", "TA2"],
            "math": [
                r"T_A\cos 60^\circ = T_B\cos 45^\circ",
                r"T_A\sin 60^\circ + T_B\sin 45^\circ = w",
                r"T_A = 0.732\,w, \qquad T_B = 0.518\,w",
            ],
            "resaltar": ["TA2", "TB"],
        },
    ]
    resultado_latex = r"a)\ T_A = 0.732\,w,\ T_B = 0.897\,w"
    resultado_nota = "b) al inclinar más la cuerda A, T_B disminuye."


class P5_9(ProblemaScene):
    numero = "5.9"
    titulo = "Piano que baja deslizándose por una rampa"
    subtitulo = "Primera ley de Newton · rampa sin fricción"
    lista_datos = [
        ("Masa del piano:", r"m = 180\ \mathrm{kg}"),
        ("Inclinación:", r"\theta = 11.0^\circ"),
        ("Movimiento:", r"\text{rapidez constante}"),
    ]

    def crear_figura(self):
        fig = Figura()
        geo = self.f_plano_inclinado(fig, "rampa", base=(-3.0, -1.8, 0),
                                     angulo_grados=11, largo=5.0)
        A, u, th = geo["A"], geo["u"], geo["theta"]
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.7,
                      etiqueta=r"\theta", etiqueta_size=24)

        centro = A + 2.6 * u + 0.4 * n
        self.f_cuerpo(fig, "bloque", centro, ancho=1.3, alto=0.75,
                      color=self.BLUE, etiqueta="piano")
        self.f_vector(fig, "w", centro, DOWN, 1.6, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=24)
        self.f_vector(fig, "N", centro, n, 1.55, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_descomponer(fig, "w", centro, DOWN, 1.6, eje1=u, eje2=n,
                           etiqueta_x=r"mg\sin\theta", etiqueta_y=r"mg\cos\theta",
                           desplaz_x=(-0.85, -0.62), desplaz_y=(0.85, 0.0))
        self.f_vector(fig, "F_a", centro, u, 0.85, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "F_b", centro, RIGHT, 1.0, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El piano baja a rapidez constante",
            "revelar": ["rampa", "bloque", "theta"],
            "text": ["Sin fricción y sin aceleración: de nuevo ΣF = 0."],
        },
        {
            "titulo": "Diagrama de cuerpo libre",
            "revelar": ["w", "N"],
            "math": [r"\sum \vec F = 0"],
            "text": ["Actúan el peso, la normal y la fuerza F que lo sostiene."],
            "resaltar": ["w", "N"],
        },
        {
            "titulo": "Descomponemos el peso en ejes de la rampa",
            "revelar": ["w_guia", "w_x", "w_y"],
            "math": [r"mg_\parallel = mg\sin\theta, \qquad mg_\perp = mg\cos\theta"],
            "resaltar": ["w_x", "w_y"],
        },
        {
            "titulo": "a) Empuje paralelo a la rampa",
            "revelar": ["F_a"],
            "math": [
                r"F = mg\sin 11.0^\circ = (180)(9.80)(0.1908)",
                r"F = 337\ \mathrm{N}",
            ],
            "resaltar": ["F_a", "w_x"],
        },
        {
            "titulo": "b) Empuje paralelo al piso",
            "ocultar": ["F_a"],
            "revelar": ["F_b"],
            "math": [
                r"F\cos 11.0^\circ = mg\sin 11.0^\circ",
                r"F = mg\tan 11.0^\circ = 343\ \mathrm{N}",
            ],
            "resaltar": ["F_b"],
        },
    ]
    resultado_latex = r"F_{\parallel} = 337\ \mathrm{N}, \qquad F_{\mathrm{piso}} = 343\ \mathrm{N}"


class P5_10(ProblemaScene):
    numero = "5.10"
    titulo = "Cuerda inclinada con fuerzas horizontales"
    subtitulo = "Primera ley de Newton · dos nudos en equilibrio"
    lista_datos = [("Peso suspendido:", r"w = 60.0\ \mathrm{N}")]

    O = p(-1.2, 1.3)
    P = p(0.21, -0.11)

    def crear_figura(self):
        fig = Figura()
        O, P = self.O, self.P
        self.f_linea(fig, "techo", p(-3.2, 2.3), p(1.6, 2.3), color=self.MUTED, grosor=3)
        self.f_linea(fig, "soporte", O, p(O[0], 2.3), color=self.WHITE, grosor=3)
        self.f_linea(fig, "cuerdaInc", O, P, color=self.WHITE, grosor=3)
        self.f_cuerpo(fig, "nudoO", O, forma="punto", color=self.WHITE)
        self.f_cuerpo(fig, "nudoP", P, forma="punto", color=self.WHITE)
        self.f_linea(fig, "cuerdaV", P, p(P[0], -0.75), color=self.WHITE, grosor=3)
        self.f_cuerpo(fig, "bloque", p(P[0], -1.05), ancho=0.7, alto=0.55,
                      color=self.ORANGE, etiqueta="w")

        self.f_angulo(fig, "ang45", O, O + RIGHT, P, radio=0.6,
                      etiqueta=r"45^\circ", etiqueta_size=20)
        self.f_angulo(fig, "ang90a", O, O + UP, O + LEFT, radio=0.5,
                      etiqueta=r"90^\circ", etiqueta_size=18)
        self.f_angulo(fig, "ang90b", P, P + RIGHT, P + DOWN, radio=0.45,
                      etiqueta=r"90^\circ", etiqueta_size=18)

        self.f_vector(fig, "T_inc", P, O - P, 0.95, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "w", p(P[0], -1.05), DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"w", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "F1", O, LEFT, 1.1, color=self.RED,
                      etiqueta=r"\vec F_1", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "F2", P, RIGHT, 1.1, color=self.RED,
                      etiqueta=r"\vec F_2", lado=UP, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Dos nudos unidos por una cuerda a 45°",
            "revelar": ["techo", "soporte", "cuerdaInc", "nudoO", "nudoP",
                        "cuerdaV", "bloque", "ang45", "ang90a", "ang90b"],
            "text": ["El nudo superior O y el inferior P están en reposo."],
        },
        {
            "titulo": "Nudo inferior P: equilibrio vertical",
            "revelar": ["T_inc", "w"],
            "math": [
                r"T\sin 45^\circ - w = 0 \;\Rightarrow\; T = \dfrac{w}{\sin 45^\circ}",
                r"T = \dfrac{60.0}{0.7071} = 84.9\ \mathrm{N}",
            ],
            "resaltar": ["T_inc", "w"],
        },
        {
            "titulo": "Equilibrio horizontal en O y en P",
            "revelar": ["F1", "F2"],
            "math": [
                r"F_1 = F_2 = T\cos 45^\circ = w",
                r"F_1 = F_2 = 60.0\ \mathrm{N}",
            ],
            "text": ["Las fuerzas horizontales sostienen la componente horizontal de T."],
            "resaltar": ["F1", "F2"],
        },
    ]
    resultado_latex = r"T = 84.9\ \mathrm{N}, \qquad F_1 = F_2 = 60.0\ \mathrm{N}"


class P5_13(ProblemaScene):
    numero = "5.13"
    titulo = "Choque de la nave Génesis"
    subtitulo = "Segunda ley de Newton · choque con aceleración constante"
    lista_datos = [
        ("Masa de la cápsula:", r"m = 210\ \mathrm{kg}"),
        ("Rapidez de impacto:", r"v = 311\ \mathrm{km/h} = 86.4\ \mathrm{m/s}"),
        ("Profundidad:", r"d = 81.0\ \mathrm{cm} = 0.810\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-3.1, 0.9), p(0.3, 0.9), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "capsula", p(-1.7, 2.0), ancho=0.8, alto=0.55,
                      color=self.BLUE)
        self.f_vector(fig, "v", p(-1.7, 2.0), DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"v", lado=RIGHT, etiqueta_size=24)
        self.f_linea(fig, "d_marca", p(-1.7, 0.9), p(-1.7, 0.1),
                     color=self.YELLOW, grosor=3, discontinuo=True,
                     etiqueta=r"d", lado=LEFT, etiqueta_size=22)
        self.f_grafica(
            fig, "grafica",
            funciones=[lambda t: 86.4 * (1.0 - t / 18.8)],
            x_range=[0, 18.8, 4], y_range=[0, 90, 30],
            x_label="t\\,(\\mathrm{ms})", y_label="v\\,(\\mathrm{m/s})",
            ancho=3.8, alto=2.1, centro=(1.7, -2.0),
        )
        return fig

    pasos = [
        {
            "titulo": "La cápsula golpea el suelo y se detiene",
            "revelar": ["suelo", "capsula", "v"],
            "text": ["Conocemos la rapidez de impacto y la distancia de frenado."],
        },
        {
            "titulo": "Cinemática: de v a la aceleración",
            "revelar": ["d_marca", "grafica_ejes"],
            "math": [
                r"v^2 = v_0^2 + 2a\,d \;\Rightarrow\; a = \dfrac{v^2}{2d}",
            ],
            "text": ["La pendiente de la recta v(t) es la aceleración."],
        },
        {
            "titulo": "Aceleración durante el choque",
            "revelar": ["grafica_c0"],
            "math": [
                r"a = \dfrac{(86.4)^2}{2(0.810)} = 4.61\times10^3\ \mathrm{m/s^2}",
                r"a = 470\,g",
            ],
            "resaltar": ["grafica_c0"],
        },
        {
            "titulo": "Fuerza del suelo sobre la cápsula",
            "math": [
                r"F = ma = (210)(4.61\times10^3) = 9.67\times10^5\ \mathrm{N}",
                r"F = 470\,w",
            ],
        },
        {
            "titulo": "Duración de la fuerza",
            "math": [r"t = \dfrac{v}{a} = \dfrac{86.4}{4.61\times10^3} = 18.8\ \mathrm{ms}"],
            "text": ["El área bajo v(t) es la distancia penetrada d."],
        },
    ]
    resultado_latex = r"a = 470\,g, \quad F = 9.67\times10^5\ \mathrm{N}, \quad t = 18.8\ \mathrm{ms}"


class P5_14(ProblemaScene):
    numero = "5.14"
    titulo = "Tres trineos tirados sobre hielo"
    subtitulo = "Segunda ley de Newton · sistema de varios cuerpos"
    lista_datos = [
        ("Masas de los trineos:", r"30.0,\ 20.0,\ 10.0\ \mathrm{kg}"),
        ("Fuerza de tirón:", r"F = 125\ \mathrm{N}"),
        ("Hielo sin fricción", r"a = ?"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "hielo", p(-4.1, -0.45), p(4.1, -0.45), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "s30", p(-3.0, -0.05), ancho=1.1, alto=0.7,
                      color=self.BLUE, etiqueta=r"30")
        self.f_cuerpo(fig, "s20", p(-0.9, -0.05), ancho=1.1, alto=0.7,
                      color=self.BLUE, etiqueta=r"20")
        self.f_cuerpo(fig, "s10", p(1.2, -0.05), ancho=1.1, alto=0.7,
                      color=self.BLUE, etiqueta=r"10")
        self.f_linea(fig, "cuerdaB", p(-2.45, -0.05), p(-1.45, -0.05), color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaA", p(-0.35, -0.05), p(0.65, -0.05), color=self.WHITE, grosor=5)
        self.f_vector(fig, "tiron", p(1.75, -0.05), RIGHT, 1.05, color=self.RED,
                      etiqueta=r"F = 125\ \mathrm{N}", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "T_A", p(0.15, -0.05), RIGHT, 0.5, color=self.GREEN,
                      etiqueta=r"T_A", lado=UP, etiqueta_size=20)
        self.f_vector(fig, "T_B", p(-1.95, -0.05), RIGHT, 0.5, color=self.YELLOW,
                      etiqueta=r"T_B", lado=UP, etiqueta_size=20)
        self.f_vector(fig, "acc", p(2.95, -0.05), RIGHT, 0.8, color=self.CYAN,
                      etiqueta=r"a", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Tres trineos unidos por cuerdas",
            "revelar": ["hielo", "s30", "s20", "s10", "cuerdaB", "cuerdaA", "tiron"],
            "text": ["Masa total = 30 + 20 + 10 = 60.0 kg; el hielo no tiene fricción."],
        },
        {
            "titulo": "Aceleración de todo el sistema",
            "revelar": ["acc"],
            "math": [
                r"a = \dfrac{F}{m_1+m_2+m_3} = \dfrac{125}{60.0}",
                r"a = 2.08\ \mathrm{m/s^2}",
            ],
            "resaltar": ["acc"],
        },
        {
            "titulo": "Tensión en la cuerda A (trineo de 10 kg)",
            "revelar": ["T_A"],
            "math": [
                r"F - T_A = m_3 a",
                r"T_A = 125 - (10.0)(2.08) = 104\ \mathrm{N}",
            ],
            "resaltar": ["T_A"],
        },
        {
            "titulo": "Tensión en la cuerda B (trineo de 30 kg)",
            "revelar": ["T_B"],
            "math": [
                r"T_B = m_1 a = (30.0)(2.08)",
                r"T_B = 62.5\ \mathrm{N}",
            ],
            "resaltar": ["T_B"],
        },
    ]
    resultado_latex = r"a = 2.08\ \mathrm{m/s^2},\quad T_A = 104\ \mathrm{N},\quad T_B = 62.5\ \mathrm{N}"


class P5_15(ProblemaScene):
    numero = "5.15"
    titulo = "Máquina de Atwood"
    subtitulo = "Segunda ley de Newton · polea ideal"
    lista_datos = [
        ("Carga de ladrillos:", r"m_1 = 15.0\ \mathrm{kg}"),
        ("Contrapeso:", r"m_2 = 28.0\ \mathrm{kg}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "soporte", p(0.0, 1.25), p(0.0, 2.1), color=self.MUTED, grosor=3)
        self.f_linea(fig, "techo", p(-2.0, 2.1), p(2.0, 2.1), color=self.MUTED, grosor=3)
        self.f_polea(fig, "polea", p(0.0, 1.25), radio=0.5, color=self.BLUE)
        self.f_linea(fig, "cuerdaI", p(-0.5, 1.25), p(-0.5, -0.55), color=self.WHITE, grosor=4)
        self.f_linea(fig, "cuerdaD", p(0.5, 1.25), p(0.5, -0.55), color=self.WHITE, grosor=4)
        self.f_cuerpo(fig, "bloque1", p(-0.5, -0.95), ancho=1.0, alto=0.7,
                      color=self.BLUE, etiqueta=r"m_1")
        self.f_cuerpo(fig, "bloque2", p(0.5, -0.95), ancho=1.0, alto=0.7,
                      color=self.GREEN, etiqueta=r"m_2")
        self.f_vector(fig, "w1", p(-0.5, -1.3), DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"m_1g", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w2", p(0.5, -1.3), DOWN, 1.35, color=self.ORANGE,
                      etiqueta=r"m_2g", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "T1", p(-0.5, -0.6), UP, 0.75, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "T2", p(0.5, -0.6), UP, 0.75, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "acc", p(1.15, 0.2), DOWN, 0.8, color=self.RED,
                      etiqueta=r"a", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Dos masas unidas por una cuerda sobre una polea",
            "revelar": ["soporte", "techo", "polea", "cuerdaI", "cuerdaD",
                        "bloque1", "bloque2"],
            "text": ["La cuerda ideal transmite la misma tensión T a ambos lados."],
        },
        {
            "titulo": "Segunda ley para cada masa",
            "revelar": ["w1", "w2", "T1", "T2", "acc"],
            "math": [
                r"m_1:\quad T - m_1g = m_1a",
                r"m_2:\quad m_2g - T = m_2a",
            ],
            "text": ["m₂ baja y m₁ sube: la aceleración tiene el mismo módulo."],
        },
        {
            "titulo": "Aceleración del sistema",
            "math": [
                r"a = \dfrac{(m_2-m_1)g}{m_1+m_2} = \dfrac{(13.0)(9.80)}{43.0}",
                r"a = 2.96\ \mathrm{m/s^2}",
            ],
            "resaltar": ["acc"],
        },
        {
            "titulo": "Tensión en la cuerda",
            "math": [
                r"T = \dfrac{2m_1m_2g}{m_1+m_2} = \dfrac{2(15.0)(28.0)(9.80)}{43.0}",
                r"T = 191\ \mathrm{N}",
            ],
            "text": ["147 N < T < 274 N: entre los dos pesos."],
            "resaltar": ["T1", "T2"],
        },
    ]
    resultado_latex = r"a = 2.96\ \mathrm{m/s^2}, \qquad T = 191\ \mathrm{N}"


class P5_17(ProblemaScene):
    numero = "5.17"
    titulo = "Bloque en mesa y masa colgante"
    subtitulo = "Segunda ley de Newton · sistema conectado"
    lista_datos = [
        ("Masa sobre la mesa:", r"m_A = 4.00\ \mathrm{kg}"),
        ("Tensión de la cuerda:", r"T = 10.0\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-2.9, 0.0), p(1.9, 0.0), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "bloqueA", p(-1.7, 0.45), ancho=1.1, alto=0.7,
                      color=self.BLUE, etiqueta=r"m_A")
        self.f_polea(fig, "polea", p(1.9, 0.45), radio=0.35, color=self.BLUE)
        self.f_linea(fig, "cuerdaH", p(-1.15, 0.45), p(1.55, 0.45), color=self.WHITE, grosor=4)
        self.f_linea(fig, "cuerdaV", p(1.9, 0.1), p(1.9, -0.45), color=self.WHITE, grosor=4)
        self.f_cuerpo(fig, "bloqueB", p(1.9, -0.8), ancho=0.9, alto=0.6,
                      color=self.GREEN, etiqueta="m")
        self.f_vector(fig, "T_A", p(-1.1, 0.45), RIGHT, 0.9, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "N_A", p(-1.7, 0.8), UP, 0.75, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w_A", p(-1.7, 0.1), DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"m_A g", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "T_B", p(1.9, -0.5), UP, 0.7, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w_B", p(1.9, -1.1), DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"mg", lado=LEFT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Sistema conectado por una cuerda",
            "revelar": ["mesa", "bloqueA", "polea", "cuerdaH", "cuerdaV", "bloqueB"],
            "text": ["La mesa es lisa y la cuerda ideal: misma T en toda su longitud."],
        },
        {
            "titulo": "Bloque sobre la mesa (horizontal)",
            "revelar": ["T_A", "N_A", "w_A"],
            "math": [
                r"a = \dfrac{T}{m_A} = \dfrac{10.0}{4.00} = 2.50\ \mathrm{m/s^2}",
            ],
            "resaltar": ["T_A"],
        },
        {
            "titulo": "Masa colgante (vertical)",
            "revelar": ["T_B", "w_B"],
            "math": [
                r"m(g-a) = T \;\Rightarrow\; m = \dfrac{T}{g-a}",
                r"m = \dfrac{10.0}{9.80-2.50} = 1.37\ \mathrm{kg}",
            ],
            "text": ["Su peso (13.4 N) es mayor que la tensión (10.0 N)."],
            "resaltar": ["w_B", "T_B"],
        },
    ]
    resultado_latex = r"a = 2.50\ \mathrm{m/s^2}, \qquad m = 1.37\ \mathrm{kg}"


class P5_19(ProblemaScene):
    numero = "5.19"
    titulo = "Roca izada con una cadena pesada"
    subtitulo = "Segunda ley de Newton · masa variable con la altura"
    lista_datos = [
        ("Masa de la roca:", r"M = 750.0\ \mathrm{kg}"),
        ("Masa de la cadena:", r"m_c = 575\ \mathrm{kg}"),
        ("Profundidad de la cantera:", r"d = 125\ \mathrm{m}"),
        ("Tensión máx. de la cadena:", r"T_{\max} = 2.50\,m_cg"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "borde", p(-2.4, 2.1), p(2.4, 2.1), color=self.MUTED, grosor=4)
        self.f_linea(fig, "paredI", p(-1.7, 2.1), p(-1.7, -2.3), color=self.MUTED, grosor=3)
        self.f_linea(fig, "paredD", p(1.7, 2.1), p(1.7, -2.3), color=self.MUTED, grosor=3)
        self.f_linea(fig, "cadena", p(0.0, 2.1), p(0.0, -1.45), color=self.WHITE, grosor=4)
        self.f_cuerpo(fig, "roca", p(0.0, -1.8), ancho=1.4, alto=0.7,
                      color=self.BLUE, etiqueta="roca")
        self.f_vector(fig, "T", p(0.0, 2.1), UP, 1.0, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w_roca", p(0.0, -2.15), DOWN, 0.8, color=self.ORANGE,
                      etiqueta=r"Mg", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w_cad", p(0.0, 0.6), DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"m_c g", lado=LEFT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "La cadena sostiene la roca y su propio peso",
            "revelar": ["borde", "paredI", "paredD", "cadena", "roca", "T",
                        "w_roca", "w_cad"],
            "text": ["La tensión máxima está en el extremo superior de la cadena."],
        },
        {
            "titulo": "Tensión máxima admisible",
            "math": [
                r"T_{\max} = 2.50\,m_cg = 2.50(575)(9.80)",
                r"T_{\max} = 1.41\times10^4\ \mathrm{N}",
            ],
            "resaltar": ["T"],
        },
        {
            "titulo": "Newton para roca + cadena (masa total)",
            "math": [
                r"T_{\max} - (M+m_c)g = (M+m_c)a",
                r"a = \dfrac{T_{\max}}{M+m_c} - g = 0.832\ \mathrm{m/s^2}",
            ],
            "resaltar": ["w_roca", "w_cad"],
        },
        {
            "titulo": "Tiempo para subir los 125 m",
            "math": [
                r"d = \tfrac12 a t^2 \;\Rightarrow\; t = \sqrt{\dfrac{2d}{a}}",
                r"t = \sqrt{\dfrac{2(125)}{0.832}} = 17.3\ \mathrm{s}",
            ],
        },
    ]
    resultado_latex = r"a = 0.832\ \mathrm{m/s^2}, \qquad t = 17.3\ \mathrm{s}"


class P5_21(ProblemaScene):
    numero = "5.21"
    titulo = "Fuerza del suelo en un salto"
    subtitulo = "Segunda ley de Newton · fuerza impulsora"
    lista_datos = [
        ("Altura del salto:", r"h = 0.60\ \mathrm{m}"),
        ("Distancia de empuje:", r"d = 0.50\ \mathrm{m}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-2.6, -1.8), p(2.6, -1.8), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "persona", p(0.0, -1.3), forma="punto", color=self.BLUE)
        self.f_linea(fig, "h_marca", p(1.0, -1.8), p(1.0, 0.45), color=self.YELLOW,
                     grosor=2, discontinuo=True, etiqueta=r"h=0.60", lado=RIGHT,
                     etiqueta_size=20)
        self.f_linea(fig, "d_marca", p(-1.0, -1.8), p(-1.0, -1.3), color=self.GREEN,
                     grosor=3, etiqueta=r"d=0.50", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "N", p(0.0, -1.3), UP, 1.15, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", p(0.0, -1.3), DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"w", lado=LEFT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Dos fases: empuje y vuelo",
            "revelar": ["suelo", "persona", "h_marca", "d_marca"],
            "text": ["Durante el empuje el suelo acelera a la persona hacia arriba."],
        },
        {
            "titulo": "Rapidez de despegue (fase de vuelo)",
            "math": [
                r"v^2 = 2gh \;\Rightarrow\; v = \sqrt{2(9.80)(0.60)}",
                r"v = 3.43\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "Aceleración durante el empuje",
            "math": [
                r"v^2 = 2ad \;\Rightarrow\; a = \dfrac{v^2}{2d} = 11.8\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Fuerza del suelo (diagrama de cuerpo libre)",
            "revelar": ["N", "w"],
            "math": [
                r"N - w = ma \;\Rightarrow\; N = w\left(1+\dfrac{a}{g}\right)",
                r"N = 2.2\,w",
            ],
            "resaltar": ["N", "w"],
        },
    ]
    resultado_latex = r"v = 3.43\ \mathrm{m/s}, \qquad N = 2.2\,w"


class P5_27(ProblemaScene):
    numero = "5.27"
    titulo = "Bodeguero empujando una caja"
    subtitulo = "Segunda ley de Newton · fricción cinética"
    lista_datos = [
        ("Masa de la caja:", r"m = 11.2\ \mathrm{kg}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.20"),
        ("Rapidez constante:", r"v = 3.50\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-3.4, 0.0), p(3.4, 0.0), color=self.MUTED, grosor=4)
        centro = p(0.0, 0.48)
        self.f_cuerpo(fig, "caja", centro, ancho=1.35, alto=0.78,
                      color=self.BLUE, etiqueta="caja")
        self.f_vector(fig, "F", centro, RIGHT, 1.25, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "fk", centro, LEFT, 1.15, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "N", centro, UP, 1.0, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", centro, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La caja se mueve a rapidez constante",
            "revelar": ["suelo", "caja"],
            "text": ["Sin aceleración: la fuerza del bodeguero iguala a la fricción."],
        },
        {
            "titulo": "Diagrama de cuerpo libre y fuerza aplicada",
            "revelar": ["F", "fk", "N", "w"],
            "math": [r"F = f_k = \mu_k mg = 0.20(11.2)(9.80) = 22.0\ \mathrm{N}"],
            "resaltar": ["F", "fk"],
        },
        {
            "titulo": "Se suelta la caja: distancia de frenado",
            "math": [
                r"a = \mu_k g = 1.96\ \mathrm{m/s^2}",
                r"d = \dfrac{v^2}{2a} = \dfrac{(3.50)^2}{2(1.96)} = 3.13\ \mathrm{m}",
            ],
        },
    ]
    resultado_latex = r"F = 22.0\ \mathrm{N}, \qquad d = 3.13\ \mathrm{m}"


class P5_31(ProblemaScene):
    numero = "5.31"
    titulo = "Dos cajas subidas juntas por una rampa"
    subtitulo = "Segunda ley de Newton · sistema con fricción"
    lista_datos = [
        ("Masa inferior:", r"m_1 = 48.0\ \mathrm{kg}"),
        ("Masa superior:", r"m_2 = 32.0\ \mathrm{kg}"),
        ("Altura / base de la rampa:", r"2.50\ \mathrm{m} / 4.75\ \mathrm{m}"),
        ("Fricción rampa-caja:", r"\mu_k = 0.444"),
    ]

    def crear_figura(self):
        fig = Figura()
        geo = self.f_plano_inclinado(fig, "rampa", base=(-3.2, -1.6, 0),
                                     angulo_grados=27.8, largo=4.2)
        A, u, th = geo["A"], geo["u"], geo["theta"]
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.7,
                      etiqueta=r"\theta", etiqueta_size=22)
        bajo = A + 1.75 * u + 0.42 * n
        alto = bajo + 0.86 * n
        g1 = self.f_cuerpo(fig, "caja1", bajo, ancho=1.25, alto=0.72,
                           color=self.BLUE, etiqueta=r"48")
        g1[0].rotate(th, about_point=bajo)
        g2 = self.f_cuerpo(fig, "caja2", alto, ancho=1.15, alto=0.7,
                           color=self.GREEN, etiqueta=r"32")
        g2[0].rotate(th, about_point=alto)
        self.f_vector(fig, "w", bajo, DOWN, 1.7, color=self.ORANGE,
                      etiqueta=r"(m_1+m_2)g", lado=DOWN, etiqueta_size=22)
        self.f_descomponer(fig, "w", bajo, DOWN, 1.7, eje1=u, eje2=n,
                           etiqueta_x=r"(m_1+m_2)g\sin\theta",
                           etiqueta_y=r"(m_1+m_2)g\cos\theta",
                           desplaz_x=(-1.05, -0.62), desplaz_y=(0.95, -0.05))
        self.f_vector(fig, "F", bajo + 0.72 * u, u, 1.2, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "fk1", bajo - 0.72 * u, -u, 0.8, color=self.YELLOW,
                      etiqueta=r"f_k", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "fk2", alto - 0.62 * u, -u, 0.65, color=self.YELLOW,
                      etiqueta=r"f", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Geometría de la rampa",
            "revelar": ["rampa", "caja1", "caja2", "theta"],
            "math": [r"\theta = \arctan\dfrac{2.50}{4.75} = 27.8^\circ"],
        },
        {
            "titulo": "Peso total y su descomposición",
            "revelar": ["w", "w_guia", "w_x", "w_y"],
            "text": ["El sistema de 80.0 kg se empuja rampa arriba a rapidez constante."],
            "resaltar": ["w_x"],
        },
        {
            "titulo": "Fuerza aplicada (empuje + fricción)",
            "revelar": ["F", "fk1", "fk2"],
            "math": [
                r"F = (m_1+m_2)g(\sin\theta + \mu_k\cos\theta)",
                r"F = 784(0.466 + 0.393) = 673\ \mathrm{N}",
            ],
            "resaltar": ["F", "fk1"],
        },
        {
            "titulo": "Fricción que sostiene a la caja superior",
            "math": [
                r"f = m_2g\sin\theta = (32.0)(9.80)(0.466)",
                r"f = 146\ \mathrm{N}",
            ],
            "text": ["Hacia arriba de la rampa."],
            "resaltar": ["fk2"],
        },
    ]
    resultado_latex = r"F = 673\ \mathrm{N}, \qquad f = 146\ \mathrm{N}"


class P5_33(ProblemaScene):
    numero = "5.33"
    titulo = "Distancia de frenado"
    subtitulo = "Segunda ley de Newton · fricción cinética"
    lista_datos = [
        ("Rapidez inicial:", r"v = 28.7\ \mathrm{m/s}"),
        ("Pavimento seco:", r"\mu_k = 0.80"),
        ("Pavimento húmedo:", r"\mu_k = 0.25"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "pista", p(-3.6, 0.0), p(3.6, 0.0), color=self.MUTED, grosor=4)
        centro = p(-0.6, 0.45)
        self.f_cuerpo(fig, "auto", centro, ancho=1.7, alto=0.72,
                      color=self.BLUE, etiqueta="auto")
        self.f_vector(fig, "v", centro, RIGHT, 1.35, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "fk", centro, LEFT, 1.3, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=26)
        self.f_vector(fig, "N", centro, UP, 0.9, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w", centro, DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        self.f_linea(fig, "d_marca", p(0.6, -0.1), p(3.3, -0.1),
                     color=self.GREEN, grosor=2, discontinuo=True,
                     etiqueta=r"d", lado=DOWN, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La fricción es la única fuerza horizontal",
            "revelar": ["pista", "auto", "v", "fk", "N", "w"],
            "math": [r"f_k = \mu_k mg = ma \;\Rightarrow\; a = \mu_k g"],
            "resaltar": ["fk"],
        },
        {
            "titulo": "Distancia de frenado en pavimento seco",
            "revelar": ["d_marca"],
            "math": [
                r"d = \dfrac{v^2}{2\mu_k g} = \dfrac{(28.7)^2}{2(0.80)(9.80)}",
                r"d = 52.5\ \mathrm{m}",
            ],
            "resaltar": ["d_marca"],
        },
        {
            "titulo": "Rapidez segura en pavimento húmedo",
            "math": [
                r"v = \sqrt{2\mu_k g d} = \sqrt{2(0.25)(9.80)(52.5)}",
                r"v = 16.0\ \mathrm{m/s}",
            ],
            "text": ["Recorrer los mismos 52.5 m exige ir mucho más despacio."],
        },
    ]
    resultado_latex = r"d = 52.5\ \mathrm{m}, \qquad v_{\mathrm{mojado}} = 16.0\ \mathrm{m/s}"


class P5_34(ProblemaScene):
    numero = "5.34"
    titulo = "Bloques A y B con polea y fricción"
    subtitulo = "Primera ley de Newton · fricción cinética"
    lista_datos = [
        ("Peso del bloque A:", r"w_A = 45.0\ \mathrm{N}"),
        ("Peso del bloque B:", r"w_B = 25.0\ \mathrm{N}"),
        ("Peso del gato:", r"w_{\mathrm{gato}} = 45.0\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.0, 0.0), p(1.9, 0.0), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "bloqueA", p(-1.7, 0.42), ancho=1.2, alto=0.72,
                      color=self.BLUE, etiqueta="A")
        self.f_cuerpo(fig, "gato", p(-1.7, 1.0), ancho=0.9, alto=0.45,
                      color=self.GREEN, etiqueta="gato")
        self.f_polea(fig, "polea", p(1.9, 0.42), radio=0.32, color=self.BLUE)
        self.f_linea(fig, "cuerdaH", p(-1.1, 0.42), p(1.58, 0.42), color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaV", p(1.9, 0.1), p(1.9, -0.5), color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "bloqueB", p(1.9, -0.82), ancho=0.9, alto=0.6,
                      color=self.GREEN, etiqueta="B")
        self.f_vector(fig, "T_A", p(-1.1, 0.42), RIGHT, 0.9, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "N_A", p(-1.7, 0.78), UP, 0.7, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w_A", p(-1.7, 0.06), DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"w_A", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "T_B", p(1.9, -0.52), UP, 0.65, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w_B", p(1.9, -1.12), DOWN, 0.8, color=self.ORANGE,
                      etiqueta=r"w_B", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "fk", p(-1.7, 0.42), LEFT, 0.95, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "A sobre la mesa y B colgando",
            "revelar": ["mesa", "bloqueA", "polea", "cuerdaH", "cuerdaV", "bloqueB"],
            "text": ["A se mueve a velocidad constante: su aceleración es cero."],
        },
        {
            "titulo": "La cuerda solo transmite el peso de B",
            "revelar": ["T_A", "T_B", "w_B"],
            "math": [r"T = w_B = 25.0\ \mathrm{N}"],
            "resaltar": ["T_A", "T_B"],
        },
        {
            "titulo": "Coeficiente de fricción cinética",
            "revelar": ["N_A", "w_A", "fk"],
            "math": [
                r"T = f_k = \mu_k w_A",
                r"\mu_k = \dfrac{25.0}{45.0} = 0.556",
            ],
            "resaltar": ["fk"],
        },
        {
            "titulo": "El gato se duerme sobre A",
            "revelar": ["gato"],
            "math": [
                r"N = 90.0\ \mathrm{N}, \quad f_k = 0.556(90.0) = 50.0\ \mathrm{N}",
                r"a = \dfrac{25.0 - 50.0}{(90.0+25.0)/9.80} = -2.13\ \mathrm{m/s^2}",
            ],
            "text": ["La fricción supera al peso de B: B frena, su aceleración apunta hacia arriba."],
            "resaltar": ["gato", "fk"],
        },
    ]
    resultado_latex = r"\mu_k = 0.556, \qquad a = 2.13\ \mathrm{m/s^2}\ (\text{B hacia arriba})"


class P5_42(ProblemaScene):
    numero = "5.42"
    titulo = "Carrito en pista circular vertical"
    subtitulo = "Segunda ley de Newton · dinámica circular"
    lista_datos = [
        ("Masa del carrito:", r"m = 0.800\ \mathrm{kg}"),
        ("Radio de la pista:", r"R = 5.00\ \mathrm{m}"),
        ("Normal en el punto alto:", r"N_B = 6.00\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        centro = p(0.0, 0.0)
        radio = 2.2
        aro = Circle(radius=radio, color=self.BLUE, stroke_width=7).move_to(centro)
        fig.registrar("aro", aro, lambda m: Create(m))
        A = centro + DOWN * radio
        B = centro + UP * radio
        self.f_cuerpo(fig, "cartA", A, ancho=0.8, alto=0.55,
                      color=self.BLUE, etiqueta="A")
        self.f_cuerpo(fig, "cartB", B, ancho=0.8, alto=0.55,
                      color=self.GREEN, etiqueta="B")
        self.f_vector(fig, "N_A", A + LEFT * 0.22, UP, 1.05, color=self.CYAN,
                      etiqueta=r"N_A", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w_A", A + RIGHT * 0.22, DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "N_B", B + LEFT * 0.22, DOWN, 0.75, color=self.CYAN,
                      etiqueta=r"N_B", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w_B", B + RIGHT * 0.22, DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "El carrito recorre la pista circular",
            "revelar": ["aro", "cartA", "cartB"],
            "text": ["En cada punto, la fuerza neta hacia el centro produce el giro."],
        },
        {
            "titulo": "Punto más alto (B)",
            "revelar": ["N_B", "w_B"],
            "math": [r"N_B + mg = \dfrac{mv^2}{R}"],
            "text": ["Aquí la pista empuja al carrito hacia abajo."],
            "resaltar": ["N_B"],
        },
        {
            "titulo": "Punto más bajo (A)",
            "revelar": ["N_A", "w_A"],
            "math": [r"N_A - mg = \dfrac{mv^2}{R}"],
            "resaltar": ["N_A"],
        },
        {
            "titulo": "Restando ambas ecuaciones",
            "math": [
                r"N_A - N_B = 2mg = 2(0.800)(9.80) = 15.7\ \mathrm{N}",
                r"N_A = 6.00 + 15.7 = 21.7\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"N_A = 21.7\ \mathrm{N}"


class P5_44(ProblemaScene):
    numero = "5.44"
    titulo = "Curva plana sin peralte"
    subtitulo = "Segunda ley de Newton · fricción como centrípeta"
    lista_datos = [
        ("Radio de la curva:", r"R = 220.0\ \mathrm{m}"),
        ("Rapidez del automóvil:", r"v = 25.0\ \mathrm{m/s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        C = p(0.0, 0.9)
        for r, nombre in [(2.35, "bordeI"), (2.9, "bordeD")]:
            arco = Arc(radius=r, start_angle=195 * DEGREES, angle=150 * DEGREES,
                       color=self.MUTED, stroke_width=3).move_to(C)
            fig.registrar(nombre, arco, lambda m: Create(m))
        M = C + p(0.0, -2.75)
        self.f_cuerpo(fig, "auto", M, ancho=1.1, alto=0.7,
                      color=self.BLUE, etiqueta="auto")
        self.f_vector(fig, "fs", M, UP, 1.2, color=self.YELLOW,
                      etiqueta=r"f_s", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "v", M, RIGHT, 1.35, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=26)
        return fig

    pasos = [
        {
            "titulo": "Vista superior de la curva plana",
            "revelar": ["bordeI", "bordeD", "auto"],
            "text": ["La fricción estática apunta al centro y produce el giro."],
        },
        {
            "titulo": "La fricción es la fuerza centrípeta",
            "revelar": ["fs", "v"],
            "math": [
                r"f_s = \dfrac{mv^2}{R} = \mu_s N = \mu_s mg",
                r"\mu_s = \dfrac{v^2}{gR} = \dfrac{(25.0)^2}{(9.80)(220.0)} = 0.290",
            ],
            "resaltar": ["fs"],
        },
        {
            "titulo": "Rapidez máxima sobre hielo",
            "math": [
                r"\mu = \dfrac{0.290}{3} = 0.0967",
                r"v = \sqrt{\mu g R} = \sqrt{(0.0967)(9.80)(220.0)} = 14.4\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"\mu_s = 0.290, \qquad v_{\mathrm{hielo}} = 14.4\ \mathrm{m/s}"


class P5_45(ProblemaScene):
    numero = "5.45"
    titulo = "Curva peraltada para auto y camión"
    subtitulo = "Segunda ley de Newton · peralte sin fricción"
    lista_datos = [
        ("Masa del automóvil:", r"1125\ \mathrm{kg}"),
        ("Masa del camión:", r"2250\ \mathrm{kg}"),
        ("Radio de la curva:", r"R = 225\ \mathrm{m}"),
        ("Rapidez de diseño:", r"v = 65.0\ \mathrm{mi/h}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(21.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-1.7, -0.65)
        B = A + 3.4 * u
        self.f_linea(fig, "calzada", A, B, color=self.WHITE, grosor=6)
        self.f_linea(fig, "base", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.55,
                      etiqueta=r"\theta", etiqueta_size=22)
        centro = A + 1.5 * u + 0.48 * n
        g = self.f_cuerpo(fig, "auto", centro, ancho=1.25, alto=0.72,
                          color=self.BLUE, etiqueta="auto")
        g[0].rotate(th, about_point=centro)
        self.f_vector(fig, "N", centro, n, 1.5, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", centro, DOWN, 1.15, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=22)
        self.f_descomponer(fig, "N", centro, n, 1.5, eje1=RIGHT, eje2=UP,
                           etiqueta_x=r"N\sin\theta", etiqueta_y=r"N\cos\theta",
                           desplaz_x=(-0.75, -0.3), desplaz_y=(0.6, 0.25))
        return fig

    pasos = [
        {
            "titulo": "Rapidez de diseño en el SI",
            "revelar": ["calzada", "base", "auto", "theta"],
            "math": [r"v = 65.0\ \mathrm{mi/h} = 29.1\ \mathrm{m/s}"],
        },
        {
            "titulo": "La normal tiene componente centrípeta",
            "revelar": ["N", "w"],
            "math": [r"N\sin\theta = \dfrac{mv^2}{R}, \qquad N\cos\theta = mg"],
            "resaltar": ["N"],
        },
        {
            "titulo": "Ángulo de peralte",
            "revelar": ["N_x", "N_y", "N_guia"],
            "math": [
                r"\tan\theta = \dfrac{v^2}{gR} = \dfrac{(29.1)^2}{(9.80)(225)} = 0.383",
                r"\theta = 21.0^\circ",
            ],
            "text": ["No depende de la masa: el camión no necesita ir más lento."],
            "resaltar": ["N_x"],
        },
        {
            "titulo": "Fuerza normal sobre cada vehículo",
            "math": [
                r"N = \dfrac{mg}{\cos\theta}",
                r"N_{\mathrm{auto}} = 1.18\times10^4\ \mathrm{N}",
                r"N_{\mathrm{camion}} = 2.36\times10^4\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"\theta = 21.0^\circ, \quad N_{\mathrm{auto}} = 1.18\times10^4\ \mathrm{N}"
    resultado_nota = "N del camión = 2.36×10⁴ N (el doble, por su masa)."


class P5_46(ProblemaScene):
    numero = "5.46"
    titulo = "El columpio gigante de la feria"
    subtitulo = "Segunda ley de Newton · péndulo cónico"
    lista_datos = [
        ("Longitud del cable:", r"5.00\ \mathrm{m}"),
        ("Distancia del brazo al eje:", r"3.00\ \mathrm{m}"),
        ("Ángulo con la vertical:", r"30.0^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        eje = p(-2.4, -2.2)
        tope = p(-2.4, 2.0)
        self.f_linea(fig, "eje", eje, tope, color=self.MUTED, grosor=4)
        E = p(-0.9, 1.9)
        self.f_linea(fig, "brazo", p(-2.4, 1.9), E, color=self.MUTED, grosor=4)
        cable_dir = np.array([np.sin(np.deg2rad(30.0)), -np.cos(np.deg2rad(30.0)), 0.0])
        C = E + 2.5 * cable_dir
        self.f_linea(fig, "cable", E, C, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "silla", C, ancho=0.9, alto=0.65,
                      color=self.BLUE, etiqueta="silla")
        giro = CurvedArrow(p(-3.0, 1.1), p(-1.8, 1.1), angle=PI / 2,
                           color=self.YELLOW, tip_length=0.16)
        fig.registrar("giro", giro, lambda m: Create(m))
        self.f_texto(fig, "omega", r"\omega", (-2.4, 0.55, 0), size=30, color=self.YELLOW, math=True)
        self.f_linea(fig, "radio", p(-2.4, C[1]), C, color=self.GREEN,
                     grosor=2, discontinuo=True, etiqueta=r"R", lado=DOWN,
                     etiqueta_size=22)
        self.f_angulo(fig, "ang30", E, E + DOWN, C, radio=0.5,
                      etiqueta=r"30^\circ", etiqueta_size=20)
        self.f_vector(fig, "T", C, E - C, 1.15, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", C, DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"mg", lado=LEFT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Geometría del columpio giratorio",
            "revelar": ["eje", "brazo", "cable", "silla", "giro", "omega", "radio", "ang30"],
            "math": [r"R = 3.00 + 5.00\sin 30^\circ = 5.50\ \mathrm{m}"],
        },
        {
            "titulo": "La tensión sostiene y a la vez gira",
            "revelar": ["T", "w"],
            "math": [
                r"T\cos 30^\circ = mg \quad \text{(vertical)}",
                r"T\sin 30^\circ = m\omega^2 R \quad \text{(radial)}",
            ],
            "text": ["La componente horizontal de T es la fuerza centrípeta."],
            "resaltar": ["T", "w"],
        },
        {
            "titulo": "Periodo de una revolución",
            "math": [
                r"\tan 30^\circ = \dfrac{\omega^2 R}{g} \;\Rightarrow\; \omega = 1.01\ \mathrm{rad/s}",
                r"T_{\mathrm{per}} = \dfrac{2\pi}{\omega} = 6.19\ \mathrm{s}",
            ],
            "text": ["La masa no aparece: el ángulo no depende del peso del pasajero."],
        },
    ]
    resultado_latex = r"T_{\mathrm{per}} = 6.19\ \mathrm{s}"


class P5_47(ProblemaScene):
    numero = "5.47"
    titulo = "Columpio gigante con dos cables"
    subtitulo = "Segunda ley de Newton · cable inclinado y horizontal"
    lista_datos = [
        ("Peso del asiento:", r"255\ \mathrm{N}"),
        ("Peso de la persona:", r"825\ \mathrm{N}"),
        ("Rapidez angular:", r"32.0\ \mathrm{rpm}"),
        ("Distancia al eje:", r"R = 7.50\ \mathrm{m}"),
        ("Ángulo del cable:", r"40.0^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        eje_x = -2.6
        S = p(0.05, -0.2)
        self.f_linea(fig, "eje", p(eje_x, -2.2), p(eje_x, 2.1), color=self.MUTED, grosor=4)
        tope = p(eje_x, 2.0)
        self.f_linea(fig, "cableI", S, tope, color=self.WHITE, grosor=5)
        self.f_linea(fig, "cableH", p(eje_x, S[1]), S, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "asiento", S, ancho=1.1, alto=0.65,
                      color=self.BLUE, etiqueta="asiento")
        self.f_angulo(fig, "ang40", S, S + LEFT, tope, radio=0.6,
                      etiqueta=r"40^\circ", etiqueta_size=22)
        self.f_vector(fig, "Ti", S, tope - S, 1.25, color=self.CYAN,
                      etiqueta=r"T_i", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "Th", S, LEFT, 1.1, color=self.GREEN,
                      etiqueta=r"T_h", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "w", S, DOWN, 1.35, color=self.ORANGE,
                      etiqueta=r"W", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Asiento sostenido por dos cables",
            "revelar": ["eje", "cableI", "cableH", "asiento", "ang40"],
            "math": [r"W = 255 + 825 = 1080\ \mathrm{N}"],
        },
        {
            "titulo": "Aceleración centrípeta",
            "math": [
                r"\omega = 32.0\ \mathrm{rpm} = 3.35\ \mathrm{rad/s}",
                r"a_c = \omega^2 R = 84.2\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Equilibrio vertical: cable inclinado",
            "revelar": ["Ti", "w"],
            "math": [r"T_i\sin 40^\circ = W \;\Rightarrow\; T_i = 1.68\ \mathrm{kN}"],
            "resaltar": ["Ti", "w"],
        },
        {
            "titulo": "Dinámica radial: cable horizontal",
            "revelar": ["Th"],
            "math": [
                r"T_h + T_i\cos 40^\circ = m a_c",
                r"T_h = 9280 - 1287 = 7.99\ \mathrm{kN}",
            ],
            "resaltar": ["Th"],
        },
    ]
    resultado_latex = r"T_i = 1.68\ \mathrm{kN}, \qquad T_h = 7.99\ \mathrm{kN}"


class P5_51(ProblemaScene):
    numero = "5.51"
    titulo = "Avión que describe un rizo vertical"
    subtitulo = "Segunda ley de Newton · ingravidez y peso aparente"
    lista_datos = [
        ("Radio del rizo:", r"R = 150\ \mathrm{m}"),
        ("Rapidez en el punto bajo:", r"280\ \mathrm{km/h}"),
        ("Peso real del piloto:", r"700\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        centro = p(0.0, 0.0)
        radio = 2.2
        aro = Circle(radius=radio, color=self.BLUE, stroke_width=7).move_to(centro)
        fig.registrar("aro", aro, lambda m: Create(m))
        A = centro + DOWN * radio
        B = centro + UP * radio
        self.f_cuerpo(fig, "avionA", A, ancho=0.95, alto=0.6,
                      color=self.BLUE, etiqueta="bajo")
        self.f_cuerpo(fig, "avionB", B, ancho=0.95, alto=0.6,
                      color=self.GREEN, etiqueta="alto")
        self.f_vector(fig, "N_A", A + LEFT * 0.25, UP, 1.2, color=self.CYAN,
                      etiqueta=r"N", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "w_A", A + RIGHT * 0.25, DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "w_B", B, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "v_B", B + UP * 0.35, LEFT, 0.9, color=self.CYAN,
                      etiqueta=r"v", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El avión recorre el rizo circular",
            "revelar": ["aro", "avionA", "avionB"],
            "text": ["Arriba el piloto puede quedar ingrávido; abajo pesa más."],
        },
        {
            "titulo": "Punto alto: ingravidez (N = 0)",
            "revelar": ["w_B", "v_B"],
            "math": [
                r"mg = \dfrac{mv^2}{R} \;\Rightarrow\; v = \sqrt{gR}",
                r"v = \sqrt{(9.80)(150)} = 38.3\ \mathrm{m/s}",
            ],
            "resaltar": ["w_B"],
        },
        {
            "titulo": "Punto bajo: peso aparente",
            "revelar": ["N_A", "w_A"],
            "math": [
                r"v = 280\ \mathrm{km/h} = 77.8\ \mathrm{m/s}",
                r"N = m\left(g+\dfrac{v^2}{R}\right) = 71.4(9.80+40.3)",
                r"N = 3.58\times10^3\ \mathrm{N} = 5.11\,w",
            ],
            "resaltar": ["N_A"],
        },
    ]
    resultado_latex = r"v_{\mathrm{alto}} = 38.3\ \mathrm{m/s}, \qquad N = 3.58\times10^3\ \mathrm{N}"


class P5_56(ProblemaScene):
    numero = "5.56"
    titulo = "Explorador colgado de una cuerda entre riscos"
    subtitulo = "Primera ley de Newton · cuerda casi horizontal"
    lista_datos = [
        ("Masa del explorador:", r"m = 90.0\ \mathrm{kg}"),
        ("Tensión de rotura:", r"T_{\max} = 2.50\times10^4\ \mathrm{N}"),
        ("Ángulo inicial:", r"\theta = 10.0^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        izq = p(-3.2, 1.6)
        der = p(3.2, 1.6)
        E = p(0.0, 1.6 - 3.2 * np.tan(np.deg2rad(10.0)))
        self.f_linea(fig, "riscoI", p(-3.2, -2.2), p(-3.2, 1.8), color=self.MUTED, grosor=5)
        self.f_linea(fig, "riscoD", p(3.2, -2.2), p(3.2, 1.8), color=self.MUTED, grosor=5)
        self.f_linea(fig, "cuerdaI", izq, E, color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaD", E, der, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "explorador", E, forma="punto", color=self.BLUE)
        self.f_texto(fig, "et_m", r"m", (E + DOWN * 0.42), size=26, color=self.WHITE, math=True)
        self.f_angulo(fig, "angI", E, E + LEFT, izq, radio=0.5,
                      etiqueta=r"10^\circ", etiqueta_size=19)
        self.f_angulo(fig, "angD", E, E + RIGHT, der, radio=0.5,
                      etiqueta=r"10^\circ", etiqueta_size=19)
        self.f_vector(fig, "T1", E, izq - E, 1.0, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "T2", E, der - E, 1.0, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "w", E, DOWN, 1.2, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La cuerda cuelga casi horizontal",
            "revelar": ["riscoI", "riscoD", "cuerdaI", "cuerdaD", "explorador",
                        "et_m", "angI", "angD"],
            "text": ["El explorador está en reposo en el punto medio de la cuerda."],
        },
        {
            "titulo": "Equilibrio vertical en el punto medio",
            "revelar": ["T1", "T2", "w"],
            "math": [r"2T\sin\theta = mg"],
            "text": ["Solo las componentes verticales de la tensión sostienen el peso."],
            "resaltar": ["T1", "T2", "w"],
        },
        {
            "titulo": "Tensión con θ = 10.0°",
            "math": [
                r"T = \dfrac{mg}{2\sin 10^\circ} = \dfrac{(90.0)(9.80)}{2(0.1736)}",
                r"T = 2.54\times10^3\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Ángulo mínimo sin romper la cuerda",
            "math": [
                r"\sin\theta_{\min} = \dfrac{mg}{2T_{\max}} = \dfrac{882}{5.00\times10^4}",
                r"\theta_{\min} = 1.01^\circ",
            ],
            "text": ["Cuanto más horizontal, mayor la tensión: la cuerda casi no puede quedar recta."],
        },
    ]
    resultado_latex = r"N = 1.22\,mg, \qquad T = 0.700\,mg"


class P5_65(ProblemaScene):
    numero = "5.65"
    titulo = "Dos cajas con fuerza inclinada y fricción"
    subtitulo = "Segunda ley de Newton · fuerza con componente vertical"
    lista_datos = [
        ("Fuerza aplicada:", r"F = 40.0\ \mathrm{N}"),
        ("Ángulo sobre la horizontal:", r"53.1^\circ"),
        ("Masa de la caja B:", r"m_B = 5.00\ \mathrm{kg}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.30"),
        ("Aceleración:", r"a = 1.50\ \mathrm{m/s^2}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "suelo", p(-3.6, 0.0), p(3.4, 0.0), color=self.MUTED, grosor=4)
        cA = p(-1.9, 0.42)
        cB = p(0.6, 0.42)
        self.f_cuerpo(fig, "cajaA", cA, ancho=1.1, alto=0.72,
                      color=self.BLUE)
        self.f_cuerpo(fig, "cajaB", cB, ancho=1.1, alto=0.72,
                      color=self.GREEN)
        self.f_texto(fig, "etA", "A", cA + UP * 0.62, size=24, color=self.WHITE)
        self.f_texto(fig, "etB", "B", cB + UP * 0.62, size=24, color=self.WHITE)
        self.f_linea(fig, "cuerda", p(-1.35, 0.42), p(0.05, 0.42), color=self.WHITE, grosor=5)
        fdir = np.array([np.cos(np.deg2rad(53.1)), np.sin(np.deg2rad(53.1)), 0.0])
        self.f_vector(fig, "F", cB, fdir, 1.35, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_angulo(fig, "angF", cB, cB + RIGHT, cB + fdir, radio=0.55,
                      etiqueta=r"53.1^\circ", etiqueta_size=20)
        self.f_vector(fig, "T_B", p(0.05, 0.42), LEFT, 0.7, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "T_A", p(-1.35, 0.42), RIGHT, 0.7, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "N_B", cB, UP, 0.8, color=self.CYAN,
                      etiqueta=r"N_B", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w_B", cB, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"m_B g", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "fk_B", cB + DOWN * 0.3, LEFT, 0.85, color=self.YELLOW,
                      etiqueta=r"f_B", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "N_A", cA, UP, 0.85, color=self.CYAN,
                      etiqueta=r"N_A", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "w_A", cA, DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"m_A g", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "fk_A", cA + DOWN * 0.3, LEFT, 0.8, color=self.YELLOW,
                      etiqueta=r"f_A", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "B tira de A con una cuerda",
            "revelar": ["suelo", "cajaA", "cajaB", "etA", "etB", "cuerda", "F", "angF"],
            "text": ["La fuerza F tiene componente hacia arriba: alivia la normal de B."],
        },
        {
            "titulo": "Fuerza normal y fricción sobre B",
            "revelar": ["N_B", "w_B", "fk_B"],
            "math": [
                r"N_B = m_B g - F\sin 53.1^\circ = 17.0\ \mathrm{N}",
                r"f_B = \mu_k N_B = 5.10\ \mathrm{N}",
            ],
            "resaltar": ["N_B", "fk_B"],
        },
        {
            "titulo": "Tensión en la cuerda (sobre B)",
            "revelar": ["T_B", "T_A"],
            "math": [
                r"F\cos 53.1^\circ - T - f_B = m_B a",
                r"T = 24.0 - 5.10 - 7.50 = 11.4\ \mathrm{N}",
            ],
            "resaltar": ["T_B"],
        },
        {
            "titulo": "Masa de la caja A",
            "revelar": ["N_A", "w_A", "fk_A"],
            "math": [
                r"T = m(a + \mu_k g) \;\Rightarrow\; m = \dfrac{T}{a+\mu_k g}",
                r"m = \dfrac{11.4}{1.50 + 2.94} = 2.57\ \mathrm{kg}",
            ],
            "resaltar": ["T_A"],
        },
    ]
    resultado_latex = r"T = 11.4\ \mathrm{N}, \qquad m = 2.57\ \mathrm{kg}"


class P5_66(ProblemaScene):
    numero = "5.66"
    titulo = "Fuerza horizontal para subir una rampa"
    subtitulo = "Segunda ley de Newton · empuje horizontal"
    lista_datos = [
        ("Masa de la caja:", r"m = 6.00\ \mathrm{kg}"),
        ("Inclinación:", r"37.0^\circ"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.30"),
        ("Aceleración deseada:", r"a = 4.20\ \mathrm{m/s^2}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(37.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.1, -1.6)
        geo = self.f_plano_inclinado(fig, "rampa", base=tuple(A),
                                     angulo_grados=37.0, largo=4.4)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"37^\circ", etiqueta_size=22)
        centro = A + 2.2 * u + 0.42 * n
        g = self.f_cuerpo(fig, "caja", centro, ancho=1.2, alto=0.72,
                          color=self.BLUE)
        g[0].rotate(th, about_point=centro)
        self.f_vector(fig, "F", centro, RIGHT, 1.25, color=self.RED,
                      etiqueta=r"F", lado=RIGHT, etiqueta_size=26)
        self.f_vector(fig, "w", centro, DOWN, 1.25, color=self.ORANGE,
                      etiqueta=r"mg", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "N", centro, n, 1.2, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_descomponer(fig, "F", centro, RIGHT, 1.25, eje1=u, eje2=n,
                           etiqueta_x=r"F\cos 37^\circ", etiqueta_y=r"F\sin 37^\circ",
                           desplaz_x=(1.05, 0.12), desplaz_y=(-0.85, 0.3))
        self.f_descomponer(fig, "w", centro, DOWN, 1.25, eje1=u, eje2=n,
                           etiqueta_x=r"mg\sin 37^\circ", etiqueta_y=r"mg\cos 37^\circ",
                           desplaz_x=(-0.9, -0.3), desplaz_y=(0.8, -0.25))
        self.f_vector(fig, "fk", centro - 0.66 * u, -u, 0.7, color=self.YELLOW,
                      etiqueta=r"f_k", lado=DOWN, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "Empujamos la caja rampa arriba",
            "revelar": ["rampa", "caja", "theta"],
            "text": ["La fuerza F es horizontal: hay que descomponerla en ejes de la rampa."],
        },
        {
            "titulo": "Diagrama de cuerpo libre",
            "revelar": ["F", "w", "N"],
            "math": [
                r"F\cos 37^\circ - mg\sin 37^\circ - f_k = ma",
                r"N = mg\cos 37^\circ + F\sin 37^\circ",
            ],
            "resaltar": ["F", "N"],
        },
        {
            "titulo": "Descomposiciones en ejes de la rampa",
            "revelar": ["F_guia", "F_x", "F_y", "w_guia", "w_x", "w_y", "fk"],
            "text": ["F empuja contra la rampa: la normal (y la fricción) crecen con F."],
            "resaltar": ["F_x", "w_x"],
        },
        {
            "titulo": "Despejando la fuerza F",
            "math": [
                r"F(\cos 37^\circ - \mu_k\sin 37^\circ) = m(a + g\sin 37^\circ + \mu_k g\cos 37^\circ)",
                r"F = \dfrac{74.7}{0.618} = 121\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F = 31.2\ \mathrm{N}, \qquad N = 25.0\ \mathrm{N}"


class P5_77(ProblemaScene):
    numero = "5.77"
    titulo = "Báscula en un elevador que acelera"
    subtitulo = "Segunda ley de Newton · peso aparente"
    lista_datos = [
        ("Masa de la persona:", r"m = 64\ \mathrm{kg}"),
        ("Rapidez del elevador:", r"v(t) = (3.0)t + (0.20)t^2"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "muroI", p(-1.9, -2.2), p(-1.9, 2.2), color=self.MUTED, grosor=3)
        self.f_linea(fig, "muroD", p(1.9, -2.2), p(1.9, 2.2), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "cabina", p(0.0, -0.3), ancho=2.2, alto=1.9,
                      color=self.BLUE)
        self.f_texto(fig, "etCab", "elevador", p(0.0, 0.35), size=24, color=self.WHITE)
        self.f_cuerpo(fig, "persona", p(0.0, -0.7), forma="punto", color=self.WHITE)
        self.f_vector(fig, "N", p(0.0, -0.7), UP, 1.0, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", p(0.0, -0.7), DOWN, 0.7, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "a", p(1.55, -0.3), UP, 0.9, color=self.RED,
                      etiqueta=r"a", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La persona viaja dentro del elevador",
            "revelar": ["muroI", "muroD", "cabina", "etCab", "persona"],
            "text": ["La báscula mide la normal N, no el peso mg."],
        },
        {
            "titulo": "Aceleración en t = 4.0 s",
            "revelar": ["a"],
            "math": [r"a = \dfrac{dv}{dt} = 3.0 + 0.40t = 4.6\ \mathrm{m/s^2}"],
            "resaltar": ["a"],
        },
        {
            "titulo": "Lectura de la báscula",
            "revelar": ["N", "w"],
            "math": [r"N = m(g+a) = 64(9.80+4.6) = 9.2\times10^2\ \mathrm{N}"],
            "text": ["El elevador sube acelerando: la persona pesa más."],
            "resaltar": ["N"],
        },
    ]
    resultado_latex = r"N = 9.2\times10^2\ \mathrm{N}"


class P5_80(ProblemaScene):
    numero = "5.80"
    titulo = "Martillo colgante en un autobús que acelera"
    subtitulo = "Segunda ley de Newton · marco acelerado"
    lista_datos = [
        ("Ángulo con el techo:", r"67^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "techo", p(-3.0, 1.9), p(3.0, 1.9), color=self.MUTED, grosor=4)
        O = p(0.0, 1.9)
        phi = np.deg2rad(23.0)
        cuerda_dir = np.array([-np.sin(phi), -np.cos(phi), 0.0])
        M = O + 2.1 * cuerda_dir
        self.f_linea(fig, "cuerda", O, M, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "martillo", M, ancho=0.65, alto=0.55,
                      color=self.ORANGE, etiqueta="m")
        self.f_angulo(fig, "ang67", O, O + LEFT, M, radio=0.7,
                      etiqueta=r"67^\circ", etiqueta_size=22)
        self.f_angulo(fig, "angPhi", O, O + DOWN, M, radio=0.95,
                      etiqueta=r"\phi", etiqueta_size=24)
        self.f_vector(fig, "T", M, O - M, 1.05, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", M, DOWN, 0.85, color=self.ORANGE,
                      etiqueta=r"mg", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "a", p(1.5, 0.2), RIGHT, 1.0, color=self.RED,
                      etiqueta=r"a", lado=UP, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "El martillo cuelga inclinado hacia atrás",
            "revelar": ["techo", "cuerda", "martillo", "ang67"],
            "text": ["El autobús acelera hacia adelante y la cuerda se inclina."],
        },
        {
            "titulo": "Ángulo con la vertical",
            "revelar": ["angPhi"],
            "math": [r"\phi = 90^\circ - 67^\circ = 23^\circ"],
            "resaltar": ["angPhi"],
        },
        {
            "titulo": "Aceleración del autobús",
            "revelar": ["T", "w", "a"],
            "math": [
                r"T\sin\phi = ma, \qquad T\cos\phi = mg",
                r"a = g\tan\phi = (9.80)\tan 23^\circ = 4.16\ \mathrm{m/s^2}",
            ],
            "resaltar": ["T", "a"],
        },
    ]
    resultado_latex = r"a = 4.16\ \mathrm{m/s^2}"


class P5_84(ProblemaScene):
    numero = "5.84"
    titulo = "Fracción de cuerda que puede colgar de una mesa"
    subtitulo = "Primera ley de Newton · fricción estática límite"
    lista_datos = [
        ("Coef. de fricción estática:", r"\mu_s"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.2, 0.2), p(0.5, 0.2), color=self.MUTED, grosor=4)
        self.f_linea(fig, "pata", p(-2.9, 0.2), p(-2.9, -1.9), color=self.MUTED, grosor=3)
        self.f_linea(fig, "cuerdaM", p(-2.6, 0.32), p(0.5, 0.32), color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaC", p(0.5, 0.2), p(0.5, -1.4), color=self.WHITE, grosor=5)
        self.f_texto(fig, "etMesa", r"(1-x)w", (-1.1, 0.95, 0), size=26,
                     color=self.CYAN, math=True)
        self.f_texto(fig, "etCuelga", r"xw", (1.05, -0.6, 0), size=26,
                     color=self.ORANGE, math=True)
        self.f_vector(fig, "fk", p(-1.3, 0.32), LEFT, 0.9, color=self.YELLOW,
                      etiqueta=r"f_s", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "wC", p(0.5, -1.0), DOWN, 0.75, color=self.ORANGE,
                      etiqueta=r"xw", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Parte sobre la mesa y parte colgando",
            "revelar": ["mesa", "pata", "cuerdaM", "cuerdaC", "etMesa", "etCuelga"],
            "text": ["x es la fracción de cuerda que cuelga del borde."],
        },
        {
            "titulo": "Equilibrio en el borde",
            "revelar": ["fk", "wC"],
            "math": [r"xw = f_s = \mu_s(1-x)w"],
            "text": ["Lo que cuelga tira; la fricción sobre la mesa lo sostiene."],
            "resaltar": ["fk", "wC"],
        },
        {
            "titulo": "Despejando la fracción",
            "math": [r"x(1+\mu_s) = \mu_s \;\Rightarrow\; x = \dfrac{\mu_s}{1+\mu_s}"],
        },
    ]
    resultado_latex = r"x = \dfrac{\mu_s}{1+\mu_s}"


class P5_85(ProblemaScene):
    numero = "5.85"
    titulo = "Caja sobre la plataforma de una camioneta"
    subtitulo = "Segunda ley de Newton · fricción que acelera"
    lista_datos = [
        ("Masa de la caja:", r"m = 40.0\ \mathrm{kg}"),
        ("Fricción estática:", r"\mu_s = 0.30"),
        ("Fricción cinética:", r"\mu_k = 0.20"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "plataforma", p(-3.3, -0.6), p(3.3, -0.6), color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "caja", p(-0.2, -0.15), ancho=1.3, alto=0.8,
                      color=self.BLUE)
        self.f_texto(fig, "etCaja", "caja", p(-0.2, 0.55), size=22, color=self.WHITE)
        self.f_vector(fig, "accA", p(-0.2, -1.15), RIGHT, 0.95, color=self.CYAN,
                      etiqueta=r"a_N", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "fA", p(0.45, -0.15), RIGHT, 0.9, color=self.YELLOW,
                      etiqueta=r"f = 88", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "accB", p(-0.2, -1.15), LEFT, 0.95, color=self.CYAN,
                      etiqueta=r"a_S", lado=DOWN, etiqueta_size=22)
        self.f_vector(fig, "fB", p(-0.85, -0.15), LEFT, 0.85, color=self.YELLOW,
                      etiqueta=r"f_k", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La caja viaja sobre la camioneta",
            "revelar": ["plataforma", "caja", "etCaja"],
            "text": ["Solo la fricción puede acelerar a la caja con la camioneta."],
        },
        {
            "titulo": "a) Aceleración de 2.20 m/s² al norte",
            "revelar": ["accA", "fA"],
            "math": [
                r"f_{\mathrm{req}} = ma = (40.0)(2.20) = 88.0\ \mathrm{N}",
                r"f_{s,\max} = \mu_s mg = 0.30(40.0)(9.80) = 118\ \mathrm{N}",
            ],
            "text": ["Como 88.0 < 118, no desliza: f = 88.0 N al norte."],
            "resaltar": ["fA"],
        },
        {
            "titulo": "b) Aceleración de 3.40 m/s² al sur",
            "ocultar": ["accA", "fA"],
            "revelar": ["accB", "fB"],
            "math": [r"f_{\mathrm{req}} = (40.0)(3.40) = 136\ \mathrm{N} > 118\ \mathrm{N}"],
            "text": ["La caja desliza: la fricción pasa a ser cinética."],
            "resaltar": ["fB"],
        },
        {
            "titulo": "Fricción cinética",
            "math": [r"f_k = \mu_k mg = 0.20(40.0)(9.80) = 78.4\ \mathrm{N}"],
            "text": ["Al sur, opuesta al deslizamiento de la caja."],
        },
    ]
    resultado_latex = r"a)\ 88.0\ \mathrm{N}\ \text{al norte}; \qquad b)\ 78.4\ \mathrm{N}\ \text{al sur}"


class P5_87(ProblemaScene):
    numero = "5.87"
    titulo = "Dos esferas idénticas que se tocan"
    subtitulo = "Primera ley de Newton · suspensión en V"
    lista_datos = [
        ("Masa de cada esfera:", r"m = 15.0\ \mathrm{kg}"),
        ("Diámetro:", r"d = 25.0\ \mathrm{cm}"),
        ("Alambres laterales:", r"35.0\ \mathrm{cm}"),
        ("Cable único:", r"18.0\ \mathrm{cm}"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "techo", p(-2.2, 2.0), p(2.2, 2.0), color=self.MUTED, grosor=3)
        J = p(0.0, 1.1)
        self.f_linea(fig, "cable", p(0.0, 2.0), J, color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "nudo", J, forma="punto", color=self.WHITE)
        cI = p(-0.625, -0.5346)
        cD = p(0.625, -0.5346)
        self.f_linea(fig, "alambreI", J, cI, color=self.WHITE, grosor=4)
        self.f_linea(fig, "alambreD", J, cD, color=self.WHITE, grosor=4)
        esfI = Circle(radius=0.625, color=self.BLUE, stroke_width=7).move_to(cI)
        fig.registrar("esfI", esfI, lambda m: Create(m))
        esfD = Circle(radius=0.625, color=self.GREEN, stroke_width=7).move_to(cD)
        fig.registrar("esfD", esfD, lambda m: Create(m))
        self.f_angulo(fig, "phiI", J, J + DOWN, cI, radio=0.45,
                      etiqueta=r"\phi", etiqueta_size=22)
        self.f_angulo(fig, "phiD", J, J + DOWN, cD, radio=0.45,
                      etiqueta=r"\phi", etiqueta_size=22)
        self.f_vector(fig, "T1", cI, J - cI, 0.85, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "T2", cD, J - cD, 0.85, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w1", cI, DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"mg", lado=LEFT, etiqueta_size=20)
        self.f_vector(fig, "w2", cD, DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "Tc", J, UP, 0.8, color=self.GREEN,
                      etiqueta=r"T_c", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "N1", cI + UP * 0.1, LEFT, 0.7, color=self.YELLOW,
                      etiqueta=r"N", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "N2", cD + UP * 0.1, RIGHT, 0.7, color=self.YELLOW,
                      etiqueta=r"N", lado=UP, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "Dos esferas colgadas que se tocan",
            "revelar": ["techo", "cable", "nudo", "alambreI", "alambreD",
                        "esfI", "esfD", "phiI", "phiD"],
            "text": ["Los centros quedan a un diámetro: cada alambre se inclina."],
        },
        {
            "titulo": "Geometría: ángulo de cada alambre",
            "math": [r"\sin\phi = \dfrac{12.5}{35.0} = 0.357 \;\Rightarrow\; \phi = 20.9^\circ"],
            "resaltar": ["phiI", "phiD"],
        },
        {
            "titulo": "Tensión en cada alambre lateral",
            "revelar": ["T1", "T2", "w1", "w2"],
            "math": [
                r"T = \dfrac{mg}{\cos\phi} = \dfrac{(15.0)(9.80)}{\cos 20.9^\circ}",
                r"T = 157\ \mathrm{N}",
            ],
            "resaltar": ["T1", "T2"],
        },
        {
            "titulo": "Tensión en el cable único",
            "revelar": ["Tc"],
            "math": [r"T_{\mathrm{cable}} = 2mg = 2(15.0)(9.80) = 294\ \mathrm{N}"],
            "resaltar": ["Tc"],
        },
        {
            "titulo": "Empuje entre las esferas",
            "revelar": ["N1", "N2"],
            "math": [r"N = T\sin\phi = 157(0.357) = 56.2\ \mathrm{N}"],
            "resaltar": ["N1", "N2"],
        },
    ]
    resultado_latex = r"T = 157\ \mathrm{N}, \quad T_{\mathrm{cable}} = 294\ \mathrm{N}, \quad N = 56.2\ \mathrm{N}"


class P5_68(ProblemaScene):
    numero = "5.68"
    titulo = "Bloque en rampa con masa colgante"
    subtitulo = "Segunda ley de Newton · rampa con fricción"
    lista_datos = [
        ("Masa en la rampa:", r"m_1 = 20.0\ \mathrm{kg}"),
        ("Ángulo:", r"\alpha = 53.1^\circ"),
        ("Coef. de fricción:", r"\mu_k = 0.40"),
        ("Descenso:", r"12.0\ \mathrm{m} \text{ en } 3.00\ \mathrm{s}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(53.1)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.2, -1.4)
        B = A + 3.6 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=7)
        self.f_linea(fig, "suelo", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "alpha", A, A + u, A + RIGHT, radio=0.55,
                      etiqueta=r"\alpha", etiqueta_size=22)
        P = B
        self.f_polea(fig, "polea", P, radio=0.32, color=self.BLUE)
        c1 = A + 1.7 * u + 0.40 * n
        g = self.f_cuerpo(fig, "bloque1", c1, ancho=1.15, alto=0.7,
                          color=self.BLUE, etiqueta=r"m_1")
        g[0].rotate(th, about_point=c1)
        self.f_linea(fig, "cuerdaR", c1 + 0.62 * u, P, color=self.WHITE, grosor=5)
        mx = P[0] + 0.32
        self.f_linea(fig, "cuerdaV", p(mx, P[1]), p(mx, 0.45), color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "bloque2", p(mx, 0.1), ancho=0.9, alto=0.7,
                      color=self.GREEN, etiqueta=r"m_2")
        self.f_vector(fig, "T1", c1 + 0.62 * u, u, 0.8, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=22)
        self.f_vector(fig, "T2", p(mx, 0.45), UP, 0.65, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "w1", c1, DOWN, 1.15, color=self.ORANGE,
                      etiqueta=r"m_1g", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "fk1", c1 - 0.62 * u, -u, 0.7, color=self.YELLOW,
                      etiqueta=r"f_k", lado=DOWN, etiqueta_size=20)
        self.f_vector(fig, "N1", c1, n, 0.9, color=self.CYAN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w2", p(mx, 0.1), DOWN, 0.9, color=self.ORANGE,
                      etiqueta=r"m_2g", lado=LEFT, etiqueta_size=20)
        return fig

    pasos = [
        {
            "titulo": "m₁ en la rampa unido a m₂ colgante",
            "revelar": ["rampa", "suelo", "alpha", "polea", "bloque1", "bloque2",
                        "cuerdaR", "cuerdaV"],
            "text": ["La masa colgante desciende y arrastra al bloque rampa arriba."],
        },
        {
            "titulo": "Aceleración del sistema",
            "math": [r"a = \dfrac{2d}{t^2} = \dfrac{2(12.0)}{(3.00)^2} = 2.67\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Ecuación de movimiento",
            "revelar": ["T1", "T2", "w1", "fk1", "N1", "w2"],
            "math": [r"m_2 g - m_1 g\sin\alpha - \mu_k m_1 g\cos\alpha = (m_1+m_2)a"],
            "resaltar": ["T1", "T2"],
        },
        {
            "titulo": "Despejar la masa colgante",
            "math": [
                r"m_2 = \dfrac{m_1(g\sin\alpha + \mu_k g\cos\alpha + a)}{g-a}",
                r"m_2 = \dfrac{20.0(7.84+2.35+2.67)}{7.13} = 36.1\ \mathrm{kg}",
            ],
        },
    ]
    resultado_latex = r"m_2 = 36.1\ \mathrm{kg}"


class P5_72(ProblemaScene):
    numero = "5.72"
    titulo = "Bloque A y peso colgante en equilibrio"
    subtitulo = "Primera ley de Newton · fricción estática"
    lista_datos = [
        ("Peso del bloque A:", r"w_A = 60.0\ \mathrm{N}"),
        ("Coef. de fricción estática:", r"\mu_s = 0.25"),
        ("Peso colgante:", r"w = 12.0\ \mathrm{N}"),
        ("Ángulo de la cuerda:", r"45.0^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "mesa", p(-3.2, 0.0), p(-0.3, 0.0), color=self.MUTED, grosor=4)
        A = p(-1.5, 0.42)
        self.f_cuerpo(fig, "bloqueA", A, ancho=1.2, alto=0.72,
                      color=self.BLUE, etiqueta="A")
        Q = A + 1.9 * np.array([np.cos(np.deg2rad(45.0)), np.sin(np.deg2rad(45.0)), 0.0])
        self.f_polea(fig, "polea", Q, radio=0.3, color=self.BLUE)
        self.f_linea(fig, "cuerda", A + p(0.2, 0.2), Q, color=self.WHITE, grosor=5)
        self.f_linea(fig, "cuerdaV", p(Q[0] + 0.3, Q[1]), p(Q[0] + 0.3, 1.05),
                     color=self.WHITE, grosor=5)
        self.f_cuerpo(fig, "pesa", p(Q[0] + 0.3, 0.72), ancho=0.7, alto=0.55,
                      color=self.ORANGE, etiqueta="w")
        self.f_angulo(fig, "ang45", A + p(0.2, 0.2), A + p(1.2, 0.2), Q,
                      radio=0.5, etiqueta=r"45^\circ", etiqueta_size=20)
        self.f_vector(fig, "T", A + p(0.2, 0.2), Q - A, 0.95, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "f", A, LEFT, 0.9, color=self.YELLOW,
                      etiqueta=r"f", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "N_A", A, UP, 0.85, color=self.CYAN,
                      etiqueta=r"N_A", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "w_A", A, DOWN, 0.95, color=self.ORANGE,
                      etiqueta=r"w_A", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "A sobre la mesa, la pesa tira a 45°",
            "revelar": ["mesa", "bloqueA", "polea", "cuerda", "cuerdaV", "pesa", "ang45"],
            "text": ["La cuerda tira de A hacia arriba y hacia la derecha."],
        },
        {
            "titulo": "Tensión de la cuerda",
            "revelar": ["T"],
            "math": [r"T = w = 12.0\ \mathrm{N}"],
            "resaltar": ["T"],
        },
        {
            "titulo": "Fuerza de fricción sobre A",
            "revelar": ["f", "N_A", "w_A"],
            "math": [r"f = T\cos 45^\circ = 12.0(0.707) = 8.49\ \mathrm{N}"],
            "text": ["Dirigida hacia la izquierda, opuesta al tirón."],
            "resaltar": ["f"],
        },
        {
            "titulo": "Peso máximo para el equilibrio",
            "math": [
                r"w\cos 45^\circ = \mu_s(w_A - w\sin 45^\circ)",
                r"w_{\max} = \dfrac{0.25(60.0)}{0.884} = 17.0\ \mathrm{N}",
            ],
            "text": ["Al crecer w, la fricción necesaria crece pero la normal disminuye."],
        },
    ]
    resultado_latex = r"f = 8.49\ \mathrm{N}, \qquad w_{\max} = 17.0\ \mathrm{N}"


class P5_74(ProblemaScene):
    numero = "5.74"
    titulo = "Lavador de ventanas empujando el cepillo"
    subtitulo = "Primera ley de Newton · empuje contra la pared"
    lista_datos = [
        ("Peso del cepillo:", r"w = 15.0\ \mathrm{N}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.150"),
        ("Ángulo de la fuerza:", r"53.1^\circ"),
    ]

    def crear_figura(self):
        fig = Figura()
        pared_x = -2.2
        centro = p(-1.8, 0.0)
        self.f_linea(fig, "pared", p(pared_x, -1.9), p(pared_x, 1.9),
                     color=self.MUTED, grosor=4)
        self.f_cuerpo(fig, "cepillo", centro, ancho=0.7, alto=1.15,
                      color=self.BLUE)
        self.f_texto(fig, "etCep", "cepillo", centro + DOWN * 0.82,
                     size=20, color=self.MUTED)
        fdir = np.array([-np.sin(np.deg2rad(53.1)), np.cos(np.deg2rad(53.1)), 0.0])
        self.f_vector(fig, "F", centro, fdir, 1.5, color=self.RED,
                      etiqueta=r"F", lado=UP, etiqueta_size=26)
        self.f_angulo(fig, "angF", centro, centro + UP, centro + fdir, radio=0.55,
                      etiqueta=r"53.1^\circ", etiqueta_size=20)
        self.f_vector(fig, "N", centro, RIGHT, 1.05, color=self.CYAN,
                      etiqueta=r"N", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "fk", centro + RIGHT * 0.2, DOWN, 0.65, color=self.YELLOW,
                      etiqueta=r"f_k", lado=RIGHT, etiqueta_size=20)
        self.f_vector(fig, "w", centro + LEFT * 0.2, DOWN, 1.05, color=self.ORANGE,
                      etiqueta=r"w", lado=LEFT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "El cepillo sube a rapidez constante",
            "revelar": ["pared", "cepillo", "etCep"],
            "text": ["El lavador empuja hacia arriba y contra la ventana."],
        },
        {
            "titulo": "La pared responde con la normal",
            "revelar": ["F", "N", "angF"],
            "math": [r"N = F\sin 53.1^\circ, \qquad f_k = \mu_k F\sin 53.1^\circ"],
            "resaltar": ["N"],
        },
        {
            "titulo": "Equilibrio vertical (rapidez constante)",
            "revelar": ["fk", "w"],
            "math": [
                r"F\cos 53.1^\circ = w + f_k",
                r"F(\cos 53.1^\circ - \mu_k\sin 53.1^\circ) = w",
            ],
            "resaltar": ["F"],
        },
        {
            "titulo": "Resolver la fuerza y la normal",
            "math": [
                r"F = \dfrac{15.0}{0.6004-0.1200} = 31.2\ \mathrm{N}",
                r"N = F\sin 53.1^\circ = 25.0\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F = 31.2\ \mathrm{N}, \qquad N = 25.0\ \mathrm{N}"


class P5_57(ProblemaScene):
    numero = "5.57"
    titulo = "Dos cuerdas unidas a un cable de acero"
    subtitulo = "Primera ley de Newton · tensión máxima admisible"
    lista_datos = [
        ("Ángulos con la horizontal:", r"60^\circ,\ 40^\circ"),
        ("Tensión máxima admisible:", r"5000\ \mathrm{N}"),
    ]

    def crear_figura(self):
        fig = Figura()
        ty = 1.6
        K = p(0.0, -0.2)

        def tope(ang_deg, lado):
            ang = np.deg2rad(ang_deg)
            largo = (ty - K[1]) / np.sin(ang)
            x = K[0] + (-1 if lado == "izq" else 1) * largo * np.cos(ang)
            return p(x, ty)

        p1 = tope(60, "izq")
        p2 = tope(40, "der")
        self.f_linea(fig, "techo", p(-1.6, ty), p(2.7, ty), color=self.MUTED, grosor=3)
        self.f_linea(fig, "cuerda1", K, p1, color=self.CYAN, grosor=4)
        self.f_linea(fig, "cuerda2", K, p2, color=self.GREEN, grosor=4)
        self.f_cuerpo(fig, "nudo", K, forma="punto", color=self.WHITE)
        self.f_linea(fig, "cuerdaV", K, p(0.0, -1.2), color=self.MUTED, grosor=3)
        self.f_cuerpo(fig, "carga", p(0.0, -1.5), ancho=0.9, alto=0.55,
                      color=self.BLUE, etiqueta="w")
        self.f_angulo(fig, "ang1", p1, p(p1[0] + 1.0, ty), K, radio=0.45,
                      etiqueta=r"60^\circ", etiqueta_size=20)
        self.f_angulo(fig, "ang2", p2, p(p2[0] - 1.0, ty), K, radio=0.45,
                      etiqueta=r"40^\circ", etiqueta_size=20)
        self.f_vector(fig, "T1", K, p1 - K, 1.1, color=self.CYAN,
                      etiqueta=r"T_1", lado=LEFT, etiqueta_size=24)
        self.f_vector(fig, "T2", K, p2 - K, 1.1, color=self.GREEN,
                      etiqueta=r"T_2", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", K, DOWN, 1.0, color=self.ORANGE,
                      etiqueta=r"w", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "La carga cuelga de dos cuerdas",
            "revelar": ["techo", "cuerda1", "cuerda2", "nudo", "cuerdaV",
                        "carga", "ang1", "ang2"],
            "text": ["El nudo está en equilibrio y soporta el peso w."],
        },
        {
            "titulo": "Equilibrio horizontal",
            "revelar": ["T1", "T2", "w"],
            "math": [r"T_1\cos 60^\circ = T_2\cos 40^\circ \;\Rightarrow\; T_2 = 0.653\,T_1"],
            "text": ["La cuerda a 60° soporta la mayor tensión."],
            "resaltar": ["T1", "T2"],
        },
        {
            "titulo": "Equilibrio vertical",
            "math": [
                r"T_1\sin 60^\circ + T_2\sin 40^\circ = w",
                r"T_1 = 0.778\,w, \qquad T_2 = 0.508\,w",
            ],
        },
        {
            "titulo": "Peso máximo sin romper",
            "math": [r"0.778\,w \le 5000 \;\Rightarrow\; w_{\max} = 6.43\times10^3\ \mathrm{N}"],
            "text": ["La cuerda 1 (la más tensa) es la que limita."],
        },
    ]
    resultado_latex = r"T_1 = 0.778\,w > T_2, \qquad w_{\max} = 6.43\times10^3\ \mathrm{N}"


class P5_58(ProblemaScene):
    numero = "5.58"
    titulo = "Obrero levantando un peso con poleas"
    subtitulo = "Primera ley de Newton · polea móvil"
    lista_datos = [("Peso levantado:", r"w")]

    def crear_figura(self):
        fig = Figura()
        self.f_linea(fig, "techo", p(-2.6, 2.0), p(2.6, 2.0), color=self.MUTED, grosor=3)
        self.f_linea(fig, "segA", p(-1.12, 2.0), p(-1.12, 0.42), color=self.WHITE, grosor=4)
        self.f_polea(fig, "poleaF", p(1.4, 1.45), radio=0.32, color=self.BLUE)
        self.f_polea(fig, "poleaM", p(-0.8, 0.1), radio=0.32, color=self.GREEN)
        self.f_linea(fig, "segB", p(-0.48, 0.1), p(1.08, 1.45), color=self.WHITE, grosor=4)
        self.f_linea(fig, "segC", p(1.72, 1.45), p(1.72, 0.3), color=self.WHITE, grosor=4)
        self.f_linea(fig, "cadena", p(-0.8, -0.22), p(-0.8, -0.5), color=self.WHITE, grosor=4)
        self.f_cuerpo(fig, "bloque", p(-0.8, -0.85), ancho=0.95, alto=0.6,
                      color=self.ORANGE, etiqueta="w")
        self.f_vector(fig, "T1", p(-1.12, 0.55), UP, 0.8, color=self.CYAN,
                      etiqueta=r"T", lado=LEFT, etiqueta_size=22)
        self.f_vector(fig, "T2", p(-0.48, 0.55), UP, 0.8, color=self.CYAN,
                      etiqueta=r"T", lado=RIGHT, etiqueta_size=22)
        self.f_vector(fig, "F", p(1.72, 0.3), DOWN, 0.85, color=self.RED,
                      etiqueta=r"F", lado=RIGHT, etiqueta_size=24)
        return fig

    pasos = [
        {
            "titulo": "Polea móvil: dos segmentos de cuerda",
            "revelar": ["techo", "poleaF", "poleaM", "segA", "segB",
                        "segC", "cadena", "bloque"],
            "text": ["La polea verde sube con la carga: la cuerda se reparte en dos."],
        },
        {
            "titulo": "La polea móvil equilibra el peso",
            "revelar": ["T1", "T2"],
            "math": [r"2T = w \;\Rightarrow\; T = \dfrac{w}{2}"],
            "resaltar": ["T1", "T2"],
        },
        {
            "titulo": "Fuerza aplicada por el obrero",
            "revelar": ["F"],
            "math": [r"F = T = \dfrac{w}{2}"],
            "text": ["El obrero sostiene solo la mitad del peso."],
            "resaltar": ["F"],
        },
        {
            "titulo": "Tensión en cada cadena",
            "math": [r"T_{\mathrm{inferior}} = w, \qquad T_{\mathrm{superior}} = 2T = w"],
        },
    ]
    resultado_latex = r"F = \dfrac{w}{2}, \qquad T_{\mathrm{inf}} = T_{\mathrm{sup}} = w"


class P5_59(ProblemaScene):
    numero = "5.59"
    titulo = "Esfera apoyada en una pared con alambre"
    subtitulo = "Primera ley de Newton · equilibrio con geometría"
    lista_datos = [
        ("Masa de la esfera:", r"m = 45.0\ \mathrm{kg}"),
        ("Diámetro:", r"32.0\ \mathrm{cm}"),
        ("Longitud del alambre:", r"30.0\ \mathrm{cm}"),
    ]

    def crear_figura(self):
        fig = Figura()
        pared_x = -1.8
        C = p(-1.0, 0.0)
        r = 0.8
        Wp = p(pared_x, np.sqrt(1.5 ** 2 - r ** 2))
        self.f_linea(fig, "pared", p(pared_x, -1.6), p(pared_x, 1.8),
                     color=self.MUTED, grosor=4)
        self.f_linea(fig, "alambre", Wp, C, color=self.WHITE, grosor=5)
        esfera = Circle(radius=r, color=self.BLUE, stroke_width=7).move_to(C)
        fig.registrar("esfera", esfera, lambda m: Create(m))
        self.f_angulo(fig, "theta", Wp, Wp + DOWN, C, radio=0.5,
                      etiqueta=r"\theta", etiqueta_size=22)
        self.f_vector(fig, "T", C, Wp - C, 0.95, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "N", p(pared_x, 0.0), RIGHT, 0.95, color=self.GREEN,
                      etiqueta=r"N", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "w", C, DOWN, 1.15, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La esfera toca la pared y cuelga del alambre",
            "revelar": ["pared", "alambre", "esfera", "theta"],
            "text": ["El centro de la esfera está a un radio de la pared: ese es el cateto opuesto."],
        },
        {
            "titulo": "Geometría del alambre",
            "math": [r"\sin\theta = \dfrac{16.0}{30.0} = 0.533 \;\Rightarrow\; \theta = 32.2^\circ"],
            "resaltar": ["theta"],
        },
        {
            "titulo": "Equilibrio vertical: tensión",
            "revelar": ["T", "w"],
            "math": [
                r"T\cos\theta = mg \;\Rightarrow\; T = \dfrac{(45.0)(9.80)}{\cos 32.2^\circ}",
                r"T = 521\ \mathrm{N}",
            ],
            "resaltar": ["T"],
        },
        {
            "titulo": "Equilibrio horizontal: la pared empuja",
            "revelar": ["N"],
            "math": [r"N = T\sin\theta = 521(0.533) = 278\ \mathrm{N}"],
            "resaltar": ["N"],
        },
    ]
    resultado_latex = r"T = 521\ \mathrm{N}, \qquad N = 278\ \mathrm{N}"


class P5_60(ProblemaScene):
    numero = "5.60"
    titulo = "Esfera sobre rampa sostenida por alambre horizontal"
    subtitulo = "Primera ley de Newton · esfera en equilibrio"
    lista_datos = [
        ("Masa de la esfera:", r"m"),
        ("Inclinación de la rampa:", r"35.0^\circ"),
        ("Rampa lisa", r"\text{sin fricción}"),
    ]

    def crear_figura(self):
        fig = Figura()
        th = np.deg2rad(35.0)
        u = np.array([np.cos(th), np.sin(th), 0.0])
        n = np.array([-np.sin(th), np.cos(th), 0.0])
        A = p(-3.0, -1.6)
        B = A + 4.6 * u
        self.f_linea(fig, "rampa", A, B, color=self.BLUE, grosor=7)
        self.f_linea(fig, "suelo", p(A[0], A[1]), p(B[0], A[1]), color=self.MUTED, grosor=3)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"35^\circ", etiqueta_size=20)
        C = A + 2.6 * u + 0.5 * n
        esfera = Circle(radius=0.5, color=self.GREEN, stroke_width=7).move_to(C)
        fig.registrar("esfera", esfera, lambda m: Create(m))
        s_ancla = (C[1] - A[1]) / np.sin(th)
        ancla = A + s_ancla * u
        self.f_linea(fig, "alambre", C, ancla, color=self.WHITE, grosor=5)
        self.f_vector(fig, "T", C, RIGHT, 0.78, color=self.CYAN,
                      etiqueta=r"T", lado=UP, etiqueta_size=24)
        self.f_vector(fig, "N", C, n, 1.3, color=self.GREEN,
                      etiqueta=r"N", lado=RIGHT, etiqueta_size=24)
        self.f_vector(fig, "w", C, DOWN, 1.25, color=self.ORANGE,
                      etiqueta=r"mg", lado=RIGHT, etiqueta_size=22)
        return fig

    pasos = [
        {
            "titulo": "La esfera descansa en la rampa lisa",
            "revelar": ["rampa", "suelo", "esfera", "theta", "alambre"],
            "text": ["Un alambre horizontal impide que la esfera ruede hacia abajo."],
        },
        {
            "titulo": "Diagrama de cuerpo libre",
            "revelar": ["T", "N", "w"],
            "math": [r"\sum F_x = 0, \qquad \sum F_y = 0"],
            "resaltar": ["T", "N", "w"],
        },
        {
            "titulo": "Equilibrio a lo largo de la rampa",
            "math": [
                r"T\cos 35^\circ = mg\sin 35^\circ",
                r"T = mg\tan 35^\circ = 0.700\,mg",
            ],
            "resaltar": ["T"],
        },
        {
            "titulo": "Fuerza normal de la rampa",
            "math": [
                r"N = mg\cos 35^\circ + T\sin 35^\circ",
                r"N = \dfrac{mg}{\cos 35^\circ} = 1.22\,mg",
            ],
            "resaltar": ["N"],
        },
    ]
    resultado_latex = r"N = 1.22\,mg, \qquad T = 0.700\,mg"
