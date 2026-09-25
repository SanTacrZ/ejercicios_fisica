"""Plantilla reutilizable para resolver problemas del libro paso a paso en Manim.

La idea: el estudiante ve CONSTRUIR el problema, no solo la formula final.
Cada problema es una subclase de ProblemaScene con:

    numero, titulo, subtitulo
    lista_datos  -> [(etiqueta, latex), ...]
    pasos        -> [{"titulo": str, "math": [...], "text": [...],
                      "revelar": [...], "resaltar": [...], "ocultar": [...]}, ...]
    resultado_latex, resultado_nota

Si el problema define `crear_figura()`, la escena reserva la mitad izquierda
para el diagrama (que se va revelando elemento por elemento) y la derecha para
las ecuaciones. La figura persiste a lo largo de los pasos: se construye una
sola vez y cada paso enciende/apaga/resalta sus partes por nombre.

Constructor visual disponible dentro de `crear_figura`:
    self.f_cuerpo, self.f_vector, self.f_linea, self.f_ejes, self.f_angulo,
    self.f_descomponer, self.f_plano_inclinado, self.f_polea, self.f_grafica,
    self.f_texto
"""

from manim import *
import numpy as np


# --------------------------------------------------------------------------- #
#  Animaciones de entrada por tipo de mobject
# --------------------------------------------------------------------------- #
def _anim_flecha(mob):
    """Animacion de entrada para grupos con flechas/lineas + etiquetas."""
    partes = []
    for sub in mob:
        if isinstance(sub, Arrow):
            partes.append(GrowArrow(sub))
        elif isinstance(sub, Line):
            partes.append(Create(sub))
        else:
            partes.append(FadeIn(sub))
    return AnimationGroup(*partes)


def _anim_cuerpo(mob):
    partes = [DrawBorderThenFill(mob[0])]
    if len(mob) > 1:
        partes.append(FadeIn(mob[1]))
    return AnimationGroup(*partes)


def _anim_simple(mob):
    return FadeIn(mob, shift=0.08 * UP)


