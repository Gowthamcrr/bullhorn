# usr/bin/env python
import os
from xmlutils.xml2csv import xml2csv
import csv

for file in os.listdir("input"):
        if file.endswith(".xml"):
                input_url=os.path.join("input", file)
                output_url=os.path.join("output", file).replace(".xml", ".csv")
                output_temp_url="output/temp.csv"
                #print(os.path.join("input", file))
                #print output_url
                converter = xml2csv(input_url, output_temp_url, encoding="utf-8")
                converter.convert(tag="Skill")
                with open(output_temp_url,'r') as csvinput:
                        with open(output_url,'w') as csvoutput:
                                writer = csv.writer(csvoutput)
                                for row in csv.reader(csvinput):
                                        writer.writerow(row+[file.split(".")[0]])
                os.system("rm -rf output/temp.csv")
                final_out=open("output/out.csv","a")
                f = open(output_url)
                f.next()
                for line in f:
                        final_out.write(line)
                f.close()
                final_out.close()
