import streamlit as st
import os
import json
from PIL import Image
from pathlib import Path
import base64
from io import BytesIO
import urllib.parse

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION & THEME
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Swati's Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'gallery_page' not in st.session_state:
    st.session_state.gallery_page = 1

# Advanced CSS with animations and modern design
def inject_custom_css():
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Variables */
        :root {
            --primary-blue: #4A90E2;
            --secondary-blue: #357ABD;
            --accent-cyan: #00D4FF;
            --bg-dark: #0A0E27;
            --bg-secondary: #1A1F3A;
            --text-white: #FFFFFF;
            --text-gray: #B8BCC8;
            --card-bg: rgba(26, 31, 58, 0.8);
            --glass-bg: rgba(255, 255, 255, 0.1);
        }
        
        /* Main App Styling */
        .stApp {
            background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-secondary) 100%);
            color: var(--text-white);
            font-family: 'Inter', sans-serif;
        }
        
        /* Animated Background */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 50%, rgba(74, 144, 226, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(0, 212, 255, 0.1) 0%, transparent 50%);
            z-index: -1;
            animation: backgroundFlow 20s ease-in-out infinite alternate;
        }
        
        @keyframes backgroundFlow {
            0% { transform: translateX(-20px) translateY(-20px); }
            100% { transform: translateX(20px) translateY(20px); }
        }
        
        /* Modern Card Styling */
        .portfolio-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .portfolio-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-cyan));
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        
        .portfolio-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(74, 144, 226, 0.2);
        }
        
        .portfolio-card:hover::before {
            transform: scaleX(1);
        }
        
        /* Interactive Headers - FIXED: Only apply gradient to text, not emojis */
        h1 span.text-gradient, 
        h2 span.text-gradient, 
        h3 span.text-gradient {
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
        }
        
        h1, h2, h3 {
            font-weight: 600;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        /* Make emojis use system emoji font */
        .emoji {
            font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
            background: none !important;
            -webkit-text-fill-color: initial !important;
        }
        
        /* Preserve emoji appearance in sidebar */
        .stRadio label div {
            font-family: 'Inter', "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
        }
        
        /* Skill Bars */
        .skill-bar {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
            margin: 0.5rem 0;
        }
        
        .skill-progress {
            height: 8px;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-cyan));
            border-radius: 10px;
            animation: fillBar 1.5s ease-out;
        }
        
        @keyframes fillBar {
            from { width: 0%; }
        }
        
        a.custom-button {
            color: white !important;
            }
        
        a.custom-button:hover {
            color: white !important;
            }        
        
        /* Interactive Buttons */
        .custom-button {
            background: linear-gradient(200deg, var(--primary-blue), var(--secondary-blue));
            border: none;
            border-radius: 50px;
            color: white;
            padding: 12px 30px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        
        .custom-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(74, 144, 226, 0.3);
        }
        
        /* Gallery Grid */
        .gallery-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            padding: 20px 0;
        }
        
        .gallery-item {
            position: relative;
            border-radius: 15px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s ease;
            height: 200px;
            background: rgba(255, 255, 255, 0.05);
        }
        
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        }
        
        .gallery-item:hover img {
            transform: scale(1.1);
        }
        
        .gallery-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, rgba(74, 144, 226, 0.8), rgba(0, 212, 255, 0.8));
            opacity: 0;
            transition: opacity 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            text-align: center;
            padding: 20px;
        }
        
        .gallery-item:hover .gallery-overlay {
            opacity: 1;
        }
        
        /* Image Modal */
        .gallery-link {
            text-decoration: none;
            color: inherit;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 10000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.9);
        }
        .modal:target {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .modal-content {
            position: relative;
            margin: auto;
            padding: 20px;
            width: 90%;
            max-width: 900px;
        }
        .modal-content img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            max-height: 80vh;
        }
        /* FIXED: Position close button at top right of viewport */
        .close {
            position: fixed;
            top: 30px;
            right: 40px;
            color: white;
            font-size: 50px;
            font-weight: bold;
            text-decoration: none;
            z-index: 10001;
            text-shadow: 0 0 10px rgba(0,0,0,0.5);
            transition: all 0.2s ease;
        }
        .close:hover {
            color: #FF4B4B;
            cursor: pointer;
            transform: scale(1.1);
        }
        
        .pagination-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
        
        .pagination-btn {
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
            color: white;
            border: none;
            border-radius: 50px;
            padding: 8px 20px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .pagination-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(74, 144, 226, 0.4);
        }
        
        .pagination-btn:disabled {
            background: #555;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        /* Sidebar Styling */
        .css-1d391kg {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
        }
        
        /* Achievement Badges */
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 5px;
            animation: badgeGlow 2s ease-in-out infinite alternate;
        }
        
        @keyframes badgeGlow {
            0% { box-shadow: 0 0 5px rgba(74, 144, 226, 0.5); }
            100% { box-shadow: 0 0 20px rgba(74, 144, 226, 0.8); }
        }
        
        /* Custom Timeline Styling */
        .timeline-container {
            position: relative;
            padding: 20px 0;
            margin: 40px 0;
        }
        
        .timeline-container::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            left: 50%;
            width: 4px;
            background: linear-gradient(to bottom, var(--primary-blue), var(--accent-cyan));
            border-radius: 2px;
            transform: translateX(-50%);
        }
        
        .timeline-event {
            position: relative;
            margin-bottom: 60px;
            width: 45%;
        }
        
        .timeline-event:nth-child(odd) {
            left: 0;
        }
        
        .timeline-event:nth-child(even) {
            left: 55%;
        }
        
        .timeline-content {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            position: relative;
            transition: all 0.3s ease;
        }
        
        .timeline-content:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }
        
        .timeline-date {
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 15px;
            font-size: 0.9rem;
        }
        
        .timeline-content::before {
            content: '';
            position: absolute;
            top: 20px;
            right: -10px;
            width: 0;
            height: 0;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-left: 10px solid var(--card-bg);
        }
        
        .timeline-event:nth-child(even) .timeline-content::before {
            left: -10px;
            right: auto;
            border-left: none;
            border-right: 10px solid var(--card-bg);
        }
        
        .timeline-dot {
            position: absolute;
            top: 25px;
            right: -13px;
            width: 20px;
            height: 20px;
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
            border-radius: 50%;
            z-index: 1;
        }
        
        .timeline-event:nth-child(even) .timeline-dot {
            left: -13px;
            right: auto;
        }
    </style>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def get_image_base64(image_path, max_size=None, quality=85):
    """Load and optimize an image for web display"""
    try:
        img = Image.open(image_path)
        return image_to_base64(img, quality, max_size)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def create_skill_bar(skill_name, percentage):
    return f"""
    <div style="margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span>{skill_name}</span>
            <span>{percentage}%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-progress" style="width: {percentage}%;"></div>
        </div>
    </div>
    """

