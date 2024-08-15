#!/usr/bin/env python

# euler problem 54
#
###########################################



from enum import Enum

tieflag = False


class Ranks(Enum):
    NORMAL = 0
    HIGHCARD = 1
    ONEPAIR = 3
    TWOPAIR = 4
    THREEKIND = 5
    STRAIGHT = 6
    FLUSH = 7
    FULLHOUSE = 8
    FOUROFAKIND = 9
    STRAIGHT_FLUSH = 10
    ROY_STRAIGHT = 11


class SPECIALCASE(Enum):
    IFISFULLHOUSE = 1
    PAIRSSTILLTIE = 2
    FIND_ORDER = 3


SEQ_NUMBER = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('S', 'C', 'H', 'D')
acc = 1
stepfeedback = None


def process_file(rawfile: str):
    """ process raw file into lists

    :return listA, listB
    :argument rawfile
    """

    lines = []

    with open(rawfile, mode='r') as fileforhands:
        for hand in fileforhands:
            lines.append(hand.split())

    return lines


def sort_card_value(card):
    """
    used for sort function below
    :param carda:  single card

    :return:
    """

    if len(card) == 2:
        card = card[0]

    return SEQ_NUMBER.index(card)


def find_max_value(handlist):
    temp_value = 0;
    temp_hand = []
    for card, hand in handlist:
        tempcard0 = SEQ_NUMBER.index(card[0])
        if tempcard0 > temp_value:
            temp_value = tempcard0
            temp_hand = hand
    result = SEQ_NUMBER[temp_value], temp_hand

    return result


def compare_a_with_b(alist, blist):
    # comparison of same types
    simplelistA = [carda[0] for carda in alist]
    simplelistB = [cardb[0] for cardb in blist]
    dif = SEQ_NUMBER.index(max(simplelistA, key=sort_card_value)) - \
          SEQ_NUMBER.index(max(simplelistB, key=sort_card_value))
    if dif > 0:
        return 1
    elif dif < 0:
        return -1
    else:
        return 0








        # give_final result()


def card_value_compare(valuea, valueb):
    """
    return higher card value, like 'T' > '9'
    :param sublista:
    :param sublistb:
    :return: True or false
    """

    if SEQ_NUMBER.index(valuea) > SEQ_NUMBER.index(valueb):

        return True
    else:
        return False


def find_sequencer(*dual_list):
    """
    find seq related ranks
    :param handA:
    :param handB:
    :return:
    """
    global stepfeedback

    # stepfeedback_local = None



    dual_result = [(False, Ranks.NORMAL, None), (False, Ranks.NORMAL, None)]
    temp_comparison = []
    handAorB = -1
    for indx, hand in enumerate(dual_list):  # should be 2 iterates
        stats = {}

        if len(hand) != 5:
            return dual_result
        card_values = [card[0] for card in hand]

        card_values.sort(key=sort_card_value)

        if ''.join(card_values) in ''.join(SEQ_NUMBER):
            temp_comparison.append(card_values)
            handAorB = indx

    if len(temp_comparison) == 2:

        if SEQ_NUMBER.index(temp_comparison[0][0]) >= SEQ_NUMBER.index(temp_comparison[1][0]):

            dual_result = (True, Ranks.STRAIGHT, dual_list[0]), (False, Ranks.STRAIGHT, dual_list[1])

        else:
            dual_result = (False, Ranks.STRAIGHT, dual_list[0]), (True, Ranks.STRAIGHT, dual_list[1])



    elif len(temp_comparison) == 1:

        stepfeedback = SPECIALCASE.IFISFULLHOUSE
        if handAorB == 0:

            dual_result = (False, Ranks.STRAIGHT, dual_list[0]), (False, Ranks.NORMAL, None)

        elif handAorB == 1:
            dual_result = (False, Ranks.NORMAL, None), (False, Ranks.STRAIGHT, dual_list[1])

    # else: no any straights





    return dual_result


