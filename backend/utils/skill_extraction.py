"""
Skill Extraction - Extract technical and soft skills from text
Uses predefined skill database and pattern matching
"""

import re
import json

class SkillExtractor:
    """Extract skills from resume and job description"""
    
    def __init__(self):
        """Initialize with skills database"""
        self.skills_db = self._load_skills_database()
    
    def _load_skills_database(self) -> dict:
        """Load comprehensive skills database"""
        return {
            'programming_languages': [
                'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php',
                'swift', 'kotlin', 'go', 'rust', 'typescript', 'scala', 'r',
                'matlab', 'perl', 'shell', 'bash', 'powershell'
            ],
            'web_technologies': [
                'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express',
                'django', 'flask', 'spring', 'asp.net', 'jquery', 'bootstrap',
                'tailwind', 'sass', 'webpack', 'next.js', 'nuxt.js'
            ],
            'databases': [
                'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle',
                'sql server', 'sqlite', 'cassandra', 'dynamodb', 'firebase',
                'elasticsearch', 'neo4j'
            ],
            'cloud_platforms': [
                'aws', 'azure', 'google cloud', 'gcp', 'heroku', 'digitalocean',
                'ibm cloud', 'oracle cloud', 'alibaba cloud'
            ],
            'devops_tools': [
                'docker', 'kubernetes', 'jenkins', 'git', 'github', 'gitlab',
                'bitbucket', 'ci/cd', 'terraform', 'ansible', 'puppet', 'chef',
                'circleci', 'travis ci'
            ],
            'data_science_ml': [
                'machine learning', 'deep learning', 'nlp', 'computer vision',
                'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'pandas',
                'numpy', 'matplotlib', 'seaborn', 'jupyter', 'data analysis',
                'statistics', 'neural networks', 'transformers', 'bert', 'gpt'
            ],
            'business_intelligence': [
                'power bi', 'tableau', 'looker', 'qlik', 'excel', 'dax',
                'data visualization', 'reporting', 'dashboards', 'analytics'
            ],
            'mobile_development': [
                'android', 'ios', 'react native', 'flutter', 'xamarin',
                'swift', 'kotlin', 'mobile app'
            ],
            'testing': [
                'unit testing', 'integration testing', 'selenium', 'jest',
                'pytest', 'junit', 'testng', 'cypress', 'qa', 'test automation'
            ],
            'methodologies': [
                'agile', 'scrum', 'kanban', 'waterfall', 'devops', 'ci/cd',
                'tdd', 'bdd', 'microservices', 'rest api', 'graphql'
            ],
            'soft_skills': [
                'leadership', 'communication', 'teamwork', 'problem solving',
                'critical thinking', 'time management', 'collaboration',
                'adaptability', 'creativity', 'analytical'
            ],
            'other_technical': [
                'linux', 'unix', 'windows', 'networking', 'security',
                'encryption', 'authentication', 'oauth', 'jwt', 'api',
                'microservices', 'serverless', 'blockchain', 'iot'
            ]
        }
    
    def extract_skills(self, text: str) -> set:
        """
        Extract skills from text
        
        Args:
            text: Resume or job description text
            
        Returns:
            Set of identified skills
        """
        text_lower = text.lower()
        found_skills = set()
        
        # Check each skill category
        for category, skills in self.skills_db.items():
            for skill in skills:
                # Use word boundaries for exact matching
                pattern = r'\b' + re.escape(skill) + r'\b'
                if re.search(pattern, text_lower):
                    found_skills.add(skill)
        
        return found_skills
    
    def categorize_skills(self, skills: set) -> dict:
        """
        Categorize skills by type
        
        Args:
            skills: Set of skills
            
        Returns:
            Dictionary of categorized skills
        """
        categorized = {}
        
        for category, skill_list in self.skills_db.items():
            category_skills = [skill for skill in skills if skill in skill_list]
            if category_skills:
                categorized[category] = category_skills
        
        return categorized
    
    def get_skills_database(self) -> dict:
        """Return the complete skills database"""
        return self.skills_db
    
    def find_skill_gaps(self, resume_skills: set, job_skills: set) -> dict:
        """
        Find skill gaps between resume and job requirements
        
        Args:
            resume_skills: Skills from resume
            job_skills: Skills from job description
            
        Returns:
            Dictionary with matched and missing skills
        """
        matched = resume_skills & job_skills
        missing = job_skills - resume_skills
        extra = resume_skills - job_skills
        
        return {
            'matched': list(matched),
            'missing': list(missing),
            'extra': list(extra),
            'match_percentage': (len(matched) / len(job_skills) * 100) if job_skills else 0
        }