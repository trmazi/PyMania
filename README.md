# PyMania
 A simple python rhythm game test

# Formats
Here's some important documentation about how I intend on doing things.

## Game Data
Game data is stored as JSON
Here's the test V1 structure.

### Song Library
One `songs.json` for entire game.
```json
    [
        {
            "songId": "example ID",
            "title": "example title",
            "artist": "example artist",
            "genre": "example genre",
            "bpm": 120.0,
            "sourceGame": 1,
            "sourceVersion": 1,
            "revised": false,
            "secureOnly": false,
        }
    ]
```
* `songId`: Song's unique ID. Stored as string. Used for pulling files, score data, server data, and more. VERY important.
* `title`: Song's title, as string.
* `artist`: Song's artist, as string.
* `genre`: Song's genre, as string.
* `bpm`: BPM of song, as float.
* `sourceGame`: Game from which the song originated, as int.
* `sourceVersion`: Version of source game, as int.
* `revised`: Tells the game if the song has been remastered (video AND audio) as boolean.
* `secureOnly`: Tells the game to not load the song if it cannot verify legal ownership, as boolean.

### Chart Data
One for every valid chart type a song has to offer. Should be stored something like this: `/data/music/<songId>/<chartType>.json`
Game will decide what all charts the song has by walking the directory.

Inside should be a list of JSON objects, one for each expected difficulty.
```json
    [
        {
            "difficulty": 0,
            "scale": 2,
            "customName": "example chart name",
            "rate": 1.0,
            "notes": [
                {"beat": 10, "length": 1.0, "position": 1, "isBonus": false, "sound": "ex_sound_1"},
                {"beat": 11, "length": 1.0, "position": 2, "isBonus": false, "sound": "ex_sound_2"},
                {"beat": 12, "length": 1.0, "position": 3, "isBonus": false, "sound": "ex_sound_3"},
                {"beat": 13, "length": 2.0, "position": 4, "isBonus": false, "sound": "ex_sound_4"},
                {"beat": 14, "length": 3.0, "position": 5, "isBonus": false, "sound": "ex_sound_5"},
                {"beat": 15, "length": 4.0, "position": 6, "isBonus": false, "sound": "ex_sound_6"},
                {"beat": 16, "length": 5.0, "position": 7, "isBonus": false, "sound": "ex_sound_7"},
            ]
        }
    ]
```
* `difficulty`: The difficulty type for the chart, should be a valid difficulty type.
* `scale`: The shown difficulty of the chart, as an integer.
* `customName`: Allows the chart to have a custom name rather than the default for the difficulty. Can be null or string.
* `rate`: The rate at which the notes fall, as float.
* `notes`: List of all notes in the chart.

* `note` format:
    * `beat`: The beat at which the note belongs to, as an integer. 
    * `length`: How many beats long the note is, as a float.
    * `position`: The "lane" the note should be placed on, as an integer.
    * `isBonus`: Disable score dropping if note is missed, add it as a bonus. Should be a boolean.
    * `sound`: The keysound the note should play, as a string.

### Static Data
List of games and versions:
  * `0`: EZ2DJ
    * `0`: The 1st Tracks
    * `1`: The 1st Tracks (Special Edition)
    * `2`: Dance Edition (Volume 1)
    * `3`: 2nd TraX
    * `4`: 3rd TraX
    * `5`: 4th TraX
    * `6`: Platinum (5th TraX)
    * `7`: 6th TraX
    * `8`: 7th TraX ~Resistance~
    * `9`: 7th TraX 1.50
    * `10`: 7th TraX 2.01
    * `11`: 7th TraX Codename Violet
    * `12`: Bonus Edition
    * `13`: Bonus Edition Revision A
    * `14`: Azure Expression
    * `15`: Azure Expression Integral Composition
  * `1`: EZ2Dancer
    * `0`: 1st Move
    * `1`: 2nd Move
    * `3`: U.K. Move
    * `4`: U.K. 2nd Move
    * `5`: Super China
  * `2`: Sabin Sound Star
    * `0`: 3S
  * `3`: EZ2ON
    * `0`: EZ2ON (Original)
    * `1`: EZ2ON Reboot
    * `2`: EZ2ON Reboot *R*
  * `4`: EZ2AC
    * `0`: Endless Circulation
    * `1`: EvolvE
    * `2`: Night Traveler
    * `3`: Time Traveler
    * `4`: FINAL
    * `5`: FINAL EX

List of chart types:
    * `5K_O`: 5Key Only
    * `5K_R`: 5Key Ruby
    * `5K`: 5Key Standard
    * `7K`: 7Key
    * `10K`: 10Key
    * `14K`: 14Key
    * `16K`: 16Key (Andromeda)
    * `CA`: EZ2Catch
    * `TT`: Turntable Mode

List of difficulties:
    * `0`: Easy
    * `1`: Normal
    * `2`: Hard
    * `3`: Super Hard
    * `4`: Extreme

List of note positions for each game mode:
    * 5Key Modes (minus 5Key Only)
      * `0`: Turntable
      * `1` -> `5`: Main keys
      * `6`: Pedal
    * 7Key Modes
      * `0`: Turntable
      * `1` -> `7`: Main keys
      * `8`: Pedal
    * 10Key Modes
      * `0`: Left Turntable
      * `1` -> `10`: Main keys
      * `11`: Right Turntable
      * `12`: Pedal
    * 14Key Modes
      * `0`: Left Turntable
      * `1` -> `14`: Main keys
      * `15`: Right Turntable
    * 16Key Modes
      * `0`: Left Turntable
      * `1` -> `14`: Main keys
      * `15`: Right Turntable
      * `16`: Left Pedal
      * `17`: Right Pedal
    * Turntable Mode + 5Key Only
      * `0` -> `4`: Main Keys
    * EZ2Catch
      * `0` -> `255`: Valid turntable positions