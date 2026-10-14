# kimera-python

> *Archived. A Python monorepo of five small packages (core tools, databases, data, cloud and sample apps) written in 2020–2022.*

> **Archivado.** Monorepo de Python con cinco paquetes pequeños escritos entre 2020 y 2022: utilidades
> base, bases de datos, datos, nube y aplicaciones de ejemplo. Se conserva en modo lectura como referencia.

Forma parte de [kimera-tools](https://github.com/kimera-tools), el código abierto de Ismael Sarmiento.

## Paquetes

| Paquete | Versión | Qué hace |
|---|---|---|
| [`kimera-core`](kimera-core) | 0.0.13 | Utilidades base: extractores, cargadores y transformadores en crudo (ZIP, JSON), cachés locales y remotas (en memoria, por hilo, Memcached, Redis), serializadores, hash MD5, pool de hilos, logger y utilidades genéricas |
| [`kimera-db`](kimera-db) | 0.0.4 | Bases de datos con SQLAlchemy (Core y ORM) y generación de SQL a partir de ficheros de datos |
| [`kimera-data`](kimera-data) | 0.0.1 | ETL sobre Pandas: extractores, transformadores (auditoría y prelación de datos) y cargadores |
| [`kimera-cloud`](kimera-cloud) | 0.0.1 | AWS: sesión y almacenamiento en S3 con boto3 |
| [`kimera-app`](kimera-app) | 0.0.1 | Aplicaciones de ejemplo que combinan los paquetes anteriores |

## Estado verificado (octubre de 2026)

| Paquete | Tests | Resultado |
|---|---|---|
| kimera-core | 45 tests unitarios | Pasan con Python 3.11 |
| kimera-db | 5 tests (unitarios e integración con SQLite) | Pasan con Python 3.10. En 3.11+ falla una dependencia de `ddlgenerator` |
| kimera-cloud | 2 tests con S3 simulado | Pasan con Python 3.11 |
| kimera-data | Sin tests | Todos sus módulos se importan correctamente |
| kimera-app | Sin tests | 4 ejemplos ETL usan una API anterior de kimera-data y ya no funcionan |

Los paquetes se escribieron para Python 3.6–3.8, como indica su `tox.ini`.

## Ejecutar los tests

Cada paquete se prueba desde su carpeta:

```bash
cd kimera-core
pip install -r requirements.txt
python -m unittest discover
```

o con `tox` para generar además el informe de cobertura.

## Ramas

- `main`: versión estable.
- `develop`: rama de desarrollo.
- `feature/kimera-core`: línea antigua de 2021, conservada como histórico. Lo que aportaba
  (`RawJsonExtractor`, `NumberUtils` y `DictUtils`) ya está en `develop` y `main`.

## Licencia

[MIT](LICENSE)
