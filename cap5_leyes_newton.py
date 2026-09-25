"""Capítulo 5 - Aplicación de las leyes de Newton.

Lista del profesor "Leyes de Newton" (mapeada al Cap. 5):
1, 4, 5, 6, 8, 12, 14, 19, 20, 21, 33, 34, 35, 37, 43, 45, 46, 52, 56,
60, 61, 65, 66, 69, 71, 72, 75, 76, 80, 81, 84, 85, 87, 94, 97.

Render de una escena:
    manim -ql cap5_leyes_newton.py P5_1
Render de todo el capítulo:
    manim -ql cap5_leyes_newton.py
"""

from fisica_base import ProblemaScene


class P5_1(ProblemaScene):
    numero = "5.1"
    titulo = "Polea con dos pesas en equilibrio"
    lista_datos = [("Peso de cada bloque:", r"w = 25.0\ \mathrm{N}")]
    pasos = [
        {
            "titulo": "Condición de equilibrio",
            "math": [r"\sum F_y = 0", r"T - w = 0"],
            "text": ["Cada pesa está en reposo: la tensión de la cuerda iguala a su peso."],
        },
        {
            "titulo": "Tensión en la cuerda",
            "math": [r"T = w = 25.0\ \mathrm{N}"],
        },
        {
            "titulo": "Tensión en la cadena",
            "math": [r"T_{\mathrm{cadena}} = 2T = 2(25.0)", r"T_{\mathrm{cadena}} = 50.0\ \mathrm{N}"],
            "text": ["La cadena sostiene las dos ramas de la cuerda."],
        },
    ]
    resultado_latex = r"T = 25.0\ \mathrm{N}, \qquad T_{\mathrm{cadena}} = 50.0\ \mathrm{N}"


