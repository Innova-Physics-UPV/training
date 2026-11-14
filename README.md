# training

Repositorio de prueba para practicar el flujo de trabajo con GitHub antes de que sea obligatorio para entregar las tareas.

## Tarea

Cada miembro abre una pull request (PR) que añade un archivo de Python que imprime `Hello World!` por consola.

- **Archivo:** tu usuario de la UPV. Por ejemplo, Marc Sanchis crea `msanlli.py`.
- **Rama y PR:** tu nombre. Por ejemplo, `marc-sanchis`.

`example.py` muestra el contenido esperado.

## Pasos

```bash
git clone https://github.com/Innova-Physics-UPV/training.git
cd training
git switch -c nombre-apellido        # crea la rama y cámbiate a ella
# crea usuario.py con: print("Hello World!")
git add usuario.py
git commit -m "Add usuario.py"
git push -u origin nombre-apellido   # sube la rama a GitHub
```

Después abre la PR en GitHub con tu nombre como título.
