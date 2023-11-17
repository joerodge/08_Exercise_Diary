from lib.diary_entry import DiaryEntry
import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        if type(entry) == DiaryEntry:
            self._entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._entries

    def count_all_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum(entry.count_words() for entry in self._entries)
    

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")
        
        return math.ceil(self.count_all_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        no_of_words = wpm * minutes
        closest_count = 0
        best_entry = None
        for entry in self._entries:
            if no_of_words > entry.count_words() > closest_count:
                best_entry = entry
                closest_count = entry.count_words()

        return best_entry

