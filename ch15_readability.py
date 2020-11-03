from readability import Readability

text = open('C:\\...\\ch15_MLK-IHaveADream.txt')
text_up = text.read()

r = Readability(text_up)
flesch_kincaidR = r.flesch_kincaid()


print('The text has a grade '+ flesch_kincaidR.grade_level + ' readability level.')
