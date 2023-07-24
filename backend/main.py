import random
from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
import time


# https://stackoverflow.com/questions/44209978/serving-a-front-end-created-with-create-react-app-with-flask
app = Flask(__name__, static_folder="../frontend/reactfrontend/build/static", template_folder="../frontend/reactfrontend/build"
            )


# @app.route("/")
# def hello():
#     return render_template('index.html')


# @app.route('/codescreen')
# def toMain():
#     return redirect('/')

@app.route("/")
def hello():
    return 'i am working'


@app.route('/api/test')
def test():
    return 'test is a go'


@app.route("/api/getTests", methods=['POST'])
def getTests():
    print(request.get_json())

    with sqlite3.connect('racing.db') as db:
        cursor = db.cursor()
        gamecode = str(request.get_json()['gamecode'])
        res = cursor.execute(
            'SELECT input,output FROM tblTestInput,tblPlayingGroup WHERE tblPlayingGroup.joinCode=? AND tblPlayingGroup.questionID = tblTestInput.questionID', (gamecode,))
        res = list(res)[0]
        print(res)
        return jsonify({'input': res[0], 'output': res[-1]})


def getGameData(gamecode):
    print('getting ping')

    with sqlite3.connect('racing.db') as db:
        cursor = db.cursor()
        print('GAME CODE: ', gamecode)
        # res = cursor.execute(
        #     'SELECT questionTitle , questionDescription FROM tblPlayingGroup , tblQuestion WHERE tblPlayingGroup.joinCode=? AND tblQuestion.questionID = tblPlayingGroup.questionID AND tblPlayingGroup.finished = 0', (str(gamecode),))
        resItter = cursor.execute(
            'SELECT questionTitle, questionDescription FROM tblQuestion, tblPlayingGroup WHERE tblQuestion.questionID = tblPlayingGroup.questionID AND tblPlayingGroup.joinCode = ? AND tblPlayingGroup.finished=0', (gamecode,))
        resBig = list(resItter)

        testInputs = list(cursor.execute(
            'SELECT input, output FROM tblTestInput, tblPlayingGroup WHERE tblTestInput.questionID = tblPlayingGroup.questionID AND tblPlayingGroup.joinCode = ?', (gamecode,)))
        print('test inps ', testInputs)
        inps = []
        outs = []
        #res = list(res)[0]
        for case in testInputs:
            inps.append(case[0])
            outs.append(case[-1])

        try:
            res = resBig[0]
            print('res', res)

            return {'title': res[0], 'desc': res[1], 'valid': True, 'gamecode': gamecode, 'testInputs': inps, 'testOutputs': outs}
        except Exception as e:
            print(e)
            return {'title': '', 'desc': '', 'valid': False, 'testInputs': [], 'testOutputs': []}


@app.route("/api/registerPlayer", methods=['PUT'])
def registerPlayer():

    uName = request.get_json()['username']
    gamecode = request.get_json()['gamecode']
    gameData = getGameData(gamecode)
    if gameData['valid'] == False:
        return jsonify({'error': 'invalid gamepin', 'gamedata': ''})
    with sqlite3.connect('racing.db') as db:
        cursor = db.cursor()
        groupID = cursor.execute(
            'SELECT groupID FROM tblPlayingGroup WHERE joinCode =? AND finished = 0', (gamecode, ))
        groupID = list(groupID)[0][0]

        print('GROUP ID', groupID)

        if groupID == []:
            # error here, there isnt a game with that joincode
            return jsonify({'error': 'Invalid game join code, please enter a valid code.', 'gamedata': ''})
        duplicateNames = list(cursor.execute(
            'SELECT displayName FROM tblPlayer WHERE groupID = ? AND displayName = ?', (groupID, uName, )))
        # print(duplicateNames)
        # print(duplicateNames[0], len(duplicateNames[0]))
        try:
            nameList = duplicateNames[0]
        except:
            nameList = []
        if len(nameList) > 0:
            # duplicate name
            print('backend sending errors')
            return jsonify({'error': 'Name is already in use in this group, please chose another one.', 'gamedata': ''})
        cursor.execute(
            'INSERT INTO tblPlayer (displayName,groupID) VALUES (?,?)', (uName, groupID))
    return jsonify({'error': '', 'gamedata': gameData})


@app.route('/api/getAllQuestions', methods=['POST'])
def getAllQuestions():
    with sqlite3.connect('racing.db') as db:
        cursor = db.cursor()
        questionData = cursor.execute('SELECT * FROM tblQuestion')
        # print(list(questionData))

        return jsonify({'questions': list(questionData)})


@app.route('/api/createGame', methods=['POST'])
def createGame():
    questionID = request.get_json()['questionid']
    joinCodeUnique = False
    while joinCodeUnique == False:
        joinCode = ''
        for _ in range(6):
            joinCode += str(random.randint(0, 9))
        with sqlite3.connect('racing.db') as db:
            cursor = db.cursor()
            res = list(cursor.execute(
                'SELECT * FROM tblPlayingGroup WHERE joinCode = ?', (joinCode,)))
            if len(res) == 0:
                joinCodeUnique = True
                cursor.execute('INSERT INTO tblPlayingGroup (timestampStarted,finished,joinCode,questionID) VALUES (?,?,?,?)',
                               (time.time(), 0, joinCode, questionID))

    return jsonify({'joinCode': joinCode})


print('Starting Flask!')

app.debug = True
app.run(host='0.0.0.0')