def create_project_card(title, description, tech_stack, link=None):
    link_html = f'<a href="{link}" class="custom-button" target="_blank" style="color: white !important;">View Project</a>' if link else ""
    return f"""
     <div class="portfolio-card">
        <h3>{title}</h3>
        <p style="color: var(--text-gray); margin: 15px 0;">{description}</p>
        <div style="margin: 15px 0;">
            {''.join([f'<span class="badge">{tech}</span>' for tech in tech_stack])}
        </div>
        {link_html}
    </div>
    """

def image_to_base64(image, quality=85, max_size=None):
    buffered = BytesIO()
    
    # Optimize image for web
    if max_size:
        width, height = image.size
        if width > max_size or height > max_size:
            ratio = min(max_size/width, max_size/height)
            new_size = (int(width * ratio), int(height * ratio))
            image = image.resize(new_size, Image.LANCZOS)
    
    # Save with optimization
    image.save(buffered, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buffered.getvalue()).decode()

def generate_thumbnail(image_path, max_size=300):
    """Generate optimized thumbnail with lazy loading"""
    try:
        img = Image.open(image_path)
        return image_to_base64(img, quality=50, max_size=max_size)
    except Exception as e:
        st.error(f"Error generating thumbnail: {e}")
        return None

def load_full_image(image_path):
    """Load full image only when needed"""
    try:
        img = Image.open(image_path)
        return image_to_base64(img, quality=90)
    except Exception as e:
        st.error(f"Error loading full image: {e}")
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE FUNCTIONS (WITH FIXED GALLERY)
# ═══════════════════════════════════════════════════════════════════════════════

