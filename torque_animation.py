from manim import *
import numpy as np


class TorqueClass(Scene):
    BG = "#07111F"
    PANEL = "#101F35"
    CYAN = "#5EE7F7"
    BLUE = "#56A8FF"
    GREEN = "#63E6A7"
    YELLOW = "#FFD166"
    ORANGE = "#FF9F43"
    RED = "#FF6B7A"
    WHITE = "#F4F7FB"
    MUTED = "#AAB8CF"

    def make_text(self, content, size=28, color=None, **kwargs):
        return Text(
            content,
            font="DejaVu Sans",
            font_size=size,
            color=color or self.WHITE,
            **kwargs,
        )

    def make_math(self, content, size=32, color=None):
        return MathTex(content, font_size=size, color=color or self.WHITE)

    def make_panel(self, content, center, width, height, stroke=None, fill=None):
        box = RoundedRectangle(
            corner_radius=0.16,
            width=width,
            height=height,
            stroke_color=stroke or self.BLUE,
            stroke_width=2,
            fill_color=fill or self.PANEL,
            fill_opacity=0.82,
        ).move_to(center)
        content.move_to(center)
        return VGroup(box, content)

    def make_badge(self, content, center, color, width=1.9):
        box = RoundedRectangle(
            corner_radius=0.14,
            width=width,
            height=0.58,
            stroke_color=color,
            stroke_width=2,
            fill_color=self.PANEL,
            fill_opacity=0.8,
        ).move_to(center)
        label = self.make_text(content, 19, color, weight=BOLD).move_to(box)
        return VGroup(box, label)

    def section_header(self, number, title, subtitle=None):
        kicker = self.make_text(f"{number}  //  MECÁNICA", 17, self.CYAN, weight=BOLD)
        kicker.to_edge(UP, buff=0.22)
        heading_size = 31 if len(title) <= 27 else 25
        heading = self.make_text(title, heading_size, self.WHITE, weight=BOLD)
        heading.next_to(kicker, DOWN, buff=0.04, aligned_edge=LEFT)
        rule = Line(LEFT * 6.55, RIGHT * 6.55, color=self.CYAN, stroke_width=2)
        rule.next_to(heading, DOWN, buff=0.14)
        group = VGroup(kicker, heading, rule)
        if subtitle:
            sub = self.make_text(subtitle, 17, self.MUTED)
            sub.next_to(rule, DOWN, buff=0.12).align_to(heading, LEFT)
            group.add(sub)
        self.play(FadeIn(group, shift=0.15 * DOWN), run_time=0.65)
        return group

    def clear_stage(self):
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in list(self.mobjects)], run_time=0.55)
        self.wait(0.08)

    def opening(self):
        title = self.make_text("TORQUE", 76, self.WHITE, weight=BOLD)
        title.shift(LEFT * 2.35 + UP * 0.72)
        subtitle = self.make_text("Momento de una fuerza y rotación", 28, self.CYAN)
        subtitle.next_to(title, DOWN, buff=0.12).align_to(title, LEFT)
        equation = self.make_math(r"\vec{\tau}=\vec r\times\vec F", 54, self.YELLOW)
        equation.next_to(subtitle, DOWN, buff=0.34).align_to(title, LEFT)
        description = self.make_text("Física mecánica · clase visual", 21, self.MUTED)
        description.next_to(equation, DOWN, buff=0.27).align_to(title, LEFT)

        center = RIGHT * 3.55 + DOWN * 0.45
        wheel = Circle(radius=1.25, color=self.BLUE, stroke_width=6).move_to(center)
        hub = Dot(center, radius=0.09, color=self.WHITE)
        radius = Arrow(
            center,
            center + np.array([1.05, 0.8, 0]),
            buff=0,
            color=self.CYAN,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.12,
        )
        force = Arrow(
            center + np.array([0.72, 0.55, 0]),
            center + np.array([0.55, -0.78, 0]),
            buff=0,
            color=self.ORANGE,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.14,
        )
        rotation = CurvedArrow(
            center + np.array([-0.95, -0.28, 0]),
            center + np.array([0.75, 0.8, 0]),
            angle=-PI / 2,
            color=self.YELLOW,
            tip_length=0.18,
        )
        r_label = self.make_math(r"\vec r", 28, self.CYAN).next_to(radius, UP, buff=0.08)
        f_label = self.make_math(r"\vec F", 28, self.ORANGE).next_to(force, RIGHT, buff=0.1)
        diagram = VGroup(wheel, hub, radius, force, rotation, r_label, f_label)

        badge_row = VGroup(
            self.make_badge("Definición", ORIGIN, self.CYAN, 1.9),
            self.make_badge("Brazo de momento", ORIGIN, self.YELLOW, 2.45),
            self.make_badge("Dinámica rotacional", ORIGIN, self.GREEN, 2.75),
        ).arrange(RIGHT, buff=0.28)
        badge_row.move_to(LEFT * 2.2 + DOWN * 2.75)

        self.play(
            FadeIn(title, shift=0.25 * UP),
            FadeIn(subtitle, shift=0.18 * UP),
            run_time=0.8,
        )
        self.play(Write(equation), run_time=0.8)
        self.play(FadeIn(description), FadeIn(badge_row), run_time=0.7)
        self.play(
            DrawBorderThenFill(wheel),
            Create(radius),
            GrowArrow(force),
            FadeIn(hub),
            FadeIn(rotation),
            FadeIn(r_label),
            FadeIn(f_label),
            run_time=1.1,
        )
        self.play(Circumscribe(equation, color=self.YELLOW), run_time=0.8)
        self.wait(1.1)
        self.clear_stage()

    def vector_definition(self):
        self.section_header("01", "Definición vectorial", "El torque es un producto cruz")
        origin = np.array([-3.8, -0.9, 0])
        point = np.array([-0.65, 0.35, 0])
        force_end = point + np.array([2.0, -1.45, 0])
        r_base = Line(origin, point, color=self.BLUE, stroke_width=3)
        f_base = Line(point, force_end, color=self.ORANGE, stroke_width=3)
        r_vector = Arrow(origin, point, buff=0, color=self.CYAN, stroke_width=7)
        f_vector = Arrow(point, force_end, buff=0, color=self.ORANGE, stroke_width=7)
        origin_dot = Dot(origin, radius=0.1, color=self.WHITE)
        point_dot = Dot(point, radius=0.1, color=self.YELLOW)
        angle = Angle(r_base, f_base, radius=0.62, color=self.YELLOW, stroke_width=4)
        theta = self.make_math(r"\theta", 30, self.YELLOW).next_to(angle, UP, buff=0.05)
        r_label = self.make_math(r"\vec r", 30, self.CYAN).next_to(r_vector, UP, buff=0.1)
        f_label = self.make_math(r"\vec F", 30, self.ORANGE).next_to(f_vector, DOWN, buff=0.1)
        cross = self.make_math(r"\otimes", 42, self.RED).next_to(point, RIGHT + DOWN, buff=0.2)
        origin_label = self.make_text("O", 24, self.WHITE).next_to(origin_dot, LEFT + DOWN, buff=0.12)
        diagram = VGroup(
            r_base,
            f_base,
            r_vector,
            f_vector,
            origin_dot,
            point_dot,
            angle,
            theta,
            r_label,
            f_label,
            cross,
            origin_label,
        )

        formula = VGroup(
            self.make_math(r"\boxed{\vec{\tau}=\vec r\times\vec F}", 36, self.CYAN),
            self.make_math(r"|\vec{\tau}|=rF\sin\theta", 34, self.WHITE),
            self.make_text("El ángulo θ es clave", 21, self.MUTED),
        ).arrange(DOWN, buff=0.25)
        card = self.make_panel(formula, RIGHT * 3.35 + UP * 0.05, 5.35, 3.25)
        direction = self.make_text("En este ejemplo: sentido horario", 21, self.RED)
        direction.next_to(card, DOWN, buff=0.22)

        self.play(Create(r_base), GrowArrow(r_vector), FadeIn(origin_dot), FadeIn(r_label), FadeIn(origin_label))
        self.play(Create(f_base), GrowArrow(f_vector), FadeIn(point_dot), FadeIn(f_label), run_time=0.8)
        self.play(Create(angle), FadeIn(theta), FadeIn(cross), run_time=0.7)
        self.play(Write(card), FadeIn(direction), run_time=0.9)
        self.play(Indicate(formula[0], color=self.YELLOW), Flash(point_dot, color=self.RED, line_length=0.18), run_time=0.8)
        self.wait(1.0)
        self.clear_stage()

    def magnitude_and_moment_arm(self):
        self.section_header("02", "Módulo y brazo de momento", "La perpendicular es la que produce rotación")
        origin = np.array([-3.8, -0.9, 0])
        point = np.array([-0.5, -0.9, 0])
        theta_value = np.deg2rad(35)
        force_end = point + 1.9 * np.array([np.cos(-theta_value), np.sin(-theta_value), 0])
        r_base = Line(origin, point, color=self.BLUE, stroke_width=3)
        f_base = Line(point, force_end, color=self.ORANGE, stroke_width=3)
        r_vector = Arrow(origin, point, buff=0, color=self.CYAN, stroke_width=7)
        f_vector = Arrow(point, force_end, buff=0, color=self.ORANGE, stroke_width=7)
        angle = Angle(r_base, f_base, radius=0.55, color=self.YELLOW, stroke_width=4)
        theta = self.make_math(r"\theta", 28, self.YELLOW).next_to(angle, UP, buff=0.04)
        f_perp = Arrow(point, point + np.array([0, -1.45, 0]), buff=0, color=self.GREEN, stroke_width=6)
        f_parallel = Arrow(point, point + np.array([1.45, 0, 0]), buff=0, color=self.BLUE, stroke_width=5)
        component_guide = DashedLine(
            point + np.array([0, -1.45, 0]),
            point + np.array([1.45, -1.45, 0]),
            color=self.GREEN,
            dash_length=0.1,
        )
        force_direction = (force_end - point) / np.linalg.norm(force_end - point)
        foot = point + np.dot(origin - point, force_direction) * force_direction
        moment_arm = DashedLine(origin, foot, color=self.YELLOW, dash_length=0.12, stroke_width=3)
        pivot = Dot(origin, radius=0.1, color=self.WHITE)
        application = Dot(point, radius=0.09, color=self.WHITE)
        labels = VGroup(
            self.make_math(r"r", 29, self.CYAN).next_to(r_vector, UP, buff=0.08),
            self.make_math(r"\vec F", 28, self.ORANGE).next_to(f_vector, RIGHT, buff=0.08),
            self.make_math(r"F_{\perp}", 25, self.GREEN).next_to(f_perp, LEFT, buff=0.08),
            self.make_math(r"F_{\parallel}", 24, self.BLUE).next_to(f_parallel, DOWN, buff=0.08),
            self.make_math(r"d", 29, self.YELLOW).next_to(moment_arm, UP + RIGHT, buff=0.08),
        )

        formulas = VGroup(
            self.make_math(r"\boxed{|\vec{\tau}|=rF\sin\theta}", 30, self.CYAN),
            self.make_math(r"F_{\perp}=F\sin\theta", 25, self.GREEN),
            self.make_math(r"F_{\parallel}=F\cos\theta", 24, self.BLUE),
            self.make_math(r"d=r\sin\theta", 25, self.YELLOW),
            self.make_math(r"\boxed{|\vec{\tau}|=rF_{\perp}=Fd}", 28, self.WHITE),
        ).arrange(DOWN, buff=0.13)
        card = self.make_panel(formulas, RIGHT * 3.35 + UP * 0.15, 5.35, 4.15)
        note = self.make_text(
            "d es la distancia perpendicular del pivote a la línea de acción de F.",
            18,
            self.MUTED,
        ).next_to(card, DOWN, buff=0.1).shift(RIGHT * 0.55)
        note.set_width(4.8)

        self.play(Create(r_base), GrowArrow(r_vector), FadeIn(pivot), FadeIn(labels[0]))
        self.play(Create(f_base), GrowArrow(f_vector), FadeIn(application), FadeIn(angle), FadeIn(theta), FadeIn(labels[1]), run_time=0.9)
        self.play(GrowArrow(f_perp), GrowArrow(f_parallel), Create(component_guide), FadeIn(labels[2]), FadeIn(labels[3]), run_time=0.8)
        self.play(Create(moment_arm), FadeIn(labels[4]), run_time=0.7)
        self.play(Write(card), FadeIn(note), run_time=0.9)
        self.play(Indicate(formulas[0], color=self.YELLOW), Indicate(formulas[4], color=self.GREEN), run_time=0.8)
        self.wait(1.0)
        self.clear_stage()

    def cartesian_components(self):
        self.section_header("03", "Componentes cartesianos", "La fórmula que se usa en problemas de coordenadas")
        origin = np.array([-4.8, -1.0, 0])
        point = np.array([-1.25, 0.55, 0])
        force_end = point + 1.75 * np.array([np.cos(np.deg2rad(55)), np.sin(np.deg2rad(55)), 0])
        x_axis = Arrow(origin, origin + np.array([1.55, 0, 0]), buff=0, color=self.MUTED, stroke_width=3)
        y_axis = Arrow(origin, origin + np.array([0, 1.55, 0]), buff=0, color=self.MUTED, stroke_width=3)
        x_label = self.make_math(r"x", 22, self.MUTED).next_to(x_axis, RIGHT, buff=0.08)
        y_label = self.make_math(r"y", 22, self.MUTED).next_to(y_axis, UP, buff=0.08)
        projection_x = DashedLine(point, np.array([point[0], origin[1], 0]), color=self.BLUE, dash_length=0.1)
        projection_y = DashedLine(point, np.array([origin[0], point[1], 0]), color=self.BLUE, dash_length=0.1)
        r_vector = Arrow(origin, point, buff=0, color=self.CYAN, stroke_width=7)
        f_vector = Arrow(point, force_end, buff=0, color=self.ORANGE, stroke_width=7)
        f_x = Arrow(point, point + np.array([force_end[0] - point[0], 0, 0]), buff=0, color=self.GREEN, stroke_width=5)
        f_y = Arrow(point, point + np.array([0, force_end[1] - point[1], 0]), buff=0, color=self.YELLOW, stroke_width=5)
        point_dot = Dot(point, radius=0.09, color=self.WHITE)
        origin_dot = Dot(origin, radius=0.09, color=self.WHITE)
        diagram_labels = VGroup(
            self.make_math(r"\vec r", 28, self.CYAN).next_to(r_vector, UP, buff=0.08),
            self.make_math(r"\vec F", 28, self.ORANGE).next_to(f_vector, RIGHT, buff=0.08),
            self.make_math(r"F_x", 23, self.GREEN).next_to(f_x, DOWN, buff=0.07),
            self.make_math(r"F_y", 23, self.YELLOW).next_to(f_y, LEFT, buff=0.07),
        )

        formulas = VGroup(
            self.make_math(r"\vec r=r_x\hat i+r_y\hat j", 29, self.CYAN),
            self.make_math(r"\vec F=F_x\hat i+F_y\hat j", 29, self.ORANGE),
            self.make_math(r"\vec\tau=\vec r\times\vec F", 31, self.WHITE),
            self.make_math(r"\tau_z=\boxed{r_xF_y-r_yF_x}", 31, self.YELLOW),
        ).arrange(DOWN, buff=0.24)
        card = self.make_panel(formulas, RIGHT * 3.25 + UP * 0.15, 5.65, 3.75)
        sign_note = VGroup(
            self.make_text("+k: antihorario", 20, self.GREEN),
            self.make_text("-k: horario", 20, self.RED),
        ).arrange(RIGHT, buff=0.35).next_to(card, DOWN, buff=0.2)
        sign_note.shift(LEFT * 0.15)

        self.play(Create(x_axis), Create(y_axis), FadeIn(x_label), FadeIn(y_label), FadeIn(origin_dot))
        self.play(Create(projection_x), Create(projection_y), FadeIn(point_dot), run_time=0.7)
        self.play(GrowArrow(r_vector), FadeIn(diagram_labels[0]), run_time=0.6)
        self.play(GrowArrow(f_vector), FadeIn(diagram_labels[1]), run_time=0.6)
        self.play(GrowArrow(f_x), GrowArrow(f_y), FadeIn(diagram_labels[2]), FadeIn(diagram_labels[3]), run_time=0.8)
        self.play(Write(card), FadeIn(sign_note), run_time=0.9)
        self.play(Circumscribe(formulas[3], color=self.YELLOW), run_time=0.8)
        self.wait(0.9)
        self.clear_stage()

    def numerical_example(self):
        self.section_header("04", "Ejemplo numérico", "Una fuerza fija puede producir distintos torques")
        origin = np.array([-3.9, -0.8, 0])
        point = np.array([-0.8, -0.8, 0])
        tracker = ValueTracker(np.deg2rad(30))

        def dynamic_diagram():
            angle_value = tracker.get_value()
            r_end = point
            f_end = point + 1.9 * np.array([np.cos(-angle_value), np.sin(-angle_value), 0])
            r_base = Line(origin, r_end, color=self.BLUE, stroke_width=3)
            f_base = Line(r_end, f_end, color=self.ORANGE, stroke_width=3)
            r_arrow = Arrow(origin, r_end, buff=0, color=self.CYAN, stroke_width=7)
            f_arrow = Arrow(r_end, f_end, buff=0, color=self.ORANGE, stroke_width=7)
            angle = Angle(r_base, f_base, radius=0.48, color=self.YELLOW, stroke_width=4)
            angle_label = self.make_math(r"\theta", 26, self.YELLOW).next_to(angle, UP, buff=0.04)
            return VGroup(r_base, f_base, r_arrow, f_arrow, angle, angle_label)

        diagram = always_redraw(dynamic_diagram)
        pivot = Dot(origin, radius=0.1, color=self.WHITE)
        data = VGroup(
            self.make_text("r = 0,50 m", 23, self.CYAN),
            self.make_text("F = 20 N", 23, self.ORANGE),
            self.make_text("θ = 30°", 23, self.YELLOW),
        ).arrange(RIGHT, buff=0.55)
        data.next_to(diagram, UP, buff=0.42)
        r_label = self.make_math(r"r", 27, self.CYAN).next_to(point, UP, buff=0.18)
        f_label = self.make_math(r"\vec F", 27, self.ORANGE).next_to(point, DOWN + RIGHT, buff=0.1)

        readout = DecimalNumber(0, num_decimal_places=1, color=self.YELLOW, font_size=42)
        readout.add_updater(lambda mob: mob.set_value(0.5 * 20 * np.sin(tracker.get_value())))
        unit = self.make_text("N·m", 25, self.YELLOW)
        live_result = VGroup(readout, unit).arrange(RIGHT, buff=0.08)
        result_label = self.make_text("torque instantáneo", 20, self.MUTED)
        live_content = VGroup(result_label, live_result).arrange(DOWN, buff=0.08)
        live_card = self.make_panel(live_content, RIGHT * 3.35 + UP * 1.25, 3.9, 1.15, stroke=self.YELLOW)

        substitution = VGroup(
            self.make_math(r"\tau=rF\sin\theta", 31, self.WHITE),
            self.make_math(r"=(0{,}50)(20)\sin30^\circ", 31, self.WHITE),
            self.make_math(r"=10\cdot0{,}5=\boxed{5{,}0\ \mathrm{N\,m}}", 34, self.GREEN),
        ).arrange(DOWN, buff=0.18)
        card = self.make_panel(substitution, RIGHT * 3.35 + DOWN * 1.25, 5.4, 2.55, stroke=self.GREEN)
        observation = self.make_text(
            "Cuando θ = 90°, toda la fuerza es perpendicular al brazo.",
            20,
            self.MUTED,
        ).next_to(card, DOWN, buff=0.18)
        observation.set_width(5.3)

        self.play(FadeIn(pivot), FadeIn(diagram), FadeIn(data), FadeIn(r_label), FadeIn(f_label), run_time=0.9)
        self.play(FadeIn(live_card), Write(card), FadeIn(observation), run_time=0.9)
        self.play(tracker.animate.set_value(np.deg2rad(90)), run_time=2.0, rate_func=smooth)
        self.play(Indicate(live_result, color=self.YELLOW), run_time=0.7)
        self.play(tracker.animate.set_value(np.deg2rad(30)), run_time=1.6, rate_func=smooth)
        self.wait(0.8)
        readout.clear_updaters()
        self.clear_stage()

    def rotational_equilibrium(self):
        self.section_header("05", "Equilibrio rotacional", "La condición de torque neto es cero")
        beam = Line(LEFT * 3.65 + DOWN * 0.65, RIGHT * 3.65 + DOWN * 0.65, color=self.WHITE, stroke_width=8)
        pivot = Triangle(color=self.YELLOW, fill_color=self.YELLOW, fill_opacity=0.65, stroke_width=3)
        pivot.scale(0.42).next_to(beam.get_center(), DOWN, buff=0.02)
        pivot_dot = Dot(beam.get_center(), radius=0.1, color=self.WHITE)
        left_force = Arrow(LEFT * 2.25 + DOWN * 0.65, LEFT * 2.25 + DOWN * 1.8, buff=0, color=self.ORANGE, stroke_width=6)
        right_force = Arrow(RIGHT * 2.25 + DOWN * 0.65, RIGHT * 2.25 + DOWN * 1.8, buff=0, color=self.ORANGE, stroke_width=6)
        left_distance = DashedLine(beam.get_center() + DOWN * 0.04, LEFT * 2.25 + DOWN * 0.04, color=self.BLUE, dash_length=0.1)
        right_distance = DashedLine(beam.get_center() + DOWN * 0.04, RIGHT * 2.25 + DOWN * 0.04, color=self.BLUE, dash_length=0.1)
        left_label = self.make_text("F₁", 24, self.ORANGE).next_to(left_force, LEFT, buff=0.12)
        right_label = self.make_text("F₂", 24, self.ORANGE).next_to(right_force, RIGHT, buff=0.12)
        d1_label = self.make_math(r"d_1", 24, self.CYAN).next_to(left_distance, UP, buff=0.08)
        d2_label = self.make_math(r"d_2", 24, self.CYAN).next_to(right_distance, UP, buff=0.08)
        torque_left = self.make_math(r"+\tau_1", 27, self.GREEN).next_to(LEFT * 1.45 + UP * 0.05, buff=0.1)
        torque_right = self.make_math(r"-\tau_2", 27, self.RED).next_to(RIGHT * 1.45 + UP * 0.05, buff=0.1)
        formula = VGroup(
            self.make_math(r"\boxed{\sum\tau_z=0}", 39, self.YELLOW),
            self.make_math(r"\tau_1+\tau_2=0", 30, self.WHITE),
            self.make_math(r"F_1d_1=F_2d_2", 31, self.CYAN),
        ).arrange(DOWN, buff=0.16)
        card = self.make_panel(formula, UP * 1.55, 5.0, 2.2, stroke=self.YELLOW)
        example = self.make_text("Ejemplo: 10 N·2 m = 20 N·1 m = 20 N·m", 18, self.MUTED)
        example.move_to(DOWN * 2.05)
        example.set_width(5.1)

        self.play(Create(beam), FadeIn(pivot), FadeIn(pivot_dot), run_time=0.7)
        self.play(GrowArrow(left_force), GrowArrow(right_force), FadeIn(left_label), FadeIn(right_label), run_time=0.8)
        self.play(Create(left_distance), Create(right_distance), FadeIn(d1_label), FadeIn(d2_label), FadeIn(torque_left), FadeIn(torque_right), run_time=0.8)
        self.play(Write(card), FadeIn(example), run_time=0.9)
        self.play(Indicate(formula[0], color=self.GREEN), Indicate(formula[2], color=self.CYAN), run_time=0.8)
        self.wait(0.9)
        self.clear_stage()

    def rotational_dynamics(self):
        self.section_header("06", "Dinámica rotacional", "Del torque neto a la aceleración angular")
        disk_center = LEFT * 3.55 + DOWN * 0.45
        disk = Circle(radius=1.28, color=self.BLUE, stroke_width=6).move_to(disk_center)
        hub = Dot(disk_center, radius=0.1, color=self.WHITE)
        radius = Line(disk_center, disk_center + np.array([0.95, 0.78, 0]), color=self.CYAN, stroke_width=6)
        omega = CurvedArrow(
            disk_center + np.array([-0.78, -0.18, 0]),
            disk_center + np.array([0.75, 0.72, 0]),
            angle=-PI / 2,
            color=self.YELLOW,
            tip_length=0.17,
        )
        disk_labels = VGroup(
            self.make_math(r"I", 30, self.CYAN).next_to(hub, LEFT + DOWN, buff=0.16),
            self.make_math(r"\omega", 30, self.YELLOW).next_to(omega, UP, buff=0.08),
        )
        formula = VGroup(
            self.make_text("Segunda ley de Newton rotacional", 20, self.CYAN, weight=BOLD),
            self.make_math(r"\boxed{\sum\tau_z=I\alpha}", 38, self.YELLOW),
            self.make_math(r"\alpha=\frac{d\omega}{dt}", 28, self.WHITE),
            self.make_math(r"\omega=\frac{d\theta}{dt}=\omega_0+\alpha t", 24, self.WHITE),
            self.make_math(r"\theta=\theta_0+\omega_0t+\frac12\alpha t^2", 27, self.WHITE),
        ).arrange(DOWN, buff=0.18)
        card = self.make_panel(formula, RIGHT * 2.55 + UP * 0.15, 6.45, 3.55, stroke=self.YELLOW)

        inertia_title = self.make_math(r"I=\int r^2\,dm", 25, self.CYAN)
        inertia_cases = VGroup(
            self.make_math(r"\text{partícula: }I=mr^2", 19, self.WHITE),
            self.make_math(r"\text{disco: }I=\frac12MR^2", 19, self.WHITE),
            self.make_math(r"\text{barra, centro: }I=\frac1{12}ML^2", 19, self.WHITE),
            self.make_math(r"\text{barra, extremo: }I=\frac13ML^2", 19, self.WHITE),
        ).arrange(RIGHT, buff=0.28)
        inertia_content = VGroup(inertia_title, inertia_cases).arrange(DOWN, buff=0.08)
        inertia_panel = self.make_panel(inertia_content, DOWN * 2.62, 12.0, 1.5, stroke=self.CYAN)

        self.play(DrawBorderThenFill(disk), FadeIn(hub), Create(radius), FadeIn(disk_labels[0]), run_time=0.8)
        self.play(Create(omega), FadeIn(disk_labels[1]), run_time=0.7)
        self.play(Write(card), run_time=1.0)
        self.play(Indicate(formula[1], color=self.GREEN), run_time=0.7)
        self.play(FadeIn(inertia_panel), run_time=0.8)
        self.wait(0.8)
        self.clear_stage()

    def work_power_and_angular_momentum(self):
        self.section_header("07", "Trabajo, potencia y momento angular", "Las relaciones que conectan torque y movimiento")
        centers = [LEFT * 4.25, ORIGIN, RIGHT * 4.25]
        cards = []
        first = VGroup(
            self.make_text("MOMENTO ANGULAR", 18, self.CYAN, weight=BOLD),
            self.make_math(r"\vec L=\vec r\times\vec p=I\vec\omega", 24, self.WHITE),
            self.make_math(r"\vec\tau=\frac{d\vec L}{dt}", 29, self.YELLOW),
            self.make_math(r"J_\theta=\int\tau\,dt=\Delta L", 25, self.GREEN),
            self.make_text("impulso angular", 18, self.MUTED),
        ).arrange(DOWN, buff=0.2)
        second = VGroup(
            self.make_text("TRABAJO Y POTENCIA", 18, self.ORANGE, weight=BOLD),
            self.make_math(r"W=\int\tau\,d\theta", 29, self.WHITE),
            self.make_math(r"W=\tau\Delta\theta", 27, self.YELLOW),
            self.make_math(r"P=\tau\omega", 31, self.ORANGE),
            self.make_text("si τ es constante", 18, self.MUTED),
        ).arrange(DOWN, buff=0.2)
        third = VGroup(
            self.make_text("ENERGÍA ROTACIONAL", 18, self.GREEN, weight=BOLD),
            self.make_math(r"E_{\mathrm{rot}}=\frac12I\omega^2", 28, self.WHITE),
            self.make_math(r"W_{\mathrm{ext}}=\Delta E_{\mathrm{rot}}", 25, self.YELLOW),
            self.make_math(r"P=\frac{dE}{dt}", 28, self.GREEN),
            self.make_text("trabajo externo", 18, self.MUTED),
        ).arrange(DOWN, buff=0.2)
        contents = [first, second, third]
        strokes = [self.CYAN, self.ORANGE, self.GREEN]
        for content, center, stroke in zip(contents, centers, strokes):
            cards.append(self.make_panel(content, center + UP * 0.05, 3.75, 3.55, stroke=stroke))

        bottom = self.make_text(
            "Unidades del torque: newton·metro (N·m), aunque tiene las mismas dimensiones que el joule.",
            20,
            self.MUTED,
        ).next_to(VGroup(*cards), DOWN, buff=0.22)
        bottom.set_width(11.6)
        self.play(LaggedStart(*[FadeIn(card, shift=0.15 * UP) for card in cards], lag_ratio=0.18), run_time=1.2)
        self.play(FadeIn(bottom), run_time=0.7)
        self.play(
            Indicate(contents[0][2], color=self.CYAN),
            Indicate(contents[1][3], color=self.ORANGE),
            Indicate(contents[2][1], color=self.GREEN),
            run_time=0.9,
        )
        self.wait(0.9)
        self.clear_stage()

    def summary(self):
        self.section_header("08", "Resumen de fórmulas", "La idea central: perpendicularidad, torque neto y rotación")
        cards = VGroup()
        items = [
            (r"\vec\tau=\vec r\times\vec F", self.CYAN),
            (r"|\tau|=rF\sin\theta=Fd", self.YELLOW),
            (r"\tau_z=r_xF_y-r_yF_x", self.ORANGE),
            (r"\sum\tau=I\alpha", self.GREEN),
            (r"\tau=\frac{dL}{dt}", self.CYAN),
            (r"P=\tau\omega,\quad E_{\mathrm{rot}}=\frac12I\omega^2", self.GREEN),
        ]
        for index, (latex, color) in enumerate(items):
            row = index // 3
            column = index % 3
            center = np.array([-4.25 + 4.25 * column, 1.25 - 2.35 * row, 0])
            content = VGroup(
                self.make_math(latex, 27 if index != 5 else 23, color),
                self.make_text(f"{index + 1:02d}", 15, self.MUTED, weight=BOLD),
            )
            content[1].next_to(content[0], UP, buff=0.1)
            card = self.make_panel(content, center, 3.75, 1.5, stroke=color)
            cards.add(card)

        closing = self.make_text(
            "La fuerza produce rotación cuando tiene una componente perpendicular al brazo de momento.",
            23,
            self.WHITE,
            weight=BOLD,
        ).next_to(cards, DOWN, buff=0.32)
        closing.set_width(10.8)
        units = self.make_math(r"\boxed{[\tau]=\mathrm{N\,m}}", 30, self.YELLOW)
        units.next_to(closing, DOWN, buff=0.2)

        self.play(LaggedStart(*[FadeIn(card, shift=0.12 * UP) for card in cards], lag_ratio=0.12), run_time=1.1)
        self.play(Write(closing), run_time=0.8)
        self.play(FadeIn(units), Circumscribe(cards[0], color=self.CYAN), run_time=0.8)
        self.wait(1.2)

    def construct(self):
        self.camera.background_color = self.BG
        self.opening()
        self.vector_definition()
        self.magnitude_and_moment_arm()
        self.cartesian_components()
        self.numerical_example()
        self.rotational_equilibrium()
        self.rotational_dynamics()
        self.work_power_and_angular_momentum()
        self.summary()
