# Huertos medicinales comunitarios - Nova Alexandria - Versión 1

Aplicación web para configurar un huerto medicinal comunitario, consultar saberes ancestrales,
registrar actividades y observar plantas, puntos y niveles.

Proyecto de **Calidad de Software (ISWD652, período 2026B)**.

- EPN - 2026B
- GR1SW
- Integrantes: Domenica Astudillo, Bryan Ayala, Fernando Carrera, Guillermo Cevallos, Juan Chugá, Matthew Redin

[Enlace de la carpeta compartida de la documentación](https://epnecuador-my.sharepoint.com/:f:/r/personal/juan_chuga_epn_edu_ec/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjuan%5Fchuga%5Fepn%5Fedu%5Fec%2FDocuments%2FCalidad%20de%20Software&share=cgpAPIBlWcTlRoYB2Hgn%2DozUEgUC0pr97Omw7s%5F5ECGaECVdCA)

---

## Estado actual del proyecto

> [!WARNING]
> **Los modelos todavía no existen y ningún comando `python manage.py ...` funciona por ahora.**
> No ejecutes `migrate` hasta que se retire este aviso.

| Puedes hacer ahora | Todavía no |
|---|---|
| [3.1](#31-clonar-el-repositorio) a [3.3](#33-instalar-dependencias): clonar, crear el entorno virtual e instalar dependencias. | [3.5](#35-crear-la-base-de-datos-y-cargar-el-catálogo): `migrate` y `cargar_catalogo`. |
| [3.4](#34-clave-secreta-django_secret_key): generar y guardar tu clave secreta. | [3.6](#36-levantar-el-servidor): `runserver`. |
| Escribir en los archivos de tu tarea según el plan: datos del catálogo, plantillas, estilos, `reglas.py` y documentación. | `migrate` y `runserver` de la sección [4](#4-uso-diario). |
| | Ejecutar las pruebas de la sección [5](#5-pruebas). |

Cuando Bryan defina `Usuario` en `cuentas/models.py`, genere la primera migración de `cuentas` y la suba al repositorio (tarea B1, hito del 16 de octubre). Entonces se avisará al grupo y se retirará este aviso; a partir de ahí todos pueden continuar con la 3.5.

---

## Contenido

1. [Tecnologías y versiones](#1-tecnologías-y-versiones)
2. [Requisitos previos](#2-requisitos-previos)
3. [Instalación paso a paso](#3-instalación-paso-a-paso)
4. [Uso diario](#4-uso-diario)
5. [Pruebas](#5-pruebas)
6. [Estructura del proyecto](#6-estructura-del-proyecto)
7. [Reglas de trabajo con Git](#7-reglas-de-trabajo-con-git)
8. [Base de datos de demostración](#8-base-de-datos-de-demostración)

---

## 1. Tecnologías y versiones

| Pieza | Versión | Notas |
|---|---|---|
| Python | **3.13.14** | Todo el equipo usa el mismo parche. No se mezclan versiones menores. |
| Django | **5.2.18 (LTS)** | Fijado exactamente en `requirements.txt`. |
| Base de datos | SQLite | Incluida en Python. Transacciones `IMMEDIATE`, espera de 5 s. |
| tzdata | 2026.5 | Zona horaria `America/Guayaquil` en Windows. |
| Interfaz | Plantillas Django + Bootstrap 5.3 (local) + CSS mínimo | Sin CDN: la demo funciona sin internet. |
| Pruebas | Django `TestCase` + `manage.py test` | Un `tests.py` por aplicación. |

## 2. Requisitos previos

- Windows 10/11 con PowerShell.
- **Git** instalado (`git --version`).
- **Python 3.13.14**. Comprueba que el lanzador `py` lo encuentra:

  ```powershell
  py -0p
  py -3.13 --version
  ```

  Debe aparecer `Python 3.13.14`. Si no está instalado, descárgalo desde
  <https://www.python.org/downloads/windows/> (marca *Add python.exe to PATH*) o usa
  el administrador de instalaciones de Python con `py install 3.13`.

> Si tienes otra versión (por ejemplo 3.14) instalada, no importa: el entorno virtual se crea
> explícitamente con `py -3.13`.

## 3. Instalación paso a paso

Todos los comandos se ejecutan en **PowerShell**, dentro de la carpeta del repositorio.

### 3.1 Clonar el repositorio

```powershell
git clone <URL_DEL_REPOSITORIO> repositorio-huertos
cd repositorio-huertos
```

### 3.2 Crear y activar el entorno virtual

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

El prompt debe empezar con `(.venv)`. Comprueba:

```powershell
python --version   # Python 3.13.14
```

> Si PowerShell bloquea la activación ("la ejecución de scripts está deshabilitada"),
> habilítala solo para la terminal actual y vuelve a activar:
>
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> .\.venv\Scripts\Activate.ps1
> ```

### 3.3 Instalar dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3.4 Clave secreta (`DJANGO_SECRET_KEY`)

`huertos/settings.py` lee la clave de la variable de entorno `DJANGO_SECRET_KEY`.
**Cada integrante genera su propia clave local, la conserva y nunca la sube a Git.**
Esto se hace **una sola vez** por computador y **antes de `migrate`**.

```powershell
# 1. Generar la clave
$clave = python -c "import secrets; print(secrets.token_urlsafe(50))"

# 2. Guardarla de forma permanente para tu usuario de Windows (sobrevive reinicios)
setx DJANGO_SECRET_KEY $clave

# 3. Cargarla también en la terminal actual (setx solo afecta a terminales nuevas)
$env:DJANGO_SECRET_KEY = $clave
```

Comprueba que está definida (en una terminal nueva):

```powershell
echo $env:DJANGO_SECRET_KEY
```

> No cambies la clave después de crear datos: las sesiones iniciadas dejarían de ser válidas.

### 3.5 Crear la base de datos y cargar el catálogo

> [!WARNING]
> Todavía no disponible. Ver [Estado actual del proyecto](#estado-actual-del-proyecto).

```powershell
python manage.py migrate
python manage.py cargar_catalogo
```

`cargar_catalogo` crea las 18 plantas, 13 guías, opciones, materiales y eventos lunares.
Se puede ejecutar varias veces: no duplica registros ni borra actividades, pertenencias o
nombramientos.

### 3.6 Levantar el servidor

> [!WARNING]
> Todavía no disponible. Ver [Estado actual del proyecto](#estado-actual-del-proyecto).

```powershell
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/cuentas/> en el navegador. Detener con `Ctrl + C`.

## 4. Uso diario

> [!WARNING]
> Por ahora solo funcionan la activación del entorno, `git pull` y `pip install`; `migrate` y
> `runserver` todavía no. Ver [Estado actual del proyecto](#estado-actual-del-proyecto).

Cada vez que abras una terminal nueva para trabajar:

```powershell
cd repositorio-huertos
.\.venv\Scripts\Activate.ps1
git pull
python -m pip install -r requirements.txt   # solo si cambió requirements.txt
python manage.py migrate                    # solo si alguien subió migraciones nuevas
python manage.py runserver
```

### Variables de entorno disponibles

| Variable | Obligatoria | Valor por defecto | Uso |
|---|---|---|---|
| `DJANGO_SECRET_KEY` | Sí | — | Clave secreta local (sección 3.4). |
| `DJANGO_DEBUG` | No | `1` | `0` desactiva el modo depuración. |
| `DJANGO_ALLOWED_HOSTS` | No | vacío | Hosts extra separados por comas (por ejemplo, tu IP local). |

## 5. Pruebas

> [!WARNING]
> Todavía no disponible. Ver [Estado actual del proyecto](#estado-actual-del-proyecto).

```powershell
python manage.py test                 # todas las aplicaciones
python manage.py test actividades     # una sola aplicación
python manage.py test -v 2            # salida detallada
```

Las pruebas usan una base temporal; no modifican `db.sqlite3`.
Los casos manuales (CP-01 a CP-10) y sus resultados reales se registran en
[`docs/v1/resultados.md`](docs/v1/resultados.md).

## 6. Estructura del proyecto

```
repositorio-huertos/
|-- manage.py; requirements.txt; README.md; .gitignore
|-- huertos/                 # settings.py, urls.py, wsgi.py, asgi.py
|-- cuentas/                 # models, forms, servicios, views, urls, tests
|-- catalogo/                # models, servicios, views, urls, tests
|   |-- datos/               # fichas, guías, opciones, materiales y luna (Python)
|   `-- management/commands/cargar_catalogo.py
|-- comunidades/             # models, forms, servicios, views, urls, tests
|-- actividades/             # models, forms, servicios, views, urls, tests
|   `-- reglas.py            # nivel y porcentaje sin consultas
|-- templates/               # base.html, componentes/ y una carpeta por módulo
|-- static/                  # vendor/bootstrap/, css/estilos.css, img/plantas/
`-- docs/v1/                 # alcance, arquitectura, plan, diseño, resultados, demo, informe
```

Dependencias entre módulos: `catalogo` no depende de nadie; `comunidades` usa `cuentas` y
`catalogo`; `actividades` usa los tres anteriores. **Los módulos inferiores no importan
`actividades`.** Las reglas del dominio van en `servicios.py`; las vistas solo coordinan
petición y respuesta.

### Bootstrap local

Bootstrap 5.3 se guarda en el repositorio para que la demo funcione sin internet. Se agrega una
sola vez (Doménica) y el resto lo recibe con `git pull`:

1. Descargar *Compiled CSS and JS* de <https://getbootstrap.com/docs/5.3/getting-started/download/>.
2. Copiar `css/bootstrap.min.css` y `js/bootstrap.bundle.min.js` a `static/vendor/bootstrap/`.

## 7. Reglas de trabajo con Git

- Una **rama por funcionalidad** o cambio coherente: `git checkout -b feature/registro-actividad`.
- **Nunca** se suben: `.venv/`, `db.sqlite3`, copias de la base de demo, claves ni archivos `.env`
  (ya están en `.gitignore`).
- Cada cambio de modelo incluye **su migración**. Los cambios de modelos y migraciones se
  coordinan con el responsable del módulo antes de integrarlos.
- `AUTH_USER_MODEL = 'cuentas.Usuario'` debe existir **antes de la primera migración**. No
  ejecutes `migrate` hasta que `cuentas/models.py` defina `Usuario`.
- Para cambios que afecten modelos compartidos, servicios, permisos o contratos entre módulos,
  se pide una revisión breve antes de integrar.
- Si `requirements.txt` cambia, avisa al grupo. Para fijar una dependencia nueva:
  `python -m pip install <paquete>` y luego `python -m pip freeze > requirements.txt`.

| Archivo o carpeta | Coordina |
|---|---|
| `huertos/`, `cuentas/`, `requirements.txt` | Bryan |
| `catalogo/` | Matthew |
| `comunidades/` | Bryan (materiales: Juan) |
| `actividades/` | Fernando (`reglas.py`: Guillermo) |
| `templates/`, `static/`, `docs/v1/diseno/` | Doménica |
| `docs/v1/resultados.md`, `docs/v1/demo.md` | Guillermo / Juan |
| `README.md`, `docs/v1/informe.docx` | Juan |

## 8. Base de datos de demostración

La base ficticia (ciclo avanzado y dos comunidades) se prepara con el producto o con
`python manage.py shell` y se guarda **fuera de Git**. Para usarla en el ensayo o la demo:

```powershell
# Respaldar tu base de trabajo
Copy-Item db.sqlite3 db_trabajo.sqlite3

# Usar la copia de demo
Copy-Item <ruta>\db_demo.sqlite3 db.sqlite3 -Force
python manage.py runserver
```

El guion de la demo está en [`docs/v1/demo.md`](docs/v1/demo.md).
