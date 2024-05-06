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
        output, errors = process.communicate()
        if process.returncode == 0:
            return output
        else:
            err_msg = f"Runtime error: {errors}"
            err_msg += traceback.format_exc()
            return err_msg
    except Exception as e: # error
        return str(e)
    
def run(script):
    output = run_python(script)
    print(output)

