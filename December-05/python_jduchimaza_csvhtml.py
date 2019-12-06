# csv2html 
# Brief: Function to convert a CSV file to HTML table
# Author: Juan D.H.
# Date:   5 Dec 2019
# 
# This function was written as part of 'A December of Algorithms'
#----------------------------------------------------------------

import csv

def csv2html(csvfile):
   with open(csvfile,'r') as csvf:
      csvr = csv.reader(csvf,skipinitialspace=True)
      html = open('html_res.html','w+')
      html.write('<html>\n\t<body>\n\t\t<table>\n') #Write the html tags needed
      header = True
      for row in csvr:
         html.write('\t\t\t<tr>') #Write tags for table row
         for col in row:
            if header: 
               html.write('<th>'+str(col)+'</th>') # Add a cell to the row
            else:
               html.write('<td>'+str(col)+'</td>')
         header = False
         html.write('</tr>\n') #Write tags to close table row
      html.write('\t\t</table>\n\t</body>\n</html>') #Write the closing tags
      html.close()
      csvf.close()
   return 

#Testcase
filename = 'csv_to_html_res.csv'
csv2html(filename)
