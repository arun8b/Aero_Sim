"""
Starter placeholder for FiPy Thermal Diffusion Mini Solver.

Replace this with real case generation, solver execution wrappers or post-processing.
"""

from pathlib import Path
import json

PROJECT = "FiPy Thermal Diffusion Mini Solver"
TOOL = "FiPy"

def main() -> None:
    out = Path("results")
    out.mkdir(exist_ok=True)
    metadata = {
        "project": PROJECT,
        "tool": TOOL,
        "status": "starter scaffold",
        "next_step": "replace placeholder with real simulation/post-processing workflow",
    }
    (out / "metadata.json").write_text(json.dumps(metadata, indent=2))
    print(f"Created starter metadata for {PROJECT}")

if __name__ == "__main__":
    main()
