from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        domain = request.form.get('domain')
        try:
            # Run the nmap command
            result = subprocess.run(f"nmap {domain}", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                output = result.stdout  # Capture standard output
            else:
                output = f"Error: {result.stderr}"  # Capture error output
        except Exception as e:
            output = f"An error occurred: {e}"
    
    return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
