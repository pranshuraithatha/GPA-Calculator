class QAPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Q&A Page")
        self.geometry("400x200")
        self.configure(background='medium slate blue')

        self.question_label = tk.Label(self, text="Select a Question:")
        self.question_label.pack()

        self.question_var = tk.StringVar()
        self.question_dropdown = tk.OptionMenu(self, self.question_var, *self.get_question_list())
        self.question_dropdown.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit_button.pack()

    def get_question_list(self):
        # Defining the predefined questions here
        questions = [
            "What is the GPA calculation formula?",
            "How are weighted and unweighted GPAs different?",
            "Can I include courses without credit in the calculation?",
            "Which type of files will the report save as?"
            # Add more questions as needed
        ]
        return questions

    def on_submit(self):
        selected_question = self.question_var.get()
        if selected_question:
            # Get the answer based on the selected question
            answer = self.get_answer(selected_question)
            messagebox.showinfo("Answer", answer)
            self.destroy()
        else:
            messagebox.showwarning("Warning", "Please select a question.")

    def get_answer(self, question):
        # Define corresponding answers for each question
        answers = {
            "What is the GPA calculation formula?": "The GPA is calculated by dividing the total quality points by the total credits.",
            "How are weighted and unweighted GPAs different?": "Weighted GPA considers the difficulty of courses, giving extra points for honors, AP, or IB courses.",
            "Can I include courses without credit in the calculation?": "No, only courses with assigned credits are considered in the GPA calculation.",
            "Which type of files will the report save as?":"It is going to save in a notepad if you generate report, and if you back the data up in a json file.",
            # Add more answers as needed
        }
        return answers.get(question, "Sorry, the answer is not available.")
