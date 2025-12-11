"""
Text Processing Utilities
Clean, normalize, and extract keywords from text
"""

import re
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Initialize stopwords
STOP_WORDS = set(stopwords.words('english'))

# Add custom stopwords for resumes
CUSTOM_STOP_WORDS = {
    'resume', 'cv', 'curriculum', 'vitae', 'page', 'pages',
    'name', 'address', 'phone', 'email', 'linkedin', 'github'
}
STOP_WORDS.update(CUSTOM_STOP_WORDS)

def clean_text(text: str) -> str:
    """
    Clean and normalize text
    
    Args:
        text: Raw text
        
    Returns:
        Cleaned text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove phone numbers
    text = re.sub(r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '', text)
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

def extract_keywords(text: str, top_n: int = 50) -> list:
    """
    Extract important keywords from text
    
    Args:
        text: Input text
        top_n: Number of top keywords to return
        
    Returns:
        List of keywords sorted by frequency
    """
    # Tokenize
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and short words
    keywords = [
        word for word in tokens 
        if word not in STOP_WORDS 
        and len(word) > 2
        and word.isalpha()
    ]
    
    # Count frequencies
    word_freq = Counter(keywords)
    
    # Get top keywords
    top_keywords = [word for word, freq in word_freq.most_common(top_n)]
    
    return top_keywords

def extract_bigrams(text: str, top_n: int = 20) -> list:
    """
    Extract important two-word phrases
    
    Args:
        text: Input text
        top_n: Number of top bigrams to return
        
    Returns:
        List of bigrams
    """
    # Tokenize
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in STOP_WORDS and word.isalpha()]
    
    # Create bigrams
    bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
    
    # Count frequencies
    bigram_freq = Counter(bigrams)
    
    # Get top bigrams
    top_bigrams = [bigram for bigram, freq in bigram_freq.most_common(top_n)]
    
    return top_bigrams

def calculate_keyword_density(text: str, keyword: str) -> float:
    """
    Calculate density of a keyword in text
    
    Args:
        text: Input text
        keyword: Keyword to check
        
    Returns:
        Density as percentage
    """
    text_lower = text.lower()
    keyword_lower = keyword.lower()
    
    word_count = len(text.split())
    keyword_count = text_lower.count(keyword_lower)
    
    if word_count == 0:
        return 0.0
    
    density = (keyword_count / word_count) * 100
    return round(density, 2)

def normalize_text(text: str) -> str:
    """
    Normalize text for comparison
    
    Args:
        text: Input text
        
    Returns:
        Normalized text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text