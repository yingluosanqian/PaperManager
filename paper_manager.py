from pathlib import Path
import PyPDF2
from datetime import datetime


def get_pdf_title(path):
    with path.open('rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        metadata = reader.metadata
        if metadata and '/Title' in metadata:
            return metadata['/Title']
        else:
            return None


def get_file_list(current_path=Path('.')):
    file_list = []
    for path in Path('.').rglob('*'):
        if path.is_file() and path.suffix == ".pdf":
            file_list.append(path)
    return file_list


def gen_markdown(file_list, result_file_name=Path('PaperList.md')):
    with Path(result_file_name).open(mode='w', encoding='utf-8') as result_file:
        result_file.write(f'# Paper List\n\n')
        result_file.write(f'The number of pdf file is **{len(file_list)}**.\n\n')
        result_file.write(f'Last updating time is `{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}`.\n\n')
        result_file.write(f'## Papers\n\n')
        for idx, file in enumerate(file_list):
            # title
            title = get_pdf_title(file)
            if title is not None:
                result_file.write(f'**Title**: `{title}`\n\n')
            else:
                result_file.write(f'**Title**: {file.name}\n\n')
            result_file.write(f'filepath: {file}\n\n')
            result_file.write(f'---\n\n')


def main():
    file_list = get_file_list()
    gen_markdown(file_list)


if __name__ == '__main__':
    main()
