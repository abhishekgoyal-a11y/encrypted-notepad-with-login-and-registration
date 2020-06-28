import cx_Freeze
executables = [cx_Freeze.Executable("login.py")]

cx_Freeze.setup(
    name="LOGIN SYSTEM",
    options={"build_exe": {"packages":["tkinter"],
                            "include_files": ["notepad.ico"]}},
    executables = executables
    )