class Figura(VGroup):
    """Diagrama compuesto por elementos con nombre.

    Cada elemento se registra una vez y puede revelarse, resaltarse u ocultarse
    por nombre en cualquier paso. La figura completa se coloca en la mitad
    izquierda de la pantalla y nunca se borra mientras dure el problema.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mapa = {}
        self._anim = {}
        self._orden = []
        self.revelados = set()

    def registrar(self, nombre, mob, anim_factory=None):
        self._mapa[nombre] = mob
        self._anim[nombre] = anim_factory or _anim_simple
        self._orden.append(nombre)
        self.add(mob)
        return mob

    def mob(self, nombre):
        return self._mapa.get(nombre)

    def colocar_izquierda(self, centro=LEFT * 3.55, ancho_max=6.1, alto_max=6.2):
        if len(self) == 0:
            return
        escala = min(
            ancho_max / max(self.width, 1e-6),
            alto_max / max(self.height, 1e-6),
            1.45,
        )
        escala = max(escala, 0.35)
        if abs(escala - 1.0) > 0.01:
            self.scale(escala)
        self.move_to(centro)

    def revelar(self, scene, nombres, lag=0.18):
        anims = []
        for n in nombres:
            if n in self._mapa and n not in self.revelados:
                anims.append(self._anim[n](self._mapa[n]))
                self.revelados.add(n)
        if anims:
            scene.play(
                LaggedStart(*anims, lag_ratio=lag),
                run_time=0.55 + 0.22 * len(anims),
            )

    def resaltar(self, scene, nombres):
        anims = [
            Indicate(self._mapa[n], color=getattr(scene, "YELLOW"))
            for n in nombres
            if n in self._mapa
        ]
        if anims:
            scene.play(*anims, run_time=0.85)

    def ocultar(self, scene, nombres):
        anims = []
        for n in nombres:
            if n in self._mapa and n in self.revelados:
                anims.append(FadeOut(self._mapa[n]))
                self.revelados.discard(n)
        if anims:
            scene.play(*anims, run_time=0.5)


class ProblemaScene(Scene):
    BG = "#060B16"
    PANEL = "#0F1E33"
    CYAN = "#3FE0FF"
    BLUE = "#5AA9FF"
    GREEN = "#3EE58C"
    YELLOW = "#FFD23F"
    ORANGE = "#FF8B3D"
    RED = "#FF5D7A"
    WHITE = "#FFFFFF"
    MUTED = "#A9BAD4"

    numero = "0.0"
    titulo = ""
    subtitulo = "Aplicación de las leyes de Newton"
    encabezado = "CAPÍTULO 5  //  APLICACIÓN DE LAS LEYES DE NEWTON"

    lista_datos = []
    pasos = []
    resultado_latex = ""
    resultado_nota = ""

    SLOT_FIG = LEFT * 3.55
    SLOT_TXT = RIGHT * 3.55

    # ------------------------------------------------------------------ utils
    def t(self, s, size=28, color=None, weight=NORMAL):
        return Text(
            s,
            font="DejaVu Sans",
            font_size=size,
            color=color or self.WHITE,
            weight=weight,
        )

    def m(self, s, size=34, color=None):
        return MathTex(s, font_size=size, color=color or self.WHITE)

    def marco(self, content, stroke=None, pad=0.34, fill=None):
        box = RoundedRectangle(
            corner_radius=0.16,
            width=content.width + 2 * pad,
            height=content.height + 2 * pad,
            stroke_color=stroke or self.BLUE,
            stroke_width=2,
            fill_color=fill or self.PANEL,
            fill_opacity=0.9,
        )
        box.move_to(content)
        return VGroup(box, content)

    def limpiar(self, run_time=0.45):
        if self.mobjects:
            self.play(
                *[FadeOut(mob) for mob in list(self.mobjects)],
                run_time=run_time,
            )
        self.wait(0.05)

    def pie(self):
        return self.t(
            f"Física universitaria · Sears-Zemansky · problema {self.numero}",
            15,
            self.MUTED,
        ).to_edge(DOWN, buff=0.2)

    # ================================================================ FIGURA
    def crear_figura(self):
        """Sobrescribir para devolver una Figura con el diagrama del problema."""
        return None

    def _dir(self, v):
        v = np.array(v, dtype=float)
        return v / (np.linalg.norm(v) + 1e-9)

    def f_cuerpo(self, fig, nombre, centro, forma="bloque", ancho=1.1, alto=0.75,
                 color=None, etiqueta=None):
        color = color or self.BLUE
        centro = np.array(centro, dtype=float)
        if forma == "punto":
            cuerpo = Dot(centro, radius=0.15, color=color)
        else:
            cuerpo = RoundedRectangle(
                corner_radius=0.1, width=ancho, height=alto,
                stroke_color=color, stroke_width=3,
                fill_color=self.PANEL, fill_opacity=0.9,
            ).move_to(centro)
        grupo = VGroup(cuerpo)
        if etiqueta:
            if any(c in etiqueta for c in "_^{}\\"):
                lab = self.m(etiqueta, 22, self.WHITE)
            else:
                lab = self.t(etiqueta, 19, self.WHITE)
            grupo.add(lab.move_to(cuerpo))
        return fig.registrar(nombre, grupo, _anim_cuerpo)

    def f_vector(self, fig, nombre, origen, direccion, largo, color=None,
                 etiqueta=None, lado=UP, etiqueta_size=28, grosor=9, anim=None):
        color = color or self.ORANGE
        origen = np.array(origen, dtype=float)
        fin = origen + self._dir(direccion) * largo
        arrow = Arrow(
            origen, fin, buff=0, color=color, stroke_width=grosor,
            max_tip_length_to_length_ratio=0.18, max_stroke_width_to_length_ratio=6.0,
        )
        grupo = VGroup(arrow)
        if etiqueta:
            grupo.add(self.m(etiqueta, etiqueta_size, color).next_to(arrow, lado, buff=0.08))
        return fig.registrar(nombre, grupo, anim or _anim_flecha)

    def f_linea(self, fig, nombre, inicio, fin, color=None, grosor=5,
                discontinuo=False, etiqueta=None, lado=UP, etiqueta_size=24):
        color = color or self.WHITE
        if discontinuo:
            linea = DashedLine(inicio, fin, color=color, stroke_width=grosor, dash_length=0.1)
        else:
            linea = Line(inicio, fin, color=color, stroke_width=grosor)
        grupo = VGroup(linea)
        if etiqueta:
            grupo.add(self.m(etiqueta, etiqueta_size, color).next_to(linea, lado, buff=0.08))
        return fig.registrar(nombre, grupo, _anim_flecha)

    def f_texto(self, fig, nombre, contenido, pos, size=22, color=None, math=False):
        mob = self.m(contenido, size, color) if math else self.t(contenido, size, color)
        p = np.array(pos, dtype=float)
        mob.move_to(p if p.shape == (3,) else np.append(p, 0.0))
        return fig.registrar(nombre, mob, _anim_simple)

    def f_ejes(self, fig, nombre, centro, largo_x=2.0, largo_y=2.0, color=None,
               etiqueta_x=None, etiqueta_y=None):
        color = color or self.MUTED
        centro = np.array(centro, dtype=float)
        ax = Arrow(centro, centro + RIGHT * largo_x, buff=0, color=color,
                   stroke_width=3, max_tip_length_to_length_ratio=0.08)
        ay = Arrow(centro, centro + UP * largo_y, buff=0, color=color,
                   stroke_width=3, max_tip_length_to_length_ratio=0.08)
        grupo = VGroup(ax, ay)
        if etiqueta_x:
            grupo.add(self.m(etiqueta_x, 24, color).next_to(ax, RIGHT, buff=0.06))
        if etiqueta_y:
            grupo.add(self.m(etiqueta_y, 24, color).next_to(ay, UP, buff=0.06))
        return fig.registrar(nombre, grupo, _anim_flecha)

    def f_angulo(self, fig, nombre, vertice, punto1, punto2, radio=0.55,
                 color=None, etiqueta=None, etiqueta_size=26, separacion=0.34):
        color = color or self.YELLOW
        v = np.array(vertice, dtype=float)
        d1 = self._dir(np.array(punto1, dtype=float) - v)
        d2 = self._dir(np.array(punto2, dtype=float) - v)
        delta = (np.arctan2(d2[1], d2[0]) - np.arctan2(d1[1], d1[0])) % (2 * np.pi)
        if delta > np.pi:
            d1, d2 = d2, d1
        l1 = Line(v, v + d1)
        l2 = Line(v, v + d2)
        ang = Angle(l1, l2, radius=radio, color=color, stroke_width=5)
        grupo = VGroup(ang)
        if etiqueta:
            lab = self.m(etiqueta, etiqueta_size, color)
            lab.move_to(v + self._dir(d1 + d2) * (radio + separacion))
            grupo.add(lab)
        return fig.registrar(nombre, grupo, _anim_flecha)

    def f_descomponer(self, fig, nombre, origen, direccion, largo,
                      eje1=None, eje2=None, color_x=None, color_y=None,
                      etiqueta_x=None, etiqueta_y=None, lado_x=DOWN, lado_y=LEFT,
                      desplaz_x=None, desplaz_y=None):
        """Descompone un vector en dos ejes (por defecto x/y globales).

        Registra {nombre}_x, {nombre}_y y {nombre}_guia.
        """
        origen = np.array(origen, dtype=float)
        e1 = self._dir(eje1 if eje1 is not None else RIGHT)
        e2 = self._dir(eje2 if eje2 is not None else UP)
        vec = self._dir(direccion) * largo
        fin = origen + vec
        fin1 = origen + np.dot(vec, e1) * e1
        fin2 = origen + np.dot(vec, e2) * e2
        color_x = color_x or self.GREEN
        color_y = color_y or self.YELLOW

        if np.linalg.norm(fin1 - origen) > 0.02:
            ax = Arrow(origen, fin1, buff=0, color=color_x, stroke_width=8,
                       max_tip_length_to_length_ratio=0.14)
            gx = VGroup(ax)
            if etiqueta_x:
                lab = self.m(etiqueta_x, 25, color_x)
                if desplaz_x is not None:
                    lab.move_to(ax.get_center() + np.array([desplaz_x[0], desplaz_x[1], 0.0]))
                else:
                    lab.next_to(ax, lado_x, buff=0.1)
                gx.add(lab)
            fig.registrar(f"{nombre}_x", gx, _anim_flecha)
        if np.linalg.norm(fin2 - origen) > 0.02:
            ay = Arrow(origen, fin2, buff=0, color=color_y, stroke_width=8,
                       max_tip_length_to_length_ratio=0.14)
            gy = VGroup(ay)
            if etiqueta_y:
                lab = self.m(etiqueta_y, 25, color_y)
                if desplaz_y is not None:
                    lab.move_to(ay.get_center() + np.array([desplaz_y[0], desplaz_y[1], 0.0]))
                else:
                    lab.next_to(ay, lado_y, buff=0.1)
                gy.add(lab)
            fig.registrar(f"{nombre}_y", gy, _anim_flecha)
        guias = VGroup(
            DashedLine(fin1, fin, color=color_x, stroke_width=2, dash_length=0.08),
            DashedLine(fin2, fin, color=color_y, stroke_width=2, dash_length=0.08),
        )
        fig.registrar(f"{nombre}_guia", guias, lambda m: Create(m))
        return fin

    def f_plano_inclinado(self, fig, nombre, base, angulo_grados, largo=4.0,
                          color=None):
        """Dibuja rampa + suelo + altura. Devuelve A, B, C, theta (rad)."""
        color = color or self.BLUE
        base = np.array(base, dtype=float)
        th = np.deg2rad(angulo_grados)
        u = np.array([np.cos(th), np.sin(th), 0])
        A = base
        B = base + largo * u
        C = np.array([B[0], base[1], 0.0])
        rampa = Line(A, B, color=color, stroke_width=7)
        suelo = Line(A, C, color=self.MUTED, stroke_width=3)
        altura = Line(B, C, color=self.MUTED, stroke_width=2)
        fig.registrar(nombre, VGroup(rampa, suelo, altura), lambda m: Create(m))
        return {"A": A, "B": B, "C": C, "theta": th, "u": u}

    def f_polea(self, fig, nombre, centro, radio=0.55, color=None):
        color = color or self.BLUE
        centro = np.array(centro, dtype=float)
        circ = Circle(radius=radio, color=color, stroke_width=7).move_to(centro)
        hub = Dot(centro, radius=0.07, color=self.WHITE)
        return fig.registrar(
            nombre, VGroup(circ, hub),
            lambda m: AnimationGroup(Create(m[0]), FadeIn(m[1])),
        )

    def f_grafica(self, fig, nombre, funciones, x_range, y_range,
                  x_label="x", y_label="y", colores=None, ancho=4.6, alto=3.2,
                  centro=ORIGIN):
        colores = colores or [self.CYAN, self.YELLOW, self.GREEN, self.ORANGE]
        c = np.array(centro, dtype=float)
        c = c if c.shape == (3,) else np.append(c, 0.0)
        axes = Axes(
            x_range=x_range, y_range=y_range, x_length=ancho, y_length=alto,
            axis_config={
                "color": self.MUTED, "stroke_width": 2,
                "include_numbers": True, "font_size": 16,
                "tip_width": 0.12, "tip_height": 0.12,
            },
        ).move_to(c)
        labels = axes.get_axis_labels(x_label, y_label)
        fig.registrar(
            f"{nombre}_ejes", VGroup(axes, labels),
            lambda m: AnimationGroup(Create(axes), FadeIn(labels)),
        )
        for i, f in enumerate(funciones):
            p = axes.plot(f, color=colores[i % len(colores)], stroke_width=4)
            fig.registrar(f"{nombre}_c{i}", p, lambda m: Create(m))
        return axes

    # ------------------------------------------------------------- estructura
    def portada(self):
        kicker = self.t(self.encabezado, 19, self.CYAN, weight=BOLD)
        num = self.t(f"PROBLEMA {self.numero}", 25, self.YELLOW, weight=BOLD)
        title = self.t(self.titulo, 40, self.WHITE, weight=BOLD)
        title.set_width(min(title.width, 12.0))
        rule = Line(LEFT * 5.2, RIGHT * 5.2, color=self.CYAN, stroke_width=2)
        sub = self.t(self.subtitulo, 21, self.MUTED)

        head = VGroup(kicker, num).arrange(DOWN, buff=0.14)
        block = VGroup(head, title, rule, sub).arrange(DOWN, buff=0.26)
        block.move_to(ORIGIN)

        self.play(FadeIn(head, shift=0.2 * DOWN), run_time=0.5)
        self.play(FadeIn(title, shift=0.2 * UP), Create(rule), FadeIn(sub), run_time=0.8)
        self.wait(1.0)
        self.limpiar()

    def mostrar_datos(self):
        header = self.t("DATOS DEL PROBLEMA", 21, self.YELLOW, weight=BOLD)
        rows = VGroup()
        for label, value in self.lista_datos:
            fila = VGroup(
                self.t(label, 24, self.MUTED),
                self.m(value, 32, self.CYAN),
            ).arrange(RIGHT, buff=0.5)
            rows.add(fila)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        content = VGroup(header, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        panel = self.marco(content, stroke=self.CYAN, pad=0.42)
        panel.move_to(ORIGIN)
        footer = self.pie()

        box = panel[0]
        self.play(Create(box), run_time=0.7)
        self.play(FadeIn(header, shift=0.15 * DOWN), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(r, shift=0.12 * UP) for r in rows], lag_ratio=0.18),
            run_time=0.9,
        )
        self.play(FadeIn(footer), run_time=0.3)
        self.wait(0.9)
        self.limpiar()

    def mostrar_paso(self, idx, paso):
        if self._contenido is not None:
            self.play(FadeOut(self._contenido), run_time=0.3)
            self._contenido = None

        header = self.t(f"PASO {idx}", 20, self.CYAN, weight=BOLD)
        title = self.t(paso["titulo"], 27, self.WHITE, weight=BOLD)
        title.set_width(min(title.width, 11.2))
        content = VGroup(header, title).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

        math_lines = VGroup()
        for s in paso.get("math", []):
            line = self.m(s, 31, self.WHITE)
            line.set_width(min(line.width, 5.7))
            math_lines.add(line)
        if len(math_lines):
            math_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
            content.add(math_lines)

        text_lines = VGroup()
        for s in paso.get("text", []):
            line = self.t(s, 21, self.MUTED)
            line.set_width(min(line.width, 5.7))
            text_lines.add(line)
        if len(text_lines):
            text_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            content.add(text_lines)

        content.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        con_figura = self._fig is not None
        if con_figura:
            if content.width > 5.8:
                content.scale(5.8 / content.width)
            content.move_to(self.SLOT_TXT)
        else:
            content.move_to(ORIGIN)
        footer = self.pie()

        if self._fig is not None:
            if paso.get("ocultar"):
                self._fig.ocultar(self, paso["ocultar"])
            if paso.get("revelar"):
                self._fig.revelar(self, paso["revelar"])

        self.play(FadeIn(header, shift=0.15 * DOWN), FadeIn(title, shift=0.15 * DOWN),
                  run_time=0.45)
        if len(math_lines):
            self.play(
                LaggedStart(*[Write(l) for l in math_lines], lag_ratio=0.35),
                run_time=0.8 + 0.25 * len(math_lines),
            )
        if len(text_lines):
            self.play(FadeIn(text_lines, shift=0.1 * UP), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.2)
        self._contenido = VGroup(content, footer)

        if self._fig is not None and paso.get("resaltar"):
            self._fig.resaltar(self, paso["resaltar"])
        self.wait(0.9)

    def mostrar_resultado(self):
        if self._contenido is not None:
            self.play(FadeOut(self._contenido), run_time=0.3)
            self._contenido = None

        header = self.t("RESULTADO", 22, self.GREEN, weight=BOLD)
        eq = self.m(self.resultado_latex, 40, self.YELLOW)
        eq.set_width(min(eq.width, 5.6 if self._fig is not None else 11.6))
        piezas = [header, eq]
        if self.resultado_nota:
            note = self.t(self.resultado_nota, 22, self.MUTED)
            note.set_width(min(note.width, 5.5 if self._fig is not None else 11.4))
            piezas.append(note)
        group = VGroup(*piezas).arrange(DOWN, buff=0.28)
        panel = self.marco(group, stroke=self.GREEN, pad=0.5)
        panel.move_to(self.SLOT_TXT if self._fig is not None else ORIGIN)
        footer = self.pie()

        self.play(Create(panel[0]), FadeIn(header), run_time=0.5)
        self.play(Write(eq), run_time=0.8)
        if self.resultado_nota:
            self.play(FadeIn(group[2]), run_time=0.4)
        self.play(FadeIn(footer), Circumscribe(eq, color=self.YELLOW), run_time=0.9)
        self.wait(1.2)

    def construct(self):
        self.camera.background_color = self.BG
        self._fig = None
        self._contenido = None
        self.portada()
        if self.lista_datos:
            self.mostrar_datos()
        self._fig = self.crear_figura()
        if self._fig is not None:
            self._fig.colocar_izquierda(centro=self.SLOT_FIG)
        for i, paso in enumerate(self.pasos, 1):
            self.mostrar_paso(i, paso)
        if self.resultado_latex:
            self.mostrar_resultado()


# =========================================================================== #
#  EJEMPLOS DE USO DEL MOTOR VISUAL
#  Render:
#      manim -ql fisica_base.py DemoRampa
#      manim -ql fisica_base.py DemoGrafica
# =========================================================================== #
class DemoRampa(ProblemaScene):
    numero = "DEMO"
    titulo = "Bloque sobre un plano inclinado liso"
    subtitulo = "Diagrama de cuerpo libre y descomposición del peso"
    lista_datos = [
        ("Masa del bloque:", r"m = 10.0\ \mathrm{kg}"),
        ("Inclinación:", r"\theta = 30.0^\circ"),
        ("Gravedad:", r"g = 9.80\ \mathrm{m/s^2}"),
    ]

    def crear_figura(self):
        fig = Figura()
        geo = self.f_plano_inclinado(fig, "rampa", base=(-3.1, -1.9, 0), angulo_grados=30, largo=4.6)
        A, u, th = geo["A"], geo["u"], geo["theta"]
        n = np.array([-np.sin(th), np.cos(th), 0])

        centro = A + 2.9 * u + 0.42 * n
        self.f_cuerpo(fig, "bloque", centro, ancho=1.0, alto=0.7, color=self.BLUE)
        self.f_angulo(fig, "theta", A, A + u, A + RIGHT, radio=0.6,
                      etiqueta=r"\theta")

        w_len = 1.7
        self.f_vector(fig, "w", centro, DOWN, w_len, color=self.ORANGE,
                      etiqueta=r"\vec w=mg", lado=DOWN, etiqueta_size=26)
        self.f_vector(fig, "N", centro, n, w_len * np.cos(th), color=self.CYAN,
                      etiqueta=r"\vec N", lado=RIGHT, etiqueta_size=26)
        self.f_descomponer(
            fig, "w", centro, DOWN, w_len,
            eje1=u, eje2=n,
            etiqueta_x=r"mg\sin\theta", etiqueta_y=r"mg\cos\theta",
            desplaz_x=(-0.62, -0.34), desplaz_y=(0.82, -0.05),
        )
        return fig

    pasos = [
        {
            "titulo": "La geometría del problema",
            "revelar": ["rampa", "bloque", "theta"],
            "text": ["El bloque desliza sobre una superficie lisa: no hay fricción."],
        },
        {
            "titulo": "Diagrama de cuerpo libre",
            "revelar": ["w", "N"],
            "math": [r"\sum \vec F = m\vec a"],
            "text": ["Sobre el bloque actúan el peso y la normal de la rampa."],
            "resaltar": ["w", "N"],
        },
        {
            "titulo": "Descomponemos el peso",
            "revelar": ["w_guia", "w_x", "w_y"],
            "math": [r"w_\perp = mg\cos\theta", r"w_\parallel = mg\sin\theta"],
            "text": ["Elegimos ejes paralelo y perpendicular a la rampa."],
            "resaltar": ["w_x", "w_y"],
        },
        {
            "titulo": "Equilibrio perpendicular",
            "math": [
                r"N = mg\cos\theta",
                r"N = (10.0)(9.80)\cos 30^\circ = 84.9\ \mathrm{N}",
            ],
            "resaltar": ["N"],
        },
        {
            "titulo": "Aceleración a lo largo de la rampa",
            "math": [
                r"ma = mg\sin\theta \;\Rightarrow\; a = g\sin\theta",
                r"a = (9.80)\sin 30^\circ = 4.90\ \mathrm{m/s^2}",
            ],
            "resaltar": ["w_x"],
        },
    ]
    resultado_latex = r"N = 84.9\ \mathrm{N}, \qquad a = 4.90\ \mathrm{m/s^2}"
    resultado_nota = "La masa no influye en la aceleración sobre un plano liso."


class DemoGrafica(ProblemaScene):
    numero = "DEMO"
    titulo = "Gráficas del movimiento con aceleración constante"
    subtitulo = "De la ecuación a la curva, paso a paso"
    lista_datos = [
        ("Aceleración:", r"a = 2.00\ \mathrm{m/s^2}"),
        ("Velocidad inicial:", r"v_0 = 0"),
    ]

    def crear_figura(self):
        fig = Figura()
        self.f_grafica(
            fig, "grafica",
            funciones=[lambda t: 2.0 * t, lambda t: 1.0 * t ** 2],
            x_range=[0, 3, 1], y_range=[0, 10, 2],
            x_label="t\\,(\\mathrm{s})", y_label="v,\\ x", ancho=4.8, alto=3.4,
        )
        return fig

    pasos = [
        {
            "titulo": "Velocidad contra el tiempo",
            "revelar": ["grafica_ejes", "grafica_c0"],
            "math": [r"v = v_0 + at = (2.00)t"],
            "text": ["Una recta: la velocidad crece linealmente con el tiempo."],
        },
        {
            "titulo": "Posición contra el tiempo",
            "revelar": ["grafica_c1"],
            "math": [r"x = v_0t + \tfrac12 at^2 = (1.00)t^2"],
            "text": ["Una parábola: el desplazamiento crece como t al cuadrado."],
        },
        {
            "titulo": "Leer la gráfica",
            "math": [r"\text{pendiente de } v(t) = a", r"\text{área bajo } v(t) = \Delta x"],
            "text": ["La pendiente da la aceleración; el área, la distancia recorrida."],
        },
    ]
    resultado_latex = r"v = 2.00\,t, \qquad x = 1.00\,t^2"
