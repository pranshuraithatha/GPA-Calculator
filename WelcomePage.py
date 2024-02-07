class WelcomePage(tk.Tk):
    MAX_COURSES = 13
    def __init__(self):
        super().__init__()
        self.title("Welcome to GPA Calculator")
        self.geometry("400x200")
        self.configure(background='medium slate blue')

        self.welcome_label = tk.Label(self, text="Welcome to the GPA Calculator!", font=("Helvetica", 16), pady=20)
        self.welcome_label.pack()

        self.instructions_label = tk.Label(self, text="Ready to calculate your GPA? Enter the number of courses:")
        self.instructions_label.pack()

        self.course_entry = tk.Entry(self)
        self.course_entry.pack(pady=10)

        self.instructions_button = tk.Button(self, text="Instructions", command=self.show_instructions)
        self.instructions_button.pack()

        self.submit_button = tk.Button(self, text="Let's Go!", command=self.on_submit)
        self.submit_button.pack()

    def on_submit(self):
        try:
            course_count = int(self.course_entry.get())
            if 1 <= course_count <= self.MAX_COURSES:
                self.destroy()
                gpa_calculator = GPA_Calculator(course_count)
                gpa_calculator.mainloop()
            else:
                messagebox.showerror("Error", f"Oops! Please enter a number between 1 and {self.MAX_COURSES}.")
        except ValueError:
            messagebox.showerror("Error", "Oops! Please enter a valid number.")

    def show_instructions(self):
        instructions_page = InstructionsPage(self)
