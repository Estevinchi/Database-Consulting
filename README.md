![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![Architecture](https://img.shields.io/badge/Architecture-MVC-success)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-purple)
![Auth](https://img.shields.io/badge/Auth-Login%20System-red)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# Database Consulting App

Proyecto desarrollado para una escuela/academia que necesitaba una forma más eficiente, moderna y profesional de consultar y gestionar su base de datos.

Esta aplicación web permite a administradores y usuarios consultar y gestionar datos de alumnos de manera rápida, organizada y segura.

## 🚀 Cómo ejecutarlo

> Username: Test Password: Test

1️⃣ Ejecutarlo localmente

Clonar el repositorio:

```git clone https://github.com/Estevinchi/Database-Consulting.git```


Instalar dependencias:

```pip install -r requirements.txt```


Ejecutar la aplicación:

```py wsgi.py```


Abrir en el navegador:

> http://localhost:5000

2️⃣ Desde Railway

> [Enlace Railway Database](https://database-consulting-production.up.railway.app/auth/)
> User: Test Password: test


## 🗄️ Organización

<details>
  <summary>📂 Ver estructura del proyecto</summary>
  
```  
Database-Consulting/
├── app/
│   ├── controllers/
│   ├── models/
│   │   └── entities/
│   ├── routes/
│   ├── services/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── admin/
├── data/
│   └── Excels/
├── wsgi.py
├── requirements.txt
└── README.md
```

</details>

El proyecto sigue una arquitectura modular basada en Flask, separando la lógica de negocio, rutas y servicios para facilitar el mantenimiento y la escalabilidad.

# 🚀 Funcionalidades principales

>👨‍💼 Rol Administrador

Crear usuarios

Modificar usuarios

Eliminar usuarios

Cargar archivos Excel para actualizar la base de datos principal

Gestión completa del sistema

Cambio de contraseña

>👤 Rol Usuario

Iniciar sesión con usuario y contraseña

Ver los primeros 10 alumnos de la base de datos

Formulario de filtrado por cualquier columna disponible

Ordenación de la tabla:

· Por fecha (predeterminado)

· Por apellidos

Exportación de la consulta

## 📦 Estado del proyecto

🟢 Proyecto finalizado y operativo (versión inicial).

🔧 Mejoras previstas:
- Migración de la base de datos
- Adaptación responsive (dispositivos móviles)
- Panel de administración para la gestión de la base de datos
- Modo oscuro
- Modificar idioma

## 🎯 Objetivo del proyecto

Desarrollado inicialmente para una empresa concreta, pero preparado para ser publicado en el portfolio profesional sin incluir información sensible.

## 👥 Autores

Esteve Romero

Alejandro Zapata

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.
Consulta el archivo LICENSE para más detalles.