def find_sameones(handA, handB):
    mapped_handA = [card[0] for card in handA]
    mapped_handB = [card[0] for card in handB]

    one_or_two_resdicts_for_pairs = []

    stepfeedback = None

    handlist = []

    def subfind_sameones(mapped_hand, maxnumberofkind=4):

        uni_value_dict = {}

        for card_value in mapped_hand:
            uni_value_dict[card_value] = uni_value_dict.setdefault(card_value, 0) + 1

        for cardvalue, numberofkind in uni_value_dict.items():
            handlist.append((cardvalue, mapped_hand, numberofkind))

    def find_pair(listforpair: list, handA, handB, stepfeedback):

        #     find pairs of a kind
        #
        # if not listforpair:
        #     return [(None, Ranks.NORMAL, None),(None, Ranks.NORMAL, None)], None

        card_list = []

        card_list, hands_list = zip(*listforpair)  # list, list

        number_of_pairs_for_handA = hands_list.count(mapped_handA)

        number_of_pairs_for_handB = hands_list.count(mapped_handB)

        # compare_return = compare_a_with_b(handA, handB)

        max_card = ''
        mapped_hand = []

        ret_result = [[False, Ranks.NORMAL, None], [False, Ranks.NORMAL, None]]

        len_handA = number_of_pairs_for_handA
        len_handB = number_of_pairs_for_handB
        # see if it is twopair
        if len_handA == 2:
            ret_result[0] = [False, Ranks.TWOPAIR, None]
        elif len_handA == 1:
            ret_result[0] = [False, Ranks.ONEPAIR, None]

        if len_handB == 2:
            ret_result[1] = [False, Ranks.TWOPAIR, None]
        elif len_handB == 1:
            ret_result[1] = [False, Ranks.ONEPAIR, None]

            # if len_handA > len_handB:
            #     ret_result[0][0] = True
            #     # one_or_two_resdicts_for_pairs.append(ret_result)
            # elif len_handB > len_handA:
            #     ret_result[1][0] = True
            # one_or_two_resdicts_for_pairs.append(ret_result)

        if len_handA == len_handB == 2 or len_handA == len_handB == 1:
            while listforpair:
                max_card, mapped_hand = find_max_value(listforpair)

                if max_card in mapped_handA and max_card in mapped_handB \
                        and mapped_handA.count(max_card) == mapped_handB.count(max_card):
                    # same max valued pairs
                    listforpair.remove((max_card, mapped_handA))
                    listforpair.remove((max_card, mapped_handB))




                elif max_card in mapped_handA:
                    if len_handA == 2:
                        ret_result = [(True, Ranks.TWOPAIR, None), (False, Ranks.TWOPAIR, None)]
                        break
                    else:
                        ret_result = [(True, Ranks.ONEPAIR, None), (False, Ranks.ONEPAIR, None)]
                        break

                elif max_card in mapped_handB:
                    if len_handA == 2:
                        ret_result = [(False, Ranks.TWOPAIR, None), (True, Ranks.TWOPAIR, None)]
                        break
                    else:
                        ret_result = [(False, Ranks.ONEPAIR, None), (True, Ranks.ONEPAIR, None)]
                        break


            else:
                stepfeedback = SPECIALCASE.PAIRSSTILLTIE






                # one_or_two_resdicts_for_pairs.append(ret_result)
        return ret_result, stepfeedback

    def find_four_kind(listforfour, mapped_handA, mapped_handB):
        if len(listforfour) == 2:

            max_card, mapped_hand = find_max_value(listforfour)

            if mapped_hand == mapped_handA:
                return [(True, Ranks.FOUROFAKIND, max_card), (False, Ranks.FOUROFAKIND, None)]
            elif mapped_hand == mapped_handB:
                return [(False, Ranks.FOUROFAKIND, None), (True, Ranks.FOUROFAKIND, max_card)]
        elif len(listforfour) == 1:
            if listforfour[0][1] == mapped_handA:
                return [(False, Ranks.FOUROFAKIND, listforfour[0][0]), (False, Ranks.NORMAL, None)]
            else:
                return [(False, Ranks.NORMAL, None), (False, Ranks.FOUROFAKIND, listforfour[0][0])]

    def find_three_kind(listforthree, mapped_handA, mapped_handB):

        stepfeedback_local = ''  # for special case to signal others

        if len(listforthree) == 2:

            max_card, mapped_hand = find_max_value(listforthree)

            # max_pairedcard, mapped_hand_pairedcard = find_max_value(listforpair)

            stepfeedback_local = SPECIALCASE.IFISFULLHOUSE

            if mapped_hand == mapped_handA:
                return [(True, Ranks.THREEKIND, max_card), (False, Ranks.THREEKIND, None)], stepfeedback_local
            elif mapped_hand == mapped_handB:
                return [(False, Ranks.THREEKIND, None), (True, Ranks.THREEKIND, max_card)], stepfeedback_local



                # elif mapped_hand == mapped_handA and len(
                #             listforpair) == 1 and mapped_hand_pairedcard == mapped_handA:
                #
                #         return [(True, Ranks.FULLHOUSE, max_card), (False, Ranks.THREEKIND, None)]

                # elif mapped_hand == mapped_handA and len(
                #         listforpair) == 1 and mapped_hand_pairedcard == mapped_handB:
                #
                #     return [(False, Ranks.THREEKIND, max_card), (True, Ranks.FULLHOUSE, max_pairedcard)]
                #
                # elif mapped_hand == mapped_handB and len(listforpair) == 2:
                #     return [(False, Ranks.FULLHOUSE, max_card), (True, Ranks.FULLHOUSE, None)]
                #
                # elif mapped_hand == mapped_handB and len(
                #         listforpair) == 1 and mapped_hand_pairedcard == mapped_handB:
                #
                #     return [(False, Ranks.THREEKIND, max_card), (True, Ranks.FULLHOUSE, max_pairedcard)]
                # elif mapped_hand == mapped_handB and len(
                #         listforpair) == 1 and mapped_hand_pairedcard == mapped_handA:
                #
                #     return [(True, Ranks.FULLHOUSE, max_pairedcard), (False, Ranks.THREEKIND, max_card)]
                #
                # elif mapped_hand == mapped_handA and len(listforpair) == 0:
                #
                #     return [(True, Ranks.THREEKIND, max_card), (False, Ranks.THREEKIND, None)]
                # elif mapped_hand == mapped_handB and len(listforpair) == 0:
                #
                #     return [(False, Ranks.THREEKIND, None), (True, Ranks.THREEKIND, max_card)]


        elif len(listforthree) == 1:

            stepfeedback_local = SPECIALCASE.IFISFULLHOUSE

            if listforthree[0][1] == mapped_handA:
                # if listforpair and [item[1] for item in listforpair if item[1] == mapped_handA]:

                #     return [(True, Ranks.FULLHOUSE, listforthree[0][0]), (False, Ranks.NORMAL, None)]
                # else:
                #     return [(True, Ranks.THREEKIND, listforthree[0][0]), (False, Ranks.NORMAL, None)]


                return [(False, Ranks.THREEKIND, listforthree[0][0]), (False, Ranks.NORMAL, None)], \
                       stepfeedback_local

            # if listforthree[0][1] == mapped_handB:
            #     if listforpair and [item[1] for item in listforpair if item[1] == mapped_handB]:
            #
            #         return [(False, Ranks.NORMAL, None), (True, Ranks.FULLHOUSE, listforthree[0][0])]
            #     else:
            #         return [(False, Ranks.NORMAL, None), (True, Ranks.THREEKIND, listforthree[0][0])]

            else:
                return [(False, Ranks.NORMAL, None), (False, Ranks.THREEKIND, listforthree[0][0])], \
                       stepfeedback_local





            # ---------------------------------------------------------------------------------------------------


            # count numbers of every cardvalue, and put results into handlist

    subfind_sameones(mapped_handA)

    subfind_sameones(mapped_handB)

    # determination process, pre-process, break handlist into dif lists per quantity
    init = 0
    listforfour = []
    listforthree = []
    listforpair = []
    for cardvalue, mapped_hand, numberofkind in handlist:  # merged handlist

        if numberofkind == 4:
            listforfour.append((cardvalue, mapped_hand))
        elif numberofkind == 3:
            listforthree.append((cardvalue, mapped_hand))
        elif numberofkind == 2:
            listforpair.append((cardvalue, mapped_hand))

    # find fourkind

    if listforfour:
        dual_result = find_four_kind(listforfour, mapped_handA, mapped_handB)

        one_or_two_resdicts_for_pairs.append(dual_result)

    # find out threekind and full house

    if listforthree:
        dual_result, stepfeedback = find_three_kind(listforthree, mapped_handA, mapped_handB)

        one_or_two_resdicts_for_pairs.append(dual_result)

    # find out pairs (one pair and two pairs)


    if listforpair:

        if stepfeedback == SPECIALCASE.IFISFULLHOUSE:
            stepfeedback = None

            dual_result, stepfeedback = find_pair(listforpair, handA, handB, stepfeedback)

            # adjustment for fullhouse when tie exists on fullhouse

            if dual_result[0][1] == dual_result[1][1] == Ranks.ONEPAIR:
                if one_or_two_resdicts_for_pairs[0][0][0]:
                    one_or_two_resdicts_for_pairs.append([(True, Ranks.NORMAL, None),
                                                          (False, Ranks.NORMAL, None)])
                elif one_or_two_resdicts_for_pairs[0][1][0]:
                    one_or_two_resdicts_for_pairs.append([(False, Ranks.NORMAL, None),
                                                          (True, Ranks.NORMAL, None)])

            one_or_two_resdicts_for_pairs.append(dual_result)




        else:

            # twopairs, onepair ,ties
            dual_result, stepfeedback = find_pair(listforpair, handA, handB, stepfeedback)

            one_or_two_resdicts_for_pairs.append(dual_result)

    if not (listforpair or listforthree or listforfour):
        stepfeedback = SPECIALCASE.FIND_ORDER

    return one_or_two_resdicts_for_pairs, stepfeedback


