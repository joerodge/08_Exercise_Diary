import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self._title = title
        self._contents = contents
        self._words = contents.split()
        self._word_count = len(self._words)
        self._index = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self._contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")
        
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        chunk_size = wpm * minutes
        text_chunk = ' '.join(self._words[self._index:self._index + chunk_size])
        self._index += chunk_size
        
        # Loop round to start reading from the start again if all text read
        if self._index >= self._word_count:
            self._index = 0
            
        return text_chunk
