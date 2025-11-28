

import wx
import random

app = wx.App()

frame = wx.Frame(None, title="Rock Paper Scissors", size=(360, 430))
panel = wx.Panel(frame)

choices = ["rock", "paper", "scissors"]

user_score = 0
comp_score = 0
round_num = 0
total_rounds = 0

EMOJI = {
    "rock": "🪨 Rock",
    "paper": "📄 Paper",
    "scissors": "✂️ Scissors"
}

round_label = wx.StaticText(panel, label="")
user_label = wx.StaticText(panel, label="")
comp_label = wx.StaticText(panel, label="")
result_label = wx.StaticText(panel, label="")
score_label = wx.StaticText(panel, label="Score → You: 0 | Computer: 0")

rounds_text = wx.StaticText(panel, label="Enter number of rounds:")
round_box = wx.TextCtrl(panel, size=(120, -1))

def start_game(event):
    global total_rounds, round_num, user_score, comp_score
    txt = round_box.GetValue()
    if not txt.isdigit() or int(txt) <= 0:
        wx.MessageBox("Enter a valid positive number", "Error")
        return
    total_rounds = int(txt)
    round_num = 0
    user_score = 0
    comp_score = 0
    round_label.SetLabel(f"Game started: 0/{total_rounds}")
    user_label.SetLabel("")
    comp_label.SetLabel("")
    result_label.SetLabel("")
    score_label.SetLabel("Score → You: 0 | Computer: 0")

def play(user_choice):
    global round_num, user_score, comp_score
    if total_rounds == 0:
        wx.MessageBox("Start the game first!", "Info")
        return
    if round_num >= total_rounds:
        return

    round_num += 1
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "🤝 Tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        user_score += 1
        result = "🎉 You win!"
    else:
        comp_score += 1
        result = "💻 Computer wins!"

    round_label.SetLabel(f"Round {round_num}/{total_rounds}")
    user_label.SetLabel(f"You chose: {EMOJI[user_choice]}")
    comp_label.SetLabel(f"Computer chose: {EMOJI[comp_choice]}")
    result_label.SetLabel(result)
    score_label.SetLabel(f"Score → You: {user_score} | Computer: {comp_score}")

    if round_num == total_rounds:
        if user_score > comp_score:
            msg = "🎉 You won the game!"
        elif comp_score > user_score:
            msg = "💻 Computer won the game!"
        else:
            msg = "🤝 It's a tie overall!"
        wx.MessageBox(msg, "Game Over")

start_btn = wx.Button(panel, label="Start Game")
start_btn.Bind(wx.EVT_BUTTON, start_game)

rock_btn = wx.Button(panel, label="🪨 Rock")
paper_btn = wx.Button(panel, label="📄 Paper")
scissors_btn = wx.Button(panel, label="✂️ Scissors")

rock_btn.Bind(wx.EVT_BUTTON, lambda e: play("rock"))
paper_btn.Bind(wx.EVT_BUTTON, lambda e: play("paper"))
scissors_btn.Bind(wx.EVT_BUTTON, lambda e: play("scissors"))

sizer = wx.BoxSizer(wx.VERTICAL)

widgets = [
    rounds_text, round_box, start_btn,
    round_label, user_label, comp_label,
    result_label, score_label,
    rock_btn, paper_btn, scissors_btn
]

for w in widgets:
    sizer.Add(w, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 12)

panel.SetSizer(sizer)

frame.Show()
app.MainLoop()


