from flask import Flask, Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from app.module import dbModule
from app import issue, wc
import os
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

db_class = dbModule.Database()

title = 'RV Analysis - TEAMAX'

@app.route('/')
def main():
    return render_template('index.html', title=title)

@app.route('/searchingList', methods=['POST', 'GET'])
def serchingList(searching=None):
    if request.method == 'POST':
        searching = request.form['search']
        searching_db = "%" + searching + "%"
        sql     = "DROP TABLE searching_list"
        db_class.execute(sql)

        sql     = "CREATE TABLE searching_list as SELECT * FROM teamax.data_table \
                    WHERE brand LIKE %s OR model LIKE %s OR item_cate LIKE %s"
        db_class.execute(sql, (searching_db, searching_db, searching_db))

        sql     = "SELECT brand, item_cate, model, ROUND(AVG(score),2) as score FROM searching_list GROUP BY item_cate, brand, model"
        rows = db_class.executeAll(sql)

        return render_template('tables.html', searched_rows=rows, search=searching, title=title)
    
    else: 
        sql     = "SELECT brand, item_cate, model, ROUND(AVG(score),2) as score FROM data_table GROUP BY item_cate, brand, model"
        rows = db_class.executeAll(sql)
        return render_template('tables.html', searched_rows=rows)


def po_ne_values(list, values):
    for i in list:
        if i['po_ne'] == '긍정':
            values[0] = i['cnt']
        elif i['po_ne'] == '부정':
            values[1] = i['cnt']
        else:
            values[2] = i['cnt']


@app.route('/showCharts/<rowData>')
def showCharts(rowData):

    sql     = "SELECT * FROM searching_list WHERE model = %s"
    selected_rows = db_class.executeAll(sql, rowData)
    brand = selected_rows[0]['brand']
    model = selected_rows[0]['model']

    # 평점 빈도수 분석
    score_sql   = "SELECT score, COUNT(*) as cnt_score FROM searching_list WHERE model = %s GROUP BY score ORDER BY score ASC"
    score_list = db_class.executeAll(score_sql, rowData)
    score_lists = []
    score_values = []
    for i in range(len(score_list)):
        score_lists.append(score_list[i]['score'])
        score_values.append(score_list[i]['cnt_score'])

    # 배송, 상품, 서비스 카테고리별 긍부정
    deliver_sql = "SELECT deliver as po_ne, COUNT(*) as cnt FROM searching_list WHERE model = %s GROUP BY deliver"
    deliver_list = db_class.executeAll(deliver_sql, rowData)
    deliver_values = [0,0,0]

    product_sql = "SELECT product as po_ne, COUNT(*) as cnt FROM searching_list WHERE model = %s GROUP BY product"
    product_list = db_class.executeAll(product_sql, rowData)
    product_values = [0,0,0]

    service_sql = "SELECT service as po_ne, COUNT(*) as cnt FROM searching_list WHERE model = %s GROUP BY service"
    service_list = db_class.executeAll(service_sql, rowData)
    service_values = [0,0,0]

    po_ne_values(deliver_list, deliver_values)
    po_ne_values(product_list, product_values)
    po_ne_values(service_list, service_values)

    #배송, 상품, 서비스 이슈 분석
    issue_sql = "SELECT review FROM searching_list WHERE model = %s"
    issue_list = db_class.executeAll(issue_sql, rowData)
    review_list = []
    for i in range(len(issue_list)):
        review_list.append(issue_list[i]['review'])

    def file_remove(file):
        if os.path.isfile(file):
            os.remove(file)
    file_remove("app/dict/ne_issue_d.txt")
    file_remove("app/dict/ne_issue_p.txt")
    file_remove("app/dict/ne_issue_s.txt")
    
    issue.main(review_list)

    #배송, 상품, 서비스 워드클라우드 이미지 출력
    wc.wc("app/dict/ne_issue_d.txt","app/static/assets/img/d_wc.png")
    wc.wc("app/dict/ne_issue_p.txt","app/static/assets/img/p_wc.png")
    wc.wc("app/dict/ne_issue_s.txt","app/static/assets/img/s_wc.png")
    return render_template('charts.html', title=title, selected_rows=selected_rows, selected_brand=brand, selected_model=model, \
        score_lists=score_lists, score_values=score_values, deliver_values=deliver_values, product_values=product_values, service_values=service_values)        

