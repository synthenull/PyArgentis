# PyArgentis

PyArgentis is a build-time tool for protecting Python applications on Windows. It turns your source into an encrypted runtime package and can optionally produce a standalone EXE for distribution.

![PyArgentis Protector GUI](https://raw.githubusercontent.com/synthenull/PyArgentis/refs/heads/main/screenshots/pyargentis_gui.png)

---

## Features

- **Protected Source Distribution** - distribute protected application code without shipping the original source files for protected modules.
- **Advanced Strong Encryption & Obfuscation** - application logic is protected at build time.
- **Import/Memory/String Protections** - protect imported modules, runtime memory, and sensitive string data from unauthorized inspection.
- **Error / Exception Protection** - remove original source paths and line-table information from protected code objects.
- **Anti-Debugger / Anti-Analysis** - detect and resist common debugging and analysis attempts during runtime.
- **Anti-Tamper / Anti-Dump** - detect unauthorized modifications and add protection against runtime dumping and code extraction.
- **Import Hook** - load bundled protected Python files through a custom import loader without requiring separate source files.
- **Metadata Cleanup** - nonymize source paths, remove line-table information, and obscure eligible code identifiers.
- **Executable Security Checks** - check packaged executables for known unprotected project-file copies and development artifacts.
- **Optional Docstring Cleanup** - enable Clean docstrings to remove documentation strings when application compatibility permits.
- **Optional EXE packaging** - bundle a single-file or folder-based executable with PyInstaller.
- **Optional Only-EXE deliverable** - pack and keep a single `.exe` under `output/<project>/` with no intermediate package files left behind.
- **Extra protector support (Themida)** - after compiling the application to an EXE, you can protect the output EXE with Themida.
- **Device Binding** - optionally restrict execution using Hardware ID or Windows Installation binding.
- **GUI and CLI** - protect applications from the desktop interface or automate protection workflows from the command line.

---

## Supported environment

- **OS:** Windows 10/11 (64-bit)
- **Python:** 3.12, 3.13, 3.14

Use the same Python feature release for building and running protected output when possible.

---

## Quick start

1. **Get the project**
```bat
To get the project, contact synthenull.
```
2. **Protect a script (CLI)**

```bat
pyargentis create examples\example_1.py
```

Protected output is written under `output/<project>/`. The generated `main.py` contains the embedded native runtime; no separate runtime `.pyd` is shipped.

3. **Run the protected app**

```bat
python output\example_1\main.py
```

**Optional - build an EXE (CLI)** (keeps the protected package; EXE under `dist\`)

```bat
pyargentis create examples\example_1.py --pack
```

**Optional - single EXE only (CLI)** (no `main.py` / `.pyd` leftovers)

```bat
pyargentis create examples\example_1.py --only-exe -w --uac-admin --no-icon
```

**GUI (Recommended)**

```bat
launch_gui.bat
```

**CLI help**

```bat
pyargentis -h
pyargentis -v
```

---

## CLI Commands

```text
pyargentis create <source.py> [options]
```

| Option | Purpose |
|--------|---------|
| `--pack` | Build an EXE after protect (`output/<project>/dist/<name>.exe`) |
| `--only-exe` | Pack to a single EXE and remove package leftovers (`output/<project>/<name>.exe`) |
| `--open-folder` | Open `output/<project>/` when finished |
| `-p`, `--project` | Output folder name |
| `-k`, `--key-file` | Storage key file (default: `keys/project.key`) |
| `-w`, `--noconsole` | Hide the console window |
| `--name` | EXE base name (default: project name) |
| `--uac-admin` | Request administrator elevation for the EXE |
| `--onedir` | Onedir output instead of onefile (not allowed with --only-exe) |
| `--no-scan-imports` | Disable automatic import scanning of the source file |
| `--hidden-import` | Extra PyInstaller hidden-import (repeatable) |
| `--target-python` | Select the target Python version `{3.12,3.13,3.14}` |
| `--no-icon` | Disable custom icon selection (`icon=NONE`) |
| `-i`, `--icon` | Set a custom EXE icon from an `.ico` file |
| `--runtime-dir` / `--engine-dir` | Directory of runtime .pyd files |
| `--device-binding` | Set device binding `{off,hwid,windows}` |
| `--obfuscation-level` | Set the obfuscation level `{standard,maximum,extreme}` |
| `--clean-docstrings` | Remove docstrings from protected code |
| `--protect-imported-python-files` | Protect discovered project-local Python imports |

You can also run `pyargentis your_app.py` as shorthand for `create`.

For the full flag list: `pyargentis -h`.

---

## Suggested release flow

1. Protect your application  
3. Pack with `--pack`, or ship a single file with `--only-exe`  
4. Ship only the release artifact - not your source or builder keys  

Builder keys and local metadata stay on your development machine; they are not part of the customer package.

---

## License

Proprietary - see [LICENSE](LICENSE). Redistribution of the tool is not permitted unless your agreement allows it.

---

## Links

- **Repository:** [github.com/synthenull/PyArgentis](https://github.com/synthenull/PyArgentis)
- **Changelog:** [docs/RELEASES.md](docs/RELEASES.md)

---

## Getting Help

If you encounter an issue, please open a GitHub issue and include the following information:

* Your Python version
* The command or GUI steps that caused the issue
* The complete error message
* Any relevant error codes or logs

Providing these details will help us diagnose and resolve the problem more quickly.

---
