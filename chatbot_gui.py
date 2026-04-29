import tkinter as tk
from tkinter import scrolledtext
import random
from train_model import predict_intent
from chatbot_model import responses

def send_message():
    user_input = entry.get().strip()

    if user_input == "":
        return

    display_message(user_input, "user")

    if user_input.lower() in ["bye", "exit", "quit"]:
        display_message("Goodbye! 🚀", "bot")
        root.after(1000, root.quit)
        return

    try:
        intent = predict_intent(user_input)

        if intent in responses:
            reply = random.choice(responses[intent])
        else:
            reply = "Sorry, I don't understand your question."

    except:
        reply = "Something went wrong."

    display_message(reply, "bot")
    entry.delete(0, tk.END)


def display_message(message, sender):
    if sender == "user":
        chat_area.insert(tk.END, f"🧑 {message}\n", "user")
    else:
        chat_area.insert(tk.END, f"🤖 {message}\n\n", "bot")

    chat_area.yview(tk.END)


# Window setup
root = tk.Tk()
root.title("🤖 Tech Education World Chatbot")
root.geometry("480x580")
root.configure(bg="#121212")

# Header
header = tk.Label(
    root,
    text="Tech Education World",
    bg="#121212",
    fg="#00adb5",
    font=("Arial", 18, "bold")
)
header.pack(pady=5)

subheader = tk.Label(
    root,
    text="Ask about courses, internships, webinars & more 🚀",
    bg="#121212",
    fg="white",
    font=("Arial", 10)
)
subheader.pack()

# Chat area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=10,
    borderwidth=0
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Styling tags
chat_area.tag_config("user", foreground="#00ffcc", font=("Arial", 12, "bold"))
chat_area.tag_config("bot", foreground="#ffffff", font=("Arial", 12))

# Input frame
frame = tk.Frame(root, bg="#121212")
frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(
    frame,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_button = tk.Button(
    frame,
    text="Send 🚀",
    bg="#00adb5",
    fg="white",
    font=("Arial", 10, "bold"),
    command=send_message
)
send_button.pack(side=tk.RIGHT)

# Enter key support
root.bind("<Return>", lambda event: send_message())

root.mainloop()