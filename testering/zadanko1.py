raw_text=" PATIENT_age_YEARS "
text2 = "  ASDLAS _asdasd_  asdaSasdaASD "

def text_converter(text):
    new_text_1 = text.strip()
    new_text_2 = new_text_1.lower()
    new_text_3 = new_text_2.replace("_"," ")
    new_text_4 = new_text_3.title()

    new_text_5 = text.strip().lower().replace("_"," ").title()
    print(new_text_5)
text_converter(raw_text)
text_converter(text2)