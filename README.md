# 🚀 ATS Resume Analyzer

**Beat the bots, land the job!** An AI-powered tool that analyzes your resume against job descriptions, predicts ATS scores, and provides actionable improvement suggestions.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react)
![NLP](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge)
![ML](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎯 The Problem

**75% of resumes never reach human eyes** - they're filtered out by Applicant Tracking Systems (ATS).

Job seekers struggle with:
- ❌ Not knowing if their resume will pass ATS screening
- ❌ Missing critical keywords from job descriptions
- ❌ Poor formatting that ATS can't parse
- ❌ No feedback on how to improve

---

## 💡 The Solution

An intelligent resume analyzer that:
- ✅ **Predicts ATS Score** - Know your chances before applying
- ✅ **Keyword Matching** - Identifies missing critical keywords
- ✅ **Semantic Analysis** - Goes beyond simple keyword matching using NLP
- ✅ **Skill Gap Analysis** - Shows what skills you're missing
- ✅ **Actionable Suggestions** - Specific improvements to make
- ✅ **Job Matching** - Finds jobs that match your resume
- ✅ **Resume Optimization** - Export ATS-friendly version

---

## 🌟 Features

### Phase 1: MVP (Weeks 1-2) ✅
- [x] Resume text extraction (PDF, DOCX, TXT)
- [x] Job description input
- [x] Keyword matching algorithm
- [x] Basic ATS score calculation
- [x] Simple web interface

### Phase 2: AI Integration (Weeks 3-4) 🚧
- [x] NLP-based semantic matching
- [x] ML model for ATS score prediction
- [x] Skill gap analysis
- [x] AI-powered improvement suggestions
- [x] Advanced scoring algorithm

### Phase 3: Advanced Features (Weeks 5-6) 📋
- [ ] Job matching algorithm
- [ ] User dashboard with analytics
- [ ] User profiles & saved resumes
- [ ] Export optimized resume
- [ ] Batch analysis

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Frontend (React)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │  Upload  │  │  Score   │  │  Skills  │  │ Suggest │ │
│  │  Resume  │  │ Display  │  │   Gap    │  │  -ions  │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────┘
                            ↕ REST API
┌─────────────────────────────────────────────────────────┐
│                   Backend (Flask/FastAPI)                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │  Resume  │  │   NLP    │  │    ML    │  │   AI    │ │
│  │  Parser  │  │ Analyzer │  │  Scorer  │  │ Suggest │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────┐
│                  Database (MongoDB)                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Users   │  │ Resumes  │  │   Jobs   │              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core language
- **Flask/FastAPI** - REST API framework
- **spaCy** - NLP processing
- **scikit-learn** - Machine learning
- **NLTK** - Text processing
- **PyPDF2/pdfplumber** - PDF extraction
- **python-docx** - Word file parsing
- **sentence-transformers** - Semantic similarity
- **MongoDB** - Database

### Frontend
- **React 18+** - UI framework
- **Tailwind CSS** - Styling
- **Chart.js** - Data visualization
- **Axios** - API calls
- **React Router** - Navigation

### AI/ML
- **TF-IDF** - Keyword importance
- **BERT** - Semantic understanding
- **Random Forest** - ATS score prediction
- **Cosine Similarity** - Resume-job matching

---

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8+
python --version

# Node.js 16+
node --version

# MongoDB (local or Atlas)
mongod --version
```

### Installation

#### 1. Clone Repository
```bash
git clone https://github.com/Akrati36/ats-resume-analyzer.git
cd ats-resume-analyzer
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_md

# Set environment variables
cp .env.example .env
# Edit .env with your settings

# Run backend
python app.py
```

Backend runs on: http://localhost:5000

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.example .env
# Edit .env with backend URL

# Run frontend
npm start
```

Frontend runs on: http://localhost:3000

---

## 📖 Usage

### 1. Upload Resume
- Drag & drop or click to upload
- Supports PDF, DOCX, TXT
- Max size: 5MB

### 2. Paste Job Description
- Copy job posting
- Paste into text area
- Or upload job description file

### 3. Analyze
- Click "Analyze Resume"
- Wait for AI processing (~5 seconds)
- View comprehensive results

### 4. Review Results

**ATS Score (0-100)**
- 90-100: Excellent match
- 75-89: Good match
- 60-74: Fair match
- Below 60: Needs improvement

**Keyword Analysis**
- Matched keywords (green)
- Missing keywords (red)
- Keyword density comparison

**Skill Gap**
- Required skills from job
- Your current skills
- Missing skills to add

**Suggestions**
- Specific improvements
- Keyword placement tips
- Formatting recommendations

### 5. Optimize & Export
- Apply suggested changes
- Export ATS-friendly version
- Save for future reference

---

## 📊 How It Works

### 1. Resume Parsing
```python
# Extract text from resume
text = extract_text_from_pdf(resume_file)

# Clean and preprocess
cleaned_text = preprocess_text(text)

# Extract sections
sections = extract_sections(cleaned_text)
```

### 2. NLP Analysis
```python
# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Process resume and job description
resume_doc = nlp(resume_text)
job_doc = nlp(job_description)

# Extract entities and keywords
resume_keywords = extract_keywords(resume_doc)
job_keywords = extract_keywords(job_doc)
```

### 3. Semantic Matching
```python
# Use sentence transformers for semantic similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode texts
resume_embedding = model.encode(resume_text)
job_embedding = model.encode(job_description)

# Calculate similarity
similarity = cosine_similarity(resume_embedding, job_embedding)
```

### 4. ATS Score Prediction
```python
# Feature extraction
features = extract_features(resume, job_description)

# ML model prediction
ats_score = model.predict(features)

# Confidence score
confidence = model.predict_proba(features)
```

### 5. Skill Gap Analysis
```python
# Extract skills from job description
required_skills = extract_skills(job_description)

# Extract skills from resume
resume_skills = extract_skills(resume_text)

# Find gaps
missing_skills = required_skills - resume_skills
matched_skills = required_skills & resume_skills
```

---

## 🎯 Scoring Algorithm

### ATS Score Components (0-100)

**1. Keyword Match (40 points)**
- Exact keyword matches: 20 points
- Semantic keyword matches: 20 points

**2. Skills Match (25 points)**
- Required skills present: 15 points
- Additional relevant skills: 10 points

**3. Experience Match (15 points)**
- Years of experience: 10 points
- Relevant experience: 5 points

**4. Education Match (10 points)**
- Degree requirements: 7 points
- Certifications: 3 points

**5. Format & Structure (10 points)**
- ATS-friendly format: 5 points
- Clear sections: 3 points
- Contact info present: 2 points

### Score Interpretation

| Score | Rating | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Very high chance of passing ATS |
| 75-89 | Good | Good chance with minor improvements |
| 60-74 | Fair | Needs improvements to pass |
| 45-59 | Poor | Significant changes required |
| 0-44 | Very Poor | Major overhaul needed |

---

## 📁 Project Structure

```
ats-resume-analyzer/
├── backend/
│   ├── app.py                      # Main Flask application
│   ├── requirements.txt            # Python dependencies
│   ├── config.py                   # Configuration
│   ├── models/
│   │   ├── resume_parser.py        # Resume extraction
│   │   ├── nlp_analyzer.py         # NLP processing
│   │   ├── ats_scorer.py           # Scoring algorithm
│   │   └── ml_model.py             # ML predictions
│   ├── utils/
│   │   ├── text_processing.py      # Text utilities
│   │   ├── keyword_extraction.py   # Keyword extraction
│   │   └── skill_extraction.py     # Skill extraction
│   ├── routes/
│   │   ├── analyze.py              # Analysis endpoints
│   │   ├── upload.py               # File upload
│   │   └── suggestions.py          # AI suggestions
│   └── data/
│       ├── skills_database.json    # Skills taxonomy
│       └── ats_keywords.json       # Common ATS keywords
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Upload.jsx          # File upload component
│   │   │   ├── ScoreDisplay.jsx    # Score visualization
│   │   │   ├── KeywordMatch.jsx    # Keyword analysis
│   │   │   ├── SkillGap.jsx        # Skill gap display
│   │   │   └── Suggestions.jsx     # Improvement tips
│   │   ├── pages/
│   │   │   ├── Home.jsx            # Landing page
│   │   │   ├── Analyze.jsx         # Analysis page
│   │   │   └── Dashboard.jsx       # User dashboard
│   │   ├── services/
│   │   │   └── api.js              # API calls
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
├── ml_models/
│   ├── train_ats_model.py          # Model training
│   ├── ats_classifier.pkl          # Trained model
│   └── vectorizer.pkl              # TF-IDF vectorizer
├── docs/
│   ├── API.md                      # API documentation
│   ├── DEPLOYMENT.md               # Deployment guide
│   └── CONTRIBUTING.md             # Contribution guide
├── tests/
│   ├── test_parser.py
│   ├── test_analyzer.py
│   └── test_scorer.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔌 API Endpoints

### POST /api/analyze
Analyze resume against job description

**Request:**
```json
{
  "resume_file": "base64_encoded_file",
  "job_description": "Job description text",
  "file_type": "pdf"
}
```

**Response:**
```json
{
  "ats_score": 85,
  "keyword_match": {
    "matched": ["Python", "Machine Learning", "SQL"],
    "missing": ["AWS", "Docker"],
    "match_percentage": 75
  },
  "skill_gap": {
    "required": ["Python", "ML", "AWS", "Docker"],
    "present": ["Python", "ML"],
    "missing": ["AWS", "Docker"]
  },
  "suggestions": [
    "Add 'AWS' keyword in skills section",
    "Include Docker experience in projects"
  ],
  "sections": {
    "contact": true,
    "summary": true,
    "experience": true,
    "education": true,
    "skills": true
  }
}
```

### GET /api/jobs/match
Find matching jobs for resume

**Query Parameters:**
- `resume_id`: Resume ID
- `limit`: Number of results (default: 10)

**Response:**
```json
{
  "matches": [
    {
      "job_id": "123",
      "title": "ML Engineer",
      "company": "Tech Corp",
      "match_score": 92,
      "missing_skills": ["AWS"]
    }
  ]
}
```

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/ -v

# Frontend tests
cd frontend
npm test

# Integration tests
npm run test:integration

# Coverage report
pytest --cov=backend tests/
```

---

## 📈 Performance

- **Resume Parsing:** < 2 seconds
- **NLP Analysis:** < 3 seconds
- **ML Prediction:** < 1 second
- **Total Analysis:** < 6 seconds

**Optimizations:**
- Caching for repeated analyses
- Async processing for large files
- Model quantization for faster inference
- CDN for frontend assets

---

## 🎨 Screenshots

### Home Page
![Home](docs/screenshots/home.png)

### Upload Resume
![Upload](docs/screenshots/upload.png)

### Analysis Results
![Results](docs/screenshots/results.png)

### Skill Gap Analysis
![Skills](docs/screenshots/skills.png)

---

## 🚀 Deployment

### Backend (Heroku)
```bash
heroku create ats-analyzer-api
heroku addons:create mongolab
git push heroku main
```

### Frontend (Vercel)
```bash
cd frontend
vercel --prod
```

### Docker
```bash
docker-compose up -d
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 Roadmap

### Version 1.0 (Current)
- [x] Resume parsing
- [x] Basic ATS scoring
- [x] Keyword matching
- [x] Simple UI

### Version 2.0 (Next)
- [ ] Advanced ML models
- [ ] Job board integration
- [ ] User accounts
- [ ] Resume templates
- [ ] Mobile app

### Version 3.0 (Future)
- [ ] AI resume writing
- [ ] Interview preparation
- [ ] Salary insights
- [ ] Career path suggestions
- [ ] LinkedIn integration

---

## 📊 Use Cases

### For Job Seekers
- Optimize resume before applying
- Understand ATS requirements
- Identify skill gaps
- Improve job match rate

### For Career Coaches
- Help clients improve resumes
- Provide data-driven feedback
- Track improvement over time
- Batch analyze multiple resumes

### For Recruiters
- Pre-screen candidates
- Identify best matches
- Reduce manual screening time
- Improve hiring quality

---

## 🎓 Learning Resources

**Resume Writing:**
- [Harvard Resume Guide](https://hwpi.harvard.edu/files/ocs/files/hes-resume-cover-letter-guide.pdf)
- [ATS-Friendly Resume Tips](https://www.jobscan.co/blog/ats-resume/)

**NLP & ML:**
- [spaCy Documentation](https://spacy.io/usage)
- [Sentence Transformers](https://www.sbert.net/)
- [scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)

**Full-Stack Development:**
- [React Documentation](https://react.dev/)
- [Flask Tutorial](https://flask.palletsprojects.com/)
- [MongoDB University](https://university.mongodb.com/)

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 👤 Author

**Akrati Mishra**
- GitHub: [@Akrati36](https://github.com/Akrati36)
- LinkedIn: [Akrati Mishra](https://linkedin.com/in/akrati-mishra)
- Email: akratimishra366@gmail.com

---

## 🙏 Acknowledgments

- spaCy for NLP capabilities
- Hugging Face for transformer models
- React community for amazing tools
- Open source contributors

---

## 📞 Support

- 📧 Email: akratimishra366@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/Akrati36/ats-resume-analyzer/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/Akrati36/ats-resume-analyzer/discussions)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

**Built with ❤️ to help job seekers land their dream jobs**

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)

</div>