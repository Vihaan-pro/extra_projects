import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {
        "question": "1. What do you do when things go wrong?",
        "options": [
            ("Look on the bright side ☀️", "optimist"),
            ("Expect more problems 😔", "pessimist"),
            ("Accept it and move on 🤷", "realist"),
            ("Hope for a miracle 🌠", "idealist")
        ]
    },
    {
        "question": "2. How do you feel about the future?",
        "options": [
            ("It's full of opportunities 🌈", "optimist"),
            ("It’s uncertain and scary 😨", "pessimist"),
            ("It depends on what we do now 🧠", "realist"),
            ("It will be amazing, somehow ✨", "idealist")
        ]
    },
    {
        "question": "3. What do you do in a tough situation?",
        "options": [
            ("Believe everything will be okay 👍", "optimist"),
            ("Think the worst is coming 😩", "pessimist"),
            ("Analyze and act logically 📊", "realist"),
            ("Wish things were different 💭", "idealist")
        ]
    },
    {
        "question": "4. How do you describe the world?",
        "options": [
            ("Beautiful and full of wonder 🌍", "optimist"),
            ("Unfair and dangerous ⚠️", "pessimist"),
            ("Complicated but manageable 🧩", "realist"),
            ("It should be perfect 🌟", "idealist")
        ]
    },
    {
        "question": "5. When plans change suddenly, you...",
        "options": [
            ("Look for new chances 🔄", "optimist"),
            ("Get upset and assume the worst 😠", "pessimist"),
            ("Adapt and go with the flow 🌊", "realist"),
            ("Imagine how it could have gone better 💫", "idealist")
        ]
    },
    {
        "question": "6. What kind of movies do you like most?",
        "options": [
            ("Feel-good and happy endings 🎬😊", "optimist"),
            ("Dark dramas or thrillers 😱", "pessimist"),
            ("True stories and documentaries 🎥", "realist"),
            ("Fantasy or dreams coming true 🧚", "idealist")
        ]
    },
    {
        "question": "7. What do you tell a sad friend?",
        "options": [
            ("Things will get better! 💖", "optimist"),
            ("Life is hard sometimes 😞", "pessimist"),
            ("Here's what you can do next 📋", "realist"),
            ("Never stop dreaming 🌠", "idealist")
        ]
    },
    {
        "question": "8. How do you handle failure?",
        "options": [
            ("It's a lesson to grow 📈", "optimist"),
            ("I feel like giving up 😢", "pessimist"),
            ("It’s part of life 🧘", "realist"),
            ("It wasn’t meant to be 🌌", "idealist")
        ]
    },
    {
        "question": "9. What motivates you?",
        "options": [
            ("Belief that good things are ahead 🌞", "optimist"),
            ("Fear of things going wrong 😬", "pessimist"),
            ("A clear plan and goals 🎯", "realist"),
            ("A dream of a better world 🕊️", "idealist")
        ]
    },
    {
        "question": "10. How do you make decisions?",
        "options": [
            ("Follow my heart ❤️", "optimist"),
            ("Worry about the risks ⚠️", "pessimist"),
            ("Think carefully and logically 🧠", "realist"),
            ("Choose what feels like a dream path 🌈", "idealist")
        ]
    },
]

personality_descriptions = {
    "optimist": "🌞 You always see the bright side and bring joy to others!",
    "pessimist": "🌧️ You’re cautious and realistic about life’s challenges.",
    "realist": "🔍 You think clearly, stay calm, and handle life with logic.",
    "idealist": "🌠 You believe in a better world and love to dream big!"
}

# GUI App Class
class PersonalityQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 What Kind of Person Are You? 🌟")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")

        self.current_q = 0
        self.scores = {"optimist": 0, "pessimist": 0, "realist": 0, "idealist": 0}

        self.title = tk.Label(root, text="🎭 Personality Quiz", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#4b0082")
        self.title.pack(pady=20)

        self.q_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=500, bg="#f0f8ff", fg="#000080")
        self.q_label.pack(pady=10)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Helvetica", 14), width=50, wraplength=400, command=lambda i=i: self.answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.load_question()

    def load_question(self):
        q_data = questions[self.current_q]
        self.q_label.config(text=q_data["question"])
        for i, (text, _) in enumerate(q_data["options"]):
            self.buttons[i].config(text=text)

    def answer(self, choice_index):
        _, personality = questions[self.current_q]["options"][choice_index]
        self.scores[personality] += 1
        self.current_q += 1

        if self.current_q < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for btn in self.buttons:
            btn.destroy()
        self.q_label.destroy()
        self.title.config(text="🎉 Your Result!")

        top_score = max(self.scores.values())
        top_types = [ptype for ptype, score in self.scores.items() if score == top_score]

        result_text = ""
        if len(top_types) == 1:
            result_text += f"\n💡 You are a {top_types[0].capitalize()}!\n"
        else:
            result_text += "💡 You are a mix of: " + ", ".join(t.capitalize() for t in top_types) + "\n"

        for t in top_types:
            result_text += f"\n{personality_descriptions[t]}"

        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 14), wraplength=550, bg="#f0f8ff", fg="#333333")
        result_label.pack(pady=20)

        exit_button = tk.Button(self.root, text="Exit", font=("Helvetica", 14), command=self.root.destroy)
        exit_button.pack(pady=10)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityQuiz(root)
    root.mainloop()
