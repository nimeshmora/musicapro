import os
import json


def readJsonDirectoryAndLoadJson(json_file_directory):

    json_files = [pos_json for pos_json in os.listdir(json_file_directory) if pos_json.endswith('.json')]
    return json_files

def writeCSVFile():
    lowlevel_json_files = readJsonDirectoryAndLoadJson("cleandatajson/")
    csv_content = ""
    for js in lowlevel_json_files:
        with open(os.path.join("cleandatajson/", js)) as json_file:
            json_data_high_level = json.load(json_file)
            csv_content += extractInputsAndCreateString(json_data_high_level)

    text_file = open("musicagenreclass.csv", "w")
    text_file.write(csv_content)
    text_file.close()
            # print str(json_data_high_level["metadata"]["tags"]["musicbrainz_recordingid"][0])


def extractInputsAndCreateString(high_level_data):

    csv_content = str(high_level_data["tonal"]["chords_scale"])+","+str(high_level_data["tonal"]["chords_changes_rate"])+"," +str(high_level_data["tonal"]["chords_key"])+","+str(high_level_data["tonal"]["key_strength"])+"\n"
    return csv_content


writeCSVFile()

