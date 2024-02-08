class InstructionsPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Instructions")
        self.geometry("800x400")
        self.configure(background='medium slate blue')

        instructions_text = """
            Welcome to the GPA Calculator!

            1. First after clicking Lets Go button, you will be prompted to save the file.

            2. Enter the grades, course types, and credits for each course.

            3. Click on "Calculate Weighted GPA" or "Calculate Unweighted GPA" to get your GPA.

            4. Use "Start Over" to clear all entered data.

            5. Adjust the number of courses using "Adjust Number of Courses."

            6. Click on "Q&A" to get answers to common questions.

            7. The program is autobackup. To create a new file, you have to click on "New Calculation" button.

            8. Load data using the "Load Backup" button.

            9. "Delete Backup" removes a previously saved backup.

            10. Before clicking on "Generate and Save Report," remember to have your data inputted, or the backup inputted.

            11. Click "Generate and Save Report" to save your GPA to your files, as well as being able to print it out for a physical copy.

            12. Click "Exit" to close the application.
        """

        self.instructions_label = tk.Label(self, text=instructions_text, justify=tk.LEFT)
        self.instructions_label.pack(padx=10, pady=10)
