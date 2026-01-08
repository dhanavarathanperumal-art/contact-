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
    .main-header {
        font-size: 3rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .contact-info {
        background-color: #f0f2f6;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 5px solid #1E3A8A;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .development-box {
        background-color: #fff8e1;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px dashed #ff9800;
    }
    .success-box {
        background-color: #e8f5e9;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px solid #4CAF50;
    }
    .issue-box {
        background-color: #ffebee;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 3px solid #f44336;
    }
    .credentials {
        font-size: 1.3rem;
        color: #333;
        text-align: center;
        margin: 15px 0;
    }
    .name-highlight {
        color: #FF4B4B;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .success-button {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        padding: 15px 30px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
    }
    .success-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(76, 175, 80, 0.4);
    }
    .issue-button {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
        padding: 15px 30px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
    }
    .issue-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(255, 65, 108, 0.4);
    }
    .construction-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .success-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
        color: #4CAF50;
    }
    .warning-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
        color: #f44336;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid #2196F3;
    }
</style>
""", unsafe_allow_html=True)

# Your information - UPDATED WITH YOUR DETAILS
YOUR_NAME = "Dhanavarathan P (Dhana)"
YOUR_EMAIL = "dhanavarathanperumal@gmail.com"
WEBSITE_NAME = "Rag Chat"

# Function to open email client for successful app working
def report_app_working():
    subject = f"App Working Successfully - {WEBSITE_NAME}"
    body = f"""Hi {YOUR_NAME},

✅ GREAT NEWS! Your {WEBSITE_NAME} application is working perfectly!

I tested the app and everything is functioning as expected. Here are my observations:

**Application Status:**
✓ All features working properly
✓ No errors encountered
✓ Smooth performance
✓ User-friendly interface

**Test Details:**
- Date: {datetime.now().strftime('%Y-%m-%d')}
- Time: {datetime.now().strftime('%H:%M:%S')}
- Test Environment: [Your Testing Environment]

**Additional Feedback:**
[Add any positive feedback or suggestions here]

**Verification Status:**
🟢 APP IS WORKING CORRECTLY

Great job on the development! Looking forward to seeing more updates.

Best regards,
[Your Name]
[Your Contact Information]"""
    
    # Create mailto link
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    
    # Open the default email client
    webbrowser.open(mailto_link)
    
    # Show success message
    st.success(f"App working report template opened! Please confirm and send to {YOUR_EMAIL}")

# Function to open email client for issues
def report_issue():
    subject = f"Issue Report - {WEBSITE_NAME} App"
    body = f"""Hi {YOUR_NAME},

⚠️ ISSUE DETECTED in your {WEBSITE_NAME} application. Here are the details:

**Type of Issue:**
[ ] Bug/Error
[ ] Feature Request
[ ] Performance Issue
[ ] UI/UX Problem
[ ] Other

**Issue Severity:**
[ ] Critical (App not working)
[ ] High (Major feature broken)
[ ] Medium (Minor issue)
[ ] Low (Cosmetic issue)

**Description:**
[Please describe the issue in detail]

**Steps to Reproduce:**
1. 
2. 
3. 

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Screenshots/Logs:**
[Attach if available]

**Environment Details:**
- Device: [e.g., Desktop/Mobile]
- Browser: [e.g., Chrome, Safari, Firefox]
- OS: [e.g., Windows 11, macOS, iOS]
- App Version: [If known]

**Additional Information:**
[Any other relevant details]

Thank you for your attention to this matter.

