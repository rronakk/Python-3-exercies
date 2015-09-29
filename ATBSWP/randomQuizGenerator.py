"""
Create a 35 different quizzes
Create 50 multiple choice quesrions for each quiz
Provide 1 correct answer, and 3 incorrect answer for each question in random order.
Write quiz in 35 test files.
Write answer keys to 35 test files
"""

import random

capitals = {
    'Alabama': 'Montgomery', 'Montana': 'Helena',
    'Alaska': 'Juneau', 'Nebraska': 'Lincoln',
    'Arizona': 'Phoenix', 'Nevada': 'Carson City',
    'Arkansas': 'Little Rock', 'New Hampshire': 'Concord',
    'California': 'Sacramento', 'New Jersey': 'Trenton',
    'Colorado': 'Denver', 'New Mexico': 'santa Fe',
}
for quizNUM in range(10):
    # Create the quiz and answer key files
    quizFile = open('capitalQuiz%s.txt' % (quizNUM + 1), 'w')
    answerFile = open('capitalQuiz_AnswerKey%s.txt' % (quizNUM + 1), 'w')

    # Write out header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + 'State Capital Quizz (%s)' % (quizNUM + 1))
    quizFile.write('\n\n')

    # Shuffle order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all states, and making question for each state.
    for questionNum in range(12):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)

        quizFile.write('%s. What is the capital of %s ?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(('   %s. %s\n') % ('ABCD'[i], answerOption[i]))
        quizFile.write('\n')

        answerFile.write('%s. %s \n' % (questionNum + 1, 'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