def find_suit(*dual_list, min_numbercardofsamesuit=5):
    """

    :param handA:
    :param handB:
    :param min_numbercardofsamesuit:
    :return: dual_result : a list of 2 structures
    """
    global stepfeedback
    # stepfeedback_local = None
    # dual_list = [handA, handB]
    dual_result = []
    for hand in dual_list:
        stats = {}
        temp_suit_list = []
        for card in hand:

            if card[1] in SUITS:
                temp_suit_list.append(card[1])
        if len(set(temp_suit_list)) == len(temp_suit_list) - min_numbercardofsamesuit + 1:

            mid_result = False, Ranks.FLUSH, hand
        else:
            mid_result = False, Ranks.NORMAL, None

        dual_result.append(mid_result)

    if dual_result[0][1] != dual_result[1][1]:
        stepfeedback = SPECIALCASE.IFISFULLHOUSE

    return dual_result


def find_order(handA: list, handB: list):
    print("find_order", handA, handB)
    if handA and handB:

        hand_value_A = [card[0] for card in handA]
        hand_value_B = [card[0] for card in handB]

        max_card_value = max(hand_value_A + hand_value_B, key=sort_card_value)

        if max_card_value in hand_value_A and max_card_value \
                not in hand_value_B:
            return [(False, Ranks.HIGHCARD, max_card_value), (False, Ranks.NORMAL, None)]

        elif max_card_value in hand_value_B and max_card_value not in hand_value_A:
            return [(False, Ranks.NORMAL, None), (False, Ranks.HIGHCARD, max_card_value)]

        elif max_card_value in hand_value_A and max_card_value in hand_value_B:

            handA.pop(hand_value_A.index(max_card_value))
            handB.pop(hand_value_B.index(max_card_value))

            resdict = find_order(handA, handB)

    else:

        raise Exception("ties still happen here")

    return resdict


