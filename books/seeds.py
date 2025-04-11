import time
import sys

from django.core.management.base import OutputWrapper

from books.serializers import BookSerializer
from books.services import get_book_data_by_isbn, parse_book_data

stdout = OutputWrapper(sys.stdout)
stderr = OutputWrapper(sys.stderr)


OPEN_LIBRARY_BOOK_LOCAL_DATA = {
    "ISBN:1931498717": {
        "bib_key": "ISBN:1931498717",
        "info_url": "https://openlibrary.org/books/OL34424821M/Don't_Think_of_an_Elephant!",
        "preview": "borrow",
        "preview_url": "https://archive.org/details/dontthinkofeleph0000lako",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/12039210-S.jpg",
        "details": {
            "works": [{"key": "/works/OL1952998W"}],
            "title": "Don't Think of an Elephant!",
            "publishers": [
                "Chelsea Green Publishing Company",
                "Chelsea Green Pub. Co."
            ],
            "publish_date": "2004-09",
            "key": "/books/OL34424821M",
            "type": {"key": "/type/edition"},
            "identifiers": {},
            "isbn_10": ["1931498717"],
            "ocaid": "dontthinkofeleph0000lako",
            "classifications": {},
            "languages": [{"key": "/languages/eng"}],
            "covers": [12039210],
            "local_id": ["urn:nuls:31786101954094"],
            "lccn": ["2004018919"],
            "lc_classifications": ["JA85.2.U6 L35 2004"],
            "oclc_numbers": ["56324576"],
            "source_records": [
                "marc:marc_nuls/NULS_PHC_180925.mrc:337740246:1483",
                "idb:9781931498715",
                "marc:marc_columbia/Columbia-extract-20221130-010.mrc:444843893:2886",
                "marc:harvard_bibliographic_metadata/ab.bib.09.20150123.full.mrc:514845593:2002"
            ],
            "number_of_pages": 124,
            "description": {
                "type": "/type/text",
                "value": (
                    "Don't Think of an Elephant! is the antidote to the last forty years of conservative strategizing "
                    "and the right wing's stranglehold on political dialogue in the United States. "
                    "Author George Lakoff explains how conservatives think, and how to counter their arguments. He outlines in detail "
                    "the traditional American values that progressives hold, but are often unable to articulate. "
                    "Lakoff also breaks down the ways conservatives have framed the issues, and provides examples of how "
                    "progressives can reframe the debate. "
                    "Lakoff's years of research and work with environmental and political leaders have been distilled into this essential guide, "
                    "which shows progressives how to think in terms of values instead of programs, and why people vote their values and identities, "
                    "often against their best interests.--BOOK JACKET."
                ),
            },
            "latest_revision": 7,
            "revision": 7,
            "created": {
                "type": "/type/datetime",
                "value": "2021-10-04T13:27:53.906255"
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2024-12-19T07:43:28.862766"
            }
        }
    },
    "ISBN:978-0132931755": {
        "bib_key": "ISBN:978-0132931755",
        "info_url": "https://openlibrary.org/books/OL34017486M/Working_Effectively_with_Legacy_Code",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL34017486M/Working_Effectively_with_Legacy_Code",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/14430328-S.jpg",
        "details": {
            "type": {"key": "/type/edition"},
            "authors": [
                {"key": "/authors/OL1396390A", "name": "Michael C. Feathers"}
            ],
            "languages": [{"key": "/languages/eng"}],
            "number_of_pages": 456,
            "publish_date": "2004",
            "publishers": ["Pearson Education Canada"],
            "source_records": ["bwb:9780132931755"],
            "title": "Working Effectively with Legacy Code",
            "full_title": "Working Effectively with Legacy Code",
            "works": [{"key": "/works/OL25381590W"}],
            "key": "/books/OL34017486M",
            "covers": [14430328],
            "identifiers": {},
            "isbn_13": ["9780132931755"],
            "classifications": {},
            "latest_revision": 4,
            "revision": 4,
            "created": {
                "type": "/type/datetime",
                "value": "2021-09-29T15:17:38.359000",
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2023-10-01T00:59:21.887421",
            },
        },
    },
    "ISBN:978-0132542883": {
        "bib_key": "ISBN:978-0132542883",
        "info_url": "https://openlibrary.org/books/OL35566351M/Clean_Coder",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL35566351M/Clean_Coder",
        "details": {
            "type": {"key": "/type/edition"},
            "authors": [
                {
                    "key": "/authors/OL318513A",
                    "name": "Robert Martin - undifferentiated"
                }
            ],
            "languages": [{"key": "/languages/eng"}],
            "publishers": ["Pearson Education, Limited"],
            "source_records": ["bwb:9780132542883"],
            "title": "Clean Coder",
            "weight": "0.001 ",
            "subtitle": "A Code of Conduct for Professional Programmers",
            "full_title": "Clean Coder A Code of Conduct for Professional Programmers",
            "works": [{"key": "/works/OL16298147W"}],
            "key": "/books/OL35566351M",
            "identifiers": {},
            "isbn_13": ["9780132542883"],
            "classifications": {},
            "latest_revision": 3,
            "revision": 3,
            "created": {
                "type": "/type/datetime",
                "value": "2021-11-03T06:10:01.070322",
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2023-12-17T02:50:05.726036",
            },
        },
    },
    "ISBN:978-8535914849": {
        "bib_key": "ISBN:978-8535914849",
        "info_url": "https://openlibrary.org/books/OL26449397M/1984",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL26449397M/1984",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/8172473-S.jpg",
        "details": {
            "identifiers": {
                "wikidata": ["Q111263683"]
            },
            "title": "1984",
            "publish_date": "2009",
            "other_titles": [
                "Mil novecentos e oitenta e quatro",
                "Nineteen Eighty-Four"
            ],
            "publishers": ["Companhia das Letras"],
            "contributors": [
                {"role": "Translator", "name": "Alexandre Hubner"},
                {"role": "Translator", "name": "Heloísa Jahn"},
                {"role": "Posfácio", "name": "Erich Fromm"},
                {"role": "Posfácio", "name": "Ben Pimlott"},
                {"role": "Posfácio", "name": "Thomas Pynchon"},
            ],
            "covers": [8172473],
            "physical_format": "Paperback",
            "publish_places": ["São Paulo, SP, Brasil"],
            "edition_name": "1ª ed.",
            "pagination": "414p.",
            "classifications": {
                "udc": ["821.111(410)-31\"19\""]
            },
            "dewey_decimal_class": ["823"],
            "translation_of": "1984",
            "isbn_13": ["9788535914849"],
            "languages": [{"key": "/languages/por"}],
            "copyright_date": "2003",
            "type": {"key": "/type/edition"},
            "physical_dimensions": "21 x  x  centimeters",
            "key": "/books/OL26449397M",
            "number_of_pages": 416,
            "works": [{"key": "/works/OL1168083W"}],
            "latest_revision": 5,
            "revision": 5,
            "created": {
                "type": "/type/datetime",
                "value": "2018-05-14T02:43:12.244183",
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2022-03-30T22:28:30.830496",
            },
        },
    },
    "ISBN:978-1593278267": {
        "bib_key": "ISBN:978-1593278267",
        "info_url": "https://openlibrary.org/books/OL26487288M/Serious_Cryptography",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL26487288M/Serious_Cryptography",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/8232506-S.jpg",
        "details": {
            "publishers": ["No Starch Press"],
            "subtitle": "A Practical Introduction to Modern Encryption",
            "source_records": [
                "amazon:1593278268",
                "marc:marc_openlibraries_sanfranciscopubliclibrary/sfpl_chq_2018_12_24_run06.mrc:44608328:2467",
                "bwb:9781593278267",
                "idb:9781593278267"
            ],
            "title": "Serious Cryptography",
            "covers": [8232506],
            "local_id": [
                "urn:sfpl:31223123473598",
                "urn:sfpl:31223123473606"
            ],
            "isbn_13": ["9781593278267"],
            "lc_classifications": ["QA76.9.D335A9 2018"],
            "publish_date": "November 2017",
            "key": "/books/OL26487288M",
            "works": [
                {"key": "/works/OL17912167W"}
            ],
            "type": {"key": "/type/edition"},
            "number_of_pages": 312,
            "latest_revision": 9,
            "revision": 9,
            "created": {
                "type": "/type/datetime",
                "value": "2018-08-27T10:38:12.778087"
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2023-12-20T03:06:22.925232"
            }
        }
    },
    "ISBN:978-0143130727": {
        "bib_key": "ISBN:978-0143130727",
        "info_url": "https://openlibrary.org/books/OL26927371M/Ikigai",
        "preview": "restricted",
        "preview_url": "https://archive.org/details/ikigaijapanesese0000garc",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/14856644-S.jpg",
        "details": {
            "other_titles": ["Japanese secret to a long and happy life"],
            "subtitle": "The Japanese Secret to a Long and Happy Life",
            "description": "Bring meaning and joy to all your days with this internationally bestselling guide to the Japanese concept of ikigai -- the happiness of always being busy -- as revealed by the daily habits of the world's longest-living people. -- From Amazon.com summary.",
            "full_title": "Ikigai the Japanese secret to a long and happy life",
            "key": "/books/OL26927371M",
            "authors": [
                {"key": "/authors/OL7082274A", "name": "Héctor García"}
            ],
            "contributions": [
                "Miralles, Francesc, 1968- author",
                "Cleary, Heather, translator"
            ],
            "subjects": [
                "Longevity",
                "Happiness",
                "Quality of life"
            ],
            "pagination": "194 pages",
            "source_records": [
                "marc:marc_openlibraries_sanfranciscopubliclibrary/sfpl_chq_2018_12_24_run06.mrc:17328477:3730",
                "bwb:9780143130727",
                "promise:bwb_daily_pallets_2022-08-26",
                "ia:ikigaijapanesese0000garc"
            ],
            "title": "Ikigai",
            "work_titles": ["Ikigai"],
            "notes": "\"Originally published in Spanish as Ikigai: Los secretos de Japón para una vida larga y feliz by Ediciones Urano, Barcelona.\"\n\nIncludes bibliographical references.",
            "number_of_pages": 194,
            "languages": [{"key": "/languages/eng"}],
            "subject_places": ["Japan"],
            "local_id": [
                "urn:sfpl:31223118439455",
                "urn:sfpl:31223118438564",
                "urn:sfpl:31223118439448",
                "urn:sfpl:31223118439471",
                "urn:sfpl:31223118439497",
                "urn:sfpl:31223118439489",
                "urn:sfpl:31223118439463",
                "urn:bwbsku:W7-CQF-865"
            ],
            "publish_date": "2017",
            "publish_country": "nyu",
            "by_statement": "Héctor García and Francesc Miralles ; translated by Heather Cleary",
            "works": [{"key": "/works/OL19714233W"}],
            "type": {"key": "/type/edition"},
            "identifiers": {},
            "classifications": {},
            "covers": [
                14856644, 14849168, 14837349, 14832603, 14831840, 14827511,
                14820457, 14655669, 14655668, 14649976, 11300391
            ],
            "isbn_10": ["0143130722"],
            "isbn_13": ["9780143130727"],
            "lccn": ["2017005811"],
            "oclc_numbers": ["986523570"],
            "dewey_decimal_class": ["613"],
            "lc_classifications": [
                "RA776.75 .G3713 2017",
                "RA776.75.G3713 2017"
            ],
            "edition_name": "Illustrated Edition",
            "publishers": ["Penguin Life"],
            "ocaid": "ikigaijapanesese0000garc",
            "latest_revision": 21,
            "revision": 21,
            "created": {
                "type": "/type/datetime",
                "value": "2019-05-23T21:56:29.055272"
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2025-04-03T11:56:54.929482"
            }
        }
    },
    "ISBN:9781538742570": {
        "bib_key": "ISBN:9781538742570",
        "info_url": "https://openlibrary.org/books/OL49368011M/The_Housemaid",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL49368011M/The_Housemaid",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/14653835-S.jpg",
        "details": {
            "works": [{"key": "/works/OL27729743W"}],
            "title": "The Housemaid",
            "publishers": ["Hatchette UK - Bookouture"],
            "publish_date": "April 26 2022",
            "key": "/books/OL49368011M",
            "type": {"key": "/type/edition"},
            "identifiers": {"amazon": ["B09XRF2SWN"]},
            "isbn_10": ["1538742578"],
            "classifications": {},
            "physical_dimensions": "7.95 x .85 x 5.2 inches",
            "weight": "11 ounces",
            "copyright_date": "April 26, 2022",
            "physical_format": "Both paperback and audible audio",
            "number_of_pages": 336,
            "first_sentence": {
                "type": "/type/text",
                "value": "If I leave this house, it will be in handcuffs.",
            },
            "publish_places": ["Grand Central Publishing"],
            "pagination": "336",
            "series": ["Housemaid Series"],
            "covers": [14653835],
            "latest_revision": 4,
            "revision": 4,
            "created": {
                "type": "/type/datetime",
                "value": "2023-09-09T02:13:17.299886",
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2025-01-20T02:00:31.047673",
            },
        },
    },
    "ISBN:9780735211292": {
        "bib_key": "ISBN:9780735211292",
        "info_url": "https://openlibrary.org/books/OL32336498M/Atomic_Habits",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL32336498M/Atomic_Habits",
        "thumbnail_url": "https://covers.openlibrary.org/b/id/12886417-S.jpg",
        "details": {
            "works": [{"key": "/works/OL17930368W"}],
            "title": "Atomic Habits",
            "publishers": ["Avery, an Imprint of Penguin Random House LLC"],
            "publish_date": "2018",
            "key": "/books/OL32336498M",
            "type": {"key": "/type/edition"},
            "identifiers": {
                "learnawesome": ["bc60faf0-a9b8-45f8-8ddb-d9179e6d3dd4"],
                "amazon": ["B09YTXNR2H"],
                "wikidata": ["Q98178602"],
                "goodreads": ["62221762"],
            },
            "classifications": {},
            "languages": [{"key": "/languages/eng"}],
            "covers": [12886417, -1],
            "physical_dimensions": "9 x 6 x  inches",
            "publish_places": ["New York"],
            "subtitle": "Tiny Changes, Remarkable Results : An Easy & Proven Way to Build Good Habits & Break Bad Ones",
            "description": {
                "type": "/type/text",
                "value": "Learn how to make time for new habits (even when life gets crazy); overcome a lack of motivation and willpower; design your environment to make success easier; get back on track when you fall off course; ...and much more. Atomic Habits will reshape the way you think about progress and success, and give you the tools and strategies you need to transform your habits--whether you are a team looking to win a championship, an organization hoping to redefine an industry, or simply an individual who wishes to quit smoking, lose weight, reduce stress, or achieve any other goal.",
            },
            "physical_format": "Hardcover",
            "number_of_pages": 320,
            "copyright_date": "2018",
            "isbn_10": ["0735211299"],
            "isbn_13": ["9780735211292"],
            "oclc_numbers": ["11165649274"],
            "dewey_decimal_class": ["155.24"],
            "lc_classifications": ["BF335"],
            "source_records": ["idb:9780735211292"],
            "latest_revision": 72,
            "revision": 72,
            "created": {
                "type": "/type/datetime",
                "value": "2021-05-07T07:10:49.427087",
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2023-12-19T23:35:08.329132",
            },
        },
    },
    "ISBN:9781649377371": {
        "bib_key": "ISBN:9781649377371",
        "info_url": "https://openlibrary.org/books/OL53388405M/Untitled",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL53388405M/Untitled",
        "details": {
            "type": {
                "key": "/type/edition"
            },
            "authors": [
                {
                    "key": "/authors/OL2625980A",
                    "name": "TBD"
                }
            ],
            "isbn_13": ["9781649377371"],
            "languages": [
                {
                    "key": "/languages/eng"
                }
            ],
            "publish_date": "2024",
            "publishers": ["Entangled Publishing, LLC"],
            "source_records": ["bwb:9781649377371"],
            "title": "Untitled",
            "weight": "0.700",
            "full_title": "Untitled",
            "works": [
                {
                    "key": "/works/OL39213216W"
                }
            ],
            "key": "/books/OL53388405M",
            "latest_revision": 1,
            "revision": 1,
            "created": {
                "type": "/type/datetime",
                "value": "2024-08-18T04:47:24.418860"
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2024-08-18T04:47:24.418860"
            }
        }
    },
    "ISBN:9781070527710": {
        "bib_key": "ISBN:9781070527710",
        "info_url": "https://openlibrary.org/books/OL37456817M/Dad_I_Want_to_Hear_Your_Story",
        "preview": "noview",
        "preview_url": "https://openlibrary.org/books/OL37456817M/Dad_I_Want_to_Hear_Your_Story",
        "details": {
            "type": {
                "key": "/type/edition"
            },
            "authors": [
                {
                    "key": "/authors/OL7963517A",
                    "name": "Jeffrey Mason"
                }
            ],
            "isbn_13": ["9781070527710"],
            "languages": [
                {
                    "key": "/languages/eng"
                }
            ],
            "pagination": "104",
            "publish_date": "2019",
            "publishers": ["Independently Published"],
            "source_records": [
                "bwb:9781070527710",
                "promise:bwb_daily_pallets_2023-12-08:P9-BPP-581"
            ],
            "title": "Dad, I Want to Hear Your Story",
            "weight": "0.209",
            "subtitle": "A Father's Guided Journal to Share His Life and His Love",
            "full_title": "Dad, I Want to Hear Your Story A Father's Guided Journal to Share His Life and His Love",
            "works": [
                {
                    "key": "/works/OL26911723W"
                }
            ],
            "key": "/books/OL37456817M",
            "local_id": ["urn:bwbsku:P9-BPP-581"],
            "latest_revision": 2,
            "revision": 2,
            "created": {
                "type": "/type/datetime",
                "value": "2022-03-01T23:01:55.729115"
            },
            "last_modified": {
                "type": "/type/datetime",
                "value": "2023-12-10T01:06:22.784418"
            }
        }
    }
}


