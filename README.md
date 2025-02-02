# BharatFD
 <!DOCTYPE html>
<html>
<head>
    <title>BharatFD - FAQ Backend</title>
</head>
<body>
    <h1>BharatFD - FAQ Backend</h1>
    <p>A multilingual FAQ system built with Django, featuring:</p>
    <ul>
        <li>✔️ Automatic language detection for questions and answers</li>
        <li>✔️ Language-specific fields in API responses</li>
        <li>✔️ Google Translate-powered auto-translation</li>
        <li>✔️ Rich Text Editing (WYSIWYG) support with CKEditor</li>
        <li>✔️ Django Admin Panel for easy management</li>
    </ul>
    
    <h2>🚀 Features</h2>
    <ul>
        <li>✅ Detects the language of both questions and answers</li>
        <li>✅ Translates non-English content to English</li>
        <li>✅ Stores detected language codes (ISO 639-1 format) in the database</li>
        <li>✅ Exposes language details via API responses</li>
        <li>✅ Fully functional Django REST Framework (DRF) API</li>
    </ul>
    
    <h2>📦 Installation & Setup</h2>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/yourusername/django-faq-system.git
cd django-faq-system</code></pre>
        </li>
        <li><strong>Create a Virtual Environment</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Apply Migrations</strong>
            <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
        </li>
        <li><strong>Create a Superuser (for Admin Panel)</strong>
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li><strong>Run the Server</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
    </ol>
    
    <h2>🔧 Configuration</h2>
    <h3>1️⃣ Environment Variables</h3>
    <p>Create a <code>.env</code> file in the project root and add:</p>
    <pre><code>DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost</code></pre>
    
    <h3>2️⃣ CKEditor Configuration</h3>
    <pre><code>CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    }
}</code></pre>
    
    <h2>🎯 API Endpoints (with Language Detection)</h2>
    <h3>Get All FAQs</h3>
    <pre><code>GET /api/faqs/</code></pre>
    <h4>Response:</h4>
    <pre><code>[
  {
    "id": 1,
    "question": "¿Qué es Django?",
    "question_lang": "es",
    "translated_question": "What is Django?",
    "answer": "Django es un framework de Python.",
    "answer_lang": "es",
    "translated_answer": "Django is a Python framework."
  }
]</code></pre>
    
    <h3>Create an FAQ</h3>
    <pre><code>POST /api/faqs/</code></pre>
    <pre><code>{
  "question": "Was ist Django?",
  "answer": "Django ist ein Web-Framework für Python."
}</code></pre>
    
    <h3>Update an FAQ</h3>
    <pre><code>PUT /api/faqs/{id}/</code></pre>
    
    <h3>Delete an FAQ</h3>
    <pre><code>DELETE /api/faqs/{id}/</code></pre>
    
    <h2>🧪 Testing & Code Quality</h2>
    <h3>1️⃣ Run Django Tests</h3>
    <pre><code>python manage.py test</code></pre>
    <h3>2️⃣ Check Code Quality with Flake8</h3>
    <pre><code>pip install flake8
flake8 --max-line-length=100</code></pre>
    
    <h2>📜 Project Structure</h2>
    <pre><code>django-faq-system/
│── faqs/                     # FAQ app
│   ├── migrations/           # Database migrations
│   ├── models.py             # FAQ model
│   ├── views.py              # API views
│   ├── serializers.py        # API serializers
│   ├── urls.py               # App-specific routes
│   ├── admin.py              # Django Admin configuration
│
│── templates/                # HTML templates (if applicable)
│── static/                   # Static files (CSS, JS, Images)
│── manage.py                 # Django project management script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
│── .flake8                   # Flake8 config (optional)
│── .env                      # Environment variables (ignored in Git)</code></pre>
    
    <h2>🤝 Contributing</h2>
    <ol>
        <li>Fork this repository</li>
        <li>Create a branch for your feature: <code>git checkout -b feature-name</code></li>
        <li>Commit your changes: <code>git commit -m "Added a cool feature"</code></li>
        <li>Push to GitHub: <code>git push origin feature-name</code></li>
        <li>Create a Pull Request</li>
    </ol>
    
    <h2>⚖️ License</h2>
    <p>This project is licensed under the MIT License.</p>
    
    <h2>✨ Author</h2>
    <p>👤 Your Name<br>
    📧 your.email@example.com</p>
    
    <h2>✅ Happy Coding! 🚀</h2>
</body>
</html>

