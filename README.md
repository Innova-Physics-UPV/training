# training

Repositorio de prueba para practicar el flujo de trabajo con GitHub antes de que sea obligatorio para entregar las tareas.

## Tarea

Cada miembro abre una pull request (PR) que añade un archivo de Python que imprime `Hello World!` por consola.

- **Archivo:** tu usuario de la UPV. Por ejemplo, Marc Sanchis crea `msanlli.py`.
- **Rama y PR:** tu nombre en minúsculas, sin tildes ni ñ, con guiones. Por ejemplo, `marc-sanchis`.

`example.py` muestra el contenido esperado.

Cada PR pasa unos checks automáticos (GitHub Actions) que comprueban el nombre del archivo, el de la rama y que el script imprima exactamente `Hello World!`. Para hacer merge hacen falta los checks en verde, la aprobación de alguien de dirección y que todos los commits estén firmados.

## Firmar commits (obligatorio)

En la organización todos los commits deben estar firmados: GitHub no deja hacer merge de una PR con commits sin firmar. Se configura una sola vez por ordenador. Hace falta git 2.34 o posterior (`git --version`). En Windows, usa Git Bash para estos comandos.

```bash
# 1. Crea una clave SSH si no tienes (pulsa Enter para aceptar la ruta por defecto)
ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"

# 2. Dile a git que firme siempre con esa clave
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true

# 3. Usa un email verificado en tu cuenta de GitHub, o la firma saldrá "Unverified"
git config --global user.email "tu-email@ejemplo.com"
```

4. Copia la clave pública (`cat ~/.ssh/id_ed25519.pub`) y añádela en GitHub › Settings › SSH and GPG keys › **New SSH key**, eligiendo **Key type: Signing Key**. Si ya usas esa clave para conectarte, añádela otra vez como Signing Key.

Comprueba en tu PR que tus commits aparecen como **Verified**. Si ya hiciste un commit sin firmar, fírmalo y vuelve a subir tu rama:

```bash
git commit --amend --no-edit -S
git push --force-with-lease
```

Usa `--force-with-lease` solo en tu propia rama, nunca en `main`.

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
