import streamlit as st
import pickle
import pandas as pd
import os
import altair as alt

# -------------------- PATH SETUP --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "model")

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="EcoTrack AI – Carbon Footprint Predictor",
    page_icon="🌱",
    layout="wide"
)

# -------------------- LOAD CSS --------------------
def load_css():
    css_path = os.path.join(BASE_DIR, "..", "static", "styles.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- LOAD MODEL --------------------
def load_model_and_scaler():
    with open(os.path.join(MODEL_DIR, "eco_model.pkl"), "rb") as f:
        model = pickle.load(f)
    with open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

# -------------------- LIFESTYLE STRESS INDEX --------------------
def calculate_lsi(pv, elec, plane, diet, water, waste):
    score = (
        (pv / 500) * 0.25 +
        (elec / 2000) * 0.25 +
        (plane / 50) * 0.20 +
        (diet / 3) * 0.15 +
        (water / 10000) * 0.10 +
        (waste / 20) * 0.05
    )
    return min(score, 1.0)

def sustainability_grade(lsi):
    if lsi < 0.15: return "A+ 🌟"
    if lsi < 0.30: return "A 🌱"
    if lsi < 0.45: return "B 👍"
    if lsi < 0.65: return "C ⚠️"
    return "D 🔴"

# -------------------- MAIN APP --------------------
def main():
    load_css()
    model, scaler = load_model_and_scaler()

    st.markdown("<h1 class='title'>🌱 EcoTrack AI – Carbon Footprint Predictor</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>AI-based carbon footprint prediction with lifestyle stress analysis and actionable sustainability planning.</p>",
        unsafe_allow_html=True
    )
    st.markdown("""
    <div class="hero-features">
        <div class="feature-card">
            <h4>🤖 AI Prediction</h4>
            <p>Machine-learning based carbon footprint estimation</p>
        </div>
        <div class="feature-card">
            <h4>📊 Lifestyle Stress Index</h4>
            <p>Quantifies how daily habits impact sustainability</p>
        </div>
        <div class="feature-card">
            <h4>🧠 Actionable Plans</h4>
            <p>Personalized 30-day carbon reduction strategy</p>
        </div>
    </div>

    <p class="cta-hint">⬅ Start by entering your lifestyle inputs</p>
    """, unsafe_allow_html=True)


    # -------------------- SIDEBAR --------------------
    st.sidebar.header("🌍 Lifestyle Inputs")

    with st.sidebar.expander("🚗 Transport", expanded=True):
        pv = st.slider("Personal Vehicle Km / week", 0, 500, 120)
        pub = st.slider("Public Vehicle Km / week", 0, 300, 80)
        plane = st.number_input("Plane Journeys / year", 0, 50, 3)
        train = st.number_input("Train Journeys / year", 0, 50, 4)

    with st.sidebar.expander("⚡ Utilities"):
        elec = st.slider("Electricity (kWh / month)", 50, 2000, 600)
        water = st.slider("Water Usage (liters / day)", 100, 10000, 4000)

    with st.sidebar.expander("♻️ Lifestyle"):
        waste = st.slider("Waste Generated (kg / week)", 0, 20, 6)
        nonveg = st.slider("Non-Veg Meals / week", 0, 21, 10)

    diet = 0 if nonveg == 0 else 1 if nonveg <= 7 else 2 if nonveg <= 14 else 3

    if st.sidebar.button("🔍 Predict Carbon Footprint"):
        input_df = pd.DataFrame({
            "Personal_Vehicle_Km": [pv],
            "Public_Vehicle_Km": [pub],
            "Plane_Journey_Count": [plane],
            "Train_Journey_Count": [train],
            "Electricity_Kwh": [elec],
            "Water_Usage_Liters": [water],
            "Diet_Type": [diet],
            "Waste_Kg": [waste]
        })

        prediction = model.predict(scaler.transform(input_df))[0]
        lsi = calculate_lsi(pv, elec, plane, diet, water, waste)
        grade = sustainability_grade(lsi)

        # -------------------- HERO SNAPSHOT --------------------
        st.markdown("<div class='card hero'>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)

        c1.markdown(f"<div class='hero-number'>{prediction:.2f}</div><div class='hero-label'>kg CO₂ / month</div>", unsafe_allow_html=True)
        c2.metric("🌱 Green Score", grade)
        c3.metric("📈 Lifestyle Stress", f"{int(lsi*100)} %")
        c4.metric("🏷 Monthly Budget", "50 kg CO₂")

        st.progress(1 - lsi)
        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------- TABS --------------------
        tab1, tab2, tab3 = st.tabs(["🧭 Journey", "📊 Breakdown", "🧠 Insights & Plan"])

        # ---------- JOURNEY ----------
        with tab1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### Sustainability Journey")
            st.markdown("Unsustainable → Improving → Balanced → Sustainable → Climate Positive")
            st.progress(1 - lsi)
            st.markdown(f"**Current Status:** {grade}")
            st.markdown("</div>", unsafe_allow_html=True)

        # ---------- BREAKDOWN ----------
        with tab2:
            impact_df = pd.DataFrame({
                "Factor": ["Transport", "Electricity", "Water", "Diet", "Waste", "Flights"],
                "Impact": [
                    pv/500 + pub/300,
                    elec/2000,
                    water/10000,
                    diet/3,
                    waste/20,
                    plane/50
                ]
            })

            chart = alt.Chart(impact_df).mark_bar().encode(
                x="Factor",
                y="Impact",
                color=alt.Color(
                    "Factor",
                    scale=alt.Scale(
                        domain=["Transport","Electricity","Water","Diet","Waste","Flights"],
                        range=["#ef4444","#f59e0b","#3b82f6","#22c55e","#8b5cf6","#ec4899"]
                    ),
                    legend=None
                )
            ).properties(height=260).configure_view(stroke=None)

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.altair_chart(chart, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # ---------- INSIGHTS & PLAN ----------
        with tab3:
    # Top 3 contributing factors
            top_factors = (
                impact_df
                .sort_values("Impact", ascending=False)
                .head(3)["Factor"]
                .tolist()
            )

            # User inputs (adjust variable names if needed)
            user_inputs = {
                "Diet": nonveg,
                "Transport": pv,
                "Electricity": elec,
                "Water": water,
                "Waste": waste,
                "Flights": plane
            }

            # Approx emission factors (kg CO2 per unit)
            emission_factors = {
                "Diet": 0.5,
                "Transport": 0.21,
                "Electricity": 0.82,
                "Water": 0.0003,
                "Waste": 0.45,
                "Flights": 90 / 12  # monthly average
            }

            # Reduction strategy (dynamic, not hardcoded advice)
            reduction_percent = {
                "Diet": 0.30,
                "Transport": 0.25,
                "Electricity": 0.15,
                "Water": 0.20,
                "Waste": 0.25,
                "Flights": 0.50
            }

            # Normalize all inputs to MONTHLY units (important!)
            normalized_inputs = {
                "Diet": nonveg * 4,          # meals per month
                "Transport": pv * 4,         # km per month
                "Electricity": elec,         # already monthly
                "Water": water * 30,         # liters per month
                "Waste": waste * 4,          # kg per month
                "Flights": plane / 12        # flights per month
            }
            
            # Display unit conversion (monthly → original input units)
            display_units = {
                "Diet": {"unit": "meals/week", "factor": 4},
                "Transport": {"unit": "km/week", "factor": 4},
                "Electricity": {"unit": "kWh/month", "factor": 1},
                "Water": {"unit": "liters/day", "factor": 30},
                "Waste": {"unit": "kg/week", "factor": 4},
                "Flights": {"unit": "flights/year", "factor": 1/12}
            }

            primary_factor = top_factors[0]

            st.markdown("<div class='card insight'>", unsafe_allow_html=True)

            # -------- KEY INSIGHT --------
            st.markdown("### 🧠 Key Insight")
            st.markdown(
                f"Your highest environmental impact comes from **{primary_factor}**. "
                f"Reducing this area will produce the fastest carbon reduction."
            )

            # -------- 30-DAY PLAN --------
            st.markdown("### 📅 30-Day Improvement Plan")

            for factor in top_factors:
                current_value = normalized_inputs.get(factor, 0)
                reduce_by = reduction_percent[factor]

                monthly_reduction = current_value * reduce_by

                # Convert back to user input unit
                unit_info = display_units[factor]
                display_reduction = monthly_reduction / unit_info["factor"]
                unit_label = unit_info["unit"]

                estimated_saving = monthly_reduction * emission_factors[factor]
                # Friendly action text
                # action_text = {
                #     "Diet": f"Replace ~{round(reduced_amount)} non-veg meals with plant-based options",
                #     "Transport": f"Reduce personal vehicle usage by ~{round(reduced_amount)} km/month",
                #     "Electricity": f"Cut electricity usage by ~{round(reduced_amount)} kWh/month",
                #     "Water": f"Reduce water usage by ~{round(reduced_amount)} liters/day",
                #     "Waste": f"Reduce waste generation by ~{round(reduced_amount,1)} kg/week",
                #     "Flights": f"Avoid ~{round(reduced_amount,1)} short-haul flights this year"
                # }

                st.markdown(f"**🔹 {factor}**")
                st.markdown(
                    f"- **Action:** Reduce {factor.lower()} by ~{int(display_reduction)} {unit_label}"
                )
                st.markdown(
                    f"- **Estimated Impact:** Save ~{estimated_saving:.2f} kg CO₂/month"
                )

            st.markdown(
                "<span class='badge'>AI-assisted, data-driven recommendation</span>",
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
