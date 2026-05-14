"""
Starter placeholder for SU2 Aerodynamic Shape Optimisation.

Replace this with real case generation, solver execution wrappers or post-processing.
"""

from pathlib import Path
import json

PROJECT = "SU2 Aerodynamic Shape Optimisation"
TOOL = "SU2"

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
