"""
NLP Analyzer - Semantic analysis using spaCy and sentence transformers
Performs advanced text analysis beyond simple keyword matching
"""

import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class NLPAnalyzer:
    """Perform NLP analysis on resume and job description"""
    
    def __init__(self):
        """Initialize NLP models"""
        try:
            # Load spaCy model
            self.nlp = spacy.load("en_core_web_md")
            print("✓ Loaded spaCy model: en_core_web_md")
        except:
            print("⚠ spaCy model not found. Run: python -m spacy download en_core_web_md")
            self.nlp = None
        
        try:
            # Load sentence transformer for semantic similarity
            self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
            print("✓ Loaded Sentence Transformer model")
        except:
            print("⚠ Sentence Transformer model not loaded")
            self.sentence_model = None
    
    def analyze(self, resume_text: str, job_text: str) -> dict:
        """
        Perform comprehensive NLP analysis
        
        Args:
            resume_text: Cleaned resume text
            job_text: Cleaned job description text
            
        Returns:
            Dictionary with analysis results
        """
        results = {}
        
        # Semantic similarity
        if self.sentence_model:
            results['similarity'] = self._calculate_semantic_similarity(
                resume_text, job_text
            )
        else:
            results['similarity'] = 0.0
        
        # Entity extraction
        if self.nlp:
            results['resume_entities'] = self._extract_entities(resume_text)
            results['job_entities'] = self._extract_entities(job_text)
        else:
            results['resume_entities'] = []
            results['job_entities'] = []
        
        # Noun phrases (key concepts)
        if self.nlp:
            results['resume_concepts'] = self._extract_noun_phrases(resume_text)
            results['job_concepts'] = self._extract_noun_phrases(job_text)
        else:
            results['resume_concepts'] = []
            results['job_concepts'] = []
        
        return results
    
    def _calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate semantic similarity using sentence transformers
        
        Args:
            text1: First text
            text2: Second text
            
        Returns:
            Similarity score (0-1)
        """
        if not self.sentence_model:
            return 0.0
        
        try:
            # Encode texts
            embedding1 = self.sentence_model.encode([text1])
            embedding2 = self.sentence_model.encode([text2])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(embedding1, embedding2)[0][0]
            
            return float(similarity)
        except Exception as e:
            print(f"Error calculating similarity: {e}")
            return 0.0
    
    def _extract_entities(self, text: str) -> list:
        """
        Extract named entities using spaCy
        
        Args:
            text: Input text
            
        Returns:
            List of entities with labels
        """
        if not self.nlp:
            return []
        
        try:
            doc = self.nlp(text[:1000000])  # Limit text length
            entities = []
            
            for ent in doc.ents:
                entities.append({
                    'text': ent.text,
                    'label': ent.label_
                })
            
            return entities
        except Exception as e:
            print(f"Error extracting entities: {e}")
            return []
    
    def _extract_noun_phrases(self, text: str) -> list:
        """
        Extract noun phrases (key concepts)
        
        Args:
            text: Input text
            
        Returns:
            List of noun phrases
        """
        if not self.nlp:
            return []
        
        try:
            doc = self.nlp(text[:1000000])  # Limit text length
            noun_phrases = []
            
            for chunk in doc.noun_chunks:
                # Filter out very short or very long phrases
                if 2 <= len(chunk.text.split()) <= 4:
                    noun_phrases.append(chunk.text.lower())
            
            # Remove duplicates and return top phrases
            return list(set(noun_phrases))[:50]
        except Exception as e:
            print(f"Error extracting noun phrases: {e}")
            return []
    
    def calculate_keyword_density(self, text: str, keywords: list) -> dict:
        """
        Calculate density of keywords in text
        
        Args:
            text: Input text
            keywords: List of keywords to check
            
        Returns:
            Dictionary with keyword densities
        """
        text_lower = text.lower()
        word_count = len(text.split())
        
        densities = {}
        for keyword in keywords:
            count = text_lower.count(keyword.lower())
            density = (count / word_count * 100) if word_count > 0 else 0
            densities[keyword] = {
                'count': count,
                'density': round(density, 2)
            }
        
        return densities