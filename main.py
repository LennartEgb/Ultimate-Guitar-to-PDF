from src.util import convert_to_pdf, extract_tabs, fetch_html, get_full_url

if __name__ == "__main__":
    tab_identifier = input("Enter the complete URL or the part after /tab/: ")
    output_dir = input("Enter output directory: ")
    filename = input("Enter filename: ")

    tab_url = get_full_url(tab_identifier)
    webpage = fetch_html(tab_url)
    text = extract_tabs(webpage)
    filename = filename if filename != "" else tab_identifier.split("/")[-1]

    convert_to_pdf(filename, output_dir, text)
