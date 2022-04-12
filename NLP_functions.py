#pip install afinn
import pandas as pd
from afinn import Afinn
import re
from nltk.corpus  import stopwords
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
nltk.download('wordnet')
nltk.download('punkt')

def lemmatization(sentence: str):
    """
    Cette fonction lemmatise une phrase
    Argument: 
            (str) sentence
    Return: 
            (str) lemm_ouput 
    
    """
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(sentence)
    lemm_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list if w not in stopwords.words('english')])
    return lemm_output


def clean_sentence(sentence):
    """
    Cette fonction supprime les majuscules, la ponctuation et lemmatise une phrase
    Argument: 
            (str) sentence
    Return: 
            (str) lemmatized
    
    """
    lowercase = sentence.lower()
    removed=re.sub(r'[^a-z]',' ',lowercase)
    lemmatized = lemmatization(removed)
    return lemmatized

def vader_scores(text):
    """
    Cette fonction retourne les scores vader (analyse de sentiment)
    Argument: 
            (str) text
    Return: 
            (dict) {neg: score sentiment négatif entre 0 et 1,
                    neu: score sentiment neutre entre 0 et 1, 
                    pos: score sentiment négatif entre 0 et 1, 
                    compound: score composé des 3 précédents entre -1 et 1} 
    
    """
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    return vs

def vectorize(df):
    """
    Cette fonction prend un dataframe avec une colonne clean_text contenant des phrases en minuscules, sans ponctuation et lemmatisée. Compose un document avec ce corpus de phrases afin de convertir les phrase en matrices à l'aide du TfidVectorizer 
    Argument: 
            (dataframe) df contenant colonne clean_text
    Return: 
            (dataframe) df2 columns = words in corpus, lines = sentence vectorized
    
    """
    vectorizer = TfidfVectorizer()
    # ajouter une exception si colonne ne correspond pas 
    corpus = df.clean_text
    df_vect = vectorizer.fit_transform(corpus)
    features_names = vectorizer.get_feature_names()
    vect_array = df_vect.todense() # convert to nympy array
    df2 = pd.DataFrame(vect_array.tolist(), columns=features_names)
    return df2

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

