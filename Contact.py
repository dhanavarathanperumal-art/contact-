import streamlit as st
import webbrowser
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Dhanavarathan P - Portfolio",
    page_icon="👋",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main headers */
    .main-header {
        font-size: 3rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Info box for important information */
    .info-box {
        background-color: #fff3cd;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 3px solid #ffc107;
    }
    
    /* Contact info box */
    .contact-info {
        background-color: #e7f3fe;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 5px solid #2196F3;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Development box */
    .development-box {
        background-color: #fff8e1;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px dashed #ff9800;
    }
    
    /* Website box */
    .website-box {
        background-color: #e8f5e9;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px solid #4CAF50;
    }
    
    /* Success box */
    .success-box {
        background-color: #d4edda;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px solid #28a745;
    }
    
    /* Issue box */
    .issue-box {
        background-color: #f8d7da;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px solid #dc3545;
    }
    
    /* Social media icons */
    .social-icon {
        font-size: 1.5rem;
        margin-right: 10px;
    }
    
    /* Social media buttons */
    .social-btn {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin: 5px;
        transition: all 0.3s ease;
    }
    
    .instagram-btn {
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white;
    }
    
    .github-btn {
        background-color: #333;
        color: white;
    }
    
    .email-btn {
        background-color: #D44638;
        color: white;
    }
    
    /* Social media container */
    .social-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 15px;
        margin: 20px 0;
    }
    
    /* Button styles */
    .stButton > button {
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Your information
YOUR_NAME = "Dhanavarathan P (Dhana)"
YOUR_EMAIL = "dhanavarathanperumal@gmail.com"
WEBSITE_NAME = "Rag Chat"
WEBSITE_LINK = "https://offline1rag.streamlit.app"
INSTAGRAM_LINK = "https://www.instagram.com/call._.me._.dhana?igsh=MTFrdnQ1dDV1c3BtdA=="
GITHUB_LINK = "https://github.com/dhanavarathanperumal-art"

# Function to open the website
def open_website():
    webbrowser.open(WEBSITE_LINK)
    st.success(f"Opening {WEBSITE_NAME}...")

# Function to open Instagram
def open_instagram():
    webbrowser.open(INSTAGRAM_LINK)
    st.success("Opening Instagram profile...")

# Function to open GitHub
def open_github():
    webbrowser.open(GITHUB_LINK)
    st.success("Opening GitHub profile...")

# Function for success report email
def report_app_working():
    subject = f"App Working Successfully - {WEBSITE_NAME}"
    body = f"""Hi {YOUR_NAME},

✅ GREAT NEWS! Your {WEBSITE_NAME} application is working perfectly!

I tested the app and everything is functioning as expected.

Best regards,
[Your Name]"""
    
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    webbrowser.open(mailto_link)
    st.success(f"Email opened! Please send to {YOUR_EMAIL}")

# Function for issue report email
def report_issue():
    subject = f"Issue Report - {WEBSITE_NAME} App"
    body = f"""Hi {YOUR_NAME},

⚠️ ISSUE DETECTED in your {WEBSITE_NAME} application.

Please describe the issue here:

Thank you for your attention.

Best regards,
[Your Name]"""
    
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    webbrowser.open(mailto_link)
    st.success(f"Email opened! Please send to {YOUR_EMAIL}")

# ============================
# WELCOME SECTION
# ============================
st.markdown('<h1 class="main-header">👋 Welcome to My Portfolio!</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; font-size: 1.5rem; color: #1E3A8A;">Hello! I\'m <strong>{YOUR_NAME}</strong></p>', unsafe_allow_html=True)

# Divider
st.markdown("---")

# ============================
# IMPORTANT INFORMATION SECTION
# ============================
st.markdown("### 📢 IMPORTANT INFORMATION")

# Create a container for the important info
with st.container():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #ff9800;
        margin: 20px 0;
    ">
        <h4 style="color: #d35400; margin-bottom: 15px;">
            ⚠️ Note: Even if the app works correctly, please send an email to identify that it's working properly. 
            This helps in tracking and verification.
        </h4>
        
        <h5 style="color: #1E3A8A; margin-bottom: 10px;">📧 Email Purpose:</h5>
    </div>
    """, unsafe_allow_html=True)
    
    # Email purpose items using Streamlit columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background-color: #d4edda;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #28a745;
            text-align: center;
            height: 150px;
        ">
            <h5 style="color: #155724;">✅ Confirm App Working</h5>
            <p style="color: #0c5460; font-size: 0.9rem;">
                Send success report when app functions correctly
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background-color: #f8d7da;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #dc3545;
            text-align: center;
            height: 150px;
        ">
            <h5 style="color: #721c24;">⚠️ Report Issues/Bugs</h5>
            <p style="color: #0c5460; font-size: 0.9rem;">
                Report problems encountered while using the app
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background-color: #d1ecf1;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #17a2b8;
            text-align: center;
            height: 150px;
        ">
            <h5 style="color: #0c5460;">💡 Feedback/Suggestions</h5>
            <p style="color: #0c5460; font-size: 0.9rem;">
                Share ideas for improvement or new features
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ============================
# WEBSITE LINK SECTION
# ============================
st.markdown("### 🌐 My Application")

with st.container():
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 3px solid #4CAF50;
        margin: 20px 0;
    ">
        <h3 style="color: #2E7D32;">{WEBSITE_NAME}</h3>
        <p style="font-size: 1.1rem; color: #666;">URL: {WEBSITE_LINK}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Website button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Visit My Application", use_container_width=True):
            open_website()

st.markdown("---")

# ============================
# DEVELOPMENT STATUS SECTION
# ============================
st.markdown("### 🚀 Application Status")

with st.container():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 3px dashed #ff9800;
        margin: 20px 0;
    ">
        <h4 style="color: #ff8f00;">🚧 {WEBSITE_NAME} - Active Development</h4>
        <p style="color: #5d4037;">This application is currently in active development phase.</p>
        <p style="color: #795548;">Your feedback is valuable for improving the app!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    st.write("**Development Progress:**")
    progress = st.progress(75)
    st.caption("Status: 75% complete | Active Development")

st.markdown("---")

# ============================
# CONTACT & SOCIAL MEDIA SECTION
# ============================
st.markdown("### 📞 Contact & Social Media")

# Social Media Buttons
st.markdown("""
<div style="text-align: center; margin: 20px 0;">
    <h4>Connect with me on:</h4>
</div>
""", unsafe_allow_html=True)

# Social media buttons in columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📧 Email", use_container_width=True):
        webbrowser.open(f"mailto:{YOUR_EMAIL}?subject=Hello {YOUR_NAME}")

with col2:
    if st.button("📸 Instagram", use_container_width=True):
        open_instagram()

with col3:
    if st.button("💻 GitHub", use_container_width=True):
        open_github()

with col4:
    if st.button("🌐 Website", use_container_width=True):
        open_website()

# Contact Information Details
with st.container():
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
    ">
        <h4 style="color: #1565c0; text-align: center;">👤 Contact Details</h4>
        
        <div style="display: flex; flex-direction: column; gap: 15px; margin-top: 20px;">
            <!-- Email -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #D44638;">
                <span style="font-size: 1.5rem; margin-right: 15px;">📧</span>
                <div>
                    <strong style="color: #333;">Email:</strong><br>
                    <a href="mailto:{YOUR_EMAIL}" style="color: #1a73e8; text-decoration: none;">{YOUR_EMAIL}</a>
                </div>
            </div>
            
            <!-- Instagram -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #E1306C;">
                <span style="font-size: 1.5rem; margin-right: 15px;">📸</span>
                <div>
                    <strong style="color: #333;">Instagram:</strong><br>
                    <a href="{INSTAGRAM_LINK}" target="_blank" style="color: #1a73e8; text-decoration: none;">@call._.me._.dhana</a>
                </div>
            </div>
            
            <!-- GitHub -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #333;">
                <span style="font-size: 1.5rem; margin-right: 15px;">💻</span>
                <div>
                    <strong style="color: #333;">GitHub:</strong><br>
                    <a href="{GITHUB_LINK}" target="_blank" style="color: #1a73e8; text-decoration: none;">dhanavarathanperumal-art</a>
                </div>
            </div>
            
            <!-- Website -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #4CAF50;">
                <span style="font-size: 1.5rem; margin-right: 15px;">🌐</span>
                <div>
                    <strong style="color: #333;">Website:</strong><br>
                    <a href="{WEBSITE_LINK}" target="_blank" style="color: #1a73e8; text-decoration: none;">{WEBSITE_LINK}</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick copy buttons
st.markdown("### 📋 Quick Copy Links")
copy_col1, copy_col2, copy_col3, copy_col4 = st.columns(4)

with copy_col1:
    if st.button("Copy Email", use_container_width=True):
        st.code(YOUR_EMAIL)
        st.success("Email copied!")

with copy_col2:
    if st.button("Copy Instagram", use_container_width=True):
        st.code(INSTAGRAM_LINK)
        st.success("Instagram link copied!")

with copy_col3:
    if st.button("Copy GitHub", use_container_width=True):
        st.code(GITHUB_LINK)
        st.success("GitHub link copied!")

with copy_col4:
    if st.button("Copy Website", use_container_width=True):
        st.code(WEBSITE_LINK)
        st.success("Website link copied!")

st.markdown("---")

# ============================
# EMAIL ACTION BUTTONS SECTION
# ============================
st.markdown("### 📧 Send Email Reports")

# Create two main action columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
    ">
        <h5 style="color: #155724;">✅ App Working Successfully?</h5>
        <p style="color: #0c5460;">Send confirmation that app is working correctly</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✅ Confirm App is Working", use_container_width=True, key="success_btn"):
        report_app_working()

with col2:
    st.markdown("""
    <div style="
        background-color: #f8d7da;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
    ">
        <h5 style="color: #721c24;">⚠️ Found Issues?</h5>
        <p style="color: #0c5460;">Report problems, errors, or bugs encountered</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚠️ Report Issues & Bugs", use_container_width=True, key="issue_btn"):
        report_issue()

st.markdown("---")

# ============================
# TESTING CHECKLIST SECTION
# ============================
st.markdown("### 📝 Quick Checklist")

# Create expandable checklist
with st.expander("Click to expand testing checklist"):
    st.write("**Before sending email, check these:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("App loads without errors")
        st.checkbox("Navigation works properly")
        st.checkbox("All buttons respond")
        st.checkbox("No error messages shown")
    
    with col2:
        st.checkbox("Features work as expected")
        st.checkbox("Performance is smooth")
        st.checkbox("Mobile responsive")
        st.checkbox("No crashes/freezes")

# ============================
# SOCIAL MEDIA LINKS DISPLAY
# ============================
st.markdown("---")
st.markdown("### 🔗 Quick Social Media Access")

# Display social media links with icons
st.markdown(f"""
<div style="
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 15px;
    margin: 20px 0;
">
    <a href="mailto:{YOUR_EMAIL}" style="
        display: inline-flex;
        align-items: center;
        background-color: #D44638;
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    ">
        📧 Email Me
    </a>
    
    <a href="{INSTAGRAM_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    ">
        📸 Instagram
    </a>
    
    <a href="{GITHUB_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background-color: #333;
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    ">
        💻 GitHub
    </a>
    
    <a href="{WEBSITE_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    ">
        🌐 My App
    </a>
</div>
""", unsafe_allow_html=True)

# ============================
# FOOTER SECTION
# ============================
st.markdown("---")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(f"""
<div style="
    text-align: center;
    color: #666;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 10px;
    margin-top: 30px;
">
    <p>© {datetime.now().year} | Created by {YOUR_NAME}</p>
    <p style="font-size: 0.9rem;">Last updated: {current_time}</p>
    
    <div style="display: flex; justify-content: center; gap: 20px; margin: 15px 0;">
        <a href="{INSTAGRAM_LINK}" target="_blank" style="color: #E1306C; text-decoration: none;">📸 Instagram</a>
        <a href="{GITHUB_LINK}" target="_blank" style="color: #333; text-decoration: none;">💻 GitHub</a>
        <a href="mailto:{YOUR_EMAIL}" style="color: #D44638; text-decoration: none;">📧 Email</a>
        <a href="{WEBSITE_LINK}" target="_blank" style="color: #4CAF50; text-decoration: none;">🌐 Website</a>
    </div>
    
    <p style="font-size: 0.8rem; color: #ff9800;">
        ⚠️ <strong>Important:</strong> Even if app works, please send email confirmation to {YOUR_EMAIL}
    </p>
</div>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR INFORMATION
# ============================
with st.sidebar:
    st.markdown("### ℹ️ Quick Info")
    st.info(f"""
    **App:** {WEBSITE_NAME}
    **Developer:** {YOUR_NAME}
    **Email:** {YOUR_EMAIL}
    **Status:** Active Development
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔗 Quick Links")
    if st.button("📸 Instagram", use_container_width=True):
        open_instagram()
    
    if st.button("💻 GitHub", use_container_width=True):
        open_github()
    
    if st.button("🌐 Website", use_container_width=True):
        open_website()
    
    st.markdown("---")
    
    st.markdown("### 📧 Email Actions")
    if st.button("✅ Success Report", use_container_width=True):
        report_app_working()
    
    if st.button("⚠️ Issue Report", use_container_width=True):
        report_issue()
    
    st.markdown("---")
    
    st.markdown("""
    **📝 Remember:**
    1. Test the website first
    2. Send email report (success or issue)
    3. Include details in email
    4. Your feedback helps improve!
    """)
