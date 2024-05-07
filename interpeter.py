import subprocess
import traceback

def run_python(code):
    try:
        process = subprocess.Popen(
            ["python", "-c", code],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            output, errors = process.communicate(timeout=15) #15 seconds 
            if process.returncode == 0:
                return output
            else:
                err_msg = f"{errors}"
                err_msg += traceback.format_exc()
                return err_msg
        except subprocess.TimeoutExpired:
            process.kill()
            return "Interpeter timed out."
    except Exception as e:
        return str(e)

def run(script):
    output = run_python(script)
    print(output)
