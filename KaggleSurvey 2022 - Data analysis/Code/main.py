import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def PL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('PL.png')

def IDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('IDE.png')

def OP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x_to_p, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('OP.png')

def VP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('VP.png')

def ML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('ML.png')

def CV(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('CV.png')

def NLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithm libraries popularity in top 2 most participated countries ")

    c_i = 0
    c_j = 0

    for i in data['country'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['country'] == i]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('NLP.png')

#yearly

def YPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']


        normalizers = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_python = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_r = [len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)])/ normalizers[i] for i,ye in enumerate(years)]
        y_sql = [len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_c = [len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_java = [len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_julia = [len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'Python')
        axes[c_i].plot(years, y_r, label='R')
        axes[c_i].plot(years, y_sql, label = 'SQL')
        axes[c_i].plot(years, y_c, label='C')
        axes[c_i].plot( years, y_java, label = 'Java')
        axes[c_i].plot(years, y_javascript, label='Javascript')
        axes[c_i].plot(years, y_julia, label='Julia')
        axes[c_i].plot( years,  y_matlabcode, label = 'Matlab')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    #plt.show()
    plt.savefig('YPL.png')

def YIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']

        normalizers = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_jupyter = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_RStudio = [len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_Pycharm = [len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_visualStudio = [len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_spyder = [len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_matlab = [len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_vimemacs = [len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_jupyter, label = 'jupyter')
        axes[c_i].plot(years, y_RStudio, label='RStudio')
        axes[c_i].plot(years, y_Pycharm, label = 'Pycharm')
        axes[c_i].plot(years, y_visualStudio, label='visualStudio')
        axes[c_i].plot( years, y_spyder, label = 'Java')
        axes[c_i].plot(years, y_matlab, label='spyder')
        axes[c_i].plot( years, y_vimemacs, label = 'vim/emacs')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YIDE.png')

def YOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']

        normalizers = [len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_coursera = [len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_udacity = [len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_udemy = [len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_kaggleLearn = [len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_edx = [len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_linkedinLearning = [len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_universityCourses = [len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_coursera, label = 'coursera')
        axes[c_i].plot(years, y_udacity, label='udacity')
        axes[c_i].plot(years, y_udemy, label = 'udemy')
        axes[c_i].plot(years, y_kaggleLearn, label='kaggleLearn')
        axes[c_i].plot( years, y_edx, label = 'edx')
        axes[c_i].plot(years, y_linkedinLearning, label='linkedinLearning')
        axes[c_i].plot( years, y_universityCourses, label = 'universityCourses')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YOP.png')

def YVP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']

        normalizers = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_matplotlib = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_altair = [len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'matplotlib')
        axes[c_i].plot(years, y_seaborn, label='seaborn')
        axes[c_i].plot(years, y_plotly, label = 'plotly')
        axes[c_i].plot(years, y_altair, label='altair')
        axes[c_i].plot( years, y_shiny, label = 'shiny')
        axes[c_i].plot(years, y_geoplotlib, label='geoplotlib')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YVP.png')

def YML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']


        normalizers = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_python = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_r = [len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_sql = [len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_c = [len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_java = [len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_julia = [len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_rnn = [len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_trans = [len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'linear')
        axes[c_i].plot(years, y_r, label='trees')
        axes[c_i].plot(years, y_sql, label = 'GBM')
        axes[c_i].plot(years, y_c, label='bayesian')
        axes[c_i].plot( years, y_java, label = 'evolutionary')
        axes[c_i].plot(years, y_javascript, label='dnn')
        axes[c_i].plot( years, y_julia, label = 'cnn')
        axes[c_i].plot(years, y_matlabcode, label='gan')
        axes[c_i].plot( years,  y_rnn, label = 'rnn')
        axes[c_i].plot(years, y_trans, label='transformer')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YML.png')

def YCV(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']

        normalizers = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'generalVideoTools')
        axes[c_i].plot(years, y_seaborn, label='imageSegmentation')
        axes[c_i].plot(years, y_plotly, label = 'objectDetection')
        axes[c_i].plot(years, y_altair, label='imageClassification')
        axes[c_i].plot( years, y_shiny, label = 'visionTransformers')
        axes[c_i].plot(years, y_geoplotlib, label='generativeNetworks')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YCV.png')

def YNLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithms popularity in top 2 most participated countries per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['country'].unique():

        d = data[data['country'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']


        normalizers = [len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_matplotlib = [len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_matplotlib, label = 'wordEmbeding')
        axes[c_i].plot(years, y_seaborn, label='encoderDecoder')
        axes[c_i].plot(years, y_plotly, label = 'contextualizedEmbedding')
        axes[c_i].plot(years, y_altair, label='transformerLanguage')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('YNLP.png')

#Male/Female

def MFPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity among genders")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFPL.png')

def MFIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity among genders ")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFIDE.png')

def MFOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity among genders ")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x_to_p, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFOP.png')

def MFVP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity among genders ")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFVP.png')

def MFML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity among genders ")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFML.png')

def MFCV(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity among genders ")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFCV.png')

def MFNLP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP libraries popularity among genders")

    c_i = 0
    c_j = 0

    for i in data['gender'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['gender'] == i]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('MFNLP.png')

#Male/Female yearly

def MFYPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']

        normalizers = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_python = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_r = [len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)])/ normalizers[i] for i,ye in enumerate(years)]
        y_sql = [len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_c = [len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_java = [len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_julia = [len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'Python')
        axes[c_i].plot(years, y_r, label='R')
        axes[c_i].plot(years, y_sql, label = 'SQL')
        axes[c_i].plot(years, y_c, label='C')
        axes[c_i].plot( years, y_java, label = 'Java')
        axes[c_i].plot(years, y_javascript, label='Javascript')
        axes[c_i].plot( years, y_python, label = 'Python')
        axes[c_i].plot(years, y_julia, label='Julia')
        axes[c_i].plot( years,  y_matlabcode, label = 'Matlab')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYPL.png')

def MFYIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']

        normalizers = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_jupyter = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_RStudio = [len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_Pycharm = [len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_visualStudio = [
            len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_spyder = [len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_matlab = [len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_vimemacs = [
            len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]

        axes[c_i].plot(years, y_jupyter, label = 'jupyter')
        axes[c_i].plot(years, y_RStudio, label='RStudio')
        axes[c_i].plot(years, y_Pycharm, label = 'Pycharm')
        axes[c_i].plot(years, y_visualStudio, label='visualStudio')
        axes[c_i].plot( years, y_spyder, label = 'Java')
        axes[c_i].plot(years, y_matlab, label='spyder')
        axes[c_i].plot( years, y_vimemacs, label = 'vim/emacs')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYIDE.png')

def MFYOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']

        normalizers = [len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_coursera = [
            len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]
        y_udacity = [len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_udemy = [len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                   i, ye in enumerate(years)]
        y_kaggleLearn = [
            len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_edx = [len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i, ye in
                 enumerate(years)]
        y_linkedinLearning = [
            len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]
        y_universityCourses = [
            len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]

        axes[c_i].plot(years, y_coursera, label = 'coursera')
        axes[c_i].plot(years, y_udacity, label='udacity')
        axes[c_i].plot(years, y_udemy, label = 'udemy')
        axes[c_i].plot(years, y_kaggleLearn, label='kaggleLearn')
        axes[c_i].plot( years, y_edx, label = 'edx')
        axes[c_i].plot(years, y_linkedinLearning, label='linkedinLearning')
        axes[c_i].plot( years, y_universityCourses, label = 'universityCourses')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYOP.png')

def MFYVP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']

        normalizers = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_matplotlib = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_altair = [len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'matplotlib')
        axes[c_i].plot(years, y_seaborn, label='seaborn')
        axes[c_i].plot(years, y_plotly, label = 'plotly')
        axes[c_i].plot(years, y_altair, label='altair')
        axes[c_i].plot( years, y_shiny, label = 'shiny')
        axes[c_i].plot(years, y_geoplotlib, label='geoplotlib')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYVP.png')

def MFYML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']

        normalizers = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_python = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_r = [len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_sql = [len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_c = [len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_java = [
            len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_julia = [len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_rnn = [len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_trans = [
            len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'linear')
        axes[c_i].plot(years, y_r, label='trees')
        axes[c_i].plot(years, y_sql, label = 'GBM')
        axes[c_i].plot(years, y_c, label='bayesian')
        axes[c_i].plot( years, y_java, label = 'evolutionary')
        axes[c_i].plot(years, y_javascript, label='dnn')
        axes[c_i].plot( years, y_julia, label = 'cnn')
        axes[c_i].plot(years, y_matlabcode, label='gan')
        axes[c_i].plot( years,  y_rnn, label = 'rnn')
        axes[c_i].plot(years, y_trans, label='transformer')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYML.png')

def MFYCV(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']

        normalizers = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_matplotlib, label = 'generalVideoTools')
        axes[c_i].plot(years, y_seaborn, label='imageSegmentation')
        axes[c_i].plot(years, y_plotly, label = 'objectDetection')
        axes[c_i].plot(years, y_altair, label='imageClassification')
        axes[c_i].plot( years, y_shiny, label = 'visionTransformers')
        axes[c_i].plot(years, y_geoplotlib, label='generativeNetworks')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYCV.png')

def MFYNLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithms popularity among genders per year")

    y = []
    c_i = 0
    c_j = 0
    for i in data['gender'].unique():

        d = data[data['gender'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']
        normalizers = [len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [
            len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) /
                     max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                    d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [
            len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (d['year'] == ye)]) /
            max(1,normalizers[i]) for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_matplotlib, label = 'wordEmbeding')
        axes[c_i].plot(years, y_seaborn, label='encoderDecoder')
        axes[c_i].plot(years, y_plotly, label = 'contextualizedEmbedding')
        axes[c_i].plot(years, y_altair, label='transformerLanguage')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('MFYNLP.png')

#title

def TPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TPL.png')

def TIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TIDE.png')

def TOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x_to_p, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TOP.png')

def TVP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TVP.png')

def TML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TML.png')

def TCV(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TCV.png')

def TNLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithm libraries popularity")

    c_i = 0
    c_j = 0

    for i in data['job_title'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['job_title'] == i]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('TNLP.png')

#yearly

def TYPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']

        normalizers = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_python = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_r = [len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)])/ normalizers[i] for i,ye in enumerate(years)]
        y_sql = [len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_c = [len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_java = [len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_julia = [len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'Python')
        axes[c_i].plot(years, y_r, label='R')
        axes[c_i].plot(years, y_sql, label = 'SQL')
        axes[c_i].plot(years, y_c, label='C')
        axes[c_i].plot( years, y_java, label = 'Java')
        axes[c_i].plot(years, y_javascript, label='Javascript')
        axes[c_i].plot(years, y_julia, label='Julia')
        axes[c_i].plot( years,  y_matlabcode, label = 'Matlab')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYPL.png')

def TYIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']

        normalizers = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_jupyter = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_RStudio = [len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_Pycharm = [len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_visualStudio = [
            len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_spyder = [len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_matlab = [len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_vimemacs = [
            len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]

        axes[c_i].plot(years, y_jupyter, label = 'jupyter')
        axes[c_i].plot(years, y_RStudio, label='RStudio')
        axes[c_i].plot(years, y_Pycharm, label = 'Pycharm')
        axes[c_i].plot(years, y_visualStudio, label='visualStudio')
        axes[c_i].plot( years, y_spyder, label = 'Java')
        axes[c_i].plot(years, y_matlab, label='spyder')
        axes[c_i].plot( years, y_vimemacs, label = 'vim/emacs')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYIDE.png')

def TYOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']

        normalizers = [len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_coursera = [
            len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]
        y_udacity = [len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_udemy = [len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                   i, ye in enumerate(years)]
        y_kaggleLearn = [
            len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_edx = [len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i, ye in
                 enumerate(years)]
        y_linkedinLearning = [
            len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]
        y_universityCourses = [
            len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]

        axes[c_i].plot(years, y_coursera, label = 'coursera')
        axes[c_i].plot(years, y_udacity, label='udacity')
        axes[c_i].plot(years, y_udemy, label = 'udemy')
        axes[c_i].plot(years, y_kaggleLearn, label='kaggleLearn')
        axes[c_i].plot( years, y_edx, label = 'edx')
        axes[c_i].plot(years, y_linkedinLearning, label='linkedinLearning')
        axes[c_i].plot( years, y_universityCourses, label = 'universityCourses')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYOP.png')

def TYVP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']

        normalizers = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_matplotlib = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_altair = [len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'matplotlib')
        axes[c_i].plot(years, y_seaborn, label='seaborn')
        axes[c_i].plot(years, y_plotly, label = 'plotly')
        axes[c_i].plot(years, y_altair, label='altair')
        axes[c_i].plot( years, y_shiny, label = 'shiny')
        axes[c_i].plot(years, y_geoplotlib, label='geoplotlib')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYVP.png')

def TYML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']

        normalizers = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_python = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_r = [len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_sql = [len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_c = [len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_java = [
            len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_julia = [len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_rnn = [len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_trans = [
            len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'linear')
        axes[c_i].plot(years, y_r, label='trees')
        axes[c_i].plot(years, y_sql, label = 'GBM')
        axes[c_i].plot(years, y_c, label='bayesian')
        axes[c_i].plot( years, y_java, label = 'evolutionary')
        axes[c_i].plot(years, y_javascript, label='dnn')
        axes[c_i].plot( years, y_julia, label = 'cnn')
        axes[c_i].plot(years, y_matlabcode, label='gan')
        axes[c_i].plot( years,  y_rnn, label = 'rnn')
        axes[c_i].plot(years, y_trans, label='transformer')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYML.png')

def TYCV(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']

        normalizers = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) /max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)]) /max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'generalVideoTools')
        axes[c_i].plot(years, y_seaborn, label='imageSegmentation')
        axes[c_i].plot(years, y_plotly, label = 'objectDetection')
        axes[c_i].plot(years, y_altair, label='imageClassification')
        axes[c_i].plot( years, y_shiny, label = 'visionTransformers')
        axes[c_i].plot(years, y_geoplotlib, label='generativeNetworks')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYCV.png')

def TYNLP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithms popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['job_title'].unique():

        d = data[data['job_title'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']

        normalizers = [len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [
            len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) /
                     max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                    d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [
            len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (d['year'] == ye)]) /
            max(1,normalizers[i]) for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_matplotlib, label = 'wordEmbeding')
        axes[c_i].plot(years, y_seaborn, label='encoderDecoder')
        axes[c_i].plot(years, y_plotly, label = 'contextualizedEmbedding')
        axes[c_i].plot(years, y_altair, label='transformerLanguage')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('TYNLP.png')


#education

def EPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('EPL.png')

def EIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('EIDE.png')

def EOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x_to_p, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('EOP.png')

def EVP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('EVP.png')

def EML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('EML.png')

def ECV(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('ECV.png')

def ENLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithm libraries popularity ")

    c_i = 0
    c_j = 0

    for i in data['formal_education'].unique():

        new_d = pd.DataFrame(columns = ['x', 'y' , 'country'])

        d = data[data['formal_education'] == i]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']
        #x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']
        y = [len(d[(d[p] != -1) & (d[p].isna() == False)]) for p in x]
        sns.barplot(ax = axes[c_i], x = x, y = y).set(title = f'{i}', xlabel = 'Langauge', ylabel = 'Count')
        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1
    plt.savefig('ENLP.png')

#yearly

def EYPL(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Programming langauge popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['python', 'R', 'sql', 'C/C++', 'Java', 'JavaScript', 'Julia', 'MatlabCode']

        normalizers = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_python = [len(d[(d['python'] != -1) & (d['python'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_r = [len(d[(d['R'] != -1) & (d['R'].isna() == False) & (d['year'] == ye)])/ normalizers[i] for i,ye in enumerate(years)]
        y_sql = [len(d[(d['sql'] != -1) & (d['sql'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_c = [len(d[(d['C/C++'] != -1) & (d['C/C++'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_java = [len(d[(d['Java'] != -1) & (d['Java'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['JavaScript'] != -1) & (d['JavaScript'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_julia = [len(d[(d['Julia'] != -1) & (d['Julia'].isna() == False) & (d['year'] == ye)])  / normalizers[i] for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['MatlabCode'] != -1) & (d['MatlabCode'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'Python')
        axes[c_i].plot(years, y_r, label='R')
        axes[c_i].plot(years, y_sql, label = 'SQL')
        axes[c_i].plot(years, y_c, label='C')
        axes[c_i].plot( years, y_java, label = 'Java')
        axes[c_i].plot(years, y_javascript, label='Javascript')
        axes[c_i].plot(years, y_julia, label='Julia')
        axes[c_i].plot( years,  y_matlabcode, label = 'Matlab')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYPL.png')

def EYIDE(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("IDE popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['jupyter', 'RStudio', 'Pycharm', 'visualStudio', 'spyder', 'matlab', 'vim/emacs']

        normalizers = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_jupyter = [len(d[(d['jupyter'] != -1) & (d['jupyter'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_RStudio = [len(d[(d['RStudio'] != -1) & (d['RStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_Pycharm = [len(d[(d['Pycharm'] != -1) & (d['Pycharm'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_visualStudio = [
            len(d[(d['visualStudio'] != -1) & (d['visualStudio'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_spyder = [len(d[(d['spyder'] != -1) & (d['spyder'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_matlab = [len(d[(d['matlab'] != -1) & (d['matlab'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                    i, ye in enumerate(years)]
        y_vimemacs = [
            len(d[(d['vim/emacs'] != -1) & (d['vim/emacs'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]

        axes[c_i].plot(years, y_jupyter, label = 'jupyter')
        axes[c_i].plot(years, y_RStudio, label='RStudio')
        axes[c_i].plot(years, y_Pycharm, label = 'Pycharm')
        axes[c_i].plot(years, y_visualStudio, label='visualStudio')
        axes[c_i].plot( years, y_spyder, label = 'Java')
        axes[c_i].plot(years, y_matlab, label='spyder')
        axes[c_i].plot( years, y_vimemacs, label = 'vim/emacs')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYIDE.png')

def EYOP(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Online platforms popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedinLearning', 'universityCourses']
        x_to_p = ['coursera', 'udacity', 'udemy', 'kaggleLearn', 'edx', 'linkedin', 'university']

        normalizers = [len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_coursera = [
            len(d[(d['coursera'] != -1) & (d['coursera'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
            i, ye in enumerate(years)]
        y_udacity = [len(d[(d['udacity'] != -1) & (d['udacity'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
                     for i, ye in enumerate(years)]
        y_udemy = [len(d[(d['udemy'] != -1) & (d['udemy'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for
                   i, ye in enumerate(years)]
        y_kaggleLearn = [
            len(d[(d['kaggleLearn'] != -1) & (d['kaggleLearn'].isna() == False) & (d['year'] == ye)]) / normalizers[i]
            for i, ye in enumerate(years)]
        y_edx = [len(d[(d['edx'] != -1) & (d['edx'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i, ye in
                 enumerate(years)]
        y_linkedinLearning = [
            len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]
        y_universityCourses = [
            len(d[(d['universityCourses'] != -1) & (d['universityCourses'].isna() == False) & (d['year'] == ye)]) /
            normalizers[i] for i, ye in enumerate(years)]

        axes[c_i].plot(years, y_coursera, label = 'coursera')
        axes[c_i].plot(years, y_udacity, label='udacity')
        axes[c_i].plot(years, y_udemy, label = 'udemy')
        axes[c_i].plot(years, y_kaggleLearn, label='kaggleLearn')
        axes[c_i].plot( years, y_edx, label = 'edx')
        axes[c_i].plot(years, y_linkedinLearning, label='linkedinLearning')
        axes[c_i].plot( years, y_universityCourses, label = 'universityCourses')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYOP.png')

def EYVP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Visualization libraries popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['matplotlib', 'seaborn', 'plotly', 'altair', 'shiny', 'geoplotlib']


        normalizers = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)])
                       for ye in years]


        y_matplotlib = [len(d[(d['matplotlib'] != -1) & (d['matplotlib'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['seaborn'] != -1) & (d['seaborn'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['plotly'] != -1) & (d['plotly'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_altair = [len(d[(d['altair'] != -1) & (d['altair'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['shiny'] != -1) & (d['shiny'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['linkedinLearning'] != -1) & (d['linkedinLearning'].isna() == False) & (d['year'] == ye)]) / normalizers[i] for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'matplotlib')
        axes[c_i].plot(years, y_seaborn, label='seaborn')
        axes[c_i].plot(years, y_plotly, label = 'plotly')
        axes[c_i].plot(years, y_altair, label='altair')
        axes[c_i].plot( years, y_shiny, label = 'shiny')
        axes[c_i].plot(years, y_geoplotlib, label='geoplotlib')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYVP.png')

def EYML(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("Machine learning algorithms popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['linear', 'trees', 'GBM', 'bayesian', 'evolutionary', 'dnn', 'cnn', 'gan', 'rnn', 'transformer']

        normalizers = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_python = [len(d[(d['linear'] != -1) & (d['linear'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_r = [len(d[(d['trees'] != -1) & (d['trees'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_sql = [len(d[(d['GBM'] != -1) & (d['GBM'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_c = [len(d[(d['bayesian'] != -1) & (d['bayesian'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_java = [
            len(d[(d['evolutionary'] != -1) & (d['evolutionary'].isna() == False) & (d['year'] == ye)]) /max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_javascript = [len(d[(d['dnn'] != -1) & (d['dnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_julia = [len(d[(d['cnn'] != -1) & (d['cnn'].isna() == False) & (d['year'] == ye)]) /max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_matlabcode = [len(d[(d['gan'] != -1) & (d['gan'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_rnn = [len(d[(d['rnn'] != -1) & (d['rnn'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_trans = [
            len(d[(d['transformer'] != -1) & (d['transformer'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_python, label = 'linear')
        axes[c_i].plot(years, y_r, label='trees')
        axes[c_i].plot(years, y_sql, label = 'GBM')
        axes[c_i].plot(years, y_c, label='bayesian')
        axes[c_i].plot( years, y_java, label = 'evolutionary')
        axes[c_i].plot(years, y_javascript, label='dnn')
        axes[c_i].plot( years, y_julia, label = 'cnn')
        axes[c_i].plot(years, y_matlabcode, label='gan')
        axes[c_i].plot( years,  y_rnn, label = 'rnn')
        axes[c_i].plot(years, y_trans, label='transformer')
        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYML.png')

def EYCV(data):

    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("CV algorithms popularity")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['generalVideoTools', 'imageSegmentation', 'objectDetection', 'imageClassification', 'visionTransformers', 'generativeNetworks']


        normalizers = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [len(d[(d['generalVideoTools'] != -1) & (d['generalVideoTools'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['imageSegmentation'] != -1) & (d['imageSegmentation'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_plotly = [len(d[(d['objectDetection'] != -1) & (d['objectDetection'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [len(d[(d['imageClassification'] != -1) & (d['imageClassification'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_shiny = [len(d[(d['visionTransformers'] != -1) & (d['visionTransformers'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_geoplotlib = [len(d[(d['generativeNetworks'] != -1) & (d['generativeNetworks'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]


        axes[c_i].plot(years, y_matplotlib, label = 'generalVideoTools')
        axes[c_i].plot(years, y_seaborn, label='imageSegmentation')
        axes[c_i].plot(years, y_plotly, label = 'objectDetection')
        axes[c_i].plot(years, y_altair, label='imageClassification')
        axes[c_i].plot( years, y_shiny, label = 'visionTransformers')
        axes[c_i].plot(years, y_geoplotlib, label='generativeNetworks')


        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYCV.png')

def EYNLP(data):
    fig, axes = plt.subplots(1, 2, figsize = (15,10))
    fig.suptitle("NLP algorithms popularity ")

    y = []
    c_i = 0
    c_j = 0
    for i in data['formal_education'].unique():

        d = data[data['formal_education'] == i]
        years = [2018, 2019, 2020, 2021, 2022]
        x = ['wordEmbeding', 'encoderDecoder', 'contextualizedEmbedding', 'transformerLanguage']
        normalizers = [len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) +
                       len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                                   d['year'] == ye)]) +
                       len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (
                                   d['year'] == ye)])
                       for ye in years]

        y_matplotlib = [
            len(d[(d['wordEmbeding'] != -1) & (d['wordEmbeding'].isna() == False) & (d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_seaborn = [len(d[(d['encoderDecoder'] != -1) & (d['encoderDecoder'].isna() == False) & (d['year'] == ye)]) /
                     max(1, normalizers[i]) for i, ye in enumerate(years)]
        y_plotly = [len(d[(d['contextualizedEmbedding'] != -1) & (d['contextualizedEmbedding'].isna() == False) & (
                    d['year'] == ye)]) / max(1,normalizers[i]) for i,ye in enumerate(years)]
        y_altair = [
            len(d[(d['transformerLanguage'] != -1) & (d['transformerLanguage'].isna() == False) & (d['year'] == ye)]) /
            max(1,normalizers[i]) for i,ye in enumerate(years)]

        axes[c_i].plot(years, y_matplotlib, label = 'wordEmbeding')
        axes[c_i].plot(years, y_seaborn, label='encoderDecoder')
        axes[c_i].plot(years, y_plotly, label = 'contextualizedEmbedding')
        axes[c_i].plot(years, y_altair, label='transformerLanguage')

        axes[c_i].legend()
        axes[c_i].set_title(str(i))

        c_i += 1
        if( c_i % 5 == 0):
            c_i = 0
            c_j += 1

    plt.savefig('EYNLP.png')

def durationGenderHist(data):

    data = data[data['duration'].astype(int) < 10000]
    plt.hist(data[data['gender'] == 'Male']['duration'].astype(int), alpha = 0.5, label = 'Male')
    plt.hist(data[data['gender'] == 'Female']['duration'].astype(int), alpha=0.5, label='Female')
    plt.legend(loc = 'upper right')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = pd.read_csv('dataframe1.csv')
    data_gen = pd.read_csv('dataframe1.csv')
    data_title = pd.read_csv('dataframe1.csv')
    data_education = pd.read_csv('dataframe1.csv')

    data_gen['gender'] = data_gen['gender'].replace({'Man':'Male', 'Woman':'Female'})
    data_gen = data_gen[(data_gen['gender'] == 'Male') | (data_gen['gender'] == 'Female')]

    data_education = data_education[(data_education['formal_education'] == data_education['formal_education'].unique()[3]) | (data_education['formal_education'] == data_education['formal_education'].unique()[2])]

    data_title['job_title'] = data_title['job_title'].replace({data['job_title'].unique()[28]: 'Data Analyst'})
    data_title = data_title[(data_title['job_title'] == 'Data Scientist') | (data_title['job_title'] == 'Data Analyst') | (data_title['job_title'] == data['job_title'].unique()[28])]

    data = data.groupby('country').filter(lambda x: len(x) > 10000)
    countries = {i: len(data[data['country'] == i]) for i in data['country'].unique()}
    countries = dict(sorted(countries.items(), key=lambda item: item[1]))

    PL(data)
    IDE(data)
    OP(data)
    VP(data)
    ML(data)
    CV(data)
    NLP(data)
    YPL(data)
    YIDE(data)
    YOP(data)
    YVP(data)
    YML(data)
    YCV(data)
    YNLP(data)

    MFPL(data_gen)
    MFIDE(data_gen)
    MFOP(data_gen)
    MFVP(data_gen)
    MFML(data_gen)
    MFCV(data_gen)
    MFNLP(data_gen)
    MFYPL(data_gen)
    MFYIDE(data_gen)
    MFYOP(data_gen)
    MFYVP(data_gen)
    MFYML(data_gen)
    MFYCV(data_gen)
    MFYNLP(data_gen)

    TPL(data_title)
    TIDE(data_title)
    TOP(data_title)
    TVP(data_title)
    TML(data_title)
    TCV(data_title)
    TNLP(data_title)
    TYPL(data_title)
    TYIDE(data_title)
    TYOP(data_title)
    TYVP(data_title)
    TYML(data_title)
    TYCV(data_title)
    TYNLP(data_title)

    EPL(data_education)
    EIDE(data_education)
    EOP(data_education)
    EVP(data_education)
    EML(data_education)
    ECV(data_education)
    ENLP(data_education)
    EYPL(data_education)
    EYIDE(data_education)
    EYOP(data_education)
    EYVP(data_education)
    EYML(data_education)
    EYCV(data_education)
    EYNLP(data_education)



    #durationGenderHist(data_gen)


    # countries = {i : len(data[data['country'] == i]) for i in data['country'].unique()}
    # countries = dict(sorted(countries.items(), key = lambda item : item[1]))
