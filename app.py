import streamlit as st
from email_generator import generate_email
import streamlit.components.v1 as components

# Page configuration with custom theme
st.set_page_config(
    page_title="Cold Email Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
        /* Main background - BLACK */
        .main {
            padding: 2rem;
            background-color: #000000 !important;
        }
        
        [data-testid="stAppViewContainer"] {
            background-color: #000000 !important;
        }
        
        /* Header styling */
        h1 {
            color: white !important;
            text-align: center;
            font-size: 3rem !important;
            margin-bottom: 0.5rem !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        /* Subheader styling */
        h2 {
            color: #667eea !important;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        /* Input field styling */
        .stTextInput > div > div > input {
            border: 2px solid #667eea !important;
            border-radius: 10px !important;
            padding: 12px !important;
            font-size: 1rem !important;
            background-color: #1a1a1a !important;
            color: white !important;
        }
        
        .stTextArea > div > div > textarea {
            border: 2px solid #667eea !important;
            border-radius: 10px !important;
            padding: 12px !important;
            font-size: 1rem !important;
            background-color: #1a1a1a !important;
            color: white !important;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 12px 32px !important;
            font-size: 1.1rem !important;
            font-weight: bold !important;
            cursor: pointer !important;
            transition: transform 0.2s, box-shadow 0.2s !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
        }
        
        /* Container styling */
        .css-1d391kg {
            padding: 2rem;
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin: 1.5rem 0;
        }
        
        /* Label styling */
        label {
            font-weight: 600 !important;
            color: #fff !important;
        }
        
        /* Text styling for black background */
        p, h3, h2 {
            color: white !important;
        }
        
        /* Email container with copy button */
        .email-container {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            position: relative;
            margin: 1.5rem 0;
        }
        
        .email-content {
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
""", unsafe_allow_html=True)

# Title with description
st.markdown("<h1>📧 Cold Email Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 1.1rem; margin-bottom: 2rem;'>Craft professional cold emails powered by AI</p>", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📝 Email Details")
    company = st.text_input("🏢 Company Name", placeholder="e.g., Google, Microsoft")
    role = st.text_input("💼 Position/Role", placeholder="e.g., Senior Developer, Product Manager")

with col2:
    st.markdown("### 💡 Your Information")
    skills = st.text_area("🎯 Your Skills & Experience", placeholder="e.g., Python, JavaScript, Data Science, 5 years experience...", height=120)

# Generate button with centered layout
st.markdown("<div style='text-align: center; margin: 2rem 0;'>", unsafe_allow_html=True)
generate_button = st.button("✨ Generate Email", use_container_width=True, type="primary")
st.markdown("</div>", unsafe_allow_html=True)

# Response handling
if generate_button:
    if company and role and skills:
        with st.spinner("🤖 Crafting your perfect email..."):
            email = generate_email(company, role, skills)
        
        # Success message
        st.success("✅ Email generated successfully!")
        
        # Display generated email with copy button
        st.markdown("### 📬 Your Generated Email")
        
        # Store email in session state for copying
        st.session_state.current_email = email
        
        # Display the email in a nice box
        st.markdown(f"""
        <div class="email-container">
            <div class="email-content">{email}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Copy button using columns
        col1, col2, col3 = st.columns([1, 2, 2])
        
        with col1:
            if st.button("📋 Copy Email", use_container_width=True, key="copy_email_btn"):
                # Create a simple HTML/JS to copy to clipboard
                html_code = """
                <script>
                    var text = document.body.innerText;
                    navigator.clipboard.writeText(text);
                </script>
                """
                components.html(html_code, height=0)
                st.success("✅ Email copied to clipboard!")
    else:
        st.error("⚠️ Please fill in all fields to generate your email")