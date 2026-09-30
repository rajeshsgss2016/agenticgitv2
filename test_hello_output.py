import subprocess

def test_hello_output():
    result = subprocess.run([
        "python", "src/hello.py"
    ], capture_output=True, text=True)
    assert result.stdout.strip() == "test"
