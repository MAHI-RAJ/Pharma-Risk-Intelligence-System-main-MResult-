import fitz


def extract_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    print(f"\nProcessing PDF: {pdf_path}")

    for page_num, page in enumerate(doc):

        page_text = page.get_text("text")

        if page_text and page_text.strip():

            text += page_text + "\n"

        else:

            print(
                f"No text found on page {page_num + 1}"
            )

    doc.close()

    print("\nText extraction completed!")

    return text