from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np
from models import *

def plotAUC(truth, pred, lab):
    fpr, tpr, thresholds = roc_curve(truth, pred)
    roc_auc = auc(fpr, tpr)
    c = (np.random.rand(), np.random.rand(), np.random.rand())
    plt.plot(fpr, tpr, color=c, label= lab+' (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC')
    plt.legend(loc="lower right")

def plotModels():
    plotAUC(Y_test, logRegression(), 'LR' )
    plotAUC(Y_test, randomForest(), 'RF')

if __name__ == '__main__':
    plotModels()