'''
complete the program below, so that after you have two lists of files for two specified folders, the program
    0) comment the existing code that gets the list of file names
    1) creates an empty dictionary for artist
    2) adds that dictionary to the lyric dictionary list. make sure you lower-case all the words.
    3) goes through each file in the artist's folder, counts the words in each file, and adds them to the appropriate
        dictionary
    4) prints out:
        - a list of the artists
        - their total number of songs
        - their total number of unique words
        - their total number of words overall
        like this:
            artist      songs       unique words       total words     unique word ratio
            swift       10          105                 986             9.10
            kanye       10          108                 751             7.54
'''
import os, sys
##import library
lyric_dictionary_list = []
##create an empty list
input_directory = sys.argv[1]
##save arguments input in the terminal
artist_list = os.listdir(input_directory)
##convert the file names into a list

for artist in artist_list:
    if not artist == '.DS_Store':
        artist_dictionary = {}
        ##not printing file '.DS_Store'
        song_list = os.listdir(input_directory + artist)
        ##convert song names into a list
        song_count = 0
        total_word_count = 0
        unique_word = 0
        for song in song_list:

            file_name = input_directory + artist + "/" + song
            f = open(file_name)

            for line in f:
                word = line.lower()
                word = word.strip('\n')
                word = word.split(' ')
                for i in range(len(word)):
                    if word[i] in artist_dictionary.keys():
                        word_count = int(artist_dictionary.get(word[i]))
                        word_count += 1
                        artist_dictionary[word[i]] = word_count
                    else:
                        artist_dictionary[word[i]] = 1
                        unique_word += 1
                    total_word_count += 1

            f.close()

            song_count += 1    
        lyric_dictionary_list.append(artist_dictionary)

        
    unique_word_ratio = unique_word / total_word_count

    print('artist'+'      '+'songs'+'      '+'unique words'+'      '+'total words'+'      '+'unique word ratio')
    print("{0}       {1}          {2}                 {3}             {4}".format(artist,song_count,unique_word,total_word_count,unique_word_ratio))

