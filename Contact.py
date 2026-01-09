import streamlit as st
import webbrowser
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Dhanavarathan P - Portfolio",
    page_icon="👋",
    layout="centered"
)

# Your information
YOUR_NAME = "Dhanavarathan P (Dhana)"
YOUR_EMAIL = "dhanavarathanperumal@gmail.com"
YOUR_PHONE = "9500343825"
WEBSITE_NAME = "Rag Chat"
WEBSITE_LINK = "https://offline1rag.streamlit.app"
INSTAGRAM_LINK = "https://www.instagram.com/call._.me._.dhana?igsh=MTFrdnQ1dDV1c3BtdA=="
GITHUB_LINK = "https://github.com/dhanavarathanperumal-art"
WHATSAPP_LINK = f"https://wa.me/{YOUR_PHONE}"

# Function to open links
def open_website():
    webbrowser.open(WEBSITE_LINK)
    st.success(f"Opening {WEBSITE_NAME}...")

def open_instagram():
    webbrowser.open(INSTAGRAM_LINK)
    st.success("Opening Instagram...")

def open_github():
    webbrowser.open(GITHUB_LINK)
    st.success("Opening GitHub...")

def open_whatsapp():
    webbrowser.open(WHATSAPP_LINK)
    st.success("Opening WhatsApp...")

def report_app_working():
    subject = f"App Working Successfully - {WEBSITE_NAME}"
    body = f"""Hi {YOUR_NAME},

✅ Your {WEBSITE_NAME} application is working perfectly!

Best regards,
[Your Name]"""
    
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    webbrowser.open(mailto_link)
    st.success(f"Email opened! Please send to {YOUR_EMAIL}")

def report_issue():
    subject = f"Issue Report - {WEBSITE_NAME} App"
    body = f"""Hi {YOUR_NAME},

⚠️ Issue detected in {WEBSITE_NAME}.

Please describe the issue:

Thank you.
[Your Name]"""
    
    mailto_link = f"mailto:{YOUR_EMAIL}?subject={subject}&body={body}"
    webbrowser.open(mailto_link)
    st.success(f"Email opened! Please send to {YOUR_EMAIL}")

# ==================== WELCOME SECTION ====================
st.title("👋 Welcome to My Portfolio!")
st.subheader(f"Hello! I'm {YOUR_NAME}")

st.markdown("---")

# ==================== IMPORTANT INFORMATION ====================
st.header("📢 IMPORTANT INFORMATION")

# Important note
st.warning("""
**⚠️ Note:** Even if the app works correctly, please send an email to identify that it's working properly. 
This helps in tracking and verification.
""")

# Email purpose cards
st.subheader("📧 Email Purpose:")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**✅ Confirm App Working**\n\nSend success report when app functions correctly")

with col2:
    st.error("**⚠️ Report Issues/Bugs**\n\nReport problems encountered while using the app")

with col3:
    st.success("**💡 Feedback/Suggestions**\n\nShare ideas for improvement or new features")

st.markdown("---")

# ==================== MY APPLICATION ====================
st.header("🌐 My Application")

# Website card
with st.container():
    st.markdown(f"""
    ### {WEBSITE_NAME}
    **URL:** {WEBSITE_LINK}
    """)
    
    if st.button("🚀 Visit My Application", type="primary", use_container_width=True):
        open_website()

st.markdown("---")

# ==================== APPLICATION STATUS ====================
st.header("🚀 Application Status")

# Development status
st.markdown(f"""
### {WEBSITE_NAME} - Active Development
This application is currently in active development phase.
Your feedback is valuable for improving the app!
""")

# Progress bar
st.write("**Development Progress:**")
progress = st.progress(75)
st.caption("Status: 75% complete | Active Development")

st.markdown("---")

# ==================== CONTACT INFORMATION ====================
st.header("📞 Contact Information")

# Personal details in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    **👤 Name:**  
    {YOUR_NAME}
    """)

with col2:
    st.markdown(f"""
    **📱 Phone/WhatsApp:**  
    {YOUR_PHONE}
    """)

# Contact details cards
st.subheader("📱 Contact Channels")

# Email
with st.expander("📧 Email", expanded=True):
    st.markdown(f"""
    **Email Address:**  
    `{YOUR_EMAIL}`
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send Email", key="email_btn", use_container_width=True):
            webbrowser.open(f"mailto:{YOUR_EMAIL}")
    with col2:
        if st.button("Copy Email", key="copy_email", use_container_width=True):
            st.code(YOUR_EMAIL)
            st.success("Copied!")

