from pathlib import Path

# Ruta raíz del proyecto, independiente del directorio de trabajo.
ROOT_DIR = Path(__file__).resolve().parent

# Directorios de datos.
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Directorios de modelos y reportes.
MODELS_DIR = ROOT_DIR / "models"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Dataset elegido.
DATASET_ID = 17
DATASET_NAME = "Breast Cancer Wisconsin (Diagnostic)"
TARGET = "Diagnosis"

# Semilla de reproducibilidad.
RANDOM_STATE = 42
