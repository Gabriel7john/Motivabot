import random
import pyttsx3

FRASES = [
    "Um passo de cada vez, mas não pare.",
    "Hoje é um ótimo dia para evoluir.",
    "Disciplina vence motivação.",
    "Todo código bonito começou com um bug.",
]

engine = pyttsx3.init()
engine.setProperty("rate", 150)  # velocidade da fala
engine.say(f"Bom dia, Gabriel! {random.choice(FRASES)}")
engine.runAndWait()