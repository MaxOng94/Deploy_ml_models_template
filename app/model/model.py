import pathlib
import pickle
import re

__version__ = "0.1.0"

BASE_DIR= pathlib.Path(__file__).parent.absolute()

pickle_file= BASE_DIR.joinpath(f"trained_pipeline-{__version__}.pkl")

with open(pickle_file,"rb") as f:
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]