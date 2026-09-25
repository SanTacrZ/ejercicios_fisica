# ejercicios_fisica

Ejercicios de física mecánica (Sears-Zemansky) resueltos paso a paso en
[Manim](https://www.manim.community/), con diagramas que se construyen
como lo haría un profesor en el tablero: diagrama de cuerpo libre,
descomposición de vectores y, de ahí, las ecuaciones.

## Estructura

- `fisica_base.py` — motor visual reutilizable (`ProblemaScene`, `Figura`)
  y escenas demo (`DemoRampa`, `DemoGrafica`).
- `cap5_visual.py` — Capítulo 5, edición visual paso a paso.
- `cap5_leyes_newton.py` — Capítulo 5, edición solo ecuaciones (legado).
- `torque_animation.py` — clase visual de torque.

## Renderizar

```bash
manim -ql fisica_base.py DemoRampa        # 480p, rápido
manim -qh cap5_visual.py P5_7             # 1080p 60fps, final
manim -ql cap5_visual.py                  # todo el archivo
```

Los videos generados (`media/`) y los PDF/imágenes fuente no se versionan.
