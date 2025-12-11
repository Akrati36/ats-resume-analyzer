"""
ATS Resume Analyzer - Main Flask Application
Analyzes resumes against job descriptions using NLP and ML
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Import custom modules
from models.resume_parser import ResumeParser
from models.nlp_analyzer import NLPAnalyzer
from models.ats_scorer import ATSScorer
from utils.text_processing import clean_text, extract_keywords
from utils.skill_extraction import SkillExtractor

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx', 'txt'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize components
resume_parser = ResumeParser()
nlp_analyzer = NLPAnalyzer()
ats_scorer = ATSScorer()
skill_extractor = SkillExtractor()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_uploaded_file(file):
    """Save uploaded file and return path"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filepath
    return None

# ============================================================================
# API ROUTES
# ============================================================================

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'message': 'ATS Resume Analyzer API',
        'version': '1.0.0',
        'endpoints': {
            'analyze': '/api/analyze',
            'health': '/api/health',
            'skills': '/api/skills'
        }
    })

@app.route('/api/health')
def health():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'components': {
            'parser': 'ready',
            'nlp': 'ready',
            'scorer': 'ready'
        }
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_resume():
    """
    Main endpoint to analyze resume against job description
    
    Request:
        - resume_file: PDF/DOCX/TXT file
        - job_description: Text of job posting
        
    Response:
        - ats_score: Overall ATS score (0-100)
        - keyword_match: Matched and missing keywords
        - skill_gap: Required vs present skills
        - suggestions: Improvement recommendations
        - sections: Resume section analysis
    """
    try:
        # Validate request
        if 'resume_file' not in request.files:
            return jsonify({'error': 'No resume file provided'}), 400
        
        if 'job_description' not in request.form:
            return jsonify({'error': 'No job description provided'}), 400
        
        # Get files and data
        resume_file = request.files['resume_file']
        job_description = request.form['job_description']
        
        if resume_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(resume_file.filename):
            return jsonify({'error': 'Invalid file type. Use PDF, DOCX, or TXT'}), 400
        
        # Save uploaded file
        filepath = save_uploaded_file(resume_file)
        if not filepath:
            return jsonify({'error': 'Failed to save file'}), 500
        
        # Step 1: Parse resume
        print(f"[1/5] Parsing resume: {resume_file.filename}")
        resume_text = resume_parser.extract_text(filepath)
        resume_sections = resume_parser.extract_sections(resume_text)
        
        # Step 2: Clean and preprocess
        print("[2/5] Preprocessing text")
        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_description)
        
        # Step 3: NLP Analysis
        print("[3/5] Performing NLP analysis")
        nlp_results = nlp_analyzer.analyze(resume_clean, job_clean)
        
        # Step 4: Extract keywords and skills
        print("[4/5] Extracting keywords and skills")
        resume_keywords = extract_keywords(resume_clean)
        job_keywords = extract_keywords(job_clean)
        
        resume_skills = skill_extractor.extract_skills(resume_text)
        job_skills = skill_extractor.extract_skills(job_description)
        
        # Step 5: Calculate ATS score
        print("[5/5] Calculating ATS score")
        ats_results = ats_scorer.calculate_score(
            resume_text=resume_text,
            job_description=job_description,
            resume_sections=resume_sections,
            nlp_results=nlp_results,
            resume_keywords=resume_keywords,
            job_keywords=job_keywords,
            resume_skills=resume_skills,
            job_skills=job_skills
        )
        
        # Keyword matching
        matched_keywords = list(set(resume_keywords) & set(job_keywords))
        missing_keywords = list(set(job_keywords) - set(resume_keywords))
        
        keyword_match_percentage = (len(matched_keywords) / len(job_keywords) * 100) if job_keywords else 0
        
        # Skill gap analysis
        matched_skills = list(set(resume_skills) & set(job_skills))
        missing_skills = list(set(job_skills) - set(resume_skills))
        
        # Generate suggestions
        suggestions = generate_suggestions(
            ats_results['score'],
            missing_keywords,
            missing_skills,
            resume_sections
        )
        
        # Clean up uploaded file
        try:
            os.remove(filepath)
        except:
            pass
        
        # Prepare response
        response = {
            'success': True,
            'ats_score': round(ats_results['score'], 2),
            'score_breakdown': ats_results['breakdown'],
            'rating': get_rating(ats_results['score']),
            'keyword_match': {
                'matched': matched_keywords[:20],  # Top 20
                'missing': missing_keywords[:20],
                'match_percentage': round(keyword_match_percentage, 2),
                'total_job_keywords': len(job_keywords),
                'total_matched': len(matched_keywords)
            },
            'skill_gap': {
                'required': list(job_skills)[:15],
                'present': list(matched_skills)[:15],
                'missing': list(missing_skills)[:15],
                'match_percentage': round((len(matched_skills) / len(job_skills) * 100) if job_skills else 0, 2)
            },
            'sections': {
                'contact': resume_sections.get('contact', False),
                'summary': resume_sections.get('summary', False),
                'experience': resume_sections.get('experience', False),
                'education': resume_sections.get('education', False),
                'skills': resume_sections.get('skills', False),
                'projects': resume_sections.get('projects', False)
            },
            'suggestions': suggestions,
            'semantic_similarity': round(nlp_results.get('similarity', 0) * 100, 2),
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        print(f"✓ Analysis complete! ATS Score: {response['ats_score']}")
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in analyze_resume: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/skills', methods=['GET'])
def get_skills_database():
    """Get list of common skills by category"""
    try:
        skills = skill_extractor.get_skills_database()
        return jsonify({
            'success': True,
            'skills': skills
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/keywords', methods=['POST'])
def extract_keywords_endpoint():
    """Extract keywords from text"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        keywords = extract_keywords(text)
        
        return jsonify({
            'success': True,
            'keywords': keywords[:50],  # Top 50
            'count': len(keywords)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_rating(score):
    """Convert score to rating"""
    if score >= 90:
        return {
            'level': 'Excellent',
            'color': 'green',
            'message': 'Very high chance of passing ATS!'
        }
    elif score >= 75:
        return {
            'level': 'Good',
            'color': 'blue',
            'message': 'Good chance with minor improvements'
        }
    elif score >= 60:
        return {
            'level': 'Fair',
            'color': 'yellow',
            'message': 'Needs improvements to pass ATS'
        }
    elif score >= 45:
        return {
            'level': 'Poor',
            'color': 'orange',
            'message': 'Significant changes required'
        }
    else:
        return {
            'level': 'Very Poor',
            'color': 'red',
            'message': 'Major overhaul needed'
        }

def generate_suggestions(score, missing_keywords, missing_skills, sections):
    """Generate actionable improvement suggestions"""
    suggestions = []
    
    # Score-based suggestions
    if score < 60:
        suggestions.append({
            'type': 'critical',
            'category': 'Overall',
            'message': 'Your resume needs significant improvements to pass ATS screening',
            'action': 'Focus on adding relevant keywords and restructuring content'
        })
    
    # Keyword suggestions
    if missing_keywords:
        top_missing = missing_keywords[:5]
        suggestions.append({
            'type': 'high',
            'category': 'Keywords',
            'message': f'Add these critical keywords: {", ".join(top_missing)}',
            'action': 'Incorporate these keywords naturally in your experience and skills sections'
        })
    
    # Skill suggestions
    if missing_skills:
        top_skills = missing_skills[:5]
        suggestions.append({
            'type': 'high',
            'category': 'Skills',
            'message': f'Missing required skills: {", ".join(top_skills)}',
            'action': 'Add these skills if you have them, or consider learning them'
        })
    
    # Section suggestions
    if not sections.get('summary'):
        suggestions.append({
            'type': 'medium',
            'category': 'Structure',
            'message': 'Add a professional summary at the top',
            'action': 'Write a 2-3 sentence summary highlighting your key qualifications'
        })
    
    if not sections.get('skills'):
        suggestions.append({
            'type': 'high',
            'category': 'Structure',
            'message': 'Add a dedicated Skills section',
            'action': 'Create a clear skills section with relevant technical and soft skills'
        })
    
    # Formatting suggestions
    suggestions.append({
        'type': 'low',
        'category': 'Formatting',
        'message': 'Use standard section headings',
        'action': 'Use clear headings like "Experience", "Education", "Skills"'
    })
    
    suggestions.append({
        'type': 'low',
        'category': 'Formatting',
        'message': 'Avoid tables, images, and complex formatting',
        'action': 'Use simple text formatting that ATS can easily parse'
    })
    
    # Positive feedback
    if score >= 75:
        suggestions.insert(0, {
            'type': 'success',
            'category': 'Overall',
            'message': 'Great job! Your resume is well-optimized for ATS',
            'action': 'Make the suggested minor improvements to reach excellent level'
        })
    
    return suggestions

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({
        'error': 'File too large. Maximum size is 5MB'
    }), 413

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error'
    }), 500

# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("ATS RESUME ANALYZER - Backend Server")
    print("="*70)
    print("Starting Flask application...")
    print("API will be available at: http://localhost:5000")
    print("="*70)
    
    # Run in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)