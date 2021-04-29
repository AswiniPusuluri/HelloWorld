import pandas as pd


data=pd.read_csv("BL-Flickr-Images-Book-truncated50.csv")
choose = ['London', 'LONDON']
result = data[data['Place of Publication'].isin(choose)]
finalresult=result.drop(['Identifier','Edition Statement','Contributors','Corporate Author',
                'Corporate Contributors','Former owner','Engraver','Issuance type',
             'Flickr URL','Shelfmarks'], axis=1)
finalresult.to_csv('BL-Flickr-Images-Book-truncated50_Output.csv')