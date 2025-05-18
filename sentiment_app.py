import streamlit as st
from textblob import TextBlob

def main():
    st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

    st.title("🌸 Real-Time Sentiment Analyzer")
    st.write("Enter your text below to find out its sentiment:")

    user_input = st.text_area("Type something...", height=150)

    if st.button("Analyze"):
        if user_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            blob = TextBlob(user_input)
            polarity = blob.sentiment.polarity

            if polarity > 0:
                sentiment = "😊 Positive"
            elif polarity < 0:
                sentiment = "😠 Negative"
            else:
                sentiment = "😐 Neutral"

            st.success(f"Sentiment: {sentiment}")
            st.write(f"`Polarity Score: {polarity}`")

# Required to run on Streamlit Cloud
if __name__ == "__main__":
    main()
