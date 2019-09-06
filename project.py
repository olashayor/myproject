
import pymysql.cursors

# connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='shayor',
                            charset='utf8mb4',
                            cursorclass=pymysql
                            .cursors.
                            DictCursor)

# create a new table
# with connection.cursor() as cursor:
#     sql = """CREATE TABLE Depression_rate
#     (id int NOT NULL KEY AUTO_INCREMENT,
#     gender VARCHAR(8), 
#     age VARCHAR (10),
#     depression_percentage INT(50)) """
#     cursor.execute(sql)
#     connection.commit()


# print("""GOOD DAY SIR/MA
#     WELCOME ON BOARD 
#     We are learning about depression, how to detect it and how we can keep ourselves \n""")
# input("press enter to continue")

# print("""Depression is a mood disorder that causes feelings of sadness and a loss of interest in activities once enjoyed. 
# It can lead to a variety of emotional and physical problems and can decrease a person’s ability to function at work and at home.
# Depression is a common and serious medical illness that negatively affects how you feel, the way you think and how you act.\n
# Fortunately, it is also treatable. \n""")
# input("press enter to continue")

# print("Read the following questions and answer them appropriately as it apply to you within the last two week")
# input("press enter to continue")

questions = {
    'question one':
        '''How do you fill about yourself presently? 
            (a) Awesome
            (b) Good
            (c) Helpless 
            (d) Hopeless
            (e) Miserable''', 
 
    'question two':
        '''Do you think life has been so unfair with you?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',

    'question three':
        '''Are you confidence in yourself, do you believe in yourself?
            (a) Yes always
            (b) Not sure
            (c) Yes sometime
            (d) Not always
            (e) Not at all''',
    
    'question four':
        '''Do you have hidden pain your heart that you are living with and you are being reminded constantly in you heart?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',
    
    'question five':
        '''Do you try as much as possible to avoid social gathering and preferred to just stay alone?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',
               
    'question six':
        '''Do you blame yourselves easily even on things that are not directly your fault or those that you have little or no control over? 
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',
             
    'question seven':
        '''Do you have problem thinking fast or concentrating easily? 
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',
             
    'question eight':
        '''Do you remember things easily without stress? 
            (a) Yes always
            (b) Not sure
            (c) Yes sometime
            (d) Not always
            (e) Not at all''',
          
    'question nine':
        '''Do you have control over your mood switch easily? 
            (a) Yes always
            (b) Not sure
            (c) Yes few time
            (d) Not easily
            (e) Not at all''',
           
    'question ten':
        '''Do things irritate you easily even things you naturally over look? 
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',
    
    'question eleven':
        '''Do you think people always misunderstand you or maybe they don’t even care?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',     
    
    'question twelve':
        '''Have you ever questioned your existence or think you are worth nothing?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',        
    
    'question thirteen':
        '''What is your personal hygiene like, has it changed over time? 
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',       
    
    'question fourteen':
        '''The things that you love to do normally, do you still find them interesting? 
            (a) Yes always
            (b) Not sure
            (c) Yes few times
            (d) Not easily
            (e) Not at all''',      
    
    'question fifteen':
        '''How active are you, do you do your daily activities without stress? 
            (a) Yes always
            (b) Not sure
            (c) Yes sometimes
            (d) Not easily
            (e) Not at all''',      
    
    'question sixteen':
        '''How is your feeding habits, do you still eat the way you were eating before?
            (a) Yes
            (b) Not sure
            (c) Yes few times
            (d) Not easily
            (e) Not at all''',       
    
    'question seventeen':
        '''Do you sleep well, how your sleeping habits is diferent from the way it before, either less or more?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Not easily
            (e) Yes always''',      
    
    'question eighteen':
        '''Do you feel restless and anxious?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Not easily
            (e) Yes always''',      
    
    'question nineteen':
        '''Do you have any physical pain in your body that you cannot explain?
            (a) Not at all
            (b) Not sure
            (c) Yes few times
            (d) Yes sometimes
            (e) Yes always''',        
    
    'question twenty':
        '''Have you ever blame God when you walk up in the morning for waking you?
            (a) Not at all,
            (b) Not sure,
            (c) Yes few times,
            (d) Yes sometimes,
            (e) Yes always''',
    
}

# final_answer = 0
# sex = input("Entre your gender(M/F): ".lower())
# agee = input("Entre your age (in figures): ")

# for question in questions:

#     print(question, '\n', questions[question], '\n')
    
#     answer = input('entre your answer: ')

#     if answer == 'b':
#         final_answer += 2
#     elif answer == 'c':
#         final_answer += 3
#     elif answer == 'd':
#         final_answer += 4
#     elif answer == 'e':
#         final_answer += 5
#     else:
#         pass
    
# print(f"your score is {final_answer}")

# # # to create new column
# with connection.cursor() as cursor:
#     sql = """insert into Depression_rate
#         (gender,  age, question, depression_percentage) 
#         values ("{}","{}","{}","{}")
#         """.format(sex,agee,questions[question],final_answer)

#     cursor.execute(sql)

#     connection.commit()

# if final_answer <= 30:
#     print("You score is  very low \n You are not depressed \n You need take live easy with yourself, see the good side of life and be happy ")

# elif final_answer > 30 and final_answer <= 50:
#     print("Your score is low \n You are probabily not depressed \n But you need to watch yourself, stay around people that see good in life")

# elif final_answer > 50 and final_answer < 70:
#     print("Your score is more than average \n You are probabily depressed \n You need to see a doctor")
    
# else:
#     print("Your grade is very high \n You need to see a doctor urgently before is too late")


# with connection.cursor() as cursor:
#     sql = """CREATE TABLE question_table
#     (id int NOT NULL KEY AUTO_INCREMENT,
#     question VARCHAR(100)) """

#     cursor.execute(sql)
#     connection.commit()

questionn = ['How do you fill about yourself presently?',
            'Do you think life has been so unfair with you?',
            'Are you confidence in yourself, do you believe in yourself?',
            'Do you have hidden pain your heart that you are living with and you are being reminded constantly in you heart?',
            'Do you try as much as possible to avoid social gathering and preferred to just stay alone?',
            'Do you blame yourselves easily even on things that are not directly your fault or those that you have little or no control over?',
            'Do you have problem thinking fast or concentrating easily?',
            'Do you remember things easily without stress?',
            'Do you have control over your mood switch easily?',
            'Do things irritate you easily even things you naturally over look?',
            'Do you think people always misunderstand you or maybe they don’t even care?',
            'Have you ever questioned your existence or think you are worth nothing?',
            'What is your personal hygiene like, has it changed over time?',
            'The things that you love to do normally, do you still find them interesting?',
            'How active are you, do you do your daily activities without stress?',
            'How is your feeding habits, do you still eat the way you were eating before?',
            'Do you sleep well, how your sleeping habits is diferent from the way it before, either less or more?',
            'Do you feel restless and anxious?',
            'Do you have any physical pain in your body that you cannot explain?',
            'Have you ever blame God when you walk up in the morning for waking you?']


# with connection.cursor() as cursor:
#     for q in questionn:
#         sql = """INSERT INTO question_table
#             (question) values (%s)"""

#     cursor.executemany(sql,questionn)

#     connection.commit()


# with connection.cursor() as cursor:
#     sql = """CREATE TABLE answer_table
#     (id int NOT NULL KEY AUTO_INCREMENT,
#     answer VARCHAR(1000)) """
#     cursor.execute(sql)
#     connection.commit()

answerr = ['Not at all',
            'Not sure',
            'Yes always',
            'Yes few times',
            'Not easily',
            'Yes sometimes',
            'Awesome',
            'Good',
            'Helpless',
            'Hopeless',
            'Miserable']



# with connection.cursor() as cursor:

#     sql = """INSERT INTO answer_table
#         (answer) 
#         values (%s)"""

#     cursor.executemany(sql,answerr)

#     connection.commit()

# with connection.cursor() as cursor:
#     sql = """CREATE TABLE q_a (quest_id INT(3) references question_table(id), answer_id INT(3) references answer_table(id)) """
#     cursor.execute(sql)
#     connection.commit()

# with connection.cursor() as cursor:
#     sql = """SELECT id from question_table where id = 1 """
#     cursor.execute(sql)
#     response = cursor.fetchall()

#     print(response)

#     sql = f"""SELECT answer_id from q_a where quest_id = {response[0]['id']} """
#     cursor.execute(sql)
#     answer_ids = cursor.fetchall()

#     print(answer_ids)

#     for answer in answer_ids:
#         sql = f"""SELECT answer from answer_table where id = {answer['answer_id']} """
#         cursor.execute(sql)
#         answer_text = cursor.fetchall()
#         print(answer_text)

# with connection.cursor() as cursor:
#     sql = """SELECT id from question_table"""
#     for question in sql:
#         cursor.execute(sql)
#         que = cursor.fetchall()
#         print(que)

# que = []
# ans = []
with connection.cursor() as cursor:
    for question in questions:
        sql = """SELECT question from question_table"""
        cursor.execute(sql)
        cursor.fetchall()

        que = """SELECT id from question_table"""
        cursor.execute(que)
        cursor.fetchall()

    for question in questions:
        will = questions[question]
        print(will)

    # for question in questions:
    # for question in questions:
        if sql in will:
            print(que)
            # que.append(question_table.id)
            # sql1 = f"""INSERT INTO q_a.question_id value {que}"""

        else:
            pass

        sqll = """SELECT answer from answer_table"""
        cursor.execute(sqll)
        cursor.fetchall()

        ans = """SELECT id from answer_table"""
        cursor.execute(ans)
        cursor.fetchall()
        # if sqll in question:
        #     print(ans)
        #     # ans.append(answer_table.id)
        #     # sql2 = f"""INSERT INTO q_a.answer_table value {ans}"""
        

    # cursor.executemany(sql1,sql2)
    # cursor.fetchall()

    # cursor.executemany(sql,sqll)
    # cursor.fetchall()





    # sql1 = """SELECT id FROM answer_table"""
    # cursor.execute(sql1)
    # response1 = cursor.fetchall()
    # print(response1)

    # sql = f"""SELECT answer_id from q_a where quest_id = {response[0]['id']} """
    # cursor.execute(sql)
    # answer_ids = cursor.fetchall()

    # print(answer_ids)

    # for answer in answer_ids:
    #     sql = f"""SELECT answer from answer_table where id = {answer['answer_id']} """
    #     cursor.execute(sql)
    #     answer_text = cursor.fetchall()
    #     print(answer_text)










