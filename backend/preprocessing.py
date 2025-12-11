"""
COMPLETE DATA PREPROCESSING PIPELINE
Meets: "Data preprocessing: Text cleaning, tokenization, normalization"
"""

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

class RecipePreprocessor:
    """Complete NLP preprocessing pipeline for recipes"""
    
    def __init__(self):
        
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
        
        self.measurement_patterns = [
            r'\d+\s*(tbsp|tsp|cup|cups|oz|g|kg|ml|l|pound|lb)',
            r'\d+\s*(slice|slices|piece|pieces)',
            r'\d+-\d+\s*\w+'
        ]
    
    def clean_text(self, text: str) -> str:
        """Text cleaning: remove special chars, normalize"""
        # Lowercase
        text = text.lower()
        
       
        for pattern in self.measurement_patterns:
            text = re.sub(pattern, ' ', text)
        
        
        text = re.sub(r'[^\w\s]', ' ', text)
        
        
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize(self, text: str) -> list:
        """Tokenization into words"""
        return word_tokenize(text)
    
    def remove_stopwords(self, tokens: list) -> list:
        """Remove common stopwords"""
        return [token for token in tokens if token not in self.stop_words]
    
    def lemmatize(self, tokens: list) -> list:
        """Lemmatization: reduce words to base form"""
        return [self.lemmatizer.lemmatize(token) for token in tokens]
    
    def full_pipeline(self, text: str) -> str:
        """
        COMPLETE NLP PREPROCESSING PIPELINE
        Returns cleaned text ready for transformer
        """
       
        cleaned = self.clean_text(text)
        
      
        tokens = self.tokenize(cleaned)
        
       
        filtered = self.remove_stopwords(tokens)
        
       
        lemmatized = self.lemmatize(filtered)
        
        
        return ' '.join(lemmatized)