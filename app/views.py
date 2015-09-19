from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .forms import enterinForm,questionForm,answerForm
from .models import User, Post
import MySQLdb
from datetime import timedelta
from flask import session
import time
import ast
import datetime




@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/archive')
def archive():
    ippo=datetime.datetime.now()
    ippoday=int(ippo.day)
    ippomonth=int(ippo.month)
    ippotime=int(ippo.hour)
    dbql = MySQLdb.connect("localhost","root","*****","*****")
    cursor = dbql.cursor()
    fsql = """SELECT * FROM xxxxxx """
    cursor.execute(fsql)
    dataofv = cursor.fetchall()
    arr = []
    for ch in dataofv:
        aat = str(ch[6])
        aat=aat.split(" ")
        aat=aat[0].split("-")

        if ippoday==int(aat[2]) and ippomonth==int(aat[1]) and ippotime<21:
            emdict = {}
            emdict['ahead'] = str(ch[5])
            emdict['acreator'] = str(ch[1])
            emdict['aquest'] = str(ch[2])
            emdict['aqa'] = "WAIT TILL 9pm IST FOR ANSWERS"
            vartime = str(ch[6])
            vartime = vartime.split(" ")
            emdict['atime'] = str(vartime[0])
            arr.append(emdict)
        else:
            emdict = {}
            emdict['ahead'] = str(ch[5])
            emdict['acreator'] = str(ch[1])
            emdict['aquest'] = str(ch[2])
            emdict['aqa'] = str(ch[3])
            vartime = str(ch[6])
            vartime = vartime.split(" ")
            emdict['atime'] = str(vartime[0])
            arr.append(emdict)
    arr.reverse()
    dbql.commit()
    dbql.close()
    return render_template('archive.html',arch = arr)



@app.route('/creator', methods=['GET', 'POST'])
def creator():
    t = datetime.datetime.now()
    strt = str(t)
    formlogin = enterinForm()
    formquestion = questionForm()
    dbql = MySQLdb.connect("localhost","root","*****","*****")
    cursor = dbql.cursor()
    if 'topass' in session:
        if time.time()>session['logtime']+900:
            session.pop('topass', None)
            return render_template('creator.html', form = formlogin)
        if request.method == 'POST':
            #should enter the question in the db here
            #flash tat it was a success
            sql = """INSERT INTO xxxxxx (***,***,***,***,***) VALUES(%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(formquestion.creator.data,formquestion.originalquestion.data,formquestion.originalanswer.data,formquestion.creator1.data,strt))
            dbql.commit()
            dbql.close()
            flash("You have successfully created today's question and its answers")
            session.pop('topass', None)
            return render_template('home.html')
        if request.method == 'GET':
            if time.time()>session['logtime']+900:
                session.pop('topass', None)
                return render_template('creator.html', form = formlogin)
            return render_template('creator.html', form = formquestion)

    else:
        if request.method == 'POST':
            if formlogin.validate() == False:
                return render_template('creator.html',form = formlogin)
            else:
                session['topass']="I'm rock"
                session['logtime'] = time.time()
                return render_template('creator.html', form = formquestion)
        elif request.method == 'GET':
            return render_template('creator.html', form = formlogin)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def replies():

    formanswer = answerForm()
    dbql = MySQLdb.connect("localhost","root","*****","*****")
    cursor = dbql.cursor()
    if request.method == 'POST':
        #flash tat it was a success
        fsql = """SELECT * FROM xxxxxx ORDER BY sno DESC LIMIT 1"""
        cursor.execute(fsql)
        dataofv = cursor.fetchall()
        allanswers = ""
        qa = ""
        head = ""
        for ch in dataofv:
            allanswers = ch[4]
            qa = ch[3]
            head = ch[5]
        #needs to be updated
        if allanswers:
            #already some have answered
            allanswers = ast.literal_eval(allanswers)
            allanswers[formanswer.creator.data] = formanswer.originalquestion.data
            allanswers = str(allanswers)
            sql = """UPDATE xxxxxx SET answers = %s WHERE sno ORDER BY sno DESC LIMIT 1"""
            # needs to be updated
            cursor.execute(sql,allanswers)
            dbql.commit()
            dbql.close()
        else:
            #no one has answered so far
            firstanswer = {}
            firstanswer[formanswer.creator.data] = formanswer.originalquestion.data
            firstanswer = str(firstanswer)
            sql = """UPDATE xxxxxx SET answers = %s WHERE sno ORDER BY sno DESC LIMIT 1"""
            # needs to be updated
            cursor.execute(sql,firstanswer)
            dbql.commit()
            dbql.close()
        flash("Your answers")
        ca = []
        ca = formanswer.originalquestion.data.split('\n')
        act = []
        act = qa.split("\n")
        for e in ca:
            flash(e)
        flash("###############")
        flash("Actual answers")

        for a in act:
            flash(a)
        flash("###############")

        questions = ""
        return render_template('replies.html', form = formanswer,questions=questions)
    if request.method == 'GET':
        fsql = """SELECT * FROM xxxxxx ORDER BY sno DESC LIMIT 1"""
        cursor.execute(fsql)
        dataofv = cursor.fetchall()
        questions = ""
        head = ""
        for ch in dataofv:
            questions = ch[2]
            head = ch[5]

        questlist = []
        questlist = questions.split('\n')

        return render_template('replies.html', form = formanswer,questions = questlist,head = head)



@app.route('/answers', methods=['GET', 'POST'])
def answers():
    formlogin = enterinForm()

    dbql = MySQLdb.connect("localhost","root","*****","*****")
    cursor = dbql.cursor()
    if 'topass' in session:
        if time.time()>session['logtime']+120:
            session.pop('topass', None)
            return render_template('creator.html', form = formlogin)
        if request.method == 'POST':
            #retriving the last record
            sql = """SELECT * FROM xxxxxx ORDER BY sno DESC LIMIT 1"""
            cursor.execute(sql)
            dataofv = cursor.fetchall()
            answers = ""
            for ch in dataofv:
                answers = ch[4]
	    if answers:
            	answers = ast.literal_eval(answers)
	    else:
		answers = {'No one has answered':'so far'}


            dbql.commit()
            dbql.close()

            return render_template('answers.html', answers = answers)
        if request.method == 'GET':
            if time.time()>session['logtime']+120:
                session.pop('topass', None)
                return render_template('answers.html', form = formlogin)
            sql = """SELECT * FROM xxxxxx ORDER BY sno DESC LIMIT 1"""
            cursor.execute(sql)
            dataofv = cursor.fetchall()
            answers = ""
            for ch in dataofv:
                answers = ch[4]
	    if answers:
         	answers = ast.literal_eval(answers)
	    else:
		answers = {'No one has answered':'so far'}


            dbql.commit()
            dbql.close()
            return render_template('answers.html', answers = answers)

    else:
        if request.method == 'POST':
            if formlogin.validate() == False:
                return render_template('answers.html',form = formlogin)
            else:
                session['topass']="I'm rock"
                session['logtime'] = time.time()
                sql = """SELECT * FROM xxxxxx ORDER BY sno DESC LIMIT 1"""
                cursor.execute(sql)
                dataofv = cursor.fetchall()
                answers = ""
                for ch in dataofv:
                    answers = ch[4]
		if answers:
			#only if answers is valid, what if no answers so far
                	answers = ast.literal_eval(answers)
		else:
			answers = {'No one has answered':'so far'}



                dbql.commit()
                dbql.close()
                return render_template('answers.html', answers = answers)
        elif request.method == 'GET':
            return render_template('answers.html', form = formlogin)
