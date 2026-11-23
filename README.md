# Clasificación supervisada de tumores mamarios con aprendizaje automático

Proyecto académico de clasificación binaria con el conjunto **Breast Cancer Wisconsin (Diagnostic)**. Se comparan tres clasificadores solicitados en la actividad —Gaussian Naive Bayes, Support Vector Machine (SVM) y un perceptrón multicapa (MLP)— frente a un modelo de referencia de regresión logística.

El proyecto cubre exploración, preparación, entrenamiento, ajuste con validación cruzada, evaluación, análisis de errores y comunicación de resultados.
## 1. Dataset

Fuente: [UCI Machine Learning Repository — Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast-cancer-wisconsin-diagnostic), DOI: [10.24432/C5DW2B](https://doi.org/10.24432/C5DW2B).

El conjunto utilizado contiene 569 muestras: 357 benignas y 212 malignas; 30 variables numéricas y la etiqueta `Diagnosis`. Las 30 variables describen diez características de los núcleos celulares (radio, textura, perímetro, área, suavidad, compacidad, concavidad, puntos cóncavos, simetría y dimensión fractal), resumidas como media, error estándar y peor valor. La columna `ID` se conserva únicamente como metadato para rastrear errores; no se utiliza como predictor.

Codificación de la variable objetivo: `B = 0` (benigno) y `M = 1` (maligno).

El CSV utilizado ya está incluido en `data/raw/breast_cancer_wisconsin.csv`; no es necesario descargarlo por separado.

## 2. Estructura del proyecto

```text
proyecto_data_scients/
├── data/
│   ├── raw/
│   │   └── breast_cancer_wisconsin.csv
│   └── processed/
│       ├── X_train.csv
│       ├── X_val.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_val.csv
│       ├── y_test.csv
│       └── test_metadata.csv
├── models/
│   ├── regresion_logistica.joblib
│   ├── gaussian_naive_bayes.joblib
│   ├── svm.joblib
│   └── mlp.joblib
├── notebooks/
│   ├── 01_Analisis_Exploratorio.ipynb
│   ├── 02_Preprocesamiento.ipynb
│   └── 03_Modelos.ipynb
├── reports/
│   ├── figures/
│   │   ├── figura_1_distribucion_diagnosticos.png
│   │   ├── figura_2_histograma_radius1.png
│   │   ├── figura_3_matriz_correlaciones.png
│   │   ├── figura_4_comparacion_curvas_roc.png
│   │   ├── figura_5_matrices_confusion.png
│   │   ├── figura_6_precision_recall_test.png
│   │   ├── figura_7_matrices_confusion_test.png
│   │   ├── figura_8_f1_validacion_cruzada.png
│   │   └── figura_9_metricas_test.png
│   ├── comparacion_modelos_validacion_cruzada.csv
│   ├── resultados_evaluacion_test.csv
│   ├── resultados_precision_recall.csv
│   ├── resumen_errores_test.csv
│   └── analisis_errores_test.csv
├── paper_ieee.pdf
├── paper_ieee.tex
├── presentacion_resultados.pptx
├── presentacion_resultados.pdf
├── LISTA_VERIFICACION_ENTREGA.md
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

Las carpetas `data/processed`, `models`, `reports` y `reports/figures` contienen resultados generados durante el flujo de trabajo. Se incluyen en el repositorio para facilitar la consulta y la reproducción.

## 3. Requisitos previos

- Python **3.12.10** (versión utilizada para desarrollar y probar el proyecto).
- Visual Studio Code.
- Extensiones **Python** y **Jupyter** de Visual Studio Code.

Las dependencias de Python están fijadas en `requirements.txt`.

## 4. Instalación del proyecto

### 4.1. Obtener el código

Se puede descargar el ZIP del repositorio desde GitHub o clonarlo desde una terminal:

```bash
git clone https://github.com/Diego1012Bv/proyecto_data_scients.git
cd proyecto_data_scients
```

### 4.2. Crear y activar el entorno virtual en Windows PowerShell

Ejecutar estos comandos desde la carpeta raíz del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4.3. Instalar las dependencias

Con el entorno `.venv` activado:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
```

### 4.4. Seleccionar el intérprete y kernel en Visual Studio Code

1. Abrir la carpeta raíz del proyecto en Visual Studio Code.
2. Abrir la paleta de comandos (`Ctrl+Shift+P`) y seleccionar **Python: Select Interpreter**.
3. Elegir el intérprete ubicado en `.venv`.
4. Abrir un notebook `.ipynb` y, en el selector de kernel de la esquina superior derecha, elegir el entorno `.venv`.

## 5. Instrucciones de ejecución

**Ejecutar los tres notebooks en el orden indicado.** Antes de empezar, confirmar que el entorno `.venv` está seleccionado como intérprete y kernel en Visual Studio Code. Los notebooks localizan `config.py` buscando en la carpeta actual y sus carpetas superiores; por eso se recomienda abrir la carpeta raíz completa del proyecto, no únicamente la carpeta `notebooks`.

### Paso 1. Análisis exploratorio

Abrir `notebooks/01_Analisis_Exploratorio.ipynb` y seleccionar **Run All** (Ejecutar todo).

Este notebook:

- Lee `data/raw/breast_cancer_wisconsin.csv`.
- Inspecciona dimensiones, tipos de datos, valores faltantes, duplicados y distribución de las clases.
- Genera e interpreta las gráficas exploratorias.
- Guarda las figuras 1, 2 y 3 en `reports/figures/`.

### Paso 2. Preparación de los datos

Cuando termine el primer notebook, abrir `notebooks/02_Preprocesamiento.ipynb` y seleccionar **Run All**.

Este notebook:

- Carga el CSV original desde `data/raw/`.
- Separa las 30 variables predictoras (`X`) de la etiqueta (`y`); `ID` no se incluye en `X`.
- Codifica `B = 0` y `M = 1`.
- Divide los registros de forma estratificada en 70% entrenamiento, 15% validación y 15% prueba, utilizando `RANDOM_STATE = 42`.
- Guarda `X_train.csv`, `X_val.csv`, `X_test.csv`, `y_train.csv`, `y_val.csv`, `y_test.csv` y `test_metadata.csv` en `data/processed/`.
- Comprueba dimensiones, distribución de clases, identificadores únicos y que no haya registros compartidos entre las particiones.

El notebook compara la partición de prueba nueva con los archivos procesados que ya existan para evitar cambiar silenciosamente los registros evaluados anteriormente. **Si se modifica intencionalmente el dataset o `RANDOM_STATE` para crear una partición distinta**, primero se debe respaldar y retirar el contenido anterior de `data/processed/`; después se ejecuta de nuevo este notebook y se vuelve a ejecutar el entrenamiento y la evaluación.

### Paso 3. Entrenamiento y evaluación de modelos

Después de completar el segundo notebook, abrir `notebooks/03_Modelos.ipynb` y seleccionar **Run All**.

Este notebook:

- Carga las seis particiones y los metadatos desde `data/processed/`; no vuelve a dividir el dataset original.
- Evalúa la regresión logística de referencia mediante validación cruzada estratificada de cinco pliegues.
- Ejecuta `GridSearchCV` para Gaussian Naive Bayes, SVM y MLP, seleccionando la configuración según F1.
- Calcula métricas en validación y prueba: accuracy, precision, recall, F1 y ROC-AUC.
- Genera curvas ROC, curvas Precision-Recall, matrices de confusión, tablas comparativas y análisis de errores.
- Guarda los modelos finales en `models/`, las tablas CSV en `reports/` y las figuras en `reports/figures/`.

## 6. Modelos e hiperparámetros

- **Regresión logística:** modelo de referencia con `StandardScaler` y `max_iter=2000`.
- **Gaussian Naive Bayes:** búsqueda de `var_smoothing` entre `10^-12` y `10^-6`.
- **SVM:** se prueban los kernels lineal y RBF; `C` en `{0.1, 1, 10, 100}` y `gamma` en `{scale, auto, 0.001, 0.01, 0.1}` para RBF. `StandardScaler` se encuentra dentro del pipeline.
- **MLP:** capas ocultas `(32,)`, `(64,)` y `(64, 32)`; activaciones `relu` y `tanh`; `alpha` en `{0.0001, 0.001}`; tasa de aprendizaje inicial en `{0.001, 0.01}`; máximo de 2000 iteraciones y detención temprana (`early_stopping=True`, `validation_fraction=0.10`, `n_iter_no_change=20`). `StandardScaler` se encuentra dentro del pipeline.

Las búsquedas de hiperparámetros utilizan validación cruzada estratificada de cinco pliegues y `refit="f1"`. La selección de hiperparámetros se realiza con los datos de entrenamiento; el conjunto de prueba se conserva para la evaluación final.

