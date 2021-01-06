from cx_Freeze import *

includefiles = ['calc.ico']
base = "win32GUI"

shortcut_table = [
    ("DekstopShortcut",
    "DekstopFolder",
    "calculator",
    "TARGETDIR",
    "[TARGETDIR]\adityacalculator.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR"
    )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_option = {'data':msi_data}
setup(
    version='0.1',
    description="calculator",
    author="Aditya Bhushan",
    name="calculator",
    option={'build_exe':{"include_files":includefiles},"bdist_msi":bdist_msi_option},
    executables=[
        Executable(
            script="adityacalculator.py",
            base=base,
            icon='calc.ico'
        )
    ]
)