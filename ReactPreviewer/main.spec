# -*- mode: python ; coding: utf-8 -*-
import sys
import os

path = os.path.abspath(".")


a = Analysis(
    ["main.py"],
    pathex=[path],
    datas=[('border.png', '.'), ('icon.ico', '.'), ('fringe.png', '.')],
    hookspath=[],
    excludes=['cv2', 'numpy'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    debug=False,
    strip=False,
    upx=True,
    name="ReactPreviewer",
    console=False,
    icon="icon.ico"
)
