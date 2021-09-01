<p align="center">
  <img height=180 src="readme_assets/logo.png">
</p>

#### What is Time tracker?

Time tracker is a GUI version of the script called [time-tracker-cli](https://github.com/pazitos10/time-tracker-cli).

#### Dependencies

* `PyQt5`
* `time-tracker-cli`
* `Pandas`
* `Plotly`

Install them via: `pip install -r requirements.txt`

#### How to use:

The binary version is not available yet but you can run it manually anyway: `python app.py`

1) Create your data file or open an existing one.

<p align="center">
  <img src="readme_assets/0_1.png">
  <img src="readme_assets/0_2.png">
</p>

2) Create projects/tasks you want to work on. Once created, every task is marked as started.

<p align="center">
  <img src="readme_assets/1.png">
</p>

3) Edit (rename) or remove tasks as you please.

<p align="center">
  <img src="readme_assets/2.png">
</p>

4) Start/Stop your working sessions.

<p align="center">
  <img src="readme_assets/3.png">
</p>

<p align="center">
  <img src="readme_assets/4.png">
</p>

5) Data is stored in a JSON file. <br><br>

6) View a visual report of "Work done per project" by clicking on `Report>Projects Chart` from the Menu Bar. The chart is displayed on your default browser.

<img align="center" src="readme_assets/fig1.svg" width="100%">

7) View a visual report of "Daily Work Done" by clicking on `Report>Time-Series Chart` from the Menu Bar. The chart is displayed on your default browser. Show/hide projects on the chart by clicking once on its legend entry. Isolate/deisolate projects on the chart by double-clicking on its legend entry.

<img align="center" src="readme_assets/fig2.svg" width="100%">

8) Interact with the reports and export them:
   - Plots can be exported as png.
   - Plots can be panned and zoomed.
   - Plots have tooltips on mouse hover. Try hovering over different bars on the plot to reveal additional info.
   - For more info regarding functionality of the plots see [Plotly](https://plotly.com/python/) documentation.
<br><br>

#### TODO

 - [x] Clean and document the code.
 - [ ] Create binary versions.
 - [ ] Redesign logo.
 - [ ] (Optional) replace text in buttons with icons.
