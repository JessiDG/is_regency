import string
import fileinput

class Is_Regency:

    def __init__(self, manuscript, dictionary):
        self.manuscript = self.to_unique_set(manuscript)
        self.dictionary = self.to_unique_set(dictionary)

    def to_unique_set(self, text):

        if type(text) is not str:
            raise TypeError("Please input a string")

        to_remove = string.punctuation + '-' + "\"" + "\'" + "“" + "‘" + "’" + string.digits
        stripped_string = ""
        for char in str(text):
            if char in to_remove:
                stripped_string += ' '
            else:
                stripped_string += char.lower()

        list_stripped_string = stripped_string.split()

        unique_words_set = set(list_stripped_string)
        return unique_words_set


    def find_difference(self):
        return self.manuscript - self.dictionary


    def __str__(self):
        i = 0
        difference = self.find_difference()
        return_str = ""
        for word in difference:
            if word is not None:
                return_str += str(i) + ": " + str(word) + "\n"
            i += 1
        return return_str


if __name__ == "__main__":
    with open('manuscript.txt', 'r') as ms:
        with open('websters_dictionary_1828.txt', 'r') as websters_dict:
            with open('all_jane_austen_pre_1828.txt', 'r') as all_austen:
                with open('dictionary_of_the_vulgar_tongue.txt', 'r') as vulgar_tongue:
                    with open('all_keats_pre_1828.txt', 'r') as keats:
                        with open('all_edgeworth_pre_1828.txt', 'r') as edgeworth:
                            with open('all_shelley_pre_1828.txt', 'r') as shelley:
                                with open('all_p_shelley_pre_1828.txt', 'r') as p_shelley:

                                    manuscript = ms.read()
                                    websters = websters_dict.read()
                                    austen = all_austen.read()
                                    vulgar = vulgar_tongue.read()
                                    keats = keats.read()
                                    edgeworth = edgeworth.read()
                                    shelley = shelley.read()
                                    p_shelley = p_shelley.read()

                                    print("Comparing text against Webster's 2nd Edition, 1828")
                                    websters_compare = Is_Regency(manuscript, websters)
                                    print("Comparing text against all of Jane Austen's novels")
                                    austen_compare = Is_Regency(websters_compare.__str__(), austen)
                                    print("Comparing text against the 1811 Dictionary in the "
                                          "Vulgar Tongue")
                                    vulgar_compare = Is_Regency(austen_compare.__str__(), vulgar)
                                    print("Comparing text against all of Keats")
                                    keats_compare = Is_Regency(vulgar_compare.__str__(), keats)
                                    print("Comparing text against all of Edgeworth")
                                    edgeworth_compare = Is_Regency(keats_compare.__str__(), edgeworth)
                                    print("Comparing text against all of Shelley")
                                    shelley_compare = Is_Regency(edgeworth_compare.__str__(), shelley)
                                    print("Comparing text against all of P.B. Shelley")
                                    all_compare = Is_Regency(shelley_compare.__str__(), p_shelley)

                                    legnth = len(manuscript) + len(websters) + len(austen) + len(
                                        vulgar) + len(keats) + len(edgeworth) + len(shelley) + \
                                             len(p_shelley)
                                    print("Compared against: " + "{:,}".format(legnth) + " words "
                                                                                         "used in the regency era. \n")

                                    print(all_compare)
