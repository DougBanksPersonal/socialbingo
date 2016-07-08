#!/usr/bin/env python

import sys
import re
import random


card_template_header = """
<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">.lst-kix_dpfdckkw5041-0>li\
:before{content:""}.lst-kix_pc088b8pwvpt-0>.lst-kix_5gsf6y5s2jvw-1>li:before{content:"\00\
25cb  "}.lst-kix_dpfdckkw5041-4>li:before{content:"\0025cb  "}ul.lst-kix_pc088b8pwvpt-0{list-style-type:circle}.lst-kix_5gsf6y5s2j\
vw-0>.lst-kix_dpfdckkw5041-1>li:before{content:"\0025cb  "}.lst-kix_dpfdckkw5041-5>li:before{conte\
nt:"\0025a0  "}.lst-kix_dpfdckkw5041-2>li:before{content:"\0025a0  "}.lst-kix_dpfdckkw5041-3>ul.ls\
t-kix_pc088b8pwvpt-6{list-style-type:circle}ul.lst-kix_pc088b8pwvpt-5{list-style-type:circle}ul.lst-kix_pc088b8pwvpt-8{list-style-ty\
pe:none}ul.lst-kix_pc088b8pwvpt-7{list-style-type:circle}ul.lst-kix_pc088b8pwvpt-2{list-style-type:circle}ul.lst-kix_pc088b8pwvpt-1{\
list-style-type:circle}ul.lst-kix_pc088b8pwvpt-4{list-style-type:circle}ul.lst-kix_pc088b8pwvpt-3{list-style-type:circle}ul.lst-kix_dp\
fdckkw5041-0{list-style-type:circle}ul.lst-kix_dpfdckkw5041-2{list-style-type:circle}ul.lst-kix_dpfdckkw5041-1{list-style-type:circle}\
ul.lst-kix_dpfdckkw5041-8{list-style-type:circle}ul.lst-kix_dpfdckkw5041-7{list-style-type:circle}ul.lst-kix_dpfdckkw5041-4{list-sty\
le-type:none}ul.lst-kix_dpfdckkw5041-3{list-style-type:circle}ul.lst-kix_dpfdckkw5041-6{list-style-type:circle}ul.lst-kix_dpfdckkw50\
41-5{list-style-type:circle}ul.lst-kix_5gsf6y5s2jvw-1{list-style-type:circle}ul.lst-kix_5gsf6y5s2jvw-0{list-style-type:circle}.lst-kix\
_5gsf6y5s2jvw-8>li:before{content:"\0025a0  "}.lst-kix_pc088b8pwvpt-7>li:before{content:"\0025cb  "}.lst-kix_pc088b8pwvpt-6>li:b\
efore{content:""}.lst-kix_5gsf6y5s2jvw-7>li:before{content:"\0025cb  "}.lst-kix_dpfdckkw5041-8>li:before{content:"\0025\
a0  "}ul.lst-kix_5gsf6y5s2jvw-8{list-style-type:circle}ul.lst-kix_5gsf6y5s2jvw-7{list-style-type:circle}ul.lst-kix_5gsf6y5s2jvw-6{li\
st-style-type:none}ul.lst-kix_5gsf6y5s2jvw-5{list-style-type:circle}.lst-kix_dpfdckkw5041-6>ul.lst-k\
ix_5gsf6y5s2jvw-4{list-style-type:circle}.lst-kix_pc088b8pwvpt-8>li:before{content:"\0025a0  "}ul.lst-kix_5gsf6y5s2jvw-3{list-styl\
e-type:none}.lst-kix_dpfdckkw5041-7>li:before{content:"\0025cb  "}ul.lst-kix_5gsf6y5s2jvw-2{list-style-type:circle}.lst-kix_pc088b\
8pwvpt-1>li:before{content:"\0025cb  "}.lst-kix_5gsf6y5s2jvw-2>li:before{content:"\0025a0  "}.lst-kix_pc088b8pwvpt-3>li:before{c\
ontent:""}.lst-kix_pc088b8pwvpt-2>li:before{content:"\0025a0  "}.lst-kix_5gsf6y5s2jvw-3>.\
lst-kix_pc088b8pwvpt-5>li:before{content:"\0025a0  "}.lst-kix_5gsf6y5s2jvw-4>li:before{content:"\0025cb  "}.lst-kix_5gsf6y5s2jvw\
-6>.lst-kix_pc088b8pwvpt-4>li:before{content:"\0025cb  "}.lst-kix_5gsf6y5s2jvw-5>li:before{content\
:"\0025a0  "}ol{margin:0;padding:0}table td,table th{padding:0}.c1{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-botto\
m-color:#000000;border-top-width:1pt;border-right-width:1pt;border-left-color:#000000;vertical-align:middle;border-right-color:#\
000000;border-left-width:1pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:93.6pt;border-top-colo\
r:#000000;border-bottom-style:solid}.c2{color:#000000;font-weight:normal;text-decoration:none;vertical-align:baseline;font-size:\
11pt;font-family:"Arial";font-style:normal}.c3{margin-left:36pt;orphans:2;widows:2;padding-left:0pt}.c10{margin-left:auto;border\
-spacing:0;border-collapse:collapse;margin-right:auto}.c4{padding-top:0pt;padding-bottom:0pt;line-height:1.0;text-align:center}.\
c13{font-size:14pt;font-style:italic;font-weight:bold}.c6{orphans:2;widows:2;height:11pt}.c7{background-color:#ffffff;max-width:\
468pt;padding:72pt 72pt 72pt 72pt}.c0{orphans:2;widows:2;text-align:center}.c11{background-color:#ffffff;color:#222222}.c5{paddi\
ng:0;margin:0}.c8{orphans:2;widows:2}.c12{page-break-after:avoid}.c9{height:72pt}.title{padding-top:0pt;color:#000000;font-size:\
26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:center}.subtitle\
{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;or\
phans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;fon\
t-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-b\
reak-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-fam\
ily:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-si\
ze:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{pad\
ding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphan\
s:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height\
:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:\
4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}</style></h\
ead><body class="c7">
"""