ISBNs = [
    "9780060934347",  # Don Quixote
    "9780141439600",  # A Tale of Two Cities
    "9780544003415",  # The Lord of the Rings
    "9780156012195",  # The Little Prince
    "9780747532699",  # Harry Potter and the Philosopher’s Stone
    "9780062073488",  # And Then There Were None
    "9780140442939",  # Dream of the Red Chamber
    "9780547928227",  # The Hobbit
    "9780140437638",  # She: A History of Adventure
    "9780064471046",  # The Lion, the Witch and the Wardrobe
    "9780307474278",  # The Da Vinci Code
    "9780439064873",  # Harry Potter and the Chamber of Secrets
    "9780316769488",  # The Catcher in the Rye
    "9780061122415",  # The Alchemist
    "9780446516525",  # The Bridges of Madison County
    "9780060883287",  # One Hundred Years of Solitude
    "9780679723165",  # Lolita
    "9780141322568",  # Heidi
    "9780671734206",  # The Common Sense Book of Baby and Child Care
    "9780553213133",  # Anne of Green Gables
    "9780141321035",  # Black Beauty
    "9780156001311",  # The Name of the Rose
    "9780425177181",  # The Eagle Has Landed
    "9780743277709",  # Watership Down
    "9780440153849",  # The Hite Report
    "9780064400558",  # Charlotte's Web
    "9780802144669",  # The Ginger Man
    "9780310337508",  # The Purpose Driven Life
    "9780385504225",  # The Lost Symbol
    "9780439023481",  # The Hunger Games
    "9780140374247",  # James and the Giant Peach
    "9780399144462",  # Who Moved My Cheese?
    "9780553380163",  # A Brief History of Time
    "9782010008526",  # Paul et Virginie
    "9780452262492",  # Lust for Life
    "9780143039099",  # The Wind in the Willows
    "9780743269513",  # The 7 Habits of Highly Effective People
    "9784770020676",  # Totto-Chan: The Little Girl at the Window
    "9780446671002",  # The Celestine Prophecy
    "9780140120837",  # Perfume
    "9780143039433",  # The Grapes of Wrath
    "9780143034902",  # The Shadow of the Wind
    "9780395927205",  # Interpreter of Maladies
]


