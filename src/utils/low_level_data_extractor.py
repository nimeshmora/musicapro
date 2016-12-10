import urllib2
import os, json
import pandas as pd
import csvgenereator

music_brainz_id_list = []
PATH_TO_JSON_DIRECTORY = '/home/nimesha/Documents/level-4-research-project/DatasetEssentia/data500'

def readJsonDirectoryAndLoadJson(json_file_directory):

    json_files = [pos_json for pos_json in os.listdir(json_file_directory) if pos_json.endswith('.json')]
    return json_files

def readHighLevelJsonFiles(json_file_directory):

    json_files = readJsonDirectoryAndLoadJson(json_file_directory)
    for js in json_files:
        with open(os.path.join(json_file_directory, js)) as json_file:
            json_data_high_level = json.load(json_file)
           # print str(json_data_high_level["metadata"]["tags"]["musicbrainz_recordingid"][0])
            music_brainz_id_list.append(json_data_high_level["metadata"]["tags"]["musicbrainz_recordingid"][0])

    return music_brainz_id_list


def createCleanJsonFile(url_id):

    url = "https://acousticbrainz.org/api/v1/" + url_id+ "/low-level"
    json_output = urllib2.urlopen(url).read()

    # print json_output
    writeDataToJson(json_output, url_id)


def writeDataToJson(low_level_data_json, id):
    text_file = open("cleandatajson/"+id+".json", "w")
    text_file.write(low_level_data_json)
    text_file.close()

def readAndWriteLowLevelJsonFiles():
        filewritecount = 1
        id_list = readHighLevelJsonFiles(PATH_TO_JSON_DIRECTORY)
        # print id_list

        for id in id_list:

            # print id
            createCleanJsonFile(id)
            print "wrote "+ str(filewritecount) + " json file " + "ID = " + id

            filewritecount +=1

readAndWriteLowLevelJsonFiles()

# readLowLevelData("96685213-a25c-4678-9a13-abd9ec81cf35")