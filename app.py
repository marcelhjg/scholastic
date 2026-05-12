import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Scholastic Hub — Class Schedule",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --rtu-blue: #003C8F;
        --rtu-gold: #F4B400;
        --rtu-bg: #F5F7FB;
        --rtu-surface: #FFFFFF;
        --rtu-text: #111827;
        --rtu-muted: #475569;
        --rtu-border: #E2E8F0;
        --rtu-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
    }

    body {
        background: var(--rtu-bg);
        color: var(--rtu-text);
    }

    .content-wrapper {
        max-width: 1400px;
        margin: 0 auto;
        padding: 1.5rem 1.5rem 3rem;
    }

    .page-header-card {
        background: var(--rtu-surface);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: var(--rtu-shadow);
        margin-bottom: 1.75rem;
        border: 1px solid rgba(226, 232, 240, 0.8);
    }

    .header-grid {
        display: grid;
        grid-template-columns: 1fr auto;
        gap: 2rem;
        align-items: center;
    }

    .title-group {
        display: grid;
        gap: 0.65rem;
    }

    .eyebrow {
        color: var(--rtu-gold);
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        font-size: 0.82rem;
        margin: 0;
    }

    .page-header-card h1 {
        margin: 0;
        font-size: clamp(2rem, 2.5vw, 2.7rem);
        color: var(--rtu-text);
    }

    .page-header-card p {
        margin: 0;
        color: var(--rtu-muted);
        font-size: 1rem;
        line-height: 1.6;
    }

    .header-accent {
        width: 90px;
        height: 6px;
        border-radius: 999px;
        background: linear-gradient(90deg, var(--rtu-blue) 0%, var(--rtu-gold) 100%);
        margin-top: 0.85rem;
    }

    .student-info {
        background: #F8FAFF;
        border-radius: 18px;
        padding: 1.25rem;
        border: 1px solid rgba(226, 232, 240, 0.9);
        display: grid;
        gap: 0.85rem;
    }

    .student-info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        padding: 0.35rem 0;
    }

    .student-info-row .label {
        color: var(--rtu-muted);
        font-size: 0.88rem;
    }

    .student-info-row .value {
        color: var(--rtu-text);
        font-weight: 700;
        font-size: 0.95rem;
    }

    .header-note {
        color: var(--rtu-muted);
        margin-top: 1rem;
        font-size: 0.95rem;
    }

    .stats-card {
        background: var(--rtu-surface);
        border-radius: 20px;
        padding: 1.4rem 1.35rem;
        box-shadow: var(--rtu-shadow);
        border-top: 4px solid var(--rtu-blue);
        min-height: 150px;
    }

    .card-title {
        margin: 0;
        color: var(--rtu-muted);
        font-size: 0.95rem;
        font-weight: 700;
    }

    .card-value {
        margin: 0.85rem 0 0;
        font-size: 2rem;
        color: var(--rtu-text);
        font-weight: 700;
    }

    .schedule-section {
        background: var(--rtu-surface);
        border-radius: 24px;
        padding: 1.6rem;
        box-shadow: var(--rtu-shadow);
        border: 1px solid rgba(226, 232, 240, 0.9);
        margin-top: 2.5rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .schedule-grid {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 10px;
    }

    .schedule-grid th,
    .schedule-grid td {
        padding: 0.8rem 0.9rem;
        vertical-align: top;
    }

    .schedule-grid thead th {
        font-weight: 700;
        color: var(--rtu-text);
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-size: 0.9rem;
        border-bottom: 1px solid rgba(226, 232, 240, 0.9);
        padding-bottom: 1.15rem;
    }

    .schedule-grid tbody tr td:first-child {
        font-weight: 700;
        color: var(--rtu-muted);
        width: 130px;
        white-space: nowrap;
    }

    .day-cell {
        min-width: 160px;
        padding: 0;
    }

    .schedule-card {
        background: #F8FAFF;
        border-radius: 18px;
        border: 1px solid rgba(226, 232, 240, 0.9);
        padding: 1rem;
        box-shadow: 0 12px 24px rgba(15, 23, 42, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .schedule-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 30px rgba(15, 23, 42, 0.12);
    }

    .schedule-badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.9rem;
    }

    .schedule-card h4 {
        margin: 0 0 0.55rem;
        font-size: 1rem;
        line-height: 1.35;
        color: var(--rtu-text);
    }

    .schedule-card p {
        margin: 0.18rem 0;
        color: var(--rtu-muted);
        font-size: 0.92rem;
    }

    .subject-tag {
        display: inline-block;
        margin-top: 0.8rem;
        padding: 0.4rem 0.75rem;
        border-radius: 999px;
        background: white;
        color: var(--rtu-text);
        font-size: 0.82rem;
        font-weight: 700;
        border: 1px solid rgba(226, 232, 240, 0.95);
    }

    .day-card-empty {
        min-height: 138px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 18px;
        border: 1px dashed rgba(226, 232, 240, 0.9);
        background: #FBFCFE;
        color: var(--rtu-muted);
        font-size: 0.95rem;
    }

    @media (max-width: 1100px) {
        .header-grid,
        .student-info {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 760px) {
        .content-wrapper {
            padding: 1rem 0.75rem 2rem;
        }

        .schedule-grid thead {
            display: none;
        }

        .schedule-grid,
        .schedule-grid tbody,
        .schedule-grid tr,
        .schedule-grid td {
            display: block;
            width: 100%;
        }

        .schedule-grid tr {
            margin-bottom: 1rem;
        }

        .schedule-grid td {
            padding-left: 0;
        }

        .schedule-grid td:first-child {
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

schedule_header = {
    "title": "Class Schedule",
    "subtitle": "Second Semester AY 2025–2026",
    "student_info": [
        {"label": "Program", "value": "BSIT"},
        {"label": "Block Section", "value": "401A"},
        {"label": "Year Level", "value": "2th Year"},
        {"label": "Semester Status", "value": "Enrolled"},
    ],
}

summary_cards = [
    {"label": "Total Subjects", "value": "9"},
    {"label": "Total Units", "value": "23"},
    {"label": "Laboratory Classes", "value": "4"},
    {"label": "Class Days", "value": "3"},
]

schedule_data = {
    "Monday": [
        {
            "time": "7:00 AM – 9:00 AM",
            "subject": "ITP221 - Networking 1",
            "room": "E501",
            "code": "2220081",
            "color": "#003C8F",
        },
        {
            "time": "9:00 AM – 12:00 PM",
            "subject": "ITP220 - Quantitative Methods",
            "room": "E305",
            "code": "2220080",
            "color": "#1D4ED8",
        },
        {
            "time": "1:00 PM – 4:00 PM",
            "subject": "ITP221L - Networking 1 Laboratory",
            "room": "E501",
            "code": "2220082",
            "color": "#2563EB",
        },
    ],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [
        {
            "time": "7:00 AM – 10:00 AM",
            "subject": "ITP224L - Multimedia Production and Design Laboratory",
            "room": "E508",
            "code": "2220088",
            "color": "#003C8F",
        },
        {
            "time": "10:00 AM – 12:00 PM",
            "subject": "ITP224 - Multimedia Production and Design",
            "room": "E208",
            "code": "2220087",
            "color": "#1D4ED8",
        },
        {
            "time": "1:00 PM – 4:00 PM",
            "subject": "ITP223L - Computer Graphics Laboratory",
            "room": "E206",
            "code": "2220086",
            "color": "#0F766E",
        },
        {
            "time": "4:00 PM – 6:00 PM",
            "subject": "ITP223 - Computer Graphics",
            "room": "E501",
            "code": "2220085",
            "color": "#003C8F",
        },
    ],
    "Friday": [],
    "Saturday": [
        {
            "time": "7:00 AM – 9:00 AM",
            "subject": "ITP222 - Integrative Programming and Tech 1",
            "room": "E409",
            "code": "2220083",
            "color": "#003C8F",
        },
        {
            "time": "9:00 AM – 12:00 PM",
            "subject": "ITP222L - Integrative Programming and Tech 1 Lab",
            "room": "E206",
            "code": "2220084",
            "color": "#2563EB",
        },
        {
            "time": "1:00 PM – 3:00 PM",
            "subject": "PE04 - Physical Activities Towards Health and Fitness II",
            "room": "E501",
            "code": "2220089",
            "color": "#F4B400",
        },
    ],
}

schedule_slots = [
    "7:00 AM – 9:00 AM",
    "9:00 AM – 12:00 PM",
    "1:00 PM – 4:00 PM",
    "4:00 PM – 6:00 PM",
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

st.markdown("""
    <div class='content-wrapper'>
""", unsafe_allow_html=True)

student_info_html = ""
for item in schedule_header["student_info"]:
    student_info_html += (
        f"<div class='student-info-row'>"
        f"<span class='label'>{item['label']}</span>"
        f"<span class='value'>{item['value']}</span>"
        f"</div>"
    )

st.markdown(
    f"""
    <div class='page-header-card'>
        <div class='header-grid'>
            <div class='title-group'>
                <div class='eyebrow'>Rizal Technological University</div>
                <h1>{schedule_header['title']}</h1>
                <p>{schedule_header['subtitle']}</p>
                <div class='header-accent'></div>
            </div>
            <div class='student-info'>
                {student_info_html}
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

card_cols = st.columns(4, gap="large")
for index, card in enumerate(summary_cards):
    card_cols[index].markdown(
        f"""
        <div class='stats-card'>
            <p class='card-title'>{card['label']}</p>
            <p class='card-value'>{card['value']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class='schedule-section'>
        <div class='section-title'>Weekly Class Schedule</div>
    """,
    unsafe_allow_html=True,
)

schedule_html = """
    <table class='schedule-grid'>
        <thead>
            <tr>
                <th>Time</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
                <th>Saturday</th>
            </tr>
        </thead>
        <tbody>
"""

for slot in schedule_slots:
    schedule_html += f"<tr><td class='time-slot'>{slot}</td>"
    for day in days:
        day_entries = schedule_data.get(day, [])
        entry = next((item for item in day_entries if item["time"] == slot), None)
        if entry:
            schedule_html += (
                f"<td class='day-cell'><div class='schedule-card' style='border-left: 4px solid {entry['color']};'>"
                f"<div class='schedule-badge' style='background:{entry['color']};'>{entry['code']}</div>"
                f"<h4>{entry['subject']}</h4>"
                f"<p style='margin-top:0.85rem; font-weight:700; color: var(--rtu-text);'>{entry['room']}</p>"
                f"</div></td>"
            )
        else:
            schedule_html += (
                "<td class='day-cell'><div class='day-card-empty'>No scheduled class</div></td>"
            )
    schedule_html += "</tr>"

schedule_html += "</tbody></table>"

st.markdown(schedule_html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
