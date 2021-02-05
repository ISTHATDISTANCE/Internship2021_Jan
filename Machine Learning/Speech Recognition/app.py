from flask import Flask, render_template, request
import pymysql
# import base64
# import MySQLdb

app = Flask(__name__)
db = pymysql.connect(host='localhost', user='root', password='Lt@6890838', database='ass')

num = 1

@app.route('/')
def hello_world():
    return render_template('video.html')


@app.route('/save', methods=['GET', 'POST'])
def save():
    aud = request.files['wave_file']
    file_name = "Record" + str(num) + ".mp3"
    # aud.save('data/test.mp3')
    aud.seek(0)
    aud_bytes = aud.read()
    print(len(aud_bytes))
    # aud_b64 = base64.b64encode(aud_bytes)
    # print(len(aud_b64))
    aud_hex = ''.join(['%02x' % x for x in aud_bytes])
    # print(aud_hex)
    cursor = db.cursor()
    sql = f"""insert into audio_files (file_name, content) values ('{file_name}', 0x%s);"""
    print(len(sql % aud_hex))
    cursor.execute(
        sql % aud_hex
    )
    db.commit()
    cursor.close()
    return 'done'


@app.route('/download')
def download():
    cursor = db.cursor()
    sql = f"""select max(id), content from audio_files"""
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "result": str(res[0][1])
    }
    # print(res)
    return data

if __name__ == '__main__':
    app.run()