def seeds_online_data():
    for isbn in ISBNs:
        try:
            stdout.write(f'ISBN {isbn}: Requesting book details')
            book_data = get_book_data_by_isbn(isbn=isbn)
            book_serializer = BookSerializer(data=book_data)
            if not book_serializer.is_valid():
                stdout.write(f'ISBN {isbn}: Was not saved')
                continue

            stdout.write(f'ISBN {isbn}: Saving book')
            book_serializer.save()
            stdout.write(f'ISBN {isbn}: Was saved')
        except Exception as e:
            stderr.write(f'ISBN {isbn}: An error {str(e)} occurred when seeding book')
            continue
        time.sleep(2)


def seeds_local_data():
    for isbn, book in OPEN_LIBRARY_BOOK_LOCAL_DATA.items():
        stdout.write(f'ISBN {isbn}: Start parsing book data')
        try:
            stdout.write(f'ISBN {isbn}: Getting book details')
            book_data = book['details']
            book_serializer = BookSerializer(
                data=parse_book_data(isbn=isbn.split(':')[1], book_data=book_data)
            )
            if not book_serializer.is_valid():
                stdout.write(f'ISBN {isbn}: Was not saved')
                continue

            stdout.write(f'ISBN {isbn}: Saving book')
            book_serializer.save()
            stdout.write(f'ISBN {isbn}: Was saved')
        except Exception as e:
            stderr.write(f'ISBN {isbn}: An error {str(e)} occurred when seeding book')
            continue
