import streamlit as st

st.title("📚 Lessons")

subject = st.selectbox(
    "Choose a subject",
    [
        "SQL",
        "Data Visualization",
        "Python",
        "Statistics",
        "Machine Learning"
    ]
)


if subject == "SQL":
    st.header("🗄️ SQL")

    lecture = st.selectbox(
        "Choose Lecture",
        [
            "Lecture 1",
            "Lecture 2",
            "Lecture 3"
        ]
    )

    st.subheader(lecture)
    st.write("Add lesson summary here...")


elif subject == "Data Visualization":
    st.header("📊 Data Visualization")

    lecture = st.selectbox(
        "Choose Lecture",
        [
            "Lecture 1",
            "Lecture 2",
            "Lecture 3"
        ]
    )

    st.subheader(lecture)
    st.write("Add lesson summary here...")


elif subject == "Python":
    st.header("🐍 Python")

    lecture = st.selectbox(
        "Choose Lecture",
        [
            "Lecture 1",
            "Lecture 2"
        ]
    )

    st.subheader(lecture)
    st.write("Add lesson summary here...")


elif subject == "Statistics":
    st.header("📈 Statistics")

    lecture = st.selectbox(
        "Choose Lecture",
        [
            "Lecture 1",
            "Lecture 2"
        ]
    )

    st.subheader(lecture)
    st.write("Add lesson summary here...")


elif subject == "Machine Learning":
    st.header("🤖 Machine Learning")

    lecture = st.selectbox(
        "Choose Lecture",
        [
            "Lecture 1",
            "Lecture 2"
        ]
    )

    st.subheader(lecture)
    st.write("Add lesson summary here...")
    