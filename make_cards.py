#!/usr/bin/env python

import sys
import re
import random


card_template_header = """
<!DOCTYPE html>
<!-- saved from url=(0051)file:///Users/dbanks/gitstuff/socialbingo/card.html -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <title>Title</title>

<style>
.page_size {
    width:8.5in;
    height:11in;
}

.page_div {
  position:relative;
}

.page_background {
    top: 0;
    left: 0;
    position: absolute;
}

.top_pad{
    padding-top: 265px;
}

.mytable {
    margin-left: auto;
    margin-right: auto;
}

body.nomargin {
  margin: 0px;
}

.mytable TD {
    width: 95px;
    height: 84px;
    padding:12px;
    text-align:center;
    font-family: "Tahoma";
    font-size: 12px;
    line-height: 1.5;
}

.stuff_on_top {
    position: absolute;
    top: 0px;
    left: 0px;
}

.my_page_break {
    page-break-after:always;
    margin: 0px;
}

table, th, td {
    border: 1px solid rgba(0, 0, 0, 0);
}
</style>

</head>
<body class="nomargin">
"""

card_template_body = """
<div class="page_div page_size">
    <img class="page_background page_size" src="background.png"\>
    <div class="stuff_on_top page_size">
    <div class="top_pad"></div>
    <table class="mytable">
        <tbody><tr>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
        </tr>
        <tr>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
        </tr>
        <tr>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>

            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
        </tr>
        <tr>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
        </tr>
        <tr>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
            <td>
                XXX
            </td>
        </tr>
    </tbody></table>
    </div>
</div>
<p class="my_page_break"/>
"""

card_template_body_parts = card_template_body.split("XXX")

card_template_footer = """
</body></html>
"""

def print_usage():
    """
    Remind user how to run this thing.
    :return:
    """
    sys.stderr.write("make_cards <number of cards> <filename for questions>\n")

def parse_command_line_args():
    """
    Pick apart command line, raise errors if something is wrong.
    :return:
    """
    if len(sys.argv) != 3:
        print_usage()
        raise Exception("Expected 2 arguments, found %d\n" % (len(sys.argv) - 1))

    try:
        num_cards = int(sys.argv[1])
    except ValueError:
        print_usage()
        raise Exception("Could not parse '" + sys.argv[1] + "' as a number.\n")

    filename = sys.argv[2]

    return filename, num_cards


first_clause = "[^\[]*"
second_clause = "[^\]]*"

p = re.compile("(" + first_clause + ")\[(" + second_clause + ")\](.*)")

def make_pq_from_line(line):

    matches = p.search(line)
    if matches == None:
        return {
            "question": line,
            "params": []
        }
    else:
        groups = matches.groups()
        params = groups[1].split(",")
        params = map(str.strip, params)
        return {
            "question": groups[0] + "%s" + groups[2],
#            "question": groups[0] + "%s",
            "params": params
        }

def parse_questions_file(filename):
    parametrized_questions = []

    f = open(filename, 'r')

    lines = f.readlines()

    for line in lines:
        line = line.strip()

        pq = make_pq_from_line(line)
        parametrized_questions.append(pq)


    return parametrized_questions


def print_card(parametrized_questions):

    random.shuffle(parametrized_questions)

    index = 0
    num_questions = len(card_template_body_parts) - 1
    while index < num_questions:
        sys.stdout.write(card_template_body_parts[index])

        pq = parametrized_questions[index]
        question = pq["question"]
        if len(pq["params"]) > 0:
            param = random.choice(pq["params"])
            question = question % param
        sys.stdout.write(question)
        index += 1

    sys.stdout.write(card_template_body_parts[index])



filename, num_cards = parse_command_line_args()
parametrized_questions = parse_questions_file(filename)


sys.stdout.write(card_template_header)

for i in range(num_cards):
    print_card(parametrized_questions)

sys.stdout.write(card_template_footer)