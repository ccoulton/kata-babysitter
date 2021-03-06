# Babysitter Kata

## Background
This kata simulates a babysitter working and getting paid for one night.  The rules are pretty straight forward.

## Feature
*As a babysitter<br>
In order to get paid for 1 night of work<br>
I want to calculate my nightly charge<br>*

## Requirements
The babysitter:
- starts no earlier than 5:00PM *done*
- leaves no later than 4:00AM *done*
- only babysits for one family per night *done-ish* (doesn't check for the date.)
- gets paid for full hours (no fractional hours) *done?* (disallows fractional hours currently)
- should be prevented from mistakes when entering times (e.g. end time before start time, or outside of allowable work hours) *done*

The job:
- Pays different rates for each family (based on bedtimes, kids and pets, etc...) *done*
- Family A pays $15 per hour before 11pm, and $20 per hour the rest of the night *done*
- Family B pays $12 per hour before 10pm, $8 between 10 and 12, and $16 the rest of the night *done*
- Family C pays $21 per hour before 9pm, then $15 the rest of the night *done*
- The time ranges are the same as the babysitter (5pm through 4am) *done*

Deliverable:
- Calculate total pay, based on babysitter start and end time, and a family. *done*

Directions:

To run unit tests run python /files/test/tests.py from the root directory,
-v is for a more verbose version of the output.

To use application run python /files/src/babysittertime.py from root directory.