def sorter(handA, handB):
    """

    :param listA:
    :param listB:
    :return:
    """

    # sum_dict = {}

    global stepfeedback

    # handA is 5 item list
    resdict_list = []
    resdict = find_sequencer(handA, handB)  # return a list of (boolean, matched type, detail)

    resdict_list.append(resdict)

    resdict = find_suit(handA, handB)

    resdict_list.append(resdict)

    if resdict_list[0][0][1] == resdict_list[0][1][1] == resdict_list[1][0][1] \
            == resdict_list[1][1][1] == Ranks.NORMAL or \
                    stepfeedback == SPECIALCASE.IFISFULLHOUSE:

        one_or_two_of_resdict, stepfeedback = find_sameones(handA,
                                                            handB)  # must cover all cases and total results for dif pair types

        if type(one_or_two_of_resdict) == tuple:  # only one cell taken back

            resdict_list.append(one_or_two_of_resdict)
        elif type(one_or_two_of_resdict) == list:

            resdict_list.extend(one_or_two_of_resdict)

    if stepfeedback == SPECIALCASE.PAIRSSTILLTIE or stepfeedback == SPECIALCASE.FIND_ORDER or tieflag:
        resdict = find_order(handA, handB)
        resdict_list.append(resdict)

    return resdict_list


def result_merger(resdict_list, handA, handB):
    player1_score = 0
    player2_score = 0
    global player1_wins
    global player2_wins
    global tieflag
    tieflag = False
    global acc

    def cutlistifties(handAlocal, handBlocal):

        card_value_listB = [card_value for card_value, card_suit in handBlocal]

        for card_value, card_suit in handAlocal:

            try:

                handBlocal.pop(card_value_listB.index(card_value))

            except ValueError:
                continue

            else:
                break

        handAlocal.remove(card_value + card_suit)

        return handAlocal, handBlocal

    for player1, player2 in resdict_list:
        bool_resultA, typeA, detailA = player1
        bool_resultB, typeB, detailB = player2

        # result accumulation


        player1_score += typeA.value + bool_resultA

        player2_score += typeB.value + bool_resultB

    if player1_score > player2_score:
        player1_wins += 1
    elif player1_score < player2_score:
        player2_wins += 1

    else:  # equal to
        # print("player1 and player2 ties" )
        tieflag = True

        cutlistifties(handA, handB)

    # print(str(acc) + ':', player1_score, player2_score)

    acc += 1

    return player1_score, player2_score


player2_wins = 0
player1_wins = 0


def main():
    from pprint import pprint
    global tieflag

    lines = process_file(r'C:\Users\danny\PycharmProjects\N1\p054_poker.txt')

    for line in lines:

        tieflag = False;
        stepfeedback = None

        handA = line[:5];
        handB = line[5:]

        print(handA, handB)

        while True:

            resdict_list = sorter(handA, handB)

            pprint(resdict_list, width=120)

            p1_score, p2_score = result_merger(resdict_list, handA, handB)

            print(p1_score, p2_score)

            if not tieflag:
                break

            print("tieflag")

    print("total:", player1_wins, player2_wins)


if __name__ == '__main__':
    main()
