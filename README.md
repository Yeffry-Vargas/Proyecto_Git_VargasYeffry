# BiblioStock - Biblioteca Comunitaria Horizonte

Sistema de inventario y préstamos por consola (CLI) en Python
Integrantes: Yeffry Vargas y Diosito

# Funcionalidades
- Registrar ítem en el inventario
- Listar ítems registrados
- Buscar ítem por título o código
- Registrar préstamo
- Registrar devolución
- Persistencia de datos en archivos JSON (inventario.json, prestamos.json)

# Comandos utilizados

| Comando | Uso en el proyecto |
| `git init` | Inicializar el repositorio local |
| `git config --global user.name/user.email` | Configurar identidad del autor de los commits |
| `git add` | Preparar archivos para el commit |
| `git commit -m "tipo: mensaje"` | Guardar cambios siguiendo Conventional Commits (feat:, fix:, docs:, chore:) |
| `git remote add origin` | Vincular el repositorio local con GitHub |
| `git push` | Subir cambios al repositorio remoto |
| `git pull` | Traer cambios actualizados desde GitHub |
| `git checkout -b` | Crear y cambiar a una nueva rama |
| `git branch` | Ver las ramas existentes |
| `git clone` | Clonar el repositorio simulando la incorporación de un nuevo usuario |
| `git status` | `git diff` | Revisar cambios pendientes antes de hacer commit|
| `git restore` | Descartar cambios locales no deseados |

# Conflicto de merge resuelto
Simule una especie de conflicto editando la misma sección del archivo `README.md` desde dos ramas distintas (`fix/actualizar-readme-v1`, creada en el repositorio local, y `fix/actualizar-readme-v2`, creada desde un clon del repositorio simulando a otro usuario). Al fusionar la segunda rama contra `main`, GitHub detectó el conflicto. Se resolvió combinando el contenido de ambas versiones directamente en el editor de conflictos de GitHub, eliminando las marcas `<<<<<<<`, `=======` y `>>>>>>>`, y confirmando la resolución con `Mark as resolved` y `Commit merge`.

# Clonación
Clone el repositorio en una carpeta separada (`Proyecto_Git_VargasYeffry_Clon`) con `git clone`, simulando la incorporación de un nuevo usuario al proyecto.

# Conclusión 
Trate de hacer mi mejor esfuerzo al realizar según los criterios o rubricas mencionados o impuestas, tratando de enfocarme sobre todo en aplicar bien el flujo del trabajo con Git  