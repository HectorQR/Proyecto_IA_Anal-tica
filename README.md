# PREDI-RENTA: Sistema Predictivo de Rentabilidad

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/UPC_logo_transparente.png" alt="Logo UPC" />
</p>



Este proyecto utiliza técnicas de Inteligencia Artificial y modelos de Machine Learning para predecir la rentabilidad y viabilidad de tiendas comerciales. La aplicación permite cargar datos sobre el desempeño de una tienda para obtener predicciones precisas que apoyen la toma de decisiones estratégicas.

## Características principales

- **Carga de datos**: Los usuarios pueden cargar un archivo CSV con datos como área de la tienda, inventario disponible, número de clientes diarios y ventas mensuales.
- **Modelos predictivos avanzados**: Uso de Random Forest Regressor para capturar relaciones no lineales y mejorar la precisión de las predicciones.
- **Variables derivadas**: Implementación de nuevas características, como artículos por cliente y ventas por artículo, para enriquecer el análisis.
- **Interfaz amigable**: Una aplicación web fácil de usar que incluye funcionalidad de inicio de sesión y un historial de predicciones.

## Dataset

El proyecto utiliza el conjunto de datos "Supermarket Store Branches Sales Analysis" disponible en Kaggle, el cual incluye información de más de 800 sucursales de supermercados.

[Link al dataset]([https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data](https://www.kaggle.com/datasets/surajjha101/stores-area-and-sales-data))

## Cómo usar

1. **Preparar el entorno**:
   - Instalar Python 3.7 o superior.
   - Instalar las dependencias listadas en `requirements.txt`.

2. **Ejecutar la aplicación**:
   - Clonar este repositorio.
   - Ejecutar el archivo `app.py` para iniciar el servidor local.

3. **Subir datos y obtener predicciones**:
   - Subir un archivo CSV con el formato requerido.
   - Visualizar las predicciones generadas por el modelo.

## Tecnologías utilizadas

- **Lenguajes y herramientas**: Python, Flask, HTML/CSS, Scikit-learn, Pandas.
- **Modelo de Machine Learning**: Random Forest Regressor.
- **Análisis de datos**: Pandas, Matplotlib, Seaborn.

## Colaboradores

- **Jhonny Elias Ruiz Santos** - [@JhonnyRuiz](https://github.com/jhonnyE20)
- **Hector Jesus Quintana Robatti** - [@HectorQuintana](https://github.com/HectorQR)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE.txt) para más detalles.
