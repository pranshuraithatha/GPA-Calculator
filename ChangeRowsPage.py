class ChangeRowsPage(tk.Toplevel):
    MAX_COURSES = 13
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Change Number of Rows")
        self.geometry("400x200")
        self.configure(background='lightblue')

        self.instructions_label = tk.Label(self, text="Sure thing! How many courses would you like now?")
        self.instructions_label.pack()

        self.course_entry = tk.Entry(self)
        self.course_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Update", command=self.on_submit)
        self.submit_button.pack()

    def on_submit(self):
        try:
            course_count = int(self.course_entry.get())
            if 1 <= course_count <= self.MAX_COURSES:
                self.destroy()
                parent = self.master
                parent.update_course_count(course_count)
            else:
                messagebox.showerror("Error", f"Oops! Please enter a number between 1 and {self.MAX_COURSES}.")
        except ValueError:
            messagebox.showerror("Error", "Oops! Please enter a valid number.")
