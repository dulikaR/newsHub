def run_quickstart():
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\NewsApp-723820770a3c.json'

    # GOOGLE_APPLICATION_CREDENTIALS = 'C:\NewsApp-723820770a3c.json'

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'si'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]


if __name__ == '__main__':
    run_quickstart()