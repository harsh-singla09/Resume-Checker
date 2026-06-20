import re


def clean_text(text):

    # Convert all text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        text
    )

    # Remove extra spaces
    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()




if __name__ == "__main__":

    sample = """
    Python Developer!!!
    Skills: Python, Flask, SQL.
    """

    result = clean_text(sample)

    print(result)