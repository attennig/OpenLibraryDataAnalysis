import json

input_file = open("books_json.txt", 'r', encoding='utf-8')
output_file = open("books_long.csv", 'w', encoding='utf-8')
fields = ["key", "title", "subtitle", "authors", "translated_titles", "subjects", "subject_places", "subject_times", "subject_people", "description", "dewey_number", "lc_classifications", "first_sentence", "original_languages ", "other_titles", "first_publish_date", "links", "notes", "cover_edition", "covers"]
head = ["key", "title", "subtitle", "authors", "translated_titles", "subjects", "description", "dewey_number", "lc_classifications", "first_sentence", "original_languages ", "other_titles", "first_publish_date", "links", "notes", "cover_edition", "covers"]

output_file.writelines("{}\n".format(';'.join(head)))

#limit = 50000

while True:
    line = input_file.readline()
    #limit -= 1
    if not line:# or limit < 0:
        break
    json_obj = json.loads(line.split("\t")[4])
    not_null_fields = json_obj.keys()
    line_to_write = ""
    for field in head:
        if field in not_null_fields:
            if field == "authors":
                authors = []
                for el in json_obj[field]:
                    try:
                        authors += [el["author"]["key"].split('/')[2].replace(';', ',')]
                    except:
                        continue
                line_to_write += '{}'.format(authors)

            elif field == "key":
                book_id = json_obj[field].split('/')[2]
                line_to_write += '{}'.format(book_id.replace(';', ','))

            elif field == "description":
                if type(json_obj["description"]) == dict:
                    text = json_obj["description"]["value"]
                else:
                    text = json_obj["description"]
                '''text = text.replace('\n', '')
                text = text.replace('\r', '')
                text = text.replace('\t', '')'''
                line_to_write += text.replace(';', ',')
            elif field == "subjects":
                subjects = []
                for subfield in ["subjects", "subject_places", "subject_times", "subject_people"]:
                    try:
                        for el in json_obj[subfield]:
                            subjects += [el.replace(';', ',')]
                    except: continue

                line_to_write += '{}'.format(subjects)
            else:
                line_to_write += '{}'.format(str(json_obj[field]).replace(';', ','))



        line_to_write += ";"
    line_to_write = line_to_write.replace('\t', '')
    line_to_write = line_to_write.replace('\r', '')
    line_to_write = line_to_write.replace('\n', '')
    line_to_write +="\n"

    output_file.writelines(line_to_write)


input_file.close()
output_file.close()