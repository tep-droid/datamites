import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

sample_text = "Natural Language Processing, or NLP, is a fascinating field of artificial intelligence that allows machines to understand, interpret, and generate human language. Many companies use NLP to analyze customer feedback, improve chatbots, and automate content creation."

# data cleaning
# replacing patterns with empty spaces
def clean_data(sample_text):
    text = sample_text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9 ,.-]', '', text)
    #print(text)
    return(text)

# tokenisation
nltk.download('punkt_tab')

def tokenize_data(text):
    tokens = word_tokenize(text)
    return(tokens)

# stopwords
nltk.download('stopwords')

def rem_stopwords(tokens):
    stop_words = set(stopwords.words("english"))
    filtered_data = [word for word in tokens if word not in stop_words]
    #print(filtered_data)
    return(filtered_data)


#lemmatising
nltk.download('wordnet')

def lemma(filtered_data):
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in filtered_data]
    #print(lemmas)
    return(lemmas)


#normalisation
def normalisation(lemmas):
    skill_map = {
        'python': 'Python',
        'java': 'Java',
        'nodejs': 'Node.js',
        'spring_boot': 'Spring Boot',
        'django': 'Django',
        'mysql': 'MySQL',
        'postgresql': 'PostgreSQL',
        'mongodb': 'MongoDB',
        'aws': 'AWS',
        'docker': 'Docker',
        'git': 'Git',
        'rest': 'REST API'
    }

    normalised_skill_set = [skill_map[word]for word in lemmas if word in skill_map]
    #print(normalised_skill_set)
    return(normalised_skill_set)
