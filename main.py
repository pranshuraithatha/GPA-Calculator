import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import json
import os
import webbrowser
import tkinter.filedialog as filedialog
import ChangeRowsPage.py
import GPA_Calculator.py
import InstructionsPage.py
import QAPage.py
import WelcomePage.py

# Constants for grade values and quality points
GRADE_VALUES = {"A": 4.0, "B": 3.0, "C": 2.0, "F": 0.0}

COURSE_QUALITY_POINTS_WEIGHTED = {
    "Honors": 0.0,
    "On-level": 0.0,
    "Accelerated": 0.0,
    "AP": 1.0,
    "IB": 1.0
}

COURSE_QUALITY_POINTS_UNWEIGHTED = {
    "Honors": 0.0,
    "On-level": 0.0,
    "Accelerated": 0.0,
    "AP": 0.0,
    "IB": 0.0
}

if __name__ == "__main__":
    WelcomePage()
