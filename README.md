# VISUALISATION_OF_DISK_SCHEDULING_ALGORITHM
This Python application, "Disk Scheduling," provides a comprehensive tool for visualizing and comparing various disk scheduling algorithms. Developed with tkinter for the GUI and matplotlib for dynamic visualizations, it allows users to experiment with different algorithms and understand their performance in terms of seek time.
Features:

    Algorithm Visualization (Practice Tab):
        FCFS (First-Come, First-Served): Simulates and visualizes the FCFS algorithm, showing the seek operations and total seek time.
        SSTF (Shortest Seek Time First): Implements and graphically represents SSTF, highlighting how it minimizes seek time by prioritizing the closest request.
        SCAN (Elevator Algorithm): Visualizes the SCAN algorithm, demonstrating its movement across the disk and handling of requests based on direction.
        C-SCAN (Circular SCAN): Shows the C-SCAN algorithm's behavior, which is similar to SCAN but wraps around to the other end of the disk after reaching one extreme.
        LOOK: Simulates the LOOK algorithm, an optimization of SCAN where the head only travels as far as the last request in each direction.
        C-LOOK: Visualizes the C-LOOK algorithm, an optimized version of C-SCAN that only moves as far as the last request in each direction before reversing.
        Interactive Plots: Each algorithm's execution is animated with a matplotlib graph, showing the read/write head position against the seek time spent.
        Detailed Reports: Provides the total number of seek operations and the sequence of accessed tracks for each algorithm.
        PDF Export: Allows users to save the input parameters and the algorithm's output (seek time and sequence) as a PDF report.

    Algorithm Comparison (Comparison Tab):
        Multiple Algorithm Selection: Users can select and compare the performance (total seek time) of multiple disk scheduling algorithms simultaneously.
        Best Algorithm Identification: The application identifies and displays the algorithm with the minimum seek time for the given set of requests.
        Individual Seek Times: Shows the calculated total seek time for each selected algorithm, enabling direct comparison.

How to Use:

    Input Request Points: Enter a comma-separated list of cylinder numbers in the "Enter Request Points" field.
    Set Initial Head Position: Specify the starting position of the read/write head.
    Choose Direction (for SCAN/C-SCAN/LOOK/C-LOOK): Select "RIGHT" or "LEFT" for the initial direction of the head movement.
    Define Cylinder Range: Input the maximum and minimum cylinder numbers for the disk.
    Select Algorithm (Practice Tab): Choose a single algorithm from the dropdown menu and click "RUN" to see its visualization and report.
    Compare Algorithms (Comparison Tab): Select multiple algorithms using the checkboxes and click "RUN" to compare their seek times and identify the best performer.
    Save Report: Use the "SAVE" button on the Practice tab to export the current algorithm's details and results into a text file.

Requirements:

    Python 3.x
    tkinter (usually bundled with Python)
    matplotlib
    numpy
    pyttsx3
    gTTS
    fpdf
    Pillow (for matplotlib integration with tkinter if issues arise)

You can install the required libraries using pip:
pip install matplotlib numpy pyttsx3 gTTS fpdf Pillow
File Structure:

    OS_PROJECT.py: The main Python script containing the GUI, algorithm implementations, and visualization logic.

This project serves as an educational tool for understanding disk scheduling concepts and their practical implications in operating systems.
