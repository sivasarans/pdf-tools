from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import PyPDF2
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    try:
        # Create a PdfMerger object
        merger = PyPDF2.PdfMerger()

        # Get the selected PDF files from the first input
        pdf_files_1 = request.files.getlist('pdf_files')

        # Get the selected PDF file from the second input
        pdf_file_2 = request.files['pdf_files_2']

        # Check if at least two PDF files are selected
        if len(pdf_files_1) < 1 or pdf_file_2 is None:
            raise ValueError("Please select at least two PDF files for merging.")

        # Iterate through selected PDF files from the first input
        for file in pdf_files_1:
            # Check if the file is a PDF
            if file.filename.endswith(".pdf"):
                # Append the PDF file to the merger
                merger.append(file)

        # Check if the file from the second input is a PDF
        if pdf_file_2.filename.endswith(".pdf"):
            # Append the PDF file from the second input to the merger
            merger.append(pdf_file_2)

        # Create an in-memory file-like object to store the merged PDF
        output_pdf = io.BytesIO()

        # Write the merged PDF to the in-memory file
        merger.write(output_pdf)
        merger.close()

        # Seek to the beginning of the in-memory file
        output_pdf.seek(0)

        # Return the in-memory file for download with a specified filename
        return send_file(output_pdf, as_attachment=True, download_name='combined.pdf')
    except Exception as e:
        # Render the error template with the error message
        return render_template('error.html', error_message=str(e))

@app.route('/success/<filename>')
def success(filename):
    # Display a success message with a link to go back to the index page
    return f'Merged PDF successfully! <a href="{url_for("index")}">Go back</a>'

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
