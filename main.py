import pyttsx3
import PyPDF2

reader = pyttsx3.init()  # object creation
""" RATE"""
rate = reader.getProperty('rate')  # getting details of current speaking rate
print("Current voice rate" + str(rate))  # printing current voice rate
reader.setProperty('rate', 125)  # setting up new voice rate

"""VOLUME"""
volume = reader.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print("Starting volume level : " + str(volume))  # printing current volume level
reader.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
print("Setting volume level to 100%.")  # printing current volume level

"""VOICE"""
voices = reader.getProperty('voices')  # getting details of current voice
reader.setProperty('voice', voices[1].id)  # changing voices index. 0 for male and 1 for female


def read(text):
    reader.say(text)
    reader.runAndWait()
    reader.stop()
    return text


file = open('resources/Designing Data Intensive Applications.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(file)
print("Total Number of pages: " + str(pdfReader.numPages))
pageNo = 115


def get_page(number):
    page = pdfReader.getPage(number)
    # Extracting text from page
    # And splitting it into chunks of lines
    text = page.extractText()

    # Iterate through each line and store into lines
    lines = []
    for line in text:
        # Loop through each character of the line and add gap when , and . is present.
        # Also ignore if there ae any special character.
        for char in line:
            if char == '.':
                lines.append(".\n\n")
            elif char == ',':
                lines.append(",\n")
            elif char != '-':
                lines.append(char)
    return ''.join(lines)


def start_reading_file():
    print(read("Starting the Reader"))
    for cur_page_no in range(pageNo - 1, pdfReader.numPages):
        # Creating a page object
        cur_page_lines = get_page(cur_page_no)
        print(read(cur_page_lines))


# read("This is a test message.")
start_reading_file()
# get_page(111)
# get_page(112)
