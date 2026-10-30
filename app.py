import os
import html
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv

from services.ticket_router import route_ticket
from services.google_sheets import (
    save_ticket,
    get_tickets,
    update_ticket_status,
)

load_dotenv()

st.set_page_config(
    page_title="CloudContact Assist",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- DESIGN SYSTEM --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --text: #f4f7ff;
}
.stApp {
    background:
        radial-gradient(ellipse at 8% 4%, #163b77 0%, transparent 31%),
        radial-gradient(ellipse at 94% 12%, #51256c 0%, transparent 28%),
        radial-gradient(ellipse at 55% 100%, #102d48 0%, transparent 36%),
        linear-gradient(135deg, #070b18, #10162e 52%, #100b22);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}
.block-container { max-width: 1380px; padding-top: 1.6rem; padding-bottom: 3rem; }
h1,h2,h3,h4,p,label { color: var(--text); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background: #0b1227; }

.hero {
    padding: 30px 34px; border-radius: 26px; margin-bottom: 24px;
    border: 1px solid rgba(164,180,255,.38);
    background: linear-gradient(115deg, rgba(34,91,201,.96), rgba(103,60,204,.96) 57%, rgba(173,48,172,.96));
    box-shadow: 0 8px 0 #090e20, 0 22px 46px rgba(0,0,0,.35), inset 0 1px rgba(255,255,255,.2);
}
.hero h1 { font-size: clamp(2rem,4vw,3rem); font-weight: 900; letter-spacing: -1.4px; margin: 0; }
.hero p { color: #e7ebff !important; margin-bottom: 0; }
.eyebrow { color: #9bf6ff !important; font-size: .72rem; font-weight: 800; letter-spacing: 3px; margin-bottom: 8px; }

.panel {
    padding: 22px 24px; border-radius: 22px; margin-bottom: 18px;
    border: 1px solid rgba(143,164,240,.28);
    background: linear-gradient(145deg, rgba(30,44,83,.95), rgba(15,22,44,.98));
    box-shadow: 0 7px 0 #090e20, 0 16px 32px rgba(0,0,0,.24), inset 0 1px rgba(255,255,255,.06);
}
.metric-card {
    padding: 19px; min-height: 132px; border-radius: 19px;
    border: 1px solid var(--accent);
    background: linear-gradient(145deg, var(--tint), #131a32 80%);
    box-shadow: 0 6px 0 #080d1b, 0 14px 24px rgba(0,0,0,.24);
}
.metric-label { color: #c2d0f2; font-size: .82rem; font-weight: 600; }
.metric-value { color: white; font-size: 2rem; font-weight: 900; margin-top: 8px; letter-spacing: -.8px; }
.metric-note { color: #a9b9e4; font-size: .76rem; margin-top: 3px; }

.category-card {
    border-radius: 17px; padding: 17px 15px; min-height: 122px;
    border: 1px solid var(--accent);
    background: linear-gradient(145deg, var(--tint), #12192f 82%);
    box-shadow: 0 5px 0 #090e20, 0 12px 22px rgba(0,0,0,.2);
}
.category-icon { font-size: 24px; }
.category-name { color: #dce5ff; font-size: .8rem; margin-top: 9px; }
.category-count { color: #fff; font-size: 1.8rem; font-weight: 900; margin-top: 4px; }

.game-card {
    min-height: 225px; padding: 26px 22px; border-radius: 24px;
    border: 1px solid rgba(155,174,255,.38);
    background: linear-gradient(145deg, #202f60, #131a35 75%);
    box-shadow: 0 8px 0 #090e20, 0 18px 32px rgba(0,0,0,.3);
    text-align: center; margin-bottom: 18px;
}
.game-icon { font-size: 2.8rem; filter: drop-shadow(0 7px 12px rgba(99,120,255,.45)); }
.game-card h2 { font-size: 1.5rem; font-weight: 800; }
.game-card p { color: #c5d0f6 !important; line-height: 1.6; }

div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
    background: #f0f3ff !important; border: 2px solid #b5c4ff !important; border-radius: 12px !important;
}
div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea { color: #17203d !important; }

.stButton > button, .stFormSubmitButton > button {
    width: 100%; min-height: 46px; border-radius: 12px; color: white !important;
    font-weight: 800; border: 1px solid #8ca4ff;
    background: linear-gradient(100deg, #2875ff, #7046ed, #b43fd0);
    box-shadow: 0 5px 0 #29245f, 0 10px 20px rgba(75,90,255,.2); transition: .18s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    transform: translateY(-2px); border-color: #d3c5ff;
    box-shadow: 0 7px 0 #29245f, 0 14px 25px rgba(95,90,255,.3);
}
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #263b72, #171e3e);
    padding: 16px; border: 1px solid #495da4; border-radius: 17px;
    box-shadow: 0 5px 0 #0a1024;
}
div[data-testid="stMetricLabel"] { color: #d6dfff !important; }
div[data-testid="stMetricValue"] { color: white !important; }
div[data-testid="stDataFrame"] { border: 1px solid #44558f; border-radius: 14px; overflow: hidden; }
div[data-baseweb="tab-list"] { gap: 8px; }
.stAlert { border-radius: 12px; }
.footer { text-align: center; color: #91a3d2; font-size: 12px; padding-top: 28px; }

@media(max-width: 760px) {
    .block-container { padding: 1rem; }
    .hero { padding: 23px 18px; }
    .panel { padding: 17px; }
    .metric-value { font-size: 1.55rem; }
}
</style>
""", unsafe_allow_html=True)


# -------------------- SESSION STATE --------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


def go_to(page):
    st.session_state.page = page
    st.rerun()


def show_header():
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">✦ SMART SUPPORT OPERATIONS ✦</div>
      <h1>🎮 CloudContact Assist</h1>
      <p>Every customer query. The right team. One intelligent workspace.</p>
    </div>
    """, unsafe_allow_html=True)


def show_footer():
    st.markdown(
        '<div class="footer">CLOUDCONTACT ASSIST &nbsp; • &nbsp; SMART TICKET ROUTING</div>',
        unsafe_allow_html=True,
    )


def show_navigation():
    left, right = st.columns([4, 1])
    with left:
        st.caption("CLOUDCONTACT ASSIST / WORKSPACE")
    with right:
        if st.button("⌂ Home", key="nav_home"):
            go_to("home")


def render_metric(label, value, note, color, icon):
    tint = color + "38"
    st.markdown(f"""
    <div class="metric-card" style="--accent:{color};--tint:{tint}">
      <div class="metric-label">{icon} &nbsp; {html.escape(label)}</div>
      <div class="metric-value">{html.escape(str(value))}</div>
      <div class="metric-note">{html.escape(note)}</div>
    </div>
    """, unsafe_allow_html=True)


def render_category_card(category, count, icon, color):
    st.markdown(f"""
    <div class="category-card" style="--accent:{color};--tint:{color}38">
      <div class="category-icon">{icon}</div>
      <div class="category-name">{html.escape(category)}</div>
      <div class="category-count">{count}</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- HEADER --------------------

show_header()


# -------------------- HOME --------------------

if st.session_state.page == "home":
    st.markdown(
        "<h2 style='text-align:center'>Choose your destination</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center;color:#bdc9f2'>Select how you want to access CloudContact Assist.</p>",
        unsafe_allow_html=True,
    )

    customer_col, admin_col = st.columns(2, gap="large")

    with customer_col:
        st.markdown("""
        <div class="game-card">
          <div class="game-icon">🎧</div>
          <h2>Customer Support</h2>
          <p>Submit a query and let the routing system assign it to the right team.</p>
          <p>✦ Quick submission &nbsp; ✦ Automatic routing</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Open Support Portal", key="customer_open"):
            go_to("customer")

    with admin_col:
        st.markdown("""
        <div class="game-card">
          <div class="game-icon">🛡️</div>
          <h2>Admin Control Center</h2>
          <p>Track tickets, review team assignments, monitor priorities and update status.</p>
          <p>✦ Ticket tracking &nbsp; ✦ Status management</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔐 Admin Login", key="admin_open"):
            go_to("admin_login")

    show_footer()


# -------------------- CUSTOMER FORM --------------------

elif st.session_state.page == "customer":
    show_navigation()

    st.markdown("""
    <div class="panel">
      <h2>🎧 Customer Support Portal</h2>
      <p>Describe your issue. Our routing rules will direct it to the appropriate team.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("customer_form", clear_on_submit=True):
        email = st.text_input("Customer email", placeholder="you@example.com")
        subject = st.text_input("Issue subject", placeholder="e.g. Payment failed")
        message = st.text_area(
            "Describe your issue",
            placeholder="Tell us what happened...",
            height=150,
        )
        submitted = st.form_submit_button(
            "🚀 Submit Support Ticket",
            use_container_width=True,
        )

    if submitted:
        if not email.strip() or not subject.strip() or not message.strip():
            st.error("Please complete all fields.")
        elif "@" not in email or "." not in email.split("@")[-1]:
            st.error("Please enter a valid email address.")
        else:
            try:
                routing = route_ticket(subject, message)
                ticket_id = save_ticket(
                    email.strip(),
                    subject.strip(),
                    message.strip(),
                    routing,
                )

                st.success("Your support ticket has been created.")
                st.markdown(f"""
                <div class="panel">
                  <h3>✨ Ticket details</h3>
                  <p><b>Ticket ID:</b> {html.escape(str(ticket_id))}</p>
                  <p><b>Category:</b> {html.escape(str(routing["Category"]))}</p>
                  <p><b>Assigned team:</b> {html.escape(str(routing["Assigned_Team"]))}</p>
                  <p><b>Priority:</b> {html.escape(str(routing["Priority"]))}</p>
                  <p><b>Status:</b> {html.escape(str(routing["Status"]))}</p>
                </div>
                """, unsafe_allow_html=True)

            except Exception as error:
                st.error(f"Could not save your ticket: {error}")

    show_footer()


# -------------------- ADMIN LOGIN --------------------

elif st.session_state.page == "admin_login":
    show_navigation()
    _, center, _ = st.columns([1, 1.5, 1])

    with center:
        st.markdown("""
        <div class="panel">
          <h2 style="text-align:center">🔐 Admin Login</h2>
          <p style="text-align:center">Authorized administrators only.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("admin_login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_clicked = st.form_submit_button(
                "🔓 Sign In to Dashboard",
                use_container_width=True,
            )

        if login_clicked:
            correct_username = os.getenv("ADMIN_USERNAME")
            correct_password = os.getenv("ADMIN_PASSWORD")

            if (
                correct_username
                and correct_password
                and username == correct_username
                and password == correct_password
            ):
                st.session_state.admin_logged_in = True
                go_to("dashboard")
            else:
                st.error("Invalid login or missing admin credentials in .env.")

    show_footer()


# -------------------- ADVANCED ADMIN DASHBOARD --------------------

elif st.session_state.page == "dashboard":
    if not st.session_state.admin_logged_in:
        st.session_state.page = "admin_login"
        st.rerun()

    show_navigation()

    st.markdown("""
    <div class="panel">
      <div class="eyebrow">ADMINISTRATION / ANALYTICS</div>
      <h2>🛡️ Support Operations Center</h2>
      <p>Monitor ticket volume, categories, priorities and workflow status.</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([4, 1])

    with left:
        st.caption("DATA SOURCE: GOOGLE SHEETS")

    with right:
        if st.button("🚪 Logout", key="admin_logout"):
            st.session_state.admin_logged_in = False
            go_to("home")

    try:
        tickets = get_tickets()

        if not tickets:
            st.info("No tickets yet. Submit a customer query to populate the dashboard.")
            show_footer()

        else:
            df = pd.DataFrame(tickets)

            # Add missing columns to support older spreadsheet rows.
            required_columns = [
                "Category", "Assigned_Team", "Priority", "Status",
                "Received_Date", "Ticket_ID", "Customer_Email",
                "Subject", "Message",
            ]

            for column in required_columns:
                if column not in df.columns:
                    df[column] = ""

            for column in ["Category", "Assigned_Team", "Priority", "Status"]:
                df[column] = df[column].fillna("").astype(str)

            total = len(df)
            open_count = int(df["Status"].str.lower().eq("open").sum())
            progress_count = int(df["Status"].str.lower().eq("in progress").sum())
            high_count = int(df["Priority"].str.lower().eq("high").sum())

            st.markdown("### ✨ Performance Overview")
            m1, m2, m3, m4 = st.columns(4, gap="medium")

            with m1:
                render_metric(
                    "Total Tickets", total, "All recorded requests",
                    "#4385ff", "🎫",
                )

            with m2:
                render_metric(
                    "Open Tickets", open_count, "Awaiting action",
                    "#e8a34c", "📂",
                )

            with m3:
                render_metric(
                    "In Progress", progress_count, "Currently being handled",
                    "#9565ff", "⚙️",
                )

            with m4:
                render_metric(
                    "High Priority", high_count, "Needs close attention",
                    "#ed5c8b", "🔥",
                )

            # -------------------- CATEGORY CARDS --------------------

            st.markdown("### 🎯 Ticket Categories")

            known_categories = [
                "Billing", "Technical Support",
                "Order Support", "General Support",
            ]

            actual_categories = sorted({
                value.strip()
                for value in df["Category"].tolist()
                if value.strip()
            })

            categories = list(dict.fromkeys(known_categories + actual_categories))

            category_styles = {
                "Billing": ("💳", "#4385ff"),
                "Technical Support": ("🛠️", "#9565ff"),
                "Order Support": ("📦", "#20cdb5"),
                "General Support": ("🎧", "#e15cce"),
            }

            for start in range(0, len(categories), 4):
                cols = st.columns(4, gap="medium")

                for col, category in zip(cols, categories[start:start + 4]):
                    icon, color = category_styles.get(
                        category, ("🎫", "#6080df")
                    )
                    count = int(
                        df["Category"].str.strip().eq(category).sum()
                    )

                    with col:
                        render_category_card(category, count, icon, color)

            # -------------------- CHART DATA --------------------

            st.markdown("### 📊 Analytics Studio")

            chart1, chart2 = st.columns(2, gap="large")

            category_counts = (
                df["Category"].replace("", "Uncategorized")
                .value_counts()
                .rename_axis("Category")
                .reset_index(name="Tickets")
            )

            priority_counts = (
                df["Priority"].replace("", "Unspecified")
                .value_counts()
                .rename_axis("Priority")
                .reset_index(name="Tickets")
            )

            status_counts = (
                df["Status"].replace("", "Unspecified")
                .value_counts()
                .rename_axis("Status")
                .reset_index(name="Tickets")
            )

            # Category donut chart
            with chart1:
                st.markdown(
                    '<div class="panel"><h3>🧩 Tickets by Category</h3></div>',
                    unsafe_allow_html=True,
                )

                fig_category = px.pie(
                    category_counts,
                    names="Category",
                    values="Tickets",
                    hole=0.62,
                    color_discrete_sequence=[
                        "#4385ff", "#9565ff", "#20cdb5",
                        "#e15cce", "#e8a34c",
                    ],
                )

                fig_category.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#edf2ff",
                    legend_title_text="",
                    margin=dict(l=10, r=10, t=15, b=10),
                    height=330,
                )

                fig_category.update_traces(
                    textposition="inside",
                    textinfo="percent",
                    marker=dict(line=dict(color="#11182f", width=2)),
                )

                st.plotly_chart(
                    fig_category,
                    use_container_width=True,
                )

            # Priority bar chart
            with chart2:
                st.markdown(
                    '<div class="panel"><h3>🔥 Tickets by Priority</h3></div>',
                    unsafe_allow_html=True,
                )

                fig_priority = px.bar(
                    priority_counts,
                    x="Priority",
                    y="Tickets",
                    color="Priority",
                    color_discrete_map={
                        "High": "#ed5c8b",
                        "Medium": "#e8a34c",
                        "Low": "#20cdb5",
                        "Unspecified": "#7c8fb8",
                    },
                )

                fig_priority.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#edf2ff",
                    showlegend=False,
                    margin=dict(l=10, r=10, t=15, b=10),
                    height=330,
                    xaxis_title="Priority",
                    yaxis_title="Number of tickets",
                )

                fig_priority.update_xaxes(
                    gridcolor="rgba(160,180,230,.12)"
                )
                fig_priority.update_yaxes(
                    gridcolor="rgba(160,180,230,.12)",
                    rangemode="tozero",
                )

                st.plotly_chart(
                    fig_priority,
                    use_container_width=True,
                )

            # Status and team charts
            chart3, chart4 = st.columns(2, gap="large")

            with chart3:
                st.markdown(
                    '<div class="panel"><h3>📌 Workflow Status</h3></div>',
                    unsafe_allow_html=True,
                )

                fig_status = px.bar(
                    status_counts,
                    x="Status",
                    y="Tickets",
                    color="Status",
                    color_discrete_map={
                        "Open": "#e8a34c",
                        "In Progress": "#9565ff",
                        "Resolved": "#20cdb5",
                        "Unspecified": "#7c8fb8",
                    },
                )

                fig_status.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#edf2ff",
                    showlegend=False,
                    margin=dict(l=10, r=10, t=15, b=10),
                    height=310,
                    xaxis_title="Status",
                    yaxis_title="Number of tickets",
                )

                fig_status.update_xaxes(
                    gridcolor="rgba(160,180,230,.12)"
                )
                fig_status.update_yaxes(
                    gridcolor="rgba(160,180,230,.12)",
                    rangemode="tozero",
                )

                st.plotly_chart(
                    fig_status,
                    use_container_width=True,
                )

            with chart4:
                st.markdown(
                    '<div class="panel"><h3>👥 Tickets by Assigned Team</h3></div>',
                    unsafe_allow_html=True,
                )

                team_counts = (
                    df["Assigned_Team"].replace("", "Unassigned")
                    .value_counts()
                    .rename_axis("Team")
                    .reset_index(name="Tickets")
                )

                fig_team = px.bar(
                    team_counts,
                    x="Tickets",
                    y="Team",
                    orientation="h",
                    color="Team",
                    color_discrete_sequence=[
                        "#4385ff", "#9565ff", "#20cdb5",
                        "#e15cce", "#e8a34c",
                    ],
                )

                fig_team.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#edf2ff",
                    showlegend=False,
                    margin=dict(l=10, r=10, t=15, b=10),
                    height=310,
                    xaxis_title="Number of tickets",
                    yaxis_title="",
                )

                fig_team.update_xaxes(
                    gridcolor="rgba(160,180,230,.12)",
                    rangemode="tozero",
                )

                st.plotly_chart(
                    fig_team,
                    use_container_width=True,
                )

            # -------------------- TICKET EXPLORER --------------------

            st.markdown("### 🔎 Ticket Explorer")

            filter1, filter2, filter3 = st.columns(3)

            team_options = ["All Teams"] + sorted(
                value for value in df["Assigned_Team"].unique() if value
            )
            status_options = ["All Statuses"] + sorted(
                value for value in df["Status"].unique() if value
            )
            priority_options = ["All Priorities"] + sorted(
                value for value in df["Priority"].unique() if value
            )

            with filter1:
                selected_team = st.selectbox(
                    "Assigned team", team_options
                )

            with filter2:
                selected_status = st.selectbox(
                    "Status", status_options
                )

            with filter3:
                selected_priority = st.selectbox(
                    "Priority", priority_options
                )

            filtered = df.copy()

            if selected_team != "All Teams":
                filtered = filtered[
                    filtered["Assigned_Team"] == selected_team
                ]

            if selected_status != "All Statuses":
                filtered = filtered[
                    filtered["Status"] == selected_status
                ]

            if selected_priority != "All Priorities":
                filtered = filtered[
                    filtered["Priority"] == selected_priority
                ]

            st.caption(f"Showing {len(filtered)} of {total} tickets")

            visible_columns = [
                column for column in [
                    "Ticket_ID", "Received_Date", "Customer_Email",
                    "Subject", "Category", "Assigned_Team",
                    "Priority", "Status",
                ]
                if column in filtered.columns
            ]

            st.dataframe(
                filtered[visible_columns],
                use_container_width=True,
                hide_index=True,
            )

            # -------------------- UPDATE TICKET STATUS --------------------

            st.markdown("### 🛠️ Manage Ticket Status")

            ticket_ids = filtered["Ticket_ID"].astype(str).tolist()
            ticket_ids = [
                ticket_id for ticket_id in ticket_ids
                if ticket_id and ticket_id.lower() != "nan"
            ]

            if ticket_ids:
                with st.form("update_ticket_form"):
                    selected_id = st.selectbox(
                        "Select ticket ID", ticket_ids
                    )

                    new_status = st.selectbox(
                        "New status",
                        ["Open", "In Progress", "Resolved"],
                    )

                    update_clicked = st.form_submit_button(
                        "💾 Save Status",
                        use_container_width=True,
                    )

                if update_clicked:
                    try:
                        update_ticket_status(selected_id, new_status)
                        st.success(
                            f"{selected_id} updated to {new_status}."
                        )
                        st.rerun()

                    except Exception as error:
                        st.error(f"Could not update ticket: {error}")

            else:
                st.info("No tickets match the current filters.")

            # CSV export
            st.download_button(
                "⬇️ Download filtered tickets as CSV",
                data=filtered.to_csv(index=False).encode("utf-8"),
                file_name="cloudcontact_tickets.csv",
                mime="text/csv",
            )

            show_footer()

    except Exception as error:
        st.error(f"Could not load dashboard data: {error}")
        st.caption("Check your Google Sheets connection and column headers.")