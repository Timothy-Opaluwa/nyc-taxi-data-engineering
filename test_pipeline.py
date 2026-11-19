
import subprocess
import sys

print("TESTING PIPELINE ORCHESTRATION", flush=True)

steps = [
    ["-c", "print('Step 1: Extract - PASS')"],
    ["-c", "print('Step 2: Transform - PASS')"],
    ["-c", "import sys; print('Step 3: Upload - FAILED'); sys.exit(1)"],
    ["-c", "print('Step 4: Load - PASS')"],
    ["-c", "print('Step 5: Quality Check - PASS')"],
]

for step in steps:
    result = subprocess.run(
        [sys.executable, *step],
        check=False
    )

    if result.returncode != 0:
        print("PIPELINE TEST FAILED")
        sys.exit(result.returncode)

print("\nPIPELINE ORCHESTRATION TEST PASSED!")