class P5_4(ProblemaScene):
    numero = "5.4"
    titulo = "Tracción de la columna vertebral"
    lista_datos = [
        ("Masa del paciente:", r"m = 78.5\ \mathrm{kg}"),
        ("Coef. de fricción estática:", r"\mu_s = 0.75"),
        ("Ángulo de cada cable:", r"\theta = 65^\circ"),
    ]
    pasos = [
        {
            "titulo": "La tracción máxima vence la fricción estática",
            "math": [
                r"F_{\max} = f_{s,\max} = \mu_s N = \mu_s m g",
                r"F_{\max} = 0.75(78.5)(9.80)",
                r"F_{\max} = 577\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Tensión en cada cable del collarín",
            "math": [
                r"2T\cos 65^\circ = F_{\max}",
                r"T = \dfrac{F_{\max}}{2\cos 65^\circ} = \dfrac{577}{2(0.4226)}",
                r"T = 683\ \mathrm{N}",
            ],
            "text": ["Los dos cables comparten la fuerza horizontal de tracción."],
        },
    ]
    resultado_latex = r"F_{\max}=577\ \mathrm{N}, \qquad T=683\ \mathrm{N}"


class P5_5(ProblemaScene):
    numero = "5.5"
    titulo = "Cuadro colgado por dos alambres"
    lista_datos = [
        ("Tensión en cada alambre:", r"T = 0.75\,w"),
        ("Ángulos iguales con la vertical:", r"\theta"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio vertical",
            "math": [r"2T\cos\theta = w"],
        },
        {
            "titulo": "Sustituyendo la tensión",
            "math": [r"2(0.75w)\cos\theta = w", r"\cos\theta = \dfrac{w}{1.5w} = 0.6667"],
        },
        {
            "titulo": "Ángulo con la vertical",
            "math": [r"\theta = \arccos(0.6667) = 48.2^\circ"],
        },
    ]
    resultado_latex = r"\theta = 48.2^\circ"


class P5_6(ProblemaScene):
    numero = "5.6"
    titulo = "Bola de demolición sostenida por dos cables"
    lista_datos = [
        ("Masa de la bola:", r"m = 4090\ \mathrm{kg}"),
        ("Cable B con la vertical:", r"40^\circ"),
        ("Cable A horizontal", r"T_A"),
    ]
    pasos = [
        {
            "titulo": "Peso de la bola",
            "math": [r"w = mg = (4090)(9.80) = 4.01\times10^4\ \mathrm{N}"],
        },
        {
            "titulo": "Cable inclinado (equilibrio vertical)",
            "math": [
                r"T_B\cos 40^\circ = w",
                r"T_B = \dfrac{4.01\times10^4}{\cos 40^\circ} = 5.23\times10^4\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Cable horizontal (equilibrio horizontal)",
            "math": [
                r"T_A = T_B\sin 40^\circ",
                r"T_A = (5.23\times10^4)(0.6428) = 3.36\times10^4\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"T_B = 5.23\times10^4\ \mathrm{N}, \qquad T_A = 3.36\times10^4\ \mathrm{N}"


class P5_8(ProblemaScene):
    numero = "5.8"
    titulo = "Automóvil retenido sobre una rampa lisa"
    lista_datos = [
        ("Masa del automóvil:", r"m = 1130\ \mathrm{kg}"),
        ("Inclinación de la rampa:", r"25.0^\circ"),
        ("Cable sobre la rampa:", r"31.0^\circ"),
    ]
    pasos = [
        {
            "titulo": "Componentes del peso",
            "math": [
                r"mg\sin 25^\circ = 4.68\times10^3\ \mathrm{N}",
                r"mg\cos 25^\circ = 1.00\times10^4\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Equilibrio a lo largo de la rampa",
            "math": [
                r"T\cos 31^\circ = mg\sin 25^\circ",
                r"T = \dfrac{4680}{\cos 31^\circ} = 5.46\times10^3\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Fuerza normal de la rampa",
            "math": [
                r"N = mg\cos 25^\circ - T\sin 31^\circ",
                r"N = 1.00\times10^4 - 2.81\times10^3 = 7.22\times10^3\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"T = 5.46\times10^3\ \mathrm{N}, \qquad N = 7.22\times10^3\ \mathrm{N}"


class P5_12(ProblemaScene):
    numero = "5.12"
    titulo = "Cohete con fuente de energía a bordo"
    lista_datos = [
        ("Masa total del cohete:", r"m = 125\ \mathrm{kg}"),
        ("Empuje del motor:", r"F = 1720\ \mathrm{N}"),
        ("Peso de la fuente:", r"w_s = 15.5\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del cohete",
            "math": [
                r"F - mg = ma",
                r"a = \dfrac{1720 - (125)(9.80)}{125}",
                r"a = 3.96\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Masa de la fuente de energía",
            "math": [r"m_s = \dfrac{w_s}{g} = \dfrac{15.5}{9.80} = 1.58\ \mathrm{kg}"],
        },
        {
            "titulo": "Fuerza normal del piso sobre la fuente",
            "math": [
                r"N - m_s g = m_s a",
                r"N = m_s(g+a) = (1.58)(13.76)",
                r"N = 21.8\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"a = 3.96\ \mathrm{m/s^2}, \qquad N = 21.8\ \mathrm{N}"


class P5_14(ProblemaScene):
    numero = "5.14"
    titulo = "Tres trineos tirados sobre hielo"
    lista_datos = [
        ("Fuerza de tirón:", r"F = 125\ \mathrm{N}"),
        ("Masas:", r"10.0,\ 20.0,\ 30.0\ \mathrm{kg}"),
    ]
    pasos = [
        {
            "titulo": "Masa total y aceleración del sistema",
            "math": [
                r"m_{\mathrm{total}} = 10.0+20.0+30.0 = 60.0\ \mathrm{kg}",
                r"a = \dfrac{F}{m_{\mathrm{total}}} = \dfrac{125}{60.0} = 2.08\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Tensión en la cuerda A",
            "math": [
                r"T_A = (m_{20}+m_{30})\,a = (50.0)(2.08)",
                r"T_A = 104\ \mathrm{N}",
            ],
            "text": ["La cuerda A arrastra los dos trineos traseros."],
        },
        {
            "titulo": "Tensión en la cuerda B",
            "math": [r"T_B = m_{30}\,a = (30.0)(2.08) = 62.5\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"a = 2.08\ \mathrm{m/s^2},\quad T_A = 104\ \mathrm{N},\quad T_B = 62.5\ \mathrm{N}"


class P5_19(ProblemaScene):
    numero = "5.19"
    titulo = "Roca izada con cadena desde una cantera"
    lista_datos = [
        ("Masa de la roca:", r"m_r = 750.0\ \mathrm{kg}"),
        ("Masa de la cadena:", r"m_c = 575\ \mathrm{kg}"),
        ("Profundidad:", r"h = 125\ \mathrm{m}"),
    ]
    pasos = [
        {
            "titulo": "Tensión máxima de la cadena",
            "math": [
                r"T_{\max} = 2.50\,m_c g = 2.50(575)(9.80)",
                r"T_{\max} = 1.41\times10^4\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Aceleración máxima",
            "math": [
                r"T_{\max} = (m_r + m_c)(g+a)",
                r"g+a = \dfrac{1.41\times10^4}{1325} = 10.63\ \mathrm{m/s^2}",
                r"a = 10.63 - 9.80 = 0.83\ \mathrm{m/s^2}",
            ],
            "text": ["La tensión es máxima al inicio, cuando toda la cadena cuelga."],
        },
        {
            "titulo": "Tiempo para subir 125 m",
            "math": [
                r"h = \tfrac12 a t^2 \Rightarrow t = \sqrt{\dfrac{2(125)}{0.83}}",
                r"t = 17.3\ \mathrm{s}",
            ],
        },
    ]
    resultado_latex = r"a_{\max} = 0.83\ \mathrm{m/s^2},\quad t = 17.3\ \mathrm{s}"


class P5_20(ProblemaScene):
    numero = "5.20"
    titulo = "Peso aparente en un elevador"
    lista_datos = [
        ("Peso del estudiante:", r"w = 550\ \mathrm{N}"),
        ("Masa del elevador + estudiante:", r"M = 850\ \mathrm{kg}"),
        ("Lecturas de la báscula:", r"450,\ 670,\ 0\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Masa del estudiante",
            "math": [r"m = \dfrac{w}{g} = \dfrac{550}{9.80} = 56.1\ \mathrm{kg}"],
        },
        {
            "titulo": "Lectura de 450 N",
            "math": [
                r"N - mg = ma \Rightarrow a = \dfrac{N-mg}{m}",
                r"a = \dfrac{450-550}{56.1} = -1.78\ \mathrm{m/s^2}",
            ],
            "text": ["Aceleración de 1.78 m/s² hacia abajo."],
        },
        {
            "titulo": "Lectura de 670 N",
            "math": [r"a = \dfrac{670-550}{56.1} = 2.14\ \mathrm{m/s^2}"],
            "text": ["Aceleración de 2.14 m/s² hacia arriba."],
        },
        {
            "titulo": "Lectura de 0 N",
            "math": [r"N = 0 \Rightarrow a = -g = 9.80\ \mathrm{m/s^2}"],
            "text": ["Caída libre: el cable se rompió. Sí debe preocuparse."],
        },
        {
            "titulo": "Tensión del cable",
            "math": [
                r"T = M(g-a) = 850(9.80-1.78) = 6.82\times10^3\ \mathrm{N}",
                r"T = M(g-g) = 0 \quad (\text{lectura } 0)",
            ],
        },
    ]
    resultado_latex = r"a_a = 1.78\ \mathrm{m/s^2}\downarrow,\quad a_b = 2.14\ \mathrm{m/s^2}\uparrow,\quad a_c = g"


class P5_21(ProblemaScene):
    numero = "5.21"
    titulo = "Fuerza en un salto vertical"
    lista_datos = [
        ("Altura máxima del salto:", r"h = 0.60\ \mathrm{m}"),
        ("Distancia de impulso:", r"d = 0.50\ \mathrm{m}"),
    ]
    pasos = [
        {
            "titulo": "Rapidez de despegue",
            "math": [r"v = \sqrt{2gh} = \sqrt{2(9.80)(0.60)} = 3.43\ \mathrm{m/s}"],
        },
        {
            "titulo": "Aceleración durante el impulso",
            "math": [r"a = \dfrac{v^2}{2d} = \dfrac{(3.43)^2}{2(0.50)} = 11.8\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Fuerza del suelo en función de w",
            "math": [
                r"N - w = ma = \dfrac{w}{g}a",
                r"N = w\left(1+\dfrac{a}{g}\right) = w\left(1+\dfrac{11.8}{9.80}\right)",
                r"N = 2.20\,w",
            ],
        },
    ]
    resultado_latex = r"N = 2.20\,w"


class P5_33(ProblemaScene):
    numero = "5.33"
    titulo = "Distancia de frenado"
    lista_datos = [
        ("Rapidez inicial:", r"v = 28.7\ \mathrm{m/s}"),
        ("Pavimento seco:", r"\mu_k = 0.80"),
        ("Pavimento húmedo:", r"\mu_k = 0.25"),
    ]
    pasos = [
        {
            "titulo": "Desaceleración por fricción",
            "math": [r"f_k = \mu_k mg = ma \Rightarrow a = \mu_k g"],
        },
        {
            "titulo": "Distancia de frenado (seco)",
            "math": [
                r"d = \dfrac{v^2}{2\mu_k g} = \dfrac{(28.7)^2}{2(0.80)(9.80)}",
                r"d = 52.5\ \mathrm{m}",
            ],
        },
        {
            "titulo": "Rapidez segura en mojado",
            "math": [
                r"v = \sqrt{2\mu_k g d} = \sqrt{2(0.25)(9.80)(52.5)}",
                r"v = 16.0\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"d = 52.5\ \mathrm{m},\quad v_{\mathrm{mojado}} = 16.0\ \mathrm{m/s}"


class P5_34(ProblemaScene):
    numero = "5.34"
    titulo = "Bloques A y B con polea y fricción"
    lista_datos = [
        ("Peso del bloque A:", r"w_A = 45.0\ \mathrm{N}"),
        ("Peso del bloque B:", r"w_B = 25.0\ \mathrm{N}"),
        ("Peso del gato:", r"w_{\mathrm{gato}} = 45.0\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Velocidad constante implica a = 0",
            "math": [r"T = w_B = 25.0\ \mathrm{N}"],
        },
        {
            "titulo": "Coeficiente de fricción cinética",
            "math": [
                r"T = f_k = \mu_k w_A",
                r"\mu_k = \dfrac{25.0}{45.0} = 0.556",
            ],
        },
        {
            "titulo": "Con el gato dormido sobre A",
            "math": [
                r"N = 90.0\ \mathrm{N},\quad f_k = 0.556(90.0) = 50.0\ \mathrm{N}",
                r"\sum F = w_B - f_k = 25.0 - 50.0 = -25.0\ \mathrm{N}",
                r"a = \dfrac{-25.0}{(90.0+25.0)/9.80} = -2.13\ \mathrm{m/s^2}",
            ],
            "text": ["La fricción supera al peso de B: B desacelera; su aceleración es hacia arriba."],
        },
    ]
    resultado_latex = r"\mu_k = 0.556,\quad a = 2.13\ \mathrm{m/s^2}\ (\text{hacia arriba para }B)"


class P5_35(ProblemaScene):
    numero = "5.35"
    titulo = "Dos cajas unidas a velocidad constante"
    lista_datos = [
        ("Masas de las cajas:", r"m_A,\ m_B"),
        ("Coef. de fricción cinética:", r"\mu_k"),
    ]
    pasos = [
        {
            "titulo": "Velocidad constante implica a = 0",
            "math": [r"F = f_A + f_B = \mu_k (m_A + m_B)g"],
        },
        {
            "titulo": "Tensión en la cuerda (bloque A)",
            "math": [r"T = f_A = \mu_k m_A g"],
        },
    ]
    resultado_latex = r"F = \mu_k (m_A + m_B)g, \qquad T = \mu_k m_A g"


class P5_37(ProblemaScene):
    numero = "5.37"
    titulo = "Bloques con polea y mesa con fricción"
    lista_datos = [
        ("Masa del bloque A:", r"m_A = 2.25\ \mathrm{kg}"),
        ("Masa del bloque B:", r"m_B = 1.30\ \mathrm{kg}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.450"),
        ("Distancia recorrida:", r"d = 3.00\ \mathrm{cm}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema",
            "math": [
                r"a = \dfrac{m_B g - \mu_k m_A g}{m_A + m_B}",
                r"a = \dfrac{12.74 - 9.92}{3.55} = 0.794\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Rapidez tras moverse 3.00 cm",
            "math": [
                r"v = \sqrt{2ad} = \sqrt{2(0.794)(0.0300)}",
                r"v = 0.218\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "Tensión en la cuerda",
            "math": [
                r"T = m_B(g-a) = 1.30(9.80-0.794)",
                r"T = 11.7\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"v = 0.218\ \mathrm{m/s},\qquad T = 11.7\ \mathrm{N}"


class P5_43(ProblemaScene):
    numero = "5.43"
    titulo = "Barra giratoria con masas en los extremos"
    lista_datos = [
        ("Longitud de la barra:", r"L = 40.0\ \mathrm{cm}"),
        ("Masa en cada extremo:", r"m = 1.15\ \mathrm{kg}"),
        ("Fuerza máxima de los tornillos:", r"F_{\max} = 75.0\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Radio de giro",
            "math": [r"r = \dfrac{L}{2} = 0.200\ \mathrm{m}"],
        },
        {
            "titulo": "Rapidez máxima en el plano horizontal",
            "math": [
                r"F = \dfrac{mv^2}{r} \Rightarrow v = \sqrt{\dfrac{F r}{m}}",
                r"v = \sqrt{\dfrac{(75.0)(0.200)}{1.15}} = 3.61\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "En círculo vertical el punto crítico es abajo",
            "math": [
                r"T_{\mathrm{abajo}} = \dfrac{mv^2}{r} + mg",
                r"T_{\mathrm{arriba}} = \dfrac{mv^2}{r} - mg",
            ],
            "text": ["La tensión es mayor en la parte inferior: ahí es más probable que se desprenda."],
        },
        {
            "titulo": "Rapidez máxima en círculo vertical",
            "math": [
                r"\dfrac{mv^2}{r} = F_{\max} - mg = 63.7\ \mathrm{N}",
                r"v = \sqrt{\dfrac{(63.7)(0.200)}{1.15}} = 3.33\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"v_{\mathrm{horiz}} = 3.61\ \mathrm{m/s},\qquad v_{\mathrm{vert}} = 3.33\ \mathrm{m/s}"


class P5_45(ProblemaScene):
    numero = "5.45"
    titulo = "Curva peraltada para auto y camión"
    lista_datos = [
        ("Masa del automóvil:", r"1125\ \mathrm{kg}"),
        ("Masa del camión:", r"2250\ \mathrm{kg}"),
        ("Radio de la curva:", r"R = 225\ \mathrm{m}"),
        ("Rapidez de diseño:", r"v = 65.0\ \mathrm{mi/h}"),
    ]
    pasos = [
        {
            "titulo": "Rapidez en unidades SI",
            "math": [r"v = 65.0\ \mathrm{mi/h} = 29.1\ \mathrm{m/s}"],
        },
        {
            "titulo": "Ángulo de peralte",
            "math": [
                r"\tan\theta = \dfrac{v^2}{gR} = \dfrac{(29.1)^2}{(9.80)(225)} = 0.383",
                r"\theta = 21.0^\circ",
            ],
            "text": ["No depende de la masa: el camión no necesita ir más lento."],
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
    resultado_latex = r"\theta = 21.0^\circ,\quad N_{\mathrm{auto}} = 1.18\times10^4\ \mathrm{N},\quad N_{\mathrm{camion}} = 2.36\times10^4\ \mathrm{N}"


class P5_52(ProblemaScene):
    numero = "5.52"
    titulo = "Piloto acrobático saliendo de una picada"
    lista_datos = [
        ("Masa del piloto:", r"m = 50.0\ \mathrm{kg}"),
        ("Rapidez en el punto bajo:", r"v = 95.0\ \mathrm{m/s}"),
        ("Aceleración máxima:", r"a_{\max} = 4.00g"),
    ]
    pasos = [
        {
            "titulo": "Radio mínimo del círculo",
            "math": [
                r"a = \dfrac{v^2}{R} \le 4.00g \Rightarrow R \ge \dfrac{v^2}{4.00g}",
                r"R_{\min} = \dfrac{(95.0)^2}{4.00(9.80)} = 230\ \mathrm{m}",
            ],
        },
        {
            "titulo": "Peso aparente en el punto más bajo",
            "math": [
                r"N = m\left(g + \dfrac{v^2}{R}\right) = m(g + 4.00g) = 5mg",
                r"N = 5(50.0)(9.80) = 2450\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"R_{\min} = 230\ \mathrm{m},\qquad N = 2450\ \mathrm{N}"


class P5_56(ProblemaScene):
    numero = "5.56"
    titulo = "Explorador colgado de una cuerda entre riscos"
    lista_datos = [
        ("Masa del explorador:", r"m = 90.0\ \mathrm{kg}"),
        ("Tensión de rotura:", r"T_{\max} = 2.50\times10^4\ \mathrm{N}"),
        ("Ángulo inicial:", r"\theta = 10.0^\circ"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio vertical en el punto medio",
            "math": [r"2T\sin\theta = mg"],
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
        },
    ]
    resultado_latex = r"T = 2.54\times10^3\ \mathrm{N},\qquad \theta_{\min} = 1.01^\circ"


class P5_60(ProblemaScene):
    numero = "5.60"
    titulo = "Esfera sobre rampa sostenida por alambre horizontal"
    lista_datos = [
        ("Masa de la esfera:", r"m"),
        ("Inclinación de la rampa:", r"35.0^\circ"),
        ("Rampa lisa", r"\text{sin fricción}"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio a lo largo de la rampa",
            "math": [
                r"T\cos 35^\circ = mg\sin 35^\circ",
                r"T = mg\tan 35^\circ = 0.700\,mg",
            ],
        },
        {
            "titulo": "Fuerza normal de la rampa",
            "math": [
                r"N = mg\cos 35^\circ + T\sin 35^\circ",
                r"N = \dfrac{mg}{\cos 35^\circ} = 1.22\,mg",
            ],
        },
    ]
    resultado_latex = r"N = 1.22\,mg,\qquad T = 0.700\,mg"


class P5_61(ProblemaScene):
    numero = "5.61"
    titulo = "Fuerzas durante las flexiones en barra"
    lista_datos = [
        ("Peso de la persona:", r"w = 680\ \mathrm{N}"),
        ("Altura del cuerpo:", r"d = 30\ \mathrm{cm}"),
        ("Tiempo total:", r"t = 1.0\ \mathrm{s}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración en la primera mitad",
            "math": [
                r"d = \tfrac12 a_1(0.5)^2 + \left(a_1(0.5)(0.5)-\tfrac12 a_1(0.5)^2\right)",
                r"0.30 = 0.25\,a_1 \Rightarrow a_1 = 1.2\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Fuerza que ejercen los brazos",
            "math": [
                r"F - w = \dfrac{w}{g}a_1",
                r"F = w\left(1+\dfrac{a_1}{g}\right) = 680\left(1+\dfrac{1.2}{9.80}\right)",
                r"F = 763\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F = 763\ \mathrm{N}"


class P5_65(ProblemaScene):
    numero = "5.65"
    titulo = "Dos cajas con fuerza inclinada y fricción"
    lista_datos = [
        ("Fuerza aplicada:", r"F = 40.0\ \mathrm{N}"),
        ("Ángulo sobre la horizontal:", r"53.1^\circ"),
        ("Masa de la caja B:", r"m_B = 5.00\ \mathrm{kg}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.30"),
        ("Aceleración:", r"a = 1.50\ \mathrm{m/s^2}"),
    ]
    pasos = [
        {
            "titulo": "Fuerza normal y fricción sobre B",
            "math": [
                r"N_B = m_B g - F\sin 53.1^\circ = 17.0\ \mathrm{N}",
                r"f_B = \mu_k N_B = 5.10\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Tensión en la cuerda (sobre B)",
            "math": [
                r"F\cos 53.1^\circ - T - f_B = m_B a",
                r"T = 24.0 - 5.10 - 7.50 = 11.4\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Masa de la caja A",
            "math": [
                r"T = m(a + \mu_k g) \Rightarrow m = \dfrac{T}{a+\mu_k g}",
                r"m = \dfrac{11.4}{1.50 + 2.94} = 2.57\ \mathrm{kg}",
            ],
        },
    ]
    resultado_latex = r"T = 11.4\ \mathrm{N},\qquad m = 2.57\ \mathrm{kg}"


class P5_66(ProblemaScene):
    numero = "5.66"
    titulo = "Fuerza horizontal para subir una rampa"
    lista_datos = [
        ("Masa de la caja:", r"m = 6.00\ \mathrm{kg}"),
        ("Inclinación:", r"37.0^\circ"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.30"),
        ("Aceleración deseada:", r"a = 4.20\ \mathrm{m/s^2}"),
    ]
    pasos = [
        {
            "titulo": "Ecuaciones a lo largo y perpendicular",
            "math": [
                r"F\cos 37^\circ - mg\sin 37^\circ - f_k = ma",
                r"N = mg\cos 37^\circ + F\sin 37^\circ,\quad f_k = \mu_k N",
            ],
        },
        {
            "titulo": "Despejando la fuerza F",
            "math": [
                r"F(\cos 37^\circ - \mu_k\sin 37^\circ) = m(a + g\sin 37^\circ + \mu_k g\cos 37^\circ)",
                r"F = \dfrac{74.7}{0.618} = 121\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F = 121\ \mathrm{N}"


class P5_69(ProblemaScene):
    numero = "5.69"
    titulo = "Fricción de rodamiento de dos neumáticos"
    lista_datos = [
        ("Rapidez inicial:", r"v_0 = 3.50\ \mathrm{m/s}"),
        ("Neumático a 40 psi:", r"d_1 = 18.1\ \mathrm{m}"),
        ("Neumático a 105 psi:", r"d_2 = 92.9\ \mathrm{m}"),
    ]
    pasos = [
        {
            "titulo": "La rapidez se reduce a la mitad",
            "math": [
                r"\left(\dfrac{v_0}{2}\right)^2 = v_0^2 - 2ad",
                r"a = \dfrac{3v_0^2}{8d} \Rightarrow \mu_r = \dfrac{3v_0^2}{8dg}",
            ],
        },
        {
            "titulo": "Coeficiente para cada neumático",
            "math": [
                r"\mu_{r,1} = \dfrac{3(3.50)^2}{8(18.1)(9.80)} = 0.0259",
                r"\mu_{r,2} = \dfrac{3(3.50)^2}{8(92.9)(9.80)} = 0.00505",
            ],
        },
    ]
    resultado_latex = r"\mu_{r,1} = 0.0259,\qquad \mu_{r,2} = 0.00505"


class P5_71(ProblemaScene):
    numero = "5.71"
    titulo = "Masa colgante sobre plano inclinado"
    lista_datos = [
        ("Masas:", r"m_1,\ m_2"),
        ("Ángulo del plano:", r"\alpha"),
        ("Coeficientes:", r"\mu_s,\ \mu_k"),
    ]
    pasos = [
        {
            "titulo": "Subiendo con rapidez constante",
            "math": [
                r"m_2 g = m_1 g\sin\alpha + \mu_k m_1 g\cos\alpha",
                r"m_2 = m_1(\sin\alpha + \mu_k\cos\alpha)",
            ],
        },
        {
            "titulo": "Bajando con rapidez constante",
            "math": [
                r"m_2 g = m_1 g\sin\alpha - \mu_k m_1 g\cos\alpha",
                r"m_2 = m_1(\sin\alpha - \mu_k\cos\alpha)",
            ],
        },
        {
            "titulo": "Rango de m₂ para permanecer en reposo",
            "math": [r"m_1(\sin\alpha - \mu_s\cos\alpha) \le m_2 \le m_1(\sin\alpha + \mu_s\cos\alpha)"],
        },
    ]
    resultado_latex = r"m_2^{\uparrow} = m_1(\sin\alpha + \mu_k\cos\alpha),\quad m_2^{\downarrow} = m_1(\sin\alpha - \mu_k\cos\alpha)"


class P5_72(ProblemaScene):
    numero = "5.72"
    titulo = "Bloque A y peso colgante en equilibrio"
    lista_datos = [
        ("Peso del bloque A:", r"w_A = 60.0\ \mathrm{N}"),
        ("Coef. de fricción estática:", r"\mu_s = 0.25"),
        ("Peso colgante:", r"w = 12.0\ \mathrm{N}"),
        ("Ángulo de la cuerda:", r"45.0^\circ"),
    ]
    pasos = [
        {
            "titulo": "Tensión de la cuerda",
            "math": [r"T = w = 12.0\ \mathrm{N}"],
        },
        {
            "titulo": "Fuerza de fricción sobre A",
            "math": [r"f = T\cos 45^\circ = 12.0(0.707) = 8.49\ \mathrm{N}"],
            "text": ["Dirigida hacia la izquierda, opuesta al tirón."],
        },
        {
            "titulo": "Peso máximo para el equilibrio",
            "math": [
                r"w\cos 45^\circ = \mu_s(w_A - w\sin 45^\circ)",
                r"w(\cos 45^\circ + \mu_s\sin 45^\circ) = \mu_s w_A",
                r"w_{\max} = \dfrac{0.25(60.0)}{0.884} = 17.0\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"f = 8.49\ \mathrm{N},\qquad w_{\max} = 17.0\ \mathrm{N}"


class P5_75(ProblemaScene):
    numero = "5.75"
    titulo = "El salto de una pulga (lectura de gráfica)"
    lista_datos = [
        ("Masa de la pulga:", r"m = 210\ \mu\mathrm{g} = 2.10\times10^{-7}\ \mathrm{kg}"),
        ("Eje vertical de la gráfica:", r"a/g"),
    ]
    pasos = [
        {
            "titulo": "Lecturas de la gráfica a-g contra t",
            "math": [
                r"(a/g)_0 \approx 50,\quad (a/g)_{\max}\approx 145",
                r"t_{\max}\approx 1.1\ \mathrm{ms}",
            ],
        },
        {
            "titulo": "Fuerza neta inicial y máxima",
            "math": [
                r"F_0 = m a_0 = (2.10\times10^{-7})(50)(9.80) = 1.0\times10^{-4}\ \mathrm{N}",
                r"F_{\max} = (2.10\times10^{-7})(145)(9.80) = 3.0\times10^{-4}\ \mathrm{N}",
            ],
            "text": ["El peso de la pulga es solo 2.06×10⁻⁶ N."],
        },
        {
            "titulo": "Rapidez máxima = área bajo la curva",
            "math": [
                r"v_{\max} \approx \text{area} \approx (100\,g)(1.25\times10^{-3}\ \mathrm{s})",
                r"v_{\max} \approx 1.2\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"F_0 = 1.0\times10^{-4}\ \mathrm{N},\quad F_{\max} = 3.0\times10^{-4}\ \mathrm{N},\quad v_{\max} = 1.2\ \mathrm{m/s}"


class P5_76(ProblemaScene):
    numero = "5.76"
    titulo = "Cohete e instrumento colgado de un alambre"
    lista_datos = [
        ("Masa del cohete:", r"M = 25000\ \mathrm{kg}"),
        ("Peso del instrumento:", r"w_i = 15.0\ \mathrm{N}"),
        ("Tensión máxima del alambre:", r"T_{\max} = 45.0\ \mathrm{N}"),
        ("Rapidez del sonido:", r"v = 330\ \mathrm{m/s}"),
    ]
    pasos = [
        {
            "titulo": "Masa del instrumento",
            "math": [r"m_i = \dfrac{15.0}{9.80} = 1.53\ \mathrm{kg}"],
        },
        {
            "titulo": "Aceleración máxima sin romper el alambre",
            "math": [
                r"T_{\max} = m_i(g+a) \Rightarrow g+a = \dfrac{45.0}{1.53} = 29.4\ \mathrm{m/s^2}",
                r"a = 19.6\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Tiempo mínimo y empuje máximo",
            "math": [
                r"t = \dfrac{v}{a} = \dfrac{330}{19.6} = 16.8\ \mathrm{s}",
                r"F = M(g+a) = 25000(29.4) = 7.35\times10^5\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Altura al romper la barrera del sonido",
            "math": [r"h = \tfrac12 a t^2 = \tfrac12(19.6)(16.8)^2 = 2.78\times10^3\ \mathrm{m}"],
        },
    ]
    resultado_latex = r"t = 16.8\ \mathrm{s},\quad F = 7.35\times10^5\ \mathrm{N},\quad h = 2.78\times10^3\ \mathrm{m}"


class P5_80(ProblemaScene):
    numero = "5.80"
    titulo = "Martillo colgante en un autobús que acelera"
    lista_datos = [
        ("Ángulo con el techo:", r"67^\circ"),
    ]
    pasos = [
        {
            "titulo": "Ángulo con la vertical",
            "math": [r"\phi = 90^\circ - 67^\circ = 23^\circ"],
        },
        {
            "titulo": "Aceleración del autobús",
            "math": [
                r"a = g\tan\phi = (9.80)\tan 23^\circ",
                r"a = 4.16\ \mathrm{m/s^2}",
            ],
        },
    ]
    resultado_latex = r"a = 4.16\ \mathrm{m/s^2}"


class P5_81(ProblemaScene):
    numero = "5.81"
    titulo = "Caja deslizando por rampa con rondana colgante"
    lista_datos = [
        ("Inclinación de la rampa:", r"37^\circ"),
        ("Ángulo con la tapa:", r"68^\circ"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema por la rampa",
            "math": [r"a = g(\sin 37^\circ - \mu_k\cos 37^\circ)"],
        },
        {
            "titulo": "Dirección efectiva de la gravedad en la caja",
            "math": [r"\tan 68^\circ = \dfrac{g\cos 37^\circ}{g\sin 37^\circ - a}"],
        },
        {
            "titulo": "Resolver para el coeficiente",
            "math": [
                r"g\sin 37^\circ - a = g\cos 37^\circ\cot 68^\circ",
                r"\mu_k = \dfrac{g\sin 37^\circ - a}{g\cos 37^\circ} = \dfrac{3.16}{7.83}",
                r"\mu_k = 0.40",
            ],
        },
    ]
    resultado_latex = r"\mu_k = 0.40"


class P5_84(ProblemaScene):
    numero = "5.84"
    titulo = "Fracción de cuerda que puede colgar de una mesa"
    lista_datos = [
        ("Coef. de fricción estática:", r"\mu_s"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio en el borde",
            "math": [r"xw = \mu_s(1-x)w"],
            "text": ["x es la fracción de cuerda que cuelga."],
        },
        {
            "titulo": "Despejando la fracción",
            "math": [r"x(1+\mu_s) = \mu_s \Rightarrow x = \dfrac{\mu_s}{1+\mu_s}"],
        },
    ]
    resultado_latex = r"x = \dfrac{\mu_s}{1+\mu_s}"


class P5_85(ProblemaScene):
    numero = "5.85"
    titulo = "Caja sobre la plataforma de una camioneta"
    lista_datos = [
        ("Masa de la caja:", r"m = 40.0\ \mathrm{kg}"),
        ("Fricción estática:", r"\mu_s = 0.30"),
        ("Fricción cinética:", r"\mu_k = 0.20"),
        ("Aceleraciones:", r"2.20\ \mathrm{N},\ 3.40\ \mathrm{S}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración de 2.20 m/s² hacia el norte",
            "math": [
                r"f_{\mathrm{req}} = ma = (40.0)(2.20) = 88.0\ \mathrm{N}",
                r"f_{s,\max} = \mu_s mg = 0.30(40.0)(9.80) = 118\ \mathrm{N}",
            ],
            "text": ["Como 88.0 < 118, no desliza: f = 88.0 N hacia el norte."],
        },
        {
            "titulo": "Aceleración de 3.40 m/s² hacia el sur",
            "math": [r"f_{\mathrm{req}} = (40.0)(3.40) = 136\ \mathrm{N} > 118\ \mathrm{N}"],
            "text": ["La caja desliza: la fricción es cinética."],
        },
        {
            "titulo": "Fricción cinética",
            "math": [r"f_k = \mu_k mg = 0.20(40.0)(9.80) = 78.4\ \mathrm{N}"],
            "text": ["Hacia el sur, opuesta al movimiento relativo de la caja."],
        },
    ]
    resultado_latex = r"a)\ 88.0\ \mathrm{N}\ \text{al norte};\qquad b)\ 78.4\ \mathrm{N}\ \text{al sur}"


class P5_87(ProblemaScene):
    numero = "5.87"
    titulo = "Dos esferas idénticas que se tocan"
    lista_datos = [
        ("Masa de cada esfera:", r"m = 15.0\ \mathrm{kg}"),
        ("Diámetro:", r"d = 25.0\ \mathrm{cm}"),
        ("Alambres laterales:", r"35.0\ \mathrm{cm}"),
        ("Cable único:", r"18.0\ \mathrm{cm}"),
    ]
    pasos = [
        {
            "titulo": "Geometría: ángulo de cada alambre",
            "math": [
                r"\sin\phi = \dfrac{12.5}{35.0} = 0.357 \Rightarrow \phi = 20.9^\circ",
            ],
        },
        {
            "titulo": "Tensión en cada alambre lateral",
            "math": [
                r"T = \dfrac{mg}{\cos\phi} = \dfrac{(15.0)(9.80)}{\cos 20.9^\circ}",
                r"T = 157\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Tensión en el cable único",
            "math": [r"T_{\mathrm{cable}} = 2mg = 2(15.0)(9.80) = 294\ \mathrm{N}"],
        },
        {
            "titulo": "Empuje entre las esferas",
            "math": [r"N = T\sin\phi = 157(0.357) = 56.2\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"T = 157\ \mathrm{N},\quad T_{\mathrm{cable}} = 294\ \mathrm{N},\quad N = 56.2\ \mathrm{N}"


class P5_94(ProblemaScene):
    numero = "5.94"
    titulo = "Bloques A, B y C: masa máxima de C"
    lista_datos = [
        ("Masa del bloque A:", r"m_A = 8.00\ \mathrm{kg}"),
        ("Masa del bloque B:", r"m_B = 5.00\ \mathrm{kg}"),
        ("Fricción estática A-B:", r"\mu_s = 0.750"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema",
            "math": [r"a = \dfrac{m_C g}{m_A+m_B+m_C}"],
        },
        {
            "titulo": "Condición para que B no deslice",
            "math": [
                r"m_B a \le \mu_s m_B g \Rightarrow a \le \mu_s g = 7.35\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Masa máxima de C",
            "math": [
                r"m_C(9.80) \le 7.35(13.0+m_C)",
                r"m_C \le 39.0\ \mathrm{kg}",
            ],
        },
    ]
    resultado_latex = r"m_{C,\max} = 39.0\ \mathrm{kg}"


class P5_97(ProblemaScene):
    numero = "5.97"
    titulo = "Bloque contra el frente de un carrito"
    lista_datos = [
        ("Coef. de fricción estática:", r"\mu_s"),
    ]
    pasos = [
        {
            "titulo": "Fuerza normal del carrito sobre el bloque",
            "math": [r"N = ma"],
        },
        {
            "titulo": "Condición para que el bloque no caiga",
            "math": [r"\mu_s N \ge mg \Rightarrow \mu_s m a \ge mg"],
        },
        {
            "titulo": "Aceleración mínima",
            "math": [r"a \ge \dfrac{g}{\mu_s}"],
        },
    ]
    resultado_latex = r"a_{\min} = \dfrac{g}{\mu_s}"


class P5_46(ProblemaScene):
    numero = "5.46"
    titulo = "El columpio gigante de la feria"
    lista_datos = [
        ("Longitud del cable:", r"5.00\ \mathrm{m}"),
        ("Distancia del brazo al eje:", r"3.00\ \mathrm{m}"),
        ("Ángulo con la vertical:", r"30.0^\circ"),
    ]
    pasos = [
        {
            "titulo": "Radio de la trayectoria circular",
            "math": [r"R = 3.00 + 5.00\sin 30^\circ = 5.50\ \mathrm{m}"],
        },
        {
            "titulo": "Equilibrio vertical y dinámica radial",
            "math": [
                r"T\cos 30^\circ = mg",
                r"T\sin 30^\circ = m\omega^2 R",
                r"\tan 30^\circ = \dfrac{\omega^2 R}{g}",
            ],
        },
        {
            "titulo": "Periodo de una revolución",
            "math": [
                r"\omega = \sqrt{\dfrac{g\tan 30^\circ}{R}} = 1.01\ \mathrm{rad/s}",
                r"T_{\mathrm{per}} = \dfrac{2\pi}{\omega} = 6.19\ \mathrm{s}",
            ],
            "text": ["La masa no aparece: el ángulo no depende del peso del pasajero."],
        },
    ]
    resultado_latex = r"T_{\mathrm{per}} = 6.19\ \mathrm{s}"


class P5_2(ProblemaScene):
    numero = "5.2"
    titulo = "Tres arreglos de poleas en equilibrio"
    lista_datos = [("Peso de cada bloque:", r"w")]
    pasos = [
        {
            "titulo": "Caso a) cuerda anclada a la pared",
            "math": [r"T = w"],
            "text": ["La cuerda ideal transmite la misma tensión en toda su longitud."],
        },
        {
            "titulo": "Caso b) polea fija con dos pesos w",
            "math": [r"T = w"],
        },
        {
            "titulo": "Caso c) cuerda sobre dos poleas fijas",
            "math": [r"T = w"],
        },
    ]
    resultado_latex = r"a)\ T = w, \qquad b)\ T = w, \qquad c)\ T = w"


class P5_7(ProblemaScene):
    numero = "5.7"
    titulo = "Tensión en cada cuerda de un objeto suspendido"
    lista_datos = [("Peso suspendido:", r"w")]
    pasos = [
        {
            "titulo": "Caso a) cuerdas a 30° y 45°",
            "math": [
                r"T_A\cos 30^\circ = T_B\cos 45^\circ",
                r"T_A\sin 30^\circ + T_B\sin 45^\circ = w",
                r"T_A = 0.732\,w,\quad T_B = 0.897\,w",
            ],
        },
        {
            "titulo": "Caso b) cuerdas a 60° y 45°",
            "math": [
                r"T_A\cos 60^\circ = T_B\cos 45^\circ",
                r"T_A\sin 60^\circ + T_B\sin 45^\circ = w",
                r"T_A = 0.732\,w,\quad T_B = 0.518\,w",
            ],
        },
    ]
    resultado_latex = r"a)\ T_A = 0.732\,w,\ T_B = 0.897\,w;\qquad b)\ T_A = 0.732\,w,\ T_B = 0.518\,w"


class P5_9(ProblemaScene):
    numero = "5.9"
    titulo = "Piano que baja deslizándose por una rampa"
    lista_datos = [
        ("Masa del piano:", r"m = 180\ \mathrm{kg}"),
        ("Inclinación:", r"11.0^\circ"),
        ("Sin fricción", r"\text{rapidez constante}"),
    ]
    pasos = [
        {
            "titulo": "Empuje paralelo a la rampa",
            "math": [
                r"F = mg\sin 11.0^\circ = (180)(9.80)(0.1908)",
                r"F = 337\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Empuje paralelo al piso",
            "math": [
                r"F\cos 11.0^\circ = mg\sin 11.0^\circ",
                r"F = mg\tan 11.0^\circ = 343\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F_{\parallel} = 337\ \mathrm{N},\qquad F_{\mathrm{piso}} = 343\ \mathrm{N}"


class P5_10(ProblemaScene):
    numero = "5.10"
    titulo = "Sistema de cuerdas con fuerzas horizontales"
    lista_datos = [("Peso suspendido:", r"w = 60.0\ \mathrm{N}")]
    pasos = [
        {
            "titulo": "Equilibrio vertical en el nudo",
            "math": [
                r"T\sin 45^\circ = w",
                r"T = \dfrac{w}{\sin 45^\circ} = 84.9\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Fuerzas horizontales",
            "math": [
                r"F_1 = F_2 = T\cos 45^\circ = w",
                r"F_1 = F_2 = 60.0\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"T = 84.9\ \mathrm{N},\qquad F_1 = F_2 = 60.0\ \mathrm{N}"


class P5_13(ProblemaScene):
    numero = "5.13"
    titulo = "Choque de la nave Génesis"
    lista_datos = [
        ("Masa de la cápsula:", r"m = 210\ \mathrm{kg}"),
        ("Rapidez de impacto:", r"v = 311\ \mathrm{km/h} = 86.4\ \mathrm{m/s}"),
        ("Profundidad:", r"d = 81.0\ \mathrm{cm}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración durante el choque",
            "math": [
                r"a = \dfrac{v^2}{2d} = \dfrac{(86.4)^2}{2(0.810)} = 4.61\times10^3\ \mathrm{m/s^2}",
                r"a = 470\,g",
            ],
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
        },
    ]
    resultado_latex = r"a = 470\,g,\quad F = 9.67\times10^5\ \mathrm{N},\quad t = 18.8\ \mathrm{ms}"


class P5_15(ProblemaScene):
    numero = "5.15"
    titulo = "Máquina de Atwood"
    lista_datos = [
        ("Carga de ladrillos:", r"m_1 = 15.0\ \mathrm{kg}"),
        ("Contrapeso:", r"m_2 = 28.0\ \mathrm{kg}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema",
            "math": [
                r"a = \dfrac{(m_2-m_1)g}{m_1+m_2} = \dfrac{(13.0)(9.80)}{43.0}",
                r"a = 2.96\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Tensión en la cuerda",
            "math": [
                r"T = \dfrac{2m_1m_2g}{m_1+m_2} = \dfrac{2(15.0)(28.0)(9.80)}{43.0}",
                r"T = 191\ \mathrm{N}",
            ],
            "text": ["147 N < T < 274 N, entre los dos pesos."],
        },
    ]
    resultado_latex = r"a = 2.96\ \mathrm{m/s^2},\qquad T = 191\ \mathrm{N}"


class P5_17(ProblemaScene):
    numero = "5.17"
    titulo = "Bloque en mesa y masa colgante"
    lista_datos = [
        ("Masa sobre la mesa:", r"m_A = 4.00\ \mathrm{kg}"),
        ("Tensión de la cuerda:", r"T = 10.0\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del bloque sobre la mesa",
            "math": [r"a = \dfrac{T}{m_A} = \dfrac{10.0}{4.00} = 2.50\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Masa del bloque colgado",
            "math": [
                r"m(g-a) = T \Rightarrow m = \dfrac{T}{g-a}",
                r"m = \dfrac{10.0}{9.80-2.50} = 1.37\ \mathrm{kg}",
            ],
            "text": ["Su peso (13.4 N) es mayor que la tensión (10.0 N)."],
        },
    ]
    resultado_latex = r"a = 2.50\ \mathrm{m/s^2},\qquad m = 1.37\ \mathrm{kg}"


class P5_27(ProblemaScene):
    numero = "5.27"
    titulo = "Bodeguero empujando una caja"
    lista_datos = [
        ("Masa de la caja:", r"m = 11.2\ \mathrm{kg}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.20"),
        ("Rapidez constante:", r"v = 3.50\ \mathrm{m/s}"),
    ]
    pasos = [
        {
            "titulo": "Fuerza para mantener el movimiento",
            "math": [r"F = \mu_k mg = 0.20(11.2)(9.80) = 22.0\ \mathrm{N}"],
        },
        {
            "titulo": "Distancia hasta detenerse",
            "math": [
                r"a = \mu_k g = 1.96\ \mathrm{m/s^2}",
                r"d = \dfrac{v^2}{2a} = \dfrac{(3.50)^2}{2(1.96)} = 3.13\ \mathrm{m}",
            ],
        },
    ]
    resultado_latex = r"F = 22.0\ \mathrm{N},\qquad d = 3.13\ \mathrm{m}"


class P5_31(ProblemaScene):
    numero = "5.31"
    titulo = "Dos cajas bajando juntas por una rampa"
    lista_datos = [
        ("Masa inferior:", r"48.0\ \mathrm{kg}"),
        ("Masa superior:", r"32.0\ \mathrm{kg}"),
        ("Altura / base de la rampa:", r"2.50\ \mathrm{m} / 4.75\ \mathrm{m}"),
        ("Fricción rampa-caja:", r"\mu_k = 0.444"),
    ]
    pasos = [
        {
            "titulo": "Ángulo de la rampa",
            "math": [r"\theta = \arctan\dfrac{2.50}{4.75} = 27.8^\circ"],
        },
        {
            "titulo": "Fuerza aplicada (sistema completo)",
            "math": [
                r"F = (m_1+m_2)g(\sin\theta + \mu_k\cos\theta)",
                r"F = 784(0.466 + 0.393) = 673\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Fricción sobre la caja superior",
            "math": [
                r"f = m_{\mathrm{sup}}g\sin\theta = (32.0)(9.80)(0.466)",
                r"f = 146\ \mathrm{N}",
            ],
            "text": ["Hacia arriba de la rampa."],
        },
    ]
    resultado_latex = r"F = 673\ \mathrm{N},\qquad f = 146\ \mathrm{N}"


class P5_42(ProblemaScene):
    numero = "5.42"
    titulo = "Carrito en pista circular vertical"
    lista_datos = [
        ("Masa del carrito:", r"m = 0.800\ \mathrm{kg}"),
        ("Radio de la pista:", r"R = 5.00\ \mathrm{m}"),
        ("Normal en el punto alto:", r"N_B = 6.00\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "En el punto más alto (B)",
            "math": [r"N_B + mg = \dfrac{mv^2}{R}"],
        },
        {
            "titulo": "En el punto más bajo (A)",
            "math": [r"N_A - mg = \dfrac{mv^2}{R}"],
        },
        {
            "titulo": "Diferencia entre A y B",
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
    lista_datos = [
        ("Radio de la curva:", r"R = 220.0\ \mathrm{m}"),
        ("Rapidez del automóvil:", r"v = 25.0\ \mathrm{m/s}"),
    ]
    pasos = [
        {
            "titulo": "Coeficiente mínimo de fricción",
            "math": [r"\mu_s = \dfrac{v^2}{gR} = \dfrac{(25.0)^2}{(9.80)(220.0)} = 0.290"],
        },
        {
            "titulo": "Rapidez máxima sobre hielo",
            "math": [
                r"\mu = \dfrac{0.290}{3} = 0.0967",
                r"v = \sqrt{\mu g R} = \sqrt{(0.0967)(9.80)(220.0)} = 14.4\ \mathrm{m/s}",
            ],
        },
    ]
    resultado_latex = r"\mu_s = 0.290,\qquad v_{\mathrm{hielo}} = 14.4\ \mathrm{m/s}"


class P5_47(ProblemaScene):
    numero = "5.47"
    titulo = "Columpio gigante con dos cables"
    lista_datos = [
        ("Peso del asiento:", r"255\ \mathrm{N}"),
        ("Peso de la persona:", r"825\ \mathrm{N}"),
        ("Rapidez angular:", r"32.0\ \mathrm{rpm}"),
        ("Distancia al eje:", r"R = 7.50\ \mathrm{m}"),
        ("Ángulo del cable:", r"40.0^\circ"),
    ]
    pasos = [
        {
            "titulo": "Aceleración centrípeta",
            "math": [
                r"W = 1080\ \mathrm{N},\quad \omega = 32.0\ \mathrm{rpm} = 3.35\ \mathrm{rad/s}",
                r"a_c = \omega^2 R = 84.2\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Tensión en el cable inclinado",
            "math": [r"T_i\sin 40^\circ = W \Rightarrow T_i = \dfrac{1080}{\sin 40^\circ} = 1.68\ \mathrm{kN}"],
        },
        {
            "titulo": "Tensión en el cable horizontal",
            "math": [
                r"T_h + T_i\cos 40^\circ = m a_c",
                r"T_h = 9280 - 1287 = 7.99\ \mathrm{kN}",
            ],
        },
    ]
    resultado_latex = r"T_i = 1.68\ \mathrm{kN},\qquad T_h = 7.99\ \mathrm{kN}"


class P5_51(ProblemaScene):
    numero = "5.51"
    titulo = "Avión que describe un rizo vertical"
    lista_datos = [
        ("Radio del rizo:", r"R = 150\ \mathrm{m}"),
        ("Rapidez en el punto bajo:", r"280\ \mathrm{km/h}"),
        ("Peso real del piloto:", r"700\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Rapidez en el punto más alto (ingravidez)",
            "math": [
                r"mg = \dfrac{mv^2}{R} \Rightarrow v = \sqrt{gR}",
                r"v = \sqrt{(9.80)(150)} = 38.3\ \mathrm{m/s}",
            ],
        },
        {
            "titulo": "Peso aparente en el punto más bajo",
            "math": [
                r"v = 280\ \mathrm{km/h} = 77.8\ \mathrm{m/s}",
                r"N = m\left(g+\dfrac{v^2}{R}\right) = 71.4(9.80+40.3)",
                r"N = 3.58\times10^3\ \mathrm{N} = 5.11\,w",
            ],
        },
    ]
    resultado_latex = r"v_{\mathrm{alto}} = 38.3\ \mathrm{m/s},\qquad N = 3.58\times10^3\ \mathrm{N}"


class P5_57(ProblemaScene):
    numero = "5.57"
    titulo = "Dos cuerdas unidas a un cable de acero"
    lista_datos = [
        ("Ángulos con la horizontal:", r"60^\circ,\ 40^\circ"),
        ("Tensión máxima admisible:", r"5000\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio horizontal",
            "math": [r"T_1\cos 60^\circ = T_2\cos 40^\circ \Rightarrow T_2 = 0.653\,T_1"],
            "text": ["La cuerda a 60° soporta la mayor tensión."],
        },
        {
            "titulo": "Equilibrio vertical",
            "math": [
                r"T_1\sin 60^\circ + T_2\sin 40^\circ = w",
                r"T_1 = 0.778\,w,\quad T_2 = 0.508\,w",
            ],
        },
        {
            "titulo": "Peso máximo sin romper",
            "math": [r"0.778\,w \le 5000 \Rightarrow w_{\max} = 6.43\times10^3\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"T_1 = 0.778\,w > T_2,\qquad w_{\max} = 6.43\times10^3\ \mathrm{N}"


class P5_58(ProblemaScene):
    numero = "5.58"
    titulo = "Obrero levantando un peso con poleas"
    lista_datos = [("Peso levantado:", r"w")]
    pasos = [
        {
            "titulo": "Polea móvil: dos segmentos de cuerda",
            "math": [r"2T = w \Rightarrow T = \dfrac{w}{2}"],
        },
        {
            "titulo": "Fuerza aplicada por el obrero",
            "math": [r"F = T = \dfrac{w}{2}"],
        },
        {
            "titulo": "Tensión en cada cadena",
            "math": [r"T_{\mathrm{inferior}} = w,\qquad T_{\mathrm{superior}} = 2T = w"],
        },
    ]
    resultado_latex = r"F = \dfrac{w}{2},\qquad T_{\mathrm{inf}} = T_{\mathrm{sup}} = w"


class P5_59(ProblemaScene):
    numero = "5.59"
    titulo = "Esfera apoyada en una pared con alambre"
    lista_datos = [
        ("Masa de la esfera:", r"m = 45.0\ \mathrm{kg}"),
        ("Diámetro:", r"32.0\ \mathrm{cm}"),
        ("Longitud del alambre:", r"30.0\ \mathrm{cm}"),
    ]
    pasos = [
        {
            "titulo": "Geometría del alambre",
            "math": [r"\sin\theta = \dfrac{16.0}{30.0} = 0.533 \Rightarrow \theta = 32.2^\circ"],
        },
        {
            "titulo": "Tensión en el alambre",
            "math": [
                r"T\cos\theta = mg \Rightarrow T = \dfrac{(45.0)(9.80)}{\cos 32.2^\circ}",
                r"T = 521\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Empuje de la esfera sobre la pared",
            "math": [r"N = T\sin\theta = 521(0.533) = 278\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"T = 521\ \mathrm{N},\qquad N = 278\ \mathrm{N}"


class P5_68(ProblemaScene):
    numero = "5.68"
    titulo = "Bloque en rampa con masa colgante"
    lista_datos = [
        ("Masa en la rampa:", r"m_1 = 20.0\ \mathrm{kg}"),
        ("Ángulo:", r"\alpha = 53.1^\circ"),
        ("Coef. de fricción:", r"\mu_k = 0.40"),
        ("Descenso:", r"12.0\ \mathrm{m} en 3.00\ \mathrm{s}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema",
            "math": [r"a = \dfrac{2d}{t^2} = \dfrac{2(12.0)}{(3.00)^2} = 2.67\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Ecuación de movimiento",
            "math": [r"m_2 g - m_1 g\sin\alpha - \mu_k m_1 g\cos\alpha = (m_1+m_2)a"],
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


class P5_74(ProblemaScene):
    numero = "5.74"
    titulo = "Lavador de ventanas empujando el cepillo"
    lista_datos = [
        ("Peso del cepillo:", r"w = 15.0\ \mathrm{N}"),
        ("Coef. de fricción cinética:", r"\mu_k = 0.150"),
        ("Ángulo de la fuerza:", r"53.1^\circ"),
    ]
    pasos = [
        {
            "titulo": "Fuerza normal y fricción",
            "math": [r"N = F\sin 53.1^\circ,\quad f_k = \mu_k F\sin 53.1^\circ"],
        },
        {
            "titulo": "Equilibrio vertical (rapidez constante)",
            "math": [
                r"F\cos 53.1^\circ = w + f_k",
                r"F(\cos 53.1^\circ - \mu_k\sin 53.1^\circ) = w",
            ],
        },
        {
            "titulo": "Resolver la fuerza y la normal",
            "math": [
                r"F = \dfrac{15.0}{0.6004-0.1200} = 31.2\ \mathrm{N}",
                r"N = F\sin 53.1^\circ = 25.0\ \mathrm{N}",
            ],
        },
    ]
    resultado_latex = r"F = 31.2\ \mathrm{N},\qquad N = 25.0\ \mathrm{N}"


class P5_77(ProblemaScene):
    numero = "5.77"
    titulo = "Báscula en un elevador que acelera"
    lista_datos = [
        ("Masa de la persona:", r"m = 64\ \mathrm{kg}"),
        ("Rapidez:", r"v(t) = (3.0)t + (0.20)t^2"),
    ]
    pasos = [
        {
            "titulo": "Aceleración en t = 4.0 s",
            "math": [r"a = \dfrac{dv}{dt} = 3.0 + 0.40t = 4.6\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Lectura de la báscula",
            "math": [r"N = m(g+a) = 64(9.80+4.6) = 9.2\times10^2\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"N = 9.2\times10^2\ \mathrm{N}"


class P5_92(ProblemaScene):
    numero = "5.92"
    titulo = "Bloques en dos planos sin fricción"
    lista_datos = [
        ("Masa en el plano de 30.0°:", r"100\ \mathrm{kg}"),
        ("Masa en el plano de 53.1°:", r"50\ \mathrm{kg}"),
    ]
    pasos = [
        {
            "titulo": "Comparar las tendencias al deslizamiento",
            "math": [r"m_1 g\sin 30^\circ = 490\ \mathrm{N},\quad m_2 g\sin 53.1^\circ = 392\ \mathrm{N}"],
            "text": ["El bloque de 100 kg baja y el de 50 kg sube."],
        },
        {
            "titulo": "Aceleración del sistema",
            "math": [
                r"a = \dfrac{m_1 g\sin 30^\circ - m_2 g\sin 53.1^\circ}{m_1+m_2}",
                r"a = \dfrac{98.0}{150} = 0.653\ \mathrm{m/s^2}",
            ],
        },
        {
            "titulo": "Tensión en la cuerda",
            "math": [r"T = m_2(g\sin 53.1^\circ + a) = 50(7.84+0.653) = 425\ \mathrm{N}"],
        },
    ]
    resultado_latex = r"a = 0.653\ \mathrm{m/s^2},\qquad T = 425\ \mathrm{N}"


class P5_100(ProblemaScene):
    numero = "5.100"
    titulo = "Acelerómetro de plataforma"
    lista_datos = [
        ("Masa colgante:", r"m_1 = 250\ \mathrm{kg}"),
        ("Masa de la plataforma:", r"m_2 = 1250\ \mathrm{kg}"),
    ]
    pasos = [
        {
            "titulo": "Aceleración del sistema",
            "math": [r"a = \dfrac{m_1 g}{m_1+m_2} = \dfrac{(250)(9.80)}{1500} = 1.63\ \mathrm{m/s^2}"],
        },
        {
            "titulo": "Ángulo de la bola",
            "math": [r"\tan\theta = \dfrac{a}{g} \Rightarrow \theta = \arctan\dfrac{1.63}{9.80} = 9.46^\circ"],
        },
        {
            "titulo": "Ángulo máximo posible",
            "math": [r"a < g \Rightarrow \theta_{\max} = 45^\circ"],
            "text": ["Se logra haciendo m1 mucho mayor que m2."],
        },
    ]
    resultado_latex = r"\theta = 9.46^\circ,\qquad \theta_{\max} = 45^\circ"


class P5_101(ProblemaScene):
    numero = "5.101"
    titulo = "Curva peraltada I"
    lista_datos = [
        ("Radio:", r"R = 120\ \mathrm{m}"),
        ("Rapidez de diseño:", r"v_0 = 20\ \mathrm{m/s}"),
        ("Rapidez real:", r"v = 30\ \mathrm{m/s}"),
    ]
    pasos = [
        {
            "titulo": "Ángulo de peralte",
            "math": [
                r"\tan\theta = \dfrac{v_0^2}{gR} = \dfrac{(20)^2}{(9.80)(120)} = 0.340",
                r"\theta = 18.8^\circ",
            ],
        },
        {
            "titulo": "Coeficiente mínimo de fricción a 30 m/s",
            "math": [
                r"\mu_s = \dfrac{v^2/(gR) - \tan\theta}{1 + (v^2/(gR))\tan\theta}",
                r"\dfrac{v^2}{gR} = \dfrac{900}{1176} = 0.765",
                r"\mu_s = \dfrac{0.765-0.340}{1+0.260} = 0.337",
            ],
        },
    ]
    resultado_latex = r"\mu_s = 0.337"


class P5_103(ProblemaScene):
    numero = "5.103"
    titulo = "Bloques A, B y C conectados"
    lista_datos = [
        ("Peso de A y B:", r"25.0\ \mathrm{N}\ \text{cada uno}"),
        ("Coef. de fricción:", r"\mu_k = 0.35"),
        ("Rampa:", r"36.9^\circ"),
    ]
    pasos = [
        {
            "titulo": "Tensión entre A y B",
            "math": [r"T_{AB} = \mu_k w_A = 0.35(25.0) = 8.75\ \mathrm{N}"],
        },
        {
            "titulo": "Peso del bloque C",
            "math": [
                r"w_C = T_{AB} + w_B\sin 36.9^\circ + \mu_k w_B\cos 36.9^\circ",
                r"w_C = 8.75 + 15.0 + 7.00 = 30.8\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Si se corta la cuerda entre A y B",
            "math": [
                r"a = \dfrac{w_C - w_B\sin 36.9^\circ - \mu_k w_B\cos 36.9^\circ}{(w_C+w_B)/g}",
                r"a = \dfrac{8.75}{5.69} = 1.54\ \mathrm{m/s^2}",
            ],
        },
    ]
    resultado_latex = r"T_{AB} = 8.75\ \mathrm{N},\quad w_C = 30.8\ \mathrm{N},\quad a = 1.54\ \mathrm{m/s^2}"


class P5_110(ProblemaScene):
    numero = "5.110"
    titulo = "Bloque girando con dos cuerdas"
    lista_datos = [
        ("Masa del bloque:", r"m = 4.00\ \mathrm{kg}"),
        ("Cuerdas:", r"1.25\ \mathrm{m}\ \text{cada una}"),
        ("Varilla:", r"2.00\ \mathrm{m}"),
        ("Tensión superior:", r"T_1 = 80.0\ \mathrm{N}"),
    ]
    pasos = [
        {
            "titulo": "Geometría y ángulo",
            "math": [
                r"r = \sqrt{1.25^2-1.00^2} = 0.750\ \mathrm{m}",
                r"\sin\theta = \dfrac{1.00}{1.25} = 0.800,\quad \cos\theta = 0.600",
            ],
        },
        {
            "titulo": "Tensión en la cuerda inferior",
            "math": [
                r"T_1\sin\theta - T_2\sin\theta = mg",
                r"T_2 = T_1 - \dfrac{mg}{\sin\theta} = 80.0 - 49.0 = 31.0\ \mathrm{N}",
            ],
        },
        {
            "titulo": "Revoluciones por minuto",
            "math": [
                r"(T_1+T_2)\cos\theta = m\omega^2 r",
                r"\omega = 4.71\ \mathrm{rad/s} \Rightarrow 45.0\ \mathrm{rpm}",
            ],
        },
        {
            "titulo": "Cuando la cuerda inferior pierde tensión",
            "math": [
                r"T_1\sin\theta = mg \Rightarrow T_1 = 49.0\ \mathrm{N}",
                r"\omega = \sqrt{\dfrac{T_1\cos\theta}{mr}} = 3.13\ \mathrm{rad/s} \Rightarrow 29.9\ \mathrm{rpm}",
            ],
        },
    ]
    resultado_latex = r"T_2 = 31.0\ \mathrm{N},\quad 45.0\ \mathrm{rpm},\quad 29.9\ \mathrm{rpm}"


class P5_112(ProblemaScene):
    numero = "5.112"
    titulo = "Piedra lanzada hacia arriba en agua"
    lista_datos = [
        ("Rapidez terminal:", r"v_t = 2.0\ \mathrm{m/s}"),
        ("Rapidez inicial:", r"v_0 = 6.0\ \mathrm{m/s}"),
    ]
    pasos = [
        {
            "titulo": "Sin resistencia del fluido",
            "math": [
                r"h = \dfrac{v_0^2}{2g} = \dfrac{(6.0)^2}{2(9.80)} = 1.84\ \mathrm{m}",
                r"t = \dfrac{v_0}{g} = 0.612\ \mathrm{s}",
            ],
        },
        {
            "titulo": "Con resistencia del fluido",
            "math": [
                r"t = \dfrac{v_t}{g}\arctan\dfrac{v_0}{v_t} = \dfrac{2.0}{9.80}\arctan 3.0 = 0.255\ \mathrm{s}",
                r"h = \dfrac{v_t^2}{2g}\ln\!\left(1+\dfrac{v_0^2}{v_t^2}\right) = 0.470\ \mathrm{m}",
            ],
            "text": ["Ambas respuestas disminuyen por la resistencia del fluido."],
        },
    ]
    resultado_latex = r"h:\ 1.84 \to 0.470\ \mathrm{m};\qquad t:\ 0.612 \to 0.255\ \mathrm{s}"


class P5_119(ProblemaScene):
    numero = "5.119"
    titulo = "Cuenta sobre un aro giratorio"
    lista_datos = [
        ("Radio del aro:", r"R = 0.100\ \mathrm{m}"),
        ("Rotación:", r"4.00\ \mathrm{rev/s}"),
    ]
    pasos = [
        {
            "titulo": "Equilibrio en el marco giratorio",
            "math": [
                r"N\cos\beta = mg,\quad N\sin\beta = m\omega^2 R\sin\beta",
                r"\cos\beta = \dfrac{g}{\omega^2 R}",
            ],
        },
        {
            "titulo": "Ángulo a 4.00 rev/s",
            "math": [
                r"\omega = 4.00(2\pi) = 25.1\ \mathrm{rad/s}",
                r"\cos\beta = \dfrac{9.80}{(25.1)^2(0.100)} = 0.155 \Rightarrow \beta = 81.1^\circ",
            ],
        },
        {
            "titulo": "A 1.00 rev/s",
            "math": [r"\cos\beta = \dfrac{9.80}{(6.28)^2(0.100)} = 2.48 > 1"],
            "text": ["No hay solución: la cuenta permanece en el fondo del aro."],
        },
    ]
    resultado_latex = r"\beta = 81.1^\circ;\qquad \text{a }1.00\ \mathrm{rev/s}\ \text{queda en el fondo}"


class P5_127(ProblemaScene):
    numero = "5.127"
    titulo = "Esfera que oscila tras cortar una cuerda"
    lista_datos = [("Ángulo de la cuerda de soporte:", r"\beta")]
    pasos = [
        {
            "titulo": "En A (antes de cortar la cuerda horizontal)",
            "math": [r"T_A\cos\beta = mg \Rightarrow T_A = \dfrac{mg}{\cos\beta}"],
        },
        {
            "titulo": "En B (extremo de la oscilación, v = 0)",
            "math": [r"T_B = mg\cos\beta"],
        },
        {
            "titulo": "Razón entre las tensiones",
            "math": [r"\dfrac{T_B}{T_A} = \dfrac{mg\cos\beta}{mg/\cos\beta} = \cos^2\beta"],
        },
    ]
    resultado_latex = r"\dfrac{T_B}{T_A} = \cos^2\beta"
