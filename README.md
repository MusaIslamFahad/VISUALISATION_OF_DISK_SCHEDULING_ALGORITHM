# 🌟 Disk Scheduling Algorithm Visualizer 🌟

This Python application, "Disk Scheduling," provides a comprehensive tool for visualizing and comparing various disk scheduling algorithms. Developed with `tkinter` for the GUI and `matplotlib` for dynamic visualizations, it allows users to experiment with different algorithms and understand their performance in terms of seek time. Here's how to interact with this tool:

---

**🚀 START HERE: SET UP YOUR SIMULATION**  
1. **Input Requests**  
   *In the "Enter Request Points" field:*  
   `Type` a comma-separated list (e.g., `98, 183, 37, 122, 14`).  
   *(Pro Tip: Use the sample data first to see it in action!)*  

2. **Configure Settings**  
   - **Initial Head Position**: Where does the read/write head start? *(e.g., `53`)*  
   - **Direction** (for SCAN/C-SCAN/LOOK/C-LOOK): Choose `LEFT` or `RIGHT` from the dropdown.  
   - **Cylinder Range**: Define your disk size (Min: `0`, Max: `200` by default).  

---

**🔧 PRACTICE TAB: MASTER ONE ALGORITHM**  
*Want to see how SSTF reduces seek time? Or why SCAN acts like an elevator?*  

1. **Select an Algorithm**  
   Choose from:  
   - `FCFS` (First-Come, First-Served)  
   - `SSTF` (Shortest Seek Time First)  
   - `SCAN` (Elevator Algorithm)  
   - `C-SCAN` (Circular SCAN)  
   - `LOOK` / `C-LOOK`  

2. **Click "RUN"**  
   Watch the animation! The red line shows the head movement, and dots mark requested tracks.  

3. **Analyze the Results**  
   - Total seek time displayed instantly.  
   - Track access sequence listed below.  
   - *Example: "SSTF: 236 seeks | Sequence: 53 → 37 → 14 → ..."*  

4. **Save Your Report**  
   Hit "SAVE" to generate a PDF with your inputs, results, and a summary.  

---

**📊 COMPARISON TAB: BATTLE OF ALGORITHMS**  
*Which algorithm is fastest for your workload? Let’s find out!*  

1. **Check Multiple Algorithms**  
   *(Try selecting SSTF, SCAN, and LOOK together!)*  

2. **Click "RUN COMPARISON"**  
   A bar chart appears:  
   - **Bars**: Total seek time for each algorithm.  
   - **Green Highlight**: The winner (lowest seek time).  

3. **Compare Behavior**  
   *Why does C-SCAN sometimes outperform SCAN? Use different directions to test!*  

---

**🎓 LEARNING MODE: PRO TIPS**  
- **Test Edge Cases**: What if requests are *already sorted*? Try FCFS vs SSTF.  
- **Reverse Direction**: Change from `RIGHT` to `LEFT` in SCAN/C-SCAN to see how the path changes.  
- **Extreme Requests**: Add a request close to the `MAX` cylinder (e.g., `200`) to watch C-SCAN wrap around.  

---

**⚙️ TECHNICAL NOTES**  
- **Install Dependencies**: Run `pip install matplotlib numpy pyttsx3 gTTS fpdf Pillow` if you haven’t.  
- **OS Compatibility**: Works best on Windows/macOS with Python 3.7+.  

---

**📁 SAMPLE WORKFLOW**  
1. Input: `98, 183, 37, 122, 14, 124, 65, 67`  
2. Head Start: `53` | Direction: `RIGHT` | Max Cylinder: `200`  
3. **Practice Tab**: Run `SCAN` → See the head sweep to `200` before reversing.  
4. **Comparison Tab**: Select `FCFS`, `SSTF`, `SCAN` → SSTF wins with the lowest seeks!  

---

**🔗 GET STARTED NOW**  
Clone the code, run `OS_PROJECT.py`, and start optimizing virtual disk arms like a pro! 🖥️  
