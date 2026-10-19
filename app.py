import streamlit as st

st.set_page_config(page_title="Neerathesh ARV | Portfolio", page_icon="🚀", layout="centered")

# ---------- Header ----------
st.title("Neerathesh ARV")
st.subheader("BTech CSE (AI & ML) Student | Hyderabad")
st.write(
    "Second-year engineering student passionate about Artificial Intelligence, "
    "machine learning and building practical, health-focused tech."
)
c1, c2 = st.columns(2)
c1.link_button("📧 Email", "mailto:neeratheshadduru@gmail.com")
c2.link_button("💼 LinkedIn", "https://www.linkedin.com/in/neerathesh-adduru")

st.divider()

# ---------- Education ----------
st.header("🎓 Education")
st.markdown(
    """
**B.Tech – CSE (AI & ML)**, Ellenki College of Engineering and Technology  
CGPA: **8.76** · Expected graduation: **2028**

**Intermediate (12th)**, Sri Chaitanya Jr Kalashala – **97.6%**

**10th**, Rao's High School – **9.8 CGPA**
"""
)

# ---------- Skills ----------
st.header("🛠️ Skills")
skills = {
    "Languages": ["Python", "SQL", "HTML", "CSS"],
    "AI / ML": ["Regression", "Classification"],
    "Tools": ["VS Code", "Tinkercad"],
    "Spoken": ["English", "Hindi", "Telugu"],
}
for category, items in skills.items():
    st.markdown(f"**{category}:** " + " · ".join(f"`{s}`" for s in items))

# ---------- Projects ----------
st.header("🚀 Projects")

with st.expander("HealthGuard – AI Health Companion (in progress)", expanded=True):
    st.write(
        "Android app that reads smartwatch health data, explains patterns in plain "
        "language using AI, warns when readings look unusual, and can notify "
        "emergency contacts. Includes biometric lock and a simple family status view."
    )

with st.expander("Sentiment Review Analysis"):
    st.write("Built for a hackathon: analyses reviews to classify sentiment.")

with st.expander("IoT Healthcare Monitoring System"):
    st.write("Real-time healthcare monitoring system simulated with Tinkercad and IoT.")

# ---------- Certifications ----------
st.header("📜 Certifications & Workshops")
st.markdown(
    """
- HackerRank – Python (Basic)
- HackerRank – SQL (Advanced)
- IoT Devices and Simulation workshop, Ellenki College (March 2025)
"""
)

st.divider()
st.caption("Built with Python & Streamlit")
