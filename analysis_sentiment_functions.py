#pip install afinn
from afinn import Afinn
import re

def class_afinn(score: float):
    """
    Cette fonction prend en argument le score renvoyé par la fonction afinn
    et classifie le texte initial selon trois catégories: 
        - 'negative' si le score est strictement négatif
        - 'neutral' si le score est compris entre 0 et 1 inclus
        - 'positive' si le score est strictement supérieur à 1
    Argument: 
            (float) score afinn
    Return: 
            (str) classification 'negative', 'neutral' ou 'positive'
    
    """
    if score < 0:
        return 'negative'
    elif score > 1:
        return 'positive'
    else:
        return 'neutral'


def category_afinn(text: str):
    """
    Cette fonction prend en argument un texte calcule le score de la fonction afinn
    et classifie le texte initial selon trois catégories: 
        - 'negative' si le score est strictement négatif
        - 'neutral' si le score est compris entre 0 et 1 inclus
        - 'positive' si le score est strictement supérieur à 1
    Argument: 
            (str) texte
    Return: 
            (str) classification 'negative', 'neutral' ou 'positive'
    
    """
    afinn=Afinn()
    afinn_scores = afinn.score(text)
    if afinn_scores < 0:
        return 'negative'
    elif afinn_scores > 1:
        return 'positive'
    else:
        return 'neutral'
    
def maj_count(text: str):
    """
    Fonction qui compte le nombre de lettres majuscules dans un texte.
    Argument: 
            (str) text
    Return:
            (int) nombre de lettres majuscules
    """
    r = re.compile(r"[A-Z]") 
    pointeur = r.findall(text)
    return len(list(pointeur))

def maj_count2(text):
    """
    Fonction qui compte le nombre de chaînes de 2 lettres majuscules dans un texte.
    Argument: 
            (str) text
    Return:
            (int) nombre de chaînes de 2 lettres majuscules
    """
    r = re.compile(r"[A-Z]{2}") 
    pointeur = r.findall(text)
    return len(list(pointeur))

