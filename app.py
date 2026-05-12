import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Scholastic Hub - Academic Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== SESSION STATE ====================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ==================== CUSTOM CSS & STYLING ====================
st.markdown(
    """
    <style>
        /* ========== GLOBAL STYLES ========== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            color: #1a1a1a;
        }

        /* ========== HERO SECTION STYLES ========== */
        .hero-container {
            background: linear-gradient(135deg, #ffffff 0%, #f0f4f8 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
        }

        .hero-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            max-width: 1400px;
            width: 100%;
            align-items: center;
        }

        /* LEFT SIDE - Introduction */
        .intro-section {
            padding: 40px 30px;
        }

        .academic-badge {
            display: inline-block;
            background: linear-gradient(135deg, #0047AB 0%, #003580 100%);
            color: #F4B400;
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 30px;
            text-transform: uppercase;
            box-shadow: 0 4px 15px rgba(0, 71, 171, 0.2);
        }

        .main-headline {
            font-size: 48px;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 25px;
            color: #1a1a1a;
        }

        .highlight-blue {
            color: #0047AB;
            font-style: italic;
        }

        .intro-description {
            font-size: 16px;
            line-height: 1.7;
            color: #4a4a4a;
            margin-bottom: 40px;
            text-align: justify;
        }

        .cta-buttons {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #0047AB 0%, #003580 100%);
            color: white;
            padding: 14px 32px;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 71, 171, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 71, 171, 0.4);
        }

        .btn-secondary {
            background: white;
            color: #0047AB;
            padding: 14px 32px;
            border: 2px solid #0047AB;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-secondary:hover {
            background: #f0f7ff;
            transform: translateY(-2px);
        }

        /* RIGHT SIDE - Login Card */
        .login-card {
            background: white;
            border-radius: 16px;
            padding: 50px 40px;
            box-shadow: 0 20px 60px rgba(0, 71, 171, 0.12);
            border: 1px solid rgba(244, 180, 0, 0.1);
        }

        .login-logo {
            text-align: center;
            margin-bottom: 25px;
        }

        .login-logo-icon {
            font-size: 36px;
            margin-bottom: 10px;
        }

        .login-logo-text {
            font-size: 22px;
            font-weight: 700;
            color: #0047AB;
            letter-spacing: 0.5px;
        }

        .login-welcome {
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .form-input {
            width: 100%;
            padding: 12px 14px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            transition: all 0.3s ease;
            background: #f9f9f9;
        }

        .form-input:focus {
            outline: none;
            border-color: #0047AB;
            background: white;
            box-shadow: 0 0 0 3px rgba(0, 71, 171, 0.1);
        }

        .login-btn {
            width: 100%;
            background: linear-gradient(135deg, #0047AB 0%, #003580 100%);
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 71, 171, 0.3);
        }

        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 71, 171, 0.4);
        }

        .forgot-password {
            text-align: center;
            margin-top: 18px;
            font-size: 13px;
        }

        .forgot-password a {
            color: #0047AB;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .forgot-password a:hover {
            text-decoration: underline;
            color: #003580;
        }

        .signup-link {
            text-align: center;
            margin-top: 20px;
            font-size: 13px;
            color: #666;
        }

        .signup-link a {
            color: #0047AB;
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s ease;
        }

        .signup-link a:hover {
            color: #003580;
            text-decoration: underline;
        }

        /* ========== DASHBOARD SECTION STYLES ========== */
        .dashboard-container {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            padding: 50px 20px;
            min-height: 100vh;
        }

        .dashboard-title {
            text-align: center;
            font-size: 36px;
            font-weight: 800;
            color: #0047AB;
            margin-bottom: 15px;
        }

        .dashboard-subtitle {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-bottom: 50px;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: 250px 1fr 300px;
            gap: 25px;
            max-width: 1600px;
            margin: 0 auto;
        }

        /* Sidebar */
        .dashboard-sidebar {
            background: white;
            border-radius: 12px;
            padding: 25px 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            height: fit-content;
            position: sticky;
            top: 20px;
        }

        .sidebar-menu-item {
            padding: 14px 20px;
            color: #666;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            border-left: 3px solid transparent;
        }

        .sidebar-menu-item:hover {
            background: #f5f5f5;
            color: #0047AB;
            border-left-color: #F4B400;
        }

        .sidebar-menu-item.active {
            background: #f0f7ff;
            color: #0047AB;
            font-weight: 600;
            border-left-color: #0047AB;
        }

        /* Main Content */
        .dashboard-main {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .dashboard-card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            border-top: 4px solid #0047AB;
        }

        .card-title {
            font-size: 18px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .schedule-item {
            padding: 14px;
            background: #f8f9fa;
            border-left: 3px solid #0047AB;
            border-radius: 6px;
            margin-bottom: 12px;
            font-size: 13px;
        }

        .schedule-time {
            color: #0047AB;
            font-weight: 700;
        }

        .schedule-subject {
            color: #1a1a1a;
            margin-top: 4px;
            font-weight: 600;
        }

        .schedule-room {
            color: #999;
            font-size: 12px;
            margin-top: 3px;
        }

        /* Sidebar Right */
        .dashboard-right {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .notification-item {
            padding: 14px;
            background: #fffbf0;
            border-left: 3px solid #F4B400;
            border-radius: 6px;
            margin-bottom: 12px;
            font-size: 13px;
        }

        .notification-title {
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 4px;
        }

        .notification-time {
            color: #999;
            font-size: 12px;
        }

        .task-item {
            display: flex;
            gap: 10px;
            padding: 12px;
            background: #f8f9fa;
            border-radius: 6px;
            margin-bottom: 10px;
            font-size: 13px;
            align-items: flex-start;
        }

        .task-checkbox {
            width: 18px;
            height: 18px;
            margin-top: 2px;
            cursor: pointer;
            accent-color: #0047AB;
        }

        .task-text {
            color: #1a1a1a;
            flex: 1;
        }

        /* ========== FEATURES SECTION ========== */
        .features-section {
            background: white;
            padding: 80px 20px;
        }

        .features-title {
            text-align: center;
            font-size: 42px;
            font-weight: 800;
            color: #0047AB;
            margin-bottom: 20px;
        }

        .features-subtitle {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-bottom: 60px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .feature-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 71, 171, 0.1);
            text-align: center;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 71, 171, 0.15);
            border-color: #0047AB;
        }

        .feature-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .feature-title {
            font-size: 18px;
            font-weight: 700;
            color: #0047AB;
            margin-bottom: 12px;
        }

        .feature-description {
            font-size: 14px;
            color: #666;
            line-height: 1.6;
        }

        /* ========== RESPONSIVE DESIGN ========== */
        @media (max-width: 1200px) {
            .hero-content {
                grid-template-columns: 1fr;
                gap: 40px;
            }

            .dashboard-grid {
                grid-template-columns: 1fr;
            }

            .dashboard-sidebar {
                position: static;
            }

            .main-headline {
                font-size: 36px;
            }
        }

        @media (max-width: 768px) {
            .intro-section {
                padding: 20px;
            }

            .login-card {
                padding: 30px 20px;
            }

            .cta-buttons {
                flex-direction: column;
            }

            .main-headline {
                font-size: 28px;
            }

            .features-grid {
                grid-template-columns: 1fr;
            }

            .dashboard-right {
                flex-direction: row;
            }

            .features-title {
                font-size: 32px;
            }
        }

        /* ========== UTILITY CLASSES ========== */
        .text-center {
            text-align: center;
        }

        .mt-3 { margin-top: 30px; }
        .mt-5 { margin-top: 50px; }
        .mb-3 { margin-bottom: 30px; }
        .mb-5 { margin-bottom: 50px; }
        .p-3 { padding: 30px; }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==================== HELPER FUNCTIONS ====================

def render_hero_section():
    """Render the hero section with introduction and login"""
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-content">
                <!-- LEFT SIDE: Introduction -->
                <div class="intro-section">
                    <div class="academic-badge">🎓 ICS-401A • RTU PASIG</div>
                    
                    <h1 class="main-headline">
                        Everything Academic, In <span class="highlight-blue">One Place.</span>
                    </h1>
                    
                    <p class="intro-description">
                        Scholastic Hub is a centralized academic management and collaboration platform 
                        designed for ICS-401A students. It streamlines schedules, lecture files, announcements, 
                        assignments, notifications, and student collaboration into one organized system.
                    </p>
                    
                    <div class="cta-buttons">
                        <button class="btn-primary" onclick="document.querySelector('[data-testid=\\\"stForm\\\"]').scrollIntoView();">
                            Get Started
                        </button>
                        <button class="btn-secondary" onclick="alert('Learn more about Scholastic Hub!');">
                            Learn More
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_login_panel():
    """Render the login panel (overlaid on hero)"""
    st.markdown(
        """
        <div style="position: absolute; right: 40px; top: 50%; transform: translateY(-50%); width: 100%; max-width: 420px;">
            <div class="login-card">
                <div class="login-logo">
                    <div class="login-logo-icon">🎓</div>
                    <div class="login-logo-text">Scholastic Hub</div>
                </div>
                
                <div class="login-welcome">Welcome Back</div>
                
                <div class="form-group">
                    <label class="form-label">Institutional Email</label>
                    <input type="email" class="form-input" placeholder="your.email@rtu.edu.ph" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Password</label>
                    <input type="password" class="form-input" placeholder="Enter your password" required>
                </div>
                
                <button class="login-btn">Sign In</button>
                
                <div class="forgot-password">
                    <a href="#forgot">Forgot Password?</a>
                </div>
                
                <div class="signup-link">
                    Don't have an account? <a href="#signup">Create one now</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_dashboard():
    """Render the main dashboard after login"""
    st.markdown(
        """
        <div class="dashboard-container">
            <h1 class="dashboard-title">📊 Academic Dashboard</h1>
            <p class="dashboard-subtitle">Welcome to your personalized academic management system</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Dashboard Grid
    col_sidebar, col_main, col_right = st.columns([1, 2.5, 1.2], gap="large")

    # ===== SIDEBAR =====
    with col_sidebar:
        st.markdown(
            """
            <div class="dashboard-sidebar">
                <div class="sidebar-menu-item active">📊 Dashboard</div>
                <div class="sidebar-menu-item">📅 Schedule</div>
                <div class="sidebar-menu-item">📁 Lecture Files</div>
                <div class="sidebar-menu-item">✏️ Assignments</div>
                <div class="sidebar-menu-item">📢 Announcements</div>
                <div class="sidebar-menu-item">👥 Collaboration</div>
                <div class="sidebar-menu-item">⚙️ Settings</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ===== MAIN CONTENT =====
    with col_main:
        # Profile Card
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="card-title">👤 Student Profile</div>
                <table style="width:100%; font-size:14px;">
                    <tr>
                        <td style="padding:8px; font-weight:600; color:#666; width:40%;">Name:</td>
                        <td style="padding:8px; color:#1a1a1a;">John Doe</td>
                    </tr>
                    <tr style="background:#f9f9f9;">
                        <td style="padding:8px; font-weight:600; color:#666;">Student ID:</td>
                        <td style="padding:8px; color:#1a1a1a;">2220081</td>
                    </tr>
                    <tr>
                        <td style="padding:8px; font-weight:600; color:#666;">Block:</td>
                        <td style="padding:8px; color:#1a1a1a;">ICS-01-401A</td>
                    </tr>
                    <tr style="background:#f9f9f9;">
                        <td style="padding:8px; font-weight:600; color:#666;">Semester:</td>
                        <td style="padding:8px; color:#1a1a1a;">2nd Semester, SY 2024-2025</td>
                    </tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Today's Schedule
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="card-title">📅 Today's Schedule (Monday)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        schedule_items = [
            ("07:00 - 09:00", "ITP221 - Networking 1", "Room E501"),
            ("09:00 - 12:00", "ITP220 - Quantitative Methods", "Room E305"),
            ("13:00 - 16:00", "ITP221L - Networking 1 Laboratory", "Room E501"),
        ]

        for time, subject, room in schedule_items:
            st.markdown(
                f"""
                <div class="schedule-item">
                    <div class="schedule-time">{time}</div>
                    <div class="schedule-subject">{subject}</div>
                    <div class="schedule-room">{room}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Lecture Files
        st.markdown(
            """
            <div class="dashboard-card" style="margin-top: 25px;">
                <div class="card-title">📁 Recent Lecture Files</div>
                <table style="width:100%; font-size:14px;">
                    <tr style="border-bottom:1px solid #eee;">
                        <td style="padding:10px; font-weight:600; color:#0047AB;">ITP221_Networking_Basics.pdf</td>
                        <td style="text-align:right; padding:10px; color:#999; font-size:12px;">2 days ago</td>
                    </tr>
                    <tr style="border-bottom:1px solid #eee; background:#f9f9f9;">
                        <td style="padding:10px; font-weight:600; color:#0047AB;">ITP220_Statistical_Analysis.pptx</td>
                        <td style="text-align:right; padding:10px; color:#999; font-size:12px;">5 days ago</td>
                    </tr>
                    <tr style="background:#f9f9f9;">
                        <td style="padding:10px; font-weight:600; color:#0047AB;">ITP223_Graphics_Tutorial.zip</td>
                        <td style="text-align:right; padding:10px; color:#999; font-size:12px;">1 week ago</td>
                    </tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ===== RIGHT SIDEBAR =====
    with col_right:
        # Notifications
        st.markdown(
            """
            <div class="dashboard-card">
                <div class="card-title">🔔 Notifications</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        notifications = [
            ("New Assignment", "ITP221L Assignment Due"),
            ("Announcement", "Class Postponed Today"),
            ("Reminder", "Quiz Next Monday"),
        ]

        for title, message in notifications:
            st.markdown(
                f"""
                <div class="notification-item">
                    <div class="notification-title">{title}</div>
                    <div class="notification-time">{message}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # To-Do List
        st.markdown(
            """
            <div class="dashboard-card" style="margin-top: 25px;">
                <div class="card-title">✅ To-Do List</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        tasks = [
            "Complete ITP221 Lab",
            "Submit ITP220 Report",
            "Study for ITP223 Quiz",
            "Prepare Group Project",
        ]

        for task in tasks:
            st.markdown(
                f"""
                <div class="task-item">
                    <input type="checkbox" class="task-checkbox">
                    <div class="task-text">{task}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

def render_features_section():
    """Render the features section"""
    st.markdown(
        """
        <div class="features-section">
            <h1 class="features-title">🚀 Platform Features</h1>
            <p class="features-subtitle">
                Discover all the powerful tools designed to streamline your academic experience
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    features = [
        {
            "icon": "📊",
            "title": "Dashboard Management",
            "description": "Personalized dashboard with quick access to all your academic data and activities.",
        },
        {
            "icon": "📅",
            "title": "Schedule Viewer",
            "description": "Visual class schedule with real-time updates, room locations, and instructor information.",
        },
        {
            "icon": "📁",
            "title": "Lecture Repository",
            "description": "Centralized storage for all lecture materials, notes, and study resources.",
        },
        {
            "icon": "✏️",
            "title": "Task & Assignment Tracker",
            "description": "Track assignments with due dates, submission status, and grade tracking.",
        },
        {
            "icon": "🔔",
            "title": "Smart Notifications",
            "description": "Receive timely alerts about deadlines, announcements, and important updates.",
        },
        {
            "icon": "👥",
            "title": "Student Collaboration",
            "description": "Connect with classmates for group projects and academic discussions.",
        },
        {
            "icon": "📢",
            "title": "Announcements Hub",
            "description": "Stay informed with instructor announcements and class updates.",
        },
    ]

    cols = st.columns(3, gap="large")
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{feature['icon']}</div>
                    <div class="feature-title">{feature['title']}</div>
                    <div class="feature-description">{feature['description']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Add remaining feature if not divisible by 3
    if len(features) % 3 != 0:
        st.empty()

# ==================== MAIN APP LOGIC ====================

if not st.session_state.logged_in:
    # FRONT PAGE with Login
    
    # Create absolute positioning for login card using HTML/CSS overlay
    st.markdown(
        """
        <style>
            .hero-wrapper {
                position: relative;
            }
            
            .login-overlay {
                position: fixed;
                right: 60px;
                top: 50%;
                transform: translateY(-50%);
                width: 380px;
                z-index: 100;
            }
            
            @media (max-width: 1200px) {
                .login-overlay {
                    position: relative;
                    right: auto;
                    top: auto;
                    transform: none;
                    width: 100%;
                    margin-top: 40px;
                }
                
                .hero-content {
                    grid-template-columns: 1fr !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Hero Section
    col_left, col_right_space = st.columns([1.2, 1], gap="large")

    with col_left:
        st.markdown(
            """
            <div class="intro-section">
                <div class="academic-badge">🎓 ICS-401A • RTU PASIG</div>
                
                <h1 class="main-headline">
                    Everything Academic, In <span class="highlight-blue">One Place.</span>
                </h1>
                
                <p class="intro-description">
                    Scholastic Hub is a centralized academic management and collaboration platform 
                    designed for ICS-401A students. It streamlines schedules, lecture files, announcements, 
                    assignments, notifications, and student collaboration into one organized system.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_right_space:
        st.markdown(
            """
            <div class="login-card">
                <div class="login-logo">
                    <div class="login-logo-icon">🎓</div>
                    <div class="login-logo-text">Scholastic Hub</div>
                </div>
                
                <div class="login-welcome">Welcome Back</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Login Form
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=True):
        st.markdown(
            "<div class='login-card' style='padding: 25px 30px; margin-top: 20px;'>",
            unsafe_allow_html=True,
        )

        email = st.text_input(
            "Institutional Email",
            placeholder="your.email@rtu.edu.ph",
            label_visibility="collapsed",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            label_visibility="collapsed",
        )

        col1, col2 = st.columns([1, 1])
        with col1:
            submit = st.form_submit_button("Sign In", use_container_width=True)

        if submit:
            if email and password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Please enter both email and password")

        st.markdown("<div style='text-align: center; font-size: 13px; margin-top: 15px; color: #666;'>", unsafe_allow_html=True)
        st.markdown("[Forgot Password?](https://rtu.edu.ph) | [Create Account](https://rtu.edu.ph)")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # Features Section
    render_features_section()

else:
    # LOGGED IN - DASHBOARD PAGE
    # Add logout button in sidebar
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.user_email.split('@')[0]}! 👋")
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.rerun()

    render_dashboard()