Best regards,
[Your Name]
[Your Contact Information]"""
    
    # Create mailto link
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    
    # Open the default email client
    webbrowser.open(mailto_link)
    
    # Show success message
    st.success(f"Issue report template opened! Please fill in the details and send to {YOUR_EMAIL}")

# Welcome Section
st.markdown('<h1 class="main-header">👋 Welcome to My Portfolio!</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; font-size: 1.5rem;">Hello! I\'m <span class="name-highlight">{YOUR_NAME}</span></p>', unsafe_allow_html=True)

# Divider
st.divider()

# Important Information Box
st.markdown("""
<div class="info-box">
<h3>📢 IMPORTANT INFORMATION</h3>
<p><strong>Note:</strong> Even if the app works correctly, please send an email to identify that it's working properly. This helps in tracking and verification.</p>
<p><strong>Email Purpose:</strong></p>
<ul>
<li>✅ Confirm the app is working (Send success report)</li>
<li>⚠️ Report any issues or bugs</li>
<li>💡 Provide feedback or suggestions</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Development Status Section
st.markdown('<h2 style="text-align: center;">🚀 Application Status</h2>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="development-box">', unsafe_allow_html=True)
    st.markdown('<div class="construction-icon">🚧</div>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: center; color: #ff9800;">{WEBSITE_NAME} - Under Development</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">This application is currently in active development phase.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.1rem; color: #666;">Your feedback is valuable for improving the app!</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Progress bar for development
st.write("**Development Progress:**")
progress_value = st.slider("Current progress", 0, 100, 65, disabled=True, label_visibility="collapsed")
progress = st.progress(progress_value)
st.caption(f"Development Status: {progress_value}% complete | Beta Testing Phase")

# Divider
st.divider()

# App Working Success Report Section
st.markdown('<h2 style="text-align: center;">✅ App Working Successfully?</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem;"><strong>Even if the app works perfectly, please send a confirmation email!</strong></p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown('<div class="success-icon">✅</div>', unsafe_allow_html=True)
    st.markdown('<h4 style="text-align: center; color: #2E7D32;">Report App Working Successfully</h4>', unsafe_allow_html=True)
    
    # Email button for success report
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Confirm App is Working", use_container_width=True, type="primary", key="success_report"):
            report_app_working()
    
    st.markdown('<p style="text-align: center; margin-top: 20px; color: #666;">Click to send confirmation that the app is working correctly.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Divider
st.divider()

# Report Issues Section
st.markdown('<h2 style="text-align: center;">⚠️ Found Issues?</h2>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="issue-box">', unsafe_allow_html=True)
    st.markdown('<div class="warning-icon">🚨</div>', unsafe_allow_html=True)
    
    # Email button for issues
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⚠️ Report Issues & Bugs", use_container_width=True, key="issue_report"):
            report_issue()
    
    st.markdown('<p style="text-align: center; margin-top: 20px; color: #666;">Click to report any problems, errors, or bugs encountered.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Email templates preview
st.markdown("---")
st.markdown("### 📋 Email Templates Preview")

tab1, tab2 = st.tabs(["✅ Success Report", "⚠️ Issue Report"])

with tab1:
    st.markdown("**When app works correctly:**")
    st.info("""
    Subject: App Working Successfully - Rag Chat
    
    Content:
    - Confirmation that app is working
    - Test environment details
    - Any positive feedback
    - Verification status
    """)
    
with tab2:
    st.markdown("**When issues are found:**")
    st.error("""
    Subject: Issue Report - Rag Chat App
    
    Content:
    - Issue type and severity
    - Detailed description
    - Steps to reproduce
    - Environment details
    - Expected vs actual behavior
    """)

# Divider
st.divider()

# Contact Information (Email only)
st.markdown('<h2 style="text-align: center;">📧 Contact Information</h2>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="contact-info">', unsafe_allow_html=True)
    
    # Display details
    st.markdown(f"""
    <div style="text-align: center;">
        <h3>👤 {YOUR_NAME}</h3>
        <p style="font-size: 1.3rem;">📧 {YOUR_EMAIL}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### **📬 Send Email For:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **✅ Success Reports:**
        - App working properly
        - All features functional
        - Performance good
        - No errors found
        """)
        
    with col2:
        st.markdown("""
        **⚠️ Issue Reports:**
        - Bugs or errors
        - Feature requests
        - Performance issues
        - UI/UX problems
        """)
    
    # Quick email button
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📨 Send General Email", use_container_width=True):
            webbrowser.open(f"mailto:{YOUR_EMAIL}?subject=General Inquiry - {WEBSITE_NAME}&body=Hi {YOUR_NAME},%0D%0A%0D%0A")
            st.success("Email client opened!")
    
    with col2:
        if st.button("📅 Request Update", use_container_width=True):
            webbrowser.open(f"mailto:{YOUR_EMAIL}?subject=Update Request - {WEBSITE_NAME}&body=Hi {YOUR_NAME},%0D%0A%0D%0ARequesting update on development progress.%0D%0A%0D%0A")
            st.success("Email client opened!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Testing checklist
st.markdown("---")
st.markdown("### 📝 Testing Checklist")
st.markdown("Before sending email, please check:")

test_items = {
    "Basic Functionality": ["App loads without errors", "Navigation works", "Buttons respond"],
    "Features": ["Core features work", "No broken links", "Forms submit correctly"],
    "Performance": ["Fast loading", "No crashes", "Smooth operation"],
    "UI/UX": ["Layout looks good", "Text readable", "Mobile responsive"]
}

for category, items in test_items.items():
    with st.expander(f"📋 {category}"):
        for item in items:
            st.checkbox(item)

# Footer
st.markdown("---")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>© {datetime.now().year} | Created by {YOUR_NAME}</p>
    <p style="font-size: 0.9rem;">Last updated: {current_time}</p>
    <p style="font-size: 0.8rem; color: #888;">Status: Under Development 🚧 | Version: Beta 1.0</p>
    <p style="font-size: 0.8rem; color: #FF9800;">⚠️ <strong>Important:</strong> Even if app works, please send email confirmation to {YOUR_EMAIL}</p>
</div>
""", unsafe_allow_html=True)

# Sidebar information
with st.sidebar:
    st.markdown("### ℹ️ Quick Info")
    st.markdown(f"**App:** {WEBSITE_NAME}")
    st.markdown(f"**Developer:** {YOUR_NAME}")
    st.markdown(f"**Email:** {YOUR_EMAIL}")
    st.markdown(f"**Status:** Beta Testing")
    
    st.markdown("---")
    st.markdown("### 📊 Testing Status")
    st.markdown("""
    - ✅ App Working: Send confirmation
    - ⚠️ Issues Found: Report immediately
    - 💡 Suggestions: Always welcome
    """)
    
    st.markdown("---")
    st.markdown("### 🔄 Quick Actions")
    if st.button("🔄 Refresh Page", use_container_width=True):
        st.rerun()
    
    st.markdown("""
    ---
    **Remember:** 
    Your emails help identify:
    1. If app works correctly
    2. What needs fixing
    3. User experience
    4. Development progress
    """)
