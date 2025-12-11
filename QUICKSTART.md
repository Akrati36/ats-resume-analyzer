# ⚡ Quick Start Guide - ATS Resume Analyzer

Get the project running in 10 minutes!

---

## 🚀 Super Quick Start

### Backend (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/Akrati36/ats-resume-analyzer.git
cd ats-resume-analyzer/backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download spaCy model
python -m spacy download en_core_web_md

# 5. Run backend
python app.py
```

Backend runs on: **http://localhost:5000**

### Frontend (5 minutes)

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Run frontend
npm start
```

Frontend runs on: **http://localhost:3000**

---

## 📋 Detailed Setup

### Prerequisites

**Required:**
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Node.js 16+ ([Download](https://nodejs.org/))
- pip (comes with Python)
- npm (comes with Node.js)

**Optional:**
- MongoDB (for user accounts feature)
- Git ([Download](https://git-scm.com/))

### Step-by-Step Installation

#### 1. Get the Code

**Option A: Using Git**
```bash
git clone https://github.com/Akrati36/ats-resume-analyzer.git
cd ats-resume-analyzer
```

**Option B: Download ZIP**
1. Go to https://github.com/Akrati36/ats-resume-analyzer
2. Click **Code** → **Download ZIP**
3. Extract and open terminal in folder

#### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Download NLP models
python -m spacy download en_core_web_md
python -m nltk.downloader punkt stopwords

# Create environment file
cp .env.example .env
# Edit .env if needed

# Create uploads folder
mkdir uploads

# Run backend
python app.py
```

**Expected Output:**
```
======================================================================
ATS RESUME ANALYZER - Backend Server
======================================================================
Starting Flask application...
API will be available at: http://localhost:5000
======================================================================
 * Running on http://0.0.0.0:5000
```

#### 3. Frontend Setup

Open a **new terminal** (keep backend running):

```bash
cd frontend

# Install Node packages
npm install

# Create environment file
cp .env.example .env
# Edit .env to point to backend (http://localhost:5000)

# Run frontend
npm start
```

**Expected Output:**
```
Compiled successfully!

You can now view ats-resume-analyzer in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.1.x:3000
```

---

## 🧪 Test the Application

### 1. Open Browser
Navigate to: **http://localhost:3000**

### 2. Upload Resume
- Click "Upload Resume" or drag & drop
- Use PDF, DOCX, or TXT file
- Max size: 5MB

### 3. Paste Job Description
- Copy a job posting
- Paste into text area

### 4. Analyze
- Click "Analyze Resume"
- Wait ~5 seconds
- View results!

---

## 🔧 Troubleshooting

### Backend Issues

**Issue: "Module not found"**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install flask flask-cors PyPDF2 spacy
```

**Issue: "spaCy model not found"**
```bash
# Download model
python -m spacy download en_core_web_md

# Verify installation
python -c "import spacy; nlp = spacy.load('en_core_web_md'); print('OK')"
```

**Issue: "Port 5000 already in use"**
```bash
# Change port in app.py
# Line: app.run(debug=True, host='0.0.0.0', port=5001)

# Or kill process on port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

### Frontend Issues

**Issue: "npm not found"**
```bash
# Install Node.js from nodejs.org
# Verify installation
node --version
npm --version
```

**Issue: "Dependencies not installing"**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Issue: "Cannot connect to backend"**
```bash
# Check backend is running on port 5000
# Update .env file with correct backend URL
REACT_APP_API_URL=http://localhost:5000
```

### Common Errors

**Error: "File too large"**
- Max file size is 5MB
- Compress your resume PDF

**Error: "Invalid file type"**
- Only PDF, DOCX, TXT supported
- Convert your resume to supported format

**Error: "Analysis failed"**
- Check resume file isn't corrupted
- Try a different file
- Check backend logs for details

---

## 📊 Sample Test Data

### Sample Resume Text
```
John Doe
Software Engineer
john.doe@email.com | (555) 123-4567

SUMMARY
Experienced software engineer with 5+ years in Python and machine learning.

EXPERIENCE
Senior Software Engineer | Tech Corp | 2020-Present
- Developed ML models using Python, TensorFlow, scikit-learn
- Built REST APIs with Flask and FastAPI
- Deployed applications on AWS

EDUCATION
B.S. Computer Science | University | 2018

SKILLS
Python, JavaScript, React, Flask, TensorFlow, AWS, Docker, Git
```

### Sample Job Description
```
Senior Software Engineer - Machine Learning

Requirements:
- 5+ years of software development experience
- Strong Python programming skills
- Experience with machine learning frameworks (TensorFlow, PyTorch)
- Knowledge of REST APIs and web frameworks
- Cloud platform experience (AWS, Azure, GCP)
- Bachelor's degree in Computer Science or related field

Preferred:
- Experience with Docker and Kubernetes
- React or similar frontend framework
- CI/CD pipeline experience
```

---

## 🎯 Next Steps

### Explore Features
1. Try different resumes
2. Test various job descriptions
3. Check keyword matching
4. Review skill gap analysis
5. Read improvement suggestions

### Customize
1. Modify scoring weights in `ats_scorer.py`
2. Add more skills to `skill_extraction.py`
3. Customize UI in React components
4. Add your own features

### Contribute
1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Submit pull request

---

## 📚 Documentation

- **README.md** - Full project documentation
- **API.md** - API endpoint details
- **CONTRIBUTING.md** - Contribution guidelines
- **LINKEDIN_ANNOUNCEMENT.md** - Social media templates

---

## 🆘 Get Help

**Issues:**
- Check [GitHub Issues](https://github.com/Akrati36/ats-resume-analyzer/issues)
- Search for similar problems
- Create new issue if needed

**Questions:**
- Email: akratimishra366@gmail.com
- GitHub Discussions
- LinkedIn: [Akrati Mishra](https://linkedin.com/in/akrati-mishra)

---

## ✅ Checklist

Before you start:
- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] Git installed (optional)
- [ ] 10 minutes of time

Setup:
- [ ] Repository cloned
- [ ] Backend dependencies installed
- [ ] spaCy model downloaded
- [ ] Backend running on port 5000
- [ ] Frontend dependencies installed
- [ ] Frontend running on port 3000

Testing:
- [ ] Opened http://localhost:3000
- [ ] Uploaded sample resume
- [ ] Pasted job description
- [ ] Got analysis results

---

**You're all set! Start analyzing resumes! 🚀**

**Questions?** Check the troubleshooting section or open an issue.