import PyPDF2
import os

# Specify the directory path to scan for PDF files
directory_path = "D:\\job portfolio"

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Iterate through files in the specified directory
for file in os.listdir(directory_path):
    # Check if the file is a PDF
    if file.endswith(".pdf"):
        # Append the PDF file to the merger
        file_path = os.path.join(directory_path, file)
        merger.append(file_path)

# Write the merged PDF to a file named "combined.pdf"
merger.write("D:\\job portfolio/combined.pdf")
merger.close()  # Make sure to close the merger after writing
