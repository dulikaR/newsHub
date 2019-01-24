# -*- coding: utf-8 -*-
from googletrans import Translator
import MySQLdb

# english 1-4  hiru 13-16  derana 25 - 28
# sinhala 5-8
# tamil 9-12
def channelLoop():
    channelNames=['sirasa','hiru','derana']
    for cNames in channelNames:
        start(cNames)


def start(cNames):
    result_set = []
    db = MySQLdb.connect( "localhost", "root", "", "newsapp" , charset='utf8' )
    cursor = db.cursor()
    result_set = []
    try:

        if (cNames == "sirasa"):
            cursor.execute("SELECT id, category, heading, content FROM " + cNames + " Where category IN ('1','2','3','4')" )  # NOT IN
            result_set = cursor.fetchall()
            db.commit()
        elif(cNames == "hiru"):
            cursor.execute("SELECT id, category, heading, content FROM " + cNames + " Where category IN ('13','14','15','16')" )  # NOT IN
            result_set = cursor.fetchall()
            db.commit()
        else:
            cursor.execute( "SELECT id, category, heading, content FROM "+cNames+" Where category IN ('25','26','27','28')" )  #NOT IN
            result_set = cursor.fetchall()
            db.commit()
    except:
        db.rollback()
        print "not working"

    for row in result_set:
            translation(cNames,row)



def translation(cNames,row):
    Header = ''
    Body = ''

    splitedHeader = row[2].split( ". " )
    splitedBody = row[3].split( ". " )

    translator = Translator()
    headerTranslations = translator.translate( splitedHeader , dest='si' )
    for translation in headerTranslations:
        Header+= translation.text + '. '

    bodyTranslations = translator.translate( splitedBody , dest='si' )
    for translation in bodyTranslations:
        Body += translation.text + '. '

    idNum = str(row[0])
    db = MySQLdb.connect( "localhost", "root", "", "newsapp", charset='utf8' )
    cursor = db.cursor()
    cursor.execute( "UPDATE "+cNames+" SET convertOne=%s, convertTwo=%s WHERE id=%s", (Header, Body, idNum) )
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    channelLoop()
