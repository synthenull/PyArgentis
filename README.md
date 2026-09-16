# PyArgentis

PyArgentis is a build-time tool for protecting Python applications on Windows. It turns your source into an encrypted runtime package and can optionally produce a standalone EXE for distribution.

![PyArgentis Protector GUI](https://raw.githubusercontent.com/synthenull/PyArgentis/refs/heads/main/screenshots/pyargentis_gui.png)

---

## Features

- **No source in the release** - end users receive a protected runtime package, not your original `.py` files.
- **Advanced Strong Encryption & Obfuscation** - application logic is protected at build time.
- **Import/Memory/String Protections** - protect imported modules, runtime memory, and sensitive string data from unauthorized inspection.
- **Error / Exception Protection** - prevent error messages, tracebacks, and runtime exceptions from exposing sensitive application or source information.
- **Anti-Debugger / Anti-Analysis** - detect and resist common debugging and analysis attempts during runtime.
- **Anti-Tamper / Anti-Dump** - detect unauthorized modifications and add protection against runtime dumping and code extraction.
- **Metadata Removal & Code Cleanup** - remove unnecessary metadata, debug information, comments, and other potentially sensitive artifacts from the protected build.
- **Optional EXE packaging** - bundle a single-file or folder-based executable with PyInstaller.
- **Optional Only-EXE deliverable** - pack and keep a single `.exe` under `output/<project>/` with no intermediate package files left behind.
- **Extra protector support (Themida)** - after compiling the application to an EXE, you can protect the output EXE with Themida.
- **Machine binding** - optional HWID lock and Windows-specific key binding for licensed deployments.
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
2. **Protect a script**

```bat
pyargentis create examples\example_1.py
```

Protected output is written under `output/<project>/` (for example `output\example_1\main.py` plus the native runtime).

3. **Run the protected app**

```bat
python output\example_1\main.py
```

**Optional - build an EXE** (keeps the protected package; EXE under `dist\`)

```bat
pyargentis create examples\example_1.py --pack
```

**Optional - single EXE only** (no `main.py` / `.pyd` leftovers)

```bat
pyargentis create examples\example_1.py --only-exe -w --uac-admin --no-icon
```

**GUI**

```bat
launch_gui.bat
```

**CLI help**

```bat
pyargentis -h
pyargentis -v
```

---

## Common options

```text
pyargentis create <source.py> [options]
```

| Option | Purpose |
|--------|---------|
| `--pack` | Build an EXE after protect (`output/<project>/dist/<name>.exe`) |
| `--only-exe` | Pack to a single EXE and remove package leftovers (`output/<project>/<name>.exe`) |
| `--open-folder` | Open `output/<project>/` when finished |
| `-p`, `--project` | Output folder name |
| `--name` | EXE base name (default: project name) |
| `-w`, `--noconsole` | Hide the console window |
| `--uac-admin` | Request administrator elevation for the EXE |
| `--no-icon` / `-i` | Default icon, or custom `.ico` |
| `--bind-hwid` | Lock execution to the build machine fingerprint |
| `--dpapi-bind` | Bind protection to this Windows installation |

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

## Getting help

Open an issue on GitHub with your Python version and the command or GUI steps you used. Include log output when reporting a build failure.
