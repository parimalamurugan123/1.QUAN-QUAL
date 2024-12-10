class Univariate():

    def quanQual(dataset):
        quan = []
        qual = []
        for ColumnName in dataset.columns:
            #print(ColumnName)
            if (dataset[ColumnName].dtype == 'O'):
                    #print ("QUAL")
                    qual.append(ColumnName)
            else:
                    #print("QUAN")
                    quan.append(ColumnName)
        return quan,qual