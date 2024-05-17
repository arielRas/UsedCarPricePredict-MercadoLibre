import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, classification_report

class Metrics():
    def __init__(self) -> None:
        pass

    def plot_matrix_confusion(self, y_true, y_pred):
        matrix = confusion_matrix(y_true, y_pred)
        sns.heatmap(matrix, fmt='.0f', annot=True, cmap='inferno')
        plt.title('Matriz de confusion')
        plt.xlabel('Predict data')        
        plt.ylabel('True data')
        #plt.xticks(ticks=[0.5,1.5], labels=[label_0, label_1])
        #plt.yticks(ticks=[0.5,1.5], labels=[label_0, label_1])
        plt.show()

    def plot_roc_curve(y_true , y_prob):
        mpl.style.use('ggplot')
        false_positive_rate, true_positive_rate, _threshold = roc_curve(y_true, y_prob)
        sns.lineplot(x=false_positive_rate, y=true_positive_rate)
        plt.plot([0, 1], ls="--")
        plt.title('Curva ROC')
        plt.xlabel('False positive rate')
        plt.ylabel('True positive rate')
        plt.tight_layout()
        plt.show()
        mpl.style.use('default')

    def get_metrics(self, model:str, y_true, y_pred, y_prob)->dict:
        report = classification_report(y_true, y_pred, output_dict=True)
        precision_0 = report.get('0', {}).get('precision', None)
        precision_1 = report.get('1', {}).get('precision', None)
        recall_0 = report.get('0', {}).get('recall', None)
        recall_1 = report.get('1', {}).get('recall', None)
        f1_0 = report.get('0', {}).get('f1-score', None)
        f1_1 = report.get('1', {}).get('f1-score', None)
        accuracy = report.get('accuracy', None)
        roc_score = roc_auc_score(y_true, y_prob)
        keys = ['model','accuracy','roc_score','precision_0','precision_1','recall_0','recall_1','f1_score_0','f1_score_1']
        values =  [model, accuracy, roc_score, precision_0, precision_1, recall_0, recall_1, f1_0, f1_1]
        metrics = {}
        for key, value in zip(keys, values):
            if key == 'model':
                metrics[key] = value
            else:
                metrics[key] = round(float(value),4)
        return metrics


class Correlations():
    def __init__(self, df:pd.DataFrame, target_var:str, vars:list, vars_type:str):
        self.df = df
        self.target_var = target_var
        self.vars = vars
        self.vars_type = vars_type

    #CREA UN DATAFRAME VACIO PARA ALOJAR LAS CORRELACIONES
    def _get_correlation_dataframe(self) -> pd.DataFrame:
        df_corr = pd.DataFrame(index=self.vars, columns=['correlation'])
        return df_corr    

    #DEVUELVE EL NUMERO MULTIPLO DE 10 SUPERIOR INMEDIATO AL VALOR MAXIMO DE LA SERIE
    def _get_limit_value(self, values:pd.Series) -> float:
        limit_value = values.abs().max()
        limit_value = np.ceil(limit_value*10)/10
        return limit_value

    #FUNCION PARA PLOTEAR CORRELACION DE PUNTO BISERIAL
    def plot_biserial_point(self):
        df_corr = self._get_correlation_dataframe()
        corr_list = [stats.pointbiserialr(self.df[self.target_var], self.df[var]) for var in self.vars]
        for var, corr in zip(self.vars, corr_list):
            df_corr.loc[var, 'correlation'] = corr.statistic
        self._plot_correlation(df_corr)    

    #FUNCION PARA PLOTEAR COEFICIENTE DE CONTINGENCIA
    def plot_contingency_coef(self):
        n = self.df.shape[0]
        df_corr = self._get_correlation_dataframe()
        for var in self.vars:
            contingency_table = pd.crosstab(self.df[var], self.df[self.target_var])
            chi_2 = stats.chi2_contingency(contingency_table)
            df_corr.loc[var, 'correlation'] = math.sqrt(chi_2.statistic/(n + chi_2.statistic))            
        self._plot_correlation(df_corr)

    #FUNCION PARA PLOTEAR EL GRAFICO DE BARRAS
    def _plot_correlation(self, df_corr:pd.DataFrame):
        colors = ['#000E9E' if corr < 0 else '#3DB2DA' for corr in df_corr.correlation]
        limit_value = self._get_limit_value(df_corr.correlation)
        plt.style.use("bmh")
        plt.figure(figsize=(8,5))  
        sns.barplot(x=df_corr.correlation, y=df_corr.index, hue=df_corr.index, palette=colors)
        plt.title(f'Correlacion de variable objetivo con variables {self.vars_type}', fontsize=14)
        plt.xlabel('Coeficiente de correlacion')
        plt.ylabel(f'Variables {self.vars_type}')
        plt.xlim(-1*limit_value, limit_value)
        plt.axvline(x=0, color='black', linestyle='-')
        plt.tight_layout()
        plt.show()
        plt.style.use("default")


class DescrStat:
    def __init__(self) -> None:
        pass

    def get_var_data(data:pd.Series):
        data_stats = {
            'median' : data.median(),
            'mean' : data.mean().round(4),
            'mode' : stats.mode(data, keepdims=False)[0],
            'std' : data.std().round(4),
            'variance' : data.var().round(4),
            'skew' : data.skew().round(4),
            'kurtosys' : data.kurtosis().round(4)
        }
        return pd.Series(data_stats)
    

    def get_outliers_info(data:pd.Series):
        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        irq = q3-q1
        data_stats = {
            'irq' : q3-q1,
            'max_non_outlier' : q3+(irq*1.5),
            'min_non_outlier' : q1-(irq*1.5)
        }
        return pd.Series(data_stats)