import tkinter as tk
import random

# Start with the full character pool
all_characters = [
    "Shrek", "Elon Musk", "MrBeast", "Taylor Swift", "SpongeBob", "Batman", "Albert Einstein",
    "Dwayne Johnson", "Billie Eilish", "Wednesday Addams", "Barbie", "Naruto", "Queen Elizabeth",
    "Ronaldo", "Harry Potter", "Iron Man"
]

# Funny random result options
funny_comments = [
    ("You guys are unstoppable!", 100),
    ("Strong team with questionable fashion.", 85),
    ("You’ll survive, but it’s gonna be chaotic.", 70),
    ("Good luck… You’ll need it.", 50),
    ("You’ll probably end up zombies in 5 mins.", 25),
    ("You're doomed, but at least it's funny.", 10)
]

class ZombieTeamBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("🧟‍♂️ Build Your Zombie Survival Team!")
        self.root.geometry("700x500")
        self.root.configure(bg="black")

        self.available_characters = all_characters.copy()
        self.team = []
        self.round = 1

        self.title_label = tk.Label(root, text="🧠 Pick your teammate!", font=("Comic Sans MS", 22, "bold"), fg="lime", bg="black")
        self.title_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 16), width=30, bg="#222", fg="cyan", activebackground="green", command=lambda i=i: self.select_character(i))
            btn.pack(pady=10)
            self.option_buttons.append(btn)

        self.status_label = tk.Label(root, text="", font=("Arial", 16), fg="yellow", bg="black")
        self.status_label.pack(pady=20)

        self.next_round()

    def next_round(self):
        self.status_label.config(text=f"Team so far: {', '.join(self.team) if self.team else 'No one yet'}")
        self.title_label.config(text=f"🧠 Round {self.round}: Pick a teammate")

        # Make sure only unpicked characters are shown
        self.choices = random.sample(self.available_characters, 4)
        for i, char in enumerate(self.choices):
            self.option_buttons[i].config(text=char)

    def select_character(self, index):
        selected = self.choices[index]
        self.team.append(selected)
        self.available_characters.remove(selected)

        if self.round == 4:
            self.show_result()
        else:
            self.round += 1
            self.next_round()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        comment, chance = random.choice(funny_comments)
        team_string = ", ".join(self.team)

        tk.Label(self.root, text="🧟‍♂️ YOUR ZOMBIE APOCALYPSE SQUAD", font=("Impact", 22), fg="cyan", bg="black").pack(pady=30)
        tk.Label(self.root, text=team_string, font=("Comic Sans MS", 18), fg="lime", bg="black", wraplength=600).pack(pady=20)
        tk.Label(self.root, text=f"🧬 Survival Chance: {chance}%", font=("Arial", 18), fg="orange", bg="black").pack(pady=10)
        tk.Label(self.root, text=comment, font=("Comic Sans MS", 16), fg="yellow", bg="black", wraplength=600, justify="center").pack(pady=20)

        tk.Button(self.root, text="🔁 Build New Team", font=("Arial", 14), bg="purple", fg="white", command=self.restart).pack(pady=20)

    def restart(self):
        self.available_characters = all_characters.copy()
        self.team = []
        self.round = 1
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

# Run the app
root = tk.Tk()
app = ZombieTeamBuilder(root)
root.mainloop()
