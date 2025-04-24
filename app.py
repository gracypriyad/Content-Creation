import customtkinter as ctk
from sentiment_model import predict_sentiment

# Initialize the UI theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Main Application Class
class SentimentApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.title("AI Sentiment Analyzer")
        self.geometry("600x500")  # Increased height for better UI
        self.configure(padx=20, pady=20)

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="AI Sentiment Analyzer", font=("Helvetica", 24, "bold"), text_color="#4A90E2")
        self.title_label.pack(pady=20)

        # Text Input Box (Replaced Entry with Textbox for dynamic resizing)
        self.input_textbox = ctk.CTkTextbox(self, width=500, height=80, font=("Arial", 14))
        self.input_textbox.insert("0.0", "")  # Placeholder text
        self.input_textbox.pack(pady=10, expand=True, fill="both")

        # Analyze Button
        self.analyze_button = ctk.CTkButton(self, text="Analyze Sentiment", command=self.analyze_sentiment, font=("Arial", 16, "bold"), fg_color="#4CAF50", hover_color="#45A049")
        self.analyze_button.pack(pady=15)

        # Output Label for Sentiment
        self.sentiment_label = ctk.CTkLabel(self, text="Sentiment: ", font=("Arial", 18, "bold"))
        self.sentiment_label.pack(pady=10)

        # Output Label for Response
        self.response_label = ctk.CTkLabel(self, text="Response: ", font=("Arial", 16), wraplength=500, justify="center")
        self.response_label.pack(pady=10)

    def analyze_sentiment(self):
        """Analyze the sentiment of user input and display the result."""
        user_input = self.input_textbox.get("1.0", "end").strip()  # Get full text from Textbox
        if user_input:
            sentiment, response = predict_sentiment(user_input)
            self.sentiment_label.configure(text=f"Sentiment: {sentiment}", text_color=self.get_color(sentiment))
            self.response_label.configure(text=f"Response: {response}")
        else:
            self.sentiment_label.configure(text="Sentiment: Please enter some text.", text_color="#E74C3C")
            self.response_label.configure(text="Response: Please type a review first.")

    def get_color(self, sentiment):
        """Return a color based on sentiment."""
        colors = {
            "Positive": "#2ECC71",  # Green
            "Neutral": "#F1C40F",   # Yellow
            "Negative": "#E74C3C"   # Red
        }
        return colors.get(sentiment, "#34495E")  # Default gray

# Run the application
if __name__ == "__main__":
    app = SentimentApp()
    app.mainloop()