import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 18, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.question_label = tk.Label()
        self.question_label.config(text="Question 0", bg=THEME_COLOR, fg="white")
        self.question_label.grid(row=1, column=1, padx=20, pady=20)

        self.score_label = tk.Label()
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2, padx=20, pady=20)

        self.question_canvas = tk.Canvas(width=300, height=250,
                                         bg="WHITE", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125,
                                                              font=QUESTION_FONT, fill=THEME_COLOR,
                                                              width=290, justify="left")
        self.question_canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        self.true_button = tk.Button()
        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button.config(image=self.true_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.true)
        self.true_button.grid(row=3, column=1, pady=20)

        self.false_button = tk.Button()
        self.false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button.config(image=self.false_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.false)
        self.false_button.grid(row=3, column=2, pady=20)

        self.has_finished = False
        self.color_response_to_answer = None

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.question_label.config(text=f"Question {self.quiz_brain.question_number}")
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.question_canvas.itemconfig(self.question_text, text=question)
        else:
            if not self.has_finished:
                self.question_canvas.itemconfig(self.question_text, text=f"Quiz finished.\n"
                                                                         f"Final score: {self.quiz_brain.score}/"
                                                                         f"{self.quiz_brain.question_number}")
                self.has_finished = True

    def true(self):
        if self.color_response_to_answer is not None:
            pass
        else:
            if not self.has_finished:
                self.send_answer("true")
            else:
                pass

    def false(self):
        if self.color_response_to_answer is not None:
            pass
        else:
            if not self.has_finished:
                self.send_answer("false")
            else:
                pass

    def send_answer(self, answer: str):
        self.result_ui(self.quiz_brain.check_answer(answer))

    def result_ui(self, correct: bool):
        if correct:
            color = "green"
        else:
            color = "red"

        self.question_canvas.config(bg=color)
        self.color_response_to_answer = self.window.after(1000, func=self.reset_canvas)

    def reset_canvas(self):
        self.question_canvas.config(bg="white")
        self.get_next_question()
        self.color_response_to_answer = None
