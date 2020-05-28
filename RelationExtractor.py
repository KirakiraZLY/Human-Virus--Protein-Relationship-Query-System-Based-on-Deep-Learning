import textrazor
import os
textrazor.api_key = "69daf537deb507f29633c2d315e8df41ba6ad8e7b28b948f06f5beb4"
client = textrazor.TextRazor(extractors=["words", "entities", "entailments", "relations"])

manager = textrazor.ClassifierManager()
raw_text = ''
# rel_input = ""
# rel_input = input("Please input a relationship that u want to search for:")
for file in os.listdir("D:\\MY_STUDY\\scientific_research\\MY_NOTEBOOK\\RUNNING\\Seg2.0\\contentNotDone\\"):
    if file.endswith(".txt"):
        raw_text = open("D:\\MY_STUDY\\scientific_research\\MY_NOTEBOOK\\RUNNING\\Seg2.0\\contentNotDone\\"+file, errors='ignore').read() + '\n\n'
    text = raw_text

    # text = "Chicken type I interferons (type I IFNs) are key antiviral players of the chicken immune system and mediate the first line\
    #  of defense against viral pathogens infecting the avian species. Recognition of viral pathogens by specific pattern recognition receptors (PRRs)\
    #   induce chicken type I IFNs expression followed by their subsequent interaction to IFN receptors and induction of a variety of IFN stimulated antiviral proteins.\
    #    These antiviral effectors establish the antiviral state in neighboring cells and thus protect the host from infection. Three subtypes of chicken type I IFNs;\
    #     chIFN-α, chIFN-β, and a recently discovered chIFN-κ have been identified and characterized in chicken. Chicken type I IFNs are activated by various host cell\
    #      pathways and constitute a major antiviral innate defense in chicken. This review will help to understand the chicken type 1 IFNs, host cellular pathways that\
    #       are involved in activation of chicken type I IFNs and IFN stimulated antiviral effectors along with the gaps in knowledge which will be important for future \
    #       investigation. These findings will help us to comprehend the role of chicken type I IFNs and\
    #  to develop different strategies for controlling viral infection in poultry.Copyright © 2019 Elsevier Ltd. All rights reserved."
    buy_relations = []
    response = client.analyze(text)
    print(response.matching_rules())
    for relation in response.relations():
        for word in relation.predicate_words:

            # if word.lemma in (rel_input):
            # print(word.lemma)
            # buy_relations.append(relation)
            entity_params = []
            for param in relation.params:
                all_entities = list(param.entities())
                if all_entities:
                    entity_params.append(all_entities[0])
            if len(entity_params) > 1:
                print(" {0} between:{1}".format(word.lemma,entity_params))
                # print(relation)
            # break
        # print(buy_relations)
    #     # print("\n")
    for relation1 in buy_relations:
        entity_params = []
        # print(relation1.params)
        for param in relation1.params:
            all_entities = list(param.entities())
            if all_entities:
                entity_params.append(all_entities[0])
        if len(entity_params) > 1:
            print("Found valid relationship between:",entity_params)


    # >> > break
    for property in response.properties():
        for word in property.predicate_words:
            for property_word in property.property_words:
                for phrase in property_word.noun_phrases:
                    print(phrase)