# WhatsApp
with st.expander("💬 WhatsApp", expanded=True):
    st.markdown(f"""
    **Phone Number:**  
    `{YOUR_PHONE}`
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open WhatsApp", key="whatsapp_btn", use_container_width=True):
            open_whatsapp()
    with col2:
        if st.button("Copy Phone", key="copy_phone", use_container_width=True):
            st.code(YOUR_PHONE)
            st.success("Copied!")

# Instagram
with st.expander("📸 Instagram", expanded=True):
    st.markdown(f"""
    **Instagram Handle:**  
    `@call._.me._.dhana`
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open Instagram", key="insta_btn", use_container_width=True):
            open_instagram()
    with col2:
        if st.button("Copy Instagram", key="copy_insta", use_container_width=True):
            st.code(INSTAGRAM_LINK)
            st.success("Copied!")

# GitHub
with st.expander("💻 GitHub", expanded=True):
    st.markdown(f"""
    **GitHub Profile:**  
    `dhanavarathanperumal-art`
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open GitHub", key="github_btn", use_container_width=True):
            open_github()
    with col2:
        if st.button("Copy GitHub", key="copy_github", use_container_width=True):
            st.code(GITHUB_LINK)
            st.success("Copied!")

st.markdown("---")

# ==================== QUICK CONTACT BUTTONS ====================
st.header("🚀 Quick Contact Actions")

# Button grid
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📧 Email", use_container_width=True):
        webbrowser.open(f"mailto:{YOUR_EMAIL}")

with col2:
    if st.button("💬 WhatsApp", use_container_width=True):
        open_whatsapp()

with col3:
    if st.button("📸 Instagram", use_container_width=True):
        open_instagram()

with col4:
    if st.button("💻 GitHub", use_container_width=True):
        open_github()

with col5:
    if st.button("🌐 Website", use_container_width=True):
        open_website()

st.markdown("---")

# ==================== EMAIL REPORTS ====================
st.header("📧 Send Email Reports")

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Confirm App is Working", type="primary", use_container_width=True):
        report_app_working()

with col2:
    if st.button("⚠️ Report Issues & Bugs", type="secondary", use_container_width=True):
        report_issue()

st.markdown("---")

# ==================== TESTING CHECKLIST ====================
st.header("📝 Quick Checklist")

with st.expander("Click to expand testing checklist", expanded=False):
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

st.markdown("---")

# ==================== QUICK LINKS ====================
st.header("🔗 Quick Access Links")

# Display links as clickable text
st.markdown(f"""
**Email:** [{YOUR_EMAIL}](mailto:{YOUR_EMAIL})  
**WhatsApp:** [{YOUR_PHONE}]({WHATSAPP_LINK})  
**Instagram:** [@call._.me._.dhana]({INSTAGRAM_LINK})  
**GitHub:** [dhanavarathanperumal-art]({GITHUB_LINK})  
**Website:** [{WEBSITE_NAME}]({WEBSITE_LINK})
""")

# Footer
st.markdown("---")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(f"""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>© {datetime.now().year} | Created by {YOUR_NAME}</p>
    <p style="font-size: 0.9rem;">Last updated: {current_time}</p>
    <p style="font-size: 0.8rem; color: #ff9800;">
        ⚠️ <strong>Important:</strong> Even if app works, please send email confirmation to {YOUR_EMAIL}
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("ℹ️ Quick Info")
    
    st.markdown(f"""
    **Name:** {YOUR_NAME}  
    **Email:** {YOUR_EMAIL}  
    **Phone:** {YOUR_PHONE}  
    **App:** {WEBSITE_NAME}  
    **Status:** Active Development
    """)
    
    st.markdown("---")
    
    st.header("📞 Quick Contact")
    
    if st.button("📧 Send Email", use_container_width=True):
        webbrowser.open(f"mailto:{YOUR_EMAIL}")
    
    if st.button("💬 WhatsApp", use_container_width=True):
        open_whatsapp()
    
    if st.button("📸 Instagram", use_container_width=True):
        open_instagram()
    
    if st.button("💻 GitHub", use_container_width=True):
        open_github()
    
    if st.button("🌐 Website", use_container_width=True):
        open_website()
    
    st.markdown("---")
    
    st.header("📧 Email Actions")
    
    if st.button("✅ Success Report", use_container_width=True):
        report_app_working()
    
    if st.button("⚠️ Issue Report", use_container_width=True):
        report_issue()
