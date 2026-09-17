# Changelog

## v1.6.0 - 2026-09-09

### Added
* Code obfuscation level option for GUI and CLI (Standard / Maximum / Extreme).

### Changed
* Packaged EXE files are now smaller.
* The GUI checkboxes have been changed to toggle buttons.

### Security
* Multi-stage hardening implemented against both static and dynamic reverse engineering of the runtime component.

### Removed
* The Output tab has been removed from the GUI.

### Fixed
* Various bugs fixed.

---

## V1.5 - 2026-07-20

### Added
* The CLI has been updated.
### Changed
* The packaging output is now cleaner: With the standard `--pack` option, the final EXE file is located in the `output/<project>/dist/` directory; temporary PyInstaller build and specification files are no longer left in the project folder.
* The output log no longer displays the entire PyInstaller command line (only brief status information is provided).
* Some runtime security improvements and packaging optimizations have been made.

---

## V1.4 - 2026-07-12

### Added
* Stronger native runtime protection for protected packages.
* `build_library.bat` helper to rebuild the shipped native runtime library.

### Changed
* Improved compatibility with heavy GUI apps and optional third-party native protectors.
* Protector GUI clock in the title bar now updates live.

### Fixed
* Fixed crashes in some multi-threaded / GUI protected apps.
* Fixed protect-time breakage for functions called with keyword arguments.
* Reduced false security stops under heavy UI load.
  
---

## v1.3.5 - 2026-06-05

### Added
* Graphical User Interface (GUI) added.

### Changed
* Removed random `.pyd` filename generation in protected output packages.
* Updated internal APIs to match the new output layout and naming.

### Fixed
* Fixed several GUI layout and usability issues in the Protector desktop app.

---

## v1.3 - 2026-06-29

### Added

* English language support.

### Changed

* Improved startup reliability.
* Enhanced error handling and user feedback.
* Removed build cache; all builds are now generated from a clean state.
* General stability, performance, and usability improvements.

### Fixed

* Resolved `.pyd` file locking issues during compilation.
* Fixed a rare startup-related issue.
* Addressed various minor bugs.

---

## v1.2 - 2026-06-25

### Added

* Optional string encryption with runtime decryption.
* Additional configuration options.

### Changed

* Strengthened the protection layer.
* Improved resistance against static analysis.
* Enhanced output cleanliness and overall usability.
* Expanded configuration flexibility.

### Security

* Removed unnecessary and potentially unsafe exports from release builds.
* Disabled the offline decryption path.

---

## v1.1 - 2026-06-24

### Changed

* Simplified the distribution structure.
* Refactored the overall protection architecture.
* Consolidated distribution output into a single package.
* Reduced the exposed surface area.
* Improved compatibility and stability.

---

## v1.0 - 2026-06-23

### Changed

* Strengthened protection layers.
* Improved runtime resilience.
* Enhanced integrity validation between protection components.
* General stability improvements.

### Release

* First stable release.

---

## v0.9 - 2026-06-14

### Changed

* Enhanced integrity verification mechanisms.
* Expanded multi-layer validation.
* Improved runtime monitoring resilience.
* General stability improvements.

---

## v0.8 - 2026-06-13

### Changed

* Reworked the runtime architecture.
* Improved startup flow and execution efficiency.
* Optimized memory usage.
* Increased overall reliability and stability.

---

## v0.7 - 2026-06-12

### Changed

* Strengthened protection mechanisms.
* Improved runtime resilience.
* Increased tamper resistance.
* Enhanced fault tolerance.
* General improvements and refinements.

---

## v0.6 - 2026-06-11

### Added

* Support for Python 3.12, 3.13, and 3.14.

### Changed

* Improved compatibility across supported Python versions.
* Increased overall stability.

### Fixed

* Resolved known loading issues.
* Improved version transition handling.

---

## v0.5 - 2026-06-08

### Added

* Initial protection infrastructure.
* Core runtime loader.
* Initial configuration and workflow system.

### Release

* First public release.
