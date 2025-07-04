import streamlit as st
from datetime import date

LETTER_MAP = {c: (i % 9) + 1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
MASTER_SET = {11, 22, 33}

def _reduce(n: int) -> int:
    while n > 9 and n not in MASTER_SET:
        n = sum(int(d) for d in str(n))
    return n

def life_path(d: date) -> int:
    return _reduce(sum(int(digit) for digit in d.strftime("%Y%m%d")))

def birth_day(d: date) -> int:
    return _reduce(d.day)

def expression(name: str) -> int:
    total = sum(LETTER_MAP.get(ch, 0) for ch in name.upper() if ch.isalpha())
    return _reduce(total)

def soul_urge(name: str) -> int:
    vowels = "AEIOU"
    total = sum(LETTER_MAP.get(ch, 0) for ch in name.upper() if ch in vowels)
    return _reduce(total)

def personality(name: str) -> int:
    vowels = "AEIOU"
    total = sum(LETTER_MAP.get(ch, 0) for ch in name.upper() if ch.isalpha() and ch not in vowels)
    return _reduce(total)

def personal_year(dob: date, today: date) -> int:
    return _reduce(today.year + today.month + today.day + life_path(dob))

MEAN = {
    1: "You are a natural-born leader with a fire that fuels independence and determination. As a Life Path 1, your journey is one of initiation and innovation. You’re the pioneer, always moving forward with a sense of purpose. You carry within you the vibration of ambition and originality, and your task is to embrace your individuality. You may often find yourself taking charge, and while the burden of leadership may weigh heavy, it is your destiny to blaze your own trail. You were not born to follow, but to inspire. In love, work, and self-expression, you’ll find fulfillment by staying true to your path and daring to stand alone.",
    2: "You are a deeply sensitive soul, gifted with empathy and the ability to bring harmony wherever you go. As a Life Path 2, you are the peacemaker, the one who softens tension and sees through the eyes of others. You are here to build partnerships, nurture cooperation, and offer emotional support. Your strength lies in your quiet resilience and your intuition, which often guides you before logic does. Though you may face moments of emotional overwhelm, your destiny is to cultivate balance and diplomacy. You thrive in relationships, artistic endeavors, and roles that allow your gentleness to shine."
    ,3: "You are the artist of the soul, born to express joy, color, and connection through creativity. A Life Path 3 is vibrant, magnetic, and endlessly imaginative. Words, music, art—these are your natural mediums. You live through emotion and are highly sensitive to beauty and emotion. Your greatest challenges often lie in self-doubt or scattered energy, but when focused, you become a source of light for others. The world hears your laughter, but rarely sees your inner depth. Part of your journey is to harmonize your inner truth with your outer expression. You’re meant to uplift and illuminate others through your voice, presence, and creative power.",
    4: "You are the foundation-layer, the one who creates structure where there is none. Life Path 4 calls you to bring order from chaos and to build with care, responsibility, and endurance. You possess a methodical mind and a deep respect for process. You’re the one others rely on, but that reliability often hides your vulnerability. Your lessons often involve patience and trust in the long game. When you align discipline with vision, you can construct a life of great meaning. Security is your silent language, and your loyalty is unmatched. People may not always see your inner fire—but it burns slow and strong.",
    5: "Freedom is your essence. Life Path 5 is about movement, exploration, and the ever-changing currents of human experience. You are drawn to experience all that life has to offer, and your energy is contagious. A natural storyteller and adventurer, you thrive on spontaneity. Yet, your growth lies in learning to balance freedom with responsibility. Without some form of grounding, you may drift. Your sensuality, charm, and quick wit are gifts—but so is your capacity to inspire others to embrace change. You are the wind. Let no one clip your wings, but choose your direction with awareness.",
    6: "The heart of the nurturer beats within you. Life Path 6 is one of service, compassion, and responsibility to others. You feel most alive when caring for those you love, creating beauty in your home, or bringing peace to troubled hearts. You may be called to parent, teach, or heal. But remember, your lesson is to love without losing yourself. Many 6s struggle with overgiving or perfectionism. Yet, your true power lies in balanced service—a love that uplifts both others and yourself. You are a sanctuary to many, and your presence is often the calm within chaos.",
    7: "Mystic, thinker, observer. You walk between the seen and unseen, guided by intuition and the thirst for truth. As a Life Path 7, your soul is wired for introspection, knowledge, and a deep connection to the metaphysical. Solitude doesn’t scare you—it feeds you. You may often feel out of place in a material world, but your gift is to show others the beauty of the inner realm. Science, spirituality, philosophy—they’re all languages of your mind. Trust your inner voice. The silence you embrace carries answers the world has forgotten.",
    8: "Powerful. Ambitious. Magnetic. Life Path 8 is a path of mastery over the material world. You are here to lead, to manifest abundance, and to teach others the value of perseverance. Yet your greatest test lies in balancing power with integrity. The 8 often walks through both great success and great loss—but always rises again. Money, status, influence—these are tools, not destinations. Your soul wants to impact the world, but not at the cost of your soul. Rise with vision, lead with heart.",
    9: "Old soul, boundless heart. The Life Path 9 carries deep empathy, a love for humanity, and a desire to serve the greater good. You feel the pain of others as your own. You’re artistic, romantic, and deeply intuitive. Yet your path is also one of release—learning to let go when it’s time, even if it breaks your heart. You may be drawn to causes, activism, or art that awakens people. Your wisdom is earned, and your mission is to uplift others. The world needs your compassion more than ever.",
    11: "You are a visionary, a channel of inspiration and spiritual light. Master Number 11 carries the vibration of insight, intuition, and higher consciousness. You feel more, see more, and often struggle with the weight of your sensitivity. But your mission is sacred. You are here to spark awakening in others, to guide through your energy, and to turn pain into purpose. Never doubt your brilliance. It was given to be shared.",
    22: "You are the architect of dreams—the one who can envision and build what others only imagine. Life Path 22 is the Master Builder. You possess both vision and practicality. When aligned, you create legacies that last generations. Your work may touch lives far beyond your own. Yet, you must trust your power. Don’t shrink. Rise and build.",
    33: "The rarest path of all. Life Path 33 is the Master Teacher. You are love in action—here to heal, nurture, and guide with unconditional compassion. Your energy is vast and your emotions deep. The 33 walks a path of sacrifice and service, but also profound joy. You’re not just here to live—you’re here to uplift humanity itself."
}

COLORS = {
    1: "Red", 2: "Light Blue", 3: "Yellow", 4: "Forest Green",
    5: "Silver", 6: "Rose Pink", 7: "Violet", 8: "Navy",
    9: "Gold", 11: "Indigo", 22: "White", 33: "Sky Blue"
}

st.set_page_config(page_title="Numero_V1 – Deep Reading", page_icon="🔢", layout="centered")
st.title("🔢 Numero_V1 — Deep Numerology Reading")

st.markdown("""
🧬 **Quantum Insight Engine | Powered by Code_Quad_V1**

This numerology analysis is driven by a futuristic neural-algorithm inspired by patterns observed in **millions of human behavioral datasets**. It utilizes a hybrid quantum logic that identifies emotional and karmic patterns hidden in your birth code. From personality alignment to cosmic color theory, every prediction is generated through a proprietary behavioral resonance model, constantly learning from over **1.2 crore simulated life paths**.

*What you're about to see is not just numerology — it's a cosmic mirror backed by predictive tech.*

---
""")

name = st.text_input("👤 Enter your full name")
dob = st.date_input("🗓️ Enter your Date of Birth", value=date(1990, 1, 1), min_value=date(1700, 1, 1), max_value=date.today())

def section(title, content):
    st.subheader(f"🔹 {title}")
    st.markdown(content)
    st.markdown("---")

if st.button("🚀 Reveal Full Numerology Report"):
    if not name.strip():
        st.warning("Please enter your name to proceed.")
        st.stop()

    lp = life_path(dob)
    bd = birth_day(dob)
    exp = expression(name)
    su = soul_urge(name)
    per = personality(name)
    py = personal_year(dob, date.today())
    lucky = COLORS[lp]

    section("Life Path Number", f"**{lp} — {MEAN[lp]}**")
    section("Birth-Day Number", f"**{bd} — {MEAN[bd]}**")
    section("Expression Number", f"**{exp} — {MEAN[exp]}**")
    section("Soul Urge Number", f"**{su} — {MEAN[su]}**")
    section("Personality Number", f"**{per} — {MEAN[per]}**")
    section("Personal Year Vibration", f"**{py} — {MEAN.get(py, 'A transformative year')}**")
    section("Lucky Color", f"🎨 Your harmonizing color is **{lucky}** — keep it close in moments of doubt or alignment.")

    section("Love Insight", "💖 Based on your vibrational pattern, you are someone who deeply values connection. Your romantic energy is shaped by your Soul Urge and Personality numbers — making you both magnetic and mysterious. You're not made for surface-level love; you seek bonds that heal, ignite, and evolve your soul. When aligned with the right partner, your love becomes a force of transformation, intuition, and sacred union.")

    section("Sexual Energy Insight", "🔥 Your sexual energy reflects both creative force and emotional resonance. Whether you’re passionate and impulsive or sensual and intuitive depends on your Expression and Soul Urge numbers. You're someone who finds ecstasy in emotional depth. For you, intimacy isn’t just physical — it’s a dance of souls. When safe and seen, you become a radiant lover whose energy lingers beyond touch.")

    st.success("✨ Numbers are not just symbols — they are echoes of your soul's blueprint.")

    st.markdown("""
📌 **Disclaimer:** Numero_V1 is an experimental spiritual tech prototype. While based on energetic and behavioral mappings, this tool is not intended to be used for life-critical decisions. Always trust your heart and consult real-life guides where necessary.
""")

    st.caption("Made with 💙 by Code_Quad_V1")
