"""
Resume Parser - Extract text and sections from resume files
Supports PDF, DOCX, and TXT formats
"""

import re
import PyPDF2
import docx
from typing import Dict, Optional

class ResumeParser:
    """Parse resume files and extract structured information"""
    
    def __init__(self):
        """Initialize parser with section patterns"""
        self.section_patterns = {
            'contact': r'(email|phone|linkedin|github|address)',
            'summary': r'(summary|objective|profile|about)',
            'experience': r'(experience|employment|work history)',
            'education': r'(education|academic|qualification)',
            'skills': r'(skills|technical skills|competencies)',
            'projects': r'(projects|portfolio)',
            'certifications': r'(certifications|certificates|licenses)',
            'achievements': r'(achievements|awards|honors)'
        }
    
    def extract_text(self, filepath: str) -> str:
        """
        Extract text from resume file
        
        Args:
            filepath: Path to resume file
            
        Returns:
            Extracted text content
        """
        file_extension = filepath.lower().split('.')[-1]
        
        if file_extension == 'pdf':
            return self._extract_from_pdf(filepath)
        elif file_extension == 'docx':
            return self._extract_from_docx(filepath)
        elif file_extension == 'txt':
            return self._extract_from_txt(filepath)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
    
    def _extract_from_pdf(self, filepath: str) -> str:
        """Extract text from PDF file"""
        text = ""
        try:
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
        
        return text.strip()
    
    def _extract_from_docx(self, filepath: str) -> str:
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(filepath)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            raise Exception(f"Error reading DOCX: {str(e)}")
        
        return text.strip()
    
    def _extract_from_txt(self, filepath: str) -> str:
        """Extract text from TXT file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            raise Exception(f"Error reading TXT: {str(e)}")
        
        return text.strip()
    
    def extract_sections(self, text: str) -> Dict[str, bool]:
        """
        Identify which sections are present in resume
        
        Args:
            text: Resume text
            
        Returns:
            Dictionary of section names and presence (True/False)
        """
        text_lower = text.lower()
        sections = {}
        
        for section_name, pattern in self.section_patterns.items():
            # Check if section heading exists
            sections[section_name] = bool(re.search(pattern, text_lower, re.IGNORECASE))
        
        return sections
    
    def extract_contact_info(self, text: str) -> Dict[str, Optional[str]]:
        """
        Extract contact information from resume
        
        Args:
            text: Resume text
            
        Returns:
            Dictionary with email, phone, linkedin, github
        """
        contact_info = {
            'email': None,
            'phone': None,
            'linkedin': None,
            'github': None
        }
        
        # Email pattern
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, text)
        if email_match:
            contact_info['email'] = email_match.group()
        
        # Phone pattern (various formats)
        phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        phone_match = re.search(phone_pattern, text)
        if phone_match:
            contact_info['phone'] = phone_match.group()
        
        # LinkedIn pattern
        linkedin_pattern = r'linkedin\.com/in/[\w-]+'
        linkedin_match = re.search(linkedin_pattern, text, re.IGNORECASE)
        if linkedin_match:
            contact_info['linkedin'] = linkedin_match.group()
        
        # GitHub pattern
        github_pattern = r'github\.com/[\w-]+'
        github_match = re.search(github_pattern, text, re.IGNORECASE)
        if github_match:
            contact_info['github'] = github_match.group()
        
        return contact_info
    
    def extract_education(self, text: str) -> list:
        """
        Extract education information
        
        Args:
            text: Resume text
            
        Returns:
            List of education entries
        """
        education = []
        
        # Common degree patterns
        degree_patterns = [
            r'(Bachelor|B\.S\.|B\.A\.|BS|BA)',
            r'(Master|M\.S\.|M\.A\.|MS|MA|MBA)',
            r'(Ph\.D\.|PhD|Doctorate)',
            r'(Associate|A\.S\.|A\.A\.)'
        ]
        
        for pattern in degree_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get surrounding context (50 chars before and after)
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end].strip()
                education.append(context)
        
        return education
    
    def extract_experience_years(self, text: str) -> Optional[int]:
        """
        Extract years of experience from resume
        
        Args:
            text: Resume text
            
        Returns:
            Number of years of experience (or None)
        """
        # Pattern for "X years of experience"
        pattern = r'(\d+)\+?\s*years?\s*(of)?\s*experience'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            return int(match.group(1))
        
        # Alternative: Count date ranges in experience section
        # This is a simplified approach
        date_pattern = r'(20\d{2}|19\d{2})\s*[-–]\s*(20\d{2}|19\d{2}|present|current)'
        dates = re.findall(date_pattern, text, re.IGNORECASE)
        
        if dates:
            years = []
            for start, end in dates:
                start_year = int(start)
                if end.lower() in ['present', 'current']:
                    end_year = 2024  # Current year
                else:
                    end_year = int(end)
                years.append(end_year - start_year)
            
            return sum(years) if years else None
        
        return None