card_template_body = """
<p class="c0 c12 title" id="h.43cplygceymy"><span>RDC 2016 Bingo</span></p><p class="c0"><span>Fill squares\
 by finding matching people; have them write their name (legibly!) in the square.</span></p><p class="c0"><span>You can only use\
 a given person once! </span></p><p class="c0"><span>You can&rsquo;t use yourself!</span></p><p class="c6"><span></span></p><p c\
lass="c8"><span>Prizes for the first card with:</span></p><ul class="c5 lst-kix_dpfdckkw5041-0 start"><li class="c3"><span>Five \
filled squares in a row (vertical, horizontal, or diagonal)</span></li><li class="c3"><span>A 3x3 block of filled squares</span>\
</li><li class="c3"><span>All squares filled</span></li></ul><p class="c6"><span></span></p><p class="c0"><span class="c13">Find\
 someone who&hellip;</span></p><p class="c6"><span></span></p><a id="t.5b8654e8209fc94700f6b91e1f88633051925c12"></a><a id="t.0"\
></a><table class="c10"><tbody><tr class="c9"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></\
p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowsp\
an="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">X\
XX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td></tr><tr class="c9"><\
td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><\
p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span\
></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" ro\
wspan="1"><p class="c4"><span class="c2">XXX</span></p></td></tr><tr class="c9"><td class="c1" colspan="1" rowspan="1"><p class=\
"c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></t\
d><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">Free Space!</span></p></td><td class="c1" colspan="1" ro\
wspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2\
">XXX</span></p></td></tr><tr class="c9"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c11">XXX</span></p></\
td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="\
1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</\
span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td></tr><tr class="c9"><td c\
lass="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p cl\
ass="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p\
></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c2">XXX</span></p></td><td class="c1" colspan="1" rowspa\
n="1"><p class="c4"><span class="c2">XXX</span></p></td></tr></tbody></table><p class="c6"><span></span></p>
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

        sys.stderr.write("\n")
        sys.stderr.write(line + "\n")

        pq = make_pq_from_line(line)
        parametrized_questions.append(pq)

        sys.stderr.write(str(pq) + "\n")

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
    sys.stdout.write('<p style="page-break-after:always;"></p>')



filename, num_cards = parse_command_line_args()
parametrized_questions = parse_questions_file(filename)


sys.stdout.write(card_template_header)

for i in range(num_cards):
    print_card(parametrized_questions)

sys.stdout.write(card_template_footer)