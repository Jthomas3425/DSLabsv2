class QuickFuncs:
    
    def get_correlations(data, corr_percent):
        corr_matrix = data.corr() > corr_percent 
        corr_values = []
        for feature in corr_matrix:
            corr_values.append({feature : corr_matrix.columns[corr_matrix[feature] == True]})
        return corr_values
    
    def minmax_scale(data):
        scaled_data = []
        for val in data:
            scaled_data.append((val - data.min())/(data.max() - data.min()))
        return scaled_data
    
    def mean_scale(data):
        scaled_data = []
        for val in data:
            scaled_data.append((val - data.mean())/(data.max() - data.min()))
        return scaled_data