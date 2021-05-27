# -*- coding: utf-8 -*-
import re


def set_id(pair_list, id_dict, id):
    """
    This method is to assign id numbers to synonyms/similar words;
    Each set of synonyms will have the same id number.
    """
    synonym_leftpart = pair_list[0]
    synonym_rightpart = pair_list[1]

    # case 1: synonym_leftpart or synonym_rightpart is not in id_dict, which means the synonym word is not assigned an ID yet
    # (1) if synonym_leftpart is not in id_dict, then assign an ID to it
    if synonym_leftpart not in id_dict:
        id_dict[synonym_leftpart] = [id, synonym_rightpart]
        id += 1

    # (2) if synonym_rightpart is not in id_dict, since synonym_leftpart must be in id_dict, so assign the same ID to it
    if synonym_rightpart not in id_dict:
        id_dict[synonym_rightpart] = [id_dict[synonym_leftpart][0], synonym_leftpart]

    # case 2: synonym_leftpart and synonym_rightpart are both in id_dict
    # check if synonym_leftpart and synonym_rightpart have the same ID
    # if not, update the larger ID to the smaller one
    id_leftpart = id_dict[synonym_leftpart][0]
    id_rightpart = id_dict[synonym_rightpart][0]
    pair_leftpart = id_dict[synonym_leftpart][1]
    pair_rightpart = id_dict[synonym_rightpart][1]

    if id_leftpart > id_rightpart:
        id_dict[synonym_leftpart][0] = id_rightpart
        id_dict[pair_leftpart][0] = id_rightpart
    elif id_leftpart < id_rightpart:
        id_dict[synonym_rightpart][0] = id_leftpart
        id_dict[pair_rightpart][0] = id_leftpart

    return id_dict, id


def format_word(word):
    new_word = re.sub(r'{|}|\"|”|“|\(|\)', '', word).strip()
    return new_word


if __name__ == "__main__":
    # Read the filenames of the user inputs
    print("Input:")
    filename_WF = input("\tPlease enter the file name of WF: ")
    filename_SYN = input("\tPlease enter the file name of SYN: ")

    # Using a dictionary id_dict to record the id assignment for all synonyms pairs
    # id starts from 0, increased by 1 when meeting a different word
    # Each element of id_dict is a key: value pair, and key: synonym_leftpart, value: [id, synonym_rightpart]
    id_dict = {}
    id = 0

    # Initial the result_dict dictionary which will be the final output result
    # Each element in result_dict is a key: value pair, and key: id, value: [the word, the total frequency]
    result_dict = {}

    # Used to get the entire string SYN for final output display
    SYN_string = ""
    # Used to get the entire string WF for final output display
    WF_string = ""

    try:
        with open(filename_SYN, "r") as f_SYN:
            # Read SYN file line by line
            for each_line in f_SYN:
                pair_list = []
                SYN_string += each_line
                for each_word in each_line.split(","):
                    each_word = format_word(each_word)
                    if len(pair_list) < 2:
                        pair_list.append(each_word)
                    else:
                        # Call set_id() to assign/update an id for each pair of synonyms in SYN
                        id_dict, id = set_id(pair_list, id_dict, id)
                        # Reset the pair_list
                        pair_list = [each_word]

                # Assign an id to the last pair of each line
                id_dict, id = set_id(pair_list, id_dict, id)

        with open(filename_WF, "r") as f_WF:
            # Read WF file line by line
            # Convert the string WF to a dictionary WF, and each element in WF is a word:frequency pair
            WF = {}
            for each_line in f_WF:
                WF_string += each_line
                sublist = []
                for each_word in each_line.split(","):
                    each_word = format_word(each_word)
                    if len(sublist) < 2:
                        sublist.append(each_word)
                    else:
                        WF[sublist[0]] = sublist[1]
                        sublist = [each_word]
                # Add the last pair of each line to the dictionary WF
                WF[sublist[0]] = sublist[1]

            # Check each pair [word, frequency] in the list WF
            for each_pair in WF.items():
                word = each_pair[0]
                frequency = int(each_pair[1])
                # If the word is not in id_dict, which means this word has no synonym, then add [word, frequency] directly to result_dict
                if word not in id_dict:
                    result_dict[id] = [word, frequency]
                    id += 1
                else:
                    # else (which means the word is in id_dict and has some synonym), 2 steps need to be done:
                    syn_id = id_dict[word][0]
                    if syn_id not in result_dict:
                        result_dict[syn_id] = [word, frequency]
                    else:
                        # step 1: compare and store the word that is the earliest in the alphabet in result_dict
                        if word < result_dict[syn_id][0]:
                            result_dict[syn_id][0] = word
                        # step 2: calculate the cumulative frequency of its synonyms in result_dict
                        result_dict[syn_id][1] += frequency

            # print the result to screen
            print("\nOutput:")
            print("\tThe WF : " + WF_string)
            print("\tThe SYN: " + SYN_string)
            print("\tThe CF : {", end="")
            counter = 0
            for each_id in result_dict:
                counter += 1
                if counter == len(result_dict):
                    break
                print("(\"" + result_dict[each_id][0] + "\", " + str(result_dict[each_id][1]) + "),", end="")
            print("(\"" + result_dict[each_id][0] + "\", " + str(result_dict[each_id][1]) + ")}")

    # if there is no such file or the file cannot be opened, an error is raised
    except Exception as reason:
        print(reason)
