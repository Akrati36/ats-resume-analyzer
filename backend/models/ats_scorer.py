"""
ATS Scorer - Calculate comprehensive ATS score
Combines multiple factors to predict resume's ATS performance
"""

class ATSScorer:
    """Calculate ATS score based on multiple factors"""
    
    def __init__(self):
        """Initialize scorer with weights"""
        self.weights = {
            'keyword_match': 0.40,      # 40 points
            'skills_match': 0.25,       # 25 points
            'experience_match': 0.15,   # 15 points
            'education_match': 0.10,    # 10 points
            'format_structure': 0.10    # 10 points
        }
    
    def calculate_score(self, **kwargs) -> dict:
        """
        Calculate overall ATS score
        
        Args:
            resume_text: Full resume text
            job_description: Job description text
            resume_sections: Dict of section presence
            nlp_results: NLP analysis results
            resume_keywords: List of resume keywords
            job_keywords: List of job keywords
            resume_skills: Set of resume skills
            job_skills: Set of job skills
            
        Returns:
            Dictionary with score and breakdown
        """
        # Extract arguments
        resume_text = kwargs.get('resume_text', '')
        job_description = kwargs.get('job_description', '')
        resume_sections = kwargs.get('resume_sections', {})
        nlp_results = kwargs.get('nlp_results', {})
        resume_keywords = kwargs.get('resume_keywords', [])
        job_keywords = kwargs.get('job_keywords', [])
        resume_skills = kwargs.get('resume_skills', set())
        job_skills = kwargs.get('job_skills', set())
        
        # Calculate component scores
        keyword_score = self._calculate_keyword_score(
            resume_keywords, job_keywords, nlp_results
        )
        
        skills_score = self._calculate_skills_score(
            resume_skills, job_skills
        )
        
        experience_score = self._calculate_experience_score(
            resume_text, job_description
        )
        
        education_score = self._calculate_education_score(
            resume_text, job_description
        )
        
        format_score = self._calculate_format_score(
            resume_sections
        )
        
        # Calculate weighted total
        total_score = (
            keyword_score * self.weights['keyword_match'] +
            skills_score * self.weights['skills_match'] +
            experience_score * self.weights['experience_match'] +
            education_score * self.weights['education_match'] +
            format_score * self.weights['format_structure']
        ) * 100
        
        return {
            'score': total_score,
            'breakdown': {
                'keyword_match': round(keyword_score * 100, 2),
                'skills_match': round(skills_score * 100, 2),
                'experience_match': round(experience_score * 100, 2),
                'education_match': round(education_score * 100, 2),
                'format_structure': round(format_score * 100, 2)
            }
        }
    
    def _calculate_keyword_score(self, resume_keywords, job_keywords, nlp_results):
        """Calculate keyword matching score (0-1)"""
        if not job_keywords:
            return 0.5  # Neutral score if no job keywords
        
        # Exact keyword matches (50%)
        matched = set(resume_keywords) & set(job_keywords)
        exact_match_ratio = len(matched) / len(job_keywords)
        exact_score = min(exact_match_ratio, 1.0) * 0.5
        
        # Semantic similarity (50%)
        semantic_score = nlp_results.get('similarity', 0) * 0.5
        
        return exact_score + semantic_score
    
    def _calculate_skills_score(self, resume_skills, job_skills):
        """Calculate skills matching score (0-1)"""
        if not job_skills:
            return 0.6  # Neutral score if no required skills
        
        # Required skills present (60%)
        matched_skills = resume_skills & job_skills
        required_ratio = len(matched_skills) / len(job_skills)
        required_score = min(required_ratio, 1.0) * 0.6
        
        # Additional relevant skills (40%)
        additional_skills = resume_skills - job_skills
        additional_score = min(len(additional_skills) / 10, 1.0) * 0.4
        
        return required_score + additional_score
    
    def _calculate_experience_score(self, resume_text, job_description):
        """Calculate experience matching score (0-1)"""
        score = 0.5  # Base score
        
        # Check for years of experience
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Look for experience mentions
        experience_keywords = ['years', 'experience', 'worked', 'developed']
        for keyword in experience_keywords:
            if keyword in resume_lower and keyword in job_lower:
                score += 0.1
        
        return min(score, 1.0)
    
    def _calculate_education_score(self, resume_text, job_description):
        """Calculate education matching score (0-1)"""
        score = 0.5  # Base score
        
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Common degree levels
        degrees = ['bachelor', 'master', 'phd', 'doctorate', 'mba']
        
        for degree in degrees:
            if degree in job_lower:
                if degree in resume_lower:
                    score += 0.3
                    break
        
        # Certifications
        cert_keywords = ['certified', 'certification', 'license']
        for keyword in cert_keywords:
            if keyword in resume_lower and keyword in job_lower:
                score += 0.2
                break
        
        return min(score, 1.0)
    
    def _calculate_format_score(self, resume_sections):
        """Calculate format and structure score (0-1)"""
        score = 0.0
        
        # Essential sections
        essential = ['contact', 'experience', 'education']
        for section in essential:
            if resume_sections.get(section, False):
                score += 0.25
        
        # Important sections
        important = ['skills', 'summary']
        for section in important:
            if resume_sections.get(section, False):
                score += 0.125
        
        return min(score, 1.0)