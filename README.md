# Mission-unit-converter

Python script to convert one set of units to another using JSON maps.

its really just a find and replace...

## Usage

        python convert.py <missionFolder> <conversionJson>

eg

        python convert.py ../TBC-Operation_Dinosaur_V1.Tanoa/ conversions/Replace_Project_Opfor.json

Original mission will be backed up as `mission-backup.sqm` and the original `mission.sqm` will be overwritten.
if trying to remove a mod you may have to open up the mission in the editor or text editor to search for remaining units,custom-kits, etc

## Configuration
Create json file to map old units to new ones like this or use one in the conversion folder

        {
            "OLD": "NEW",
            "LOP_IRA_Infantry_TL": "rhsgref_ins_rifleman_akm"
        }
**BE WARNED ORDER MATTERS more specific names must go before more general ones ie LOP_IRA_Infantry_TL must go before LOP_IRA_Infantry otherwise replace may not work**

Feel free to contribute any conversions you have