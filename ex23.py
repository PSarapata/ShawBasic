import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<==>", cooked_string)


languages = open("pyt3pw/languages.txt", encoding="utf-8")

main(languages, encoding, error)

#  e.g. "python ex23.py utf-8 strict"
#  "python ex23.py idna strict"
#  "python ex23.py punycode ignore"
#  "python ex23.py unicode_escape ignore"
#  "python ex23.py big5 replace"
#  kodowanie stringów w tych systemach to kodeki. (codecs)

"""
Kodowanie to ustalony standard, określający w jaki sposób sekwencja bitów powinna
reprezentować liczbę.

Najpopularniejszy we wczesnej fazie rozwoju informatyki był standard ASCII:
American Standard Code for Information Interchange. Mapuje liczby na litery.
Greatest limitation of ASCII is that it serves only English and few other alike languages.

To answer that a group of scientists developped UNICODE standard - universal encoding for all languages.
It is similar to ASCII, but much more complex. You can use 32 bytes to encode a Unicode sign. That is 4 294 967 295 (2^32).
Additional space is now being used to encode emoticons and icons.

Najpopularniejszy jest więc UTF-8, Unicode Transformation Format - 8bit, czyli kodowanie z kompresją.
"""

"""
Python has a special convention called DBES:
Decode Bytes, Encode Strings
"""