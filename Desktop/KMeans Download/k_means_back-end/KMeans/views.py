from django.http import HttpResponse, StreamingHttpResponse
from sklearn.cluster import KMeans as kmeans
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pandas as pd
import json
from django.utils.encoding import escape_uri_path


def KMeans_upload(request):
    UploadFile = request.FILES.get("file")
    #UploadFile = json.loads(request.body)
    print(UploadFile)
    # 存储文件到本地
    path = default_storage.save('FileStorage/'+UploadFile.name, ContentFile(UploadFile.read()))
    return HttpResponse(request.method)


def KMeans_run(request):
    url = 'Joyce'
    # 以json数据返回到前端
    requestData = str(request.body)

    data = requestData.replace("{", "")
    data = data.replace("}", "")
    data = data.replace(" ", "")
    data = data.replace('"', "")
    data = data.replace("b'", "")
    print(data)

    dataList1 = data.split(",")
    resultList, resultName = [], []
    for i in dataList1:
        tem_list = i.split(":")
        resultName.append(tem_list[0])
        if (tem_list[0] == 'activeStep' or tem_list[0] == 'n_clusters' or tem_list[0] == 'max_iter' or  tem_list[0] == 'n_init'):
            resultList.append(int(tem_list[1]))
        elif(  tem_list[0] =='algorithm' or tem_list[0] =='filename'):
            resultList.append(tem_list[1])
        elif (tem_list[0] == 'precompute_distances'):
            if(tem_list[1]=="True"):
                resultList.append(True)
            elif(tem_list[1]=="False"):
                resultList.append(False)
            else:
                resultList.append(tem_list[1])
        elif(tem_list[0] == 'tol'):
            resultList.append(float(tem_list[1]))


    # resultName == > ['activeStep', 'n_clusters', 'n_init', 'max_iter', 'tol', 'precompute_distances', 'algorithm', 'success', 'filename', 'url']
    print("resultName===>", resultName)
    # resultName == > [1.0, 4.0, 10.0, 300.0, 0.0001, 'Auto', 'Auto', '\\xe6\\x9c\\x80\\xe6\\x96\\xb0\\xe6\\x89\\x80\\xe6\\x9c\\x89\\xe8\\x81\\x9a\\xe7\\xb1\\xbb\\xe5\\x8f\\x8a\\xe8\\xa1\\xa8\\xe6\\xa0\\xbc2(1).xls']
    print("resultList===>", resultList)

    N_clusters, N_init, Max_iter, Tol, Precompute_distances, Algorithm = resultList[1], resultList[2], resultList[3], resultList[4], resultList[5], resultList[6]
    fileName = resultList[7]

    path = r'C:\Users\张瘦瘦\PycharmProjects\KMeans_React\FileStorage\DataKMeans.xls'
    print(path)
    df1 = pd.read_excel(path, index_col=0)
    y_pred = kmeans(n_clusters=N_clusters, n_init=N_init, max_iter=Max_iter, tol=Tol,
                    precompute_distances=Precompute_distances, algorithm=Algorithm).fit_predict(df1)

    for i in df1.index:
        df1.loc[i, "clusters"] = y_pred[i - 1]

    print(df1)
    df1.to_excel(r'C:\Users\张瘦瘦\PycharmProjects\PythonTest\Data_kmeans_modify.xls')
    return HttpResponse('success')

def downloadFile(request):
    file = open(r'C:\Users\张瘦瘦\PycharmProjects\PythonTest\Data_kmeans_modify.xls', 'r')
    filename = 'Data_kmeans_modify.xls'
    response = HttpResponse(file)
    response['Content-Type'] = "application/vnd.ms-excel"  # 设置头信息，告诉浏览器这是个文件
    response["Content-Disposition"] = 'attachment;filename=Data_kmeans_modify.xls'
    return response