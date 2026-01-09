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
    
    /* WhatsApp specific styles */
    .whatsapp-btn {
        background-color: #25D366;
        color: white;
    }
    
    /* Button styles */
    .stButton > button {
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Your information
YOUR_NAME = "Dhanavarathan P (Dhana)"
YOUR_EMAIL = "dhanavarathanperumal@gmail.com"
YOUR_PHONE = "9500343825"
WEBSITE_NAME = "Rag Chat"
WEBSITE_LINK = "https://offline1rag.streamlit.app"
INSTAGRAM_LINK = "https://www.instagram.com/call._.me._.dhana?igsh=MTFrdnQ1dDV1c3BtdA=="
GITHUB_LINK = "https://github.com/dhanavarathanperumal-art"
WHATSAPP_LINK = f"https://wa.me/{YOUR_PHONE}"

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

# Function to open WhatsApp
def open_whatsapp():
    webbrowser.open(WHATSAPP_LINK)
    st.success("Opening WhatsApp...")

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
st.markdown("### 📞 Contact Information")

# Contact cards in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        border: 2px solid #2196F3;
    ">
        <h5 style="color: #1565c0;">👤 Personal Details</h5>
        <p style="font-size: 1.2rem; color: #0d47a1;"><strong>{YOUR_NAME}</strong></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 10px 0;
        border: 2px solid #4CAF50;
    ">
        <h5 style="color: #2E7D32;">📱 Mobile Number</h5>
        <p style="font-size: 1.3rem; color: #1B5E20;"><strong>{YOUR_PHONE}</strong></p>
        <p style="color: #666; font-size: 0.9rem;">For WhatsApp & Calls</p>
    </div>
    """, unsafe_allow_html=True)

# Contact Information Details
with st.container():
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
    ">
        <h4 style="color: #495057; text-align: center; margin-bottom: 25px;">📱 Contact Channels</h4>
        
        <div style="display: flex; flex-direction: column; gap: 15px; margin-top: 20px;">
            <!-- Email -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #D44638; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.8rem; margin-right: 20px; color: #D44638;">📧</span>
                <div style="flex-grow: 1;">
                    <strong style="color: #333; font-size: 1.1rem;">Email</strong><br>
                    <span style="color: #666;">{YOUR_EMAIL}</span>
                </div>
            </div>
            
            <!-- WhatsApp -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #25D366; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.8rem; margin-right: 20px; color: #25D366;">💬</span>
                <div style="flex-grow: 1;">
                    <strong style="color: #333; font-size: 1.1rem;">WhatsApp / Phone</strong><br>
                    <span style="color: #666;">{YOUR_PHONE}</span>
                </div>
            </div>
            
            <!-- Instagram -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #E1306C; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.8rem; margin-right: 20px; color: #E1306C;">📸</span>
                <div style="flex-grow: 1;">
                    <strong style="color: #333; font-size: 1.1rem;">Instagram</strong><br>
                    <span style="color: #666;">@call._.me._.dhana</span>
                </div>
            </div>
            
            <!-- GitHub -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.8rem; margin-right: 20px; color: #333;">💻</span>
                <div style="flex-grow: 1;">
                    <strong style="color: #333; font-size: 1.1rem;">GitHub</strong><br>
                    <span style="color: #666;">dhanavarathanperumal-art</span>
                </div>
            </div>
            
            <!-- Website -->
            <div style="display: flex; align-items: center; background-color: white; padding: 15px; border-radius: 10px; border-left: 5px solid #4CAF50; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.8rem; margin-right: 20px; color: #4CAF50;">🌐</span>
                <div style="flex-grow: 1;">
                    <strong style="color: #333; font-size: 1.1rem;">Website</strong><br>
                    <span style="color: #666;">{WEBSITE_LINK}</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick contact buttons
st.markdown("### 🚀 Quick Contact Actions")
contact_col1, contact_col2, contact_col3, contact_col4, contact_col5 = st.columns(5)

with contact_col1:
    if st.button("📧 Email", use_container_width=True):
        webbrowser.open(f"mailto:{YOUR_EMAIL}?subject=Hello%20{YOUR_NAME}")

with contact_col2:
    if st.button("💬 WhatsApp", use_container_width=True):
        open_whatsapp()

with contact_col3:
    if st.button("📸 Instagram", use_container_width=True):
        open_instagram()

with contact_col4:
    if st.button("💻 GitHub", use_container_width=True):
        open_github()

with contact_col5:
    if st.button("🌐 Website", use_container_width=True):
        open_website()

# Copy buttons
st.markdown("### 📋 Copy Contact Details")
copy_col1, copy_col2, copy_col3, copy_col4, copy_col5 = st.columns(5)

with copy_col1:
    if st.button("Copy Email", use_container_width=True):
        st.code(YOUR_EMAIL)
        st.success("Email copied!")

with copy_col2:
    if st.button("Copy Phone", use_container_width=True):
        st.code(YOUR_PHONE)
        st.success("Phone number copied!")

with copy_col3:
    if st.button("Copy Instagram", use_container_width=True):
        st.code(INSTAGRAM_LINK)
        st.success("Instagram link copied!")

with copy_col4:
    if st.button("Copy GitHub", use_container_width=True):
        st.code(GITHUB_LINK)
        st.success("GitHub link copied!")

with copy_col5:
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
# CONTACT LINKS DISPLAY
# ============================
st.markdown("---")
st.markdown("### 🔗 Quick Access Links")

# Display contact links with icons
st.markdown(f"""
<div style="
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 10px;
    margin: 20px 0;
">
    <a href="mailto:{YOUR_EMAIL}" style="
        display: inline-flex;
        align-items: center;
        background-color: #D44638;
        color: white;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    ">
        📧 Email
    </a>
    
    <a href="{WHATSAPP_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background-color: #25D366;
        color: white;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    ">
        💬 WhatsApp
    </a>
    
    <a href="{INSTAGRAM_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    ">
        📸 Instagram
    </a>
    
    <a href="{GITHUB_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background-color: #333;
        color: white;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    ">
        💻 GitHub
    </a>
    
    <a href="{WEBSITE_LINK}" target="_blank" style="
        display: inline-flex;
        align-items: center;
        background-color: #4CAF50;
        color: white;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    ">
        🌐 Website
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
    
    <div style="display: flex; justify-content: center; gap: 15px; margin: 15px 0; flex-wrap: wrap;">
        <span style="color: #D44638;">📧 {YOUR_EMAIL}</span>
        <span style="color: #25D366;">💬 {YOUR_PHONE}</span>
        <a href="{INSTAGRAM_LINK}" target="_blank" style="color: #E1306C; text-decoration: none;">📸 Instagram</a>
        <a href="{GITHUB_LINK}" target="_blank" style="color: #333; text-decoration: none;">💻 GitHub</a>
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
    **Name:** {YOUR_NAME}
    **Email:** {YOUR_EMAIL}
    **Phone:** {YOUR_PHONE}
    **App:** {WEBSITE_NAME}
    **Status:** Active Development
    """)
    
    st.markdown("---")
    
    st.markdown("### 📞 Quick Contact")
    if st.button("📧 Send Email", use_container_width=True):
        webbrowser.open(f"mailto:{YOUR_EMAIL}?subject=Hello%20{YOUR_NAME}")
    
    if st.button("💬 WhatsApp", use_container_width=True):
        open_whatsapp()
    
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
