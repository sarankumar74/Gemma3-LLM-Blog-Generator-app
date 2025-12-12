import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama


def getGemmaresponse(system_prompt, input_text, no_word, blog_style):

    llm = Ollama(
        model="gemma3:1b",
        temperature=0.01
    )

    template = """
SYSTEM INSTRUCTION:
{system_prompt}

USER REQUEST:
Write a blog for a {style} audience on the topic "{text}".
Limit the blog to around {n_words} words.

Write the final blog below:
"""

    prompt = PromptTemplate(
        input_variables=["system_prompt", "style", "text", "n_words"],
        template=template,
    )

    final_prompt = prompt.format(
        system_prompt=system_prompt,
        style=blog_style,
        text=input_text,
        n_words=no_word,
    )

    response = llm.invoke(final_prompt)

    if isinstance(response, dict):
        if "text" in response:
            return response["text"]
        return str(response)

    return str(response)



# PAGE CONFIG

st.set_page_config(page_title="Blog Generator", page_icon="📝", layout="wide")

st.markdown(
    """
<style>

body {
    background-color: #f5f7fb;
    font-family: "Inter", sans-serif;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

/* Result Box */
.result-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    margin-top: 25px;
}

/* BOTTOM INPUT BAR */
.bottom-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 85%;
    max-width: 900px;
    background: #eef1f5;
    border: 1px solid #dcdfe5;
    border-radius: 35px;
    padding: 14px 22px;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 18px rgba(0,0,0,0.10);
    z-index: 1000;
}

.bottom-input {
    width: 100%;
    border: none;
    outline: none;
    background: transparent;
    font-size: 17px;
    color: #333;
}

.send-btn {
    font-size: 24px;
    cursor: pointer;
    margin-left: 10px;
    color: #7c7f83;
}

.send-btn:hover {
    color: black;
}

</style>
""",
    unsafe_allow_html=True,
)



# HEADER

st.markdown("<h1 class='main-title'>📝 Gemma Based Blog Generator</h1>", unsafe_allow_html=True)
st.write("Generate high-quality structured blogs using Gemma 3.")


# SIDEBAR SETTINGS

with st.sidebar:
    st.header("⚙️ Blog Settings")

    no_words = st.text_input("Number of Words", placeholder="Example: 150")

    blog_style = st.selectbox(
        "Audience Type",
        ["Researchers", "Students", "Common People", "Teachers", "Content Creators"],
    )

    st.write("---")
    st.header("🧠 System Prompt Mode")

    mode = st.selectbox(
        "AI Behavior",
        [
            "Default Assistant",
            "Expert Blog Writer",
            "SEO Writer",
            "Creative Writer",
            "Step-by-Step Reasoning",
            "Short Chain-of-Thought",
            "Ultra Concise Mode",
            "JSON Output Mode",
        ],
    )

    custom_prompt = st.text_area(
        "Custom System Instructions", placeholder="Add extra rules here...", height=130
    )


# SYSTEM PROMPT 


def build_system_prompt():
    base = {
        "Default Assistant": "You are a helpful AI assistant.",
        "Expert Blog Writer": "Write expert-level blogs with structure, clarity and depth.",
        "SEO Writer": "Write SEO-optimized blogs using smooth keyword placement.",
        "Creative Writer": "Write blogs with creativity, engaging tone and storytelling.",
        "Step-by-Step Reasoning": "Think step-by-step before answering.",
        "Short Chain-of-Thought": "Give only a short reasoning then final answer.",
        "Ultra Concise Mode": "Very short, direct answers only.",
        "JSON Output Mode": "Respond only in VALID JSON.",
    }.get(mode, "")

    if custom_prompt.strip():
        base += "\n\n" + custom_prompt.strip()

    return base



if "result" not in st.session_state:
    st.session_state.result = ""

if st.session_state.result:
    st.write("### 📄 Generated Blog")
    st.write(st.session_state.result)
    st.markdown("</div>", unsafe_allow_html=True)




col1, col2 = st.columns([12, 1])

with col1:
    user_topic = st.text_input(
        "",
        key="bottom_input",
        placeholder="Type your blog topic...",
        label_visibility="collapsed",
    )

with col2:
    send_bottom = st.button("➤", key="bottom_send")


if send_bottom and user_topic.strip():
    system_prompt = build_system_prompt()

    with st.spinner("Generating blog..."):
        result = getGemmaresponse(system_prompt, user_topic, no_words, blog_style)

    st.session_state.result = result
    st.rerun()