def show_hero_section():
    st.markdown('<div class="">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Load and display profile image
        profile_img = get_image_base64("profile.jpeg", max_size=200)
        
        if profile_img:
            st.markdown(f"""
            <div style="width: 200px; height: 200px; border-radius: 50%; 
                        background: linear-gradient(135deg, #4A90E2, #00D4FF);
                        margin: 0 auto; overflow: hidden; border: 3px solid rgba(255,255,255,0.2)">
                <img src="data:image/jpeg;base64,{profile_img}" 
                    style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback to emoji if image missing
            st.markdown("""
            <div style="width: 200px; height: 200px; border-radius: 50%; 
                        background: linear-gradient(135deg, #4A90E2, #00D4FF);
                        margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 80px;">👩‍💻</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
            <h1 style="display: block; text-align: center;">Swati Gulati</h1>
            <h3 style="color: var(--text-gray); display: block; text-align: center;">IT Trainer | Data Science | Gen-AI</h3>
            <p style="font-size: 1.1rem; margin: 20px 0;">
                🚀 2+ years delivering high-impact AI, ML, and Gen-AI Programs<br>
                📍 Delhi, India | 💼 200+ Professionals Trained
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive buttons row
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            st.link_button("📧 Contact", "#contact-section")
        
        with col_btn2:
            st.download_button(
                "📄 Resume",
                data=open("Swati_Gulati_Technical_Trainer_Resume.pdf", "rb").read(),
                file_name="Swati_Gulati_Technical_Trainer_Resume.pdf",
                mime="application/pdf"
            )
        
        with col_btn3:
            st.link_button("🔗 LinkedIn", "https://linkedin.com/in/iamswatigulati")
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_about_skills():
    st.markdown("""
    <h2>
        <span class="emoji">🎯</span>
        <span class="text-gradient">Professional Summary</span>
    </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="portfolio-card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            IT Technologies Trainer with 2+ years delivering high-impact AI, ML, and Gen-AI Programs, 
            including specialized training in Prompt Engineering Techniques. Designed and delivered 
            technical curriculum for 200+ professionals across diverse industries. Certified Data Analyst 
            with expertise in Gen-AI Applications and Predictive Analytics. Passionate Self-Taught Programmer 
            and Continuous Learner focused on cutting-edge AI upskilling.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2>
        <span class="emoji">💻</span>
        <span class="text-gradient">Core Skills & Expertise</span>
    </h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Technical Skills")
        st.markdown("""
        <div class="portfolio-card">
            {python_bar}
            {sql_bar}
            {htmlcss_bar}
            {data_analysis_bar}
            {ml_bar}
            {prompt_bar}
        
        """.format(
            python_bar=create_skill_bar("Python and JavaScript", 95),
            sql_bar=create_skill_bar("SQL", 85),
            htmlcss_bar=create_skill_bar("HTML5/CSS3", 80),
            data_analysis_bar=create_skill_bar("Data Analysis", 92),
            ml_bar=create_skill_bar("Machine Learning", 88),
            prompt_bar=create_skill_bar("Prompt Engineering", 85)
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Tools & Platforms")
        st.markdown("""
        <div class="portfolio-card">
            {powerbi_bar}
            {tf_keras_bar}
            {git_bar}
            {cloud_bar}
            {web_bar}
            {msoffice_bar}
        
        """.format(
            powerbi_bar=create_skill_bar("Power BI", 90),
            tf_keras_bar=create_skill_bar("TensorFlow/Keras", 88),
            git_bar=create_skill_bar("Git/GitHub", 85),
            cloud_bar=create_skill_bar("IBM Cloud", 80),
            web_bar=create_skill_bar("Web Development", 75),
            msoffice_bar=create_skill_bar("MS Office", 90)
        ), unsafe_allow_html=True)

def show_experience_timeline():
    st.markdown("""
    <h2>
        <span class="emoji">💼</span>
        <span class="text-gradient">Professional Journey</span>
    </h2>
    """, unsafe_allow_html=True)
    
    # Career timeline data
    timeline_data = [
        {
            "start_date": "Sep 2022",
            "end_date": "Jun 2025",
            "title": "Subject Matter Expert (IT Training)",
            "company": "Edunet Foundation",
            "description": [
                "Certified by the Great Place To Work®, an organization that works with Top Global Corporations & the Indian Government.",
                "Delivered AI/Data Science Courses/Workshops for IBM and Microsoft programs.",
                "Created technical curriculum for 200+ professionals."
            ]
        },
        {
            "start_date": "Sep 2021",
            "end_date": "Feb 2022",
            "title": "Artificial Intelligence Intern",
            "company": "IBM India Pvt. Ltd.",
            "description": [
                "Developed brain-tumor detection system (92% accuracy).",
                "Led 5-member AI team.",
                "Created reusable AI knowledge base."
            ]
        }
    ]
    
    # Render timeline using Streamlit components
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    
    for event in timeline_data:
        with st.container():
            st.markdown(f"""
            <div class="timeline-event">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <span class="timeline-date">{event['start_date']} - {event['end_date']}</span>
                    <h3>{event['title']}</h3>
                    <p><strong>{event['company']}</strong></p>
            """, unsafe_allow_html=True)
            
            with st.expander("Details", expanded=True):
                for item in event['description']:
                    st.markdown(f"• {item}")
            
            st.markdown("""
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_projects_showcase():
    st.markdown("""
    <h2>
        <span class="emoji">🛠️</span>
        <span class="text-gradient">Featured Projects</span>
    </h2>
    """, unsafe_allow_html=True)
    
    # Project cards with enhanced styling
    projects = [
        {
            "title": "AI-Based Brain Tumor Detection System",
            "description": "Developed an end-to-end medical-image AI solution with Python, TensorFlow/Keras, OpenCV, and CNNs achieving 92% accuracy. Built robust preprocessing pipelines and clinical interface.",
            "tech_stack": ["Python", "TensorFlow", "OpenCV", "CNNs", "Medical Imaging"],
            "link": "https://nostalgic-wright-bf9840.netlify.app/"
        },
        {
            "title": "COVID-19 Data Analysis & Prediction",
            "description": "Analyzed COVID-19 datasets using Python, Pandas, and statistical methods to create predictive models with 85% accuracy for Germany. Developed interactive visualizations with Matplotlib/Seaborn.",
            "tech_stack": ["Python", "Pandas", "Matplotlib", "Statistical Modeling"],
            "link": "https://iamswati.github.io/covid_19_project/"
        },
        {
            "title": "Gold Price Prediction",
            "description": "Project is to build a Machine Learning system that can predict gold prices based on several other stock prices. Find the Correlation of the other features with GLD (gold) price and predict it",
            "tech_stack": ["Time Series Data, Pedictive Analysis"],
            "link": "https://iamswati.github.io/data_analysis_gold_price/"
        },
        {
            "title": "EDA on Loan Payments Data",
            "description": "Analyzed initial Analysis and EDA (Exploratory Data Analysis) on Loan Payments Data.",
            "tech_stack": ["Data Analysis, Data Visulaization"],
            "link": "https://iamswati.github.io/eda-loan/"
        },
         {
            "title": "Send Text Message(FAST2SMS)",
            "description": "It is about sending text messages to the registered phone number using FAST2SMS.",
            "tech_stack": ["Python Project"],
            "link": "https://github.com/iamswati/Send_text_msg"
        }
    ]
    
    for project in projects:
        st.markdown(create_project_card(**project), unsafe_allow_html=True)

def show_interactive_gallery():
    st.markdown("""
    <h2>
        <span class="emoji">📸</span>
        <span class="text-gradient">Training Sessions Gallery</span>
    </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="portfolio-card">
        <p style="color: var(--text-gray);">
            Snapshots from various training sessions, workshops, and professional engagements. 
            Each image tells a story of knowledge sharing and skill development.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Gallery controls
    col1, col2 = st.columns([2, 1])
    with col1:
        sort_option = st.selectbox("📋 Sort by", ["Newest", "Oldest", "A-Z", "Z-A"])
    with col2:
        view_style = st.radio("👁️ View", ["Grid", "List"], horizontal=True, key="gallery_view")
    
    # Get all images from gallery directory
    gallery_path = Path("gallery")
    image_files = []
    
    if gallery_path.exists() and gallery_path.is_dir():
        for ext in ["*.jpg", "*.jpeg", "*.png", "*.webp"]:
            image_files.extend(gallery_path.glob(ext))
        
        # Apply sorting
        if sort_option == "Newest":
            image_files.sort(key=os.path.getmtime, reverse=True)
        elif sort_option == "Oldest":
            image_files.sort(key=os.path.getmtime)
        elif sort_option == "A-Z":
            image_files.sort(key=lambda x: x.name)
        elif sort_option == "Z-A":
            image_files.sort(key=lambda x: x.name, reverse=True)
        
        if not image_files:
            st.info("🔍 No images found matching your search criteria")
            return
            
        # Pagination settings
        items_per_page = 9 if view_style == "Grid" else 6
        total_pages = (len(image_files) // items_per_page + (1 if len(image_files) % items_per_page else 0))
        
        # Pagination buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.session_state.gallery_page > 1:
                if st.button("⬅️ Previous", key="prev_page", use_container_width=True):
                    st.session_state.gallery_page -= 1
                    st.rerun()
        with col2:
            st.markdown(f"<div style='text-align: center; padding: 10px;'>Page {st.session_state.gallery_page} of {total_pages}</div>", 
                        unsafe_allow_html=True)
        with col3:
            if st.session_state.gallery_page < total_pages:
                if st.button("Next ➡️", key="next_page", use_container_width=True):
                    st.session_state.gallery_page += 1
                    st.rerun()
        
        # Calculate current page items
        start_idx = (st.session_state.gallery_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(image_files))
        current_page_images = image_files[start_idx:end_idx]
        
        # Show image grid or list
        if view_style == "Grid":
            cols = st.columns(3)
            col_index = 0
            
            # Collect modals HTML
            modals_html = ""
            
            for i, img_path in enumerate(current_page_images):
                try:
                    # Generate thumbnail (optimized, low resolution)
                    thumb_b64 = generate_thumbnail(img_path, max_size=300)
                    
                    if thumb_b64:
                        with cols[col_index]:
                            # Create unique modal ID for this image
                            modal_id = f"modal-{start_idx + i}"
                            
                            # Create clickable image that opens modal
                            st.markdown(f"""
                            <div style="margin-bottom: 30px;">  <!-- ADDED MARGIN CONTAINER -->
                                <a href="#{modal_id}" class="gallery-link">
                                    <div class="gallery-item">
                                        <img src="data:image/jpeg;base64,{thumb_b64}" alt="">
                                        <div class="gallery-overlay">
                                            <!-- Empty overlay - no text -->
                                        </div>
                                    </div>
                                </a>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Generate modal HTML
                        full_b64 = load_full_image(img_path)
                        if full_b64:
                            modals_html += f"""
                            <div id="{modal_id}" class="modal">
                                <div class="modal-content">
                                    <a href="#" class="close">&times;</a>
                                    <img src="data:image/jpeg;base64,{full_b64}" alt="Full-size image">
                                </div>
                            </div>
                            """
                        
                        col_index = (col_index + 1) % 3
                except Exception as e:
                    st.error(f"Error loading image: {img_path.name}")
            
            # Render all modals at the end
            st.markdown(modals_html, unsafe_allow_html=True)
        else:
            # List view
            for img_path in current_page_images:
                with st.expander(f"📷 {img_path.stem.replace('_', ' ').title()}", expanded=False):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        try:
                            # Generate thumbnail (optimized, low resolution)
                            thumb_b64 = generate_thumbnail(img_path, max_size=300)
                            
                            if thumb_b64:
                                # Create unique modal ID for this image
                                modal_id = f"modal-{img_path.name}"
                                
                                # Create clickable image that opens modal
                                st.markdown(f"""
                                <a href="#{modal_id}" class="gallery-link">
                                    <div class="gallery-item">
                                        <img src="data:image/jpeg;base64,{thumb_b64}" alt="" style="width:100%;">
                                    </div>
                                </a>
                                """, unsafe_allow_html=True)
                                
                                # Generate modal HTML
                                full_b64 = load_full_image(img_path)
                                if full_b64:
                                    st.markdown(f"""
                                    <div id="{modal_id}" class="modal">
                                        <div class="modal-content">
                                            <a href="#" class="close">&times;</a>
                                            <img src="data:image/jpeg;base64,{full_b64}" alt="Full-size image">
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error loading image: {img_path.name}")
                    with col2:
                        st.write(f"**Filename:** {img_path.name}")
                        st.write(f"**Size:** {img_path.stat().st_size // 1024} KB")
                        st.write(f"**Session:** {img_path.stem.replace('_', ' ').title()}")
    else:
        # Create gallery directory if it doesn't exist
        gallery_path.mkdir(exist_ok=True)
        st.markdown("""
        <div class="portfolio-card" style="text-align: center;">
            <h3>📁 Gallery Directory Created</h3>
            <p style="color: var(--text-gray);">
                Add your training session photos to the <code>gallery</code> folder.<br>
                Supported formats: JPG, JPEG, PNG, WEBP
            </p>
        </div>
        """, unsafe_allow_html=True)

def show_achievements():
    st.markdown("""
    <h2>
        <span class="emoji">🏆</span>
        <span class="text-gradient">Certifications & Achievements</span>
    </h2>
    """, unsafe_allow_html=True)
    
    achievements_data = [
        {"title": "IBM Certified Data Analyst", "year": "2022", "issuer": "IBM & Think-it"},
        {"title": "19+ IBM Digital Badges", "year": "2021-2022", "issuer": "IBM SkillsBuild"},
        {"title": "9th All-India Female Rank (84.2%)", "year": "2022", "issuer": "Advanced Diploma in IT, Networking & Cloud Computing NSTI-DGT (Govt. of India)"},
        {"title": "Featured on IBM SkillsBuild", "year": "2021", "issuer": "For COVID-19 Analytics Project"}
    ]
    
    # Interactive achievement showcase
    for achievement in achievements_data:
        st.markdown(f"""
        <div class="portfolio-card">
            <h4>🎖️ {achievement['title']}</h4>
            <p><strong>{achievement['issuer']}</strong> • {achievement['year']}</p>
        </div>
        """, unsafe_allow_html=True)

def show_contact_form():
    st.markdown("""<a name="contact-section"></a>""", unsafe_allow_html=True)
    st.markdown("""
    <h2>
        <span class="emoji">📬</span>
        <span class="text-gradient">Get In Touch</span>
    </h2>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="portfolio-card" style="text-align: center;">
            <h3>Let's Collaborate!</h3>
            <p style="color: var(--text-gray); margin: 20px 0; font-size: 1.1rem;">
                I'm always excited to discuss new opportunities in AI training, 
                curriculum design, and innovative technology projects.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📍 Contact Details")
            st.markdown("**📧 Email:**  \nswatigulati@outlook.in")
            st.markdown("**📱 Phone:**  \n+91 930 697 9702")
            st.markdown("**🌍 Location:**  \nDelhi, India")
        
        with col2:
            st.subheader("🔗 Connect With Me")
            st.markdown("**LinkedIn:**  \n[iamswatigulati](https://linkedin.com/in/iamswatigulati)")
            st.markdown("**Portfolio:**  \n[View Online](https://tinyurl.com/swati-portfolio)")
            st.markdown("**GitHub:**  \n[iamswati](https://github.com/iamswati)")
        
        # Buttons
        st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            st.link_button("📧 Email Me", "mailto:swatigulati@outlook.in")
        with col_btn2:
            st.link_button("🔗 LinkedIn", "https://linkedin.com/in/iamswatigulati")
        with col_btn3:
            st.link_button("🐙 GitHub", "https://github.com/iamswati")
        st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    inject_custom_css()
    
    # Enhanced Sidebar with profile
    with st.sidebar:
        # Load sidebar profile image
        sidebar_img = get_image_base64("profile.jpeg", max_size=120)
        
        if sidebar_img:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <div style="width: 120px; height: 120px; border-radius: 50%; 
                            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
                            margin: 0 auto 20px; overflow: hidden; border: 2px solid rgba(255,255,255,0.2);">
                    <img src="data:image/jpeg;base64,{sidebar_img}" 
                        style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <h2 style="display: block; text-align: center;">Swati Gulati</h2>   
                <p style="color: var(--text-gray);">🎯 Self-Taught Programmer</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback to emoji
            st.markdown("""
            <div style="text-align: center; padding: 20px;">
                <div style="width: 120px; height: 120px; border-radius: 50%; 
                            background: linear-gradient(135deg, var(--primary-blue), var(--accent-cyan));
                            margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 48px;">👩‍💻</span>
                </div>
                <h2 style="display: block; text-align: center;">Swati Gulati</h2>
                <p style="color: var(--text-gray);">🎯 Self-Taught Programmer</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Navigation with icons
        page = st.radio(
            "🧭 Navigation",
            [
                "🏠 Home",
                "👤 About & Skills", 
                "💼 Experience",
                "🛠️ Projects",
                "📸 Gallery",
                "🏆 Achievements",
                "📬 Contact"
            ],
            key="navigation"
        )
        
        # Sidebar footer
        st.markdown("""
        <div style="position: fixed; bottom: 20px; text-align: center;">
            <p style="font-size: 0.8rem; color: var(--text-gray);">
                © 2025 Swati Gulati<br>
                Built with ❤️ using Streamlit
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content routing
    if page == "🏠 Home":
        show_hero_section()
    elif page == "👤 About & Skills":
        show_about_skills()
    elif page == "💼 Experience":
        show_experience_timeline()
    elif page == "🛠️ Projects":
        show_projects_showcase()
    elif page == "📸 Gallery":
        show_interactive_gallery()
    elif page == "🏆 Achievements":
        show_achievements()
    elif page == "📬 Contact":
        show_contact_form()

if __name__ == "__main__":
    main()
