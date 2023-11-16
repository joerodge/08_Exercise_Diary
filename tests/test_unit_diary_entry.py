from lib.diary_entry import *

# Test __init__
def test_diary_entry_init():
    entry = DiaryEntry('Day1', 'Went for a walk')
    assert entry._title == 'Day1'
    assert entry._contents == 'Went for a walk'

