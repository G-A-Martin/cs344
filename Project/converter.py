import json
import os
import re

from pandas import np

MY_NAME = "Gavin Martin"
combinedDictionary = {}


def cleanMessage(message):
    # Remove new lines within message
    cleanedMessage = message.replace('\n',' ').lower()
    # Deal with some weird tokens
    cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
    # Remove punctuation
    cleanedMessage = re.sub('([.,!?])','', cleanedMessage)
    # Remove multiple spaces in message
    cleanedMessage = re.sub(' +',' ', cleanedMessage)
    return cleanedMessage

def read_messages_from_file(filename):
    parsed_message_list = []
    with open(filename) as json_file:
        data = json.load(json_file)
        messages = data['messages']
        for i in range(len(messages)):
            message = messages[i]
            response = messages[i - 1]
            i += 1
            if ('content' in message) & ('content' in response):
                sender_name = message['sender_name']
                responder_name = response['sender_name']
                if(sender_name != MY_NAME) & (responder_name == MY_NAME):
                    parsed_message = {
                        "Name": sender_name,
                        "Message": cleanMessage(message['content']),
                        "Response": cleanMessage(response['content'])
                    }
                    parsed_message_list.append(parsed_message)
    return parsed_message_list


def get_all_messages_from_directories(file_path):
    all_parsed_messages = []
    for filename in os.listdir(file_path):
        if filename == ".DS_Store":
            continue
        individual_person_file_path = os.path.join(file_path, filename)
        for file in os.listdir(individual_person_file_path):
            if file.endswith("message_1.json"):
                complete_file_path = individual_person_file_path + "/message_1.json"
                all_parsed_messages.extend(read_messages_from_file(complete_file_path))
    return all_parsed_messages


def confirmed_clean(message_string):
    return True
    print("confirmedClean start")
    pattern = r'[^\.a-z0-9 ]'
    #pattern = r'[A-Za-z0-9 _.,!"?/$]*'
    if re.search(pattern, message_string):
        # Character other then . a-z 0-9 was found
        print('Invalid : %r' % (message_string,))
        return False
    else:
        # No character other then . a-z 0-9 was found
        print('Valid   : %r' % (message_string,))
        return True
    return False

def write_parsed_messages_to_dict(all_parsed_messages):
    for item in all_parsed_messages:
        #message_response_string = item["Message"] + "\t" + item["Response"] + "\n"
        if(confirmed_clean(item["Message"]) & confirmed_clean(item["Response"])):

            combinedDictionary[item["Message"]] = item["Response"]
    np.save('conversationDictionary.npy', combinedDictionary)


def write_parsed_messages_to_file(message_directory):
    all_parsed_messages = get_all_messages_from_directories(message_directory)
    write_parsed_messages_to_dict(all_parsed_messages)
    output_file = open("messages.txt", "w+")
    #for item in all_parsed_messages:
    #    message_response_string = item["Message"] + "\t" + item["Response"] + "\n"
    #    output_file.write(message_response_string)
    #output_file.close()
    for key, value in combinedDictionary.items():
        if (not key.strip() or not value.strip()):
            # If there are empty strings
            continue
        output_file.write(key.strip() + " " + value.strip() + " ")




# --------------- MAIN ----------------

write_parsed_messages_to_file('code/messages/inbox')



