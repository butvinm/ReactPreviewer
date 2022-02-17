<p align="center">
  <img src="icon.svg" alt="Python GUIs for Humans" height="100px">
  <h1 align="center">React Previewer</h1>
</p>

# What
VERY simple browser based on PySide WebView that provides easy ReactNative applications preview in standalone window

# Creating reason
<p>
That program was created cause ReactNative has handy feature - browser preview - but most of browsers have fixed minimum width of window (and build-in vs code browsers from extension too) and you can not open it with your code editor convenient.
</p>
<p>
But with this application your workspace may look like that: 
<img src="screenshot0.png"/>
</p>

# Features
<h3>All browser functionality consists in menu bar:</h3>
<p><img src="screenshot3.png" width="80%"/></p>

So, you can:
- Reload page
- Change url
- Enable border
- Enable fringe
- Change size ratio

<h3>
	If border or/and fringe enabled rounded borders and fringe images stack on page:
</h3>
<p>
	<img src="screenshot1.png" width="30%" style="margin-right: 100px;"/>
	<img src="screenshot2.png" width="30%"/>
</p>

# Compilation instruction

If you want to compile program to binary install pyinstaller (https://pyinstaller.readthedocs.io/en/stable/usage.html) and run that command in terminal at ReactPreviewer directory:
<p><strong>$ pyinstaller main.spec</strong></p>