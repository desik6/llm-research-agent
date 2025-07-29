from langchain.document_loaders import PyPDFLoader

def get_pdf_reader_tool():

    def read_pdf(file_path):

        loader = PyPDFLoader(file_path)

        pages = loader.load()

        return pages[0].page_content if pages else "PDF is empty."

    return {

        "name": "PDF Reader",

        "func": read_pdf,

        "description": "Reads content from the first page of a PDF file."

    }
 