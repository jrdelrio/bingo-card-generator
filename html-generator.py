import os
import csv
from jinja2 import Template
import glob

directory = '/Users/macbookderai/Desktop/Programación/Python/Programas/bingo fran/'
file_list = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
file_list = glob.glob("*.csv")
file_list.remove('palabras.csv')

for csv_file in file_list:
    # Read the CSV file and extract the values
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # next(reader) no header row
        values = [row[0] for row in reader]

        # Generate the HTML file using a Jinja2 template
        template_str = """
        <html>
            <head>
                <style>
                .wrapper {
                    border: solid 20px #8faea4;
                    max-width: 1000px;
                }
                .picture {
                    max-width: 7cm;
                    margin: auto;
                }
                #leaves-picture {
                    rotate: -90deg;
                    display: block;
                    position: relative;
                    margin-top: -235px;
                    margin-bottom: -280px;
                }
                .title {
                    text-align: center;
                    font-size: 120px;
                    color: #1f5458;
                    margin-bottom: 30px;
                }
                .title > p {
                    display: inline;
                }
                .baby {
                    font-family: 'Barlow', sans-serif;
                }
                .bingo {
                    padding-left: 20px;
                    font-family: 'Sacramento', cursive;
                }
                .table {
                    text-align: center;
                    margin-bottom: 40px;
                }
                .row {
                    display: inline-block;
                    margin-right: 10px;
                }

                .col {
                    height: 150px;
                    width: 150px;
                    background-color:rgb(181, 221, 172, 0.5) ;
                    text-align: center;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-bottom: 10px;
                    color: #1f5458;
                    font-family: 'Lora', serif;
                    font-size: 22px;
                }

                #lyon {
                    max-height: 80%;
                }
	            </style>
	            <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500&family=Lora&family=Sacramento&display=swap" rel="stylesheet">
            </head>
            <body>
                <div class='wrapper'>
                    <div class='picture'>
                        <img id='leaves-picture' src="hojas.webp">
                    </div>
                    <div class='title'>
                        <p class='baby'>BABY</p><p class='bingo'>bingo</p>
                    </div>
                    <div class='table'>
                        <div class='row'>
                            <div class='col'>{{ values[0] }}</div>
                            <div class='col'>{{ values[1] }}</div>
                            <div class='col'>{{ values[2] }}</div>
                            <div class='col'>{{ values[3] }}</div>
                            <div class='col'>{{ values[4] }}</div>
                        </div>
                        <div class='row'>
                            <div class='col'>{{ values[5] }}</div>
                            <div class='col'>{{ values[6] }}</div>
                            <div class='col'>{{ values[7] }}</div>
                            <div class='col'>{{ values[8] }}</div>
                            <div class='col'>{{ values[9] }}</div>
                        </div>
                        <div class='row'>
                            <div class='col'>{{ values[10] }}</div>
                            <div class='col'>{{ values[11] }}</div>
                            <div class='col'><img id='lyon' src='leoncito.png'/></div>
                            <div class='col'>{{ values[12] }}</div>
                            <div class='col'>{{ values[13] }}</div>
                        </div>
                        <div class='row'>
                            <div class='col'>{{ values[14] }}</div>
                            <div class='col'>{{ values[15] }}</div>
                            <div class='col'>{{ values[16] }}</div>
                            <div class='col'>{{ values[17] }}</div>
                            <div class='col'>{{ values[18] }}</div>
                        </div>
                        <div class='row'>
                            <div class='col'>{{ values[19] }}</div>
                            <div class='col'>{{ values[20] }}</div>
                            <div class='col'>{{ values[21] }}</div>
                            <div class='col'>{{ values[22] }}</div>
                            <div class='col'>{{ values[23] }}</div>
                        </div>
                    </div>
                </div>
            </body>
        <body>
        """
        template = Template(template_str)
        html = template.render(values=values)

        # Write the HTML file to disk
        with open('{}.html'.format(csv_file[:-3]), 'w') as new_html_file:
            new_html_file.write(html)
