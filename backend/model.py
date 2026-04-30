import os
import pickle

MODEL_PATH = "hybrid.pkl"

_model = None


def load_model_from_disk():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"{MODEL_PATH} not found in current directory"
        )

    print(f"Loading model from {MODEL_PATH}...")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    print("Model loaded successfully")
    return model


def get_model():
    global _model

    if _model is None:
        _model = load_model_from_disk()

    return _model


